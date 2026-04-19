from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass
from types import SimpleNamespace
from typing import TypeAlias

import httpx
from openai import AsyncAzureOpenAI, AsyncOpenAI

from backend.config import ModelConfig

logger = logging.getLogger(__name__)

__all__ = ["GrokChatClient", "HttpChatClient", "LLMClient", "create_client"]


def _http_status_is_retryable(status: int) -> bool:
    if status == 429:
        return True
    return 500 <= status <= 599


def _normalise_message_content(content: object) -> str:
    """Turn ``message.content`` into a string (OpenAI can use a string or a list of parts)."""
    if content is None:
        return ""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
                continue
            if not isinstance(block, dict):
                continue
            if block.get("type") == "text" and isinstance(block.get("text"), str):
                parts.append(block["text"])
            elif isinstance(block.get("content"), str):
                parts.append(block["content"])
            elif isinstance(block.get("reasoning"), str):
                parts.append(block["reasoning"])
        return "".join(parts).strip()
    return ""


def _extract_assistant_content(data: dict) -> str:
    """Read assistant text from a chat-completions JSON body.

    Azure AI / Grok reasoning deployments sometimes leave ``message.content`` empty and put text in
    ``reasoning_content``; some APIs use list-shaped ``content`` blocks.
    """
    choices = data.get("choices")
    if not isinstance(choices, list) or not choices:
        return ""
    first = choices[0]
    if not isinstance(first, dict):
        return ""
    msg = first.get("message")
    if not isinstance(msg, dict):
        return ""
    text = _normalise_message_content(msg.get("content"))
    if text:
        return text
    rc = msg.get("reasoning_content")
    if rc is not None:
        text = _normalise_message_content(rc)
        if text:
            return text
    return ""


async def _fetch_inference_json_with_retries(
    http: httpx.AsyncClient,
    *,
    url: str,
    headers: dict[str, str],
    payload: dict,
    max_retries: int,
    log_label: str,
) -> dict:
    """POST JSON to an Azure-style inference URL; retry on 429 / 5xx / transport errors."""
    r: httpx.Response | None = None
    for attempt in range(max_retries + 1):
        try:
            r = await http.post(url, json=payload, headers=headers)
            r.raise_for_status()
            break
        except httpx.HTTPStatusError as exc:
            code = exc.response.status_code if exc.response is not None else 0
            body = exc.response.text[:500] if exc.response is not None else ""
            logger.warning(
                "%s HTTP error: %s %s body_snippet=%r",
                log_label,
                code or "?",
                url,
                body,
            )
            retryable = exc.response is not None and _http_status_is_retryable(code)
            if not retryable or attempt >= max_retries:
                raise
            delay_s = 0.5 * (2**attempt)
            logger.warning(
                "%s retry %s/%s in %.1fs after HTTP %s",
                log_label,
                attempt + 1,
                max_retries,
                delay_s,
                code,
            )
            await asyncio.sleep(delay_s)
        except httpx.RequestError as exc:
            logger.warning("%s request failed: %s url=%s", log_label, exc, url)
            if attempt >= max_retries:
                raise
            delay_s = 0.5 * (2**attempt)
            logger.warning(
                "%s retry %s/%s in %.1fs after %s",
                log_label,
                attempt + 1,
                max_retries,
                delay_s,
                type(exc).__name__,
            )
            await asyncio.sleep(delay_s)

    assert r is not None
    try:
        return r.json()
    except json.JSONDecodeError:
        snippet = (r.text or "")[:500]
        logger.warning(
            "%s response is not JSON status=%s snippet=%r",
            log_label,
            r.status_code,
            snippet,
        )
        raise


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
    def __init__(
        self,
        *,
        url: str,
        api_key: str,
        api_key_header: str = "api-key",
        max_retries: int = 3,
    ) -> None:
        self._url = url
        self._api_key = api_key
        self._api_key_header = api_key_header
        self._max_retries = max_retries
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
            # Explicit non-streaming; some Azure Model Inference deployments default oddly without this.
            "stream": False,
        }
        # Do not send OpenAI's ``response_format`` here: Azure AI Model Inference often rejects it
        # for Grok and other models with 422 ``parameter_not_supported``. Call sites already ask
        # for JSON in the prompt; AsyncOpenAI / AsyncAzureOpenAI paths still use ``response_format``.

        headers = {
            self._api_key_header: self._api_key,
            "Content-Type": "application/json",
        }

        logger.debug(
            "Azure inference POST model=%s messages=%d json_mode_in_prompt_only=%s",
            model,
            len(messages),
            response_format is not None,
        )

        data = await _fetch_inference_json_with_retries(
            self._http,
            url=self._url,
            headers=headers,
            payload=payload,
            max_retries=self._max_retries,
            log_label="Azure inference",
        )

        content = _extract_assistant_content(data)
        logger.debug("Azure inference OK")
        return _ChatCompletionResponse(choices=[_Choice(message=_Message(content=content))])

    async def aclose(self) -> None:
        await self._http.aclose()


class _GrokChatCompletions:
    """Azure AI Foundry Grok: ``Authorization: Bearer`` plus ``max_completion_tokens`` / ``top_p``."""

    def __init__(
        self,
        *,
        url: str,
        api_key: str,
        max_retries: int = 3,
        max_completion_tokens: int = 4000,
    ) -> None:
        self._url = url
        self._api_key = api_key
        self._max_retries = max_retries
        self._max_completion_tokens = max_completion_tokens
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
            "stream": False,
            "top_p": 1,
            "max_completion_tokens": self._max_completion_tokens,
        }
        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

        logger.debug(
            "Grok inference POST model=%s messages=%d max_completion_tokens=%s json_mode_in_prompt_only=%s",
            model,
            len(messages),
            self._max_completion_tokens,
            response_format is not None,
        )

        data = await _fetch_inference_json_with_retries(
            self._http,
            url=self._url,
            headers=headers,
            payload=payload,
            max_retries=self._max_retries,
            log_label="Grok inference",
        )

        content = _extract_assistant_content(data)
        logger.debug("Grok inference OK")
        return _ChatCompletionResponse(choices=[_Choice(message=_Message(content=content))])

    async def aclose(self) -> None:
        await self._http.aclose()


class GrokChatClient:
    """HTTP shim for Grok on Azure AI Foundry (Bearer auth, Grok-tuned payload)."""

    def __init__(
        self,
        *,
        url: str,
        api_key: str,
        max_retries: int = 3,
        max_completion_tokens: int = 4000,
    ) -> None:
        self._completions = _GrokChatCompletions(
            url=url,
            api_key=api_key,
            max_retries=max_retries,
            max_completion_tokens=max_completion_tokens,
        )
        self.chat = SimpleNamespace(completions=self._completions)

    async def aclose(self) -> None:
        await self._completions.aclose()


class HttpChatClient:
    """Tiny client shim that matches the subset of the OpenAI SDK we use:
    client.chat.completions.create(...)
    """

    def __init__(
        self,
        *,
        url: str,
        api_key: str,
        api_key_header: str = "api-key",
        max_retries: int = 3,
    ) -> None:
        self._completions = _HttpChatCompletions(
            url=url,
            api_key=api_key,
            api_key_header=api_key_header,
            max_retries=max_retries,
        )
        self.chat = SimpleNamespace(completions=self._completions)

    async def aclose(self) -> None:
        await self._completions.aclose()


LLMClient: TypeAlias = AsyncOpenAI | AsyncAzureOpenAI | GrokChatClient | HttpChatClient


def create_client(cfg: ModelConfig) -> LLMClient:
    """Build an async LLM client from a universal ModelConfig."""
    if cfg.provider == "azure":
        return AsyncAzureOpenAI(
            api_key=cfg.api_key,
            azure_endpoint=cfg.azure_endpoint or "",
            api_version=cfg.azure_api_version or "",
        )
    if cfg.provider == "azure_inference":
        if cfg.client_kind == "grok":
            return GrokChatClient(
                url=cfg.base_url or "",
                api_key=cfg.api_key,
                max_retries=cfg.http_inference_max_retries,
                max_completion_tokens=cfg.grok_max_completion_tokens,
            )
        return HttpChatClient(
            url=cfg.base_url or "",
            api_key=cfg.api_key,
            api_key_header=cfg.api_key_header,
            max_retries=cfg.http_inference_max_retries,
        )
    base = cfg.base_url or "https://api.openai.com/v1"
    return AsyncOpenAI(api_key=cfg.api_key, base_url=base)
