#!/bin/bash
# Usage: ./rollback.sh <agent-name> <version>
AGENT=$1; VERSION=$2
DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ)

if [ -z "$AGENT" ] || [ -z "$VERSION" ]; then
  echo "Usage: ./rollback.sh <agent-name> <version>"
  exit 1
fi

SRC="agents/$AGENT/versions/$VERSION.md"
DEST=".claude/agents/$AGENT.md"

if [ ! -f "$SRC" ]; then
  echo "ERROR: $SRC not found"
  exit 1
fi

cp "$SRC" "$DEST"
echo "{\"date\":\"$DATE\",\"agent\":\"$AGENT\",\"action\":\"rollback\",\"to_version\":\"$VERSION\"}" \
  >> "agents/$AGENT/versions/changelog.jsonl"

echo "Rolled back $AGENT to $VERSION"
