# Research: Enhanced Todo CLI with Professional UI/UX

**Feature**: 002-todo-cli-enhanced-ux
**Date**: 2025-12-31

## Phase 0 Research Summary

This feature enhances the existing Phase 1 Todo CLI with professional UI/UX elements. All technology choices are already constrained by the constitution (Python 3.13+, standard library only, CLI only, in-memory storage).

## Technical Decisions

### Decision 1: ASCII Art Banner Implementation

**Decision**: Embed pre-designed ASCII art as a multi-line string constant
**Rationale**:
- Python standard library has no ASCII art generation capability
- Pre-designed banner ensures consistent, professional appearance
- Multi-line strings (`"""..."""`) are idiomatic Python
- No external dependencies required

**Alternatives Considered**:
- Generate dynamically using `pyfiglet` - Rejected (external library prohibited)
- Build character-by-character - Rejected (unnecessary complexity)
- Read from file - Rejected (persistence prohibited)

### Decision 2: Table Formatting Approach

**Decision**: Manual ASCII table rendering using string formatting
**Rationale**:
- Python's f-strings and `.ljust()/.rjust()` provide precise column alignment
- ASCII characters (+, -, |) are universal and require no special terminal support
- Calculated column widths based on content ensure proper alignment
- No external table libraries needed

**Alternatives Considered**:
- `tabulate` library - Rejected (external library prohibited)
- `rich` library - Rejected (external library prohibited)
- Fixed-width columns - Rejected (inflexible for varying content)

### Decision 3: UTF-8 Status Symbols

**Decision**: Use Unicode symbols for task status indicators
**Rationale**:
- Modern terminals universally support UTF-8
- Symbols are more visually distinct than text
- Checkmark (✓), checkbox (☐), and X (✗) are widely supported
- Falls within Python's native string handling

**Symbols Chosen**:
- Complete: ✓ (U+2713 CHECK MARK)
- Pending: ☐ (U+2610 BALLOT BOX)
- Overdue: ✗ (U+2717 BALLOT X)

**Alternatives Considered**:
- ASCII-only ([x], [ ], [!]) - Acceptable fallback if UTF-8 issues arise
- ANSI colors - Rejected (not universally supported, out of scope)

### Decision 4: Date Comparison for Overdue Detection

**Decision**: Use Python `datetime` module with YYYY-MM-DD string parsing
**Rationale**:
- `datetime` is part of Python standard library
- YYYY-MM-DD is ISO 8601 standard and sorts lexicographically
- Simple `strptime()` for parsing, comparison with `date.today()`
- Lenient validation (accept any string, fail gracefully on comparison)

**Alternatives Considered**:
- `dateutil` library - Rejected (external library prohibited)
- Manual string parsing - Rejected (error-prone)
- No date validation - Selected for input, validate only on display

### Decision 5: Extended Task Attributes Storage

**Decision**: Add new attributes directly to Task class
**Rationale**:
- Maintains simplicity of existing Task class
- Backward compatible (new attributes have defaults)
- No need for inheritance or composition patterns
- All attributes are simple types (strings, lists)

**New Attributes**:
- `priority: str` - Default "None"
- `due_date: str` - Default "" (empty)
- `category: str` - Default "" (empty)
- `tags: list[str]` - Default [] (empty list)

### Decision 6: Statistics Calculation Approach

**Decision**: Compute statistics on-demand from task list
**Rationale**:
- In-memory storage means no caching needed
- Task list is small enough for O(n) iteration
- No pre-computed statistics to maintain
- Single source of truth (task list itself)

**Metrics**:
- Completion %: `(completed_count / total_count) * 100`
- Counts: Filter tasks by `is_complete`
- Priority breakdown: Group by `priority` attribute
- Category breakdown: Group by `category` attribute
- Overdue: Filter incomplete tasks with past due dates

### Decision 7: Section Header Formatting

**Decision**: Bordered headers using = and - characters
**Rationale**:
- Consistent visual structure across all screens
- ASCII characters for maximum compatibility
- Fixed width (80 chars) for alignment
- Clear visual hierarchy

**Format Example**:
```
════════════════════════════════════════════════════════════════════════════════
                               MAIN MENU
════════════════════════════════════════════════════════════════════════════════
```

### Decision 8: Menu Organization

**Decision**: Group menu items by function with visual separators
**Rationale**:
- Logical grouping improves scanability
- Separators create visual hierarchy
- Numbering remains sequential for easy selection
- Statistics as new menu option (option 6)

**Menu Structure**:
1. Add Task
2. View Tasks
---
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
---
6. Statistics
---
7. Exit

## Dependencies Review

### Python Standard Library Modules Required

| Module | Purpose | Constitution Check |
|--------|---------|-------------------|
| `datetime` | Date parsing and comparison for overdue detection | ALLOWED (standard library) |
| `typing` | Type hints for code clarity | ALLOWED (standard library) |

### Existing Code Dependencies

| File | Purpose | Modification Needed |
|------|---------|---------------------|
| `src/task.py` | Task class | Add new attributes |
| `src/task_manager.py` | CRUD operations | Extend add/update methods |
| `src/main.py` | CLI interface | Extensive UI enhancements |

## Unknowns Resolved

| Unknown | Resolution |
|---------|------------|
| ASCII banner design | Pre-designed and embedded (see data-model.md) |
| Table column widths | Calculated dynamically from content |
| Date format validation | Accept any string, validate only during comparison |
| UTF-8 terminal support | Assume supported (documented in assumptions) |

## No External Research Required

All technology choices are constrained by the constitution:
- Language: Python 3.13+ (defined)
- Dependencies: Standard library only (defined)
- Storage: In-memory only (defined)
- Interface: CLI only (defined)

No NEEDS CLARIFICATION items remain. Ready for Phase 1 design.
