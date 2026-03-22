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


ANALYSIS_QUALITY_JUDGE_PROMPT = """You are evaluating a fact-checking analysis system.

The system was given CLAIMS and SOURCES, and produced an ANALYSIS RESULT.
Your job is to judge if the analysis is correct and well-reasoned.

CLAIMS:
{claims}

SOURCES:
{sources}

ANALYSIS RESULT:
- Verdict: {verdict}
- Score: {score}/100
- Explanation: {explanation}
- Confidence: {confidence}

EXPECTED VERDICT (one of these is acceptable):
{expected_verdicts}

Evaluate the analysis on three dimensions:

1. VERDICT CORRECTNESS: Is the verdict reasonable given the evidence in the sources?
   - The verdict should match what the sources actually say
   - Consider: Do sources support, contradict, or provide mixed evidence?

2. REASONING QUALITY: Does the explanation correctly interpret the sources?
   - Are sources cited or referenced appropriately?
   - Is the reasoning logical and based on the evidence?
   - Are there any misinterpretations of the source content?

3. SCORE ALIGNMENT: Is the numerical score consistent with the verdict?
   - true/mostly_true should have scores 70-100
   - mixed should have scores 40-70
   - mostly_false/false should have scores 0-40
   - unverifiable typically 40-60

Return a JSON object:
{{
  "pass": true or false,
  "reason": "Brief explanation of the judgment",
  "verdict_correct": true or false,
  "reasoning_sound": true or false,
  "score_aligned": true or false,
  "issues": ["list of specific issues found, if any"]
}}

A test passes if:
- verdict_correct is true (verdict matches expected options)
- reasoning_sound is true (explanation makes sense given sources)
- score_aligned is true (score matches verdict range)

Be fair but rigorous. Minor phrasing differences are OK, but logical errors or misinterpretations should fail."""


async def judge_analysis_quality(
    claims: list[str],
    sources: list[dict],
    analysis_result: dict,
    expected_verdicts: list[str],
) -> dict:
    """
    Use GPT-4o to judge whether the analysis is correct and well-reasoned.

    Args:
        claims: The claims that were analyzed
        sources: The sources used for analysis
        analysis_result: The result from analyze_evidence()
        expected_verdicts: List of acceptable verdicts (e.g., ["true", "mostly_true"])

    Returns:
        dict with keys: pass, reason, verdict_correct, reasoning_sound, score_aligned, issues
    """
    claims_text = "\n".join(f"- {c}" for c in claims)
    sources_text = "\n\n".join(
        f"Source {i+1}: {s.get('title', 'Untitled')}\n  URL: {s.get('url', '')}\n  Content: {s.get('content', '')[:800]}"
        for i, s in enumerate(sources)
    )

    prompt = ANALYSIS_QUALITY_JUDGE_PROMPT.format(
        claims=claims_text,
        sources=sources_text,
        verdict=analysis_result.get("verdict", "unknown"),
        score=analysis_result.get("score", 0),
        explanation=analysis_result.get("explanation", "No explanation"),
        confidence=analysis_result.get("confidence", "unknown"),
        expected_verdicts=", ".join(expected_verdicts),
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
        "verdict_correct": result.get("verdict_correct", False),
        "reasoning_sound": result.get("reasoning_sound", False),
        "score_aligned": result.get("score_aligned", False),
        "issues": result.get("issues", []),
    }


E2E_QUALITY_JUDGE_PROMPT = """You are evaluating an end-to-end fact-checking system.

The system was given INPUT TEXT and produced a FACT CHECK RESULT.
Your job is to judge if the entire pipeline produced a correct and reasonable result.

INPUT TEXT:
{input_text}

FACT CHECK RESULT:
- Extracted Claims: {claims}
- Verdict: {verdict}
- Score: {score}/100
- Explanation: {explanation}
- Number of Sources Found: {source_count}

EXPECTED BEHAVIOR:
- Expected Verdicts (one of these is acceptable): {expected_verdicts}
- Description: {description}

Evaluate the end-to-end result on four dimensions:

1. CLAIM EXTRACTION: Were the right claims extracted from the input?
   - Factual claims should be extracted
   - Opinions and subjective statements should NOT be extracted
   - If input is pure opinion, no claims should be extracted

2. VERDICT CORRECTNESS: Is the final verdict reasonable?
   - Does it match one of the expected verdicts?
   - Is it consistent with what a reasonable fact-checker would conclude?

3. SCORE ALIGNMENT: Is the numerical score consistent with the verdict?
   - true/mostly_true should have scores 70-100
   - mixed should have scores 40-70
   - mostly_false/false should have scores 0-40
   - unverifiable typically 40-60

4. EXPLANATION QUALITY: Is the explanation helpful and accurate?
   - Does it explain why the verdict was given?
   - Is it clear and understandable?

Return a JSON object:
{{
  "pass": true or false,
  "reason": "Brief explanation of the judgment",
  "claims_correct": true or false,
  "verdict_correct": true or false,
  "score_aligned": true or false,
  "explanation_quality": "good", "acceptable", or "poor",
  "issues": ["list of specific issues found, if any"]
}}

A test passes if:
- claims_correct is true (appropriate claims were extracted)
- verdict_correct is true (verdict matches expected options)
- score_aligned is true (score matches verdict range)
- explanation_quality is "good" or "acceptable"

Be fair but rigorous. The system should produce sensible fact-check results."""


async def judge_e2e_quality(
    input_text: str,
    result: dict,
    expected_verdicts: list[str],
    description: str,
) -> dict:
    """
    Use GPT-4o to judge whether the end-to-end fact-check result is correct.

    Args:
        input_text: The original text that was fact-checked
        result: The FactCheckResponse as a dict
        expected_verdicts: List of acceptable verdicts
        description: Description of what the test case is checking

    Returns:
        dict with keys: pass, reason, claims_correct, verdict_correct,
                       score_aligned, explanation_quality, issues
    """
    prompt = E2E_QUALITY_JUDGE_PROMPT.format(
        input_text=input_text,
        claims="\n".join(f"- {c}" for c in result.get("claims", [])) if result.get("claims") else "(no claims extracted)",
        verdict=result.get("verdict", "unknown"),
        score=result.get("score", 0),
        explanation=result.get("explanation", "No explanation"),
        source_count=len(result.get("sources", [])),
        expected_verdicts=", ".join(expected_verdicts),
        description=description,
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

    result_json = json.loads(resp.choices[0].message.content)

    return {
        "pass": result_json.get("pass", False),
        "reason": result_json.get("reason", "No reason provided"),
        "claims_correct": result_json.get("claims_correct", False),
        "verdict_correct": result_json.get("verdict_correct", False),
        "score_aligned": result_json.get("score_aligned", False),
        "explanation_quality": result_json.get("explanation_quality", "poor"),
        "issues": result_json.get("issues", []),
    }
