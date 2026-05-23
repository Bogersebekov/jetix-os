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

**Counts:** 1273 window / 573 chrome / 204 afk events. **Sessions ≥30s:** 209.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-22 | 12h37m | 6h59m | 21h02m |
| 2026-05-23 | 45m19s | 40m42s | 3h16m |

## §2 Top apps per day

### 2026-05-22

| App | Time |
|---|---|
| `chrome.exe` | 6h10m |
| `Code.exe` | 3h29m |
| `Telegram.exe` | 1h34m |
| `claude.exe` | 1h08m |
| `Loom.exe` | 7m23s |
| `iVCam.exe` | 2m36s |
| `WindowsTerminal.exe` | 2m13s |
| `explorer.exe` | 1m20s |
| `cmd.exe` | 44s |

### 2026-05-23

| App | Time |
|---|---|
| `chrome.exe` | 30m09s |
| `Notepad.exe` | 12m49s |
| `claude.exe` | 1m43s |
| `Telegram.exe` | 39s |

## §3 Top Chrome domains per day

### 2026-05-22

| Domain | Time |
|---|---|
| newtab | 2h45m |
| miro.com | 37m14s |
| track.toggl.com | 33m34s |
| console.hetzner.com | 13m27s |
| claude.ai | 7m36s |
| www.loom.com | 4m15s |
| docs.google.com | 3m59s |
| open.spotify.com | 3m57s |
| www.notion.so | 3m41s |
| aisystant.system-school.ru | 3m21s |
| github.com | 2m58s |
| www.youtube.com | 2m40s |
| meet.google.com | 1m54s |
| app.fireflies.ai | 1m11s |
| www.mermaidonline.live | 52s |

### 2026-05-23

| Domain | Time |
|---|---|
| aisystant.system-school.ru | 4m08s |
| github.com | 1m14s |
| newtab | 38s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
