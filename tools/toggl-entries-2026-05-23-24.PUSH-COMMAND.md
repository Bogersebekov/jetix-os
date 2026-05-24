---
name: Toggl push command — 2026-05-23 → 2026-05-24
description: 9 entries 23.05 16:30 → 24.05 12:20 (Ruslan dictation 24.05 lunch; cross-ref AW export 2026-05-24-export)
created: 2026-05-24
status: READY-TO-PUSH
---

# Команда для local push (Toggl API)

## TL;DR

9 entries за 23.05 16:30 → 24.05 12:20 (~19h50m spans без gaps).

JSON: `tools/toggl-entries-2026-05-23-24.json`

## Breakdown по проектам

| Project | Total | Entries |
|---|---|---|
| Deep Work | 7h10m | 2 (планирование research 1h / поиск книг + запуск/контроль research prompts 6h10m) |
| Отдых | 2h | 2 (отдых после планирования 30m / втык YouTube 1h30m) |
| Сон | 7h40m | 1 |
| Рутина | 2h40m | 3 (магаз+еда 2h / утренняя ×2 = 40m) |
| Зарядка | 20m | 1 |

**Coverage:** 23.05 16:30 → 24.05 12:20 = 19h50m **continuous, no gaps**.

## Запуск (в repo root)

```bash
cd ~/Desktop/jetix-os
PYTHONIOENCODING=utf-8 python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-23-24.json
```

(`PYTHONIOENCODING=utf-8` обязательно для русских tags.)

## Pre-flight verify

```bash
PYTHONIOENCODING=utf-8 python3 -c "
import json
from datetime import datetime
with open('tools/toggl-entries-2026-05-23-24.json', encoding='utf-8') as f:
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

- `raw/activitywatch/2026-05-24-export/timeline-2026-05-23.md` — substrate для 23.05 evening (магаз → планирование → research launches)
- `raw/activitywatch/2026-05-24-export/timeline-2026-05-24.md` — substrate для 24.05 morning (research overnight → YouTube → сон → утренняя рутина)

## Notes

- **Deep Work 7h10m** массивный block research launches overnight (Mistral OCR + book-driven agents prompts + exec-agents)
- **YouTube втык 1.5h** classified как Отдых (recovery — not productive)
- **Сон 7h40m** более adequate vs predыдущий 14h recovery 23.05
