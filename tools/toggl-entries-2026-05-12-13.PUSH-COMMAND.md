---
name: Toggl push command — 2026-05-12 → 2026-05-13
description: Ready-to-run command для server CC чтобы залить 17 entries
created: 2026-05-13
status: AWAITING-ACK
---

# Команда для server CC

## TL;DR

17 entries за 12.05 04:00 → 13.05 17:30. JSON готов в `tools/toggl-entries-2026-05-12-13.json`.

## Запуск (server CC, в repo root)

```bash
cd ~/Desktop/jetix-os
python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-12-13.json
```

(Если `tools/toggl_log_entries.py` ещё не существует — см. log-time skill SKILL.md §workflow.4. Альтернатива: запустить skill `/log-time` с предзаполненным JSON.)

## Pre-flight check

Перед push — verify нет overlap с уже существующими entries:

```bash
python3 -c "
import json
from datetime import datetime
with open('tools/toggl-entries-2026-05-12-13.json') as f:
    entries = json.load(f)
prev = None
for e in entries:
    s = datetime.fromisoformat(e['start'])
    t = datetime.fromisoformat(e['stop'])
    print(f\"{s.strftime('%d.%m %H:%M')}-{t.strftime('%d.%m %H:%M')} {e['project']:10s} {','.join(e['tags']):40s} {e['description']}\")
    if prev and s < prev:
        print('  ⚠️ OVERLAP с предыдущим')
    prev = t
"
```

## Breakdown (для verify)

| Дата/время (Berlin) | Длит. | Проект | Что | Tags |
|---|---|---|---|---|
| 12.05 04:00-06:10 | 2h 10m | Deep Work | Теория игр + Дилемма заключённого | OBR, Jetix-foundation, understand |
| 12.05 06:10-07:00 | 50m | Отдых | — | другое |
| 12.05 07:00-09:00 | 2h | Deep Work | Charter v0 + Mentor/Partner Pitch | SOZD, Jetix-foundation, doc |
| 12.05 09:00-09:30 | 30m | Сон | попытка (беспокойный) | беспокойный |
| 12.05 09:30-14:50 | 5h 20m | Сон | сон | глубокий |
| 12.05 14:50-15:10 | 20m | Рутина | — | другое |
| 12.05 15:10-15:30 | 20m | Зарядка | — | тело |
| 12.05 15:30-17:15 | 1h 45m | Deep Work | Звонок Антон + выгруз + отчёт 2мес | KOM, Jetix-foundation, understand |
| 12.05 17:15-17:35 | 20m | Отдых | после созвона | другое |
| 12.05 17:35-19:00 | 1h 25m | Deep Work | Наладка камеры под видео Цэрэну | PODG, Tseren, nothing |
| 12.05 19:00-19:30 | 30m | Рутина | сбор на работу | другое |
| 12.05 19:30 - 13.05 01:00 | 5h 30m | Рутина | работа тупая | тупая-работа |
| 13.05 01:00-04:00 | 3h | Рутина | работа тупая + инсайты | тупая-работа, поток-инсайтов |
| 13.05 04:00-05:15 | 1h 15m | Отдых | дома + инсайты | активный, поток-инсайтов |
| 13.05 05:15-16:40 | 11h 25m | Сон | сон | глубокий |
| 13.05 16:40-17:10 | 30m | Рутина | — | другое |
| 13.05 17:10-17:30 | 20m | Зарядка | — | тело |

**Total:** 37h 30m (12.05 04:00 → 13.05 17:30 = 37.5h ✓)

**Sums по проектам:**
- Сон: 17h 15m (5h 50m + 11h 25m)
- Deep Work: 7h 20m (4 entries)
- Рутина: 10h 40m (6 entries)
- Отдых: 2h 25m (3 entries)
- Зарядка: 40m (2 entries)

## Open questions / ack нужен от Руслана

1. **Sub-direction для DW звонок Антон** — поставил `KOM` (коммуникация). Альтернативы: `RES` (рефлексия / выгруз был). Если правильнее `RES` — измени и перезапусти.
2. **DW наладка камеры** — поставил `PODG` (подготовка) + `Tseren` project tag. Output: `nothing` (технический setup). Если для видео была SOZD часть (сценарий пробовал) — переклассифицируй.
3. **Рутина «работа тупая»** — tag `тупая-работа`. Если в canonical taxonomy другой alias (например `внешний-job`) — поправь через `tools/toggl_sync.py:PROJECT_LABEL_MAP`.
4. **Gap 05:00-05:15 (13.05, 15min)** — продлил последний "Отдых" до 05:15 (стык с сном). Если был отдельный block (рутина перед сном) — добавь entry.

После Ruslan-ack — push, потом commit:
```
git add tools/toggl-entries-2026-05-12-13.json
git commit -m "[time-tracking] Toggl entries 2026-05-12 → 2026-05-13 (17 entries: theory of games DW + Charter v0 + Anton call + camera setup + work shift + sleep)"
```
