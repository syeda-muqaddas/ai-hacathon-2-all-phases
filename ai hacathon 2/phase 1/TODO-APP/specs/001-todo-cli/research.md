# Research: In-Memory Todo CLI Application

**Feature**: 001-todo-cli
**Date**: 2025-12-30
**Status**: Complete (no clarifications needed)

## Overview

This document captures research findings and design decisions for the In-Memory Todo CLI Application. Given the simplicity of Phase I requirements and the explicit technology constraints in the constitution, minimal research was required.

## Research Tasks

### 1. Python CLI Menu Patterns

**Decision**: Use `while True` loop with `if/elif/else` chain

**Rationale**:
- Most beginner-friendly pattern for menu-driven applications
- Clear control flow, easy to read and debug
- Allows clean `break` for exit
- No external dependencies required

**Alternatives Considered**:
- `match/case` (Python 3.10+): Slightly more elegant but less familiar to beginners
- Dictionary dispatch: More advanced pattern, adds unnecessary complexity for 6 menu options
- Class-based state machine: Over-engineered for this use case

### 2. In-Memory Data Storage

**Decision**: Use a Python list to store Task objects, with a class-level counter for ID generation

**Rationale**:
- List provides O(n) lookup by ID, acceptable for expected scale
- Simple iteration for viewing all tasks
- Easy deletion and modification
- No external dependencies

**Alternatives Considered**:
- Dictionary keyed by ID: Faster lookup, but adds complexity; list is sufficient
- Named tuples: Immutable, would complicate updates
- Dataclasses: Good option, but simple class is clearer for beginners

### 3. Task ID Generation

**Decision**: Sequential integer counter starting at 1, managed by TaskManager class

**Rationale**:
- Simple, predictable, deterministic
- Human-readable IDs (1, 2, 3...)
- Counter never resets within session (IDs are not reused when tasks deleted)
- Aligns with spec requirement for unique numeric IDs

**Alternatives Considered**:
- UUID: Over-engineered, not human-friendly
- Array index: Breaks when tasks are deleted
- Timestamp: Over-complicated for this use case

### 4. Input Validation Approach

**Decision**: Validate at point of input using try/except for type conversion, strip() for whitespace

**Rationale**:
- Immediate feedback to user
- Prevents invalid data from entering the system
- Simple pattern: validate → process or show error → return to menu

**Alternatives Considered**:
- Validation decorators: Over-engineered
- Separate validation layer: Adds files and complexity unnecessarily

### 5. Error Message Strategy

**Decision**: Consistent, user-friendly error messages defined as constants

**Rationale**:
- Deterministic output (same error = same message)
- Easy to test against expected messages
- Centralized for consistency

**Error Messages Defined**:
- `"Task not found."` - Invalid ID
- `"Please enter a valid number."` - Non-numeric input
- `"Task title cannot be empty."` - Empty/whitespace title
- `"Invalid choice. Please try again."` - Invalid menu selection

## Technology Decisions Summary

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Menu pattern | while True + if/elif | Beginner-friendly, clear |
| Storage | Python list | Simple, sufficient |
| ID strategy | Sequential counter | Deterministic, readable |
| Task representation | Simple class | Clear, mutable |
| Validation | Inline try/except | Immediate feedback |
| Output | f-strings | Clean, readable |

## Constitution Compliance Verification

All research decisions verified against constitution principles:

- **Principle III (Beginner-Friendly)**: All patterns are simple, idiomatic Python
- **Principle IV (Deterministic)**: No randomness, no external state
- **Principle V (YAGNI)**: No over-engineering, simplest solutions chosen
- **Phase I Constraints**: No libraries, no persistence, CLI only

## Open Questions

None. All requirements are clear and all technical decisions have been made.

## References

- Python documentation: input(), print(), list operations
- PEP 8 Style Guide (for code formatting)
- Constitution v1.0.0 (for constraints)
