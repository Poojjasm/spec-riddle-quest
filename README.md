# Riddle Quest 🧩

A fun command-line riddle guessing game built with Python and Spec Kit.

## Requirements

- [uv](https://docs.astral.sh/uv/) (Python package manager)

## Running the Game

```bash
# Play a full session (all riddles, shuffled)
uv run python -m riddlequest play

# Play with a specific number of riddles
uv run python -m riddlequest play --count 5

# Get a single random riddle
uv run python -m riddlequest one

# List all available riddle questions (no answers)
uv run python -m riddlequest list

# Show help
uv run python -m riddlequest --help
```

## Running Tests

```bash
uv run pytest
```

## How to Play

1. Run `uv run python -m riddlequest play`
2. Read each riddle carefully
3. Type your answer and press Enter
4. Get instant feedback — Correct ✅ or Wrong ❌ (with the real answer)
5. See your final score at the end

Answers are matched case-insensitively with whitespace trimmed.

## Features

- **25 classic riddles** bundled in the package
- **3 game modes**: full session, single riddle, list all
- **Score tracking** within each session
- **Difficulty levels** (easy/medium/hard) — Round 2 feature
- **Hint system** — Round 3 feature

## Project Structure

```
src/riddlequest/
├── cli.py          # Click CLI commands
├── game.py         # Game logic and session tracking
├── loader.py       # Riddle data loading
└── data/
    └── riddles.json    # 25 bundled riddles

tests/
├── test_cli.py     # CLI integration tests
├── test_game.py    # Game logic unit tests
└── test_loader.py  # Data loader tests
```
