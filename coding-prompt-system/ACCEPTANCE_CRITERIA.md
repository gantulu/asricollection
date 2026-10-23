# ACCEPTANCE CRITERIA

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
Define objective, testable conditions for accepting an audit, plan, or implementation.

### General criteria
- Every in-scope requirement has an ID and a documented status.
- Audit claims are supported by file paths, code references, command output, or other available evidence.
- Each planned change names affected files, reason, risk, and expected behavior.
- Changes do not exceed approved scope.
- Existing relevant behavior is preserved or regression impact is documented.
- Build, lint, and tests are reported only when actually run.
- Unavailable checks are marked with reasons.
- Final report lists changed files and maps outcomes to acceptance criteria.
- Prior versions remain present within the same filenames.
- No unauthorized database, secret, deployment, or real-payment action occurs.

### Feature-specific criteria
Add measurable criteria for each feature before implementation. Include normal paths, empty/loading/error states, accessibility/responsiveness where relevant, and regression cases. Do not invent project-specific behavior without evidence or approval.

## VERSION V2 — ADDITIVE EXTENSION
Status: Proposed
Based on: V1
Changes: Not yet specified. Add approved additions here without deleting V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.
