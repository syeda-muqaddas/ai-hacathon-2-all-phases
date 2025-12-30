---
name: qa.report-bug
description: Create structured, actionable bug reports for the To-Do App Phase 1
owner: todo-qa-agent
triggers:
  - "report bug"
  - "create bug report"
  - "log defect"
  - "found a bug"
---

# qa.report-bug

## Purpose

Create a comprehensive, structured bug report that enables developers to quickly understand, reproduce, and fix defects in the To-Do App. This skill transforms bug observations into actionable documentation with clear reproduction steps, severity classification, and supporting evidence.

## When to Use

- **During testing**: Document defects found during QA activities
- **After user reports**: Formalize informal bug descriptions
- **During validation**: Record failures found in acceptance testing
- **Regression discovery**: Document bugs introduced by changes

## Input

| Parameter | Required | Description |
|-----------|----------|-------------|
| `title` | Yes | Brief, descriptive bug title (max 80 chars) |
| `description` | Yes | What happened vs what should happen |
| `steps` | Yes | Steps to reproduce (list format) |
| `feature` | No | Affected feature name (auto-detected if possible) |
| `severity` | No | Critical/High/Medium/Low (assessed if not provided) |
| `evidence` | No | Error messages, output, or other proof |
| `output_path` | No | Where to save report (default: `bugs/BUG-XXX.md`) |

## Step-by-Step Process

### Step 1: Gather Bug Information
```
1. Collect all provided parameters
2. If description unclear, prompt for:
   - What were you trying to do?
   - What happened instead?
   - What should have happened?
3. Validate reproduction steps are complete
```

### Step 2: Verify Reproducibility
```
1. Follow provided reproduction steps
2. Confirm bug occurs consistently
3. If not reproducible:
   - Ask for additional context
   - Note as "intermittent" if confirmed sporadic
4. Document exact behavior observed
```

### Step 3: Assess Severity
```
If severity not provided, classify based on:

CRITICAL:
- Application crash
- Data loss
- Complete feature failure
- Security vulnerability

HIGH:
- Major feature broken
- No workaround available
- Blocks primary user workflow

MEDIUM:
- Feature partially broken
- Workaround exists
- Non-critical workflow affected

LOW:
- Minor inconvenience
- Cosmetic issues
- Edge case only
```

### Step 4: Identify Related Artifacts
```
1. Link to affected specification (if exists)
2. Link to related acceptance criteria
3. Identify potentially affected code files
4. Check for duplicate/related bugs
```

### Step 5: Generate Bug ID
```
1. Read existing bugs in bugs/ directory
2. Find highest BUG-XXX number
3. Increment for new ID: BUG-[XXX+1]
4. If no bugs exist, start with BUG-001
```

### Step 6: Create Bug Report
```
1. Fill all sections of bug template
2. Include all evidence
3. Add environment details
4. Write to output_path
5. Confirm creation to user
```

## Output

### Bug Report Structure

```markdown
# BUG-[ID]: [Title]

## Summary

| Field | Value |
|-------|-------|
| ID | BUG-[XXX] |
| Severity | [Critical/High/Medium/Low] |
| Status | Open |
| Feature | [Affected feature] |
| Reported | [ISO date] |
| Reporter | todo-qa-agent |

## Description

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

## Environment

- **Platform:** Python CLI
- **Storage:** In-memory
- **Python Version:** [if relevant]

## Steps to Reproduce

1. [Prerequisite state]
2. [Action 1]
3. [Action 2]
4. [Observe bug]

## Evidence

### Error Output
```
[Captured error messages or unexpected output]
```

### Expected Output
```
[What output should have been]
```

## Impact Assessment

**User Impact:** [How this affects users]
**Workaround:** [If any exists, describe it]
**Blocked Features:** [What else might be affected]

## Related Artifacts

- **Specification:** [Link to spec.md if applicable]
- **Acceptance Criteria:** [Which AC is violated]
- **Related Bugs:** [Links to related issues]

## Technical Notes

[Any observations about potential cause, affected code areas, etc.]

## Resolution

**Status:** Open
**Assigned To:** [Unassigned]
**Fix Version:** [TBD]
```

### Console Output
```
Bug Report Created
==================
ID: BUG-007
Title: Empty task name causes application crash
Severity: CRITICAL
Feature: add-task

Saved to: bugs/BUG-007.md

Summary:
- Application crashes when user enters empty task name
- Expected: Error message and prompt retry
- Impact: Complete workflow failure

Next Steps:
1. Review bugs/BUG-007.md for full details
2. Assign to developer for investigation
3. Link to sprint backlog if applicable
```

## Failure Handling

| Failure Condition | Response |
|-------------------|----------|
| Missing title | `ERROR: Bug title required. Provide brief description.` |
| Missing steps | `ERROR: Reproduction steps required. List steps to trigger bug.` |
| Cannot reproduce | `WARNING: Bug not reproducible. Marking as intermittent. Add more context.` |
| Duplicate found | `WARNING: Possible duplicate of BUG-XXX. Review before creating.` |
| Output dir missing | Create `bugs/` directory automatically |

## Bug Report Quality Checklist

Before finalizing, verify:
- [ ] Title is specific and searchable
- [ ] Steps are numbered and complete
- [ ] Expected vs actual clearly stated
- [ ] Severity is justified
- [ ] Evidence is included
- [ ] Environment specified
- [ ] Related artifacts linked

## Example Invocation

```
User: Report a bug - the app crashes when I try to delete a task that doesn't exist
Agent: I'll create a bug report for this issue. Let me verify the bug first...

Reproducing:
1. Start application
2. Attempt to delete task with invalid ID
3. Observed: Application raises unhandled exception

Bug Report Created
==================
ID: BUG-003
Title: Unhandled exception when deleting non-existent task
Severity: HIGH
Feature: delete-task

Saved to: bugs/BUG-003.md

Summary:
- Deleting task with invalid ID raises IndexError
- Expected: Friendly error message "Task not found"
- Impact: User must restart application

Recommended Priority: Fix before release
```

## Severity Guidelines for To-Do App

| Severity | Examples |
|----------|----------|
| Critical | App won't start, crash on any input, data corruption |
| High | Cannot add tasks, cannot view tasks, crash on common action |
| Medium | Cannot delete specific task, formatting issues, unclear messages |
| Low | Typo in message, extra whitespace, minor UX friction |

## Phase 1 Constraints

This skill operates within To-Do App Phase 1 boundaries:
- Bugs are documented as **Markdown files** (no issue tracker)
- Environment is always **CLI + in-memory**
- Evidence is **text-based** (CLI output)
- Bug reports stored in **bugs/** directory
