---
name: deps-audit
description: Audit Python dependency manifests and lockfiles for reproducibility, resolver, and upgrade risk. Use only when the user explicitly invokes @deps-audit or /deps-audit; distinguish local manifest findings from live vulnerability evidence, and never claim current CVE status without current scanner output.
---

# Python Dependency Audit

Assess Python dependency configuration without turning stale model knowledge into a security finding.

## Modes

- **Manifest review:** Read dependency files and identify reproducibility, resolver, and upgrade-risk issues. This is the default and requires no network access.
- **Live vulnerability audit:** Use only when the user explicitly asks for live results or approves the required commands. Treat scanner output as the source of truth for current vulnerability findings.
- **Upgrade planning:** Assess a proposed package change against the repository's declared constraints, lockfile, Python version, callers, tests, and release notes supplied by the user or read with permission.

## Intake and source of truth

1. Read applicable repository instructions and identify the project boundary. In a monorepo, list discovered Python projects and ask the user to choose if the scope is broad.
2. Inventory `pyproject.toml`, `pylock*.toml`, `requirements*.txt`, `constraints*.txt`, `Pipfile`, `Pipfile.lock`, `setup.cfg`, and `setup.py` within that boundary.
3. Identify the dependency authority before comparing versions. Treat a declaration file and its lockfile as a pair, not as automatically conflicting sources.
4. Parse includes and constraints (`-r`, `-c`), environment markers, extras, hashes, editable dependencies, direct URLs, and the declared Python version before drawing conclusions.

## Manifest review

Report only evidence visible in local files, with `path:line` references. Check for:

- missing or stale lockfiles where the project expects reproducible application builds;
- unpinned or overly broad constraints when they conflict with the project's release model;
- incompatible constraints across the active dependency path;
- unsupported Python-version markers, duplicate declarations, direct URLs, or editable dependencies that need review;
- missing hashes or index policy when repository instructions require supply-chain controls.

Exact pins are often appropriate for deployed applications; compatible ranges are often appropriate for libraries. Do not label either pattern as wrong without understanding the project type.

## Live vulnerability audit

Do not assert a current CVE, fixed version, exploit status, or package age from model memory. Ask for permission to run a live scanner or ask the user to provide its output.

Use the narrowest applicable command, for example:

```bash
python -m pip_audit -r requirements.txt
python -m pip_audit --locked .
python -m pip check
```

Treat `pip check` as installed-environment compatibility evidence, not a manifest vulnerability audit. Never use `--fix` or modify dependency files unless the user separately requests a change.

## Output

```markdown
## Python Dependency Audit

- Mode: `<manifest review | live vulnerability audit | upgrade planning>`
- Scope: `<files and project boundary>`
- Evidence: `<local manifests | scanner output | both>`

## Findings

- [severity] `path:line` — issue, impact, and recommended action.

## Live Vulnerability Results

- Include only current scanner findings, their identifiers, affected versions, and available fixes.
- Otherwise: `No live vulnerability scan was run; no current CVE conclusion is made.`

## Upgrade Considerations

- Compatibility, lockfile, Python-version, and test implications.

## Recommended Next Step

1. <Concrete safe next action.>
```

Use `critical` or `high` only for confirmed live vulnerability evidence or a clearly demonstrated production-breaking dependency issue. Keep offline manifest hygiene findings at `medium` or `low` unless local evidence proves a stronger impact. Save an artifact only when the user asks or repository instructions require it.
