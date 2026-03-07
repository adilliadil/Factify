from backend.llm import extract_claims, analyze_evidence
from backend.search import search_claim
from backend.models import FactCheckResponse, Source


async def fact_check(text: str) -> FactCheckResponse:
    claims = await extract_claims(text)

    if not claims:
        return FactCheckResponse(
            claims=[],
            score=0,
            verdict="unverifiable",
            explanation="No factual claims were detected in the provided text.",
            sources=[],
        )

    all_sources = []
    seen_urls = set()

    for claim in claims:
        results = await search_claim(claim)
        for s in results:
            if s["url"] not in seen_urls:
                seen_urls.add(s["url"])
                all_sources.append(s)

    if not all_sources:
        return FactCheckResponse(
            claims=claims,
            score=50,
            verdict="unverifiable",
            explanation="Unable to retrieve sources to verify the claims.",
            sources=[],
        )

    analysis = await analyze_evidence(claims, all_sources)

    response_sources = [
        Source(title=s["title"], url=s["url"])
        for s in all_sources[:8]
    ]

    return FactCheckResponse(
        claims=claims,
        score=analysis["score"],
        verdict=analysis["verdict"],
        explanation=analysis["explanation"],
        sources=response_sources,
    )
