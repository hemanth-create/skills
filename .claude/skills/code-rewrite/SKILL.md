---
name: code-rewrite
description: Review or make a small, behavior-preserving quality improvement to one to five explicitly named source files. Use only when the user explicitly invokes @code-rewrite or /code-rewrite for targeted senior-level code review, cleanup, or overly verbose/AI-like code; do not use for a broad refactor or whole-repository audit.
---

# Code Rewrite

Review selected code with direct, evidence-based senior-engineering feedback. Rewrite only when the user explicitly asks for changes.

## Scope and modes

Require explicit file targets. Keep the normal scope to one through five source files. If the request names a broad folder or needs cross-cutting design, ask the user to narrow the target or recommend a planning workflow.

Choose a mode from the request:

- **Review only:** identify findings and recommendations; do not edit files.
- **Rewrite:** review first, make a short plan, then apply the requested targeted changes.
- **Findings to rewrite:** verify the cited findings against the named files before changing them.
- **Planning handoff:** stop after identifying the broader work when a safe rewrite would require a schema, public API, deployment, or multi-area design change.

## Workflow

1. Read applicable repository instructions. If `.helpers/README.md` exists, follow it; otherwise use normal repository tools.
2. Read the selected files. Identify their language, local conventions, observable behavior, direct callers, public interfaces, and relevant tests before judging or editing.
3. Review the code for behavior and edge cases, data and security boundaries, error handling, performance/reliability, local consistency, test coverage, naming, comments, and unnecessary complexity.
4. If the user asks whether code appears AI-generated, describe only observable low-maintenance signals such as boilerplate, stale comments, needless abstraction, or ignored callers. Do not make provenance or authorship claims.
5. For review-only mode, return the findings in chat. For rewrite mode, first state the files, behavior to preserve, intended changes, checks to run, and any assumption or blocker.
6. Edit only the selected files and directly related tests or documentation. Use a focused patch, preserve public behavior unless asked to change it, and re-read changed sections.
7. Run the most focused safe verification available. State clearly what ran, what passed, and what could not be verified.

## Rewrite guidance

Match the repository's language, conventions, and established architecture. Prefer the smallest clear diff. Extract a function, module, or abstraction only when it meaningfully improves responsibility, testing, or maintenance; never split cohesive code merely to meet an arbitrary line count.

Keep authorization and data-handling boundaries visible and testable. Follow the repository's existing enforcement pattern rather than imposing a universal controller/service/repository structure. Do not add dependencies, rename or delete files, change generated artifacts, or introduce broad formatting churn without approval.

## Output

Use this structure for a review:

```markdown
## Verdict

<Short judgment and score out of 10.>

## Findings

- [severity] `path:line` — problem, impact, and practical fix.

## Low-Maintenance Signals

- Specific observed signals, or "None significant."

## Verification

- Relevant tests, callers, or checks reviewed; limitations if any.

## Planning Candidates

- Broader follow-up work, or "None."
```

Use `critical` for likely security/privacy exposure, data loss, or production breakage; use `high` for a likely user-visible or unsafe behavior issue. Keep style-only findings low severity.

For a rewrite, also report changed files, preserved behavior, verification, and remaining risks. Save an artifact only when the user asks for one or repository instructions require it; otherwise keep the result in chat.
