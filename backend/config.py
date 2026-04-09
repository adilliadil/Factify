"""Centralized configuration loaded from environment variables.

Usage:
    from backend.config import config

    config.llm.model       # "gpt-4o-mini" or a registry alias
    config.llm.api_key     # from OPENAI_API_KEY
    config.models          # dict of registry alias -> ModelConfig (optional Azure models)
    config.search.api_key  # from TAVILY_API_KEY
    config.judge.model     # from JUDGE_MODEL
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Literal

logger = logging.getLogger(__name__)

Provider = Literal["openai", "openai_compatible", "azure", "azure_inference"]


class ConfigError(Exception):
    """Raised when a required environment variable is missing or empty."""


def _require_env(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise ConfigError(f"Missing required environment variable: {name}")
    return val


def _optional_env(*names: str) -> str | None:
    """Return the first non-empty env var from names, else None."""
    for n in names:
        v = os.getenv(n)
        if v:
            return v
    return None


def _parse_provider(name: str, default: Provider) -> Provider:
    raw = (os.getenv(name, default) or default).strip().lower()
    aliases: dict[str, Provider] = {
        "openai": "openai",
        "compatible": "openai_compatible",
        "openai_compatible": "openai_compatible",
        "azure": "azure",
        "azure_openai": "azure",
        "azure_inference": "azure_inference",
        "azure_ai": "azure_inference",
        "inference": "azure_inference",
        "nebius": "openai_compatible",
    }
    if raw not in aliases:
        raise ConfigError(
            f"Invalid {name}: {raw} "
            f"(expected openai, openai_compatible/nebius, azure, azure_inference)"
        )
    out = aliases[raw]
    logger.debug("Resolved %s=%r -> %s", name, raw, out)
    return out


@dataclass(frozen=True)
class ModelConfig:
    """Universal LLM endpoint configuration (pipeline, judge, or registry entries)."""

    provider: Provider
    model: str
    api_key: str
    base_url: str | None = None  # OpenAI-compatible base URL, or full inference URL for azure_inference
    azure_endpoint: str | None = None
    azure_api_version: str | None = None
    api_key_header: str = "api-key"  # for azure_inference (e.g. api-key header)


@dataclass(frozen=True)
class SearchConfig:
    api_key: str


def _build_model_registry() -> dict[str, ModelConfig]:
    """Optional named models from grouped Azure env vars (see .env.example)."""
    out: dict[str, ModelConfig] = {}

    def add_azure_inference(alias: str, url: str, api_key: str, model_name: str) -> None:
        out[alias] = ModelConfig(
            provider="azure_inference",
            model=model_name.strip(),
            api_key=api_key,
            base_url=url,
        )
        logger.info("Model registry: alias %r -> model %r (azure_inference)", alias, model_name.strip())

    azure_url = _optional_env("AZURE_BASE_URL")
    azure_key = _optional_env("AZURE_API_KEY")
    if azure_url and not azure_key:
        logger.warning(
            "AZURE_BASE_URL is set but AZURE_API_KEY is missing; skipping grok/kimi/deepseek-r registry entries"
        )
    if azure_key and not azure_url:
        logger.warning(
            "AZURE_API_KEY is set but AZURE_BASE_URL is missing; skipping grok/kimi/deepseek-r registry entries"
        )
    if azure_url and azure_key:
        for alias, env_name in (
            ("grok-reasoning", "GROK_REASONING_MODEL_NAME"),
            ("grok-nonreasoning", "GROK_NONREASONING_MODEL_NAME"),
            ("kimi", "KIMI_MODEL_NAME"),
            ("deepseek-r", "DEEPSEEK_R_MODEL_NAME"),
        ):
            m = os.getenv(env_name)
            if m and m.strip():
                add_azure_inference(alias, azure_url, azure_key, m)

    weird_url = _optional_env("AZURE_WEIRDOS_BASE_URL")
    weird_key = _optional_env("AZURE_WEIRDOS_KEY")
    if weird_url and not weird_key:
        logger.warning(
            "AZURE_WEIRDOS_BASE_URL is set but AZURE_WEIRDOS_KEY is missing; skipping deepseek-v/llama-maverick"
        )
    if weird_key and not weird_url:
        logger.warning(
            "AZURE_WEIRDOS_KEY is set but AZURE_WEIRDOS_BASE_URL is missing; skipping deepseek-v/llama-maverick"
        )
    if weird_url and weird_key:
        for alias, env_name in (
            ("deepseek-v", "DEEPSEEK_V_MODEL_NAME"),
            ("llama-maverick", "LLAMA_MODEL_NAME"),
        ):
            m = os.getenv(env_name)
            if m and m.strip():
                add_azure_inference(alias, weird_url, weird_key, m)

    ao_url = _optional_env("AZURE_OPENAI_BASE_URL")
    ao_key = _optional_env("AZURE_OPENAI_KEY")
    if ao_url and not ao_key:
        logger.warning(
            "AZURE_OPENAI_BASE_URL is set but AZURE_OPENAI_KEY is missing; skipping gpt-nano/gpt-mini registry"
        )
    if ao_key and not ao_url:
        logger.warning(
            "AZURE_OPENAI_KEY is set but AZURE_OPENAI_BASE_URL is missing; skipping gpt-nano/gpt-mini registry"
        )
    if ao_url and ao_key:
        for alias, env_name in (
            ("gpt-nano", "GPT_NANO_MODEL_NAME"),
            ("gpt-mini", "GPT_MINI_MODEL_NAME"),
        ):
            m = os.getenv(env_name)
            if m and m.strip():
                add_azure_inference(alias, ao_url, ao_key, m)

    return out


def _make_llm_from_provider() -> ModelConfig:
    provider = _parse_provider("LLM_PROVIDER", "openai")
    if provider == "azure":
        api_key = _optional_env("LLM_AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_KEY", "OPENAI_API_KEY")
        if not api_key:
            raise ConfigError("Missing required environment variable: AZURE_OPENAI_API_KEY (or LLM_AZURE_OPENAI_API_KEY)")

        endpoint = _optional_env("LLM_AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_ENDPOINT")
        if not endpoint:
            raise ConfigError("Missing required environment variable: AZURE_OPENAI_ENDPOINT (or LLM_AZURE_OPENAI_ENDPOINT)")

        api_version = _optional_env("LLM_AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_API_VERSION")
        if not api_version:
            raise ConfigError("Missing required environment variable: AZURE_OPENAI_API_VERSION (or LLM_AZURE_OPENAI_API_VERSION)")

        return ModelConfig(
            provider=provider,
            api_key=api_key,
            model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1"),
            azure_endpoint=endpoint,
            azure_api_version=api_version,
        )

    if provider == "azure_inference":
        api_key = _optional_env("LLM_INFERENCE_API_KEY", "SECONDARY_LLM_API_KEY", "AZURE_OPENAI_API_KEY", "OPENAI_API_KEY")
        if not api_key:
            raise ConfigError(
                "Missing required environment variable: LLM_INFERENCE_API_KEY "
                "(or SECONDARY_LLM_API_KEY)"
            )

        url = _optional_env("LLM_INFERENCE_URL", "SECONDARY_LLM_BASE_URL")
        if not url:
            raise ConfigError(
                "Missing required environment variable: LLM_INFERENCE_URL "
                "(or SECONDARY_LLM_BASE_URL)"
            )

        header = os.getenv("LLM_INFERENCE_API_KEY_HEADER", "api-key")
        return ModelConfig(
            provider=provider,
            api_key=api_key,
            model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            base_url=url,
            api_key_header=header,
        )

    return ModelConfig(
        provider=provider,
        api_key=_optional_env("LLM_API_KEY", "OPENAI_API_KEY") or _require_env("OPENAI_API_KEY"),
        model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1"),
    )


def _make_judge_from_provider() -> ModelConfig:
    provider = _parse_provider("JUDGE_PROVIDER", "openai_compatible")
    if provider == "azure":
        api_key = _optional_env("JUDGE_AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_KEY", "NEBIUS_API_KEY", "OPENAI_API_KEY")
        if not api_key:
            raise ConfigError("Missing required environment variable: JUDGE_AZURE_OPENAI_API_KEY (or AZURE_OPENAI_API_KEY)")

        endpoint = _optional_env("JUDGE_AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_ENDPOINT")
        if not endpoint:
            raise ConfigError("Missing required environment variable: JUDGE_AZURE_OPENAI_ENDPOINT (or AZURE_OPENAI_ENDPOINT)")

        api_version = _optional_env("JUDGE_AZURE_OPENAI_API_VERSION", "AZURE_OPENAI_API_VERSION")
        if not api_version:
            raise ConfigError("Missing required environment variable: JUDGE_AZURE_OPENAI_API_VERSION (or AZURE_OPENAI_API_VERSION)")

        return ModelConfig(
            provider=provider,
            api_key=api_key,
            model=os.getenv("JUDGE_MODEL", "deepseek-ai/DeepSeek-V3-0324"),
            base_url=os.getenv("JUDGE_BASE_URL", "https://api.tokenfactory.nebius.com/v1/"),
            azure_endpoint=endpoint,
            azure_api_version=api_version,
        )

    if provider == "azure_inference":
        api_key = _optional_env("JUDGE_INFERENCE_API_KEY", "SECONDARY_LLM_API_KEY", "AZURE_OPENAI_API_KEY", "NEBIUS_API_KEY", "OPENAI_API_KEY")
        if not api_key:
            raise ConfigError(
                "Missing required environment variable: JUDGE_INFERENCE_API_KEY "
                "(or SECONDARY_LLM_API_KEY)"
            )

        url = _optional_env("JUDGE_INFERENCE_URL", "SECONDARY_LLM_BASE_URL")
        if not url:
            raise ConfigError(
                "Missing required environment variable: JUDGE_INFERENCE_URL "
                "(or SECONDARY_LLM_BASE_URL)"
            )

        header = os.getenv("JUDGE_INFERENCE_API_KEY_HEADER", "api-key")
        return ModelConfig(
            provider=provider,
            api_key=api_key,
            model=os.getenv("JUDGE_MODEL", "deepseek-ai/DeepSeek-V3-0324"),
            base_url=url,
            api_key_header=header,
        )

    return ModelConfig(
        provider=provider,
        api_key=_optional_env("JUDGE_API_KEY", "NEBIUS_API_KEY", "OPENAI_API_KEY") or _require_env("NEBIUS_API_KEY"),
        model=os.getenv("JUDGE_MODEL", "deepseek-ai/DeepSeek-V3-0324"),
        base_url=os.getenv("JUDGE_BASE_URL", "https://api.tokenfactory.nebius.com/v1/"),
    )


class _Config:
    """Lazy-loaded configuration singleton. Each property validates and
    caches its config on first access so missing env vars surface
    immediately at the point of use."""

    def __init__(self) -> None:
        self._llm: ModelConfig | None = None
        self._search: SearchConfig | None = None
        self._judge: ModelConfig | None = None
        self._model_registry: dict[str, ModelConfig] | None = None

    @property
    def models(self) -> dict[str, ModelConfig]:
        """Named models from optional Azure env groupings (aliases like grok-reasoning, gpt-nano)."""
        if self._model_registry is None:
            self._model_registry = _build_model_registry()
        return dict(self._model_registry)

    @property
    def llm(self) -> ModelConfig:
        if self._llm is None:
            model_id = (os.getenv("LLM_MODEL") or "gpt-4o-mini").strip()
            reg = self.models
            if model_id in reg:
                self._llm = reg[model_id]
            else:
                self._llm = _make_llm_from_provider()
        return self._llm

    @property
    def search(self) -> SearchConfig:
        if self._search is None:
            self._search = SearchConfig(api_key=_require_env("TAVILY_API_KEY"))
        return self._search

    @property
    def judge(self) -> ModelConfig:
        if self._judge is None:
            model_id = (os.getenv("JUDGE_MODEL") or "deepseek-ai/DeepSeek-V3-0324").strip()
            reg = self.models
            if model_id in reg:
                self._judge = reg[model_id]
            else:
                self._judge = _make_judge_from_provider()
        return self._judge

    def reset(self) -> None:
        """Clear cached configs so they are re-read from env on next access."""
        self._llm = None
        self._search = None
        self._judge = None
        self._model_registry = None


config = _Config()
