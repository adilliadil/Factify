"""Unit tests for the benchmark failure audit renderer."""

from scripts import benchmark_failure_audit as audit


def test_build_audit_renders_inputs_outputs_and_evidence(monkeypatch):
    monkeypatch.setattr(
        audit,
        "_load_samples",
        lambda: {
            ("ds", "1"): {
                "gold_evidence": [
                    {
                        "title": "Gold source",
                        "url": "https://example.com/gold",
                        "content": "Direct evidence text.",
                    }
                ]
            }
        },
    )
    monkeypatch.setattr(audit, "_load_cache", lambda: {})

    results = {
        "timestamp": "2026-01-01T00:00:00+00:00",
        "model": "m",
        "commit": "abc123",
        "arm_a": [
            {
                "dataset": "ds",
                "id": "1",
                "claim": "The claim",
                "label": "Supported",
                "expected_verdicts": ["true"],
                "expected_score_range": [60, 100],
                "actual_verdict": "mixed",
                "score": 50,
                "confidence": "medium",
                "correct": False,
                "within_one": True,
                "tldr": "A concise model summary.",
                "explanation": "The model explanation.",
                "confidence_reason": "Partial evidence",
                "claim_verdicts": [],
                "source_stances": {},
            }
        ],
    }

    text = audit.build_audit(results, arms=["arm_a"], limit=None)

    assert "Benchmark Failure Audit" in text
    assert "**Claim:** The claim" in text
    assert "**Actual verdict:** `mixed`" in text
    assert "A concise model summary." in text
    assert "The model explanation." in text
    assert "Partial evidence" in text
    assert "```json\n[]\n```" in text
    assert "```json\n{}\n```" in text
    assert "Gold source" in text


def test_build_audit_derives_source_stances_from_sources(monkeypatch):
    monkeypatch.setattr(audit, "_load_samples", lambda: {})
    monkeypatch.setattr(audit, "_load_cache", lambda: {})

    results = {
        "arm_c": [
            {
                "dataset": "ds",
                "id": "1",
                "claim": "The claim",
                "label": "Supported",
                "expected_verdicts": ["true"],
                "actual_verdict": "false",
                "score": 10,
                "confidence": "high",
                "correct": False,
                "within_one": False,
                "claims": [{"text": "The claim", "verdict": "contradicted"}],
                "sources": [
                    {
                        "title": "Source",
                        "url": "https://example.com",
                        "stance": "contradicting",
                    }
                ],
            }
        ],
    }

    text = audit.build_audit(results, arms=["arm_c"], limit=None)

    assert '"text": "The claim"' in text
    assert '"https://example.com": "contradicting"' in text
