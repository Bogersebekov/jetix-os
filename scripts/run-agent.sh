#!/bin/bash
# Usage: ./run-agent.sh <agent-name> "<message>"
set -e
AGENT=$1; MESSAGE=$2
DATE=$(date +%Y-%m-%d); TS=$(date +%H%M%S)
LOG_DIR="logs/$DATE"; mkdir -p "$LOG_DIR"

if [ -z "$AGENT" ] || [ -z "$MESSAGE" ]; then
  echo "Usage: ./run-agent.sh <agent-name> \"<message>\""
  exit 1
fi

echo "[$DATE $TS] Running: $AGENT" >> "$LOG_DIR/$AGENT.log"
echo "Message: $MESSAGE" >> "$LOG_DIR/$AGENT.log"

claude --agent "$AGENT" --message "$MESSAGE" >> "$LOG_DIR/$AGENT.log" 2>&1

echo "[$DATE $TS] Completed: $AGENT" >> "$LOG_DIR/$AGENT.log"
