"""Dataset-agnostic benchmark evals with four-arm design.

Auto-discovers all benchmark_*.json files in evals/datasets/ and runs:
  Arm 0 — analyze_evidence() with NO evidence (LLM baseline / parametric knowledge)
  Arm A — analyze_evidence() with gold evidence (skipped if no gold_evidence)
  Arm B — search_claim() + analyze_evidence() with retrieved evidence
  Arm C — full fact_check() pipeline

Reports are auto-generated at session end (see conftest.py hooks).
"""

import pytest
from conftest import load_all_benchmark_samples, store_benchmark_result
from backend.llm import analyze_evidence
from backend.search import search_claim
from backend.pipeline import fact_check

ALL_SAMPLES = load_all_benchmark_samples()
GOLD_SAMPLES = [(ds, s) for ds, s in ALL_SAMPLES if s.get("gold_evidence")]


@pytest.mark.benchmark
class TestBaselineAnalysis:
    """Arm 0 — analyze_evidence() with NO evidence (parametric knowledge only).
    Measures LLM baseline without any external sources."""

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "dataset_name,sample",
        ALL_SAMPLES,
        ids=[f"{ds}-{s['id']}" for ds, s in ALL_SAMPLES],
    )
    async def test_baseline(self, dataset_name, sample):
        result = await analyze_evidence([sample["claim"]], [])

        store_benchmark_result("arm_baseline", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result["verdict"],
            "score": result["score"],
            "confidence": result.get("confidence", "unknown"),
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
        sources = await search_claim(sample["claim"])

        if not sources:
            pytest.skip(f"No search results for: {sample['claim'][:80]}")

        result = await analyze_evidence([sample["claim"]], sources)

        store_benchmark_result("arm_b", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result["verdict"],
            "score": result["score"],
            "confidence": result.get("confidence", "unknown"),
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
        result = await fact_check(sample["claim"])

        store_benchmark_result("arm_c", f"{dataset_name}-{sample['id']}", {
            "actual_verdict": result.verdict,
            "score": result.score,
            "confidence": result.confidence,
        })

        assert result.verdict in sample["expected_verdicts"], (
            f"[{dataset_name}/{sample['id']}] "
            f"Expected verdict in {sample['expected_verdicts']}, got {result.verdict}"
        )
