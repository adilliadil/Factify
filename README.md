# Factify (TruthLens)

AI-powered Chrome extension for verifying factual claims on webpages.

## Prerequisites

- Python 3.11+
- A `.env` file in the project root (see `.env.example` or `specs.md` for required keys)

## Getting Started

### 1. Install backend dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### 2. Start the backend

```bash
./venv/bin/uvicorn backend.main:app --reload --port 8000
```

The API will be available at **http://localhost:8000**. Check health at `/health`.

### 3. Serve the extension mock UI

In a separate terminal:

```bash
cd extension
python3 -m http.server 3000
```

Then open **http://localhost:3000/mock.html** in your browser to interact with the mock UI.
