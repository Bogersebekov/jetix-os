---
type: migration-plan
status: draft
stage: strategic-framing
version: draft-v0
owner: ruslan
created: 2026-04-16
updated: 2026-04-16
related:
  - SYSTEM-DESIGN-HUMAN.md
  - MIGRATION.md (legacy knowledge-base → wiki)
  - ARCHITECTURE-CURRENT.md
---

# NOTION-MIGRATION-PLAN.md — Полный перенос знаний Notion → Jetix OS на сервере

> **Черновик.** Мастер-план миграции. Конечная цель: перестать пользоваться Notion.
> Вся работа — только через wiki/ на сервере + git + Claude Code + Obsidian.
> Notion остаётся read-only архив на случай "если что-то забыли".

---

## 1. Зачем мы это делаем

### 1.1 Решение зафиксированное сегодня (2026-04-16)

Ruslan принял стратегическое решение: **полностью перейти на сервер**.
Notion деприкэйтим. Всё ценное — переезжает в `wiki/` + `projects/` + `shared/state/` +
`daily-log/`. Новые заметки пишутся сразу туда.

### 1.2 Почему Notion уходит

- **SPOF:** Notion MCP — single-point-of-failure. Уже падал посреди сессий
  (Inventory report 2026-04-16, gap #2). 8 агентов + 4 skill'а зависят от него —
  и теряют функциональность когда мост отваливается.
- **Двойная правда:** сейчас Notion = external truth, wiki = internal truth.
  Это рассинхрон: одна идея живёт в двух местах. Непонятно какая версия актуальна.
- **Нет compounding:** каждый запрос к Notion открывает знание заново.
  В wiki/ знание накапливается через `/ingest` + `/ask` writeback.
- **Стоимость переключения контекста:** каждый раз когда открываешь Notion —
  тратишь attention на навигацию. Wiki + Obsidian + Claude Code — единое поле.
- **Автономия:** когда Notion выключится, вся система продолжит работать.
  Сейчас она не продолжит.

### 1.3 Что Notion остаётся делать (после миграции)

- **Архив** — read-only snapshot, к которому можно вернуться если что-то забыли.
- **Внешний интерфейс** (возможно, в будущем) — для клиентов/сообщества, когда
  понадобится показать материалы во внешний мир. Но это отдельный проект,
  не этот.

---

## 2. Парадокс и его решение

### 2.1 Формулировка парадокса

Ruslan сформулировал это точно:

> Чтобы адекватно описать систему (Шаг 2), нужен пласт знаний из Notion.
> Но чтобы описать правильный pipeline вытягивания из Notion — нужна уже описанная
> система (правила, pipeline, frontmatter convention).

Круг. Нельзя делать всё последовательно.

### 2.2 Решение — этапность с разрывом круга

Разрываем через **минимально-достаточный объём** на первом проходе:

```
Фаза α (quick extract)  → Фаза β (system design done)  → Фаза γ (full extract)  → Фаза δ (decommission)
    ↓                         ↓                             ↓                       ↓
 50-70% знаний            описание + правила             100% знаний            Notion off
 чтоб описать систему     полная wiki + плагины          по новым правилам
```

**Фаза α** — quick-dirty, ПРАВИЛА ЕЩЁ НЕПОЛНЫЕ. Тянем по текущим конвенциям
(которые уже есть в `.claude/skills/ingest.md` и `wiki/_templates/`).
Цель — собрать философию/видение/ICP/pipelines/Life OS из Notion,
чтоб было с чем писать SYSTEM-DESIGN-HUMAN.md.

**Фаза β** — описываем систему целиком. В SYSTEM-DESIGN-HUMAN.md появляется
секция "Notion Migration Principles" = правила Фазы γ.

**Фаза γ** — строгий полный extract по новым правилам. Всё остальное:
оставшиеся 400+ идей, Daily Log полностью, Projects DB, Journal of Chats,
все child-pages, старые версии страниц.

**Фаза δ** — Notion → read-only → off.

### 2.3 Минимально-достаточный объём (для Фазы α)

**Что нужно получить для описания SYSTEM-DESIGN-HUMAN:**

1. **Банк идей (все 650+)** — JSONL dump с metadata + content preview.
   Из них RELEVANT (~100-200) импорт в `wiki/ideas/`.
2. **11 Notion-страниц о системе** (перечислены в CLAUDE.md Key Notion IDs +
   plan-day Notion page):
   - Манифест как мы строим систему
   - Архитектура Memory+KB Karpathy+
   - Command Center
   - Pipeline рабочего дня
   - Анализ недели
   - Типы чатов и правила работы с AI
   - Потоки информации — куда что сохранять
   - Формат страницы дня
   - Life OS
   - Research Hub
   - ICP Page
3. **Daily Log digest** — insights/reflections за все даты (не полные записи,
   а выжимки касающиеся системы).

Этого хватит чтобы описать все 7 частей SYSTEM-DESIGN-HUMAN.md.

**Что в α НЕ тянем:**
- Projects DB (оставляем Фаза γ)
- Journal of Chats (оставляем Фаза γ)
- Банк идей кроме RELEVANT (оставляем JSONL как staging для Фазы γ)
- Старые daily logs без system-insights (Фаза γ)
- Sub-pages под главными (Фаза γ)

---

## 3. Inventory Notion — что там вообще есть

### 3.1 Databases (collections)

| DB | ID | Описание | Кол-во записей (оценочно) |
|----|-----|----------|----------------------------|
| Daily Log | 30a24963-33bf-8005-817a-000beb10bcd4 | Ежедневные записи (Day Type, Key Action, Insights, Reflection) | ~50-200 дат |
| Projects | 69a3c581-ab33-48d9-9827-ec8a8bb69d14 | Проекты и их статусы | ~10-30 проектов |
| Journal of Chats | 89c2ac5e-797e-4bff-bd53-4316026f8094 | Лог чатов с AI | ~30-200 записей |
| Банк идей | bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7 | Все идеи (65% импортировано: 60/~650) | 648+ идей |

### 3.2 Top-level pages (Command Center иерархия)

| Page | ID | Содержимое |
|------|-----|-----------|
| Command Center | 3322496333bf8161b6d3ea789d039356 | Корневая страница с навигацией, проекты, ресурсы, дневные планы |
| ICP Page | 3372496333bf8125a72cd7352124b5ee | Ideal Customer Profile Jetix |
| Research Hub | 32c2496333bf81e8807cd490f9d17872 | Исследования, блоки A-F, синтезы |
| Life OS | 3322496333bf8184b31bc985a93222d7 | Система жизни, здоровье, энергия |
| Pipeline рабочего дня | 3342496333bf8150a87ece4cfacab815 | Как утром/день/вечер |
| Анализ недели | 3342496333bf814a88e1d0699d1d469d | Еженедельная ретроспектива |
| Типы чатов и правила работы с AI | 3342496333bf814db239c8bfc55aacb2 | 1 чат = 1 тема |
| Потоки информации | 3342496333bf81fa9950cbb53bd0e8f5 | Куда что сохранять |
| Формат страницы дня | 33c2496333bf81f3a360e0e90a05265b | Шаблон Daily Log |
| Манифест как строим систему | 3442496333bf818184a1fbc3108b38cb | 7 принципов |
| Архитектура Memory+KB Karpathy+ | 3442496333bf819cb864cf0e04c9de74 | Скелет архитектуры памяти |

Под каждой — потенциально десятки sub-pages. Полный inventory делается на Фазе α.

### 3.3 Unknown территория

Что может быть что мы ещё не знаем:
- Скрытые workspaces или shared pages
- Старые эксперименты которые Ruslan отключил но не удалил
- Заметки в "Miscellaneous" страницах
- Attachments (файлы внутри Notion — их в wiki не утащить напрямую)
- Comments и дискуссии на страницах

**Фаза α вытащит top-level + DBs.** Остальное — Фаза γ со скриптом обхода всех страниц через API.

---

## 4. Архивная структура на сервере — куда что ложится

| Notion | Сервер (куда) | Пример пути |
|--------|--------------|-------------|
| Банк идей (одна идея) | `wiki/ideas/{slug}.md` + `wiki/sources/{date}-{slug}.md` + `raw/notion-ideas/{slug}.md` | `wiki/ideas/focus-theory-5-people-ai-1-task.md` |
| Notion-страница (top-level) | `wiki/sources/{date}-{slug}.md` + разбор на `concepts/`, `claims/`, `foundations/` | `wiki/sources/2026-04-16-manifest-system-building.md` |
| Daily Log entry | `daily-log/YYYY-MM-DD.md` (если ещё нет) + выжимки в `wiki/summaries/` | `daily-log/2026-04-16.md` |
| Project из Projects DB | `projects/{project-slug}/overview.md` + `projects/{project-slug}/log.md` | `projects/quick-money/overview.md` |
| Journal of Chat | `archive/chat-journal/YYYY-MM-DD-chat-N.md` | `archive/chat-journal/2026-04-10-chat-3.md` |
| Attachment (PDF/Image) | `raw/attachments/{date}-{slug}.{ext}` | `raw/attachments/2026-04-01-diagram.png` |
| Sub-page (ребёнок) | `wiki/sources/{date}-{parent-slug}-{child-slug}.md` с frontmatter parent: | (составной slug) |

**Принцип:** ничего не теряем. Каждая Notion-единица получает дом в структуре сервера.

---

## 5. Четырёхфазная миграция — детально

### Фаза α — Quick extract (под Шаг 2)

**Цель:** собрать минимально-достаточный пласт знаний чтобы описать целевую систему.

**Объём:** ~70% того что нужно для SYSTEM-DESIGN-HUMAN.md.

**Расписание:** этот день (2026-04-16) после окончания текущего server-run.

**Что тянем:**

| # | Источник | Метод | Куда |
|---|----------|-------|------|
| α.1 | Банк идей (650+) — JSONL metadata всех | notion-query-database-view × pagination | `raw/notion-bank-sweep-2026-04-16.jsonl` |
| α.2 | Банк идей RELEVANT (100-200) — full content | notion-fetch per idea + `/ingest` | `wiki/ideas/*`, `wiki/sources/*`, `raw/notion-ideas/*` |
| α.3 | 11 страниц о системе — полный content | notion-fetch per page | `raw/notion-pages/{slug}.md` + `/ingest` → `wiki/sources/*` |
| α.4 | Daily Log — все записи | notion-query + filter system-insights | `raw/notion-daily-log-dump-2026-04-16.jsonl` + digest в `wiki/summaries/` |

**Кто делает:**
- **Локальный Claude Code (Windows)** — все `mcp__notion-*` операции. Мой Notion MCP
  работает. Дампы сохраняю в `raw/` → коммит → push.
- **Серверный Claude Code** — читает dumps из `raw/`, запускает `/ingest` локально
  (без Notion MCP). Тэгирует + создаёт staging.

**Почему два Claude:** серверный Notion MCP не аутентифицирован и чинить его
сейчас — не в приоритете. Проще использовать git как bridge: локальный делает
queries, пушит как файлы, сервер их обрабатывает.

**Выход Фазы α:**
- `raw/notion-bank-sweep-2026-04-16.jsonl` — metadata всех 650+ идей
- `raw/notion-pages/{11 slugs}.md` — 11 страниц о системе
- `raw/notion-daily-log-dump-2026-04-16.jsonl` — все Daily Log entries
- `wiki/ideas/*` дополнены до ~200 RELEVANT
- `wiki/sources/*` + 11 system pages
- `wiki/topics/system-design-hub.md` — hub (частично готов серверным Claude)
- `design/SYSTEM-DESIGN-INPUTS.md` — staging (частично готов серверным Claude,
  дособирается на Фазе α.5)

**Коммиты Фазы α:** 5-8 штук. Префикс `[notion-α]`.

### Фаза β — System design completion (Шаг 2 готов)

**Цель:** закрыть SYSTEM-DESIGN-HUMAN.md полностью. В нём появляется секция
**Notion Migration Principles** которая становится правилом Фазы γ.

**Объём:** 7 частей документа + 5+ Miro-визуализаций + секция правил миграции внутри Части 4.

**Расписание:** следующие 2-4 сессии диктовки.

**Что делается:**
1. Ruslan + я (локальный) — диктовка + запись Частей 1-6 SYSTEM-DESIGN-HUMAN.md
   (используя `design/SYSTEM-DESIGN-INPUTS.md` как конспект).
2. Я — Miro-визуализации.
3. **Новая секция в SYSTEM-DESIGN-HUMAN.md:**
   > `## 7. Правила миграции Notion → wiki (для Фазы γ)`
   >
   > - Какие сущности где живут (из §4 этого плана + детализация)
   > - Frontmatter convention для каждого типа
   > - Что делать с attachments
   > - Как разрешать конфликты (одна идея в двух местах)
   > - Как сохранять history (версии страниц)
   > - Что делать с comments/discussions
   > - Критерии "готово к декомиссии"
4. Фиксация → `SYSTEM-DESIGN-HUMAN.v1.md` + Notion-чистовик (в тот же Notion
   который декомиссионим — мета-момент: финальный чистовик живёт в обеих
   системах на время Фазы γ).

**Выход Фазы β:** SYSTEM-DESIGN-HUMAN.v1.md с полностью описанной системой +
правила Фазы γ.

### Фаза γ — Full extract (под новые правила)

**Цель:** вытащить из Notion ВСЁ что осталось. Ни одной непрогнанной страницы.

**Объём:** 100% - то что уже перенесено Фазой α (~70%).

**Расписание:** 2-5 дней после Фазы β.

**Что тянем:**

| # | Источник | Объём оценочно | Куда |
|---|----------|-----------------|------|
| γ.1 | Банк идей IRRELEVANT + UNCLEAR | 400-500 идей | `wiki/ideas/*` (остальные + topic tags) |
| γ.2 | Projects DB — все проекты | 10-30 проектов | `projects/{slug}/` (merge с существующими) |
| γ.3 | Journal of Chats | 30-200 записей | `archive/chat-journal/*` + insights extract |
| γ.4 | Daily Log — полное содержимое | 50-200 дат | `daily-log/YYYY-MM-DD.md` |
| γ.5 | Все sub-pages под 11 top-level | ? | `wiki/sources/*` composite slugs |
| γ.6 | Attachments (файлы) | ? | `raw/attachments/*` |
| γ.7 | Comments/discussions | ? | inline в target files как `> [[note]]` или `archive/notion-discussions/` |
| γ.8 | Миграция knowledge-base/ legacy (старый MIGRATION.md trek) | ~N файлов | `wiki/*` по MIGRATION.md |

**Кто делает:** в основном серверный Claude Code, используя специальные skills
которые мы напишем на Фазе β:
- `/migrate-notion-batch` — обрабатывает очередь
- `/migrate-project` — Projects DB → `projects/*`
- `/migrate-attachments` — скачивает файлы
- `/verify-migration` — проверяет что ничего не потеряно

**Локальный Claude Code** — Notion API queries (полный inventory перед batches).

**Коммиты Фазы γ:** много, может 30-50. Префикс `[notion-γ]`.

**Выход Фазы γ:** wiki/ + projects/ + archive/ содержат 100% Notion-контента.
Лог полный. `_lint-report` чист. `/build-graph` рестроит граф.

### Фаза δ — Decommission

**Цель:** выключить Notion как source of truth.

**Расписание:** после полной Фазы γ + 1 неделя обкатки.

**Что делается:**

1. **Verify migration** — запуск `/verify-migration`:
   - Count check: каждая Notion-страница имеет соответствие в wiki/projects/archive
   - Content check: random sample 10% страниц — сравнение текстом
   - Attachment check: все файлы скачаны
   - Link check: wikilinks → все живые

2. **Update CLAUDE.md + все `.claude/agents/*.md`:**
   - Убрать `mcp__notion-*` из tools агентов
   - Убрать "Notion = external truth" — заменить на "wiki/ = sole source of truth"
   - Убрать Key Notion IDs секцию (или перевести в archive/notion-ids-deprecated.md)

3. **Update `.claude/skills/*`:**
   - `/plan-day`, `/close-day`, `/ingest` — уберают Notion-sync шаги
   - `/sync_context.py` — deprecate или удалить
   - `inbox-processor` — пишет сразу в wiki, не в Notion

4. **Notion → Read-only:**
   - Либо закрыть workspace (Personal plan)
   - Либо пометить все DB/pages как archived
   - Либо оставить read-access но убрать все integrations

5. **Git tag:** `notion-decommissioned-2026-MM-DD` — зафиксировать точку невозврата.

**Коммиты Фазы δ:** 5-10 штук. Префикс `[notion-δ]`.

**Выход Фазы δ:** работаем только с сервером. Notion — архив.

---

## 6. Роли и коммуникация

### 6.1 Локальный Claude Code (Windows, где сейчас я)

- **Интерфейс к Notion.** Все `mcp__notion-*` операции.
- **Writer SYSTEM-DESIGN-HUMAN.md.** Диктовка + запись.
- **Orchestrator планов.** Обновляет roadmap, создаёт новые design-документы.
- **Notion Extraction Hub.** Делает queries/fetches, сохраняет в `raw/`, коммитит.

### 6.2 Серверный Claude Code (100.99.156.28)

- **Processor.** Читает dumps из `raw/`, запускает `/ingest` / `/migrate-*`.
- **Wiki-worker.** Создаёт/обновляет `wiki/*`, `projects/*`, `archive/*`.
- **Background runner.** Тяжёлые задачи на часы — через tmux + autonomous mode.
- **Sub-agent orchestrator.** Spawn-им `sweep-worker`, `staging-writer`, и т.д.

### 6.3 Git как bridge

Простой протокол:
- Локальный пушит `raw/*` dumps → сервер pull'ит → обрабатывает → пушит `wiki/*`.
- Сервер пушит staging → локальный pull'ит → проверяет.
- Оба читают главное панно (`SYSTEM-DESIGN-HUMAN.md`, этот план и roadmap).

Не пытаемся синхронизировать "в реальном времени". Git — точка синхронизации.

---

## 7. Критерии декомиссии Notion

Notion можно выключать когда ВСЕ условия TRUE:

| # | Критерий | Как проверяем |
|---|----------|---------------|
| 1 | Все страницы Notion имеют соответствие на сервере | `/verify-migration` count check |
| 2 | Все Databases (4 шт) полностью экспортированы | Запись в `reports/migration-verify-{date}.md` |
| 3 | Все attachments скачаны | ls `raw/attachments/` = N файлов |
| 4 | `/ask` может ответить на любой вопрос без Notion MCP | тест 20 вопросов про систему/идеи |
| 5 | Ни один агент не объявлен с `mcp__notion-*` в tools | grep в `.claude/agents/*.md` |
| 6 | Ни один skill не вызывает Notion MCP | grep в `.claude/skills/*.md` |
| 7 | CLAUDE.md обновлён (убрана "Notion = external truth") | manual review |
| 8 | Прошло 7 дней от последней миграции без новых всплывающих потерь | log в `reports/decommission-watch.md` |
| 9 | Ruslan даёт финальное "ОК" | в чате + в git tag |

---

## 8. Риски и mitigations

| Риск | Вероятность | Impact | Mitigation |
|------|-------------|--------|------------|
| Notion MCP падает посреди extract'а | Высокая | Средний | Retry × 3, частые коммиты, SAFE-SAVE pattern |
| Rate limit Notion API | Средняя | Низкий | Batch + sleep между запросами |
| Атачменты не скачиваются | Средняя | Средний | Отдельная задача γ.6, fallback — ручной экспорт |
| Pages с нестандартными блоками (embeds, formulas) | Высокая | Низкий | Выдирать плоский markdown, сохранять сырые blocks в `raw/notion-pages-raw/` |
| Дубликаты контента (одна идея в 2 местах Notion) | Высокая | Средний | dedup по notion_id + merge pattern (как в batch2) |
| SYSTEM-DESIGN-HUMAN описывает правила под γ которые плохо ложатся на реальность | Средняя | Высокий | γ начинается с pilot на 20 страницах → ревью → корректировка правил → полный запуск |
| Ruslan забывает что-то в Notion что не описал явно | Высокая | Средний | Final sweep: query ALL Notion content, Check-list что ничего не пропущено |
| Серверный Claude дропает работу (API 529) | Высокая | Низкий | foreground fallback, tmux survival, SAFE-SAVE |
| Merge conflicts между Windows и сервером | Средняя | Низкий | Разные папки (`raw/` = local-only, `wiki/` = server-only mostly) |

---

## 9. Как этот план интегрируется с SYSTEM-DESIGN-HUMAN.md

### 9.1 В Часть 4 "Потоки информации" добавится секция "Миграционный поток"

```
### 4.N Миграционный поток: Notion → wiki
- Notion — временная внешняя truth до декомиссии (см. NOTION-MIGRATION-PLAN.md)
- После декомиссии: wiki/ = sole source of truth
- Поток раньше: заметка → Notion → (вручную) → wiki
- Поток сейчас: заметка → inbox/ → /ingest → wiki/
- Поток после декомиссии: нет Notion в цепочке
```

### 9.2 Секция "Правила миграции Notion" внутри Части 4

(Пишется на Фазе β после первого прохода 1-7 основной структуры)

Именно эти правила становятся input'ом для Фазы γ. Без них — хаос. Раньше
планировалась как отдельная "Часть 7", но структура устаканилась на 7 частях
без выделенной — правила миграции вошли логично в Часть 4 "Потоки информации"
(сам переезд — это один из потоков).

### 9.3 Часть 2 "Цели и результаты" должна упомянуть декомиссию Notion

Как одну из целей Шага 2-8 roadmap. Метрика: после декомиссии ни один агент
не имеет `mcp__notion-*` в tools (см. §7 этого плана, критерий декомиссии #5).

### 9.4 Обратная связь

SYSTEM-DESIGN-HUMAN.md — ЗНАЕТ про этот план (ссылка). Этот план — ЗНАЕТ про
SYSTEM-DESIGN-HUMAN.md (ссылка). Два дока не дублируют содержимое, они дополняют.

---

## 10. Обновлённый roadmap Jetix OS (Шаги 1-10)

Старый план был 1-8. Сейчас раздвигается до 10 шагов с параллельными треками:

| Шаг | Название | Статус | Когда | Трек |
|-----|----------|--------|-------|------|
| 1 | Инвентаризация (точка А) | ✅ готово | 2026-04-16 | A |
| 1.5 | Разбор birds-eye на человеческом | ✅ готово | 2026-04-16 | A |
| 2 | Описать целевую систему на человеческом | 🔄 в работе | 2026-04-16..18 | A |
| 2.α | Quick extract из Notion (для Шага 2) | 🔄 в работе (server) | 2026-04-16 | B |
| 2.β | SYSTEM-DESIGN-HUMAN заполнено (7 частей + мета) | ⏳ | 2026-04-17..18 | A |
| 3 | Фиксация → v1.md + Notion-чистовик | ⏳ | 2026-04-18 | A |
| 4 | Перевод на архитектурный язык | ⏳ | 2026-04-19..21 | A |
| 5 | Внедрение через Claude Code на сервере | ⏳ | 2026-04-22..25 | A |
| 6 | Тестирование + баги | ⏳ | 2026-04-25..28 | A |
| 7 (старый "обработать заметки") = **γ. Full Notion migration** | ⏳ | 2026-04-28..05-05 | B |
| 8 (новый) | Декомиссия Notion | ⏳ | после γ + 7 дней обкатки | B |
| 9 | Миграция knowledge-base/ legacy | ⏳ | parallel с γ | B |
| 10 | Стратегический документ (STRATEGY) | ⏳ | после 8 | A |

Даты ориентировочные. Цель `$50K до 30.06.2026` достигается после Шага 10.

---

## 11. Текущее состояние (2026-04-16, 20:00)

- **Серверный Claude Code:** Фаза 8 из 10 первого sweep run
  (SYSTEM-DESIGN-INPUTS filling). Completes ~20-30 мин.
- **Notion MCP на сервере:** ❌ не аутентифицирован (Фазы 2/3/4 пропущены).
- **Notion MCP локально (Windows):** ✅ работает.
- **Готово:**
  - `SYSTEM-DESIGN-HUMAN.md` каркас (279 строк)
  - 2 subagent'а + skill + 2 prompt-файла
  - `ARCHITECTURE-CURRENT.md` (Шаг 1 inventory)
  - `wiki/`: 60 ideas, 137 edges, 4 communities
  - 58/60 ideas помечены `topics:[system-design]` (серверный Claude, Фаза 5)
- **Не готово:**
  - Полный dump Банка идей (650+) в `raw/`
  - 11 Notion-страниц в `raw/notion-pages/`
  - Daily Log dump
  - `design/SYSTEM-DESIGN-INPUTS.md` полный (сейчас частично из 58 идей)

---

## 12. Следующие 3 хода (после окончания текущего server run)

### Ход 1 (локально, сейчас или сразу после server'а)

**Я (локальный Claude) делаю Notion dumps:**
- `raw/notion-bank-sweep-2026-04-16.jsonl` — metadata 650+ идей
- `raw/notion-pages/{11 slugs}.md` — 11 страниц о системе (full content)
- `raw/notion-daily-log-dump-2026-04-16.jsonl` — все Daily Log entries

Коммит + push. Префикс `[notion-α]`.

### Ход 2 (серверный Claude, запуск)

Даём серверному Claude новый промпт — уже не sweep через MCP, а:
- Прочитать dumps из `raw/`
- Для RELEVANT идей (по критериям) — `/ingest` локально из JSONL
- Для 11 страниц — `/ingest` per file
- Для Daily Log — выделить system-insights, digest → `/ingest`
- Дополнить `design/SYSTEM-DESIGN-INPUTS.md` новыми inputs
- Rebuild graph + lint
- Финальный отчёт

Коммит + push. Префикс `[notion-α]`.

### Ход 3 (Ruslan + я)

Ruslan открывает `design/SYSTEM-DESIGN-INPUTS.md` как второе панно (split view
в Antigravity). Диктует Часть 1 "Видение / Стратегия" SYSTEM-DESIGN-HUMAN.md.
Я (локально) структурирую и записываю с attribution.

---

## Приложение: принципы миграции (черновик, раскрывается на Фазе β)

Эти принципы будут раскрыты в Части 7 SYSTEM-DESIGN-HUMAN.md. Предварительный набросок:

1. **Additive only.** Ничего не удаляем из Notion до верификации переноса.
2. **Attribution всегда.** Каждая wiki-страница имеет `sources:` во frontmatter.
3. **Dedup by notion_id.** Не импортим дважды.
4. **Original text preserved.** Если идея в Notion короткая — wiki-страница может
   быть дольше (расширение), но оригинал сохраняется в source card.
5. **Frontmatter convention.**
   - `notion_id:` — всегда
   - `source_url:` — всегда
   - `captured:` — дата импорта
   - `created:` — createdTime из Notion
   - `topics:` — массив, обязательно `system-design` если относится
   - `niche:` — один из 6
   - `pipeline:` — `ingested` / `compiled` / `ready`
6. **Slug stability.** После Фазы γ slug'и НЕ меняются (чтобы wikilinks не ломались).
7. **Pilot before full.** Любая новая миграционная команда тестится на 10-20 pages
   перед полным запуском.
8. **Human-gate для неочевидного.** Если Claude сомневается при миграции —
   IRRELEVANT/UNCLEAR отдельный bucket для ручного ревью.

---

## История итераций

| Дата | Версия | Что изменилось |
|------|--------|----------------|
| 2026-04-16 | draft-v0 | Создан план: 4 фазы (α/β/γ/δ), 12 секций, roadmap обновлён до 10 шагов |
