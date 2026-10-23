# INSTRUCTION

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
Define mandatory project-specific instructions and execution boundaries.

### Instruction loading
Before work, identify relevant instruction files, read the available content, record version/status, and report missing or unreadable instructions. Never claim to have followed content that was not inspected.

### Mandatory rules
- Preserve filenames and paths unless explicitly approved otherwise.
- Keep V1 and all previous versions intact; append additive V2/V3 sections inside the same file.
- Do not silently remove, weaken, duplicate, or reinterpret approved requirements.
- Stop and report conflicts that affect scope, safety, or correctness.
- Use official documentation and actual repository code as evidence.
- Do not commit, merge, deploy, alter database/schema/RLS/secrets, or execute real payments without explicit authorization for that action.
- Report scope deviations and failed or unavailable checks honestly.

### Priority
Applicable higher-priority system/safety rules prevail. Within project documents, use the approved source-of-truth policy and explicit decisions. If two approved project instructions conflict, do not choose silently; document the conflict and request resolution.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
