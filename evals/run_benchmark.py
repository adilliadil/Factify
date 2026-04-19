"""Run benchmark tests for multiple LLM aliases in parallel and write a Markdown comparison report.

Example::

    python -m evals.run_benchmark --models gpt-nano kimi --samples 10 --class TestGoldEvidenceAnalysis

Requires the same credentials as ``pytest evals/test_benchmark.py -m benchmark`` (see README).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
# Pytest must run with cwd here so ``rootdir`` is ``evals/`` and ``conftest`` can import
# ``benchmark_reporting`` (see ``evals/pytest.ini`` ``pythonpath = ..``).
EVAL_ROOT = REPO_ROOT / "evals"


def _load_dotenv_for_cli() -> None:
    """Load the same `.env` files pytest uses so ``config.models`` matches subprocess runs.

    Pytest loads ``.env`` via ``pytest-dotenv`` (see ``evals/pytest.ini``); the CLI parent
    process does not, so registry-alias warnings were false positives without this.
    """
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    root_env = REPO_ROOT / ".env"
    if root_env.is_file():
        load_dotenv(root_env, override=False)
    eval_env = EVAL_ROOT / ".env"
    if eval_env.is_file():
        load_dotenv(eval_env, override=False)


def _safe_filename_fragment(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_") or "model"


def _warn_if_not_registry_alias(models: list[str]) -> None:
    """Warn when a model id is not in ``config.models`` (may still be valid via generic LLM_MODEL)."""
    from backend.config import config

    config.reset()
    try:
        reg = set(config.models.keys())
    finally:
        config.reset()

    for m in models:
        if m not in reg:
            print(
                f"Warning: {m!r} is not in the model registry (config.models). "
                "If you intend a raw provider model id, ensure LLM_PROVIDER and keys are set.",
                file=sys.stderr,
            )


def _build_pytest_cmd(benchmark_class: str | None) -> list[str]:
    """Build pytest argv; run with ``cwd=EVAL_ROOT`` so imports match ``python -m pytest`` from ``evals/``."""
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "test_benchmark.py",
        "-c",
        "pytest.ini",
        "-m",
        "benchmark",
        "--tb",
        "no",
        "-q",
    ]
    if benchmark_class:
        cmd.extend(["-k", benchmark_class])
    return cmd


def _run_one_model(
    model: str,
    json_out: Path,
    *,
    samples: int | None,
    benchmark_class: str | None,
) -> tuple[str, int, float]:
    """Run pytest for one model; return (model, exit_code, wall_time_s)."""
    env = os.environ.copy()
    env["LLM_MODEL"] = model
    env["BENCHMARK_OUTPUT_FILE"] = str(json_out)
    if samples is not None:
        env["BENCHMARK_MAX_SAMPLES"] = str(samples)
    else:
        env.pop("BENCHMARK_MAX_SAMPLES", None)

    cmd = _build_pytest_cmd(benchmark_class)
    t0 = time.perf_counter()
    proc = subprocess.run(
        cmd,
        env=env,
        cwd=str(EVAL_ROOT),
        capture_output=True,
        text=True,
    )
    wall = time.perf_counter() - t0
    if proc.returncode != 0:
        tail = ((proc.stderr or "") + "\n" + (proc.stdout or "")).strip()
        if tail:
            print(f"--- pytest output for {model!r} (exit {proc.returncode}) ---\n{tail[-12000:]}\n", file=sys.stderr)
    return model, proc.returncode, wall


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Run benchmark evals for multiple LLMs in parallel and emit a comparison report.",
    )
    p.add_argument(
        "--models",
        nargs="+",
        required=True,
        metavar="ALIAS",
        help="One or more LLM_MODEL values (registry aliases or raw model ids).",
    )
    p.add_argument(
        "--samples",
        type=int,
        default=None,
        metavar="N",
        help="Cap benchmark rows to the first N combined samples (default: all).",
    )
    p.add_argument(
        "--class",
        dest="benchmark_class",
        default=None,
        metavar="NAME",
        help="Pytest class name filter, e.g. TestGoldEvidenceAnalysis (default: all benchmark classes).",
    )
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    models = list(args.models)
    if args.samples is not None and args.samples < 1:
        print("--samples must be >= 1", file=sys.stderr)
        return 2

    _load_dotenv_for_cli()
    _warn_if_not_registry_alias(models)

    reports_dir = REPO_ROOT / "evals" / "reports"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M%S")
    run_dir = reports_dir / f"comparison_{ts}"
    run_dir.mkdir(parents=True, exist_ok=True)

    json_paths = {m: run_dir / f"benchmark_{_safe_filename_fragment(m)}.json" for m in models}

    wall_by_model: dict[str, float] = {}
    code_by_model: dict[str, int] = {}

    max_workers = min(len(models), max(1, (os.cpu_count() or 4)))

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {
            ex.submit(
                _run_one_model,
                m,
                json_paths[m],
                samples=args.samples,
                benchmark_class=args.benchmark_class,
            ): m
            for m in models
        }
        for fut in as_completed(futs):
            m = futs[fut]
            try:
                model, exit_code, wall = fut.result()
                wall_by_model[model] = wall
                code_by_model[model] = exit_code
            except Exception as exc:
                print(f"Error running benchmark for {m!r}: {exc}", file=sys.stderr)
                wall_by_model[m] = 0.0
                code_by_model[m] = -1

    from .benchmark_reporting import format_comparison_report, get_git_commit

    runs: dict[str, dict] = {}
    for m in models:
        path = json_paths[m]
        base: dict = {
            "wall_time_s": float(wall_by_model.get(m, 0.0)),
            "pytest_exit_code": int(code_by_model.get(m, -1)),
            "arm_a": [],
            "arm_b": [],
            "arm_c": [],
        }
        if path.is_file():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
                base["arm_a"] = data.get("arm_a") or []
                base["arm_b"] = data.get("arm_b") or []
                base["arm_c"] = data.get("arm_c") or []
            except (json.JSONDecodeError, OSError) as exc:
                print(f"Warning: could not read results for {m!r} from {path}: {exc}", file=sys.stderr)
        else:
            print(
                f"Warning: missing JSON for {m!r}: {path}. "
                "If pytest exited 0, benchmark hooks may not have run (e.g. all benchmark tests skipped — "
                "check `.env` has valid pipeline LLM + Tavily keys for live benchmarks).",
                file=sys.stderr,
            )
        runs[m] = base

    ts_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    try:
        md = format_comparison_report(
            runs,
            samples_cap=args.samples,
            timestamp_iso=ts_iso,
            commit=get_git_commit(),
            benchmark_class=args.benchmark_class,
        )
        out_md = run_dir / f"comparison_{ts}.md"
        out_md.write_text(md, encoding="utf-8")
        print(md)
        print(f"\nComparison report written to: {out_md}", file=sys.stderr)
    except Exception as exc:
        print(f"Error generating comparison report: {exc}", file=sys.stderr)
        import traceback

        traceback.print_exc(file=sys.stderr)
    print(f"Per-model JSON under: {run_dir}", file=sys.stderr)

    # Non-zero if any pytest run failed
    if any(code_by_model.get(m, 0) != 0 for m in models):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
