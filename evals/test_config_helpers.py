"""Unit tests for `backend.config` helper functions (imported explicitly for coverage)."""

import pytest

from conftest import collect_eval_config_errors

from backend.config import (
    ConfigError,
    Provider,
    _optional_env,
    _parse_provider,
    _require_env,
    config,
)


@pytest.fixture(autouse=True)
def reset_config():
    config.reset()
    yield
    config.reset()


def test_require_env_missing(monkeypatch):
    monkeypatch.delenv("FACTIFY_REQUIRE_ENV_TEST", raising=False)
    with pytest.raises(ConfigError, match="FACTIFY_REQUIRE_ENV_TEST"):
        _require_env("FACTIFY_REQUIRE_ENV_TEST")


def test_require_env_empty_string(monkeypatch):
    monkeypatch.setenv("FACTIFY_REQUIRE_ENV_TEST", "")
    with pytest.raises(ConfigError, match="FACTIFY_REQUIRE_ENV_TEST"):
        _require_env("FACTIFY_REQUIRE_ENV_TEST")


def test_optional_env_first_wins(monkeypatch):
    monkeypatch.setenv("A", "first")
    monkeypatch.setenv("B", "second")
    assert _optional_env("A", "B") == "first"


def test_optional_env_skips_empty(monkeypatch):
    monkeypatch.setenv("A", "")
    monkeypatch.setenv("B", "ok")
    assert _optional_env("A", "B") == "ok"


def test_optional_env_none_when_all_missing(monkeypatch):
    monkeypatch.delenv("A", raising=False)
    monkeypatch.delenv("B", raising=False)
    assert _optional_env("A", "B") is None


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("openai", "openai"),
        ("OPENAI", "openai"),
        ("compatible", "openai_compatible"),
        ("openai_compatible", "openai_compatible"),
        ("nebius", "openai_compatible"),
        ("azure", "azure"),
        ("azure_openai", "azure"),
        ("azure_inference", "azure_inference"),
        ("azure_ai", "azure_inference"),
        ("inference", "azure_inference"),
    ],
)
def test_parse_provider_aliases(monkeypatch, raw: str, expected: Provider):
    monkeypatch.setenv("LLM_PROVIDER", raw)
    assert _parse_provider("LLM_PROVIDER", "openai") == expected


def test_parse_provider_invalid(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "anthropic")
    with pytest.raises(ConfigError, match="Invalid LLM_PROVIDER"):
        _parse_provider("LLM_PROVIDER", "openai")


def test_collect_eval_config_errors_registry_llm_without_openai_or_nebius(monkeypatch):
    """Benchmark-style gate: pipeline via registry + Tavily does not require OPENAI/NEBIUS."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("NEBIUS_API_KEY", raising=False)
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.setenv("TAVILY_API_KEY", "tvly-test")
    monkeypatch.setenv("LLM_MODEL", "kimi")
    monkeypatch.setenv("AZURE_BASE_URL", "https://example.azure.com/chat?api-version=1")
    monkeypatch.setenv("AZURE_API_KEY", "azure-key")
    monkeypatch.setenv("KIMI_MODEL_NAME", "Kimi-K2.5")
    config.reset()
    assert collect_eval_config_errors(need_judge=False) == []


def test_collect_eval_config_errors_skips_when_pipeline_llm_unconfigured(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.delenv("AZURE_BASE_URL", raising=False)
    monkeypatch.delenv("AZURE_API_KEY", raising=False)
    monkeypatch.setenv("TAVILY_API_KEY", "tvly-test")
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("LLM_MODEL", "gpt-4o-mini")
    config.reset()
    errs = collect_eval_config_errors(need_judge=False)
    assert errs
    assert any("OPENAI_API_KEY" in e for e in errs)


def test_collect_eval_config_errors_live_api_requires_judge_credentials(monkeypatch):
    """live_api gate also validates judge config; benchmark-only does not."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("NEBIUS_API_KEY", raising=False)
    monkeypatch.delenv("JUDGE_API_KEY", raising=False)
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.setenv("TAVILY_API_KEY", "tvly-test")
    monkeypatch.setenv("LLM_MODEL", "kimi")
    monkeypatch.setenv("AZURE_BASE_URL", "https://example.azure.com/chat?api-version=1")
    monkeypatch.setenv("AZURE_API_KEY", "azure-key")
    monkeypatch.setenv("KIMI_MODEL_NAME", "Kimi-K2.5")
    config.reset()
    assert collect_eval_config_errors(need_judge=False) == []
    config.reset()
    errs = collect_eval_config_errors(need_judge=True)
    assert errs
    assert any("NEBIUS_API_KEY" in e or "OPENAI_API_KEY" in e for e in errs)
