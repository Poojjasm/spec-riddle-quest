"""Integration tests for CLI commands (TDD - written before implementation)."""
import pytest
from click.testing import CliRunner
from riddlequest.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


class TestPlayCommand:
    def test_play_count_1_shows_one_riddle(self, runner):
        result = runner.invoke(cli, ["play", "--count", "1"], input="anything\n")
        assert result.exit_code == 0
        assert "correct" in result.output.lower() or "wrong" in result.output.lower()

    def test_play_shows_final_score(self, runner):
        result = runner.invoke(cli, ["play", "--count", "2"], input="x\nx\n")
        assert result.exit_code == 0
        assert "out of" in result.output.lower()

    def test_play_correct_answer_recognized(self, runner):
        # Patch riddles to a known set for deterministic testing
        from unittest.mock import patch
        fake_riddles = [{"question": "What is 1+1?", "answers": ["2", "two"]}]
        with patch("riddlequest.cli.load_riddles", return_value=fake_riddles):
            result = runner.invoke(cli, ["play", "--count", "1"], input="2\n")
        assert "correct" in result.output.lower()
        assert result.exit_code == 0

    def test_play_wrong_answer_shows_correct(self, runner):
        from unittest.mock import patch
        fake_riddles = [{"question": "What is 1+1?", "answers": ["2"]}]
        with patch("riddlequest.cli.load_riddles", return_value=fake_riddles):
            result = runner.invoke(cli, ["play", "--count", "1"], input="99\n")
        assert "wrong" in result.output.lower()
        assert "2" in result.output
        assert result.exit_code == 0

    def test_play_empty_answer_reprompts(self, runner):
        from unittest.mock import patch
        fake_riddles = [{"question": "Q?", "answers": ["a"]}]
        with patch("riddlequest.cli.load_riddles", return_value=fake_riddles):
            result = runner.invoke(cli, ["play", "--count", "1"], input="\na\n")
        assert result.exit_code == 0


class TestListCommand:
    def test_list_shows_questions(self, runner):
        result = runner.invoke(cli, ["list"])
        assert result.exit_code == 0
        assert len(result.output.strip()) > 0

    def test_list_numbers_riddles(self, runner):
        result = runner.invoke(cli, ["list"])
        assert "1." in result.output or "1)" in result.output

    def test_list_does_not_show_answers(self, runner):
        from unittest.mock import patch
        fake_riddles = [{"question": "What is the secret?", "answers": ["xyzzy42"]}]
        with patch("riddlequest.cli.load_riddles", return_value=fake_riddles):
            result = runner.invoke(cli, ["list"])
        assert "xyzzy42" not in result.output
        assert "What is the secret?" in result.output


class TestOneCommand:
    def test_one_shows_single_riddle(self, runner):
        from unittest.mock import patch
        fake_riddles = [{"question": "What is 1+1?", "answers": ["2"]}]
        with patch("riddlequest.cli.load_riddles", return_value=fake_riddles):
            result = runner.invoke(cli, ["one"], input="2\n")
        assert result.exit_code == 0
        assert "correct" in result.output.lower() or "wrong" in result.output.lower()

    def test_one_exits_after_single_riddle(self, runner):
        result = runner.invoke(cli, ["one"], input="anything\n")
        assert result.exit_code == 0
