"""Evals for the claim extraction stage."""

import pytest
from unittest.mock import AsyncMock
from conftest import load_dataset, make_llm_response
from judges import judge_claim_extraction
from backend.llm import extract_claims


class TestClaimExtractionUnit:
    """Unit tests for extract_claims() - mocked LLM, tests parsing logic."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dataset = load_dataset("claims")

    @pytest.mark.asyncio
    async def test_single_factual_claim(self, mock_llm_client):
        """Single clear factual statement should be extracted as-is."""
        case = next(c for c in self.dataset if c["id"] == "single_factual_claim")

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": case["expected_claims"]})
        )

        result = await extract_claims(case["input"])

        assert result == case["expected_claims"], f"Expected {case['expected_claims']}, got {result}"

    @pytest.mark.asyncio
    async def test_multiple_claims(self, mock_llm_client):
        """Multiple factual claims should each be extracted."""
        case = next(c for c in self.dataset if c["id"] == "multiple_claims")

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": case["expected_claims"]})
        )

        result = await extract_claims(case["input"])

        assert len(result) == len(case["expected_claims"]), f"Expected {len(case['expected_claims'])} claims, got {len(result)}"

    @pytest.mark.asyncio
    async def test_opinion_only_returns_empty(self, mock_llm_client):
        """Pure opinion should result in no claims."""
        case = next(c for c in self.dataset if c["id"] == "opinion_only")

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": []})
        )

        result = await extract_claims(case["input"])

        assert result == [], f"Expected no claims for opinion, got {result}"

    @pytest.mark.asyncio
    async def test_trivial_fact_returns_empty(self, mock_llm_client):
        """Trivial unimportant facts should not be extracted as check-worthy."""
        case = next(c for c in self.dataset if c["id"] == "trivial_factual_claim")

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": []})
        )

        result = await extract_claims(case["input"])

        assert result == [], f"Expected no claims for trivial fact, got {result}"

    @pytest.mark.asyncio
    async def test_extracts_historical_claim(self, mock_llm_client):
        """Historical facts should be extracted."""
        case = next(c for c in self.dataset if c["id"] == "historical_claim")

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": case["expected_claims"]})
        )

        result = await extract_claims(case["input"])

        assert len(result) >= 1, "Should extract at least one historical claim"

    @pytest.mark.asyncio
    async def test_handles_empty_response(self, mock_llm_client):
        """Should handle empty or malformed responses gracefully."""
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({})
        )

        result = await extract_claims("Some text")

        assert result == [], "Should return empty list for empty response"

    @pytest.mark.asyncio
    async def test_handles_list_response_format(self, mock_llm_client):
        """Should handle response as direct list (not wrapped in object)."""
        claims = ["Claim 1", "Claim 2"]
        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response(claims)
        )

        result = await extract_claims("Some text")

        assert result == claims, "Should handle list response format"


class TestClaimExtractionQuality:
    """Quality tests for claim extraction - real LLM calls, tests actual behavior."""

    pytestmark = pytest.mark.live_api

    @pytest.fixture(autouse=True)
    def setup(self):
        self.golden_dataset = load_dataset("claim_extraction_golden")

    def _get_case(self, case_id: str) -> dict:
        return next(c for c in self.golden_dataset if c["id"] == case_id)

    @pytest.mark.asyncio
    async def test_single_fact(self):
        """Single clear factual statement should be extracted."""
        case = self._get_case("single_fact")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_opinion_only(self):
        """Pure opinion should not be extracted as a claim."""
        case = self._get_case("opinion_only")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_fact_and_opinion_mixed(self):
        """Should extract facts but reject opinions from mixed text."""
        case = self._get_case("fact_and_opinion_mixed")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_multiple_facts(self):
        """Multiple factual claims should all be extracted."""
        case = self._get_case("multiple_facts")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_health_claim(self):
        """Health-related claims should be extracted for verification."""
        case = self._get_case("health_claim")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_statistical_claim(self):
        """Statistical claims with numbers should be preserved."""
        case = self._get_case("statistical_claim")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_historical_claim(self):
        """Historical facts with dates should be extracted."""
        case = self._get_case("historical_claim")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_cause_effect_claim(self):
        """Causal claims should be extracted."""
        case = self._get_case("cause_effect_claim")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_disputed_but_verifiable(self):
        """Disputed claims should still be extracted (they're verifiable)."""
        case = self._get_case("disputed_but_verifiable")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_future_prediction(self):
        """Speculative predictions should not be extracted."""
        case = self._get_case("future_prediction")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_trivial_fact(self):
        """Trivial unimportant facts should not be extracted as check-worthy."""
        case = self._get_case("trivial_fact")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_complex_paragraph(self):
        """Should extract multiple facts from paragraph, ignoring opinions."""
        case = self._get_case("complex_paragraph")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_quote_with_claim(self):
        """Factual claims within quotes should be extracted."""
        case = self._get_case("quote_with_claim")

        actual_claims = await extract_claims(case["input"])
        judgment = await judge_claim_extraction(
            input_text=case["input"],
            expected_claims=case["expected_claims"],
            actual_claims=actual_claims,
            should_exclude=case.get("should_exclude", []),
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"
