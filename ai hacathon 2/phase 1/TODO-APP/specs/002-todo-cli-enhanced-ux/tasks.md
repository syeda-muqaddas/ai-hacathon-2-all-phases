# Tasks: Enhanced Todo CLI with Professional UI/UX

**Input**: Design documents from `/specs/002-todo-cli-enhanced-ux/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, quickstart.md, research.md

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

## Phase 1: Setup (No New Files)

**Purpose**: This feature extends existing Phase 1 codebase - no new project setup required.

- [x] T001 Verify existing src/task.py, src/task_manager.py, src/main.py are present and functional
- [x] T002 Verify Python 3.13+ environment is active

**Checkpoint**: Existing codebase verified - enhancement work can begin ✓

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core enhancements that MUST be complete before ANY user story UI work can begin

**CRITICAL**: No user story work can begin until this phase is complete

### 2.1 Extended Task Model

- [x] T003 Add priority attribute to Task class in src/task.py with default "None"
- [x] T004 Add due_date attribute to Task class in src/task.py with default ""
- [x] T005 Add category attribute to Task class in src/task.py with default ""
- [x] T006 Add tags attribute to Task class in src/task.py with default []
- [x] T007 Update Task.__init__() in src/task.py to accept new optional parameters

### 2.2 UI Module (NEW)

- [x] T008 [P] Create src/ui.py with ASCII_BANNER constant (per data-model.md)
- [x] T009 [P] Add print_banner() function in src/ui.py to display centered banner
- [x] T010 [P] Add print_header(title) function in src/ui.py for section headers with ═ borders
- [x] T011 [P] Add print_success(message) function in src/ui.py with ✓ prefix
- [x] T012 [P] Add print_error(message) function in src/ui.py with ⚠ prefix
- [x] T013 [P] Add print_separator() function in src/ui.py for menu group separators
- [x] T014 Add get_status_symbol(task) function in src/ui.py returning ✓/☐/✗ based on is_complete and overdue
- [x] T015 Add is_overdue(task) helper function in src/ui.py using datetime comparison
- [x] T016 Add truncate_string(text, max_length) function in src/ui.py for table columns

### 2.3 Extended TaskManager

- [x] T017 Update TaskManager.add_task() in src/task_manager.py to accept priority, due_date, category, tags
- [x] T018 Update TaskManager.update_task() in src/task_manager.py to handle new attributes

**Checkpoint**: Foundation ready - user story implementation can now begin ✓

---

## Phase 3: User Story 1 + 2 - Startup & Menu (Priority: P1)

**Goal**: Professional startup display with ASCII banner and enhanced menu navigation

**Independent Test**: Launch app → Verify banner displays centered → Verify menu shows section headers and grouping

### Implementation for US1 + US2 (Combined - tightly coupled)

- [x] T019 [US1] Add startup sequence to main() in src/main.py: call print_banner() on launch
- [x] T020 [US1] Add app header display after banner in src/main.py
- [x] T021 [US2] Refactor display_menu() in src/main.py to use print_header("MAIN MENU")
- [x] T022 [US2] Add menu group labels to display_menu() in src/main.py: "Task Operations", "Task Management", "Insights"
- [x] T023 [US2] Add visual separators between menu groups in display_menu() using print_separator()
- [x] T024 [US2] Update menu numbering to 1-7 (adding Statistics option 6, Exit becomes 7) in src/main.py
- [x] T025 [US2] Update main() loop in src/main.py to handle new menu options 1-7

**Checkpoint**: US1 + US2 complete - app shows professional startup and menu ✓

---

## Phase 4: User Story 3 - Add Task with Extended Attributes (Priority: P1)

**Goal**: User can add tasks with priority, due date, category, and tags

**Independent Test**: Add Task → Enter all optional fields → Verify task stored with all attributes

### Implementation for US3

- [x] T026 [US3] Add print_header("ADD TODO") call to add_task_menu() in src/main.py
- [x] T027 [US3] Add priority prompt (1=High, 2=Medium, 3=Low, 4=None) to add_task_menu() in src/main.py
- [x] T028 [US3] Add parse_priority(input) helper function in src/main.py to convert input to priority string
- [x] T029 [US3] Add due date prompt to add_task_menu() in src/main.py
- [x] T030 [US3] Add category prompt to add_task_menu() in src/main.py
- [x] T031 [US3] Add tags prompt (comma-separated) to add_task_menu() in src/main.py
- [x] T032 [US3] Add parse_tags(input) helper function in src/main.py to split and trim tags
- [x] T033 [US3] Update add_task_menu() to pass all new fields to manager.add_task() in src/main.py
- [x] T034 [US3] Update success message to use print_success("Task added successfully! (ID: X)") in src/main.py

**Checkpoint**: US3 complete - can add tasks with all extended attributes ✓

---

## Phase 5: User Story 4 - View Tasks in Table Layout (Priority: P1)

**Goal**: Display tasks in professional ASCII table with aligned columns

**Independent Test**: Add multiple tasks → View Tasks → Verify table with headers, borders, aligned columns

### Implementation for US4

- [x] T035 [US4] Add print_header("ALL TODOS") call to view_tasks_menu() in src/main.py
- [x] T036 [US4] Add print_task_table(tasks) function in src/ui.py with column headers (ID, S, Title, Priority, Due Date, Category)
- [x] T037 [US4] Implement table row formatting with | borders and column widths per data-model.md in src/ui.py
- [x] T038 [US4] Add table header separator row (+----+---+...) in print_task_table() in src/ui.py
- [x] T039 [US4] Integrate get_status_symbol() for Status column in print_task_table() in src/ui.py
- [x] T040 [US4] Add title truncation (27 chars + "...") in print_task_table() using truncate_string() in src/ui.py
- [x] T041 [US4] Add summary row after table: "Total: X | ✓ Completed: X | ☐ Pending: X | ✗ Overdue: X" in src/ui.py
- [x] T042 [US4] Refactor view_tasks_menu() in src/main.py to use print_task_table()

**Checkpoint**: US4 complete - tasks display in professional table format ✓

---

## Phase 6: User Story 5 - Visual Task Status Symbols (Priority: P2)

**Goal**: Consistent status symbols across all task displays

**Independent Test**: Create tasks in different states → Verify ✓/☐/✗ symbols appear correctly

### Implementation for US5

- [x] T043 [US5] Verify get_status_symbol() handles Complete (✓), Pending (☐), Overdue (✗) in src/ui.py
- [x] T044 [US5] Verify is_overdue() correctly compares YYYY-MM-DD dates with today in src/ui.py
- [x] T045 [US5] Add fallback for invalid date format in is_overdue() (treat as not overdue) in src/ui.py

**Checkpoint**: US5 complete - status symbols work correctly ✓

---

## Phase 7: User Story 6 - Statistics Dashboard (Priority: P2)

**Goal**: Show completion progress, counts, priority/category breakdowns

**Independent Test**: Add tasks with various attributes → View Statistics → Verify all metrics display

### Implementation for US6

- [x] T046 [P] [US6] Create src/statistics.py with compute_statistics(tasks) function returning dict of metrics
- [x] T047 [US6] Implement total_count, completed_count, incomplete_count in compute_statistics() in src/statistics.py
- [x] T048 [US6] Implement completion_percentage calculation in compute_statistics() in src/statistics.py
- [x] T049 [US6] Implement priority_breakdown dict in compute_statistics() in src/statistics.py
- [x] T050 [US6] Implement category_breakdown dict in compute_statistics() in src/statistics.py
- [x] T051 [US6] Implement overdue_count in compute_statistics() in src/statistics.py
- [x] T052 [US6] Add print_statistics_dashboard(stats) function in src/ui.py with bordered sections
- [x] T053 [US6] Add progress bar visualization in print_statistics_dashboard() using █ and ░ characters in src/ui.py
- [x] T054 [US6] Create statistics_menu() function in src/main.py calling compute_statistics and print_statistics_dashboard
- [x] T055 [US6] Wire statistics_menu() to menu option 6 in main() loop in src/main.py

**Checkpoint**: US6 complete - statistics dashboard shows all metrics ✓

---

## Phase 8: User Story 7 - Update Task with Extended Attributes (Priority: P2)

**Goal**: User can update all task attributes including new fields

**Independent Test**: Create task → Update each attribute → Verify changes saved

### Implementation for US7

- [x] T056 [US7] Add print_header("UPDATE TODO") call to update_task_menu() in src/main.py
- [x] T057 [US7] Display current task values (including new attributes) before prompts in update_task_menu() in src/main.py
- [x] T058 [US7] Add priority update prompt to update_task_menu() in src/main.py
- [x] T059 [US7] Add due_date update prompt to update_task_menu() in src/main.py
- [x] T060 [US7] Add category update prompt to update_task_menu() in src/main.py
- [x] T061 [US7] Add tags update prompt to update_task_menu() in src/main.py
- [x] T062 [US7] Update call to manager.update_task() to include new attributes in src/main.py
- [x] T063 [US7] Use print_success() for success message in update_task_menu() in src/main.py

**Checkpoint**: US7 complete - can update all task attributes ✓

---

## Phase 9: User Story 8 - Friendly Feedback Messages (Priority: P2)

**Goal**: Consistent success/error messages with symbols across all operations

**Independent Test**: Perform all operations → Verify ✓ success and ⚠ error messages

### Implementation for US8

- [x] T064 [US8] Update delete_task_menu() in src/main.py: add print_header("DELETE TODO"), use print_success/print_error
- [x] T065 [US8] Update toggle_complete_menu() in src/main.py: add print_header("MARK COMPLETE/INCOMPLETE"), use print_success/print_error
- [x] T066 [US8] Update main() error handling to use print_error("Invalid choice. Please try again.") in src/main.py
- [x] T067 [US8] Verify all input validation uses print_error() consistently across all menu functions in src/main.py

**Checkpoint**: US8 complete - all feedback messages use consistent symbols ✓

---

## Phase 10: User Story 9 - Consistent Visual Layout (Priority: P3)

**Goal**: Polish all screens for visual consistency and professional appearance

**Independent Test**: Navigate through all screens → Verify consistent headers, spacing, prompts

### Implementation for US9

- [x] T068 [US9] Standardize input prompt format to "> " prefix across all menu functions in src/main.py
- [x] T069 [US9] Verify all section headers use print_header() with consistent formatting in src/main.py
- [x] T070 [US9] Add consistent vertical spacing (blank lines) between sections in all menu functions in src/main.py
- [x] T071 [US9] Add goodbye message with separator on exit in src/main.py

**Checkpoint**: US9 complete - all screens have consistent professional appearance ✓

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and cleanup

- [x] T072 [P] Add docstrings to all new functions in src/ui.py
- [x] T073 [P] Add docstrings to all new functions in src/statistics.py
- [x] T074 [P] Update docstrings for modified functions in src/task.py
- [x] T075 [P] Update docstrings for modified functions in src/task_manager.py
- [x] T076 Run through quickstart.md demo script to verify all features work end-to-end
- [x] T077 Verify all error messages match spec exactly (data-model.md validation rules)
- [x] T078 Verify Task backward compatibility: tasks created with title-only still work

---

## Implementation Complete

**Total Tasks**: 78 (T001-T078)
**Completed**: 78
**Status**: ✓ ALL PHASES COMPLETE

### Files Created/Modified

| File | Action | Description |
|------|--------|-------------|
| src/task.py | Modified | Extended with priority, due_date, category, tags |
| src/task_manager.py | Modified | Extended add_task/update_task for new attributes |
| src/ui.py | Created | ASCII banner, headers, table, status symbols, feedback |
| src/statistics.py | Created | Statistics computation functions |
| src/main.py | Modified | Enhanced menu, all user story implementations |

### Verification

- All Python files compile successfully
- All functions have docstrings
- All user stories implemented (US1-US9)
- Backward compatibility maintained
