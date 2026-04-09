# Unfry

**Stop supervising your AI. Start using it.**

Brain Fry doesn't come from using Claude Code. It comes from managing it — re-explaining context, tracking what happened, keeping state in your head between sessions.

Unfry is the memory layer that takes that load off.

---

## Two Ways to Use It

### `/unfry` — Manual (30 seconds setup)

A slash command you run at the end of any session.
Reads the conversation. Extracts what matters. Saves it so the next session starts informed.

```
Summary / Key Decisions / Insights / Next Steps
```

**Best for:** Anyone who wants to start. Zero friction, no background process.

### Daemon — Automatic (macOS)

A background process that watches your Claude Code sessions.
Triggers automatically on compact events and session inactivity.
Writes summaries without you doing anything.

**Best for:** Heavy Claude Code users. Set it once, forget it.

---

## Install `/unfry` (30 seconds)

```bash
mkdir -p ~/.claude/skills/unfry
curl -o ~/.claude/skills/unfry/SKILL.md \
  https://raw.githubusercontent.com/rinatwe1/unfry/main/skills/unfry/SKILL.md
```

Then in any Claude Code session:

```
/unfry
```

Claude will summarize the session and offer to save it.

---

## Install `/recall`

Load the previous session's context when you open a new window:

```bash
mkdir -p ~/.claude/skills/recall
curl -o ~/.claude/skills/recall/SKILL.md \
  https://raw.githubusercontent.com/rinatwe1/unfry/main/skills/recall/SKILL.md
```

Then at the start of a new session:

```
/recall
```

---

## Install Daemon (macOS only)

```bash
git clone https://github.com/rinatwe1/unfry.git
cd unfry/daemon
./install.sh
```

The install script:
- Installs Python dependency (`watchdog`)
- Creates `~/.unfry/` for logs
- Registers a LaunchAgent that starts on login

### What it does

| Trigger | What happens |
|---------|-------------|
| Compact event detected | Summarizes conversation up to compact |
| 30 min session inactivity | Summarizes and closes the session |

Summaries are saved to `[project-dir]/unfry-sessions/YYYY-MM-DD-[project].md`.

### Daemon commands

```bash
# Check if running
launchctl list | grep unfry

# View logs
tail -f ~/.unfry/daemon.log

# Stop
launchctl unload ~/Library/LaunchAgents/com.unfry.daemon.plist

# Restart
launchctl unload ~/Library/LaunchAgents/com.unfry.daemon.plist
launchctl load ~/Library/LaunchAgents/com.unfry.daemon.plist
```

---

## How It Works

Claude Code stores every session as JSONL in `~/.claude/projects/`. All your decisions, all your context — it's already there. Nobody was doing anything with it.

Unfry reads those files, detects compact boundaries, and calls `claude -p` to generate a structured summary.

```
Claude Code session
       ↓
compact event / window closes
       ↓
daemon reads JSONL since last compact
       ↓
claude -p generates brain dump
       ↓
saved to [project]/unfry-sessions/YYYY-MM-DD.md
       ↓
/recall at next session → instant context
```

---

## Output Format

```markdown
## Summary
- [what was actually accomplished]
- [specific, not vague]

## Key Decisions
- [decision]: [why]

## Insights
- [non-obvious thing that emerged]

## Next Steps
1. [most important]
2. [next]
```

---

## Requirements

- Claude Code installed (`claude` CLI available)
- Python 3.7+
- macOS (daemon only — `/unfry` skill works everywhere)

---

## Project Structure

```
unfry/
├── skills/
│   ├── unfry/SKILL.md      — /unfry slash command
│   └── recall/SKILL.md     — /recall slash command
├── daemon/
│   ├── daemon.py           — watchdog monitor
│   ├── summarizer.py       — JSONL reader + Claude summarizer
│   ├── install.sh          — LaunchAgent installer
│   └── com.unfry.daemon.plist  — LaunchAgent config template
└── README.md
```

---

## Philosophy

The best memory system is the one that works when you're tired, distracted, and moving fast.

`/unfry` works because it's one command at the end of a session. The daemon works because it's zero commands.

Both exist because the data is already there — Claude Code just wasn't doing anything with it.

---

## Status

- [x] `/unfry` slash command
- [x] `/recall` slash command  
- [x] Daemon — compact event detection
- [x] Daemon — inactivity timeout
- [x] macOS LaunchAgent installer
- [ ] Windows support (V2)
- [ ] Dashboard — cross-project session analytics (V2)
- [ ] `/recall` auto-trigger on window open (V2)

---

**Open source. Early stage. PRs welcome.**

Made with Claude Code, by someone who got tired of explaining themselves every morning.
