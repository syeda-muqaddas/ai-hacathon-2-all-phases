"""Main entry point for the Todo CLI Application v2.0.

Features professional UI/UX with ASCII banner, section headers, table display,
extended task attributes, and statistics dashboard.
"""

from src.task_manager import TaskManager
from src.ui import (
    print_banner,
    print_header,
    print_success,
    print_error,
    print_separator,
    print_task_table,
    print_statistics_dashboard,
)
from src.statistics import compute_statistics


def parse_priority(user_input: str) -> str:
    """Convert user input to priority string.

    Args:
        user_input: User's priority selection ("1", "2", "3", "4" or priority name)

    Returns:
        Priority string: "High", "Medium", "Low", or "None"
    """
    user_input = user_input.strip().lower()

    if user_input in ("1", "high"):
        return "High"
    elif user_input in ("2", "medium"):
        return "Medium"
    elif user_input in ("3", "low"):
        return "Low"
    else:
        return "None"


def parse_tags(user_input: str) -> list[str]:
    """Parse comma-separated tags input into a list.

    Args:
        user_input: Comma-separated tags string

    Returns:
        List of trimmed, non-empty tag strings
    """
    if not user_input or not user_input.strip():
        return []

    # Split by comma, trim each, filter empty
    tags = [tag.strip() for tag in user_input.split(",")]
    return [tag for tag in tags if tag]


def display_menu() -> None:
    """Display the main menu with section headers and grouping."""
    print_header("MAIN MENU")

    print("  [ Task Operations ]")
    print_separator()
    print("  1. Add Task")
    print("  2. View Tasks")
    print()

    print("  [ Task Management ]")
    print_separator()
    print("  3. Update Task")
    print("  4. Delete Task")
    print("  5. Mark Complete/Incomplete")
    print()

    print("  [ Insights ]")
    print_separator()
    print("  6. Statistics")
    print()

    print_separator()
    print("  7. Exit")
    print()


def add_task_menu(manager: TaskManager) -> None:
    """Prompt user to add a new task with extended attributes.

    Args:
        manager: The TaskManager instance
    """
    print_header("ADD TODO")

    # Required: Title
    title = input("> Enter task title: ")
    if not title or not title.strip():
        print_error("Task title cannot be empty.")
        return

    # Optional: Description
    description = input("> Enter description (optional): ")

    # Optional: Priority
    print()
    print("  Priority options: 1=High, 2=Medium, 3=Low, 4=None")
    priority_input = input("> Enter priority [4]: ")
    priority = parse_priority(priority_input)

    # Optional: Due date
    due_date = input("> Enter due date (YYYY-MM-DD) or press Enter to skip: ")

    # Optional: Category
    category = input("> Enter category or press Enter to skip: ")

    # Optional: Tags
    tags_input = input("> Enter tags (comma-separated) or press Enter to skip: ")
    tags = parse_tags(tags_input)

    # Create the task
    task = manager.add_task(
        title=title,
        description=description,
        priority=priority,
        due_date=due_date,
        category=category,
        tags=tags
    )

    print()
    if task:
        print_success(f"Task added successfully! (ID: {task.id})")
    else:
        print_error("Task title cannot be empty.")


def view_tasks_menu(manager: TaskManager) -> None:
    """Display all tasks in a formatted table.

    Args:
        manager: The TaskManager instance
    """
    print_header("ALL TODOS")

    tasks = manager.get_all_tasks()

    if not tasks:
        print("  No tasks found.")
        return

    print_task_table(tasks)


def update_task_menu(manager: TaskManager) -> None:
    """Prompt user to update an existing task with all attributes.

    Args:
        manager: The TaskManager instance
    """
    print_header("UPDATE TODO")

    task_id_input = input("> Enter task ID to update: ")

    # Validate ID is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print_error("Please enter a valid number.")
        return

    # Check if task exists
    task = manager.get_task_by_id(task_id)
    if task is None:
        print_error("Task not found.")
        return

    # Display current values
    print()
    print("  Current values:")
    print(f"    Title:       {task.title}")
    print(f"    Description: {task.description if task.description else '(none)'}")
    print(f"    Priority:    {task.priority}")
    print(f"    Due Date:    {task.due_date if task.due_date else '(none)'}")
    print(f"    Category:    {task.category if task.category else '(none)'}")
    print(f"    Tags:        {', '.join(task.tags) if task.tags else '(none)'}")
    print()

    # Prompt for updates (Enter to keep current)
    new_title = input("> Enter new title (press Enter to keep): ")
    new_description = input("> Enter new description (press Enter to keep): ")

    print("  Priority options: 1=High, 2=Medium, 3=Low, 4=None")
    new_priority_input = input("> Enter new priority or Enter to keep: ")

    new_due_date = input("> Enter new due date (YYYY-MM-DD) or Enter to keep: ")
    new_category = input("> Enter new category or Enter to keep: ")
    new_tags_input = input("> Enter new tags (comma-separated) or Enter to keep: ")

    # Determine what to update (None means keep current)
    title_to_update = new_title if new_title else None
    description_to_update = new_description if new_description else None
    priority_to_update = parse_priority(new_priority_input) if new_priority_input else None
    due_date_to_update = new_due_date if new_due_date else None
    category_to_update = new_category if new_category else None
    tags_to_update = parse_tags(new_tags_input) if new_tags_input else None

    # If user entered something for title but it's only whitespace, reject
    if new_title and not new_title.strip():
        print_error("Task title cannot be empty.")
        return

    # Check if any updates were provided
    if all(x is None for x in [title_to_update, description_to_update, priority_to_update,
                                due_date_to_update, category_to_update, tags_to_update]):
        print("  No changes made.")
        return

    # Update the task
    success = manager.update_task(
        task_id=task_id,
        title=title_to_update,
        description=description_to_update,
        priority=priority_to_update,
        due_date=due_date_to_update,
        category=category_to_update,
        tags=tags_to_update
    )

    print()
    if success:
        print_success("Task updated successfully!")
    else:
        print_error("Task title cannot be empty.")


def delete_task_menu(manager: TaskManager) -> None:
    """Prompt user to delete a task.

    Args:
        manager: The TaskManager instance
    """
    print_header("DELETE TODO")

    task_id_input = input("> Enter task ID to delete: ")

    # Validate ID is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print_error("Please enter a valid number.")
        return

    # Delete the task
    success = manager.delete_task(task_id)

    print()
    if success:
        print_success("Task deleted successfully.")
    else:
        print_error("Task not found.")


def toggle_complete_menu(manager: TaskManager) -> None:
    """Prompt user to toggle task completion status.

    Args:
        manager: The TaskManager instance
    """
    print_header("MARK COMPLETE/INCOMPLETE")

    task_id_input = input("> Enter task ID to toggle: ")

    # Validate ID is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print_error("Please enter a valid number.")
        return

    # Get current status to report after toggle
    task = manager.get_task_by_id(task_id)
    if task is None:
        print_error("Task not found.")
        return

    # Toggle the status
    manager.toggle_complete(task_id)

    # Report new status
    new_status = "Complete" if task.is_complete else "Incomplete"
    print()
    print_success(f"Task marked as {new_status}.")


def statistics_menu(manager: TaskManager) -> None:
    """Display the statistics dashboard.

    Args:
        manager: The TaskManager instance
    """
    print_header("STATISTICS")

    tasks = manager.get_all_tasks()

    if not tasks:
        print("  No tasks to analyze.")
        return

    stats = compute_statistics(tasks)
    print_statistics_dashboard(stats)


def main() -> None:
    """Main application loop with professional UI/UX."""
    manager = TaskManager()

    # Display startup banner
    print_banner()

    while True:
        display_menu()
        choice = input("> Enter your choice (1-7): ")

        if choice == "1":
            add_task_menu(manager)
        elif choice == "2":
            view_tasks_menu(manager)
        elif choice == "3":
            update_task_menu(manager)
        elif choice == "4":
            delete_task_menu(manager)
        elif choice == "5":
            toggle_complete_menu(manager)
        elif choice == "6":
            statistics_menu(manager)
        elif choice == "7":
            print()
            print_separator()
            print()
            print("  Thank you for using Todo CLI v2.0!")
            print("  Stay productive!")
            print()
            print_separator()
            print()
            break
        else:
            print_error("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
