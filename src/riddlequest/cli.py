"""Riddle Quest CLI — play, list, and one subcommands."""
import random
import click
from riddlequest.loader import load_riddles
from riddlequest.game import Session, check_answer


@click.group()
def cli():
    """Riddle Quest - Test your wits with classic riddles!"""


@cli.command()
@click.option("--count", default=0, help="Number of riddles to play (default: all).")
def play(count: int):
    """Play a riddle session. Answer riddles and see your final score."""
    riddles = load_riddles()
    random.shuffle(riddles)
    if count > 0:
        riddles = riddles[:count]

    if not riddles:
        click.echo("No riddles available. Please check the data file.")
        raise SystemExit(1)

    session = Session(riddles)
    click.echo(f"\n🧩 Welcome to Riddle Quest! You have {session.total} riddle(s) to solve.\n")

    for i, riddle in enumerate(riddles, start=1):
        click.echo(f"Riddle {i}/{session.total}:")
        click.echo(f"  {riddle['question']}")

        while True:
            answer = click.prompt("  Your answer").strip()
            if not answer:
                click.echo("  Please enter an answer.")
                continue
            break

        if session.submit_answer(i - 1, answer):
            click.echo("  ✅ Correct!\n")
        else:
            correct = riddle["answers"][0]
            click.echo(f"  ❌ Wrong! The answer was: {correct}\n")

    click.echo("─" * 40)
    click.echo(f"🏁 Game over! {session.summary()}")
    if session.score == session.total:
        click.echo("🎉 Perfect score! You're a riddle master!")
    elif session.score >= session.total // 2:
        click.echo("👏 Good job! Keep practicing!")
    else:
        click.echo("🤔 Better luck next time!")


@cli.command(name="list")
def list_riddles():
    """List all available riddle questions (no answers shown)."""
    riddles = load_riddles()
    if not riddles:
        click.echo("No riddles available.")
        return
    click.echo(f"\n📚 Available Riddles ({len(riddles)} total):\n")
    for i, riddle in enumerate(riddles, start=1):
        click.echo(f"{i}. {riddle['question']}")
    click.echo()


@cli.command()
def one():
    """Get one random riddle to answer."""
    riddles = load_riddles()
    if not riddles:
        click.echo("No riddles available.")
        raise SystemExit(1)

    riddle = random.choice(riddles)
    click.echo(f"\n🧩 {riddle['question']}")

    while True:
        answer = click.prompt("Your answer").strip()
        if not answer:
            click.echo("Please enter an answer.")
            continue
        break

    if check_answer(answer, riddle["answers"]):
        click.echo("✅ Correct!")
    else:
        click.echo(f"❌ Wrong! The answer was: {riddle['answers'][0]}")
