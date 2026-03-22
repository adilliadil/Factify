"""Evals for the claim extraction stage."""

import pytest
from conftest import load_dataset, make_llm_response
from backend.llm import extract_claims


class TestClaimExtraction:
    """Test cases for extract_claims() function."""

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


# Import AsyncMock at module level for use in tests
from unittest.mock import AsyncMock
