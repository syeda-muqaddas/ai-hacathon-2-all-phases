"""Task class representing a single todo item."""


class Task:
    """Represents a single todo item in the application.

    Attributes:
        id: Unique numeric identifier (auto-assigned, starts at 1)
        title: Task name/summary (required, non-empty)
        description: Additional details (optional, may be empty)
        is_complete: Completion status (default: False)
    """

    def __init__(self, task_id: int, title: str, description: str = "", is_complete: bool = False):
        """Initialize a new Task.

        Args:
            task_id: Unique identifier for the task
            title: Task name (required)
            description: Additional details (optional)
            is_complete: Whether the task is complete (default: False)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.is_complete = is_complete

    def __str__(self) -> str:
        """Return formatted string representation for display.

        Format: [ID: X] Title - Description [Status]
        Description is omitted if empty.
        """
        status = "Complete" if self.is_complete else "Incomplete"

        if self.description:
            return f"[ID: {self.id}] {self.title} - {self.description} [{status}]"
        else:
            return f"[ID: {self.id}] {self.title} [{status}]"
