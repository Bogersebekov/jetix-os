#!/usr/bin/env bash
# Fetch full channel via Invidious API with continuation-token pagination.
# Usage: fetch_iv.sh <channel_id> <output.jsonl>
set -euo pipefail

CHANNEL_ID="${1:?channel_id required}"
OUT="${2:?output path required}"
INSTANCE="${INV_INSTANCE:-https://invidious.materialio.us}"
FALLBACK="${INV_FALLBACK:-https://invidious.darkness.services}"

> "$OUT"
cont=""
page=0
total=0
while :; do
  page=$((page+1))
  if [ -z "$cont" ]; then
    url="${INSTANCE}/api/v1/channels/${CHANNEL_ID}/videos"
  else
    url="${INSTANCE}/api/v1/channels/${CHANNEL_ID}/videos?continuation=${cont}"
  fi
  body=$(curl -s -m 15 "$url" || true)
  if [ -z "$body" ]; then
    echo "page=$page primary empty, trying fallback" >&2
    if [ -z "$cont" ]; then
      url="${FALLBACK}/api/v1/channels/${CHANNEL_ID}/videos"
    else
      url="${FALLBACK}/api/v1/channels/${CHANNEL_ID}/videos?continuation=${cont}"
    fi
    body=$(curl -s -m 15 "$url" || true)
  fi
  if [ -z "$body" ]; then
    echo "page=$page both instances failed" >&2
    break
  fi
  cnt=$(echo "$body" | python3 -c "import sys,json
try:
  d=json.load(sys.stdin)
  vs=d.get('videos',[])
  for v in vs: print(json.dumps(v, ensure_ascii=False))
  sys.stderr.write(str(len(vs))+'|'+(d.get('continuation') or '')+'\n')
except Exception as e:
  sys.stderr.write('parse_err:'+str(e)+'\n')
" 2>/tmp/iv_meta.txt >> "$OUT")
  meta=$(cat /tmp/iv_meta.txt)
  c=$(echo "$meta" | cut -d'|' -f1)
  cont=$(echo "$meta" | cut -d'|' -f2)
  total=$((total + ${c:-0}))
  echo "page=$page count=$c total=$total cont_len=${#cont}" >&2
  if [ -z "$cont" ] || [ "${c:-0}" = "0" ]; then
    break
  fi
  if [ "$page" -ge 20 ]; then
    echo "WARN: hit page limit 20" >&2
    break
  fi
  sleep 1
done
echo "DONE total=$total" >&2
