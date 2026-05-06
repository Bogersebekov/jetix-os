---
type: design-summary
status: v1-beta-FINAL
approval-status: approved-by-ruslan-2026-04-18
version: v1-beta-FINAL-2026-04-18
owner: ruslan
created: 2026-04-18
finalized: 2026-04-18
reading-time: 15 минут
summary-of:
  - design/SYSTEM-DESIGN-TECH.md (2451 строк)
  - design/AGENT-PROTOCOLS.md
  - design/DATA-FLOWS.md
  - design/ARCHITECTURE-TARGET.md
related:
  - SYSTEM-DESIGN-HUMAN.md (стратегический якорь)
  - reports/tech-doc-synthesis-2026-04-18.md
  - design/IMPLEMENTATION-PLAN-2026-04-18.md
audience: ruslan (primary), future-claude (secondary)
status: archived
archived_at: 2026-05-06
archived_reason: v1-beta design (April 2026) — superseded by Foundation v1.0 + Документ 1A/1B
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# SYSTEM-DESIGN-TECH-SUMMARY — Jetix OS v1-beta в 15 минут

> Сжатая читалка полного технического документа. Цель — понять всю систему
> за один присест и решить: утверждаем и идём в Шаги 3-6, или что-то меняем.
> Для глубины — §8 Reading path в конце.

---

## 1. Что такое Jetix OS — для стороннего читателя

**Jetix OS** — это не приложение и не сервис. Это **операционная система над
личным git-репозиторием**, в которой живут твои знания, решения, проекты и
агенты. Всё, что система «знает» — markdown-файлы с YAML-шапкой. Всё, что
происходит — коммит в git. Ничего не теряется, всё версионируется, к любой
точке прошлого можно вернуться как через машину времени (`git checkout`).

Один центральный Claude Code (1M context, Opus 4.7) работает как «мозг»
системы и **входит в 12 ролей** через смену system prompt + срез памяти.
Это не 12 параллельных процессов, не LangChain и не CrewAI — это одна сессия,
которая честно переключает персоны по команде. Задачи делают «агенты»
(personal-assistant, sales-lead, knowledge-synth, strategist и т.д.), но
физически это один Claude с разными масками и фильтрами знаний.

Автономии нет: в v1-beta autonomy budget = 0. Никаких cron'ов, webhooks,
фоновых действий. Всё запускается командой Ruslan'а (`/plan-day`, `/ingest`,
`/ask`, `/close-day`). Философия (Алан Кей): **методология важнее инструмента**
— если Anthropic, Groq и Notion все падают завтра, Ruslan садится за laptop,
правит markdown руками и коммитит. Система работает деградированно, но не
умирает. Главная бизнес-цель — $50K выручки до 30.06.2026; техдоку нужен
ровно для того, чтобы эту цель разблокировать, не больше.

---

## 2. Ключевые принципы (7 штук, по одной строке)

1. **Docs-as-code.** Markdown + YAML + git — наша БД. Никакого SQL, Notion или vector store. → ADR-001
2. **Один Claude, 12 ролей.** Orchestration = переключение system prompt, а не distributed framework. → ADR-002, ADR-015
3. **Event sourcing.** Всё append-only: `git log`, `shared/events.jsonl`, `wiki/log.md`, `decisions/`, `mailboxes/`. Удалений нет — только «supersedes». → ADR-003
4. **Semi-manual, autonomy = 0.** Zero cron, zero webhooks в v1-beta. Всё по команде. → ADR-004
5. **Kay-принцип.** Работаем без AI: `tools/llm.py` абстракция + Kay mode `./jetix --no-ai` + методология на бумаге. → ADR-005
6. **Karpathy wiki, не vector RAG.** 9 типов сущностей × 9 типов рёбер × 6 ниш + HippoRAG PPR для `/ask`. → ADR-006
7. **Конституция §11.** 34 инварианта (MUST/SHOULD/MAY), агенты читают их как часть system prompt, `/lint` валидирует. → ADR-013

---

## 3. Топ-10 архитектурных решений

### ADR-001. Markdown + git = база данных
**Решение.** Все знания, решения, события — в git-tracked markdown + JSONL внутри репо.
**Почему.** Вендор-независимость, diff'абельность, бесплатная история, Obsidian-совместимость. Полноценная БД требует сложности, которая не окупится при <5000 страниц (сейчас 557).
**Пришло.** Уже было в CLAUDE.md + ARCHITECTURE-CURRENT, подтверждено всеми 4 чатами. → ADR-001

### ADR-002. Один центральный Claude Code = 12 ролей, а не 12 процессов
**Решение.** Single Claude session + composition через system prompt + niche slice + 5-layer memory. Subagent через Task tool — только для тяжёлой параллели (sweep, Notion batch).
**Почему.** Единый контекст Ruslan'а, нет distributed overhead, cost-optimal. Оба инженера (Chat 3 и Chat 4) сошлись независимо. Критик (Chat 1) называл «12 агентов» фикцией — это решение честно переосмысливает.
**Пришло.** Chat 2 leverage + Chat 3 arc42 + Chat 4 C4. → ADR-002

### ADR-003. Event sourcing через append-only логи
**Решение.** `git log` — фундаментальный поток. `shared/events.jsonl` — unified canonical stream. 30 канонических event types (`idea.ingested`, `decision.recorded`, `ritual.morning.closed`, ...). Domain-specific логи (wiki/log.md, daily-log/, decisions/, mailboxes/) — views.
**Почему.** Replay-ability бесплатно (любой derived state пересчитывается). Temporal queries через `git checkout`. Audit trail навсегда. Append-only потоки мёрджатся чисто почти всегда.
**Пришло.** Chat 4 (C4+events) advocated; Chat 2 optimizer leverage «unified events.jsonl». → ADR-003

### ADR-004. Semi-manual, autonomy budget = 0 в v1-beta
**Решение.** Нет cron'ов, webhooks, event-driven реакций. Все ритуалы и maintenance (`/lint`, `/consolidate`, `/build-graph`) — только по команде.
**Почему.** Предсказуемость > скорости. Ruslan видит каждый шаг и учится системе. Rogue-agent риск = 0. Selective automation — потенциально в v1-final, после 1-2 мес обкатки.
**Пришло.** Ruslan прямо заявил в HUMAN §5.0, синтезатор заenforce'ил против optimizer'ских предложений авто-тригеров. → ADR-004

### ADR-005. LLM abstraction + Kay mode
**Решение.** `tools/llm.py` (~100 LOC) — тонкий wrapper. Swap через env: `JETIX_LLM=anthropic/claude-opus-4-7 | openai/gpt-4o | local/llama`. `./jetix --no-ai` запускает нон-LLM навыки (lint, metrics, consolidate, DuckDB query).
**Почему.** Критик указал: HUMAN заявляет «работает без AI», но архитектурно не поддержано. ADR закрывает SPOF Anthropic, операционализует Kay. v1-beta: anthropic/ реализован, остальные — stub-заглушки с TODO.
**Пришло.** Chat 1 critic weakness #3 + Chat 2 optimizer §14. → ADR-005

### ADR-006. Karpathy LLM Wiki + OmegaWiki, а не vector RAG
**Решение.** 9 entity types (concepts, entities, sources, topics, ideas, experiments, claims, summaries, foundations) × 9 edge types × 6 niches. Retrieval через HippoRAG Personalized PageRank на графе, не через embeddings.
**Почему.** Рёбра explicit, debuggable, human-readable. Нет vector DB, нет embedding compute. Obsidian wikilinks совместимы. Scale до ~5000 страниц (сейчас 557) — потолок достаточный.
**Пришло.** Основано на Karpathy принципах + OmegaWiki + оба инженера подтвердили + Chat 2 добавил HippoRAG leverage ×5-8. → ADR-006, ADR-017

### ADR-013. Инварианты как декларативная конституция
**Решение.** §11 SYSTEM-DESIGN-TECH содержит 34 инварианта (MUST/SHOULD/MAY, RFC 2119). Каждый агент в своём system.md начинается с: «Прочитай §11 инвариантов. Ты обязан их соблюдать». `/lint` валидирует.
**Почему.** Меняешь один инвариант — поведение всех 12 агентов меняется синхронно, без правки 12 scattered system prompts. Leverage ×10 (Chat 2).
**Пришло.** Chat 2 optimizer §6 + контрмера Chat 1 критики «12 агентов — фикция». → ADR-013

### ADR-014. Single-writer concurrency
**Решение.** v1-beta — одна Claude сессия пишет одновременно. Git conflict → SAFE-SAVE + Ruslan руками разрешает. Никакой auto-merge, никакого MVCC, никаких `.lock` файлов.
**Почему.** Single-user assumption истинна для v1-beta; git merge разрешает append-only конфликты >90% случаев автоматически. Formal locking — для v2, если multi-user вырастет.
**Пришло.** Chat 1 критик race conditions (7 сценариев) + Chat 3/4 оба согласны на single-writer. → ADR-014

### ADR-017. Writeback-driven knowledge compounding
**Решение.** `/ask` синтезирует → пишет `wiki/comparisons/{date}-{slug}.md` + `wiki/questions/{date}-{slug}.md` + новые рёбра в `edges.jsonl`. Повторный вопрос находит prior answer + diff.
**Почему.** Без writeback wiki замораживается, каждый `/ask` считает с нуля. С writeback knowledge compounds: больше вопросов → плотнее граф → качественнее ответы.
**Пришло.** Chat 2 optimizer §5 + §20.1 (reverse index) + Chat 4 engineer B поддержал. → ADR-017

### Инвариант I-23 + ADR-001. Timeboxing обязателен на проектах
**Решение.** Каждый `projects/{slug}/overview.md` ДОЛЖЕН иметь во frontmatter: `budget-hours`, `budget-weeks`, `kill-criterion: "if <X> by <date> then pivot/kill"`, `next_action`.
**Почему.** Защита от zombie-проектов. При $50K-дедлайне через 10 недель любой проект, который дрейфует без метрик, = потеря времени. Эта мера business-critical, не просто гигиена.
**Пришло.** Chat 2 optimizer §20.5, встроено в §11.8 как MUST. → I-23

---

## 4. Как работает система — 5 ключевых сценариев

### S1. Утро (`/plan-day` или `./jetix morning`)
1. `git pull origin main` — свежий state.
2. Central Claude читает `daily-log/YYYY-MM-DD.md`, `shared/state/focus.json`, `priorities.json`, unread в `comms/mailboxes/human.jsonl`.
3. Чекает `system-health.json` на alert'ы (notion_mcp unstable и т.д.).
4. Генерирует план дня: 1-3 focus block + ritual checklist + текущие `next_action` из active projects.
5. Пишет plan-секцию в `daily-log/` + событие `ritual.morning.closed` в `shared/events.jsonl` → `git commit + push`.

### S2. Ingest источника (`/ingest <path-or-url>` → L0→L1)
1. Source читается из `raw/` / URL / voice transcript.
2. LLM извлекает entities (claim, concept, idea, experiment) + connections.
3. Создаются wiki-страницы с `sources:` frontmatter + append `wiki/log.md` + append `edges.jsonl` (с `origin: /ingest`, `confidence`, `valid_from`).
4. `/lint` проверяет orphans и contradictions; если unclear — SAFE-SAVE + эскалация.
5. Git commit `[wiki] add: <topic> from <source>` + push.

### S3. Вопрос (`/ask "<вопрос>"` → HippoRAG + writeback)
1. Keyword match → seed nodes в графе.
2. Personalized PageRank бегает по `edges.jsonl` → top-20 страниц.
3. LLM синтезирует ответ с цитатами `[[file-ref]]`.
4. Опционально: writeback в `wiki/comparisons/{date}-{slug}.md` + `wiki/questions/{date}-{slug}.md` (question + top-5 cited + summary + `times-asked`) + новые `supports/extends/contradicts` рёбра.
5. `question.asked` event + commit + push. Повторный похожий вопрос инкрементит `times-asked` и показывает diff с прошлым ответом.

### S4. Вечер (`/close-day` → writeback drafts)
1. Ruslan запускает, Central Claude показывает дневные drafts в `daily-log/drafts/`.
2. Для каждого draft решает: в wiki/ (концепт/claim/источник) или в CRM (контакт) или в tasks/ или в projects/{x}/ или archive. Routing — через decision tree (см. DATA-FLOWS §F.5).
3. Drafts distilled → целевые места; `daily-log/YYYY-MM-DD.md` закрывается reflection-абзацем.
4. `ritual.evening.closed` event + `git commit [daily] close: YYYY-MM-DD` + push. Non-negotiable.

### S5. Weekly (`/review week` + `/cross`)
1. Ruslan запускает в субботу/воскресенье.
2. Metrics delta: `reports/metrics-delta-Wnn.md` — что выросло за 7 дней (strategies, edges, decisions).
3. `/lint` — orphans, contradictions, stale claims, missing `next_action`.
4. `/cross` (natyagivanie) — «все гипотезы × один проект» или «все идеи × ICP»; создаёт `reports/cross-{date}.md` + `cross_suggested` рёбра. Compounding.
5. Ruslan просматривает meta-agent proposals (в `plan` mode), approve/reject. Обновляет `strategy/life/2026-Wnn-weekly.md`. `ritual.weekly.completed` event + commit + push.

---

## 5. Защита от рисков — что сказал критик (Chat 1) и как закрыто

**Топ-5 рисков и контрмеры:**

1. **Ruslan — human SPOF (bus factor critical).** Критик: «2 недели оффлайн и система мертва».
   → Явно признано в §14 как R-09/R-12. Kay mode (`--no-ai`) архитектурно поддержан. V1-final: deputy mode + policy-default approvals. В v1-beta — **осознанное known limitation**, не замаскировано.

2. **«12 агентов» — фикция (6/12 mailbox'ов пустые, strategies.md все пустые).** Критик: «self-deception».
   → Честный re-framing через ADR-002: «12 ролей одного Claude, не 12 processes». План первых 2 недель v1-beta: Ruslan запускает каждого агента ≥1 раз на реальной задаче. §11.12 декларирует decision propagation — strategies.md растут органически.

3. **Anthropic SPOF + противоречие «работает без AI».** Критик: «нет fallback implementation».
   → ADR-005 + `tools/llm.py` abstraction + Kay mode `./jetix --no-ai`. Swap провайдера через env var. Human operator fallback документирован. v1-beta: anthropic/ реализован, остальные — stubs с TODO.

4. **7 race conditions на shared файлах.** Критик: «нет lock mechanism».
   → ADR-014 Single-writer assumption + git conflict → SAFE-SAVE (never auto-resolve). Formal locks отложены в v1-final backlog (ADR-020). Принято как conscious design choice для single-user.

5. **Метрики измеряют не то ($50K out-of-system, «не занимаюсь ерундой» subjective).** Критик: «нет in-system health».
   → Adopted METRICS.md с 10 каноническими in-system counter'ами (edges, decisions, unclear, orphans, stale claims, drafts-promoted...). Weekly delta reports + `system-health.json` от `/lint`. 16 QS сценариев (§13) — концретные, измеримые per quality goal.

*Полная матрица — §R.5 в `reports/tech-doc-synthesis-2026-04-18.md` (67 weaknesses в 18 категориях).*

---

## 6. Leverage — 5 улучшений оптимизатора, встроенных в v1-beta

1. **Declarative constitution (§11 invariants).** Leverage ×10. Один source of truth поведения 12 агентов. → ADR-013
2. **Decision → Strategy auto-propagation (`/propagate-decision`).** Leverage ×10. Принятое решение с `relevant-agents: [...]` → добавляется в strategies.md каждого релевантного агента. Strategies.md растут органически без ручной работы. → I-29
3. **DuckDB over frontmatter (`tools/query.py`).** Leverage ×8. `SELECT slug, updated FROM 'wiki/**/*.md' WHERE status='active' AND updated < current_date - 7` — 50 LOC, моментальные queries без внешней БД. → §6.4
4. **HippoRAG PPR retrieval.** Leverage ×5-8. Personalized PageRank на графе вместо keyword-only. Качество ответа `/ask` в 3-5× выше. → ADR-017 + I-27
5. **`./jetix` unified CLI.** Leverage ×5. Один entry point (`./jetix morning | close-day | ingest | ask | lint | metrics | cross | propagate | --no-ai`) вместо 10 разных paths. ~150 LOC argparse. Self-documenting через `--help`. → §16

*Full list из 15 leverage improvements — §R.4 synthesis report.*

---

## 7. Что явно НЕ делаем в v1-beta (границы)

| # | Non-goal | Почему НЕ | Когда пересмотреть |
|---|----------|-----------|---------------------|
| NG-01 | Distributed orchestration (Kafka/Redis/K8s) | ADR-002, ADR-015 — single Claude достаточно | >100 concurrent ролей OR v2 multi-user |
| NG-02 | Vector RAG / embedding search | ADR-006 — Karpathy wiki + PPR лучше для structured knowledge | wiki > 5000 страниц OR external corpus |
| NG-03 | Cron / event-driven автоматизация | ADR-004 — autonomy = 0 в v1-beta | v1-final (после 1-2 мес обкатки, selective) |
| NG-04 | Multi-tenant / multi-user | Single-user v1-beta; Jetix Club — v2 | >5 активных партнёров + нужна изоляция |
| NG-05 | Web UI / custom dashboard | Primary UI — Antigravity + Obsidian + CLI | Post-v1-final, если partners нужен портал |
| NG-06 | Финансовые операции автономно | HUMAN §2.4.3 — принципиальная граница | никогда |
| NG-07 | Публикация контента без Ruslan approval | HUMAN §2.4.2 | v1-final с approved templates |
| NG-08 | Удаление данных | ADR-003 append-only | никогда — архив вместо delete |
| NG-09 | Outbound communication без approval | HUMAN §5.7 | v1-final approved templates |
| NG-10 | WebFetch / WebSearch автономно | HUMAN §5.7 | v1-final active mode — отдельный проект |
| NG-11 | Generic AI chatbot | Jetix OS = OS, не chatbot | никогда (different category) |
| NG-12 | Full ISO 25010 mapping | Beta-first — 7 quality goals достаточно | v1-final / v2 |
| NG-13 | TLA+ / formal methods | Beta-first | v2+ maturity |
| NG-14 | Auto-scaling inference budget | Single-user, фиксированный monthly budget | v2 multi-user |
| NG-15 | Полный Google Model Card per agent | Lite cards (10 lines) в AGENT-PROTOCOLS достаточно | v1-final |

Попытка сделать что-то из этого списка в v1-beta = архитектурная ошибка. ADR-023/ADR-024 backlog фиксирует пересмотр.

---

## 8. Reading path — если хочется глубже

| Тема | Куда идти |
|------|-----------|
| **Бизнес-контекст, цели, границы** | `SYSTEM-DESIGN-HUMAN.md` Часть 1 + Часть 2 (30 мин) |
| **Инварианты системы (конституция)** | `design/SYSTEM-DESIGN-TECH.md` §11 — 34 MUST/SHOULD/MAY + §17 Glossary (15 мин) |
| **Архитектурные решения (ADR)** | `design/SYSTEM-DESIGN-TECH.md` §12 — все 18 ADR в Nygard формате inline (30 мин) |
| **Event sourcing модель** | `design/SYSTEM-DESIGN-TECH.md` §7 — 30 event types + routing diagram + temporal queries (15 мин) |
| **Runtime flows (morning/ingest/ask/evening/weekly/error/migration)** | `design/DATA-FLOWS.md` §F.1-F.7 — sequence diagrams + failure modes (25 мин) |
| **State machines (idea → hypothesis → project, task lifecycle, decision lifecycle)** | `design/DATA-FLOWS.md` §F.9 (15 мин) |
| **Per-agent protocols (12 core + 2 utility)** | `design/AGENT-PROTOCOLS.md` §A.1 общий + §A.2-A.16 карточки (30 мин) |
| **Контраст CURRENT → v1-beta → v1-final → v2 + Gantt** | `design/ARCHITECTURE-TARGET.md` §T.0-T.8 (25 мин) |
| **Синтез-процесс (как собрался документ из 4 чатов)** | `reports/tech-doc-synthesis-2026-04-18.md` §R.1-R.12 (30 мин) |
| **План на Шаги 3-6 (templates / folder migration / voice-notes / стратегический план)** | `design/IMPLEMENTATION-PLAN-2026-04-18.md` (20 мин) |

---

## Краткий итог

- Система — markdown + git + один Claude в 12 ролях. Никакой магии, никаких frameworks.
- Ничего не автономно в v1-beta. Всё по команде.
- Работает без AI (Kay mode); `tools/llm.py` — swap провайдера за 1-2 часа.
- 34 инварианта в §11 — конституция, agents enforce, `/lint` валидирует.
- 18 ADR зафиксированы в §12; 15 leverage improvements встроены; 15 non-goals явно очерчены.
- 10 недель до $50K — архитектура работает ровно на то, чтобы эту цель разблокировать.

**Решение для Ruslan'а.** Approve as-is → запускаем Шаги 3-6 по
`design/IMPLEMENTATION-PLAN-2026-04-18.md`. Частичное approve с правками →
iterate по конкретным §. Major revision → обсуждаем в следующей сессии.

---

*Summary v1-beta-FINAL-2026-04-18. Конденсация 2451 строки TECH + трёх
вспомогательных файлов в 15-минутное чтение. Детали — в указанных reading path.*
