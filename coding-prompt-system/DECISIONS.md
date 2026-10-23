# DECISIONS

## VERSION INDEX
- V1 — Baseline specification; status: Draft.
- V2 — Reserved for additive changes; status: Implemented.
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
### Purpose
Maintain a durable record of decisions affecting requirements, scope, architecture, workflow, and implementation.

### Decision record
- Decision ID
- Date (only when known)
- Title and context
- Options considered
- Decision and rationale
- Status: Proposed, Approved, Superseded, or Rejected
- Approver/evidence when available
- Affected requirement IDs and files
- Consequences and review trigger

### Rules
Do not infer approval from discussion alone unless the user clearly approved the specific decision. Supersede decisions explicitly; preserve prior records and links. When decisions conflict, record the conflict and request resolution rather than silently choosing.

## VERSION V2 — ADDITIVE EXTENSION
Status: Implemented
Based on: V1
Changes: See the V2 additive control sections in this file.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.


## VERSION V2 — DOCUMENTATION CONTROL DECISIONS
Status: Implemented
Based on: V1
Change summary: Record scope authorization and the V2 status model.

### DEC-DOCS-002 — Implement documentation controls
- Date: 2026-10-23
- Context: Audit identified inconsistent status semantics, incomplete requirement traceability, underspecified workflow stages, and no automated validator.
- Decision: Add V2 controls in stable existing documentation paths and add a Python validator plus GitHub Actions workflow.
- Status: Approved for the scope stated in the current user request.
- Evidence: Current conversation request; resulting commit reference is pending until commit exists.
- Requirements: REQ-009–REQ-020; acceptance: AC-009–AC-020.
- Boundary: No app code, backend, database/schema/RLS, secrets, deployment, or real-payment operations.
- Consequence: V2 is Verified only after automated and cross-file checks pass.
