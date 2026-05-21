---
name: Toggl push command — 2026-05-20 → 2026-05-21
description: 11 entries 20.05 12:50 → 21.05 13:30 (Ruslan dictation; ActivityWatch substrate cross-ref 2026-05-21-export)
created: 2026-05-21
status: READY-TO-PUSH
---

# Команда для server CC (или Windows local)

## TL;DR

11 entries за 20.05 12:50 → 21.05 13:30 (~24h40m, с gap 20:40-21:40 не зафиксирован — Ruslan «я не знаю»).

JSON: `tools/toggl-entries-2026-05-20-21.json`.

## Breakdown по проектам

| Project | Total time | Entries |
|---|---|---|
| Deep Work | 9h20m | 2 (обработка заметок Левенчук+Цэрэн 7h50m + созвон с Владом 1h30m) |
| Сон | 6h50m | 1 |
| Рутина | 5h | 4 (20m + 10m + 3h40m + 50m) |
| Отдых | 2h10m | 3 (Ибро 1h + Влад 30m + 40m) |
| Зарядка | 20m | 1 |

**Gap:** 20:40-21:40 (1h) — Ruslan «не знаю чё там», skipped — допишет в Toggl GUI если вспомнит.

## Запуск (в repo root)

```bash
cd ~/Desktop/jetix-os
PYTHONIOENCODING=utf-8 python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-20-21.json
```

(`PYTHONIOENCODING=utf-8` обязательно для русских tags на Windows.)

## Pre-flight verify

```bash
PYTHONIOENCODING=utf-8 python3 -c "
import json
from datetime import datetime
with open('tools/toggl-entries-2026-05-20-21.json') as f:
    entries = json.load(f)
prev = None
for e in entries:
    s = datetime.fromisoformat(e['start'])
    t = datetime.fromisoformat(e['stop'])
    dur = (t - s).total_seconds() / 60
    print(f\"{s.strftime('%d.%m %H:%M')}-{t.strftime('%d.%m %H:%M')} ({int(dur)}m) {e['project']:10s} {','.join(e['tags']):30s} {e['description']}\")
    if prev and s < prev:
        print('  ⚠️ OVERLAP с предыдущим')
    prev = t
"
```

## Cross-ref ActivityWatch substrate

- `raw/activitywatch/2026-05-21-export/timeline-2026-05-20.md` — вечер 20.05 (после 13:00)
- `raw/activitywatch/2026-05-21-export/timeline-2026-05-21.md` — сегодня до 13:00
