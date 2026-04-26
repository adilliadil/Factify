"""Pytest fixtures, hooks, and shared test helpers for evals."""

import json
import logging
import os
import re
import time
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from backend.config import ConfigError, config
import backend.llm as llm
from benchmark_reporting import build_structured_results, write_reports


logger = logging.getLogger(__name__)


def collect_eval_config_errors(*, need_judge: bool) -> list[str]:
    """Try loading config slices needed for live/benchmark evals; return ConfigError messages.

    Call after ``config.reset()`` so env reflects the current test process. Used by the
    autouse fixture and unit-tested in ``test_config_helpers.py``.
    """
    errors: list[str] = []
    try:
        _ = config.llm
    except ConfigError as exc:
        errors.append(str(exc))
    try:
        _ = config.search
    except ConfigError as exc:
        errors.append(str(exc))
    if need_judge:
        try:
            _ = config.judge
        except ConfigError as exc:
            errors.append(str(exc))
    return errors

FIXTURES_DIR = Path(__file__).parent / "datasets"
DEFAULT_BENCHMARK_SAMPLES_PER_DATASET = 30


# ── Benchmark data helpers ─────────────────────────────────────

def _benchmark_samples_per_dataset() -> int:
    """Default benchmark sample cap per dataset, overridable via env var."""
    raw = os.getenv("BENCHMARK_SAMPLES_PER_DATASET")
    if raw is None:
        return DEFAULT_BENCHMARK_SAMPLES_PER_DATASET
    try:
        value = int(raw)
    except ValueError:
        return DEFAULT_BENCHMARK_SAMPLES_PER_DATASET
    return value if value > 0 else DEFAULT_BENCHMARK_SAMPLES_PER_DATASET


def load_all_benchmark_samples() -> list[tuple[str, dict]]:
    """Discover benchmark_*.json files and flatten into (dataset_name, sample) pairs."""
    samples = []
    sample_cap = _benchmark_samples_per_dataset()
    for path in sorted(FIXTURES_DIR.glob("benchmark_*.json")):
        data = json.loads(path.read_text())
        name = data["metadata"]["name"]
        for sample in data["samples"][:sample_cap]:
            samples.append((name, sample))
    return samples


_benchmark_result_data: dict[str, dict] = {}
_benchmark_session_active = False


def store_benchmark_result(arm: str, key: str, data: dict) -> None:
    """Called by tests to store full result data (verdict, score, confidence) before asserting."""
    _benchmark_result_data[f"{arm}:{key}"] = data


BASELINE_FACT_CHECK_PROMPT = """You are a fact-checking assistant.

Fact-check the claim below as directly as possible. Use whatever knowledge or
native model capabilities are available. Do not assume any evidence has been
provided separately. If you cannot assess the claim, use verdict "unverifiable"
with score 50.

Claim:
{claim}

Return a JSON object with exactly these fields:
{{
  "score": <integer 0-100>,
  "verdict": "<one of: false, mostly_false, mixed, mostly_true, true, unverifiable>",
  "tldr": "<single punchy sentence, max 15 words, stating the core conclusion>",
  "explanation": "<2-3 sentence explanation based on general knowledge>",
  "confidence": "<one of: high, medium, low>",
  "confidence_reason": "<short phrase explaining why, max 12 words>"
}}"""

BASELINE_FACT_CHECK_RESPONSE_FORMAT = {
    "type": "json_schema",
    "json_schema": {
        "name": "bare_llm_fact_check",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "score": {"type": "integer", "minimum": 0, "maximum": 100},
                "verdict": {
                    "type": "string",
                    "enum": ["false", "mostly_false", "mixed", "mostly_true", "true", "unverifiable"],
                },
                "tldr": {"type": "string"},
                "explanation": {"type": "string"},
                "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                "confidence_reason": {"type": "string"},
            },
            "required": [
                "score",
                "verdict",
                "tldr",
                "explanation",
                "confidence",
                "confidence_reason",
            ],
        },
    },
}


def _claim_verdict_from_overall(verdict: str) -> str:
    if verdict in {"true", "mostly_true"}:
        return "supported"
    if verdict in {"false", "mostly_false"}:
        return "contradicted"
    if verdict == "mixed":
        return "mixed"
    return "unverifiable"


def _fallback_baseline_analysis() -> llm.AnalysisResult:
    return {
        "score": 50,
        "verdict": "unverifiable",
        "tldr": "",
        "explanation": "Unable to determine.",
        "confidence": "low",
        "confidence_reason": "Model returned invalid or empty JSON",
        "claim_verdicts": [],
        "source_stances": {},
    }


async def analyze_claim_baseline(claim: str) -> llm.AnalysisResult:
    """Eval-only bare LLM baseline for benchmark Arm 0."""
    logger.debug("analyze_claim_baseline: input length=%d model=%s", len(claim), config.llm.model)
    resp = await llm.get_client().chat.completions.create(
        model=config.llm.model,
        messages=[
            {"role": "system", "content": "You are a fact-checking assistant. Always respond with valid JSON."},
            {"role": "user", "content": BASELINE_FACT_CHECK_PROMPT.format(claim=claim)},
        ],
        response_format=BASELINE_FACT_CHECK_RESPONSE_FORMAT,
        temperature=0,
    )

    raw = resp.choices[0].message.content
    if raw is None:
        logger.warning("analyze_claim_baseline: empty message content from LLM")
        return _fallback_baseline_analysis()

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        logger.warning("analyze_claim_baseline: invalid JSON (first 200 chars): %r", raw[:200])
        return _fallback_baseline_analysis()

    if not isinstance(result, dict):
        logger.warning("analyze_claim_baseline: expected JSON object, got %s", type(result).__name__)
        return _fallback_baseline_analysis()

    try:
        score = max(0, min(100, int(result.get("score", 50))))
    except (TypeError, ValueError):
        logger.warning("analyze_claim_baseline: non-numeric score %r, defaulting to 50", result.get("score"))
        score = 50

    verdict = result.get("verdict", "unverifiable")
    valid_verdicts = {"false", "mostly_false", "mixed", "mostly_true", "true", "unverifiable"}
    if verdict not in valid_verdicts:
        logger.warning("analyze_claim_baseline: invalid verdict %r, defaulting to unverifiable", verdict)
        verdict = "unverifiable"

    confidence = result.get("confidence", "low")
    if confidence not in {"high", "medium", "low"}:
        confidence = "low"

    logger.info(
        "analyze_claim_baseline: verdict=%s score=%d confidence=%s",
        verdict,
        score,
        confidence,
    )

    return {
        "score": score,
        "verdict": verdict,
        "tldr": result.get("tldr", ""),
        "explanation": result.get("explanation", "Unable to determine."),
        "confidence": confidence,
        "confidence_reason": result.get("confidence_reason", ""),
        "claim_verdicts": [{"claim": claim, "verdict": _claim_verdict_from_overall(verdict)}],
        "source_stances": {},
    }


# ── Pytest hooks ───────────────────────────────────────────────

_benchmark_pass_fail: dict[str, list[dict]] = {
    "arm_baseline": [], "arm_a": [], "arm_b": [], "arm_c": [],
}


def pytest_collection_modifyitems(items):
    global _benchmark_session_active
    for item in items:
        if item.get_closest_marker("benchmark"):
            _benchmark_session_active = True
            return


def pytest_runtest_logreport(report):
    if not _benchmark_session_active or report.when != "call":
        return

    node_id = report.nodeid
    if "test_benchmark.py" not in node_id:
        return

    param_match = re.search(r'\[(.+)\]$', node_id)
    if not param_match:
        return
    param_key = param_match.group(1)

    if "TestBaselineAnalysis" in node_id:
        arm = "arm_baseline"
    elif "TestGoldEvidenceAnalysis" in node_id:
        arm = "arm_a"
    elif "TestSearchedEvidenceAnalysis" in node_id:
        arm = "arm_b"
    elif "TestFullPipeline" in node_id:
        arm = "arm_c"
    else:
        return

    _benchmark_pass_fail[arm].append({
        "key": param_key,
        "passed": report.passed,
    })


def pytest_sessionfinish(session, exitstatus):
    if not _benchmark_session_active:
        return

    total_results = sum(len(v) for v in _benchmark_pass_fail.values())
    if total_results == 0:
        return

    sample_lookup = {}
    for ds_name, sample in load_all_benchmark_samples():
        key = f"{ds_name}-{sample['id']}"
        sample_lookup[key] = {"dataset": ds_name, **sample}

    arm_baseline, arm_a, arm_b, arm_c = build_structured_results(
        _benchmark_pass_fail, _benchmark_result_data, sample_lookup,
    )
    write_reports(arm_baseline, arm_a, arm_b, arm_c)


# ── Fixtures ───────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def reset_clients_and_delay(request, monkeypatch):
    """Reset API clients and config cache to ensure clean state per test."""
    import backend.search
    import backend.llm
    import judges

    marker_names = [m.name for m in request.node.iter_markers()]
    needs_real_keys = any(n in ("benchmark", "live_api") for n in marker_names)
    need_judge = "live_api" in marker_names

    backend.search.client = None
    backend.llm.client = None
    judges._judge_client = None
    config.reset()

    # Mocked unit tests still read config; inject placeholders only when not calling live APIs.
    if needs_real_keys:
        missing = collect_eval_config_errors(need_judge=need_judge)
        config.reset()
        if missing:
            pytest.skip(
                f"Live/benchmark tests require configured providers ({'; '.join(missing)})"
            )
    else:
        if not os.getenv("OPENAI_API_KEY"):
            monkeypatch.setenv("OPENAI_API_KEY", "__test_openai_key__")
        if not os.getenv("NEBIUS_API_KEY"):
            monkeypatch.setenv("NEBIUS_API_KEY", "__test_nebius_key__")
        if not os.getenv("TAVILY_API_KEY"):
            monkeypatch.setenv("TAVILY_API_KEY", "__test_tavily_key__")

    backend.search.client = None
    backend.llm.client = None
    judges._judge_client = None
    config.reset()

    time.sleep(0.3)
    yield
    time.sleep(0.3)


@pytest.fixture
def mock_llm_client():
    """Mock the LLM async client."""
    with patch("backend.llm.get_client") as mock_get:
        mock_client = MagicMock()
        mock_get.return_value = mock_client
        yield mock_client


@pytest.fixture
def mock_tavily_client():
    """Mock the Tavily async client."""
    with patch("backend.search.get_client") as mock_get:
        mock_client = MagicMock()
        mock_get.return_value = mock_client
        yield mock_client


# ── Mock / fixture helpers ─────────────────────────────────────

def make_llm_response(content: dict | list) -> MagicMock:
    """Create a mock LLM chat completion response."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = json.dumps(content)
    return mock_response


def load_search_fixture(name: str) -> dict:
    """Load a pre-recorded Tavily search response."""
    fixture_path = FIXTURES_DIR / "search_fixtures" / f"{name}.json"
    with open(fixture_path) as f:
        return json.load(f)


def load_dataset(name: str) -> list[dict]:
    """Load a test dataset (claims.json, analysis.json, etc.)."""
    dataset_path = FIXTURES_DIR / f"{name}.json"
    with open(dataset_path) as f:
        return json.load(f)
