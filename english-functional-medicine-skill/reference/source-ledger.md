# Source Ledger

> **Purpose.** Central registry of every external source used in this
> workflow. Each entry documents provenance, rights classification,
> the specific claim it supports, and the reproduction boundary.

---

## Ledger Schema

Each entry uses the following fields:

| Field | Description |
|---|---|
| `id` | Unique source identifier, formatted `[S##]` |
| `title` | Document or page title |
| `owner` | Publishing organization or author |
| `url` | URL or PMID/DOI |
| `retrieved` | Date of retrieval (YYYY-MM-DD) |
| `verified` | How the URL/access was verified at retrieval time |
| `rights_class` | One of: `US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE`, `OPEN_LICENSE_VERIFIED`, `CITATION_ONLY`, `UNKNOWN_DO_NOT_REPRODUCE` |
| `supports` | Specific claim or role this source supports in the workflow |
| `allowed_use` | How this source may be used (cite, link, summarize, etc.) |
| `reproduction_boundary` | What may NOT be reproduced from this source |

---

## Entries

### [S01] Complementary, Alternative, or Integrative Health: What's In a Name?

| Field | Value |
|---|---|
| **id** | S01 |
| **title** | Complementary, Alternative, or Integrative Health: What's In a Name? |
| **owner** | National Center for Complementary and Integrative Health (NCCIH), NIH |
| **url** | https://www.nccih.nih.gov/health/complementary-alternative-or-integrative-health-whats-in-a-name |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from nccih.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Definitions of complementary and integrative health approaches; whole-person health concept; scope of NCCIH mission. Used in scope-and-red-lines §1 and source context. |
| **allowed_use** | Link; summarize key definitions in original words. |
| **reproduction_boundary** | No reproduction of full paragraphs; keep quotations under 25 words. |

---

### [S02] Dietary Supplement Fact Sheets — NIH Office of Dietary Supplements

| Field | Value |
|---|---|
| **id** | S02 |
| **title** | Dietary Supplement Fact Sheets (collection) |
| **owner** | Office of Dietary Supplements (ODS), NIH |
| **url** | https://ods.od.nih.gov/factsheets/list-all/ |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible index page from ods.od.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Evidence-based information on vitamins, minerals, herbs, probiotics; used to verify specific nutrient roles and recommended amounts. Referenced in evidence-and-uncertainty §5. |
| **allowed_use** | Link; cite specific fact sheet titles and key data points. |
| **reproduction_boundary** | No bulk reproduction of fact sheet content; no tables reproduced verbatim. |

---

### [S03] Office of Dietary Supplements — Information for Health Professionals

| Field | Value |
|---|---|
| **id** | S03 |
| **title** | Information for Health Professionals |
| **owner** | Office of Dietary Supplements (ODS), NIH |
| **url** | https://ods.od.nih.gov/HealthInformation/healthprofessional.aspx |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from ods.od.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Health-professional resources for dietary supplement evidence; guidance on evaluating supplement claims. |
| **allowed_use** | Link; summarize professional guidance points. |
| **reproduction_boundary** | No full-page reproduction. |

---

### [S04] Dietary Supplements Guidance Documents & Regulatory Information — FDA

| Field | Value |
|---|---|
| **id** | S04 |
| **title** | Dietary Supplements Guidance Documents & Regulatory Information |
| **owner** | U.S. Food and Drug Administration (FDA) |
| **url** | https://www.fda.gov/food/guidance-documents-regulatory-information-topic-food-and-dietary-supplements/dietary-supplements-guidance-documents-regulatory-information |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from fda.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Regulatory framework for dietary supplements; legal distinction between supplements and drugs; structure/function claims vs. health claims. Used in scope-and-red-lines §2 and output-contract §7. |
| **allowed_use** | Link; cite regulatory distinctions in original language. |
| **reproduction_boundary** | No reproduction of full guidance documents. |

---

### [S05] Label Claims for Food & Dietary Supplements — FDA

| Field | Value |
|---|---|
| **id** | S05 |
| **title** | Label Claims for Food & Dietary Supplements |
| **owner** | U.S. Food and Drug Administration (FDA) |
| **url** | https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/label-claims-food-dietary-supplements |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from fda.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Distinction between health claims, nutrient content claims, and structure/function claims on supplement labels; relevance to what this workflow must NOT claim. |
| **allowed_use** | Link; summarize claim categories. |
| **reproduction_boundary** | No reproduction of full regulatory text or tables. |

---

### [S06] Evaluating Health Information — MedlinePlus

| Field | Value |
|---|---|
| **id** | S06 |
| **title** | Evaluating Health Information |
| **owner** | U.S. National Library of Medicine (NLM), NIH |
| **url** | https://medlineplus.gov/evaluatinghealthinformation.html |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from medlineplus.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Criteria for evaluating reliability of health information sources; used to inform evidence-appraisal approach in evidence-and-uncertainty §5. Also supports intake context collection per general health assessment. |
| **allowed_use** | Link; cite evaluation criteria in original words. |
| **reproduction_boundary** | No full-page reproduction. |

---

### [S07] Using Dietary Supplements Wisely — NCCIH

| Field | Value |
|---|---|
| **id** | S07 |
| **title** | Using Dietary Supplements Wisely |
| **owner** | National Center for Complementary and Integrative Health (NCCIH), NIH |
| **url** | https://www.nccih.nih.gov/health/using-dietary-supplements-wisely |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from nccih.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Safety considerations for dietary supplements; cautions about supplement use; information relevant to intake section C. Used in scope-and-red-lines for safety guidance. |
| **allowed_use** | Link; summarize safety cautions in original words. |
| **reproduction_boundary** | No full-page reproduction; no tables reproduced verbatim. |

---

### [S08] Dietary and Herbal Supplements — NCCIH

| Field | Value |
|---|---|
| **id** | S08 |
| **title** | Dietary and Herbal Supplements |
| **owner** | National Center for Complementary and Integrative Health (NCCIH), NIH |
| **url** | https://www.nccih.nih.gov/health/dietary-and-herbal-supplements |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from nccih.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Interaction risks between supplements and medications; surgical considerations; general caution guidance for supplement use. |
| **allowed_use** | Link; cite interaction cautions. |
| **reproduction_boundary** | No full-page reproduction. |

---

### [S09] Herb-Drug Interactions — NCCIH Provider Digest

| Field | Value |
|---|---|
| **id** | S09 |
| **title** | Herb-Drug Interactions |
| **owner** | National Center for Complementary and Integrative Health (NCCIH), NIH |
| **url** | https://www.nccih.nih.gov/health/providers/digest/herb-drug-interactions |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from nccih.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Safety concerns about drug interactions, direct toxicities, and contamination risks with dietary and herbal supplements. Used in intake-and-triage and evidence-and-uncertainty for interaction-awareness. |
| **allowed_use** | Link; summarize key safety points. |
| **reproduction_boundary** | No full-page reproduction; no clinical case examples reproduced. |

---

### [S10] Supplements and Medications Can Interact — NIH MedlinePlus Magazine

| Field | Value |
|---|---|
| **id** | S10 |
| **title** | Did you know? Supplements and medications can interact in unexpected ways |
| **owner** | NIH MedlinePlus Magazine |
| **url** | https://magazine.medlineplus.gov/article/did-you-know-supplements-and-medications-can-interact-in-unexpected-ways |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible article from magazine.medlineplus.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Consumer/professional education on supplement-medication interactions; links to NCCIH "Know the Science" resource. |
| **allowed_use** | Link; cite interaction education points. |
| **reproduction_boundary** | No full-article reproduction. |

---

### [S11] Cochrane — Systematic Reviews in Healthcare

| Field | Value |
|---|---|
| **id** | S11 |
| **title** | Cochrane (organization homepage) |
| **owner** | Cochrane |
| **url** | https://www.cochrane.org/ |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from cochrane.org |
| **rights_class** | CITATION_ONLY |
| **supports** | Role of systematic reviews in evidence hierarchy; context for how evidence strength is assessed in this workflow. |
| **allowed_use** | Cite by name and URL only; no content reproduction. |
| **reproduction_boundary** | No abstracts, full text, tables, or figures from any Cochrane review. |

---

### [S12] PubMed — Biomedical Literature Database

| Field | Value |
|---|---|
| **id** | S12 |
| **title** | PubMed |
| **owner** | National Center for Biotechnology Information (NCBI), NLM, NIH |
| **url** | https://pubmed.ncbi.nlm.nih.gov/ |
| **retrieved** | 2026-07-17 |
| **verified** | Web search returned accessible page from pubmed.ncbi.nlm.nih.gov |
| **rights_class** | US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE |
| **supports** | Database for verifying peer-reviewed literature citations (PMID lookup). Used as verification tool, not content source. |
| **allowed_use** | Link; cite as lookup tool. |
| **reproduction_boundary** | No abstracts or full text reproduced. |

---

## Notes

- All sources were retrieved on 2026-07-17 by the Skill author; the 12 listed URLs were access-rechecked successfully on 2026-07-20 before this public release.
- Government (.gov) sources are generally in the US public domain but
  may contain third-party elements with separate rights. Each is
  classified as `US_GOV_PUBLIC_DOMAIN_OR_CHECK_NOTICE` to flag that
  page-level rights notices should be checked before republication.
- `CITATION_ONLY` sources may not be reproduced at all; bibliographic
  citation (author, title, URL, date) is the only permitted use.
- Peer-reviewed articles retrieved via PubMed/Crossref are verified
  by PMID/DOI but classified as `CITATION_ONLY` unless the specific
  open-license status is confirmed.
- Before this public release, the maintainer checked the subtree for copied source paragraphs, tables, figures and case examples and found none. The conservative rights classes and reproduction boundaries still apply. This ledger and screening are not a legal opinion or legal clearance.
