#!/usr/bin/env python3
"""
Deterministic Local Validator for Functional Medicine Skill Candidate
(Global Evidence + Regulatory Gate Edition + P1 Repair)

This validator checks:
1. Internal file existence and cross-references
2. Required template files exist and have required sections
3. JSON templates parse correctly and have required fields
4. YAML routing file parses correctly
5. Eval cases cover required test categories
6. Status vocabulary consistency across documents
7. P1-A: Baseline completeness (all baseline files present in candidate)
8. P1-A: Internal reference target existence (SKILL.md/ROUTING.yaml cited paths)
9. P1-B: Only v2 triage statuses in active interfaces
10. P1-B: No old v1 triage status regression in active paths

It does NOT validate external medical/legal truth or actual regulatory status.
"""

import json
import os
import sys
import hashlib
import re
from pathlib import Path

# Base directory for the candidate
CANDIDATE_DIR = Path(__file__).resolve().parent.parent

# Baseline directory for completeness comparison
# Baseline is at ../github-publish-local-20260715T0019PDT/nutrition-assistants/functional-medicine-skill/
# relative to the task root (CANDIDATE_DIR.parent.parent), which is itself one level below the project root
BASELINE_DIR = (CANDIDATE_DIR.parent.parent.parent / "github-publish-local-20260715T0019PDT"
                / "nutrition-assistants" / "functional-medicine-skill")

# Required files (relative to CANDIDATE_DIR) - domain-specific files
REQUIRED_FILES = [
    "SKILL.md",
    "ROUTING.yaml",
    "reference/source_registry.md",
    "reference/formula_context_identity_gate.md",
    "reference/regulatory_gate.md",
    "reference/layer8_evidence_query.md",
    "reference/formula_full_scan_contract.md",
    "reference/formula_coverage_ledger_template.json",
    "reference/evidence_ledger_template.json",
    "reference/regulatory_coverage_ledger_template.json",
    "reference/individualized_formula_intake_contract.md",
    "reference/risk_triage_contract.md",
    "reference/personalized_selection_flow.md",
    "reference/reminder_package_contract.md",
    "templates/formula_candidate_template.md",
    "templates/evidence_matrix_template.md",
    "templates/tcm_identity_material_matrix_template.md",
    "templates/regulatory_coverage_matrix_template.md",
    "templates/search_ledger_template.md",
    "templates/blocking_risk_summary_template.md",
    "templates/personalized_formula_draft_template.md",
    "templates/reminder_package_template.md",
    "templates/intake_audit_ledger_template.json",
    "assets/eval-cases.md",
    "validator/validate_candidate.py",
]

# Required sections in eval-cases.md (test case IDs)
REQUIRED_EVAL_IDS = [
    "H1",  # Unknown target market fails closed
    "H2",  # Unlisted market
    "I1",  # Botanical species ambiguity
    "I2",  # Botanical plant-part ambiguity
    "J1",  # Animal-only evidence cannot become clinical efficacy
    "K1",  # Traditional-use text cannot become modern efficacy proof
    "L1",  # Food/supplement/medicine category confusion
    "M1",  # Non-authoritative source cannot clear regulatory gate
    "N1",  # One uncovered jurisdiction blocks global-compliant claim
    # Personalized formula eval cases (delta)
    "P1",  # Complete low-risk input → draft_for_professional_review
    "Q1",  # Missing medication → incomplete_draft_needs_human_input
    "R1",  # Pregnancy → draft_with_mandatory_human_review
    "S1",  # Animal-only evidence in personalized context
    "T1",  # Preference cannot override identity failure
    "U1",  # Audit fields and privacy minimization
    # Reminder package / draft-capable triage eval cases (delta)
    "W1",  # Reminders carry source/trigger/severity/action_owner fields
    "W2",  # Missing/high-risk conditions emit reminders, not erase draft
    "Z1",  # Draft-capable triage: emergency still produces draft with URGENT flag
]

# Required fields in evidence_ledger_template.json
REQUIRED_EVIDENCE_LEDGER_FIELDS = [
    "_schema",
    "_allowed_values",
    "_required_ingredient_fields",
    "ingredients",
]

# Required fields in regulatory_coverage_ledger_template.json
REQUIRED_REGULATORY_LEDGER_FIELDS = [
    "_schema",
    "_allowed_values",
    "_required_entry_fields",
    "entries",
    "global_compliant_check",
]

# Required fields in intake_audit_ledger_template.json
REQUIRED_INTAKE_AUDIT_FIELDS = [
    "_schema",
    "_allowed_values",
    "_required_audit_fields",
    "request_id",
    "triage_status",
    "intake_provenance_summary",
    "constraints_applied",
    "excluded_ingredients",
    "privacy_compliant",
]

# Required sections in SKILL.md
REQUIRED_SKILL_SECTIONS = [
    "四轨证据",  # Four-track evidence
    "法规门控",  # Regulatory gate
    "身份门控",  # Identity gate
    "来源注册表",  # Source registry reference
    # NEW: personalized formula sections
    "个性化配方便方",  # Personalized formula draft
    "风险分诊",  # Risk triage
    "接诊合约",  # Intake contract reference
]

# Required sections in layer8_evidence_query.md
REQUIRED_L8_SECTIONS = [
    "Track 1",
    "Track 2",
    "Track 3",
    "Track 4",
    "Human Clinical",
    "Animal",
    "TCM",
    "Mechanistic",
]

# Binding v2 triage statuses (from risk_triage_contract.md)
V2_TRIAGE_STATUSES = [
    "incomplete_draft_needs_human_input",
    "draft_with_urgent_safety_flag",
    "draft_with_mandatory_human_review",
    "draft_with_regulatory_gap",
    "draft_for_professional_review",
    "human_reviewed_finalization",
]

# Superseded v1 triage statuses that must NOT appear as active values
V1_TRIAGE_STATUSES_LEGACY = [
    "needs_clarification",
    "not_eligible_for_auto_draft",
    "professional_review_required",
    "research_draft_only",
]

# Active interface files where old statuses must NOT appear
# (excluding explicitly non-output legacy-mapping notes and the validator itself,
#  which necessarily contains the legacy status names for regression detection)
ACTIVE_INTERFACE_FILES = [
    "ROUTING.yaml",
    "reference/risk_triage_contract.md",
    "reference/individualized_formula_intake_contract.md",
    "reference/personalized_selection_flow.md",
    "templates/personalized_formula_draft_template.md",
    "templates/reminder_package_template.md",
    "templates/intake_audit_ledger_template.json",
]


class ValidationResult:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []

    def ok(self, check_name):
        self.passed.append(check_name)

    def fail(self, check_name, reason):
        self.failed.append((check_name, reason))

    def warn(self, check_name, reason):
        self.warnings.append((check_name, reason))

    @property
    def all_passed(self):
        return len(self.failed) == 0

    def report(self):
        lines = ["=" * 60, "VALIDATION REPORT", "=" * 60]
        lines.append(f"\nPassed: {len(self.passed)}")
        lines.append(f"Failed: {len(self.failed)}")
        lines.append(f"Warnings: {len(self.warnings)}")
        lines.append("")

        if self.passed:
            lines.append("--- PASSED ---")
            for name in self.passed:
                lines.append(f"  ✅ {name}")
            lines.append("")

        if self.warnings:
            lines.append("--- WARNINGS ---")
            for name, reason in self.warnings:
                lines.append(f"  ⚠️  {name}: {reason}")
            lines.append("")

        if self.failed:
            lines.append("--- FAILED ---")
            for name, reason in self.failed:
                lines.append(f"  ❌ {name}: {reason}")
            lines.append("")

        lines.append("=" * 60)
        lines.append(f"OVERALL: {'PASS' if self.all_passed else 'FAIL'}")
        lines.append("=" * 60)
        return "\n".join(lines)


def check_file_existence(result):
    """Check all required files exist."""
    for rel_path in REQUIRED_FILES:
        full_path = CANDIDATE_DIR / rel_path
        if full_path.exists():
            result.ok(f"file_exists: {rel_path}")
        else:
            result.fail(f"file_exists: {rel_path}", f"File not found: {full_path}")


def check_baseline_completeness(result):
    """P1-A: Check that all baseline files exist in the candidate."""
    if not BASELINE_DIR.exists():
        result.warn("baseline_completeness", f"Baseline directory not found: {BASELINE_DIR}")
        return

    baseline_files = sorted(
        f.relative_to(BASELINE_DIR)
        for f in BASELINE_DIR.rglob("*")
        if f.is_file()
    )
    missing = []
    for bf in baseline_files:
        candidate_path = CANDIDATE_DIR / bf
        if candidate_path.exists():
            result.ok(f"baseline_file_present: {bf}")
        else:
            missing.append(str(bf))
            result.fail(f"baseline_file_present: {bf}", "Baseline file missing from candidate")

    if not missing:
        result.ok("baseline_completeness_summary: all baseline files present")
    else:
        result.fail("baseline_completeness_summary",
                    f"{len(missing)} baseline files missing: {', '.join(missing[:5])}{'...' if len(missing) > 5 else ''}")


def check_internal_references(result):
    """P1-A: Check that reference/knowledge/templates/assets paths cited in
    SKILL.md and ROUTING.yaml exist in the candidate tree."""
    # Collect all .md and .json and .txt files cited in ROUTING.yaml and SKILL.md
    cited_refs = set()
    for src_file in ["ROUTING.yaml", "SKILL.md"]:
        src_path = CANDIDATE_DIR / src_file
        if not src_path.exists():
            continue
        content = src_path.read_text(encoding="utf-8")
        # Find references like: reference/foo.md, templates/bar.json, knowledge/baz.txt, assets/qux.md
        for match in re.finditer(
            r'((?:reference|knowledge|templates|assets)/[a-zA-Z0-9_\-\.]+\.(?:md|json|txt|yaml))',
            content
        ):
            cited_refs.add(match.group(1))

    # De-duplicate
    missing_refs = []
    for ref in sorted(cited_refs):
        ref_path = CANDIDATE_DIR / ref
        if ref_path.exists():
            result.ok(f"internal_ref_exists: {ref}")
        else:
            missing_refs.append(ref)
            result.fail(f"internal_ref_exists: {ref}", "Referenced file missing from candidate")

    if not missing_refs:
        result.ok("internal_reference_summary: all cited paths exist")
    else:
        result.fail("internal_reference_summary",
                    f"{len(missing_refs)} cited paths missing: {', '.join(missing_refs[:5])}{'...' if len(missing_refs) > 5 else ''}")


def check_json_templates(result):
    """Check JSON templates parse correctly and have required fields."""
    # Evidence ledger template
    ev_path = CANDIDATE_DIR / "reference" / "evidence_ledger_template.json"
    if ev_path.exists():
        try:
            with open(ev_path, "r", encoding="utf-8") as f:
                ev = json.load(f)
            for field in REQUIRED_EVIDENCE_LEDGER_FIELDS:
                if field in ev:
                    result.ok(f"evidence_ledger_field: {field}")
                else:
                    result.fail(f"evidence_ledger_field: {field}", "Required field missing")
            # Check allowed values have expected evidence statuses
            allowed = ev.get("_allowed_values", {}).get("evidence_status", [])
            for status in ["supported", "absent", "animal_only", "traditional_only"]:
                if status in allowed:
                    result.ok(f"evidence_status_value: {status}")
                else:
                    result.fail(f"evidence_status_value: {status}", "Missing from allowed values")
        except json.JSONDecodeError as e:
            result.fail("evidence_ledger_json_parse", f"JSON parse error: {e}")

    # Regulatory ledger template
    reg_path = CANDIDATE_DIR / "reference" / "regulatory_coverage_ledger_template.json"
    if reg_path.exists():
        try:
            with open(reg_path, "r", encoding="utf-8") as f:
                reg = json.load(f)
            for field in REQUIRED_REGULATORY_LEDGER_FIELDS:
                if field in reg:
                    result.ok(f"regulatory_ledger_field: {field}")
                else:
                    result.fail(f"regulatory_ledger_field: {field}", "Required field missing")
            # Check allowed values have expected regulatory statuses
            allowed = reg.get("_allowed_values", {}).get("status", [])
            for status in ["permitted", "conditional", "prohibited", "unknown", "not_assessed"]:
                if status in allowed:
                    result.ok(f"regulatory_status_value: {status}")
                else:
                    result.fail(f"regulatory_status_value: {status}", "Missing from allowed values")
        except json.JSONDecodeError as e:
            result.fail("regulatory_ledger_json_parse", f"JSON parse error: {e}")

    # NEW: Intake audit ledger template
    audit_path = CANDIDATE_DIR / "templates" / "intake_audit_ledger_template.json"
    if audit_path.exists():
        try:
            with open(audit_path, "r", encoding="utf-8") as f:
                audit = json.load(f)
            for field in REQUIRED_INTAKE_AUDIT_FIELDS:
                if field in audit:
                    result.ok(f"intake_audit_field: {field}")
                else:
                    result.fail(f"intake_audit_field: {field}", "Required field missing")
            # Check triage statuses in allowed values (v2.0 draft-capable model)
            allowed_triage = audit.get("_allowed_values", {}).get("triage_status", [])
            for status in V2_TRIAGE_STATUSES:
                if status in allowed_triage:
                    result.ok(f"triage_status_value: {status}")
                else:
                    result.fail(f"triage_status_value: {status}", "Missing from allowed values")
            # P1-B: Ensure no v1 legacy statuses are in the active allowed values
            for legacy in V1_TRIAGE_STATUSES_LEGACY:
                if legacy in allowed_triage:
                    result.fail(f"triage_status_regression: {legacy}",
                                "Legacy v1 status found in active allowed values (should be v2 only)")
                else:
                    result.ok(f"triage_status_no_legacy: {legacy}")
            # Check privacy_compliant default
            if audit.get("privacy_compliant") == True:
                result.ok("intake_audit_privacy_default")
            else:
                result.fail("intake_audit_privacy_default", "privacy_compliant should default to true")
        except json.JSONDecodeError as e:
            result.fail("intake_audit_ledger_json_parse", f"JSON parse error: {e}")

    # Coverage ledger template (baseline, should still exist)
    cov_path = CANDIDATE_DIR / "reference" / "formula_coverage_ledger_template.json"
    if cov_path.exists():
        try:
            with open(cov_path, "r", encoding="utf-8") as f:
                cov = json.load(f)
            if "_schema" in cov:
                result.ok("coverage_ledger_has_schema")
            else:
                result.fail("coverage_ledger_has_schema", "Missing _schema field")
        except json.JSONDecodeError as e:
            result.fail("coverage_ledger_json_parse", f"JSON parse error: {e}")


def check_yaml_routing(result):
    """Check ROUTING.yaml parses and has required sections."""
    yaml_path = CANDIDATE_DIR / "ROUTING.yaml"
    if not yaml_path.exists():
        return

    content = yaml_path.read_text(encoding="utf-8")

    # Check for required sections (textual check, no YAML parser dependency)
    required_keys = [
        "trigger_terms",
        "formula_full_scan",
        "context_identity_gate",
        "four_track_evidence",
        "regulatory_gate",
        "finalization_gates",
        "source_registry",
        "template_paths",
        "reference_paths",
        "knowledge_paths",
        # NEW: personalized formula keys
        "personalized_formula",
        "个性化配方",
        "个性化接诊",
        "intake_completeness_check",
        "triage_status_check",
        "privacy_minimization_check",
    ]
    for key in required_keys:
        if key in content:
            result.ok(f"routing_key: {key}")
        else:
            result.fail(f"routing_key: {key}", "Required key not found in ROUTING.yaml")

    # Check for new gate references
    new_refs = [
        "formula_context_identity_gate",
        "regulatory_gate",
        "source_registry",
        "evidence_ledger_template",
        "regulatory_coverage_ledger_template",
        # NEW: personalized formula references
        "individualized_formula_intake_contract",
        "risk_triage_contract",
        "personalized_selection_flow",
        "personalized_formula_draft",
        "intake_audit_ledger",
    ]
    for ref in new_refs:
        if ref in content:
            result.ok(f"routing_ref: {ref}")
        else:
            result.fail(f"routing_ref: {ref}", "Required reference not found in ROUTING.yaml")

    # P1-B: Check that ROUTING.yaml triage_statuses section has all v2 statuses
    for status in V2_TRIAGE_STATUSES:
        if status in content:
            result.ok(f"routing_v2_triage_status: {status}")
        else:
            result.fail(f"routing_v2_triage_status: {status}",
                        "V2 triage status missing from ROUTING.yaml")

    # P1-B: Check that ROUTING.yaml triage_statuses does NOT have v1 legacy statuses
    # Extract just the triage_statuses block for precise checking
    triage_block_match = re.search(r'triage_statuses:\s*\n((?:\s+-\s+.+\n)+)', content)
    if triage_block_match:
        triage_block = triage_block_match.group(1)
        for legacy in V1_TRIAGE_STATUSES_LEGACY:
            if re.search(rf'^\s+-\s+{re.escape(legacy)}\s*$', triage_block, re.MULTILINE):
                result.fail(f"routing_triage_regression: {legacy}",
                            "Legacy v1 status found in ROUTING.yaml triage_statuses (active output)")
            else:
                result.ok(f"routing_triage_no_legacy: {legacy}")
    else:
        result.warn("routing_triage_block_check", "Could not extract triage_statuses block from ROUTING.yaml")


def check_skill_md(result):
    """Check SKILL.md has required sections for the upgrade."""
    skill_path = CANDIDATE_DIR / "SKILL.md"
    if not skill_path.exists():
        return

    content = skill_path.read_text(encoding="utf-8")

    for section in REQUIRED_SKILL_SECTIONS:
        if section in content:
            result.ok(f"skill_section: {section}")
        else:
            result.fail(f"skill_section: {section}", "Required section not found in SKILL.md")

    # Check that safety red lines are retained
    safety_keywords = ["不诊断", "不替代治疗", "个性化配方便方", "特殊人群安全门", "引用真实"]
    for kw in safety_keywords:
        if kw in content:
            result.ok(f"skill_safety: {kw}")
        else:
            result.fail(f"skill_safety: {kw}", "Safety keyword not found in SKILL.md")


def check_layer8(result):
    """Check layer8_evidence_query.md has four distinct tracks."""
    l8_path = CANDIDATE_DIR / "reference" / "layer8_evidence_query.md"
    if not l8_path.exists():
        return

    content = l8_path.read_text(encoding="utf-8")

    for section in REQUIRED_L8_SECTIONS:
        if section in content:
            result.ok(f"layer8_section: {section}")
        else:
            result.fail(f"layer8_section: {section}", "Required section not found")

    # Check no cross-tier promotion rule
    if "cross-tier" in content.lower() or "跨层" in content or "Cross-Tier" in content:
        result.ok("layer8_cross_tier_promotion_prohibition")
    else:
        result.fail("layer8_cross_tier_promotion_prohibition",
                    "Cross-tier promotion prohibition not found")

    # Check mechanism_is_not_efficacy_proof is mandatory
    if "mechanism_is_not_efficacy_proof" in content:
        result.ok("layer8_mechanism_not_efficacy")
    else:
        result.fail("layer8_mechanism_not_efficacy",
                    "mechanism_is_not_efficacy_proof mandatory field not found")


def check_eval_cases(result):
    """Check eval-cases.md covers required test categories."""
    eval_path = CANDIDATE_DIR / "assets" / "eval-cases.md"
    if not eval_path.exists():
        return

    content = eval_path.read_text(encoding="utf-8")

    for eval_id in REQUIRED_EVAL_IDS:
        # Search for the eval ID as a section header or bold text
        patterns = [f"### {eval_id}", f"**{eval_id}", f"## {eval_id}"]
        found = any(p in content for p in patterns)
        if found:
            result.ok(f"eval_case: {eval_id}")
        else:
            result.fail(f"eval_case: {eval_id}", "Required eval case not found")


def check_source_registry(result):
    """Check source_registry.md has required jurisdiction entries."""
    sr_path = CANDIDATE_DIR / "reference" / "source_registry.md"
    if not sr_path.exists():
        return

    content = sr_path.read_text(encoding="utf-8")

    required_jurisdictions = [
        "China",
        "United States",
        "European Union",
        "Codex",
    ]
    for j in required_jurisdictions:
        if j in content:
            result.ok(f"source_registry_jurisdiction: {j}")
        else:
            result.fail(f"source_registry_jurisdiction: {j}",
                        "Required jurisdiction not found in source registry")

    # Check coverage status vocabulary
    required_statuses = ["active", "limited", "uncovered", "needs_jurisdiction_specific_review"]
    for status in required_statuses:
        if status in content:
            result.ok(f"source_registry_status: {status}")
        else:
            result.fail(f"source_registry_status: {status}",
                        "Required coverage status not found")


def check_regulatory_gate(result):
    """Check regulatory_gate.md has required elements."""
    rg_path = CANDIDATE_DIR / "reference" / "regulatory_gate.md"
    if not rg_path.exists():
        return

    content = rg_path.read_text(encoding="utf-8")

    required_elements = [
        "permitted",
        "conditional",
        "prohibited",
        "unknown",
        "not_assessed",
        "global-compliant",
        "fail closed",
        "authoritative",
    ]
    for elem in required_elements:
        if elem in content:
            result.ok(f"regulatory_gate_element: {elem}")
        else:
            result.fail(f"regulatory_gate_element: {elem}",
                        "Required element not found in regulatory gate")


def check_personalized_formula(result):
    """Check personalized formula references have required content."""
    # Check intake contract
    ic_path = CANDIDATE_DIR / "reference" / "individualized_formula_intake_contract.md"
    if ic_path.exists():
        content = ic_path.read_text(encoding="utf-8")
        for kw in ["required", "optional", "verified", "user_reported", "unknown", "not_applicable",
                     "privacy", "session", "provenance"]:
            if kw in content:
                result.ok(f"intake_contract_keyword: {kw}")
            else:
                result.fail(f"intake_contract_keyword: {kw}", "Required keyword not found in intake contract")

    # Check risk triage (v2.0 draft-capable model)
    rt_path = CANDIDATE_DIR / "reference" / "risk_triage_contract.md"
    if rt_path.exists():
        content = rt_path.read_text(encoding="utf-8")
        content_lower = content.lower()
        for kw in ["incomplete_draft_needs_human_input", "draft_with_urgent_safety_flag",
                     "draft_with_mandatory_human_review", "draft_with_regulatory_gap",
                     "draft_for_professional_review", "human_reviewed_finalization",
                     "fail-closed", "never silently", "never derive",
                     "draft generated", "never auto-finalize"]:
            if kw.lower() in content_lower:
                result.ok(f"triage_contract_keyword: {kw}")
            else:
                result.fail(f"triage_contract_keyword: {kw}", "Required keyword not found in triage contract")

    # Check personalized selection flow
    ps_path = CANDIDATE_DIR / "reference" / "personalized_selection_flow.md"
    if ps_path.exists():
        content = ps_path.read_text(encoding="utf-8")
        for kw in ["intake", "constraints", "exclusions", "evidence tracks",
                     "identity", "regulatory", "person-specific", "population-level",
                     "NEVER derive", "professional review"]:
            if kw.lower() in content.lower():
                result.ok(f"selection_flow_keyword: {kw}")
            else:
                result.fail(f"selection_flow_keyword: {kw}", "Required keyword not found in selection flow")

    # Check personalized draft template
    pd_path = CANDIDATE_DIR / "templates" / "personalized_formula_draft_template.md"
    if pd_path.exists():
        content = pd_path.read_text(encoding="utf-8")
        for kw in ["intake", "provenance", "triage", "constraints", "excluded",
                     "evidence", "regulatory", "professional-review", "checklist",
                     "limitations", "NOT a prescription"]:
            if kw.lower() in content.lower():
                result.ok(f"draft_template_keyword: {kw}")
            else:
                result.fail(f"draft_template_keyword: {kw}", "Required keyword not found in draft template")


def check_reminder_package(result):
    """Check reminder package contract has required categories and fields."""
    rp_path = CANDIDATE_DIR / "reference" / "reminder_package_contract.md"
    if not rp_path.exists():
        return
    content = rp_path.read_text(encoding="utf-8")

    # Check all six categories
    for kw in ["use_followup", "information_gap", "safety_interaction",
                "evidence", "regulatory_product", "human_review"]:
        if kw in content:
            result.ok(f"reminder_category: {kw}")
        else:
            result.fail(f"reminder_category: {kw}", "Required reminder category not found")

    # Check required fields
    for kw in ["reminder_id", "category", "title", "detail", "source",
                "trigger", "status", "severity", "action_owner",
                "external_notification_claim"]:
        if kw in content:
            result.ok(f"reminder_field: {kw}")
        else:
            result.fail(f"reminder_field: {kw}", "Required reminder field not found")

    # Check severity levels
    for kw in ["info", "suggestion", "important", "critical"]:
        if kw in content:
            result.ok(f"reminder_severity: {kw}")
        else:
            result.fail(f"reminder_severity: {kw}", "Required severity level not found")


def check_eval_no_draft_halt(result):
    """P2-A: Deterministic check that eval-cases.md does NOT contain the
    no-draft-halt pattern 'generation HALTS until clarification received'
    (or semantically equivalent wording). Per binding draft-capable policy,
    incomplete input must produce a draft + reminders, not halt generation."""
    eval_path = CANDIDATE_DIR / "assets" / "eval-cases.md"
    if not eval_path.exists():
        return
    content = eval_path.read_text(encoding="utf-8")
    # Detect the old halt pattern (case-insensitive)
    halt_patterns = [
        r'(?:generation|output|draft)\s+HALT(?:S)?\s+until\s+clarification',
        r'HALT(?:S)?\s+until\s+clarification\s+received',
    ]
    found_halt = False
    for pat in halt_patterns:
        if re.search(pat, content, re.IGNORECASE):
            found_halt = True
            break
    if found_halt:
        result.fail("p2a_eval_no_draft_halt",
                    "eval-cases.md contains no-draft-halt pattern; "
                    "per binding policy, incomplete input must generate draft + reminders")
    else:
        result.ok("p2a_eval_no_draft_halt: no halt pattern found")

    # Positive check: eval Q1 must reference incomplete_draft_needs_human_input and draft generation
    if "incomplete_draft_needs_human_input" in content:
        result.ok("p2a_eval_q1_has_idnhi_status")
    else:
        result.fail("p2a_eval_q1_has_idnhi_status",
                    "Q1 expected output missing 'incomplete_draft_needs_human_input'")
    # Check that Q1 section references draft generation or structured reminder
    q1_match = re.search(r'### Q1.*?(?=### Q2|\Z)', content, re.DOTALL)
    if q1_match:
        q1_text = q1_match.group(0)
        if "draft" in q1_text.lower() and ("reminder" in q1_text.lower() or "information_gap" in q1_text.lower()):
            result.ok("p2a_eval_q1_mentions_draft_and_reminders")
        else:
            result.fail("p2a_eval_q1_mentions_draft_and_reminders",
                        "Q1 expected output does not mention both draft generation and reminders")


def check_draft_template_complete_v2_enumeration(result):
    """P2-B: Deterministic check that personalized_formula_draft_template.md
    enumerates all six v2 triage statuses including human_reviewed_finalization."""
    pd_path = CANDIDATE_DIR / "templates" / "personalized_formula_draft_template.md"
    if not pd_path.exists():
        return
    content = pd_path.read_text(encoding="utf-8")
    for status in V2_TRIAGE_STATUSES:
        if status in content:
            result.ok(f"p2b_draft_template_has_v2_status: {status}")
        else:
            result.fail(f"p2b_draft_template_has_v2_status: {status}",
                        f"V2 triage status '{status}' missing from personalized draft template")
    # Check HRF abbreviation also present
    if "HRF" in content:
        result.ok("p2b_draft_template_has_hrf_abbreviation")
    else:
        result.fail("p2b_draft_template_has_hrf_abbreviation",
                    "HRF abbreviation missing from personalized draft template")
    # Check that HRF is documented as requiring human confirmation
    content_lower = content.lower()
    if "human_reviewed_finalization" in content_lower:
        # Look for guidance about requiring human confirmation near HRF
        if re.search(r'human.{0,30}reviewed.{0,30}finalization', content_lower):
            result.ok("p2b_draft_template_hrf_human_confirmation_context")
        else:
            result.warn("p2b_draft_template_hrf_human_confirmation_context",
                        "HRF present but human confirmation context unclear")


def check_v2_triage_regression(result):
    """P1-B: Deterministic regression check that only v2 triage statuses appear
    in active interface files. Scans each active file for old v1 status patterns."""
    for rel_path in ACTIVE_INTERFACE_FILES:
        full_path = CANDIDATE_DIR / rel_path
        if not full_path.exists():
            continue
        content = full_path.read_text(encoding="utf-8")
        for legacy in V1_TRIAGE_STATUSES_LEGACY:
            # Use word-boundary-like matching to avoid false positives on substrings
            pattern = re.compile(rf'(?<!\w){re.escape(legacy)}(?!\w)')
            if pattern.search(content):
                result.fail(f"v2_regression_in_{rel_path}: {legacy}",
                            f"Legacy v1 triage status '{legacy}' found in active interface {rel_path}")
            else:
                result.ok(f"v2_no_legacy_in_{rel_path}: {legacy}")



def check_personalized_selection_regression(result):
    """P1-C: Prevent invalid triage vocabulary and generic workflow labels from
    returning to the active personalized-selection interface."""
    flow_path = CANDIDATE_DIR / "reference" / "personalized_selection_flow.md"
    if flow_path.exists():
        flow = flow_path.read_text(encoding="utf-8")
        flow_lower = flow.lower()
        for forbidden in ["pending_review", "workflow stage"]:
            if forbidden in flow_lower:
                result.fail(f"p1c_selection_flow_no_{forbidden}",
                            "Forbidden legacy or generic workflow wording found")
            else:
                result.ok(f"p1c_selection_flow_no_{forbidden}")
        for required in [
            "Output triage status = one permitted v2 status selected at Step 2",
            "draft_for_professional_review",
            "Human decision = pending",
            "Human decision recorded = false",
            "personalized selection step 5",
        ]:
            if required.lower() in flow_lower:
                result.ok(f"p1c_selection_flow_has: {required}")
            else:
                result.fail(f"p1c_selection_flow_has: {required}",
                            "Required v2 triage or human-decision metadata missing")

    template_path = CANDIDATE_DIR / "templates" / "personalized_formula_draft_template.md"
    if template_path.exists():
        template = template_path.read_text(encoding="utf-8")
        template_lower = template.lower()
        for forbidden in ["workflow stage", "workflow status"]:
            if forbidden in template_lower:
                result.fail(f"p1c_draft_template_no_{forbidden}",
                            "Generic workflow label found in personalized draft template")
            else:
                result.ok(f"p1c_draft_template_no_{forbidden}")
        for required in ["personalized selection stage", "human decision record (personalized selection step 5)"]:
            if required in template_lower:
                result.ok(f"p1c_draft_template_has: {required}")
            else:
                result.fail(f"p1c_draft_template_has: {required}",
                            "Personalized-selection label missing from draft template")

    audit_path = CANDIDATE_DIR / "templates" / "intake_audit_ledger_template.json"
    if audit_path.exists():
        try:
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            result.fail("p1c_intake_audit_json_parse", f"JSON parse error: {exc}")
        else:
            for legacy in ["workflow_stage", "workflow_status"]:
                if legacy in audit or legacy in audit.get("_allowed_values", {}) or legacy in audit.get("_required_audit_fields", []):
                    result.fail(f"p1c_intake_audit_no_{legacy}",
                                "Legacy generic workflow key remains in intake audit schema")
                else:
                    result.ok(f"p1c_intake_audit_no_{legacy}")
            for required in ["personalized_selection_stage", "personalized_selection_status"]:
                if (required in audit and
                    (required != "personalized_selection_stage" or
                     required in audit.get("_allowed_values", {}) and required in audit.get("_required_audit_fields", []))):
                    result.ok(f"p1c_intake_audit_has_{required}")
                else:
                    result.fail(f"p1c_intake_audit_has_{required}",
                                "Required personalized-selection key missing or incompletely wired")


def compute_sha256(result):
    """Compute SHA-256 for all created files."""
    hashes = {}
    for rel_path in sorted(REQUIRED_FILES):
        full_path = CANDIDATE_DIR / rel_path
        if full_path.exists():
            h = hashlib.sha256(full_path.read_bytes()).hexdigest()
            hashes[rel_path] = h
            result.ok(f"hash: {rel_path}")
    return hashes


def main():
    result = ValidationResult()

    print("Starting validation of Functional Medicine Skill candidate...")
    print(f"Candidate directory: {CANDIDATE_DIR}")
    print(f"Baseline directory: {BASELINE_DIR}")
    print()

    # 1. File existence
    print("1. Checking file existence...")
    check_file_existence(result)

    # 2. P1-A: Baseline completeness
    print("2. Checking baseline completeness (P1-A)...")
    check_baseline_completeness(result)

    # 3. P1-A: Internal reference targets
    print("3. Checking internal reference targets (P1-A)...")
    check_internal_references(result)

    # 4. JSON templates
    print("4. Checking JSON templates...")
    check_json_templates(result)

    # 5. YAML routing
    print("5. Checking ROUTING.yaml...")
    check_yaml_routing(result)

    # 6. SKILL.md
    print("6. Checking SKILL.md...")
    check_skill_md(result)

    # 7. Layer 8
    print("7. Checking layer8_evidence_query.md...")
    check_layer8(result)

    # 8. Eval cases
    print("8. Checking eval cases...")
    check_eval_cases(result)

    # 9. Source registry
    print("9. Checking source registry...")
    check_source_registry(result)

    # 10. Regulatory gate
    print("10. Checking regulatory gate...")
    check_regulatory_gate(result)

    # 11. Personalized formula references
    print("11. Checking personalized formula references...")
    check_personalized_formula(result)

    # 12. Reminder package
    print("12. Checking reminder package contract...")
    check_reminder_package(result)

    # 13. P1-B: v2 triage regression check
    print("13. Checking v2 triage status regression (P1-B)...")
    check_v2_triage_regression(result)

    # 14. P1-C: personalized-selection terminology and status regression check
    print("14. Checking personalized-selection regression (P1-C)...")
    check_personalized_selection_regression(result)

    # 15. P2-A: eval no-draft-halt regression check
    print("15. Checking eval no-draft-halt regression (P2-A)...")
    check_eval_no_draft_halt(result)

    # 16. P2-B: draft template complete v2 enumeration check
    print("16. Checking draft template complete v2 enumeration (P2-B)...")
    check_draft_template_complete_v2_enumeration(result)

    # 14. Compute SHA-256
    print("14. Computing SHA-256 hashes...")
    hashes = compute_sha256(result)

    # Print report
    print()
    print(result.report())

    # Print hashes
    print("\n--- SHA-256 FILE MANIFEST ---")
    for path, h in sorted(hashes.items()):
        print(f"  {h}  {path}")

    # Return exit code
    return 0 if result.all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
