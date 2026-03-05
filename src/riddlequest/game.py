"""Core game logic: answer checking and session management."""


def check_answer(user_input: str, accepted_answers: list[str]) -> bool:
    """Return True if user_input matches any accepted answer (case-insensitive, stripped)."""
    normalized = user_input.strip().lower()
    if not normalized:
        return False
    return any(normalized == ans.strip().lower() for ans in accepted_answers)


class Session:
    """Tracks a single play-through of riddles."""

    def __init__(self, riddles: list[dict]):
        self.riddles = riddles
        self.total = len(riddles)
        self.score = 0

    def submit_answer(self, riddle_index: int, user_input: str) -> bool:
        """Submit an answer for riddle at riddle_index. Returns True if correct."""
        riddle = self.riddles[riddle_index]
        correct = check_answer(user_input, riddle["answers"])
        if correct:
            self.score += 1
        return correct

    def summary(self) -> str:
        """Return a human-readable score summary."""
        return f"You got {self.score} out of {self.total} correct!"
