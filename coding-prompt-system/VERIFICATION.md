# VERIFICATION

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
Specify evidence-based verification for code and documentation changes.

### Verification checklist
1. Inspect the final diff and ensure scope compliance.
2. Check syntax and formatting where tooling is available.
3. Run repository-defined lint command if present.
4. Run relevant tests if present.
5. Run build if a build script is present and dependencies/environment permit.
6. Check affected behavior and regression risks.
7. Check links, paths, filenames, and version indexes for documentation changes.
8. Verify requirement-to-evidence traceability.
9. Report skipped checks and exact reasons.

### Result vocabulary
- PASS: command/check ran and passed.
- FAIL: command/check ran and failed.
- BLOCKED: prerequisite or access prevented execution.
- NOT RUN: intentionally not executed.
- NOT AVAILABLE: no supported command/tool found.

Never infer PASS from the absence of an error message if the check did not execute. Do not claim UI, integration, security, or production behavior was verified without appropriate evidence.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
