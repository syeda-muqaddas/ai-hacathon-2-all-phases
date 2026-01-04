# Implementation Plan: Enhanced Todo CLI with Professional UI/UX

**Branch**: `002-todo-cli-enhanced-ux` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-todo-cli-enhanced-ux/spec.md`

## Summary

Enhance the existing Phase 1 Todo CLI by adding professional UI/UX elements (ASCII banner, section headers, table display) and extended task attributes (priority, due date, category, tags). Includes a new statistics dashboard feature. All enhancements maintain backward compatibility with existing functionality while improving demo-readiness and user experience.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory (Python list/dictionary)
**Testing**: Manual CLI testing (no test framework required for Phase I)
**Target Platform**: Any platform with Python 3.13+ (Windows, macOS, Linux)
**Project Type**: Single project
**Performance Goals**: Menu displays in <1 second, instant response to user input
**Constraints**: No persistence, no external libraries, no async, CLI only
**Scale/Scope**: Single user, single session, unlimited tasks (memory-bound)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Evidence |
|-----------|--------|----------|
| I. Spec-First Development | PASS | Specification created and approved before planning |
| II. AI-Generated Implementation | PASS | All code will be generated via Claude Code |
| III. Beginner-Friendly Design | PASS | Simple patterns: string formatting, loops, ASCII output |
| IV. Deterministic Behavior | PASS | No randomness, same input = same output |
| V. Appropriate Simplicity (YAGNI) | PASS | Extensions only to meet spec, no premature abstractions |
| VI. Full Traceability | PASS | PHRs created, tasks will trace to spec |

**Phase I Constraints Check**:

| Constraint | Status | Evidence |
|------------|--------|----------|
| CLI only | PASS | Uses input() and print() only |
| In-memory only | PASS | Python list storage, no file/DB |
| Python only | PASS | Python files in src/ |
| Standard library only | PASS | datetime module is standard library |
| Core features preserved | PASS | Add, View, Update, Delete, Mark Complete unchanged |

**Gate Status**: ALL GATES PASSED

## Project Structure

### Documentation (this feature)

```text
specs/002-todo-cli-enhanced-ux/
├── spec.md              # Feature specification (created)
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py          # Package marker
├── main.py              # Entry point with enhanced menu loop and UI
├── task.py              # Extended Task class with new attributes
├── task_manager.py      # Extended TaskManager with statistics
├── ui.py                # NEW: UI helper functions (banner, headers, tables)
└── statistics.py        # NEW: Statistics computation functions

tests/                   # Reserved for future phases
```

**Structure Decision**: Extend single project structure from Phase 1. Add two new modules (`ui.py` for display helpers, `statistics.py` for stats computation) to maintain separation of concerns while keeping codebase simple. All existing files (`task.py`, `task_manager.py`, `main.py`) are modified rather than replaced.

## Complexity Tracking

> No violations detected. Design follows YAGNI principles.

| Aspect | Decision | Justification |
|--------|----------|---------------|
| File structure | 5 files (3 existing + 2 new) | Separation of concerns without over-engineering |
| Data storage | Extended Python list | Same approach as Phase 1, just more attributes |
| UI helpers | Dedicated ui.py module | Keeps main.py focused on flow, UI code reusable |
| Statistics | Dedicated statistics.py | Clear boundary for computational logic |
| Date handling | datetime standard library | Simplest approach for YYYY-MM-DD comparison |

## Design Artifacts

### Phase 0: Research (Complete)

See [research.md](./research.md) for:
- ASCII banner implementation decision
- Table formatting approach
- UTF-8 symbol choices
- Date comparison strategy
- Extended attribute storage design

### Phase 1: Data Model (Complete)

See [data-model.md](./data-model.md) for:
- Extended Task entity definition
- TaskStatus computation logic
- Statistics computation formulas
- Visual element specifications (banner, headers, tables)
- Validation rules

### Phase 1: Quickstart (Complete)

See [quickstart.md](./quickstart.md) for:
- Step-by-step demo script
- Expected output examples
- Error handling scenarios

## Implementation Strategy

### Approach: Incremental Enhancement

1. **Extend Task Class First** - Add new attributes with defaults for backward compatibility
2. **Add UI Module** - Create display helpers before modifying main.py
3. **Enhance Main Flow** - Update each menu function one at a time
4. **Add Statistics Last** - New feature added after core enhancements complete

### Key Design Decisions

1. **Backward Compatibility**: New Task attributes have defaults so existing code works
2. **UI Module Separation**: Display logic extracted to ui.py for reusability
3. **Status Computation**: Derived from is_complete + due_date, not stored
4. **Statistics On-Demand**: Computed when viewed, not cached

### Risk Mitigations

| Risk | Mitigation |
|------|------------|
| UTF-8 display issues | Documented assumption; ASCII fallback possible |
| Terminal width issues | Designed for 80-char; truncation handles overflow |
| Date parsing errors | Lenient validation; comparison fails gracefully |
| Breaking existing behavior | Extensive default values; original methods preserved |

## Phase Boundaries

| Phase | Content | Status |
|-------|---------|--------|
| Phase 0 | research.md | COMPLETE |
| Phase 1 | data-model.md, quickstart.md | COMPLETE |
| Phase 2 | tasks.md | PENDING (`/sp.tasks` command) |

## Next Steps

Run `/sp.tasks` to generate implementation tasks based on this plan.

**Recommended Task Organization**:
1. Extend Task class with new attributes
2. Create ui.py with display helpers
3. Update TaskManager for extended attributes
4. Enhance main.py menu functions
5. Create statistics.py module
6. Add statistics menu option
7. Polish and validate against quickstart.md
