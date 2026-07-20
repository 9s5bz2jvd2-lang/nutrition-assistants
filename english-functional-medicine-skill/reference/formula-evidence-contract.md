# Formula Evidence Contract

## Principle

Evidence is multidimensional. Do not collapse design, quality, directness, precision, population fit, formulation, range, duration, outcome validity, safety and regulatory status into one scalar tier.

## Evidence lanes

Every source belongs to one lane for the claim being assessed:

- `human_guideline_or_consensus`
- `human_systematic_review`
- `human_randomized_trial`
- `human_nonrandomized_or_observational`
- `human_safety_or_pharmacokinetic`
- `case_report_or_safety_signal`
- `animal_in_vivo`
- `mechanism_in_vitro`
- `traditional_classical_record`
- `official_identity_or_quality_standard`
- `regulatory_record`
- `secondary_summary`
- `bibliographic_only`
- `unverified_lead`

These are source types, not a universal rank.

## Required claim record

Each substantive claim or proposed ingredient/range carries:

- source ID and stable identifier;
- source lane;
- verification/full-text state;
- study design and risk-of-bias notes;
- population, intervention/form/range, duration and outcome;
- directness and applicability;
- precision, consistency and contradictions;
- retraction/correction/currentness check;
- exact claim supported;
- allowed claim strength;
- limitations and evidence debt.

## Anti-laundering rules

- animal findings do not establish human efficacy, safety or range;
- mechanism does not establish efficacy, diagnosis or clinical range;
- traditional/classical use does not establish clinical efficacy;
- official identity/quality standards do not establish efficacy;
- regulatory permission does not establish efficacy;
- clinical evidence does not establish marketing authorization;
- population evidence does not prove an individual response;
- absence of evidence does not establish safety;
- a scoped zero-result search does not prove non-existence;
- case narratives may define test failures but never establish efficacy or range.

## Range and dose states

Every proposed range uses one state:

- `human_evidence_derived`
- `current_guideline_derived`
- `population_reference_not_a_prescription`
- `qualified_practice_range_with_source`
- `NOT_DERIVABLE`

Forbidden states include animal-scaled, mechanism-extrapolated, unsourced traditional amount and copied old case/table amount.

## Source registry fields

Authority, access and currentness are separate:

- authority/scope;
- access state: `available_now`, `paywalled_or_subscription`, `unavailable`, `not_checked`;
- last verified date;
- version/edition;
- limitations.

Never call a source locally active merely because it exists. Do not hard-code a pharmacopoeia edition, legal status, monograph count or market rule without current primary-source verification.

## Search ledger

Log every attempt, including zero results and access failure: query, source, date, lane, result count when known, selected sources, access state, outcome and limitations. Search snippets are discovery leads only.
