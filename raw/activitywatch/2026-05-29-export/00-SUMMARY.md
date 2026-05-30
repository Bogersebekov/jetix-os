---
title: ActivityWatch Export — 2026-05-29 full day (Berlin TZ)
date: 2026-05-29
source: ActivityWatch localhost:5600 (window/afk/chrome buckets)
range_utc: 2026-05-28T22:00Z → 2026-05-29T22:30Z
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — 2026-05-29 full day

**Counts:** 381 window / 161 chrome / 48 afk events. **Sessions ≥30s:** 67.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-29 | 2h52m | 1h55m | 29h23m |

## §2 Top apps per day

### 2026-05-29

| App | Time |
|---|---|
| `Code.exe` | 1h09m |
| `claude.exe` | 50m36s |
| `chrome.exe` | 42m58s |
| `Telegram.exe` | 7m46s |
| `Acrobat.exe` | 1m47s |

## §3 Top Chrome domains per day

### 2026-05-29

| Domain | Time |
|---|---|
| track.toggl.com | 14m25s |
| app.notion.com | 13m40s |
| www.notion.so | 4m32s |
| claude.ai | 3m49s |
| newtab | 3m34s |
| www.instagram.com | 2m23s |
| history | 31s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
