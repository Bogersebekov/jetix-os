---
title: ActivityWatch Export — last ~40h (Berlin TZ)
date: 2026-05-28
source: ActivityWatch localhost:5600 (4 buckets: window/afk/chrome/...)
range_utc: 2026-05-26T22:00Z → 2026-05-28T13:45Z
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — last 2 days timeline

**Counts:** 672 window / 296 chrome / 80 afk events. **Sessions ≥30s:** 110.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-27 | 6h00m | 3h55m | 60h40m |
| 2026-05-28 | 1h32m | 1h38m | 24h27m |

## §2 Top apps per day

### 2026-05-27

| App | Time |
|---|---|
| `chrome.exe` | 2h05m |
| `Telegram.exe` | 1h34m |
| `claude.exe` | 1h13m |
| `Code.exe` | 1h03m |
| `explorer.exe` | 2m59s |
| `WindowsTerminal.exe` | 1m04s |

### 2026-05-28

| App | Time |
|---|---|
| `Code.exe` | 1h11m |
| `claude.exe` | 11m55s |
| `chrome.exe` | 3m53s |
| `Telegram.exe` | 3m38s |
| `explorer.exe` | 1m28s |

## §3 Top Chrome domains per day

### 2026-05-27

| Domain | Time |
|---|---|
| track.toggl.com | 1h18m |
| www.notion.so | 18m08s |
| console.hetzner.com | 13m37s |
| www.youtube.com | 6m11s |
| oejgccbfbmkkpaidnkphaiaecficdnfn | 2m29s |
| open.spotify.com | 2m20s |
| newtab | 1m23s |
| github.com | 7s |

### 2026-05-28

| Domain | Time |
|---|---|
| www.notion.so | 14m14s |
| open.spotify.com | 3m22s |
| newtab | 1m15s |
| track.toggl.com | 15s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
