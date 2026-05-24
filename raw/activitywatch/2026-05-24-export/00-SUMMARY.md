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

**Counts:** 1444 window / 720 chrome / 126 afk events. **Sessions ≥30s:** 158.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-23 | 6h39m | 3h18m | 8h37m |
| 2026-05-24 | 3h21m | 2h08m | 6h40m |

## §2 Top apps per day

### 2026-05-23

| App | Time |
|---|---|
| `Code.exe` | 3h01m |
| `chrome.exe` | 2h08m |
| `claude.exe` | 1h15m |
| `Telegram.exe` | 13m50s |
| `explorer.exe` | 31s |

### 2026-05-24

| App | Time |
|---|---|
| `Code.exe` | 1h32m |
| `chrome.exe` | 57m40s |
| `claude.exe` | 51m26s |

## §3 Top Chrome domains per day

### 2026-05-23

| Domain | Time |
|---|---|
| www.notion.so | 2h00m |
| github.com | 47m19s |
| www.google.com | 31m54s |
| oceanofpdf.com | 18m50s |
| open.spotify.com | 7m30s |
| newtab | 5m23s |
| web.krao.kg | 3m17s |
| degital5.com | 2m43s |
| www.instagram.com | 2m38s |
| www.academia.edu | 2m25s |
| file:///D:/Downloads/_OceanofPDF.com_The_WEIRDest_ | 2m17s |
| thenetworkstate.com | 2m14s |
| saomi.site | 2m08s |
| monoskop.org | 1m49s |
| file:///D:/Downloads/_OceanofPDF.com_Frogs_Into_Pr | 1m42s |

### 2026-05-24

| Domain | Time |
|---|---|
| newtab | 58m20s |
| www.youtube.com | 25m48s |
| open.spotify.com | 16m02s |
| www.google.com | 2m |
| github.com | 1m40s |
| base44.com | 1m13s |
| v2.auth.mistral.ai | 1m07s |
| boosty.to | 53s |
| console.mistral.ai | 47s |
| mistral.ai | 32s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
