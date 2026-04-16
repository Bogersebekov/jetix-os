---
type: architecture-inventory
date: 2026-04-16
scope: as-is snapshot, 3 levels of detail
author: claude-code
miro_board: https://miro.com/app/board/uXjVG2-05Ns=/
md: ARCHITECTURE-CURRENT.md
status: complete
---
# Architecture Inventory — Final Report (2026-04-16)

## Что сделано

11 артефактов в Miro + 1 markdown:

| Уровень | Miro | md секция |
|---------|------|-----------|
| L1 Birds-Eye | 1 flowchart | §1 |
| L2 Component Deep-Dive | 6 sub-diagrams (2A IO, 2B Knowledge, 2C Agents+Skills, 2D Apps, 2E External, 2F Data Flow) + header doc | §2 (с подсекциями 2.1-2.6) |
| L3 Agent Interactions | 1 flowchart (departments map) + 3 UML sequence (delegation / /ingest / /close-day) + header doc | §3 (таблица + gap list) |

3 коммита:
- `5c914bd` L1
- `ade9978` L2
- `6f2973b` L3

Файл: `/home/ruslan/jetix-os/ARCHITECTURE-CURRENT.md` (337 строк).

## 3 ключевые находки (что работает)

### 1. Wiki/ — самая зрелая часть системы

`wiki/` v2 (Karpathy LLM Wiki + OmegaWiki) реально функционирует:

- **60 идей** импортировано из Notion (полная цепочка `raw/notion-ideas/` →
  `/ingest` → `wiki/ideas/*.md` + sources).
- **137 typed edges** в `wiki/graph/edges.jsonl` (9 типов; 81 supports,
  35 extends, 20 derived_from, 1 contradicts).
- **4 communities** после `/build-graph` (business 44 нод, life 15, meta 10,
  tech 4).
- Writeback loop работает: `/ask` сохраняет ценные ответы в `comparisons/` +
  обратные edges в `edges.jsonl`.
- Maintenance (`/lint`) даёт регулярные отчёты — `_lint-report-2026-04-16.md`,
  `_lint-report-2026-04-16-v2.md`.
- Lint baseline: 1 broken link (vs 11 до прошлого ingest).

**Это единственный pipeline в системе, у которого есть подтверждённый
output на этом масштабе.**

### 2. JSONL-mailbox + JSON-state дизайн пригоден для текущего scope

Решение из `ARCHITECTURE.md` §1 (один JSONL на агента, schema-validated,
append-only, без Redis) — обоснованное для 5-12 агентов:

- Schema (`shared/schemas/message.schema.json`) полная: id-regex
  `msg-YYYYMMDD-NNN`, enum `from` (12 агентов + human), 8 типов, 4 priorities,
  5 статусов.
- Шина-like структура (12 inbox JSONL + общий `human.jsonl`) понятна,
  отлаживаема, видна в файловой системе.
- Per-agent memory (5 layers: system, baseline, strategies, scratchpad,
  niche/) задаёт пространство для System Prompt Learning без оверкилла.

Когда агенты начнут говорить — инфраструктура готова.

### 3. Skill'ы — правильная гранулярность

`/ingest`, `/ask`, `/build-graph`, `/lint`, `/consolidate` — каждый делает
одно дело, append-only, идемпотентно (build-graph), с явным алгоритмом
(в самих markdown-файлах skill'ов).

Прошлый импорт 30 ideas: ~3 часа. Текущий (31-60): ~22 минуты — **8× быстрее**
не из-за параллелизма (он не сработал из-за 529), а потому что skill'ы
хорошо делятся на bulk-операции (Python для raw + sources, Claude для
ideas-страниц). Архитектура skill'ов это позволяет.

## 3 ключевых gap'а (что не работает)

### 1. Multi-agent orchestration — фикция на 2026-04-16

CLAUDE.md и `ARCHITECTURE.md` описывают систему «12 agents in production
running an AI consulting business». Файлы существуют. Реальность:

- **6 mailbox'ов пустые**: inbox-processor, knowledge-synth, meta-agent,
  personal-assistant, sales-outreach, sales-researcher.
- **Остальные 6** содержат **только тестовый трафик** от 14-15 апреля
  (`msg-20260414-001..010`, `msg-20260415-001`). Production-сообщений = 0.
- Pipeline'ы (`scripts/morning-pipeline.sh`, `evening-pipeline.sh`) **не на
  cron'е**, запускаются только вручную.
- `tools/distribute.py.bak` — намеренно отключён.
- `meta-agent` и `strategist` работают в `permissionMode: plan` — пишут
  планы, не исполняют.
- В `agents/{id}/strategies.md` нет ни одного накопления System Prompt
  Learning.
- В `logs/audits/` — пусто.

**Что есть на самом деле:** один Claude Code, выполняющий задачи сам,
изредка дёргающий subagent'ов через Task tool. «12 агентов» — это сейчас
12 agent definition files, 24 niche symlinks и 12 пустых mailbox'ов.

### 2. Notion MCP — single-point-of-failure

8 из 12 агентов и 4 skill'а (`/plan-day`, `/close-day`, manager workflow,
inbox-processor) полагаются на `mcp__notion-*` методы для:

- Создания/обновления Daily Log в Notion.
- Записи идей в Банк идей.
- Чтения Командного центра.
- Обновления project page'й.

**На этой сессии Notion MCP отключился среди работы** (system reminder:
"following deferred tools are no longer available... mcp__notion-*").
В этот момент `manager`, `inbox-processor`, `personal-assistant`,
`sales-lead`, `knowledge-synth`, `life-coach`, `crazy-agent`, `meta-agent`
+ `/plan-day`/`/close-day` теряют ключевую функциональность.

Дублирующего fallback'а на локальный файл (`raw/notion-export/`) нет.
`tools/sync_context.py` существует, но не вызывается из skill'ов
автоматически.

### 3. Долговая яма из 3 нерешённых миграций

`reports/arch-migration-2026-04-16.md` фиксирует 5 open questions для Руслана.
Все 5 — на 2026-04-16 — **не разрешены**, при этом новые слои поверх уже
строятся:

| # | Open question | Статус |
|---|---------------|--------|
| 1 | `baseline.md` vs `system.md` (canonical для каждого агента) | не выбран; обе содержат идентичный текст |
| 2 | `.claude/skills/ingest.md` vs `ingest.md.new` (2 версии) | старая версия в `ingest.md`; новая (та, по которой реально работали все 60 ingest'ов) интегрирована, `ingest.md.new` отсутствует — но конфликт изначально не ревьюился |
| 3 | `knowledge-base/` → `wiki/` migration | 0/4 кластеров перенесено (`MIGRATION.md` показывает все галочки `[ ] не начато`) |
| 4 | Obsidian vault scope (только `wiki/` или весь репо) | без явного решения; vault открыт на `wiki/` |
| 5 | niche `global` (папка или только enum) | папки нет, enum есть, никто не использует |

Плюс новые расхождения (см. §3.3 gap-list): orphan `agents/content-team/`,
`agents/research-team/`, `agents/sales-team/` папки; mismatch `crazy-agent`
tools между CLAUDE.md и фактическим frontmatter; отсутствующий
`comms/escalation.jsonl`.

**Это — typical multi-phase architectural drift.** Phase 2 закрыта формально,
но debt не оплачен. Перед Phase 3 имеет смысл провести закрывающую сессию по
этим 5 + новым пунктам, иначе слой за слоем будет наращивать sloppiness.

## Рекомендация по дальнейшему движению (одно предложение)

Прежде чем оживлять multi-agent orchestration — закрыть `MIGRATION.md` open
questions + добавить fallback на локальные exports для Notion-зависимых
skill'ов; иначе развитие будет строиться на нестабильном основании.
