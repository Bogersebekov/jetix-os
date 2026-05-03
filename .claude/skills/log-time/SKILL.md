---
name: log-time
description: Запись времени в Toggl + Daily Log из текста (Wispr Flow → CC → entries). Используется когда Ruslan диктует «работал 9-12 над X, потом обед, 13-15 outreach Tseren» и хочет автоматическую структуру.
trigger:
  - "запиши в toggl"
  - "log time"
  - "/log-time"
  - "запиши время"
  - "залогируй"
inputs: text-блок про прошедшие активности (Wispr Flow output или typed)
outputs: parsed entries → POST к Toggl API + ack в чате + опциональный Daily Log append
---

# log-time skill

## Цель
Распарсить текст-описание прошедших активностей в JSON-структуру и залогировать в Toggl Track + Daily Log Notion. Канон — `swarm/wiki/operations/time-tracking-categories.md` v1.1+.

## Канонические inputs
- 8 направлений: Сон / Зарядка / Спорт / Рутина / Deep Work / Гулял / Отдых / Ебланил
- DW sub-direction: RES / OBR / SOZD / UCH / PODG / KOM
- Energy: flow / обычный / тяжело / пиздец
- Output: doc / решение / understand / gap / nothing
- Project tags: Jetix-foundation / Jetix-workshop / Jetix-TRM / Jetix-pipeline / Jetix-malware-analysis / Jetix-time-tracking / Jetix-CC-OS / Jetix-voice / Tseren / Mittelstand
- Sub-tags по категориям (см. canonical doc §5.1)

## Workflow

### 1. Парсинг
Прочитать text input. Извлечь sequence of activities. Для каждой определить:
- **start** time (если указано «9-12», начало 09:00; если «потом», вычислить от предыдущего stop)
- **stop** time (если указано — иначе спросить Ruslan-а)
- **project** (одна из 8 канонических — нормализовать через `tools/toggl_sync.py:PROJECT_LABEL_MAP`)
- **tags**: для Deep Work — обязательно sub-direction + energy + output + project_tag; для других — соответствующие sub-tags
- **description** — конкретный output / artifact (per §5.4 v1.1 description templates)

### 2. Валидация
Проверить:
- Project в каноническом наборе 8 (или alias `New info or thinking` → `Deep Work`)
- Нет overlap по timeline (стопы / старты не пересекаются)
- Для Deep Work entries: ≥1 sub-direction + ≥1 project tag + желательно energy + output
- Description не каша (см. §5.4 anti-patterns)

Если что-то ambiguous — **спросить Ruslan-а конкретный вопрос**, не угадывать.

### 3. Show preview + ask confirmation
Вывести в чат table preview:

```
| Time | Project | Tags | Description |
|------|---------|------|-------------|
| 09:00-12:00 | Deep Work | SOZD, Tseren, doc, flow | Создание презы — структура целиком |
| 12:00-13:00 | Рутина | еда | обед |
| 13:00-15:00 | Deep Work | KOM, Tseren, решение | Отправка видео + tracking |
```

Спросить: **«Залогировать N entries в Toggl? (yes/no/edit)»**

### 4. Запись (после yes)
- Создать temp file с JSON массивом entries
- Запустить `python3 tools/toggl_log_entries.py /tmp/entries.json`
- Capture output (created/failed counts + ids)
- Если failed > 0 — flag explicitly + show errors

### 5. Daily Log auto-append (опционально)
Если в input есть упоминание «daily log» / «в Notion» / `--notion` flag:
- Найти Daily Log entry за указанную дату через notion-search
- Append section "## ⏱️ Time tracking summary" с table из step 3
- Если sub-section уже существует — update (replace_content)

## Hard rules
1. **Canonical schema only** — не выдумывай новые projects или tags. Если что-то не fit'ится в 8 направлений — flag в чат, не promote.
2. **Description discipline** — следовать template из v1.1 §5.4 (DW: глагол + output + контекст). Не каша.
3. **Инсайты НЕ в description** — если в input есть «понял что X» — это отдельный output tag `understand`, а сам insight идёт в `wiki/ideas/` (отдельный шаг, не в этом skill).
4. **AI = scribe** — не диктуй sub-direction если Ruslan не указал. Спроси если ambiguous.
5. **Timezone** — Berlin (Europe/Berlin). Если Ruslan указывает время «09:00» — это локальное Berlin time. Convert в UTC для Toggl API (subtract 1h winter / 2h summer).
6. **No retroactive overlap** — не создавать entry который пересекается с существующими. Сначала GET /me/time_entries для verify.

## Examples

### Input (text):
```
лёг 23:30, встал 7:45 (нормальный сон).
9-12 работал над презой Tseren — создавал структуру целиком, был в потоке.
12-13 обед.
13-15 продолжил работу над презой — добавил 3 слайда видения TRM, тяжело шло.
15-16 гулял с бро по Берлину.
```

### Parsed entries:
```json
[
  {"start": "2026-05-02T23:30:00+02:00", "stop": "2026-05-03T07:45:00+02:00",
   "project": "Сон", "tags": ["глубокий"], "description": "нормальный сон"},
  {"start": "2026-05-03T09:00:00+02:00", "stop": "2026-05-03T12:00:00+02:00",
   "project": "Deep Work", "tags": ["SOZD", "Tseren", "doc", "flow"],
   "description": "Создание презы — структура целиком"},
  {"start": "2026-05-03T12:00:00+02:00", "stop": "2026-05-03T13:00:00+02:00",
   "project": "Рутина", "tags": ["еда"], "description": "обед"},
  {"start": "2026-05-03T13:00:00+02:00", "stop": "2026-05-03T15:00:00+02:00",
   "project": "Deep Work", "tags": ["SOZD", "Tseren", "doc", "тяжело"],
   "description": "Создание презы — 3 слайды видения TRM"},
  {"start": "2026-05-03T15:00:00+02:00", "stop": "2026-05-03T16:00:00+02:00",
   "project": "Гулял", "tags": ["с-кем-то"], "description": "с бро по Берлину"}
]
```

## Server-side execution
```bash
# 1. Save parsed entries
echo '<json array>' > /tmp/entries.json

# 2. Validate (dry run)
python3 tools/toggl_log_entries.py --dry /tmp/entries.json

# 3. Submit
python3 tools/toggl_log_entries.py /tmp/entries.json
```

## Related
- Canonical schema: `swarm/wiki/operations/time-tracking-categories.md` v1.1+
- Server-side reading: `tools/toggl_sync.py`
- POST helper: `tools/toggl_log_entries.py`
- AW pipeline: `tools/aggregate_activity.py`
- Daily Log Notion DB: `30a24963-33bf-8005-817a-000beb10bcd4`
