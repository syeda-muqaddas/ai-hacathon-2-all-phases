# Todo CLI Application

A simple command-line todo application built with Python. Phase I implements in-memory task management with 5 core features.

## Features

- **Add Task**: Create new tasks with title and optional description
- **View Tasks**: Display all tasks with ID, title, description, and status
- **Update Task**: Modify existing task title or description
- **Delete Task**: Remove tasks by ID
- **Mark Complete/Incomplete**: Toggle task completion status

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

## Usage

When you start the application, you'll see a menu:

```
001 version not available
=== To-Do Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6):

### 002 version you see this now available


                       ████████╗ ██████╗ ██████╗  ██████╗
                      ╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
                         ██║   ██║   ██║██║  ██║██║   ██║
                         ██║   ██║   ██║██║  ██║██║   ██║
                         ██║   ╚██████╔╝██████╔╝╚██████╔╝
                          ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝

                   Todo CLI v2.0 - Your Productivity Partner


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

> Enter your choice (1-7): 7

  ─────────────────────────────────────

  Thank you for using Todo CLI v2.0!
  Stay productive!

  ─────────────────────────────────────


```

### Adding a Task

1. Select option `1`
2. Enter a task title (required)
3. Enter a description (optional, press Enter to skip)

### Viewing Tasks

Select option `2` to see all tasks with their ID, title, description, and completion status.

### Updating a Task

1. Select option `3`
2. Enter the task ID to update
3. Enter new title (press Enter to keep current)
4. Enter new description (press Enter to keep current)

### Deleting a Task

1. Select option `4`
2. Enter the task ID to delete

### Marking Complete/Incomplete

1. Select option `5`
2. Enter the task ID to toggle its completion status

### Exiting

Select option `6` to exit the application.

## Notes

- This is Phase I: All tasks are stored in memory only
- Tasks are lost when the application exits
- Task IDs are assigned sequentially and never reused within a session

## Project Structure

```
TODO-APP/
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point and menu
│   ├── task.py           # Task class
│   └── task_manager.py   # TaskManager with CRUD operations
├── specs/                # Specifications and planning
├── pyproject.toml
└── README.md
```

## License

This project is part of a hackathon demonstration.
