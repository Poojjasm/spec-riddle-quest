# Feature Specification: Core Riddle Game

**Feature Branch**: `001-core-riddle-game`
**Created**: 2026-03-05
**Status**: Draft
**Input**: User description: "Core riddle game: display riddles, accept player answers, track score within session, show result at end"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Play a Complete Riddle Session (Priority: P1)

A player launches the game from the command line and is presented with riddles one at a time.
For each riddle, the player types their answer and receives immediate feedback (correct/incorrect
along with the actual answer if wrong). At the end of the session, the player sees their final
score (e.g., "You got 7 out of 10 correct!").

**Why this priority**: This is the core game loop — without it, the product delivers zero value.
All other features depend on this foundation.

**Independent Test**: Can be fully tested by launching the CLI, answering a series of riddles,
and verifying correct/incorrect feedback plus a final score summary are displayed.

**Acceptance Scenarios**:

1. **Given** the game is launched, **When** a riddle is displayed, **Then** the player sees
   the riddle text and a prompt to enter their answer.
2. **Given** a player types a correct answer, **When** they press Enter, **Then** the game
   shows "Correct!" and increments the score.
3. **Given** a player types an incorrect answer, **When** they press Enter, **Then** the game
   shows "Wrong! The answer was: [correct answer]".
4. **Given** all riddles in a session have been answered, **When** the session ends,
   **Then** the game displays the final score and a friendly message.
5. **Given** a player's answer differs only in case or leading/trailing whitespace,
   **When** they submit, **Then** it is still counted as correct (case-insensitive matching).

---

### User Story 2 - Browse Riddles Without Playing (Priority: P2)

A player can list all available riddles (questions only, no answers) so they can preview
the game content before committing to a full session.

**Why this priority**: Nice-to-have for graders to quickly inspect the riddle database.
Delivers value without the full game loop.

**Independent Test**: Can be tested by running the list command and verifying riddle questions
are displayed without answers.

**Acceptance Scenarios**:

1. **Given** the player runs the list command, **When** riddles are available,
   **Then** all riddle questions are printed, numbered, with no answers revealed.
2. **Given** the player runs the list command, **When** no riddles exist in the data file,
   **Then** the program outputs a friendly message saying no riddles are available.

---

### User Story 3 - Quick Single Riddle Mode (Priority: P3)

A player can request one random riddle at a time from the command line, answer it, and see
the result without committing to a full multi-riddle session.

**Why this priority**: Useful for quick fun; extends replayability. Depends on core game
infrastructure from P1.

**Independent Test**: Can be tested by running the single-riddle command, providing an answer,
and verifying feedback is shown.

**Acceptance Scenarios**:

1. **Given** the player runs the single-riddle command, **When** executed, **Then** one
   random riddle is presented and the player can answer it.
2. **Given** the player answers the single riddle, **When** they submit, **Then** correct/incorrect
   feedback is shown and the program exits cleanly.

---

### Edge Cases

- What happens when the player enters an empty answer? → Prompt again with "Please enter an answer."
- What happens when the riddle data file is missing or empty? → Display a clear error message and exit gracefully.
- What happens when the player types a partial answer? → Only exact (case-insensitive, whitespace-trimmed) matches count; partial matches are incorrect.
- How does the system handle a session where there are fewer riddles than the requested count? → Use all available riddles without repetition.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display riddles one at a time during a session, in a shuffled order.
- **FR-002**: System MUST accept a text answer from the player for each riddle.
- **FR-003**: System MUST compare answers case-insensitively with leading/trailing whitespace stripped.
- **FR-004**: System MUST display "Correct!" when the answer matches, and "Wrong! The answer was: [answer]" when it does not.
- **FR-005**: System MUST track and display the score (correct answers / total riddles) at the end of a session.
- **FR-006**: System MUST load riddles from a bundled data file within the project directory.
- **FR-007**: System MUST provide a `list` subcommand that shows all riddle questions (no answers).
- **FR-008**: System MUST provide a `play` subcommand that starts a full riddle session.
- **FR-009**: System MUST provide a `one` subcommand that presents a single random riddle.
- **FR-010**: System MUST exit gracefully with a helpful message if the riddle data is missing or empty.
- **FR-011**: Users MUST be able to specify how many riddles to play via a `--count` option on the `play` command (default: all).

### Key Entities

- **Riddle**: A question-answer pair. Has a question (string) and one or more acceptable answers (list of strings).
- **Session**: A single play-through. Tracks which riddles were asked, answers given, and current score.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Players can complete a 10-riddle session in under 5 minutes of actual playing time.
- **SC-002**: All 100% of correct answers (case-insensitive, trimmed) are recognized as correct.
- **SC-003**: Final score is always displayed accurately as "X out of Y correct".
- **SC-004**: The program exits with code 0 on normal completion and non-zero on error.
- **SC-005**: All functional requirements have passing pytest tests before implementation is considered done.

## Assumptions

- Riddles are stored as a JSON file bundled with the package (e.g., `data/riddles.json`).
- At least 20 riddles will be included in the initial data set.
- A "session" is one continuous run of the `play` command; no persistence between runs is required.
- Answer matching is case-insensitive with whitespace trimming; no fuzzy matching.
