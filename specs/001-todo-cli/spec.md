# Feature Specification: In-Memory Todo CLI Application

**Feature Branch**: `001-todo-cli`
**Created**: 2025-12-30
**Status**: Complete
**Input**: User description: "In-Memory Todo Python Console App (Phase I)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Task (Priority: P1)

As a user, I want to add a new task to my todo list so that I can track items I need to complete.

**Why this priority**: Adding tasks is the foundational operation. Without it, no other features can be demonstrated or tested.

**Independent Test**: Can be fully tested by running the app, selecting "Add Task", entering a title and optional description, and verifying the task appears in the list with a unique ID and "incomplete" status.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** I select "Add Task" and enter "Buy groceries" as the title, **Then** a new task is created with a unique ID, the title "Buy groceries", status "incomplete", and a success message is displayed.
2. **Given** I am adding a task, **When** I enter "Buy groceries" as title and "Milk, bread, eggs" as description, **Then** the task is created with both title and description stored.
3. **Given** I am adding a task, **When** I leave the description empty and press Enter, **Then** the task is created with an empty description (description is optional).
4. **Given** I am adding a task, **When** I enter an empty or whitespace-only title, **Then** an error message is displayed and no task is created.

---

### User Story 2 - View All Tasks (Priority: P1)

As a user, I want to view all tasks in my todo list so that I can see what needs to be done and what has been completed.

**Why this priority**: Viewing tasks is essential for verifying all other operations and provides the primary interface for task management.

**Independent Test**: Can be fully tested by adding tasks and then selecting "View Tasks" to verify all tasks display with correct ID, title, description, and status.

**Acceptance Scenarios**:

1. **Given** tasks exist in the list, **When** I select "View Tasks", **Then** all tasks are displayed showing ID, title, description (if any), and completion status.
2. **Given** no tasks exist, **When** I select "View Tasks", **Then** a message "No tasks found." is displayed.
3. **Given** multiple tasks exist with different statuses, **When** I view tasks, **Then** each task clearly shows whether it is "Complete" or "Incomplete".

---

### User Story 3 - Mark Task Complete/Incomplete (Priority: P2)

As a user, I want to mark tasks as complete or incomplete so that I can track my progress on tasks.

**Why this priority**: Toggling completion status is the core value proposition of a todo app, enabling progress tracking.

**Independent Test**: Can be fully tested by adding a task, marking it complete, verifying the status change, then marking it incomplete again and verifying it toggles back.

**Acceptance Scenarios**:

1. **Given** an incomplete task with ID 1 exists, **When** I select "Mark Complete/Incomplete" and enter ID 1, **Then** the task status changes to "Complete" and a confirmation message is displayed.
2. **Given** a complete task with ID 1 exists, **When** I select "Mark Complete/Incomplete" and enter ID 1, **Then** the task status changes to "Incomplete" and a confirmation message is displayed.
3. **Given** I enter an ID that does not exist, **When** I try to mark complete/incomplete, **Then** an error message "Task not found." is displayed.
4. **Given** I enter non-numeric input for the ID, **When** I try to mark complete/incomplete, **Then** an error message "Please enter a valid number." is displayed.

---

### User Story 4 - Update Task (Priority: P2)

As a user, I want to update an existing task's title or description so that I can correct mistakes or add more details.

**Why this priority**: Updates allow users to refine tasks without deleting and recreating them, improving usability.

**Independent Test**: Can be fully tested by adding a task, updating its title and/or description, and verifying the changes appear in the task list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** I select "Update Task", enter ID 1, and provide a new title "Updated title", **Then** the task title is updated and a success message is displayed.
2. **Given** a task with ID 1 exists, **When** I update only the description (leaving title unchanged by pressing Enter), **Then** only the description is updated.
3. **Given** a task with ID 1 exists, **When** I update only the title (leaving description unchanged by pressing Enter), **Then** only the title is updated.
4. **Given** I enter an ID that does not exist, **When** I try to update, **Then** an error message "Task not found." is displayed.
5. **Given** I try to update a task with an empty title (when title is being changed), **When** I submit, **Then** an error message is displayed and the update is rejected.

---

### User Story 5 - Delete Task (Priority: P2)

As a user, I want to delete a task so that I can remove tasks that are no longer relevant.

**Why this priority**: Deletion allows users to clean up their task list and remove completed or irrelevant items.

**Independent Test**: Can be fully tested by adding a task, deleting it by ID, and verifying it no longer appears in the task list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** I select "Delete Task" and enter ID 1, **Then** the task is removed and a success message "Task deleted successfully." is displayed.
2. **Given** I enter an ID that does not exist, **When** I try to delete, **Then** an error message "Task not found." is displayed.
3. **Given** I enter non-numeric input for the ID, **When** I try to delete, **Then** an error message "Please enter a valid number." is displayed.

---

### User Story 6 - Application Navigation (Priority: P1)

As a user, I want a clear menu system so that I can easily navigate between features and exit the application.

**Why this priority**: The menu is the entry point for all features and critical for usability.

**Independent Test**: Can be fully tested by verifying the menu displays all options, handles invalid choices gracefully, and exits cleanly.

**Acceptance Scenarios**:

1. **Given** the application starts, **When** the main menu displays, **Then** all options are shown: Add Task, View Tasks, Update Task, Delete Task, Mark Complete/Incomplete, Exit.
2. **Given** I am at the main menu, **When** I select "Exit", **Then** the application displays "Goodbye!" and terminates cleanly.
3. **Given** I am at the main menu, **When** I enter an invalid choice, **Then** an error message "Invalid choice. Please try again." is displayed and the menu is shown again.

---

### Edge Cases

- **Empty title validation**: Whitespace-only titles (e.g., "   ") are treated as empty and rejected.
- **ID uniqueness**: Task IDs are assigned sequentially starting from 1 and never reused within a session.
- **Non-numeric ID input**: All ID inputs are validated; non-numeric entries display a friendly error.
- **Case sensitivity**: Menu choices accept both numeric (1-6) input for selection.
- **Maximum tasks**: No explicit limit on number of tasks (limited only by available memory).
- **Special characters**: Titles and descriptions may contain any printable characters.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display a numbered menu with options: 1. Add Task, 2. View Tasks, 3. Update Task, 4. Delete Task, 5. Mark Complete/Incomplete, 6. Exit.
- **FR-002**: System MUST allow users to add a task with a required title and optional description.
- **FR-003**: System MUST assign each new task a unique numeric ID (sequential, starting from 1).
- **FR-004**: System MUST set new tasks to "incomplete" status by default.
- **FR-005**: System MUST display all tasks showing ID, title, description, and status.
- **FR-006**: System MUST show "No tasks found." when viewing an empty task list.
- **FR-007**: System MUST allow updating a task's title and/or description by ID.
- **FR-008**: System MUST allow deleting a task by ID.
- **FR-009**: System MUST toggle task status between complete and incomplete by ID.
- **FR-010**: System MUST validate that task titles are non-empty (reject empty or whitespace-only).
- **FR-011**: System MUST validate that ID inputs are numeric and correspond to existing tasks.
- **FR-012**: System MUST display clear error messages for all invalid operations.
- **FR-013**: System MUST return to the main menu after completing any operation.
- **FR-014**: System MUST exit gracefully when the Exit option is selected.

### Key Entities

- **Task**: Represents a todo item with the following attributes:
  - `id`: Unique numeric identifier (integer, auto-assigned, starts at 1)
  - `title`: Task name (string, required, non-empty)
  - `description`: Additional details (string, optional, may be empty)
  - `status`: Completion state (boolean or enum: "complete" / "incomplete")

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, view, update, delete, and toggle completion on tasks within a single session.
- **SC-002**: All 5 core task operations complete successfully with valid input.
- **SC-003**: 100% of invalid inputs (empty titles, non-numeric IDs, non-existent IDs) produce clear error messages without crashing.
- **SC-004**: Users can navigate all features using the menu within 3 interactions (menu → action → result).
- **SC-005**: Application starts and displays the menu in under 1 second.
- **SC-006**: A first-time user can successfully add and view a task without documentation (intuitive interface).

## Out of Scope

The following are explicitly **NOT** included in Phase I:

- Data persistence (files, databases)
- Task priorities or due dates
- Task categories or tags
- Search or filter functionality
- Multi-user support
- Undo/redo operations
- Task sorting options
- Recurring tasks
- Notifications or reminders
- Any web, API, or GUI interface

## Assumptions

- Users interact via a terminal/command prompt that supports standard input/output.
- The application runs in a single session; all data is lost when the application exits.
- Task IDs are assigned sequentially and are never reused during a session.
- The application assumes a single user at a time (no concurrent access considerations).
- Menu options are selected by entering the corresponding number.
- Unicode/special characters in titles and descriptions are supported (standard Python string handling).

## Dependencies

- Python 3.13+ runtime environment
- UV for environment management (development dependency)
- No external libraries required (Python standard library only)
