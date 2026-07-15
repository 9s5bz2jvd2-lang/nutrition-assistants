#!/usr/bin/env python3
"""Static contract checks for the isolated Mode C v3 candidate.

These checks verify documentation/fixture invariants only; they do not validate
clinical efficacy, legal compliance, actual web search quality, or LLM behavior.
"""
from pathlib import Path
import json
import sys

SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL
REF = SKILL / "reference"

checks = []

def need(path: Path, needle: str, label: str):
    text = path.read_text(encoding="utf-8")
    ok = needle in text
    checks.append((label, ok, f"{path.relative_to(ROOT)} contains {needle!r}"))

def absent(path: Path, needle: str, label: str):
    text = path.read_text(encoding="utf-8")
    ok = needle not in text
    checks.append((label, ok, f"{path.relative_to(ROOT)} omits obsolete {needle!r}"))

need(SKILL / "SKILL.md", "draft_generated=true", "root draft invariant")
need(SKILL / "SKILL.md", "T4 法规", "root four-track taxonomy")
need(SKILL / "SKILL.md", "机制、已知不良反应、潜在相互作用", "root safety sidecar")
need(SKILL / "SKILL.md", "mode_c_two_column_output_template.md", "root two-column template link")
need(REF / "mode_c_automatic_contract.md", "DRAFT_CREATED", "state machine")
need(REF / "mode_c_automatic_contract.md", "HUMAN_FINALIZATION_REQUIRED", "human finalization boundary")
need(REF / "formula_full_scan_contract.md", "Track 4: Regulatory Evidence", "formula T4 regulatory")
need(REF / "formula_full_scan_contract.md", "BLOCKED_IDENTITY", "formula retained blocked identity")
absent(REF / "formula_full_scan_contract.md", "abort formula generation", "formula no abort draft")
need(REF / "layer8_evidence_query.md", "Track 4: Regulatory Evidence", "layer8 T4 regulatory")
need(REF / "layer8_evidence_query.md", "Reminder/Safety Sidecar", "layer8 safety outside track")
need(REF / "layer8_evidence_query.md", "outcome=blocked", "layer8 blocked ledger")
need(REF / "formula_context_identity_gate.md", "Mode C v3 precedence", "identity override")
need(REF / "regulatory_gate.md", "Mode C v3 precedence", "regulatory override")
need(REF / "risk_triage_contract.md", "Mode C v3 precedence", "triage precedence")
need(SKILL / "templates" / "mode_c_two_column_output_template.md", "Individualized plan draft", "two-column plan")
need(SKILL / "templates" / "mode_c_two_column_output_template.md", "Reminders and human-review list", "two-column reminders")

fixture_path = SKILL / "tests" / "mode_c_anonymous_regression_case.json"
try:
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    inv = fixture["required_invariants"]
    ok = (inv["draft_generated"] is True and inv["two_column_output"] is True and
          inv["tracks"] == ["T1_human", "T2_animal", "T3_tcm_material", "T4_regulatory"] and
          inv["mechanism_is_not_efficacy_proof"] is True and
          inv["unknowns_do_not_suppress_draft"] is True and
          inv["human_finalization_required"] is True)
    checks.append(("anonymous regression fixture", ok, "fixture carries exact v3 invariants"))
except Exception as exc:
    checks.append(("anonymous regression fixture", False, repr(exc)))

for label, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'} | {label} | {detail}")
failed = [x for x in checks if not x[1]]
print(f"SUMMARY | {len(checks)-len(failed)} passed | {len(failed)} failed")
sys.exit(1 if failed else 0)
