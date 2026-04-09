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


def test_accuracy_empty():
    assert br.accuracy([]) == 0.0


def test_accuracy_and_within_one():
    rows = [
        {"correct": True, "within_one": True},
        {"correct": False, "within_one": True},
    ]
    assert br.accuracy(rows) == 50.0
    assert br.within_one_accuracy(rows) == 100.0


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


def test_score_distribution_single_row():
    rows = [{"label": "l", "score": 10, "correct": True}]
    dist = br.score_distribution(rows)
    assert dist["l"]["std"] == 0.0


def test_build_structured_results_merges_pass_fail_and_stored():
    pass_fail = {
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
        },
    }
    arm_a, _, _ = br.build_structured_results(pass_fail, result_data, sample_lookup)
    assert len(arm_a) == 1
    assert arm_a[0]["actual_verdict"] == "true"
    assert arm_a[0]["correct"] is True


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
            "within_one": True,
        },
    ]
    text = br.format_report([], arm_b, [])
    assert "Benchmark Report" in text
    assert "gpt-4o-mini" in text
    assert "Overall Accuracy" in text
    config.reset()


def test_write_reports_writes_txt_and_json(tmp_path, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "k")
    monkeypatch.setenv("LLM_MODEL", "m")
    from backend.config import config

    config.reset()
    monkeypatch.setattr(br, "REPORTS_DIR", tmp_path)
    p = br.write_reports([], [], [])
    assert p.suffix == ".txt"
    assert (tmp_path / "benchmark_results.json").is_file()
    data = json.loads((tmp_path / "benchmark_results.json").read_text())
    assert data["model"] == "m"
    config.reset()
