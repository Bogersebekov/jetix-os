---
type: review-package
status: draft
created: 2026-04-18
audience: Ruslan (human review + approval)
sources:
  - SYSTEM-DESIGN-HUMAN.md
  - prompts/tech-doc-{0..5}.md
  - reviews/tech-doc-{1..4}-*-2026-04-18.md
  - design/SYSTEM-DESIGN-TECH.md
  - reports/tech-doc-synthesis-2026-04-18.md
---

# Review-пакет: технический документ Jetix OS v1-beta — 2026-04-18

> Документ подготовлен для **чтения Русланом и утверждения / возврата на доработку**.
> Никакие правки, шаблоны, папки **не создавались** (кроме этого отчёта).
> Ничего из синтеза ещё **не утверждено**.

---

## 1. Что было на входе

### 1.1 SYSTEM-DESIGN-HUMAN §4.1 — якорь «папочная структура» (кратко)

`SYSTEM-DESIGN-HUMAN.md:928` вводит v1-beta-предложение папочной структуры
под принцип §4.0 «код системы жизни должен оставаться ЧИСТЫМ — как на GitHub»
(`SYSTEM-DESIGN-HUMAN.md:915-926`). Цель — у каждого типа информации **заранее
заготовленное место**. В дереве жирным помечено «уже в репо», курсивом — NEW
или TODO-migration (`SYSTEM-DESIGN-HUMAN.md:931-1022`).

Итог §4.1 — 23 верхне-уровневые папки в `jetix-os/`: стратегические доки
(`design/`, `strategy/`), проекты и менеджерские пулы (`projects/`, `decisions/`,
`tasks/`, `ideas-pool/`, `hypotheses/`, `tools-catalog/`), общая KB и
производные (`wiki/`, `reflection/`, `health/`, `crm/`, `daily-log/`),
immutable-хранилище (`raw/`, `inbox/`), оперативная часть (`agents/`, `comms/`,
`shared/`), инструменты и отчётность (`reports/`, `tools/`, `scripts/`,
`docs/adr/`, `prompts/`). Все файлы — с YAML frontmatter, kebab-case,
дата `YYYY-MM-DD`, append-only логи (`SYSTEM-DESIGN-HUMAN.md:1024-1032`).

### 1.2 Файлы промптов `prompts/tech-doc-*.md`

| Файл | Роль в пятичатовой методологии |
|------|--------------------------------|
| `prompts/tech-doc-0-context.md` | Общий контекст для 5 чатов (Ruslan, Jetix OS, must-read, 18 категорий, формат). Читается **первым** всеми. |
| `prompts/tech-doc-1-critic.md` | Чат 1 — **Критик / адвокат дьявола**. 18 категорий слабостей (SPOF, cascades, race, drift, мусор, оркестрация, контекст, human-in-loop, дисциплина, границы, масштаб, decisions, Notion-migration, метрики, культура, тех.долг, обучение агентов, gaps). |
| `prompts/tech-doc-2-optimizer.md` | Чат 2 — **Оптимизатор / visionary**. Leverage, композиции, паттерны arc42/C4/ADR/event-sourcing/CQRS/GraphRAG/HippoRAG; поиск ×10-улучшений. |
| `prompts/tech-doc-3-engineer-a.md` | Чат 3 — **Системный инженер A (arc42 / ISO 42010)**. Rigor-first, 12 секций arc42, явные ADR, ISO 25010 quality attributes. |
| `prompts/tech-doc-4-engineer-b.md` | Чат 4 — **Системный инженер B (C4 + event-sourcing + ADR-first)**. Simplicity > completeness, визуальные диаграммы, 10-20 коротких ADR. |
| `prompts/tech-doc-5-synthesizer.md` | Чат 5 — **Синтезатор / главный инженер**. Запускается **после** 1-4, читает 4 отчёта, решает конфликты, выдаёт финальные документы в `design/`. |

Чаты 1-4 работают **параллельно и независимо**, без переписки
(`prompts/tech-doc-0-context.md:156-168`).

---

## 2. Что сказал каждый из 4 ревьюеров

### 2.1 Чат 1 — Критик (`reviews/tech-doc-1-critic-weaknesses-2026-04-18.md`, 1632 строк)

**Главный тезис.** SYSTEM-DESIGN-HUMAN v1-beta честно обозначает ограничения,
но содержит критичные архитектурные слабости, которые **не адресуются** оговоркой
«это beta»: система физически не выживает без Ruslan'а, «чистота без автоматики»
математически невыполнима, «12 агентов» — абстракция на фикции, метрики измеряют
не то, архитектура hardcoded под одного пользователя при обещании 100+ через год.

**Top-5 критичных находок:**

1. **Ruslan как человеческий SPOF** (§1.1): 24-48ч offline = стагнация; 2 недели = коллапс.
2. **«Чистота без автоматики» — конфликт** (§9.1): 25+ папок × 13 компонентов × ~30 заметок/день при 4-5ч/день и запрете автоматики — невозможно.
3. **«12 агентов» — self-deception** (§6.1): 6 mailbox'ов пусты, 6 только с тестом; реально один Claude в сессии.
4. **Метрики измеряют не то** (§2.3): $50K достижим без Jetix OS или не достижим при отлично работающей системе.
5. **Hardcoded под одного пользователя** (§4.1, §6.1): 25+ папок, 13 компонентов, 3 CRM базы — долг для multi-tenant.

**Ещё 10 конкретных находок:**

6. Central Claude session crash без recovery контекста (§1.2).
7. API 529 / GitHub / VPS без fallback-провайдера (§1.3-1.5).
8. Concurrent writes в `edges.jsonl`, `state/*.json` без lock-mechanism (§3.1, §3.6).
9. Нет deputy / acting-mode на время offline Ruslan'а (§1.1).
10. Approval-поток — 20-30 решений/день невозможен (§8.1-8.7).
11. Отсутствует formal permission model read/write per-agent (§7.2.5).
12. `escalation.jsonl` не формализован (§5.4, inventory gap #11).
13. Security baseline не описан: какие папки НЕ читаются агентами, где API keys, gitignore (строки 1544-1545 review).
14. Численные границы каждого паттерна не заданы: N заметок/день, M tokens/session, K pages в append-only (строки 1566-1589 review).
15. Notion γ/δ без hard-deadlines → migration затянется (§13).

**С кем соглашается / спорит.** Критик работает независимо (не читает других).
Но в финале его наблюдения **пересекаются** с обоими инженерами (оба тоже
предлагают single central Claude → подтверждают тезис #3) и расходятся
с оптимистичной интонацией Оптимизатора (тот говорит «leverage», критик —
«фундамент с трещинами»).

---

### 2.2 Чат 2 — Оптимизатор (`reviews/tech-doc-2-optimizer-improvements-2026-04-18.md`, 1619 строк)

**Главный тезис.** v1-beta — Linux-grade фундамент (git + markdown + wiki + 12 агентов + Claude Code),
работающий на ×1-2 от потенциала; 30+ leverage-улучшений (композиции, паттерны, skills)
замкнут compounding-петли для ×5-×10 роста за 1-3 месяца.

**Top-5 сильнейших leverage:**

1. **Decision → Strategy auto-propagation** (§1.1): решения индексируются в `strategies.md` всех 12 агентов одним skill'ом — ×10, стоимость 1 skill.
2. **Declarative Constitution (invariants §11)** (§6.1): SYSTEM-DESIGN-TECH как «закон», читаемый каждым агентом при старте; меняешь одно место → меняется всё — ×10.
3. **Agents read SDT as context** (§6.3): `§invariants` включается в `system.md` каждого агента — constitution приходит в каждый запуск.
4. **LLM abstraction layer** (§14.1): все calls через `tools/llm.py`; `export JETIX_LLM=openai/gpt-4o` переключает провайдера — ×8, 100 строк.
5. **DuckDB over frontmatter** (§2.2): SQL-запросы к markdown, «что делал на неделе» → SELECT query — ×8, 50 строк.

**Ещё 10 предложений:**

6. Personalized PageRank (HippoRAG lite) на 572 edges — `/ask` качество ×5, 50 строк Python (§5.1).
7. Unified CLI `./jetix` — один entry-point для 10 команд (§13.1).
8. «Натяжки-as-primitive» skill `/cross <what> <onto>` с gradient-boosting cycle (§1.2).
9. Identity-resolution loop daily-log → CRM (§1.3).
10. Weekly reflection-agent с честной критикой в `reflection/insights/` (§1.5).
11. Temporal edges + confidence-scores в `edges.jsonl` (§5.3-5.4).
12. Unified event log `shared/events.jsonl` для cross-component queries (§7.1).
13. Timeboxing first-class: `budget-hours` + `kill-criterion` на проекты (§20.5) — критично для $50K.
14. Fractal strategy с Obsidian-style transclude blocks (§8.1).
15. METRICS.md — 1 строка, 10 счётчиков (стратегии/неделю, натяжки, decisions, wiki-edges) (§12.1).

**С кем соглашается / спорит.** Соглашается с обоими инженерами на Karpathy-wiki
и single Claude (тезисы конструктивны). Прямо **спорит с настроением критика**:
критик говорит «фикция», оптимизатор — «латентная сила». Оба частично правы —
синтезатор (см. §3) берёт и предупреждения критика, и leverage оптимизатора.

---

### 2.3 Чат 3 — Инженер A (arc42) (`reviews/tech-doc-3-engineer-a-architecture-2026-04-18.md`, 2874 строк)

**Главный тезис.** Jetix OS должна быть построена как **docs-as-code персональная ОС**
на принципах arc42 / ISO 42010, с центральным Claude-оркестратором,
markdown+git хранилищем и фазированной миграцией от Notion; приоритеты качества —
Transparency (Q1) > Portability (Q2) > Learnability (Q3) > Modifiability (Q4) > Data-safety (Q5).

**Структура его документа — 12 arc42-секций:**

1. Introduction & Goals (9 FR, 7 quality goals, 13 stakeholders).
2. Architecture Constraints (9 технических + 7 организационных + 4 convention).
3. Context & Scope (3 trust zones).
4. Solution Strategy (Q1-Q5 → механизмы → ADR refs).
5. Building Block View (14 компонентов).
6. Runtime View (7 сценариев: /plan-day, /ingest, /ask, /close-day, weekly, Notion fallback, migration).
7. Deployment View (Windows + VPS Ubuntu + GitHub, 6 DR-сценариев).
8. Crosscutting Concepts (10 тем: security, memory, concurrency, persistence, communication, error, testing, observability, i18n, rate-limits).
9. ADRs (14 принятых + 4 backlog).
10. Quality Requirements (tree + 15 scenarios).
11. Risks & Technical Debt (12 risks + 14 TD-items).
12. Glossary (47 терминов).

**Top-7 ключевых архитектурных решений:**

1. **ADR-001** Docs-as-code (markdown+git) как source of truth.
2. **ADR-002** Single central Claude Code orchestrator — 12 агентов как роли, не процессы.
3. **ADR-006** Karpathy LLM Wiki + OmegaWiki (9+9 типов, 6 niches) вместо vector DB.
4. **ADR-005** Semi-manual v1-beta (no cron, no event-driven).
5. **ADR-010** Phased Notion decommission α/β/γ/δ.
6. **ADR-009** Append-only logs с ротацией >30.
7. **ADR-011** 5-chat review для критических docs.

**ADRs, которые A предложил:** ADR-001..014 accepted, ADR-014 proposed,
ADR-015..018 в backlog (locking, client API, distributed, permission matrix).

**С кем соглашается / спорит.** Соглашается с **Инженером B** на single central
Claude + Karpathy-wiki + Notion-decommission. **Спорит** с B по стилю:
A — rigor, явные trade-offs, полная ISO 25010 ориентация, 12 секций;
B — simplicity, визуализация, минимум формальности. Соглашается с критиком
по Ruslan-SPOF (R-10 в его risks). Соглашается с оптимизатором на `system.md`
каноническом (ADR-013).

---

### 2.4 Чат 4 — Инженер B (C4 + event-sourcing) (`reviews/tech-doc-4-engineer-b-architecture-2026-04-18.md`, 2931 строк)

**Главный тезис.** Jetix OS — ОС на markdown+git с единственным Claude Code в 12 ролях,
работающая через append-only event-логи и ADR-first методологию (вместо arc42);
принцип **«простота > полнота, визуализм > проза, события > снимки состояния»**.

**Структура документа:** C4 Level 1 (System Context — Ruslan + партнёры + external),
Level 2 (8 контейнеров: Brain / Wiki / Operations / Strategy / DayLoop / Archive / Agents / Integration),
Level 3 (компоненты per container). Event model — иерархия логов (git + wiki/log.md +
daily-log/ + decisions/ + mailboxes/ + hypotheses/) с 25 canonical event types
(decision.recorded, ritual.closed, agent.escalated, safe-save.fired, ...).
Всё на mermaid-диаграммах.

**Top-7 ключевых решений:**

1. **ADR-001** Markdown + git как БД (никаких DB / Redis / vector-store на v1).
2. **ADR-002** Central Claude Code с role-switching (не 12 процессов).
3. **ADR-003** Event sourcing через append-only логи (git commits + специализированные streams).
4. **ADR-004** Semi-manual без cron / event-driven в v1-beta.
5. **ADR-007** Notion phased decommission; filesystem — единственный SoT.
6. **ADR-012** Karpathy-wiki (9 entity + 9 edge types, 6 niches) вместо vector RAG.
7. **ADR-010** SAFE-SAVE как universal error handler — append-only commit после каждого блока.

**ADRs, которые B предложил:** 18 inline ADR в §10 (ADR-001..018):
markdown-git, central-claude, event-sourcing, semi-manual, vendor-diversity,
knowledge-compounding, notion-decommission, docs-as-code, multi-chat-review,
safe-save, no-orchestration-framework, Karpathy-wiki, 5-layer-memory, CRM-3-bases,
system-prompt-learning, daily-log-drafts, projects-as-primary, ADR-lightweight-format.

**Принципиальные отличия от A:**

- **Simplicity vs Rigor.** B: 1 строка на агента, 5-10 строк на MCP; A: полная spec.
- **Visual-first vs Prose-heavy.** B: mermaid C4; A: текстовые описания arc42.
- **Events vs State.** B: event-sourcing ментальная модель; A: состояние компонентов.
- **ADR-first vs Explanatory.** B: 18 lightweight ADR (Nygard); A: подробные обоснования в тексте.

**С кем соглашается / спорит.** Соглашается с A по трём фундаментам (markdown-git,
central Claude, Karpathy-wiki, Notion-decommission). **Спорит со стилем A**
(simplicity vs rigor). Соглашается с оптимизатором по event-sourcing (один из
ключевых leverage-паттернов). Частично закрывает опасения критика через
SAFE-SAVE и explicit semi-manual режим.

---

## 3. Что вошло в синтез (`design/SYSTEM-DESIGN-TECH.md`, 2451 строк)

### 3.1 Оглавление

| § | Раздел | Содержание (коротко) |
|---|--------|------------------------|
| §0 | How to read this document | Структура + reading order (`:38-87`) |
| §1 | Introduction & goals | Бизнес-рамка, 7 quality goals, 9 FR, stakeholders (`:89-167`) |
| §2 | Architecture constraints | 9 tech + 7 org + conventions (`:169-261`) |
| §3 | System context (C4 L1) | Периметр, trust zones, autonomy-budget=0 (`:263-344`) |
| §4 | Solution strategy | Strategy table, 12 key decisions, 6-layer decomposition (`:347-408`) |
| §5 | Containers view (C4 L2) | 9 контейнеров репо (`:411-496`) |
| §6 | Components view (C4 L3) | Brain, Wiki, Ops, Integration |
| §7 | Event sourcing model | 30 canonical event types, unified `shared/events.jsonl` |
| §8 | Runtime view | 7 канонических сценариев |
| §9 | Deployment view | Инфраструктура, DR, cloud |
| §10 | Crosscutting concepts | Security, memory (5-layer), concurrency, error, observability, testing |
| §11 | Invariants (constitution) | 34 MUST/SHOULD/MAY |
| §12 | ADRs | 18 unified решений (Nygard format) |
| §13 | Quality requirements | Tree + QS-01..QS-16 |
| §14 | Risks & technical debt | R-01..R-12 + TD-01..TD-14 + matrix |
| §15 | NOT doing | 15 non-goals (NG-01..NG-15) |
| §16 | Operational interface `./jetix` CLI | Unified command routing (~150 LOC, `:2265-2305`) |
| §17 | Glossary | 45+ терминов (`:2330-2388`) |
| §18 | Reading order | Paths для Claude и humans (`:2391+`) |
| §19 | Closing — key invariants summary | |

### 3.2 Ключевые решения (14 штук одной строкой)

1. **ADR-001 (§4.2)** Docs-as-code (markdown + git + append-only + SAFE-SAVE).
2. **ADR-002 (§4.2, `:366`)** Single central Claude Code; 12 агентов = роли, не процессы.
3. **ADR-003 (§4.2, `:374`)** Event sourcing central; 30 event types; unified `shared/events.jsonl`.
4. **ADR-004 (§4.2, `:369`)** Semi-manual v1-beta — zero cron, zero event-driven.
5. **ADR-005 (§4.2, `:375`, `:181`)** LLM abstraction `tools/llm.py` + Kay mode `--no-ai`.
6. **ADR-006 (§4.2, `:368`)** Karpathy Wiki + OmegaWiki (9+9 типов, 6 niches), graph не vector.
7. **ADR-007 (§4.2, `:370`)** Notion decommission α/β/γ/δ с fallback `raw/notion-*`.
8. **ADR-013 (§4.2, `:376`)** Invariants as constitution — 34 declarative правила, каждый агент reads.
9. **ADR-014 (§4.2, `:377`, `:194-204`)** Single-writer concurrency; конфликты → SAFE-SAVE + manual.
10. **ADR-017 (`:2021-2040`)** Writeback + HippoRAG PPR; `/ask` сохраняет comparisons + questions + edges; temporal edges + confidence.
11. **§16 (`:2265-2305`)** `./jetix` unified CLI — 20 subcommands, роутинг в skills + utils.
12. **§11 I-23 (`:117-120`)** Timeboxing mandatory — `budget-hours`, `budget-weeks`, `kill-criterion` (критично для $50K).
13. **§11 I-29 (`:121`, `:262`)** Decision → strategies propagation через `/propagate-decision`.
14. **§14 R-09 / R-12 (`:2198-2201`)** Honestly documented limitations: Ruslan как SPOF (Critical); 2-недельный offline = backlog-risk.

### 3.3 Attribution — что из 4 ревью принято

**Из критика (chat 1):**
- Risk R-01, R-09 (Ruslan SPOF) + honest re-frame «12 agents fiction» → ADR-002 confirmation.
- Metrics misalignment → METRICS.md принят.
- Context pollution concern → HippoRAG PPR.
- 7 race-condition сценариев → ADR-014 single-writer + SAFE-SAVE.
- Semi-manual ↔ automation конфликт признан; `/lint` даёт visibility.

**Из оптимизатора (chat 2):**
- Decision → strategy propagation (×10) — invariant I-29.
- Declarative constitution §11 (×10).
- LLM abstraction `tools/llm.py` (×8).
- HippoRAG PPR (×5-8).
- `./jetix` unified CLI (×5) — §16 целиком.
- DuckDB over frontmatter `tools/query.py` (×8).
- Temporal edges + confidence (×5).

**Из инженера A (arc42):**
- Threat model table → §8.1.
- Extensive glossary → §17.
- «What NOT doing» расширен до 15 non-goals (§15).
- Detailed deployment §7 → §9.
- `system.md` canonical (ADR-013).
- Tier 0+1 testing (`/lint` Tier 1).

**Из инженера B (C4 + events):**
- C4 L1/L2/L3 backbone (§3-6) как навигационная структура.
- Event sourcing central (30 types, §7) — ADR-003.
- 18 ADR (Nygard) — unified format.
- Минимальный quality-attrs → 7 quality goals.
- Permission model через role boundaries.

### 3.4 Что отвергнуто (и почему)

1. **12 separate agent processes** (critic «fiction») — вместо single central + role composition (ADR-002).
2. **Full ISO 25010 mapping** (A) — beta-first; 7 quality goals (NG-12, `:2258`).
3. **Vector RAG / embeddings** — Karpathy + HippoRAG лучше для Learnability (NG-02).
4. **Google Model Cards per agent** (A) — lite 10-line cards (NG-13).
5. **Formal permission matrix v1-beta** — prompt-level + tool allowlist; ADR-019 backlog.
6. **Cron / event-driven automation v1-beta** — semi-manual (ADR-004, NG-03).
7. **Multi-tenant v1-beta** — single-user; v2 separate arch (NG-04).

### 3.5 Противоречия между ревьюерами — как разрешены

| Противоречие | Разрешение в синтезе |
|--------------|----------------------|
| arc42 (A, 12 секций + ISO 25010) vs C4 (B, L1/L2/L3 + events) | **Hybrid**: C4 backbone + arc42 quality/crosscutting/risks sections (§0.1 таблица) |
| 12 processes (critic) vs single Claude + roles (оба инженера) | Single Claude central — ADR-002 |
| Event sourcing: not central (A) vs central (B) | **Принят B** — ADR-003, 30 types, unified `shared/events.jsonl` |
| Quality: ×4 observability (A) vs 4 minimal (B) vs metrics out-of-system (critic) | 7 key quality goals (консенсус) |
| ADR count: 14+4 (A) vs 18 (B) | 18 unified |
| Escalation: one-level (A) vs direct-to-Ruslan (B) | One-level v1-beta; hub-and-spoke v1-final (TD-06) |
| Glossary: extensive (A) vs minimal (B) | Extensive из A + B-entries merged (§17) |
| Permission model: formal (A future) vs role boundaries (B) | Prompt-level + tool allowlist v1-beta; ADR-019 formal v1-final |

### 3.6 Open questions (осталось нерешённым в финале)

Из synthesis-report §R.11.3 (требуется context-specific knowledge Ruslan'а):

1. **Gantt-даты в ARCHITECTURE-TARGET §T.3** — оптимистичны или реалистичны? (зависит от capacity).
2. **v1-final → v2 timing** — зависит от Jetix Club launch.
3. **Agent roster extensions** (`legal-advisor` и т.д.) — business-driven, Ruslan решает.
4. **Monthly Anthropic budget** — какой tier реально у Ruslan'а?
5. **Partners joining beta** — когда (недели) и сколько (5-10?).

**Из technical debt (§14.2) не fully resolved:**

- **TD-01** (`:2207`) `baseline.md` vs `system.md` duplicate — resolve в phase β.
- **TD-03** (`:2209`) orphan-папки `agents/content-team/` и т.д. — investigate week 1.
- **TD-06** (`:2212`) inbox-processor flat routing (не hub-and-spoke) — document v1-beta, enforce v1-final.
- **TD-09** (`:2215`) `/lint` 7 checks — реализованы ли? (audit needed).

**Validation needed (§R.11.4 — lower confidence):**

- HippoRAG quality improvement — документировано; нужна метрика.
- Decision propagation adoption — зависит от дисциплины Ruslan'а.
- Meta-agent cycle operationalization — зависит от weekly-trigger дисциплины.

---

## 4. Текущая реальность репозитория

### 4.1 `ls` по корню `jetix-os/`

```
agents/           ARCHITECTURE-CURRENT.md   ARCHITECTURE.md   automations/
chat-journal/     CLAUDE.md                 command-center/   comms/
config/           crm/                      daily-log/        dashboard/
design/           HOME.md                   ideas/            inbox/
knowledge-base/   logs/                     _meta/            MIGRATION.md
private/          projects/                 prompts/          raw/
README.md         reports/                  reviews/          scripts/
shared/           SYSTEM-DESIGN-HUMAN.md    templates/        test-sync.md
tools/            wiki/
```

### 4.2 Соответствие §4.1 SYSTEM-DESIGN-HUMAN

**УЖЕ существуют (помечены жирным в §4.1):**

- `design/` ✅ (+ уже наполнена: AGENT-PROTOCOLS, ARCHITECTURE-TARGET, DATA-FLOWS, FOUNDATION-DOCS-RESEARCH, NOTION-MIGRATION-PLAN, SYSTEM-DESIGN-INPUTS, SYSTEM-DESIGN-TECH)
- `projects/` ✅ (подпапки: `01-research`, `02-business`, `03-community`, `04-ai-tools`, `05-life-os`, ...)
- `wiki/` ✅
- `crm/` ✅
- `daily-log/` ✅
- `raw/` ✅
- `inbox/` ✅
- `agents/` ✅
- `comms/` ✅
- `shared/` ✅
- `reports/` ✅
- `tools/` ✅
- `scripts/` ✅
- `prompts/` ✅

**Ещё НЕ существуют (помечены NEW / UPDATE / TODO в §4.1):**

| Папка | Статус в §4.1 | Статус в репо |
|-------|---------------|----------------|
| `strategy/` | NEW (life/, projects/{slug}/) | ❌ MISSING |
| `decisions/` | NEW (life-decisions-log, 2026-MM) | ❌ MISSING |
| `tasks/` | NEW (master.md) | ❌ MISSING |
| `ideas-pool/` | UPDATE (inbox.md) | ❌ MISSING (есть `ideas/` — имя отличается) |
| `hypotheses/` | NEW (active, backlog, validated-archive) | ❌ MISSING |
| `tools-catalog/` | NEW ({tool-slug}.md) | ❌ MISSING |
| `reflection/` | NEW (log.md, insights/) | ❌ MISSING |
| `health/` | NEW (habits, log, wiki/) | ❌ MISSING |
| `daily-log/drafts/` | NEW подпапка | ❌ MISSING (сам `daily-log/` есть, `drafts/` нет) |
| `docs/adr/` | FUTURE | ❌ MISSING |

**NEW-подпапки внутри существующих папок проектов** (в §4.1 `projects/{slug}/`
обещаны `hypotheses.md`, `decisions.md`, `open-questions.md`) — **отсутствуют
в `projects/01-research/..05-life-os/`** (проверялось листингом; список содержимого
подпапок не выводил эти файлы в стандартной структуре; точечной валидации по
каждому проекту **не проводилось**).

### 4.3 Расхождения между синтезом (SYSTEM-DESIGN-TECH) и реальной структурой

1. **`SYSTEM-DESIGN-HUMAN.md` лежит в корне**, а §4.1 указывает его как
   `design/SYSTEM-DESIGN-HUMAN.md` (`SYSTEM-DESIGN-HUMAN.md:938`). Синтез
   TECH ссылается на HUMAN как on-repo-file, но путь в §4.1 ≠ фактический.
2. **В корне есть `reviews/`** (создано для методологии 5 чатов) — **не упомянуто**
   в §4.1 HUMAN и не упомянуто явно в §5 синтеза как контейнер. Однако
   `prompts/` как контейнер для 5-chat-методологии **упомянут** в §4.1.
3. **Orphan-папки в корне**, не покрытые §4.1 HUMAN и не адресованные в §5 синтеза:
   `automations/`, `chat-journal/`, `command-center/`, `config/`, `dashboard/`,
   `ideas/` (вместо `ideas-pool/`), `knowledge-base/` (в миграции, см. MIGRATION.md),
   `logs/`, `_meta/`, `private/`, `templates/`. Часть из них — legacy до Phase α
   Notion-миграции; часть (`_meta/`, `private/`, `templates/`) — возможно
   служебные и должны остаться. Синтез TD-03 (`:2209`) упоминает «investigate
   orphan-папки `agents/content-team/` etc.» — т.е. проблема признана, но
   конкретный список orphan-корневых папок **в синтезе не зафиксирован**.
4. **`SYSTEM-DESIGN-TECH.md` сам лежит в `design/`** — это согласуется с §0.1
   и с §4.1 HUMAN.
5. **`reports/tech-doc-synthesis-2026-04-18.md` существует** — соответствует
   обещанию в `prompts/tech-doc-5-synthesizer.md:11`.

### 4.4 Summary gap'ов

- **9 папок** обещаны в §4.1, но физически отсутствуют (`strategy/`, `decisions/`,
  `tasks/`, `ideas-pool/`, `hypotheses/`, `tools-catalog/`, `reflection/`,
  `health/`, `docs/adr/`) + `daily-log/drafts/`.
- **1 папка имеет расхождение в имени** (`ideas/` vs обещанный `ideas-pool/`).
- **~11 orphan-папок** в корне, не покрытых §4.1 HUMAN (частично — legacy).
- **Синтез TECH (§4) предполагает 6-layer decomposition** — это проверяемо
  только после реального создания недостающих папок и перенаполнения orphan'ов.

---

## Приложение. Какие файлы прочитаны для этого отчёта

- `SYSTEM-DESIGN-HUMAN.md` §4.1 (`:913-1140`) — dir-структура.
- `prompts/tech-doc-0-context.md` (215 строк, полностью).
- `prompts/tech-doc-1..5.md` — по первым 60 строкам каждого (роли + мандаты).
- `reviews/tech-doc-1-critic-weaknesses-2026-04-18.md` — через Explore-агент.
- `reviews/tech-doc-2-optimizer-improvements-2026-04-18.md` — через Explore.
- `reviews/tech-doc-3-engineer-a-architecture-2026-04-18.md` — через Explore.
- `reviews/tech-doc-4-engineer-b-architecture-2026-04-18.md` — через Explore.
- `design/SYSTEM-DESIGN-TECH.md` — оглавление через Grep + Explore-саммари.
- `reports/tech-doc-synthesis-2026-04-18.md` — через Explore-саммари.
- `ls` по `/home/ruslan/jetix-os/` + точечные проверки NEW-папок.

**Не предлагал правок, не создавал шаблоны/папки/файлы кроме этого отчёта.**
