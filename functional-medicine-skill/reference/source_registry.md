# Authoritative Source Registry — Formula Evidence & Regulatory Gate

> **Schema version:** `source-registry-v1.0`
> **Generated:** 2026-07-15 (candidate, not yet deployed)
> **Purpose:** Define authoritative source families for formula-level evidence discovery and regulatory assessment. This registry is the single source of truth for which sources are authoritative, what they cover, and what they do NOT cover.

---

## 1. Registry Principles

1. **Versioned and bounded.** Every source family has an explicit name, URL, scope, coverage status, and known limitations. An unregistered source cannot clear a gate.
2. **Fail-closed on ambiguity.** If a source's jurisdiction, product category, or coverage status is uncertain, the assessment is `unknown` — never `cleared`.
3. **Separate evidence from compliance.** Clinical evidence sources and regulatory sources are distinct families. A PubMed RCT does not authorize market sale; an FDA GRAS letter does not prove clinical efficacy.
4. **Honest coverage statuses.** Each source has one of: `active`, `limited`, `uncovered`, `needs_jurisdiction_specific_review`.
5. **No fabricated access.** Dates and identifiers must be verifiable. A search snippet is never evidence.

---

## 2. Evidence Source Families

### 2.1 Human Clinical Evidence Sources

| Source ID | Name | URL | Scope | Coverage Status | Notes |
|-----------|------|-----|-------|-----------------|-------|
| `pubmed` | PubMed / MEDLINE | https://pubmed.ncbi.nlm.nih.gov | Biomedical literature, RCTs, systematic reviews, meta-analyses | `active` | Free text search; does NOT index all Chinese-language journals comprehensively |
| `cochrane` | Cochrane Library | https://www.cochranelibrary.com | Systematic reviews, meta-analyses, clinical trials | `active` | Gold standard for systematic reviews; some full-text requires subscription |
| `embase` | Embase (Elsevier) | https://www.embase.com | Biomedical + pharmacological literature, conference abstracts | `active` | Broader pharmacological coverage than PubMed; subscription required |
| `clinicaltrials_gov` | ClinicalTrials.gov | https://clinicaltrials.gov | US and international trial registrations, results | `active` | Includes unpublished/negative results; does NOT cover all non-US registries |
| `who_ictrp` | WHO ICTRP | https://trialsearch.who.int | International clinical trial registry platform | `active` | Aggregates multiple national registries; coverage varies by country |
| `cnki` | CNKI (China National Knowledge Infrastructure) | https://www.cnki.net | Chinese-language journals, dissertations, conference proceedings | `active` | Primary source for Chinese TCM clinical studies; subscription/full-text access varies |
| `cbm` | CBM (China Biology Medicine) | https://www.sinomed.ac.cn | Chinese biomedical literature | `limited` | Complements CNKI for TCM and clinical studies |
| `who_itrp` | WHO International Traditional Medicine references | https://www.who.int/health-topics/traditional-complementary-and-integrative-medicine | WHO-positioned traditional medicine frameworks | `limited` | Policy-level, not primary evidence |

**Coverage limitation notes:**
- No single database covers all languages, all countries, and all study types.
- Chinese-language TCM clinical studies require CNKI/CBM in addition to PubMed.
- Preprints, grey literature, and conference abstracts require Embase or specific repository access.
- A `web_search` snippet alone is NOT an authoritative source and cannot clear an evidence gate.

### 2.2 Animal Evidence Sources

Animal studies are indexed in the same primary databases (PubMed, Embase, CNKI) using species-specific search terms. No separate animal-only registry exists. Animal evidence is tracked in the evidence matrix with explicit species, model, dose, and translation-limit fields.

### 2.3 TCM Classical/Traditional Sources

| Source ID | Name | Scope | Coverage Status | Notes |
|-----------|------|-------|-----------------|-------|
| `cp2020` | Pharmacopoeia of the People's Republic of China (2020 Edition) | Official TCM monographs, chemical drugs, biologics; 5,911 monographs | `active` | Current official edition; issued by NMPA/NHC; updated every ~5 years |
| `cp_previous` | Previous editions of Chinese Pharmacopoeia | Historical monographs | `limited` | Superseded by 2020 edition for regulatory purposes; useful for historical reference |
| `tcm_classics` | Classical TCM texts (Shennong Bencao Jing, Bencao Gangmu, etc.) | Traditional materia medica, classical formulations | `active` for traditional record | Traditional record is NOT clinical-efficacy evidence; editions must be specified |
| `who_mong` | WHO Monographs on Selected Medicinal Plants | Standardized botanical monographs | `active` | International reference; does not replace national pharmacopoeias |
| `escop` | ESCOP Monographs (European Scientific Cooperative on Phytotherapy) | European herbal medicine monographs | `active` | Peer-reviewed; supplements but does not replace EU regulatory decisions |
| `hmpdc` | Herbal Medicines Product Database Committee (various national) | National-level herbal product standards | `needs_jurisdiction_specific_review` | Varies by country; must specify national authority |

**Critical rule:** Traditional/classical records, pharmacopeial/official monographs, and modern clinical evidence are three DISTINCT tiers. No cross-tier promotion is permitted (see Section 5).

### 2.4 Mechanistic/Safety Signal Sources

Mechanistic studies and safety signals are drawn from the same primary databases. Specific additional sources:

| Source ID | Name | Scope | Coverage Status | Notes |
|-----------|------|-------|-----------------|-------|
| `nih_ods` | NIH Office of Dietary Supplements Fact Sheets | Nutrient reference intakes, safety summaries | `active` | US-centric; authoritative for RDA/UL values |
| `examine` | Examine.com | Supplement research summaries, human-effect matrix | `active` for summary | Secondary source; links to primary studies; NOT a regulatory authority |
| `naturalmedicines` | Natural Medicines (Therapeutic Research Center) | Evidence-based supplement monographs, interactions | `active` | Subscription; professional-grade evidence ratings |
| `pubchem` | PubChem | Chemical compound data, safety data sheets | `active` | For chemical identity and safety data |
| `lactmed` | LactMed (NIH) | Drugs and lactation database | `active` | Specific to breastfeeding safety |

---

## 3. Regulatory Source Families

### 3.1 China

| Source ID | Authority | URL | Scope | Coverage Status | Key Documents |
|-----------|-----------|-----|-------|-----------------|---------------|
| `cn_samr` | State Administration for Market Regulation (SAMR) | https://www.samr.gov.cn | Health food registration/filing, product approvals | `active` | Health food registration certificates, filing notifications |
| `cn_nhc` | National Health Commission (NHC) | https://www.nhc.gov.cn | Food safety national standards (GB series), new food raw materials, health food raw material directory | `active` | GB standards, health food permitted ingredients catalogs |
| `cn_nmpa` | National Medical Products Administration (NMPA) | https://www.nmpa.gov.cn | Drug registration, pharmacopoeia | `active` | Drug registration certificates, pharmacopoeia editions |
| `cn_cp` | Chinese Pharmacopoeia Commission | via NMPA | Official pharmacopeial monographs (2020 edition: 5,911 monographs) | `active` | CP 2020 Vol I-IV |
| `cn_cfda_archived` | Former CFDA (now SAMR/NMPA) | Historical | Legacy approvals prior to institutional restructuring | `limited` | Historical registrations; replaced by SAMR/NMPA pathways |
| `cn_gbt` | GB/T and GB National Standards | Via SAC/NHC | Nutrient reference intakes, food additive standards | `active` | GB 14880 (food additives), Chinese DRIs |

**China coverage limitations:**
- Health food registration (保健食品注册) and filing (保健食品备案) are separate pathways.
- The "Blue Hat" (蓝帽子) registration is required for health function claims.
- "Drug-food dual-use" (药食同源) materials have a separate catalog maintained by NHC.
- Coverage status `active` means the authority exists and its scope is defined; it does NOT mean every ingredient has been assessed by this candidate.

### 3.2 United States

| Source ID | Authority | URL | Scope | Coverage Status | Key Documents |
|-----------|-----------|-----|-------|-----------------|---------------|
| `us_fda` | U.S. Food and Drug Administration | https://www.fda.gov | Food, dietary supplements, drugs, biologics | `active` | DSHEA (1994), 21 CFR Part 101/111, GRAS notices, NDI notifications |
| `us_fda_gras` | FDA GRAS Notification Program | https://www.fda.gov/food/food-ingredients-packaging/generally-recognized-safe-gras | GRAS self-determinations and FDA-acknowledged notifications | `active` | GRAS notice inventory |
| `us_fda_ndi` | FDA New Dietary Ingredient Notifications | https://www.fda.gov/food/food-ingredients-packaging/new-dietary-ingredient-ndi-notification-process | NDI pre-market notification for new dietary ingredients | `active` | NDI notification database |
| `us_nih_ods` | NIH Office of Dietary Supplements | https://ods.od.nih.gov | Fact sheets, RDA/AI/UL values | `active` | DRI tables |
| `us_usda` | USDA | https://www.usda.gov | Food composition, labeling | `active` | USDA FoodData Central |
| `us_ftc` | FTC | https://www.ftc.gov | Advertising claims for supplements | `active` | Truth-in-advertising enforcement |

**US coverage limitations:**
- DSHEA does NOT require pre-market approval for dietary supplements (unlike drugs).
- GRAS self-determination by manufacturers is NOT equivalent to FDA approval.
- An NDI notification is NOT an FDA approval; FDA may object or not respond.
- Structure/function claims require "significant scientific agreement" but differ from drug claims.
- `active` means the regulatory framework is documented, not that every ingredient is cleared.

### 3.3 European Union

| Source ID | Authority | URL | Scope | Coverage Status | Key Documents |
|-----------|-----------|-----|-------|-----------------|---------------|
| `eu_efsa` | European Food Safety Authority | https://www.efsa.europa.eu | Food safety, nutrient reference values, health claims evaluation | `active` | NDA Panel opinions, tolerable upper intake levels |
| `eu_ec` | European Commission | https://ec.europa.eu | Directive 2002/46/EC (food supplements), NHCR 1924/2006 | `active` | Food supplement directive, health claims regulation |
| `eu_ema` | European Medicines Agency | https://www.ema.europa.eu | Herbal medicinal products, HMPC monographs | `active` | Community herbal monographs, list entries |
| `eu_lex` | EUR-Lex | https://eur-lex.europa.eu | EU law texts | `active` | Regulations, directives, implementing decisions |

**EU coverage limitations:**
- The Nutrition and Health Claims Regulation (NHCR) 1924/2006 is the primary gate for health claims.
- Botanical health claims remain under "on hold" status for many substances (as of 2026).
- EU member states have divergent approaches to food supplement maximum levels.
- `active` means the legal framework exists and is documented.

### 3.4 Codex Alimentarius (International)

| Source ID | Authority | URL | Scope | Coverage Status | Key Documents |
|-----------|-----------|-----|-------|-----------------|---------------|
| `codex` | Codex Alimentarius Commission (FAO/WHO) | https://www.fao.org/fao-who-codexalimentarius | International food standards, guidelines | `active` | CXG 55-2005 (Guidelines for Vitamin and Mineral Food Supplements), GLVs |
| `codex_ccnfsdu` | CCNFSDU | via Codex | Nutrition and Foods for Special Dietary Uses | `active` | Work on supplement guidelines |

**Codex limitations:**
- Codex guidelines are voluntary; adoption depends on national implementation.
- CXG 55-2005 covers only vitamin and mineral supplements, not botanicals.

### 3.5 Other Jurisdictions

| Source ID | Authority | Coverage Status | Notes |
|-----------|-----------|-----------------|-------|
| `jp_mhlw` | Japan MHLW / Consumer Affairs Agency | `needs_jurisdiction_specific_review` | Foods for Specified Health Uses (FOSHU), Foods with Function Claims |
| `au_tga` | Australia TGA | `needs_jurisdiction_specific_review` | Listed medicines, complementary medicines |
| `kr_mfds` | South Korea MFDS | `needs_jurisdiction_specific_review` | Health functional foods |
| `ca_hc` | Canada Health Canada | `needs_jurisdiction_specific_review` | Natural Health Products Regulations |

> **Any jurisdiction not explicitly listed above is `uncovered`.** Do not assume clearance for unlisted markets. The `needs_jurisdiction_specific_review` status means the authority is known to exist but this candidate has not performed an ingredient-level assessment.

---

## 4. Source Reliability Hierarchy

For evidence assessment, sources are ranked:

| Tier | Source Type | Examples | Weight |
|------|------------|----------|--------|
| 1 | Systematic review / meta-analysis of RCTs | Cochrane reviews, published SR/MA | Highest |
| 2 | Large RCT (n>200, double-blind, placebo-controlled) | Published in indexed journals | High |
| 3 | Small RCT (n<200) or single-center | Published in indexed journals | Moderate |
| 4 | Controlled clinical trial (non-randomized) | Published | Lower |
| 5 | Animal study (in vivo) | Published, specified model | Informational only; no direct clinical proof |
| 6 | In vitro / mechanistic | Published | Informational only; no clinical proof |
| 7 | Traditional / classical record | Named source with edition | Historical/traditional record only; no clinical proof |
| 8 | Expert opinion / narrative review | Published or institutional | Weakest |

**Retraction caution:** Sources should be checked against retraction databases (e.g., PubMed retraction notices, Retraction Watch) where feasible.

---

## 5. TCM Evidence Tier Separation (No Cross-Tier Promotion)

| Tier | Description | Evidence Status |
|------|-------------|-----------------|
| T1 | Traditional/classical record (e.g., Shennong Bencao Jing, Bencao Gangmu) | Traditional use record only. NOT clinical efficacy evidence. |
| T2 | Official pharmacopeial/monograph (e.g., CP 2020, WHO monographs) | Official quality/identity standard. May include traditional indications. NOT clinical efficacy proof. |
| T3 | Modern TCM clinical research (RCTs, observational studies) | May support clinical efficacy if study quality is adequate. Assessed under human clinical evidence track. |

**Rule:** T1 and T2 records must NEVER be promoted to clinical efficacy proof. T3 evidence is assessed by the same quality hierarchy as non-TCM clinical evidence.

---

## 6. Adding New Jurisdictions or Sources

A new source family may be added to this registry only when ALL of the following are documented:
1. Authority name and official URL
2. Legal basis / enabling legislation
3. Scope (what product categories it covers)
4. Known limitations and gaps
5. Date of last verification

Until all five fields are complete, the jurisdiction/category is `uncovered` or `needs_jurisdiction_specific_review`.

---

## 7. Registry Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-07-15 | Initial candidate registry created for formula-global-evidence-regulatory-gate upgrade |
