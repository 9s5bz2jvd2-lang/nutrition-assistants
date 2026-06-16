# Route Log Template — loop-engineering

After a serious loop-design or evaluation session, record:

```yaml
task_summary: <one line>
mode: <quick | normal | design | danger_check | full_redesign>
selected_experts: <list>
skipped_experts: <list>
sweep_items_checked: <list>
sweep_hits: <list>
budget_tier: <shared_core | routed | heavy>
output_artifacts: <list>
followup_needed: <yes/no + details>
```

## Route log examples

### Example 1: Morning triage loop design

```yaml
task_summary: "Design a daily triage loop for a Node.js monorepo"
mode: design
selected_experts: [primitives, loop-design-pattern]
skipped_experts: [dangers]
sweep_items_checked: [maker_checker_split, verification_gate, state_on_disk]
sweep_hits: ["missing verification sub-agent — added to design"]
budget_tier: routed
output_artifacts: ["loop-design.md with checklist"]
followup_needed: "yes — need to add skills for build steps and test commands"
```

### Example 2: Unattended loop danger check

```yaml
task_summary: "Evaluate an overnight loop that auto-merges PRs"
mode: danger_check
selected_experts: [dangers, eval-cases]
skipped_experts: [loop-design-pattern]
sweep_items_checked: [verification_gate, comprehension_debt, cognitive_surrender, maker_checker]
sweep_hits: ["no verification gate", "no human review before merge", "cognitive surrender risk HIGH"]
budget_tier: routed
output_artifacts: ["danger-report with 3 red flags"]
followup_needed: "yes — loop must be paused until verification gate is added"
```
