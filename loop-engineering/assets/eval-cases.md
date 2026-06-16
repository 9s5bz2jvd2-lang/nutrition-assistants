# Eval Cases — loop-engineering verification tests

## A. Positive triggers

### A1 Design an autonomous coding-agent loop

**Input:**
> I want my coding agent to automatically triage issues and draft fixes every morning.

**Expected:**
- Trigger this skill
- Load `reference/primitives.md` (automations, sub-agents, state) + `reference/loop-design-pattern.md`
- Output: a loop design with cadence, skill, maker-checker split, state file, and escalation path

### A2 Evaluate an existing loop

**Input:**
> My loop runs nightly but I keep finding bugs it missed. What's wrong?

**Expected:**
- Trigger this skill
- Load `reference/dangers.md` + `reference/primitives.md` (sub-agents section)
- Check: maker-checker split present? Verification gate? Separate model for stop condition?

### A3 Scale parallel agents

**Input:**
> I want to run 5 agents in parallel on the same repo.

**Expected:**
- Trigger this skill
- Load `reference/primitives.md` (worktrees) + `reference/loop-design-pattern.md` (scaling rules)
- Warn about orchestration tax: review bandwidth is the ceiling, not the tool
- Recommend worktree per agent + token budget for sub-agents

## B. Anti-triggers

### B1 Simple one-shot code generation

**Input:**
> Write a function that checks if a number is prime.

**Expected:**
- Do NOT trigger this skill
- This is a simple single prompt — no loop needed

### B2 Article summary

**Input:**
> Summarize the Loop Engineering article for me.

**Expected:**
- Do NOT trigger this skill
- Use a summary tool or provide directly; loop engineering is about operational design, not reading comprehension

### B3 No agent involved

**Input:**
> Help me set up a CI pipeline for my project.

**Expected:**
- Do NOT trigger this skill
- This is DevOps tooling, not coding-agent loop design

## C. Danger scenarios

### C1 Unattended loop without verification

**Input:**
> I set up a loop that merges PRs automatically when tests pass.

**Expected sweep:**
- 🔴 Verification debt: who confirms the code works beyond tests?
- 🔴 Cognitive surrender: is anyone reviewing?
- Recommendation: add a human review gate before merge, or at minimum a separate verifier sub-agent

### C2 Loop running for days without human input

**Input:**
> My loop has been running overnight for 3 days and everything looks fine.

**Expected sweep:**
- 🔴 Comprehension debt: have you read what it produced?
- 🔴 Cognitive surrender: "looks fine" without reading is surrender
- Recommendation: schedule a review session; read the last N PRs

### C3 Speed over understanding

**Input:**
> The loop ships so fast now, I don't even need to understand the codebase anymore.

**Expected sweep:**
- 🔴🔴🔴 Cognitive surrender confirmed
- Recommendation: stop the loop, read what it shipped, rebuild comprehension before resuming

## D. Budget tests

### D1 Simple loop question

**Input:**
> What's the difference between /loop and /goal?

**Expected:**
- Load SKILL.md + one expert (primitives.md automations section)
- Route cost very low
- Direct answer: `/loop` = recurring cadence, `/goal` = run until condition true

### D2 Full loop design

**Input:**
> Design a complete autonomous loop for my team's morning triage.

**Expected:**
- Load shared core + primitives + loop-design-pattern + dangers
- Staged output: boundary → primitives → checklist → danger check
- Route log produced
