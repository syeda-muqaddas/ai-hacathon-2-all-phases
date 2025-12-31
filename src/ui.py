"""UI helper functions for the Todo CLI Application.

Provides display functions for ASCII banner, section headers, tables,
success/error messages, and status symbols.
"""

from datetime import date

# ASCII Art Banner (per data-model.md)
ASCII_BANNER = """
████████╗ ██████╗ ██████╗  ██████╗
╚══██╔══╝██╔═══██╗██╔══██╗██╔═══██╗
   ██║   ██║   ██║██║  ██║██║   ██║
   ██║   ██║   ██║██║  ██║██║   ██║
   ██║   ╚██████╔╝██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝
"""

# Application header
APP_HEADER = "Todo CLI v2.0 - Your Productivity Partner"

# Terminal width for centering and borders
TERMINAL_WIDTH = 80


def print_banner() -> None:
    """Display the ASCII art banner centered on the screen."""
    print()
    for line in ASCII_BANNER.strip().split('\n'):
        # Center each line of the banner
        padding = (TERMINAL_WIDTH - len(line)) // 2
        print(" " * padding + line)
    print()
    # Print centered app header
    padding = (TERMINAL_WIDTH - len(APP_HEADER)) // 2
    print(" " * padding + APP_HEADER)
    print()


def print_header(title: str) -> None:
    """Display a section header with bordered formatting.

    Args:
        title: The section title to display (will be centered and uppercased)
    """
    border = "═" * TERMINAL_WIDTH
    print()
    print(border)
    # Center the title
    padding = (TERMINAL_WIDTH - len(title)) // 2
    print(" " * padding + title.upper())
    print(border)
    print()


def print_success(message: str) -> None:
    """Display a success message with checkmark symbol.

    Args:
        message: The success message to display
    """
    print(f"✓ {message}")


def print_error(message: str) -> None:
    """Display an error message with warning symbol.

    Args:
        message: The error message to display
    """
    print(f"⚠ {message}")


def print_separator() -> None:
    """Display a visual separator line for menu grouping."""
    print("  " + "─" * 37)


def is_overdue(task) -> bool:
    """Check if a task is overdue based on its due date.

    A task is overdue if it is incomplete and has a due date in the past.
    Invalid date formats are treated as not overdue.

    Args:
        task: The Task object to check

    Returns:
        True if the task is overdue, False otherwise
    """
    # If task is complete, it cannot be overdue
    if task.is_complete:
        return False

    # If no due date, not overdue
    if not task.due_date:
        return False

    # Try to parse the due date (YYYY-MM-DD format)
    try:
        year, month, day = task.due_date.split("-")
        due = date(int(year), int(month), int(day))
        return due < date.today()
    except (ValueError, AttributeError):
        # Invalid date format - treat as not overdue
        return False


def get_status_symbol(task) -> str:
    """Get the visual status symbol for a task.

    Args:
        task: The Task object to get status for

    Returns:
        ✓ for complete, ✗ for overdue, ☐ for pending
    """
    if task.is_complete:
        return "✓"
    elif is_overdue(task):
        return "✗"
    else:
        return "☐"


def truncate_string(text: str, max_length: int) -> str:
    """Truncate a string to max_length, adding '...' if truncated.

    Args:
        text: The string to truncate
        max_length: Maximum length including the '...'

    Returns:
        The original string if short enough, or truncated with '...'
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def print_task_table(tasks: list) -> None:
    """Display tasks in a formatted ASCII table.

    Columns: ID (4), Status (3), Title (30), Priority (10), Due Date (12), Category (15)

    Args:
        tasks: List of Task objects to display
    """
    # Column widths
    id_w = 4
    status_w = 3
    title_w = 30
    priority_w = 10
    date_w = 12
    category_w = 15

    # Build separator row
    sep = f"+{'-' * id_w}+{'-' * status_w}+{'-' * title_w}+{'-' * priority_w}+{'-' * date_w}+{'-' * category_w}+"

    # Print table header
    print(sep)
    print(f"| {'ID':>{id_w - 2}} | {'S':^{status_w - 2}} | {'Title':<{title_w - 2}} | {'Priority':<{priority_w - 2}} | {'Due Date':<{date_w - 2}} | {'Category':<{category_w - 2}} |")
    print(sep)

    # Track counts for summary
    completed_count = 0
    pending_count = 0
    overdue_count = 0

    # Print each task row
    for task in tasks:
        status = get_status_symbol(task)
        title = truncate_string(task.title, title_w - 2)
        priority = task.priority if task.priority else "None"
        due_date = task.due_date if task.due_date else ""
        category = truncate_string(task.category, category_w - 2) if task.category else ""

        print(f"| {task.id:>{id_w - 2}} | {status:^{status_w - 2}} | {title:<{title_w - 2}} | {priority:<{priority_w - 2}} | {due_date:<{date_w - 2}} | {category:<{category_w - 2}} |")

        # Count statuses
        if task.is_complete:
            completed_count += 1
        elif is_overdue(task):
            overdue_count += 1
        else:
            pending_count += 1

    print(sep)

    # Print summary row
    total = len(tasks)
    print()
    print(f"Total: {total} tasks | ✓ Completed: {completed_count} | ☐ Pending: {pending_count} | ✗ Overdue: {overdue_count}")


def print_statistics_dashboard(stats: dict) -> None:
    """Display the statistics dashboard with bordered sections.

    Args:
        stats: Dictionary containing computed statistics:
            - total_count: Total number of tasks
            - completed_count: Number of completed tasks
            - incomplete_count: Number of incomplete tasks
            - completion_percentage: Percentage complete (0-100)
            - priority_breakdown: Dict of priority -> count
            - category_breakdown: Dict of category -> count
            - overdue_count: Number of overdue tasks
            - pending_count: Number of pending (not overdue, not complete) tasks
    """
    box_width = 75
    box_top = "  ┌" + "─" * box_width + "┐"
    box_bottom = "  └" + "─" * box_width + "┘"
    box_empty = "  │" + " " * box_width + "│"

    # Completion Progress Section
    print(box_top)
    print(f"  │{'COMPLETION PROGRESS':^{box_width}}│")
    print(box_empty)

    # Progress bar
    percentage = stats.get("completion_percentage", 0)
    bar_width = 40
    filled = int(bar_width * percentage / 100)
    empty = bar_width - filled
    progress_bar = "█" * filled + "░" * empty
    bar_line = f"  [{progress_bar}] {percentage:.0f}%"
    print(f"  │{bar_line:<{box_width}}│")

    print(box_empty)

    # Summary counts
    total = stats.get("total_count", 0)
    completed = stats.get("completed_count", 0)
    pending = stats.get("pending_count", 0)
    overdue = stats.get("overdue_count", 0)
    summary = f"  Total Tasks: {total}  |  ✓ Completed: {completed}  |  ☐ Pending: {pending}  |  ✗ Overdue: {overdue}"
    print(f"  │{summary:<{box_width}}│")

    print(box_bottom)
    print()

    # Priority Breakdown Section
    print(box_top)
    print(f"  │{'PRIORITY BREAKDOWN':^{box_width}}│")
    print(box_empty)

    priority_breakdown = stats.get("priority_breakdown", {})
    for priority in ["High", "Medium", "Low", "None"]:
        count = priority_breakdown.get(priority, 0)
        # Use ASCII indicators instead of emoji
        if priority == "High":
            indicator = "[!]"
        elif priority == "Medium":
            indicator = "[+]"
        elif priority == "Low":
            indicator = "[-]"
        else:
            indicator = "[ ]"
        task_word = "task" if count == 1 else "tasks"
        line = f"  {indicator} {priority}:    {count} {task_word}"
        print(f"  │{line:<{box_width}}│")

    print(box_bottom)
    print()

    # Category Breakdown Section
    category_breakdown = stats.get("category_breakdown", {})
    if category_breakdown:
        print(box_top)
        print(f"  │{'CATEGORY BREAKDOWN':^{box_width}}│")
        print(box_empty)

        for category, count in sorted(category_breakdown.items()):
            task_word = "task" if count == 1 else "tasks"
            line = f"  {category}:  {count} {task_word}"
            print(f"  │{line:<{box_width}}│")

        print(box_bottom)
