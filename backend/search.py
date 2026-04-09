import logging

from tavily import AsyncTavilyClient

from backend.config import config

logger = logging.getLogger(__name__)

client: AsyncTavilyClient | None = None


def get_client() -> AsyncTavilyClient:
    global client
    if client is None:
        client = AsyncTavilyClient(api_key=config.search.api_key)
    return client


async def search_claim(claim: str, max_results: int = 5) -> list[dict]:
    """Search for evidence about a claim using Tavily. Returns list of source dicts."""
    try:
        response = await get_client().search(
            query=f"{claim} evidence fact check",
            max_results=max_results,
            include_answer=False,
            search_depth="advanced",
        )
    except Exception:
        logger.exception("Tavily search failed for claim (truncated): %s", claim[:120])
        return []

    sources = []
    for result in response.get("results", []):
        sources.append({
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "content": result.get("content", ""),
        })
    return sources
