# /log Skill — Claude Session Log

**Trigger:** `/log` or "log this session" or "save session"  
**Purpose:** Write a structured summary of this Claude Code session to a log file.

---

## What This Skill Does

Captures the session in a structured format:
- What was worked on
- Key decisions made
- Tasks created
- Files changed
- Next steps

Saves to `sessions/YYYY-MM-DD-[project].md` and offers to update project files.

---

## Execution Steps

### Step 1: Identify the Project

Check if the project is obvious from context:
- What directory is active?
- What files were discussed?
- What tags/topics came up?

If unclear, ask:
> "Which project is this session about? (e.g., spirit, nx2u, recipehub, personal)"

Accept a short answer — don't require full path.

---

### Step 2: Determine Session Duration

Estimate based on complexity and number of topics:
- **short** — single focused task, <30 min
- **medium** — a few tasks or topics, 30 min–2 hours  
- **long** — multiple topics, major changes, 2+ hours

---

### Step 3: Extract Key Information

Review the conversation and extract:

**What We Worked On** (3-6 bullet points)
- Describe the main activities, not just files touched
- Focus on what was accomplished, not just attempted
- Be specific: "Finalized taxonomy (24 categories)" not "worked on taxonomy"

**Key Decisions** (2-5 bullet points)
- Only decisions with lasting impact
- Format: "Decided [what] because [why]"
- Include tradeoffs if relevant
- Skip minor preferences

**Tasks Created** (as checkboxes)
- Only concrete action items that came out of this session
- Format: `- [ ] [Verb] [specific thing]`
- If no tasks were explicitly created, list "Next Steps" items as tasks

**Files Changed** (list)
- Actual files that were created, edited, or significantly discussed
- Use relative paths from project root
- Note if file was created (new) vs edited (updated)

**Next Steps** (3-5 items)
- What should happen NEXT SESSION, not someday
- Ordered by priority
- Specific enough to act on without re-reading this log

**Notes** (optional)
- Anything that doesn't fit above
- Overall mood/progress of session
- Blockers encountered
- Dependencies on others

---

### Step 4: Determine Log File Path

Construct the path:
```
sessions/YYYY-MM-DD-[project-name].md
```

Where:
- `YYYY-MM-DD` = today's date
- `[project-name]` = lowercase, hyphenated project name (e.g., `spirit`, `claude-session-log`, `nx2u`)

If a log already exists for today + project, append `-2` (e.g., `2026-04-08-spirit-2.md`).

---

### Step 5: Write the Log File

Use this exact template:

```markdown
---
date: YYYY-MM-DD
project: [project-name]
topics: [topic1, topic2, topic3]
duration: [short/medium/long]
---

# Session Log — [YYYY-MM-DD] — [Project Name]

## What We Worked On
- [bullet 1]
- [bullet 2]
- [bullet 3]

## Key Decisions
- [decision 1: what + why]
- [decision 2: what + why]

## Tasks Created
- [ ] [task 1]
- [ ] [task 2]

## Files Changed
- [path/to/file.md] (created)
- [path/to/other.md] (updated)

## Next Steps
- [next step 1 — priority: high/medium/low]
- [next step 2]
- [next step 3]

## Notes
[Any additional context, blockers, or observations]
```

After writing, verify the file exists by reading it back.

---

### Step 6: Offer to Update Project Files

Ask:
> "Session logged! Want me to also update any project files?
> - [C] Update CHANGELOG.md
> - [T] Create task files for next steps
> - [M] Update CLAUDE.md with new context
> - [R] Update roadmap (if direction changed)
> - [N] No thanks, log is enough"

**If CHANGELOG.md update requested:**
- Find the project's CHANGELOG.md
- Add an entry under today's date in the format:
  ```markdown
  ## [YYYY-MM-DD]
  ### Session: [Project]
  [2-3 bullet highlights from this session]
  ```

**If task files requested:**
- For each "Tasks Created" item, offer to create a task file in `_System/tasks/`
- Use Teresa Torres format (type, due, tags)

**If CLAUDE.md update requested:**
- Find the project's CLAUDE.md
- Add key decisions to the relevant section
- Update "Status" if applicable

**If roadmap update requested:**
- Find the project's roadmap.md
- Update status or add new items based on session

---

### Step 7: Confirm

Report back:
> "Session logged to `sessions/[filename].md`
> [List any additional updates made]
> 
> Next session, start with: 'Read the last session log for [project]'"

---

## Edge Cases

**No clear project:**  
Ask once. If still unclear, use "general" as the project name.

**Very short session (< 5 min):**  
Ask "This seems like a short session — worth logging?" If yes, log a minimal version (just decisions + next steps).

**Multiple projects in one session:**  
Create one log per project, or one combined log with project tags.

**Sessions from yesterday:**  
If the user says "log yesterday's session", use yesterday's date. Ask what was worked on if not clear from context.

---

## Example Output

```markdown
---
date: 2026-04-08
project: spirit
topics: [taxonomy, lovable, shopify, event-form]
duration: long
---

# Session Log — 2026-04-08 — Spirit

## What We Worked On
- Completed all Lovable prompts (A, 7, B) for event creation form
- Fixed Step 7 routing bug (step was unreachable due to form state issue)
- Reviewed data model — identified dual type systems conflict
- Renamed event types for consistency with Shopify conventions
- Sent Foundation + User-Facing specs to Worx

## Key Decisions
- Renamed `performance` → `show` and `online_event` → `online` to match Shopify norms
- Spirit Pick badge: admin-assigned only, NOT self-selected by instructors
- Decided against workspace.yaml — stateless architecture is cleaner

## Tasks Created
- [ ] Update instructor-dashboard-spec.md — add approval flow + draft list
- [ ] Send instructor specs to Worx (phase 2 of docs)
- [ ] GitHub setup for Spirit specs repo

## Files Changed
- Spirit/01_Product/lovable/lovable-event-creation.md (updated)
- Spirit/01_Product/04-event-page-spec.md (updated — badges section)
- Spirit/01_Product/02-search-page-spec.md (updated — badges section)

## Next Steps
- Update instructor-dashboard-spec.md (priority: high — blocks Worx phase 2)
- GitHub repo setup for Spirit (priority: medium)
- Add is_spirit_pick + custom_badge to Lovable EventCard (priority: low)

## Notes
Very productive session. All Lovable prompts complete — major milestone.
Docs sent to Worx. Next session can focus on instructor dashboard spec.
```
