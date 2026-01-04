# Tasks: In-Memory Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, quickstart.md

**Tests**: Tests are NOT included (manual testing only per Phase I constitution).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure: src/__init__.py, src/main.py, src/task.py, src/task_manager.py
- [x] T002 [P] Create pyproject.toml with project metadata (name: todo-cli, version: 0.1.0, python: >=3.13)
- [x] T003 [P] Create README.md with project description and run instructions

**Checkpoint**: Project structure ready - foundational implementation can begin

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data model that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task class in src/task.py with attributes: id (int), title (str), description (str), is_complete (bool)
- [x] T005 Add Task.__init__() method with id, title, description="", is_complete=False parameters
- [x] T006 Add Task.__str__() method returning formatted display string per data-model.md
- [x] T007 Create TaskManager class in src/task_manager.py with tasks list and next_id counter
- [x] T008 Add TaskManager.__init__() initializing empty tasks list and next_id=1

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 & 2 - Add Task + View Tasks (Priority: P1)

**Goal**: User can add new tasks and view all tasks in the list

**Independent Test**: Run app → Add Task → Enter title/description → View Tasks → Verify task appears with ID, title, description, status

### Implementation for User Story 1 & 2 (Combined - tightly coupled)

- [x] T009 [US1] Add TaskManager.add_task(title, description="") method in src/task_manager.py returning new Task
- [x] T010 [US1] Implement title validation in add_task(): reject empty/whitespace-only titles
- [x] T011 [US2] Add TaskManager.get_all_tasks() method in src/task_manager.py returning list of all tasks
- [x] T012 [US1] Create add_task_menu() function in src/main.py prompting for title and description
- [x] T013 [US2] Create view_tasks_menu() function in src/main.py displaying all tasks or "No tasks found."

**Checkpoint**: User Story 1 & 2 complete - can add and view tasks

---

## Phase 4: User Story 6 - Application Navigation (Priority: P1)

**Goal**: User can navigate all features via menu and exit cleanly

**Independent Test**: Run app → Verify menu displays → Test invalid input → Test Exit option

### Implementation for User Story 6

- [x] T014 [US6] Create display_menu() function in src/main.py showing all 6 options
- [x] T015 [US6] Create main() function in src/main.py with while True loop and menu dispatch
- [x] T016 [US6] Implement menu input validation: reject non-1-6 input with "Invalid choice. Please try again."
- [x] T017 [US6] Implement Exit option (choice 6): print "Goodbye!" and break loop
- [x] T018 [US6] Add if __name__ == "__main__": main() entry point in src/main.py

**Checkpoint**: User Story 6 complete - full menu navigation working, app can run end-to-end

---

## Phase 5: User Story 3 - Mark Complete/Incomplete (Priority: P2)

**Goal**: User can toggle task completion status

**Independent Test**: Add task → Mark complete → View (shows Complete) → Mark incomplete → View (shows Incomplete)

### Implementation for User Story 3

- [x] T019 [US3] Add TaskManager.get_task_by_id(task_id) method in src/task_manager.py returning Task or None
- [x] T020 [US3] Add TaskManager.toggle_complete(task_id) method in src/task_manager.py returning bool
- [x] T021 [US3] Create toggle_complete_menu() function in src/main.py prompting for task ID
- [x] T022 [US3] Add ID input validation in toggle_complete_menu(): "Please enter a valid number." for non-numeric
- [x] T023 [US3] Add task existence validation: "Task not found." for invalid ID
- [x] T024 [US3] Wire toggle_complete_menu() to menu option 5 in main()

**Checkpoint**: User Story 3 complete - can toggle task status

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: User can update task title and/or description

**Independent Test**: Add task → Update title → View (shows new title) → Update description → View (shows new description)

### Implementation for User Story 4

- [x] T025 [US4] Add TaskManager.update_task(task_id, title=None, description=None) method in src/task_manager.py
- [x] T026 [US4] Implement partial update logic: only update fields that are provided and non-empty
- [x] T027 [US4] Create update_task_menu() function in src/main.py prompting for ID, new title, new description
- [x] T028 [US4] Add title validation in update_task_menu(): reject empty title if user attempts to change it
- [x] T029 [US4] Wire update_task_menu() to menu option 3 in main()

**Checkpoint**: User Story 4 complete - can update tasks

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: User can delete tasks by ID

**Independent Test**: Add task → Delete by ID → View (task gone)

### Implementation for User Story 5

- [x] T030 [US5] Add TaskManager.delete_task(task_id) method in src/task_manager.py returning bool
- [x] T031 [US5] Create delete_task_menu() function in src/main.py prompting for task ID
- [x] T032 [US5] Add ID validation in delete_task_menu(): numeric check and existence check
- [x] T033 [US5] Wire delete_task_menu() to menu option 4 in main()

**Checkpoint**: User Story 5 complete - can delete tasks

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final cleanup and validation

- [x] T034 [P] Verify all error messages match spec exactly (data-model.md validation rules)
- [x] T035 [P] Verify display format matches data-model.md: "[ID: X] Title - Description [Status]"
- [x] T036 Run through quickstart.md demo script to verify all features work end-to-end
- [x] T037 [P] Add docstrings to all public functions and classes

---

## Dependencies & Execution Order

### Phase Dependencies

```text
Phase 1 (Setup)
    ↓
Phase 2 (Foundational) ← BLOCKS all user stories
    ↓
Phase 3 (US1+US2: Add+View) ← MVP Core
    ↓
Phase 4 (US6: Navigation) ← Makes app runnable
    ↓
[Can run in parallel after Phase 4]
├── Phase 5 (US3: Toggle)
├── Phase 6 (US4: Update)
└── Phase 7 (US5: Delete)
    ↓
Phase 8 (Polish)
```

### User Story Dependencies

| Story | Depends On | Can Parallelize With |
|-------|------------|---------------------|
| US1 (Add) | Phase 2 | - |
| US2 (View) | US1 | - |
| US6 (Navigation) | US1, US2 | - |
| US3 (Toggle) | Phase 4 | US4, US5 |
| US4 (Update) | Phase 4 | US3, US5 |
| US5 (Delete) | Phase 4 | US3, US4 |

### Within Each Phase

- Models before services (T004-T008 before T009+)
- Services before CLI functions (T009-T011 before T012-T013)
- Core logic before menu wiring

---

## Parallel Execution Examples

### Phase 1 Parallel Tasks

```text
Parallel group (independent files):
- T002: pyproject.toml
- T003: README.md
```

### Phase 5-7 Parallel Stories

```text
After Phase 4 complete, launch in parallel:
- Phase 5: US3 Toggle (T019-T024)
- Phase 6: US4 Update (T025-T029)
- Phase 7: US5 Delete (T030-T033)
```

---

## Implementation Strategy

### MVP First (Phases 1-4)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (Task + TaskManager)
3. Complete Phase 3: Add + View Tasks
4. Complete Phase 4: Menu Navigation
5. **STOP and VALIDATE**: Test adding and viewing tasks via menu

### Incremental Delivery

1. Phases 1-4 → MVP (Add, View, Menu)
2. Add Phase 5 → Toggle Complete
3. Add Phase 6 → Update Task
4. Add Phase 7 → Delete Task
5. Phase 8 → Polish and validate

---

## Summary

| Phase | Tasks | User Stories | Parallel Opportunities |
|-------|-------|--------------|----------------------|
| 1. Setup | 3 | - | T002, T003 |
| 2. Foundational | 5 | - | None (sequential) |
| 3. Add+View | 5 | US1, US2 | None (dependencies) |
| 4. Navigation | 5 | US6 | None (dependencies) |
| 5. Toggle | 6 | US3 | With Phase 6, 7 |
| 6. Update | 5 | US4 | With Phase 5, 7 |
| 7. Delete | 4 | US5 | With Phase 5, 6 |
| 8. Polish | 4 | - | T034, T035, T037 |

**Total Tasks**: 37
**Completed Tasks**: 37
**Status**: IMPLEMENTATION COMPLETE
