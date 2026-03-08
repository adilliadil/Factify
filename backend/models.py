from pydantic import BaseModel, Field


class FactCheckRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)


class Source(BaseModel):
    title: str
    url: str


class ClaimResult(BaseModel):
    text: str
    verdict: str  # "supported", "contradicted", "mixed", "unverifiable"


class FactCheckResponse(BaseModel):
    original_text: str
    claims: list[ClaimResult]
    score: int = Field(..., ge=0, le=100)
    verdict: str
    tldr: str
    explanation: str
    sources: list[Source]


class ErrorResponse(BaseModel):
    error: str
    detail: str | None = None
