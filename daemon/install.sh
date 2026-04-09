#!/bin/bash
# Unfry Daemon Installer
# Installs the background daemon that auto-summarizes Claude Code sessions

set -e

DAEMON_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_NAME="com.unfry.daemon"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
PLIST_DEST="$LAUNCH_AGENTS_DIR/$PLIST_NAME.plist"
UNFRY_DIR="$HOME/.unfry"

echo "=== Unfry Daemon Installer ==="
echo ""

# Check Python
PYTHON=$(which python3)
if [ -z "$PYTHON" ]; then
    echo "Error: python3 not found. Please install Python 3."
    exit 1
fi
echo "✓ Python: $PYTHON"

# Check Claude CLI
if ! command -v claude &> /dev/null; then
    echo "Error: 'claude' CLI not found. Is Claude Code installed?"
    exit 1
fi
echo "✓ Claude CLI: $(which claude)"

# Install watchdog
echo ""
echo "Installing dependencies..."
pip3 install watchdog --quiet
echo "✓ watchdog installed"

# Create ~/.unfry directory for logs
mkdir -p "$UNFRY_DIR"
echo "✓ Created $UNFRY_DIR"

# Generate the plist from template
echo ""
echo "Installing LaunchAgent..."
mkdir -p "$LAUNCH_AGENTS_DIR"

sed \
    -e "s|PYTHON_PATH_PLACEHOLDER|$PYTHON|g" \
    -e "s|DAEMON_PATH_PLACEHOLDER|$DAEMON_DIR/daemon.py|g" \
    -e "s|HOME_PLACEHOLDER|$HOME|g" \
    -e "s|DAEMON_DIR_PLACEHOLDER|$DAEMON_DIR|g" \
    "$DAEMON_DIR/com.unfry.daemon.plist" > "$PLIST_DEST"

echo "✓ Plist written to $PLIST_DEST"

# Load the agent
if launchctl list | grep -q "$PLIST_NAME"; then
    echo "Stopping existing daemon..."
    launchctl unload "$PLIST_DEST" 2>/dev/null || true
fi

launchctl load "$PLIST_DEST"
echo "✓ Daemon started"

echo ""
echo "=== Done! ==="
echo ""
echo "Unfry is now running in the background."
echo "  • Logs:  $UNFRY_DIR/daemon.log"
echo "  • Auto-summarizes on: compact events + 30min inactivity"
echo "  • Summaries saved to: [project-dir]/unfry-sessions/"
echo ""
echo "To stop:   launchctl unload $PLIST_DEST"
echo "To check:  tail -f $UNFRY_DIR/daemon.log"
