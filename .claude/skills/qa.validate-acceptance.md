---
name: qa.validate-acceptance
description: Validate implementation against acceptance criteria for the To-Do App Phase 1
owner: todo-qa-agent
triggers:
  - "validate acceptance"
  - "check acceptance criteria"
  - "verify implementation"
  - "run acceptance tests"
---

# qa.validate-acceptance

## Purpose

Systematically validate that an implementation meets all acceptance criteria defined in its specification. This skill executes each criterion as a test, documents results with evidence, and produces a compliance report that determines if the feature is ready for approval.

## When to Use

- **After implementation**: Verify code meets all requirements
- **Before PR approval**: Gate check for spec compliance
- **During code review**: Provide objective evidence of correctness
- **Sprint demos**: Prove feature completion to stakeholders

## Input

| Parameter | Required | Description |
|-----------|----------|-------------|
| `feature_name` | Yes | Name of the feature to validate |
| `spec_path` | Yes | Path to specification (e.g., `specs/add-task/spec.md`) |
| `code_path` | No | Path to implementation file(s) (auto-detected if not provided) |
| `output_path` | No | Where to save report (default: `specs/<feature>/validation-report.md`) |

## Step-by-Step Process

### Step 1: Load Specification and Implementation
```
1. Read specification from `spec_path`
2. Extract all acceptance criteria (must be numbered/bulleted)
3. Locate implementation code:
   - If `code_path` provided, use it
   - Otherwise, search for main Python file in project
4. If spec or code missing, STOP with error
```

### Step 2: Parse Acceptance Criteria
```
For each acceptance criterion:
1. Assign validation ID: VAL-[FEATURE]-[AC#]
2. Identify:
   - Input conditions
   - Expected behavior
   - Success indicators
3. Classify type: Functional | Edge Case | Error Handling
```

### Step 3: Execute Validation Tests
```
For each criterion:
1. Set up preconditions (if any)
2. Execute the implementation via CLI
3. Capture output (stdout, stderr)
4. Compare actual vs expected behavior
5. Record result: PASS | FAIL | BLOCKED
6. Capture evidence (actual output, screenshots, logs)
```

### Step 4: Document Findings
```
For PASS results:
- Record evidence of correct behavior
- Note any observations

For FAIL results:
- Document expected vs actual behavior
- Identify specific deviation
- Assess severity of failure
- Suggest remediation if obvious

For BLOCKED results:
- Document blocking condition
- Identify prerequisite that failed
```

### Step 5: Calculate Compliance Score
```
1. Count: PASS, FAIL, BLOCKED
2. Calculate pass rate: PASS / (PASS + FAIL) * 100
3. Determine overall status:
   - APPROVED: 100% pass, 0 blocked
   - CONDITIONAL: >80% pass, minor failures
   - REJECTED: <80% pass OR any critical failure
```

### Step 6: Generate Report
```
1. Compile all results into structured report
2. Include executive summary
3. List all criteria with status and evidence
4. Provide recommendations
5. Write to output_path
```

## Output

### Validation Report Structure

```markdown
# Acceptance Criteria Validation Report

## Executive Summary

| Metric | Value |
|--------|-------|
| Feature | [feature_name] |
| Spec Version | [version/date] |
| Validation Date | [ISO date] |
| Overall Status | APPROVED / CONDITIONAL / REJECTED |
| Pass Rate | X% (Y of Z criteria) |

## Criteria Status Overview

| ID | Criterion | Status | Severity |
|----|-----------|--------|----------|
| VAL-XXX-01 | [Brief description] | PASS | - |
| VAL-XXX-02 | [Brief description] | FAIL | High |

## Detailed Results

### VAL-[FEATURE]-01: [Criterion Text]
**Status:** PASS
**Test Method:** [How it was tested]
**Evidence:**
```
[Actual output or observation]
```
**Notes:** [Any relevant observations]

---

### VAL-[FEATURE]-02: [Criterion Text]
**Status:** FAIL
**Test Method:** [How it was tested]
**Expected:**
```
[Expected behavior]
```
**Actual:**
```
[Actual behavior]
```
**Severity:** High
**Remediation:** [Suggested fix]

## Recommendations

1. [Action item 1]
2. [Action item 2]

## Approval Decision

**Status:** [APPROVED / CONDITIONAL / REJECTED]
**Rationale:** [Explanation]
**Required Actions:** [If not approved, what must be done]
```

### Console Output
```
Acceptance Criteria Validation
==============================
Feature: [feature_name]
Spec: [spec_path]

Validating criteria...
[1/5] AC#1: Adding task with valid name............ PASS
[2/5] AC#2: Empty task name rejected............... PASS
[3/5] AC#3: Task appears in list after add......... PASS
[4/5] AC#4: Duplicate task names allowed........... FAIL
[5/5] AC#5: Success message displayed.............. PASS

Results: 4 PASS | 1 FAIL | 0 BLOCKED
Pass Rate: 80%

Overall Status: CONDITIONAL
Report saved to: specs/add-task/validation-report.md
```

## Failure Handling

| Failure Condition | Response |
|-------------------|----------|
| Spec not found | `ERROR: Specification not found at [path]. Cannot validate.` |
| No acceptance criteria | `ERROR: No acceptance criteria found in spec.` |
| Implementation not found | `ERROR: Cannot locate implementation. Provide code_path.` |
| Runtime error during test | `BLOCKED: Test [ID] failed with error: [message]` |
| Ambiguous criterion | `WARNING: Criterion [ID] is ambiguous. Interpreted as: [interpretation]` |

## Validation Rules

### PASS Criteria
- Output matches expected behavior exactly
- No errors or warnings produced
- State changes are correct

### FAIL Criteria
- Output differs from expected
- Errors occur when none expected
- Missing functionality

### BLOCKED Criteria
- Cannot execute test (dependency failure)
- Environment issue
- Prerequisite not met

## Example Invocation

```
User: Validate the add-task implementation against its spec
Agent: Loading specification from specs/add-task/spec.md...
       Found 5 acceptance criteria
       Locating implementation...

Acceptance Criteria Validation
==============================
Feature: add-task

[1/5] AC#1: User can add task with title........... PASS
[2/5] AC#2: Empty title shows error................ PASS
[3/5] AC#3: Task gets unique ID.................... PASS
[4/5] AC#4: Success confirmation displayed......... PASS
[5/5] AC#5: Task visible in list view.............. PASS

Results: 5 PASS | 0 FAIL | 0 BLOCKED
Pass Rate: 100%

Overall Status: APPROVED
Report saved to: specs/add-task/validation-report.md
```

## Phase 1 Constraints

This skill operates within To-Do App Phase 1 boundaries:
- Validation is performed via **CLI interaction**
- Tests assume **fresh in-memory state** per execution
- Evidence is captured as **text output** (no screenshots)
- Manual execution by QA agent (no automated test runner)
