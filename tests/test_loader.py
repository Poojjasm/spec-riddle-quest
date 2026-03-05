"""Tests for riddle data loader (TDD - written before implementation)."""
import pytest
from riddlequest.loader import load_riddles


def test_load_riddles_returns_list():
    riddles = load_riddles()
    assert isinstance(riddles, list)


def test_load_riddles_not_empty():
    riddles = load_riddles()
    assert len(riddles) >= 20


def test_riddles_have_question_and_answers():
    riddles = load_riddles()
    for riddle in riddles:
        assert "question" in riddle, f"Missing 'question' key in {riddle}"
        assert "answers" in riddle, f"Missing 'answers' key in {riddle}"


def test_riddle_question_is_string():
    riddles = load_riddles()
    for riddle in riddles:
        assert isinstance(riddle["question"], str)
        assert len(riddle["question"]) > 0


def test_riddle_answers_is_nonempty_list():
    riddles = load_riddles()
    for riddle in riddles:
        assert isinstance(riddle["answers"], list)
        assert len(riddle["answers"]) >= 1
