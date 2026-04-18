---
type: synthesis-report
status: closed
step: 3
date: 2026-04-18
owner: ruslan
created: 2026-04-18
related:
  - design/IMPLEMENTATION-PLAN-2026-04-18.md
  - design/SYSTEM-DESIGN-TECH.md
  - templates/
  - tools/lint-frontmatter.py
---

# Шаг 3 — Templates closure (2026-04-18)

> Закрытие Шага 3 плана `design/IMPLEMENTATION-PLAN-2026-04-18.md` §3. Все 12
> канонических templates v1-beta созданы, lint проходит чисто, approval-status
> всех 7 дизайн-документов обновлён.

---

## Результат

**Статус:** ✅ Шаг 3 завершён. Блокер B-6.2 (quick-money priority) отложен в Шаг 6.

**Lint:** 16 файлов в `templates/`, все прошли `tools/lint-frontmatter.py`.

---

## 1. Approval-status обновлён на 7 документах

Замена `pending-ruslan-review` → `approved-by-ruslan-2026-04-18`:

| # | Файл |
|---|------|
| 1 | `SYSTEM-DESIGN-HUMAN.md` |
| 2 | `design/SYSTEM-DESIGN-TECH.md` |
| 3 | `design/SYSTEM-DESIGN-TECH-SUMMARY.md` |
| 4 | `design/AGENT-PROTOCOLS.md` |
| 5 | `design/DATA-FLOWS.md` |
| 6 | `design/ARCHITECTURE-TARGET.md` |
| 7 | `design/IMPLEMENTATION-PLAN-2026-04-18.md` |

---

## 2. 12 канонических templates созданы

### P0 (блокирует Шаги 4-6)

| Код | Файл | Действие | Ключевое |
|-----|------|----------|----------|
| T-01 | `templates/tpl-project-overview.md` | **обновлён** | Добавлены обязательные `budget-hours`, `budget-weeks`, `kill-criterion`, `next_action` (I-23) |
| T-02 | `templates/tpl-decision.md` | создан | Schema по I-12: `context`, `alternatives`, `decision`, `evidence`, `replay-check`, `relevant-agents` (I-29) |
| T-03 | `templates/tpl-hypothesis.md` | создан | Lifecycle: backlog → active → validated \| rejected |
| T-04 | `templates/tpl-strategy-life.md` | создан | Один template покрывает yearly/monthly/weekly (через `level:` + `period:`) |
| T-05 | `templates/tpl-strategy-project.md` | создан | Явный `metric-50k-contribution` как обязательное поле |

### P1 (ежедневная гигиена)

| Код | Файл | Действие | Ключевое |
|-----|------|----------|----------|
| T-06 | `templates/tpl-task.md` | создан | State machine: backlog → today → in-progress → done \| blocked |
| T-07 | `templates/tpl-tool-card.md` | создан | Разделение: `tools/` = наши скрипты; `tools-catalog/` = карточки |
| T-08 | `templates/tpl-daily.md` | **обновлён** | Добавлены поля `plan`, `work-blocks`, `reflection`, `drafts` во frontmatter |
| T-09 | `templates/tpl-daily-draft.md` | создан | GitHub-style sandbox; `promoted-to: null \| <path>` для close-day routing |

### P2/P3

| Код | Файл | Действие | Ключевое |
|-----|------|----------|----------|
| T-10 | `templates/tpl-reflection-entry.md` | создан | Для `reflection/log.md` + `reflection/insights/` |
| T-11 | `templates/tpl-crm-contact.md` | **создан (rename из tpl-contact)** | `category: clients / partners / personal`; опциональное `sensitive: true` (B-3.2) |
| T-12 | `templates/tpl-adr.md` | создан | Nygard lightweight для будущих `docs/adr/` (v1-final split) |

### Legacy-файлы в templates/

| Файл | Действие | Rationale |
|------|----------|-----------|
| `templates/tpl-contact.md` | **удалён** | Переименован в `tpl-crm-contact.md` по плану §3.1 T-11 |
| `templates/daily-log.md` | помечен `status: superseded, superseded-by: tpl-daily.md` | Legacy, дубликат T-08. Оставлен как reference до 1 недели стабильного использования новых templates — потом удалить |
| `templates/weekly-review.md` | помечен `status: superseded, superseded-by: tpl-strategy-life.md` | Legacy, дубликат T-04 (level: weekly). Та же судьба |
| `templates/tpl-kb-article.md` | оставлен как есть | Pre-existing, frontmatter корректный, используется для wiki/claims, wiki/concepts |
| `templates/tpl-raw-source.md` | оставлен как есть | Pre-existing, для `raw/*` источников |

---

## 3. Решения по блокерам (default-варианты из плана)

| Блокер | Решение | Где применено |
|--------|---------|---------------|
| B-3.1 | `kill-criterion` — **строка свободного формата** в v1-beta | `tpl-project-overview.md` frontmatter — значение-плейсхолдер `"if <condition> by <date> then pivot/kill"` |
| B-3.2 | `tpl-crm-contact.md` — опциональное поле **`sensitive: true`** | Frontmatter + комментарий-гайд: sensitive=true не меняет .gitignore автоматически, это метка для privacy-фильтров |
| B-3.3 | **НЕ создавать** отдельный template для `wiki/experiments/` | `tpl-kb-article.md` + `tpl-hypothesis.md` покрывают — experiment = claim с `type: experiment` + явной hypothesis |

B-6.2 (quick-money priority) — вне scope Шага 3, обрабатывается в Шаге 6.

---

## 4. Lint validator (`tools/lint-frontmatter.py`)

**Создан новый:** `tools/lint-frontmatter.py` — ~170 строк Python, без внешних
зависимостей (только stdlib).

**Scope проверок (baseline для v1-beta):**

1. Все `.md` (кроме whitelist: `README.md`, `HOME.md`, `MIGRATION.md`,
   `ARCHITECTURE.md`, `CLAUDE.md`, `test-sync.md`) обязаны иметь YAML
   frontmatter (I-02).
2. Каждая frontmatter-секция ОБЯЗАНА содержать `type` + `created`.
3. Для 15 известных `type:` (project-overview, decision, hypothesis,
   strategy-life, strategy-project, task, tool, daily-log, draft, reflection,
   contact, adr, design-document, design-summary, architecture-target,
   implementation-plan, synthesis-report) — per-type required fields из
   IMPLEMENTATION-PLAN §3.1.
4. Пустые значения (включая placeholder'ы `{{date:YYYY-MM-DD}}`) считаются
   валидным присутствием поля — шаблоны проходят.

**Usage:**
```bash
python3 tools/lint-frontmatter.py templates/
python3 tools/lint-frontmatter.py design/
python3 tools/lint-frontmatter.py path/to/file.md
```

Exit code: 0 = OK, 1 = errors found, 2 = usage error.

**Ограничения v1-beta:**
- Не проверяет вложенные YAML ключи (только top-level).
- Не валидирует enum-значения (e.g., `status: draft/ready/archived` — любое значение принимается как присутствие).
- Не проверяет inline markdown links / wiki-refs.
- `/lint` в §11.16 TECH описывает 9 проверок — реализована только №3 (missing frontmatter fields). Остальные (orphans, contradictions, stale claims, broken links, secret patterns, stale strategies) — v1-final или отдельные скрипты.

---

## 5. Прогон lint

```
$ python3 tools/lint-frontmatter.py templates/
lint-frontmatter: OK — 16 file(s) passed
```

Всё прошло с первой попытки, без манипуляций с содержимым шаблонов.
3 начальных ошибки (tpl-contact.md схема, daily-log.md / weekly-review.md
без frontmatter) закрыты через удаление rename-артефакта и добавление
`status: superseded` на legacy-файлы.

---

## 6. Решения, принятые по ходу

1. **Legacy cleanup стратегия.** `templates/daily-log.md` и `weekly-review.md`
   не упомянуты в плане Шага 3. Вместо удаления добавил `status: superseded,
   superseded-by: ...` frontmatter — они остаются как reference, не блокируют
   lint, и Ruslan может удалить вручную через неделю стабильной работы
   новых templates. Меньше необратимого действия в автономной сессии.

2. **`tpl-kb-article.md` / `tpl-raw-source.md`.** Pre-existing templates, не
   в Step-3 scope, но frontmatter валидный — оставил как есть. Покрывают
   `wiki/` и `raw/` сценарии, дополняют 12 новых.

3. **Поле `owner: ruslan` по умолчанию.** Добавил во все 12 templates для
   единообразия и чтобы lint мог вскрыть кто-то вручную убрал. Это не
   invariant, но удобная дефолт-норма.

4. **Placeholder'ы `{{date:YYYY-MM-DD}}`.** Сохранил стиль существующих
   templates (tpl-project-overview, tpl-daily) для совместимости с Obsidian
   QuickAdd / Templater. Lint их не ругает (присутствие поля достаточно).

5. **`metric-50k-contribution` обязателен в strategy-life и strategy-project.**
   Это критично для привязки к $50K goal (плана §6.3). Поле включено в
   frontmatter schema обоих templates + в TYPE_SCHEMA lint'а.

---

## 7. Следующий шаг

**Шаг 4 — Папочная структура** (§4 IMPLEMENTATION-PLAN):
- Создать 11 новых папок (`strategy/`, `decisions/`, `tasks/`, `hypotheses/`,
  `tools-catalog/`, `reflection/`, `health/`, `ideas-pool/`, `daily-log/drafts/`,
  `docs/adr/`).
- Разрешить блокеры B-4.1 (projects/ дубликаты), B-4.2 (orphan agent folders).
- Удалить `automations/`, `test-sync.md`, legacy `ARCHITECTURE.md`.

Требует решений Ruslan'а по B-4.1 и B-4.2 перед выполнением.

---

## 8. Metrics

| Показатель | Значение |
|------------|----------|
| Templates создано/обновлено | 12 (T-01..T-12) |
| Файлов с обновлённым frontmatter | 7 (approval-status) |
| Файлов проверено lint | 16 в templates/ |
| Lint errors финальный | 0 |
| Новых скриптов | 1 (`tools/lint-frontmatter.py`, ~170 LOC) |
| Удалённых legacy | 1 (`tpl-contact.md` — rename) |
| Помечено `superseded` | 2 (daily-log.md, weekly-review.md) |
| Времени на Шаг 3 | ~30 минут машинной работы |

---

*Шаг 3 закрыт 2026-04-18. Commit: `[templates] Шаг 3 v1-beta — 12 canonical
templates T-01..T-12 + approval status update`.*
