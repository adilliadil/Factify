"""Generate a human-readable benchmark failure audit.

Reads `evals/reports/benchmark_results.json` and enriches failed rows with
dataset gold evidence or cached Tavily search inputs where available.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from textwrap import shorten


ROOT = Path(__file__).resolve().parents[2]
EVALS_DIR = ROOT / "evals"
DATASETS_DIR = EVALS_DIR / "datasets"
REPORTS_DIR = EVALS_DIR / "reports"
DEFAULT_RESULTS = REPORTS_DIR / "benchmark_results.json"
DEFAULT_OUTPUT = REPORTS_DIR / "benchmark_failure_audit.md"

ARM_LABELS = {
    "arm_a": "Arm A - Gold Evidence",
    "arm_b": "Arm B - Searched Evidence",
    "arm_c": "Arm C - Full Pipeline",
    "arm_baseline": "Arm 0 - Bare LLM",
}
MISSING = object()


def _normalize_claim(claim: str) -> str:
    text = claim.strip().lower()
    text = text.replace("’", "'").replace("`", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def _load_samples() -> dict[tuple[str, str], dict]:
    samples: dict[tuple[str, str], dict] = {}
    for path in sorted(DATASETS_DIR.glob("benchmark_*.json")):
        data = _load_json(path)
        dataset = data["metadata"]["name"]
        for sample in data["samples"]:
            samples[(dataset, sample["id"])] = sample
    return samples


def _load_cache() -> dict[str, list[dict]]:
    cache_path = DATASETS_DIR / "tavily_search_cache.json"
    if not cache_path.exists():
        return {}

    by_claim: dict[str, list[dict]] = {}
    for entry in _load_json(cache_path).values():
        if not isinstance(entry, dict):
            continue
        claim = entry.get("normalized_claim") or _normalize_claim(entry.get("claim", ""))
        results = entry.get("results", [])
        if claim and isinstance(results, list):
            by_claim[claim] = results
    return by_claim


def _failure_reasons(row: dict) -> list[str]:
    reasons: list[str] = []
    expected = row.get("expected_verdicts") or []
    actual = row.get("actual_verdict", "?")
    if actual not in expected:
        reasons.append(f"verdict got `{actual}`, expected one of `{', '.join(expected)}`")

    return reasons or ["benchmark assertion failed"]


def _source_label(arm: str) -> str:
    if arm == "arm_baseline":
        return "Baseline Prompt"
    if arm == "arm_a":
        return "Gold Evidence Input"
    if arm == "arm_b":
        return "Search Evidence Input"
    if arm == "arm_c":
        return "Pipeline Sources Output"
    return "Evidence Input"


def _sources_for_row(
    arm: str,
    row: dict,
    sample_lookup: dict[tuple[str, str], dict],
    cache_lookup: dict[str, list[dict]],
) -> list[dict]:
    if row.get("sources"):
        return row["sources"]

    sample = sample_lookup.get((row.get("dataset", ""), row.get("id", "")), {})
    if arm == "arm_a":
        return sample.get("gold_evidence", [])
    if arm in {"arm_b", "arm_c"}:
        return cache_lookup.get(_normalize_claim(row.get("claim", "")), [])
    return []


def _format_source(source: dict, idx: int) -> list[str]:
    title = source.get("title") or "Untitled"
    url = source.get("url") or ""
    stance = source.get("stance")
    content = source.get("content") or ""

    lines = [f"{idx}. **{title}**"]
    if url:
        lines.append(f"   URL: {url}")
    if stance:
        lines.append(f"   Stance: `{stance}`")
    if content:
        lines.append(f"   Content: {shorten(content.replace(chr(10), ' '), width=700, placeholder=' [...]')}")
    return lines


def _row_value(row: dict, key: str) -> object:
    return row[key] if key in row else MISSING


def _claim_verdicts_for_row(row: dict) -> object:
    if "claim_verdicts" in row:
        return row["claim_verdicts"]
    if "claims" in row:
        return row["claims"]
    return MISSING


def _source_stances_for_row(row: dict, sources: list[dict]) -> object:
    if "source_stances" in row:
        return row["source_stances"]

    stances = {
        source["url"]: source["stance"]
        for source in sources
        if source.get("url") and source.get("stance")
    }
    return stances if stances else MISSING


def _format_optional_block(label: str, value: object) -> list[str]:
    if value is MISSING:
        return [f"- **{label}:** _not captured in this benchmark result_"]
    if value in (None, ""):
        return [f"- **{label}:** _captured as empty_"]
    if isinstance(value, (list, dict)):
        rendered = json.dumps(value, indent=2, ensure_ascii=False)
        return [f"- **{label}:**", "```json", rendered, "```"]
    return [f"- **{label}:** {value}"]


def _format_failure(
    arm: str,
    row: dict,
    sample_lookup: dict[tuple[str, str], dict],
    cache_lookup: dict[str, list[dict]],
    index: int,
) -> list[str]:
    sources = _sources_for_row(arm, row, sample_lookup, cache_lookup)

    lines = [
        f"### {index}. {row.get('dataset', 'Unknown')} / {row.get('id', '?')} - {row.get('label', 'unknown')}",
        "",
        "#### Input",
        f"- **Claim:** {row.get('claim', '')}",
        f"- **Expected label:** {row.get('label', 'unknown')}",
        f"- **Expected verdicts:** `{', '.join(row.get('expected_verdicts') or [])}`",
        f"- **Expected score range:** `{row.get('expected_score_range')}`",
        "",
        "#### Output",
        f"- **Actual verdict:** `{row.get('actual_verdict', '?')}`",
        f"- **Score:** `{row.get('score', '?')}`",
        f"- **Confidence:** `{row.get('confidence', 'unknown')}`",
        f"- **Correct:** `{row.get('correct')}`",
        f"- **Within one level:** `{row.get('within_one')}`",
        f"- **Failure reason:** {'; '.join(_failure_reasons(row))}",
        *_format_optional_block("TLDR", _row_value(row, "tldr")),
        *_format_optional_block("Explanation", _row_value(row, "explanation")),
        *_format_optional_block("Confidence reason", _row_value(row, "confidence_reason")),
        *_format_optional_block("Claim verdicts", _claim_verdicts_for_row(row)),
        *_format_optional_block("Source stances", _source_stances_for_row(row, sources)),
        "",
        f"#### {_source_label(arm)}",
    ]

    if not sources:
        if arm == "arm_baseline":
            lines.append("_No evidence sources are used for the bare LLM baseline._")
        else:
            lines.append("_No evidence sources captured or found in cache._")
    else:
        for idx, source in enumerate(sources, start=1):
            lines.extend(_format_source(source, idx))
            lines.append("")

    lines.extend([
        "#### Human Review Notes",
        "- Evidence sufficient? yes / no / unclear",
        "- Likely failure type: analyzer reasoning / evidence insufficient / label mapping / retrieval / extraction / other",
        "- Notes:",
        "",
    ])
    return lines


def build_audit(results: dict, *, arms: list[str], limit: int | None) -> str:
    sample_lookup = _load_samples()
    cache_lookup = _load_cache()

    lines = [
        "# Benchmark Failure Audit",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Results timestamp: {results.get('timestamp', 'unknown')}",
        f"- Model: {results.get('model', 'unknown')}",
        f"- Commit: {results.get('commit', 'unknown')}",
        "",
        "This report expands failed benchmark rows into a reviewable format with inputs, outputs, and evidence.",
        "Fields are marked as not captured only when the benchmark JSON does not contain them.",
        "",
    ]

    for arm in arms:
        rows = [row for row in results.get(arm, []) if not row.get("correct")]
        if limit is not None:
            rows = rows[:limit]
        lines.extend([
            f"## {ARM_LABELS.get(arm, arm)}",
            "",
            f"Failures shown: {len(rows)}",
            "",
        ])
        for index, row in enumerate(rows, start=1):
            lines.extend(_format_failure(arm, row, sample_lookup, cache_lookup, index))

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--arm",
        dest="arms",
        action="append",
        choices=sorted(ARM_LABELS),
        help="Arm to include. May be passed multiple times. Defaults to arm_a, arm_b, arm_c.",
    )
    parser.add_argument("--include-baseline", action="store_true")
    parser.add_argument("--limit", type=int, default=None, help="Maximum failures per arm.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    arms = args.arms or ["arm_a", "arm_b", "arm_c"]
    if args.include_baseline and "arm_baseline" not in arms:
        arms = ["arm_baseline", *arms]

    results = _load_json(args.results)
    audit = build_audit(results, arms=arms, limit=args.limit)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(audit)
    print(f"Failure audit written to: {args.output}")


if __name__ == "__main__":
    main()
