"""Benchmark metrics computation, report formatting, and file output.

Called by conftest.py hooks at session end to generate reports (``.txt`` + ``benchmark_results.json``,
or JSON-only when ``BENCHMARK_OUTPUT_FILE`` is set for multi-model runs).
Uses `backend.config` for the resolved pipeline model label (pytest `pythonpath` includes repo root).

Set ``BENCHMARK_OUTPUT_FILE`` to an absolute path to write the JSON snapshot there instead of
``reports/benchmark_results.json`` (used by ``run_benchmark`` for parallel LLM runs).
"""

import json
import os
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


def failure_reasons(r: dict, *, check_score_range: bool) -> list[str]:
    """Explain why a benchmark row is incorrect (reconstructs assertions from `test_benchmark`)."""
    reasons: list[str] = []
    expected = r.get("expected_verdicts") or []
    actual = r.get("actual_verdict", "?")
    if actual not in expected:
        exp = "/".join(expected) if expected else "(none)"
        reasons.append(f"verdict: got {actual}, expected one of {exp}")

    if check_score_range:
        rng = r.get("expected_score_range")
        if rng is not None and len(rng) == 2:
            lo, hi = int(rng[0]), int(rng[1])
            score = r.get("score", -1)
            if not (lo <= score <= hi):
                reasons.append(f"score: got {score}, expected in [{lo}, {hi}]")

    return reasons or ["unknown (assertion mismatch not reconstructed)"]


# ── Aggregate metrics ─────────────────────────────────────────

def accuracy(results: list[dict]) -> float:
    """Exact-match accuracy over rows where the pipeline returned a result (excludes request failures)."""
    eligible = [r for r in results if not r.get("request_failed")]
    if not eligible:
        return 0.0
    return sum(1 for r in eligible if r["correct"]) / len(eligible) * 100


def verdict_accuracy(results: list[dict]) -> float:
    """Accuracy based on verdict correctness only (ignores score-range checks)."""
    if not results:
        return 0.0
    return sum(1 for r in results if r["verdict_correct"]) / len(results) * 100


def within_one_accuracy(results: list[dict]) -> float:
    """Within-one-level accuracy over rows with a completed request (excludes request failures)."""
    eligible = [r for r in results if not r.get("request_failed")]
    if not eligible:
        return 0.0
    return sum(1 for r in eligible if r["within_one"]) / len(eligible) * 100


def request_failure_rate(results: list[dict]) -> float:
    """Share of benchmark rows where the API call failed before a result was stored."""
    if not results:
        return 0.0
    return sum(1 for r in results if r.get("request_failed")) / len(results) * 100


def _incorrect_assertion_count(arm: list[dict]) -> int:
    """Rows where we got a result but verdict/score did not match gold (excludes request failures)."""
    return sum(1 for r in arm if not r.get("correct") and not r.get("request_failed"))


def _request_failure_count(arm: list[dict]) -> int:
    return sum(1 for r in arm if r.get("request_failed"))


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
        if r.get("request_failed"):
            continue
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
    bl = by_label([r for r in results if not r.get("request_failed")])
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
            request_failed = bool(pf.get("request_failed"))

            actual_verdict = stored.get("actual_verdict", "?")
            score = stored.get("score", -1)
            conf = stored.get("confidence", "unknown")
            expected = meta.get("expected_verdicts", [])

            verdict_correct = actual_verdict in expected if expected else False
            within_one = (
                False
                if request_failed
                else (pf["passed"] or within_one_level(actual_verdict, expected))
            )

            results.append({
                "dataset": meta.get("dataset", "Unknown"),
                "id": meta.get("id", key),
                "claim": meta.get("claim", ""),
                "label": meta.get("label", "unknown"),
                "expected_verdicts": expected,
                "expected_score_range": meta.get("expected_score_range"),
                "actual_verdict": actual_verdict,
                "score": score,
                "confidence": conf,
                "request_failed": request_failed,
                "correct": pf["passed"],
                "verdict_correct": verdict_correct,
                "within_one": within_one,
            })
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

    hdr_0 = "Arm 0 (None)"
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

    # Request failures (API error before result stored; excluded from accuracy above)
    lines.append("── Request failures (%) ─────────────────────────────────────")
    lines.append(f"{'':20s} {'Arm A (Gold)':>14s}  {'Arm B (Search)':>14s}  {'Arm C (Full)':>14s}")
    for ds in all_datasets:
        a_rf = f"{request_failure_rate(arm_a_by_ds.get(ds, [])):.1f}%" if ds in arm_a_by_ds else "—"
        b_rf = f"{request_failure_rate(arm_b_by_ds.get(ds, [])):.1f}%"
        c_rf = f"{request_failure_rate(arm_c_by_ds.get(ds, [])):.1f}%"
        lines.append(f"  {ds:18s} {a_rf:>14s}  {b_rf:>14s}  {c_rf:>14s}")
    a_rf_tot = f"{request_failure_rate(arm_a):.1f}%" if arm_a else "—"
    b_rf_tot = f"{request_failure_rate(arm_b):.1f}%"
    c_rf_tot = f"{request_failure_rate(arm_c):.1f}%"
    lines.append(f"  {'Combined':18s} {a_rf_tot:>14s}  {b_rf_tot:>14s}  {c_rf_tot:>14s}")
    lines.append("")

    # Within-One-Level Accuracy
    lines.append("── Within-One-Level Accuracy ─────────────────────────────────────────────────")
    bl_w1 = f"{within_one_accuracy(arm_baseline):.1f}%" if arm_baseline else "—"
    a_w1 = f"{within_one_accuracy(arm_a):.1f}%" if arm_a else "—"
    b_w1 = f"{within_one_accuracy(arm_b):.1f}%" if arm_b else "—"
    c_w1 = f"{within_one_accuracy(arm_c):.1f}%" if arm_c else "—"
    lines.append(f"  {'Combined':18s} {bl_w1:>14s}  {a_w1:>14s}  {b_w1:>14s}  {c_w1:>14s}")
    lines.append("")

    # Delta Analysis (verdict-only so Arms are compared on equal footing;
    # Arm A also checks score range, which would unfairly penalise it)
    lines.append("── Delta Analysis (verdict-only) ────────────────────────────────────────────")

    if arm_baseline and arm_b:
        evidence_delta = verdict_accuracy(arm_b) - verdict_accuracy(arm_baseline)
        direction = "search evidence helps" if evidence_delta > 0 else "no evidence better" if evidence_delta < 0 else "no difference"
        lines.append(f"  Evidence delta (B - 0): {evidence_delta:+.1f}%  ← {direction}")

    if arm_a:
        if arm_baseline:
            arm_bl_comparable = [r for r in arm_baseline if r["dataset"] in arm_a_by_ds]
            gold_delta = verdict_accuracy(arm_a) - verdict_accuracy(arm_bl_comparable)
            direction = "gold evidence helps" if gold_delta > 0 else "no evidence better" if gold_delta < 0 else "no difference"
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
            eligible = [i for i in items if not i.get("request_failed")]
            correct = sum(1 for i in eligible if i["correct"])
            total = len(eligible)
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
        ("Arm 0 — Baseline (No Evidence)", arm_baseline, False),
        ("Arm A — Gold Evidence", arm_a, True),
        ("Arm B — Searched Evidence", arm_b, False),
        ("Arm C — Full Pipeline", arm_c, False),
    ]
    failures_exist = any(not r["correct"] for _, results, _ in arm_specs for r in results)
    if failures_exist:
        lines.append("── Failed Samples ───────────────────────────────────────────────────────────")
        lines.append("")
        for arm_label, results, check_score_range in arm_specs:
            failed = [r for r in results if not r["correct"]]
            if not failed:
                continue
            req_failed = [r for r in failed if r.get("request_failed")]
            incorrect = [r for r in failed if not r.get("request_failed")]
            lines.append(
                f"  {arm_label} ({len(failed)} failed / {len(results)} total"
                f"{f', {len(req_failed)} request failure(s)' if req_failed else ''}):"
            )
            if req_failed:
                lines.append(f"    Request failed (no stored result): {', '.join(str(r['id']) for r in req_failed)}")
            if not incorrect:
                lines.append("")
                continue
            lines.append(
                f"    {'ID':16s}{'Label':34s}{'Verdict (got / expected)':40s}"
                f"{'Score (got / exp. range)':26s}Failure reasons"
            )
            for r in incorrect:
                exp_v = "/".join(r["expected_verdicts"])
                verdict_col = f"{r['actual_verdict']} / {exp_v}"
                sr = r.get("expected_score_range")
                if check_score_range and sr is not None and len(sr) == 2:
                    score_col = f"{r['score']} / [{sr[0]}, {sr[1]}]"
                else:
                    score_col = f"{r['score']}" + ("  (no range check)" if not check_score_range else "")
                reasons = "; ".join(failure_reasons(r, check_score_range=check_score_range))
                lines.append(
                    f"    {r['id']:16s}{r['label'][:34]:34s}{verdict_col:40s}{score_col:26s}{reasons}"
                )
            lines.append("")

    lines.append("═" * 80)
    return "\n".join(lines)


# ── Multi-model comparison (Markdown) ──────────────────────────

def _sample_count_for_timing(arm_a: list[dict], arm_b: list[dict], arm_c: list[dict]) -> int:
    """How many benchmark rows ran (used for average wall time per sample)."""
    return max(len(arm_a), len(arm_b), len(arm_c))


def _primary_arm_results(
    arm_a: list[dict], arm_b: list[dict], arm_c: list[dict],
) -> tuple[str, list[dict]]:
    """Pick the first non-empty arm for per-label / calibration tables."""
    if arm_a:
        return ("Arm A (Gold)", arm_a)
    if arm_b:
        return ("Arm B (Search)", arm_b)
    if arm_c:
        return ("Arm C (Full)", arm_c)
    return ("(none)", [])


def _per_label_accuracy_table(
    models: list[str],
    runs: dict[str, dict],
) -> list[str]:
    """Build markdown rows: | Label | m1 | m2 | ... |"""
    # Union of labels across models from primary arm
    labels: set[str] = set()
    primary_by_model: dict[str, list[dict]] = {}
    for m in models:
        d = runs[m]
        arm_a = d.get("arm_a") or []
        arm_b = d.get("arm_b") or []
        arm_c = d.get("arm_c") or []
        _, rows = _primary_arm_results(arm_a, arm_b, arm_c)
        primary_by_model[m] = rows
        for r in rows:
            labels.add(r.get("label") or "unknown")

    lines: list[str] = []
    if not labels:
        lines.append("_No per-label data._")
        return lines

    header = "| Label | " + " | ".join(models) + " |"
    sep = "|---|" + "|".join("---" for _ in models) + "|"
    lines.extend([header, sep])

    for label in sorted(labels):
        cells = []
        for m in models:
            items = [r for r in primary_by_model[m] if (r.get("label") or "unknown") == label]
            if not items:
                cells.append("—")
            else:
                acc = accuracy(items)
                cells.append(f"{acc:.1f}%")
        lines.append("| " + label.replace("|", "\\|") + " | " + " | ".join(cells) + " |")
    return lines


def _confidence_calibration_md(results: list[dict]) -> list[str]:
    if not results:
        return ["_No confidence data._"]
    cal = confidence_calibration(results)
    out = []
    for conf, stats in sorted(cal.items()):
        out.append(
            f'- **{conf}**: {stats["accuracy"]:.1f}% correct ({stats["correct"]}/{stats["total"]})'
        )
    return out


def format_comparison_report(
    runs: dict[str, dict],
    *,
    samples_cap: int | None = None,
    timestamp_iso: str | None = None,
    commit: str | None = None,
    benchmark_class: str | None = None,
) -> str:
    """Build a Markdown report comparing multiple benchmark JSON payloads.

    Each value in ``runs`` should include ``arm_a``, ``arm_b``, ``arm_c`` (lists like JSON export),
    and ``wall_time_s`` (float, seconds). Optional: ``pytest_exit_code`` (int). Row dicts may include
    ``request_failed`` (bool) when the pipeline errored before ``store_benchmark_result``; accuracy
    excludes those rows; request-failure tables use them.

    Keys of ``runs`` are display names (usually LLM aliases).
    """
    now = timestamp_iso or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    commit_s = commit if commit is not None else get_git_commit()
    models = list(runs.keys())

    lines: list[str] = [
        "# Benchmark comparison report",
        "",
        f"**Date:** {now}  |  **Commit:** {commit_s}",
    ]
    if benchmark_class:
        lines.append(f"**Test class:** `{benchmark_class}`")
    if samples_cap is not None:
        lines.append(f"**Sample cap:** {samples_cap} (first N combined benchmark rows)")
    lines.append("")

    # Timing
    lines.append("## Timing")
    lines.append("")
    lines.append("| Model | Wall time | Avg / sample | Samples (max arm) | Pytest |")
    lines.append("|---|---|---|---|---|")
    for m in models:
        d = runs[m]
        wt = float(d.get("wall_time_s", 0.0))
        arm_a = d.get("arm_a") or []
        arm_b = d.get("arm_b") or []
        arm_c = d.get("arm_c") or []
        n = _sample_count_for_timing(arm_a, arm_b, arm_c)
        avg = wt / n if n else 0.0
        exit_code = d.get("pytest_exit_code")
        exit_cell = "—" if exit_code is None else str(exit_code)
        lines.append(
            f"| `{m}` | {wt:.2f}s | {avg:.2f}s | {n} | {exit_cell} |"
        )
    lines.append("")

    # Accuracy by arm
    lines.append("## Accuracy by arm")
    lines.append("")
    lines.append("| Model | Arm A exact | Arm A w/in 1 | Arm B exact | Arm B w/in 1 | Arm C exact | Arm C w/in 1 |")
    lines.append("|---|---|---|---|---|---|---|")
    for m in models:
        d = runs[m]
        arm_a = d.get("arm_a") or []
        arm_b = d.get("arm_b") or []
        arm_c = d.get("arm_c") or []
        def cells(arm: list[dict]) -> tuple[str, str]:
            if not arm:
                return ("—", "—")
            return (f"{accuracy(arm):.1f}%", f"{within_one_accuracy(arm):.1f}%")

        a1, a2 = cells(arm_a)
        b1, b2 = cells(arm_b)
        c1, c2 = cells(arm_c)
        lines.append(f"| `{m}` | {a1} | {a2} | {b1} | {b2} | {c1} | {c2} |")
    lines.append("")

    # Request failure rate by arm (share of rows where the API call failed before a result was stored)
    lines.append("## Request failures (% by arm)")
    lines.append("")
    lines.append("| Model | Arm A | Arm B | Arm C |")
    lines.append("|---|---|---|---|")
    for m in models:
        d = runs[m]
        arm_a = d.get("arm_a") or []
        arm_b = d.get("arm_b") or []
        arm_c = d.get("arm_c") or []

        def rf_cell(arm: list[dict]) -> str:
            if not arm:
                return "—"
            return f"{request_failure_rate(arm):.1f}%"

        lines.append(f"| `{m}` | {rf_cell(arm_a)} | {rf_cell(arm_b)} | {rf_cell(arm_c)} |")
    lines.append("")

    # Per-label on primary arm
    lines.append("## Per-label accuracy (primary arm)")
    arm_label, _ = _primary_arm_results(
        runs[models[0]].get("arm_a") or [],
        runs[models[0]].get("arm_b") or [],
        runs[models[0]].get("arm_c") or [],
    )
    lines.append(
        f"_Per-label table: each column uses that model's primary arm (first non-empty among A, B, C); "
        f"example from first model: **{arm_label}**._"
    )
    lines.append("")
    lines.extend(_per_label_accuracy_table(models, runs))
    lines.append("")

    # Confidence calibration (primary arm of each model)
    lines.append("## Confidence calibration (primary arm per model)")
    lines.append("")
    for m in models:
        d = runs[m]
        arm_a = d.get("arm_a") or []
        arm_b = d.get("arm_b") or []
        arm_c = d.get("arm_c") or []
        _, rows = _primary_arm_results(arm_a, arm_b, arm_c)
        lines.append(f"### `{m}`")
        lines.extend(_confidence_calibration_md(rows))
        lines.append("")

    # Incorrect verdict / score (excludes request failures; accuracy denominator matches these)
    lines.append("## Incorrect verdicts (counts, excl. request failures)")
    lines.append("")
    lines.append("| Model | Arm A | Arm B | Arm C | Total |")
    lines.append("|---|---|---|---|---|")
    for m in models:
        d = runs[m]
        fa = _incorrect_assertion_count(d.get("arm_a") or [])
        fb = _incorrect_assertion_count(d.get("arm_b") or [])
        fc = _incorrect_assertion_count(d.get("arm_c") or [])
        tot = fa + fb + fc
        lines.append(f"| `{m}` | {fa} | {fb} | {fc} | {tot} |")
    lines.append("")

    # Request failures (counts)
    lines.append("## Request failures (counts)")
    lines.append("")
    lines.append("| Model | Arm A | Arm B | Arm C | Total |")
    lines.append("|---|---|---|---|---|")
    req_fail_totals: list[tuple[int, str]] = []
    for m in models:
        d = runs[m]
        fa = _request_failure_count(d.get("arm_a") or [])
        fb = _request_failure_count(d.get("arm_b") or [])
        fc = _request_failure_count(d.get("arm_c") or [])
        tot = fa + fb + fc
        req_fail_totals.append((tot, m))
        lines.append(f"| `{m}` | {fa} | {fb} | {fc} | {tot} |")
    lines.append("")

    # Worst models by incorrect verdicts
    inc_totals: list[tuple[int, str]] = []
    for m in models:
        d = runs[m]
        fa = _incorrect_assertion_count(d.get("arm_a") or [])
        fb = _incorrect_assertion_count(d.get("arm_b") or [])
        fc = _incorrect_assertion_count(d.get("arm_c") or [])
        inc_totals.append((fa + fb + fc, m))
    inc_totals.sort(reverse=True)
    if inc_totals and inc_totals[0][0] > 0:
        lines.append(
            "**Most incorrect verdicts (total across arms):** "
            + ", ".join(f"`{x[1]}` ({x[0]})" for x in inc_totals[: min(5, len(inc_totals))] if x[0] > 0)
        )
        lines.append("")

    req_fail_totals.sort(reverse=True)
    if req_fail_totals and req_fail_totals[0][0] > 0:
        lines.append(
            "**Most request failures (total across arms):** "
            + ", ".join(f"`{x[1]}` ({x[0]})" for x in req_fail_totals[: min(5, len(req_fail_totals))] if x[0] > 0)
        )
        lines.append("")

    lines.append("---")
    lines.append("_Generated by `python -m evals.run_benchmark`._")
    return "\n".join(lines)


# ── File output ────────────────────────────────────────────────

def write_reports(
    arm_baseline: list[dict],
    arm_a: list[dict],
    arm_b: list[dict],
    arm_c: list[dict],
) -> Path:
    """Generate benchmark reports.

    Standalone ``pytest`` runs write a timestamped ``.txt`` report and ``benchmark_results.json``.
    When ``BENCHMARK_OUTPUT_FILE`` is set (``python -m evals.run_benchmark`` subprocesses), only
    the JSON snapshot is written so the parent can emit a single Markdown comparison — no per-model
    ``.txt`` spam under ``reports/``.

    Returns the path to the primary artefact: ``.txt`` for standalone runs, otherwise the JSON path.
    """
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    out_override = os.environ.get("BENCHMARK_OUTPUT_FILE")
    is_subprocess_run = bool(out_override)

    primary_path: Path
    if not is_subprocess_run:
        report_text = format_report(arm_baseline, arm_a, arm_b, arm_c)
        print(f"\n\n{report_text}")
        primary_path = REPORTS_DIR / f"{now.strftime('%Y-%m-%d_%H%M%S')}.txt"
        primary_path.write_text(report_text)
        print(f"\nReport written to: {primary_path}")
    else:
        primary_path = Path(out_override).expanduser() if out_override else REPORTS_DIR / "benchmark_results.json"

    json_path = Path(out_override).expanduser() if out_override else REPORTS_DIR / "benchmark_results.json"
    json_data = {
        "timestamp": now.isoformat(),
        "model": config.llm.model,
        "commit": get_git_commit(),
        "arm_baseline": arm_baseline,
        "arm_a": arm_a,
        "arm_b": arm_b,
        "arm_c": arm_c,
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(json_data, indent=2, ensure_ascii=False))
    print(f"JSON snapshot written to: {json_path}")

    return primary_path
