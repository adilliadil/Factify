import json
import logging
import re
from typing import TypedDict

from openai import NOT_GIVEN

from backend.config import config
from backend.llm_clients import LLMClient, create_client

logger = logging.getLogger(__name__)

client: LLMClient | None = None

# Reasoning models reject an explicit temperature parameter entirely.
_NO_TEMPERATURE_PATTERN = re.compile(
    r"^(o\d|o\d-|gpt-5\.5|gpt-5\.5-)", re.IGNORECASE
)


def _temperature(model: str):
    """Return temperature=0 for standard models, NOT_GIVEN for reasoning models."""
    if _NO_TEMPERATURE_PATTERN.match(model):
        return NOT_GIVEN
    return 0


def get_client() -> LLMClient:
    global client
    if client is None:
        client = create_client(config.llm)
    return client


class ClaimVerdictItem(TypedDict):
    claim: str
    verdict: str


class AnalysisResult(TypedDict):
    score: int
    verdict: str
    tldr: str
    explanation: str
    confidence: str
    confidence_reason: str
    claim_verdicts: list[ClaimVerdictItem]
    source_stances: dict[str, str]


CLAIM_EXTRACTION_PROMPT = """Extract only the check-worthy factual claims from the text below.

A check-worthy factual claim is a statement that:
- Asserts something as objectively true or false about the world, AND
- The general public would care whether it is true or false (e.g. health claims, statistics, historical facts, scientific assertions, cause-effect statements made by public figures).

Exclude ALL of the following:
- Subjective opinions and preferences (e.g. "this is the best policy", "chocolate is delicious")
- Future predictions with no factual basis (e.g. "it will rain tomorrow")
- Trivial or unimportant facts nobody would bother checking (e.g. "we had lunch yesterday", "next Tuesday is a weekday")
- Greetings, filler, and conversational sentences with no factual content
- Purely emotional or rhetorical statements

Rules:
- Return a JSON object with a "claims" key containing an array of claim strings.
- Each claim should be a self-contained sentence.
- If no check-worthy claims exist, return an empty array: {{"claims": []}}.
- If the entire text is a single check-worthy claim, return it as-is in the array.

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
  "confidence": "<one of: high, medium, low>",
  "confidence_reason": "<short phrase explaining why, max 12 words, e.g. 'Multiple independent sources agree' or 'Only one tangentially relevant source found'>",
  "claim_verdicts": [
    {{
      "claim": "<the exact claim text>",
      "verdict": "<one of: supported, contradicted, mixed, unverifiable>"
    }}
  ],
  "source_stances": [
    {{
      "url": "<the exact source URL>",
      "stance": "<one of: supporting, contradicting, neutral>"
    }}
  ]
}}

There must be exactly one entry in "claim_verdicts" for each claim listed above, in the same order.
There must be exactly one entry in "source_stances" for each source listed above, using the exact URL.

Score guide:
- 0-20: False (sources clearly contradict the claims)
- 21-40: Mostly false (sources mostly contradict with minor support)
- 41-60: Mixed (sources both support and contradict)
- 61-80: Mostly true (sources mostly support with minor caveats)
- 81-100: True (sources clearly support the claims)

Confidence guide:
- high: 3+ independent, authoritative sources agree; claims are directly addressed
- medium: 2+ sources with partial coverage; some claims only indirectly addressed
- low: few or weak sources; claims mostly unaddressed or sources conflict heavily

If the sources don't contain enough information to evaluate, use verdict "unverifiable" with score 50."""


async def extract_claims(text: str) -> list[str]:
    logger.debug("extract_claims: input length=%d model=%s", len(text), config.llm.model)
    resp = await get_client().chat.completions.create(
        model=config.llm.model,
        messages=[
            {"role": "system", "content": "You extract factual claims from text. Always respond with valid JSON."},
            {"role": "user", "content": CLAIM_EXTRACTION_PROMPT.format(text=text)},
        ],
        response_format={"type": "json_object"},
        temperature=_temperature(config.llm.model),
    )

    raw = resp.choices[0].message.content
    if raw is None:
        logger.warning("extract_claims: empty message content from LLM")
        return []
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        logger.warning("extract_claims: invalid JSON from LLM (first 200 chars): %r", raw[:200])
        return []

    if isinstance(parsed, list):
        out = parsed
    elif isinstance(parsed, dict):
        for key in ("claims", "factual_claims", "results"):
            if key in parsed and isinstance(parsed[key], list):
                out = parsed[key]
                break
        else:
            vals = list(parsed.values())
            out = vals[0] if vals and isinstance(vals[0], list) else []
    else:
        out = []

    logger.info("extract_claims: extracted %d claim(s)", len(out))
    return out


async def analyze_evidence(claims: list[str], sources: list[dict]) -> AnalysisResult:
    logger.debug(
        "analyze_evidence: claims=%d sources=%d model=%s",
        len(claims),
        len(sources),
        config.llm.model,
    )
    sources_text = "\n\n".join(
        f"Source {i+1}: {s.get('title', 'Untitled')}\nURL: {s.get('url', '')}\nContent: {s.get('content', '')}"
        for i, s in enumerate(sources)
    )
    claims_text = "\n".join(f"- {c}" for c in claims)

    resp = await get_client().chat.completions.create(
        model=config.llm.model,
        messages=[
            {"role": "system", "content": "You are a fact-checking assistant. Always respond with valid JSON."},
            {"role": "user", "content": EVIDENCE_ANALYSIS_PROMPT.format(claims=claims_text, sources=sources_text)},
        ],
        response_format={"type": "json_object"},
        temperature=_temperature(config.llm.model),
    )

    raw = resp.choices[0].message.content
    if raw is None:
        logger.warning("analyze_evidence: empty message content from LLM")
        return _fallback_analysis()

    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        logger.warning("analyze_evidence: invalid JSON (first 200 chars): %r", raw[:200])
        return _fallback_analysis()

    if not isinstance(result, dict):
        logger.warning("analyze_evidence: expected JSON object, got %s", type(result).__name__)
        return _fallback_analysis()

    score = max(0, min(100, int(result.get("score", 50))))
    verdict = result.get("verdict", "unverifiable")
    valid_verdicts = {"false", "mostly_false", "mixed", "mostly_true", "true", "unverifiable"}
    if verdict not in valid_verdicts:
        logger.warning("analyze_evidence: invalid verdict %r, defaulting to unverifiable", verdict)
        verdict = "unverifiable"

    claim_verdicts = result.get("claim_verdicts", [])
    valid_claim_verdicts = {"supported", "contradicted", "mixed", "unverifiable"}
    sanitized_verdicts: list[ClaimVerdictItem] = []
    for cv in claim_verdicts:
        if not isinstance(cv, dict):
            continue
        v = cv.get("verdict", "unverifiable")
        if v not in valid_claim_verdicts:
            v = "unverifiable"
        sanitized_verdicts.append({
            "claim": cv.get("claim", ""),
            "verdict": v,
        })

    confidence = result.get("confidence", "low")
    if confidence not in {"high", "medium", "low"}:
        confidence = "low"

    valid_stances = {"supporting", "contradicting", "neutral"}
    source_stances: dict[str, str] = {}
    for ss in result.get("source_stances", []):
        if not isinstance(ss, dict):
            continue
        stance = ss.get("stance", "neutral")
        if stance not in valid_stances:
            stance = "neutral"
        source_stances[ss.get("url", "")] = stance

    logger.info(
        "analyze_evidence: verdict=%s score=%d confidence=%s",
        verdict,
        score,
        confidence,
    )

    return {
        "score": score,
        "verdict": verdict,
        "tldr": result.get("tldr", ""),
        "explanation": result.get("explanation", "Unable to determine."),
        "confidence": confidence,
        "confidence_reason": result.get("confidence_reason", ""),
        "claim_verdicts": sanitized_verdicts,
        "source_stances": source_stances,
    }


def _fallback_analysis() -> AnalysisResult:
    return {
        "score": 50,
        "verdict": "unverifiable",
        "tldr": "",
        "explanation": "Unable to determine.",
        "confidence": "low",
        "confidence_reason": "Model returned invalid or empty JSON",
        "claim_verdicts": [],
        "source_stances": {},
    }
