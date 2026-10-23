# REQUIREMENTS

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
Status: Implemented
Based on: V1
Changes: See the V2 additive control sections in this file.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.


## VERSION V2 — REQUIREMENT SCHEMA AND TRACEABILITY
Status: Implemented
Based on: V1
Change summary: Preserve REQ-001–REQ-008 and add standardized records for documentation-system controls.

### Canonical record schema
Each record must provide: ID, title, description, source, priority (P0/P1/P2), lifecycle status, dependencies (IDs or `None`), acceptance criteria IDs, evidence (path/URL/commit or `Pending`), and introduced version. Stable IDs are never reused. `Pending` explicitly means evidence has not yet been supplied.

### Additional requirements

#### REQ-009 — Canonical lifecycle and audit statuses
- Description: Separate lifecycle status from observed implementation classification and define evidence-backed transitions.
- Source: Documentation-system audit; Priority: P0; Status: Implemented
- Dependencies: REQ-007; Acceptance: AC-009; Evidence: `coding-prompt-system/README.md`, `coding-prompt-system/VERIFICATION.md`; Introduced: V2

#### REQ-010 — Requirement traceability
- Description: Link every requirement to acceptance criteria, change evidence, and verification results.
- Source: Documentation-system audit; Priority: P0; Status: Implemented
- Dependencies: REQ-005, REQ-006; Acceptance: AC-010; Evidence: `coding-prompt-system/ACCEPTANCE_CRITERIA.md`, `coding-prompt-system/VERIFICATION.md`; Introduced: V2

#### REQ-011 — Additive versioning contract
- Description: Preserve V1 and append version history within stable filenames; distinguish Proposed, Approved, Implemented, and Verified.
- Source: User workflow constraints; Priority: P0; Status: Implemented
- Dependencies: REQ-007; Acceptance: AC-011; Evidence: all 13 documentation files; Introduced: V2

#### REQ-012 — Workflow stage contracts
- Description: Define stage inputs, outputs, stop conditions, and continuation rules.
- Source: Documentation-system audit; Priority: P0; Status: Implemented
- Dependencies: REQ-002, REQ-004; Acceptance: AC-012; Evidence: `coding-prompt-system/WORKFLOW.md`; Introduced: V2

#### REQ-013 — Source-of-truth precedence
- Description: Establish conflict handling and evidence precedence without treating proposals or secondary sources as production contracts.
- Source: Documentation-system audit; Priority: P0; Status: Implemented
- Dependencies: REQ-002; Acceptance: AC-013; Evidence: `coding-prompt-system/SOURCE_OF_TRUTH.md`; Introduced: V2

#### REQ-014 — Configuration validation
- Description: Validate YAML syntax, required keys, status vocabulary, and version index before workflow execution.
- Source: Documentation-system audit; Priority: P0; Status: Implemented
- Dependencies: REQ-006; Acceptance: AC-014; Evidence: `coding-prompt-system/variables.yaml`, `scripts/validate_coding_prompt_docs.py`; Introduced: V2

#### REQ-015 — Status transition evidence
- Description: Do not promote lifecycle status without the required approval, change evidence, or passing verification output.
- Source: Documentation-system audit; Priority: P0; Status: Implemented
- Dependencies: REQ-009; Acceptance: AC-015; Evidence: `coding-prompt-system/VERIFICATION.md`; Introduced: V2

#### REQ-016 — Reproducible audit report
- Description: Record repository, branch, commit, date when known, scope, inspected areas, findings, commands, outcomes, and limitations.
- Source: Documentation-system audit; Priority: P1; Status: Implemented
- Dependencies: REQ-002; Acceptance: AC-016; Evidence: `coding-prompt-system/AUDIT_REPORT.md`; Introduced: V2

#### REQ-017 — Changelog and decision history
- Description: Record dated changes, approvals, affected requirements, evidence, and supersession without fabricating missing data.
- Source: Documentation-system audit; Priority: P1; Status: Implemented
- Dependencies: REQ-007; Acceptance: AC-017; Evidence: `coding-prompt-system/CHANGELOG.md`, `coding-prompt-system/DECISIONS.md`; Introduced: V2

#### REQ-018 — Reviewable implementation plan
- Description: Map scope, requirements, files, dependencies, risks, acceptance, approval, and verification before execution.
- Source: Documentation-system audit; Priority: P1; Status: Implemented
- Dependencies: REQ-003, REQ-005; Acceptance: AC-018; Evidence: `coding-prompt-system/IMPLEMENTATION_PLAN.md`; Introduced: V2

#### REQ-019 — Automated documentation validation
- Description: Automatically validate required files, internal links, version sections, requirement/acceptance traceability, and YAML configuration.
- Source: Documentation-system audit; Priority: P1; Status: Implemented
- Dependencies: REQ-010, REQ-014; Acceptance: AC-019; Evidence: `scripts/validate_coding_prompt_docs.py`, `.github/workflows/coding-prompt-docs.yml`; Introduced: V2

#### REQ-020 — Scope and side-effect protection
- Description: Keep audit read-only by default and require separate explicit authorization for code/backend/database/secrets/deployment/real-payment side effects.
- Source: User workflow constraints; Priority: P0; Status: Implemented
- Dependencies: REQ-003, REQ-004, REQ-008; Acceptance: AC-020; Evidence: `coding-prompt-system/INSTRUCTION.md`, `coding-prompt-system/WORKFLOW.md`; Introduced: V2
