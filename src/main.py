"""Main entry point for the Todo CLI Application."""

from src.task_manager import TaskManager


def display_menu() -> None:
    """Display the main menu options."""
    print("\n=== To-Do Application ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")


def add_task_menu(manager: TaskManager) -> None:
    """Prompt user to add a new task.

    Args:
        manager: The TaskManager instance
    """
    print()
    title = input("Enter task title: ")

    # Validate title
    if not title or not title.strip():
        print("Task title cannot be empty.")
        return

    description = input("Enter task description (optional): ")

    task = manager.add_task(title, description)
    if task:
        print(f"\nTask added successfully! (ID: {task.id})")
    else:
        print("Task title cannot be empty.")


def view_tasks_menu(manager: TaskManager) -> None:
    """Display all tasks.

    Args:
        manager: The TaskManager instance
    """
    tasks = manager.get_all_tasks()

    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n=== Your Tasks ===")
    for task in tasks:
        print(task)


def update_task_menu(manager: TaskManager) -> None:
    """Prompt user to update an existing task.

    Args:
        manager: The TaskManager instance
    """
    print()
    task_id_input = input("Enter task ID to update: ")

    # Validate ID is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Please enter a valid number.")
        return

    # Check if task exists
    task = manager.get_task_by_id(task_id)
    if task is None:
        print("Task not found.")
        return

    print(f"Current title: {task.title}")
    new_title = input("Enter new title (press Enter to keep current): ")

    print(f"Current description: {task.description if task.description else '(none)'}")
    new_description = input("Enter new description (press Enter to keep current): ")

    # Determine what to update
    title_to_update = new_title if new_title else None
    description_to_update = new_description if new_description else None

    # If user entered something for title but it's only whitespace, reject
    if new_title and not new_title.strip():
        print("Task title cannot be empty.")
        return

    # Update the task
    if title_to_update is None and description_to_update is None:
        print("No changes made.")
        return

    success = manager.update_task(task_id, title_to_update, description_to_update)
    if success:
        print("\nTask updated successfully!")
    else:
        print("Task title cannot be empty.")


def delete_task_menu(manager: TaskManager) -> None:
    """Prompt user to delete a task.

    Args:
        manager: The TaskManager instance
    """
    print()
    task_id_input = input("Enter task ID to delete: ")

    # Validate ID is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Please enter a valid number.")
        return

    # Delete the task
    success = manager.delete_task(task_id)
    if success:
        print("\nTask deleted successfully.")
    else:
        print("Task not found.")


def toggle_complete_menu(manager: TaskManager) -> None:
    """Prompt user to toggle task completion status.

    Args:
        manager: The TaskManager instance
    """
    print()
    task_id_input = input("Enter task ID to mark complete/incomplete: ")

    # Validate ID is numeric
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Please enter a valid number.")
        return

    # Get current status to report after toggle
    task = manager.get_task_by_id(task_id)
    if task is None:
        print("Task not found.")
        return

    # Toggle the status
    manager.toggle_complete(task_id)

    # Report new status
    new_status = "Complete" if task.is_complete else "Incomplete"
    print(f"\nTask marked as {new_status}.")


def main() -> None:
    """Main application loop."""
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

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
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
