# Repository Guidelines

## Purpose

This repository is a practical, curated collection of reusable skills for Claude Code and Codex. A skill should solve one repeatable workflow clearly enough that another developer or agent can use it without tribal knowledge.

## Repository layout

- Keep each skill under `.codex/skills/<skill-name>/SKILL.md`.
- Use lowercase kebab-case directory names, such as `aws-investigation` or `pr-review`.
- Keep shared examples, scripts, or reference material inside that skill's directory.
- Keep the root `README.md` focused on discovering and using the collection.

## Writing skills

- Begin every `SKILL.md` with valid YAML front matter containing `name` and `description`.
- Make the description specific about when the skill should be used and when it should not.
- Write actionable, ordered instructions; explain required inputs, safe defaults, verification, and likely failure cases.
- Prefer small, focused skills over broad catch-all instructions.
- Do not include secrets, personal tokens, customer data, or environment-specific credentials.
- Preserve the intent of an imported skill unless a change is explicitly requested.

## Quality check before committing

- Review every changed `SKILL.md` for valid Markdown and YAML front matter.
- Make sure paths, commands, links, and tool names are real and current.
- Check that examples are safe to copy and do not perform destructive actions by default.
- Keep unrelated cleanup out of the same change.

## Git workflow

- Inspect the working tree before making changes; preserve work that is already present.
- Use a focused branch and concise commit message for each logical improvement.
- Do not push, open a pull request, or merge changes without the user's explicit approval.
