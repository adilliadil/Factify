"""Guard against dual-loading ``evals/conftest.py`` (breaks ``store_benchmark_result`` vs hooks)."""

import sys
from pathlib import Path


def test_evals_dir_has_no_init_py():
    """PEP 420: ``evals`` must be a namespace package so pytest loads a single ``conftest`` module."""
    evals_root = Path(__file__).resolve().parent
    assert not (evals_root / "__init__.py").is_file(), (
        "Remove evals/__init__.py — otherwise conftest can load twice (conftest vs evals.conftest) "
        "and benchmark hooks miss stored results."
    )


def test_conftest_not_loaded_twice_as_distinct_modules():
    """After ``import conftest``, there must be no separate ``evals.conftest`` module object."""
    evals_dir = str(Path(__file__).resolve().parent)
    if evals_dir not in sys.path:
        sys.path.insert(0, evals_dir)

    # Import the evals-local conftest (same as pytest when ``evals/`` is on ``sys.path``).
    import conftest as conftest_mod  # noqa: PLC0415

    main = sys.modules["conftest"]
    assert main is conftest_mod
    # If evals/__init__.py exists, pytest may register evals.conftest as a different object.
    assert sys.modules.get("evals.conftest", main) is main
