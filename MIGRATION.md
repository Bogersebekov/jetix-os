---
type: migration-plan
created: 2026-04-16
updated: 2026-04-16
owner: ruslan
status: active
---
# Migration Plan — старая архитектура → wiki/ + agent memory

Phase 2 создал новую архитектуру (см. `reports/arch-migration-2026-04-16.md`).
Старые структуры остались на месте. Миграция — постепенная, через `/ingest`.

## Старое → Новое

| Старое | Новое | Метод | Статус |
|--------|-------|-------|--------|
| `knowledge-base/ai-consulting/` | `wiki/` | `/ingest` на каждую статью | [ ] не начато |
| `knowledge-base/market/` | `wiki/` | `/ingest` | [ ] не начато |
| `knowledge-base/sales/` | `wiki/` + `wiki/niches/sales/` | `/ingest` | [ ] не начато |
| `knowledge-base/_health/` | `wiki/niches/life/` + claims | `/ingest` | [ ] не начато |
| `raw/transcripts/*.txt` | `wiki/sources/` + связанные | `/ingest` | [ ] не начато |
| `raw/voice-memos/*.ogg` | сначала transcripts, потом `/ingest` | `tools/transcribe.py` → `/ingest` | [ ] не начато |
| `raw/imports/`, `raw/research/` | `wiki/` | `/ingest` | [ ] не начато |
| Notion pages (Command Center, Research Hub, ICP) | `wiki/` | Ручной экспорт → raw/ → `/ingest` | [ ] позже |

## Приоритет

1. **Sanity-check на одном источнике:** выбрать одну статью из `knowledge-base/ai-consulting/`
   и прогнать через `/ingest` — проверить, что skill работает как задумано.
2. **knowledge-base/ai-consulting/** — основной коммерческий материал, поднимаем первым.
3. **knowledge-base/sales/** — сразу заполнит `wiki/niches/sales/` для sales-агентов.
4. **Транскрипты** — параллельно, по 5-10 штук за сессию.
5. **Голосовые** — только после накопления 20+ ingest-страниц (чтобы была база для cross-ref).
6. **Notion** — последним, когда локальная wiki уже устоялась.

## Правила миграции

- Старую структуру НЕ удаляем. Перенос только через копирование (в виде ingest).
- В каждой исходной директории можно оставить `MIGRATION-STATUS.md` с отметками.
- Если `/ingest` выявил ошибку в skill — стопаемся, фиксим skill, продолжаем.
- После полного переноса `knowledge-base/` — архивируем в `_archive/knowledge-base-pre-2026-04-16/`
  (делает вручную Руслан, не Claude).

## Что пока НЕ мигрируем

- `projects/` — живёт параллельно, ссылки из wiki по необходимости.
- `crm/` — multi-purpose contact network (people + orgs). Built 2026-04-26 в
  cycle-10-crm-build, NOT в legacy/migration scope. Own schema, scripts, skills
  (`/crm-*`), tests. Cross-references в wiki через `wiki/graph/edges.jsonl`
  (8 CRM edge types в `wiki/graph/edge-types.md`). Authoritative spec:
  `crm/README.md` + `crm/PLAN.md`.
- `inbox/`, `ideas/`, `chat-journal/`, `daily-log/` — операционные, не KB.
- `dashboard/`, `tools/`, `scripts/`, `automations/` — код, не контент.

## Что делать дальше

См. `reports/arch-migration-2026-04-16.md` секция "Next steps".
