#!/usr/bin/env bash
# Sync inbox/ from local Windows to server via rsync over Tailscale SSH.
# Server then processes inbox and pushes converted Markdown to git.
#
# Usage: bash tools/convert/sync_to_server.sh
#
# Prerequisites:
#   - SSH key configured for ruslan@100.99.156.28 (Tailscale)
#   - rsync available (Git Bash has it on Windows)

set -eu

SERVER_USER="ruslan"
SERVER_HOST="100.99.156.28"
SERVER_PATH="/home/ruslan/jetix-os/inbox"

REPO_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
cd "$REPO_ROOT"

LOCAL_INBOX="inbox"

if [ ! -d "$LOCAL_INBOX" ]; then
    echo "❌ $LOCAL_INBOX does not exist. Run scrape_blogs.sh first + положи PDFs вручную."
    exit 1
fi

SIZE=$(du -sh "$LOCAL_INBOX" 2>/dev/null | cut -f1)
COUNT=$(find "$LOCAL_INBOX" -type f 2>/dev/null | wc -l)

echo "=== Sync inbox to server ==="
echo "Local: $LOCAL_INBOX ($SIZE, $COUNT files)"
echo "Server: $SERVER_USER@$SERVER_HOST:$SERVER_PATH"
echo ""

# Check SSH first
if ! ssh -o ConnectTimeout=10 -o BatchMode=yes "$SERVER_USER@$SERVER_HOST" "echo ok" 2>/dev/null; then
    echo "⚠️  SSH to $SERVER_HOST failed. Check:"
    echo "   1. Tailscale active?  (tailscale status)"
    echo "   2. SSH key configured?  (ssh-add -l)"
    echo "   3. Server online?"
    exit 1
fi

echo "SSH OK. Starting rsync..."
echo ""

# Rsync with progress
rsync -av --progress \
    --exclude=".DS_Store" --exclude="Thumbs.db" --exclude="*.tmp" \
    "$LOCAL_INBOX/" \
    "$SERVER_USER@$SERVER_HOST:$SERVER_PATH/"

echo ""
echo "=== Sync complete ==="
echo ""
echo "NEXT STEP — на сервере запустить Claude Code:"
echo ""
echo "  ssh $SERVER_USER@$SERVER_HOST"
echo "  tmux new -s convert"
echo "  cd ~/jetix-os"
echo "  git pull origin claude/jolly-margulis-915d34"
echo "  claude --dangerously-skip-permissions"
echo ""
echo "Внутри Claude paste prompt из файла:"
echo "  tools/convert/server_task.md"
