# Changelog

All notable changes to this project will be documented in this file.

## 0.2.14

- **Merge:** resolved conflicts in `evals/benchmark_reporting.py` and `evals/test_benchmark_reporting.py` (combined `verdict_correct` with `request_failed` / `within_one` handling; `write_reports` standalone path calls `format_report` with all four arms including baseline). Restored `evals/reports/benchmark_results.json` from `main`. Fixed subprocess `write_reports` tests to pass four arm lists.

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
