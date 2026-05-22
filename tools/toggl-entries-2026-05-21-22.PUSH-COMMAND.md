---
name: Toggl push command — 2026-05-21 → 2026-05-22
description: 10 entries 21.05 13:30 → 22.05 11:30 (Ruslan dictation 22.05 evening; cross-ref AW export 2026-05-22-export)
created: 2026-05-22
status: READY-TO-PUSH
---

# Команда для server CC (или local)

## TL;DR

10 entries за 21.05 13:30 → 22.05 11:30 (~22h spans with 2 gaps: 19:20-19:30 + 20:10-20:30 = 30m total).

JSON: `tools/toggl-entries-2026-05-21-22.json`

## Breakdown по проектам

| Project | Total | Entries |
|---|---|---|
| Deep Work | 10h | 3 (сбор идей + созвон 3h30m / метод deep description 2h / обработка заметок 4h30m) |
| Рутина | 4h50m | 3 (Zip тест 40m / утренняя 20m / работа тупая 3h50m) |
| Сон | 5h | 1 |
| Отдых | 1h20m | 2 (отдых 20m / кушал 1h) |
| Зарядка | 20m | 1 |

**Gaps:** 19:20-19:30 (10m) + 20:10-20:30 (20m) = 30m skipped.

## Запуск (в repo root)

```bash
cd ~/Desktop/jetix-os
PYTHONIOENCODING=utf-8 python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-21-22.json
```

(`PYTHONIOENCODING=utf-8` обязательно для русских tags.)

## Pre-flight verify

```bash
PYTHONIOENCODING=utf-8 python3 -c "
import json
from datetime import datetime
with open('tools/toggl-entries-2026-05-21-22.json', encoding='utf-8') as f:
    entries = json.load(f)
prev = None
total = 0
for e in entries:
    s = datetime.fromisoformat(e['start'])
    t = datetime.fromisoformat(e['stop'])
    dur = (t - s).total_seconds() / 60
    total += dur
    print(f\"{s.strftime('%d.%m %H:%M')}-{t.strftime('%d.%m %H:%M')} ({int(dur)}m) {e['project']:10s} {','.join(e['tags']):30s} {e['description']}\")
    if prev and s < prev:
        print('  WARN OVERLAP')
    prev = t
print(f'TOTAL: {int(total)}m = {int(total/60)}h{int(total%60)}m / {len(entries)} entries')
"
```

## Cross-ref ActivityWatch

- `raw/activitywatch/2026-05-22-export/timeline-2026-05-21.md` — substrate для 21.05 (Deep Work blocks Code.exe + claude.exe activity)
- `raw/activitywatch/2026-05-22-export/timeline-2026-05-22.md` — substrate для 22.05 morning
