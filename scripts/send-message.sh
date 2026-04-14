#!/bin/bash
# Usage: ./send-message.sh <from> <to> <type> <priority> <subject> <body> [project]
set -e

FROM=$1; TO=$2; TYPE=$3; PRIORITY=$4; SUBJECT=$5; BODY=$6; PROJECT=${7:-""}
DATE=$(date +%Y%m%d)
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Auto-increment message ID
COUNTER_FILE="comms/.msg-counter"
if [ -f "$COUNTER_FILE" ]; then
  COUNTER=$(cat "$COUNTER_FILE")
else
  COUNTER=0
fi
COUNTER=$((COUNTER + 1))
echo "$COUNTER" > "$COUNTER_FILE"

MSG_ID="msg-${DATE}-$(printf '%03d' $COUNTER)"

# Build JSON
MSG=$(jq -n \
  --arg id "$MSG_ID" \
  --arg ts "$TIMESTAMP" \
  --arg from "$FROM" \
  --arg to "$TO" \
  --arg type "$TYPE" \
  --arg pri "$PRIORITY" \
  --arg subj "$SUBJECT" \
  --arg body "$BODY" \
  --arg proj "$PROJECT" \
  '{id: $id, timestamp: $ts, from: $from, to: $to, type: $type,
    priority: $pri, subject: $subj, body: $body,
    context: {project: $proj}, status: "pending"}')

# Write to recipient mailbox
MAILBOX="comms/mailboxes/${TO}.jsonl"
echo "$MSG" >> "$MAILBOX"

# If broadcast, write to all mailboxes
if [ "$TO" = "broadcast" ]; then
  for f in comms/mailboxes/*.jsonl; do
    echo "$MSG" >> "$f"
  done
fi

echo "Sent $MSG_ID: $FROM → $TO ($TYPE/$PRIORITY)"
