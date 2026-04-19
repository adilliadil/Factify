"""Evals for the evidence analysis stage."""

import pytest
from unittest.mock import AsyncMock
from conftest import load_dataset, make_llm_response
from judges import judge_analysis_quality
from backend.llm import analyze_evidence


class TestAnalysisUnit:
    """Unit tests for analyze_evidence() - mocked LLM, tests parsing logic."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dataset = load_dataset("analysis")

    def _get_case(self, case_id: str) -> dict:
        return next(c for c in self.dataset if c["id"] == case_id)

    @pytest.mark.asyncio
    async def test_true_claim_scores_high(self, mock_llm_client):
        """Well-established facts with supporting sources should score high."""
        case = self._get_case("clearly_true_claim")

        mock_response = {
            "score": 95,
            "verdict": "true",
            "tldr": "Supported by multiple scientific sources.",
            "explanation": "NASA and Britannica confirm Earth orbits the Sun.",
            "confidence": "high",
            "confidence_reason": "Multiple authoritative sources agree",
            "claim_verdicts": [{"claim": case["claims"][0], "verdict": "supported"}],
            "source_stances": [
                {"url": s["url"], "stance": "supporting"} for s in case["sources"]
            ],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        assert result["verdict"] in case["expected_verdicts"], \
            f"Expected verdict in {case['expected_verdicts']}, got {result['verdict']}"
        min_score, max_score = case["expected_score_range"]
        assert min_score <= result["score"] <= max_score, \
            f"Expected score in [{min_score}, {max_score}], got {result['score']}"

    @pytest.mark.asyncio
    async def test_false_claim_scores_low(self, mock_llm_client):
        """Debunked claims with contradicting sources should score low."""
        case = self._get_case("clearly_false_claim")

        mock_response = {
            "score": 10,
            "verdict": "false",
            "tldr": "Contradicts scientific consensus.",
            "explanation": "Multiple sources confirm Earth is spherical, not flat.",
            "confidence": "high",
            "confidence_reason": "Overwhelming scientific evidence",
            "claim_verdicts": [{"claim": case["claims"][0], "verdict": "contradicted"}],
            "source_stances": [
                {"url": s["url"], "stance": "contradicting"} for s in case["sources"]
            ],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        assert result["verdict"] in case["expected_verdicts"], \
            f"Expected verdict in {case['expected_verdicts']}, got {result['verdict']}"
        min_score, max_score = case["expected_score_range"]
        assert min_score <= result["score"] <= max_score, \
            f"Expected score in [{min_score}, {max_score}], got {result['score']}"

    @pytest.mark.asyncio
    async def test_mixed_evidence_returns_mixed_verdict(self, mock_llm_client):
        """Claims with both supporting and contradicting evidence should return mixed."""
        case = self._get_case("mixed_evidence_claim")

        mock_response = {
            "score": 55,
            "verdict": "mixed",
            "tldr": "Evidence is mixed on health effects.",
            "explanation": "Some benefits noted but also risks mentioned.",
            "confidence": "medium",
            "confidence_reason": "Sources present conflicting views",
            "claim_verdicts": [{"claim": case["claims"][0], "verdict": "mixed"}],
            "source_stances": [
                {"url": case["sources"][0]["url"], "stance": "supporting"},
                {"url": case["sources"][1]["url"], "stance": "contradicting"},
            ],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        assert result["verdict"] in case["expected_verdicts"], \
            f"Expected verdict in {case['expected_verdicts']}, got {result['verdict']}"

    @pytest.mark.asyncio
    async def test_returns_required_fields(self, mock_llm_client):
        """Analysis result should contain all required fields."""
        case = self._get_case("clearly_true_claim")

        mock_response = {
            "score": 90,
            "verdict": "true",
            "tldr": "Test summary",
            "explanation": "Test explanation",
            "confidence": "high",
            "confidence_reason": "Test reason",
            "claim_verdicts": [{"claim": case["claims"][0], "verdict": "supported"}],
            "source_stances": [],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        required_fields = ["score", "verdict", "explanation", "confidence", "claim_verdicts"]
        for field in required_fields:
            assert field in result, f"Missing required field: {field}"

    @pytest.mark.asyncio
    async def test_sanitizes_invalid_verdict(self, mock_llm_client):
        """Should sanitize invalid verdicts to 'unverifiable'."""
        case = self._get_case("clearly_true_claim")

        mock_response = {
            "score": 50,
            "verdict": "invalid_verdict",  # Invalid
            "explanation": "Test",
            "confidence": "medium",
            "claim_verdicts": [],
            "source_stances": [],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        valid_verdicts = {"false", "mostly_false", "mixed", "mostly_true", "true", "unverifiable"}
        assert result["verdict"] in valid_verdicts, \
            f"Verdict should be sanitized to valid value, got {result['verdict']}"

    @pytest.mark.asyncio
    async def test_clamps_score_to_valid_range(self, mock_llm_client):
        """Score should be clamped to 0-100 range."""
        case = self._get_case("clearly_true_claim")

        mock_response = {
            "score": 150,  # Out of range
            "verdict": "true",
            "explanation": "Test",
            "confidence": "high",
            "claim_verdicts": [],
            "source_stances": [],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        assert 0 <= result["score"] <= 100, \
            f"Score should be clamped to 0-100, got {result['score']}"

    @pytest.mark.asyncio
    async def test_null_score_does_not_crash(self, mock_llm_client):
        """Grok/Azure sometimes returns ``\"score\": null``; int(null) would raise before store."""
        case = self._get_case("clearly_true_claim")

        mock_response = {
            "score": None,
            "verdict": "true",
            "tldr": "Ok.",
            "explanation": "Test",
            "confidence": "high",
            "claim_verdicts": [{"claim": case["claims"][0], "verdict": "supported"}],
            "source_stances": [],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        assert result["score"] == 50

    @pytest.mark.asyncio
    async def test_string_score_parsed(self, mock_llm_client):
        case = self._get_case("clearly_true_claim")

        mock_response = {
            "score": "88",
            "verdict": "true",
            "tldr": "Ok.",
            "explanation": "Test",
            "confidence": "high",
            "claim_verdicts": [{"claim": case["claims"][0], "verdict": "supported"}],
            "source_stances": [],
        }
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(mock_response)
        )

        result = await analyze_evidence(case["claims"], case["sources"])

        assert result["score"] == 88


class TestAnalysisQuality:
    """Quality tests for analysis - real LLM calls, tests verdict and reasoning quality."""

    pytestmark = pytest.mark.live_api

    @pytest.fixture(autouse=True)
    def setup(self):
        self.golden_dataset = load_dataset("analysis_quality_golden")

    def _get_case(self, case_id: str) -> dict:
        return next(c for c in self.golden_dataset if c["id"] == case_id)

    @pytest.mark.asyncio
    async def test_clear_true_scientific(self):
        """Well-established scientific fact should be verified as true."""
        case = self._get_case("clear_true_scientific")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_clear_false_myth(self):
        """Common myth should be identified as false."""
        case = self._get_case("clear_false_myth")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_mixed_health_claim(self):
        """Health claim with mixed evidence should return mixed verdict."""
        case = self._get_case("mixed_health_claim")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_unverifiable_obscure(self):
        """Claim that sources don't directly address should be unverifiable."""
        case = self._get_case("unverifiable_obscure")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_statistics_verified(self):
        """Statistical claim with confirming data should be true."""
        case = self._get_case("statistics_verified")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_nuanced_health_vitamin(self):
        """Nuanced health claim should reflect the caveats in sources."""
        case = self._get_case("nuanced_health_vitamin")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_historical_fact_verified(self):
        """Clear historical fact should be verified as true."""
        case = self._get_case("historical_fact_verified")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_contradicted_outdated(self):
        """Outdated claim that is now false should be identified."""
        case = self._get_case("contradicted_outdated")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_partial_truth_nutrition(self):
        """Oversimplified nutrition claim should reflect partial truth."""
        case = self._get_case("partial_truth_nutrition")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_recent_scientific_consensus(self):
        """Recent scientific consensus should be verified as true."""
        case = self._get_case("recent_scientific_consensus")

        result = await analyze_evidence(case["claims"], case["sources"])
        judgment = await judge_analysis_quality(
            claims=case["claims"],
            sources=case["sources"],
            analysis_result=result,
            expected_verdicts=case["expected_verdicts"],
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"
