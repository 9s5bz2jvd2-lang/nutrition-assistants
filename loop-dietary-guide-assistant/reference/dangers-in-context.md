# Dangers in Context — Loop Engineering Risks Applied to Dietary Guidance

The three dangers from Loop Engineering become **more specific and more consequential** when the loop is dispensing dietary advice instead of code.

---

## 1. Verification Debt → Dangerous Nutrition Claims

### What it is
A dietary loop running unattended is also a loop making **nutrition claims** unattended. The maker-checker split makes the loop's "this advice is correct" mean something — but even then, "verified" is a claim, not a proof.

### Why it's worse in dietary context
- A code bug can be fixed. A dangerous dietary recommendation given to a pregnant woman can't be undone.
- The stakes are asymmetric: a false negative (missing a safety flag) can harm; a false positive (being overly cautious) merely inconveniences.
- "Close enough" in nutrition is not good enough. Adult sodium limits applied to a child are dangerous.

### Dietary-specific mitigation
- [ ] Maker-checker split enforced for every VERIFY-category question
- [ ] Checker runs the full safety checklist (life stage, alcohol, medical boundary, quantitative accuracy)
- [ ] Max 2 revision cycles before escalation
- [ ] Human reviews all ESCALATE-category items before they're answered
- [ ] Weekly compliance audit: re-check a sample of published answers

### Red flag
> If the loop says "verified" and no human checked the safety boundaries for a special population, it isn't verified — it's unconfirmed.

---

## 2. Comprehension Debt → Knowledge Gap About What the Loop Advised

### What it is
The more dietary advice the loop dispenses, the bigger the gap between what was advised and what the human operator actually understands about the advice being given.

### Why it's worse in dietary context
- The operator may not notice that the loop has been giving advice that subtly drifts from the Guidelines (e.g., gradually simplifying alcohol guidance)
- New guidelines or evidence may emerge without the operator noticing the loop is using stale skills
- The loop may be handling questions about populations the operator didn't intend

### Dietary-specific mitigation
- [ ] Weekly review of all advice given (at minimum a random sample)
- [ ] State file includes a "drift log" — any deviation from Guidelines must be recorded
- [ ] Monthly skill refresh check: are the Guidelines still current?
- [ ] The operator must be able to explain the last significant piece of advice the loop gave

### Red flag
> If you can't explain what dietary advice the loop gave yesterday and why, you have comprehension debt — and it's accumulating in a domain where the stakes are health.

---

## 3. Cognitive Surrender → "The Loop Knows Best" About Nutrition

### What it is
When the loop runs itself smoothly, it's very tempting to stop having an opinion about dietary advice and just accept whatever the loop produces.

### Why it's the most dangerous in dietary context
- In coding, cognitive surrender leads to bad software. In nutrition, cognitive surrender can lead to **harmful health advice reaching vulnerable populations**.
- The loop doesn't know that a user is pregnant unless the user says so. The loop doesn't know a claim is outdated unless someone checks. The loop doesn't know the difference between "safe" and "verified" — it only knows what the checker reports.
- **The same loop giving safe answers to adults can give dangerous answers to children if the life-stage check is skipped once.**

### Dietary-specific mitigation
- [ ] Maintain independent judgment about whether the loop's dietary advice is safe
- [ ] Disagree with the loop when it's wrong (and verify that you can tell)
- [ ] Never let the loop answer ESCALATE-category questions without human review
- [ ] Regularly test: "If the loop were wrong about [X], would I notice?"
- [ ] Never trust the loop more than the Guidelines it was built on

### Red flag
> If you approve every piece of dietary advice the loop produces without reading it, you're not a nutrition supervisor — you're a rubber stamp. And rubber stamps don't protect special populations.

---

## The Unifying Pattern (Dietary Context)

| Danger | What the loop does | What you must do | Dietary-specific stakes |
|---|---|---|---|
| **Verification debt** | Ships advice faster than you confirm | Confirm it's safe yourself | Wrong advice → health risk |
| **Comprehension debt** | Generates advice you didn't review | Read and understand what it advised | Drift from Guidelines → misguidance |
| **Cognitive surrender** | Runs itself without your input | Maintain independent judgment | Unchecked loop → vulnerable populations harmed |

---

## When to worry (dietary-specific)

You should be especially vigilant when:
- The loop has answered questions about infants, children, or pregnant/lactating women without explicit human review
- The last 5+ dietary advice responses were published without a human reading the checker's notes
- The loop's advice about alcohol doesn't distinguish between official and uncompromised positions
- You can't explain the last dietary claim the loop verified
- The loop has been running unattended for >1 day without anyone checking the state file
- The loop says a food is "safe" or "recommended" without citing a specific Guideline
