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


## VERSION V2 — TRACEABLE ACCEPTANCE CRITERIA
Status: Implemented
Based on: V1
Change summary: Add measurable acceptance checks for REQ-009–REQ-020.

- **AC-009 (REQ-009):** Lifecycle statuses and audit classifications are separately defined and consistently used; no status is inferred from another.
- **AC-010 (REQ-010):** Every REQ-009–REQ-020 record names at least one AC ID, and each AC ID names its related requirement; verification evidence is recorded or explicitly Pending.
- **AC-011 (REQ-011):** All 13 original documentation paths remain stable; V1 sections remain present; V2 status is not represented as Verified before checks pass.
- **AC-012 (REQ-012):** Each workflow stage specifies inputs, outputs, stop conditions, and continuation conditions.
- **AC-013 (REQ-013):** Source precedence is ordered; conflicts and inaccessible sources have an explicit handling rule.
- **AC-014 (REQ-014):** Validator parses variables.yaml and checks required configuration keys and allowed status values.
- **AC-015 (REQ-015):** Status promotion rules require explicit approval, recorded implementation, or passing verification as appropriate.
- **AC-016 (REQ-016):** Audit template includes repo/branch/commit/scope, inspected files, findings, commands/outcomes, and limitations.
- **AC-017 (REQ-017):** Changelog and decision records support approval/evidence links and do not fabricate unknown dates or outcomes.
- **AC-018 (REQ-018):** Plan template maps requirements to files, dependencies, risks, acceptance, approval, and verification.
- **AC-019 (REQ-019):** A local Python validator checks required paths, Markdown local links, version headings, traceability, and YAML; CI invokes it on push and pull request.
- **AC-020 (REQ-020):** Instructions and workflow explicitly prohibit out-of-scope side effects without separate authorization.
