"""Dataset-agnostic benchmark evals with four-arm design.

Auto-discovers all benchmark_*.json files in evals/datasets/ and runs:
  Arm 0 — eval-only analyze_claim_baseline() with claim only
  Arm A — analyze_evidence() with gold evidence (skipped if no gold_evidence)
  Arm B — search_claim() + analyze_evidence() with retrieved evidence
  Arm C — full fact_check() pipeline

Reports are auto-generated at session end (see conftest.py hooks).
"""

import pytest
from unittest.mock import patch
from conftest import analyze_claim_baseline, load_all_benchmark_samples, store_benchmark_result
from backend.llm import analyze_evidence
from backend.pipeline import fact_check
from tavily_cache import cached_search_claim

ALL_SAMPLES = load_all_benchmark_samples()
GOLD_SAMPLES = [(ds, s) for ds, s in ALL_SAMPLES if s.get("gold_evidence")]


@pytest.mark.benchmark
class TestBaselineAnalysis:
    """Arm 0 — bare LLM claim-only baseline (parametric knowledge only)."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "dataset_name,sample",
        ALL_SAMPLES,
        ids=[f"{ds}-{s['id']}" for ds, s in ALL_SAMPLES],
    )
    async def test_baseline(self, dataset_name, sample):
        result = await analyze_claim_baseline(sample["claim"])

        store_benchmark_result("arm_baseline", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result["verdict"],
            "score": result["score"],
            "confidence": result.get("confidence", "unknown"),
            "confidence_reason": result.get("confidence_reason", ""),
            "tldr": result.get("tldr", ""),
            "explanation": result.get("explanation", ""),
            "claim_verdicts": result.get("claim_verdicts", []),
            "source_stances": result.get("source_stances", {}),
        })

        assert result["verdict"] in sample["expected_verdicts"], (
            f"[{dataset_name}/{sample['id']}] "
            f"Expected verdict in {sample['expected_verdicts']}, got {result['verdict']}"
        )


@pytest.mark.benchmark
class TestGoldEvidenceAnalysis:
    """Arm A — analyze_evidence() with gold evidence.
    Only runs for samples that include gold_evidence (e.g. AVeriTeC)."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "dataset_name,sample",
        GOLD_SAMPLES,
        ids=[f"{ds}-{s['id']}" for ds, s in GOLD_SAMPLES],
    )
    async def test_gold_evidence(self, dataset_name, sample):
        result = await analyze_evidence([sample["claim"]], sample["gold_evidence"])

        store_benchmark_result("arm_a", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result["verdict"],
            "score": result["score"],
            "confidence": result.get("confidence", "unknown"),
            "confidence_reason": result.get("confidence_reason", ""),
            "tldr": result.get("tldr", ""),
            "explanation": result.get("explanation", ""),
            "claim_verdicts": result.get("claim_verdicts", []),
            "source_stances": result.get("source_stances", {}),
            "sources": sample["gold_evidence"],
        })

        assert result["verdict"] in sample["expected_verdicts"], (
            f"[{dataset_name}/{sample['id']}] "
            f"Expected verdict in {sample['expected_verdicts']}, got {result['verdict']}"
        )

        lo, hi = sample["expected_score_range"]
        assert lo <= result["score"] <= hi, (
            f"[{dataset_name}/{sample['id']}] "
            f"Expected score in [{lo}, {hi}], got {result['score']}"
        )


@pytest.mark.benchmark
class TestSearchedEvidenceAnalysis:
    """Arm B — search_claim() + analyze_evidence() with Tavily-retrieved evidence."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "dataset_name,sample",
        ALL_SAMPLES,
        ids=[f"{ds}-{s['id']}" for ds, s in ALL_SAMPLES],
    )
    async def test_searched_evidence(self, dataset_name, sample):
        sources = await cached_search_claim(sample["claim"])

        if not sources:
            pytest.skip(f"No search results for: {sample['claim'][:80]}")

        result = await analyze_evidence([sample["claim"]], sources)

        store_benchmark_result("arm_b", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result["verdict"],
            "score": result["score"],
            "confidence": result.get("confidence", "unknown"),
            "confidence_reason": result.get("confidence_reason", ""),
            "tldr": result.get("tldr", ""),
            "explanation": result.get("explanation", ""),
            "claim_verdicts": result.get("claim_verdicts", []),
            "source_stances": result.get("source_stances", {}),
            "sources": sources,
        })

        assert result["verdict"] in sample["expected_verdicts"], (
            f"[{dataset_name}/{sample['id']}] "
            f"Expected verdict in {sample['expected_verdicts']}, got {result['verdict']}"
        )


@pytest.mark.benchmark
class TestFullPipeline:
    """Arm C — full fact_check() pipeline (extract_claims + search + analyze)."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "dataset_name,sample",
        ALL_SAMPLES,
        ids=[f"{ds}-{s['id']}" for ds, s in ALL_SAMPLES],
    )
    async def test_full_pipeline(self, dataset_name, sample):
        with patch("backend.pipeline.search_claim", side_effect=cached_search_claim):
            result = await fact_check(sample["claim"])

        store_benchmark_result("arm_c", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result.verdict,
            "score": result.score,
            "confidence": result.confidence,
            "confidence_reason": result.confidence_reason,
            "tldr": result.tldr,
            "explanation": result.explanation,
            "claim_verdicts": [
                {"claim": claim.text, "verdict": claim.verdict}
                for claim in result.claims
            ],
            "source_stances": {
                source.url: source.stance
                for source in result.sources
            },
            "claims": [claim.model_dump() for claim in result.claims],
            "sources": [source.model_dump() for source in result.sources],
        })

        assert result.verdict in sample["expected_verdicts"], (
            f"[{dataset_name}/{sample['id']}] "
            f"Expected verdict in {sample['expected_verdicts']}, got {result.verdict}"
        )
