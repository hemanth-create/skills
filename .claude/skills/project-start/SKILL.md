---
name: project-start
description: "Bootstrap or refresh a repo-local Claude Code workspace from verified repository evidence. Use only after explicit /project-start invocation; perform read-only discovery first and do not rewrite an existing CLAUDE.md without user confirmation."
---

# Project Start

Use this skill to make a repository easier for future Claude Code work without treating onboarding as a code change. It is not for generic repository questions.

## Ownership and boundaries

Run only after explicit `/project-start` invocation. Read applicable repository instructions before writing anything.

- An existing `CLAUDE.md` is repository-owned: preserve it unless the user explicitly asks to change a named section.
- If no `CLAUDE.md` exists, create a minimal one only from verified repository facts and user-provided command boundaries. Mark unknowns rather than inventing commands, architecture, or deployment ownership.
- Create missing `.claude/README.md` and `.claude/status.md` from [the onboarding templates](references/onboarding_templates.md). Preserve useful existing content; update only clearly generated status facts.
- Do not copy helper folders, add dependencies, alter source/configuration, or turn an onboarding artifact into canonical product documentation.

## Workflow

1. Determine the workspace root and read its instructions. Use repository-prescribed, read-only inspection tools where available.
2. Discover only lightweight source-of-truth material needed for onboarding: root README, manifests, configuration, directory layout, test guidance, and existing developer docs. Do not inspect secrets or sensitive data.
3. Do not run git, tests, builds, installs, linters, package managers, cloud, Docker, database, migration, deployment, or live-service commands during discovery.
4. Record verified repository shape, known commands, safety boundaries, and gaps. Keep command guidance factual; do not import global rules that are not present in the repository or user request.
5. Create or safely refresh the onboarding files allowed by the ownership rules, then save one artifact under `.claude/artifacts/project-start/YYYY-MM-DD_HHmm_<topic>.md`. Never overwrite an artifact; append `-2`, `-3`, and so on when needed.
6. Re-read the files written and report what changed, what was intentionally not changed, discovery sources, and the next safe action.

## Artifact requirements

The artifact must include the repository root, files read, files created or updated, detected layout, verified command guidance, unknowns, skipped commands, and the suggested next action. Redact secrets, tokens, credentials, account IDs, PHI, raw transcripts, and sensitive logs.

Use `status: blocked` when missing instructions or an ownership conflict prevents safe onboarding; otherwise use `status: completed`. Do not create an artifact when the workspace root itself is unknown.

## Final response

State the onboarding and artifact paths, any preserved file that was intentionally not changed, and one recommended next action. Do not invoke `/plan-it`, `/execute`, or another skill automatically.
