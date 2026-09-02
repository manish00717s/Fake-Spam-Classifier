"""
Unit tests for the NLP preprocessing pipeline.

Run with:
    python -m pytest tests/ -v
"""

import os
import sys

# Make the deployment app package importable.
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "Week_6_Deployment", "app"),
)

from preprocessing import preprocess_text  # noqa: E402


def test_lowercases_and_stems():
    result = preprocess_text("RUNNING running Runs")
    # PorterStemmer reduces run variants to the "run" stem.
    assert "run" in result


def test_removes_stopwords():
    result = preprocess_text("this is a test of the system")
    for stopword in ("this", "is", "a", "of", "the"):
        assert stopword not in result.split()


def test_strips_special_characters():
    result = preprocess_text("Win $$$ CASH now!!! @@@")
    assert "$" not in result
    assert "@" not in result
    assert "!" not in result


def test_empty_string_returns_empty():
    assert preprocess_text("") == ""
    assert preprocess_text("   ") == ""


def test_non_string_input_is_safe():
    assert preprocess_text(None) == ""
    assert preprocess_text(12345) == ""


def test_returns_string_type():
    assert isinstance(preprocess_text("hello world"), str)
