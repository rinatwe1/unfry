#!/bin/bash

# session-end.sh
# Claude Session Log — Stop Hook
#
# This script runs when Claude Code stops (via Stop hook in settings.json).
# It writes a basic session marker so you never lose track of when sessions happened,
# even if you forgot to run /log.
#
# This is NOT a full summary — that's Claude's job via /log.
# This just ensures a timestamp record exists.
#
# Setup (add to Claude Code settings.json):
# {
#   "hooks": {
#     "Stop": [{
#       "matcher": "",
#       "hooks": [{
#         "type": "command",
#         "command": "/path/to/claude-session-log/hooks/session-end.sh"
#       }]
#     }]
#   }
# }

set -e

# Configuration
SESSIONS_DIR="$(dirname "$(dirname "$0")")/sessions"
MARKER_FILE="$SESSIONS_DIR/.last-session"

# Create sessions dir if it doesn't exist
mkdir -p "$SESSIONS_DIR"

# Get current info
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
DATE=$(date "+%Y-%m-%d")
WORKING_DIR="${PWD:-unknown}"
PROJECT=$(basename "$WORKING_DIR")

# Write marker file (overwrite each time)
cat > "$MARKER_FILE" << EOF
last_session: $TIMESTAMP
working_dir: $WORKING_DIR
project_guess: $PROJECT
log_written: false
EOF

# Also append to session history (one line per session)
HISTORY_FILE="$SESSIONS_DIR/.session-history"
echo "$TIMESTAMP | $WORKING_DIR" >> "$HISTORY_FILE"

# Print a reminder (shown in Claude Code terminal if hooks output is visible)
echo "[Claude Session Log] Session ended at $TIMESTAMP"
echo "[Claude Session Log] Working directory: $WORKING_DIR"
echo "[Claude Session Log] Remember to run /log if this was a meaningful session!"
echo "[Claude Session Log] Marker written to: $MARKER_FILE"

exit 0
