from tavily import AsyncTavilyClient
import os

client: AsyncTavilyClient | None = None


def get_client() -> AsyncTavilyClient:
    global client
    if client is None:
        client = AsyncTavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    return client


async def search_claim(claim: str, max_results: int = 5) -> list[dict]:
    """Search for evidence about a claim using Tavily. Returns list of source dicts."""
    try:
        response = await get_client().search(
            query=f"{claim} evidence fact check",
            max_results=max_results,
            include_answer=False,
        )
    except Exception:
        return []

    sources = []
    for result in response.get("results", []):
        sources.append({
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "content": result.get("content", ""),
        })
    return sources
