"""Statistics computation functions for the Todo CLI Application.

Provides functions to compute task metrics including completion percentage,
counts, priority/category breakdowns, and overdue detection.
"""

from src.ui import is_overdue


def compute_statistics(tasks: list) -> dict:
    """Compute all statistics from a list of tasks.

    Args:
        tasks: List of Task objects to analyze

    Returns:
        Dictionary containing:
            - total_count: Total number of tasks
            - completed_count: Number of completed tasks
            - incomplete_count: Number of incomplete tasks
            - pending_count: Number of pending (incomplete, not overdue) tasks
            - overdue_count: Number of overdue tasks
            - completion_percentage: Percentage of tasks completed (0-100)
            - priority_breakdown: Dict mapping priority -> count
            - category_breakdown: Dict mapping category -> count (non-empty only)
    """
    total_count = len(tasks)

    if total_count == 0:
        return {
            "total_count": 0,
            "completed_count": 0,
            "incomplete_count": 0,
            "pending_count": 0,
            "overdue_count": 0,
            "completion_percentage": 0,
            "priority_breakdown": {},
            "category_breakdown": {},
        }

    # Count by status
    completed_count = sum(1 for task in tasks if task.is_complete)
    incomplete_count = total_count - completed_count
    overdue_count = sum(1 for task in tasks if is_overdue(task))
    pending_count = incomplete_count - overdue_count

    # Calculate percentage
    completion_percentage = (completed_count / total_count) * 100

    # Priority breakdown
    priority_breakdown = {"High": 0, "Medium": 0, "Low": 0, "None": 0}
    for task in tasks:
        priority = task.priority if task.priority in priority_breakdown else "None"
        priority_breakdown[priority] += 1

    # Category breakdown (non-empty categories only)
    category_breakdown = {}
    for task in tasks:
        if task.category:
            if task.category in category_breakdown:
                category_breakdown[task.category] += 1
            else:
                category_breakdown[task.category] = 1

    return {
        "total_count": total_count,
        "completed_count": completed_count,
        "incomplete_count": incomplete_count,
        "pending_count": pending_count,
        "overdue_count": overdue_count,
        "completion_percentage": completion_percentage,
        "priority_breakdown": priority_breakdown,
        "category_breakdown": category_breakdown,
    }
