#!/bin/bash
# Usage: ./read-mailbox.sh <agent-name> [--pending-only] [--count]
set -e

AGENT=$1
MAILBOX="comms/mailboxes/${AGENT}.jsonl"

if [ -z "$AGENT" ]; then
  echo "Usage: ./read-mailbox.sh <agent-name> [--pending-only] [--count]"
  exit 1
fi

if [ ! -f "$MAILBOX" ]; then
  echo "No mailbox found for: $AGENT"
  exit 1
fi

if [ "$2" = "--count" ]; then
  TOTAL=$(wc -l < "$MAILBOX")
  PENDING=$(grep -c '"status":"pending"' "$MAILBOX" 2>/dev/null || echo 0)
  echo "$AGENT: $TOTAL total, $PENDING pending"
  exit 0
fi

if [ "$2" = "--pending-only" ]; then
  jq -c 'select(.status == "pending")' "$MAILBOX"
else
  jq -c '.' "$MAILBOX"
fi
