# Formula Two-Pass Retrieval Contract — 功能医学综合Skill

> **"过一遍全文" = 全覆盖索引检查，不是把整本书加载到一个上下文里。**
> The formula route performs full *coverage check*, not full *body loading*.

## 1. Trigger

When user request contains any: 配方, 补剂, 营养素处方, 营养素方案, 处剂, 配方案, 营养补充方案, 分阶段干预策略, formula, supplement regimen, nutrient protocol — the system enters Mode B.

## 2. Two-Pass Architecture

### Phase A — Targeted Deep Retrieval

**Purpose:** Load and deeply read only the highest-relevance source passages for this specific formula.

**Inputs used for targeting:**
- Formula purpose / therapeutic goal
- Patient symptoms and diagnoses
- Current medications and contraindications
- Target nutrients and supplement candidates
- Special populations (pregnancy, pediatric, elderly, hepatic/renal, drug interactions)

**Process:**
1. From the inputs above, identify the relevant body systems (e.g., digestive, hormonal, immune)
2. Use the v2 expert-index lexical routing (or manual routing table) to select the highest-relevance expert nodes and source chunks
3. Load those selected source passages in full
4. Read deeply: extract candidate nutrients, dose ranges, contraindications, synergies/antagonisms, special-population adjustments
5. Record each deep-read passage in the coverage ledger with `phase: A` and `status: complete`

**What Phase A is NOT:**
- It does NOT load every knowledge file at full depth
- It does NOT require equal reading cost for all chapters
- It loads only the passages most relevant to this formula's specific clinical picture

### Phase B — Corpus-Wide Omission/Safety Sweep

**Purpose:** Evaluate EVERY canonical chapter/chunk's compact index to catch omissions, conflicts, contraindications, interactions, and uncertainties that Phase A may have missed.

**Process:**
1. Walk every canonical chunk in the stable order of the **built v2 registry/index**; verify each identity and hash against `source-manifest.json`
2. For each chunk, evaluate ONLY its compact index entry:
   - L0 weighted trigger terms
   - L0 expert anti-triggers
   - L1 brief and safety red lines
   - L1 uncertainty declarations
   - Chunk-level risk tags
3. Record in coverage ledger: `phase: B`, `sweep_status: swept`
4. **Escalation rule:** If any sweep reveals:
   - A new candidate nutrient not found in Phase A
   - A conflict with Phase A recommendations
   - A contraindication or drug-nutrient interaction
   - An uncertainty or safety red line relevant to this formula
   → **Escalate that exact chunk to deep loading.** Load the full original passage, read it, extract details, record `sweep_status: escalated_resolved` or `escalated_unresolved`
5. **After escalation:** ANY `escalated_unresolved` or `unreadable` item blocks formula finalization absolutely — no exceptions, no justification bypass

**What Phase B is NOT:**
- It does NOT load all full source bodies equally into context
- It does NOT give every chapter the same deep-reading cost
- It evaluates compact index entries (L0/L1) only, escalating to full bodies on hit

## 3. Finalization Gates

Formula finalization is allowed ONLY when ALL four conditions are met:

| Gate | Condition | Fail-Closed Rule |
|------|-----------|-----------------|
| (A) | All Phase A targeted sources were deep-read | Missing/unreadable source → abort |
| (B) | Every corpus index/chunk was swept in Phase B | Missing index/chunk/hash → abort |
| (C) | All sweep hits were escalated and resolved | ANY `escalated_unresolved` or `unreadable` item → abort |
| (D) | All SHA-256 hashes pass against source-manifest | Hash mismatch → abort |

## 4. Coverage Ledger Schema

Each entry in the ledger tracks exactly one canonical registry chunk:

| Field | Type | Description |
|-------|------|-------------|
| `chunk_id` | string | Unique chunk ID from the built registry |
| `chunk_path` | string | Exact relative chunk path from the built registry |
| `sha256` | string | SHA-256 from source-manifest or corpus_manifest |
| `phase` | enum | `A` (deep-read) or `B` (sweep-only) |
| `status` | enum | `pending` / `complete` / `unreadable` |
| `sweep_status` | enum | `pending` / `swept` / `escalated_resolved` / `escalated_unresolved` / `N/A` (for Phase A deep-read entries) |
| `escalation_reason` | string | Why this chunk was escalated (empty if not escalated) |
| `extracted_candidates` | integer | Candidate nutrients extracted from this entry |
| `constraints_extracted` | integer | Contraindications/interactions/adjustments extracted |

### Coverage Calculation
```
phase_A_pct = (entries where phase=A and status=complete) / (all Phase A targeted entries) * 100
phase_B_pct = (entries where sweep_status in {swept, escalated_resolved}) / (total corpus entries) * 100
all_resolved = no entries with sweep_status=escalated_unresolved OR status=unreadable
# ANY escalated_unresolved or unreadable entry blocks finalization absolutely
```

**Finalization condition:** `phase_A_pct == 100 AND phase_B_pct == 100 AND all_resolved == true`

## 5. Output

1. **Formula table:** Nutrient, dose, indication, source chunk reference
2. **Phased protocol:** 强化期 → 维持期
3. **Evidence table (Table 1):** RCT/animal/molecular-pathway evidence per nutrient
4. **Standards table (Table 2):** China RNI/UL, US RDA/UL, EU EFSA
5. **Coverage ledger:** Full JSON with phase A/B entries, sweep statuses, escalation reasons
6. **Safety annotations:** Special-population safety-gate results
7. **Limitations statement**

## 6. Key Distinction from Old Contract

| Aspect | Old (Equal-Depth) | New (Two-Pass) |
|--------|-------------------|----------------|
| Loading strategy | Load ALL full source bodies | Phase A: deep-read selected only; Phase B: sweep compact index only |
| Runtime cost | Proportional to total corpus size | Proportional to Phase A selection + Phase B index size |
| Escalation | None (everything loaded) | Sweep hits escalate to targeted deep loading |
| "过一遍全文" meaning | Copy entire book into context | Check every chunk's index, escalate on hit |
| Correctness equivalence? | Not established merely by loading everything | Not assumed; safety depends on complete semantic indexing, full index coverage, exact-source escalation, and resolution of every hit |

## 7. One-Time V2 Distillation (Separate Requirement)

The v2 `sparse-book-to-skill-distillation` method requires complete semantic review of every chunk (L0-L3 authoring) before any sparse runtime use. This is a one-time prerequisite, not a per-query cost. The formula two-pass contract operates *after* the v2 build is complete, using the built index/registry for Phase B sweeps.
