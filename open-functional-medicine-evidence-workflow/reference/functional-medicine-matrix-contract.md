# Functional Medicine Matrix Contract

## Purpose

Generate a real, standalone functional-medicine matrix worksheet and companion data/report from a normalized, source-grounded case state. The default user-facing worksheet is the complete Markdown text matrix; generate the standalone SVG rendering only after an explicit image/SVG/diagram request. The artifact is an organizational and completeness view, not an official or proprietary branded instrument, not a diagnostic score, and not causal proof.

## Fixed layout

The matrix is **not a graph**.

- **Left:** three ATM story sections — `antecedent` (Antecedents/predispositions), `trigger` (Triggering events), `mediator` (Mediators/perpetuators).
- **Center/right:** exactly seven physiological systems in fixed spatial positions:
  1. `assimilation`
  2. `defense_and_repair`
  3. `structural_integrity`
  4. `energy`
  5. `communication`
  6. `transport`
  7. `biotransformation_and_elimination`
- **Center:** MES = `Mental · Emotional · Spiritual`. It is its own center, **not** an eighth physiological system/domain.
- **Bottom:** five lifestyle pillars — `sleep`, `movement`, `nutrition`, `stress`, `relationships`.
- **No spokes, edges or system-to-system lines** in the SVG.

## Input schema

Top-level keys (exact set):

```json
{
  "schema_version": "2.0",
  "language": "en",
  "case_key": "safe-id",
  "generated_at": "ISO-ish text",
  "items": [...],
  "lifestyle": {"sleep":[], "movement":[], "nutrition":[], "stress":[], "relationships":[]},
  "links": [...],
  "flags": {"red_flags":[], "safety_concerns":[], "missing_data":[], "uncertainty_notes":[]},
  "review": {"status": "draft|reviewed|rejected|incomplete", "reviewer_role": "text"}
}
```

Item keys (exact set):

- `id`, `text`, `provenance`, `period`, `domains`, `mes`, `story_role`, `certainty`, `contradictions`.
- `domains` contains only the seven system IDs; `mindbody` is rejected.
- `mes` is a boolean indicating central MES membership.
- `story_role` is one of `antecedent`, `trigger`, `mediator`, `unclassified`.

Link keys (exact set):

- `id`, `source_item_ids`, `domains`, `relation_type`, `provenance`, `evidence_refs`, `uncertainty`, `contradictions`, `reviewer_status`.
- `reviewer_status` is one of `unreviewed`, `accepted`, `revised`, `rejected`, `disputed`.

## Per-item contract

Every item must include a stable ID, bounded text, provenance, period, zero or more system assignments, MES flag, story role, certainty, and contradictions/alternatives. Do not silently upgrade reported information to verified information. Do not invent missing items.

## Relationship contract

Every link must include source item IDs, systems, relation type, evidence references, uncertainty, alternatives/contradictions and reviewer status. Allowed relationship types:

- `temporal_precedes`
- `co_occurs`
- `possible_influence`
- `shared_context`
- `contradicts`
- `unknown`

`possible_influence` is a hypothesis label, never a causal conclusion. Links are listed as candidate hypotheses in JSON/Markdown; they are **not drawn as edges or spokes** in the matrix image.

## Coverage

Coverage is the number of physiological systems containing at least one item. It measures documentation completeness only. It must never be styled or described as severity, disease burden, causal weight, risk score or treatment priority.

## Required files

A successful default invocation writes the text matrix bundle:

- `functional_medicine_matrix.json`
- `functional_medicine_matrix.md` — complete text-equivalent worksheet (default human-facing deliverable)
- `functional_medicine_matrix_manifest.json` (written last; exact file hashes must match)

An explicit `--include-svg` opt-in adds `functional_medicine_matrix.svg` to the bundle. The manifest lists only the files actually emitted; consumers reject a bundle whose manifest file set does not match the files present. PNG, PDF and HTML are outside this release contract.

## Rendering and safety

- static SVG only; no JavaScript, remote font, remote image, iframe or external resource;
- no `<line>` elements (no spokes/edges);
- XML/Markdown escaping is mandatory;
- deterministic ordering and bytes for identical input;
- malformed or unknown fields fail closed without overwriting prior good files;
- fixed worksheet labels are English; dynamic user-supplied Unicode text is preserved and escaped, not machine-translated;
- every artifact repeats the non-diagnostic boundary and AI/reviewer disclosure;
- manifest is written last; consumers reject the bundle if any listed file hash differs.
