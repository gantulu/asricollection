# IMPLEMENTATION PLAN

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
Status: Implemented
Based on: V1
Changes: See the V2 additive control sections in this file.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.


## VERSION V2 — DOCUMENTATION CONTROL PLAN
Status: Implemented
Based on: V1
Change summary: Add traceable plan for documentation controls.

### Plan DOCS-V2
- Scope: Documentation workflow, requirement traceability, configuration validation, CI validation, and cross-file consistency only.
- Out of scope: Application code, backend, database/schema/RLS, secrets, deployment, and real payments.
- Requirements: REQ-009–REQ-020; acceptance: AC-009–AC-020.
- Files: Existing 13 documentation files plus `scripts/validate_coding_prompt_docs.py` and `.github/workflows/coding-prompt-docs.yml`.
- Risks: Markdown link parsing edge cases, YAML parser dependency, stale status/evidence. Mitigation: deterministic checks and explicit result reporting.
- Verification: `python scripts/validate_coding_prompt_docs.py`, inspect stable paths/version headings, and confirm CI invokes validator.
- Approval: Current user request authorizes these documentation controls only.
- Rollback: Revert the documentation-only commit while preserving prior history.


## V3 — CANONICAL DOCUMENT REFERENCES
Status: Implemented
Based on: V2

This document retains its specific purpose and historical V1/V2 content. Reusable coding workflow, approval gates, version/status semantics, and general change control are owned by [coding-prompt-system/MASTER_PROMPT.md](MASTER_PROMPT.md). Asri Collection Storefront/Admin requirements and frontend-only scope are owned by [masterprompt.md](../masterprompt.md). Keep this document focused on its named function; refer to those sources instead of copying their full rules.
