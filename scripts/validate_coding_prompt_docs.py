#!/usr/bin/env python3
"""Validate Coding Prompt System documentation and cross-file traceability."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BASELINE = [
    "README.md",
    "coding-prompt-system/MASTER_PROMPT.md",
    "coding-prompt-system/INSTRUCTION.md",
    "coding-prompt-system/variables.yaml",
    "coding-prompt-system/REQUIREMENTS.md",
    "coding-prompt-system/ACCEPTANCE_CRITERIA.md",
    "coding-prompt-system/WORKFLOW.md",
    "coding-prompt-system/VERIFICATION.md",
    "coding-prompt-system/CHANGELOG.md",
    "coding-prompt-system/SOURCE_OF_TRUTH.md",
    "coding-prompt-system/IMPLEMENTATION_PLAN.md",
    "coding-prompt-system/AUDIT_REPORT.md",
    "coding-prompt-system/DECISIONS.md",
]
errors = []
contents = {}

def error(message):
    errors.append(message)

for rel in BASELINE:
    path = ROOT / rel
    if not path.is_file():
        error(f"missing required file: {rel}")
        continue
    try:
        contents[rel] = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        error(f"cannot read {rel}: {exc}")

for rel, content in contents.items():
    if not rel.endswith(".md"):
        continue
    for version in ("VERSION V1", "VERSION V2", "VERSION V3"):
        if version not in content:
            error(f"{rel}: missing {version} section")
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
        target = match.group(1).strip().split("#", 1)[0]
        if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
            continue
        resolved = ((ROOT / rel).parent / target).resolve()
        if not resolved.exists():
            error(f"{rel}: broken local link: {target}")

req_text = contents.get("coding-prompt-system/REQUIREMENTS.md", "")
ac_text = contents.get("coding-prompt-system/ACCEPTANCE_CRITERIA.md", "")
for n in range(9, 21):
    req_id, ac_id = f"REQ-{n:03d}", f"AC-{n:03d}"
    if req_id not in req_text:
        error(f"missing {req_id}")
    if ac_id not in req_text:
        error(f"{req_id} does not reference {ac_id}")
    if ac_id not in ac_text:
        error(f"missing {ac_id}")
    if req_id not in ac_text:
        error(f"{ac_id} does not reference {req_id}")

try:
    import yaml
    config = yaml.safe_load((ROOT / "coding-prompt-system/variables.yaml").read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        error("variables.yaml root must be a mapping")
    else:
        required = {"version_index", "active_version", "project", "technology", "task", "scope", "workflow", "verification"}
        missing = sorted(required - set(config))
        if missing:
            error("variables.yaml missing top-level keys: " + ", ".join(missing))
        allowed = {"Proposed", "Approved", "Implemented", "Verified", "Blocked", "Unverified", "Draft"}
        versions = config.get("version_index")
        if not isinstance(versions, list) or not versions:
            error("variables.yaml version_index must be a non-empty list")
        else:
            for item in versions:
                if not isinstance(item, dict) or item.get("status") not in allowed:
                    error("variables.yaml contains an invalid version status record")
except ImportError:
    error("PyYAML required; install with: python -m pip install PyYAML")
except (OSError, UnicodeError) as exc:
    error(f"cannot read variables.yaml: {exc}")
except Exception as exc:
    error(f"variables.yaml parse/validation error: {exc}")

workflow = ROOT / ".github/workflows/coding-prompt-docs.yml"
if not workflow.is_file():
    error("missing .github/workflows/coding-prompt-docs.yml")
else:
    text = workflow.read_text(encoding="utf-8")
    if "validate_coding_prompt_docs.py" not in text:
        error("CI workflow does not invoke the documentation validator")

if errors:
    print("FAIL: documentation validation found issues:")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)
print(f"PASS: {len(BASELINE)} baseline files, local Markdown links, version sections, REQ/AC traceability, YAML config, and CI invocation.")
