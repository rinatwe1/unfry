#!/usr/bin/env python3
"""
Unfry Summarizer
Reads a Claude Code JSONL session file and generates a brain dump.
Saves output to {cwd}/unfry-sessions/YYYY-MM-DD-{project}.md
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def extract_messages(jsonl_path: str, since_last_compact: bool = True) -> tuple[list, str]:
    """
    Extract user/assistant messages from a JSONL session file.
    Returns (messages, cwd).
    If since_last_compact=True, only returns messages after the last compact_boundary.
    """
    messages = []
    cwd = None
    last_compact_index = -1
    all_entries = []

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                all_entries.append(obj)
            except json.JSONDecodeError:
                continue

    # Find last compact_boundary
    if since_last_compact:
        for i, obj in enumerate(all_entries):
            if obj.get("type") == "system" and obj.get("subtype") == "compact_boundary":
                last_compact_index = i

    # Extract messages after last compact (or all if no compact)
    start_index = last_compact_index + 1

    for obj in all_entries[start_index:]:
        msg_type = obj.get("type")

        # Get cwd from user messages
        if msg_type == "user" and not cwd:
            cwd = obj.get("cwd", "")

        # Extract user text
        if msg_type == "user":
            message = obj.get("message", {})
            content = message.get("content", "")
            text = ""
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        text += item.get("text", "")
            elif isinstance(content, str):
                text = content
            if text.strip():
                messages.append({"role": "user", "text": text.strip()})

        # Extract assistant text
        elif msg_type == "assistant":
            message = obj.get("message", {})
            content = message.get("content", [])
            text = ""
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "text":
                        text += item.get("text", "")
            elif isinstance(content, str):
                text = content
            if text.strip():
                messages.append({"role": "assistant", "text": text[:500]})  # truncate long responses

    return messages, cwd or ""


def build_prompt(messages: list, project_name: str) -> str:
    """Build the summarization prompt."""
    conversation_text = ""
    for msg in messages[-40:]:  # last 40 messages max
        role = "User" if msg["role"] == "user" else "Claude"
        conversation_text += f"\n{role}: {msg['text'][:300]}\n"

    return f"""You are summarizing a Claude Code work session for project: {project_name}

Here is the conversation:
{conversation_text}

Generate a structured brain dump in this exact format (in the same language as the conversation — if Hebrew, write Hebrew):

## Summary
- [what was accomplished — specific, not vague]
- [bullet]
- [bullet]

## Key Decisions
- [decision]: [why]
- [decision]: [why]

## Insights
- [non-obvious thing that emerged]

## Next Steps
1. [most important]
2. [next]
3. [next]

Be concise. Skip obvious things. Focus on what matters for the next session."""


def save_summary(content: str, cwd: str, project_name: str) -> str:
    """Save the summary to unfry-sessions/ in the project directory."""
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-{project_name}.md"

    output_dir = Path(cwd) / "unfry-sessions"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename

    # If file exists today, append with separator
    if output_path.exists():
        with open(output_path, "a", encoding="utf-8") as f:
            f.write(f"\n\n---\n\n# Session (continued — {datetime.now().strftime('%H:%M')})\n\n")
            f.write(content)
    else:
        header = f"---\ndate: {today}\nproject: {project_name}\n---\n\n"
        header += f"# /unfry — {today} — {project_name}\n\n"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(header + content)

    return str(output_path)


def summarize_session(jsonl_path: str, since_last_compact: bool = True) -> Optional[str]:
    """
    Main entry point. Summarizes a session and saves it.
    Returns the path to the saved file, or None if nothing to summarize.
    """
    messages, cwd = extract_messages(jsonl_path, since_last_compact)

    if len(messages) < 3:
        return None  # Not enough content to summarize

    # Derive project name from cwd
    if cwd:
        project_name = Path(cwd).name.lower().replace(" ", "-")
    else:
        project_name = "unknown"

    prompt = build_prompt(messages, project_name)

    # Call claude CLI
    try:
        result = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            print(f"[unfry] claude CLI error: {result.stderr}", file=sys.stderr)
            return None
        summary = result.stdout.strip()
    except FileNotFoundError:
        print("[unfry] claude CLI not found. Is Claude Code installed?", file=sys.stderr)
        return None
    except subprocess.TimeoutExpired:
        print("[unfry] Summarization timed out.", file=sys.stderr)
        return None

    if not summary:
        return None

    save_path = save_summary(summary, cwd, project_name)
    print(f"[unfry] Saved: {save_path}")
    return save_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: summarizer.py <path-to-session.jsonl> [--full]")
        sys.exit(1)

    jsonl_path = sys.argv[1]
    full_session = "--full" in sys.argv

    result = summarize_session(jsonl_path, since_last_compact=not full_session)
    if not result:
        print("[unfry] Nothing to summarize (session too short or error).")
        sys.exit(1)
