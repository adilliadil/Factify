# Changelog

All notable changes to this project will be documented in this file.

## 0.2.22

- **Rebase:** resolved conflicts when applying **Benching multi-LLM** onto the rebased WIP: merged changelog with **0.2.21**–**0.2.14** from that branch; combined `evals/benchmark_reporting.py` failed-samples / skipped-sample section; took **`evals/reports/benchmark_results.json`** from the incoming commit. Removed **`evals/__init__.py`** (PEP 420 namespace; see **0.2.21**).

## 0.2.21

- **Benchmark conftest:** keep **`evals/`** as a PEP 420 namespace package — do **not** add **`evals/__init__.py`**, or pytest can load **`conftest`** twice and mis-report assertion failures as request failures. Regression test in **`evals/test_conftest_loading.py`**.
- **Benchmark reporting:** **`pytest.skip`** rows (e.g. Arm B with no search sources) are tracked as **`skipped`** — excluded from accuracy / within-one / calibration; text and comparison Markdown add **skipped (%)** and **skipped (counts)** alongside request-failure stats; standalone reports list skipped sample IDs separately. Tests in **`evals/test_benchmark_reporting.py`** and **`evals/test_run_benchmark.py`**.
- **`run_benchmark`:** subprocess pytest uses **`--tb line`** (one-line tracebacks on failure) instead of **`--tb no`**.

## 0.2.20

- **Grok on Azure AI Foundry:** registry aliases **`grok-reasoning`** and **`grok-nonreasoning`** now use **`GrokChatClient`** — **`Authorization: Bearer`** (matches Foundry) plus **`max_completion_tokens`** and **`top_p: 1`**. Cap via optional **`GROK_MAX_COMPLETION_TOKENS`** (default **4000**). `ModelConfig` gains **`client_kind`** / **`grok_max_completion_tokens`**; other `azure_inference` aliases unchanged. Tests in `evals/test_llm_clients.py` and `evals/test_provider_config.py`.

## 0.2.19

- **`analyze_evidence`:** tolerate **`score: null`**, string numerics, and other awkward **`score`** shapes from models (e.g. Grok on Azure) instead of raising before benchmark hooks store a row. Tests in `evals/test_analysis.py`.
- **`HttpChatClient` (`azure_inference`):** send **`stream: false`**; normalise **list-shaped `reasoning_content`** (including plain string list items); log when the response body is not JSON. Tests in `evals/test_llm_clients.py`.

## 0.2.18

- **`HttpChatClient` (`azure_inference`):** **`HTTP_INFERENCE_MAX_RETRIES`** (optional, default **3**) controls how many times transient failures are retried; stored on `ModelConfig.http_inference_max_retries`. Tests in `evals/test_llm_clients.py`.

## 0.2.17

- **`HttpChatClient` (`azure_inference`):** omit **`response_format`** from the chat-completions JSON body (Azure Model Inference often rejects it for Grok and similar models; JSON output remains prompt-enforced). Assistant text is taken from **`message.content`**, with fallbacks for **list-shaped content** and for **`reasoning_content`** when `content` is empty (Grok reasoning on Azure). Tests in `evals/test_llm_clients.py`.

## 0.2.16

- **`HttpChatClient` (`azure_inference`):** up to **3 retries** on transient failures (HTTP **429** and **5xx**, plus **`httpx.RequestError`** such as timeouts), with exponential backoff (0.5s, 1s, 2s). Non-retryable HTTP errors (e.g. 400) fail immediately. Tests in `evals/test_llm_clients.py`.

## 0.2.15

- **`run_benchmark`:** when a requested model is missing from `config.models`, stderr now adds a short **env hint** for known registry aliases (e.g. `gpt-5.4` → `GPT_MODEL_NAME`). README clarifies that each Azure OpenAI alias needs its own `*_MODEL_NAME`. Test in `evals/test_run_benchmark.py`.

## 0.2.14

- **Model registry:** `gpt-5.4` alias (standard GPT-5.4 on Azure OpenAI Service) alongside `gpt-nano` / `gpt-mini`, driven by `GPT_MODEL_NAME` with the same `AZURE_OPENAI_BASE_URL` / `AZURE_OPENAI_KEY` group. Documented in `.env.example` and README; tests in `evals/test_provider_config.py` and `evals/test_run_benchmark.py`.

## 0.2.13

- **Docs:** resolved README merge conflict in the evals Mermaid diagram: optional **multi-LLM benchmark** subgraph (`run_benchmark` → Markdown report) sits alongside **Eval Types** (unit, quality, three-arm benchmark).

## 0.2.12

- **Benchmark reporting:** track **request failures** (API/pipeline errors before a result is stored via `store_benchmark_result`). Pytest hook sets `request_failed` when the call outcome is **failed** and no result was stored (skips are not counted as request failures); exact accuracy and within-one metrics exclude those rows; **request failure %** is reported separately (text report, JSON rows, and `run_benchmark` Markdown: per-arm rates, incorrect-verdict counts vs request-failure counts). README evals diagram note updated. Tests in `evals/test_benchmark_reporting.py` and `evals/test_run_benchmark.py`.

## 0.2.11

- **Benchmark reporting:** when `BENCHMARK_OUTPUT_FILE` is set (`python -m evals.run_benchmark` subprocesses), skip writing per-model timestamped `.txt` files under `evals/reports/`; the parent process emits the single Markdown comparison. `run_benchmark` catches and prints tracebacks if comparison Markdown generation fails. Tests in `evals/test_benchmark_reporting.py` and `evals/test_run_benchmark.py`.

## 0.2.10

- **`run_benchmark`:** load the project `.env` (and optional `evals/.env`) in the CLI process before checking registry aliases, matching pytest’s `pytest-dotenv` behaviour so `gpt-nano`, `kimi`, etc. do not spuriously warn when those aliases are defined via env. Declared `python-dotenv` in `evals/requirements.txt`.

## 0.2.9

- **`run_benchmark`:** run pytest subprocesses with `cwd=evals/` so `conftest` can import `benchmark_reporting` (fixes `ModuleNotFoundError` / pytest exit code 4 when the parent process used repo root as cwd). Print a clearer warning when the per-model JSON file is missing after a “successful” pytest run (typically all benchmark tests skipped due to missing API config).

## 0.2.8

- **Multi-LLM benchmark runner:** `python -m evals.run_benchmark` runs `evals/test_benchmark.py` in parallel subprocesses (one per `--models` alias), records wall-clock and average time per sample, and writes a Markdown comparison report under `evals/reports/comparison_<timestamp>/`. Env: `BENCHMARK_MAX_SAMPLES` caps combined benchmark rows in `evals/test_benchmark.py`; `BENCHMARK_OUTPUT_FILE` redirects the benchmark JSON snapshot (used by the runner). Tests in `evals/test_run_benchmark.py` and `evals/test_benchmark_reporting.py`.
- README: documented the comparison runner and updated the evals diagram.

## 0.2.7

- Benchmark text reports: failed sample rows now include verdict vs expected, score vs expected range (Arm A gold only), and reconstructed failure reasons so score-only failures are visible. `expected_score_range` is included in structured results / JSON snapshot. Tests in `evals/test_benchmark_reporting.py`.
- README: documented filtering benchmark runs by arm (`-k` class name), by sample ID, and with `-s` / `--log-cli-level` for debugging.

## 0.2.6

- Model registry (`gpt-nano`, `gpt-mini`): when `AZURE_OPENAI_BASE_URL` is a bare Azure resource host (no path), expand it to `/openai/deployments/<GPT_*_MODEL_NAME>/chat/completions?api-version=...` so requests hit the real chat API instead of the resource root (which can return an empty 200). Optional `AZURE_OPENAI_REGISTRY_API_VERSION` overrides the default API version. Documented in `.env.example` and `README.md`; tests in `evals/test_provider_config.py`.

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
