"""TaskManager class for managing the collection of tasks."""

from src.task import Task


class TaskManager:
    """Manages the collection of tasks and provides CRUD operations.

    Attributes:
        tasks: In-memory storage of all tasks
        next_id: Counter for next task ID (starts at 1)
    """

    def __init__(self):
        """Initialize TaskManager with empty task list and ID counter."""
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task | None:
        """Create a new task with auto-assigned ID.

        Args:
            title: Task name (required, must be non-empty after strip)
            description: Additional details (optional)

        Returns:
            The newly created Task, or None if title is invalid
        """
        # Validate title is non-empty
        if not title or not title.strip():
            return None

        # Create new task with current ID
        task = Task(
            task_id=self.next_id,
            title=title.strip(),
            description=description.strip() if description else "",
            is_complete=False
        )

        # Add to list and increment counter
        self.tasks.append(task)
        self.next_id += 1

        return task

    def get_all_tasks(self) -> list[Task]:
        """Return all tasks in the list.

        Returns:
            List of all Task objects
        """
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Task | None:
        """Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            The Task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str | None = None, description: str | None = None) -> bool:
        """Update a task's title and/or description.

        Args:
            task_id: The ID of the task to update
            title: New title (None or empty string to keep current)
            description: New description (None to keep current, empty string to clear)

        Returns:
            True if task was updated, False if task not found or invalid title
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Update title if provided and non-empty
        if title is not None and title.strip():
            task.title = title.strip()
        elif title is not None and not title.strip():
            # User tried to set empty title - reject
            return False

        # Update description if provided (can be empty to clear)
        if description is not None:
            task.description = description.strip()

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def toggle_complete(self, task_id: int) -> bool:
        """Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if task was toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.is_complete = not task.is_complete
        return True
