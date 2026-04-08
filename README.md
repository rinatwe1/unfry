# Claude Session Log

**Version:** 0.1  
**Purpose:** Automatic conversation logging for Claude Code — never lose context between sessions.

---

## The Problem

Claude Code is powerful but stateless. Every new window = blank slate.

You make decisions, create files, have breakthroughs — and next session Claude has no idea what happened. You repeat context, re-explain decisions, lose momentum.

**Claude Session Log is the memory layer.**

---

## What It Does

- Logs every meaningful Claude Code session to a structured file
- Extracts key decisions, tasks created, files changed, and next steps
- Links sessions to projects so context is findable
- Updates your project files (changelog, tasks, CLAUDE.md) with session insights
- Works across all Claude Code windows and projects

---

## How to Install

### Step 1: Clone this repo

```bash
git clone https://github.com/rinatwe1/claude-session-log.git
cd claude-session-log
```

### Step 2: Add CLAUDE.md to your project

Copy the `CLAUDE.md` from this repo into your project root. It tells Claude to run `/log` at the end of each session.

```bash
cp CLAUDE.md /path/to/your/project/
```

Or add this block to your existing `CLAUDE.md`:

```markdown
## Session Logging

At the end of every meaningful session, run `/log`.
This writes a session summary to `sessions/YYYY-MM-DD-[project].md`.
```

### Step 3: Copy the `/log` skill

```bash
mkdir -p ~/.claude/skills/log
cp skills/log/SKILL.md ~/.claude/skills/log/SKILL.md
```

That's it. Now run `/log` at the end of any session.

---

## How It Works

```
You work with Claude
        ↓
End of session → run /log
        ↓
Claude asks: which project is this about?
        ↓
Claude summarizes: decisions, tasks, files, next steps
        ↓
Writes to sessions/YYYY-MM-DD-[project].md
        ↓
Offers to update: changelog / tasks / CLAUDE.md
        ↓
Next session: Claude reads previous log → instant context
```

---

## Example Session Log Output

```markdown
---
date: 2026-04-08
project: spirit
topics: [taxonomy, lovable, shopify]
duration: long
---

# Session Log — 2026-04-08 — Spirit

## What We Worked On
- Finalized taxonomy: 24 categories, 6 event types
- Completed Lovable prompts A, 7, B for event creation form
- Fixed Step 7 routing bug (was unreachable)

## Key Decisions
- Renamed `performance` → `show`, `online_event` → `online` for consistency
- Decided NOT to use workspace.yaml (stateless architecture)
- Spirit Pick badge logic: auto-assigned by admin, not self-selected

## Tasks Created
- [ ] Update instructor-dashboard-spec.md with approval flow
- [ ] Send instructor specs to Worx (phase 2)
- [ ] Set up GitHub repo for Spirit specs

## Files Changed
- Spirit/01_Product/lovable/lovable-event-creation.md
- Spirit/01_Product/04-event-page-spec.md
- Spirit/01_Product/02-search-page-spec.md

## Next Steps
- Update instructor dashboard spec (priority: high)
- GitHub setup for Spirit docs
- Lovable: add is_spirit_pick + custom_badge to EventCard

## Notes
Long session, very productive. All Lovable prompts done. Docs sent to Worx.
```

---

## Folder Structure

```
Claude-Session-Log/
├── README.md              — This file
├── CLAUDE.md              — Instructions for Claude (copy to your project)
├── skills/
│   └── log/
│       └── SKILL.md       — The /log skill (copy to ~/.claude/skills/log/)
├── hooks/
│   └── session-end.sh     — Optional: auto-trigger on session end
├── templates/
│   └── session-template.md — Session log template
└── sessions/
    └── .gitkeep           — Your logs go here (gitignored by default)
```

---

## Optional: Auto-trigger via Stop Hook

If you want to be prompted to log even when you forget, add the stop hook:

```bash
# In your Claude Code settings.json, add:
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/claude-session-log/hooks/session-end.sh"
          }
        ]
      }
    ]
  }
}
```

This writes a session marker (timestamp + directory) so you never lose track of when sessions happened, even if you didn't run `/log`.

---

## Philosophy

Claude Code is not a chatbot. It's a thinking partner.

But a thinking partner you have to re-introduce yourself to every day is exhausting.

Session Log turns ephemeral conversations into **institutional memory** — structured, searchable, actionable.

> "The best productivity system is the one that remembers so you don't have to."

---

## Contributing

This is an open-source project. PRs welcome.

Ideas for future versions:
- Auto-detect project from working directory
- Parse Claude's output to pre-fill the log
- Integration with GitHub Issues
- Weekly digest of session logs
- Vector search over session history

---

**Made with Claude Code.**
