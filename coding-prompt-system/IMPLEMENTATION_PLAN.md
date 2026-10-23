# IMPLEMENTATION PLAN

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
### Purpose
Record a reviewable, file-level plan before code changes.

### Required plan fields
- Plan ID and version
- Related requirement IDs
- Goal and in/out of scope
- Current-state evidence
- Proposed changes by file
- Dependencies and order
- Risks and rollback considerations
- Acceptance criteria
- Verification commands/checks
- Approval status and approval evidence

### Execution rules
A plan is not implementation authorization by itself. Mark proposed changes separately from completed changes. If the actual repository differs from the plan, pause the affected work and update the plan/seek approval when scope changes.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
