---
title: ActivityWatch Export — last ~64h (Berlin TZ, refreshed)
date: 2026-05-29
source: ActivityWatch localhost:5600 (4 buckets: window/afk/chrome/...)
range_utc: 2026-05-26T22:00Z → 2026-05-29T14:00Z
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — last 2 days timeline

**Counts:** 782 window / 362 chrome / 126 afk events. **Sessions ≥30s:** 134.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-27 | 6h00m | 3h55m | 60h40m |
| 2026-05-28 | 5h49m | 2h07m | 55h50m |
| 2026-05-29 | 3m31s | 3m53s | 0s |

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
| `Code.exe` | 5h01m |
| `claude.exe` | 29m55s |
| `Telegram.exe` | 11m07s |
| `chrome.exe` | 4m57s |
| `explorer.exe` | 1m28s |

### 2026-05-29

| App | Time |
|---|---|
| `Code.exe` | 2m58s |
| `claude.exe` | 33s |

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
| www.notion.so | 3h16m |
| open.spotify.com | 3m22s |
| track.toggl.com | 2m52s |
| newtab | 1m15s |

### 2026-05-29

| Domain | Time |
|---|---|
| www.notion.so | 1m28s |
| newtab | 8s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
