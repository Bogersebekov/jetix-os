---
title: ActivityWatch Export — last ~60h (Berlin TZ)
date: 2026-05-20
source: ActivityWatch localhost:5600 (4 buckets: window/afk/chrome/...)
range_utc: 2026-05-17T22:00Z → 2026-05-20T11:00Z
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — last 2 days timeline

**Counts:** 108 window / 133 chrome / 59 afk events. **Sessions ≥30s:** 30.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-26 | 3h43m | 1h34m | 14h30m |

## §2 Top apps per day

### 2026-05-26

| App | Time |
|---|---|
| `chrome.exe` | 2h17m |
| `Code.exe` | 50m05s |
| `claude.exe` | 19m05s |
| `Telegram.exe` | 15m57s |
| `ShellHost.exe` | 42s |

## §3 Top Chrome domains per day

### 2026-05-26

| Domain | Time |
|---|---|
| github.com | 36m09s |
| www.notion.so | 13m09s |
| uakinogo.org | 3m52s |
| open.spotify.com | 1m19s |
| track.toggl.com | 1m03s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
