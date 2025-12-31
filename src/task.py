"""Task class representing a single todo item with extended attributes."""


class Task:
    """Represents a single todo item in the application.

    Attributes:
        id: Unique numeric identifier (auto-assigned, starts at 1)
        title: Task name/summary (required, non-empty)
        description: Additional details (optional, may be empty)
        is_complete: Completion status (default: False)
        priority: Importance level - "High", "Medium", "Low", "None" (default: "None")
        due_date: Target completion date as string in YYYY-MM-DD format (optional)
        category: Grouping category (optional)
        tags: List of labels for the task (optional, default: empty list)
    """

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str = "",
        is_complete: bool = False,
        priority: str = "None",
        due_date: str = "",
        category: str = "",
        tags: list[str] | None = None
    ):
        """Initialize a new Task with extended attributes.

        Args:
            task_id: Unique identifier for the task
            title: Task name (required)
            description: Additional details (optional)
            is_complete: Whether the task is complete (default: False)
            priority: Importance level - "High", "Medium", "Low", "None" (default: "None")
            due_date: Target date as YYYY-MM-DD string (optional)
            category: Grouping category (optional)
            tags: List of labels (optional, default: empty list)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.is_complete = is_complete
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.tags = tags if tags is not None else []

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
