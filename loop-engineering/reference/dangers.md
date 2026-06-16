# The Three Dangers — What the Loop Still Does Not Do for You

The loop changes the work; it does not delete you from it. Three problems actually get **sharper** as the loop gets better, not easier.

---

## 1. Verification Debt

### What it is
A loop running unattended is also a loop making mistakes unattended. The whole reason you split the verifier sub-agent from the maker is to make the loop's "it's done" mean something — and even then, **"done" is a claim and not a proof**.

### Why it gets sharper
The faster the loop ships, the more tempting it is to skip verification. Smooth loops make verification feel optional.

### Mitigation checklist
- [ ] Every unattended loop has a verification sub-agent (maker ≠ checker)
- [ ] The `/goal` stop condition is checked by a separate model
- [ ] Human reviews critical changes before merge
- [ ] "Your job is to ship code you confirmed works" — not code the loop claims works

### Red flag
> If the loop says "done" and nobody checked, it isn't done — it's unconfirmed.

---

## 2. Comprehension Debt

### What it is
The faster the loop ships code you did not write, the bigger the gap between what exists and what you actually understand. This is **comprehension debt**, and a smooth loop just makes it grow faster unless you read what the loop made.

### Why it gets sharper
The smoother the loop, the less you feel the need to read the output. But "the agent wrote it" is not the same as "I understand it."

### Mitigation checklist
- [ ] Review loop output regularly (daily? per-PR?)
- [ ] Read the code the loop wrote, not just the PR description
- [ ] Maintain mental model of the codebase that includes loop-generated changes
- [ ] Track comprehension debt like technical debt: when it accumulates, slow down and read

### Red flag
> If you can't explain what the loop changed and why, you have comprehension debt.

---

## 3. Cognitive Surrender

### What it is
When the loop runs itself, it's very tempting to stop having an opinion and just take whatever it gives back. The author calls this **cognitive surrender**.

### Why it's the most dangerous
Designing the loop is the **cure** when you do it with judgement, and the **accelerant** when you do it to avoid thinking. Same action, opposite result.

> Two people can build the exact same loop and get completely opposite results. One uses it to move faster on work they understand deeply. The other uses it to avoid understanding the work at all. The loop doesn't know the difference. You do.

### Mitigation checklist
- [ ] Maintain independent judgment about code quality
- [ ] Disagree with the loop when it's wrong (and verify that you can tell)
- [ ] Do not let speed replace understanding
- [ ] Ask: "If the loop were wrong, would I notice?" If the answer is no, you've surrendered.

### Red flag
> If you approve every loop output without reading it, you're not engineering — you're pressing "go."

---

## The Unifying Pattern

| Danger | What the loop does | What you must do |
|---|---|---|
| **Verification debt** | Ships code faster than you can confirm | Confirm it works yourself |
| **Comprehension debt** | Generates code you didn't write | Read and understand what it made |
| **Cognitive surrender** | Runs itself without your input | Maintain independent judgment |

> If I weren't reviewing the code myself or if I relied entirely on automated loops to fix it, my product's quality would suffer. I'd likely end up stuck in a downward spiral, continuously digging myself into a deeper hole. — Addy Osmani

---

## When to Worry

You should be especially vigilant when:
- The loop has been running unattended for >1 day
- You approved the last 5+ PRs without reading them
- You can't explain the last change the loop made
- The loop's output "looks right" every time (no failures = no one is checking hard enough)
- You designed the loop to avoid a task you didn't want to understand
