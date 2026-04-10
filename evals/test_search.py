"""Evals for the search stage (Tavily integration)."""

import pytest
from unittest.mock import AsyncMock
from conftest import load_search_fixture, load_dataset
from judges import judge_search_relevance
from backend.search import search_claim


class TestSearchUnit:
    """Unit tests for search_claim() - mocked Tavily, tests wrapper logic."""

    @pytest.mark.asyncio
    async def test_returns_sources_with_required_fields(self, mock_tavily_client):
        """Search results should have title, url, and content."""
        fixture = load_search_fixture("earth_sun_orbit")

        mock_tavily_client.search = AsyncMock(return_value=fixture)

        results = await search_claim("The Earth orbits the Sun")

        assert len(results) > 0, "Should return at least one result"
        for source in results:
            assert "title" in source, "Source must have title"
            assert "url" in source, "Source must have url"
            assert "content" in source, "Source must have content"

    @pytest.mark.asyncio
    async def test_handles_empty_results(self, mock_tavily_client):
        """Should handle empty search results gracefully."""
        fixture = load_search_fixture("empty_results")

        mock_tavily_client.search = AsyncMock(return_value=fixture)

        results = await search_claim("obscure claim with no results")

        assert results == [], "Should return empty list for no results"

    @pytest.mark.asyncio
    async def test_handles_api_error(self, mock_tavily_client, caplog):
        """Should return empty list on API error and log the failure."""
        import logging

        mock_tavily_client.search = AsyncMock(side_effect=Exception("API Error"))

        caplog.set_level(logging.ERROR)
        results = await search_claim("any claim")

        assert results == [], "Should return empty list on error"
        assert "Tavily search failed" in caplog.text

    @pytest.mark.asyncio
    async def test_respects_max_results(self, mock_tavily_client):
        """Should pass max_results to the API."""
        fixture = load_search_fixture("earth_sun_orbit")

        mock_tavily_client.search = AsyncMock(return_value=fixture)

        await search_claim("The Earth orbits the Sun", max_results=3)

        # Verify the API was called with correct max_results
        call_kwargs = mock_tavily_client.search.call_args.kwargs
        assert call_kwargs.get("max_results") == 3, "Should pass max_results to API"

    @pytest.mark.asyncio
    async def test_adds_fact_check_to_query(self, mock_tavily_client):
        """Should append 'evidence fact check' to the search query."""
        fixture = load_search_fixture("earth_sun_orbit")

        mock_tavily_client.search = AsyncMock(return_value=fixture)

        await search_claim("The Earth orbits the Sun")

        call_kwargs = mock_tavily_client.search.call_args.kwargs
        query = call_kwargs.get("query", "")
        assert "evidence fact check" in query, "Should append fact check context to query"


class TestSearchQuality:
    """Quality tests for search - real Tavily calls, tests actual search relevance."""

    pytestmark = pytest.mark.live_api

    @pytest.fixture(autouse=True)
    def setup(self):
        self.golden_dataset = load_dataset("search_quality_golden")

    def _get_case(self, case_id: str) -> dict:
        return next(c for c in self.golden_dataset if c["id"] == case_id)

    @pytest.mark.asyncio
    async def test_well_known_scientific_fact(self):
        """Well-established scientific fact should return relevant sources."""
        case = self._get_case("well_known_scientific_fact")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_health_claim(self):
        """Health claim should return relevant medical sources."""
        case = self._get_case("health_claim")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_statistical_claim(self):
        """Statistical claim should return sources with data."""
        case = self._get_case("statistical_claim")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_historical_fact(self):
        """Historical fact should return relevant historical sources."""
        case = self._get_case("historical_fact")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_disputed_myth(self):
        """Common myth should return debunking sources."""
        case = self._get_case("disputed_myth")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_recent_scientific(self):
        """Recent scientific topic should return relevant sources."""
        case = self._get_case("recent_scientific")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_precise_scientific_constant(self):
        """Scientific constant should return physics/science sources."""
        case = self._get_case("precise_scientific_constant")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_nutrition_claim(self):
        """Nutrition claim should return health sources."""
        case = self._get_case("nutrition_claim")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_technology_claim(self):
        """Technology claim should return relevant tech sources."""
        case = self._get_case("technology_claim")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"

    @pytest.mark.asyncio
    async def test_environmental_claim(self):
        """Environmental claim should return scientific sources."""
        case = self._get_case("environmental_claim")

        sources = await search_claim(case["claim"])
        judgment = await judge_search_relevance(
            claim=case["claim"],
            sources=sources,
        )

        assert judgment["pass"], f"[{case['id']}] {judgment['reason']}"
