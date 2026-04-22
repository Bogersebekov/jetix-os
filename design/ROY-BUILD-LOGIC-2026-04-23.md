---
title: ROY Build Logic — where agents live + how they communicate + how CC launches them
date: 2026-04-23
status: approved-by-ruslan
parent_notion: https://www.notion.so/34a2496333bf81d1b5b6eeb9819eedd2
supersedes: none
type: design
---

# ROY Build Logic — утверждённая архитектура построения роя

Фиксация alignment session Ruslan ↔ Cloud Cowork 2026-04-23 по Шагу 2.2.1.
Без этих решений master prompt для Шага 2.2.4 (agent construction) не может
быть написан — эти параметры определяют **где** файлы физически лежат,
**как** cells коммуницируют, **как** Claude Code orchestrates, и **как** не
сломать existing систему в процессе.

---

## 1. Location — где файлы агентов и swarm runtime data лежат

**Утверждённый hybrid подход:**

### 1.1 Agent system prompt files → `.claude/agents/` (native location)

Файлы агентов кладутся в **native Claude Code agent location**, потому что
Claude Code auto-discovery работает на `.claude/agents/*.md` top-level only.
Subdirectories не auto-discoverable; custom paths требуют explicit param,
которого Task tool в текущей версии не имеет.

```
.claude/agents/
├── [14 legacy files]            # ОСТАЮТСЯ нетронутыми (существующие workflows)
├── brigadier.md                 # НОВЫЙ, ~1500-3000 строк
├── engineering-expert.md        # НОВЫЙ
├── mgmt-expert.md               # НОВЫЙ
├── systems-expert.md            # НОВЫЙ
├── philosophy-expert.md         # НОВЫЙ
└── investor-expert.md           # НОВЫЙ
```

**Legacy 14 files не трогаем** в Phase A. Они продолжают работать для
existing workflows. Deprecation decision — отдельно после того как new
swarm proven в production.

**Namespace collision check** (легaси vs new):
- Legacy: `manager`, `personal-assistant`, `system-admin`, `sales-lead`,
  `sales-researcher`, `sales-outreach`, `inbox-processor`, `crazy-agent`,
  `knowledge-synth`, `strategist`, `life-coach`, `meta-agent`,
  `staging-writer`, `sweep-worker`
- New: `brigadier`, `engineering-expert`, `mgmt-expert`, `systems-expert`,
  `philosophy-expert`, `investor-expert`
- **No collisions** ✅

### 1.2 Swarm runtime data → `swarm/` top-level folder

Всё swarm-specific data — в отдельной папке top-level, **не ломая**
existing `wiki/` / `knowledge-base/` / `decisions/` / `raw/` structures.

```
swarm/
├── README.md                    # навигация + usage guide
│
├── wiki/                        # task-scoped + global wiki (v3 spec TBD in 2.2.3)
│   ├── tasks/                   # per-task scoped subdirs
│   │   └── <task-id>/
│   │       ├── context/         # domain-filtered material из Private Library
│   │       ├── artefacts/       # expert outputs накопительно
│   │       ├── decisions/       # brigadier integration decisions
│   │       └── open-questions.md
│   ├── global/                  # накопленные compound learnings (post-task)
│   ├── concepts/                # Karpathy LLM Wiki pattern (entities, concepts)
│   ├── graph/edges.jsonl        # typed relationships (GraphRAG influence)
│   └── _templates/              # entity/concept/claim templates (уже есть в existing wiki/)
│
├── strategies/                  # per-expert долгая память (Compound step appends)
│   ├── brigadier.md
│   ├── engineering-expert.md
│   ├── mgmt-expert.md
│   ├── systems-expert.md
│   ├── philosophy-expert.md
│   └── investor-expert.md
│
├── scratchpads/                 # working memory (эphemeral, .gitignored)
│   └── <agent>.md               # cleared after each cycle
│
├── gates/                       # AWAITING-APPROVAL gate files
│   └── <topic>-<date>.md
│
├── mailboxes/                   # async queue (fallback, minimal Phase A)
│   └── <agent>.jsonl
│
└── logs/                        # cycle logs for audit trail
    └── <cycle-id>.md
```

### 1.3 Что НЕ трогаем
- `.claude/agents/*.md` (14 legacy) — нетронуты
- `wiki/` top-level (existing Karpathy v2 wiki with `concepts/`, `sources/`, etc.)
- `knowledge-base/` (migration в процессе, см. `MIGRATION.md`)
- `decisions/`, `design/`, `raw/`, `prompts/`, `tools/`
- `CLAUDE.md` + `.claude/rules/`
- Existing `.claude/skills/`

### 1.4 Rationale
- **Изоляция:** swarm operates в своей sandbox без перекрёстных эффектов на legacy workflows
- **Reversibility:** если swarm fails — `rm -rf swarm/ && rm .claude/agents/{brigadier,*-expert}.md` возвращает систему к pre-swarm state
- **Co-existence:** legacy + new запускаются параллельно без conflicts
- **Git-tracked:** вся swarm data (кроме scratchpads) auditable через git history

---

## 2. Communication — 3 layer механика

### 2.1 Layer 1 — Task tool invocation (PRIMARY, direct)

**Механика:** Brigadier — единственный caller. Experts invokable только через
Task tool.

**Canonical invocation (pseudocode inside brigadier reasoning):**

```python
result = Task(
    subagent_type="engineering-expert",
    description="Review termination stack for over-engineering",
    prompt="""
    Mode: critic
    Task context: <task-id>=T1 (design co-evolution loop with partners)
    Input artefact: swarm/wiki/tasks/T1/context/termination-stack-draft.md
    Canonical lens: Ousterhout deep-modules + Brooks accidental complexity
    Output file: swarm/wiki/tasks/T1/artefacts/eng-critic-01.md
    Success predicate: 3+ concrete over-engineering flags with book citations.
    Max turns: 25
    """
)
```

**Sub-agent execution:**
- Task spawn-ит fresh Claude Code instance в isolated context window
- Sub-agent reads `.claude/agents/engineering-expert.md` system prompt
- Sub-agent parses `Mode: critic` prefix → activates critic mode section
- Sub-agent reads input artefact paths из prompt
- Sub-agent produces output artefact in wiki
- Sub-agent returns summary string to brigadier (not full artefact — artefact
  is written, summary is delta + verdict)

**Why Layer 1 primary:**
- Native Claude Code primitive, battle-tested
- Fresh context per sub-agent → no cross-contamination
- Parallel invocation supported: brigadier spawns 4 critics concurrently, all
  return when done
- Brigadier stays in control — can gate, integrate, or re-invoke

### 2.2 Layer 2 — Stigmergic through wiki (SHARED STATE, indirect)

**Механика:** Experts не говорят друг с другом напрямую. Координация через
shared environment — `swarm/wiki/`.

**Flow:**
1. Expert A (engineering × critic) writes artefact to
   `swarm/wiki/tasks/T1/artefacts/eng-critic-01.md`
2. Brigadier reads Expert A's artefact + commits it
3. Brigadier invokes Expert B (philosophy × critic) with prompt pointing to
   Expert A's artefact as input reference
4. Expert B reads artefact, produces own artefact
   (`swarm/wiki/tasks/T1/artefacts/phil-critic-01.md`)
5. Brigadier invokes Integrator cell с inputs = оба artefacts
6. Integrator writes synthesized artefact

**Single-writer rule Phase A:**
- **Only brigadier commits to `swarm/wiki/`.** Experts produce artefacts,
  brigadier picks them up from Task return + commits them.
- Предотвращает race conditions (multiple cells writing simultaneously).
- Phase B+: CRDT/MVCC может быть введён если contention observed
  (see ALIGN §10).

**Provenance mandatory on every wiki entry:**
```yaml
---
source: <input artefact path(s)>
captured_by: <agent-name> × <mode>
captured_date: YYYY-MM-DD
task_id: <task-id>
commit_sha: <git sha после commit>
---
```

**Why Layer 2 critical:**
- Eliminates Flappy Bird summary-passing fragility (AP-1)
- Provides audit trail (all cell outputs in git history)
- Enables future analysis (Phase B swarm reads own past artefacts)
- Allows task-scoped compound effect (Ruslan's insight; Wiki v3 spec в 2.2.3)

### 2.3 Layer 3 — Mailbox JSONL (FALLBACK, async edge-cases)

**Механика:** Per-agent JSONL queue в `swarm/mailboxes/<agent>.jsonl`.

**Usage Phase A:** минимизирован. Используется только для:
- Async notifications (expert finds critical issue after return, notifies
  brigadier без нового Task invocation)
- Escalation messages (HITL triggers)
- Cross-cycle messaging (if applicable)

**Message schema:** inherits from `shared/schemas/message.schema.json`
(existing).

**Why Layer 3 de-emphasized в Phase A:**
- Stigmergic через wiki достаточно для 95% coordination
- Mailboxes добавляют state которое нужно manage
- Master synthesis Part 5 §5.5 favors wiki-first

---

## 3. Claude Code launch pattern — single session, brigadier as entry

**Утверждённая модель:** **Single tmux session** на сервере. Brigadier =
entry point. Experts = sub-agents через Task tool.

### 3.1 Launch procedure

```bash
# On server (ruslan@100.99.156.28):
ssh ruslan@100.99.156.28
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34

# Max subscription discipline:
unset ANTHROPIC_API_KEY                  # prevents accidental API billing
unset GROQ_API_KEY 2>/dev/null           # if Whisper pipeline not in use

# Isolated tmux session:
tmux new -ds roy-<task-id>

# Inside tmux:
claude --dangerously-skip-permissions
```

### 3.2 First message pattern

```
You are operating as the brigadier agent in the Jetix swarm. Read
.claude/agents/brigadier.md for your full system prompt.

Current task: [Ruslan's task description, full paste]

Task ID: <task-id>
Operating mode: [Full-Auto | Stage-Gated]

Proceed per brigadier protocol (intake → decompose → invoke cells →
integrate → gate → compound → report).
```

### 3.3 Execution flow

1. **Claude Code** reads `.claude/agents/brigadier.md` (system prompt)
2. **Brigadier** analyzes task, writes plan в scratchpad
3. **Brigadier** initializes `swarm/wiki/tasks/<task-id>/` (creates subdirs)
4. **Brigadier** decomposes task into cell invocations per §4.8 decision tree
5. **Brigadier** invokes matrix cells via Task tool:
   ```
   Task(subagent_type="<domain>-expert", prompt="Mode: <mode>\n<context>")
   ```
6. **Sub-agents** execute in parallel or sequential, return artefact paths +
   summaries
7. **Brigadier** reads artefacts, commits to wiki
8. **Brigadier** invokes Integrator cell для synthesis
9. **Brigadier** создаёт gate file `swarm/gates/<topic>-<date>.md` if
   Stage-Gated mode + gate trigger
10. **If gate:** brigadier commits, pushes, pauses
11. **On Ruslan approval:** brigadier continues
12. **Compound step:** brigadier extracts rules → writes to `swarm/strategies/<expert>.md`
13. **Brigadier** writes cycle log `swarm/logs/<cycle-id>.md`, commits, ends
    session OR continues next task

### 3.4 Detach procedure

```
Ctrl+B, D      # detach from tmux session, swarm continues in background
```

### 3.5 Monitoring without SSH

GitHub commits feed: https://github.com/Bogersebekov/jetix-os/commits/claude/jolly-margulis-915d34

Expected commit sequence per task:
- `[brigadier] T1 intake + plan`
- `[brigadier] T1 cell invocation: engineering × critic`
- `[artefact] T1 eng-critic-01 (mode: critic)`
- `[artefact] T1 phil-critic-01 (mode: critic)`
- `[artefact] T1 eng-integrator-01 (synthesis of 2 critics)`
- `[gate] T1 AWAITING-APPROVAL <topic>` (if Stage-Gated)
- `[brigadier] T1 compound step: 2 rules → strategies/engineering-expert.md`
- `[brigadier] T1 complete: cycle log written`

### 3.6 Why single-session (not multi-tmux)

**Pros:**
- Atomic: одна session = один task = one git audit trail
- Stage-Gated работает natively (brigadier pauses entire session at gate)
- Shared filesystem context — все cells видят one wiki state
- Simpler cost tracking (один `tmux` = один Max-subscription quota usage)

**Cons accepted:**
- Brigadier's main context holds orchestration state across turns — может
  приблизиться к context window limit на long tasks. Mitigation:
  CLAUDE.md hierarchical lazy-load + brigadier regularly offloads state
  to wiki + new session после каждого big task.

**Alternatives rejected:**
- **Multi-tmux parallel** (each expert own session) — no native
  coordination, manual sync hell, Stage-Gated impossible.
- **Daemon mode** (persistent brigadier process) — complex infrastructure,
  overkill для Phase A.

---

## 4. Task-scoped wiki assembly (Ruslan's 2026-04-23 insight)

**Status:** approved conceptually, **detailed spec deferred to Шаг 2.2.3**
(Wiki v3 spec document).

### 4.1 Core concept

Wiki **не generic KB.** Wiki собирается **under the specific task** being
solved, and **layers stack** as tasks accumulate.

### 4.2 Layering mechanism (high-level)

1. **Task T1 arrives:**
   - Brigadier initializes `swarm/wiki/tasks/T1/` with subdirs
   - Brigadier populates `context/` with domain-filtered slice из:
     - Private Library (books relevant to T1 domains)
     - `decisions/` (current approved decisions)
     - 24 Locks subset applicable to T1
     - Previous relevant global learnings (empty for T1)
   - Task T1 scope is everything inside `swarm/wiki/tasks/T1/`
2. **Cells work within T1 scope:**
   - Expert reads own `strategies.md` + T1 `context/` + T1 prior artefacts
   - Expert produces artefacts into T1 `artefacts/`
3. **T1 completion — compound step:**
   - Brigadier extracts generalizable rules → `swarm/strategies/<expert>.md`
   - Brigadier copies reusable artefacts to `swarm/wiki/global/` with
     provenance (source: task=T1, captured_date, commit_sha)
   - T1 task-scoped wiki preserved в `swarm/wiki/tasks/T1/` (audit trail)
4. **Task T2 arrives (later):**
   - Brigadier initializes `swarm/wiki/tasks/T2/`
   - Brigadier populates `context/` including **relevant slices из
     `swarm/wiki/global/`** (learnings from T1 that apply)
   - T2 operates с **layered context** — own scope + global learnings

### 4.3 Compound effect applied to tasks

After N tasks:
- Global wiki contains N layers of learnings
- Each new task gets baseline + progressively richer global reference
- Experts' strategies.md have accumulated N cycles' rules
- Swarm becomes measurably smarter per task completion

### 4.4 Details TBD in Шаг 2.2.3

- How `context/` populated — manual brigadier decision or automatic
  retrieval (HippoRAG-style PPR)?
- What gets promoted to global vs stays task-local?
- Retention policy for task-scoped wikis (archive after N weeks?)
- Multi-task context fusion heuristics
- Taxonomic integration: Karpathy LLM Wiki + GraphRAG typed edges +
  Zettelkasten atomic notes + HippoRAG retrieval — how unified

Input: `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
(828 lines, covers all these patterns).

---

## 5. What does NOT break in existing system

Explicit list of untouched systems:

- `.claude/agents/*.md` (14 legacy files) — продолжают работать для current
  workflows (personal-assistant, manager, sales-lead, system-admin, etc.)
- `wiki/` top-level — existing Karpathy v2 wiki remains functional
- `knowledge-base/` — migration в процессе per `MIGRATION.md`
- `decisions/`, `design/`, `raw/`, `prompts/`, `tools/` top-level structure
- `CLAUDE.md` + `.claude/rules/global.md`
- Existing `.claude/skills/` (plan-day, close-day, ingest, ask, lint, etc.)
- Voice-notes pipeline, content pipeline, Notion integrations, MCP servers

**Rollback path if swarm fails:**
```bash
rm -rf swarm/
rm .claude/agents/{brigadier,engineering-expert,mgmt-expert,systems-expert,philosophy-expert,investor-expert}.md
git commit -m "[rollback] swarm Phase A retired"
```
→ Система back to pre-swarm state, legacy 14 agents + existing wiki все
ещё работают.

---

## 6. Approval

**Approved by Ruslan, 2026-04-23.** Verbatim quote:

> «ну интересно тогда дофиксируй все эти фиксирую все мои решения получается
> эту логику построения я подтверждаю все ее фиксируем отлично насчет вот
> коммуницируют 3 слой механика в принципе тоже отлично вот особенно как я
> понимаю две самые важные вот бригадир первый вариант и 2-й [layer] особенно
> вот [layer] 2 у нас будет отдельный глубокий раздел в итоге это тоже
> подтверждаю окей отлично в принципе ну посмотрим потом как этот клауд код
> будет с этим работать в целом окей насчет и википедии мы потом ее еще
> разберем глубже в итоге вот это все что ты там написал я подтверждаю что
> можем идти дальше делать»

---

## 7. Ссылки

- Parent Notion: [🏗️ Шаг 2.2](https://www.notion.so/34a2496333bf81d1b5b6eeb9819eedd2)
- Grand-parent Notion: [🤖 Шаг 2](https://www.notion.so/34a2496333bf817d93bff4cb66775587)
- Inputs:
  - `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` (blueprint)
  - `decisions/ROY-ALIGNMENT-2026-04-22.md` (base params)
  - `raw/research/knowledge-architecture-deep-research-2026-04-19.md` (wiki v3 source)

## 8. Next step

**Шаг 2.2.2** — детальный разбор структуры агента изнутри (что в каждой
section system prompt'а, как mode-switching работает mechanically, как
strategies.md читается каждый invocation, как Compound step пишет rules).
