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

**Counts:** 1551 window / 682 chrome / 218 afk events. **Sessions ≥30s:** 280.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-18 | 6h19m | 4h03m | 23h00m |
| 2026-05-19 | 7h53m | 4h46m | 25h36m |
| 2026-05-20 | 35m42s | 14m47s | 4h26m |

## §2 Top apps per day

### 2026-05-18

| App | Time |
|---|---|
| `Antigravity.exe` | 2h39m |
| `claude.exe` | 2h02m |
| `chrome.exe` | 1h26m |
| `Telegram.exe` | 9m34s |
| `explorer.exe` | 1m01s |
| `WindowsTerminal.exe` | 52s |

### 2026-05-19

| App | Time |
|---|---|
| `claude.exe` | 2h42m |
| `Antigravity.exe` | 2h17m |
| `chrome.exe` | 1h57m |
| `Telegram.exe` | 55m18s |
| `explorer.exe` | 38s |

### 2026-05-20

| App | Time |
|---|---|
| `claude.exe` | 31m |
| `chrome.exe` | 1m19s |
| `Antigravity.exe` | 1m11s |
| `Photos.exe` | 53s |
| `Telegram.exe` | 45s |
| `explorer.exe` | 35s |

## §3 Top Chrome domains per day

### 2026-05-18

| Domain | Time |
|---|---|
| www.youtube.com | 1h15m |
| track.toggl.com | 29m23s |
| open.spotify.com | 24m48s |
| www.notion.so | 11m23s |
| www.sapienship.co | 1m40s |
| claude.ai | 51s |
| newtab | 41s |
| www.google.com | 37s |

### 2026-05-19

| Domain | Time |
|---|---|
| www.youtube.com | 1h35m |
| newtab | 38m36s |
| www.notion.so | 8m13s |
| open.spotify.com | 4m11s |
| www.olx.ua | 4m02s |
| www.instagram.com | 2m54s |
| track.toggl.com | 1m49s |
| platform.claude.com | 1m29s |
| account.ama1984.com | 1m14s |
| braginskyoleg.com | 1m06s |
| claude.ai | 56s |
| www.google.com | 42s |
| shop.ama1984.com | 41s |
| history | 6s |

### 2026-05-20

| Domain | Time |
|---|---|
| www.youtube.com | 13m12s |
| track.toggl.com | 2m57s |
| history | 2m13s |
| open.spotify.com | 9s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
