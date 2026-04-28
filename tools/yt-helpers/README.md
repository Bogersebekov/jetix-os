---
title: "YouTube research helpers (Invidious-based)"
date: 2026-04-28
type: tooling-readme
parent_track: tseren-tserenov-outreach-analysis
---

# YouTube research helpers

Helper scripts built during Шаг 1.2.2 (Tseren YouTube analysis, 2026-04-28) when
yt-dlp's per-video extraction got blocked by YouTube bot challenge on the Jetix
server IP. Strategy: pull metadata via Invidious public instances API.

## Why these exist

`yt-dlp` per-video extraction triggers YouTube's bot challenge ("Sign in to
confirm you're not a bot") + HTTP 429 rate-limit on shared/datacenter IPs.
`youtube-transcript-api` reports `IpBlocked`. Invidious instances proxy YouTube
metadata (and bypass the bot challenge for most fields) — but their caption
endpoints return empty bodies (downstream YouTube PoT requirement).

## Pipeline

```bash
# 1. Channel listing (full video index, 60/page paginated):
./tools/yt-helpers/fetch_iv.sh <CHANNEL_ID> /tmp/<channel>.jsonl

# 2. Convert to per-video info.json (yt-dlp-compatible schema):
python3 tools/yt-helpers/iv_to_info.py /tmp/<channel>.jsonl raw/research/<dir>/<channel>/

# 3. Enrich with full descriptions + precise dates (parallel, fast):
python3 tools/yt-helpers/enrich_parallel.py raw/research/<dir>/<channel>/ 8

# 4. Top up with serial slow retries (after rate-limit recovery):
python3 tools/yt-helpers/enrich_slow.py raw/research/<dir>/<channel>/ 1.5

# 5. Targeted enrichment for filtered subset (paths via stdin):
cat /tmp/paths-to-enrich.txt | python3 tools/yt-helpers/enrich_targeted.py 2.0

# 6. Run analysis:
python3 tools/analyze_tseren_yt.py raw/research/<dir>/

# 7. (BLOCKED in 2026-04 — captions endpoint empty on all probed instances)
python3 tools/yt-helpers/fetch_captions.py raw/research/<dir>/top-transcripts/ <vid> ...
```

## Known invidious instances (probed 2026-04-28)

| Instance | Channel listing | /videos endpoint | /captions endpoint |
|---|---|---|---|
| invidious.darkness.services | OK | OK | empty body |
| invidious.materialio.us | OK | empty for `/videos` | empty body |
| yt.opnxng.com | unstable | unstable | empty body |
| inv.tux.pizza | unstable | unstable | empty body |

Instance liveness rotates; expect to update `INSTANCES` list in scripts as
public Invidious deployments come and go.

## Limitations

- **Date precision via /channels/.../videos**: relative-text approximation only
  (e.g., "1 year ago" → 2025-04-28). Use `/api/v1/videos/{id}` for precise
  unix timestamp (this is what `enrich_parallel/slow/targeted.py` do).
- **Description truncation via channel listing**: ~110 chars only. Per-video
  endpoint gives full description.
- **Captions blocked**: all probed instances return HTTP 200 + empty body for
  `/api/v1/captions/{id}`. Likely Google's PoT (Proof of Origin Token)
  requirement for timedtext API. Fallback: NotebookLM manual paste, or
  `youtube-transcript-api` from a non-blocked IP / browser-cookied session.
- **Like counts**: usually 0 (YouTube hidden / Invidious unable to extract).
  Not a reliable signal.
- **Failure rate**: ~20-50% of `/api/v1/videos/{id}` calls fail per attempt
  due to instance load, rate limits, or transient errors. Retry pass with
  longer sleeps recovers most.

## Files

- `fetch_iv.sh` — channel paginator (bash + python3 inline)
- `iv_to_info.py` — JSONL → per-video info.json with yt-dlp-compatible keys
- `enrich_parallel.py` — ThreadPoolExecutor enricher (8 workers default)
- `enrich_slow.py` — serial enricher with sleep, for rate-limit recovery
- `enrich_targeted.py` — enrich a specific list of paths (stdin)
- `fetch_captions.py` — caption track downloader (currently blocked, kept
  for future when Invidious caption support recovers)
