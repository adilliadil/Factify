"""Tests for `backend.llm_clients` (HTTP shim and client factory)."""

import json

import httpx
import pytest
import respx

from backend.config import ModelConfig
from backend.llm_clients import HttpChatClient, create_client


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
async def test_http_chat_client_passes_response_format():
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
    assert captured["body"]["response_format"] == {"type": "json_object"}


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
async def test_http_chat_client_http_error_raises():
    with respx.mock:
        respx.post("https://example.com/v1/chat").mock(
            return_value=httpx.Response(429, text="rate limited")
        )
        c = HttpChatClient(url="https://example.com/v1/chat", api_key="k")
        try:
            with pytest.raises(httpx.HTTPStatusError):
                await c.chat.completions.create(model="m", messages=[], temperature=0)
        finally:
            await c.aclose()


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
