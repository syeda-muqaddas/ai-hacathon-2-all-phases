<!--
SYNC IMPACT REPORT
==================
Version change: 0.0.0 → 1.0.0 (MAJOR - initial constitution establishment)

Modified principles: N/A (initial creation)

Added sections:
- Core Principles (I through VI)
- Technology Stack
- Constraints
- Success Criteria
- Governance

Removed sections: N/A (initial creation)

Templates requiring updates:
- .specify/templates/plan-template.md: ✅ No changes needed (already generic)
- .specify/templates/spec-template.md: ✅ No changes needed (already generic)
- .specify/templates/tasks-template.md: ✅ No changes needed (already generic)

Follow-up TODOs: None
-->

# In-Memory Todo Python Console App Constitution

## Core Principles

### I. Spec-First Development (NON-NEGOTIABLE)

All development MUST follow the Spec-Kit Plus workflow in strict sequence:

1. **Constitution** establishes project principles and constraints
2. **Specification** defines feature requirements and acceptance criteria
3. **Plan** documents architectural decisions and design
4. **Tasks** breaks work into testable, traceable implementation units
5. **Implementation** generates code that fulfills approved tasks

No code may be written without an approved specification. No specification may be created without an established constitution. Traceability from Constitution → Spec → Plan → Tasks → Code MUST be maintained at all times.

### II. AI-Generated Implementation

All production code MUST be generated via Claude Code following approved specifications:

- No manual coding outside the Spec-Kit Plus workflow
- All changes MUST trace back to approved tasks
- Implementation MUST match specification exactly—no undocumented behavior
- No hallucinated features or assumptions beyond what is specified

### III. Beginner-Friendly Professional Design

Code MUST be clear, readable, and professionally structured:

- Use descriptive variable and function names (no abbreviations)
- Prefer simple, idiomatic Python patterns over clever solutions
- Include brief comments only where logic is non-obvious
- Follow PEP 8 style guidelines consistently
- Structure code for teachability—a Python beginner should understand it

### IV. Deterministic Explainable Behavior

All application behavior MUST be predictable and demonstrable:

- Same input MUST always produce same output
- Error messages MUST be clear and actionable
- All state changes MUST be explicit and traceable
- Behavior MUST be suitable for live demos without surprises
- No side effects or hidden state modifications

### V. Appropriate Simplicity (YAGNI)

Solutions MUST be the simplest that satisfy requirements:

- No over-engineering or premature abstractions
- No features beyond Phase I scope
- No patterns that add complexity without clear benefit
- Every line of code MUST justify its existence
- When in doubt, choose the simpler approach

### VI. Full Traceability

All artifacts MUST maintain clear provenance:

- Every code change traces to a task ID
- Every task traces to a specification
- Every specification traces to this constitution
- Prompt History Records (PHRs) capture all significant interactions
- Architecture Decision Records (ADRs) document significant choices

## Technology Stack

| Component | Specification |
|-----------|---------------|
| Language | Python 3.13+ |
| Environment | UV for dependency and environment management |
| AI Tooling | Claude Code with Spec-Kit Plus |
| Interface | Command-line only (stdin/stdout) |
| Storage | In-memory only (no persistence between runs) |
| Source Control | GitHub |

## Constraints

### Phase I Scope (STRICT BOUNDARIES)

This constitution governs Phase I only. The following constraints are absolute:

**ALLOWED:**
- Command-line interface via `input()` and `print()`
- In-memory data structures (lists, dictionaries)
- Basic Python standard library only
- Five core features: Add Task, View Tasks, Update Task, Delete Task, Mark Complete/Incomplete

**PROHIBITED:**
- Databases (SQLite, PostgreSQL, etc.)
- File persistence (JSON, CSV, pickle, etc.)
- APIs or network calls
- Web frameworks (Flask, FastAPI, Django)
- GUI frameworks (Tkinter, PyQt, etc.)
- Async/await patterns
- Distributed systems concepts
- Features from Phase II or later
- Third-party libraries beyond standard library

### Code Quality Gates

All code MUST pass these checks before approval:

- [ ] Follows PEP 8 style guidelines
- [ ] No unused imports or variables
- [ ] All functions have clear, single responsibilities
- [ ] Error handling is present for user input
- [ ] No hardcoded values that should be configurable
- [ ] No security vulnerabilities (command injection, etc.)

## Success Criteria

Phase I is complete when ALL of the following are true:

1. **Feature Completeness**: Working console application with all 5 core features
   - Add Task: User can create new tasks with titles
   - View Tasks: User can see all tasks with status
   - Update Task: User can modify existing task details
   - Delete Task: User can remove tasks
   - Mark Complete/Incomplete: User can toggle task status

2. **Workflow Compliance**: All code generated via approved Spec-Kit workflow
   - Every feature has corresponding spec.md
   - Every spec has corresponding plan.md
   - Every plan has corresponding tasks.md
   - All tasks completed and verified

3. **Documentation**: Repository includes required documentation
   - README.md with setup and execution instructions
   - CLAUDE.md with agent guidance
   - All specs preserved in `/specs` directory

4. **Traceability**: Full audit trail exists
   - Constitution ratified and versioned
   - PHRs recorded for significant interactions
   - ADRs created for architectural decisions

5. **Demo Readiness**: Application suitable for evaluation
   - Clean startup and shutdown
   - Intuitive menu navigation
   - Graceful error handling
   - Predictable, explainable behavior

## Governance

### Amendment Process

1. Proposed changes MUST be documented with rationale
2. Changes MUST be reviewed against success criteria impact
3. Version MUST be incremented according to semantic versioning:
   - MAJOR: Backward-incompatible principle changes
   - MINOR: New principles or significant expansions
   - PATCH: Clarifications and non-semantic refinements
4. All dependent artifacts MUST be reviewed for sync

### Compliance Verification

- All PRs MUST verify constitution compliance before merge
- Complexity additions MUST be justified in writing
- Scope violations MUST be rejected without exception
- PHRs MUST be created for all significant interactions

### Authority Hierarchy

1. This Constitution (highest authority)
2. Feature Specifications
3. Implementation Plans
4. Task Definitions
5. Generated Code

Lower-level artifacts MUST NOT contradict higher-level artifacts. Conflicts are resolved by deferring to the higher authority.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30
