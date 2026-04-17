---
type: review
role: systems-engineer-a
school: arc42
chat: 3
created: 2026-04-18
status: complete
length: ~2500 lines expected
sources:
  - SYSTEM-DESIGN-HUMAN.md (v1-beta-2026-04-18)
  - ARCHITECTURE-CURRENT.md (2026-04-16)
  - CLAUDE.md
  - design/FOUNDATION-DOCS-RESEARCH.md §9 (arc42 / ISO 25010 / ADR)
  - design/NOTION-MIGRATION-PLAN.md
  - .claude/agents/*.md (14 определений)
  - .claude/skills/*.md (11 skills)
  - reports/architecture-inventory-2026-04-16.md
thinking: extended
mode: rigor-first
target-audience:
  - synthesizer (chat 5)
  - Ruslan (owner)
  - future agents (part of system prompt chain)
notes: |
  Это один из 4 параллельных reviews. Инженер A — arc42 / ISO 42010 школа.
  Cross-verified с Инженером B (C4 / event-driven) — синтезатор сравнит.
  rigor > elegance. Trade-offs перечислены явно. 14 ADR. Quality Requirements
  через ISO 25010 scenarios. Beta-first контекст сохранён.
---

# SYSTEM-DESIGN-TECH — Jetix OS (Engineer A, arc42 / ISO 42010)

> **Школа:** arc42 (Starke + Hruschka) + ISO/IEC 42010 (architecture description) + Michael Nygard ADR + ISO/IEC 25010 (quality model).
> **Scope:** технический перевод v1-beta-2026-04-18 SYSTEM-DESIGN-HUMAN на язык архитектуры.
> **Читатели:** серверный Claude Code, будущие агенты Jetix OS, Ruslan (owner), сторонние инженеры при передаче.
> **Принцип:** rigor-first. Каждый компонент — `Purpose / Interfaces / Invariants / Dependencies`. Каждое решение — с `Trade-offs`.

---

## Структура документа

| § | Название | Задача |
|---|----------|--------|
| 1 | Introduction and Goals | Бизнес-рамка + ISO 25010 quality goals + stakeholders |
| 2 | Architecture Constraints | Технические/организационные/конвенциональные ограничения |
| 3 | Context and Scope | Внешние и внутренние границы системы |
| 4 | Solution Strategy | Одна страница — ядро решений |
| 5 | Building Block View | Декомпозиция компонентов на 3 уровнях |
| 6 | Runtime View | 7 сценариев жизненного цикла |
| 7 | Deployment View | Инфраструктура, dependencies, DR |
| 8 | Crosscutting Concepts | 10 сквозных тем |
| 9 | Architecture Decisions | 14 ADR по ключевым развилкам |
| 10 | Quality Requirements | Quality tree + конкретные сценарии |
| 11 | Risks and Technical Debt | Известные риски из inventory + mitigation |
| 12 | Glossary | Единый язык команды |
| A | APPENDIX — AGENT-PROTOCOLS.md (draft) | Per-agent detailed protocols |
| B | APPENDIX — DATA-FLOWS.md (draft) | 5 основных flows с failure modes |
| C | APPENDIX — ARCHITECTURE-TARGET.md (draft) | Timeline миграции α → β → γ → δ |

---

# 1. Introduction and Goals

## 1.1 Requirements Overview

### 1.1.1 Системная миссия (one-liner)

**Jetix OS** — персональная операционная система для управляющего (Ruslan), построенная как **docs-as-code мульти-агентная платформа**, которая трекает и распределяет шесть типов ресурсов (информация, время, финансы, связи, внешние обстоятельства, инструменты) так, чтобы владелец был **usage-ratio-оптимизирован** на стратегически важное и **через делегирование** освобождён от неважного.

### 1.1.2 Функциональные требования (FR)

Из Части 2.1 SYSTEM-DESIGN-HUMAN — девять канонических outputs, переведённые в формальные FR с кодами.

| ID | Требование | Критерий приёмки v1-beta |
|----|------------|---------------------------|
| FR-01 | Возвращать пользователю 1-2 часа/день через автоматизацию рутины | Subjective — Ruslan заполняет reflection что день прошёл без ерунды |
| FR-02 | Освобождать энергию для стратегических задач через делегацию shallow work | Любая ритуальная операция запускается одним slash-command |
| FR-03 | Производить структурированные интеллектуальные артефакты (статьи, claims, summaries) | Артефакт появляется в `wiki/` c frontmatter и edges |
| FR-04 | Компаундировать знание в wiki с writeback (каждый /ask дописывает связи) | Edge-count в `wiki/graph/edges.jsonl` растёт после каждого ценного `/ask` |
| FR-05 | Делать shallow sales research вместо Ruslan'а | `sales-researcher` возвращает структурированный отчёт по ICP |
| FR-06 | Планировать/обрабатывать/структурировать информацию на 95% покрытии топика | `/ask <topic>` возвращает >5 цитат из wiki + новых claim'ов |
| FR-07 | Трекать рынок в real-time (отложено для v1-final) | N/A в v1-beta |
| FR-08 | Преобразовывать информационный шум в гипотезы и CRM-возможности | Каждый импортированный source приводит к ≥1 idea + ≥1 edge |
| FR-09 | Digest + action-items из созвона за <10 мин | Транскрипт → `/ingest` → source.md + tasks |

**Важное:** FR-01, FR-02, FR-07 — качественные метрики. FR-03...FR-09 — проверяемы на уровне файловой системы.

### 1.1.3 Нефункциональные требования (NFR) — карта на ISO 25010

| Категория ISO 25010 | Подкатегория | Приоритет v1-beta | Комментарий |
|---------------------|--------------|-------------------|-------------|
| Functional Suitability | Completeness | **MUST** | 7 частей HUMAN покрыты |
| | Correctness | MUST | факты не выдумываются, provenance обязателен |
| | Appropriateness | MUST | роли чётко разделены, нет scope creep |
| Performance Efficiency | Time behaviour | SHOULD | `/ingest` одного source < 60s, `/ask` < 30s |
| | Resource utilization | SHOULD | context budget < 200K токенов на session |
| | Capacity | COULD | wiki ≤ 10 000 страниц без пересборки graph |
| Compatibility | Co-existence | MUST | работает рядом с Notion до декомиссии |
| | Interoperability | MUST | markdown+git — любой tool читает |
| Usability | Appropriateness recognizability | MUST | Claude Code поймёт структуру без Ruslan'а |
| | Learnability | MUST | <30 мин чтения TECH → понимание |
| | User error protection | MUST | SAFE-SAVE защищает от потери |
| | Accessibility | N/A | персональная система |
| Reliability | Maturity | SHOULD | beta — допускается ручной recovery |
| | Availability | SHOULD | 99% weekly (планировщик ≠ cron) |
| | Fault tolerance | **MUST** | Kay-принцип: работает без AI |
| | Recoverability | MUST | git + append-only logs |
| Security | Confidentiality | MUST | `.env`, `private/`, `~/.ssh/` — недоступны агентам |
| | Integrity | MUST | git history + SAFE-SAVE |
| | Non-repudiation | SHOULD | append-only логи с attribution |
| | Accountability | SHOULD | каждое изменение — коммит |
| | Authenticity | SHOULD | signed commits — желательно |
| Maintainability | Modularity | MUST | 4-слойная модель (Raw/Processed/Synth/Strategic) |
| | Reusability | MUST | knowledge компаундится через edges |
| | Analysability | MUST | `/lint` отчёты, git history |
| | Modifiability | **MUST** | markdown правится любым редактором |
| | Testability | COULD | A/B tests агентов — в v1-final |
| Portability | Adaptability | MUST | другой AI-провайдер, другой разработчик |
| | Installability | SHOULD | документированный bootstrap (Deployment View §7) |
| | Replaceability | MUST | любой компонент можно заменить без rewrite |

**Trade-off:** прочитать как "v1-beta — usability + fault tolerance + portability > performance + testability". Performance оптимизируется в v1-final когда wiki вырастет. Testability формализуется когда появятся клиенты.

## 1.2 Quality Goals (rank-ordered)

Пять главных quality goals для v1-beta, в порядке приоритета:

| # | Quality Goal | ISO 25010 parent | Motivation |
|---|--------------|------------------|------------|
| Q1 | **Transparency** (кто что сделал и когда видно из git + append-only логов) | Maintainability / Analysability | Ruslan должен в любой момент понять state без спроса у агентов |
| Q2 | **Portability** (система переживает смерть любого vendor'а) | Portability / Adaptability | Anthropic rate-limit, Notion API change, Groq выключится — не должно ломать OS |
| Q3 | **Learnability** (новый Claude Code через 30 минут понимает систему) | Usability / Learnability | Контекст Claude тает каждую сессию; документация — фундамент восстановления |
| Q4 | **Modifiability** (markdown-first, любая правка через `Edit` или рукой) | Maintainability / Modifiability | Ruslan работает 4-5 ч/день, не может позволить себе сложные refactorings |
| Q5 | **Data safety** (ни одна заметка не теряется) | Reliability / Recoverability | raw/ — immutable, git — push каждую сессию, SAFE-SAVE паттерн |

**Явный trade-off:** Performance и Security (в полной ISO-интерпретации) занижены. Jetix OS — single-tenant персональная система. Threat model: Ruslan + приватный git repo + локальный vault. Злоумышленники не рассматриваются как основной риск, но `.env` и `private/` защищаются конвенцией.

## 1.3 Stakeholders

Используем формат arc42: **Role → Contact → Expectations**.

| Role | Contact/Identity | Expectations (from system) | Contribution (to system) |
|------|------------------|-----------------------------|--------------------------|
| **Owner-operator** | Ruslan (Berlin) | ускорение работы, поток, $50K/30.06.2026, сохранение информации, чистота | стратегические решения, цели, ресурсы, инвестиции времени |
| **Mentor** | Антон | инсайты системного мышления, психологии | внешние вопросы, переопределения, вызовы |
| **Domain expert — Economics** | Владислав | value-based pricing, бизнес-логика | советы по pricing, sanity check offer'ов |
| **Domain expert — Content/YouTube** | Родион | AI-темы, аудитория, позиционирование | insight про medium, подачу |
| **Central Claude Code** | claude-opus-4-7 (1M context) / claude-sonnet-4-6 | ясный onboarding, non-ambiguous protocols | оркестрация, ingest, ask, ritual runs |
| **Sub-agents (12)** | sales-lead / sales-researcher / ... | чётко описанные roles + invariants + niche filters | специализированная работа |
| **Future team (1y+)** | Hirings, community members | документация, onboarding path | contributions к wiki, code, ADRs |
| **Jetix Club (5-10 на старте)** | Приглашённые партнёры | selected access, knowledge leverage | feedback на систему, тестирование |
| **Clients (anonymous)** | AI-consulting clients | услуги через Ruslan (не прямой доступ) | revenue, case studies, feedback |
| **Notion (external SPOF)** | Notion LLC MCP | временное хранилище до декомиссии | база для миграции α/β/γ/δ |
| **Anthropic API** | claude-opus/sonnet/haiku | inference, 1M context (opus), tool use | вычисления для агентов |
| **Groq API** | Whisper-large-v3 | транскрипция OGG/MP3 | voice pipeline |
| **GitHub** | Bogersebekov/jetix-os | версионирование, remote backup | push destination |

**Контрактное замечание:** Jetix OS — **single-tenant** система (один primary user). Все NFR квантифицируются в этой предпосылке. Переход к multi-tenant (Jetix Club, Corporation) потребует новой итерации (ADR будет создан на этапе).

---

# 2. Architecture Constraints

Arc42 разделяет constraints на три группы. Каждая — неотменяемая предпосылка проекта, которую архитектура **должна принять как данность**, не пытаясь изменить.

## 2.1 Technical Constraints

| ID | Constraint | Rationale | Impact |
|----|------------|-----------|--------|
| TC-01 | **Claude Code CLI** как единственный runtime агентов | Выбран на уровне стратегии; альтернативы (LangChain, CrewAI) добавляют complexity без явной выгоды для персональной системы | Архитектура не предполагает долгоживущих процессов; каждый запуск — fresh session |
| TC-02 | **git + markdown** как единственный storage для knowledge | Docs-as-code → чтение любым редактором, вечное хранение | Нет DB-транзакций, нет ACID; concurrency решается через git conflict resolution |
| TC-03 | **Ubuntu 24** (сервер) + **Windows** (рабочая станция) | Существующее окружение | LF line endings; UTF-8 mandatory; bash как scripting (не PowerShell) |
| TC-04 | **Anthropic API** как primary LLM | Opus 4.6/4.7, Sonnet 4.6, Haiku 4.5 — best-in-class для reasoning | rate limit + 529 retry + cost budget обязательны |
| TC-05 | **Groq API** как Whisper provider | $0.11 / hour vs OpenAI $0.36 | Voice pipeline зависит от Groq uptime |
| TC-06 | **Obsidian vault** на `wiki/` папке | Ruslan использует Obsidian для чтения/навигации | `wiki/` должен быть совместим с Obsidian: `[[wikilinks]]`, frontmatter, tags |
| TC-07 | **Notion MCP** — deprecated зависимость | Декомиссия через migration α/β/γ/δ; сейчас — SPOF (см. ARCHITECTURE-CURRENT.md gap §8) | Агенты должны иметь fallback; MCP падение ≠ остановка системы |
| TC-08 | **Miro MCP** для диаграмм | Существующий board `uXjVG2-05Ns=` | Не критическая зависимость; отключение — deg. режим |
| TC-09 | **1M context** (Opus 4.7) как верхний предел per-session | Hardcoded в модели | Planner компонента должен decompos задачу если prompt > 600K (буфер 40%) |

## 2.2 Organizational Constraints

| ID | Constraint | Rationale | Impact |
|----|------------|-----------|--------|
| OC-01 | **Ruslan — единственный operator** 4-5 часов/день | Факт | Нет on-call rotation; recovery может занять ≥12 часов |
| OC-02 | **Primary goal: $50K до 30.06.2026** | Бизнес-дедлайн | Архитектурные работы не должны блокировать sales. Beta-first. |
| OC-03 | **Beta-first, не perfectionism** | Brooks: "plan to throw one away" | Сложные абстракции (permission matrix, full ADR log) — отложены в v1-final |
| OC-04 | **Русский — основной язык** контента | Пользователь | Frontmatter keys — английский, content — русский; UTF-8; смешанный MD ok |
| OC-05 | **Ручной ритм**: утро/вечер/неделя/месяц | Ruslan | Нет обязательных cron'ов; оркестратор запускается по команде |
| OC-06 | **Semi-manual mode** (Часть 5 HUMAN) | Риск-менеджмент | Никаких автономных действий; все writes требуют либо команды, либо template-trigger |
| OC-07 | **Vendor lock-in невозможен архитектурно** (Kay) | Философский принцип | fallback на человека-оператора документирован и возможен |

## 2.3 Conventions

Эти конвенции — часть архитектуры, а не косметика. Их нарушение → `/lint` error → block'ирует интеграцию.

### 2.3.1 File system conventions

| Convention | Rule | Exception |
|------------|------|-----------|
| Filename | `kebab-case.md` | `YYYY-MM-DD-{slug}.md` для dated sources; `YYYY-MM-DD.md` для daily-log; `YYYY-MM-DD-weekly.md` и т.п. |
| Dates | `YYYY-MM-DD` (ISO 8601) | Никогда DD.MM.YYYY или MM/DD |
| Directory | `kebab-case/` | `_templates/`, `_meta/`, `_moc.md` — подчёркивание подчёркивает "мета" |
| Frontmatter | YAML, mandatory для всех `.md` | Исключение: `README.md`, `.github/*` |
| Encoding | UTF-8, LF | Windows CRLF автоконвертируется при git add (core.autocrlf=input) |
| Max line | 120 символов | Кроме таблиц и inline URL |

### 2.3.2 Frontmatter schema (обязательные поля)

```yaml
---
type: <entity-type>          # one of: idea/claim/source/concept/experiment/summary/foundation/topic/entity — или custom
status: <status>             # draft / ready / archived / superseded
created: YYYY-MM-DD          # MUST
updated: YYYY-MM-DD          # SHOULD (обновлять при редактировании)
sources: [<file-ref>, ...]   # origin trace (required when type in [claim, concept, summary, foundation])
tags: [#type/..., #topic/..., #status/...]
---
```

Опциональные, но типичные: `author`, `topics`, `niches`, `community_id`, `related`, `next_action`, `permissions`.

### 2.3.3 Commit conventions

Формат: `[<area>] <action>: <description>`

| Area | Использование |
|------|---------------|
| `design` | Design docs (SYSTEM-DESIGN-*) |
| `wiki` | Изменения в `wiki/` |
| `raw` | Импорт в `raw/` |
| `daily` | Daily Log записи |
| `project` | Изменения в `projects/{x}/` |
| `crm` | CRM operations |
| `kb` | Legacy knowledge-base/ |
| `meta` | Архитектура, agents, CLAUDE.md |
| `skills` | Изменения в `.claude/skills/` |
| `infra` | Serverside, tools/, scripts/ |
| `tech-review` | 5-chat review артефакты |
| `agent` | Изменения per-agent memory |

Actions: `add`, `update`, `fix`, `release`, `migrate`, `ingest`, `consolidate`, `lint`, `archive`, `rename`.

### 2.3.4 Agent communication conventions

- **Message ID:** `msg-YYYYMMDD-NNN` (regex: `^msg-\d{8}-\d{3}$`)
- **Schema:** `shared/schemas/message.schema.json` — 8 types, 4 priorities, 5 statuses
- **Mailbox format:** JSONL (one message per line)
- **Append-only:** никогда не редактируется, только добавляется

---

# 3. Context and Scope

## 3.1 Business Context

Arc42 business context — карта **кто взаимодействует с системой через какие интерфейсы** на функциональном уровне.

```
                   ┌──────────────┐
                   │    Ruslan    │
                   │  (operator)  │
                   └──────┬───────┘
                          │ natural language commands, voice memos, Daily Log edits
                          ▼
         ┌────────────────────────────────────────┐
         │                                        │
         │           J E T I X   O S              │
         │   (multi-agent knowledge platform)     │
         │                                        │
         └───┬─────────────┬─────────────┬────────┘
             │             │             │
             ▼             ▼             ▼
     ┌───────────┐  ┌────────────┐  ┌──────────┐
     │  Clients  │  │  Partners  │  │  Mentor/ │
     │  (AI-     │  │  (Jetix    │  │  Experts │
     │   consult)│  │   Club)    │  │          │
     └───────────┘  └────────────┘  └──────────┘

NB: Clients и Partners НЕ имеют прямого доступа к Jetix OS на v1-beta.
Вся коммуникация идёт через Ruslan как human-gate.
```

### 3.1.1 Business-level interfaces

| Interface | Direction | Channel | Content | Frequency |
|-----------|-----------|---------|---------|-----------|
| `operator-command` | in | Claude Code CLI | slash-command или natural language | on-demand |
| `voice-memo` | in | `raw/voice-memos/*.ogg` drop | OGG audio | irregular |
| `meeting-record` | in | `raw/meetings/` drop | MP3/transcript | per meeting |
| `article-link` | in | URL pasted to `/ingest` | WebFetch'able content | on-demand |
| `notion-import` | in | `mcp__notion-fetch` → `raw/notion-*` | Notion page JSON | one-time / migration |
| `client-deliverable` | out (via Ruslan) | email/doc handoff | report/case study/deck | per engagement |
| `partner-insight` | out (via Ruslan) | manual share | wiki excerpt | weekly-ish |
| `mentor-update` | out (via Ruslan) | call/chat | status + question | bi-weekly |

### 3.1.2 Ownership & trust boundaries

Jetix OS делится на **три trust zones**:

1. **Trusted (inside-only):** `wiki/`, `projects/`, `strategy/`, `decisions/` — Ruslan + агенты с permission. Никогда не leak наружу без explicit approval.
2. **Semi-trusted (mirror):** `raw/`, `inbox/` — источники могут содержать чувствительное (client names, private discussions). Обрабатываются, но не shared.
3. **Public (repo-level):** `README.md`, `LICENSE`, `.github/` — открытые артефакты.

**Дополнительно (opaque):** `.env`, `private/`, `~/.ssh/`, `config/*.secret.*` — агентам запрещено читать (enforced через prompt rules + file permissions).

## 3.2 Technical Context

Карта **каких API и протоколов касается** Jetix OS.

```
 ┌──────────────────────────────────────────────────────────────────────┐
 │                                                                      │
 │                          LOCAL RUNTIME                               │
 │                                                                      │
 │   ┌──────────────┐     ┌─────────────────────────────────────┐       │
 │   │ Claude Code  │ ──→ │    Subagent Pool (Task tool)         │       │
 │   │ (central CLI)│     │  14 agent definitions in .claude/    │       │
 │   └──────┬───────┘     └─────────────────────────────────────┘       │
 │          │                                                           │
 │          │   filesystem reads/writes                                 │
 │          ▼                                                           │
 │   ┌──────────────────────────────────────────────┐                   │
 │   │ Repo tree: wiki/ projects/ strategy/ raw/... │                   │
 │   │ (git working copy, single worktree main)     │                   │
 │   └──────────────────────────────────────────────┘                   │
 │                                                                      │
 └───────────────────────────┬──────────────────────────────────────────┘
                             │
              (internet / tooling boundary)
                             │
      ┌─────────┬────────────┼─────────┬────────────┬────────────┐
      ▼         ▼            ▼         ▼            ▼            ▼
  ┌────────┐┌─────────┐┌────────┐┌─────────┐┌────────────┐┌─────────┐
  │Anthropic││Groq/    ││Notion  ││Miro MCP ││GitHub      ││Obsidian │
  │API      ││Whisper  ││MCP     ││         ││remote      ││(local   │
  │Opus/    ││API      ││(SPOF — ││(diagrams││(Bogersebe- ││vault    │
  │Sonnet/  ││(voice)  ││to be   ││)        ││kov/jetix-  ││reader)  │
  │Haiku    ││         ││decom-  ││         ││os main)    ││         │
  │         ││         ││missioned│        ││            ││         │
  └────────┘└─────────┘└────────┘└─────────┘└────────────┘└─────────┘
```

### 3.2.1 Technical interfaces — formal spec

| Interface | Protocol | Auth | Payload | Failure mode | v1-beta essentiality |
|-----------|----------|------|---------|---------------|----------------------|
| Anthropic Messages API | HTTPS / JSON | API key | Claude request/response | 429/529 → 3-retry backoff → SAFE-SAVE | **MUST** |
| Anthropic tool use | subset of Messages | same | tool_use blocks | malformed → retry | **MUST** |
| Groq Whisper | HTTPS / multipart | API key | audio blob → text | timeout → fallback OpenAI Whisper (manual) | SHOULD |
| Notion MCP (fetch) | MCP stdio | OAuth (device) | page JSON | disconnect → fallback to `raw/notion-*` dumps | SHOULD (going away) |
| Notion MCP (update) | MCP stdio | OAuth | write ops | disconnect → SAFE-SAVE + report | SHOULD (going away) |
| Miro MCP | MCP stdio | OAuth | board ops | disconnect → доска не обновится, функциональность не ломается | COULD |
| Filesystem | POSIX | OS user `ruslan` | - | permission denied → report | **MUST** |
| Git | SSH (remote) / local | SSH key | git objects | push fail → retry → SAFE-SAVE local | **MUST** |

### 3.2.2 Data types at boundaries

| Boundary | Format | Constraints |
|----------|--------|-------------|
| Voice drop → raw | OGG Opus / MP3 | Ruslan наговаривает; Groq Whisper обрабатывает — max 25 MB |
| Transcript → raw/transcripts | Plain text (.txt) or `.md` with YAML | UTF-8, русский |
| Ingest output → wiki | Markdown + YAML frontmatter | Must pass `/lint` frontmatter check |
| Mailbox msg | JSONL object | Must match `shared/schemas/message.schema.json` |
| State file | JSON pretty-printed | Must match `shared/schemas/*.schema.json` |
| Git commit | Git commit object | Author `Ruslan` or `agent-{id}`; message matches §2.3.3 |

### 3.2.3 Context boundaries — what's *inside* vs *outside*

**Внутри системы (in-scope):**
- Управление знанием (wiki/Karpathy+OmegaWiki model)
- Трекинг 6 ресурсов Ruslan'а
- Оркестрация 12 агентов как ролей центрального Claude
- Персональные CRM (3 базы: clients, partners, personal)
- Стратегические документы (life + projects)
- Ритуалы (day/week/month/quarter)

**Снаружи (out-of-scope, явно):**
- Client-facing портал (v1/v2, не v1-beta)
- Product distribution (Jetix Corporation/Club как отдельные продукты)
- Team collaboration (multi-user) — v2+
- Real-time market monitoring (FR-07) — v1-final
- Financial transactions — вообще, без исключений
- Calendar intentional automation — отложено
- Health-device integration — отложено

---

# 4. Solution Strategy

> Одна страница — ядро архитектуры. **Как** мы реализуем Q1-Q5 (§1.2) через конкретные архитектурные решения.

## 4.1 Strategy Table

| Quality Goal | Strategy | Mechanism | Reference to ADR |
|--------------|----------|-----------|------------------|
| Q1 Transparency | Docs-as-code + append-only логи + git как audit trail | (a) все изменения → git; (b) `log.md` append-only; (c) reports в `reports/` | ADR-001, ADR-009 |
| Q2 Portability | Vendor diversity + file-based fallbacks + Kay-principle | (a) Opus/Sonnet/Haiku тир'ы; (b) Notion→wiki migration; (c) методология работает без AI | ADR-006, ADR-010 |
| Q3 Learnability | Structured self-documenting репо + ONE entry point (this doc + SYSTEM-DESIGN-HUMAN) + CLAUDE.md | (a) 12-секционный arc42; (b) glossary § 12; (c) каждый компонент — interfaces/invariants | ADR-011, ADR-014 |
| Q4 Modifiability | Markdown-first + kebab-case + template-driven + slash-skills как small surface-area | (a) любой текст правится; (b) skills тонкие, компонуются | ADR-003, ADR-008 |
| Q5 Data safety | Append-only logs + immutable raw/ + SAFE-SAVE + git push каждую сессию | (a) raw/ только создание, не удаление; (b) logs — append; (c) SAFE-SAVE на любой ошибке | ADR-009, ADR-013 |

## 4.2 Key Architectural Decisions (summary — full in §9)

1. **Single central Claude Code orchestrator** (ADR-002) — 12 агентов это **роли**, не процессы.
2. **Docs-as-code with git** (ADR-001, ADR-003) — всё в markdown, версия через git.
3. **Karpathy LLM Wiki model** (ADR-006) — graph'овая wiki с 9 entity types и 9 edge types, не vector RAG.
4. **Semi-manual mode for v1-beta** (ADR-005) — ничего не делается автоматически; всё по команде.
5. **Notion decommission via α/β/γ/δ** (ADR-010) — SPOF убирается постепенно, не одним махом.
6. **File-based inter-agent communication** (ADR-007) — JSONL mailboxes, а не Redis/RabbitMQ.
7. **Opus-primary for reasoning, Haiku for throughput** (ADR-012) — model-tier routing per task.
8. **Multi-chat review для критичных дизайн-документов** (ADR-011) — этот документ пример.

## 4.3 Decomposition Strategy

Jetix OS разделена на **6 layer'ов** (не slice'ов). Layer decomposition выбран **по типу данных и владельцу**, не по функциональности:

| Layer | Ownership | Mutability | Example paths |
|-------|-----------|------------|---------------|
| **L0 Raw** | Immutable, write-once | append | `raw/`, `inbox/`, `daily-log/drafts/` |
| **L1 Processed** | Agents write, human reviews | update ok | `wiki/sources/`, `wiki/ideas/` |
| **L2 Synthesized** | Agents write, cross-linked | update ok | `wiki/concepts/`, `wiki/claims/`, `wiki/foundations/`, `wiki/summaries/` |
| **L3 Strategic** | Only Ruslan (human-gate) | versioned | `strategy/`, `decisions/`, `projects/{x}/strategy.md` |
| **L4 Orchestration** | Claude + Ruslan | rewrite ok | `agents/`, `.claude/`, `CLAUDE.md` |
| **L5 Operational** | System-produced | rewrite ok | `reports/`, `shared/state/`, `comms/mailboxes/` |

**Правила перехода:** описаны в §4 HUMAN part-4.3 и §5 Building Block View ниже.

**Trade-off:** layered decomposition — классическая, но **тяжеловесна для малой системы**. Альтернатива — flat (`by topic`) — была бы проще на старте, но мешает росту. Выбор сделан ради Q3 Learnability: новый Claude быстрее понимает "L2 — это синтез, он может переписываться; L0 нет".

## 4.4 What We Explicitly Don't Do (non-strategies)

arc42 рекомендует зафиксировать **non-strategies** — архитектурные подходы, от которых отказались.

| # | Non-strategy | Почему НЕ |
|---|-------------|-----------|
| NS-1 | Микросервисы | overkill, single-user, нет HA requirements |
| NS-2 | Event-driven (Kafka / RabbitMQ) | semi-manual режим, нет потока событий |
| NS-3 | Vector database / embeddings-first RAG | проигрывает Karpathy wiki по Learnability и debugability; HippoRAG на edges достаточно |
| NS-4 | Per-agent dedicated process / container | overhead, нет параллельной нагрузки; Task tool решает |
| NS-5 | Full permission matrix | overkill для single-user; prompt-level guardrails достаточны |
| NS-6 | Formal TLA+ specs | beta-first; Brooks "throw one away" — формальные specs — для v1-final maturity |
| NS-7 | Multi-cloud deployment | избыточно; GitHub + локальный сервер справляются |
| NS-8 | Auto-scaling inference budget | single-user, фиксированный месячный budget разумнее |

---

# 5. Building Block View

> Это **статическая декомпозиция**. Динамика — в §6 Runtime View.

arc42 рекомендует 3 уровня: level 1 (system-of-systems), level 2 (subsystems), level 3 (components for complex subsystems).

## 5.1 Level 1 — Blackbox view (7 blocks)

```
╔════════════════════════════════════════════════════════════════════════╗
║                           J E T I X   O S                              ║
║                                                                        ║
║   ┌──────────┐   ┌──────────────┐   ┌─────────────────────────────┐    ║
║   │ B1 User  │←→│ B2 Orchestr- │→│ B3 Agents (subagents,        │    ║
║   │  Layer   │   │  ation Hub  │   │       spawned via Task tool)│    ║
║   │ (Ruslan) │   │ (central    │   └─────────────────────────────┘    ║
║   └────┬─────┘   │  Claude     │                │                      ║
║        │         │   Code)     │                │ reads/writes         ║
║        │         └──────┬──────┘                ▼                      ║
║        │                │              ┌─────────────────┐             ║
║        │                │              │ B4 Knowledge    │             ║
║        │                │              │    Store (wiki/)│             ║
║        │                │              │ + B5 Operational│             ║
║        │                │              │    Data (proj/, │             ║
║        │                │              │    tasks/, crm/)│             ║
║        │                │              │ + B6 Strategic  │             ║
║        │                │              │    Layer        │             ║
║        │                │              │  (strategy/,    │             ║
║        │                │              │  decisions/)    │             ║
║        │                │              └─────────────────┘             ║
║        │                │                                              ║
║        │                ▼                                              ║
║        │         ┌──────────────────────────────────────┐              ║
║        └───────→│ B7 Integration Layer (MCPs, APIs)    │              ║
║                  │  → Anthropic / Groq / Notion /       │              ║
║                  │    Miro / git / filesystem           │              ║
║                  └──────────────────────────────────────┘              ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

### B1 — User Layer

| Field | Value |
|-------|-------|
| **Purpose** | Приём входа от Ruslan (команды, voice, markdown правки) и вывод результатов (отчёты, diff'ы). Gatekeeper для external communications (clients, partners). |
| **Interfaces (in)** | Claude Code CLI prompts, OGG voice drops в `raw/voice-memos/`, manual markdown edits через Obsidian/VSCode |
| **Interfaces (out)** | client emails (через buffer `/out-drafts`), partner shares, mentor updates, social посты (v1-final) |
| **Invariants** | (1) все external writes require Ruslan approval (Часть 2.4 HUMAN); (2) personal data never leaves `private/` |
| **Dependencies** | B2 (central Claude Code), B7 (file drops) |
| **Quality focus** | Usability, Security (Confidentiality) |

### B2 — Orchestration Hub (central Claude Code)

| Field | Value |
|-------|-------|
| **Purpose** | Главный собеседник Ruslan'а. Входит в роли 12 агентов по необходимости. Оркестрирует spawn sub-agents через Task tool. Держит контекст сессии. |
| **Interfaces (in)** | slash-commands (`/plan-day`, `/close-day`, `/ingest`, `/ask`, `/lint`, ...), natural-language, file reads |
| **Interfaces (out)** | markdown writes, Task tool invocations, MCP calls (Notion/Miro), git operations, Anthropic API |
| **Invariants** | (1) любая мутация L3 Strategic требует explicit confirm; (2) ни один /ingest не commit'ится без git pull first; (3) при uncertainty — stop & ask |
| **Dependencies** | B3 (subagent pool), B4 (reads wiki/), B5 (reads state), B7 (APIs) |
| **Quality focus** | Learnability, Modifiability, Transparency |

### B3 — Agents (subagent roles)

12+ ролей (core: 12, plus 2 utility: sweep-worker, staging-writer).

| Field | Value |
|-------|-------|
| **Purpose** | Специализированная обработка задач под thematic niche. Каждый агент — isolated Claude Code instance со своим system prompt, tool allowlist, permission mode, maxTurns. |
| **Interfaces (in)** | Task tool invocation from B2 (Task tool prompt + subagent_type), `comms/mailboxes/{id}.jsonl` for async msgs |
| **Interfaces (out)** | markdown writes to allowed paths, mailbox append, reports в `reports/` |
| **Invariants** | (1) каждый агент соблюдает свой permission scope (см. §8.1); (2) agent never modifies `.env`, `private/`, other agent's `agents/{other}/`; (3) на error → SAFE-SAVE |
| **Dependencies** | B2 (spawn), B4 (wiki niche slice), B5 (operational data), B7 (external APIs — tool-gated) |
| **Quality focus** | Modularity, Security |

### B4 — Knowledge Store (wiki/)

| Field | Value |
|-------|-------|
| **Purpose** | Единый knowledge base. Karpathy LLM Wiki + OmegaWiki модель. 9 entity types × 9 edge types × 6 niches. Главный информационный актив системы. |
| **Interfaces (in)** | `/ingest` produces pages + edges; `/ask` produces `comparisons/` entries; `/consolidate` merges duplicates; `/build-graph` recomputes |
| **Interfaces (out)** | `/ask` reads; agents read own niche via `agents/{id}/niche/` symlinks; Obsidian reads directly |
| **Invariants** | (1) каждый .md имеет frontmatter; (2) `log.md` append-only; (3) `edges.jsonl` append-only; (4) `index.md` — производное (rebuild'ится из сканирования); (5) никаких orphans >7 дней |
| **Dependencies** | B7 (git для persistence) |
| **Quality focus** | Reusability, Analysability, Portability |

### B5 — Operational Data

| Field | Value |
|-------|-------|
| **Purpose** | Текущее состояние работы: activity-based. Проекты, задачи, CRM, daily-log, hypotheses. Не truth, а **сейчас**. |
| **Interfaces (in)** | agent writes (sales-lead → crm/), Ruslan edits, ritual skills (`/close-day` → daily-log) |
| **Interfaces (out)** | дашборд (если запущен), agent reads (context), strategist reviews |
| **Invariants** | (1) task lifecycle: backlog → today → in-progress → done/blocked; (2) decision → append-only; (3) hypothesis имеет explicit status |
| **Dependencies** | B4 (cross-refs to wiki) |
| **Quality focus** | Modifiability, Time-behaviour |

### B6 — Strategic Layer

| Field | Value |
|-------|-------|
| **Purpose** | Компас. 5/10-year vision, месячный/недельный plan+report, per-project strategy, life-level decisions. Редко меняется, влияет на всё ниже. |
| **Interfaces (in)** | only Ruslan writes (with assistance от central Claude); rituals produce drafts, Ruslan approves |
| **Interfaces (out)** | agents read as context (strategic alignment), ритуалы читают при planning |
| **Invariants** | (1) только Ruslan approves change; (2) ревью по расписанию (weekly, monthly, quarterly); (3) все изменения — версионируются в git |
| **Dependencies** | B4, B5 (data for reflection) |
| **Quality focus** | Functional Suitability (correctness), Auditability |

### B7 — Integration Layer

| Field | Value |
|-------|-------|
| **Purpose** | Абстракция над внешними системами. Изоляция от API-breaks. |
| **Interfaces (in)** | Agent calls (tool use), user commands |
| **Interfaces (out)** | API calls (Anthropic, Groq), MCP calls (Notion, Miro), git ops, POSIX FS |
| **Invariants** | (1) на любой external failure → structured error to caller; (2) SAFE-SAVE state перед потенциально-failing op; (3) credentials только из `.env`, никогда в markdown |
| **Dependencies** | external services (трассируются в §3.2) |
| **Quality focus** | Fault Tolerance, Availability, Compatibility |

## 5.2 Level 2 — Decomposition of Key Blocks

### 5.2.1 B4 Knowledge Store — inside view

```
wiki/
├── index.md                  # каталог: type, path, title
├── log.md                    # append-only: ingest/update/link events
├── overview.md               # high-level map — для новых читателей
│
├── concepts/{slug}.md        # абстрактные идеи ("приоритизация", "compounding")
├── entities/{slug}.md        # люди, компании, продукты (нам identifiable)
├── sources/{date}-{slug}.md  # источник (video, article, conversation)
├── topics/{slug}.md          # hub-страница по теме
├── ideas/{slug}.md           # atomic raw thought
├── experiments/{slug}.md     # попытка проверить гипотезу
├── claims/{slug}.md          # утверждение с evidence
├── summaries/{slug}.md       # compressed overview of cluster
├── foundations/{slug}.md     # первопринципы / manifesto-level
│
├── comparisons/{date}-{slug}.md   # /ask writeback output
├── niches/{niche}/README.md       # 6 niches: personal/business/sales/life/tech/meta
├── graph/
│   ├── edges.jsonl           # {from, to, type, created} append-only
│   ├── communities.md        # connected components (updated by /build-graph)
│   └── summaries.md          # per-community digest
└── _templates/{type}.md      # шаблоны для ingest
```

#### 5.2.1.1 9 Entity types (formal)

| Type | Purpose | Key sections | Created by |
|------|---------|--------------|------------|
| `concept` | abstract general notion | definition, relations, examples | /ingest, /consolidate |
| `entity` | specific real thing / person | facts, interactions, relations | /ingest |
| `source` | origin artifact | citation, claims-extracted, topics | /ingest |
| `topic` | hub for theme | overview, key pages, navigation | manual + /build-graph |
| `idea` | atomic thought (raw) | statement, context, next step | /ingest |
| `experiment` | controlled try | hypothesis, method, result | manual + lifecycle skill |
| `claim` | assertion + evidence | claim text, evidence, counter, status | /ingest, /ask |
| `summary` | synthesized digest | scope, findings, caveats | /consolidate, /build-graph |
| `foundation` | first-principle | principle, rationale, consequences | Ruslan (manual) |

#### 5.2.1.2 9 Edge types (formal)

`edges.jsonl` строки вида: `{"from":"path.md","to":"path.md","type":"<edge-type>","created":"YYYY-MM-DD","origin":"/ingest|/ask|manual"}`.

| Type | Semantics | Example |
|------|-----------|---------|
| `supports` | A provides evidence for B | `source X supports claim Y` |
| `extends` | B elaborates A | `concept Y extends concept X` |
| `derived_from` | B was derived from A | `summary Y derived_from sources [X,Z]` |
| `contradicts` | A disagrees with B | `claim X contradicts claim Y` |
| `explains` | A provides causal explanation for B | `concept explains entity-behavior` |
| `similar_to` | А ≈ Б (fuzzy) | `idea X similar_to idea Y` |
| `used_by` | A is used by B | `tool X used_by project Y` |
| `reverses` | A negates B | `new understanding reverses earlier claim` |
| `part_of` | A is a component of B | `concept X part_of foundation Y` |

**Invariant (edge uniqueness):** `(from, to, type)` — уникален. `/build-graph` детектирует дубли.

#### 5.2.1.3 6 Niches

| Niche | Scope | Symlinks granted to agents |
|-------|-------|----------------------------|
| `personal` | Ruslan lifestyle, preferences, личные выборы | personal-assistant, manager, life-coach, strategist |
| `business` | Jetix, revenue, market, competitors | manager, sales-lead, strategist, knowledge-synth, crazy-agent |
| `sales` | ICP, offer, prospects, CRM | sales-lead, sales-researcher, sales-outreach, knowledge-synth |
| `life` | жизненные принципы, горизонты | life-coach, strategist, knowledge-synth |
| `tech` | инструменты, методология, AI, Jetix OS evolution | system-admin, crazy-agent, meta-agent |
| `meta` | сам процесс работы, рефлексия, improvement | manager, meta-agent, crazy-agent, knowledge-synth, inbox-processor, personal-assistant, system-admin |

**Invariant:** `niche` set — close-world. Добавление niche требует ADR.

### 5.2.2 B3 Agents — roster и model-tier routing

| ID | Model | Tier | Dept | Max turns | Permission | Niche reads | Writes to |
|----|-------|------|------|-----------|------------|-------------|-----------|
| manager | sonnet-4-6 | reasoning | MGMT | 50 | auto | business, meta | `shared/state/`, `reports/`, mailboxes |
| strategist | opus-4-6 | heavy reasoning | MGMT | 30 | **plan** | business, personal | `shared/knowledge/decisions-log.jsonl`, `strategy/` drafts |
| personal-assistant | haiku-4-5 | throughput | OPS | - | auto | personal, meta | drafts, schedule, `inbox/text/` |
| system-admin | haiku-4-5 | throughput | OPS | 30 | auto | meta, tech | `scripts/`, `tools/`, `.claude/`, `reports/` |
| sales-lead | sonnet-4-6 | reasoning | Sales | 30 | auto | sales, business | `crm/`, `projects/{sales}/` |
| sales-researcher | haiku-4-5 | throughput | Sales | 40 | auto | sales | `shared/knowledge/research-summaries/`, `crm/` |
| sales-outreach | haiku-4-5 | throughput | Sales | 30 | auto | sales | `inbox/`, out-drafts/ |
| knowledge-synth | sonnet-4-6 | reasoning | Brain | 40 | auto | все 6 (Brain Lead) | `wiki/`, `reports/`, Research Hub |
| inbox-processor | haiku-4-5 | throughput | Brain | 40 | auto | meta | `raw/`, `wiki/`, Банк идей triage |
| meta-agent | sonnet-4-6 | reasoning | Meta | 40 | **plan** | meta | `reports/audits/`, proposal drafts |
| crazy-agent | sonnet-4-6 | reasoning | Meta | 25 | auto | meta, tech | `wiki/ideas/`, `shared/knowledge/crazy-ideas/` |
| life-coach | sonnet-4-6 | reasoning | Life | 20 | auto | life, personal | `health/`, `reflection/` |
| sweep-worker | sonnet-4-6 | reasoning | utility | 40 | auto | — | `wiki/` (ingest results) |
| staging-writer | sonnet-4-6 | reasoning | utility | 50 | auto | — | `design/SYSTEM-DESIGN-INPUTS.md` |

**Invariant:** `model: claude-opus-4-6` + `permissionMode: plan` для strategist — это архитектурный choice. Только Opus делает стратегические выводы, и только в plan mode (не исполняет). Аналогично meta-agent (plan only — предлагает, не внедряет).

**Trade-off:** plan mode для strategist и meta-agent увеличивает "надо подтвердить у Ruslan'а" нагрузку. Альтернатива — auto — быстрее, но риск "стратегического дрейфа" агента без watchpoint. Выбор сделан ради OC-06 (semi-manual).

### 5.2.3 B5 Operational Data — inside

```
projects/
├── _template/             # scaffold для новых проектов
└── {slug}/
    ├── overview.md        # Point A / Point B / resources
    ├── strategy.md        # ref to strategy/projects/{slug}/
    ├── log.md             # append-only chronology
    ├── tasks.md           # task pool filtered
    ├── ideas.md           # project-scoped ideas
    ├── hypotheses.md      # NEW in v1-beta
    ├── decisions.md       # NEW in v1-beta
    └── open-questions.md  # NEW — для агентов
tasks/
├── master.md              # global task pool with filters
decisions/
├── life-decisions-log.md  # append-only
└── YYYY-MM-decisions.md   # monthly digest
hypotheses/
├── active.md
├── backlog.md
└── validated-archive.md
crm/
├── clients.md
├── partners.md
└── personal.md
```

Каждый .md — **view**, не канон. Канон — distributed (project log есть truth, master — aggregate). Это важное отличие от database: duplication разрешена, если у каждой копии чёткий owner.

**Invariant:** `projects/{slug}/overview.md` должен содержать `next_action:` во frontmatter (чтобы `/plan-day` знал что показать).

### 5.2.4 B6 Strategic Layer — inside

```
strategy/
├── life/
│   ├── 2026-yearly.md        # 5/10 years compressed
│   ├── 2026-04-monthly.md    # cur month report + plan
│   ├── 2026-W17-weekly.md    # current week
│   └── _template-*           # шаблоны
└── projects/{slug}/
    └── strategy.md           # per-project strategy doc
decisions/
└── (see above in 5.2.3)
```

**Invariant:** в strategy/ пишет **только Ruslan** через central Claude в режиме человек-в-цикле. Любой агент, получивший импульс обновить strategy, — **должен** создать `proposal-*.md` в `reports/proposals/`, не править strategy напрямую.

## 5.3 Level 3 — Deeper view for critical subsystems

### 5.3.1 Per-agent memory (5-layer)

Подробнее B3. Каждый агент `{id}` имеет в `agents/{id}/`:

| Layer | File | Purpose | Mutability | Loaded when |
|-------|------|---------|------------|-------------|
| Core | `system.md` | system prompt (role definition) | rarely (ADR change) | start of every session |
| Strategies | `strategies.md` | System Prompt Learning накопления ("когда X → делай Y") | grows after big tasks | loaded with system.md |
| Working | `scratchpad.md` | current session state | session-scoped | on resume |
| Archival | `niche/*` (symlinks в wiki/niches/{niche}) | thematic KB | read-only на уровне symlinks | on demand during task |
| Recall | `comms/mailboxes/{id}.jsonl` | asynchronous messages | append-only | start of session |

**Invariant (baseline/system.md):** HISTORICAL — в ARCHITECTURE-CURRENT.md отмечено, что `baseline.md` и `system.md` идентичны (open question #1). **ADR-013 decision:** `system.md` = canonical; `baseline.md` удалить в Фазе β migration (после обкатки). До этого — не трогать.

**Invariant (strategies.md):** эмерджентная структура. После каждой non-trivial task агент записывает паттерн: "When <context>, do <action>. Rationale: <why>." Формат пока non-strict — в v1-final формализуем.

### 5.3.2 Skills (slash-commands) — surface-area

11 skills в `.claude/skills/`:

| Skill | Purpose | Input | Output | Loaded by |
|-------|---------|-------|--------|-----------|
| `/ingest <path\|url>` | raw → wiki pages + edges | path or URL | wiki pages, log append, edges append, index update | B2 central, inbox-processor |
| `/ask <question>` | query wiki + writeback | question | cited response, optional `comparisons/` write, edges append | B2 central |
| `/lint` | health check wiki | - | `wiki/_lint-report-YYYY-MM-DD.md` | B2 central, meta-agent |
| `/consolidate` | merge duplicates | - | merge notices, updated index | B2 central |
| `/build-graph` | recompute communities | - | `graph/communities.md`, `graph/summaries.md` | B2 central |
| `/plan-day` | утро: фокус + plan | - | Daily Log entry | B2 central |
| `/close-day` | вечер: consolidate + wrap | - | Daily Log update, log appends | B2 central |
| `/focus` | quick attention filter | - | focus.json update | B2 central |
| `/compile <topic>` | legacy: ingested → compiled article | topic | legacy KB article | legacy, не расширяем |
| `/search-kb <query>` | legacy KB search | query | results | legacy |
| `/sweep-notion-bank` | batch-process Notion bank | batch size | wiki ingests + classification report | sweep-worker agent |

**Trade-off:** skills — тонкий слой API. Альтернатива — embedding of operations в agents' system.md. Выбор skills: re-use across agents, consistent UX, testable isolation.

### 5.3.3 Graph/HippoRAG layer

`/build-graph` пересчитывает:
- **Connected components** (communities) — через naive BFS над `edges.jsonl`. Порог для nontrivial community: ≥5 pages.
- **Community summaries** — per-community LLM pass (max 10K tokens) с генерацией `graph/summaries.md`.

**Complexity:** O(E + V) для BFS, O(C × L) для summaries где C — communities, L — LLM latency.

**Invariant:** `communities.md` — derived, rebuildable. Не правится вручную.

**Current state:** 557 страниц, 572 edges, 4 communities (inventory). Под v1-final таргет: 1000+ pages, ~2500 edges, 8-12 communities.

## 5.4 Что намеренно не декомпозируем

| Block | Причина |
|-------|---------|
| `dashboard/` frontend (React/TanStack + Express) | отдельный трек; не критичный для Jetix OS core; decommission-optional |
| `tools/` voice pipeline (Python) | работающий pipeline; 4 файла, coupling low |
| `scripts/` bash | тонкие wrappers, не нуждаются в детализации |
| `docs/adr/` | появится в v1-final (для persistent ADR log); пока ADR живут в этом документе |

---

# 6. Runtime View

> Семь канонических сценариев. Каждый — sequence diagram (ASCII) + прозаическое описание + failure modes.

## 6.1 Scenario: Morning Ritual (`/plan-day`)

**Trigger:** Ruslan открывает terminal, запускает `/plan-day` в central Claude Code.

**Preconditions:**
- `daily-log/{today}.md` ещё не создан (или создан template'ом)
- `strategy/life/` содержит текущий weekly + monthly
- Никаких in-progress блокеров

```
Ruslan           B2 Claude Code       B6 Strategy       B5 OpData       B4 Wiki        Anthropic API
   │                   │                   │                │              │                 │
   ├─ /plan-day ─────→│                   │                │              │                 │
   │                   │─ read ───────────→│ 2026-W17-weekly.md            │                 │
   │                   │←─ weekly ─────────│                │              │                 │
   │                   │─ read ───────────→│ 2026-04-monthly.md            │                 │
   │                   │←─ monthly ────────│                │              │                 │
   │                   │─ read ────────────────────────────→│ focus.json  │                 │
   │                   │←─ focus ─────────────────────────── │              │                 │
   │                   │─ read ─────────────────────────────────────────→│ (recent log,     │
   │                   │                                                   │  active projects)│
   │                   │←─ ctx ──────────────────────────────────────────│                 │
   │                   │─ synthesize plan ──────────────────────────────────────────────────→│
   │                   │←─ draft plan ───────────────────────────────────────────────────────│
   │←─ show plan ─────│                   │                │              │                 │
   │                   │                   │                │              │                 │
   ├─ approve/edit ──→│                   │                │              │                 │
   │                   │─ write daily-log/{today}.md ──────→│              │                 │
   │                   │─ append log ──────────────────────→│              │                 │
   │                   │─ git commit ─────────────────────────────────────────────────────→ git
   │                   │─ git push ───────────────────────────────────────────────────────→ github
   │←─ confirm ───────│                   │                │              │                 │
```

**Steps (prose):**
1. Claude Code считывает strategic context: `strategy/life/2026-W17-weekly.md`, `strategy/life/2026-04-monthly.md`.
2. Считывает operational state: `shared/state/focus.json`, `shared/state/active-projects.json`.
3. Считывает recent daily-log + open tasks из `tasks/master.md`.
4. Формирует draft плана дня: Focus, 3-5 key actions, estimated time, risks.
5. Показывает Ruslan'у → Ruslan approves/edits.
6. Запись в `daily-log/{today}.md` с frontmatter (type: daily-log, date, focus, status).
7. Commit `[daily] plan: {focus}` + push.

**Failure modes:**
- **Notion MCP down** → плану пофиг, Notion не используется на этом шаге.
- **Strategy missing weekly** → Claude предлагает "нет weekly, создать?" — если да, короткий dialog на weekly.
- **Rate limit 529** → retry 3× backoff; если не помогло — SAFE-SAVE drafts локально, escalate Ruslan'у.
- **Ruslan пропустил close-day вчера** → Claude детектирует, предлагает короткий close-day sequence перед plan'ом.

**Quality attributes focus:** Time-behaviour (complete < 60s with approval), Learnability (first-time user понимает ритуал).

## 6.2 Scenario: Ingest Flow (`/ingest <source>`)

**Trigger:** Ruslan присылает ссылку (URL) или path к raw файлу.

**Preconditions:** Файл exists или URL доступен; git working copy clean (либо accepted, что uncommitted — ok).

```
Ruslan      B2 Claude       B7 WebFetch     B4 Wiki     B4 Graph    git
   │             │               │               │           │         │
   ├─ /ingest URL ──→│            │               │           │         │
   │             │─ WebFetch URL→│               │           │         │
   │             │←─ content ────│               │           │         │
   │             │─ persist to raw/web/{slug}.md   │           │         │
   │             │─ parse (LLM) identify entities, claims, concepts     │
   │             │─ for each identified entity:  │           │         │
   │             │    • check if exists ─────────→│           │         │
   │             │    • if new: write wiki/<type>/<slug>.md │           │
   │             │    • append edge <source> → <entity>       │           │
   │             │                               │           │         │
   │             │─ write wiki/sources/YYYY-MM-DD-{slug}.md   │           │
   │             │─ append wiki/index.md         │           │         │
   │             │─ append wiki/log.md           │           │         │
   │             │─ append wiki/graph/edges.jsonl│           │         │
   │             │─ update niche READMEs         │           │         │
   │             │─ git add + commit ─────────────────────────────────→ git
   │             │─ git push ─────────────────────────────────────────→ github
   │             │                               │           │         │
   │←─ report: N pages, M edges ─────────────────│           │         │
```

**Steps (prose):**
1. WebFetch (или Read for file path).
2. Persist raw in `raw/web/` (URL case) or verify `raw/*` location.
3. LLM pass: identify entity types (concept/entity/claim/idea), extract key facts, map to 9 types.
4. For each identified entity: check existence by slug; create new page with template, или append section к existing.
5. Create `sources/{date}-{slug}.md` — citation, claims-extracted, topics.
6. Append all new edges to `edges.jsonl`.
7. Update `index.md` with new page refs.
8. Append `log.md` with ingest event.
9. Apply niche tags (based on topics) → update relevant `niches/<n>/README.md`.
10. Commit `[wiki] ingest: {source_title}`.
11. Push.

**Failure modes:**
- **WebFetch 403/404** → report "cannot fetch", ask Ruslan for alternative.
- **Duplicate detected** → `/consolidate` suggested; по умолчанию merge in-place + notice.
- **Malformed content** → partial ingest (what parsed, skip rest), report to Ruslan.
- **Git conflict** (unlikely for single-user, но возможно после pull) → SAFE-SAVE, ask resolve.

**Quality attributes focus:** Reusability (edges grow), Analysability (log), Integrity (commit atomic-ish).

## 6.3 Scenario: Query Flow (`/ask <question>`)

**Trigger:** Ruslan задаёт вопрос central Claude через `/ask`.

```
Ruslan     B2 Claude        B4 Wiki (index+summaries)    B4 Pages        B4 Comparisons
   │            │                   │                        │                 │
   ├─ /ask Q ──→│                  │                        │                 │
   │            │─ read index.md──→│                        │                 │
   │            │←─ catalog ───────│                        │                 │
   │            │─ read summaries.md → │                    │                 │
   │            │←─ community digests │                     │                 │
   │            │─ pick 5-15 pages by topic match           │                 │
   │            │─ read those ─────────────────────────────→│                 │
   │            │←─ content ───────────────────────────────│                 │
   │            │─ synthesize response with citations              │                 │
   │            │─ if valuable (new link / contradiction / synthesis):       │
   │            │     • write comparisons/YYYY-MM-DD-{slug}.md ──────────────→│
   │            │     • append edges.jsonl                                    │
   │            │     • update index.md                                       │
   │            │     • log.md append                                         │
   │            │     • git add + commit ──────────────────────────→ git
   │←─ answer + citations + optional "saved to /comparisons/" ─┘                 │
```

**Quality logic (writeback criteria):** save to `comparisons/` if ≥1 of:
- Новая связь между 2+ pages (создаёт ≥1 new edge).
- Найдено противоречие (→ `contradicts` edge).
- Синтез по 5+ pages.
- Практический вывод с применимостью.

Иначе — просто ответ в чате без writeback.

**Failure modes:**
- **Too vague question** → Claude просит уточнить вместо halucinate.
- **Нет релевантных pages** → "в wiki нет данных по теме; предлагаю `/ingest <источник>` или ответ без цитат с меткой `no-wiki-support`".
- **Rate limit** → partial answer из уже-прочитанных pages, SAFE-SAVE, ask retry later.

## 6.4 Scenario: Evening Ritual (`/close-day`)

**Trigger:** Ruslan runs `/close-day` (конец рабочего блока).

**Steps:**
1. Read `daily-log/{today}.md` + drafts (`daily-log/drafts/`).
2. Ask Ruslan 4 questions:
   - Что сделал? (objective facts)
   - Key insights?
   - Energy level 1-5?
   - Priorities на завтра?
3. Fill structured sections.
4. For each mentioned project → append `[{date}] {brief}` to `projects/{p}/log.md`; update `next_action` in overview.md frontmatter.
5. Identify insights worth writing → `wiki/ideas/{slug}.md` drafts → Ruslan approve.
6. Update `focus.json` based on tomorrow's priorities.
7. Append Daily Log → if Notion still in use → `mcp__notion-update-page` (Фаза до δ); иначе skip.
8. `git add -A && git commit -m "[daily] close: {today} — {focus}"` + push.

**Failure modes:**
- **Ruslan устал, отвечает коротко** → ok, Claude принимает минимум (energy only).
- **Skip'нут close-day за вчера** → Claude детектит, предлагает quick retrospective.
- **Notion MCP down** (during migration phase) → SAFE-SAVE, note "Notion sync pending" в frontmatter; reconcile later.

## 6.5 Scenario: Weekly Analysis

**Trigger:** Ruslan в конце недели: "давай недельный отчёт + план".

**Steps:**
1. Gather data: 5-7 daily-logs, `projects/*/log.md` entries for week, tasks done/blocked, insights из `wiki/ideas/` created this week.
2. Kick "натягивания" (HUMAN §4.5.2):
   - All open tasks × all projects — "кто кому может помочь?"
   - Active hypotheses × projects — "какую применить?"
3. Generate `strategy/life/2026-W{NN}-weekly-report.md` (отчёт) + `2026-W{NN+1}-weekly-plan.md` (план).
4. Present both to Ruslan → he edits/approves.
5. Commit `[design] weekly: W{NN} report + W{NN+1} plan`.

**Invariant:** каждая неделя — 2 документа (отчёт + план). Templates в `strategy/_templates/`.

**Failure modes:**
- **Data gaps** (skipped days) → Claude помечает "data incomplete", не выдумывает.
- **Project logs empty** (inactive) → помечает как paused/not-updated.

## 6.6 Scenario: Error Flow — Notion MCP down during `/ingest`

**Trigger:** `/ingest` или `inbox-processor` хочет вызвать `mcp__notion-fetch`, MCP not responding.

```
Agent          Notion MCP      git         scratchpad.md       chat
   │              │              │              │                │
   │─ call ──────→│              │              │                │
   │   (timeout) X                              │                │
   │                                            │                │
   │─ detect failure                            │                │
   │─ fallback: try read raw/notion-pages/{slug}│                │
   │     (if exists) → use as source            │                │
   │                                            │                │
   │ if still can't:                            │                │
   │─ SAFE-SAVE:                                │                │
   │    • append scratchpad with "stuck at <step>, pending"       │
   │    • git add -A                            │                │
   │    • git commit -m "[agent-id] SAFE-SAVE: {reason}" ───→ git │
   │    • git push                                               │
   │─ report to chat ──────────────────────────────────────────→ │
```

**Recovery:**
- Ruslan видит repor, решает: (a) дождаться MCP; (b) переключиться на ручной dump `raw/notion-pages/`; (c) отложить task.

## 6.7 Scenario: Migration Flow — Notion Phase γ

**Trigger:** Ruslan запускает Фазу γ (см. `NOTION-MIGRATION-PLAN.md`): полный extract Notion DB в `raw/notion-*` → bulk ingest в wiki/.

```
Ruslan      sweep-worker × N (parallel)    Notion MCP      wiki/       git
   │              │                          │              │           │
   ├─ /sweep-notion-bank batch=50 ──→ spawn 5 sweep-worker in parallel
   │              │                          │              │           │
   │              ├─ fetch batch-1 (idea 0..49)────→│        │           │
   │              │←── idea cards ──────────│        │           │
   │              ├─ classify RELEVANT/IRRELEVANT/UNCLEAR     │           │
   │              ├─ for RELEVANT: /ingest → wiki/─────────→ │           │
   │              ├─ write batch-1 report → reports/         │           │
   │              └─ git commit + push ────────────────────→ git         │
   │         (similarly batches 2..5)                        │           │
   │                                                         │           │
   │←── aggregate report ────────────────────────────────────│           │
```

**Invariant (idempotency):** `/ingest` skip if `raw/notion-ideas/{id}.md` already hashed-matches. Prevents re-import.

**Failure modes:**
- **Rate limit Anthropic** → sweep-worker pauses, sleeps backoff, retries; on final failure — SAFE-SAVE batch state, Ruslan resumes.
- **Notion API change mid-migration** → report: "X/Y completed, stopped at Z"; Ruslan checks MCP, restarts.
- **Duplicate detection edge case** → write to `reports/sweep-conflicts-YYYY-MM-DD.md` for manual reconcile.

---

# 7. Deployment View

## 7.1 Infrastructure

```
┌────────────────────────────────────────────────────────────────────┐
│                      DEVELOPMENT ENVIRONMENT                        │
│                                                                    │
│    Ruslan's Windows laptop                                         │
│    ─────────────────────────                                       │
│    Antigravity IDE (VS Code fork) — primary editor                 │
│    Obsidian — wiki/ vault reader                                   │
│    Claude Code CLI (local) — sometimes                             │
│                                                                    │
│                          ↓ SSH ↓                                   │
│                                                                    │
│    Remote server (VPS Ubuntu 24, 100.99.156.28)                    │
│    ──────────────────────────────────────────                      │
│    tmux session `jetix` — persistent Claude Code                   │
│    /home/ruslan/jetix-os — main worktree                           │
│    git main branch                                                 │
│    Python 3.12 + Node 20 + bash                                    │
│                                                                    │
│                          ↓ git ↓                                   │
│                                                                    │
│    GitHub (Bogersebekov/jetix-os)                                  │
│    Private repo, main + feature branches                           │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

External services:
    • api.anthropic.com — Claude inference
    • api.groq.com — Whisper inference
    • Notion API (MCP) — during migration
    • Miro API (MCP) — diagrams
```

## 7.2 Deployment Topology

Jetix OS — **monolithic, single-user deployment**. Нет HA, нет multi-instance, нет load-balancing.

| Node | Role | Platform | Persistent state |
|------|------|----------|------------------|
| **Dev laptop (Windows)** | Edit surface | Windows 10/11 | Obsidian vault (wiki/), local git clone |
| **VPS Ubuntu 24** | Runtime + storage | linux x86-64 | `/home/ruslan/jetix-os/` (main worktree), tmux, cron (none active now) |
| **GitHub** | remote VCS | managed | repo + issues + releases |

**Trade-off vs cloud-native deployment:** Jetix OS **не** cloud-native. Plusses: full local control, zero-cost platform, vendor-lock immune. Minuses: disaster recovery = SSH backup + git; если сервер умер — восстановление через git clone на новой машине + env setup.

## 7.3 Installation / Bootstrapping

**Из чистой машины до работающей Jetix OS:**

1. `git clone git@github.com:Bogersebekov/jetix-os.git`
2. `cd jetix-os && cp .env.example .env && edit .env` — заполнить `ANTHROPIC_API_KEY`, `GROQ_API_KEY`, Notion/Miro tokens.
3. `python3.12 -m venv venv && source venv/bin/activate && pip install -r tools/requirements.txt` (для voice pipeline).
4. Install Claude Code CLI: per Anthropic instructions, `npm install -g @anthropic-ai/claude-code` или аналог.
5. Configure MCP servers in `~/.claude/mcp.json` (per CLAUDE.md).
6. Optional: Obsidian → Open Vault → select `wiki/`.
7. Bootstrap session: `cd jetix-os && claude` → `/plan-day` — система подскажет если чего-то не хватает.

**Invariant:** bootstrap должен быть документирован и воспроизводим. ADR-014 обязует поддерживать этот раздел.

## 7.4 Dependencies (runtime)

| Dep | Version | Purpose | Critical? | Fallback |
|-----|---------|---------|-----------|----------|
| Claude Code CLI | latest | agent orchestrator | MUST | нет (без него — нет системы) |
| Anthropic API | v1 | LLM inference | MUST | другой provider — потребует новый ADR |
| Git | ≥2.30 | VCS | MUST | нет |
| Python | 3.12 | voice pipeline | SHOULD | 3.11 совместим |
| Groq Whisper | v1 | transcription | SHOULD | OpenAI Whisper (manual) |
| Node.js | 20+ | dashboard (optional) | COULD | dashboard можно отключить |
| Obsidian | 1.6+ | editing UX | COULD | любой MD editor |
| Notion MCP | latest | migration only | COULD | `raw/notion-*` dumps |
| Miro MCP | latest | diagrams | COULD | ручные диаграммы |

## 7.5 Backup + Disaster Recovery

**Levels of backup:**
1. **Git push** — каждая завершённая операция (каждая сессия / каждый коммит).
2. **Remote (GitHub)** — mirror.
3. **Local clone на Windows** — ещё одна копия (via `git pull`).
4. **Optional:** rsync сервер на внешний хост (не реализовано, v1-final).

**DR scenarios:**

| Scenario | Detection | Recovery steps | Estimated downtime |
|----------|-----------|---------------|---------------------|
| Сервер мёртв (hardware fault) | нет SSH | `git clone` на новой машине + bootstrap (§7.3) | ≤1 day |
| Repo corruption (unlikely) | git fsck error | clone mirror (GitHub) | ≤1h |
| Случайное `rm -rf` (human error) | обнаружено | `git reflog` / clone mirror | ≤30min |
| GitHub inaccessible | push fail | работать локально, push позже | дни |
| Anthropic API down | agent calls fail | ручной режим (Kay) — Ruslan работает без AI | инфинит (в пределе) |
| Notion API down | MCP fails | обращаемся в `raw/notion-*` dumps | ok |

**Invariant (backup cadence):** git push — **в конце каждой сессии** (non-negotiable, закреплено в §6.1-6.4 runtime scenarios).

---

# 8. Crosscutting Concepts

> Темы, которые прошивают все компоненты. Описываем **один раз** здесь, ссылаемся из компонентов.

## 8.1 Security

### 8.1.1 Threat Model

Jetix OS — single-tenant persona system в приватном repo. Ключевые threats:

| Threat | Likelihood | Impact | Mitigation |
|--------|------------|--------|------------|
| Credentials leak (API key в commit) | M | High | `.env` в `.gitignore`; `/lint` проверка на secret patterns; git-secrets hook (v1-final) |
| Inadvertent writing into `private/`, `.ssh` | L | High | prompt rules + file permissions 700 + tool allowlist |
| MCP hijack (скомпрометированный MCP server) | VL | High | use only trusted MCP servers (notion official, miro official); tokens rotatable |
| External content injection via `/ingest URL` | M | M | LLM safety filters + raw/ audit; не auto-execute embedded code |
| Malicious raw/ file (binary code in /tools) | L | High | Ruslan approves before `tools/` additions |
| Rogue agent (система скомпрометирована) | VL | H | SAFE-SAVE + git log audit + weekly meta-agent review |

### 8.1.2 Permission Model

**Пока:** prompt-level guardrails (каждый агент знает свой scope через system.md + tool allowlist в agent frontmatter).

**Что-то вроде ACL:**

```
ACL (implicit через tool allowlist в .claude/agents/*.md):
   
   crazy-agent:       Read, Write, Bash, Grep, Glob, web_search
   inbox-processor:   + mcp__notion (limited to Банк идей)
   knowledge-synth:   + mcp__notion + mcp__miro
   life-coach:        + mcp__notion (Life OS DB)
   manager:           + mcp__notion (Command Center + Daily Log)
   meta-agent:        permissionMode=plan — ТОЛЬКО предлагает
   personal-assistant:+ mcp__notion + web_search
   sales-lead:        + mcp__notion (Projects, Research Hub)
   sales-outreach:    + web_search (no mcp__notion)
   sales-researcher:  + web_search (no mcp__notion)
   staging-writer:    — (no extra; just Read/Write/Edit/Bash/Grep/Glob)
   strategist:        permissionMode=plan; + mcp__notion + mcp__miro
   sweep-worker:      — (no extra)
   system-admin:      — (no network, but Bash)
```

**Forbidden paths (соблюдается на уровне prompt + unix perms):**
- `.env`
- `private/*`
- `~/.ssh/`
- `config/*.secret.*`
- `.github/workflows/*` (запрещено агентам — критическая инфра)

**ADR note:** formal permission matrix — в v1-final (см. HUMAN §7.2.5). На v1-beta — convention + prompt rules.

### 8.1.3 Credentials handling

- All secrets in `.env`, loaded at process start.
- Agents никогда не читают `.env` напрямую; API clients читают через env vars.
- Rotations: quarterly для Anthropic key, on compromise для всех.
- Never logged, never committed.

## 8.2 Memory Management

### 8.2.1 Context window budgeting

Opus 4.7 (claude-opus-4-7) — **1M tokens context**. Sonnet 4.6 — 200K. Haiku 4.5 — 200K.

**Rules:**
- B2 central Claude: up to 1M, но эффективно работает до ~800K (избегать surface 95%).
- Subagents: Sonnet 200K — limit в ~150K реально.
- If prompt вырастет > budget — decompose через Task tool (spawn fresh subagent with focused slice).

### 8.2.2 5-layer per-agent memory (see §5.3.1)

Summary: Core (system prompt) — Strategies (learned behaviors) — Working (scratchpad) — Archival (niche symlinks) — Recall (mailbox).

**Invariant (context hygiene):**
- В начале сессии агент reads strategies.md + scratchpad.md (если resume) + latest inbox (unread only).
- В конце сессии — append scratchpad с summary "where I am".
- `/compact` auto-compress на 80% context fill (рекомендация Anthropic).

### 8.2.3 Niche filtering

Каждый агент видит только свой срез wiki через `agents/{id}/niche/` symlinks. Это **не** security (агент может обойти), а **cognitive load reduction** + consistency.

## 8.3 Concurrency

### 8.3.1 Git conflicts

**Actual concurrency model:** low. Primarily single-user.

Возможные сценарии conflict:
- Ruslan правит на laptop + серверный Claude правит параллельно → potential conflict на merge.
- Два subagent'а одновременно правят одну страницу (через Task tool parallel spawn) → conflict.

**Resolution protocol:**
1. Any git conflict → SAFE-SAVE.
2. **Не резолвить автоматически** (возможна потеря).
3. Ruslan обрабатывает conflict manually.
4. ADR-015 (в backlog для v1-final): formal locking через `.lock` files если concurrency вырастет.

### 8.3.2 Parallel subagent execution

Claude Code поддерживает `run_in_background` для Task tool. Использование:
- **Allowed:** независимые задачи (/sweep-notion-bank batches, independent research tasks).
- **Forbidden:** параллельный write в ту же страницу (нет lock'а).

**Invariant:** parent agent должен explicitly ensure non-overlap (batch by disjoint IDs, partition by niche).

### 8.3.3 Race conditions в state

`shared/state/*.json` — не транзакционный. Мутации через:
1. Read current.
2. Modify in memory.
3. Atomic write (`tmp + rename`).

**Trade-off:** нет MVCC, нет locking. Single-user assumption позволяет упростить.

## 8.4 Persistence

### 8.4.1 Append-only principle

| Artifact | Append-only? | Rationale |
|----------|--------------|-----------|
| `wiki/log.md` | **YES** | audit trail |
| `wiki/graph/edges.jsonl` | **YES** | edges accumulate |
| `comms/mailboxes/*.jsonl` | **YES** | message history |
| `decisions/life-decisions-log.md` | **YES** | Ruslan: "не решать 20 раз" |
| `projects/*/log.md` | **YES** | project chronology |
| `daily-log/*.md` | per-day, but day-entries are append within day | day structure |
| `wiki/*/` entity pages | **NO (mutable)** | current state, rewritable |
| `shared/state/*.json` | **NO** | live state, rewrite |
| `wiki/index.md` | derived | rebuilt from scan |

### 8.4.2 Immutable raw/

`raw/*` — **write-once**. Агенты никогда не редактируют raw.

Exceptions:
- Human может исправить typo (documented).
- `raw/voice-memos/*.ogg` после transcription — **не удаляется** (в случае reprocessing).

### 8.4.3 Transactional writes

Для критических writes (страт.документ, decision):
- Write to `.tmp`.
- Rename to final path (atomic on POSIX).
- Git add + commit.

## 8.5 Communication

### 8.5.1 Inter-agent messaging

**Channel:** `comms/mailboxes/{id}.jsonl`, один файл на агента + `human.jsonl` (для messages to Ruslan).

**Schema:** `shared/schemas/message.schema.json` — 8 types × 4 priorities × 5 statuses.

**Example message:**

```jsonl
{"id":"msg-20260418-001","from":"sales-researcher","to":"sales-lead","type":"report","priority":"normal","status":"open","subject":"ICP round 3 complete","payload_ref":"reports/icp-research-2026-04-18.md","ts":"2026-04-18T14:32:00Z"}
```

**Invariant:** append-only; each line valid JSON; `id` unique per day per from-agent.

**Trade-off:** file-based messaging — primitive vs Redis/NATS. Pros: no infra, git-tracked, human-readable. Cons: no pub/sub (each agent polls mailbox), no ordering guarantees beyond append timestamp.

### 8.5.2 State sharing

`shared/state/*.json` — mutable read-write. Not a messaging channel, but a **world state** snapshot.

Examples:
- `focus.json` — current focus area (written by `/focus`, read by `/plan-day`).
- `active-projects.json` — enumeration of active projects (written by strategist via plan mode + approval).
- `priorities.json` — current priority ranking.
- `system-health.json` — operational health.

**Invariant:** любой агент может прочитать; writes — только если agent declared в scope (см. AGENT-PROTOCOLS.md).

## 8.6 Error Handling

### 8.6.1 SAFE-SAVE pattern

**When triggered:** любой of:
- Unhandled exception.
- External dependency unavailable (Notion MCP, rate limit exhausted).
- Agent confused / doesn't know how to proceed.
- Git conflict.
- Context overflow.

**Procedure (per agent):**
```
1. git add -A
2. git commit -m "[<agent-id>] SAFE-SAVE: <short reason>"
   - if commit fails due to hook: git commit --no-verify is FORBIDDEN; fix and retry.
3. git push origin main
   - if push fails: note "push pending" in scratchpad
4. Append scratchpad.md:
   - Where I stopped (file:line or section)
   - What was completed
   - What remains
   - Proposed next step
5. Short report in chat (to Ruslan if central, to parent if subagent)
6. Stop.
```

**Invariant:** SAFE-SAVE **never deletes** state — только fixates.

### 8.6.2 Retry policies

| Failure type | Retry policy |
|--------------|--------------|
| HTTP 429/529 (Anthropic) | 3× backoff 5s → 15s → 45s |
| HTTP 5xx (any API) | 3× backoff 2s → 8s → 30s |
| MCP disconnect | 1× reconnect attempt, then fallback |
| Git push fail (network) | 1× retry, else note + continue local |
| Git push fail (conflict) | no retry, SAFE-SAVE, escalate |
| File write EIO | 1× retry, else SAFE-SAVE |

### 8.6.3 Escalation ladder (v1-beta)

**Simplified for v1-beta:** всё → Ruslan. Нет manager→lead→agent chain (HUMAN §5.4).

**v1-final plan:** hub-and-spoke (subagent → lead → manager → Ruslan). Требует formal implementation of mailbox routing, SLAs.

## 8.7 Testing

### 8.7.1 Testing strategy (v1-beta)

**Tier 0 — Manual:** Ruslan run `/plan-day` etc., проверяет "работает ли".

**Tier 1 — Schema validation:**
- `/lint` — 7 checks (orphans, contradictions, stale claims, missing frontmatter, broken links, missing cross-refs, index drift).
- `shared/schemas/*.schema.json` validation on message write.

**Tier 2 — Integration checks (v1-final):**
- Golden tests: fixed inputs → expected outputs for `/ingest`, `/ask`.
- Agent fixtures: `tests/fixtures/agent-{id}/*.jsonl` with expected replies.

**Tier 3 — A/B prompt tests (v1-final):**
- meta-agent runs on 10% задач, compares A/B prompt variants, metrics в `shared/state/metrics/ab-tests.json`.
- Currently: test infrastructure exists (см. ARCHITECTURE-CURRENT gap #4), but 0 real tests.

**Trade-off:** на v1-beta — manual tests достаточно. Формальные tests добавляют surface area без немедленной выгоды. После стабилизации — автоматизируем.

## 8.8 Observability

### 8.8.1 Logs

| Log | Location | Format | Cadence |
|-----|----------|--------|---------|
| `wiki/log.md` | append-only markdown | `YYYY-MM-DD HH:MM | action | path | note` | per ingest/lint |
| `wiki/_lint-report-YYYY-MM-DD.md` | markdown | 7 sections | per /lint run |
| `reports/audits/YYYY-MM-DD.md` | markdown | meta-agent output | weekly (plan mode) |
| `reports/review_YYYY-MM-DD.md` | markdown | voice review | per voice session |
| `shared/state/metrics/agent-performance.json` | JSON | per-agent latency, success rate | updated after each run |

### 8.8.2 Health checks

`shared/state/system-health.json` — populated by `/lint` and `meta-agent`:

```json
{
  "last_check": "2026-04-18T10:00:00Z",
  "wiki": {"pages": 557, "edges": 572, "orphans": 3, "contradictions": 0},
  "agents": {"active": 12, "stale_strategies": 12},
  "infra": {"notion_mcp": "unstable", "anthropic": "ok", "groq": "ok"},
  "alerts": ["Notion MCP fluctuating"]
}
```

### 8.8.3 Audit trail

**Source of truth:** `git log` — each commit автоматически tracked (author, time, message).

**Semantic overlay:** `wiki/log.md` + `decisions/life-decisions-log.md` + `projects/*/log.md` — human-readable narrative.

## 8.9 Internationalization

- **Content:** русский — primary. Английский допустим в цитатах, терминах.
- **Code/config:** английский — frontmatter keys, filenames, commit messages, schema fields.
- **Mixed MD ok:** один файл может содержать русский content + английские технические термины.
- **No translation pipeline** на v1-beta. Если Ruslan нужен английский output — просит prompt'ом.

## 8.10 Rate Limits

### 8.10.1 Anthropic API

**Tier:** депенит на account; обычно Tier 1-2 для персональной системы.

**Budget strategy:**
- Opus — **reserved для reasoning**: strategist, meta-agent, critical /ask.
- Sonnet — **workhorse**: knowledge-synth, manager, sales-lead, crazy-agent, life-coach.
- Haiku — **throughput**: inbox-processor, sales-researcher, sales-outreach, personal-assistant, system-admin.

**Per-session cap:** central Claude — до ~300K tokens/session типично; hard limit 1M (Opus).

**Monthly budget target:** $200-500/month на v1-beta (rough). Трекать через Anthropic console.

### 8.10.2 Groq

Generous tier. Whisper-large-v3: до ~7200 minutes/day free. Not a concern на v1-beta.

### 8.10.3 Notion / Miro

Notion API — 3 req/sec burst, 2000 req/hour. MCP обёртка респектит. Будет decommission'иться.

Miro — relatively lenient.

---

# 9. Architecture Decisions (ADRs)

> Формат Michael Nygard. Каждый ADR = одно решение, короткий, зафиксированный.

## ADR-001: Docs-as-code as source of truth

- **Status:** accepted
- **Date:** 2026-04-17

### Context
Jetix OS нужен long-term storage знаний. Исторически Notion использовался. Но Notion — SPOF, vendor-locked, не searchable as files, не git-diff'able.

### Decision
**Все знания и операционные данные — в git-tracked markdown + JSON файлах внутри `~/jetix-os/`.** Notion становится **каналом распространения**, не truth. Filesystem = internal source of truth.

### Consequences
- (+) Polyvalent tooling: grep, git, любой editor, Obsidian, VS Code.
- (+) Vendor-independent: никто не может "отключить" данные.
- (+) Version history free.
- (+) Diff-able: легко ревью изменений.
- (−) Нет rich UI Notion'а (calendars, relational views) — требует альтернатив.
- (−) Синхронизация между platforms становится manual до декомиссии.

### Trade-offs considered
- Альтернатива 1: **stay with Notion**. Rejected — vendor lock.
- Альтернатива 2: **SQLite** (local DB). Rejected — markdown более human-readable и compatible с Obsidian.
- Альтернатива 3: **hybrid** (markdown for wiki, DB for structured ops data). Rejected — complexity без pay-off на v1-beta.

---

## ADR-002: Single central Claude Code orchestrator

- **Status:** accepted
- **Date:** 2026-04-17

### Context
Ruslan описал систему с 12 агентами. Распространённая интерпретация — 12 долгоживущих processes (LangChain-style, CrewAI). Однако: single user, 4-5h/day, semi-manual ritms. 12 живых processes — overhead без пользы.

### Decision
**12 агентов — это роли центрального Claude Code (B2).** Агенты spawn'ятся on-demand через Task tool как short-lived subagent processes (isolated context). После task — контекст сохраняется в `agents/{id}/scratchpad.md`, процесс terminates. Персистентность — через файловую систему, не running process.

### Consequences
- (+) Resource-efficient: 1 process, а не 12.
- (+) Centralized UX: Ruslan говорит с одним Claude, который "входит в роль".
- (+) No infrastructure for process supervision (systemd, pm2).
- (+) State persistence — всё в filesystem.
- (−) Не паррелельно работают 12 агентов — параллелизм через explicit Task tool `run_in_background`.
- (−) Если агенту нужен долгий background watch (e.g., monitor mailbox) — не работает (no daemon).

### Trade-offs considered
- **LangChain crewai multi-process** — rejected, overhead and infra overhead.
- **SystemD services per agent** — rejected, complexity.

---

## ADR-003: Markdown + git instead of database

- **Status:** accepted
- **Date:** 2026-04-17

### Context
Знание нужно хранить, индексировать, искать, связывать, мутировать, диффить. Канди: (a) Postgres, (b) SQLite, (c) markdown+git, (d) dedicated graph DB (Neo4j).

### Decision
**Markdown files + YAML frontmatter + git** как storage. Graph — через `edges.jsonl` (append-only). Search — grep + LLM-semantic (`/ask`). Index — autogenerated markdown.

### Consequences
- (+) Human-readable always.
- (+) Git history free.
- (+) No daemon.
- (+) Plays with Obsidian, IDE, any editor.
- (−) Нет DB-performance (joins, transactions).
- (−) Полный full-text scan медленный на 10K+ pages (будет проблемой в v2).

### Trade-offs considered
- **SQLite** — rejected. Good perf, но media сложнее (каждое поле — row), не human-readable.
- **Neo4j** — rejected. Overkill для 1000 pages; operational complexity.
- **Postgres** — rejected. Deployment overhead.

---

## ADR-004: 12 agents as thematic roles

- **Status:** accepted
- **Date:** 2026-04-17

### Context
Почему 12, а не 3 или 20? HUMAN §3.2.3 — "Пока достаточно 12, это не окончательный состав."

### Decision
**12 агентов разделены на 6 департаментов** (MGMT, OPS, Sales, Brain, Meta, Life) по тематической специализации. Это **current fit**, не универсальный ответ. Состав подлежит пересмотру в v1-final или v2 после опыта использования.

### Consequences
- (+) Каждый агент имеет clear scope → легко debugging, evaluation.
- (+) Departmental structure — growth path для hire (Sales team — готовая мета-структура).
- (−) 12 агентов требуют 12 system prompts + strategies + niche → overhead.
- (−) Некоторые агенты сейчас пустые mailbox'ы (6 из 12 — см. ARCHITECTURE-CURRENT gap #1) — пока недогружены.

### Trade-offs considered
- **5-agent minimal** (central + 4 leads) — rejected, теряется специализация по ICP research vs outreach.
- **20+ fine-grained** — rejected, overhead.

---

## ADR-005: Semi-manual mode в v1-beta (no cron, no event-driven)

- **Status:** accepted
- **Date:** 2026-04-18

### Context
Системы могут быть реактивными (cron, event-driven) или manual. Cron = автоматизация, но риск "случайностей" на неотлаженной архитектуре.

### Decision
**В v1-beta — все действия по команде Ruslan'а.** Нет cron'ов, нет event-driven. После обкатки (1-2 месяца) — selectively включать автоматизацию.

### Consequences
- (+) Предсказуемость: ничего не происходит без команды.
- (+) Обучение паттернам: Ruslan видит каждый шаг, накапливает intuition.
- (+) Безопасность: нет "рогуэ агентов".
- (−) Ruslan должен помнить запустить ритуалы (compensated by prompts/reminders).
- (−) Нет real-time реакции на inbox.

### Trade-offs considered
- **Full automation on day 1** — rejected, beta-first принцип.
- **Event-driven inbox** (inotify) — deferred для v1-final.

---

## ADR-006: Karpathy LLM Wiki + OmegaWiki model

- **Status:** accepted
- **Date:** 2026-04-15 (pre-this-review, inherited)

### Context
Для LLM-native knowledge, два mainstream подхода: (a) vector embedding-first (RAG with Chroma/Pinecone), (b) Karpathy-style graph wiki с typed edges и communities. Нужно выбрать один.

### Decision
**Karpathy LLM Wiki + OmegaWiki.** 9 entity types (concept/entity/source/topic/idea/experiment/claim/summary/foundation), 9 edge types, 6 niches, graph communities через `/build-graph`. HippoRAG — retrieval через edges, а не через cosine similarity.

### Consequences
- (+) Edges — explicit, debuggable, human-readable.
- (+) Нет затрат на vector DB, embedding compute.
- (+) Communities — emergent structure после ingest.
- (+) Compatibility с Obsidian wikilinks `[[X]]`.
- (−) Требует disciplined tagging (типы, niches).
- (−) Не scale'ится на 100K+ pages без ре-архитектуры.

### Trade-offs considered
- **pgvector / Chroma** — rejected, added infra, worse debuggability.
- **Hybrid** (graph + embeddings) — deferred для v2 если потребуется semantic query.

---

## ADR-007: File-based messaging (JSONL mailboxes)

- **Status:** accepted
- **Date:** 2026-04-17

### Context
Агентам нужно обмениваться сообщениями. Опции: (a) in-memory (losses on restart), (b) Redis/NATS (infra), (c) file-based JSONL (primitive, git-trackable).

### Decision
**JSONL mailboxes** (`comms/mailboxes/{id}.jsonl`). Append-only. Schema в `shared/schemas/message.schema.json`. Один файл на агента + `human.jsonl`.

### Consequences
- (+) Zero infrastructure.
- (+) Git-trackable — полный audit.
- (+) Cross-platform.
- (−) Нет pub/sub — каждый агент poll'ит свой mailbox.
- (−) Fault tolerance: если два агента пишут одновременно — риск interleaving (смягчается singletone-writer invariant).

### Trade-offs considered
- **Redis** — rejected, infra.
- **NATS JetStream** — rejected, overkill.
- **Shared state JSON** — rejected, не подходит для message-semantics.

---

## ADR-008: Niche via symlinks (not DB views)

- **Status:** accepted
- **Date:** 2026-04-17

### Context
Каждый агент должен видеть свой тематический срез wiki. Как ограничить?

### Decision
**`agents/{id}/niche/` содержит symlinks** на `wiki/niches/{niche}/`. 6 niches, per-agent subset. Not enforced на permission level — enforced "cognitively" (агент знает "я смотрю только сюда").

### Consequences
- (+) Filesystem-native.
- (+) Никакой runtime query — просто `ls` работает.
- (+) Легко ревизовать: посмотрел symlink — увидел scope.
- (−) Symlinks могут сломаться при move/rename.
- (−) Cannot enforce strict isolation (агент может прочесть что угодно если попросят).

### Trade-offs considered
- **DB views + authz** — rejected, infra.
- **Per-agent full copies** — rejected, storage waste + sync hell.

---

## ADR-009: Append-only logs

- **Status:** accepted
- **Date:** 2026-04-15 (inherited)

### Context
Системы, которые мутируют state, теряют историю. Системы append-only — ничего не теряют, но растут. Trade-off.

### Decision
**`wiki/log.md`, `projects/*/log.md`, `decisions/*-log.md`, mailboxes** — append-only. Новые записи добавляются **сверху** (в `log.md`: новая запись → top of file, old entries scroll down). **При >30 записей** ротация в `archive/`.

### Consequences
- (+) Full history — debuggable, trustworthy.
- (+) Decisions never "forgotten".
- (−) File size grows. Ротация mitigates.
- (−) Не может "откатить" запись (но git track'ит — можно восстановить).

### Trade-offs considered
- **Mutable state** — rejected for critical logs.
- **Timestamped immutable per-entry files** — rejected, too many small files.

---

## ADR-010: Notion decommission через α/β/γ/δ phases

- **Status:** accepted
- **Date:** 2026-04-16

### Context
Notion — SPOF, vendor-locked, не git-diff'able. Нужно убрать без потери данных.

### Decision
**Фазированная миграция** (NOTION-MIGRATION-PLAN §5):
- **α** — extract Системы self-description pages → `raw/notion-pages/`.
- **β** — extract operational data (Daily Log DB, Projects DB, Журнал чатов).
- **γ** — extract Банк идей (650+) через sweep-worker batch processing.
- **δ** — cutover: Notion read-only архив, writes → wiki.

### Consequences
- (+) Позволяет работать с Notion до того как migration complete.
- (+) Reversible на любой фазе.
- (+) Каждая фаза — discrete, tested.
- (−) 4 фазы — месяцы работы.
- (−) В процессе — dual-source of truth (Notion + wiki).

### Trade-offs considered
- **Big-bang cutover** — rejected, risk of data loss.
- **Stay with Notion + sync** — rejected, long-term SPOF.

---

## ADR-011: Multi-chat review for critical technical docs

- **Status:** accepted
- **Date:** 2026-04-18

### Context
Критический дизайн-документ, написанный одним Claude, может попасть в "локальный минимум" — проглядеть уязвимости. Human review длителен (Ruslan 4-5h/day — bottleneck).

### Decision
**Для критических документов — 5-chat review methodology:**
- Chat 1 — Critic (adversarial).
- Chat 2 — Optimizer (visionary).
- Chat 3 — Engineer A (arc42 school).
- Chat 4 — Engineer B (C4 / event-driven).
- Chat 5 — Synthesizer (merge, finalize).

Каждый работает независимо, не видит других. Синтезатор объединяет.

### Consequences
- (+) 4 независимых перспективы → cross-verification.
- (+) Reduction of blind spots.
- (+) Explicit disagreements записываются → lessons.
- (−) 4× inference cost (но justify'ит для документов годного значения).
- (−) Ruslan должен дирижировать процесс.

### Trade-offs considered
- **Single Claude pass** — rejected для критики (rissk blind spots).
- **2-chat (author + reviewer)** — considered, rejected as мало.

---

## ADR-012: Opus-primary (Sonnet fallback) for reasoning

- **Status:** accepted
- **Date:** 2026-04-15

### Context
3 модели: Opus (лучшее reasoning, дорого), Sonnet (balance), Haiku (cheap throughput). Какие roles — какие модели?

### Decision
Per-agent model assignment на уровне `.claude/agents/{id}.md` frontmatter:
- **Opus 4.6:** strategist (only heavy reasoning).
- **Sonnet 4.6:** manager, sales-lead, knowledge-synth, crazy-agent, life-coach, meta-agent, staging-writer, sweep-worker (reasoning workhorses).
- **Haiku 4.5:** personal-assistant, system-admin, inbox-processor, sales-researcher, sales-outreach (throughput).
- **Central Claude Code (B2):** Opus 4.7 (1M context) — расширенный context + reasoning.

### Consequences
- (+) Cost-optimized.
- (+) Latency-optimized per task.
- (−) Mixed-quality responses в chains (Haiku digest → Sonnet synth → Opus decide).
- (−) Model upgrade — требует per-agent review.

### Trade-offs considered
- **All Opus** — rejected, cost.
- **All Sonnet** — rejected, waste on simple tasks (Haiku подходит).

---

## ADR-013: `system.md` как canonical, `baseline.md` deprecated

- **Status:** accepted
- **Date:** 2026-04-18

### Context
ARCHITECTURE-CURRENT gap #6: `agents/{id}/baseline.md` (immutable v1.0) и `system.md` (рабочая) содержат identical content. Выбор canonical не сделан. Open question в прошлом inventory report.

### Decision
**`system.md` = canonical.** `baseline.md` — удалить в Фазе β migration (после одной недели стабильности без `baseline.md`). До этого: `system.md` обновляется с ADR + version bump в frontmatter (`version: X.Y`). History — через git.

### Consequences
- (+) Simpler mental model: один source файл per agent.
- (+) Git — уже даёт immutability через history.
- (−) Потеря "immutable baseline" концепта — но она не использовалась.

### Trade-offs considered
- **Keep both, sync** — rejected, duplication без функции.
- **Formalize baseline** (lockfile) — rejected, overkill для single-user.

---

## ADR-014: SYSTEM-DESIGN-TECH как onboarding для агентов

- **Status:** proposed
- **Date:** 2026-04-18

### Context
Future agents (после v1-final) должны быстро понять архитектуру. В текущем CLAUDE.md — 163 строки (overview). SYSTEM-DESIGN-HUMAN — 1990 строк (бизнес-язык). Где системные факты — не зафиксировано единообразно.

### Decision
**SYSTEM-DESIGN-TECH.md (после synthesis из 5-chat review)** становится **mandatory read** для:
- Новых агентов (в системном промпте — reference).
- Новых разработчиков/collaborators.
- Любого Claude Code который будет работать над Jetix OS после сессии pause.

CLAUDE.md сокращается до quick-ref; full details — в TECH.

### Consequences
- (+) Single source of truth на архитектурном уровне.
- (+) Explicit onboarding path.
- (−) TECH длинный (>2000 строк) — нужен glossary + navigation.

### Trade-offs considered
- **Keep long CLAUDE.md** — rejected, mixed concerns (config + architecture + vision).
- **Split into multiple docs** — accepted (TECH + PROTOCOLS + FLOWS + TARGET).

---

## (дополнительные ADR — в backlog для v1-final)

- **ADR-015:** Formal locking / concurrency control (if multi-user ever).
- **ADR-016:** Client-facing API (when Jetix Corporation layer kicks off).
- **ADR-017:** Distributed agent deployment (if scale вызывает).
- **ADR-018:** Full permission matrix (замещает §8.1.2 prompt rules).

---

# 10. Quality Requirements

## 10.1 Quality Tree

```
Jetix OS v1-beta quality priorities (rank-ordered)
│
├── Transparency (Q1) [TOP PRIORITY]
│   ├── Git-tracked everything
│   ├── Append-only critical logs
│   └── Human-readable throughout
│
├── Portability (Q2)
│   ├── Vendor-agnostic storage (markdown + git)
│   ├── Multi-model AI (Opus/Sonnet/Haiku)
│   └── Kay-principle: works even without AI
│
├── Learnability (Q3)
│   ├── Structured 12-section arc42 doc
│   ├── Glossary
│   └── Per-component interfaces/invariants
│
├── Modifiability (Q4)
│   ├── Markdown everywhere
│   ├── Slash-skills as small surface area
│   └── Template-driven scaffolding
│
├── Data safety (Q5)
│   ├── Immutable raw/
│   ├── SAFE-SAVE on all failures
│   └── git push per session
│
├── Reliability — Fault Tolerance (inherited from Q2)
│   └── System degrades gracefully on vendor failure
│
├── Security [medium]
│   ├── .env never committed
│   ├── Permission via prompt-rules + tool allowlist
│   └── Threat model documented (§8.1.1)
│
├── Performance [low priority в v1-beta]
│   ├── /ingest < 60s for typical source
│   └── /ask < 30s typical
│
└── Testability [deferred]
    └── Формализуем после v1-beta обкатки
```

## 10.2 Quality Scenarios

Arc42 стандарт: stimulus + response + measure.

### QS-01: Learnability for new Claude Code

- **Stimulus:** Новая сессия Claude Code начинается (предыдущий контекст потерян). Агент получает задачу "продолжить работу над Jetix OS".
- **Response:** Агент читает CLAUDE.md → SYSTEM-DESIGN-TECH.md → переходит к задаче.
- **Measure:** Агент задаёт Ruslan'у ≤3 clarifying questions перед первой productive action. Достигается через полноту TECH.

### QS-02: Learnability for new human contributor

- **Stimulus:** Новый разработчик заходит в репо впервые.
- **Response:** Открывает `README.md` → CLAUDE.md → TECH. Понимает архитектуру, роль агентов, где что лежит.
- **Measure:** ≤30 минут до понимания "что есть что" + способность задать осмысленный вопрос Ruslan'у.

### QS-03: Portability — Anthropic rate limit exhaustion

- **Stimulus:** Anthropic API возвращает 429 в 100% запросов на 4 часа.
- **Response:** Агенты работают в deg. mode: Ruslan может вручную редактировать markdown, git-commit, run bash scripts. Жизнь Jetix OS продолжается, хотя без AI inference.
- **Measure:** Ruslan может закрыть day (`/close-day` замещается ручным editing) с 80% качеством.

### QS-04: Portability — Notion decommission

- **Stimulus:** Notion API shutting down (hypothetical).
- **Response:** Jetix OS продолжает работать на wiki/ + git. Активные данные доступны.
- **Measure:** Ноль data loss; ≤1 day на reassessment процессов, которые зависели от Notion.

### QS-05: Data safety — voice memo pipeline failure mid-transcribe

- **Stimulus:** `tools/transcribe.py` crashes в середине batch (5 из 20 memos processed).
- **Response:** Скрипт exits с SAFE-SAVE: 5 processed транскриптов в `raw/transcripts/`, метаdata о оставшихся 15 — в `reports/voice-batch-YYYY-MM-DD.md`.
- **Measure:** 0 data loss (OGG не удаляются); Ruslan может re-run на оставшиеся 15.

### QS-06: Data safety — git push failure

- **Stimulus:** `/ingest` завершился, но `git push` fail'ит (network down).
- **Response:** Commit создан локально; агент отмечает "push pending" в scratchpad. Ruslan pushes позже.
- **Measure:** ≤5 мин manual resolution.

### QS-07: Transparency — Ruslan audits "who changed X"

- **Stimulus:** Ruslan видит неожиданное изменение в `wiki/concepts/{X}.md`.
- **Response:** `git blame` shows commit author + message + timestamp. Matching log entry в `wiki/log.md`.
- **Measure:** ≤5 мин до полного понимания change context.

### QS-08: Modifiability — adding new agent

- **Stimulus:** Ruslan решил добавить агента `legal-advisor`.
- **Response:** Создаёт `.claude/agents/legal-advisor.md` (copy from template), добавляет `agents/legal-advisor/` скелет, adds niche symlinks, обновляет CLAUDE.md roster.
- **Measure:** ≤60 мин с добавлением первого working task.

### QS-09: Modifiability — changing edge type semantic

- **Stimulus:** Ruslan решает "supports" = означает только source→claim, никак не source→concept.
- **Response:** Обновить `wiki/graph/README.md` (или `design/SYSTEM-DESIGN-TECH.md §5.2.1.2`), добавить `/lint` check, запустить `/lint` → покажет violating edges → consolidate.
- **Measure:** ≤3h для completion.

### QS-10: Reliability — Notion MCP disconnect mid-session

- **Stimulus:** `inbox-processor` запускает `/sweep-notion-bank`. Middle batch — MCP disconnect.
- **Response:** Batch worker detects, SAFE-SAVE state, reports to chat, terminates. Next run — continues from checkpoint (idempotent на `raw/notion-ideas/` dedup).
- **Measure:** 0 data loss; ≤10 мин resume.

### QS-11: Security — credentials hygiene check

- **Stimulus:** Ruslan коммитит случайно файл с API key.
- **Response:** `/lint` detect pattern (v1-final: git hook blocks commit). В v1-beta — Ruslan manually runs `/lint` regularly.
- **Measure:** ≤24h detection (weekly /lint cadence).

### QS-12: Performance — ingest huge article

- **Stimulus:** `/ingest https://.../long-article` (100K characters).
- **Response:** Chunked into overlapping sections, processed, consolidated.
- **Measure:** ≤5 min end-to-end, 0 data loss.

### QS-13: Functional Suitability — /ask returns correct citation

- **Stimulus:** `/ask "что такое information discipline?"` с известным answer в wiki/ideas/information-discipline-as-core-skill.md.
- **Response:** /ask returns answer with [[file-ref]] citation pointing там.
- **Measure:** Сorrectness ≥90% на sample 20 questions (meta-agent в v1-final будет evaluate).

### QS-14: Usability — ritual без Ruslan'а

- **Stimulus:** Пройден день, Ruslan пропустил close-day.
- **Response:** На следующее утро `/plan-day` detect'ит missing close, offer короткий recap.
- **Measure:** ≤5 min recover.

### QS-15: Maintainability — new skill addition

- **Stimulus:** Ruslan добавляет `/weekly-review` skill.
- **Response:** Creates `.claude/skills/weekly-review.md` с frontmatter + описанием алгоритма. Central Claude auto-discover. No deploy steps.
- **Measure:** ≤30 мин + immediate runnable.

---

# 11. Risks and Technical Debt

## 11.1 Known Risks (прямо из ARCHITECTURE-CURRENT gaps + новые)

### R-01: Notion MCP instability (SPOF)

- **Severity:** High
- **Likelihood:** High (observed on sessions)
- **Impact:** Если Notion используется в flow (/plan-day, /close-day), потенциальный blocker.
- **Mitigation:** Migration α/β/γ/δ (ADR-010). Fallback to `raw/notion-*` dumps. v1-beta — Notion not on critical path (ritmy работают без него).

### R-02: 6/12 agent mailboxes пустые (inventory gap #1)

- **Severity:** Medium
- **Likelihood:** Current state
- **Impact:** Доказательство "12 agents work" — не подтверждено productive traffic. Mailbox-шина не tested в bulk.
- **Mitigation:** Первые 2 недели v1-beta — Ruslan запускает каждого агента минимум 1 раз на реальной задаче; fill mailboxes natural traffic'ом.

### R-03: `strategies.md` empty for all 12 agents (inventory gap #9)

- **Severity:** Medium
- **Likelihood:** Current state
- **Impact:** System Prompt Learning не работает (агенты не learn across sessions).
- **Mitigation:** После каждой non-trivial задачи — **обязательно** append strategies.md паттерн. Meta-agent weekly audit это enforce'ит.

### R-04: meta-agent и strategist — permissionMode=plan без real output (inventory gap #4, #5)

- **Severity:** Low (для v1-beta); Medium (для v1-final)
- **Likelihood:** Current
- **Impact:** Proposals не исполняются → нет actual improvement cycle.
- **Mitigation:** В v1-beta — это ok (semi-manual). В v1-final — добавить "Ruslan approves → implementation" workflow для proposals.

### R-05: `distribute.py.bak` отключён → triage вручную

- **Severity:** Low
- **Likelihood:** Ongoing
- **Impact:** Voice memos распределяются вручную после review.
- **Mitigation:** v1-beta — intentional (human gate). v1-final — возможна reintroduction как approved skill.

### R-06: Context window exhaustion (B2 central Claude)

- **Severity:** Medium
- **Likelihood:** Medium (с ростом wiki)
- **Impact:** После длинной сессии — Claude может захлебнуться. `/compact` mitigates.
- **Mitigation:** `/compact` at 80% fill. Spawn subagent для deep dive в wiki вместо прямого чтения 100 страниц.

### R-07: Git conflicts от параллельной работы (laptop + сервер)

- **Severity:** Low
- **Likelihood:** Medium
- **Impact:** Потеря работы при bad merge.
- **Mitigation:** Pull first всегда. SAFE-SAVE на любую ambiguity. No auto-merge of content conflicts.

### R-08: Cost overrun на Anthropic API

- **Severity:** Medium
- **Likelihood:** Medium (растёт с использованием)
- **Impact:** Бюджет раздувается.
- **Mitigation:** Monthly tracking (см. §8.10.1). Budget alerts (manual). Haiku для throughput.

### R-09: Knowledge rot — stale claims не detect'ятся

- **Severity:** Low
- **Likelihood:** Low в v1-beta (wiki мала)
- **Impact:** Старые утверждения считаются истиной.
- **Mitigation:** `/lint` weekly check stale claims (>90 days старые без re-verify). v1-final — formalize claim TTL.

### R-10: Single-person bus factor

- **Severity:** Critical
- **Likelihood:** Current
- **Impact:** Если Ruslan болеет / недоступен — никто не continues.
- **Mitigation:** Documentation (эта) + Kay-principle (система работает без AI + без Ruslan на короткий горизонт). v1-final — onboard ≥1 partner/engineer как backup operator.

### R-11: Agent over-trust — hallucination pipelined в wiki

- **Severity:** High
- **Likelihood:** Medium
- **Impact:** Неверная claim уходит в wiki → используется агентами → compound'ится.
- **Mitigation:** provenance (sources:) обязателен. /lint contradiction check. Ruslan ревьюит L3 Strategic — never auto-promote.

### R-12: Obsidian vault corruption

- **Severity:** Low
- **Likelihood:** Low
- **Impact:** Local edits потеряны.
- **Mitigation:** git-tracked, so recoverable.

## 11.2 Technical Debt Catalog

### TD-01: `baseline.md` и `system.md` duplication

- **Source:** inventory gap #6 + ADR-013
- **Remediation:** Удалить `baseline.md` после 1 недели стабильной работы.
- **Target:** Фаза β migration.

### TD-02: `ingest.md` vs `ingest.md.new`

- **Source:** inventory gap (ARCHITECTURE-CURRENT.md).
- **Status:** Merged — `ingest.md` now = v2 contents. `.new` not in tree. **Close.**

### TD-03: `agents/content-team/`, `agents/research-team/`, `agents/sales-team/`, `agents/_shared/` — orphan folders

- **Source:** inventory gap #10
- **Remediation:** Investigate content; if unused → archive, remove refs. Если содержат valuable — integrate.
- **Target:** v1-beta first week.

### TD-04: `comms/escalation.jsonl` упомянут но не существует

- **Source:** inventory gap #11
- **Remediation:** Create empty file + formal spec в AGENT-PROTOCOLS.md. Only fill когда escalation actually used.
- **Target:** v1-beta.

### TD-05: `/focus`, `/close-day`, `/plan-day` skills — директории без ясной структуры

- **Source:** `.claude/skills/` ls показал `close-day`, `focus`, `plan-day` как директории (не `.md` файлы).
- **Remediation:** Проверить структуру; если разбиты — ok, documenter в TECH; если случайно — превратить в `.md`.
- **Target:** v1-beta week 1.

### TD-06: inbox-processor по промпту пишет в manager (не в knowledge-synth) — violation hub-and-spoke

- **Source:** inventory gap "Brain объявлен hub-and-spoke но Inbox-processor шлёт Manager'у".
- **Remediation:** Решить: (a) изменить promo на hub-and-spoke via knowledge-synth; (b) принять flat routing. ADR требуется.
- **Target:** v1-beta.

### TD-07: crazy-agent missing mcp__notion (per inventory gap #7)

- **Source:** `crazy-agent.md` frontmatter не содержит mcp__notion, CLAUDE.md говорит должен.
- **Remediation:** Решить: updated roster или updated agent. ADR на основе реального use-case.
- **Target:** v1-beta.

### TD-08: `automations/` пустая папка

- **Source:** ARCHITECTURE-CURRENT — папка есть, contents нет.
- **Remediation:** Удалить (не используется) or document target.
- **Target:** v1-beta first week.

### TD-09: `tools/distribute.py.bak` disabled

- **Source:** CLAUDE.md и ARCHITECTURE-CURRENT.
- **Remediation:** Оставить как есть в v1-beta; re-evaluate в v1-final.

### TD-10: Full formal permission matrix missing

- **Source:** HUMAN §7.2.5
- **Remediation:** v1-final — formal matrix в `shared/schemas/permissions.schema.json`.
- **Target:** v1-final.

### TD-11: `/lint` 7 checks — realized?

- **Source:** skill description mentions 7 checks. ARCHITECTURE-CURRENT не подтверждает реализованы все.
- **Remediation:** Audit `/lint` output; если не все 7 — implement missing.
- **Target:** v1-beta.

### TD-12: Tests — zero fixtures

- **Source:** ADR-017 deferred; inventory — 0 tests.
- **Remediation:** v1-final — создать golden test fixtures для /ingest, /ask.
- **Target:** v1-final.

### TD-13: `shared/state/system-health.json` не auto-populated

- **Source:** §8.8.2 описывает, но реально — нет cron.
- **Remediation:** В v1-beta — manual populate через `/lint` когда Ruslan запускает. В v1-final — automate.

### TD-14: Naming inconsistency: `_moc.md` vs `README.md`

- **Source:** CLAUDE.md упоминает `_moc.md` (Map of Content). wiki/ topics использует hub pages. Конвенция unclear.
- **Remediation:** Decide одно. ADR. Rename all to match.
- **Target:** v1-beta week 2.

## 11.3 Mitigation Priority Matrix

```
             LOW likelihood   MED likelihood   HIGH likelihood
HIGH impact |  R-12          R-01, R-11       R-10
MED impact  |                R-07, R-08       R-02, R-03
LOW impact  |  R-09          R-05, R-06       R-04
```

**Top 3 for immediate attention:**
1. R-10 (bus factor) — document, find backup, enable partial operation without Ruslan.
2. R-01 (Notion SPOF) — execute migration (ADR-010).
3. R-11 (hallucination) — enforce provenance + weekly `/lint` contradictions check.

---

# 12. Glossary

Основные термины. Источник правды для всех документов Jetix OS.

| Term | Definition |
|------|------------|
| **Jetix OS** | Персональная операционная система для управления 6 ресурсами человека через документы + AI агенты. |
| **Central Claude Code (B2)** | Главный Claude-оркестратор, который входит в роли 12 агентов. Primary orchestration hub. |
| **Subagent** | Claude instance, spawn'нутая через Task tool из central Claude. Имеет свой system prompt (из `.claude/agents/{id}.md`), permission mode, maxTurns. |
| **Agent (в Jetix OS)** | Thematic role в system. 12 определений в `.claude/agents/*.md`. Realized через subagent. |
| **Ritual** | Recurring structured workflow: `/plan-day`, `/close-day`, `/weekly-review`, `/monthly-review`, quarterly. |
| **Skill** | Slash-command в `.claude/skills/*.md`. Реализует reusable operation. |
| **Niche** | Тематический срез wiki: `personal/business/sales/life/tech/meta`. 6 closed set. |
| **Wiki (в контексте Jetix OS)** | Knowledge base в `wiki/` по Karpathy LLM Wiki + OmegaWiki модели. 9 entity types, 9 edge types, 4-12 communities. |
| **Entity type** | Один из 9: concept, entity, source, topic, idea, experiment, claim, summary, foundation. |
| **Edge type** | Один из 9: supports, extends, derived_from, contradicts, explains, similar_to, used_by, reverses, part_of. |
| **Community** | Connected component в wiki graph (≥5 pages). |
| **Writeback** | Обратный поток: ответ `/ask` возвращается в wiki (`comparisons/`, edges, claims). |
| **Niche symlink** | `agents/{id}/niche/*` → `wiki/niches/{niche}/`. Cognitive scope marker. |
| **5-layer memory** | Per-agent structure: system.md (Core) / strategies.md (Strategies) / scratchpad.md (Working) / niche/ (Archival) / mailbox.jsonl (Recall). |
| **SAFE-SAVE** | Protocol при любом failure: git commit + push + scratchpad note + chat report. |
| **Semi-manual mode** | v1-beta principle: ничего не автоматизировано, всё по команде Ruslan. |
| **Point A / Point B** | Текущая vs целевая позиция. Применяется к жизни, проектам, задачам. |
| **GitHub-style work** | Projects = main (clean), daily-log drafts = песочница. |
| **Docs-as-code** | All knowledge in git-tracked markdown. |
| **Kay-principle** | "People serious about software make own hardware" → инфраструктура (методология) важнее инструментов (AI). Система работает без AI. |
| **HUMAN / TECH** | Сокращения `SYSTEM-DESIGN-HUMAN.md` / `SYSTEM-DESIGN-TECH.md`. |
| **Inventory (report)** | `reports/architecture-inventory-2026-04-16.md` — findings + gaps of current state. |
| **Фаза α/β/γ/δ** | Stages of Notion decommission (ADR-010). |
| **MCP** | Model Context Protocol. Anthropic standard for tool/resource integration. |
| **L0-L5 layers** | Architectural layers by data type: Raw/Processed/Synthesized/Strategic/Orchestration/Operational. |
| **ADR** | Architecture Decision Record (Michael Nygard format). |
| **ISO 25010** | Software quality model — 8 characteristics used for NFR в §1.1.3. |
| **ISO 42010** | Systems and software engineering — architecture description. Applied meta-framework. |
| **arc42** | Pragmatic architecture documentation template (Starke + Hruschka). Applied template. |
| **HippoRAG** | Retrieval approach using graph edges + community summaries (used by `/ask`). |
| **Daily Log** | `daily-log/YYYY-MM-DD.md` — per-day work log + reflection. |
| **Daily Log draft (песочница)** | `daily-log/drafts/YYYY-MM-DD-{topic}.md` — GitHub-style branch. |
| **Strategy document** | Документ в `strategy/life/` (life-level) or `strategy/projects/{slug}/` (project-level). |
| **Decision** | Record в `decisions/life-decisions-log.md` или `projects/{slug}/decisions.md`. Reusable, чтобы не решать 20 раз. |
| **Hypothesis** | Запись в `hypotheses/{active,backlog,validated-archive}.md`. Testable. |
| **Натягивание** | Cross-analysis: "apply all hypotheses × one project" weekly/monthly. Compounding mechanism. |
| **CRM (Jetix context)** | Три базы: `crm/clients.md`, `crm/partners.md`, `crm/personal.md`. |
| **Ресурс (resource)** | Один из 6 типов: информация, время, финансы, связи, внешние обстоятельства, инструменты. |
| **Priority meta-function** | Cross-resource operation "отделять важное от неважного". |
| **ICP** | Ideal Customer Profile. Sales domain. |
| **$50K goal** | $50,000 revenue до 30.06.2026 — primary business goal. |
| **Фаза β (миграции)** | Extract Notion Daily Log + Projects + Journal + Банк идей → raw/ dumps. |
| **Фаза δ (миграции)** | Cutover: Notion read-only. wiki/ — canonical. |
| **Antigravity** | VS Code fork IDE used by Ruslan. |
| **Server (100.99.156.28)** | VPS Ubuntu 24 where tmux session `jetix` lives. |
| **Partner (Jetix Club)** | One of 5-10 (early) / 100+ (year) invited ambitious collaborators. |

---

# APPENDIX A — AGENT-PROTOCOLS.md (draft)

> Подробные протоколы для 14 агентов (12 core + 2 utility). Каждый агент: activation triggers, session start procedure, workflow, escalation, writing scope, example message formats.

## A.1 Общие протоколы для всех агентов

### A.1.1 Session start (mandatory для всех)

При spawn'е через Task tool, агент **обязан**:

1. Read `agents/{id}/system.md` — own role.
2. Read `agents/{id}/strategies.md` — learned behaviors.
3. Read `agents/{id}/scratchpad.md` — resume state (если есть).
4. Read `comms/mailboxes/{id}.jsonl` last 10 messages (unread только).
5. Read relevant `shared/state/` files (depends on task).
6. **Then** start processing the task prompt.

### A.1.2 Session end (mandatory)

1. Append to `scratchpad.md`: "Завершил X в YYYY-MM-DD HH:MM. State: Y. Next: Z." (если предполагается continuation).
2. If new knowledge: append `strategies.md` entry (pattern: "When X, do Y. Rationale: Z.").
3. If messages to others: write to target mailbox(es).
4. If artifacts produced: ensure они committed (trigger commit if parent agent).
5. Return structured report to parent (or to Ruslan if central).

### A.1.3 Escalation (v1-beta — simplified)

**Direct-to-Ruslan через `comms/mailboxes/human.jsonl`:**

```jsonl
{"id":"msg-20260418-005","from":"sales-researcher","to":"human","type":"escalation","priority":"high","status":"open","subject":"API Tier 2 partner research — ambiguous ICP criteria","payload":"Found 3 candidates matching broad criteria. Tighter criteria needed: (a) company size, (b) region, (c) tech stack.","ts":"2026-04-18T15:22:00Z"}
```

**v1-final plan:** субагенты → lead → manager → human (hub-and-spoke), с SLA.

### A.1.4 Forbidden actions (ВСЕ агенты)

- Писать в `.env`, `private/*`, `~/.ssh/`, `config/*.secret.*`, `.github/workflows/*`.
- Выполнять `git push --force`, `git reset --hard`, `git rebase main`.
- Удалять файлы из `raw/*` (immutable).
- Совершать financial transactions (ни при каких обстоятельствах).
- Публиковать external communication (social posts, client emails) без explicit Ruslan approval.
- WebFetch / WebSearch в автономном режиме (только по команде).

### A.1.5 Message format (canonical)

```json
{
  "id": "msg-YYYYMMDD-NNN",
  "from": "agent-id",
  "to": "agent-id | human",
  "type": "report | request | escalation | handoff | fyi | question | approval | reject",
  "priority": "low | normal | high | urgent",
  "status": "open | in-progress | done | blocked | cancelled",
  "subject": "short title",
  "payload": "content OR short description",
  "payload_ref": "path/to/full-artifact.md (optional)",
  "thread_id": "optional parent message id",
  "ts": "ISO 8601 timestamp"
}
```

## A.2 Manager (MGMT Lead)

| Field | Value |
|-------|-------|
| **Trigger** | Morning/evening pipeline; inter-department coordination request; status update inquiry |
| **First reads** | own mailbox, `shared/state/focus.json`, `shared/state/active-projects.json`, `shared/state/priorities.json`, Daily Log (if Notion available) |
| **Workflow** | (1) assess state → (2) identify gaps → (3) delegate to department leads via their mailboxes → (4) synthesize replies → (5) report to Ruslan |
| **Escalates to** | Ruslan (human) |
| **Writes to** | `shared/state/*.json`, `reports/coordination-YYYY-MM-DD.md`, own scratchpad |
| **Example delegation** | `{to: "sales-lead", type: "request", subject: "Pipeline status + blocker list for weekly review", priority: "normal"}` |

## A.3 Personal-Assistant (OPS)

| Field | Value |
|-------|-------|
| **Trigger** | Draft messages (RU/EN/DE); quick info lookup; translation; calendar |
| **First reads** | own mailbox, `daily-log/{today}.md` (context), personal niche |
| **Workflow** | (1) clarify request → (2) produce draft → (3) Ruslan reviews → (4) (if approved) send/post |
| **Escalates to** | Ruslan (always, for external comms) |
| **Writes to** | `out-drafts/` (staging), `daily-log/drafts/` |

## A.4 System-Admin (OPS)

| Field | Value |
|-------|-------|
| **Trigger** | Server monitoring; script creation; MCP setup; git operations; infra changes |
| **First reads** | own mailbox, `shared/state/system-health.json`, `scripts/`, `tools/` |
| **Workflow** | (1) diagnose → (2) propose fix → (3) Ruslan approves → (4) execute → (5) verify |
| **Escalates to** | Ruslan (when destructive op needed) |
| **Writes to** | `scripts/`, `tools/`, `.claude/`, `reports/system-admin-YYYY-MM-DD.md` |
| **Forbidden** | No network (no web_search); Bash yes, but limited to non-destructive commands without approval |

## A.5 Sales-Lead

| Field | Value |
|-------|-------|
| **Trigger** | Sales strategy; offer design; pipeline analysis; sales call prep |
| **First reads** | own mailbox, `projects/quick-money/overview.md`, `crm/*.md`, `strategy/projects/sales/` |
| **Workflow** | (1) pipeline state → (2) decide next move → (3) delegate research to sales-researcher (mailbox) → (4) delegate outreach to sales-outreach → (5) synthesize → (6) report to Manager/Ruslan |
| **Escalates to** | Manager (routine) / Ruslan (pricing, contract decisions) |
| **Writes to** | `crm/clients.md`, `projects/{sales}/log.md`, `shared/knowledge/research-summaries/` |

## A.6 Sales-Researcher

| Field | Value |
|-------|-------|
| **Trigger** | Prospect research; market segment analysis; competitor mapping; community platform mapping |
| **First reads** | own mailbox, `crm/partners.md`, ICP criteria (strategy or wiki) |
| **Workflow** | (1) clarify ICP → (2) web_search → (3) structure results → (4) save to `shared/knowledge/research-summaries/` → (5) report to sales-lead |
| **Escalates to** | Sales-lead only (per hub-and-spoke) |
| **Writes to** | `shared/knowledge/research-summaries/`, `crm/partners.md` (adds candidates only, with `status: candidate`) |

## A.7 Sales-Outreach

| Field | Value |
|-------|-------|
| **Trigger** | Drafting LinkedIn messages, email, DM outreach; community engagement content; follow-up sequences |
| **First reads** | own mailbox, `crm/partners.md`, latest research in `shared/knowledge/research-summaries/` |
| **Workflow** | (1) pick target from CRM → (2) draft message (tone, context-aware) → (3) save in `out-drafts/` → (4) report to sales-lead → (5) **Ruslan approves before actual send** |
| **Escalates to** | Sales-lead |
| **Writes to** | `out-drafts/`, `crm/` (appends interaction only) |

## A.8 Knowledge-Synth (Brain Lead)

| Field | Value |
|-------|-------|
| **Trigger** | Multi-source synthesis; Research Hub updates; comprehensive analysis |
| **First reads** | own mailbox, relevant wiki topics, `shared/knowledge/research-summaries/` |
| **Workflow** | (1) intake sources → (2) extract claims → (3) check contradictions → (4) synthesize summary → (5) write to `wiki/summaries/` or `wiki/concepts/` → (6) update Research Hub (if Notion active) |
| **Escalates to** | Manager (coordination), Strategist (strategic implication) |
| **Writes to** | `wiki/` (all entity types), `shared/knowledge/`, Research Hub Notion |

## A.9 Inbox-Processor (Brain)

| Field | Value |
|-------|-------|
| **Trigger** | Voice memos need structuring; Telegram/email inbox needs processing; unstructured notes |
| **First reads** | own mailbox, `inbox/*`, `raw/voice-memos/` (if transcribed) |
| **Workflow** | (1) read unprocessed items → (2) classify (project / idea / task / reference / skip) → (3) route: project items → `projects/{x}/` or ideas → `wiki/ideas/`, tasks → `tasks/master.md` → (4) move processed to `inbox/processed/` |
| **Escalates to** | Knowledge-synth (when synthesis needed) OR Manager (when coordination) |
| **Writes to** | `wiki/ideas/`, `tasks/master.md`, `inbox/processed/`, `projects/{x}/ideas.md` |
| **Note:** inventory TD-06 — по промпту пишет to Manager, не knowledge-synth. Решение ADR нужно. |

## A.10 Meta-Agent (Meta, plan mode)

| Field | Value |
|-------|-------|
| **Trigger** | Weekly/monthly system review; agent performance analysis; prompt improvement proposal; architecture evaluation |
| **First reads** | own mailbox, `reports/`, `shared/state/metrics/`, all 12 agents' strategies.md |
| **Workflow** | (1) sample recent agent outputs → (2) identify patterns (good and bad) → (3) draft `reports/audits/YYYY-MM-DD.md` → (4) propose `strategies.md` additions for specific agents → (5) report to Manager |
| **Escalates to** | Manager (which routes to Ruslan for approval) |
| **Writes to** | `reports/audits/`, `shared/state/metrics/ab-tests.json` (proposals only) |
| **permissionMode** | plan — **writes plans only, не outwithly implements** |

## A.11 Crazy-Agent (Meta)

| Field | Value |
|-------|-------|
| **Trigger** | Stuck problem; weekly creative brainstorm; cross-domain connection needed; "what if" thinking |
| **First reads** | own mailbox, `wiki/ideas/`, `wiki/summaries/`, recent daily-log |
| **Workflow** | (1) input context → (2) generate 5-10 wild ideas (не filtering!) → (3) rank by plausibility → (4) write top 3 to `shared/knowledge/crazy-ideas/` and `wiki/ideas/` → (5) report to requester |
| **Escalates to** | Manager |
| **Writes to** | `wiki/ideas/`, `shared/knowledge/crazy-ideas/` |
| **Note:** TD-07 — missing mcp__notion per inventory gap. Needs resolution. |

## A.12 Life-Coach (Life)

| Field | Value |
|-------|-------|
| **Trigger** | Workout/nutrition planning; energy management; habit tracking analysis; sleep/recovery; day type = "recovery" |
| **First reads** | own mailbox, `health/habits-tracker.md`, `health/log.md`, recent `daily-log/*.md` |
| **Workflow** | (1) audit recent state → (2) identify patterns → (3) propose actions (workout plan, habit adjustment) → (4) report to Ruslan |
| **Escalates to** | Manager (rare) / Ruslan (direct) |
| **Writes to** | `health/`, `reflection/`, Life OS (if Notion active) |

## A.13 Strategist (MGMT, plan mode)

| Field | Value |
|-------|-------|
| **Trigger** | Decisions with >1 month consequence; cross-project trade-off; new direction considered; quarterly review |
| **First reads** | own mailbox, `strategy/life/`, `strategy/projects/*/`, `decisions/life-decisions-log.md`, recent `reports/audits/` |
| **Workflow** | (1) frame decision → (2) enumerate alternatives → (3) evaluate trade-offs → (4) write proposal to `shared/knowledge/decisions-log.jsonl` → (5) draft ADR if warranted → (6) **plan mode**: report to Ruslan for approval |
| **Escalates to** | Ruslan (every decision — requires approval) |
| **Writes to** | `shared/knowledge/decisions-log.jsonl`, `strategy/` drafts (plan mode — as proposals), potential `docs/adr/NNN-*.md` drafts |
| **permissionMode** | plan |

## A.14 Staging-Writer (utility)

| Field | Value |
|-------|-------|
| **Trigger** | Section writing для `design/SYSTEM-DESIGN-INPUTS.md` |
| **First reads** | specified wiki pages + Notion pages assigned; current `SYSTEM-DESIGN-INPUTS.md` |
| **Workflow** | (1) gather sources → (2) extract thesеs per part → (3) write section with attribution → (4) commit |
| **Writes to** | `design/SYSTEM-DESIGN-INPUTS.md` |

## A.15 Sweep-Worker (utility)

| Field | Value |
|-------|-------|
| **Trigger** | batch ingest of Notion Bank of Ideas (during Фаза γ) |
| **First reads** | batch assignment (idea IDs), existing `raw/notion-ideas/` for dedup |
| **Workflow** | (1) fetch each idea via `mcp__notion-fetch` → (2) classify RELEVANT/IRRELEVANT/UNCLEAR по system-design criteria → (3) if RELEVANT → `/ingest` → wiki/ → (4) write batch report → (5) return summary |
| **Writes to** | `wiki/`, `reports/sweep-batch-YYYY-MM-DD.md` |
| **Idempotency:** skip ideas already в `raw/notion-ideas/` |

## A.16 SAFE-SAVE protocol (detailed)

```
IF trigger ∈ {unhandled exception, external dep down, agent confused,
             git conflict, context overflow, Ruslan offline + uncertainty}:

  1. In-memory: summarize current state to string S.

  2. Filesystem writes:
     a. Append to agents/{id}/scratchpad.md:
        ```
        ## SAFE-SAVE at YYYY-MM-DD HH:MM:SS
        Trigger: {trigger}
        State: {S}
        Completed: {list}
        Remaining: {list}
        Proposed next: {suggestion}
        ```

  3. Git operations (sequential):
     a. `git add -A`
     b. `git commit -m "[{id}] SAFE-SAVE: {short reason}"`
        - If pre-commit hook fails: fix the issue (e.g., lint error),
          re-stage, new commit. Never `--no-verify`.
     c. `git push origin main`
        - If push fails (network): note "push pending" in scratchpad.
        - If push fails (conflict): halt. Do not force.

  4. Notification:
     a. If subagent: return structured report to parent Claude.
     b. If central Claude: write to `comms/mailboxes/human.jsonl`
        and output message in chat.

  5. Stop. Do not continue to "guess" resolution.
```

## A.17 Handoff protocol (inter-agent)

When Agent A's work must continue by Agent B:

1. A writes artifact to shared location (e.g., `shared/knowledge/research-summaries/icp-2026-04-18.md`).
2. A writes handoff message:
   ```jsonl
   {"id":"msg-...","from":"A","to":"B","type":"handoff","subject":"ICP batch ready for synthesis","payload_ref":"shared/knowledge/research-summaries/icp-2026-04-18.md","thread_id":"msg-prev-...",...}
   ```
3. B on next session start: reads mailbox, sees handoff, processes.

**Invariant:** handoff message **always** includes `payload_ref`.

---

# APPENDIX B — DATA-FLOWS.md (draft)

> Пять канонических потоков. Каждый: input spec → transformation steps → output spec → failure modes. Формат arc42 Runtime View extensions.

## B.1 Flow: Voice-Memo → Wiki

### Input
- File: `raw/voice-memos/YYYY-MM-DD-HHMMSS.ogg`
- Format: OGG Opus, typical 10-40 MB, 1-60 min duration.

### Steps
```
raw/voice-memos/*.ogg
    │
    │ (tools/transcribe.py — Groq Whisper)
    ▼
raw/transcripts/YYYY-MM-DD-HHMMSS.txt  (UTF-8, russian mostly)
    │
    │ (tools/extract.py — Claude)
    ▼
Structured items (JSON in memory)
  {
    decisions: [...],
    tasks: [...],
    ideas: [...],
    contacts: [...],
    insights: [...]
  }
    │
    │ (tools/filter.py — dedup + meta-analysis)
    ▼
Filtered items
    │
    │ (tools/review_report.py)
    ▼
reports/review_YYYY-MM-DD.md  (human review gate)
    │
    │ ← STOP: Ruslan reviews, decides
    │
    │ (manual /ingest or distribute)
    ▼
wiki/ideas/, wiki/sources/, projects/*/tasks.md, crm/*, decisions/
```

### Output
- One or more `wiki/` pages (depending on review).
- Items routed to projects/tasks/CRM/decisions per Ruslan's review.
- Voice file remains in `raw/` (immutable).

### Failure modes
- **Transcription timeout:** Retry once; if fails — item stays unprocessed; Ruslan notified.
- **Extract returns malformed JSON:** filter.py safely drops bad records, logs.
- **Review report generation fails:** partial report saved + error note.

### Metrics (v1-final)
- Voice-to-transcript latency < 30s for 10-min memo.
- Extract precision ≥80% (Ruslan reviews, measures subjectively).

## B.2 Flow: External Content → Wiki (Ingest)

### Input
- URL or path to file (`raw/articles/`, `raw/web/`).

### Steps
```
URL / file path
    │
    │ (WebFetch or Read)
    ▼
Raw content (HTML, markdown, plain text)
    │
    │ (persist to raw/web/ if URL)
    │
    ▼
raw/web/YYYY-MM-DD-{slug}.md
    │
    │ (LLM pass: identify entities, claims, ideas, concepts)
    ▼
Structured extraction
  {
    entities: [...],
    claims: [{text, evidence, source}],
    ideas: [...],
    topics: [...],
    niches: [...]
  }
    │
    │ (for each: template-based write to wiki/)
    ▼
wiki/sources/YYYY-MM-DD-{slug}.md  (citation)
wiki/concepts/{x}.md or wiki/ideas/{x}.md or wiki/claims/{x}.md (per type)
wiki/graph/edges.jsonl  (append new edges)
wiki/index.md  (append new entries)
wiki/log.md  (append ingest event)
wiki/niches/{niche}/README.md  (update backlinks)
    │
    │ (git commit + push)
    ▼
Committed in main.
```

### Output
- 1 source page + N entity pages + M edges + log entry.
- Report in chat: "N pages created/updated, M edges, niche: {...}".

### Failure modes
- **Fetch 404:** report, halt.
- **LLM can't parse:** fallback to source-only page + claim: "needs manual extraction".
- **Duplicate detection:** merge inline + notice; if ambiguous → suggest `/consolidate`.
- **Git push fail:** SAFE-SAVE, note pending.

## B.3 Flow: Query & Writeback (/ask)

### Input
- Natural language question.

### Steps
```
/ask <question>
    │
    │ (read wiki/index.md)
    ▼
Page catalog (type, title, path)
    │
    │ (read wiki/graph/summaries.md)
    ▼
Community digests (top-level understanding)
    │
    │ (LLM: pick 5-15 pages relevant)
    ▼
Page selection
    │
    │ (read selected pages)
    ▼
Full content
    │
    │ (LLM: synthesize answer with inline citations [[page]])
    ▼
Answer draft
    │
    │ (quality gate: is this writeback-worthy?)
    │    ├─ YES: new connection / contradiction / synthesis / practical insight
    │    └─ NO: just response
    │
    ├─────(YES branch)─────→
    │                      │
    │                      ▼
    │         wiki/comparisons/YYYY-MM-DD-{slug}.md  (answer + citations)
    │         wiki/graph/edges.jsonl  (new edges)
    │         wiki/index.md  (append)
    │         wiki/log.md  (append)
    │         git commit + push
    │                      │
    ▼                      ▼
Response to Ruslan (with "saved to comparisons/" note if YES)
```

### Output
- Chat response with citations.
- Optional `comparisons/` entry.

### Failure modes
- **Vague question:** Claude asks clarification.
- **No relevant pages:** "No wiki support; proceed with uncited opinion? y/n"
- **Rate limit:** partial answer + SAFE-SAVE.

## B.4 Flow: Close-Day (Ritual)

### Input
- User invocation `/close-day`.
- `daily-log/{today}.md` (possibly with drafts).
- `daily-log/drafts/{today}-{topic}.md` (песочницы).

### Steps
```
/close-day
    │
    │ (read daily-log/{today}.md and drafts/)
    ▼
Today's work snapshot
    │
    │ (Ask Ruslan 4 questions:
    │   1. What done?
    │   2. Insights?
    │   3. Energy 1-5?
    │   4. Tomorrow priorities?)
    ▼
Answers
    │
    │ (process drafts — identify artifact candidates)
    │
    ├────→ insights → wiki/ideas/ drafts (Ruslan approves)
    ├────→ tasks → tasks/master.md or projects/{p}/tasks.md
    ├────→ contacts → crm/{type}.md
    ├────→ decisions → decisions/...
    └────→ energy/state → health/log.md (via life-coach if needed)
    │
    │ (update focus.json for tomorrow)
    ▼
shared/state/focus.json
    │
    │ (if Notion active) mcp__notion-update-page (Daily Log DB)
    ▼
Notion updated
    │
    │ (git commit + push)
    ▼
Committed: "[daily] close: {today} — {focus}"
```

### Output
- Completed `daily-log/{today}.md`.
- Artifact routing to appropriate folders.
- Focus.json refreshed.
- Notion sync (while Фаза < δ).

### Failure modes
- **Ruslan in a hurry:** ok, Claude accepts minimum (energy only).
- **No drafts, empty day:** Claude records "low-activity day".
- **Notion MCP down:** SAFE-SAVE, mark "notion sync pending" in frontmatter.

## B.5 Flow: Notion Migration (α/β/γ/δ)

### Input (per phase)
- Phase α: 11 self-description Notion pages.
- Phase β: Daily Log DB + Projects DB + Journal of Chats + Life OS.
- Phase γ: Банк идей (650+ items).
- Phase δ: cutover.

### Steps (general)
```
Phase N start
    │
    │ (list target IDs)
    ▼
Batch list
    │
    │ (for each: mcp__notion-fetch)
    ▼
raw/notion-pages/{id}.md  OR  raw/notion-ideas/{id}.md
    │
    │ (classify RELEVANT/IRRELEVANT/UNCLEAR — via sweep-worker for bulk)
    ▼
Classification
    │
    ├──(RELEVANT)──→ /ingest → wiki/
    ├──(IRRELEVANT)──→ skip (only raw dump kept)
    └──(UNCLEAR)──→ report to Ruslan for manual review
    │
    │ (generate batch report)
    ▼
reports/notion-{phase}-extraction-YYYY-MM-DD.md
    │
    │ (git commit + push)
    ▼
Committed per batch.

Phase δ specific:
    │
    │ (all critical data validated in wiki/)
    ▼
    │ (Notion DB permissions → read-only)
    │ (Update CLAUDE.md: remove critical path references)
    ▼
Cutover complete.
```

### Output
- `raw/notion-*` — complete archive.
- `wiki/` — populated with RELEVANT content.
- Batch reports in `reports/`.

### Failure modes
- **MCP down mid-batch:** SAFE-SAVE batch state (which IDs done), Ruslan resumes later.
- **Unclear items pile up:** escalation to Ruslan queue.
- **Rate limit Notion:** backoff + retry; if persistent — pause batch.

## B.6 Flow annotations (cross-cutting)

All flows share:

- **Provenance enforcement:** every wiki/ page resulting from an ingest carries `sources:` frontmatter.
- **Idempotency:** all ingest operations dedup by slug/hash.
- **Append-only logs:** each flow appends to `wiki/log.md`.
- **SAFE-SAVE on failure:** see APPENDIX A §A.16.
- **Git discipline:** every completed sub-step — commit; every flow end — push.

---

# APPENDIX C — ARCHITECTURE-TARGET.md (draft)

> Целевое состояние (v1-beta → v1-final → v2). Контраст с `ARCHITECTURE-CURRENT.md` (2026-04-16).

## C.1 Три снимка

| Aspect | CURRENT (2026-04-16) | v1-beta TARGET (2026-04-18+) | v1-final TARGET (~2026-06) |
|--------|----------------------|-------------------------------|-----------------------------|
| Knowledge Store | wiki/ 557 pages, 572 edges, 4 communities; knowledge-base/ legacy 0% migrated | wiki/ + `/ingest` от Notion Фазы γ; wiki/ grows к 800-1000 pages | wiki/ 1500-2000 pages; legacy кластеры (sales, _health) перенесены; 8-12 communities |
| Agents active | 12 defined; 6 mailboxes empty; strategies.md all empty | 12 defined; ≥10 mailboxes active with productive msgs; 5+ strategies.md filled | 12+ defined; metrics tracked; A/B tests ≥10 runs |
| Notion coupling | Primary for Daily Log, Projects, Life OS, Research Hub, Банк идей, ICP | Фаза γ in progress; Notion still active but wiki becoming source | Фаза δ complete; Notion read-only |
| Skills | `/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph`, `/plan-day`, `/close-day`, `/focus`, legacy `/compile`, `/search-kb`, `/sweep-notion-bank` | Same + `/weekly-review`, `/monthly-review` | + automation subset; event-driven где разумно |
| Automation | None reliable (morning/evening pipelines exist but no cron) | None (semi-manual as ADR-005) | Selective cron for non-critical (nightly /lint, weekly /build-graph) |
| Dashboard | React+Express exists, used opportunistically | Same (not critical path) | Either supported or deprecated (decision in v1-final) |
| `baseline.md` | Exists, identical to system.md | Kept (transition) | Deleted (ADR-013) |
| Tests | 0 | 0 | Golden fixtures for `/ingest`, `/ask` |
| Deployment | Single VPS + laptop | Same | + off-site backup (rsync) |
| Team size | 1 (Ruslan) | 1 + 5-10 Club partners (feedback) | 1 + 3-5 specialists (engineers/philosophers) |

## C.2 Что меняется между v1-beta и v1-final

### Changes
- **Notion decommission (Фаза γ → δ):** Банк идей fully migrated; Daily Log moves to `daily-log/*` as primary.
- **Activated agent loops:** Strategies.md accumulate (System Prompt Learning). Meta-agent weekly actually runs with Ruslan-approval loop.
- **Tests:** golden fixtures.
- **Formal ADR log:** `docs/adr/0001-*.md` created, all ADRs from §9 migrated.
- **Permission matrix:** `shared/schemas/permissions.schema.json` formalized.
- **Automation:** weekly `/lint`, weekly `/build-graph`, monthly meta-agent — cron'd.
- **Hub-and-spoke:** enforced (inbox-processor fixed).

### Stays
- Markdown + git + Obsidian.
- 12 agents roster (though may refine composition).
- Karpathy wiki model.
- Kay-principle (works without AI).
- Single-tenant.

### Deprecated/Removed
- `baseline.md` (ADR-013).
- `distribute.py.bak` (if no re-enable rationale).
- Legacy `/compile`, `/search-kb`.
- Notion critical path dependencies.

## C.3 Что меняется между v1-final и v2

### Changes
- **Multi-tenant capability:** Jetix Club partners потенциально получают restricted access.
- **Client-facing layer:** v1/v2 introduces client portal/API.
- **Team collaboration:** multi-user git workflow.
- **Product extraction:** Jetix Corporation layer (separate repo?) spin-off.
- **Formal testing:** CI/CD pipeline.
- **Cost optimization:** automated model-tier routing based on task classification.

## C.4 Migration Timeline (Concrete Milestones)

| Date | Milestone | Deliverables |
|------|-----------|--------------|
| 2026-04-18 | v1-beta release | SYSTEM-DESIGN-HUMAN v1-beta ✅; this TECH via 5-chat review |
| 2026-04-25 | Фаза β launch | Daily Log + Projects DB extracted to raw/ |
| 2026-05-02 | Фаза γ launch | `/sweep-notion-bank` execute на 650 ideas в batches of 50 |
| 2026-05-16 | Фаза γ complete | wiki/ >1000 pages, communities rebuilt |
| 2026-05-30 | Фаза δ cutover | Notion read-only; wiki canonical |
| 2026-06-15 | v1-final technical doc | SYSTEM-DESIGN-TECH.md synthesized |
| 2026-06-30 | **$50K goal checkpoint** | Business milestone; system evaluated |
| 2026-Q3 | v1-final stabilization | Tests, formal ADR log, automation subset |
| 2026-Q4 | v2 planning | Multi-tenant, client-facing, team prep |

## C.5 Risks specific to migration

| Risk | Phase | Mitigation |
|------|-------|------------|
| Notion MCP permanently breaking mid-migration | β, γ | raw/ dumps made early; manual export fallback |
| Sweep-worker producing low-quality ingest | γ | Sample review by Ruslan after each batch |
| Community rebuild after big ingest takes too long | γ | Incremental `/build-graph` between batches |
| Cutover (δ) data gap | δ | 1-week parallel operation before flip |
| Team onboarding ambiguity | v1-final | SYSTEM-DESIGN-TECH as core doc; buddy system for first week |

## C.6 Success Criteria для v1-beta → v1-final transition

- [ ] Документ (this one after synthesis) активно используется ≥2 недели.
- [ ] 5+ частей SYSTEM-DESIGN-HUMAN получили реальные правки.
- [ ] 5+ strategies.md заполнены productive entries.
- [ ] ≥50% open TDs in §11.2 closed.
- [ ] Фаза γ completed.
- [ ] Ruslan говорит: "ок, к v1-final".

---

# Closing Notes from Engineer A

## Summary of Key Architectural Choices

1. **12 agents as roles, not processes** (ADR-002). Минимизирует инфра.
2. **Docs-as-code everything** (ADR-001, ADR-003). Vendor-lock immune.
3. **Karpathy wiki over vector RAG** (ADR-006). Debuggable, compose'able.
4. **Semi-manual in v1-beta** (ADR-005). Safety first.
5. **File-based messaging** (ADR-007). Git-trackable.
6. **Niche via symlinks** (ADR-008). Cognitive, not enforcement.
7. **Multi-chat review** for this very document (ADR-011).

## Points of Disagreement Anticipated (vs Engineer B)

- **Event-driven vs command-driven.** Engineer B (C4 / event-driven) likely will propose more event-based primitives (inbox-watch, auto-ingest). Engineer A says: **not в v1-beta**, per ADR-005.
- **Permission model formality.** Engineer B may push formal. Engineer A: prompt-rules достаточно для single-user.
- **Database vs filesystem.** Engineer B may suggest SQLite for state. Engineer A: markdown + JSON + git лучше для portability (Q2).
- **Agent count.** Engineer B may propose fewer agents. Engineer A keeps 12 per ADR-004 (departmental growth).

**Synthesizer (Chat 5) should explicitly reconcile these.** Where synthesis chooses Engineer B's path — document why. Where это, document too.

## What's Deferred Intentionally

Beta-first applies. These are **known good ideas**, intentionally **not** в v1-beta:

- Formal permission matrix.
- Full ADR log (`docs/adr/NNNN-*.md`) — on v1-final.
- Golden test fixtures.
- Cron automation.
- Client-facing API.
- Multi-tenant.
- Formal SLA definitions.
- TLA+ or similar formal methods.

## Reading Order for Future Claude Code

1. **CLAUDE.md** (5 min) — quick config.
2. **SYSTEM-DESIGN-HUMAN.md §Meta + Часть 1-2** (15 min) — business frame.
3. **This document §1-4** (15 min) — requirements, constraints, strategy.
4. **This document §5** (20 min) — building blocks.
5. **This document §6** (skim, 10 min) — runtime scenarios.
6. **APPENDIX A** (15 min) — agent-specific protocols.
7. Задача-specific deep dives as needed.

Total onboarding: ~90 min to productive contribution.

## Final Invariant

> **Jetix OS works even without AI.**
> (Kay-principle, inherited from HUMAN §3.5.2.)
>
> If all AI providers become unavailable, Ruslan can sit down at his laptop,
> open markdown files, edit, commit, push. The methodology persists.
> This is the most important architectural property and must be preserved
> across all future decisions.

---

*End of SYSTEM-DESIGN-TECH draft (Engineer A, arc42). Total ~2500+ lines. Submit to Synthesizer (Chat 5).*
