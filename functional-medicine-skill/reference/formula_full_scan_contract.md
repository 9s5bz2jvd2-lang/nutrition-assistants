# Formula Two-Pass Retrieval Contract — Global Evidence + Regulatory Gate Edition

> **Schema version:** `formula-full-scan-contract-v2.0`
> **Supersedes:** `formula_full_scan_contract.md` v1 (baseline commit `9f48aee`)
> **Purpose:** Define a complete, non-blocking draft and evidence contract for formula-mode operation. Fail-closed rules apply to finalization, efficacy promotion, and market claims—not to creating a reviewable draft or recording evidence gaps.

---

## 1. Trigger

When user request contains any: 配方, 补剂, 营养素方案, 处方, 配方案, 营养补充方案, 分阶段干预策略, formula, supplement regimen, nutrient protocol — the system enters Mode B.

**New trigger additions:** The system also enters Mode B when any of the following are requested:
- Regulatory assessment or compliance check for a formula
- Market-readiness evaluation
- Cross-jurisdiction ingredient status

---

## 2. Pre-Formula Gate: Context & Identity

Mode C v3 treats context and identity as **recording and evidence-eligibility gates**, not a reason to suppress a reviewable draft.

- Preserve every supplied field. For formula purpose, intended use, product category, target markets, target population, medication, pregnancy/lactation, allergy, and treatment history, missing means `UNKNOWN` and becomes a reminder/human-review row.
- For every ingredient, record common name, scientific Latin name (if botanical), plant part, processing, extract ratio/marker, chemical form, and dose/unit when supplied.
- A botanical with an unresolved scientific identity, plant part, preparation, marker, or dose unit becomes `BLOCKED_IDENTITY`: retain its draft row, write a blocked search-ledger row, and do not run botanical-specific evidence queries until identity is resolved.
- Missing target market or product category becomes `unknown`/`not_assessed` in T4. It blocks market-ready/global-compliant claims only.
- These gaps never abort draft creation or unrelated evidence tracks.

## 3. Two-Pass Corpus Architecture (Retained)

### Phase A — Targeted Deep Retrieval

**Purpose:** Load and deeply read only the highest-relevance source passages for this specific formula.

**Inputs used for targeting:**
- Formula purpose / therapeutic goal
- Patient symptoms and diagnoses
- Current medications and contraindications
- Target nutrients and supplement candidates
- Special populations (pregnancy, pediatric, elderly, hepatic/renal, drug interactions)
- Target markets / jurisdictions

**Process:**
1. From the inputs above, identify the relevant body systems
2. Use the v2 expert-index lexical routing (or manual routing table) to select the highest-relevance expert nodes and source chunks
3. Load those selected source passages in full
4. Read deeply: extract candidate nutrients, dose ranges, contraindications, synergies/antagonisms, special-population adjustments
5. Record each deep-read passage in the coverage ledger with `phase: A` and `status: complete`

### Phase B — Corpus-Wide Omission/Safety Sweep

**Purpose:** Evaluate EVERY canonical chapter/chunk's compact index to catch omissions, conflicts, contraindications, interactions, and uncertainties that Phase A may have missed.

**Process:**
1. Walk every canonical chunk in the stable order of the built v2 registry/index
2. For each chunk, evaluate ONLY its compact index entry (L0/L1)
3. Record in coverage ledger: `phase: B`, `sweep_status: swept`
4. **Escalation rule:** If sweep reveals new candidates, conflicts, contraindications, or safety red lines → escalate to deep loading
5. **After escalation:** ANY `escalated_unresolved` or `unreadable` item blocks formula finalization absolutely

---

## 4. Post-Draft: Four-Track Evidence Discovery

After `DRAFT_CREATED`, automatically execute the following **four** tracks for each evidence-eligible ingredient. Every attempted query, zero result, inaccessible source, or blocked identity writes a ledger row with ingredient, track, source, query, date, outcome, and reason.

### Track 1: Human Clinical Evidence
- SR/MA/RCT and other verified human clinical records; source families include PubMed, Cochrane, Embase, CNKI.
- Report locator, population, intervention/specification, dose, duration, outcomes, and limitations.

### Track 2: Animal/In-vivo Evidence
- Report species/model, route, animal dose/unit, duration, endpoints, and limitations.
- Every entry states animal results and dose are not directly translatable to human efficacy or dose.

### Track 3: TCM/Material Evidence
- T1 classical record: only with title, edition/version, and specific original location.
- T2 pharmacopeial/official monograph identity: only with verifiable monograph/source details.
- T3 modern TCM clinical research is assessed under Track 1 standards.
- T1/T2 are never clinical efficacy proof.

### Track 4: Regulatory Evidence
- Assess ingredient × declared target market × product category from authoritative sources.
- Values are `permitted`, `conditional`, `prohibited`, `unknown`, or `not_assessed`.
- Unknown market/category remains visible as `not provided` / `not_assessed`; it never invents clearance and never suppresses the draft or T1–T3.

### Reminder/Safety Sidecar (not an evidence track)
- Record mechanisms, adverse-effect signals, interaction signals, medication/use-time questions, and red flags.
- Set `mechanism_is_not_efficacy_proof=true`; these items cannot support a human efficacy claim or a regulatory conclusion.

## 5. Finalization and Market-Claim Gates

Phase A/B failures, unresolved identity, unexecuted/failed evidence queries, safety gaps, or T4 unknowns remain visible in the draft output and block the relevant **finalization, efficacy, or market claim**. They do not erase `DRAFT_CREATED` or stop independent work.

## 6. Finalization Gates (Comprehensive)

| Gate | Condition | Fail-Closed Rule |
|------|-----------|------------------|
| (A) | All Phase A targeted sources were deep-read | Missing/unreadable source → block finalization; retain draft + gap row |
| (B) | Every corpus index/chunk was swept in Phase B | Missing index/chunk/hash → block finalization; retain draft + gap row |
| (C) | All sweep hits were escalated and resolved | ANY `escalated_unresolved` or `unreadable` → block finalization; retain draft + gap row |
| (D) | All SHA-256 hashes pass against source-manifest | Hash mismatch → block finalization; retain draft + gap row |
| (E1) | Formula context and identity fully resolved | Missing/ambiguous → record UNKNOWN/BLOCKED_IDENTITY; retain draft |
| (E2) | All four evidence tracks executed for every ingredient | Any unexecuted track → ledger row + block finalization, not draft |
| (E3) | Human evidence status does not imply efficacy when absent | Text implies efficacy + `evidence_status=absent` → abort |
| (E4) | Animal/traditional/mechanistic not promoted to clinical proof | Cross-tier promotion → abort |
| (E5) | Regulatory assessment for every ingredient × every jurisdiction × every category | Any `unknown` or `not_assessed` → blocks market-ready claim |
| (E6) | No fabricated citations, DOIs, trials, or regulatory statuses | Fabrication → block finalization; retain correction/review record |
| (E7) | Search ledger recorded for all queries | Missing search record → block finalization; retain draft |
| (E8) | Existing two-pass corpus safety contract retained | Phase A/B incomplete → block finalization; retain draft |

---

## 7. Coverage Ledger Schema (Retained, Unchanged)

Each entry in the ledger tracks exactly one canonical registry chunk (see `formula_coverage_ledger_template.json`). Fields: chunk_id, chunk_path, sha256, phase (A/B), status (pending/complete/unreadable), sweep_status (pending/swept/escalated_resolved/escalated_unresolved/N/A), escalation_reason, extracted_candidates, constraints_extracted.

**Finalization condition:** `phase_A_pct == 100 AND phase_B_pct == 100 AND all_resolved == true`

---

## 8. Output Templates

The complete formula output MUST include:

1. **Formula candidate** (see `templates/formula_candidate_template.md`)
2. **Four-track evidence matrix** (see `templates/evidence_matrix_template.md`)
3. **TCM identity & material matrix** (see `templates/tcm_identity_material_matrix_template.md`, if applicable)
4. **Regulatory coverage matrix** (see `templates/regulatory_coverage_matrix_template.md`)
5. **Per-source search ledger** (see `templates/search_ledger_template.md`)
6. **Two-pass coverage ledger** (see `reference/formula_coverage_ledger_template.json`)
7. **Blocking/residual-risk summary** (see `templates/blocking_risk_summary_template.md`)

Every template must include source date/version and status values.

---

## 9. Finalization Checklist (Updated)

1. ✅ Phase A: All targeted sources deep-read (status=complete)
2. ✅ Phase B: Every corpus chunk swept (sweep_status ≠ pending)
3. ✅ No `escalated_unresolved` items
4. ✅ No `unreadable` or hash mismatches
5. ✅ Every candidate ingredient has source annotation
6. ✅ Special-population safety gate checked
7. ✅ Four-track evidence matrix generated (Track 1-4 for every ingredient)
8. ✅ Regulatory coverage matrix generated (every ingredient × every jurisdiction × every category)
9. ✅ Search ledger generated (all queries recorded)
10. ✅ Coverage ledger output with formula
11. ✅ Context and identity gate resolved
12. ✅ No cross-tier promotion violations (TCM T1/T2 → efficacy)
13. ✅ No fabricated citations or regulatory statuses
14. ✅ Blocking/residual-risk summary generated

---

## 10. Key Distinction from Baseline

| Aspect | Baseline (v1) | Upgraded (v2) |
|--------|--------------|---------------|
| Evidence tracks | Human RCT + animal + molecular pathway (single table) | Four distinct tracks (human, animal, TCM three-tier, mechanistic/safety) |
| TCM separation | Rudimentary | Explicit T1/T2/T3 separation with no cross-tier promotion |
| Regulatory coverage | "各国使用标准" table (China/US/EU) | Full jurisdiction-registry model with per-ingredient × per-market assessment |
| Identity gate | Implicit | Explicit fail-closed identity tuple for every ingredient |
| Botanical identity | Not enforced | Species/plant-part/extract ambiguity → fail closed |
| Source registry | Not versioned | Versioned, bounded, with explicit coverage statuses |
| Non-authoritative sources | Not explicitly rejected | Explicitly cannot clear regulatory gate |
| Market-ready claims | No gate | Requires ALL ingredients × ALL jurisdictions assessed |
| Output templates | 2 tables (evidence + standards) | 7 templates with complete status vocabulary |
| Finalization gates | 4 (A-D) | 13 (A-D, E1-E8) |
