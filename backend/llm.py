import json
from openai import AsyncOpenAI

client: AsyncOpenAI | None = None


def get_client() -> AsyncOpenAI:
    global client
    if client is None:
        client = AsyncOpenAI()
    return client


CLAIM_EXTRACTION_PROMPT = """Extract all distinct factual claims from the text below.

A factual claim is any statement that asserts something as true or false about the world,
including health claims, statistics, cause-effect statements, historical facts, and scientific assertions.

Rules:
- Return a JSON object with a "claims" key containing an array of claim strings.
- Each claim should be a self-contained sentence.
- Only exclude purely subjective opinions (e.g. "chocolate is the best flavor") and future predictions with no factual basis.
- If in doubt, include the claim.
- If the entire text is a single claim, return it as-is in the array.

Text:
{text}"""

EVIDENCE_ANALYSIS_PROMPT = """You are a rigorous fact-checking assistant.

Evaluate whether the provided sources support or contradict each claim.
Only use the information present in the sources. Do not invent or assume facts.

Claims:
{claims}

Sources:
{sources}

Return a JSON object with exactly these fields:
{{
  "score": <integer 0-100>,
  "verdict": "<one of: false, mostly_false, mixed, mostly_true, true, unverifiable>",
  "tldr": "<single punchy sentence, max 15 words, stating the core conclusion — be direct and opinionated, e.g. 'This contradicts medical consensus.' or 'Supported by multiple scientific sources.'>",
  "explanation": "<2-3 sentence explanation citing specific sources>",
  "claim_verdicts": [
    {{
      "claim": "<the exact claim text>",
      "verdict": "<one of: supported, contradicted, mixed, unverifiable>"
    }}
  ]
}}

There must be exactly one entry in "claim_verdicts" for each claim listed above, in the same order.

Score guide:
- 0-20: False (sources clearly contradict the claims)
- 21-40: Mostly false (sources mostly contradict with minor support)
- 41-60: Mixed (sources both support and contradict)
- 61-80: Mostly true (sources mostly support with minor caveats)
- 81-100: True (sources clearly support the claims)

If the sources don't contain enough information to evaluate, use verdict "unverifiable" with score 50."""


async def extract_claims(text: str) -> list[str]:
    resp = await get_client().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You extract factual claims from text. Always respond with valid JSON."},
            {"role": "user", "content": CLAIM_EXTRACTION_PROMPT.format(text=text)},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    raw = resp.choices[0].message.content
    parsed = json.loads(raw)

    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict):
        for key in ("claims", "factual_claims", "results"):
            if key in parsed and isinstance(parsed[key], list):
                return parsed[key]
        vals = list(parsed.values())
        if vals and isinstance(vals[0], list):
            return vals[0]
    return []


async def analyze_evidence(claims: list[str], sources: list[dict]) -> dict:
    sources_text = "\n\n".join(
        f"Source {i+1}: {s.get('title', 'Untitled')}\nURL: {s.get('url', '')}\nContent: {s.get('content', '')[:2000]}"
        for i, s in enumerate(sources)
    )
    claims_text = "\n".join(f"- {c}" for c in claims)

    resp = await get_client().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a fact-checking assistant. Always respond with valid JSON."},
            {"role": "user", "content": EVIDENCE_ANALYSIS_PROMPT.format(claims=claims_text, sources=sources_text)},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )

    raw = resp.choices[0].message.content
    result = json.loads(raw)

    score = max(0, min(100, int(result.get("score", 50))))
    verdict = result.get("verdict", "unverifiable")
    valid_verdicts = {"false", "mostly_false", "mixed", "mostly_true", "true", "unverifiable"}
    if verdict not in valid_verdicts:
        verdict = "unverifiable"

    claim_verdicts = result.get("claim_verdicts", [])
    valid_claim_verdicts = {"supported", "contradicted", "mixed", "unverifiable"}
    sanitized_verdicts = []
    for cv in claim_verdicts:
        v = cv.get("verdict", "unverifiable")
        if v not in valid_claim_verdicts:
            v = "unverifiable"
        sanitized_verdicts.append({
            "claim": cv.get("claim", ""),
            "verdict": v,
        })

    return {
        "score": score,
        "verdict": verdict,
        "tldr": result.get("tldr", ""),
        "explanation": result.get("explanation", "Unable to determine."),
        "claim_verdicts": sanitized_verdicts,
    }
