#!/bin/bash
set -e
DATE=$(date +%Y-%m-%d)
LOG_DIR="logs/$DATE"
mkdir -p "$LOG_DIR"
echo "[$DATE $(date +%H:%M)] Evening pipeline started" >> "$LOG_DIR/evening.log"

# 1. Manager collects and reports
claude --agent manager \
  --message "Evening pipeline: collect all agent reports from mailboxes. Update Notion Daily Log 'Что сделано'. Update project 'Лог работы'. Update active-projects.json and metrics." \
  >> "$LOG_DIR/evening.log" 2>&1

# 2. Git commit
cd "$(dirname "$0")/.."
git add -A
git commit -m "[system] daily auto-commit: $DATE" || true
git push origin main 2>/dev/null || true

echo "[$DATE $(date +%H:%M)] Evening pipeline completed" >> "$LOG_DIR/evening.log"
