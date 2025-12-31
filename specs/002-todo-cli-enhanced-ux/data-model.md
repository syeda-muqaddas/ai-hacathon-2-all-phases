# Data Model: Enhanced Todo CLI with Professional UI/UX

**Feature**: 002-todo-cli-enhanced-ux
**Date**: 2025-12-31

## Entity Definitions

### Task (Extended)

The Task entity is extended from Phase 1 to include additional organizational attributes.

**Attributes**:

| Attribute | Type | Required | Default | Validation |
|-----------|------|----------|---------|------------|
| `id` | `int` | Yes | Auto-assigned | Unique, sequential, starts at 1, never reused |
| `title` | `str` | Yes | - | Non-empty after strip, max display 30 chars |
| `description` | `str` | No | `""` | Any string, empty allowed |
| `is_complete` | `bool` | No | `False` | Boolean value |
| `priority` | `str` | No | `"None"` | One of: "High", "Medium", "Low", "None" |
| `due_date` | `str` | No | `""` | String in YYYY-MM-DD format (lenient validation) |
| `category` | `str` | No | `""` | Any non-empty string, empty allowed |
| `tags` | `list[str]` | No | `[]` | List of trimmed strings, comma-separated input |

**State Transitions**:

```
                    ┌─────────────────┐
                    │    Created      │
                    │ (is_complete=   │
                    │     False)      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
    ┌─────────────────┐     │     ┌─────────────────┐
    │    Updated      │◄────┼────►│   Completed     │
    │ (attributes     │     │     │ (is_complete=   │
    │  modified)      │     │     │     True)       │
    └────────┬────────┘     │     └────────┬────────┘
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                    ┌─────────────────┐
                    │    Deleted      │
                    │ (removed from   │
                    │     list)       │
                    └─────────────────┘
```

### TaskStatus (Computed)

Task status is computed from `is_complete` and `due_date` attributes.

| Status | Condition | Symbol |
|--------|-----------|--------|
| Complete | `is_complete == True` | ✓ |
| Pending | `is_complete == False AND (no due_date OR due_date >= today)` | ☐ |
| Overdue | `is_complete == False AND due_date < today` | ✗ |

### Statistics (Computed)

Statistics are computed on-demand from the task list.

| Metric | Formula |
|--------|---------|
| Total Count | `len(tasks)` |
| Completed Count | `sum(1 for t in tasks if t.is_complete)` |
| Incomplete Count | `total - completed` |
| Completion Percentage | `(completed / total) * 100` (0% if no tasks) |
| Priority Breakdown | `{priority: count for each priority level}` |
| Category Breakdown | `{category: count for each non-empty category}` |
| Overdue Count | `sum(1 for t in tasks if is_overdue(t))` |

## Visual Elements

### ASCII Art Banner

```
████████╗ ██████╗ ██████╗  ██████╗
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
   ██║   ██║   ██║██║  ██║██║   ██║
   ██║   ██║   ██║██║  ██║██║   ██║
   ██║   ╚██████╔╝██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝
```

**Application Header**:
```
              Todo CLI v2.0 - Your Productivity Partner
```

### Section Headers

All section headers follow this format (80 characters wide):

```
════════════════════════════════════════════════════════════════════════════════
                               [SECTION NAME]
════════════════════════════════════════════════════════════════════════════════
```

### Menu Layout

```
════════════════════════════════════════════════════════════════════════════════
                                 MAIN MENU
════════════════════════════════════════════════════════════════════════════════

  [ Task Operations ]
  ─────────────────────────────────────
  1. Add Task
  2. View Tasks

  [ Task Management ]
  ─────────────────────────────────────
  3. Update Task
  4. Delete Task
  5. Mark Complete/Incomplete

  [ Insights ]
  ─────────────────────────────────────
  6. Statistics

  ─────────────────────────────────────
  7. Exit

════════════════════════════════════════════════════════════════════════════════
> Enter your choice (1-7):
```

### Task Table Format

```
════════════════════════════════════════════════════════════════════════════════
                                 ALL TODOS
════════════════════════════════════════════════════════════════════════════════

+----+---+------------------------------+----------+------------+---------------+
| ID | S | Title                        | Priority | Due Date   | Category      |
+----+---+------------------------------+----------+------------+---------------+
|  1 | ✓ | Buy groceries                | High     | 2025-01-05 | Personal      |
|  2 | ☐ | Finish project report        | Medium   | 2025-01-10 | Work          |
|  3 | ✗ | Pay electricity bill         | High     | 2024-12-30 | Bills         |
|  4 | ☐ | Read Python documentation    | Low      |            | Learning      |
+----+---+------------------------------+----------+------------+---------------+

Total: 4 tasks | ✓ Completed: 1 | ☐ Pending: 2 | ✗ Overdue: 1

════════════════════════════════════════════════════════════════════════════════
```

**Column Specifications**:

| Column | Width | Alignment | Truncation |
|--------|-------|-----------|------------|
| ID | 4 | Right | None |
| Status (S) | 3 | Center | None |
| Title | 30 | Left | Truncate with "..." at 27 chars |
| Priority | 10 | Left | None |
| Due Date | 12 | Left | None |
| Category | 15 | Left | Truncate with "..." at 12 chars |

### Statistics Dashboard Layout

```
════════════════════════════════════════════════════════════════════════════════
                                STATISTICS
════════════════════════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         COMPLETION PROGRESS                              │
  │                                                                          │
  │  [████████████████████░░░░░░░░░░░░░░░░░░░░] 42%                         │
  │                                                                          │
  │  Total Tasks: 12  |  ✓ Completed: 5  |  ☐ Pending: 5  |  ✗ Overdue: 2  │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         PRIORITY BREAKDOWN                               │
  │                                                                          │
  │  🔴 High:    3 tasks                                                    │
  │  🟡 Medium:  4 tasks                                                    │
  │  🟢 Low:     3 tasks                                                    │
  │  ⚪ None:    2 tasks                                                    │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         CATEGORY BREAKDOWN                               │
  │                                                                          │
  │  Work:      5 tasks                                                     │
  │  Personal:  4 tasks                                                     │
  │  Bills:     2 tasks                                                     │
  │  Learning:  1 task                                                      │
  └─────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
```

**Note**: Priority symbols (colored circles) are for illustration. Implementation will use ASCII alternatives: `[!]` High, `[+]` Medium, `[-]` Low, `[ ]` None.

### Feedback Messages

**Success Messages**:
```
✓ Task added successfully! (ID: 5)
✓ Task updated successfully!
✓ Task deleted successfully.
✓ Task marked as Complete.
```

**Error Messages**:
```
⚠ Task title cannot be empty.
⚠ Please enter a valid number.
⚠ Task not found.
⚠ Invalid choice. Please try again.
```

### Input Prompts

All input prompts follow consistent format:
```
> Enter your choice (1-7):
> Enter task title:
> Enter priority (1=High, 2=Medium, 3=Low, 4=None) [4]:
> Enter due date (YYYY-MM-DD) or press Enter to skip:
> Enter category or press Enter to skip:
> Enter tags (comma-separated) or press Enter to skip:
```

## Validation Rules

### Title Validation
- Must not be empty after stripping whitespace
- Leading/trailing whitespace is trimmed
- Any printable characters allowed

### Priority Validation
- Input: "1", "2", "3", "4" or "High", "Medium", "Low", "None"
- Case-insensitive matching
- Invalid input defaults to "None"

### Due Date Validation
- Empty input is valid (no due date)
- Format should be YYYY-MM-DD
- Lenient: accept any non-empty string
- Comparison only on display (overdue check)

### Category Validation
- Empty input is valid (no category)
- Any non-empty string accepted
- Leading/trailing whitespace trimmed

### Tags Validation
- Empty input results in empty list
- Comma-separated input
- Each tag trimmed of whitespace
- Empty tags (from ",,") are filtered out

## Backward Compatibility

The extended Task class must maintain backward compatibility with Phase 1:

1. All original attributes preserved (`id`, `title`, `description`, `is_complete`)
2. Original `__str__()` behavior can be replaced with enhanced table display
3. TaskManager methods extended, not replaced
4. Tasks created with only title work correctly (new attributes use defaults)
