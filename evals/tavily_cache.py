"""Eval-only cache for Tavily search results.

Persists results to datasets/tavily_search_cache.json so benchmark runs
don't hit the Tavily API for claims that were already searched.

Cache entries expire after CACHE_TTL_DAYS (default 60).  To manually
invalidate the whole cache, delete the JSON file or call `clear_cache()`.

This module is intentionally isolated from backend/ — it is only used by
the eval harness and has no effect on production search behaviour.
"""

from __future__ import annotations

import hashlib
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

from backend.search import search_claim as _real_search_claim

logger = logging.getLogger(__name__)

CACHE_TTL_DAYS: int = 60
_CACHE_FILE = Path(__file__).parent / "datasets" / "tavily_search_cache.json"


def _normalize_claim(claim: str) -> str:
    """Normalize claim text for stable cache lookup across minor wording variants."""
    text = claim.strip().lower()
    # Normalize common punctuation/quote variants, then remove punctuation.
    text = text.replace("’", "'").replace("`", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _claim_key(claim: str) -> str:
    """Stable cache key: sha256 of normalized claim text."""
    return hashlib.sha256(_normalize_claim(claim).encode()).hexdigest()


def _load_cache() -> dict:
    if _CACHE_FILE.exists():
        try:
            return json.loads(_CACHE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            logger.warning("tavily_cache: could not read cache file, starting fresh")
    return {}


def _save_cache(cache: dict) -> None:
    _CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    _CACHE_FILE.write_text(json.dumps(cache, indent=2))


def _is_fresh(entry: dict, ttl_days: int) -> bool:
    try:
        cached_at = datetime.fromisoformat(entry["cached_at"])
        age = datetime.now(timezone.utc) - cached_at
        return age.days < ttl_days
    except (KeyError, ValueError):
        return False


async def cached_search_claim(
    claim: str,
    max_results: int = 5,
    ttl_days: int = CACHE_TTL_DAYS,
) -> list[dict]:
    """Drop-in replacement for search_claim() that caches results on disk.

    On a cache hit (entry exists and is within ttl_days) the real Tavily
    API is never called.  On a miss the result is fetched, stored, and
    returned as normal.
    """
    key = _claim_key(claim)
    normalized_claim = _normalize_claim(claim)
    cache = _load_cache()

    entry = cache.get(key)
    if entry and _is_fresh(entry, ttl_days):
        logger.debug("tavily_cache: HIT for claim (key=%s…)", key[:12])
        return entry["results"]

    logger.debug("tavily_cache: MISS for claim (key=%s…), fetching from Tavily", key[:12])
    results = await _real_search_claim(claim, max_results=max_results)

    cache[key] = {
        "cached_at": datetime.now(timezone.utc).isoformat(),
        "claim": claim,
        "normalized_claim": normalized_claim,
        "results": results,
    }
    _save_cache(cache)
    return results


def clear_cache() -> None:
    """Remove all cached entries by deleting the cache file."""
    if _CACHE_FILE.exists():
        _CACHE_FILE.unlink()
        logger.info("tavily_cache: cache cleared")
