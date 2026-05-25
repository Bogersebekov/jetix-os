---
title: ActivityWatch Export — 24-25.05.2026 (Berlin TZ)
date: 2026-05-25
source: ActivityWatch localhost:5600 (3 active buckets: window/afk/chrome)
range_utc: 2026-05-23T22:00Z → 2026-05-25T21:59Z
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — 24-25.05.2026 timeline

**Counts:** 1242 window / 709 chrome / 181 afk events. **Sessions ≥30s:** 252.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-24 | 11h51m | 7h48m | 19h43m |
| 2026-05-25 | 1h30m | 20m45s | 21h06m |

## §2 Top apps per day

### 2026-05-24

| App | Time |
|---|---|
| `Code.exe` | 5h34m |
| `chrome.exe` | 3h10m |
| `claude.exe` | 2h44m |
| `explorer.exe` | 10m31s |
| `Telegram.exe` | 9m33s |
| `Wispr Flow.exe` | 59s |

### 2026-05-25

| App | Time |
|---|---|
| `chrome.exe` | 1h10m |
| `Code.exe` | 9m54s |
| `claude.exe` | 8m22s |
| `explorer.exe` | 52s |
| `ShellHost.exe` | 37s |

## §3 Top Chrome domains per day

### 2026-05-24

| Domain | Time |
|---|---|
| newtab | 1h41m |
| www.youtube.com | 59m53s |
| github.com | 34m25s |
| open.spotify.com | 29m20s |
| www.google.com | 28m42s |
| uakinogo.org | 12m37s |
| www.notion.so | 10m59s |
| erotik.markt.de | 7m03s |
| oceanofpdf.com | 5m22s |
| track.toggl.com | 3m26s |
| vetalroots.online | 3m05s |
| videochatru.com | 1m19s |
| base44.com | 1m13s |
| saomi.site | 1m12s |
| file:///D:/Downloads/peer-instruction-a-users-manu | 1m08s |

### 2026-05-25

| Domain | Time |
|---|---|
| uakinogo.org | 5m19s |
| open.spotify.com | 2m30s |
| newtab | 46s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
