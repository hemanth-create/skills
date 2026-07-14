---
name: local-sast-analyzer
description: "Perform a local-only pre-SAST review or triage a user-provided SARIF, CSV, or JSON export. Use only when the user explicitly invokes /local-sast-analyzer; require evidence for findings, avoid vendor APIs, and do not edit source without separate approval."
---

# Local SAST Analyzer

Review static repository evidence before an official scan or triage a scanner export without treating scanner output as automatic truth.

## Invocation and modes

Run only after explicit `/local-sast-analyzer` invocation. Work from local repository files and user-provided exports only. Do not call vendor APIs, authenticate to scanners, change scanner dispositions, commit, push, or edit source without separate approval.

- **Pre-SAST:** Review a selected local project before an official scan.
- **Post-SAST:** Triage a user-supplied SARIF, CSV, or JSON export.

If a monorepo has several plausible projects, list them and ask the user to choose. For post-SAST mode, ask for the export path if it was not supplied.

## Safe scope

Read applicable `CLAUDE.md` first. Follow its command policy. This is static analysis: do not run application code, builds, tests, package installs, virtual-environment activation, network calls, or scanner commands unless the user separately approves them.

Restrict discovery to the chosen project. Exclude dependency/vendor directories, build output, binaries, and fixtures by default unless they are deployed or security-relevant. Do not read `.env`, private keys, credential files, or secret stores without explicit user approval. When a possible secret is relevant, report only a masked indicator and its location.

## Evidence standard

Every reported finding must state:

- classification, severity, exact file and line when available;
- the suspicious source, sink, control, or configuration evidence actually observed;
- reachability as `reachable`, `unreachable`, or `unknown` with a reason; and
- a specific remediation and validation approach.

Use a source-to-sink trace only when the finding has one. For hardcoded secrets, insecure configuration, or missing controls, leave source and sink absent rather than inventing a data flow.

Use these classifications exactly:

- `CONFIRMED`
- `CANDIDATE`
- `LIKELY_FALSE_POSITIVE`
- `DEAD_OR_UNREACHABLE`
- `NEEDS_HUMAN_REVIEW`
- `FIXED_PENDING_RESCAN`

Use `critical` or `high` only for a reachable, high-impact weakness supported by concrete evidence. An unverified pattern remains a `CANDIDATE` at `medium` or lower unless local evidence proves stronger impact.

## Pre-SAST workflow

1. Identify the selected project, entry points, languages, package/build files, and externally reachable boundaries.
2. Inventory high-risk surfaces: authentication and authorization, request handling, database access, file handling, deserialization, network calls, redirects, crypto, configuration, sessions, and error handling.
3. Search focused high-signal patterns and deduplicate by root cause, file, sink, and weakness category.
4. Trace only the files necessary to establish reachability, controls, and exploitability. Record uncertainty instead of guessing.
5. Prioritize confirmed and high-impact candidates with project-native remediation and focused tests.

## Post-SAST workflow

1. Parse the export structurally. For SARIF, use `scripts/normalize_sarif.py` when local command policy permits; it only reads an export and writes JSON to standard output unless an output path is requested.
2. Preserve scanner rule IDs, messages, paths, locations, and data-flow locations when present. Record unsupported or unresolved fields rather than dropping them silently.
3. Map paths to the selected repository and inspect the reported code plus only the required callers or controls.
4. Group duplicates by root cause, classify each finding from local evidence, and mark locally remediated code as `FIXED_PENDING_RESCAN` until a new scan confirms it.

## Output and approval gate

Return a Markdown report in chat by default. Use a short finding list for a narrow review; add an executive summary, coverage, and detailed sections only for a repository-wide review or multiple findings. Save a report file only when the user asks or repository rules require it.

```markdown
## Local SAST Review

- Mode: <pre-SAST | post-SAST>
- Scope: <project and files or export>
- Coverage and limits: <what was reviewed and what remains unknown>

## Findings

- [classification] [severity] `path:line` — evidence, reachability, remediation, and validation.

## Recommended Next Action

1. <one safe, concrete next action>
```

Before editing source, ask for explicit approval and list the files, findings, expected risk, and verification. Keep approved remediation small and project-native. Read [references/security-standards.md](references/security-standards.md) only when you need standards context, CWE/OWASP mapping, or SARIF format guidance.
