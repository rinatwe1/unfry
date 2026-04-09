#!/usr/bin/env python3
"""
Unfry Daemon
Watches ~/.claude/projects/ for Claude Code session activity.
Triggers summarization on:
  1. compact_boundary events (immediate)
  2. Session inactivity (30 min after last message = session likely closed)
"""

import json
import logging
import os
import sys
import time
from pathlib import Path
from threading import Timer
from typing import Optional

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print(
        "[unfry] watchdog not installed. Run: pip install watchdog",
        file=sys.stderr,
    )
    sys.exit(1)

from summarizer import summarize_session

# Config
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
INACTIVITY_TIMEOUT_SECONDS = 30 * 60  # 30 minutes
LOG_FILE = Path.home() / ".unfry" / "daemon.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [unfry] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("unfry")


class SessionTracker:
    """Tracks active sessions and their last-seen line count."""

    def __init__(self):
        self._sessions: dict[str, int] = {}  # path -> last line count
        self._inactivity_timers: dict[str, Timer] = {}  # path -> timer

    def get_line_count(self, path: str) -> int:
        return self._sessions.get(path, 0)

    def update(self, path: str, count: int):
        self._sessions[path] = count
        self._reset_inactivity_timer(path)

    def _reset_inactivity_timer(self, path: str):
        if path in self._inactivity_timers:
            self._inactivity_timers[path].cancel()

        timer = Timer(
            INACTIVITY_TIMEOUT_SECONDS,
            self._on_session_inactive,
            args=[path],
        )
        timer.daemon = True
        timer.start()
        self._inactivity_timers[path] = timer

    def _on_session_inactive(self, path: str):
        log.info(f"Session inactive (30 min): {Path(path).name}")
        try:
            result = summarize_session(path, since_last_compact=True)
            if result:
                log.info(f"Inactivity summary saved: {result}")
        except Exception as e:
            log.error(f"Error summarizing on inactivity: {e}")
        finally:
            self._inactivity_timers.pop(path, None)


tracker = SessionTracker()


def read_new_lines(path: str) -> list[dict]:
    """Read lines from last known position."""
    known_count = tracker.get_line_count(path)
    new_entries = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = lines[known_count:]
        tracker.update(path, len(lines))

        for line in new_lines:
            line = line.strip()
            if not line:
                continue
            try:
                new_entries.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    except (OSError, IOError) as e:
        log.warning(f"Could not read {path}: {e}")

    return new_entries


def has_compact_boundary(entries: list[dict]) -> bool:
    return any(
        e.get("type") == "system" and e.get("subtype") == "compact_boundary"
        for e in entries
    )


class JasonlHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        path = event.src_path
        if not path.endswith(".jsonl"):
            return

        new_entries = read_new_lines(path)
        if not new_entries:
            return

        if has_compact_boundary(new_entries):
            log.info(f"Compact event detected in {Path(path).name}")
            try:
                result = summarize_session(path, since_last_compact=True)
                if result:
                    log.info(f"Compact summary saved: {result}")
                else:
                    log.info("Compact: nothing to summarize (session too short)")
            except Exception as e:
                log.error(f"Error summarizing compact: {e}")

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".jsonl"):
            log.info(f"New session file: {Path(event.src_path).name}")
            # Initialize tracker for this file
            tracker.update(event.src_path, 0)


def main():
    if not CLAUDE_PROJECTS_DIR.exists():
        log.error(f"Claude projects dir not found: {CLAUDE_PROJECTS_DIR}")
        sys.exit(1)

    log.info(f"Starting Unfry daemon. Watching: {CLAUDE_PROJECTS_DIR}")

    # Initialize tracker for all existing JSONL files
    for jsonl in CLAUDE_PROJECTS_DIR.rglob("*.jsonl"):
        line_count = sum(1 for _ in open(jsonl, encoding="utf-8"))
        tracker.update(str(jsonl), line_count)

    log.info(f"Tracking {len(list(CLAUDE_PROJECTS_DIR.rglob('*.jsonl')))} existing sessions")

    observer = Observer()
    observer.schedule(JasonlHandler(), str(CLAUDE_PROJECTS_DIR), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        log.info("Stopping Unfry daemon.")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
