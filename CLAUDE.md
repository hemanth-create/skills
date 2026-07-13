# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repository is a curated collection of reusable **skills** for Codex and Claude Code (see README.md). A skill is a bounded, explicitly-invoked workflow — not auto-triggered — that solves one repeatable task clearly enough that another developer or agent can use it without tribal knowledge.

There is no build or test tooling here — no package.json. A GitHub Actions workflow (`.github/workflows/ci.yml`) lints every `SKILL.md`'s front matter and every relative Markdown link on each pull request and push to `main`; run the same check locally with `pip install pyyaml && python3 .github/scripts/check_docs.py` (see `.github/scripts/check_docs.py`). Otherwise the repo is documentation/prompt content only; "development" means writing or editing Markdown skill files.

## Repository structure

- Each skill lives under `.codex/skills/<skill-name>/SKILL.md`, using lowercase kebab-case directory names (e.g. `architecture-review`).
- A skill's supporting material (reference docs, examples, scripts) stays inside that skill's own directory, e.g. `.codex/skills/architecture-review/references/clinical-ai-review.md`.
- `README.md` is the discovery/index surface for the collection — its skills table must stay in sync whenever a skill is added, renamed, or removed.
- `AGENTS.md` holds the authoritative repository guidelines (layout, writing conventions, git workflow); the important parts are folded into this file below.

## Anatomy of a SKILL.md

Every `SKILL.md` in this repo follows the same shape, established consistently across the current skills (`agent-relay`, `architecture-review`, `code-rewrite`):

1. **YAML front matter** with `name` and `description`. The `description` is the trigger contract: it must state explicitly when the skill applies *and* when it doesn't (e.g. "Use only when the user explicitly invokes @code-rewrite ... do not use for a broad refactor"). Skills here are opt-in only, never auto-invoked from a generic prompt.
2. **Scope/inputs** — what the skill requires before it can run (an explicit file list, a target document, a file path) and what to do when that's missing (ask one concise question rather than guessing).
3. **Workflow** — an ordered, numbered procedure.
4. **Output** — a fixed Markdown template returned in chat (verdict / findings / severity-tagged sections). Each skill defines its own severity vocabulary (e.g. `critical`/`high`, or a 0–10 score) and applies it consistently in that template.
5. **Artifacts** — a skill only writes a saved copy of its output when the user asks, under `.codex/artifacts/<skill-name>/YYYY-MM-DD_HHmm_<topic>.md`; otherwise the result stays in chat only.

Some skills also check for a `.helpers/README.md` at the start of their workflow and defer to it if present, falling back to normal repository tools otherwise — treat this as a hook for repo-specific overrides, not something to assume exists.

## Writing or editing a skill

- Prefer small, single-purpose skills over broad catch-all instructions. Keep file-target scope narrow (e.g. `code-rewrite` caps itself at 1–5 named files and hands broader work off to a planning recommendation rather than expanding its own scope).
- Only add instructions or context genuinely specific to the workflow — don't restate generic engineering advice.
- No secrets, personal tokens, customer data, or environment-specific credentials in any skill file.
- When a skill's content originated from an import, preserve its intent unless the user explicitly asks for a change.
- Before treating a skill change as done: confirm the front matter is valid YAML, verify every path/command/link/tool name mentioned actually exists, confirm examples are safe to copy (no destructive actions by default), and keep unrelated cleanup out of the same change.

## Git workflow

- Inspect the working tree before making changes; preserve work that is already present.
- Use one focused branch and a concise commit message per logical improvement.
- Do not push, open a pull request, or merge without the user's explicit approval for that specific action.
