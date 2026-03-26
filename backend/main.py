import logging
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from fastapi.responses import JSONResponse
from starlette.responses import StreamingResponse

from backend.config import config, ConfigError
from backend.models import FactCheckRequest, FactCheckResponse, ErrorResponse
from backend.pipeline import fact_check, fact_check_stream

logger = logging.getLogger(__name__)

try:
    _ = config.llm
    _ = config.search
except ConfigError as exc:
    logger.error("Configuration error at startup: %s", exc)
    raise SystemExit(1) from exc

app = FastAPI(title="Factify", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/factcheck", response_model=FactCheckResponse)
async def factcheck_endpoint(request: FactCheckRequest):
    try:
        result = await fact_check(request.text)
        return result
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(error="Pipeline failed", detail=str(e)).model_dump(),
        )


@app.post("/factcheck/stream")
async def factcheck_stream_endpoint(request: FactCheckRequest):
    return StreamingResponse(
        fact_check_stream(request.text),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/health")
async def health():
    return {"status": "ok"}
