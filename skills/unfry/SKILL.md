---
name: unfry
description: Load previous session context — start the session oriented, not fried
allowed-tools: Read, Glob
---

# /unfry — Start Fresh

Pull up what happened last time. Start oriented, not fried.

---

## Execution

### Step 1: Find the most recent session

Look for the latest file in `{current-directory}/unfry-sessions/`.

If the directory doesn't exist or is empty:
> "No previous session found for this project. Run `/wrap` at the end of sessions to start building a history."

### Step 2: Read the file

Read the most recent `unfry-sessions/YYYY-MM-DD-*.md` file.

### Step 3: Display it

**Default:** Show the content as-is, prefixed with:

```
🧠 /unfry — [date] — [project]

[content of the file]
```

**If `--brief` was passed:** Extract only the top 3 most important things from the file — the single most critical next step, the most impactful decision, and one key insight. Format:

```
🧠 /unfry --brief — [date] — [project]

**Top 3:**
1. [most critical next step]
2. [most impactful decision]
3. [key insight]
```

Then add:
> Ready to continue. What are we working on?

---

## Notes

- Always use the most recent file (sort by filename — YYYY-MM-DD sorts correctly)
- If there are multiple files from the same day, show the last one
- Default: don't summarize the summary — show it as-is
- `--brief`: synthesize, don't just truncate
- This is meant to be the first command in a new session
