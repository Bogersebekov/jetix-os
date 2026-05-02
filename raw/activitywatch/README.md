---
title: ActivityWatch storage directory
type: data_source
created: 2026-05-02
---

# ActivityWatch — local time-tracking data

Этот директорий — destination для daily ActivityWatch exports с Windows-машины.
Local-first storage, потом aggregated в `reports/activity_YYYY-MM-DD.md`.

## Структура

```
raw/activitywatch/
├── README.md                       (this file, committed)
├── json/                           (.gitignored — raw data sensitive)
│   ├── 2026-05-02.json            (daily export, ~MB-tier)
│   ├── 2026-05-03.json
│   └── ...
└── archive/                        (.gitignored — old exports >90d)
    └── ...
```

## Pipeline

1. **Windows side** (`tools/export_activitywatch.ps1`):
   - Runs daily at 23:55 (Windows Task Scheduler)
   - Calls `http://localhost:5600/api/0/buckets/.../events` for each bucket
   - Saves JSON locally to `%LOCALAPPDATA%\activitywatch-export\YYYY-MM-DD.json`
   - scp uploads to server `~/jetix-os/raw/activitywatch/json/`
   - Triggers `tools/aggregate_activity.py YYYY-MM-DD` on server

2. **Server aggregation** (`tools/aggregate_activity.py`):
   - Reads `raw/activitywatch/json/YYYY-MM-DD.json`
   - Categorises events (deep_work / communication / research / social / off_topic / afk)
   - Generates `reports/activity_YYYY-MM-DD.md` markdown with:
     - Total active time / AFK time / ratio
     - Time per category
     - Top 20 apps by time
     - Top 20 URLs (domains) by time

3. **Daily Log integration** (manual для Phase 1):
   - Ruslan reviews `reports/activity_YYYY-MM-DD.md` в EOD section Daily Log
   - Future Phase 2: auto-append через Notion API

## Privacy / .gitignore

JSON exports содержат **all URLs + window titles** — sensitive (passwords в URLs, personal sites, etc.).

`.gitignore` excludes:
- `raw/activitywatch/json/` (raw data)
- `raw/activitywatch/archive/` (rotated old data)

Aggregated reports в `reports/activity_*.md` — committed (no raw URLs, only categorised + top-20 domains).

## Server access

- Tailscale: `ssh ruslan@100.99.156.28`
- Repo: `~/jetix-os`
- Branch: server-side work obычно `claude/jolly-margulis-915d34`

## Manual operations

**Run aggregation manually:**
```bash
cd ~/jetix-os
python3 tools/aggregate_activity.py 2026-05-02
```

**Force re-aggregate last 7 days:**
```bash
python3 tools/aggregate_activity.py --last-7
```

**Inspect raw JSON:**
```bash
jq '.buckets | keys' raw/activitywatch/json/2026-05-02.json
jq '.buckets["aw-watcher-window_*"].events | length' raw/activitywatch/json/2026-05-02.json
```

## Categorization

Heuristic rules в `tools/aggregate_activity.py:CATEGORIES`. Extend as needed:
- **deep_work** — Claude / Antigravity / Code editors / Terminal / Notion / Miro
- **communication** — Telegram / Discord / Slack / Email
- **research** — GitHub / StackOverflow / Anthropic docs / YouTube watch / Wikipedia
- **social** — Twitter / Instagram / Reddit / TikTok
- **off_topic** — YouTube (non-watch) / Netflix / Spotify / Twitch
- **afk** — idle periods (per ActivityWatch AFK detector)
- **uncategorized** — fallback (review and add rules)

## Future enhancements (Phase 2+)

- Manual session start/stop via AutoHotkey + REST API events
- Auto-append summary to Notion Daily Log via API
- Cross-day analytics (weekly / monthly trends)
- Goal vs actual: planned focus blocks vs measured time
- AI-generated insight: «You spent 2h on YouTube on Tue when goal was research — pivot?»
