# SOURCE OF TRUTH

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
### Source precedence
1. Applicable higher-priority safety and platform rules.
2. Explicit user-approved decisions and scope for the current task.
3. Actual repository contents and commit/branch state for implementation facts.
4. Official documentation from the relevant technology/provider.
5. Approved project requirement and instruction documents.
6. Secondary sources, used only as supporting evidence.

### Evidence rules
- Cite the exact URL, file path, commit, or documentation section where available.
- For current implementation behavior, inspect repository code rather than relying on README claims alone.
- Use official Supabase, PostgreSQL, React, Vite, and Duitku documentation for their respective contracts.
- Do not treat an example, proposal, mock data shape, or unverified comment as a production contract.
- Record source access failures and conflicting evidence.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
