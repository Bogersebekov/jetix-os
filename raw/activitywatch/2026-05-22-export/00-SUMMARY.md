---
title: ActivityWatch Export — last ~22h (Berlin TZ)
date: 2026-05-22
source: ActivityWatch localhost:5600 (3 buckets: window/afk/chrome)
range_utc: 2026-05-21T11:00Z → 2026-05-22T09:30Z
range_berlin: 2026-05-21 13:00 → 2026-05-22 11:30 CEST
hostname: mashinachui
aggregation: sessions = same (app,title) merged with <120s gap, kept if ≥30s
tz: Europe/Berlin (UTC+2 / CEST)
---

# ActivityWatch — last ~22h timeline (21.05 13:00 → 22.05 11:30)

**Counts:** 765 window / 382 chrome / 148 afk events. **Sessions ≥30s:** 186.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-21 | 10h16m | 4h51m | 10h38m |
| 2026-05-22 | 1h17m | 1h17m | 6h35m |

## §2 Top apps per day

### 2026-05-21

| App | Time |
|---|---|
| `Code.exe` | 5h26m |
| `claude.exe` | 2h03m |
| `chrome.exe` | 1h43m |
| `Telegram.exe` | 48m46s |
| `explorer.exe` | 8m44s |
| `ShellExperienceHost.exe` | 5m45s |

### 2026-05-22

| App | Time |
|---|---|
| `chrome.exe` | 44m13s |
| `Code.exe` | 15m29s |
| `claude.exe` | 15m13s |
| `explorer.exe` | 1m20s |
| `Telegram.exe` | 1m11s |

## §3 Top Chrome domains per day

### 2026-05-21

| Domain | Time |
|---|---|
| www.notion.so | 1h43m |
| claude.ai | 55m59s |
| track.toggl.com | 43m50s |
| corpbasis.com | 43m08s |
| newtab | 38m30s |
| open.spotify.com | 3m43s |
| getadblock.com | 1m14s |
| accounts.google.com | 1m |
| mail.google.com | 7s |

### 2026-05-22

| Domain | Time |
|---|---|
| claude.ai | 6m21s |
| www.youtube.com | 2m40s |
| www.notion.so | 2m23s |
| newtab | 1m36s |
| www.deepl.com | 17s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
