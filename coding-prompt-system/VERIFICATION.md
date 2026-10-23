# VERIFICATION

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
Status: Implemented
Based on: V1
Changes: See the V2 additive control sections in this file.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.


## VERSION V2 — AUTOMATED VALIDATION CONTRACT
Status: Implemented
Based on: V1
Change summary: Add deterministic checks for documentation integrity and traceability.

### Required automated checks
1. All 13 baseline documentation files exist at their stable paths.
2. Markdown local links resolve to existing files (ignore external URLs and anchor-only fragments; validate local target paths).
3. Each Markdown document retains V1, V2, and V3 version headings; the V2 status is not called Verified unless the relevant checks actually pass.
4. REQ-009–REQ-020 map to AC-009–AC-020 and acceptance criteria point back to requirement IDs.
5. `variables.yaml` parses as YAML and contains the required top-level keys and allowed lifecycle statuses.
6. GitHub Actions runs the validator on pushes and pull requests.

### Execution
Run: `python scripts/validate_coding_prompt_docs.py`
Expected successful exit code: 0. Any validation finding must produce a non-zero exit code. Record the actual command output; do not claim success until it has run.


## V3 — CANONICAL DOCUMENT REFERENCES
Status: Implemented
Based on: V2

This document retains its specific purpose and historical V1/V2 content. For current interpretation and future changes, reusable coding workflow, approval gates, version/status semantics, and general change control are governed by [coding-prompt-system/MASTER_PROMPT.md](MASTER_PROMPT.md). Asri Collection Storefront/Admin requirements and frontend-only scope are governed by [masterprompt.md](../masterprompt.md). Repeated V1/V2 wording is preserved as historical record, not a competing canonical source. Future additions must reference these canonical sources instead of restating their full rules.
