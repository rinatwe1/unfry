---
name: wrap
description: Wrap up this session — summarize, extract insights and next steps, save
allowed-tools: Write
---

# /wrap — Session Wrap-Up

Summarize the current session. Extract what matters. Clear the cognitive load.

---

## What this does

Reads the current conversation and produces:
1. **Summary** — what we worked on (3-5 bullets)
2. **Key Decisions** — what was decided and why
3. **Insights** — non-obvious things that emerged
4. **Next Steps** — concrete, ordered, ready to act on

Saves to a file so the next session starts with full context.

---

## Execution

### Step 1: Generate the brain dump

Read the current conversation and extract:

**Summary** (3-5 bullets)
- What was actually accomplished — not just discussed
- Specific, not vague ("Renamed event types performance→show" not "worked on naming")

**Key Decisions** (2-4 items)
- Format: Decision → Why
- Only decisions with lasting impact
- Skip obvious or trivial choices

**Insights** (1-3 items)
- Things that weren't obvious at the start
- Patterns, realizations, strategic shifts
- The "aha" moments

**Next Steps** (ordered by priority)
- Concrete enough to act on without re-reading
- Start with the most important
- Flag blockers if any

---

### Step 2: Display immediately

Show the brain dump in this format:

```
📦 /wrap — [date] — [project name if obvious]

## Summary
- [bullet]
- [bullet]
- [bullet]

## Key Decisions
- [decision]: [why]
- [decision]: [why]

## Insights
- [insight]

## Next Steps
1. [most important — priority: high]
2. [next]
3. [next]
```

---

### Step 3: Offer to save

Ask:
> "Save this? (y/n) — will write to `unfry-sessions/YYYY-MM-DD-[project].md`"

If yes → write the file to the current project directory.
If no → done. The brain dump was the point.

---

## Edge cases

**Very short session:** Still run it. Even a 15-minute session has decisions worth capturing.

**Unclear project:** Use the current directory name as the project.

**Multiple projects in one session:** Note both in the header.

---

## Philosophy

The point of `/wrap` is offloading — not logging.

You ran it because your brain is full. The output should feel like putting something down, not like creating more work.

Keep it short. Keep it honest. Keep it useful.
