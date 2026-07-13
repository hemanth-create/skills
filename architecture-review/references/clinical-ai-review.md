# Clinical AI Review Reference

Read this reference only for systems that process clinical data, PHI, transcripts, LLM outputs, or generated form answers.

## Data and tenant boundaries

- Trace PHI from intake through processing, storage, logs, callbacks, and deletion.
- Confirm tenant and application isolation at every lookup, storage key, queue message, and callback.
- Identify retention, TTL, redaction, audit, and artifact-cleanup behavior.

## Model and evidence controls

- Confirm which facts must be deterministic and which may be model-inferred.
- Verify output-schema validation, retry behavior, confidence handling, and hallucination containment.
- Verify that generated answers can be traced to supporting source spans when evidence is required.
- Confirm that model, prompt, and form/version identifiers make outputs reproducible.

## Safety and operations

- Check escalation and review paths for self-harm, suicidality, or other safety-sensitive content.
- Check whether synthetic data, transcripts, feedback, and generated answer packages remain separated.
- Check idempotency, partial writes, retries, dead-letter handling, observability, cost/latency limits, and rollback behavior.

Report only controls that are supported by evidence. Mark the rest as assumptions or unknowns.
