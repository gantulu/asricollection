# WORKFLOW

## VERSION INDEX
- V1 — Baseline specification; status: Draft.
- V2 — Reserved for additive changes; status: Proposed.
- V3 — Reserved for subsequent additive changes; status: Proposed.

## VERSIONING RULES
- Keep this filename and path stable across versions.
- Preserve all prior version content; never silently overwrite or remove requirements.
- Add each new version in this same file, with date, based-on version, status, change summary, and full specification where applicable.
- Statuses are distinct: Proposed, Approved, Implemented, Verified, Blocked, Unverified.
- Do not represent a proposed version as approved, implemented, or verified.
- Approval requirements and higher-priority safety constraints always apply.

## VERSION V1 — BASELINE
Status: Draft
Based on: Initial specification
### Stage 1 — Load
Read Master Prompt, applicable instructions, variables, requirements, source-of-truth policy, and relevant decisions. Record unavailable inputs.

### Stage 2 — Audit
Inspect repository and current implementation. Audit is read-only. Cite evidence and do not infer that missing evidence proves absence unless the inspected scope is sufficient.

### Stage 3 — Classify
Map each requirement to Existing, Partial, Missing, Unverified, or Blocked. Record evidence and dependencies.

### Stage 4 — Recommend and plan
Describe recommended approach, alternatives where material, affected files, risks, acceptance criteria, and verification plan.

### Stage 5 — Approval gate
Wait for explicit approval when required. Approval for one scope does not authorize unrelated changes or external side effects.

### Stage 6 — Implement
Make minimal changes only to approved files and behaviors. Preserve existing work. Record unexpected blockers before expanding scope.

### Stage 7 — Verify
Run relevant checks available in the project. Separate successful, failed, skipped, and unavailable checks.

### Stage 8 — Report
Summarize outcomes, changed files, requirement traceability, evidence, risks, and follow-up work.

### Workflow exception
If the user explicitly authorizes a precise implementation scope and workflow policy allows it, proceed within that scope. Never bypass higher-priority safety requirements.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
