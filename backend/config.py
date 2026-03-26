"""Centralized configuration loaded from environment variables.

Usage:
    from backend.config import config

    config.llm.model      # "gpt-4o-mini"
    config.llm.api_key    # from OPENAI_API_KEY
    config.search.api_key  # from TAVILY_API_KEY
    config.judge.model     # from JUDGE_MODEL
"""

import os
from dataclasses import dataclass


class ConfigError(Exception):
    """Raised when a required environment variable is missing or empty."""


def _require_env(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise ConfigError(f"Missing required environment variable: {name}")
    return val


@dataclass(frozen=True)
class LLMConfig:
    api_key: str
    model: str = "gpt-4o-mini"
    base_url: str = "https://api.openai.com/v1"


@dataclass(frozen=True)
class SearchConfig:
    api_key: str


@dataclass(frozen=True)
class JudgeConfig:
    api_key: str
    model: str = "deepseek-ai/DeepSeek-V3-0324"
    base_url: str = "https://api.tokenfactory.nebius.com/v1/"


class _Config:
    """Lazy-loaded configuration singleton. Each property validates and
    caches its config on first access so missing env vars surface
    immediately at the point of use."""

    def __init__(self) -> None:
        self._llm: LLMConfig | None = None
        self._search: SearchConfig | None = None
        self._judge: JudgeConfig | None = None

    @property
    def llm(self) -> LLMConfig:
        if self._llm is None:
            self._llm = LLMConfig(
                api_key=_require_env("OPENAI_API_KEY"),
                model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
                base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1"),
            )
        return self._llm

    @property
    def search(self) -> SearchConfig:
        if self._search is None:
            self._search = SearchConfig(api_key=_require_env("TAVILY_API_KEY"))
        return self._search

    @property
    def judge(self) -> JudgeConfig:
        if self._judge is None:
            self._judge = JudgeConfig(
                api_key=_require_env("NEBIUS_API_KEY"),
                model=os.getenv("JUDGE_MODEL", "deepseek-ai/DeepSeek-V3-0324"),
                base_url=os.getenv("JUDGE_BASE_URL", "https://api.tokenfactory.nebius.com/v1/"),
            )
        return self._judge

    def reset(self) -> None:
        """Clear cached configs so they are re-read from env on next access."""
        self._llm = None
        self._search = None
        self._judge = None


config = _Config()
