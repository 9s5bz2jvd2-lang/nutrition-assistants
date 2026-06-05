# outline-design

Design the target skill before extraction. A book’s table of contents is a clue, not the final architecture.

## Design questions

- What human/agent task should trigger this skill?
- What should be explicitly excluded?
- What is the primary routing axis: phase, issue, document type, jurisdiction, persona, or risk severity?
- Which parts belong in `SKILL.md` as router vs. `reference/` as depth?
- Which templates/assets/scripts would let an agent act rather than merely read?
- What facts or law must be refreshed outside the source?
- What validation prompts will prove the skill works?

## Agent-native architecture patterns

| Source type | Useful architecture |
|---|---|
| professional manual | workflow router + issue modules + templates |
| legal/tax/accounting treatise | issue taxonomy + current-law verification map + report patterns |
| software manual | task router + command recipes + troubleshooting tree |
| academic monograph | concept map + method cards + citation graph |
| policy handbook | eligibility decision tree + evidence checklist + exception handling |

## Progressive disclosure rule

The first loaded file should be small and decisive. It should tell the agent which deeper file to load next. Put depth where the agent can request it by topic; avoid giant “all knowledge” files.

## Rewrite unit selection

Pick units by how an agent will use them, not by chapter length. A 90-page chapter may need many issue leaves; a 6-page chapter may be one checklist. Repeated book schemas should become reusable module templates.
