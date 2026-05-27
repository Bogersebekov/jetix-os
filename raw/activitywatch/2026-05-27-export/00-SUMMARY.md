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

**Counts:** 272 window / 60 chrome / 32 afk events. **Sessions ≥30s:** 28.

## §1 Per-day active vs AFK

| Day | Active (window sessions ≥30s) | not-afk (mouse/keyboard) | afk (idle) |
|---|---|---|---|
| 2026-05-27 | 1h19m | 1h02m | 42h04m |

## §2 Top apps per day

### 2026-05-27

| App | Time |
|---|---|
| `Code.exe` | 36m56s |
| `claude.exe` | 35m58s |
| `explorer.exe` | 2m28s |
| `chrome.exe` | 1m36s |
| `WindowsTerminal.exe` | 1m04s |
| `Telegram.exe` | 1m02s |

## §3 Top Chrome domains per day

### 2026-05-27

| Domain | Time |
|---|---|
| www.notion.so | 13m59s |
| console.hetzner.com | 13m37s |

## §4 Files in this export

- `00-SUMMARY.md` — this file (per-day app/chrome/AFK totals)
- `timeline-YYYY-MM-DD.md` — per-day chronological sessions ≥30s (window + chrome merged) ⭐
- `chrome-by-day.md` — full Chrome URLs per day with titles
- `apps-by-day.md` — full apps breakdown с window titles per day
- `window-events.json` / `chrome-events.json` / `afk-events.json` — raw ActivityWatch exports
- `buckets-metadata.json` — bucket meta
- `aggregate.py` — this aggregation script
