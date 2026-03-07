import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from backend.models import FactCheckRequest, FactCheckResponse, ErrorResponse
from backend.pipeline import fact_check

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
        from fastapi.responses import JSONResponse
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(error="Pipeline failed", detail=str(e)).model_dump(),
        )


@app.get("/health")
async def health():
    return {"status": "ok"}
