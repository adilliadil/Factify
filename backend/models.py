from pydantic import BaseModel, Field


class FactCheckRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)


class Source(BaseModel):
    title: str
    url: str


class FactCheckResponse(BaseModel):
    claims: list[str]
    score: int = Field(..., ge=0, le=100)
    verdict: str
    explanation: str
    sources: list[Source]


class ErrorResponse(BaseModel):
    error: str
    detail: str | None = None
