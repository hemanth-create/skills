---
name: error-triage
description: "Diagnose a concrete pasted failure from logs, stack traces, test output, or build output. Use only when the user explicitly invokes /error-triage; establish an evidence-backed root cause and propose or apply a narrow safe fix."
---

# Error Triage

Turn failure evidence into the smallest safe next action. This is for a concrete error, not an open-ended request to improve a codebase.

## Invocation and inputs

Run only after explicit `/error-triage` invocation. Start with the error text and failing command. Use expected versus actual behavior, reproduction steps, runtime/version, and recent changes when they are available. Ask one focused question only when a missing detail blocks a responsible diagnosis.

## Modes

- **Explain:** Diagnose the failure and recommend a next step. Do not edit files.
- **Fix:** Use only when the user explicitly asks for a fix. Make one narrow, evidence-backed change.
- **Plan:** Use when a safe fix needs multiple design decisions, cross-cutting changes, schema or deployment work, or live-system knowledge. State the decision needed and stop; do not invoke another skill automatically.

## Workflow

1. Read applicable `CLAUDE.md` and any repo-local inspection guidance. Follow the repository's command, test, data, and approval rules.
2. Preserve the useful evidence: exception type, status, first repo-owned frame, command, file path, line number, and relevant timestamp. Redact secrets, credentials, PHI, raw transcripts, account identifiers, and private data.
3. State the initial diagnosis:
   - Symptom: what failed.
   - Root-cause candidate: the most likely cause.
   - Evidence: the exact log line or `path:line` supporting it.
   - Confidence: `high`, `medium`, or `low`.
4. Read only the implicated code and nearby callers or configuration. Treat framework and dependency frames as context, not automatically as the cause.
5. Confirm or revise the diagnosis by tracing the failing path, input shape, configuration, and stated environment assumptions. Never invent unseen runtime state.
6. Choose the next action:
   - In **Explain** mode, stop after the diagnosis and recommendation.
   - In **Fix** mode, use `apply_patch` only on files needed for the confirmed cause.
   - In **Plan** mode, give a concrete decision-aware plan rather than making a broad patch.
7. After a fix, re-read changed sections and run the smallest focused verification allowed by repository rules. If verification fails or cannot run, say so plainly; do not claim the failure is resolved.

## Safety boundaries

- Follow repository policy for commands. Do not install packages, access credentials, call live services, deploy, or change infrastructure without explicit user approval.
- Do not add dependencies, rename or delete files, alter schemas, edit generated output, or make broad formatting changes unless the user separately approves that scope.
- Recommend another workflow when helpful, but do not invoke it automatically.
- Do not create an artifact by default. Save one only when the user asks or repository rules require it. Use `.claude/artifacts/error-triage/YYYY-MM-DD_HHmm_<topic>.md` and record only confirmed, redacted facts.

## Response format

```markdown
## Diagnosis

- Symptom: <what failed>
- Root cause: <confirmed cause or best-supported hypothesis>
- Evidence: `<path:line>` or concise error excerpt
- Confidence: <high | medium | low>

## Change or Recommendation

- <what changed, or the safest next action>

## Verification

- <check and result, or why it was not run>

## Next Step

- <one concrete action>
```
