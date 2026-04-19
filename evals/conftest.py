"""Pytest fixtures, hooks, and shared test helpers for evals."""

import json
import os
import re
import time
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from backend.config import ConfigError, config
from benchmark_reporting import build_structured_results, write_reports


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


# ── Benchmark data helpers ─────────────────────────────────────

def load_all_benchmark_samples() -> list[tuple[str, dict]]:
    """Discover all benchmark_*.json files and flatten into (dataset_name, sample) pairs."""
    samples = []
    for path in sorted(FIXTURES_DIR.glob("benchmark_*.json")):
        data = json.loads(path.read_text())
        name = data["metadata"]["name"]
        for sample in data["samples"]:
            samples.append((name, sample))
    return samples


_benchmark_result_data: dict[str, dict] = {}
_benchmark_session_active = False


def store_benchmark_result(arm: str, key: str, data: dict) -> None:
    """Called by tests to store full result data (verdict, score, confidence) before asserting."""
    _benchmark_result_data[f"{arm}:{key}"] = data


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

    # ``request_failed``: call raised before ``store_benchmark_result`` (not skipped / setup failure).
    outcome = getattr(report, "outcome", None)
    request_failed = (
        outcome == "failed"
        and f"{arm}:{param_key}" not in _benchmark_result_data
    )

    _benchmark_pass_fail[arm].append({
        "key": param_key,
        "passed": report.passed,
        "request_failed": request_failed,
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
