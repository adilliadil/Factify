"""Benchmark metrics computation, report formatting, and file output.

Called by conftest.py hooks at session end to generate timestamped .txt and .json reports.
Uses `backend.config` for the resolved pipeline model label (pytest `pythonpath` includes repo root).
"""

import json
import statistics
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from backend.config import config

REPORTS_DIR = Path(__file__).parent / "reports"
VERDICT_ORDER = ["false", "mostly_false", "mixed", "mostly_true", "true", "unverifiable"]


# ── Verdict helpers ────────────────────────────────────────────

def verdict_index(v: str) -> int:
    try:
        return VERDICT_ORDER.index(v)
    except ValueError:
        return -1


def within_one_level(actual: str, expected_verdicts: list[str]) -> bool:
    actual_idx = verdict_index(actual)
    if actual_idx == -1:
        return False
    return any(
        verdict_index(ev) != -1 and abs(actual_idx - verdict_index(ev)) <= 1
        for ev in expected_verdicts
    )


def failure_reasons(r: dict) -> list[str]:
    reasons: list[str] = []
    expected = r.get("expected_verdicts") or []
    actual = r.get("actual_verdict", "?")
    if actual not in expected:
        exp = "/".join(expected) if expected else "(none)"
        reasons.append(f"verdict: got {actual}, expected one of {exp}")

    return reasons or ["unknown (assertion mismatch not reconstructed)"]


# ── Aggregate metrics ─────────────────────────────────────────

def accuracy(results: list[dict]) -> float:
    if not results:
        return 0.0
    return sum(1 for r in results if r["correct"]) / len(results) * 100


def verdict_accuracy(results: list[dict]) -> float:
    if not results:
        return 0.0
    return sum(1 for r in results if r["verdict_correct"]) / len(results) * 100


def within_one_accuracy(results: list[dict]) -> float:
    if not results:
        return 0.0
    return sum(1 for r in results if r["within_one"]) / len(results) * 100


def by_dataset(results: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for r in results:
        grouped.setdefault(r["dataset"], []).append(r)
    return grouped


def by_label(results: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for r in results:
        grouped.setdefault(r["label"], []).append(r)
    return grouped


def confidence_calibration(results: list[dict]) -> dict[str, dict]:
    by_conf: dict[str, list[dict]] = {}
    for r in results:
        conf = r.get("confidence", "unknown")
        by_conf.setdefault(conf, []).append(r)

    calibration = {}
    for conf, items in sorted(by_conf.items()):
        total = len(items)
        correct = sum(1 for i in items if i["correct"])
        calibration[conf] = {
            "total": total,
            "correct": correct,
            "accuracy": correct / total * 100 if total else 0.0,
        }
    return calibration


def score_distribution(results: list[dict]) -> dict[str, dict]:
    bl = by_label(results)
    dist = {}
    for label, items in sorted(bl.items()):
        scores = [r["score"] for r in items if r["score"] >= 0]
        if scores:
            dist[label] = {
                "mean": round(statistics.mean(scores), 1),
                "std": round(statistics.stdev(scores), 1) if len(scores) > 1 else 0.0,
                "count": len(scores),
            }
        else:
            dist[label] = {"mean": 0.0, "std": 0.0, "count": 0}
    return dist


def get_git_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return "unknown"


# ── Result assembly ────────────────────────────────────────────

def build_structured_results(
    pass_fail: dict[str, list[dict]],
    result_data: dict[str, dict],
    sample_lookup: dict[str, dict],
) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    """Merge pass/fail status with stored result data and sample metadata."""
    arm_lists = {}
    for arm_key in ("arm_baseline", "arm_a", "arm_b", "arm_c"):
        results = []
        for pf in pass_fail[arm_key]:
            key = pf["key"]
            meta = sample_lookup.get(key, {})
            stored = result_data.get(f"{arm_key}:{key}", {})

            actual_verdict = stored.get("actual_verdict", "?")
            score = stored.get("score", -1)
            conf = stored.get("confidence", "unknown")
            expected = meta.get("expected_verdicts", [])

            verdict_correct = actual_verdict in expected if expected else False
            row = {
                "dataset": meta.get("dataset", "Unknown"),
                "id": meta.get("id", key),
                "claim": meta.get("claim", ""),
                "label": meta.get("label", "unknown"),
                "expected_verdicts": expected,
                "expected_score_range": meta.get("expected_score_range"),
                "actual_verdict": actual_verdict,
                "score": score,
                "confidence": conf,
                "correct": verdict_correct,
                "verdict_correct": verdict_correct,
                "within_one": verdict_correct or within_one_level(actual_verdict, expected),
            }
            for field in (
                "confidence_reason",
                "tldr",
                "explanation",
                "claim_verdicts",
                "source_stances",
                "claims",
                "sources",
            ):
                if field in stored:
                    row[field] = stored[field]
            results.append(row)
        arm_lists[arm_key] = results
    return arm_lists["arm_baseline"], arm_lists["arm_a"], arm_lists["arm_b"], arm_lists["arm_c"]


# ── Report formatting ─────────────────────────────────────────

def format_report(
    arm_baseline: list[dict],
    arm_a: list[dict],
    arm_b: list[dict],
    arm_c: list[dict],
) -> str:
    now = datetime.now(timezone.utc)
    commit = get_git_commit()
    model = config.llm.model

    datasets_summary: dict[str, int] = {}
    for r in arm_b or arm_baseline:
        datasets_summary[r["dataset"]] = datasets_summary.get(r["dataset"], 0) + 1
    ds_str = ", ".join(f"{name} ({count} samples)" for name, count in sorted(datasets_summary.items()))
    tavily_searches = len(arm_b) + len(arm_c)

    lines = [
        f"Benchmark Report — {now.strftime('%Y-%m-%d %H:%M:%S')} UTC",
        f"Model: {model}",
        f"Commit: {commit}",
        f"Datasets: {ds_str}",
        f"Total Tavily searches: {tavily_searches}",
        "─" * 80,
        "",
    ]

    hdr_0 = "Arm 0 (Bare)"
    hdr_a = "Arm A (Gold)"
    hdr_b = "Arm B (Search)"
    hdr_c = "Arm C (Full)"

    # Overall Accuracy
    lines.append("── Overall Accuracy ──────────────────────────────────────────────────────────")
    lines.append(
        f"{'':20s} {hdr_0:>14s}  {hdr_a:>14s}  {hdr_b:>14s}  {hdr_c:>14s}"
    )

    ref_arm = arm_b or arm_baseline
    all_datasets = sorted(set(r["dataset"] for r in ref_arm)) if ref_arm else []
    arm_bl_by_ds = by_dataset(arm_baseline)
    arm_a_by_ds = by_dataset(arm_a)
    arm_b_by_ds = by_dataset(arm_b)
    arm_c_by_ds = by_dataset(arm_c)

    for ds in all_datasets:
        bl_acc = f"{accuracy(arm_bl_by_ds.get(ds, [])):.1f}%" if ds in arm_bl_by_ds else "—"
        a_acc = f"{accuracy(arm_a_by_ds.get(ds, [])):.1f}%" if ds in arm_a_by_ds else "—"
        b_acc = f"{accuracy(arm_b_by_ds.get(ds, [])):.1f}%" if ds in arm_b_by_ds else "—"
        c_acc = f"{accuracy(arm_c_by_ds.get(ds, [])):.1f}%" if ds in arm_c_by_ds else "—"
        lines.append(f"  {ds:18s} {bl_acc:>14s}  {a_acc:>14s}  {b_acc:>14s}  {c_acc:>14s}")

    bl_total = f"{accuracy(arm_baseline):.1f}%" if arm_baseline else "—"
    a_total = f"{accuracy(arm_a):.1f}%" if arm_a else "—"
    b_total = f"{accuracy(arm_b):.1f}%" if arm_b else "—"
    c_total = f"{accuracy(arm_c):.1f}%" if arm_c else "—"
    lines.append(f"  {'Combined':18s} {bl_total:>14s}  {a_total:>14s}  {b_total:>14s}  {c_total:>14s}")
    lines.append("")

    # Within-One-Level Accuracy
    lines.append("── Within-One-Level Accuracy ─────────────────────────────────────────────────")
    bl_w1 = f"{within_one_accuracy(arm_baseline):.1f}%" if arm_baseline else "—"
    a_w1 = f"{within_one_accuracy(arm_a):.1f}%" if arm_a else "—"
    b_w1 = f"{within_one_accuracy(arm_b):.1f}%" if arm_b else "—"
    c_w1 = f"{within_one_accuracy(arm_c):.1f}%" if arm_c else "—"
    lines.append(f"  {'Combined':18s} {bl_w1:>14s}  {a_w1:>14s}  {b_w1:>14s}  {c_w1:>14s}")
    lines.append("")

    lines.append("── Delta Analysis ───────────────────────────────────────────────────────────")

    if arm_baseline and arm_b:
        evidence_delta = verdict_accuracy(arm_b) - verdict_accuracy(arm_baseline)
        direction = "search evidence helps" if evidence_delta > 0 else "bare LLM better" if evidence_delta < 0 else "no difference"
        lines.append(f"  Evidence delta (B - 0): {evidence_delta:+.1f}%  ← {direction}")

    if arm_a:
        if arm_baseline:
            arm_bl_comparable = [r for r in arm_baseline if r["dataset"] in arm_a_by_ds]
            gold_delta = verdict_accuracy(arm_a) - verdict_accuracy(arm_bl_comparable)
            direction = "gold evidence helps" if gold_delta > 0 else "bare LLM better" if gold_delta < 0 else "no difference"
            lines.append(f"  Gold delta    (A - 0): {gold_delta:+.1f}%  ← {direction}")

        arm_b_comparable = [r for r in arm_b if r["dataset"] in arm_a_by_ds]
        search_delta = verdict_accuracy(arm_a) - verdict_accuracy(arm_b_comparable)
        direction = "search helps" if search_delta < 0 else "gold evidence better" if search_delta > 0 else "no difference"
        lines.append(f"  Search delta  (A - B): {search_delta:+.1f}%  ← {direction}")

    if arm_b and arm_c:
        extract_delta = verdict_accuracy(arm_b) - verdict_accuracy(arm_c)
        direction = "extraction helps" if extract_delta < 0 else "extraction hurts" if extract_delta > 0 else "no difference"
        lines.append(f"  Extract delta (B - C): {extract_delta:+.1f}%  ← {direction}")

    lines.append("")

    # Per-Label Accuracy (Arm C)
    lines.append("── Per-Label Accuracy (Arm C — Full Pipeline) ──────────────────────────────")
    for ds in all_datasets:
        ds_results = arm_c_by_ds.get(ds, [])
        bl = by_label(ds_results)
        lines.append(f"  {ds}:")
        for label, items in sorted(bl.items()):
            correct = sum(1 for i in items if i["correct"])
            total = len(items)
            pct = correct / total * 100 if total else 0
            lines.append(f"    {label:40s} {pct:5.1f}%  ({correct}/{total})")
        lines.append("")

    # Confidence Calibration (Arm C)
    lines.append("── Confidence Calibration (Arm C) ───────────────────────────────────────────")
    cal = confidence_calibration(arm_c)
    for conf, stats in cal.items():
        lines.append(
            f'  When system says "{conf}": '
            f"{stats['accuracy']:.1f}% actually correct  ({stats['correct']}/{stats['total']})"
        )
    lines.append("")

    # Score Distribution (Arm C)
    lines.append("── Score Distribution (Arm C, mean ± std by label) ─────────────────────────")
    dist = score_distribution(arm_c)
    for label, stats in dist.items():
        lines.append(f"  {label:40s} {stats['mean']:5.1f} ± {stats['std']:4.1f}  (n={stats['count']})")
    lines.append("")

    # Failed Samples
    arm_specs = [
        ("Arm 0 — Bare LLM Baseline", arm_baseline),
        ("Arm A — Gold Evidence", arm_a),
        ("Arm B — Searched Evidence", arm_b),
        ("Arm C — Full Pipeline", arm_c),
    ]
    failures_exist = any(not r["correct"] for _, results in arm_specs for r in results)
    if failures_exist:
        lines.append("── Failed Samples ───────────────────────────────────────────────────────────")
        lines.append("")
        for arm_label, results in arm_specs:
            failed = [r for r in results if not r["correct"]]
            if not failed:
                continue
            lines.append(f"  {arm_label} ({len(failed)} failed / {len(results)} total):")
            lines.append(
                f"    {'ID':16s}{'Label':34s}{'Verdict (got / expected)':40s}"
                f"{'Score':22s}Failure reasons"
            )
            for r in failed:
                exp_v = "/".join(r["expected_verdicts"])
                verdict_col = f"{r['actual_verdict']} / {exp_v}"
                score_col = f"{r['score']}"
                reasons = "; ".join(failure_reasons(r))
                lines.append(
                    f"    {r['id']:16s}{r['label'][:34]:34s}{verdict_col:40s}{score_col:22s}{reasons}"
                )
            lines.append("")

    lines.append("═" * 80)
    return "\n".join(lines)


# ── File output ────────────────────────────────────────────────

def write_reports(
    arm_baseline: list[dict],
    arm_a: list[dict],
    arm_b: list[dict],
    arm_c: list[dict],
) -> Path:
    """Generate and write both .txt and .json reports. Returns the .txt path."""
    report_text = format_report(arm_baseline, arm_a, arm_b, arm_c)
    print(f"\n\n{report_text}")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)

    txt_path = REPORTS_DIR / f"{now.strftime('%Y-%m-%d_%H%M%S')}.txt"
    txt_path.write_text(report_text)
    print(f"\nReport written to: {txt_path}")

    json_path = REPORTS_DIR / "benchmark_results.json"
    json_data = {
        "timestamp": now.isoformat(),
        "model": config.llm.model,
        "commit": get_git_commit(),
        "arm_baseline": arm_baseline,
        "arm_a": arm_a,
        "arm_b": arm_b,
        "arm_c": arm_c,
    }
    json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False))
    print(f"JSON snapshot written to: {json_path}")

    return txt_path
