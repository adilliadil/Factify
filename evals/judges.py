"""LLM-as-judge functions for evaluating extraction and analysis quality."""

import json
from openai import AsyncOpenAI

# Use a separate client for judging to allow different model
_judge_client: AsyncOpenAI | None = None


def get_judge_client() -> AsyncOpenAI:
    global _judge_client
    if _judge_client is None:
        _judge_client = AsyncOpenAI()
    return _judge_client


CLAIM_EXTRACTION_JUDGE_PROMPT = """You are evaluating a claim extraction system.

Your task is to determine if the ACTUAL CLAIMS adequately capture the EXPECTED CLAIMS.

INPUT TEXT:
{input_text}

EXPECTED CLAIMS (what should be extracted):
{expected_claims}

ACTUAL CLAIMS (what the system extracted):
{actual_claims}

SHOULD EXCLUDE (opinions/speculation that should NOT be extracted):
{should_exclude}

Evaluation criteria:
1. Coverage: Are all expected claims present in the actual output? (Paraphrasing is OK)
2. Precision: Are there spurious claims that shouldn't be there (opinions, speculation)?
3. Self-contained: Is each claim understandable on its own?

Return a JSON object:
{{
  "pass": true or false,
  "reason": "Brief explanation of the judgment",
  "coverage_score": 0.0 to 1.0 (what fraction of expected claims are covered),
  "missing_claims": ["list of expected claims not found in actual"],
  "spurious_claims": ["list of actual claims that are opinions or shouldn't be there"]
}}

A test passes if:
- coverage_score >= 0.8 (most expected claims are captured)
- No items from SHOULD EXCLUDE appear in actual claims
- spurious_claims is empty or contains only minor issues

Be lenient with paraphrasing - "The Earth is approximately 4.5 billion years old" covers "The Earth is 4.5 billion years old".
Be strict about opinions - subjective statements like "X is the best" should not be extracted."""


async def judge_claim_extraction(
    input_text: str,
    expected_claims: list[str],
    actual_claims: list[str],
    should_exclude: list[str] | None = None,
) -> dict:
    """
    Use GPT-4o to judge whether claim extraction was successful.

    Args:
        input_text: The original text that was processed
        expected_claims: Claims that should have been extracted
        actual_claims: Claims that were actually extracted
        should_exclude: Phrases/claims that should NOT have been extracted (opinions, etc.)

    Returns:
        dict with keys: pass, reason, coverage_score, missing_claims, spurious_claims
    """
    should_exclude = should_exclude or []

    prompt = CLAIM_EXTRACTION_JUDGE_PROMPT.format(
        input_text=input_text,
        expected_claims="\n".join(f"- {c}" for c in expected_claims) if expected_claims else "(none expected)",
        actual_claims="\n".join(f"- {c}" for c in actual_claims) if actual_claims else "(none extracted)",
        should_exclude="\n".join(f"- {c}" for c in should_exclude) if should_exclude else "(none specified)",
    )

    resp = await get_judge_client().chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a precise evaluator. Always respond with valid JSON."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    result = json.loads(resp.choices[0].message.content)

    # Ensure required fields exist with defaults
    return {
        "pass": result.get("pass", False),
        "reason": result.get("reason", "No reason provided"),
        "coverage_score": result.get("coverage_score", 0.0),
        "missing_claims": result.get("missing_claims", []),
        "spurious_claims": result.get("spurious_claims", []),
    }


SEARCH_RELEVANCE_JUDGE_PROMPT = """You are evaluating search results for a fact-checking system.

Your task is to determine if the search results are useful for verifying or refuting a claim.

CLAIM TO VERIFY:
{claim}

SEARCH RESULTS:
{sources}

Evaluate the search results on two dimensions:

1. RELEVANCE: Do the sources actually relate to the claim?
   - 1.0 = All sources directly address the claim
   - 0.5 = Some sources are relevant, some are off-topic
   - 0.0 = Sources are completely unrelated

2. COVERAGE: Do the sources provide enough information to verify or refute the claim?
   - 1.0 = Sources contain clear evidence to confirm or deny the claim
   - 0.5 = Sources provide partial information, but not conclusive
   - 0.0 = Sources don't help verify the claim at all

Return a JSON object:
{{
  "pass": true or false,
  "reason": "Brief explanation of the judgment",
  "relevance_score": 0.0 to 1.0,
  "coverage_score": 0.0 to 1.0,
  "relevant_source_count": number of sources that are relevant,
  "irrelevant_sources": ["URLs of sources that are not relevant"]
}}

A test passes if:
- relevance_score >= 0.6 (at least 60% of sources relate to the claim)
- coverage_score >= 0.5 (sources provide some verification info)

Note: If zero sources are returned, that's a failure (relevance_score = 0, coverage_score = 0)."""


async def judge_search_relevance(
    claim: str,
    sources: list[dict],
) -> dict:
    """
    Use GPT-4o to judge whether search results are relevant and useful.

    Args:
        claim: The claim that was searched for
        sources: List of source dicts with title, url, content

    Returns:
        dict with keys: pass, reason, relevance_score, coverage_score,
                       relevant_source_count, irrelevant_sources
    """
    if not sources:
        return {
            "pass": False,
            "reason": "No sources returned from search",
            "relevance_score": 0.0,
            "coverage_score": 0.0,
            "relevant_source_count": 0,
            "irrelevant_sources": [],
        }

    sources_text = "\n\n".join(
        f"Source {i+1}:\n  Title: {s.get('title', 'Untitled')}\n  URL: {s.get('url', '')}\n  Content: {s.get('content', '')[:500]}..."
        for i, s in enumerate(sources)
    )

    prompt = SEARCH_RELEVANCE_JUDGE_PROMPT.format(
        claim=claim,
        sources=sources_text,
    )

    resp = await get_judge_client().chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a precise evaluator. Always respond with valid JSON."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    result = json.loads(resp.choices[0].message.content)

    return {
        "pass": result.get("pass", False),
        "reason": result.get("reason", "No reason provided"),
        "relevance_score": result.get("relevance_score", 0.0),
        "coverage_score": result.get("coverage_score", 0.0),
        "relevant_source_count": result.get("relevant_source_count", 0),
        "irrelevant_sources": result.get("irrelevant_sources", []),
    }
