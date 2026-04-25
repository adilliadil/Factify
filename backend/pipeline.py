import asyncio
import json
import logging
from typing import AsyncGenerator

from backend.llm import extract_claims, analyze_evidence
from backend.search import search_claim
from backend.models import FactCheckResponse, Source, ClaimResult

logger = logging.getLogger(__name__)


async def fact_check_stream(text: str) -> AsyncGenerator[str, None]:
    """Yields SSE-formatted events as the pipeline progresses."""

    def sse(event: str, data: dict) -> str:
        return f"event: {event}\ndata: {json.dumps(data)}\n\n"

    yield sse("step", {"step": "extracting"})
    claims = await extract_claims(text)

    if not claims:
        logger.info("fact_check_stream: no claims extracted (input length=%d)", len(text))
        result = FactCheckResponse(
            original_text=text,
            claims=[],
            score=0,
            verdict="unverifiable",
            tldr="No factual claims detected.",
            explanation="No factual claims were detected in the provided text.",
            confidence="low",
            confidence_reason="No claims to evaluate",
            sources=[],
        )
        yield sse("result", result.model_dump())
        return

    yield sse("step", {"step": "searching", "claims_found": len(claims)})

    all_sources = []
    seen_urls: set[str] = set()
    search_results = await asyncio.gather(*[search_claim(claim) for claim in claims])
    for results in search_results:
        for s in results:
            if s["url"] not in seen_urls:
                seen_urls.add(s["url"])
                all_sources.append(s)

    if not all_sources:
        logger.warning(
            "fact_check_stream: no sources after search (claims=%d)",
            len(claims),
        )
        result = FactCheckResponse(
            original_text=text,
            claims=[ClaimResult(text=c, verdict="unverifiable") for c in claims],
            score=50,
            verdict="unverifiable",
            tldr="Unable to find sources to verify.",
            explanation="Unable to retrieve sources to verify the claims.",
            confidence="low",
            confidence_reason="No sources found",
            sources=[],
        )
        yield sse("result", result.model_dump())
        return

    yield sse("step", {"step": "analyzing", "sources_found": len(all_sources)})

    analysis = await analyze_evidence(claims, all_sources)

    claim_verdicts_map = {
        cv["claim"]: cv["verdict"]
        for cv in analysis.get("claim_verdicts", [])
    }
    claim_results = []
    for c in claims:
        verdict = claim_verdicts_map.get(c, "unverifiable")
        claim_results.append(ClaimResult(text=c, verdict=verdict))

    source_stances = analysis.get("source_stances", {})
    response_sources = [
        Source(title=s["title"], url=s["url"], stance=source_stances.get(s["url"], "neutral"))
        for s in all_sources[:8]
    ]

    result = FactCheckResponse(
        original_text=text,
        claims=claim_results,
        score=analysis["score"],
        verdict=analysis["verdict"],
        tldr=analysis.get("tldr", ""),
        explanation=analysis["explanation"],
        confidence=analysis.get("confidence", "low"),
        confidence_reason=analysis.get("confidence_reason", ""),
        sources=response_sources,
    )
    logger.info(
        "fact_check_stream: done verdict=%s score=%s sources=%d",
        result.verdict,
        result.score,
        len(response_sources),
    )
    yield sse("result", result.model_dump())


async def fact_check(text: str) -> FactCheckResponse:
    claims = await extract_claims(text)

    if not claims:
        logger.info("fact_check: no claims extracted (input length=%d)", len(text))
        return FactCheckResponse(
            original_text=text,
            claims=[],
            score=0,
            verdict="unverifiable",
            tldr="No factual claims detected.",
            explanation="No factual claims were detected in the provided text.",
            confidence="low",
            confidence_reason="No claims to evaluate",
            sources=[],
        )

    all_sources = []
    seen_urls = set()

    search_results = await asyncio.gather(*[search_claim(claim) for claim in claims])
    for results in search_results:
        for s in results:
            if s["url"] not in seen_urls:
                seen_urls.add(s["url"])
                all_sources.append(s)

    if not all_sources:
        logger.warning("fact_check: no sources after search (claims=%d)", len(claims))
        return FactCheckResponse(
            original_text=text,
            claims=[ClaimResult(text=c, verdict="unverifiable") for c in claims],
            score=50,
            verdict="unverifiable",
            tldr="Unable to find sources to verify.",
            explanation="Unable to retrieve sources to verify the claims.",
            confidence="low",
            confidence_reason="No sources found",
            sources=[],
        )

    analysis = await analyze_evidence(claims, all_sources)

    claim_verdicts_map = {
        cv["claim"]: cv["verdict"]
        for cv in analysis.get("claim_verdicts", [])
    }
    claim_results = []
    for c in claims:
        verdict = claim_verdicts_map.get(c, "unverifiable")
        claim_results.append(ClaimResult(text=c, verdict=verdict))

    source_stances = analysis.get("source_stances", {})
    response_sources = [
        Source(title=s["title"], url=s["url"], stance=source_stances.get(s["url"], "neutral"))
        for s in all_sources[:8]
    ]

    out = FactCheckResponse(
        original_text=text,
        claims=claim_results,
        score=analysis["score"],
        verdict=analysis["verdict"],
        tldr=analysis.get("tldr", ""),
        explanation=analysis["explanation"],
        confidence=analysis.get("confidence", "low"),
        confidence_reason=analysis.get("confidence_reason", ""),
        sources=response_sources,
    )
    logger.info(
        "fact_check: done verdict=%s score=%s sources=%d",
        out.verdict,
        out.score,
        len(response_sources),
    )
    return out
