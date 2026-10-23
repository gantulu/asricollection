# CHANGELOG

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
Summarize additions and changes across versions while each document retains its own internal history.

### Entry format
For each entry record version, date (ISO 8601 when known), status, source version, changed files, change summary, rationale, approval reference, and verification evidence.

### Rules
- Changelog entries do not replace version content in individual files.
- Distinguish proposed, approved, implemented, and verified changes.
- Do not invent dates, approvals, commits, or verification results.
- Record reversals and corrections transparently; preserve previous history.

## VERSION V2 — ADDITIVE EXTENSION
Status: Implemented
Based on: V1
Changes: See the V2 additive control sections in this file.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.


## VERSION V2 — DOCUMENTATION CONTROL
Status: Implemented
Based on: V1
Date: 2026-10-23
Approval reference: User request in the current conversation to implement versioning/status, traceability, workflow, source/configuration alignment, audit trail, automated validation, and cross-file verification.
Changed files: Existing 13 documentation files plus `scripts/validate_coding_prompt_docs.py` and `.github/workflows/coding-prompt-docs.yml`.
Summary: Standardized lifecycle and audit statuses; added REQ-009–REQ-020 and AC-009–AC-020; defined workflow stage contracts; aligned source/configuration rules; added automated documentation validation and CI.
Verification evidence: Pending execution of validator and cross-file checks. Do not mark V2 Verified until checks pass.
