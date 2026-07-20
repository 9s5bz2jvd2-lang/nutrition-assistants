#!/usr/bin/env python3
"""
Validate the integrated functional-medicine evidence-workflow candidate package.

Usage:
    python3 validate_candidate.py <candidate_root>

Exit code 0 = all checks pass; exit code 1 = one or more failures.
"""

import os
import re
import sys
import json

# ──────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────

SKILL_MAX_LINES = 260
QUOTE_MAX_WORDS = 25
SOURCE_LEDGER_MAX_SOURCES = 20
CJK_PATTERN = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]")

REQUIRED_REFERENCE_FILES = [
    "reference/scope-and-red-lines.md",
    "reference/intake-and-triage.md",
    "reference/invocation-and-evidence-routing.md",
    "reference/evidence-and-uncertainty.md",
    "reference/evidence-governance.md",
    "reference/evidence-and-safety-debt.md",
    "reference/formula-evidence-contract.md",
    "reference/formula-class-gates.md",
    "reference/model-io-and-output-validation.md",
    "reference/functional-medicine-matrix-contract.md",
    "reference/six-eye-insight.md",
    "reference/six-eye-inquiry.md",
    "reference/output-contract.md",
    "reference/source-ledger.md",
    "reference/learned-knowledge-framework.md",
    "reference/system-relationships.md",
    "reference/private-study-provenance.md",
]

REQUIRED_ASSET_FILES = [
    "assets/structured-intake-template.md",
    "assets/evidence-card-template.md",
    "assets/review-output-template.md",
    "assets/general-education-question-template.md",
    "assets/hypothetical-case-template.md",
    "assets/evidence-exploration-template.md",
    "assets/individual-diagnostic-support-template.md",
    "assets/functional-medicine-matrix-state-template.json",
    "assets/release-status-template.json",
    "assets/food-lifestyle-plan-template.md",
    "assets/supplement-plan-template.md",
    "assets/medical-nutrition-template.md",
    "assets/tcm-formula-template.md",
]

REQUIRED_SCRIPTS = [
    "scripts/validate_candidate.py",
    "scripts/similarity_screen.py",
    "scripts/generate_functional_medicine_matrix.py",
    "scripts/test_functional_medicine_matrix.py",
]

REQUIRED_FILES = (
    ["SKILL.md", "README.md"]
    + REQUIRED_REFERENCE_FILES
    + REQUIRED_ASSET_FILES
    + REQUIRED_SCRIPTS
)

FORBIDDEN_EXTENSIONS = {".txt", ".pdf", ".docx"}

FORBIDDEN_MATRIX_CODES = [
    "DIG", "IMM", "ENM", "HRC", "DET", "STR", "NRM", "SLP", "ENV",
]

FORBIDDEN_BRANDED_TERMS = [
    "Institute for Functional Medicine",
    "IFM",
    "AFMCP",
    "5R Protocol",
    "GOTOIT",
    "GO-TO-IT",
]

SIX_EYE_LENS_NAMES = ["Body", "Mind", "Behavior", "Relationship", "Time", "Cause"]

RCT_VERIFICATION_STATUSES = [
    "FULL_TEXT_VERIFIED",
    "BIBLIOGRAPHIC_ONLY",
    "UNVERIFIED_LEAD",
]

VALID_RIGHTS_CLASSES = [
    "US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE",
    "OPEN_LICENSE_VERIFIED",
    "CITATION_ONLY",
    "UNKNOWN_DO_NOT_REPRODUCE",
]

REQUIRED_SAFETY_PHRASES = [
    "not medical advice",
    "licensed healthcare professional",
    "not a final diagnosis",
]

REQUIRED_FRONTMATTER_FIELDS = {
    "name": "open-functional-medicine-evidence-workflow",
    "version": "0.4.0",
}

# Patterns for unqualified self-execution or unauthorized individualized action.
# Numeric ranges are not forbidden by themselves: class-gated supplement, medical-
# nutrition and TCM drafts may contain them only when their evidence/reviewer gates pass.
PROHIBITED_ACTION_PATTERNS = [
    r"\byou\s+should\s+take\s+\d+\s*(mg|mcg|μg|IU|g|ml|mL)\b",
    r"\bstart\s+this\s+(supplement|formula|regimen|medication)\s+now\b",
    r"\b(stop|switch|replace)\s+(your\s+)?medication\b",
    r"\border\s+(a\s+)?(lab|test)\b",
    r"\byour\s+SNP\b",
    r"\byour\s+labs?\s+(show|prove)\b",
]

failures = []
warnings = []


def fail(msg):
    failures.append(msg)
    print(f"  FAIL: {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  WARN: {msg}")


def ok(msg):
    print(f"  OK:   {msg}")


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def word_count(text):
    return len(text.split())


def extract_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    raw = m.group(1)
    fm = {}
    for line in raw.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key and val:
                fm[key] = val
    return fm


def is_negative_or_non_affiliation_context(line):
    lower = line.lower()
    neg_patterns = [
        "not affiliated", "non-affiliation", "not endorsed", "not derived from",
        "must not", "must never", "may not appear", "forbidden", "excluded",
        "not included", "is not", "does not", "do not", "never", "no body-system",
        "no proprietary", "taxonomy code", "high-risk", "evidence debt",
        "refuse", "prohibited", "unsafe", "cannot", "may not", "e.g.", "example",
        "not ", "never contain",
    ]
    return any(p in lower for p in neg_patterns)


# ──────────────────────────────────────────────────────────────────────
# Check 1: Required files exist
# ──────────────────────────────────────────────────────────────────────

def check_required_files(root):
    print("\n[CHECK] Required files exist")
    for rel in REQUIRED_FILES:
        path = os.path.join(root, rel)
        if os.path.isfile(path):
            ok(rel)
        else:
            fail(f"Missing required file: {rel}")


# ──────────────────────────────────────────────────────────────────────
# Check 2: No forbidden extensions
# ──────────────────────────────────────────────────────────────────────

def check_no_forbidden_extensions(root):
    print("\n[CHECK] No forbidden file extensions (.txt/.pdf/.docx)")
    found = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            _, ext = os.path.splitext(fn)
            if ext.lower() in FORBIDDEN_EXTENSIONS:
                rel = os.path.relpath(os.path.join(dirpath, fn), root)
                found.append(rel)
    if found:
        for f in found:
            fail(f"Forbidden file type found: {f}")
    else:
        ok("No .txt/.pdf/.docx files found")


def check_no_literal_cjk(root):
    print("\n[CHECK] English release has no literal CJK characters")
    hits = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() not in {".md", ".py", ".json"}:
                continue
            path = os.path.join(dirpath, fn)
            for line_no, line in enumerate(read_file(path).splitlines(), 1):
                if CJK_PATTERN.search(line):
                    hits.append(f"{os.path.relpath(path, root)}:{line_no}")
    if hits:
        for hit in hits:
            fail(f"Literal CJK character found: {hit}")
    else:
        ok("No literal CJK characters found in Markdown, Python or JSON files")


# ──────────────────────────────────────────────────────────────────────
# Check 3: SKILL.md frontmatter
# ──────────────────────────────────────────────────────────────────────

def check_skill_frontmatter(root):
    print("\n[CHECK] SKILL.md frontmatter")
    path = os.path.join(root, "SKILL.md")
    if not os.path.isfile(path):
        fail("SKILL.md not found")
        return

    text = read_file(path)
    fm = extract_frontmatter(text)
    if fm is None:
        fail("SKILL.md: no YAML frontmatter found")
        return

    for key, expected in REQUIRED_FRONTMATTER_FIELDS.items():
        actual = fm.get(key)
        if actual is None:
            fail(f"SKILL.md frontmatter missing field: {key}")
        elif actual != expected:
            fail(f"SKILL.md frontmatter {key}: expected '{expected}', got '{actual}'")
        else:
            ok(f"Frontmatter {key} = '{actual}'")

    frontmatter_source = text.split("---", 2)[1] if text.startswith("---") else ""
    for key in ("description", "tags", "last_changed_at"):
        if re.search(rf"(?m)^\s*{key}:\s*", frontmatter_source):
            ok(f"Frontmatter key present: {key}")
        else:
            fail(f"SKILL.md frontmatter missing field: {key}")


# ──────────────────────────────────────────────────────────────────────
# Check 4: SKILL.md line count
# ──────────────────────────────────────────────────────────────────────

def check_skill_line_count(root):
    print(f"\n[CHECK] SKILL.md <= {SKILL_MAX_LINES} lines")
    path = os.path.join(root, "SKILL.md")
    if not os.path.isfile(path):
        fail("SKILL.md not found")
        return
    count = len(read_file(path).splitlines())
    if count <= SKILL_MAX_LINES:
        ok(f"SKILL.md has {count} lines (limit: {SKILL_MAX_LINES})")
    else:
        fail(f"SKILL.md has {count} lines (limit: {SKILL_MAX_LINES})")


# ──────────────────────────────────────────────────────────────────────
# Check 5: SKILL.md enumerates all reference/asset/script files
# ──────────────────────────────────────────────────────────────────────

def check_skill_enumeration(root):
    print("\n[CHECK] SKILL.md enumerates all reference/asset/script files")
    path = os.path.join(root, "SKILL.md")
    if not os.path.isfile(path):
        fail("SKILL.md not found")
        return

    text = read_file(path)
    all_files = REQUIRED_REFERENCE_FILES + REQUIRED_ASSET_FILES + REQUIRED_SCRIPTS
    for rel in all_files:
        basename = os.path.basename(rel)
        if basename in text or rel in text:
            ok(f"SKILL.md mentions {rel}")
        else:
            fail(f"SKILL.md does not mention {rel}")


# ──────────────────────────────────────────────────────────────────────
# Check 6: Source ledger schema
# ──────────────────────────────────────────────────────────────────────

def check_source_ledger(root):
    print("\n[CHECK] Source ledger: entry schema, source count, and rights classes")
    path = os.path.join(root, "reference", "source-ledger.md")
    if not os.path.isfile(path):
        fail("source-ledger.md not found")
        return

    text = read_file(path)
    entry_pattern = re.compile(r"(?ms)^### \[S(\d{2})\].*?(?=^---\s*$|^### \[S|\Z)")
    entries = entry_pattern.findall(text)
    blocks = list(entry_pattern.finditer(text))
    entry_count = len(entries)

    if 1 <= entry_count <= SOURCE_LEDGER_MAX_SOURCES:
        ok(f"Source ledger has {entry_count} entries (limit: {SOURCE_LEDGER_MAX_SOURCES})")
    else:
        fail(f"Source ledger has {entry_count} entries (expected 1-{SOURCE_LEDGER_MAX_SOURCES})")

    if len(set(entries)) != entry_count:
        fail("Source ledger contains duplicate source IDs")
    expected_ids = [f"{i:02d}" for i in range(1, entry_count + 1)]
    if entries == expected_ids:
        ok("Source IDs are unique and sequential")
    else:
        fail(f"Source IDs are not sequential: {entries}")

    required_fields = [
        "id", "title", "owner", "url", "retrieved", "verified",
        "rights_class", "supports", "allowed_use", "reproduction_boundary",
    ]
    class_counts = {rc: 0 for rc in VALID_RIGHTS_CLASSES}

    for match in blocks:
        sid = f"S{match.group(1)}"
        block = match.group(0)
        for field in required_fields:
            if re.search(rf"(?mi)^\|\s*\*\*{re.escape(field)}\*\*\s*\|", block):
                continue
            fail(f"{sid} missing ledger field: {field}")

        rights = re.findall(
            r"(?mi)^\|\s*\*\*rights_class\*\*\s*\|\s*([A-Z_]+)\s*\|",
            block,
        )
        if len(rights) != 1:
            fail(f"{sid} must have exactly one rights_class, found {len(rights)}")
        elif rights[0] not in VALID_RIGHTS_CLASSES:
            fail(f"{sid} has invalid rights_class: {rights[0]}")
        else:
            class_counts[rights[0]] += 1

    if not any("missing ledger field" in f or "rights_class" in f for f in failures):
        ok("Every source entry has the required schema and exactly one valid rights class")
    for rc, count in class_counts.items():
        if count:
            ok(f"Rights class count: {rc} = {count}")


# ──────────────────────────────────────────────────────────────────────
# Check 7: No URL outside source ledger
# ──────────────────────────────────────────────────────────────────────

def check_no_url_outside_ledger(root):
    print("\n[CHECK] No URLs outside source-ledger.md")
    ledger_path = os.path.join(root, "reference", "source-ledger.md")
    url_pattern = re.compile(r"https?://\S+")

    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            fp = os.path.join(dirpath, fn)
            if not fn.endswith(".md"):
                continue
            if fp == ledger_path:
                continue
            if fn == "SKILL.md":
                continue

            text = read_file(fp)
            urls = url_pattern.findall(text)
            if urls:
                rel = os.path.relpath(fp, root)
                for url in urls:
                    fail(f"URL found in {rel}: {url[:80]}")

    if not any("URL found" in f for f in failures):
        ok("No URLs found outside source-ledger.md")


# ──────────────────────────────────────────────────────────────────────
# Check 8: No quote-like paragraph over threshold
# ──────────────────────────────────────────────────────────────────────

def check_quote_limit(root):
    print(f"\n[CHECK] No quoted passage exceeds {QUOTE_MAX_WORDS} consecutive words")
    quote_pattern = re.compile(r"^>\s*(.+)", re.MULTILINE)

    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            text = read_file(fp)

            for match in quote_pattern.finditer(text):
                quote_text = match.group(1).strip()
                if len(quote_text) < 10:
                    continue
                wc = word_count(quote_text)
                if wc > QUOTE_MAX_WORDS:
                    rel = os.path.relpath(fp, root)
                    fail(f"Quote exceeds {QUOTE_MAX_WORDS} words in {rel}: '{quote_text[:60]}...' ({wc} words)")

    if not any("Quote exceeds" in f for f in failures):
        ok(f"All blockquotes within {QUOTE_MAX_WORDS}-word limit")


# ──────────────────────────────────────────────────────────────────────
# Check 9: No forbidden matrix codes
# ──────────────────────────────────────────────────────────────────────

def check_no_forbidden_codes(root):
    print("\n[CHECK] No forbidden matrix codes (DIG/IMM/ENM/HRC/DET/STR/NRM/SLP/ENV)")
    found_any = False

    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            text = read_file(fp)

            for code in FORBIDDEN_MATRIX_CODES:
                pattern = re.compile(r'\b' + code + r'\b')
                for m in pattern.finditer(text):
                    line_start = text.rfind('\n', 0, m.start()) + 1
                    line_end = text.find('\n', m.end())
                    if line_end == -1:
                        line_end = len(text)
                    line = text[line_start:line_end]

                    if is_negative_or_non_affiliation_context(line):
                        continue

                    rel = os.path.relpath(fp, root)
                    fail(f"Forbidden code '{code}' found in {rel}: '{line.strip()[:80]}'")
                    found_any = True

    if not found_any:
        ok("No forbidden matrix codes found")


# ──────────────────────────────────────────────────────────────────────
# Check 10: No proprietary/branded framework terms
# ──────────────────────────────────────────────────────────────────────

def check_no_branded_terms(root):
    print("\n[CHECK] No proprietary/branded framework terms")
    found_any = False

    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            text = read_file(fp)

            for term in FORBIDDEN_BRANDED_TERMS:
                if term.lower() not in text.lower():
                    continue

                for m in re.finditer(re.escape(term), text, re.IGNORECASE):
                    line_start = text.rfind('\n', 0, m.start()) + 1
                    line_end = text.find('\n', m.end())
                    if line_end == -1:
                        line_end = len(text)
                    line = text[line_start:line_end]

                    if is_negative_or_non_affiliation_context(line):
                        continue

                    rel = os.path.relpath(fp, root)
                    fail(f"Branded term '{term}' found in {rel}: '{line.strip()[:80]}'")
                    found_any = True

    if not found_any:
        ok("No proprietary/branded framework terms found")


# ──────────────────────────────────────────────────────────────────────
# Check 11: Six-Eye names and rules present
# ──────────────────────────────────────────────────────────────────────

def check_six_eye(root):
    print("\n[CHECK] Six-Eye lens names and required rules")
    paths = [
        os.path.join(root, "reference", "six-eye-inquiry.md"),
        os.path.join(root, "reference", "six-eye-insight.md"),
    ]
    texts = []
    for p in paths:
        if os.path.isfile(p):
            texts.append(read_file(p))
        else:
            fail(f"Missing Six-Eye file: {os.path.relpath(p, root)}")

    combined = "\n".join(texts)

    for name in SIX_EYE_LENS_NAMES:
        if name in combined:
            ok(f"Six-Eye lens name found: {name}")
        else:
            fail(f"Six-Eye lens name missing: {name}")

    required_phrases = [
        "internal design",
        "unvalidated",
        "NOT a diagnostic tool",
        "NOT a validated",
        "at most one bounded",
    ]
    for phrase in required_phrases:
        if phrase in combined:
            ok(f"Six-Eye required phrase found: '{phrase}'")
        else:
            fail(f"Six-Eye required phrase missing: '{phrase}'")


# ──────────────────────────────────────────────────────────────────────
# Check 12: RCT verification statuses and evidence fields
# ──────────────────────────────────────────────────────────────────────

def check_rct_governance(root):
    print("\n[CHECK] RCT verification statuses and evidence fields")
    paths = [
        os.path.join(root, "reference", "evidence-governance.md"),
        os.path.join(root, "reference", "evidence-and-uncertainty.md"),
    ]
    texts = []
    for p in paths:
        if os.path.isfile(p):
            texts.append(read_file(p))
        else:
            fail(f"Missing evidence file: {os.path.relpath(p, root)}")

    combined = "\n".join(texts)

    for status in RCT_VERIFICATION_STATUSES:
        if status in combined:
            ok(f"Verification status found: {status}")
        else:
            fail(f"Verification status missing: {status}")

    required_fields = [
        "identifier",
        "Applicability",
        "Harms",
        "contradict",
        "alternative",
        "falsif",
        "evidence debt",
        "Limitation",
        "GENERATION-ONLY",
        "professional reasoning alone is insufficient",
        "question-generation note",
        "must not be emitted as Evidence Cards",
        "must not support a substantive factual or clinical finding",
    ]
    for field in required_fields:
        if field.lower() in combined.lower():
            ok(f"Evidence field/boundary found: '{field}'")
        else:
            fail(f"Evidence field/boundary missing: '{field}'")


# ──────────────────────────────────────────────────────────────────────
# Check 13: Required safety/red-line language
# ──────────────────────────────────────────────────────────────────────

def check_safety_language(root):
    print("\n[CHECK] Required safety/red-line language")

    path = os.path.join(root, "reference", "scope-and-red-lines.md")
    if os.path.isfile(path):
        text = read_file(path)
        stripped = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
        collapsed = " ".join(stripped.lower().split())
        for phrase in REQUIRED_SAFETY_PHRASES:
            if phrase.lower() in collapsed:
                ok(f"Safety phrase found in scope-and-red-lines.md: '{phrase}'")
            else:
                fail(f"Safety phrase missing in scope-and-red-lines.md: '{phrase}'")

    path = os.path.join(root, "reference", "output-contract.md")
    if os.path.isfile(path):
        text = read_file(path)
        if "PROFESSIONAL DIAGNOSTIC-SUPPORT DISCLAIMER" in text:
            ok("Output contract has diagnostic-support disclaimer header")
        else:
            fail("Output contract missing 'PROFESSIONAL DIAGNOSTIC-SUPPORT DISCLAIMER'")

    path = os.path.join(root, "SKILL.md")
    if os.path.isfile(path):
        text = read_file(path)
        if "PROFESSIONAL DIAGNOSTIC-SUPPORT DISCLAIMER" in text:
            ok("SKILL.md has diagnostic-support disclaimer header")
        else:
            fail("SKILL.md missing 'PROFESSIONAL DIAGNOSTIC-SUPPORT DISCLAIMER'")

    diagnostic_support_guards = {
        "SKILL.md": "authorized, minimum-necessary, de-identified",
        "reference/scope-and-red-lines.md": "licensed healthcare professional",
        "reference/intake-and-triage.md": "AUTHORIZED_DEIDENTIFIED_INDIVIDUAL",
        "reference/output-contract.md": "INDIVIDUAL DIAGNOSTIC SUPPORT DRAFT",
        "reference/evidence-and-safety-debt.md": "not automatically become a diagnosis",
        "assets/structured-intake-template.md": "AUTHORIZED DE-IDENTIFIED INDIVIDUAL CASE",
        "assets/individual-diagnostic-support-template.md": "NOT A FINAL DIAGNOSIS",
        "assets/review-output-template.md": "SYNTHETIC TRAINING USE ONLY",
        "assets/hypothetical-case-template.md": "SYNTHETIC TRAINING CASE ONLY",
    }
    for rel, phrase in diagnostic_support_guards.items():
        guarded_path = os.path.join(root, rel)
        if not os.path.isfile(guarded_path):
            fail(f"Diagnostic-support guard file missing: {rel}")
        elif phrase.lower() in read_file(guarded_path).lower():
            ok(f"Diagnostic-support guard found in {rel}")
        else:
            fail(f"Diagnostic-support guard missing in {rel}: '{phrase}'")

    card_path = os.path.join(root, "assets", "evidence-card-template.md")
    if os.path.isfile(card_path):
        card_text = read_file(card_path)
        forbidden_tiers = [
            "`PROFESSIONAL-REASONING` — based on",
            "`SPECULATIVE` — plausible connection",
        ]
        for phrase in forbidden_tiers:
            if phrase in card_text:
                fail(f"Evidence-card template reintroduces forbidden tier: {phrase}")
            else:
                ok(f"Evidence-card forbidden tier absent: {phrase.split('`')[1]}")
        for phrase in ("question-generation note", "cannot support a substantive finding"):
            if phrase.lower() in card_text.lower():
                ok(f"Evidence-card boundary found: '{phrase}'")
            else:
                fail(f"Evidence-card boundary missing: '{phrase}'")


# ──────────────────────────────────────────────────────────────────────
# Check 14: Prohibited treatment, prescribing, dosing, and order actions
# ──────────────────────────────────────────────────────────────────────

def check_prohibited_actions(root):
    print("\n[CHECK] Prohibited treatment / prescribing / dosing / order actions")
    found_any = False

    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            text = read_file(fp)
            lines = text.splitlines()

            for pattern in PROHIBITED_ACTION_PATTERNS:
                for m in re.finditer(pattern, text, re.IGNORECASE):
                    line_start = text.rfind('\n', 0, m.start()) + 1
                    line_end = text.find('\n', m.end())
                    if line_end == -1:
                        line_end = len(text)
                    line_idx = text[:line_start].count('\n')
                    line = text[line_start:line_end]

                    if is_negative_or_non_affiliation_context(line):
                        continue

                    # Check surrounding lines for negative/prohibited context.
                    window = []
                    for offset in list(range(-8, 0)) + list(range(1, 4)):
                        idx = line_idx + offset
                        if 0 <= idx < len(lines):
                            window.append(lines[idx])
                    if any(is_negative_or_non_affiliation_context(wline) for wline in window):
                        continue

                    rel = os.path.relpath(fp, root)
                    fail(f"Prohibited action pattern in {rel}: '{line.strip()[:80]}'")
                    found_any = True

    if not found_any:
        ok("No prohibited clinical action patterns found")


# ──────────────────────────────────────────────────────────────────────
# Check 15: Self-contained v0.4 routing, formula, artifact, and validation contract
# ──────────────────────────────────────────────────────────────────────

def check_v04_contract(root):
    print("\n[CHECK] Self-contained v0.4 routing / formula / artifact contract")

    phrase_contracts = {
        "SKILL.md": [
            "Route A", "Route B", "fresh, current authoritative guidance", "all four classes",
            "food/lifestyle recipe", "supplement plan", "medical nutrition",
            "TCM formula", "functional_medicine_matrix.json", "functional_medicine_matrix.svg",
            "functional_medicine_matrix.md", "functional_medicine_matrix_manifest.json", "model-I/O",
        ],
        "README.md": [
            "ordinary nutrition/health evidence questions",
            "authorized individual case analysis",
            "freshly verified guidance", "functional_medicine_matrix.svg",
            "no longitudinal history/version/current-projection feature",
            "no generic staged conversation state machine",
        ],
        "reference/invocation-and-evidence-routing.md": [
            "Route A — direct knowledge/evidence question",
            "Route B — case analysis / personalized plan",
            "do not force every question through case intake",
            "Direct evidence question → answer directly with fresh verified evidence",
            "No longitudinal history/version feature",
        ],
        "reference/model-io-and-output-validation.md": [
            "Model assistance is optional and untrusted",
            "Keep instructions separate from user data",
            "native structured-output/JSON-schema mode",
            "fields outside the requested schema",
            "Required adversarial tests",
        ],
        "reference/output-contract.md": [
            "Direct evidence answer", "Functional-medicine matrix bundle",
            "Food/lifestyle recipe", "Supplement plan",
            "Medical-nutrition plan", "TCM formula",
            "material AI-assistance disclosure",
        ],
    }
    for rel, phrases in phrase_contracts.items():
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            fail(f"v0.4 contract file missing: {rel}")
            continue
        text = read_file(path).lower()
        missing = [phrase for phrase in phrases if phrase.lower() not in text]
        if missing:
            fail(f"v0.4 contract phrases missing in {rel}: {missing}")
        else:
            ok(f"v0.4 contract phrases present in {rel}")

    expected_states = {
        "food_lifestyle": [
            "ready_for_low_risk_use",
            "professional_review_recommended",
            "blocked_for_safety_or_missing_core_input",
        ],
        "supplement": [
            "incomplete_scaffold_needs_core_input",
            "draft_for_qualified_professional_review",
            "draft_with_mandatory_specialist_review",
            "rejected_for_safety",
            "human_review_recorded",
        ],
        "medical_nutrition": [
            "incomplete_scaffold_needs_clinical_data",
            "draft_for_responsible_clinical_team",
            "rejected_or_escalated",
            "human_clinical_authorization_recorded",
        ],
        "tcm_formula": [
            "incomplete_scaffold_needs_syndrome_or_identity",
            "draft_for_licensed_tcm_practitioner_review",
            "draft_with_mandatory_cross_specialty_review",
            "rejected_for_safety",
            "human_practitioner_review_recorded",
        ],
    }
    release_path = os.path.join(root, "assets", "release-status-template.json")
    try:
        release = json.loads(read_file(release_path))
        if release.get("schema_version") != "2.0":
            fail("release-status template schema_version must be 2.0")
        states = release.get("allowed_release_states_by_class")
        if states != expected_states:
            fail("release-status class/state map does not match the four normative class gates")
        else:
            ok("Release-status JSON has exact four-class state map")
        artifact_class = release.get("artifact_class")
        if artifact_class not in expected_states:
            fail("release-status artifact_class is not one of the four classes")
        elif release.get("release_state") not in expected_states[artifact_class]:
            fail("release-status example state is invalid for its artifact_class")
        else:
            ok("Release-status example class/state pair is valid")
        validation = release.get("model_output_validation", {})
        required_validation = {
            "strict_parse", "schema_and_allowlist", "provenance_and_evidence",
            "class_gate", "safety_and_interaction",
            "renderer_and_artifact_integrity", "final_status",
        }
        if set(validation) != required_validation:
            fail("release-status model_output_validation keys are incomplete or unknown")
        else:
            ok("Release-status JSON exposes per-stage model-output validation")
        if "AI-assisted" not in release.get("ai_assistance_disclosure", ""):
            fail("release-status template must disclose AI assistance")
        else:
            ok("Release-status JSON discloses AI assistance")
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        fail(f"Could not validate release-status template: {exc}")

    formula_templates = {
        "assets/food-lifestyle-plan-template.md": expected_states["food_lifestyle"],
        "assets/supplement-plan-template.md": expected_states["supplement"],
        "assets/medical-nutrition-template.md": expected_states["medical_nutrition"],
        "assets/tcm-formula-template.md": expected_states["tcm_formula"],
    }
    for rel, states in formula_templates.items():
        text = read_file(os.path.join(root, rel))
        missing = [state for state in states if state not in text]
        if missing:
            fail(f"Formula template missing normative release states in {rel}: {missing}")
        else:
            ok(f"Formula template has exact class states: {rel}")

    matrix_path = os.path.join(root, "assets", "functional-medicine-matrix-state-template.json")
    try:
        matrix = json.loads(read_file(matrix_path))
        required_top = {
            "schema_version", "language", "case_key", "generated_at", "items",
            "lifestyle", "links", "flags", "review",
        }
        if set(matrix) != required_top:
            fail("functional-medicine-matrix input template has missing or unknown top-level keys")
        elif matrix.get("schema_version") != "2.0":
            fail("functional-medicine-matrix input schema_version must be 2.0")
        else:
            ok("Functional-medicine-matrix input template has exact schema 2.0 top-level keys")
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        fail(f"Could not validate functional-medicine-matrix input template: {exc}")

    generator_path = os.path.join(root, "scripts", "generate_functional_medicine_matrix.py")
    generator_text = read_file(generator_path)
    for token in (
        "functional_medicine_matrix.json", "functional_medicine_matrix.svg", "functional_medicine_matrix.md",
        "functional_medicine_matrix_manifest.json", "reject_unknown", "atomic_write", "md_escape",
        "items must include at least one source-grounded case item", "organizational completeness view",
    ):
        if token not in generator_text:
            fail(f"Functional-medicine-matrix generator missing required implementation token: {token}")
        else:
            ok(f"Functional-medicine-matrix generator token found: {token}")

    if re.search(r"mindbody", generator_text, re.IGNORECASE):
        fail("Functional-medicine-matrix generator source must not contain 'mindbody'")
    else:
        ok("Functional-medicine-matrix generator source does not contain 'mindbody'")

    if re.search(r"<line", generator_text, re.IGNORECASE):
        fail("Functional-medicine-matrix generator source must not contain '<line' (no spokes/edges)")
    else:
        ok("Functional-medicine-matrix generator source does not contain '<line'")


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <candidate_root>")
        sys.exit(2)

    root = sys.argv[1]
    if not os.path.isdir(root):
        print(f"Error: '{root}' is not a directory")
        sys.exit(2)

    print(f"Validating candidate at: {os.path.abspath(root)}")
    print("=" * 60)

    check_required_files(root)
    check_no_forbidden_extensions(root)
    check_no_literal_cjk(root)
    check_skill_frontmatter(root)
    check_skill_line_count(root)
    check_skill_enumeration(root)
    check_source_ledger(root)
    check_no_url_outside_ledger(root)
    check_quote_limit(root)
    check_no_forbidden_codes(root)
    check_no_branded_terms(root)
    check_six_eye(root)
    check_rct_governance(root)
    check_safety_language(root)
    check_prohibited_actions(root)
    check_v04_contract(root)

    print("\n" + "=" * 60)
    print(f"RESULTS: {len(failures)} failure(s), {len(warnings)} warning(s)")

    if failures:
        print("\nFailures:")
        for i, f in enumerate(failures, 1):
            print(f"  {i}. {f}")
        sys.exit(1)
    else:
        print("\nAll checks PASSED.")
        sys.exit(0)


if __name__ == "__main__":
    main()
