<!-- Sync Impact Report
Version change: N/A → 1.0.0 (initial ratification)
Added sections: Core Principles, Technology Standards, Development Workflow, Governance
Templates reviewed: plan-template.md ✅, spec-template.md ✅, tasks-template.md ✅
Follow-up TODOs: None - all placeholders resolved
-->

# Riddle Quest Constitution

## Core Principles

### I. uv-First Python Packaging (NON-NEGOTIABLE)

uv MUST be used for all Python packaging, dependency management, and script execution.
No other packaging tools (pip, pipenv, poetry, conda) are permitted.
All commands run via `uv run`, all dependencies declared in `pyproject.toml`.
New dependencies MUST be added with `uv add`, never manually edited.

**Rationale**: uv provides fast, reproducible environments; consistency across all developer machines
is non-negotiable for a graded project.

### II. CLI Interface

The project MUST expose all functionality through a command-line interface.
Text in/out protocol: command-line arguments and stdin → stdout, errors → stderr.
Output MUST be human-readable by default.
The program MUST be runnable with `uv run python -m riddlequest` or equivalent entry point.

**Rationale**: The assignment requires a CLI program; graders must be able to run it
immediately after cloning.

### III. Test-Driven Development (NON-NEGOTIABLE)

pytest MUST be used for all testing; no other test framework is permitted.
Red-Green-Refactor cycle MUST be enforced: tests written → tests fail → implementation → tests pass.
Every functional requirement MUST have at least one corresponding test.
Tests MUST be run with `uv run pytest` and MUST pass before any feature is considered complete.

**Rationale**: The assignment explicitly requires pytest and TDD; automated testing prevents
regressions as features are added.

### IV. Simplicity (YAGNI)

Start with the simplest solution that satisfies requirements.
No abstractions for hypothetical future use; no over-engineering.
Maximum 3 layers: CLI → logic → data. No frameworks when stdlib suffices.
Complexity MUST be justified against a simpler rejected alternative.

**Rationale**: Simple code is easier to grade, debug, and extend; complexity must earn its keep.

### V. Self-Contained & Offline

The program MUST NOT read or write files outside the directory in which it is invoked.
The program MUST NOT access the network.
All data (riddles, etc.) MUST be bundled in the repository.
File I/O is restricted to the current working directory or the package's own data directory.

**Rationale**: Assignment constraints; graders must be able to run offline after cloning.

## Technology Standards

- **Language**: Python 3.11+
- **Packaging**: uv + pyproject.toml (MANDATORY)
- **Testing**: pytest (MANDATORY)
- **Data**: JSON files bundled in the package
- **No external network calls, no databases, no file I/O outside project directory**

## Development Workflow

1. Run `/speckit.specify` to create a feature specification on a new branch.
2. Run `/speckit.plan` to produce a technical implementation plan.
3. Run `/speckit.tasks` to generate an ordered task list.
4. Run `/speckit.implement` to execute the tasks using TDD.
5. Commit after each Spec Kit command produces output.
6. Merge feature branch back to main when implementation is complete and tests pass.

All PRs/merges MUST verify that `uv run pytest` passes with zero failures.

## Governance

This constitution supersedes all other practices for this project.
Amendments require: documentation of change, bump of CONSTITUTION_VERSION, update of LAST_AMENDED_DATE.
Any deviation from uv, pytest, or TDD principles MUST be documented with justification.
All code MUST comply with Principle V (self-contained/offline) without exception.

**Version**: 1.0.0 | **Ratified**: 2026-03-05 | **Last Amended**: 2026-03-05
