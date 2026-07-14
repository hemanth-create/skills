# Onboarding templates

Use these only for files that are missing or for clearly generated sections the user authorized updating.

## Minimal `CLAUDE.md`

```markdown
# Repository guidance

## Project overview

<Verified purpose and entry points, or `Unknown from reviewed evidence.`>

## Read first

- `<path>` — <why it matters.>

## Repository layout

- `<path>` — <observed purpose.>

## Commands and approval boundaries

- Allowed read-only discovery: <verified guidance or `Follow the active environment and user approval policy.`>
- Before running build, test, install, deployment, cloud, data, or destructive commands: <verified approval rule or `Ask the user.`>

## Sensitive files

- Do not read or expose secrets, credentials, private keys, production data, or other sensitive files unless the task explicitly requires it.

## Verification

- <Verified test or validation guidance, or `Unknown from reviewed evidence.`>
```

## `.claude/README.md`

```markdown
# Claude Code workspace

`.claude/` stores Claude Code working context and generated artifacts. It is not canonical product documentation.

- `artifacts/` — skill-generated work records.
- `status.md` — lightweight current project state.

Do not store secrets, tokens, credentials, private data, raw transcripts, or sensitive logs here. Keep canonical product documentation in the repository's normal documentation location.
```

## `.claude/status.md`

```markdown
# Claude Code project status

## Current goal

Unknown from reviewed evidence.

## Known plans and work

- No verified plan or execution artifact identified.

## Open risks and unknowns

- No additional risks identified from reviewed evidence.

## Suggested next action

Inspect the relevant repository area, then explicitly choose planning, implementation, or diagnosis.
```

## Project-start artifact

```markdown
---
skill: project-start
created: YYYY-MM-DD HH:mm TZ
task: <topic>
status: completed | blocked
source: <user request>
---

# Project Start: <topic>

## Workspace and discovery

- Root: `<path>`
- Files read: <paths>
- Detected layout: <facts only>

## Files written or preserved

- `<path>` — <created, updated, or intentionally preserved>

## Commands

- Not run: <categories and reason>
- Verified guidance: <commands or approval boundaries found in the repository>

## Unknowns and next action

- <gap, ownership conflict, or `None identified from reviewed evidence.`>
- Next: <smallest safe action>
```
