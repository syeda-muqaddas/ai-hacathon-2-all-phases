# Quickstart Guide: Enhanced Todo CLI

**Feature**: 002-todo-cli-enhanced-ux
**Version**: 2.0

## Prerequisites

- Python 3.13+ installed
- Terminal with UTF-8 support (for status symbols)
- Terminal width of 80+ characters recommended

## Installation

```bash
# From the project root directory
cd "/path/to/TODO-APP"

# Run the application
python -m src.main
```

Or:
```bash
python src/main.py
```

## Demo Script

This demo script showcases all enhanced features in the Todo CLI v2.0.

### Step 1: Launch the Application

```bash
python -m src.main
```

**Expected Output**:
```
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
...
```

### Step 2: Add Tasks with Extended Attributes

Select option **1** (Add Task) and create several tasks:

**Task 1 - High Priority with Due Date**:
```
> Enter your choice (1-7): 1

════════════════════════════════════════════════════════════════════════════════
                                 ADD TODO
════════════════════════════════════════════════════════════════════════════════

> Enter task title: Buy groceries
> Enter description (optional): Milk, bread, eggs, vegetables
> Enter priority (1=High, 2=Medium, 3=Low, 4=None) [4]: 1
> Enter due date (YYYY-MM-DD) or press Enter to skip: 2025-01-05
> Enter category or press Enter to skip: Personal
> Enter tags (comma-separated) or press Enter to skip: shopping, errands

✓ Task added successfully! (ID: 1)
```

**Task 2 - Medium Priority**:
```
> Enter your choice (1-7): 1
> Enter task title: Complete project report
> Enter description (optional): Q4 financial summary
> Enter priority (1=High, 2=Medium, 3=Low, 4=None) [4]: 2
> Enter due date (YYYY-MM-DD) or press Enter to skip: 2025-01-15
> Enter category or press Enter to skip: Work
> Enter tags (comma-separated) or press Enter to skip: report, quarterly

✓ Task added successfully! (ID: 2)
```

**Task 3 - Overdue Task** (for demo purposes, use a past date):
```
> Enter your choice (1-7): 1
> Enter task title: Pay electricity bill
> Enter description (optional):
> Enter priority (1=High, 2=Medium, 3=Low, 4=None) [4]: 1
> Enter due date (YYYY-MM-DD) or press Enter to skip: 2024-12-30
> Enter category or press Enter to skip: Bills
> Enter tags (comma-separated) or press Enter to skip: urgent, bills

✓ Task added successfully! (ID: 3)
```

**Task 4 - Minimal (title only)**:
```
> Enter your choice (1-7): 1
> Enter task title: Read Python documentation
> Enter description (optional):
> Enter priority (1=High, 2=Medium, 3=Low, 4=None) [4]:
> Enter due date (YYYY-MM-DD) or press Enter to skip:
> Enter category or press Enter to skip: Learning
> Enter tags (comma-separated) or press Enter to skip:

✓ Task added successfully! (ID: 4)
```

### Step 3: View Tasks in Table Format

Select option **2** (View Tasks):

```
> Enter your choice (1-7): 2

════════════════════════════════════════════════════════════════════════════════
                                 ALL TODOS
════════════════════════════════════════════════════════════════════════════════

+----+---+------------------------------+----------+------------+---------------+
| ID | S | Title                        | Priority | Due Date   | Category      |
+----+---+------------------------------+----------+------------+---------------+
|  1 | ☐ | Buy groceries                | High     | 2025-01-05 | Personal      |
|  2 | ☐ | Complete project report      | Medium   | 2025-01-15 | Work          |
|  3 | ✗ | Pay electricity bill         | High     | 2024-12-30 | Bills         |
|  4 | ☐ | Read Python documentation    | None     |            | Learning      |
+----+---+------------------------------+----------+------------+---------------+

Total: 4 tasks | ✓ Completed: 0 | ☐ Pending: 3 | ✗ Overdue: 1

════════════════════════════════════════════════════════════════════════════════
```

### Step 4: Mark a Task Complete

Select option **5** (Mark Complete/Incomplete):

```
> Enter your choice (1-7): 5

════════════════════════════════════════════════════════════════════════════════
                           MARK COMPLETE/INCOMPLETE
════════════════════════════════════════════════════════════════════════════════

> Enter task ID: 1

✓ Task marked as Complete.
```

### Step 5: View Statistics Dashboard

Select option **6** (Statistics):

```
> Enter your choice (1-7): 6

════════════════════════════════════════════════════════════════════════════════
                                STATISTICS
════════════════════════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         COMPLETION PROGRESS                              │
  │                                                                          │
  │  [██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 25%                         │
  │                                                                          │
  │  Total Tasks: 4  |  ✓ Completed: 1  |  ☐ Pending: 2  |  ✗ Overdue: 1   │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         PRIORITY BREAKDOWN                               │
  │                                                                          │
  │  [!] High:    2 tasks                                                   │
  │  [+] Medium:  1 task                                                    │
  │  [-] Low:     0 tasks                                                   │
  │  [ ] None:    1 task                                                    │
  └─────────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────────┐
  │                         CATEGORY BREAKDOWN                               │
  │                                                                          │
  │  Personal:  1 task                                                      │
  │  Work:      1 task                                                      │
  │  Bills:     1 task                                                      │
  │  Learning:  1 task                                                      │
  └─────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
```

### Step 6: Update a Task

Select option **3** (Update Task):

```
> Enter your choice (1-7): 3

════════════════════════════════════════════════════════════════════════════════
                                UPDATE TODO
════════════════════════════════════════════════════════════════════════════════

> Enter task ID: 2

Current values:
  Title:       Complete project report
  Description: Q4 financial summary
  Priority:    Medium
  Due Date:    2025-01-15
  Category:    Work
  Tags:        report, quarterly

> Enter new title (press Enter to keep):
> Enter new description (press Enter to keep): Updated with Q3 comparison
> Enter new priority (1=High, 2=Medium, 3=Low, 4=None) or Enter to keep: 1
> Enter new due date (YYYY-MM-DD) or Enter to keep:
> Enter new category or Enter to keep:
> Enter new tags (comma-separated) or Enter to keep: report, quarterly, priority

✓ Task updated successfully!
```

### Step 7: Delete a Task

Select option **4** (Delete Task):

```
> Enter your choice (1-7): 4

════════════════════════════════════════════════════════════════════════════════
                                DELETE TODO
════════════════════════════════════════════════════════════════════════════════

> Enter task ID: 3

✓ Task deleted successfully.
```

### Step 8: Final View

Select option **2** to see final state:

```
> Enter your choice (1-7): 2

════════════════════════════════════════════════════════════════════════════════
                                 ALL TODOS
════════════════════════════════════════════════════════════════════════════════

+----+---+------------------------------+----------+------------+---------------+
| ID | S | Title                        | Priority | Due Date   | Category      |
+----+---+------------------------------+----------+------------+---------------+
|  1 | ✓ | Buy groceries                | High     | 2025-01-05 | Personal      |
|  2 | ☐ | Complete project report      | High     | 2025-01-15 | Work          |
|  4 | ☐ | Read Python documentation    | None     |            | Learning      |
+----+---+------------------------------+----------+------------+---------------+

Total: 3 tasks | ✓ Completed: 1 | ☐ Pending: 2 | ✗ Overdue: 0

════════════════════════════════════════════════════════════════════════════════
```

### Step 9: Exit

Select option **7** (Exit):

```
> Enter your choice (1-7): 7

════════════════════════════════════════════════════════════════════════════════

Thank you for using Todo CLI v2.0!
Stay productive! 🚀

════════════════════════════════════════════════════════════════════════════════
```

## Error Handling Demo

### Invalid Menu Choice
```
> Enter your choice (1-7): 9

⚠ Invalid choice. Please try again.
```

### Empty Title
```
> Enter task title:

⚠ Task title cannot be empty.
```

### Invalid Task ID
```
> Enter task ID: abc

⚠ Please enter a valid number.
```

### Task Not Found
```
> Enter task ID: 999

⚠ Task not found.
```

## Key Features Summary

| Feature | Description |
|---------|-------------|
| ASCII Banner | Professional startup display |
| Section Headers | Clear navigation structure |
| Extended Attributes | Priority, due date, category, tags |
| Table Display | Aligned columns with ASCII borders |
| Status Symbols | ✓ Complete, ☐ Pending, ✗ Overdue |
| Statistics Dashboard | Progress, counts, breakdowns |
| Friendly Feedback | Clear success/error messages |

## Notes

- All data is stored in memory and will be lost when the application exits
- Due dates should be in YYYY-MM-DD format for overdue detection to work correctly
- Terminal width of 80+ characters is recommended for optimal display
