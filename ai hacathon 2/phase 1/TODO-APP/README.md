# Todo CLI Application

A professional command-line todo application built with Python. Features an enhanced UI/UX with ASCII art, extended task attributes, table display, and statistics dashboard.

## Version History

### v2.0 - Enhanced UI/UX (002-todo-cli-enhanced-ux)

Professional interface with extended task management capabilities:

- **ASCII Art Banner**: Professional startup display with centered banner
- **Extended Task Attributes**: Priority (High/Medium/Low), Due Date, Category, Tags
- **Table Display**: Tasks shown in aligned ASCII table with column headers
- **Visual Status Symbols**: ✓ Complete, ☐ Pending, ✗ Overdue
- **Statistics Dashboard**: Completion progress bar, priority/category breakdowns
- **Section Headers**: Organized menu with grouped options
- **Friendly Feedback**: Consistent ✓ success and ⚠ error messages

### v1.0 - Core Features (001-todo-cli)

Basic in-memory task management:

- Add Task with title and description
- View Tasks list
- Update Task details
- Delete Task by ID
- Mark Complete/Incomplete toggle

## Requirements

- Python 3.13 or higher

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd TODO-APP

# Optional: Create virtual environment with UV
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Running the Application

```bash
# Run as a Python module (recommended)
python3 -m src.main

# Or with UV
uv run python -m src.main
```

## v2.0 Interface

### Startup Banner

```
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ████████╗ ██████╗ ██████╗  ██████╗      ██████╗██╗     ██╗               ║
║   ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗    ██╔════╝██║     ██║               ║
║      ██║   ██║   ██║██║  ██║██║   ██║    ██║     ██║     ██║               ║
║      ██║   ██║   ██║██║  ██║██║   ██║    ██║     ██║     ██║               ║
║      ██║   ╚██████╔╝██████╔╝╚██████╔╝    ╚██████╗███████╗██║               ║
║      ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝      ╚═════╝╚══════╝╚═╝               ║
║                                                                            ║
║                      Your Personal Task Manager v2.0                       ║
╚════════════════════════════════════════════════════════════════════════════╝
```

### Main Menu

```
╔════════════════════════════════════════════════════════════════════════════╗
║                                MAIN MENU                                   ║
╚════════════════════════════════════════════════════════════════════════════╝

  [ Task Operations ]
  ──────────────────────────────────────
  1. Add Task
  2. View Tasks

  [ Task Management ]
  ──────────────────────────────────────
  3. Update Task
  4. Delete Task
  5. Mark Complete/Incomplete

  [ Insights ]
  ──────────────────────────────────────
  6. Statistics

  ──────────────────────────────────────
  7. Exit

> Enter your choice (1-7):
```

### Task Table Display

```
╔════════════════════════════════════════════════════════════════════════════╗
║                                ALL TODOS                                   ║
╚════════════════════════════════════════════════════════════════════════════╝

+----+---+------------------------------+----------+------------+--------------+
| ID | S |            Title             | Priority |  Due Date  |   Category   |
+----+---+------------------------------+----------+------------+--------------+
|  1 | ✓ | Complete project proposal    |   High   | 2025-01-15 |     Work     |
|  2 | ☐ | Review documentation         |  Medium  | 2025-01-20 |     Work     |
|  3 | ✗ | Submit expense report        |   Low    | 2024-12-30 |   Personal   |
+----+---+------------------------------+----------+------------+--------------+

Total: 3 | ✓ Completed: 1 | ☐ Pending: 1 | ✗ Overdue: 1
```

### Statistics Dashboard

```
╔════════════════════════════════════════════════════════════════════════════╗
║                               STATISTICS                                   ║
╚════════════════════════════════════════════════════════════════════════════╝

  Completion Progress
  ──────────────────────────────────────
  [████████████████████░░░░░░░░░░░░░░░░] 45%

  Task Counts
  ──────────────────────────────────────
  Total:     10
  Completed:  4
  Pending:    5
  Overdue:    1

  Priority Breakdown
  ──────────────────────────────────────
  High:   3
  Medium: 4
  Low:    2
  None:   1

  Category Breakdown
  ──────────────────────────────────────
  Work:     5
  Personal: 3
  Health:   2
```

## Usage Guide

### Adding a Task (v2.0)

1. Select option `1`
2. Enter task title (required)
3. Enter description (optional)
4. Select priority: 1=High, 2=Medium, 3=Low, 4=None
5. Enter due date in YYYY-MM-DD format (optional)
6. Enter category (optional)
7. Enter tags as comma-separated values (optional)

### Viewing Tasks

Select option `2` to see all tasks in a formatted table with:
- ID column
- Status symbol (✓/☐/✗)
- Title (truncated if too long)
- Priority level
- Due date
- Category

### Updating a Task (v2.0)

1. Select option `3`
2. Enter task ID
3. View current values
4. Update any field (press Enter to keep current value):
   - Title, Description, Priority, Due Date, Category, Tags

### Deleting a Task

1. Select option `4`
2. Enter task ID to delete

### Toggling Complete/Incomplete

1. Select option `5`
2. Enter task ID to toggle

### Viewing Statistics

Select option `6` to see:
- Visual completion progress bar
- Task counts (total, completed, pending, overdue)
- Priority distribution
- Category distribution

### Exiting

Select option `7` to exit with a friendly goodbye message.

## Notes

- All tasks are stored in memory only (Phase I limitation)
- Tasks are lost when the application exits
- Task IDs are assigned sequentially and never reused within a session
- Overdue detection compares due dates with current system date
- UTF-8 terminal required for status symbols

## Project Structure

```
TODO-APP/
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point and enhanced menu
│   ├── task.py           # Task class with extended attributes
│   ├── task_manager.py   # TaskManager with CRUD operations
│   ├── ui.py             # UI helpers (banner, headers, tables)
│   └── statistics.py     # Statistics computation functions
├── specs/
│   ├── 001-todo-cli/           # Phase 1 specification
│   └── 002-todo-cli-enhanced-ux/ # Phase 2 specification
├── history/
│   └── prompts/          # Prompt History Records
├── pyproject.toml
└── README.md
```

## Feature Comparison

|    Feature                   | v1.0 | v2.0  |
|------------------------------|------|-------|
| Add/View/Update/Delete Tasks |  ✓   |  ✓   |
| Mark Complete/Incomplete     |  ✓   |  ✓   |
| ASCII Art Banner             |  -    |  ✓  |
| Section Headers              |  -    |  ✓  |
| Table Display                |  -    |  ✓  |
| Priority Levels              |  -    |  ✓  |
| Due Dates                    |  -    |   ✓ |
| Categories                   |  -    |  ✓  |
| Tags                         |  -    |  ✓  |
| Status Symbols(✓/☐/✗)       | -      | ✓  |
| Overdue Detection            |  -    |  ✓  |
| Statistics Dashboard         |  -    |  ✓  |
| Progress Bar                 |  -    |  ✓  |
| Friendly Feedback            |  -    |  ✓  |

## License

This project is part of a hackathon demonstration.
