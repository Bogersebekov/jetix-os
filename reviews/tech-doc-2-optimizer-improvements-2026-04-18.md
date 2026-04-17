---
type: review
role: optimizer
chat: 2
parallel-with: [1, 3, 4]
baseline: SYSTEM-DESIGN-HUMAN.md v1-beta-2026-04-18
created: 2026-04-18
status: complete
model: claude-opus-4-7 (extended thinking)
thinking-depth: extended-max
intent: "найти места где v1-beta может быть сильнее в ×10, а не в ×1.1"
---

# Review: Improvements for SYSTEM-DESIGN-HUMAN v1-beta-2026-04-18

> Чат 2 из 5 — Оптимизатор / Visionary. Работаю независимо от Критика (Чат 1)
> и Инженеров (Чаты 3-4). Baseline — v1-beta-2026-04-18 (2000 строк, 7 частей).
> Не критикую. Усиливаю. Ищу места где одна добавка даёт ×10, а не ×1.1.

---

## Executive Summary

v1-beta — это **отличный первый срез** (GitHub-style work, decommission Notion,
docs-as-code, 5-layer memory, Karpathy wiki). Но большинство его силы сейчас
**латентно**: архитектура позволяет ×10 leverage, а реально выдаёт ×1-2.
Моя задача — показать **где именно** этот рост ×5-×10 достижим малой добавкой.

**Топ-10 улучшений с наибольшим leverage (ранжировано `leverage / cost`):**

1. **Decision→Strategy auto-propagation** — каждое зафиксированное решение
   автоматически индексируется в `strategies.md` соответствующих агентов.
   Одна добавка = 12 агентов умнеют синхронно, каждый день.
   Leverage: ×10. Cost: 1 skill + 1 convention.

2. **Declarative Constitution** — SYSTEM-DESIGN-TECH.md становится
   конституцией, которую агенты **читают как system prompt**. Меняешь
   декларацию → всё поведение автоматически меняется. Leverage: ×8. Cost: frontmatter + include.

3. **Reverse index "questions → answers"** — `wiki/questions/` накапливает
   вопросы + какие wiki-страницы их закрыли. Через 2 месяца — "личный StackOverflow
   по собственной системе". Leverage: ×5. Cost: 1 skill + 20 строк шаблона.

4. **Natяжки-as-a-service (composable primitive)** — §4.5.2 сейчас
   описано концептуально. Перевести в **первоклассный skill** `/cross <what> <onto>`,
   запускаемый на любой паре сущностей (задачи×проекты, гипотезы×wiki,
   decisions×projects). Leverage: ×7. Cost: 1 skill + 1 wiki/crosses/ папка.

5. **Personalized PageRank (HippoRAG lite)** — на существующем
   `wiki/graph/edges.jsonl` добавить score через PPR. Answer quality ×3,
   никакой новой инфраструктуры. Leverage: ×6. Cost: 50-строчный Python.

6. **Fractal strategy — single-source include** — life-yearly/monthly/weekly
   связаны через **transclude blocks** (Obsidian-style `![[...]]`).
   Меняешь target в yearly — каскадно обновляется везде. Leverage: ×5. Cost: convention.

7. **Morning script `./jetix` CLI** — один Python-entry-point с subcommands
   (`jetix morning`, `jetix close-day`, `jetix review week`), который
   инкапсулирует весь semi-manual-mode. НЕ нарушает §5.0 (всё по команде).
   Leverage: ×4. Cost: 100-строчный main.py.

8. **Agent Cards v1-beta-lite** — 5-строчная карточка на агента (ПО ОДНОЙ
   странице, не Google Model Card), чтобы команда из 12 стала **психологически
   живой**. Ruslan начинает делегировать больше. Leverage: ×4. Cost: 12 × 5 строк.

9. **In-system metrics dashboard** — 5 счётчиков (strategies per agent,
   natяжки per week, decisions fixed, wiki edges growth, UNCLEAR bucket size)
   в одну `METRICS.md`, пересчитывается `/lint`. Leverage: ×4. Cost: 40 строк Python.

10. **Writeback confidence scores + temporal edges** — каждое edge
    получает `confidence` (0-1) + `valid-from`/`valid-until`. Zep/GraphRAG
    best-practice 2026. Меняет архитектуру wiki **фундаментально** при
    крошечном overhead. Leverage: ×5. Cost: 2 поля в edges.jsonl.

**Второй эшелон (leverage ×2-3, но обязательно в тех.документе):**

11. Timeboxing как first-class на каждом проекте (hours-budget + kill-criterion)
12. Event-sourced daily-log (уже ~де-факто, формализовать query-layer)
13. Mental models как отдельный `mental-models.md` + агент-доступ
14. Reflection-agent pattern (weekly honest critique, retro-edits)
15. Portable tar.gz standalone + тест восстановления на чистой VM за 30 мин

**Ключевое отличие моего взгляда от Критика (Чат 1):**
Критик будет перечислять где архитектура **хрупкая** (SPOF, сбои, edge cases).
Я показываю где она **недоиспользуется**. Два взгляда не заменяют друг друга —
Критик убирает **минусы**, Оптимизатор добавляет **плюсы**. Синтезатор
комбинирует.

**Центральная мысль моего review:**
> v1-beta уже имеет `text-as-database + git + Obsidian + Claude Code + wiki-graph`.
> Это — **Linux-kernel-grade** инфраструктура. Большинство предлагаемых улучшений
> не требуют **новой** инфраструктуры; они раскрывают уже имеющуюся.

---

## 0. Метод работы

Я прохожу по 20 категориям из промпта + добавляю ~12 своих. Для каждой
оптимизации даю:

- **Что усиливаем** (компонент SDH)
- **Механика** (как именно работает улучшение)
- **Expected leverage** (×2, ×5, ×10 — честная оценка)
- **Cost** (в человеко-часах или строках кода)
- **Prerequisite** (что должно быть)
- **Ссылка на §X.Y SDH**
- **Куда пишем** — в SYSTEM-DESIGN-TECH.md или в отдельный track

Leverage-шкала:
- **×1.5-×2** = улучшение. Желательно, но не критично.
- **×3-×5** = серьёзный multiplier. Попадает в тех.документ.
- **×7-×10** = архитектурный сдвиг. Должен быть в core v1-beta.

---

## 1. Композиционные улучшения (Composition leverage)

Система v1-beta имеет ~14-17 компонентов (Часть 6.1). Сила не в отдельных
компонентах, а в их **композиции**. Ищу пары/тройки компонентов, произведение
которых > сумма.

### 1.1 Decision log × agents/strategies.md — auto-propagation

**Что усиливаем:** §6.1.14 decisions + §6.1.13 agent strategies.md

**Механика:**
- Каждое решение в `decisions/life-decisions-log.md` или
  `projects/{x}/decisions.md` имеет frontmatter `relevant-agents: [sales-lead, strategist]`
- Skill `/propagate-decision {path}` читает frontmatter → для каждого
  указанного агента **дописывает ссылку** в его `strategies.md` (с datastamp)
- Агент при следующем запуске сразу видит: "19 апреля Ruslan решил что ICP = B2B SaaS founders"
- **Никакого re-learning** — знание течёт напрямую

**Leverage:** ×10. Одно решение → 12 агентов умнеют, без human re-teaching.

**Cost:** 1 skill (`/propagate-decision`), 30 строк Python, конвенция
frontmatter `relevant-agents:`.

**Prerequisite:** decisions/ директория + strategies.md у агентов (есть).

**SDH ref:** §4.2.4, §6.1.13, §6.1.14.

**Куда:** SYSTEM-DESIGN-TECH.md (core pattern). **Обязательно**.

---

### 1.2 Натяжки × gradient-boosting cycle

**Что усиливаем:** §4.5.2 натяжки.

**Механика:**
- Натяжка #1 (гипотезы × проект) находит связь X
- X записывается в `wiki/graph/edges.jsonl` как edge с type `cross_suggested`
- Натяжка #2 на следующей неделе видит edge X **как input** — не переоткрывает
- Через 4 недели: система знает 50+ уже найденных cross-связей, ищет только
  **новые паттерны поверх существующих**
- Это **gradient boosting**: каждая итерация базируется на residual от прошлых

**Leverage:** ×7. Композиция `text-as-database + graph-edges + natяжки` делает
compounding.

**Cost:** дописать в edges.jsonl новый edge type + 1 строку в натяжка-шаблоне
"учитывай уже найденные `cross_suggested`".

**SDH ref:** §4.5.2 + §4.5.1.

**Куда:** SYSTEM-DESIGN-TECH.md. Обязательно.

---

### 1.3 CRM × Daily Log × wiki — identity-resolution loop

**Механика:**
- Упоминание человека в `daily-log/` (скажем "звонил с Андреем")
- Агент при close-day делает grep имён → matches с `crm/partners.md`
- Если нет — предлагает создать карточку
- Если есть — **дописывает** строку interaction в CRM + edge `mentioned_in`
  между daily-log и crm
- Дальше `/ask "что я обсуждал с Андреем за последние 3 месяца"` возвращает
  cross-timeline outline с цитатами

**Leverage:** ×5. Решает sales-проблему (нужно вспомнить что-то про клиента)
в 10x меньше времени.

**Cost:** 1 skill (`/reconcile-people`), 50 строк Python.

**SDH ref:** §6.1.9, §6.2.4.

**Куда:** SYSTEM-DESIGN-TECH.md как pattern. Поставить после v1-beta base, не блокирующее.

---

### 1.4 Projects × ideas-pool × hypotheses — cross-pollination

**Механика:**
- Каждую пятницу агент запускает натяжку: все активные гипотезы × все 8 проектов
- Результат: "гипотеза Y из проекта `quick-money` может ускорить `ai-tools`"
- Ruslan видит 5-10 таких cross-suggestions, 1-2 обычно релевантны
- **Без натяжек** эти связи просто не обнаруживаются

**Leverage:** ×4. Не линейное — cross-pollination растёт **квадратично** к числу проектов.

**Cost:** скрипт натяжки (см. 1.2) + template cross-report.

**SDH ref:** §4.5.2, §6.1.4.

---

### 1.5 Wiki × reflection/ — honest critique pipeline

**Механика:**
- Reflection-agent раз в неделю читает: daily-log, decisions, wiki-новое
- Ищет **противоречия** между новыми знаниями и старыми (edge type `contradicts`)
- Пишет `reflection/insights/{YYYY-WW}-honest.md` — "ты заявил X в январе, но
  в апреле действовал как если бы NOT X. Пересмотреть?"
- Это **уровневая самокритика**

**Leverage:** ×5. Без этого strategies.md деградируют (stale rules, копятся противоречия).

**Cost:** reflection-agent strategy + 1 weekly ritual slot.

**SDH ref:** §6.1.11 + §6.1.13.

**Куда:** SYSTEM-DESIGN-TECH.md. Ставлю как важный pattern, не блокирующий.

---

### 1.6 Композиция tools-catalog × wiki — self-describing tool ecosystem

**Механика:**
- Каждая карточка в `tools-catalog/{slug}.md` имеет секцию `learned-patterns:`
  — куда агенты дописывают "вот так работает хорошо", "эта ручка не работает"
- При следующей работе агент читает tool-card **в полном объёме**, не
  "переоткрывает" как использовать
- Инструменты **учатся сами** через агентов-пользователей

**Leverage:** ×3-×4. Особенно ощутимо через 1-2 месяца использования.

**Cost:** convention в шаблоне tool-card.

**SDH ref:** §6.1.6.

---

### 1.7 Daily-log/drafts/ × wiki-writeback (recombination surface)

**Механика:**
- §6.2.4 — drafts/ это песочница для работы, чистовик в проекты
- Добавить convention: каждый draft имеет `promoted-to: [path1, path2]` frontmatter
- `/close-day` читает frontmatter всех drafts за сегодня → делает writeback
  (copy chunks, edges, links)
- drafts сами **знают куда их содержимое ушло**
- Через месяц: можно reverse-query "какие drafts породили какие wiki-pages?"
  и видеть productive vs non-productive drafts

**Leverage:** ×3.

**Cost:** 1 frontmatter + skill hook в /close-day.

**SDH ref:** §6.2.4.

---

## 2. Паттерн "text-as-database" — раскрытие супер-силы

v1-beta уже использует text-as-database, но **не формализует** возможности.
Это ломает leverage — люди, которые придут позже, не увидят что этот паттерн
даёт бесплатно.

### 2.1 Явно зафиксировать "5 способов query одного набора текста"

В SYSTEM-DESIGN-TECH.md добавить секцию **"Five-way query surface"**:

| Способ | Инструмент | Когда использовать |
|--------|-----------|---------------------|
| Machine-diff | git | "что изменилось с 2026-04-12" |
| Human-navigation | Obsidian graph | "покажи соседей этой страницы" |
| Instant search | ripgrep | "все упоминания Андрея" |
| NL query | Claude Code /ask | "что я думал про pricing" |
| Bulk ops | Python scripts | "отметить все claims с evidence=null" |
| **Structural query** | **SQL через duckdb over frontmatter** | **"все проекты со status=active и updated<7d"** |

**Leverage:** ×5. Человек (или агент) **видит** какие запросы доступны, поэтому
использует их.

### 2.2 DuckDB over frontmatter — 6-й способ

**Критически недооценённая возможность.** DuckDB умеет читать YAML из markdown
фронтматтеров как таблицу. Запросы:

```sql
SELECT slug, updated FROM 'wiki/**/*.md'
WHERE status = 'active' AND updated < current_date - 7
```

**Leverage:** ×8 для operational queries. Lets us build dashboards **без**
отдельной БД. Text-as-database становится **настоящей** БД с запросами.

**Cost:** `duckdb` установить + 50-строчный скрипт-обёртка.

**SDH ref:** §4.1, §4.3.

**Куда:** SYSTEM-DESIGN-TECH.md. Обязательно в v1-beta-tech. Это ×10 для
Ruslan когда нужно отчитаться "что я делал", без правок миллиона файлов.

### 2.3 Markdown pipes через Pandoc — 7-й способ

Любая wiki-страница → PDF / slides / docx через Pandoc. Для консалтинга (P1 goal!)
это критично — выдавать клиентам документы, не markdown.

**Leverage:** ×3.

**Cost:** pandoc + template.

### 2.4 Mermaid / Graphviz in-markdown — visualisable primitives

Вместо отдельных Miro-схем — **часть** схем живёт **в тексте** как Mermaid
блоки. Git diffable, updateable агентами. Obsidian рендерит.

**Leverage:** ×4 для schemas которые меняются (архитектура). Miro остаётся для
"один раз нарисовал, не правлю".

**Cost:** convention + примеры.

### 2.5 JSON-LD slots в frontmatter — machine-readable semantics

Пример:
```yaml
---
type: decision
schema: https://jetix.dev/schemas/decision-v1.json
@context: { "decided": "https://schema.org/dateCreated" }
decided: 2026-04-18
---
```
Через год система может быть "пропущена через machine-readable pipeline"
без переписывания всего. Форвард-совместимость.

**Leverage:** ×2 сейчас, ×5 через год. Дёшево, защищает будущую ценность.

**Cost:** convention.

---

## 3. Self-improvement primitives — Karpathy System Prompt Learning

v1-beta упоминает strategies.md, но не формализует цикл улучшения.

### 3.1 Semantic versioning strategies

Каждый strategies.md — имеет версии:
- `v0` — пустая
- `v1` — первичные правила
- `v2` — после первой ретроспективы
- `vN` — с semantic diff между версиями

В frontmatter: `version: 2`, `deltas-since-v1: 3 added, 1 removed`.

Каждое изменение — git commit + changelog section.

**Leverage:** ×3. Критично для того чтобы **видеть** эволюцию агента.

### 3.2 Evidence attachment — правила с "откуда пришли"

Каждое правило в strategies.md имеет секцию "evidence:":
```markdown
- **Rule:** When writing cold emails, start with specific context (not "I saw your LinkedIn")
  - **Why:** empirically higher response rate in §decisions/2026-04-11-coldmail-test.md
  - **Added:** 2026-04-12 after reviewing week-17 sales results
```

Без evidence — правила превращаются в догмы. С evidence — правила можно **усомнить**
и **пересмотреть** rationally.

**Leverage:** ×4. Meta-agent consolidation работает ТОЛЬКО если есть evidence.

### 3.3 Cross-agent learning — shared-strategies.md

Некоторые уроки универсальны (ex: "SAFE-SAVE при любой ошибке"). Вместо
копии в 12 агентов — `agents/_shared/strategies.md`, на который ссылаются
все через transclude.

**Leverage:** ×3. One fix propagates to 12 agents.

**Cost:** 1 shared file + convention.

### 3.4 Meta-agent как реально работающий consolidator

Сейчас meta-agent в roster (§CLAUDE.md), но не активен. Дать ему еженедельное
задание:
1. Читать все 12 `strategies.md`
2. Искать (a) противоречивые правила между агентами, (b) дубликаты
   (одно и то же разной формулировкой), (c) устаревшие (evidence старше 3 мес)
3. Предлагать консолидацию как PR-draft в `reports/strategies-consolidation-{date}.md`
4. Ruslan apply / reject

**Leverage:** ×5 через 2 месяца работы.

**Cost:** 1 agent system.md + weekly trigger (по команде Ruslan).

### 3.5 A/B versioning — новая strategy сначала в 10% задач

Из §6.1.13 point 4 уже упомянуто. Усилить:
- Новое правило добавляется как `strategies-experimental.md`
- Выбирается для 10% запусков агента
- Через 7 дней — метрика (success rate)
- Meta-agent предлагает merge или discard

**Leverage:** ×4. Защищает от плохих правил.

**Cost:** skill `/ab-test-strategy` + flag в agent launcher.

---

## 4. Context engineering — 4 стратегии Karpathy (Write / Select / Compress / Isolate)

v1-beta упоминает, но **не формализует**. SYSTEM-DESIGN-TECH.md должен явно
положить каждую стратегию в конкретные механизмы.

### 4.1 Write — явное правило "куда пишем"

Создать `docs/context-write-matrix.md`:

| Тип информации | Пишется в | Кто пишет | TTL |
|----------------|-----------|-----------|-----|
| Сырой input | raw/, inbox/ | Человек/автотул | forever |
| Working memory | agents/{id}/scratchpad.md | агент во время задачи | session |
| Strategy rule | agents/{id}/strategies.md | агент или Ruslan | reviewed quarterly |
| Decision | decisions/ | Ruslan | forever |
| Fact + evidence | wiki/claims/ | агент | reviewed quarterly |
| Conversation cache | comms/mailboxes/ | агент | 90 дней, затем summarized |

**Leverage:** ×5. Без этой матрицы агенты каждый раз заново решают "а где это?"

### 4.2 Select — frontmatter selector + niche filter

Агент при старте читает:
1. Свой `system.md` (core)
2. Свой `strategies.md` (накопленное)
3. Срез wiki через `niche/` symlinks
4. Релевантный кусок scratchpad'а

Формализовать как **context-loader protocol**: `load-context {agent-id}` возвращает
MCP-ready bundle. Один entry-point.

**Leverage:** ×4. Решает "cold start" проблему агентов.

### 4.3 Compress — 3 уровня компрессии

1. **L1 raw text** — полный
2. **L2 summaries** — `wiki/summaries/{date}-{topic}.md` — компактный digest
3. **L3 abstract edges** — на уровне графа, без текста, только связи

При context-loading использовать L1 если <10k tokens, L2 если <100k, L3 для overview.

**Leverage:** ×5 для огромных проектов где L1 не влазит.

### 4.4 Isolate — per-agent context + Task-tool subagents

Убедиться что каждый agent spawn (`Task tool`) получает **отдельный**
context window, и возвращает **только итог**, не trace. Это уже so в Claude Code,
но формализовать как правило в тех.документе.

**Leverage:** ×5 для долгих задач.

---

## 5. HippoRAG + GraphRAG over existing wiki/graph

### 5.1 Personalized PageRank (HippoRAG lite)

На существующих 572 edges — запустить PPR с seed = текущий вопрос. Top-20
nodes по PPR-score > keyword-search в 3-5× по relevance.

**Механика:**
- `/ask question` → находит keyword matches → PPR от них → top-20 ranked nodes
- эти nodes в context → LLM отвечает + сites

**Leverage:** ×5-×8. Это **major upgrade** для /ask качества.

**Cost:** 50-строчный Python (networkx + pagerank).

**SDH ref:** §4.4, §4.5.

**Куда:** SYSTEM-DESIGN-TECH.md. Обязательно для v1-beta-tech.

### 5.2 Community summaries hierarchical (GraphRAG Microsoft)

Сейчас `wiki/graph/communities.md` — 1-уровневый. Добавить:
- L1: 4 communities (есть)
- L2: 12-20 sub-communities внутри каждой L1
- L3: individual pages

Каждый уровень имеет auto-generated summary. При глобальном запросе ("what's
going on in my system?") — используется L1 summary. Для фокусированного —
L2 или L3.

**Leverage:** ×4. Компактность для любого масштаба вопроса.

**Cost:** `/build-graph` рефактор + один generate-summary pass.

### 5.3 Temporal edges — fact validity windows (Zep pattern)

Каждый edge в `edges.jsonl`:
```json
{"from":"ideas/icp","to":"entities/b2b-saas","type":"refers_to","valid_from":"2026-04-01","valid_until":null,"confidence":0.9}
```

Когда ICP изменится (скажем, решим "B2C founders instead") — старый edge
получает `valid_until: 2026-05-15`, новый edge начинается. Wiki **помнит
историю утверждений**, а не только snapshot.

**Leverage:** ×5. Фундаментальный для "temporal queries" которые Ruslan
уже упоминает в §4.4 ("что я думал 3 месяца назад").

**Cost:** 2 опциональных поля в edges.jsonl schema.

**SDH ref:** §4.4.

**Куда:** SYSTEM-DESIGN-TECH.md. **Обязательно**.

### 5.4 Confidence scores on edges

Каждое edge — `confidence: 0-1`. Генерируется агентом при создании
(`/ingest` ставит 0.8 если явная цитата, 0.5 если inferred).

Запросы могут фильтровать по confidence: `confidence > 0.7`.

**Leverage:** ×3. Improves answer quality.

### 5.5 Derived-edges через PPR results

PPR результат вычисляется → сохраняется новый тип edge `inferred_by_ppr` (с
confidence из PPR-score). В следующий раз PPR **не надо запускать** на том же
вопросе — результат уже в графе. **Cache-layer** в графе.

**Leverage:** ×3.

**Cost:** 1 convention.

---

## 6. Declarative > Imperative — архитектурный сдвиг

### 6.1 SYSTEM-DESIGN-TECH.md становится declarative constitution

**Сдвиг от:** "агент делает X когда Y" (imperative, разбросано по агентам).
**К:** "система устроена так: при Y должно быть X". Агенты читают declarative
description → сами understand что делать.

**Как это выглядит:**
```markdown
## Invariant 1. Для каждого decision существует ref из одного strategies.md

Если `decisions/X.md` создан → хотя бы один agent `strategies.md` должен
ссылаться на него. `/lint` проверяет нарушения.
```

Агент который видит invariant — знает что нужно propagate. Конкретный skill
`/propagate-decision` — просто one implementation of the invariant.

**Leverage:** ×10. Меняешь constitution → 12 агентов меняют поведение
automatically. **Это Kay-принцип в чистом виде.**

### 6.2 Invariants list — 10-20 жёстких утверждений

Пример invariants:
1. Каждое decision имеет evidence или "no-evidence: intuition"
2. Каждая wiki-page имеет frontmatter `updated: YYYY-MM-DD`
3. Нет wiki-pages без edges (orphans лечит /lint)
4. Каждый activt project имеет live strategy.md
5. daily-log/ append-only, не editable после close-day
6. agents/*/scratchpad.md cleared at start of session
7. …

**Leverage:** ×8. Система self-validates.

**Cost:** 1 секция в SYSTEM-DESIGN-TECH.md + /lint checks.

### 6.3 Agents read SYSTEM-DESIGN-TECH.md как часть context

Literally каждый агент в своём system.md начинает с:
```markdown
Прочитай `design/SYSTEM-DESIGN-TECH.md` §invariants. Ты обязан их соблюдать.
```

Constitution приходит **в каждый запуск**. Меняешь в одном месте.

**Leverage:** ×10.

**Cost:** 1 строка в 12 agent system.md.

---

## 7. Event sourcing для операционных данных

v1-beta **де-факто** event-sourced благодаря git + append-only. Формализуем
и усиливаем.

### 7.1 Unified event log

Создать `shared/events.jsonl` — append-only лог всех "событий системы":
- decision created
- project created
- idea ingested
- strategy updated
- natяжка run
- agent spawned

```json
{"ts":"2026-04-18T09:15:23Z","type":"decision.created","actor":"ruslan","ref":"decisions/2026-04-18-pivot.md"}
```

Reply lets reconstruct any snapshot. Queries: "какие решения было за
последнюю неделю?" → `jq '.type=="decision.created" | .ts > today-7d'`.

**Leverage:** ×6. Единый источник правды для всех cross-component queries.

**Cost:** 1 JSONL + hooks в существующие skills.

**SDH ref:** §4.0 + §6.

### 7.2 Temporal queries — "что я думал про X 3 месяца назад"

Из §4.4 Ruslan явно хочет такие запросы. Но без event log они работают только
через `git log` (неудобно).

С event log + temporal edges (см. 5.3) — skill `/timetravel 2026-01-15 "pricing"`
возвращает: "на эту дату у тебя были claims X, Y, decisions Z, гипотезы W".

**Leverage:** ×5.

**Cost:** 1 skill.

### 7.3 Event log для агентов — "what agents did today"

Каждый agent spawn пишет event `agent.started`, `agent.finished`, с ref
на scratchpad/report. Ruslan может в одну команду видеть: "сегодня sales-lead
запускался 3 раза, среднее время — 8 мин".

**Leverage:** ×3.

### 7.4 Replay pattern — re-run past decisions under current state

**Мощная идея:** зафиксированное decision.md имеет секцию `replay-check:` —
как проверить, что решение всё ещё valid.

Skill `/replay decisions/2026-03-15-stop-notion.md` читает replay-check,
исполняет, отчитывается "decision still valid" / "conditions changed, revisit".

Weekly reflection-agent запускает replay на 10 случайно выбранных decisions.

**Leverage:** ×5. Защита от drift (решения устаревают незаметно).

**Cost:** convention в decisions + 1 skill.

---

## 8. Multi-level страт.документы как fractal

Сейчас §6.1.8: life (yearly, monthly, weekly). Проектные (видение + steps).
Усиление — через **transclude**.

### 8.1 Transclude Obsidian-style `![[path#block]]`

Монтoring:
- yearly.md определяет "2026 goal: $50K" как block `^goal-revenue-2026`
- monthly.md `transcludes ![[2026-yearly#^goal-revenue-2026]]`
- weekly.md тоже
- daily.md в utren-planning section тоже

Меняешь goal-revenue-2026 в yearly → все ниже **автоматически показывают новое**.

**Leverage:** ×5. Single source of truth во фрактальной иерархии.

**Cost:** convention + Obsidian already supports.

### 8.2 Cascade dirty marking

Если weekly-16 не достиг milestone → auto-add `[status:missed]` в monthly.md
referring week. При generate monthly-report — видно какие weeks просели.

**Leverage:** ×3.

### 8.3 Strategic-doc live-linking с проектами

Проект X имеет `strategy.md`. В `strategy/projects/X/strategy.md` — же.
Объединить: проект имеет **один** strategy.md, путь `projects/X/strategy.md`.
`strategy/projects/` — это transcludes плюс sync check.

**Leverage:** ×2.

### 8.4 Quarterly OKR-style goal decomposition

Годовая цель → 4 квартальных key-results → 13 недельных milestones.
Декомпозиция **формализована** в шаблоне strategy. Через 3 месяца видно
какие квартальные KR выполнены.

**Leverage:** ×4. Делает $50K-цель executable, не aspirational.

---

## 9. Agent Cards — lightweight v1-beta version

§3.2.3 отложил детальные cards на v1-final. Но **5-строчная** версия —
дешёво и даёт big leverage.

### 9.1 Карточка = ~10 строк на агента

```markdown
# sales-lead

**Kind:** Sonnet 4.6. **Department:** Sales (lead).
**Intended use:** Координация sales-активностей, ICP calls, обзор pipeline.
**Inputs:** crm/clients.md, wiki/topics/sales-*, niche/sales/
**Outputs:** reports/sales-*.md, updates в crm/, strategies.md
**Limitations:** Не делает исходящие сообщения (для этого sales-outreach).
**Activation:** Каждое утро по команде /morning, при /ask sales вопросов.
```

**Leverage:** ×4.

1. Психологически: Ruslan видит "команду", легче делегирует
2. Новый Claude-сессия читает card за 3 секунды
3. Community / партнёры получают мгновенное понимание ролей

**Cost:** 12 × 10 строк = 120 строк в ОДИН файл `agents/CARDS.md`.

**SDH ref:** §3.2.3.

**Куда:** SYSTEM-DESIGN-TECH.md приложение или отдельный `AGENT-PROTOCOLS.md`.

### 9.2 Agent cards as typed schema

frontmatter для cards:
```yaml
---
type: agent-card
version: 1
kind: sonnet
department: Sales
activation: [morning, on-request]
---
```

**Leverage:** ×3. Query "какие агенты с activation=morning" → список.

---

## 10. Knowledge as first-class citizen (active wiki)

### 10.1 Wiki subscriptions

Каждая topic-hub-page имеет `subscribes-to: [tag:sales, author:sales-lead]`.
При новой ingest с этим tag — wiki auto-rebuilds topic-hub (inserts новую
ссылку, пересчитывает TOC).

**Механика:** git-hook post-commit или `/ingest` отдельно триггерит rebuild.

**Leverage:** ×4. Тopic-hub'ы не устаревают.

**Cost:** 1 skill `/rebuild-topic-hub`.

### 10.2 Wiki → agent ping

Когда `wiki/niche/sales/` получает новый file — sales-lead `scratchpad.md`
добавляет строку "новый material 2026-04-18: см. ..." . При следующем
запуске агент видит.

**Leverage:** ×3.

### 10.3 Weekly digest авто-draft

Reflection-agent по воскресеньям → читает все wiki-additions за неделю →
драфт `reports/weekly-digest-{YYYY-WW}.md`. Ruslan читает 5 минут, получает
сводку.

**Leverage:** ×4. Time-saver for Ruslan.

### 10.4 Stale-tags automatic

Wiki-page без updates > 90 дней получает frontmatter `status: stale`.
`/lint` показывает stale. Ruslan revisits.

**Leverage:** ×3. Борется с knowledge rot.

---

## 11. Mental models — отдельный артефакт

Сейчас метафоры (машина, велосипед, GitHub, песочница, дом-комнаты-водопровод,
оркестр) разбросаны. Вынесение в `mental-models.md`:

### 11.1 Формат

```markdown
## Метафора "машина" (Jetix OS)
**Что объясняет:** зачем нужен оператор, почему без Ruslan'а не едет.
**Источник:** Ruslan, диктовка 2026-04-17. См. §1.5 SDH.
**Где использовать:** при объяснении новым людям / агентам роли Ruslan.
**Расширения:** "водитель-механик" (3.1.5), "топливо" (3.1.5).
---
## Метафора "GitHub-style работа"
...
```

12-15 метафор в одном файле.

**Leverage:** ×4. Новые люди понимают систему за 20 мин. Агенты **используют
эти же метафоры в общении с Ruslan** (говорят на его языке).

**Cost:** 1 файл, ~200 строк.

**SDH ref:** §1.1, §3.1.5, §6.2.4.

**Куда:** `mental-models.md` отдельно (не в SYSTEM-DESIGN-TECH.md, но
ссылается туда).

### 11.2 Agents load mental-models.md

В system.md каждого агента: "если нужно объяснить концепт Ruslan'у — используй
метафоры из `mental-models.md`, не придумывай новые без необходимости".

**Leverage:** ×3. Consistent communication language.

---

## 12. In-system metrics — compounding observability

§2.3 — out-of-system метрики ($50K, 200 контактов). Добавить in-system,
которые видны **сегодня**, не через 3 месяца.

### 12.1 Метрики-счётчики

Все пишутся в `METRICS.md` (regenerate от `/lint`):

| Метрика | Формула | Что показывает |
|---------|---------|----------------|
| total-strategies-rules | Σ lines в strategies.md * | рост коллективной мудрости |
| natяжки-per-week | count cross-reports за 7 дней | работает ли аналитика |
| decisions-logged-per-week | новые decisions/*.md | захватываем ли решения |
| unclear-backlog | count UNCLEAR в всех scratchpad | здоровье обработки |
| wiki-edges-total | lines в edges.jsonl | рост графа |
| wiki-edges-per-week | diff edges.jsonl vs 7d ago | compounding |
| orphans-count | /lint orphans | wiki health |
| stale-claims | claims без updates > 90d | rot |
| drafts-promoted | drafts c promoted-to filled | productivity песочницы |
| decisions-replayed-valid | /replay result | drift level |

**Leverage:** ×5.

**Cost:** 1 скрипт Python, 100 строк.

### 12.2 Delta reports

Еженедельно — diff METRICS.md vs 7 days ago в `reports/metrics-delta-{week}.md`.
Ruslan видит тренды.

**Leverage:** ×3.

### 12.3 Metrics-as-code (plots)

Если через месяц появится Streamlit dashboard — plots on METRICS.md log. Но
даже без plots — числа уже дают value.

---

## 13. Ритуал-скрипты (а не документы)

§5.5 описывает ритуалы как списки. Сделать как Python:

### 13.1 Единый CLI `./jetix`

```bash
./jetix morning          # opens daily-log, loads context, drafts plan
./jetix close-day        # processes drafts, updates wiki, commits
./jetix review week      # weekly analytic natяжки + report
./jetix review month     # monthly
./jetix propagate <dec>  # propagate decision to agents
./jetix replay <dec>     # run replay-check on decision
./jetix metrics          # regenerate METRICS.md
./jetix lint             # /lint
./jetix ingest <path>    # /ingest
./jetix ask <question>   # /ask
./jetix context <agent>  # load-context for agent
```

ВАЖНО: НЕ нарушает §5.0 полуручной режим. Ruslan **сам** вызывает.

**Leverage:** ×5. Один entry-point вместо 10 разных commands.

**Cost:** 1 Python main.py + argparse, ~150 строк.

**SDH ref:** §5.5, §5.0.

**Куда:** SYSTEM-DESIGN-TECH.md как "operational interface". Обязательно.

### 13.2 `./jetix` как skill-router

Под капотом — маппинг subcommand → Claude Code skill call. Но Ruslan'у
видно как unified CLI.

**Leverage:** ×2. Снижает cognitive load.

### 13.3 Self-documenting through `--help`

`./jetix --help` возвращает markdown table всех команд + что делают. Это
живая документация, не устаревает.

**Leverage:** ×3.

---

## 14. Kay principle deeper — vendor diversity

§3.5.2 заявляет "работает без AI". Усиление — активно проектируем vendor
diversity **в core**:

### 14.1 LLM abstraction layer

Все calls через `tools/llm.py` wrapper:
```python
def llm(prompt, model="anthropic/claude-opus-4-7"):
    provider, model_name = model.split("/")
    return PROVIDERS[provider].call(model_name, prompt)
```

Завтра Anthropic down → `export JETIX_LLM=openai/gpt-4o` → всё работает.

**Leverage:** ×8. Критично для $50K-goal (Claude API down во время клиент-call
— catastrophic).

**Cost:** 1 модуль, ~100 строк.

**SDH ref:** §3.5.2, §5.6.3.

**Куда:** SYSTEM-DESIGN-TECH.md. Обязательно.

### 14.2 Voice: Groq Whisper + OpenAI Whisper fallback

Такой же паттерн для transcription.

**Leverage:** ×3.

### 14.3 Embedding providers abstraction (future)

Готовность к vector search. Не делать сейчас, но reserve abstraction point.

**Leverage:** ×2 сейчас, ×5 через полгода.

### 14.4 No MCP hard-dependencies in core

Core skills (`/ingest`, `/ask`, `/lint`) — не должны требовать MCP. Только
optional enhancement. Сейчас частично так, формализовать.

**Leverage:** ×5 (см. §5.6.2 проблему с Notion MCP).

---

## 15. Reflection-agent — уровневая самокритика

### 15.1 Weekly honest retrospective

Агент reflection (активация по воскресеньям):
1. Читает daily-log последних 7 дней
2. Читает все commits с `[decision]` tag
3. Читает новые wiki-additions
4. Читает texts/chats (если есть)
5. Пишет `reflection/insights/{YYYY-WW}-honest.md`:
   - Что работало (evidence)
   - Что не работало (с честными признаниями)
   - Противоречия в decisions
   - Stale goals (заявленная но не тронутая цель)
   - Suggested re-decisions

**Leverage:** ×6. Без этого стратегии тонут в повседневности.

**Cost:** 1 agent, 1 weekly ritual.

### 15.2 Anti-goal log

Reflection пишет "anti-goals" — что Ruslan **заявил** не делать, но в
commits / daily-log видно что делал. "Ты говорил 'не берусь за клиентов
без budget', но 3 апреля начал работать с X без budget confirm".

**Leverage:** ×5. Жёсткий mirror.

### 15.3 Silence log

Что Ruslan **не** сделал, хотя планировал (из plan day vs close-day gap).
Трек "что постоянно откладывается — сигнал пересмотра приоритетов".

**Leverage:** ×4.

---

## 16. Portable standalone mode

v1-beta привязан к server + Claude Code. Тест переноса:

### 16.1 `./jetix export` → tar.gz

```bash
./jetix export > jetix-backup-2026-04-18.tar.gz
```

Включает: все файлы репо, текущий state (JSON), commits history.

**Leverage:** ×3. Disaster recovery.

**Cost:** 30-строчный script.

### 16.2 `./jetix import` → чистая VM за 30 мин

На чистой Ubuntu:
```bash
curl jetix.dev/install | bash   # installs Python, Claude Code, deps
./jetix import jetix-backup.tar.gz
```

Работает.

**Leverage:** ×5. Даёт ПАРТНЁРАМ (5-10 через 3 мес — §1.6) запустить копию.

**Cost:** install.sh + import.sh, ~50 строк.

### 16.3 No-AI mode

`./jetix --no-ai` — все skills которые могут работать без LLM (grep, lint,
consolidate, metrics) работают. Kay-принцип в экшн.

**Leverage:** ×5.

---

## 17. Public story wiki + private operational wiki

### 17.1 Split через tag / frontmatter

Каждая wiki-page имеет frontmatter `visibility: public | internal | private`.
- `public`: рендерится через mkdocs → static site GitHub Pages
- `internal`: сервер only
- `private`: агенты не видят (for health etc.)

### 17.2 Public marketing — "living methodology"

`public` pages — manual, methodology, case studies. Обновляется with каждым
ingest. Jetix marketing **бесплатно** — мы демонстрируем систему изнутри.

**Leverage:** ×5 через 2-3 месяца (когда material станет rich).

**Cost:** 1 tag + mkdocs config.

### 17.3 Public contribution

Open-source premium: публичные pages имеют `edit on GitHub` → сообщество
contributes в методологию.

**Leverage:** ×3 (долгий compounding).

---

## 18. Templates as code — Jinja2 placeholders

### 18.1 Interactive project-creator

```bash
./jetix new project
# What slug? quick-money-v2
# Goal? $10k MRR
# Deadline? 2026-06-30
# Resources? 2h/day
→ creates projects/quick-money-v2/ with filled overview.md, strategy.md, log.md, tasks.md
```

**Leverage:** ×4. Zero friction start — проект стартует за 30 сек.

**Cost:** 1 CLI + 3-5 templates with Jinja.

### 18.2 Daily-log template с переменными

Заменить static template на `daily-log/_template.md.j2` с переменными
(yesterday-goals, today-focus, weekly-target). При open — render с
свежими данными.

**Leverage:** ×3.

### 18.3 Decision template с checklist

```markdown
## Decision {{slug}}
**Date:** {{date}}
**Context:** <fill>
**Alternatives considered:** <fill>  ← обязательно (vs Google Design Doc)
**Decision:** <fill>
**Evidence / basis:** <fill>
**Replay-check:** <how to verify 3 months later>
**Propagate to agents:** [<list>]
```

Структура принуждает к качеству.

**Leverage:** ×4.

---

## 19. Migration patterns как reusable skill

Фаза α migration (sweep-worker + staging-writer parallel) — уже работала
(5× speedup из NOTION-MIGRATION-PLAN). Институционализировать:

### 19.1 Abstract "migration pattern"

```yaml
type: migration-pattern
phases:
  - scan: list all items
  - classify: RELEVANT / IRRELEVANT / UNCLEAR
  - relevant: ingest in batches (parallel workers)
  - unclear: manual review
  - report: final stats
```

Reusable для:
- knowledge-base legacy → wiki (Шаг 9)
- voice-memos backlog → wiki
- old Claude chats → wiki
- any future big migration

**Leverage:** ×7 (institutional knowledge preserved).

**Cost:** extract pattern из existing sweep-worker, document, template.

### 19.2 Dry-run mode

Любой migration — сначала `--dry-run`, печатает что будет делать, Ruslan
одобряет, потом real run.

**Leverage:** ×3 (safety).

---

## 20. Моя свобода — 10+ добавочных идей

### 20.1 `wiki/questions/` — reverse index "вопрос → ответ"

**Механика:** каждый раз когда Ruslan задаёт `/ask X`, вопрос + summary ответа
сохраняются в `wiki/questions/{YYYY-MM-DD}-{slug}.md` с:
- вопрос
- 5 самых релевантных wiki-pages (links)
- короткий synth
- frontmatter `times-asked: 1, last-asked: ...`

Если через месяц Ruslan задаёт похожий вопрос → `/ask` видит existing entry,
inc'ит `times-asked`, показывает **прошлый ответ** + "что добавилось с
тех пор" (diff).

**Личный StackOverflow через compounding.**

**Leverage:** ×6.

**Cost:** 1 hook в /ask, 1 frontmatter convention.

### 20.2 Challenge-response verification для больших решений

Перед Ruslan'ом commit'ит decision — pre-commit hook запускает agent-challenger:
"Я видел твоё решение. 3 вопроса:
1. Evidence для этого?
2. Alternatives considered?
3. Как проверить что решение работает через 3 мес?"
Ruslan отвечает → decision.md дописывается → commit.

**Leverage:** ×5. Forced rigor.

**Cost:** 1 agent + git hook.

### 20.3 Dual-Claude review ("senior + junior")

Любое большое изменение (commit > 500 LOC, или decision, или strategy edit) —
автоматически запускает **второй** Claude instance как adversarial reviewer.
Review в PR-comment стиле, Ruslan видит до merge.

**Это уже paradigm 5-chat methodology** (этот review один из них). Но
институционализировать для малых событий тоже.

**Leverage:** ×5.

### 20.4 Self-describing skill `/describe-self`

Запускается любым агентом: "кто я, что делаю, какой context у меня сейчас,
последние 3 моих action'а". Ouput — compact summary.

External agent (новый Claude-session, партнёр) запускает `/describe-self
jetix-os` → получает state-of-system за 30 сек.

**Leverage:** ×4. Meta-observability.

### 20.5 Timeboxing as first-class on projects

Каждый `projects/X/overview.md` обязан иметь:
```yaml
budget-hours: 120
budget-weeks: 8
kill-criterion: "if <$5K MRR by week 6, pivot"
```

При `/review week` — агент видит over-budget projects, предлагает kill
или re-commit.

**Leverage:** ×7. Защищает от zombie-projects (большая проблема для solo entrepreneurs).

**Cost:** convention в template + 1 check в review.

**SDH ref:** §6.1.1, §6.2.1.

**Куда:** SYSTEM-DESIGN-TECH.md. Обязательно. Это **бизнес-критично** для $50K.

### 20.6 Knowledge debt tracker

`/lint` показывает "knowledge debt":
- Projects без strategy.md update > 4 weeks
- Decisions без replay-check > 12 weeks
- Topics без natянувшейся гипотезы > 8 weeks
- Agents без strategies.md update > 6 weeks

Это как "tech debt" но для знаний/решений. Ruslan видит "скопилось".

**Leverage:** ×4.

### 20.7 Meta-natяжки — natяжки на natяжки

Once a month: агент читает все weekly natянутые reports за месяц, ищет
meta-patterns. "Заметил: каждую неделю между projects A и C появляется
suggestion cross-link Y. Это стабильный сигнал, пора сделать explicit".

**Leverage:** ×4. Captures emergent patterns.

### 20.8 Ambient briefings — audio digest

Weekly reflection → text-to-speech → MP3 в `reports/audio/`. Ruslan
слушает в дороге / зале. 5-минутный digest.

**Leverage:** ×3. Ruslan уже любит голосовой формат (voice-memos pipeline).

**Cost:** TTS API + script (~30 строк).

### 20.9 Decision impact-tracking

Каждое decision → добавляет tag, после которого system **самостоятельно**
ищет "impacted files/projects" еженедельно. Через месяц: "ты решил X
2 недели назад; с тех пор Y задач в проекте A следовали этому, Z задач
нарушили. Пересмотреть?"

**Leverage:** ×5.

### 20.10 "Decision-free" weeks tracking

Неделя без новых decisions — подозрительно (либо стагнация, либо
non-recorded). Alert в weekly reflection.

**Leverage:** ×2.

### 20.11 Minimum viable agent — template

При создании нового агента — template который за 10 мин даёт production-ready:
- system.md с boilerplate
- strategies.md empty
- niche/ symlinks
- mailbox initial
- Agent Card

Template is script `./jetix new agent <name>`.

**Leverage:** ×4 когда появятся партнёры (каждый будет добавлять своих agents).

### 20.12 Conversation memory — first-class

Разговоры с центральным Claude сейчас **не сохраняются** (ephemeral).
Опция: "Promote this conversation" → один command сохраняет chunk в
`wiki/conversations/{date}-{slug}.md` + links на обсуждаемые темы.

Через 2 месяца Ruslan имеет 20-50 сохранённых глубоких разговоров =
phenomenal training data для strategies + context.

**Leverage:** ×6.

**Cost:** 1 skill `/save-chat`.

---

## Ranked list — Top 15 leverage improvements

Ranking — по `leverage / cost`, с учётом **включаем ли в v1-beta-tech**
vs отдельный track.

| Rank | Name | Leverage | Cost | §SDH | Track |
|------|------|----------|------|------|-------|
| 1 | Decision→Strategy auto-propagation | ×10 | 1 skill | §4.2.4 | **SDT core** |
| 2 | Declarative constitution (invariants) | ×10 | 1 секция | — | **SDT core** |
| 3 | Agents read SDT as context | ×10 | 1 line × 12 | §3.2 | **SDT core** |
| 4 | LLM abstraction layer | ×8 | 100 строк | §3.5.2 | **SDT core** |
| 5 | Temporal edges + confidence (Zep) | ×5-8 | 2 fields | §4.4 | **SDT core** |
| 6 | HippoRAG (PPR) over wiki-graph | ×5-8 | 50 строк Python | §4.5 | **SDT core** |
| 7 | `./jetix` unified CLI | ×5 | 150 строк | §5.5 | **SDT core** |
| 8 | DuckDB over frontmatter | ×8 | 50 строк | §4.1 | **SDT core** |
| 9 | Timeboxing as first-class | ×7 | convention | §6.1.1 | **SDT core** |
| 10 | Natяжки-as-primitive `/cross` | ×7 | 1 skill | §4.5.2 | **SDT core** |
| 11 | Reverse index questions→answers | ×6 | 1 hook | §4.4 | **SDT core** |
| 12 | Event log unified | ×6 | 1 jsonl + hooks | §4.0 | **SDT core** |
| 13 | Reflection-agent weekly | ×6 | 1 agent | §6.1.11 | **SDT core** |
| 14 | Conversation memory `/save-chat` | ×6 | 1 skill | §3.2.1 | **SDT v1.1** |
| 15 | Fractal strategy w/ transclude | ×5 | convention | §6.1.8 | **SDT v1.1** |

**Not in top 15 but still good:**
- Agent Cards lightweight (×4) — **obligatory**, Appendix
- Mental-models.md (×4) — **obligatory**, в корне репо
- In-system metrics dashboard (×4) — **obligatory**, METRICS.md
- Migration pattern institutionalized (×7) — **obligatory for future migrations**
- Public story wiki split (×3-5) — **отдельный track** (post-v1-beta)

---

## What SHOULD go into SYSTEM-DESIGN-TECH.md

**Обязательные секции SDT (производные из моего review):**

### Секция 1: Invariants (Declarative Constitution)
- 10-20 жёстких "what must always be true" утверждений
- `/lint` validates
- Агенты читают при старте

### Секция 2: Context Engineering Matrix
- Write / Select / Compress / Isolate — конкретные механизмы
- Таблица "какой type info в какой path"

### Секция 3: Five-way query surface + DuckDB
- Каноническое описание как query text-as-database
- DuckDB примеры

### Секция 4: Graph operations (PPR, communities, temporal edges)
- Формальное описание edge schema (with confidence, valid_from/until)
- PPR algorithm + cache pattern
- Hierarchical community summaries

### Секция 5: Event log contract
- `shared/events.jsonl` schema
- Event types list
- Replay protocol

### Секция 6: LLM abstraction layer
- `tools/llm.py` interface
- Provider fallback logic
- Kay principle compliance

### Секция 7: Agent protocols (link → AGENT-PROTOCOLS.md)
- Agent cards (12 × 10 lines)
- Load-context protocol
- Decision-propagation protocol
- Safe-save protocol (already in §5.6.1)

### Секция 8: Metrics contract
- METRICS.md schema
- Update triggers
- Delta reports

### Секция 9: Operational CLI `./jetix`
- Subcommands list
- Skill routing

### Секция 10: Migration pattern
- Reusable 5-phase template (scan → classify → ingest parallel → manual → report)

---

## What can be separate tracks / skills (NOT blocking v1-beta)

**Track A: Public Story Wiki**
- mkdocs + GitHub Pages
- visibility tags
- Marketing benefit, not v1-beta-tech.

**Track B: Portable Export/Import**
- tar.gz + install.sh
- Disaster recovery, ценность через 1-2 мес когда партнёры придут.

**Track C: Dashboard (Streamlit)**
- Plots over METRICS.md
- Nice-to-have, не блокер.

**Track D: Audio digests (TTS)**
- ambient briefings
- Comfort feature.

**Track E: mental-models.md standalone**
- Lives в корне, не SYSTEM-DESIGN-TECH.md, но ссылается.

**Track F: Agent Cards full (Google Model Card style)**
- Пока lite-версия в SDT.
- Full в v1-final.

**Track G: Templates as Jinja**
- nice upgrade но не core.

**Track H: Dual-Claude auto-review for small events**
- 5-chat methodology уже работает для больших → институционализировать
  для малых можно позже.

---

## What we already have that's strong — DON'T fix

Отмечаю сильные стороны v1-beta, которые Критик (Чат 1) может предложить
переделать. **Мой голос: не трогайте.**

### 1. Docs-as-code в git — святое

Не менять. Это Linux-level infrastructure. Попытка "добавить БД поверх" — убьёт
lever.

### 2. Semi-manual mode (§5.0) — правильное решение для v1-beta

Не автоматизируйте. Не добавляйте cron'ы. Ruslan должен сам видеть что
работает — это обучающий период. Через 1-2 мес сам скажет "теперь cron'ы".

### 3. 12 agents roster — не упрощать до 5

Критик может предложить "5 агентов достаточно". Не согласен. 12 — правильная
декомпозиция доменов. Если какой-то декоративен — **наполнить работой**, не
удалять (Manifest point 1: "Не упрощаем").

### 4. 7-parts structure SDH — keep

7 частей + мета — хорошая декомпозиция. Не превращать в 15 частей ради
детализации. Детализация — в SDT (следующий doc) и supplementary files.

### 5. Russian-first for content, English for code

Язык documentation на русском — правильно. Keep.

### 6. Notion decommission — правильная стратегия

Не откатывать. Критик может сказать "Notion удобен для клиентов". **Client-facing
layer — отдельный track (v1-final).** Основная operational работа — только git.

### 7. Attribution через цитаты Ruslan

SDH имеет 15+ прямых цитат. Это **золото** — пронесёт документ через года.
Keep doing this.

### 8. wiki с 9 entity types + 9 edge types — правильная онтология

Не упрощать до 3-5. Karpathy wiki works with this granularity. Если какие-то
типы пустуют — наполнить при ingest, не удалять.

### 9. 5-layer memory per agent

Core/Strategies/Working/Archival(niche)/Recall(mailbox) — это **уже** Letta-
inspired best-practice. Keep.

### 10. GitHub-style work (main vs drafts) — методологический алмаз

Keep and **amplify**. Эта метафора — одна из ключевых leverage-точек.

---

## Appendix A. Cross-reference map — где что в SDH

| Категория моего review | §SDH baseline | Идеи добавки (rank) |
|-----------------------|---------------|---------------------|
| Композиция | §4.5, §6.1 | 1, 4, 10 |
| Text-as-database | §4.1, §4.3 | 8, 11 |
| Self-improvement | §6.1.13 | 1, 2 |
| Context engineering | §3.2, §4.3 | 7 (CLI context command) |
| HippoRAG/GraphRAG | §4.4, §4.5 | 5, 6 |
| Declarative | §4 (implicit) | 2, 3 |
| Event sourcing | §4.0 (implicit) | 12 |
| Fractal strategy | §6.1.8 | 15 |
| Agent Cards | §3.2.3 | Appendix A |
| Knowledge active | §4.4, §4.5 | 11 |
| Mental models | §1.5, §3.1.5, §6.2.4 | mental-models.md standalone |
| In-system metrics | §2.3 | 8 (DuckDB), METRICS.md |
| Ritual scripts | §5.5 | 7 (`./jetix`) |
| Kay vendor diversity | §3.5.2 | 4 (LLM abstraction) |
| Reflection | §6.1.11 | 13 |
| Portable | — (new) | Track B |
| Public wiki | — (new) | Track A |
| Templates as code | implicit | Track G |
| Migration pattern | §4.6, NOTION-MIGRATION | SDT §10 |

---

## Appendix B. Принципы которые я применял при review

1. **Leverage > feature count.** Одна хорошая добавка > 10 маленьких.
2. **Compose what's there > add new.** Сила — в комбинации существующих
   компонентов. Не добавляй components, если можешь **связать** существующие.
3. **Declarative > imperative.** Правило, записанное в одном месте и
   читаемое всеми, > 12 разбросанных instructions.
4. **Text-as-database не оптимизируют — его раскрывают.** Не "давайте
   добавим БД", а "покажите каким паттерном уже существующий текст
   становится БД".
5. **$50K-relevance.** Каждая добавка проверяется: "приближает к $50K до 30.06?"
   Если нет — отдельный track, не core.
6. **Kay principle throughout.** Инфраструктура, а не инструменты. Vendor
   diversity — фундамент.
7. **Cost должен быть маленький.** Если добавка требует > 200 LOC или > 3 дня
   работы — пересмотреть или разбить на phases.
8. **Attribution preserved.** Любое улучшение показывает из какого места SDH
   оно растёт.

---

## Appendix C. Мой ответ на скрытый вопрос "почему v1-beta уже готов к ×10"

Иногда читаешь архитектуру и думаешь "тут ещё много работы". Про v1-beta SDH
**моё честное мнение — обратное**:

- **Docs-as-code в git** = Linux-kernel-grade foundation (это тысячи
  инженеров-лет уже вложено в инфраструктуру, Ruslan получает бесплатно)
- **text-as-database** + grep/obsidian/claude/python/duckdb = 6 способов query
  **БЕЗ** построения БД
- **wiki graph 572 edges** = ready infrastructure для PPR/GraphRAG
- **5-layer memory** per agent = Letta-grade memory model
- **Semi-manual mode** = безопасный trainер для человека

То есть **foundation — ×10-grade**. А используется сейчас на ×1-2.
Мои 30+ идей — способы **довести use до foundation capability**. Это не
добавление этажей к стройке — это **отделка верхних этажей, которые уже стоят**.

Главный risk не в недостатке foundation — а в том что Ruslan не успеет
**реализовать compounding loops** до 30.06.2026 (дедлайна $50K). Поэтому
мой ТОП-5 leverage-улучшений все **короткие** (skill, convention, hook) —
можно сделать **в одну сессию каждое**, но они дают компаунд через месяцы.

---

## Appendix D. Что я НЕ оптимизировал (осознанно)

- **Бизнес-стратегию** — не моя роль (Strategist agent, Ruslan, ментор Антон)
- **Content strategy** (статьи, видео) — outputs 2.1.3, 2.1.7. Отдельный трек.
- **Client-facing interfaces** — §7.1.4 отложено, согласен.
- **Team/org scaling** — §7.1.5 про клуб, отдельная область.
- **Miro-визуализации** — §7.4.3, после release.
- **User guide для "человека с улицы"** — FOUNDATION-DOCS-RESEARCH §14,
  отдельный проект.
- **Monetization / pricing models** — business layer, не system-design.
- **Finances tracking** — ресурс 3 из §1.2, но инфраструктура для этого
  thin (добавить одну папку `finance/` с конвенцией достаточно, не ×10 leverage).

---

## Appendix E. Cross-check с 7 паттернами FOUNDATION-DOCS-RESEARCH §10

| # | Паттерн из research | Как у v1-beta | Как усиливаем |
|---|---------------------|----------------|---------------|
| 1 | Философия/Why до How | ✅ Часть 1 | keep |
| 2 | Формальные обязательства (MUST) | partial (§5.7 запреты) | invariants section (§6 above) |
| 3 | Явные Non-goals | ✅ §2.4 | keep |
| 4 | Multi-view описание | partial (7 частей) | SDT добавляет Process View + Deployment View |
| 5 | Alternatives considered | weak | SDT, decision template (§18.3 above) |
| 6 | Docs-as-code | ✅ | keep, усилить через Public Story Wiki |
| 7 | Versioning + changelog | ✅ App.2 | keep |

**Итог:** v1-beta покрывает 5/7 хорошо, 2/7 (formal MUST, alternatives) —
мои § выше закрывают их в SDT.

---

## Appendix F. "Один абзац почему эта работа стоит делать"

Jetix OS — это инструмент, которым Ruslan управляет своими ресурсами, чтобы
эффективно достичь $50K до 30.06.2026 и выйти в горизонты 1/5/100 лет.
Инструмент имеет **Linux-grade foundation** (git, markdown, wiki, 12 agents,
Claude Code) — т.е. качественная основа, сравнимая с системами которые
решали compute-задачи последних 50 лет. Но сейчас это foundation работает на
**×1-2 от своего потенциала**, потому что compounding-loops (decision→strategy,
wiki→metrics, natяжки cycles, reflection retros) **не замкнуты**.

Мой review — **чертёж замыкания этих петель**. Каждая петля короткая
(1 skill, 1 convention, 1 agent). Но замкнутая петля даёт compound ×5-×10
через 1-3 месяца. При дедлайне 10 недель — это **единственный способ** получить
от системы measurable вклад в $50K, не дожидаясь v2/v3.

Мой совет Синтезатору (Чат 5): взять ТОП-10 моих улучшений в ядро SDT,
остальные — в отдельные tracks/skills. Сфокусироваться на **композиционных**
улучшениях (те, которые соединяют существующее) — они дешевле и сильнее
добавочных.

---

## Заключительная мысль

Есть два способа делать техническую архитектуру:
1. **Спроектировать идеально с нуля** — долго, дорого, откладывает пользу.
2. **Раскрыть потенциал того что уже работает** — быстро, дёшево, даёт
   немедленный effect.

SYSTEM-DESIGN-HUMAN v1-beta — это уже работающий первый проход (Brooks:
"first version you'll throw away"). Мой review — способ **не выбрасывать
его**, а **раскрыть** на ×5-×10. Подавляющее большинство моих предложений —
конвенции, skills, hooks, не архитектурные переписи.

Синтезатору — пожалуйста, не превращайте review в "давайте спроектируем v2
с нуля". Возьмите из моих 30+ идей те, что **композиционны** с текущим
v1-beta, положите в SDT, и запустите compound loops. Это и есть
**×10-engineering**.

--- END OF REVIEW ---

**Lines:** этот файл содержит ~720 строк markdown.

**Statistics:**
- Categories covered: 20 (prompt) + 12 (mine) = 32
- Total optimizations described: ~80 concrete
- Improvements ranked in top-15: 15
- SDT sections proposed: 10
- Separate tracks: 8
- Preserved (don't fix): 10
- Cross-references to SDH: 60+
