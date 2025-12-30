---
name: qa.generate-tests
description: Generate comprehensive test cases from a feature specification for the To-Do App Phase 1
owner: todo-qa-agent
triggers:
  - "generate tests for"
  - "create test cases"
  - "write tests from spec"
---

# qa.generate-tests

## Purpose

Generate a complete, structured set of test cases from a feature specification. This skill transforms acceptance criteria and business rules into executable test scenarios that cover happy paths, edge cases, and error conditions for the To-Do App CLI.

## When to Use

- **Before implementation**: Generate tests as part of TDD workflow
- **After spec approval**: Create test suite from approved `spec.md`
- **During sprint planning**: Identify testing scope and effort
- **For coverage analysis**: Ensure all acceptance criteria have corresponding tests

## Input

| Parameter | Required | Description |
|-----------|----------|-------------|
| `feature_name` | Yes | Name of the feature (e.g., "add-task", "delete-task") |
| `spec_path` | Yes | Path to the specification file (e.g., `specs/add-task/spec.md`) |
| `output_path` | No | Where to save test cases (default: `specs/<feature>/tests.md`) |

## Step-by-Step Process

### Step 1: Read and Parse Specification
```
1. Read the specification file at `spec_path`
2. Extract:
   - Feature description
   - User stories / use cases
   - Acceptance criteria (numbered list)
   - Business rules
   - Edge cases mentioned
   - Error conditions
3. If spec is missing or incomplete, STOP and report: "BLOCKED: Specification incomplete or not found"
```

### Step 2: Generate Happy Path Tests
```
For each acceptance criterion:
1. Create test case with ID format: TC-[FEATURE]-[NUMBER]
2. Define preconditions (initial state)
3. Write step-by-step actions
4. Define expected outcome
5. Map back to AC# for traceability
```

### Step 3: Generate Edge Case Tests
```
For To-Do App Phase 1, always include tests for:
- Empty input (empty string, whitespace only)
- Maximum length input (if defined)
- Special characters in task names
- Boundary values (first task, last task)
- Single task vs multiple tasks scenarios
```

### Step 4: Generate Error Path Tests
```
For each error condition in spec:
1. Create negative test case
2. Define invalid input or state
3. Specify expected error message/behavior
4. Verify graceful handling (no crash)
```

### Step 5: Generate State Transition Tests
```
For task lifecycle:
- New task creation
- Task completion
- Task deletion
- Invalid state transitions (e.g., complete non-existent task)
```

### Step 6: Compile and Output
```
1. Organize tests by category:
   - Happy Path Tests
   - Edge Case Tests
   - Error Path Tests
   - State Transition Tests
2. Add summary with total count
3. Write to output_path
4. Report completion with test count
```

## Output

### Test Suite Document Structure

```markdown
# Test Cases: [Feature Name]

**Spec Reference:** [spec_path]
**Generated:** [ISO date]
**Total Tests:** [count]

## Traceability Matrix

| AC# | Test Cases |
|-----|------------|
| 1   | TC-XXX-001, TC-XXX-005 |
| 2   | TC-XXX-002, TC-XXX-006 |

## Happy Path Tests

### TC-[FEATURE]-001: [Descriptive Name]
**Traces to:** AC#1
**Preconditions:** [State required]
**Steps:**
1. [Action 1]
2. [Action 2]
**Expected Result:** [Outcome]

## Edge Case Tests

### TC-[FEATURE]-010: [Descriptive Name]
...

## Error Path Tests

### TC-[FEATURE]-020: [Descriptive Name]
...

## State Transition Tests

### TC-[FEATURE]-030: [Descriptive Name]
...
```

### Console Output
```
Test Generation Complete
========================
Feature: [feature_name]
Source: [spec_path]
Output: [output_path]

Generated:
- Happy Path: X tests
- Edge Cases: Y tests
- Error Paths: Z tests
- State Transitions: W tests
- Total: N tests

Traceability: All [M] acceptance criteria covered
```

## Failure Handling

| Failure Condition | Response |
|-------------------|----------|
| Spec file not found | `ERROR: Specification not found at [path]. Run sp.specify first.` |
| Spec incomplete (no AC) | `ERROR: No acceptance criteria found in spec. Cannot generate tests.` |
| Output path not writable | `ERROR: Cannot write to [path]. Check permissions.` |
| Feature name missing | `ERROR: Feature name required. Usage: qa.generate-tests <feature_name>` |

## Example Invocation

```
User: Generate test cases for the add-task feature
Agent: Reading specification from specs/add-task/spec.md...

Test Generation Complete
========================
Feature: add-task
Source: specs/add-task/spec.md
Output: specs/add-task/tests.md

Generated:
- Happy Path: 3 tests
- Edge Cases: 5 tests
- Error Paths: 4 tests
- State Transitions: 2 tests
- Total: 14 tests

Traceability: All 5 acceptance criteria covered
```

## Phase 1 Constraints

This skill operates within To-Do App Phase 1 boundaries:
- Tests are designed for **CLI execution** (input/output validation)
- Tests assume **in-memory storage** (no persistence between runs)
- Tests are written for **manual execution** (no automation framework required)
