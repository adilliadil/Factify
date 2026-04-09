import pytest
from openai import AsyncAzureOpenAI, AsyncOpenAI

from backend.config import ConfigError, ModelConfig, config
from backend.llm_clients import HttpChatClient, create_client


@pytest.fixture(autouse=True)
def reset_config():
    config.reset()
    yield
    config.reset()


def test_llm_provider_defaults_to_openai(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    cfg = config.llm
    assert cfg.provider == "openai"
    assert cfg.api_key == "dummy"


def test_llm_provider_invalid_raises(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("LLM_PROVIDER", "anthropic")
    with pytest.raises(ConfigError, match="Invalid LLM_PROVIDER"):
        _ = config.llm


def test_llm_provider_openai_compatible(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("LLM_PROVIDER", "openai_compatible")
    monkeypatch.setenv("LLM_BASE_URL", "https://custom.example/v1")
    cfg = config.llm
    assert cfg.provider == "openai_compatible"
    assert cfg.base_url == "https://custom.example/v1"


def test_llm_api_key_priority(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "preferred")
    monkeypatch.setenv("OPENAI_API_KEY", "fallback")
    cfg = config.llm
    assert cfg.api_key == "preferred"


def test_llm_provider_azure_requires_endpoint_and_version(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "azure")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "dummy")
    monkeypatch.delenv("AZURE_OPENAI_ENDPOINT", raising=False)
    monkeypatch.delenv("AZURE_OPENAI_API_VERSION", raising=False)

    with pytest.raises(ConfigError) as exc:
        _ = config.llm
    assert "AZURE_OPENAI_ENDPOINT" in str(exc.value)


def test_llm_provider_azure_requires_version(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "azure")
    monkeypatch.setenv("AZURE_OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("AZURE_OPENAI_ENDPOINT", "https://x.openai.azure.com")
    monkeypatch.delenv("AZURE_OPENAI_API_VERSION", raising=False)

    with pytest.raises(ConfigError) as exc:
        _ = config.llm
    assert "AZURE_OPENAI_API_VERSION" in str(exc.value)


def test_judge_provider_accepts_nebius_alias(monkeypatch):
    monkeypatch.setenv("JUDGE_PROVIDER", "nebius")
    monkeypatch.setenv("NEBIUS_API_KEY", "dummy")
    cfg = config.judge
    assert cfg.provider == "openai_compatible"
    assert cfg.api_key == "dummy"


def test_judge_azure_inference_missing_url(monkeypatch):
    monkeypatch.setenv("JUDGE_PROVIDER", "azure_inference")
    monkeypatch.setenv("JUDGE_INFERENCE_API_KEY", "k")
    monkeypatch.delenv("JUDGE_INFERENCE_URL", raising=False)
    monkeypatch.delenv("SECONDARY_LLM_BASE_URL", raising=False)

    with pytest.raises(ConfigError) as exc:
        _ = config.judge
    assert "JUDGE_INFERENCE_URL" in str(exc.value)


def test_llm_provider_azure_inference_reads_secondary_vars(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "azure_inference")
    monkeypatch.setenv("SECONDARY_LLM_API_KEY", "dummy")
    monkeypatch.setenv("SECONDARY_LLM_BASE_URL", "https://example.com/models/chat/completions?api-version=2024-01-01")
    cfg = config.llm
    assert cfg.provider == "azure_inference"
    assert cfg.base_url == "https://example.com/models/chat/completions?api-version=2024-01-01"


def test_model_registry_resolves_llm_alias(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("LLM_MODEL", "kimi")
    monkeypatch.setenv("AZURE_BASE_URL", "https://example.azure.com/chat?api-version=1")
    monkeypatch.setenv("AZURE_API_KEY", "azure-key")
    monkeypatch.setenv("KIMI_MODEL_NAME", "Kimi-K2.5")
    cfg = config.llm
    assert cfg.provider == "azure_inference"
    assert cfg.model == "Kimi-K2.5"
    assert cfg.api_key == "azure-key"
    assert cfg.base_url == "https://example.azure.com/chat?api-version=1"


def test_model_registry_exposed_on_config(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("AZURE_BASE_URL", "https://x")
    monkeypatch.setenv("AZURE_API_KEY", "k")
    monkeypatch.setenv("KIMI_MODEL_NAME", "Kimi-K2.5")
    reg = config.models
    assert "kimi" in reg
    assert reg["kimi"].model == "Kimi-K2.5"


def test_registry_skips_group_when_key_missing(monkeypatch, caplog):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("AZURE_BASE_URL", "https://x")
    monkeypatch.delenv("AZURE_API_KEY", raising=False)
    monkeypatch.setenv("KIMI_MODEL_NAME", "Kimi-K2.5")
    monkeypatch.setenv("LLM_MODEL", "kimi")
    import logging

    caplog.set_level(logging.WARNING)
    cfg = config.llm
    assert "kimi" not in config.models
    assert cfg.provider == "openai"
    assert cfg.model == "kimi"
    assert "AZURE_API_KEY" in caplog.text


def test_registry_skips_blank_model_name(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("AZURE_BASE_URL", "https://x")
    monkeypatch.setenv("AZURE_API_KEY", "k")
    monkeypatch.setenv("KIMI_MODEL_NAME", "   ")
    assert "kimi" not in config.models


def test_unknown_llm_model_falls_through_to_provider(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("LLM_MODEL", "not-a-registry-alias")
    cfg = config.llm
    assert cfg.provider == "openai"
    assert cfg.model == "not-a-registry-alias"


def test_models_returned_dict_is_copy(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "dummy")
    monkeypatch.setenv("AZURE_BASE_URL", "https://x")
    monkeypatch.setenv("AZURE_API_KEY", "k")
    monkeypatch.setenv("KIMI_MODEL_NAME", "Kimi-K2.5")
    a = config.models
    a["kimi"] = ModelConfig(provider="openai", model="x", api_key="y", base_url="https://api.openai.com/v1")
    b = config.models
    assert b["kimi"].model == "Kimi-K2.5"


def test_judge_resolves_registry_alias(monkeypatch):
    monkeypatch.setenv("NEBIUS_API_KEY", "dummy")
    monkeypatch.setenv("JUDGE_MODEL", "gpt-nano")
    monkeypatch.setenv("AZURE_OPENAI_BASE_URL", "https://aoai.example/chat")
    monkeypatch.setenv("AZURE_OPENAI_KEY", "aoai-key")
    monkeypatch.setenv("GPT_NANO_MODEL_NAME", "gpt-5.4-nano")
    cfg = config.judge
    assert cfg.provider == "azure_inference"
    assert cfg.model == "gpt-5.4-nano"
    assert cfg.api_key == "aoai-key"


def test_create_client_dispatches_azure_openai():
    az = create_client(
        ModelConfig(
            provider="azure",
            model="m",
            api_key="k",
            azure_endpoint="https://x.openai.azure.com",
            azure_api_version="2024-01-01",
        )
    )
    assert isinstance(az, AsyncAzureOpenAI)


def test_create_client_openai_and_inference():
    oa = create_client(
        ModelConfig(provider="openai", model="m", api_key="k", base_url="https://api.openai.com/v1")
    )
    assert isinstance(oa, AsyncOpenAI)

    inf = create_client(
        ModelConfig(
            provider="azure_inference",
            model="m",
            api_key="k",
            base_url="https://example.com/v1/chat/completions",
        )
    )
    assert isinstance(inf, HttpChatClient)
