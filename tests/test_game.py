"""Tests for core game logic (TDD - written before implementation)."""
import pytest
from riddlequest.game import check_answer, Session


class TestCheckAnswer:
    def test_exact_match(self):
        assert check_answer("keyboard", ["keyboard"]) is True

    def test_case_insensitive(self):
        assert check_answer("Keyboard", ["keyboard"]) is True
        assert check_answer("KEYBOARD", ["keyboard"]) is True

    def test_whitespace_stripped(self):
        assert check_answer("  keyboard  ", ["keyboard"]) is True
        assert check_answer("\tkeyboard\n", ["keyboard"]) is True

    def test_wrong_answer(self):
        assert check_answer("mouse", ["keyboard"]) is False

    def test_multiple_accepted_answers(self):
        assert check_answer("a keyboard", ["keyboard", "a keyboard"]) is True
        assert check_answer("keyboard", ["keyboard", "a keyboard"]) is True

    def test_empty_answer_is_wrong(self):
        assert check_answer("", ["keyboard"]) is False
        assert check_answer("   ", ["keyboard"]) is False


class TestSession:
    def test_session_initializes_with_riddles(self):
        riddles = [
            {"question": "Q1?", "answers": ["a1"]},
            {"question": "Q2?", "answers": ["a2"]},
        ]
        session = Session(riddles)
        assert session.total == 2
        assert session.score == 0

    def test_session_score_increments_on_correct(self):
        riddles = [{"question": "Q?", "answers": ["answer"]}]
        session = Session(riddles)
        result = session.submit_answer(0, "answer")
        assert result is True
        assert session.score == 1

    def test_session_score_unchanged_on_wrong(self):
        riddles = [{"question": "Q?", "answers": ["answer"]}]
        session = Session(riddles)
        result = session.submit_answer(0, "wrong")
        assert result is False
        assert session.score == 0

    def test_session_summary(self):
        riddles = [
            {"question": "Q1?", "answers": ["a1"]},
            {"question": "Q2?", "answers": ["a2"]},
        ]
        session = Session(riddles)
        session.submit_answer(0, "a1")
        session.submit_answer(1, "wrong")
        summary = session.summary()
        assert "1" in summary
        assert "2" in summary
