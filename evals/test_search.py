"""Evals for the search stage (Tavily integration)."""

import pytest
from unittest.mock import AsyncMock
from conftest import load_search_fixture
from backend.search import search_claim


class TestSearch:
    """Test cases for search_claim() function."""

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
    async def test_handles_api_error(self, mock_tavily_client):
        """Should return empty list on API error."""
        mock_tavily_client.search = AsyncMock(side_effect=Exception("API Error"))

        results = await search_claim("any claim")

        assert results == [], "Should return empty list on error"

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
