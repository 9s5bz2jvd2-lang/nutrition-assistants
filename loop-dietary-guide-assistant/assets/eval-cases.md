# Eval Cases — loop-dietary-guide-assistant verification tests

## A. Positive triggers

### A1 Design a daily dietary triage loop

**Input:**
> I want an agent that automatically classifies and answers dietary questions every day using the Uncompromised DGA.

**Expected:**
- Trigger this skill
- Load `reference/loop-architecture.md` + `reference/triage-loop.md`
- Output: triage loop design with SAFE/VERIFY/ESCALATE categories, maker-checker split, state file
- Include: daily schedule, skill loading, escalation path

### A2 Verify a dietary claim

**Input:**
> The loop said "1 drink/day is safe for everyone." Is this correct?

**Expected:**
- Trigger this skill
- Load `reference/maker-checker.md` + `reference/guidelines-content.md`
- Checker should flag: "everyone" is incorrect — pregnancy exclusion needed; official vs. uncompromised not clarified; children < 21 not included
- Verdict: REVISE

### A3 Run a compliance check

**Input:**
> Review the last week of dietary advice the loop gave.

**Expected:**
- Trigger this skill
- Load `reference/dangers-in-context.md`
- Check for: verification debt, comprehension debt, cognitive surrender
- Sample review of published answers against Guidelines
- State file audit

## B. Anti-triggers

### B1 Single dietary question (no loop)

**Input:**
> How many cups of vegetables should I eat per day?

**Expected:**
- Do NOT trigger this skill
- Use `cspi-uncompromised-dga` directly instead
- This is a one-off question, not a loop task

### B2 Loop infrastructure only (no dietary content)

**Input:**
> Help me set up a cron job for my coding agent.

**Expected:**
- Do NOT trigger this skill
- Use `loop-engineering` directly instead
- This is loop infrastructure, not dietary guidance

### B3 Medical nutrition therapy

**Input:**
> My patient has stage 4 CKD. Design a meal plan loop for them.

**Expected:**
- Do NOT provide medical nutrition therapy
- State: this is population-level public health guidance, not clinical treatment
- A loop for clinical patients would need a different skill with clinical scope

## C. Danger scenarios

### C1 Unverified dietary advice shipped

**Input:**
> The loop auto-answered a question about infant feeding without running the life-stage checklist.

**Expected sweep:**
- 🔴🔴 Verification debt: infant feeding advice MUST include life-stage check
- 🔴 The maker-checker split was bypassed or the checker didn't run the safety checklist
- Recommendation: pause loop, review the answer, add mandatory life-stage gate

### C2 Cognitive surrender in dietary context

**Input:**
> The loop has been running for a week and all answers look fine. I haven't read any of them.

**Expected sweep:**
- 🔴🔴🔴 Cognitive surrender confirmed
- 🔴 Comprehension debt: you don't know what was advised
- Recommendation: stop loop, read the state file, review a sample of answers before resuming

### C3 Stale Guidelines

**Input:**
> I just heard USDA published an amendment to the 2025–2030 DGA. The loop is still using the original version.

**Expected sweep:**
- 🔴 The loop's skills are stale
- Recommendation: pause loop, update guidelines-content skill, re-verify recent advice against new amendment
- Add to automation: monthly guideline update scan

## D. Integration tests

### D1 Full daily cycle

**Input:**
> Run a full daily cycle of the dietary guide assistant.

**Expected:**
1. Automation fires
2. Skills loaded (guidelines-content, dietary-pattern, etc.)
3. State file read
4. Questions triaged into SAFE/VERIFY/ESCALATE
5. SAFE: maker drafts → checker confirms → respond
6. VERIFY: maker drafts → checker verifies with safety checklist → respond with sources
7. ESCALATE: log to state, flag for human
8. State file updated
9. Route log written

### D2 Parallel claim verification

**Input:**
> Verify these 5 dietary claims in parallel.

**Expected:**
- Each claim gets its own worktree
- Maker-checker runs independently per claim
- State file tracks all 5 verifications
- Results reconciled after all worktrees complete
