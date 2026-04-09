from __future__ import annotations

import logging
from dataclasses import dataclass
from types import SimpleNamespace
from typing import TypeAlias

import httpx
from openai import AsyncAzureOpenAI, AsyncOpenAI

from backend.config import ModelConfig

logger = logging.getLogger(__name__)

__all__ = ["HttpChatClient", "LLMClient", "create_client"]


@dataclass(frozen=True)
class _Message:
    content: str


@dataclass(frozen=True)
class _Choice:
    message: _Message


@dataclass(frozen=True)
class _ChatCompletionResponse:
    choices: list[_Choice]


class _HttpChatCompletions:
    def __init__(self, *, url: str, api_key: str, api_key_header: str = "api-key") -> None:
        self._url = url
        self._api_key = api_key
        self._api_key_header = api_key_header
        self._http = httpx.AsyncClient(timeout=120.0)

    async def create(
        self,
        *,
        model: str,
        messages: list[dict],
        response_format: dict | None = None,
        temperature: float = 0,
    ) -> _ChatCompletionResponse:
        payload: dict = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        if response_format is not None:
            payload["response_format"] = response_format

        headers = {
            self._api_key_header: self._api_key,
            "Content-Type": "application/json",
        }

        logger.debug(
            "Azure inference POST model=%s messages=%d response_format=%s",
            model,
            len(messages),
            response_format is not None,
        )

        try:
            r = await self._http.post(self._url, json=payload, headers=headers)
            r.raise_for_status()
        except httpx.HTTPStatusError as exc:
            body = exc.response.text[:500] if exc.response is not None else ""
            logger.warning(
                "Azure inference HTTP error: %s %s body_snippet=%r",
                exc.response.status_code if exc.response else "?",
                self._url,
                body,
            )
            raise
        except httpx.RequestError as exc:
            logger.warning("Azure inference request failed: %s url=%s", exc, self._url)
            raise

        data = r.json()

        content = (data.get("choices") or [{}])[0].get("message", {}).get("content", "")
        logger.debug("Azure inference OK status=%s", r.status_code)
        return _ChatCompletionResponse(choices=[_Choice(message=_Message(content=content))])

    async def aclose(self) -> None:
        await self._http.aclose()


class HttpChatClient:
    """Tiny client shim that matches the subset of the OpenAI SDK we use:
    client.chat.completions.create(...)
    """

    def __init__(self, *, url: str, api_key: str, api_key_header: str = "api-key") -> None:
        self._completions = _HttpChatCompletions(url=url, api_key=api_key, api_key_header=api_key_header)
        self.chat = SimpleNamespace(completions=self._completions)

    async def aclose(self) -> None:
        await self._completions.aclose()


LLMClient: TypeAlias = AsyncOpenAI | AsyncAzureOpenAI | HttpChatClient


def create_client(cfg: ModelConfig) -> LLMClient:
    """Build an async LLM client from a universal ModelConfig."""
    if cfg.provider == "azure":
        return AsyncAzureOpenAI(
            api_key=cfg.api_key,
            azure_endpoint=cfg.azure_endpoint or "",
            api_version=cfg.azure_api_version or "",
        )
    if cfg.provider == "azure_inference":
        return HttpChatClient(
            url=cfg.base_url or "",
            api_key=cfg.api_key,
            api_key_header=cfg.api_key_header,
        )
    base = cfg.base_url or "https://api.openai.com/v1"
    return AsyncOpenAI(api_key=cfg.api_key, base_url=base)
