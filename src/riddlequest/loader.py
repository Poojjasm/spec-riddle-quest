"""Load riddle data from the bundled JSON file."""
import json
import importlib.resources as pkg_resources


def load_riddles() -> list[dict]:
    """Return all riddles as a list of dicts with 'question' and 'answers' keys."""
    data = pkg_resources.files("riddlequest.data").joinpath("riddles.json")
    text = data.read_text(encoding="utf-8")
    return json.loads(text)
