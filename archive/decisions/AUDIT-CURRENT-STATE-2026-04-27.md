---
title: AUDIT — Current State Snapshot Jetix OS
date: 2026-04-27
type: audit
purpose: Pure inventory snapshot before Sub-stage 1.2 (Vision Doc) и Sub-stage 1.3 (Master Plan). НЕ interpretation, НЕ improvements proposals. Только "что есть RIGHT NOW".
sub_stage: 1.1 of Этап 1 (Architecture) of Генеральная чистка
related_docs: see Notion subpage 🏗️ Генеральная чистка
authoritative: false
status: snapshot
status: archived
archived_at: 2026-05-06
archived_reason: Pre-Foundation snapshot — superseded
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# AUDIT — Current State Snapshot Jetix OS (27.04.2026)

## §0 TL;DR

Это pure inventory snapshot системы Jetix OS на момент 26-27.04.2026 — без оценок, без proposals, без judgment. Цель — зафиксировать "что есть RIGHT NOW" как baseline для Sub-stage 1.2 (Vision Doc Руслана) и Sub-stage 1.3 (ROY Master Plan).

**Что мы имеем в виде системы (на человеческом языке):**

Jetix OS — это git-репозиторий-как-операционная-система примерно на 38 000 файлов и ~750 MB, физически расположенный в `/home/ruslan/jetix-os/`. Внутри — multi-agent swarm с 20 агент-каталогами, 28 Claude Code skills, две главные подсистемы знаний (wiki/ — 552 entity-файла + CRM с 4 контактами и 35 unit-tests), и большой архив стратегических документов (44 файла на ~600 000 слов в `decisions/`). Phase 2 архитектурной разработки технически закрыта — три "must" deep-dive (LAYER-5 Product / LAYER-6 Community / LAYER-7 Business) acked. Воспрос-конвейер (voice-pipeline) только что мигрировал на Claude Code headless (cycle 11, 26.04) и больше не требует прямого ANTHROPIC_API_KEY. CRM-система собрана и протестирована (cycle 10, 26.04). Активные cycle-10 и cycle-11 находятся в AWAITING-APPROVAL.

**Стратегический корпус** — это 6 strategic insights (M&A / Arbitrage Traffic / AI-BIOS-moment / AI-Psy-Led / Korp-Startup / etc), 3 layer deep-dive (L5/L6/L7), 5 architecture variants (V1-V5), 30 locks (D1-D30), и фундаментальные документы (JETIX-VISION / PHILOSOPHY / PLAN / ARCHITECTURE-BRIEF / SYSTEM-OVERVIEW). Общий объём чтения для нового человека, входящего в систему — порядка 600K слов (~1500 страниц A4) только в `decisions/`.

**Git-активность** очень высокая: 571 коммит за последние 30 дней, 406 за последние 7 дней — то есть система ежедневно обновляется. Активный branch — `claude/jolly-margulis-915d34` (рабочая ветка Cloud Cowork сессии). Два главных author: Ruslan (302 коммита за 90 дней) и Bogersebekov (269 коммитов).

**Pipeline статус:** voice-pipeline работает на Max-подписке через CC headless (cycle 11 done); CRM работает на филесистеме как single source of truth (cycle 10 done); wiki v3 работает с 9 entity типами + 8 наблюдённых типов рёбер в графе.

---

## §1 Repo structure

### 1.1 Top-level directories (33 каталога)

| Каталог | Что внутри (1 строка) | Файлов | Размер |
|---------|----------------------|--------|--------|
| `agents/` | Multi-agent swarm: 20 agent-каталогов с system.md / strategies.md / scratchpad.md / niche/ | 79 | 592 K |
| `clients/` | Demo client конфиги для swarm integration | 6 | 60 K |
| `comms/` | Agent communication: broadcast/ + mailboxes/*.jsonl | 16 | 36 K |
| `config/` | Корневые конфиги: context.md, profile.md, decisions.json, projects.json | 4 | 28 K |
| `crm/` | CRM подсистема: people/orgs/_schema/_scripts/_tests/_templates/views | 47 | 420 K |
| `daily-log/` | Ежедневные логи (минимально заполнено) | 1 | 8 K |
| `dashboard/` | React/Vite веб-дашборд (TS, Tailwind) — преимущественно node_modules | 34 170 | 503 M |
| `decisions/` | Стратегические решения и architecture variants (44 файла) | 45 | 3.2 M |
| `design/` | Документация системного дизайна (17 файлов) | 18 | 1.5 M |
| `directions/` | Активные направления (ai-consulting-dach, producer-services) | 2 | 344 K |
| `docs/` | Legacy архитектурные документы и ADR-фреймворк | 2 | 84 K |
| `health/` | Health/wellness журнал | 2 | 12 K |
| `hypotheses/` | Активные / backlog / validated гипотезы | 3 | 16 K |
| `ideas/`, `ideas-pool/` | Банк идей | 2 | 24 K |
| `inbox/` | Voice processing + content extraction | 160 | 4.6 M |
| `knowledge-base/` | Legacy KB (в миграции на wiki/) — 9 статей по AI-консалтингу | 9 | 88 K |
| `_meta/` | Конвенции репо | 2 | 20 K |
| `private/` | Защищённый каталог (пустой) | 0 | 16 K |
| `projects/` | Project tracking | 21 | 140 K |
| `prompts/` | Системные промпты и инструкции агентов (130 файлов) | 130 | 2.7 M |
| `raw/` | Сырые данные: research / transcripts / voice-memos / books-md / notion-ideas | 1 222 | 212 M |
| `reflection/` | Рефлексия и обучение | 2 | 12 K |
| `reports/` | Стратегические отчёты + voice review reports (21 файл) | 21 | 1.7 M |
| `reviews/` | PR / code reviews | 5 | 460 K |
| `scripts/` | Утилитарные скрипты | 6 | 28 K |
| `shared/` | Shared state + schemas | 17 | 72 K |
| `strategy/` | Стратегические документы | 2 | 16 K |
| `swarm/` | Swarm orchestration: wiki/, awaiting-approval/, logs/ (308 файлов) | 308 | 6.8 M |
| `tasks/` | Tasks tracking | 2 | 24 K |
| `templates/` | Reusable templates | 16 | 68 K |
| `tmp/` | Временные рабочие файлы | 18 | 2.0 M |
| `tools/` | Voice-pipeline + Python utilities (93 файла) | 93 | 1.8 M |
| `tools-catalog/` | Каталог инструментов | 1 | 8 K |
| `wiki/` | Главный KB v3: 9 entity типов + graph/ + niches/ | 589 | 2.6 M |

### 1.2 Top-level files

| Файл | Размер | Изменён |
|------|--------|---------|
| `CLAUDE.md` | 15 K | 2026-04-26 |
| `README.md` | 1.4 K | 2026-04-26 |
| `ARCHITECTURE-CURRENT.md` | 23 K | 2026-04-16 |
| `SYSTEM-DESIGN-HUMAN.md` | 138 K | 2026-04-18 |
| `MIGRATION.md` | 3.6 K | 2026-04-26 |
| `HOME.md` | 3.2 K | 2026-04-13 |
| `LAUNCHERS-STAGE-6.md` | 13 K | 2026-04-21 |
| `.gitignore` | 402 B | 2026-04-22 |

### 1.3 Repo-wide file totals

| Тип | Кол-во |
|-----|--------|
| Markdown (.md) | 2 736 |
| JSON (.json) | 950 |
| JSONL (.jsonl) | 66 |
| YAML (.yaml/.yml) | 53 |
| Python (.py) | 41 |

**Всего директорий root-level: 33** (не считая `.git`, `.venv-ocr`)
**Общий объём:** ~750 MB (`dashboard/` = 503 MB из них = node_modules)
**Без dashboard/node_modules:** ~250 MB

---

## §2 Strategic documents (decisions/)

### 2.1 Сводка

| Группа | Файлов | Слов |
|--------|--------|------|
| decisions/ root | 37 | ~480 K |
| decisions/variants/ | 7 | ~72 K |
| **Total** | **44** | **~604 K** |

### 2.2 Основные группы

**VISION / PHILOSOPHY / PLAN / ARCHITECTURE-BRIEF (5 docs, 45 815 слов):**
- `JETIX-VISION.md` — 6 526 слов — Identity: purpose, identity, strategic context (21.04)
- `JETIX-PHILOSOPHY.md` — 9 450 слов — 24 операционных принципа из locked decisions (21.04)
- `JETIX-PLAN.md` — 7 252 слова — Execution plan по фазам с binding inputs (24.04)
- `JETIX-ARCHITECTURE-BRIEF.md` — 11 224 слова — Binding input для Stage 6 архитекторов (21.04)
- `JETIX-SYSTEM-OVERVIEW.md` — 11 382 слова — 14-layer описание Jetix as OS (24.04, Ruslan-acked)

**LOCKS (D-серия, 2 addendum-файла):**
- `LOCKS-D25-D28-ADDENDUM-2026-04-24.md` — 1 362 слова — D25-D28 (USB-C non-negotiables)
- `LOCKS-D29-ADDENDUM-2026-04-26.md` — 1 510 слов — D29 (Korp-Startup self-narrative)
- (D1-D24 содержатся в более ранних документах — см. JETIX-PHILOSOPHY.md как агрегатор)

**STRATEGIC INSIGHTS (4 docs):**
- `STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` — 2 038 слов — AI-BIOS standardisation moment
- `STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md` — 2 716 слов — M&A advisory (Phase-2+ deferred)
- `STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md` — 1 983 слова — Arbitrage traffic (Phase-2+ deferred)
- `STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md` — 1 875 слов — AI-Psychology-led design (Phase-2+ deferred)

**LAYER DEEP-DIVES (3 docs, 150 529 слов):**
- `LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md` — 61 717 слов (Phase 2 Wave 2)
- `LAYER-6-COMMUNITY-DEEP-DIVE.md` — 27 561 слово (Phase 2 Wave 1)
- `LAYER-7-BUSINESS-TRAJECTORY-DEEP-DIVE.md` — 61 251 слово (Phase 2 Wave 3, FINAL — Phase 2 closed)

**MASTER / SYNTHESIS (4 docs):**
- `MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` — 26 349 слов (Parts 1-6 + appendices)
- `MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` — 2 138 слов (weekly living plan)
- `AWAITING-APPROVAL-master-synthesis-matrix-2026-04-22.md` — 1 428 слов (Gate 1)
- `AWAITING-APPROVAL-master-synthesis-final-2026-04-22.md` — 2 273 слова (Gate 2)

**FPF (1 doc):**
- `FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` — 9 384 слова (E-1..E-18 enhancements)

**STAGE APPROVALS (2):**
- `STAGE-3-APPROVAL.md` — 43 слова (D1/D2/D3 acked)
- `STAGE-4-APPROVAL.md` — 153 слова (D4 acked)

**CYCLE / SWARM SELF-IMPROVEMENT (5 docs):**
- `CYCLE-2-IMPLEMENTATION-REPORT-2026-04-24.md` — 4 128 слов
- `SWARM-SELF-IMPROVEMENT-HYPOTHESES-2026-04-23.md` — 3 860 слов
- `SWARM-SELF-IMPROVEMENT-OPPORTUNITIES-2026-04-23.md` — 3 220 слов
- `AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md` — 1 552 слова
- `AWAITING-APPROVAL-swarm-self-improve-gate2-2026-04-23.md` — 1 661 слово

**ROY (Phase-A baseline swarm, 3 docs):**
- `ROY-ALIGNMENT-2026-04-22.md` — 1 835 слов (5 domain experts + brigadier)
- `ROY-AGENTS-BUILT-2026-04-23.md` — 1 245 слов (Phase A complete)
- `ROY-INFORMATION-DIET.md` — 5 491 слово (philosophical + operational layers)

**KM / Wiki / Architecture (5 docs):**
- `KM-ARCHITECTURE-VARIANTS-2026-04-24.md` — 8 286 слов (6 variants, Ruslan-acked)
- `KM-MATERIALIZATION-MVP-REPORT-2026-04-24.md` — 2 515 слов
- `WIKI-V3-MECHANICS-2026-04-23.md` — 6 199 слов (9 open-questions resolved)
- `2026-04-19-architecture-v2-approval.md` — 13 953 слова (Chunks 1-8)
- `2026-04-20-jetix-architecture-final-DRAFT.md` — 11 885 слов (DRAFT v0.6)

**ARCHITECTURE VARIANTS (decisions/variants/, 7 docs, 71 975 слов):**
- `JETIX-ARCH-V1-CONSERVATIVE.md` — 12 605 слов
- `JETIX-ARCH-V2-MAXIMALIST.md` — 12 070 слов
- `JETIX-ARCH-V3-DEEPTECH.md` — 14 102 слова
- `JETIX-ARCH-V4-HYBRID.md` — 14 389 слов
- `JETIX-ARCH-V5-EMERGENT.md` — 11 743 слова
- `_CRITIC-NOTES.md` — 1 066 слов (Pass-3 critic notes on V2)
- `_STAGE-7-SCORING-AND-SUMMARIES.md` — 6 000 слов (cross-audit + scoring matrix)

**OTHER:**
- `VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` — 1 672 слова (next-week priority + 6-pillar roadmap)
- `gap-analysis-review-decisions-2026-04-20.md` — 3 726 слов (22 рекомендации + 11 open questions)
- `review-v2-progress-checklist.md` — 1 487 слов (7-chunk progress checklist)
- `life-decisions-log.md` — 186 слов (append-only лог жизненных решений)

---

## §3 Layer deep-dives + research base

### 3.1 Three Layer deep-dives (Phase 2 closed)

**LAYER-5 Product Directions** — 61 717 слов (24.04). Section structure:
- §1 TL;DR
- §2 Portfolio Overview — 9 directions
- §3.1-§3.9 направление-by-направление (AI Consulting / Producer Center / USB-C / Matchmaker / Secure Network / YouTube-Analyzer / Educational / Tokens / Smart AI)
- §12 Cross-Direction Synergy + Conflict Matrix
- §13 Evolution per Gate (9 directions × 5 gates)
- §14 Tools Roadmap per Phase
- §15 Open Questions + Preserved Dissents + F-G-R Tagging
- §16 Integration Notes

**LAYER-6 Community Deep-Dive** — 27 561 слово (24.04). Section structure:
- §1 TL;DR
- §2 ICP Trinity (Client + Partner + Team)
- §3 11 archetypes deep-dive
- §4 5-criteria filter (D22)
- §5 Alliance architecture — 3 options
- §6 Matchmaker mechanics
- §7 Outreach mechanism
- §8 Membership / invite filter
- §9 Growth model
- §10 Secure Network Architecture
- §11 Evolution per Gate (G1 €50K → G5 $1T)
- §12 Open Questions
- §13 Preserved Dissents + F-G-R + Citations

**LAYER-7 Business Trajectory Deep-Dive** — 61 251 слово (25.04, FINAL — Phase 2 closed). Section structure:
- §1 TL;DR
- §2 Pricing & Reach (9 directions)
- §3 Unit-economics per direction + Ruslan-hours rationing + compute allocation
- §4 Gate triggers & Master Table (5 gates × 14 layers)
- §5 Income-Floor reconciliation (P1A vs P1B; миллионер vs Mittelstand)
- §6 Pricing Strategy Evolution per Gate
- §7 Producer-Pilot Timing (dissent preserved)
- §8 Patent Shortlist (9 Jetix innovations)
- §9 Investor Ordering (strategic angels → DACH FOs → sovereign EU funds)
- §10 Compensation Evolution
- §11 Risk Register (15 risks; top-3: R-8 founder burnout RPN 130, R-7 client concentration RPN 112.5, R-1 €50K miss RPN 90)
- §12 Financial Tools Roadmap
- §13 Evolution Milestones + Phase-2 closure
- §14 Open Questions

### 3.2 raw/research/ — 27 markdown файлов + 12 субдиректорий

Все по pattern `<topic>-deep-research-YYYY-MM-DD.md`. Включает:
- Foundation research (consulting / agency / community / holding / platform-os / product / software / Levenchuk methodology)
- Architecture research (architecture-implementation-synthesis, architecture-synthesis-v2-final)
- Functional research (CRM/sales architecture, knowledge architecture, folder structure, jetix-life separation, mega-corp governance, org chart in git, company-as-code impl)
- Recent (24-26.04): BIOS clone wars parallel (6 345 слов), Wall Street M&A (7 144), Arbitrage Traffic (4 093)
- Subdirs: `architecture-variants-2026-04-22`, `compounding-engineering-2026-04-22`, `d6-reviews`, `levenchuk-fpf-research-2026-04-20`, `perplexity-market-ai-native-2026-04-22`, `phase-2-deep-research-2026-04-22`, `stage2-review`, `step-2-1-extractions`, `step-2-2-2-extractions`, `step-2-2-3b-extractions`, `step-2-2-3c-extractions`, `step-2-2-4-extractions`

Raw research суммарно ~260 K слов.

### 3.3 Cycles (1-11)

Cycle артефакты находятся в `swarm/wiki/cycles/`, `swarm/logs/cyc-*`, `swarm/awaiting-approval/cycle-*.md`:

| # | Имя | Дата | Описание | Статус |
|---|-----|------|----------|--------|
| 1 | cyc-swarm-self-improve-v1-2026-04-23 | 23.04 | Первый swarm-cycle: self-improvement protocols | Archived |
| 2 | (referenced cycle-2-implementation) | 24.04 | OPP-04 + OPP-01 + OPP-02 + HD-01 + HD-02 closure | In workflow |
| 3 | cyc-km-architecture-2026-04-24 | 24.04 | KM + Project-Mgmt Architecture | Archived |
| 4 | cyc-km-materialization-2026-04-24 | 24.04 | KM materialization MVP | Archived |
| 5 | cyc-jetix-system-overview-2026-04-24 | 24.04 | JETIX-SYSTEM-OVERVIEW deep-dive | Archived |
| 6 | cyc-layer-6-community-deep-dive-2026-04-24 | 24.04 | LAYER-6 Community (Phase 2 Wave 1) | Archived |
| 7 | cyc-layer-7-business-trajectory-2026-04-25 | 25.04 | LAYER-7 Business (Phase 2 Wave 3, FINAL MUST) | Phase-2-closed |
| 8 | cyc-producer-services-strategy-options-2026-04-25 | 26.04 | Producer Services OPTIONS (Phase 3 Cycle 1) | Acked |
| 9 | (не виден в filesystem) | — | — | — |
| 10 | cycle-10-crm-build-2026-04-26 | 26.04 | CRM build: 24 source files / 10 skills / 35 tests | **AWAITING-APPROVAL** |
| 11 | cycle-11-voice-migration-2026-04-26 | 26.04 | Voice-Pipeline миграция на CC headless + filter.py partial-save | **AWAITING-APPROVAL** |

---

## §4 Agents (20 каталогов)

### 4.1 agents/ — 20 субдиректорий

**С system.md (12 файлов, базовые agents per CLAUDE.md):**

| Slug | Роль (1 строка) | Изменён |
|------|----------------|---------|
| crazy-agent | Wild idea generator + cross-domain connector | 16.04 |
| inbox-processor | Information triage и routing (voice / email / ideas) | 26.04 |
| knowledge-synth | Deep knowledge synthesis + Brain Lead | 26.04 |
| life-coach | Personal wellness optimization | 16.04 |
| manager | Operations coordinator (central pipeline orchestrator) | 26.04 |
| meta-agent | System auditor + continuous improvement | 26.04 |
| personal-assistant | Personal productivity + OPS coordination | 16.04 |
| sales-lead | Sales coordinator + offer designer | 26.04 |
| sales-outreach | Outreach + community engagement | 26.04 |
| sales-researcher | Sales intelligence + prospect research | 16.04 |
| strategist | Strategic decision-maker (Opus-level) | 16.04 |
| system-admin | Server и system maintenance | 26.04 |

**Без system.md, только strategies.md (8 файлов, swarm-experts):**

| Slug | strategies.md | Назначение |
|------|--------------|------------|
| brigadier | 50 K | Главный orchestrator swarm Phase A |
| engineering-expert | 4.6 K | Engineering lens (code review, architecture) |
| investor-expert | 8.2 K | Investing + value-creation lens |
| mgmt-expert | 17 K | PM + management-philosophy lens |
| philosophy-expert | 6.7 K | Philosophy + epistemology lens |
| systems-expert | 13 K | Systems-thinking + cybernetics lens |
| quick-money-brigadier | 1.5 K | Mini-swarm orchestrator (project quick-money) |
| (примечание: levenchuk-deep-dive-brigadier — только в .claude/agents/, не в agents/) | | |

Каждый agents/<slug>/ содержит: strategies.md, scratchpad.md, niche/ (symlink в wiki/niches/), versions/ (если есть).

### 4.2 .claude/agents/ — 24 Claude Code agent definitions

Большие промпты (74-98 K):
- `engineering-expert.md` — 98 K
- `mgmt-expert.md` — 93 K
- `investor-expert.md` — 84 K
- `systems-expert.md` — 80 K
- `philosophy-expert.md` — 74 K
- `brigadier.md` — 64 K

Меньшие brigadier'ы:
- `project-brigadier.md` — 6.3 K
- `quick-money-brigadier.md` — 6.2 K
- `levenchuk-deep-dive-brigadier.md` — 2.5 K

Прочие:
- `staging-writer.md` — 6.5 K
- `sweep-worker.md` — 6.9 K
- + остальные совпадают по slug-у с agents/<slug>/

### 4.3 comms/mailboxes/ — 13 JSONL channels

| Mailbox | Lines | Размер |
|---------|-------|--------|
| `manager.jsonl` | 4 | 907 B |
| `sales-lead.jsonl` | 1 | 205 B |
| `strategist.jsonl` | 1 | 165 B |
| `system-admin.jsonl` | 1 | 198 B |
| `crazy-agent.jsonl` | 1 | 14 B |
| `life-coach.jsonl` | 1 | 11 B |
| 7 остальных (`human`, `inbox-processor`, `knowledge-synth`, `meta-agent`, `personal-assistant`, `sales-outreach`, `sales-researcher`) | 0 | 0 B |

**Активных сообщений всего: 9** (5 агентов с очередями, 8 пустых).

### 4.4 shared/state/ — 9 state файлов

- `active-projects.json` (432 B) — quick-money P1, target $50K к 2026-06-30
- `focus.json` (533 B) — global goal + weekly/daily focus
- `system-config.json` (697 B) — theme, language, agent defaults, paths
- `daily-briefing.json` (226 B) — daily briefing шаблон
- `priorities.json` (253 B) — priority weights (quick-money = 10)
- `system-health.json` (613 B) — статус: всё green
- `kanban.json` (1.7 K) — backlog/todo/in-progress/review/done
- `contacts.json` (3 B) — placeholder
- `metrics/` — agent-performance.json, ab-tests.json, feedback.jsonl, task-log.jsonl

### 4.5 shared/schemas/ — 3 JSON Schema

- `message.schema.json` (1.7 K) — JetixMessage (id/timestamp/from/to/type/priority/subject/body/context/status/deadline)
- `briefing.schema.json` (1.3 K) — DailyBriefing (date/system_health/priorities/escalations/day_type)
- `task.schema.json` (1.1 K) — JetixTask (id/created_at/assigned/status/title/description/project/priority/deadline)

---

## §5 Skills (.claude/skills/) — 28 файлов

### 5.1 По категориям

**CRM (10 skills, все 26.04):**
- `crm-add` — create person/org с auto-prefilled strategy hooks
- `crm-show` — pretty-print full record (frontmatter + 14 секций)
- `crm-list` — filtered table view (role/status/country/ICP/audience)
- `crm-search` — full-text search (name/aliases/§1+§13/tags)
- `crm-touch` — quick interaction log (+ §11 + bump last_touch_date)
- `crm-update` — update fields + optional note + resync hooks
- `crm-rebuild-index` — regenerate index.md (idempotent)
- `crm-dash` — dashboard (totals/pipeline/ICP/channels)
- `crm-stuck` — list contacts >14d без touch
- `crm-weekly` — weekly report (extends dash + new contacts)

**Wiki (7 skills, 23-24.04):**
- `ingest` (9.7 K) — parse 6 типов источников → wiki entities + edges
- `ask` (8.1 K) — Q&A с 5-15 страницами + citations
- `lint` (18 K) — 11 health checks (orphans/stale/broken/contradictions) + SG predicate validation
- `consolidate` (7.9 K) — duplicate merge (с `--weekly` флагом)
- `build-graph` (5.5 K) — community detection (Louvain-equiv)
- `search-kb` (1.9 K) — legacy KB lookup (deprecated в пользу /ask)
- `compile` (2.9 K) — legacy KB synthesis (deprecated)

**Project (5 skills, 24.04):**
- `project-bootstrap` (10.4 K) — scaffold нового проекта (4 типа + mini-swarm + client namespace)
- `project-review` (6.5 K) — еженедельный дайджест
- `project-archive` (4.4 K) — killed/closed/pivoted
- `project-de-morph` (6.2 K) — rollback до SG-N
- `project-promote` (6.7 K) — bets → consulting/research/product

**System (3 skills):**
- `company-status` (12 K) — git-native снапшот (≤80 строк)
- `knowledge-diff` (8.8 K) — wiki delta между датами по git log
- `plan-day` (2.3 K) — утреннее открытие (14.04)

**Other (3 skills):**
- `close-day` (2.3 K) — итог дня + git push (14.04)
- `focus` (2.5 K) — project context switcher (14.04)
- `sweep-notion-bank` (5.9 K) — sweep 650+ Notion идей в wiki (23.04)

**Subdirectories:** `/close-day/`, `/focus/`, `/plan-day/` (содержат вложенные SKILL.md).

**Total: 28 файлов** (25 root .md + 3 nested SKILL.md).

---

## §6 Voice-pipeline state

### 6.1 tools/lib/cc_helper.py (cycle 11 abstraction layer)

- Размер: 5.9 K, 158 строк, изменён 26.04 03:35
- Дуальный backend через `claude_call(system, user, model)` API
- **Default:** CC headless subprocess (`claude -p`) — Max-подписка, без ANTHROPIC_API_KEY
- **Legacy:** Direct anthropic SDK (включается через `JETIX_LLM_BACKEND=api`)
- Model alias mapping (e.g., `claude-3-5-sonnet-20241022` → `claude-sonnet-4-6`)
- JSON fence stripping для structured responses
- Env: `JETIX_LLM_BACKEND` (default `cc-headless`), `JETIX_LLM_TIMEOUT_SEC` (default 900), `ANTHROPIC_API_KEY` (только для backend=api)

### 6.2 Tool скрипты

| Скрипт | Размер | Изменён | Строк | Что делает |
|--------|--------|---------|-------|------------|
| `tools/transcribe.py` | 4.1 K | 15.04 | 123 | inbox/voice → Groq Whisper (`whisper-large-v3`, lang=ru) → raw/transcripts/ + raw/voice-memos/ archive |
| `tools/extract.py` | 14 K | 26.04 | 330 | transcripts → structured JSON items (category/content/priority/horizon) → consolidated YAML `inbox/processed/extract-items-latest.yaml` |
| `tools/filter.py` | 15 K | 26.04 | 358 | Batch-filter items с **fault-tolerance** (.partials/) + `--resume` (default) / `--restart` |
| `tools/summarize.py` | 5.2 K | 26.04 | 141 | Topic clustering без dedup → `~/summary-latest.md` + `reports/summary_YYYY-MM-DD.md` |
| `tools/review_report.py` | 5.2 K | 15.04 | 152 | Filtered batch → markdown review report (table format) → `~/review-latest.md` + `reports/review_YYYY-MM-DD.md` |
| `tools/run_pipeline.sh` | 1.3 K | 26.04 | 26 | Orchestrator: transcribe → extract → CRM voice-route → summarize |
| `tools/distribute.py.bak` | 5.4 K | 15.04 | 162 | (Архивирован — auto-distribution отключён, чтобы Claude-output не попадал в KB без человеческого review) |

**Env переменные:**
- `transcribe.py` → `GROQ_API_KEY`
- `extract.py` / `filter.py` / `summarize.py` → `JETIX_LLM_BACKEND`, `JETIX_LLM_TIMEOUT_SEC`, `ANTHROPIC_API_KEY` (only if backend=api)
- `review_report.py` → no external env
- `run_pipeline.sh` → bash subprocess

### 6.3 tools/test_*.py

- `test_e2e_no_api.py` — 3 теста — end-to-end smoke без ANTHROPIC_API_KEY (CC headless full pipeline)
- `test_filter_partial_save.py` — 4 теста — filter.py fault tolerance (partials, resume, final merge, --restart)

Оба теста явно `unset ANTHROPIC_API_KEY` + `JETIX_LLM_BACKEND=cc-headless`.

### 6.4 Storage state

**inbox/processed/:**
- 158 файлов всего
- `extractions/` — 140 JSON (15-26.04, новейший: `audio_539@26-04-2026_03-44-40.json`)
- `filtered/` — 4 batch JSON (15.04 / 18.04 / 21.04 / 24.04, размер 21K-525K) + 2 error logs (18.04)
- `extract-items-latest.yaml` (1.2 K, 26.04 03:37)

**raw/transcripts/:**
- 151 .txt файл, 968 K, период 08-26.04

**raw/voice-memos/:**
- 151 audio файл, 123 MB (.ogg/.m4a/.mp3/.wav/.webm)
- Нейминг: `audio_NNN@DD-MM-YYYY_HH-MM-SS.*`

**reports/ (последние review):**
- `review_2026-04-26-DEEP.md` — 112 K (deep)
- `review_2026-04-26.md` — 11 K (compact)
- `review_2026-04-24.md` — 602 K (largest)
- `review_2026-04-21.md` — 352 K
- `review_2026-04-18.md` — 154 K
- `review_2026-04-15.md` — 11 K
- `summary_2026-04-24.md` — 128 K
- `summary_2026-04-15.md` — 88 K
- + arch-migration / ideas-import / notion-alpha / tech-doc / voice-memos audit (15-18.04)

---

## §7 CRM cycle 10 deliverables

### 7.1 crm/ structure

- `README.md` — 1 414 слов (multi-purpose contact network filesystem-as-truth)
- `PLAN.md` — 1 078 слов (frozen reference, status: implemented cycle-10)
- `index.md` — 25 строк (auto-generated, 4 contacts: 4 people + 0 orgs)
- `log.md` — 54 строки (append-only, новейший: 26.04 03:35)
- `icp.md` — 67 строк (4 ICP + buyer persona framework)

| Subdir | Файлов | Размер |
|--------|--------|--------|
| `people/` | 4 | 40 K |
| `orgs/` | 0 | 4 K |
| `_schema/` | 4 | 28 K |
| `_scripts/` | 8 Python | 192 K |
| `_tests/` | 5 Python | 92 K |
| `_templates/` | 2 | 12 K |
| `views/`, `recordings/`, `transcripts/` | 0 каждая | 4 K каждая |

### 7.2 _schema/ (4 YAML)

- `frontmatter.yaml` — JSON-Schema spec, 12 field groups, schema_version + required + fields + auto_fix
- `roles.yaml` — 24 роли в 6 группах (sales / capital / partnership / advisory / team / network) + transitions
- `statuses.yaml` — 13 pipeline statuses (`draft_from_voice` → `cold` → `warm` → `contacted` → `discovery_call` → `proposal` → `negotiation` → `closed_won/lost`; + `paused`, `active`, `past`) + stuck threshold 14 days
- `strategy-hooks.yaml` — 6 offers + 6 asks с relevance filters

### 7.3 _scripts/ (8 Python, 1 659 строк)

- `crm.py` — main CLI router (482 строки)
- `dashboard.py` — dashboard + stuck + weekly (287)
- `voice_router.py` — voice → DRAFT-only (218)
- `frontmatter.py` — parser + validator + auto-fix (226)
- `views.py` — query engine (185)
- `index_builder.py` — index regenerator (135)
- `strategy_hooks.py` — offer/ask matcher (126)
- `__init__.py` — stub

### 7.4 _tests/ (5 файлов, **35 unit-тестов**)

- `test_frontmatter.py` — 12 тестов (parser + validator + auto-fix)
- `test_views.py` — 12 тестов (filter + search + sort)
- `test_strategy_hooks.py` — 7 тестов (matcher + filters + status relevance)
- `test_index_builder.py` — 4 теста (rebuild + by-role tables + idempotency)
- + fixtures: sample-person-anton.md, sample-person-vladislav.md, sample-org-acme.md

### 7.5 people/ (4 entries)

| Slug | Имя | Роли | Статус | ICP | Last Touch |
|------|-----|------|--------|-----|------------|
| anton-mentor | Антон | mentor | cold | — | 26.04 |
| vladislav-economist | Владислав | advisor | cold | — | 26.04 |
| rodion-youtuber | Родион | partner_prospect | cold | — | 26.04 |
| example-person | Example Person (TEMPLATE) | advisor / partner_prospect | paused | 18 | 26.04 |

**orgs/:** 0 entries (директория pre-allocated).
**DRAFTs:** 0 (все finalized).

### 7.6 .claude/skills/crm-*.md (10 skills) — см. §5.

---

## §8 Wiki state

### 8.1 9 entity types (552 файла)

| Тип | Каталог | Файлов |
|-----|---------|--------|
| concepts | `wiki/concepts/` | 14 |
| entities | `wiki/entities/` | 4 |
| sources | `wiki/sources/` | 271 |
| topics | `wiki/topics/` | 1 |
| ideas | `wiki/ideas/` | 257 |
| experiments | `wiki/experiments/` | 0 (пустой) |
| claims | `wiki/claims/` | 5 |
| summaries | `wiki/summaries/` | 0 (пустой) |
| foundations | `wiki/foundations/` | 0 (пустой) |

### 8.2 Index + log

- `wiki/index.md` — 23 K, 207 строк, изменён 26.04 04:06
- `wiki/log.md` — 9.7 K, 128 строк, изменён 26.04 04:06

### 8.3 Graph

- `wiki/graph/edges.jsonl` — **577 рёбер**, 108 K
- **8 наблюдённых типов рёбер** (CLAUDE.md упоминает 9 типов — observed только 8):
  1. `derived_from` (most common)
  2. `extends`
  3. `supports`
  4. `contradicts`
  5. `advisor-of`
  6. `co-founder-with`
  7. `founder-of`
  8. `part_of`
- `wiki/graph/communities.jsonl` — отсутствует

### 8.4 Niches (6/6 присутствуют)

`wiki/niches/`: business / life / meta / personal / sales / tech (по 1 anchor-файлу в каждой).

### 8.5 6 концептов ingested 26.04

| File | Title | Niche |
|------|-------|-------|
| `affirmation-ritual-founder-state.md` | Affirmation ritual для founder state stability | life |
| `founder-isolation-as-stopper-class.md` | Founder isolation как stopper класс | meta |
| `korporaciya-startup-concept.md` | Корпорация-стартап — Jetix как стартап, претендующий на корпорацию | business |
| `menedzhment-vazhnosti-informacii.md` | Менеджмент важности информации | life |
| `protocol-2-day-bad-state-limit.md` | Протокол: лимит 2 дня плохого состояния | life |
| `ai-proektirovanie-psy-led.md` | AI-проектирование psy-led — психологи проектируют AI | tech |

Распределение: 3 life / 1 meta / 1 business / 1 tech.

### 8.6 Опциональные подкаталоги

- `wiki/comparisons/` — существует (только .gitkeep)
- `wiki/drafts/` — НЕ создан
- `wiki/cycles/` — НЕ создан (cycle артефакты в `swarm/wiki/cycles/`)
- `wiki/designs/` — НЕ создан (design артефакты в `swarm/wiki/designs/`)

---

## §9 Memory state (~/.claude/projects/-home-ruslan-jetix-os/memory/)

### 9.1 Files: 2

| Файл | Тип | Слов | Изменён | Назначение |
|------|-----|------|---------|------------|
| `feedback_no_api_keys.md` | feedback | 249 | 22.04 16:49 | Никогда не вызывать ANTHROPIC_API_KEY/GROQ_API_KEY напрямую (Max sub) |
| `MEMORY.md` | index | 19 | 22.04 16:49 | Index файл со ссылками |

### 9.2 MEMORY.md содержание

```
- [No direct API keys](feedback_no_api_keys.md) — user on Max subscription;
  `ANTHROPIC_API_KEY`/`GROQ_API_KEY` calls cost real money, use built-in tools only
```

### 9.3 Other memory locations

- `~/.claude/memory/` — НЕ существует
- `/home/ruslan/jetix-os/.claude/memory/` — НЕ существует

**Итого:** 1 активная feedback-память + 1 index = 2 файла, 268 слов.

---

## §10 Notion DBs

### 10.1 Из CLAUDE.md (8 главных DB)

| DB | Notion ID | Назначение |
|----|-----------|-----------|
| Command Center | `3322496333bf8161b6d3ea789d039356` | Central hub координации |
| Daily Log DB | `30a24963-33bf-8005-817a-000beb10bcd4` | Personal activity tracking |
| Projects DB | `69a3c581-ab33-48d9-9827-ec8a8bb69d14` | Project management |
| Journal of Chats | `89c2ac5e-797e-4bff-bd53-4316026f8094` | Conversation history |
| Банк идей | `bf0e9a11-0e6f-4717-9ae5-e19f9a096ce7` | Idea storage (~590 active per 16.04) |
| ICP Page | `3372496333bf8125a72cd7352124b5ee` | Ideal Customer Profile |
| Research Hub | `32c2496333bf81e8807cd490f9d17872` | Research aggregation |
| Life OS | `3322496333bf8184b31bc985a93222d7` | Personal wellness tracking |

### 10.2 Дополнительно

- 300+ unique Notion page/DB IDs наблюдены across `.md`/`.yaml`/`.json` файлы (особенно в `raw/notion-ideas/`, `knowledge-base/`, `design/`, `swarm/wiki/`)
- Highest Notion ID density: `raw/research/architecture-variants-2026-04-22/ATOM-REGISTRY.md`, `swarm/wiki/drafts/T-jetix-system-overview-*`, `design/JETIX-ARCHITECTURE-WORKING.md`, `SYSTEM-DESIGN-HUMAN.md`

### 10.3 MCP конфигурация

- `mcp__notion__notion-fetch` — enabled (settings.local.json)
- `mcp__notion__notion-query-database-view` — enabled
- `mcp__notion__notion-update-page` — referenced в skill definitions

**Agents с Notion MCP:** sales-lead, life-coach, meta-agent, strategist, knowledge-synth.
**Skills с Notion MCP:** `/sweep-notion-bank`, `/close-day`, `/focus`.

### 10.4 Schema/row counts

NOT accessible via filesystem alone — требуют Notion MCP authentication. **В этом audit не запрашивались** (passive inventory only).

---

## §11 Env / creds / config

### 11.1 Env vars (NAMES only, no values)

| Var | Status |
|-----|--------|
| `ANTHROPIC_API_KEY` | **SET** (observed but not assessed — see §14) |
| `GROQ_API_KEY` | SET |
| `OPENAI_API_KEY` | UNSET |
| `GITHUB_TOKEN` | UNSET |
| `NOTION_API_KEY` / `NOTION_TOKEN` | UNSET |
| `MIRO_TOKEN` | UNSET |

### 11.2 Shell rc файлы

| Файл | Status | Размер | Modified | export statements | Vars |
|------|--------|--------|----------|-------------------|------|
| `~/.bashrc` | EXISTS | 4.1 K | 26.04 22:20 | 1 | `GROQ_API_KEY` |
| `~/.zshrc` | NOT EXISTS | — | — | — | — |
| `~/.profile` | EXISTS | 807 B | 13.04 | 0 | — |
| `~/.env` | NOT EXISTS | — | — | — | — |
| `/home/ruslan/jetix-os/.env` | NOT EXISTS | — | — | — | — |

### 11.3 Claude settings

| Файл | Status | Размер | Top-level keys | Permissions | Hooks | MCP |
|------|--------|--------|----------------|-------------|-------|-----|
| `/home/ruslan/jetix-os/.claude/settings.json` | NOT EXISTS | — | — | — | — | — |
| `/home/ruslan/jetix-os/.claude/settings.local.json` | EXISTS | 6.6 K | permissions, allow, mcp__* | 95 allowed Bash + 4 Miro + 2 Notion | 0 | 4 Miro tools + 2 Notion tools |
| `~/.claude/settings.json` | EXISTS | 464 B | permissions, deny, skipDangerousModePermissionPrompt | 13 deny rules | 0 | 0 |

**Allow в settings.local.json:** 95 Bash patterns (git/npm/curl/docker/python3/etc), localhost curl на портах 3000/3001.
**Deny в ~/.claude/settings.json:** 13 деструктивных команд (rm -rf, ssh-keygen, passwd, systemctl stop ssh, etc).

### 11.4 .gitignore

Excluded: `private/`, `inbox/`, `.obsidian/`, `.vectordb/`, `node_modules/`, `__pycache__/`, `.venv/`, `.env*`, `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `*~`, `*.pyc`, `raw/books-md/**/.DS_Store`.

---

## §12 Git state

### 12.1 Current state

- **Branch:** `claude/jolly-margulis-915d34`
- **Working tree:** NOT clean
  - `D .claude/scheduled_tasks.lock` (deleted)
  - `M config/context.md` (modified)

### 12.2 Branches

**Local:**
- `* claude/jolly-margulis-915d34` (current)
- `claude/xenodochial-jennings` (last: 16.04 17:42 — `[arch] inventory final report`)
- `main` (last: 19.04 19:24 — `[handoff] полный контекст-промпт`)

**Remote (origin):** 9 branches:
- main, claude/jolly-margulis-915d34, claude/xenodochial-jennings, claude/amazing-kilby-2587c6, claude/blissful-cohen-c776d8, claude/hopeful-kalam-f21ad7, claude/optimistic-feistel-362cec, claude/recursing-kirch-26223c, claude/wonderful-tharp-dcc9f8

### 12.3 Tags (2)

- `system-design-human-v1-beta-2026-04-18` (18.04)
- `v1-beta-tech-2026-04-18` (18.04)

### 12.4 Remote

- `origin git@github.com:Bogersebekov/jetix-os.git` (fetch + push)
- Last fetch: 26.04 23:25:51

### 12.5 Stats

- **Total commits all branches:** 582
- **Last 30 days:** 571
- **Last 7 days:** 406

**Most-touched files (last 30d):**
1. `decisions/2026-04-19-architecture-v2-approval.md` — 52 touches
2. `decisions/review-v2-progress-checklist.md` — 48
3. `decisions/gap-analysis-review-decisions-2026-04-20.md` — 30
4. `SYSTEM-DESIGN-HUMAN.md` — 18
5. `swarm/wiki/log.md` — 17
6. `wiki/log.md` — 13
7. `wiki/graph/edges.jsonl` — 11
8. `CLAUDE.md` — 11
9. `wiki/index.md` — 10

**Top committers (last 90d):**
- Ruslan — 302 commits
- Bogersebekov — 269 commits

### 12.6 Recent 30 commits (выборка)

```
ab06cc0 26.04 04:07 Ruslan      [voice] archive transcripts + ogg batch 24-26.04 (audio_530-539)
f077e1e 26.04 04:07 Ruslan      [decisions] add D29 Korp-Startup Lock + D30 AI-Psy-Led Strategic Insight
a2ec3e2 26.04 04:07 Ruslan      [crm] add 3 known contacts: anton-mentor + vladislav-economist + rodion-youtuber
983abdd 26.04 04:07 Ruslan      [wiki] ingest 6 concepts from voice 24-26.04
ea8685d 26.04 03:44 Ruslan      [tools] migrate voice-pipeline to CC headless + filter.py partial-save (cycle 11)
60d5558 26.04 03:44 Ruslan      [voice] add review reports for 24-26.04 (compact 10.5KB + deep 114KB)
46f46af 26.04 03:10 Ruslan      [crm] update AWAITING-APPROVAL packet — cycle 10 fully completed
6864173 26.04 03:09 Ruslan      [crm] add edges validator (build_graph.py lint)
2cf1f26 26.04 03:07 Ruslan      [crm] wire voice→CRM end-to-end via extract-items-latest.yaml
74e7054 26.04 02:51 Ruslan      [crm] core skeleton + skills + tests + dashboard
0f7247c 26.04 01:54 Ruslan      [ps-options] cycle 8 ack + Phase 7 compound + Phase 8 archive
699ce2d 26.04 01:54 Ruslan      [cd-options] Canonical strategy-OPTIONS.md integrated — ~34.6K words
0baa7a2 26.04 01:54 Ruslan      [ps-options] canonical strategy-OPTIONS.md + AWAITING-APPROVAL packet
bc11d21 26.04 01:54 Ruslan      [cd-options] Wave-A drafts (4 cells parallel)
1d6987d 26.04 01:54 Ruslan      [ps-options] cells dispatched (5 in parallel, Wave-A)
cbcdef2 26.04 03:03 Bogersebekov [handoff] полный контекст-промпт для следующего чата — 2026-04-26 evening
a831c54 26.04 01:16 Bogersebekov [ops] Advisor search FINALIZED
5ab4c82 26.04 00:35 Bogersebekov [ops] Personal mentor search — точка А + portrait
4a17f5b 25.04 13:16 Bogersebekov [ops] Team search — портреты + research
fb2f6f1 25.04 05:16 Bogersebekov [research] Arbitrage Traffic deep-dive + Strategic Insight
0ac2fff 25.04 02:41 Bogersebekov [prompts] Phase 3 OPTIONS papers — producer-services + ai-consulting-dach
```

---

## §13 Inventory totals

| Метрика | Значение |
|---------|----------|
| Total markdown файлов в `decisions/` (incl. variants/) | 44 |
| Total word count strategic docs (`decisions/`) | ~604 357 |
| Total agents (agents/) | 20 (12 с system.md + 8 без, swarm-experts) |
| Total .claude/agents/ definitions | 24 |
| Total skills (.claude/skills/) | 28 (25 root + 3 nested) |
| Total CRM entries (people + orgs) | 4 + 0 = 4 |
| Total wiki entity files (9 types) | 552 |
| Total wiki edges | 577 (8 типов наблюдено) |
| Total memory files | 2 (1 feedback + 1 index) |
| Total cycles completed (numbered) | 1-8 (cycle 9 не виден) + 10 + 11 (AWAITING) |
| Voice-pipeline status | Cycle 11 done — CC headless on Max subscription |
| CRM status | Cycle 10 done — 35 unit-tests passing, 4 entries |
| Total commits all-branches | 582 |
| Commits last 7d | 406 |
| Commits last 30d | 571 |
| Repo total size | ~750 MB (без node_modules ~250 MB) |
| Total .md files repo-wide | 2 736 |
| Total .py files repo-wide | 41 |
| Total .json/.jsonl files repo-wide | 950 + 66 = 1 016 |
| Total .yaml/.yml files repo-wide | 53 |

---

## §14 Что НЕ покрыто этим audit (transparency)

Следующие области наблюдены но НЕ оценены / НЕ глубоко покрыты в данном audit:

1. **Notion DB row counts + schemas** — passive inventory only; не делали API calls в Notion MCP. Schema deep-dive потребует отдельной авторизации.

2. **`ANTHROPIC_API_KEY` SET status** — Subagent K зафиксировал, что переменная установлена в окружении; cycle 11 cleanup expectation была "should be empty". Это **observation, not judgment** — не оцениваем правильно/неправильно.

3. **Cycle 9 артефакт** — нет в filesystem (cycles 1-8 + 10 + 11 видны, cycle 9 пропущен/не назван). Не интерпретируется как "missing" или "lost".

4. **Несоответствие counts** — CLAUDE.md упоминает "12 specialized agents", agents/ содержит 20 субдиректорий (12 с system.md + 8 swarm-experts без system.md). Subagent A описал как "17 specialized agents". Точное число зависит от определения "agent". Не разрешается в audit.

5. **dashboard/** (503 MB, 34 170 файлов) — не deep-divе'илась внутрь, т.к. в основном node_modules / build артефакты. React/Vite/TS/Tailwind стек подтверждён.

6. **raw/** (212 MB, 1 222 файла) — top-level каталоги перечислены, но deep contents (e.g., `raw/books-md/`, `raw/notion-ideas/` детально не инвентаризовались).

7. **swarm/** (6.8 MB, 308 файлов) — основные cycle-артефакты охвачены, но детальный inventory swarm/wiki/drafts/, swarm/wiki/designs/, swarm/awaiting-approval/ — не делался.

8. **prompts/** (2.7 MB, 130 файлов) — не инвентаризовалась внутрь (large prompt library).

9. **dashboard server runtime state** — не проверялся (running / stopped / built).

10. **Дашборд (React frontend) функциональность** — структура наблюдена, фактические компоненты + состояние UI не оценены.

11. **Memory directory `claudeMd` reminder mentions `/home/ruslan/.claude/projects/-home-ruslan-jetix-os/memory/`** — Subagent I проверил `~/.claude/projects/-home-ruslan-jetix-os/memory/`. Это та же директория. Один файл feedback + index.

12. **Health / wellness data, daily-log/, hypotheses/, projects/** — каталоги перечислены в §1, но contents detail не делалась.

13. **Encryption / private/ contents** — `private/` empty per inventory; if there's encrypted content elsewhere, не проверялось.

14. **Все 30 D-locks** (D1-D30) — упомянуты только D25-D29 как dedicated addendum-файлы. D1-D24 находятся внутри JETIX-PHILOSOPHY.md и других docs, не извлекались отдельно.
