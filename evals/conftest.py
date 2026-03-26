"""Pytest fixtures and mock helpers for evals."""

import json
import time
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from backend.config import config

FIXTURES_DIR = Path(__file__).parent / "datasets"


@pytest.fixture(autouse=True)
def reset_clients_and_delay():
    """Reset API clients and config cache to ensure clean state per test."""
    import backend.search
    import backend.llm
    import judges

    backend.search.client = None
    backend.llm.client = None
    judges._judge_client = None
    config.reset()

    time.sleep(0.3)
    yield
    time.sleep(0.3)


@pytest.fixture
def mock_llm_client():
    """Mock the LLM async client."""
    with patch("backend.llm.get_client") as mock_get:
        mock_client = MagicMock()
        mock_get.return_value = mock_client
        yield mock_client


@pytest.fixture
def mock_tavily_client():
    """Mock the Tavily async client."""
    with patch("backend.search.get_client") as mock_get:
        mock_client = MagicMock()
        mock_get.return_value = mock_client
        yield mock_client


def make_llm_response(content: dict | list) -> MagicMock:
    """Create a mock LLM chat completion response."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = json.dumps(content)
    return mock_response


def load_search_fixture(name: str) -> dict:
    """Load a pre-recorded Tavily search response."""
    fixture_path = FIXTURES_DIR / "search_fixtures" / f"{name}.json"
    with open(fixture_path) as f:
        return json.load(f)


def load_dataset(name: str) -> list[dict]:
    """Load a test dataset (claims.json, analysis.json, etc.)."""
    dataset_path = FIXTURES_DIR / f"{name}.json"
    with open(dataset_path) as f:
        return json.load(f)
