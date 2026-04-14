#!/bin/bash
set -e
DATE=$(date +%Y-%m-%d)
LOG_DIR="logs/$DATE"
mkdir -p "$LOG_DIR"
echo "[$DATE $(date +%H:%M)] Morning pipeline started" >> "$LOG_DIR/morning.log"

# 1. System health
claude --agent system-admin \
  --message "Run health check → shared/state/system-health.json" \
  >> "$LOG_DIR/morning.log" 2>&1

# 2. Process inbox
claude --agent inbox-processor \
  --message "Process all items in inbox/. Route to appropriate mailboxes." \
  >> "$LOG_DIR/morning.log" 2>&1

# 3. Manager creates briefing
claude --agent manager \
  --message "Morning pipeline: read mailbox, read Notion Daily Log, check active-projects. Generate daily-briefing.json. Distribute tasks." \
  >> "$LOG_DIR/morning.log" 2>&1

echo "[$DATE $(date +%H:%M)] Morning pipeline completed" >> "$LOG_DIR/morning.log"
