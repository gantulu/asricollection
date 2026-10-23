# REQUIREMENTS

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
Maintain stable requirement IDs, definitions, lifecycle status, and traceability.

### Requirement record fields
Each requirement should include: ID, title, description, source, priority, status, dependencies, acceptance criteria, evidence, and version introduced.

### Status
Use Proposed, Approved, Implemented, Verified, Blocked, or Unverified for lifecycle. For implementation audit use Existing, Partial, Missing, Unverified, or Blocked.

### Rules
- Keep IDs stable when the requirement meaning remains unchanged.
- Do not mark requirements Approved without explicit approval.
- Do not mark Implemented or Verified without evidence.
- Record conflicts, duplicates, dependencies, and supersession explicitly.
- New versions are additive; document changes instead of silently deleting old requirements.

### Initial baseline requirements
- REQ-001: Preserve repository work and existing functionality.
- REQ-002: Inspect actual repository before proposing code changes.
- REQ-003: Define explicit scope and out-of-scope actions.
- REQ-004: Require approval when the applicable workflow requires it.
- REQ-005: Link implementation changes to requirements and acceptance criteria.
- REQ-006: Verify changes with available checks and report actual outcomes.
- REQ-007: Keep filenames stable and store version history internally.
- REQ-008: Protect secrets and avoid unauthorized external side effects.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
