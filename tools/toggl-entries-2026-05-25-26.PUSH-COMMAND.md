# Toggl push command — 2026-05-25 + 26 (17 entries)

## What's inside

17 entries spanning **25.05 11:00 → 26.05 15:10** Berlin time (= UTC 25.05 09:00 → 26.05 13:10).

**25.05 breakdown:** Deep Work 9h30m (5 blocks — план дня + Дмитрий Кайзер + анализ docs + думал сообщения + обработка docs ×3) / Отдых 2h20m / Рутина 50m / Гулял 2h20m
**26.05 night → afternoon:** Deep Work 1h40m (сбор docs) / Отдых 1h40m (фильм) / Сон 8h30m / Рутина 1h10m / Зарядка 20m

**Gap (intentional, не указано):** 25.05 18:10-19:10 Berlin (16:10-17:10 UTC) — 1h без entry.

## Per-entry breakdown (Berlin time)

| # | Time (Berlin) | Project | Tags | Description |
|---|---|---|---|---|
| 1 | 25.05 11:00-12:20 | Deep Work | SOZD / Jetix-foundation / doc | Подготовка к работе + создание плана дня |
| 2 | 25.05 12:20-13:10 | Рутина | другое | Рутина |
| 3 | 25.05 13:10-16:10 | Deep Work | PODG / KOM / Jetix-foundation | Дмитрий Кайзер — подготовка + созвон |
| 4 | 25.05 16:10-17:00 | Отдых | — | Отдых |
| 5 | 25.05 17:00-18:10 | Deep Work | OBR / Jetix-foundation / doc | Анализ + фильтрация всех документов (DOCS-CLASSIFICATION) |
| — | 25.05 18:10-19:10 | **GAP** | — | (не указано) |
| 6 | 25.05 19:10-20:00 | Deep Work | SOZD / Jetix-foundation | Думал какие сообщения партнёрам + цели |
| 7 | 25.05 20:10-21:30 | Гулял | — | Прогулка |
| 8 | 25.05 21:30-22:20 | Deep Work | OBR / Jetix-foundation / doc | Обработка документов, сбор в кучу |
| 9 | 25.05 22:20-22:50 | Отдых | — | Отдых |
| 10 | 25.05 22:50-26.05 00:40 | Deep Work | OBR / Jetix-foundation / doc | Обработка documents continued |
| 11 | 26.05 00:40-01:40 | Гулял | самокат | Гулял на самокате |
| 12 | 26.05 01:40-03:20 | Deep Work | OBR / Jetix-foundation / doc | Сбор документов в кучу |
| 13 | 26.05 03:20-05:00 | Отдых | фильм | Смотрел фильм |
| 14 | 26.05 05:10-13:40 | Сон | глубокий | Ночной сон |
| 15 | 26.05 13:40-14:20 | Рутина | другое | Рутина утренняя |
| 16 | 26.05 14:20-14:40 | Зарядка | — | Утренняя зарядка |
| 17 | 26.05 14:40-15:10 | Рутина | другое | Рутина |

## Push command (на сервере)

```bash
ssh jetix
cd ~/jetix-os && git pull --ff-only
python3 tools/toggl_log_entries.py --dry tools/toggl-entries-2026-05-25-26.json   # validate first
python3 tools/toggl_log_entries.py tools/toggl-entries-2026-05-25-26.json         # push
```

Token from `~/.config/jetix/toggl_token` (mode 600 on server).

## Verification после push

Открой [toggl.com/app/timer](https://toggl.com/app/timer) → проверь что 17 entries появились 25.05 + 26.05 с правильными tags / projects / descriptions.

Если есть failures — `tools/toggl_log_entries.py` output покажет ошибки per entry (e.g., project name mismatch / tag not created / overlap).

## Notes

- Все times в UTC в JSON (Toggl API requirement); Berlin times only в этом README для reference.
- Project names canonical per `swarm/wiki/operations/time-tracking-categories.md` v1.1+ (8 направлений).
- Sub-direction tags для Deep Work: SOZD / PODG / OBR / KOM (per canonical).
- Project tag: Jetix-foundation (architecture / docs / partner work — все entries относятся к нему).
- Gap 18:10-19:10 25.05 — intentional, Ruslan не указал.
