# Product Pitch — Unfry

**Version:** 0.1
**Date:** 2026-04-09
**Author:** רינת וייס

---

## One Liner

**Unfry turns Claude Code from a tool you supervise into a system that supervises itself — so your brain doesn't have to.**

---

## The Hook

Harvard Business Review, 2025: 14% of AI-heavy workers report cognitive fatigue — "brain fry."

The culprit? Not using AI too much.
**Supervising it.**

Reviewing outputs. Re-explaining context. Monitoring what was lost in a compact. Switching between four Claude windows and remembering where each one stopped.

Simon Willison — co-creator of Django, 100+ open source projects — described it live: managing four machines with different tasks left him exhausted by 11am.

Sound familiar?

---

## The Insight

The HBR research is precise:

> "Workers who used AI to automate routine tasks showed lower burnout scores — because their mental energy shifted to meaningful work."

The burnout isn't from AI. It's from **supervising** AI.

And the most exhausting supervision task in Claude Code?
**Context.**

Every new window: re-explain the project.
Every compact: pray nothing was lost.
Every morning: where were we?

Your brain is doing work that a machine should do.

---

## The Solution

**Unfry** is a background daemon that runs alongside Claude Code.

It watches your sessions. Silently. Automatically.

When a compact happens — it captures the conversation, generates a structured summary, writes it to your project.

When you close a window — same.

When you open a new window and type `/unfry` — you get:
- What we worked on last session
- Key decisions (with the *why*)
- Exact next steps

Zero re-explanation. Zero context tax. Zero brain fry from supervision.

---

## Why This. Why Now.

Three forces converging:

**1. Claude Code is becoming the IDE.**
Developers, PMs, marketers — everyone is spending 4-6 hours/day in Claude Code. The session problem is universal.

**2. Brain Fry is becoming a category.**
HBR legitimized it. Simon Willison described it. Roytal Weinstein wrote about it. The narrative is being built — the product isn't here yet.

**3. The data is already there.**
Claude Code stores every conversation in `~/.claude/projects/`. We're not scraping or hacking — we're reading what's already written.

---

## Who It's For

**Primary:** Knowledge workers in Claude Code 4+ hours/day
— PMs building products
— Developers running agentic workflows
— Marketers managing multi-tool pipelines

**Secondary:** Teams where multiple people work on the same Claude project
— Shared context = no "wait, what did you and Claude decide yesterday?"

**Not for:** Casual Claude users, one-off tasks

---

## The Product in 30 Seconds

```
You work. Unfry captures.
Session ends → structured log written automatically.
New session → /unfry → instant context.
No explanation. No re-reading. No brain fry.
```

---

## Traction / Validation

- HBR study: 1,488 workers, 14% cognitive fatigue from AI supervision
- Simon Willison publicly described the exact problem
- The LinkedIn conversation is happening NOW — the product isn't
- Claude Code's user base: growing 40%+ month-over-month (Anthropic)
- The JSONL data already exists — technical risk is near zero

---

## The Ask

**Phase 1 (now):** Open source. GitHub. Build the community.
Get 500 stars. Get feedback. Find the 20% of features that do 80% of the work.

**Phase 2:** Team features. Shared context. Multi-project dashboard.
**Revenue:** $15/month per user. $49/month per team (5 seats).

**Phase 3:** Enterprise. Audit logs. SSO. Compliance.
**Revenue:** Custom.

---

## Name

**Unfry** — speaks directly to the Brain Fry narrative that PM builders are already having. Playful, memorable, immediately understood.

Repo: [github.com/rinatwe1/unfry](https://github.com/rinatwe1/unfry)

---

*"The best productivity system is the one that remembers so you don't have to."*
