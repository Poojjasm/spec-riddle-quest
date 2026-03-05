# Tasks: Core Riddle Game

**Input**: Design documents from `/specs/001-core-riddle-game/`
**Prerequisites**: plan.md ✅, spec.md ✅

**Tests**: TDD required per constitution — test tasks are written before implementation tasks.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize uv project with `uv init` and configure `pyproject.toml` with click and pytest dependencies
- [ ] T002 Create source package structure: `src/riddlequest/__init__.py`, `src/riddlequest/__main__.py`, `src/riddlequest/data/` directory
- [ ] T003 [P] Create `tests/` directory with `tests/__init__.py` placeholder
- [ ] T004 Create `.gitignore` for Python/uv artifacts (`__pycache__/`, `*.pyc`, `.venv/`, `dist/`, `*.egg-info/`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data and loader infrastructure that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Create riddle dataset `src/riddlequest/data/riddles.json` with 25+ riddles in `{"question": "...", "answers": [...]}` format
- [ ] T006 [P] Write failing test for riddle loader in `tests/test_loader.py` (test: file loads, returns list of dicts with question+answers keys)
- [ ] T007 Implement `src/riddlequest/loader.py` with `load_riddles()` using `importlib.resources` — make T006 tests pass
- [ ] T008 [P] Write failing tests for answer checking in `tests/test_game.py` (test: case-insensitive, whitespace-trimmed matching)
- [ ] T009 Implement `src/riddlequest/game.py` with `check_answer(user_input, answers)` and `Session` class — make T008 tests pass

**Checkpoint**: `uv run pytest tests/test_loader.py tests/test_game.py` must pass before user story work begins

---

## Phase 3: User Story 1 - Play a Complete Riddle Session (Priority: P1) 🎯 MVP

**Goal**: Player can run `uv run python -m riddlequest play`, answer riddles, and see final score

**Independent Test**: `uv run python -m riddlequest play --count 3` produces 3 riddles with feedback and a score

### Tests for User Story 1 ⚠️ Write FIRST — must FAIL before implementation

- [ ] T010 [P] [US1] Write failing CLI integration test for `play` command in `tests/test_cli.py` (test: play with mocked input produces score output)

### Implementation for User Story 1

- [ ] T011 [US1] Implement `src/riddlequest/cli.py` with click group and `play` subcommand (depends on T009, T010)
- [ ] T012 [US1] Add `--count` option to `play` command; add shuffle logic in `game.py`
- [ ] T013 [US1] Implement `src/riddlequest/__main__.py` entry point calling `cli()`
- [ ] T014 [US1] Add `riddlequest` entry point script in `pyproject.toml` and verify `uv run riddlequest play` works
- [ ] T015 [US1] Verify all T010 tests pass with `uv run pytest tests/test_cli.py::test_play`

**Checkpoint**: `uv run python -m riddlequest play --count 5` works end-to-end with score display

---

## Phase 4: User Story 2 - List Riddles (Priority: P2)

**Goal**: Player can run `uv run python -m riddlequest list` to see all riddle questions

**Independent Test**: `uv run python -m riddlequest list` prints numbered riddle questions with no answers visible

### Tests for User Story 2 ⚠️ Write FIRST

- [ ] T016 [P] [US2] Write failing test for `list` command in `tests/test_cli.py` (test: output contains questions, no answers)

### Implementation for User Story 2

- [ ] T017 [US2] Add `list` subcommand to `src/riddlequest/cli.py` (depends on T016)
- [ ] T018 [US2] Verify T016 tests pass with `uv run pytest tests/test_cli.py::test_list`

**Checkpoint**: `uv run python -m riddlequest list` works independently of `play`

---

## Phase 5: User Story 3 - Single Random Riddle (Priority: P3)

**Goal**: Player can run `uv run python -m riddlequest one` for a single riddle

**Independent Test**: `uv run python -m riddlequest one` presents one riddle, accepts answer, shows result, exits

### Tests for User Story 3 ⚠️ Write FIRST

- [ ] T019 [P] [US3] Write failing test for `one` command in `tests/test_cli.py` (test: exactly one riddle presented, feedback shown)

### Implementation for User Story 3

- [ ] T020 [US3] Add `one` subcommand to `src/riddlequest/cli.py` (depends on T019)
- [ ] T021 [US3] Verify T019 tests pass with `uv run pytest tests/test_cli.py::test_one`

**Checkpoint**: All three subcommands (`play`, `list`, `one`) work independently

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T022 [P] Run full test suite `uv run pytest` — all tests must pass
- [ ] T023 Add `README.md` at repo root documenting how to run the game (`uv run python -m riddlequest --help`)
- [ ] T024 [P] Verify edge cases: empty answer re-prompts; graceful error if data missing

---

## Dependencies & Execution Order

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: After Phase 1 — BLOCKS all user stories
- **Phase 3 (US1 play)**: After Phase 2
- **Phase 4 (US2 list)**: After Phase 2 — independent of US1
- **Phase 5 (US3 one)**: After Phase 2 — independent of US1, US2
- **Phase 6 (Polish)**: After all user stories complete

### Parallel Opportunities

- T003, T004 can run in parallel with T002
- T006, T008 can run in parallel (different test files)
- T010, T016, T019 can run in parallel (different test functions)
- US1, US2, US3 implementation can proceed in parallel after Phase 2

---

## Implementation Strategy

### MVP (User Story 1 only)
1. Phase 1: Setup → Phase 2: Foundational → Phase 3: US1 play command
2. Validate: `uv run python -m riddlequest play` works
3. Then add US2 (list) and US3 (one) incrementally

### TDD Cycle for Each Task
1. Write failing test
2. Run `uv run pytest` — confirm failure
3. Implement minimum code to pass
4. Run `uv run pytest` — confirm passing
5. Commit
