---
title: ActivityWatch Export — last ~24h (Berlin TZ)
date: 2026-05-21
source: ActivityWatch localhost:5600 (3 buckets: window/afk/chrome)
range_utc: 2026-05-20T11:00Z → 2026-05-21T11:00Z
range_berlin: 2026-05-20 13:00 → 2026-05-21 13:00 CEST
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — last ~24h timeline (20.05 afternoon → 21.05 noon)

**Counts:** 1072 window / 486 chrome / 143 afk events. **Sessions ≥30s:** 164.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-20 | 6h36m | 4h47m | 9h24m |
| 2026-05-21 | 2h20m | 1h42m | 6h04m |

## §2 Top apps per day

### 2026-05-20

| App | Time |
|---|---|
| `chrome.exe` | 2h32m |
| `claude.exe` | 1h48m |
| `Code.exe` | 1h17m |
| `Telegram.exe` | 33m09s |
| `Antigravity.exe` | 14m46s |
| `Antigravity IDE.exe` | 6m11s |
| `Antigravity IDE.tmp` | 2m40s |
| `explorer.exe` | 43s |

### 2026-05-21

| App | Time |
|---|---|
| `Telegram.exe` | 1h10m |
| `chrome.exe` | 47m54s |
| `claude.exe` | 12m04s |
| `ShellHost.exe` | 8m43s |
| `explorer.exe` | 1m46s |

## §3 Top Chrome domains per day

### 2026-05-20

| Domain | Time |
|---|---|
| open.spotify.com | 1h25m |
| newtab | 21m39s |
| claude.ai | 21m15s |
| platform.claude.com | 13m41s |
| play.google.com | 5m28s |
| v32.skladchik.org | 4m59s |
| www.notion.so | 3m50s |
| id212.skladchik.org | 3m17s |
| track.toggl.com | 2m49s |
| pay.0xprocessing.com | 2m30s |
| mail.google.com | 2m06s |
| ridero.ru | 2m04s |
| www.google.com | 1m42s |
| disk.yandex.by | 1m32s |
| allanviro.online | 1m15s |

### 2026-05-21

| Domain | Time |
|---|---|
| claude.ai | 14m18s |
| track.toggl.com | 1m05s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
