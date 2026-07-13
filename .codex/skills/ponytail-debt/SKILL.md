---
name: ponytail-debt
description: "Report deliberate, structured Ponytail shortcuts in a named repository scope without changing files. Use only after explicit $ponytail-debt or slash invocation; distinguish complete markers from incomplete or legacy markers instead of inventing missing context."
---

# Ponytail Debt

Use this read-only skill to make intentional shortcuts visible. It reports `ponytail:` markers; it does not decide whether to implement their upgrades.

## Marker contract

The preferred one-line marker is:

```text
<comment prefix> ponytail: <shortcut>; ceiling: <limit>; upgrade: <observable trigger>
```

For example:

```python
# ponytail: one global lock; ceiling: cross-account contention; upgrade: contention is measured in production
```

Do not infer a missing ceiling or trigger. Preserve free-form historical markers as `legacy` rather than pretending they meet the contract.

## Workflow

1. Run only after explicit `$ponytail-debt` invocation, or its supported slash form. Use the named scope or the current repository root if none is specified.
2. Read applicable `AGENTS.md` instructions. Use repository-approved, read-only search tools; exclude generated, vendored, cache, dependency, virtual-environment, and `.git` paths.
3. Find candidate `ponytail:` strings, then confirm each is an actual source-code comment rather than a string literal or prose mention.
4. Classify each marker as `complete`, `missing-ceiling`, `missing-upgrade`, `missing-both`, or `legacy`. Keep the shortcut text and raw marker evidence.
5. If the user asks for ownership, use line-specific blame only when the repository supports it. Do not run blame by default.

## Report

```markdown
## Ponytail debt
- Scope: `<path>`
- Scan notes: excluded generated or dependency paths.

### Markers
- `path:line` [complete] — shortcut: …; ceiling: …; upgrade: …
- `path:line` [missing-upgrade] — shortcut: …; ceiling: …; upgrade: missing

### Summary
`N complete, M incomplete, L legacy markers.`
```

If no confirmed marker exists, report: `No ponytail: debt in <scope>. Clean ledger.`

Do not edit files or create a ledger artifact. If the user asks to persist the report but does not name a destination, ask for the target path first.
