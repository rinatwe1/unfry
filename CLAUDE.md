# CLAUDE.md - Claude Session Log Instructions

**System:** Claude Session Log
**Purpose:** Automatic session logging — never lose context between sessions

---

## What This System Does

Every meaningful Claude Code session should be logged. This creates a memory layer that survives between sessions, so context, decisions, and progress are never lost.

---

## Session Logging Protocol

### When to Run `/log`

Run `/log` at the end of every session where:
- A significant decision was made
- Files were created or modified
- Tasks were defined or completed
- A product or project direction changed
- Something important was discovered

**Do NOT log:** Simple lookups, quick edits with no context value, test runs.

### How to Run

Simply say `/log` or "log this session" at the end of your work.

The `/log` skill will:
1. Ask which project this session is about (if not obvious from context)
2. Summarize in 5 key areas: what was discussed, decisions made, tasks created, files changed, next steps
3. Write to `sessions/YYYY-MM-DD-[project].md`
4. Offer to update relevant project files (changelog, tasks, CLAUDE.md)

---

## Reading Previous Logs

At the start of a new session, to restore context:

```
"Read the last session log for [project]"
```

Or to see all recent sessions:

```
"What did we work on recently?"
```

Claude will scan `sessions/` and summarize relevant logs.

---

## Log Format

Logs follow the template in `templates/session-template.md`:

```markdown
---
date: YYYY-MM-DD
project: [project-name]
topics: [topic1, topic2]
duration: [short/medium/long]
---

# Session Log — [Date] — [Project]

## What We Worked On
## Key Decisions
## Tasks Created
## Files Changed
## Next Steps
## Notes
```

---

## Updating Project Files

After logging, Claude will offer to:

1. **Update CHANGELOG.md** — Add session highlights to the project changelog
2. **Update tasks** — Create task files for "next steps" identified
3. **Update CLAUDE.md** — Add new decisions or context to project memory
4. **Update roadmap** — If direction changed significantly

Always say yes to updates that matter. Skip if the session was minor.

---

## File Locations

- Session logs: `sessions/YYYY-MM-DD-[project].md`
- Skill: `~/.claude/skills/log/SKILL.md`
- Template: `templates/session-template.md`
- Hook: `hooks/session-end.sh`

---

## Tips for Claude

- **Be specific in decisions** — "Decided X because Y" not just "Discussed X"
- **List actual filenames** in "Files Changed" — relative paths
- **Make tasks actionable** — "Update instructor-dashboard-spec.md" not "update docs"
- **Be honest about duration** — short (<30m), medium (30m-2h), long (2h+)
- **Next steps = what YOU (Claude) will do next session** — not vague goals

---

**Rule:** Never end a productive session without running `/log`. The 2 minutes it takes saves 10 minutes of context-restoring next time.
