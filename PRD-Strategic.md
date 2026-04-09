# PRD Strategic — Unfry
### AI Session Memory That Eliminates Cognitive Fatigue

**Version:** 0.1
**Date:** 2026-04-09
**Status:** Draft
**Owner:** רינת וייס
**Type:** Strategic / Business (not technical)

---

## 1. Vision

**In 3 years:** Unfry is the default memory layer for Claude Code users worldwide. Every knowledge worker using AI tools daily trusts Unfry to carry their context — so their brain carries ideas.

**In 1 year:** 10,000 active users. The go-to open source tool for Claude Code power users. Known in the Simon Willison / Lenny Rachitsky / PM Twitter circles as "the tool that solved Brain Fry."

---

## 2. Problem Statement

### The Macro Problem
HBR (2025): 14% of AI-heavy workers experience cognitive fatigue — "brain fry." Not from using AI. From **supervising** it.

The research is clear: workers who use AI to automate routine tasks show **lower** burnout than those who use it for complex, supervised tasks.

### The Specific Problem (Claude Code)
Claude Code is stateless by design. Every window is a blank slate.

This forces users to manually:
- Re-explain project context at the start of every session
- Remember what decisions were made and why
- Monitor what was lost during context compaction
- Keep mental track of where each of 3-4 parallel windows stopped
- Rebuild reasoning chains after every compact event

**This is pure supervision work. No creative value. All cognitive cost.**

### The Data
- Claude Code stores every session as JSONL in `~/.claude/projects/`
- The data exists. Nobody is reading it systematically.
- The compact events are logged. Nobody is acting on them.
- The solution is a daemon, not a new AI model.

### User Quote (paraphrased, Simon Willison)
*"Managing four machines with different tasks simultaneously leaves me exhausted by 11am."*

---

## 3. Target Users

### Primary Persona — The Power User
**Who:** PM, developer, or knowledge worker in Claude Code 4+ hours/day
**Pain:** Starts every session with 5 minutes of "let me remind you where we are"
**Frequency:** Daily
**Willingness to pay:** High — productivity tools are a professional expense

**Specific roles (per HBR data):**
- Software developers (top 3 affected by AI fatigue)
- Product managers
- Marketing professionals
- Finance/operations

### Secondary Persona — The Team Lead
**Who:** Manages a team where multiple people work with Claude on shared projects
**Pain:** "What did you and Claude decide yesterday?" — no shared memory
**Frequency:** Multiple sessions/day across team members
**Willingness to pay:** Higher — team tool, company budget

### Not a Target (for v1)
- Casual Claude.ai web users (no Claude Code)
- One-off task users
- Non-technical users who can't run a daemon

---

## 4. Market Opportunity

### Bottom-Up
- Claude Code MAU: estimated 200K-500K (growing 40%+ MoM)
- Power users (4+ hours/day): ~15-20% = 30K-100K
- Conversion at 10%: 3K-10K paying users at launch
- $15/month: $540K-$1.8M ARR at launch

### Top-Down
- Productivity software market: $96B (2024)
- AI productivity tools segment: fastest growing
- "Cognitive load tools" emerging as category (Notion AI, Mem.ai, Rewind)
- Unfry is the first to target specifically the **supervision** fatigue

### Why Now — The Window
- Brain Fry narrative is peaking (HBR, Simon Willison, LinkedIn posts)
- Claude Code adoption is accelerating
- Nobody has shipped this yet
- Open source → community → paid features: classic go-to-market

---

## 5. Value Proposition

### For Individual Users
**Before Unfry:**
- Start every session: "Let me remind you..."
- After compact: panic, re-read, re-explain
- Monday morning: "What were we working on?"
- 3-4 windows open: mental juggling act

**After Unfry:**
- Start every session: `/unfry` → instant context
- Compact: nothing lost, structured log auto-generated
- Monday morning: read 5-bullet summary from Friday
- 3-4 windows: each carries its own memory

**The promise:** All the continuity. Zero supervision tax.

### For Teams
- Shared context across team members
- "What did Sarah and Claude decide?" → read the log
- Onboarding new team member: read 3 months of session logs
- No more tribal knowledge locked in someone's chat history

---

## 6. Core Features (Strategic Level)

### MVP (Phase 1) — Open Source
| Feature | Value |
|---------|-------|
| Auto-capture on compact | Never lose context mid-session |
| Auto-capture on window close | Every session documented |
| `/unfry` skill | Instant context on demand |
| Per-project sessions | Right context for right project |
| Structured logs | Decisions, next steps, files changed |

**Success metric:** 500 GitHub stars. 100 active users. NPS > 50.

### V1 (Phase 2) — Freemium
| Feature | Value | Plan |
|---------|-------|------|
| Cross-machine sync | Same context on laptop + desktop | Paid |
| Team shared context | One source of truth | Paid |
| Decision timeline | Full history of why decisions were made | Paid |
| `/unfry --team` | Anyone can get project context | Paid |
| Weekly digest | "This week's key decisions across projects" | Paid |

### V2 (Phase 3) — Enterprise
| Feature | Value |
|---------|-------|
| SSO / SAML | Enterprise auth |
| Audit logs | Compliance |
| Admin dashboard | Team usage analytics |
| Private cloud option | Data residency |
| API access | Integration with existing tools |

---

## 7. Business Model

### Phase 1: Open Source (months 1-6)
- Free, GitHub, build community
- Goal: product-market fit validation
- Revenue: $0 (intentional)

### Phase 2: Freemium (months 7-12)
| Tier | Price | What's included |
|------|-------|-----------------|
| Free | $0 | Local only, 1 machine, 30-day history |
| Pro | $15/month | Unlimited history, sync, `/unfry` advanced |
| Team | $49/month | 5 seats, shared context, team digest |

### Phase 3: Enterprise (year 2)
- Custom pricing, $500-2000/month per organization
- Requires: SSO, compliance, SLA

### Unit Economics (target)
- CAC: $15-30 (organic/community driven)
- LTV: $180-360 (12-24 month retention)
- LTV/CAC: >6x

---

## 8. Go-to-Market

### Phase 1: Community (months 1-3)
**Channels:**
- GitHub launch — target HN "Show HN" post
- Simon Willison's blog (approach for mention/review)
- Lenny's Newsletter community
- Claude Code subreddit / Discord
- LinkedIn — Brain Fry narrative (Rinat's network)

**Messaging:** "Stop supervising Claude. Let it remember itself."

**KPIs:**
- 500 GitHub stars in 30 days
- 100 active installs
- 3 "influencer" mentions (Simon Willison tier)

### Phase 2: Content-Led (months 4-9)
**Channels:**
- LinkedIn posts (Brain Fry series)
- "How I eliminated context switching with Unfry" case studies
- PM communities (Product Hunt, Lenny's, etc.)
- Developer communities (HN, dev.to)

**Messaging:** "The cognitive load layer for AI-heavy workers."

### Phase 3: Product-Led (month 10+)
- Team invites (Slack-style viral loop)
- "Powered by Unfry" attribution in shared summaries
- Partner with Claude Code adjacent tools

---

## 9. Success Metrics

### 3 Months (MVP)
- GitHub: 500+ stars
- Active users: 100+
- Retention (D30): 40%+
- NPS: 50+
- Qualitative: at least 5 unprompted "this changed how I work" testimonials

### 12 Months (V1)
- Paying users: 500+
- MRR: $10,000+
- Team accounts: 20+
- Churn: <5%/month

### 24 Months (Scale)
- Paying users: 5,000+
- MRR: $75,000+
- Enterprise accounts: 5+
- ARR: $1M

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Anthropic ships native memory | Medium | High | Move fast. Build moat in team features + ecosystem |
| Claude Code changes JSONL format | Low | High | Abstract the parser. Monitor releases. |
| Privacy concerns (reading session files) | Medium | Medium | Full transparency. Local-first. No cloud in free tier. |
| Low willingness to pay | Medium | High | Validate early. Offer team plan first (easier B2B) |
| Market too small (Claude Code only) | Low | Medium | Architecture supports other AI tools. Expand later. |

---

## 11. Competitive Landscape

| Product | What it does | Gap |
|---------|-------------|-----|
| Rewind.ai | Records everything on your screen | Not Claude-specific, privacy concerns, expensive |
| Mem.ai | AI-powered notes with memory | Manual input required, not session-based |
| Notion AI | Workspace with AI | Not a memory layer, requires manual curation |
| Claude Projects | Built-in project memory | No session logs, no compact protection, no /unfry |
| Nothing | — | **This space is empty** |

**Unfry's moat:**
1. Claude Code native (reads JSONL directly — no screen recording, no API hacks)
2. Automatic (zero manual input required)
3. Open source (trust + community)
4. Positioned on the Brain Fry narrative (timing advantage)

---

## 12. Open Questions

- [ ] **Name:** Unfry vs Recall vs other? Needs validation with target users.
- [ ] **Privacy messaging:** How explicit to be about "reading your Claude files"?
- [ ] **Multi-tool expansion:** Cursor? Windsurf? Or stay Claude-only for focus?
- [ ] **Founding team:** Solo project or find a technical co-founder?
- [ ] **Claude Code ToS:** Does reading JSONL files violate anything? (legal review needed)
- [ ] **Pricing validation:** Is $15/month right? Survey needed.

---

## 13. What We're NOT Building (v1)

- ❌ A new AI model or LLM
- ❌ Screen recording / Rewind-style capture
- ❌ A replacement for CLAUDE.md
- ❌ A general-purpose note-taking tool
- ❌ An Obsidian plugin or Notion integration
- ❌ A mobile app

---

**Next Steps:**
1. Validate name with 5 target users
2. Build MVP daemon (2-3 weeks)
3. Soft launch on GitHub
4. Write LinkedIn Brain Fry post (Rinat)
5. Reach out to Simon Willison / Lenny community

---

*"Your brain is for having ideas. Not for remembering what Claude forgot."*
