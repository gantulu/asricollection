# Coding Prompt System

Dokumentasi untuk workflow AI coding yang modular, berbasis bukti, dapat diaudit, dan dikendalikan melalui persetujuan.

## Repository layout

```text
README.md
coding-prompt-system/
├── MASTER_PROMPT.md
├── INSTRUCTION.md
├── variables.yaml
├── REQUIREMENTS.md
├── ACCEPTANCE_CRITERIA.md
├── WORKFLOW.md
├── VERIFICATION.md
├── CHANGELOG.md
├── SOURCE_OF_TRUTH.md
├── IMPLEMENTATION_PLAN.md
├── AUDIT_REPORT.md
└── DECISIONS.md
```

## Start here

1. Read [MASTER_PROMPT.md](coding-prompt-system/MASTER_PROMPT.md).
2. Load [INSTRUCTION.md](coding-prompt-system/INSTRUCTION.md) and [variables.yaml](coding-prompt-system/variables.yaml).
3. Review [SOURCE_OF_TRUTH.md](coding-prompt-system/SOURCE_OF_TRUTH.md) and [REQUIREMENTS.md](coding-prompt-system/REQUIREMENTS.md).
4. Record findings in [AUDIT_REPORT.md](coding-prompt-system/AUDIT_REPORT.md).
5. Define [ACCEPTANCE_CRITERIA.md](coding-prompt-system/ACCEPTANCE_CRITERIA.md) and [IMPLEMENTATION_PLAN.md](coding-prompt-system/IMPLEMENTATION_PLAN.md).
6. Follow [WORKFLOW.md](coding-prompt-system/WORKFLOW.md); obtain required approval before changes.
7. Verify using [VERIFICATION.md](coding-prompt-system/VERIFICATION.md).
8. Record decisions and changes in [DECISIONS.md](coding-prompt-system/DECISIONS.md) and [CHANGELOG.md](coding-prompt-system/CHANGELOG.md).

## Stable filenames and internal versioning

Each document keeps its filename and path. V1, V2, V3, and later versions are recorded inside the same file. V1 is preserved as the baseline; later versions are additive and must not silently remove or rewrite prior requirements. Do not create per-version filenames.

Version status must be explicit: Proposed, Approved, Implemented, Verified, Blocked, or Unverified. A version's status must reflect evidence, not intention.

## Operating principles

- Evidence first; distinguish observed facts from assumptions.
- Read-only by default during audit.
- Preserve existing code, requirements, and history.
- Minimize changes and stay within approved scope.
- Never invent APIs, schemas, environment variables, or test results.
- Protect secrets and sensitive values.
- Do not deploy, change databases/secrets, or trigger real payments without separate explicit authorization.

## Status vocabulary

Requirement classification: Existing, Partial, Missing, Unverified, Blocked.
Lifecycle status: Proposed, Approved, Implemented, Verified, Blocked, Unverified.

This README describes the documentation system. It does not itself prove a project has been audited, implemented, or tested.

## VERSION INDEX
- V1 — Initial documentation entry point; status: Draft.
- V2 — Additive documentation updates; status: Implemented.
- V3 — Future additive updates; status: Proposed.

## VERSION V1 — BASELINE
Status: Draft
Defines navigation, stable filenames, internal versioning, operating principles, and workflow.

## VERSION V2 — ADDITIVE EXTENSION
Status: Implemented
Changes: See the V2 documentation control contract below; preserve V1.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Reserved for future additions; preserve V1 and V2.


## VERSION V2 — DOCUMENTATION CONTROL CONTRACT
Status: Implemented
Based on: V1
Change summary: Unify lifecycle and audit classifications; add requirement traceability and automated documentation validation.

### Canonical status contract
- Version/requirement lifecycle: Proposed → Approved → Implemented → Verified; Blocked and Unverified are non-success terminal/current states. Rejected and Superseded are decision-record statuses only.
- Audit classification describes observed implementation only: Existing, Partial, Missing, Unverified, Blocked. It is not a lifecycle status.
- Status transitions require evidence. Approval is explicit; implementation requires a recorded change; verification requires recorded check output.
- V1 remains immutable baseline content. V2/V3 additions are stored in this same file; filenames and paths remain stable.

### Traceability chain
Requirement ID → acceptance criterion ID → implementation/file evidence → verification check/result. Missing links must be reported, never inferred.

### Validation
Run `python scripts/validate_coding_prompt_docs.py`. GitHub Actions runs the same validator for pull requests and pushes. See [VERIFICATION.md](coding-prompt-system/VERIFICATION.md).
