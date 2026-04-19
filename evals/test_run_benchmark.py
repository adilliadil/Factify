"""Tests for ``evals.run_benchmark`` CLI and comparison reporting."""

import importlib
import json
from pathlib import Path
from unittest.mock import patch

import pytest

import benchmark_reporting as br
from conftest import load_all_benchmark_samples


def test_parse_args_models_and_samples():
    from evals.run_benchmark import parse_args

    ns = parse_args(["--models", "gpt-nano", "kimi", "--samples", "5", "--class", "TestGoldEvidenceAnalysis"])
    assert ns.models == ["gpt-nano", "kimi"]
    assert ns.samples == 5
    assert ns.benchmark_class == "TestGoldEvidenceAnalysis"


def test_build_pytest_cmd_includes_k_when_class_set():
    from evals.run_benchmark import _build_pytest_cmd

    cmd = _build_pytest_cmd("TestGoldEvidenceAnalysis")
    assert "-k" in cmd
    assert cmd[cmd.index("-k") + 1] == "TestGoldEvidenceAnalysis"
    assert "test_benchmark.py" in cmd
    assert "pytest.ini" in cmd


def test_build_pytest_cmd_no_k_when_class_none():
    from evals.run_benchmark import _build_pytest_cmd

    cmd = _build_pytest_cmd(None)
    assert "-k" not in cmd


def test_safe_filename_fragment():
    from evals.run_benchmark import _safe_filename_fragment

    assert _safe_filename_fragment("gpt-nano") == "gpt-nano"
    assert ".." not in _safe_filename_fragment("a/b:c")


def test_load_dotenv_for_cli_runs_without_error():
    from evals.run_benchmark import _load_dotenv_for_cli

    _load_dotenv_for_cli()


def test_format_comparison_report_structure():
    runs = {
        "m1": {
            "arm_a": [
                {
                    "dataset": "ds",
                    "id": "1",
                    "label": "Supported",
                    "expected_verdicts": ["true"],
                    "actual_verdict": "true",
                    "score": 90,
                    "confidence": "high",
                    "correct": True,
                    "within_one": True,
                },
            ],
            "arm_b": [],
            "arm_c": [],
            "wall_time_s": 10.0,
            "pytest_exit_code": 0,
        },
        "m2": {
            "arm_a": [
                {
                    "dataset": "ds",
                    "id": "1",
                    "label": "Supported",
                    "expected_verdicts": ["true"],
                    "actual_verdict": "false",
                    "score": 20,
                    "confidence": "low",
                    "correct": False,
                    "within_one": False,
                },
            ],
            "arm_b": [],
            "arm_c": [],
            "wall_time_s": 20.0,
            "pytest_exit_code": 1,
        },
    }
    md = br.format_comparison_report(
        runs,
        samples_cap=1,
        timestamp_iso="2026-01-01 00:00:00 UTC",
        commit="abc",
        benchmark_class="TestGoldEvidenceAnalysis",
    )
    assert "# Benchmark comparison report" in md
    assert "Timing" in md
    assert "`m1`" in md and "`m2`" in md
    assert "10.00s" in md or "10.0" in md
    assert "Accuracy by arm" in md
    assert "Request failures (% by arm)" in md
    assert "Incorrect verdicts (counts" in md
    assert "Request failures (counts)" in md
    assert "Per-label accuracy" in md


def test_benchmark_max_samples_caps_rows(monkeypatch):
    full = load_all_benchmark_samples()
    cap = min(2, len(full))
    if cap < 1:
        pytest.skip("No benchmark samples in datasets")

    monkeypatch.setenv("BENCHMARK_MAX_SAMPLES", str(cap))
    import evals.test_benchmark as tb

    importlib.reload(tb)
    try:
        assert len(tb.ALL_SAMPLES) == cap
        assert len(tb.GOLD_SAMPLES) <= cap
    finally:
        monkeypatch.delenv("BENCHMARK_MAX_SAMPLES", raising=False)
        importlib.reload(tb)


def test_run_one_model_sets_env(tmp_path, monkeypatch):
    from evals.run_benchmark import EVAL_ROOT, _run_one_model

    out = tmp_path / "out.json"
    calls: list[dict] = []

    def fake_run(cmd, env, cwd, capture_output, text):
        calls.append({"cmd": cmd, "env": dict(env), "cwd": cwd})
        out.write_text(
            json.dumps(
                {
                    "timestamp": "t",
                    "model": env.get("LLM_MODEL"),
                    "commit": "x",
                    "arm_a": [],
                    "arm_b": [],
                    "arm_c": [],
                }
            ),
            encoding="utf-8",
        )
        class R:
            returncode = 0

        return R()

    monkeypatch.setattr("evals.run_benchmark.subprocess.run", fake_run)
    model, code, wall = _run_one_model(
        "gpt-nano",
        out,
        samples=3,
        benchmark_class="TestGoldEvidenceAnalysis",
    )
    assert model == "gpt-nano"
    assert code == 0
    assert wall >= 0
    assert len(calls) == 1
    assert calls[0]["env"]["LLM_MODEL"] == "gpt-nano"
    assert calls[0]["env"]["BENCHMARK_OUTPUT_FILE"] == str(out)
    assert calls[0]["env"]["BENCHMARK_MAX_SAMPLES"] == "3"
    assert "-k" in calls[0]["cmd"]
    assert calls[0]["cwd"] == str(EVAL_ROOT)


def test_main_writes_comparison_md(tmp_path, monkeypatch):
    """``main()`` writes a single Markdown comparison under ``evals/reports/comparison_<ts>/``."""
    import evals.run_benchmark as rb

    monkeypatch.setattr(rb, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(rb, "_warn_if_not_registry_alias", lambda models: None)

    sample_payload = {
        "arm_a": [
            {
                "dataset": "AVeriTeC",
                "id": "av_001",
                "label": "Supported",
                "expected_verdicts": ["true"],
                "actual_verdict": "true",
                "score": 90,
                "confidence": "high",
                "correct": True,
                "within_one": True,
            },
        ],
        "arm_b": [],
        "arm_c": [],
    }

    def fake_run_one(model, json_out, *, samples, benchmark_class):
        json_out.write_text(
            json.dumps(
                {
                    "timestamp": "t",
                    "model": model,
                    "commit": "x",
                    **sample_payload,
                }
            ),
            encoding="utf-8",
        )
        return model, 0, 1.0

    monkeypatch.setattr(rb, "_run_one_model", fake_run_one)

    exit_code = rb.main(
        ["--models", "m-a", "m-b", "--samples", "1", "--class", "TestGoldEvidenceAnalysis"]
    )
    assert exit_code == 0

    reports_dir = tmp_path / "evals" / "reports"
    comparison_dirs = sorted(reports_dir.glob("comparison_*"))
    assert len(comparison_dirs) == 1
    md_files = list(comparison_dirs[0].glob("comparison_*.md"))
    assert len(md_files) == 1
    text = md_files[0].read_text(encoding="utf-8")
    assert "# Benchmark comparison report" in text
    assert "`m-a`" in text and "`m-b`" in text
