"""Tests for `backend.llm_clients` (HTTP shim and client factory)."""

import json
from unittest.mock import AsyncMock

import httpx
import pytest
import respx

from backend.config import ModelConfig
from backend.llm_clients import GrokChatClient, HttpChatClient, create_client


@pytest.mark.asyncio
async def test_http_chat_client_returns_message_content():
    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            return_value=httpx.Response(
                200,
                json={"choices": [{"message": {"content": "hello"}}]},
            )
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="secret")
        try:
            resp = await c.chat.completions.create(
                model="m",
                messages=[{"role": "user", "content": "hi"}],
                temperature=0,
            )
            assert resp.choices[0].message.content == "hello"
        finally:
            await c.aclose()


@pytest.mark.asyncio
async def test_http_chat_client_does_not_send_response_format():
    """Azure AI Model Inference often 422s on OpenAI ``response_format``; prompts enforce JSON."""
    captured: dict = {}

    def side_effect(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content.decode())
        return httpx.Response(200, json={"choices": [{"message": {"content": "{}"}}]})

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(side_effect=side_effect)
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            await c.chat.completions.create(
                model="m",
                messages=[{"role": "user", "content": "x"}],
                response_format={"type": "json_object"},
                temperature=0,
            )
        finally:
            await c.aclose()
    assert "response_format" not in captured["body"]
    assert captured["body"].get("stream") is False


@pytest.mark.asyncio
async def test_http_chat_client_reasoning_content_when_content_empty():
    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            return_value=httpx.Response(
                200,
                json={
                    "choices": [
                        {
                            "message": {
                                "role": "assistant",
                                "content": "",
                                "reasoning_content": '{"claims": []}',
                            },
                        },
                    ],
                },
            )
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            resp = await c.chat.completions.create(model="grok", messages=[], temperature=0)
            assert resp.choices[0].message.content == '{"claims": []}'
        finally:
            await c.aclose()


@pytest.mark.asyncio
async def test_http_chat_client_custom_api_key_header():
    captured: dict = {}

    def side_effect(request: httpx.Request) -> httpx.Response:
        captured["headers"] = dict(request.headers)
        return httpx.Response(200, json={"choices": [{"message": {"content": ""}}]})

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(side_effect=side_effect)
        c = HttpChatClient(
            url="https://example.com/v1/chat",
            api_key="tok",
            api_key_header="X-Custom-Key",
        )
        try:
            await c.chat.completions.create(model="m", messages=[], temperature=0)
        finally:
            await c.aclose()
    assert captured["headers"].get("x-custom-key") == "tok"


@pytest.mark.asyncio
async def test_http_chat_client_400_raises_without_retry(monkeypatch):
    calls: list[int] = []

    async def no_sleep(_: float) -> None:
        calls.append(-1)

    monkeypatch.setattr("backend.llm_clients.asyncio.sleep", no_sleep)

    with respx.mock:
        route = respx.post("https://example.com/v1/chat")

        def track_and_fail(request: httpx.Request) -> httpx.Response:
            calls.append(1)
            return httpx.Response(400, text="bad request")

        route.mock(side_effect=track_and_fail)
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            with pytest.raises(httpx.HTTPStatusError):
                await c.chat.completions.create(model="m", messages=[], temperature=0)
        finally:
            await c.aclose()
    assert calls == [1]


@pytest.mark.asyncio
async def test_http_chat_client_retries_transient_http_then_succeeds(monkeypatch):
    monkeypatch.setattr("backend.llm_clients.asyncio.sleep", AsyncMock())

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            side_effect=[
                httpx.Response(429, text="rate limited"),
                httpx.Response(503, text="unavailable"),
                httpx.Response(200, json={"choices": [{"message": {"content": "recovered"}}]}),
            ]
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            resp = await c.chat.completions.create(model="m", messages=[], temperature=0)
            assert resp.choices[0].message.content == "recovered"
        finally:
            await c.aclose()


@pytest.mark.asyncio
async def test_http_chat_client_exhausts_retries_on_503(monkeypatch):
    monkeypatch.setattr("backend.llm_clients.asyncio.sleep", AsyncMock())

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            return_value=httpx.Response(503, text="still down")
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            with pytest.raises(httpx.HTTPStatusError):
                await c.chat.completions.create(model="m", messages=[], temperature=0)
        finally:
            await c.aclose()


@pytest.mark.asyncio
async def test_http_chat_client_max_retries_zero_single_attempt(monkeypatch):
    """With ``max_retries=0`` only the initial POST is made (no backoff retries)."""
    monkeypatch.setattr("backend.llm_clients.asyncio.sleep", AsyncMock())
    calls: list[int] = []

    def track_503(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(503, text="down")

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(side_effect=track_503)
        c = HttpChatClient(
            url="https://example.com/v1/chat",
            api_key="k",
            max_retries=0,
        )
        try:
            with pytest.raises(httpx.HTTPStatusError):
                await c.chat.completions.create(model="m", messages=[], temperature=0)
        finally:
            await c.aclose()
    assert calls == [1]


@pytest.mark.asyncio
async def test_http_chat_client_empty_choices_defaults_content():
    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            return_value=httpx.Response(200, json={"choices": []})
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            resp = await c.chat.completions.create(model="m", messages=[], temperature=0)
            assert resp.choices[0].message.content == ""
        finally:
            await c.aclose()


@pytest.mark.asyncio
async def test_http_chat_client_reasoning_content_list_parts():
    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            return_value=httpx.Response(
                200,
                json={
                    "choices": [
                        {
                            "message": {
                                "role": "assistant",
                                "content": "",
                                "reasoning_content": [
                                    {"type": "text", "text": '{"verdict": "true", "score": 90}'},
                                ],
                            },
                        },
                    ],
                },
            )
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            resp = await c.chat.completions.create(model="grok", messages=[], temperature=0)
            assert "verdict" in resp.choices[0].message.content
        finally:
            await c.aclose()


@pytest.mark.asyncio
async def test_grok_chat_client_uses_bearer_auth_header():
    captured: dict = {}

    def side_effect(request: httpx.Request) -> httpx.Response:
        captured["headers"] = dict(request.headers)
        return httpx.Response(200, json={"choices": [{"message": {"content": "ok"}}]})

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(side_effect=side_effect)
        c = GrokChatClient(url="https://example.com/v1/chat", api_key="secret-token")
        try:
            await c.chat.completions.create(model="grok", messages=[], temperature=0)
        finally:
            await c.aclose()
    assert captured["headers"].get("authorization") == "Bearer secret-token"
    assert "api-key" not in {k.lower() for k in captured["headers"]}


@pytest.mark.asyncio
async def test_grok_chat_client_sends_max_completion_tokens_and_top_p():
    captured: dict = {}

    def side_effect(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content.decode())
        return httpx.Response(200, json={"choices": [{"message": {"content": "{}"}}]})

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(side_effect=side_effect)
        c = GrokChatClient(
            url="https://example.com/v1/chat",
            api_key="k",
            max_completion_tokens=2048,
        )
        try:
            await c.chat.completions.create(
                model="m",
                messages=[{"role": "user", "content": "x"}],
                response_format={"type": "json_object"},
                temperature=0,
            )
        finally:
            await c.aclose()
    assert "response_format" not in captured["body"]
    assert captured["body"].get("stream") is False
    assert captured["body"].get("top_p") == 1
    assert captured["body"].get("max_completion_tokens") == 2048


@pytest.mark.asyncio
async def test_grok_chat_client_retries_on_503(monkeypatch):
    monkeypatch.setattr("backend.llm_clients.asyncio.sleep", AsyncMock())

    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            side_effect=[
                httpx.Response(503, text="unavailable"),
                httpx.Response(200, json={"choices": [{"message": {"content": "recovered"}}]}),
            ]
        )
        c = GrokChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            resp = await c.chat.completions.create(model="m", messages=[], temperature=0)
            assert resp.choices[0].message.content == "recovered"
        finally:
            await c.aclose()


def test_create_client_dispatch_openai_and_azure_inference():
    oa = create_client(
        ModelConfig(provider="openai", model="m", api_key="k", base_url="https://api.openai.com/v1")
    )
    assert type(oa).__name__ == "AsyncOpenAI"

    inf = create_client(
        ModelConfig(
            provider="azure_inference",
            model="m",
            api_key="k",
            base_url="https://example.com/v1/chat/completions",
        )
    )
    assert isinstance(inf, HttpChatClient)

    grok = create_client(
        ModelConfig(
            provider="azure_inference",
            model="m",
            api_key="k",
            base_url="https://example.com/v1/chat/completions",
            client_kind="grok",
            grok_max_completion_tokens=4000,
        )
    )
    assert isinstance(grok, GrokChatClient)
