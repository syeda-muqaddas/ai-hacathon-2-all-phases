# Data Model: In-Memory Todo CLI Application

**Feature**: 001-todo-cli
**Date**: 2025-12-30
**Source**: [spec.md](./spec.md) Key Entities section

## Entities

### Task

Represents a single todo item in the application.

| Attribute | Type | Required | Default | Validation | Description |
|-----------|------|----------|---------|------------|-------------|
| id | int | Yes | Auto-assigned | Must be positive integer | Unique identifier, sequential starting at 1 |
| title | str | Yes | None | Non-empty, not whitespace-only | Task name/summary |
| description | str | No | "" (empty string) | Any string allowed | Additional details |
| is_complete | bool | Yes | False | Boolean | Completion status |

**Invariants**:
- `id` is assigned by TaskManager and never modified after creation
- `id` values are never reused within a session
- `title` cannot be empty or whitespace-only after strip()
- `is_complete` can only be True or False (toggled via mark operation)

### TaskManager

Manages the collection of tasks and provides CRUD operations.

| Attribute | Type | Description |
|-----------|------|-------------|
| tasks | list[Task] | In-memory storage of all tasks |
| next_id | int | Counter for next task ID (starts at 1) |

**Operations**:

| Method | Input | Output | Description |
|--------|-------|--------|-------------|
| add_task | title: str, description: str = "" | Task | Creates new task with auto-assigned ID |
| get_all_tasks | None | list[Task] | Returns all tasks |
| get_task_by_id | task_id: int | Task or None | Finds task by ID |
| update_task | task_id: int, title: str = None, description: str = None | bool | Updates task fields |
| delete_task | task_id: int | bool | Removes task from list |
| toggle_complete | task_id: int | bool | Toggles task completion status |

## State Transitions

### Task Lifecycle

```text
                    +-------------+
                    |   Created   |
                    | (Incomplete)|
                    +------+------+
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
    +-----------+    +-----------+    +-----------+
    |  Updated  |    |  Toggled  |    |  Deleted  |
    | (same ID) |    | (Complete)|    | (removed) |
    +-----------+    +-----+-----+    +-----------+
          |                |
          |                v
          |          +-----------+
          +--------->|  Toggled  |
                     |(Incomplete)|
                     +-----------+
```

### Status Values

| Status | Display Text | Internal Value |
|--------|--------------|----------------|
| Incomplete | "Incomplete" | is_complete = False |
| Complete | "Complete" | is_complete = True |

## Relationships

```text
+---------------+           +---------------+
|  TaskManager  | 1 ----* > |     Task      |
+---------------+           +---------------+
| - tasks       |           | - id          |
| - next_id     |           | - title       |
+---------------+           | - description |
| + add_task()  |           | - is_complete |
| + get_all()   |           +---------------+
| + get_by_id() |
| + update()    |
| + delete()    |
| + toggle()    |
+---------------+
```

## Validation Rules

### Task Title

| Rule | Validation | Error Message |
|------|------------|---------------|
| Required | title.strip() != "" | "Task title cannot be empty." |
| Whitespace-only | title.strip() != "" | "Task title cannot be empty." |

### Task ID (for operations)

| Rule | Validation | Error Message |
|------|------------|---------------|
| Numeric | isinstance(input, int) or input.isdigit() | "Please enter a valid number." |
| Exists | task_id in [t.id for t in tasks] | "Task not found." |

## Memory Structure

At runtime, the data is organized as:

```python
# TaskManager instance holds:
tasks = [
    Task(id=1, title="Buy groceries", description="Milk, bread", is_complete=False),
    Task(id=2, title="Call mom", description="", is_complete=True),
    Task(id=3, title="Finish report", description="Q4 summary", is_complete=False),
]
next_id = 4  # Next ID to assign
```

## Display Format

When viewing tasks, each task displays as:

```text
[ID: 1] Buy groceries - Milk, bread [Incomplete]
[ID: 2] Call mom [Complete]
[ID: 3] Finish report - Q4 summary [Incomplete]
```

Format rules:
- ID always shown in brackets
- Title always shown
- Description shown after " - " only if non-empty
- Status shown in brackets at end
