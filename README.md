# Factify (TruthLens)

AI-powered Chrome extension for verifying factual claims on webpages.

## How it works

```mermaid
flowchart TD
    A([📄 Input text]) --> B

    subgraph B["Step 1 — Extract Claims  ·  LLM"]
        B1["✅ Keep check-worthy factual claims<br/>health · statistics · history · science"]
        B2["🚫 Drop non-factual content<br/>opinions · predictions · trivial facts · greetings"]
    end

    B --> C{Claims found?}
    C -- No --> X1(["⚠ unverifiable"])
    C -- Yes --> D

    subgraph D["Step 2 — Search Evidence  ·  Tavily"]
        D1["🌐 Web search per claim<br/>query + 'evidence fact check'  ·  max 5 results"]
        D2["🔗 Deduplicate sources by URL  ·  cap at 8"]
        D1 --> D2
    end

    D --> E{Sources found?}
    E -- No --> X2(["⚠ unverifiable"])
    E -- Yes --> F

    subgraph F["Step 3 — Analyse Evidence  ·  LLM"]
        F1["🎯 Overall score 0–100 & verdict"]
        F2["📋 Per-claim verdict<br/>supported · contradicted · mixed · unverifiable"]
        F3["📰 Per-source stance<br/>supporting · contradicting · neutral"]
        F1 --> F2 --> F3
    end

    F --> G([✅ FactCheckResponse])
```

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

### How evals work

```mermaid
flowchart TD
    A([Run eval suite])

    A --> B

    subgraph B["1. Unit Tests  ·  mocked  ·  no API keys"]
        B1["🧪 Pick a test case"]
        B2["🤖 Mock LLM<br/>returns scripted extraction + analysis JSON"]
        B3["📦 Mock Tavily<br/>returns pre-recorded search fixture"]
        B4["▶ Run fact_check()"]
        B5["✅ Assert response fields<br/>score · verdict · claims · sources"]
        B1 --> B2
        B1 --> B3
        B2 --> B4
        B3 --> B4
        B4 --> B5
    end

    B --> C

    subgraph C["2. Quality Tests  ·  live APIs"]
        C1["📂 Load golden dataset case<br/>input + expected verdict + description"]
        C2["▶ Run fact_check()<br/>with real LLM + Tavily"]
        C3["⚖️ Judge with judge_e2e_quality()<br/>DeepSeek via Nebius"]
        C1 --> C2 --> C3
    end

    C --> D

    subgraph D["3. LLM-as-judge rubric"]
        D1["📝 Claim extraction<br/>right claims kept, opinions excluded"]
        D2["🎯 Verdict correctness<br/>matches expected verdict"]
        D3["🔢 Score alignment<br/>score fits verdict range"]
        D4["💬 Explanation quality<br/>helpful and accurate"]
        D1 --> D2 --> D3 --> D4
    end

    D --> E{Pass?}
```
