# Factify (TruthLens)

AI-powered Chrome extension for verifying factual claims on webpages.

## Prerequisites

- Python 3.11+
- A `.env` file in the project root (copy `.env.example` and fill in your keys)

## Configuration

Copy the example env file and add your API keys:

```bash
cp .env.example .env
```

| Variable | Required | Default | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | Yes | — | OpenAI key for claim extraction & analysis |
| `TAVILY_API_KEY` | Yes | — | Tavily key for web search |
| `NEBIUS_API_KEY` | Yes (evals) | — | Nebius key for eval judge model |
| `LLM_MODEL` | No | `gpt-4o-mini` | Model used by the backend pipeline |
| `LLM_BASE_URL` | No | `https://api.openai.com/v1` | Base URL for the LLM provider |
| `JUDGE_MODEL` | No | `deepseek-ai/DeepSeek-V3-0324` | Model used for eval judging |
| `JUDGE_BASE_URL` | No | `https://api.tokenfactory.nebius.com/v1/` | Base URL for the judge provider |

All configuration is centralized in `backend/config.py` and loaded lazily from environment variables. Missing required variables raise immediately with a clear error message.

## Getting Started

### 1. Install backend dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### 2. Start the backend

```bash
uvicorn backend.main:app --reload --port 8000
```

The API will be available at **http://localhost:8000**. Check health at `/health`.

### 3. Serve the extension mock UI

In a separate terminal:

```bash
cd extension
python3 -m http.server 3000
```

Then open **http://localhost:3000/mock.html** in your browser to interact with the mock UI.

## Running Evals

```bash
pip install -r evals/requirements.txt
python -m pytest evals/ -v
```

Unit tests (mocked) run without API keys. Quality tests require all three API keys to be set.
