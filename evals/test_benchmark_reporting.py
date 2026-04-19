"""Unit tests for `benchmark_reporting` helpers and report output."""

import json
from pathlib import Path
from unittest.mock import patch

import pytest

import benchmark_reporting as br


def test_verdict_index_and_within_one():
    assert br.verdict_index("true") == 4
    assert br.verdict_index("bogus") == -1
    assert br.within_one_level("mostly_true", ["true"])
    assert not br.within_one_level("false", ["true"])


def test_failure_reasons_verdict_only():
    r = {
        "actual_verdict": "false",
        "expected_verdicts": ["true", "mostly_true"],
        "score": 50,
        "expected_score_range": [25, 75],
    }
    out = br.failure_reasons(r, check_score_range=False)
    assert "verdict" in out[0]
    assert "score" not in "".join(out)


def test_failure_reasons_score_arm_a():
    r = {
        "actual_verdict": "mostly_false",
        "expected_verdicts": ["mostly_false", "mixed"],
        "score": 85,
        "expected_score_range": [25, 75],
    }
    out = br.failure_reasons(r, check_score_range=True)
    assert any("score" in x for x in out)
    assert not any("verdict" in x for x in out)


def test_accuracy_empty():
    assert br.accuracy([]) == 0.0


def test_accuracy_and_within_one():
    rows = [
        {"correct": True, "within_one": True},
        {"correct": False, "within_one": True},
    ]
    assert br.accuracy(rows) == 50.0
    assert br.within_one_accuracy(rows) == 100.0


def test_verdict_accuracy_ignores_score_failures():
    rows = [
        {"verdict_correct": True, "correct": False},  # score-only failure
        {"verdict_correct": True, "correct": True},
        {"verdict_correct": False, "correct": False},
    ]
    assert br.verdict_accuracy(rows) == pytest.approx(66.7, abs=0.1)
    assert br.accuracy(rows) == pytest.approx(33.3, abs=0.1)


def test_accuracy_excludes_request_failures():
    rows = [
        {"correct": True, "within_one": True, "request_failed": False},
        {"correct": False, "within_one": False, "request_failed": True},
        {"correct": False, "within_one": False, "request_failed": False},
    ]
    assert br.accuracy(rows) == 50.0
    assert br.within_one_accuracy(rows) == 50.0


def test_request_failure_rate():
    rows = [
        {"request_failed": True},
        {"request_failed": False},
        {"request_failed": True},
    ]
    assert br.request_failure_rate(rows) == pytest.approx(100 * 2 / 3)
    assert br.request_failure_rate([]) == 0.0


def test_by_dataset_and_by_label():
    rows = [
        {"dataset": "a", "label": "x", "correct": True},
        {"dataset": "a", "label": "y", "correct": False},
    ]
    assert list(br.by_dataset(rows)["a"]) == rows
    assert set(br.by_label(rows).keys()) == {"x", "y"}


def test_confidence_calibration():
    rows = [
        {"confidence": "high", "correct": True},
        {"confidence": "high", "correct": False},
    ]
    cal = br.confidence_calibration(rows)
    assert cal["high"]["total"] == 2
    assert cal["high"]["correct"] == 1


def test_confidence_calibration_excludes_request_failures():
    rows = [
        {"confidence": "high", "correct": False, "request_failed": True},
        {"confidence": "high", "correct": True, "request_failed": False},
    ]
    cal = br.confidence_calibration(rows)
    assert cal["high"]["total"] == 1
    assert cal["high"]["correct"] == 1


def test_score_distribution_single_row():
    rows = [{"label": "l", "score": 10, "correct": True}]
    dist = br.score_distribution(rows)
    assert dist["l"]["std"] == 0.0


def test_build_structured_results_merges_pass_fail_and_stored():
    pass_fail = {
        "arm_baseline": [],
        "arm_a": [{"key": "ds-1", "passed": True}],
        "arm_b": [],
        "arm_c": [],
    }
    result_data = {
        "arm_a:ds-1": {"actual_verdict": "true", "score": 80, "confidence": "high"},
    }
    sample_lookup = {
        "ds-1": {
            "dataset": "ds",
            "id": "1",
            "claim": "c",
            "label": "lab",
            "expected_verdicts": ["true"],
            "expected_score_range": [40, 90],
        },
    }
    _, arm_a, _, _ = br.build_structured_results(pass_fail, result_data, sample_lookup)
    assert len(arm_a) == 1
    assert arm_a[0]["actual_verdict"] == "true"
    assert arm_a[0]["correct"] is True
    assert arm_a[0]["verdict_correct"] is True
    assert arm_a[0]["request_failed"] is False
    assert arm_a[0]["expected_score_range"] == [40, 90]


def test_build_structured_results_baseline_arm():
    pass_fail = {
        "arm_baseline": [
            {"key": "ds-1", "passed": True},
            {"key": "ds-2", "passed": False},
        ],
        "arm_a": [],
        "arm_b": [],
        "arm_c": [],
    }
    result_data = {
        "arm_baseline:ds-1": {"actual_verdict": "true", "score": 70, "confidence": "high"},
        "arm_baseline:ds-2": {"actual_verdict": "false", "score": 20, "confidence": "low"},
    }
    sample_lookup = {
        "ds-1": {
            "dataset": "ds", "id": "1", "claim": "c1", "label": "lab",
            "expected_verdicts": ["true"], "expected_score_range": [40, 90],
        },
        "ds-2": {
            "dataset": "ds", "id": "2", "claim": "c2", "label": "lab",
            "expected_verdicts": ["true"], "expected_score_range": [40, 90],
        },
    }
    arm_bl, _, _, _ = br.build_structured_results(pass_fail, result_data, sample_lookup)
    assert len(arm_bl) == 2
    assert arm_bl[0]["verdict_correct"] is True
    assert arm_bl[1]["verdict_correct"] is False


def test_build_structured_results_request_failed_no_stored_result():
    pass_fail = {
        "arm_baseline": [],
        "arm_a": [{"key": "ds-1", "passed": False, "request_failed": True}],
        "arm_b": [],
        "arm_c": [],
    }
    result_data: dict = {}
    sample_lookup = {
        "ds-1": {
            "dataset": "ds",
            "id": "1",
            "claim": "c",
            "label": "lab",
            "expected_verdicts": ["true"],
            "expected_score_range": [40, 90],
        },
    }
    _, arm_a, _, _ = br.build_structured_results(pass_fail, result_data, sample_lookup)
    assert arm_a[0]["request_failed"] is True
    assert arm_a[0]["correct"] is False
    assert arm_a[0]["within_one"] is False
    assert arm_a[0]["actual_verdict"] == "?"


def test_format_report_contains_model_and_sections(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("LLM_MODEL", "gpt-4o-mini")
    from backend.config import config

    config.reset()
    arm_b = [
        {
            "dataset": "ds",
            "id": "1",
            "claim": "",
            "label": "l",
            "expected_verdicts": ["true"],
            "actual_verdict": "true",
            "score": 90,
            "confidence": "high",
            "correct": True,
            "verdict_correct": True,
            "within_one": True,
        },
    ]
    text = br.format_report([], [], arm_b, [])
    assert "Benchmark Report" in text
    assert "gpt-4o-mini" in text
    assert "Overall Accuracy" in text
    assert "Arm 0 (None)" in text
    assert "Request failures" in text
    config.reset()


def test_format_report_failed_samples_shows_reasons(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("LLM_MODEL", "gpt-4o-mini")
    from backend.config import config

    config.reset()
    arm_a = [
        {
            "dataset": "ds",
            "id": "av_001",
            "claim": "c",
            "label": "Cherrypicking",
            "expected_verdicts": ["mixed", "mostly_false"],
            "expected_score_range": [25, 75],
            "actual_verdict": "mostly_false",
            "score": 85,
            "confidence": "high",
            "correct": False,
            "verdict_correct": True,
            "within_one": True,
        },
    ]
    text = br.format_report([], arm_a, [], [])
    assert "Failure reasons" in text
    assert "score: got 85" in text
    assert "[25, 75]" in text
    config.reset()


def test_write_reports_writes_txt_and_json(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("LLM_MODEL", "m")
    from backend.config import config

    config.reset()
    monkeypatch.setattr(br, "REPORTS_DIR", tmp_path)
    p = br.write_reports([], [], [], [])
    assert p.suffix == ".txt"
    assert (tmp_path / "benchmark_results.json").is_file()
    data = json.loads((tmp_path / "benchmark_results.json").read_text())
    assert data["model"] == "m"
    assert "arm_baseline" in data
    config.reset()


def test_write_reports_respects_benchmark_output_file(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("LLM_MODEL", "custom-model")
    custom = tmp_path / "subdir" / "out.json"
    monkeypatch.setenv("BENCHMARK_OUTPUT_FILE", str(custom))
    from backend.config import config

    config.reset()
    monkeypatch.setattr(br, "REPORTS_DIR", tmp_path)
    ret = br.write_reports([], [], [], [])
    assert custom.is_file()
    assert ret == custom
    data = json.loads(custom.read_text())
    assert data["model"] == "custom-model"
    # Multi-model subprocess runs must not create a per-model .txt under REPORTS_DIR
    assert not any(tmp_path.glob("*.txt"))
    monkeypatch.delenv("BENCHMARK_OUTPUT_FILE", raising=False)
    config.reset()


def test_write_reports_skips_txt_when_subprocess_run(tmp_path, monkeypatch):
    """When BENCHMARK_OUTPUT_FILE is set, only JSON is written (no timestamped .txt)."""
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("LLM_MODEL", "m")
    out = tmp_path / "run.json"
    monkeypatch.setenv("BENCHMARK_OUTPUT_FILE", str(out))
    from backend.config import config

    config.reset()
    monkeypatch.setattr(br, "REPORTS_DIR", tmp_path)
    p = br.write_reports([], [], [], [])
    assert p.suffix == ".json"
    assert p == out
    assert not any(tmp_path.glob("*.txt"))
    monkeypatch.delenv("BENCHMARK_OUTPUT_FILE", raising=False)
    config.reset()
