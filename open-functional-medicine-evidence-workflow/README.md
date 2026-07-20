# Open Functional Medicine Workflow — v0.4.0 candidate

A non-web, conversation-native Skill candidate for two different needs:

1. **ordinary nutrition/health evidence questions** — answer directly from Skill knowledge plus freshly verified guidance, systematic reviews and RCTs;
2. **authorized individual case analysis** — organize messy case materials, screen red flags, generate a source-traceable functional medicine matrix and produce gated food, supplement, medical-nutrition or TCM plan drafts.

It does not make every question fill a case form.

## Example 1 — direct evidence answer

User: `What should I eat if I'm low on vitamin A?`

The Skill should:

- answer directly with food sources, preparation/pairing, cautions and when testing/professional assessment matters;
- verify current guidance and relevant human evidence;
- distinguish guideline, RCT/systematic-review, observational and mechanistic evidence;
- ask only a safety clarification that materially changes the answer;
- not generate a personal diagnosis or functional medicine matrix.

## Example 2 — case analysis

When the user supplies symptoms, labs, diagnoses, diet records, medications or an explicit personalized-plan request, the Skill:

1. confirms authorization, de-identification and minimum necessary use;
2. preserves source/date/uncertainty;
3. stops on red flags;
4. determines sufficiency separately for each requested output;
5. generates a non-diagnostic functional medicine matrix worksheet (no spokes or causal edges);
6. applies the relevant formula-class evidence and review gate;
7. returns a populated draft only when the gate passes, otherwise a useful scaffold and exact missing-data/reviewer list.

## Real local artifacts

The candidate includes a dependency-free generator:

```bash
python3 scripts/generate_functional_medicine_matrix.py INPUT.json OUTPUT_DIR
python3 scripts/generate_functional_medicine_matrix.py --include-svg INPUT.json OUTPUT_DIR
```

By default it creates:

- `functional_medicine_matrix.json`
- `functional_medicine_matrix.md` — complete non-web/text matrix
- `functional_medicine_matrix_manifest.json`

The optional `--include-svg` flag adds `functional_medicine_matrix.svg`. The SVG is standalone/responsive and uses no remote resources, JavaScript or spokes. The Markdown file is the complete non-web/text equivalent and is the default human-facing deliverable. The manifest is written last and binds exact file hashes only for files actually emitted; consumers reject a mixed/incomplete bundle. Every item and link requires provenance and uncertainty. The functional medicine matrix is not an official or proprietary branded diagnostic instrument.

## Four plan classes

| Class | What may be populated | Required boundary |
|---|---|---|
| food/lifestyle | foods, quantities, recipes, preparation, substitutions | allergy/intolerance, major medical restriction and user preference/access check |
| supplement | ingredient/form, amount, schedule, monitoring | indication, identity, evidence, medication/supplement interaction, pregnancy/allergy/organ-function considerations and qualified review |
| medical nutrition | appropriate oral/MNT/enteral product/route/amount/schedule draft | clinical data and clinical nutrition review; IV/parenteral is escalation only |
| TCM formula | formula composition and dose | explicit syndrome differentiation, complete herb identity, contraindication/interaction review, evidence status and TCM practitioner approval |

When a material gate is missing, the output remains an unpopulated scaffold. There is no guessed “safe default” dose.

## Model assistance

Model assistance is optional and untrusted. The candidate adds:

- minimum-necessary, de-identified structured projection;
- untrusted-data delimiting;
- strict schema plus output-type/release-status semantic validation;
- citation and provenance checks;
- adversarial tests for injection, leakage, fabricated citations, unsafe formulas and malformed JSON;
- deterministic local fallback when model output fails.

Human-facing artifacts remove secrets, private paths and prompt internals but retain honest AI-assistance, evidence and reviewer-status disclosure.

## What is intentionally not implemented

- no longitudinal history/version/current-projection feature;
- no generic staged conversation state machine;
- no mandatory structured intake for an ordinary question;
- no autonomous final diagnosis, medication action, care execution or IV/parenteral formulation;
- no official or proprietary branded-instrument claim;
- no clinical-validation or certified-PHI-platform claim.

## Key files

- `SKILL.md` — hub and routing
- `reference/invocation-and-evidence-routing.md` — direct question vs case route
- `reference/evidence-governance.md` — evidence verification/governance
- `reference/formula-evidence-contract.md` — formula evidence fields
- `reference/formula-class-gates.md` — four distinct release gates
- `reference/functional-medicine-matrix-contract.md` — item/link/provenance contract
- `reference/model-io-and-output-validation.md` — model trust boundary
- `reference/output-contract.md` — output types and statuses
- `assets/*template*` — direct-question, intake, case, matrix, formula and review templates
- `scripts/generate_functional_medicine_matrix.py` — local JSON+Markdown matrix generation, with optional SVG
- `scripts/validate_candidate.py` — structural/safety validator

## Current status

This directory is the parent-reviewed English publication package for the Skill. Publication does not mean that it is installed, clinically validated, or approved for autonomous clinical use. The package remains a governed evidence-and-draft workflow whose outputs require the review stated in each route and formula-class contract.
