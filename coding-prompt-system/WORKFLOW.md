# WORKFLOW

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
### Stage 1 — Load
Read Master Prompt, applicable instructions, variables, requirements, source-of-truth policy, and relevant decisions. Record unavailable inputs.

### Stage 2 — Audit
Inspect repository and current implementation. Audit is read-only. Cite evidence and do not infer that missing evidence proves absence unless the inspected scope is sufficient.

### Stage 3 — Classify
Map each requirement to Existing, Partial, Missing, Unverified, or Blocked. Record evidence and dependencies.

### Stage 4 — Recommend and plan
Describe recommended approach, alternatives where material, affected files, risks, acceptance criteria, and verification plan.

### Stage 5 — Approval gate
Wait for explicit approval when required. Approval for one scope does not authorize unrelated changes or external side effects.

### Stage 6 — Implement
Make minimal changes only to approved files and behaviors. Preserve existing work. Record unexpected blockers before expanding scope.

### Stage 7 — Verify
Run relevant checks available in the project. Separate successful, failed, skipped, and unavailable checks.

### Stage 8 — Report
Summarize outcomes, changed files, requirement traceability, evidence, risks, and follow-up work.

### Workflow exception
If the user explicitly authorizes a precise implementation scope and workflow policy allows it, proceed within that scope. Never bypass higher-priority safety requirements.

## VERSION V2 — ADDITIVE EXTENSION
Status: Implemented
Based on: V1
Changes: See the V2 additive control sections in this file.

## VERSION V3 — ADDITIVE EXTENSION
Status: Proposed
Based on: V2
Changes: Reserved. Add approved additions here without deleting V1 or V2.


## VERSION V2 — STAGE CONTRACTS
Status: Implemented
Based on: V1
Change summary: Define inputs, outputs, stop conditions, and continuation rules for each stage.

| Stage | Required inputs | Output | Stop condition | Continue when |
|---|---|---|---|---|
| 1. Load | Master prompt, instructions, variables, requirements, source policy, decisions | Loaded-source/version checklist | Required source unreadable or absent | Required inputs are recorded; missing inputs are explicitly scoped |
| 2. Audit | Repository/ref, task scope, accessible evidence | Evidence-based current-state report | Scope/access unclear or evidence insufficient for a claim | Claims are linked to evidence and limitations stated |
| 3. Classify | Requirements and audit findings | Requirement status matrix | Conflicts or unknowns materially affect correctness | Each requirement has status, dependency, and evidence/Pending |
| 4. Recommend/plan | Status matrix, constraints | Alternatives/recommendation, file plan, ACs, risks | Scope change or unresolved architecture decision | Plan is traceable and stays within requested scope |
| 5. Approval gate | Plan and exact side effects | Approval record or hold | Explicit approval missing where required | Approved scope is unambiguous; otherwise stop before writes |
| 6. Implement | Approved plan and current repo state | Minimal changes and change record | Drift, unexpected side effect, or scope expansion | Change remains in scope; deviations are reported before proceeding |
| 7. Verify | Diff, ACs, available tools | PASS/FAIL/BLOCKED/NOT RUN/NOT AVAILABLE results | Critical check fails or cannot safely run | Results and limitations are accurately recorded |
| 8. Report | Change record and verification output | Summary, files, commit, evidence, unresolved items | Evidence needed for a claim is missing | Report distinguishes completed, verified, and pending work |

### Global continuation rule
A stage may not silently skip its stop condition. Approval for documentation changes does not authorize application code, backend/database/schema/RLS/secrets, deployment, or real-payment operations. Preserve V1 text above.


## V3 — CANONICAL DOCUMENT REFERENCES
Status: Implemented
Based on: V2

This document retains its specific purpose and historical V1/V2 content. Reusable coding workflow, approval gates, version/status semantics, and general change control are owned by [coding-prompt-system/MASTER_PROMPT.md](MASTER_PROMPT.md). Asri Collection Storefront/Admin requirements and frontend-only scope are owned by [masterprompt.md](../masterprompt.md). Keep this document focused on its named function; refer to those sources instead of copying their full rules.
