---
name: Toggl push command — 2026-05-22 → 2026-05-23
description: 10 entries 22.05 11:45 → 23.05 16:20 (Ruslan dictation 23.05 evening; cross-ref AW export 2026-05-23-export)
created: 2026-05-23
status: READY-TO-PUSH
---

# Команда для local push (Toggl API)

## TL;DR

10 entries за 22.05 11:45 → 23.05 16:20 (~28h35m spans с 1 gap 00:00-00:30 = 30m).

JSON: `tools/toggl-entries-2026-05-22-23.json`

## Breakdown по проектам

| Project | Total | Entries |
|---|---|---|
| Deep Work | 9h | 4 (подготовка к звонку 2h / созвон Дмитрий 2h25m / видео + сбор 3h30m / МИМ изучение 1h10m) |
| Отдых | 3h5m | 2 (после созвона 1h25m / вечерний 1h40m) |
| Сон | 14h10m | 1 |
| Рутина | 1h20m | 2 (утренняя 20m / прогулка обдумывание 1h) |
| Зарядка | 20m | 1 |

**Gap:** 23.05 00:00-00:30 (30m, winding down после МИМ session)

## Запуск (в repo root)

```bash
cd ~/Desktop/jetix-os
PYTHONIOENCODING=utf-8 python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-22-23.json
```

(`PYTHONIOENCODING=utf-8` обязательно для русских tags.)

## Pre-flight verify

```bash
PYTHONIOENCODING=utf-8 python3 -c "
import json
from datetime import datetime
with open('tools/toggl-entries-2026-05-22-23.json', encoding='utf-8') as f:
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

- `raw/activitywatch/2026-05-23-export/timeline-2026-05-22.md` — substrate для 22.05 (Дмитрий звонок + видео запись + МИМ research)
- `raw/activitywatch/2026-05-23-export/timeline-2026-05-23.md` — substrate для 23.05 (рутина + обдумывание)

## Notes

- Сон 14h10m — большой объём recovery после intensive sprint 21-22.05 (Method V2 + Дмитрий созвон + видео + МИМ deep dive)
- Видео запись для МИМ = 3h30m (substantial) — будет artefact для Wave 1
- МИМ research = 1h10m late-night (substrate для следующих outreach prep)
