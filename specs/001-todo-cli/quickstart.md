# Quickstart: In-Memory Todo CLI Application

**Feature**: 001-todo-cli
**Date**: 2025-12-30

## Prerequisites

- Python 3.13 or higher installed
- UV package manager (optional, for environment management)
- Terminal/command prompt access

## Installation

### Option 1: Direct Python (Simplest)

```bash
# Clone or download the repository
cd TODO-APP

# Run the application
python src/main.py
```

### Option 2: Using UV (Recommended)

```bash
# Clone or download the repository
cd TODO-APP

# Initialize UV environment (if not already done)
uv init

# Run the application
uv run python src/main.py
```

## Running the Application

1. Open your terminal
2. Navigate to the project root directory
3. Run: `python src/main.py`

You should see the main menu:

```text
=== To-Do Application ===
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

## Feature Walkthrough

### Adding a Task

1. Select option `1` from the menu
2. Enter a task title (required)
3. Enter a description (optional, press Enter to skip)
4. Success message confirms task creation

```text
Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs

Task added successfully! (ID: 1)
```

### Viewing Tasks

1. Select option `2` from the menu
2. All tasks display with ID, title, description, and status

```text
Enter your choice (1-6): 2

=== Your Tasks ===
[ID: 1] Buy groceries - Milk, bread, eggs [Incomplete]
```

If no tasks exist:

```text
No tasks found.
```

### Updating a Task

1. Select option `3` from the menu
2. Enter the task ID to update
3. Enter new title (press Enter to keep existing)
4. Enter new description (press Enter to keep existing)

```text
Enter your choice (1-6): 3

Enter task ID to update: 1
Enter new title (press Enter to keep current): Buy food
Enter new description (press Enter to keep current):

Task updated successfully!
```

### Deleting a Task

1. Select option `4` from the menu
2. Enter the task ID to delete
3. Confirmation message displayed

```text
Enter your choice (1-6): 4

Enter task ID to delete: 1

Task deleted successfully.
```

### Marking Complete/Incomplete

1. Select option `5` from the menu
2. Enter the task ID to toggle
3. Status changes from Incomplete → Complete (or vice versa)

```text
Enter your choice (1-6): 5

Enter task ID to mark complete/incomplete: 1

Task marked as Complete.
```

### Exiting

1. Select option `6` from the menu
2. Application displays goodbye message and exits

```text
Enter your choice (1-6): 6

Goodbye!
```

## Error Handling

The application handles errors gracefully:

| Error | Example Input | Message |
|-------|---------------|---------|
| Empty title | (blank) | "Task title cannot be empty." |
| Invalid ID format | "abc" | "Please enter a valid number." |
| Non-existent ID | 999 | "Task not found." |
| Invalid menu choice | "7" or "hello" | "Invalid choice. Please try again." |

## Important Notes

- **No Persistence**: All tasks are stored in memory only. When you exit the application, all tasks are lost.
- **Session-Based**: This is a single-session application. Close and reopen to start fresh.
- **Sequential IDs**: Task IDs start at 1 and increment. Deleted task IDs are not reused.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "python not found" | Ensure Python 3.13+ is installed and in PATH |
| Module not found | Run from the project root directory |
| Unicode errors | Ensure terminal supports UTF-8 |

## Demo Script

For live demos, use this sequence:

1. Start application
2. View tasks (shows empty state)
3. Add task: "Prepare presentation"
4. Add task: "Review code"
5. View tasks (shows both tasks)
6. Mark task 1 as complete
7. View tasks (shows updated status)
8. Update task 2 description
9. Delete task 1
10. View tasks (shows remaining task)
11. Exit

This demonstrates all 5 core features in ~2 minutes.
