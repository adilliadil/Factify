# Changelog

All notable changes to this project will be documented in this file.

## 0.2.5

- Evals: live/benchmark gate now validates `config.llm`, `config.search`, and (for `live_api` only) `config.judge` via `ConfigError` messages instead of requiring `OPENAI_API_KEY`, `NEBIUS_API_KEY`, and `TAVILY_API_KEY` to all be set. Exposed `collect_eval_config_errors()` in `evals/conftest.py` with tests in `evals/test_config_helpers.py`.
- README: clarified eval credential requirements for benchmark vs mocked unit tests.

## 0.2.4

- Documented LLM routing in `.env.example`: registry aliases vs `LLM_PROVIDER=azure` vs `azure_inference`, and a step-by-step Grok (`grok-reasoning` / `grok-nonreasoning`) example.

## 0.2.3

- Added structured logging across the pipeline (`backend/llm.py`, `backend/pipeline.py`, `backend/search.py`), Azure inference HTTP client (`backend/llm_clients.py`), and eval judges (`evals/judges.py`); optional `LOG_LEVEL` via `backend/logging_config.py` (used by the FastAPI app).
- Tightened typing: `Provider` and `Literal` in `backend/config.py`, `AnalysisResult` / `ClaimVerdictItem` `TypedDict`s in `backend/llm.py`, and `LLMClient` union alias in `backend/llm_clients.py`; `py.typed` and `pyproject.toml` `[tool.mypy]` for the `backend` package.
- Model registry: log **warnings** when Azure env groups are only half-configured; **info** when an alias is registered.
- Evals: `pytest` `pythonpath` set to the repo root in `evals/pytest.ini`; `live_api` class `pytestmark` for quality suites; autouse fixture skips live/benchmark tests when `OPENAI_API_KEY` / `NEBIUS_API_KEY` / `TAVILY_API_KEY` are unset (after `.env` load).
- New tests: `evals/test_config_helpers.py`, `evals/test_llm_clients.py` (respx), `evals/test_benchmark_reporting.py`; expanded `evals/test_provider_config.py`; Tavily error path asserts log line in `evals/test_search.py`.

## 0.2.2

- Introduced universal `ModelConfig`, a single `create_client()` factory in `backend/llm_clients.py`, and a **model registry** (`config.models`) built from optional Azure env groups so named aliases (e.g. `kimi`, `gpt-nano`) can be used for both the pipeline (`LLM_MODEL`) and eval judge (`JUDGE_MODEL`).
- Removed duplicate `LLMConfig` / `JudgeConfig` types; benchmark reports now read the resolved pipeline model via `config.llm.model`.
- Eval unit tests set placeholder API keys when missing so mocked runs can resolve `config.llm` / `config.judge` without real credentials.

## 0.2.1

- Added `azure_inference` provider option so the pipeline LLM and judge LLM can call arbitrary Azure model inference `chat/completions` endpoints (not limited to Azure OpenAI).

## 0.2.0

- Added configurable LLM providers for both the **pipeline** and **judge** clients via env vars (`LLM_PROVIDER`, `JUDGE_PROVIDER`), supporting OpenAI/OpenAI-compatible and Azure OpenAI.
- Documented `nebius` as an alias of `openai_compatible` for both provider switches.
- Added `pytest-dotenv` so eval runs can automatically load `.env` via `evals/pytest.ini`.
