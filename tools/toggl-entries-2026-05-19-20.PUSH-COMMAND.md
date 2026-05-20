---
name: Toggl push command — 2026-05-19 → 2026-05-20
description: 14 entries 19.05 00:20 → 20.05 13:00 (Ruslan dictation; ActivityWatch substrate cross-ref)
created: 2026-05-20
status: READY-TO-PUSH (Ruslan acked «у меня файл нормальный я уже запущу»)
originSessionId: 52c96f40-e40b-4d61-bb5d-56df2e63a31e
---
# Команда для server CC

## TL;DR

14 entries за 19.05 00:20 → 20.05 13:00 (~36h40m). JSON готов в `tools/toggl-entries-2026-05-19-20.json`.

## Запуск (в repo root)

```bash
cd ~/Desktop/jetix-os
PYTHONIOENCODING=utf-8 python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-19-20.json
```

(Windows quirk per memory `feedback_cowork_can_push.md` — `PYTHONIOENCODING=utf-8` обязательно для русских tags.)

## Pre-flight verify

```bash
PYTHONIOENCODING=utf-8 python3 -c "
import json
from datetime import datetime
with open('tools/toggl-entries-2026-05-19-20.json') as f:
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

## Breakdown (verify)

| Дата/время (Berlin) | Длит. | Проект | Что | Tags |
|---|---|---|---|---|
| 19.05 00:20-02:20 | 2h | Deep Work | Инвентаризация в базе | INV, Jetix-foundation, understand |
| 19.05 02:20-04:10 | 1h50m | Рутина | Havl | другое |
| 19.05 04:15-06:50 | 2h35m | Deep Work | Claude Code работа (детали в timeline) | KOD, Jetix-foundation, doc |
| 19.05 07:00-14:00 | 7h | Рутина | работа тупая + гулял | тупая-работа |
| 19.05 14:10-15:30 | 1h20m | Deep Work | Claude Code работа (детали в timeline) | KOD, Jetix-foundation, doc |
| 19.05 15:30-17:00 | 1h30m | Отдых | отдых | другое |
| 19.05 17:00-18:00 | 1h | Deep Work | подкаст Анатолий Левенчук + DW | LIS, listen, podcast |
| 19.05 18:00-19:30 | 1h30m | Гулял | ездил гулял | один |
| 19.05 19:30-20:00 | 30m | Рутина | рутина | другое |
| 19.05 20:00 → 20.05 06:00 | 10h | Сон | сон 10ч | глубокий |
| 20.05 06:00-06:10 | 10m | Зарядка | зарядка | тело |
| 20.05 06:10-07:00 | 50m | Рутина | утренняя рутина | другое |
| 20.05 07:00-12:00 | 5h | Рутина | работа тупая | тупая-работа |
| 20.05 12:00-13:00 | 1h | Гулял | шёл домой — поток инсайтов | один, поток-инсайтов |

**Total covered:** 36h40m (gaps 5+10+10 min = 25 min между entries — не critical)

**Sums по проектам:**
- Сон: 10h
- Deep Work: 6h55m (4 entries — INV / KOD ×2 / LIS)
- Рутина: 15h10m (5 entries)
- Гулял: 2h30m (2 entries)
- Отдых: 1h30m
- Зарядка: 10m

## ActivityWatch cross-ref

Substrate для recall — `raw/activitywatch/2026-05-20-export/`:
- `timeline-2026-05-19.md` — chronological sessions ≥30s (180+ entries with HH:MM start/end)
- `apps-by-day.md` — apps + titles aggregated
- `chrome-by-day.md` — Chrome URLs per day

Cross-validation 19.05:
- Active window time: 7h53m (ActivityWatch) vs Deep Work + некоторая рутина (Ruslan dictation) — coherent (рутина и тупая работа часто = phone/Telegram, не captured ActivityWatch)
- Top apps: claude.exe 2h42m / Antigravity 2h17m / chrome 1h57m — matches Deep Work blocks
- Chrome top: YouTube 1h35m (likely в рутина блоки) / Notion 8m / Spotify 4m

## Open notes (Ruslan может correct перед push)

1. **«Havl»** — voice transcription unclear. Если хавал/еда — оставлено literal. Поменяй если нужно: `description: "хавал"` или другое.
2. **KOD tag** для Claude Code DW blocks — assumed (код); канонический tag может быть другой. Поменяй если нужно (e.g., `KOM` коммуникация / `RES` рефлексия / etc.).
3. **INV tag** для инвентаризации — assumed. Если канонический tag другой, поменяй.
4. **Gaps 04:10-04:15 + 06:50-07:00 + 14:00-14:10** (25min total) — не заполнены. Если хочешь explicit «transition» entries, добавь.

## После push — commit

```bash
git add tools/toggl-entries-2026-05-19-20.json tools/toggl-entries-2026-05-19-20.PUSH-COMMAND.md
git commit -m "[time-tracking] Toggl entries 19.05 00:20 → 20.05 13:00 (14 entries: 4 DW Левенчук-inventory + claude-code + подкаст / 5 рутина / сон 10ч / 2 гулял / отдых / зарядка)"
git push origin main
```
