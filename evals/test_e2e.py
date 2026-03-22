"""End-to-end evals for the full fact-checking pipeline."""

import pytest
from unittest.mock import AsyncMock
from conftest import make_llm_response, load_search_fixture
from backend.pipeline import fact_check
from backend.models import FactCheckResponse


class TestE2EPipeline:
    """End-to-end tests for fact_check() function."""

    @pytest.mark.asyncio
    async def test_true_statement_scores_high(self, mock_llm_client, mock_tavily_client):
        """A clearly true statement should result in a high score."""
        input_text = "The Earth orbits the Sun."

        # Mock claim extraction
        mock_llm_client.chat.completions.create = AsyncMock(
            side_effect=[
                # First call: claim extraction
                make_llm_response({"claims": ["The Earth orbits the Sun."]}),
                # Second call: analysis
                make_llm_response({
                    "score": 95,
                    "verdict": "true",
                    "tldr": "Supported by scientific consensus.",
                    "explanation": "Multiple authoritative sources confirm this.",
                    "confidence": "high",
                    "confidence_reason": "Well-established scientific fact",
                    "claim_verdicts": [{"claim": "The Earth orbits the Sun.", "verdict": "supported"}],
                    "source_stances": [{"url": "https://nasa.gov/earth", "stance": "supporting"}],
                }),
            ]
        )

        # Mock search
        fixture = load_search_fixture("earth_sun_orbit")
        mock_tavily_client.search = AsyncMock(return_value=fixture)

        result = await fact_check(input_text)

        assert isinstance(result, FactCheckResponse)
        assert result.score >= 70, f"True statement should score high, got {result.score}"
        assert result.verdict in ["true", "mostly_true"], f"Expected true/mostly_true, got {result.verdict}"

    @pytest.mark.asyncio
    async def test_false_statement_scores_low(self, mock_llm_client, mock_tavily_client):
        """A clearly false statement should result in a low score."""
        input_text = "The Earth is flat."

        mock_llm_client.chat.completions.create = AsyncMock(
            side_effect=[
                make_llm_response({"claims": ["The Earth is flat."]}),
                make_llm_response({
                    "score": 5,
                    "verdict": "false",
                    "tldr": "Contradicts all scientific evidence.",
                    "explanation": "This claim is thoroughly debunked.",
                    "confidence": "high",
                    "confidence_reason": "Overwhelming contrary evidence",
                    "claim_verdicts": [{"claim": "The Earth is flat.", "verdict": "contradicted"}],
                    "source_stances": [{"url": "https://nasa.gov/earth", "stance": "contradicting"}],
                }),
            ]
        )

        fixture = load_search_fixture("flat_earth")
        mock_tavily_client.search = AsyncMock(return_value=fixture)

        result = await fact_check(input_text)

        assert result.score <= 30, f"False statement should score low, got {result.score}"
        assert result.verdict in ["false", "mostly_false"], f"Expected false/mostly_false, got {result.verdict}"

    @pytest.mark.asyncio
    async def test_opinion_returns_no_claims(self, mock_llm_client, mock_tavily_client):
        """Pure opinion text should result in no claims extracted."""
        input_text = "Chocolate ice cream is the best."

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": []})
        )

        result = await fact_check(input_text)

        assert result.claims == [], "Opinion should have no claims"
        assert result.verdict == "unverifiable"

    @pytest.mark.asyncio
    async def test_no_sources_returns_unverifiable(self, mock_llm_client, mock_tavily_client):
        """When no sources are found, should return unverifiable."""
        input_text = "Some obscure claim."

        mock_llm_client.chat.completions.create = AsyncMock(
            return_value=make_llm_response({"claims": ["Some obscure claim."]})
        )

        # Return empty search results
        mock_tavily_client.search = AsyncMock(return_value={"results": []})

        result = await fact_check(input_text)

        assert result.verdict == "unverifiable"
        assert result.sources == []

    @pytest.mark.asyncio
    async def test_response_has_required_structure(self, mock_llm_client, mock_tavily_client):
        """Response should have all required fields populated."""
        input_text = "Water boils at 100 degrees Celsius."

        mock_llm_client.chat.completions.create = AsyncMock(
            side_effect=[
                make_llm_response({"claims": ["Water boils at 100 degrees Celsius."]}),
                make_llm_response({
                    "score": 90,
                    "verdict": "true",
                    "tldr": "Scientifically accurate.",
                    "explanation": "Standard boiling point at sea level.",
                    "confidence": "high",
                    "confidence_reason": "Well-established chemistry",
                    "claim_verdicts": [{"claim": "Water boils at 100 degrees Celsius.", "verdict": "supported"}],
                    "source_stances": [{"url": "https://example.com", "stance": "supporting"}],
                }),
            ]
        )

        fixture = load_search_fixture("earth_sun_orbit")  # Reuse fixture for structure test
        mock_tavily_client.search = AsyncMock(return_value=fixture)

        result = await fact_check(input_text)

        # Check required fields
        assert result.original_text == input_text
        assert isinstance(result.claims, list)
        assert isinstance(result.score, int)
        assert result.verdict is not None
        assert result.explanation is not None
        assert isinstance(result.sources, list)

    @pytest.mark.asyncio
    async def test_multiple_claims_aggregated(self, mock_llm_client, mock_tavily_client):
        """Multiple claims should be extracted and analyzed together."""
        input_text = "The Earth is round. Water is wet."

        mock_llm_client.chat.completions.create = AsyncMock(
            side_effect=[
                make_llm_response({"claims": ["The Earth is round.", "Water is wet."]}),
                make_llm_response({
                    "score": 85,
                    "verdict": "mostly_true",
                    "tldr": "Both claims are generally supported.",
                    "explanation": "Standard scientific facts.",
                    "confidence": "high",
                    "confidence_reason": "Multiple sources agree",
                    "claim_verdicts": [
                        {"claim": "The Earth is round.", "verdict": "supported"},
                        {"claim": "Water is wet.", "verdict": "supported"},
                    ],
                    "source_stances": [],
                }),
            ]
        )

        fixture = load_search_fixture("earth_sun_orbit")
        mock_tavily_client.search = AsyncMock(return_value=fixture)

        result = await fact_check(input_text)

        assert len(result.claims) == 2, f"Expected 2 claims, got {len(result.claims)}"
