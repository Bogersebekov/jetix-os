---
type: design-document
status: v1-beta-FINAL
approval-status: approved-by-ruslan-2026-04-18
stage: technical-synthesis
version: v1-beta-FINAL-2026-04-18
owner: ruslan
created: 2026-04-18
finalized: 2026-04-18
summary-ref: design/SYSTEM-DESIGN-TECH-SUMMARY.md
related:
  - design/SYSTEM-DESIGN-TECH.md
  - design/SYSTEM-DESIGN-TECH-SUMMARY.md
  - design/AGENT-PROTOCOLS.md
  - design/ARCHITECTURE-TARGET.md
  - design/IMPLEMENTATION-PLAN-2026-04-18.md
status: archived
archived_at: 2026-05-06
archived_reason: v1-beta design (April 2026) — superseded by Foundation v1.0 + Документ 1A/1B
moved_by: canonical-cleanup-2026-05-06 (Ruslan walkthrough ack via CANONICAL-WALKTHROUGH-2026-05-06.md)
---

# DATA-FLOWS.md — Jetix OS data flows v1-beta

> **Scope.** 7 канонических data flows + state machines + writeback loops.
> Дополняет SYSTEM-DESIGN-TECH.md §8 (Runtime view). Visual-first — mermaid
> диаграммы с прозаической подписью + failure modes.
>
> **Для кого.** Агенты при выполнении flows; Ruslan для operational review;
> новые collaborators для понимания dynamics системы.

---

## §F.0 Flow catalog

| # | Flow | Trigger | Primary output | Section |
|---|------|---------|----------------|---------|
| F1 | Morning ritual (`/plan-day`) | Ruslan command | Daily Log plan section | §F.1 |
| F2 | Voice-memo → wiki | Voice file drop + Ruslan `/ingest` | Wiki pages + edges | §F.2 |
| F3 | External content → wiki (`/ingest <source>`) | Ruslan command | Wiki pages + edges + writeback | §F.3 |
| F4 | Query + writeback (`/ask <question>`) | Ruslan command | Answer + citations + optional comparisons | §F.4 |
| F5 | Evening ritual (`/close-day`) | Ruslan command | Daily Log closed + distillate routed | §F.5 |
| F6 | Weekly natyagivanie (`/cross`) | Ruslan command | Cross-report + new tasks + insights | §F.6 |
| F7 | Error flow (SAFE-SAVE) | Any error / unclear | Commit + scratchpad + escalation | §F.7 |
| F8 | Notion migration (α/β/γ/δ) | Ruslan per phase | Raw dumps + wiki ingests | §F.8 |

**State machines (entities lifecycle):** §F.9.

**Cross-cutting flow invariants:** §F.10.

---

## §F.1 Morning ritual (`/plan-day`)

### F.1.1 Trigger & preconditions

**Trigger:** Ruslan запускает `./jetix morning` или `/plan-day` в Claude Code.

**Preconditions:**
- `daily-log/{today}.md` ещё не создан (или создан template'ом).
- `strategy/life/` содержит текущий weekly + monthly docs.
- Нет in-progress блокеров (SAFE-SAVE состояния должны быть resolved).

### F.1.2 Sequence diagram

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant CC as Claude Code
    participant Day as daily-log/
    participant Prev as previous daily-log
    participant Foc as shared/state/focus.json
    participant Strat as strategy/life/weekly
    participant Month as strategy/life/monthly
    participant Proj as shared/state/active-projects.json
    participant Events as shared/events.jsonl
    participant Git as git

    R->>CC: ./jetix morning (или /plan-day)
    CC->>Day: Read YYYY-MM-DD.md (empty or template)
    CC->>Prev: Read previous-day.md close-day section
    CC->>Foc: Read focus.json
    CC->>Strat: Read 2026-Wnn-weekly.md
    CC->>Month: Read 2026-MM-monthly.md
    CC->>Proj: Read active-projects.json (next_action per project)
    CC-->>R: "Вчера: X closed, Y blocked. Week focus: Z.<br/>Предлагаю сегодня: A / B / C. Что выбираем?"
    R->>CC: "Фокус — A. Key actions — 1, 2, 3"
    CC->>Day: Write plan section (focus, key actions, estimated time)
    CC->>Foc: Update focus.today = "A"
    CC->>Events: Append {"type":"ritual.morning.closed","actor":"central","ref":"daily-log/YYYY-MM-DD.md"}
    CC->>Git: commit "[daily] plan YYYY-MM-DD: focus A"
    CC->>Git: push origin main
    CC-->>R: "Plan зафиксирован. Commit {sha}."
```

### F.1.3 Steps (prose)

1. **Read strategic context:** weekly, monthly, yearly (if quarterly review approaching).
2. **Read operational state:** `focus.json`, `priorities.json`, `active-projects.json`.
3. **Read recent daily-log + open tasks** from `tasks/master.md` + per-project tasks.
4. **Read previous close-day** — what was planned для сегодня?
5. **Synthesize draft plan:** Focus of day + 3-5 key actions + estimated time + risks.
6. **Show plan к Ruslan → Ruslan approves/edits.**
7. **Write `daily-log/{today}.md`** с frontmatter (type: daily-log, date, focus, status).
8. **Emit event:** `ritual.morning.closed` к `shared/events.jsonl`.
9. **Commit + push.**

### F.1.4 Failure modes

| Failure | Response | Recovery |
|---------|----------|----------|
| Notion MCP down | Skip Notion steps; use local daily-log only | Proceed — Notion not on critical path for plan |
| Strategy weekly missing | Offer "create weekly first?" короткий dialog | Don't skip; weekly drives daily focus |
| Rate limit 529 | 3× backoff; then SAFE-SAVE drafts | Resume when API back |
| Ruslan пропустил close-day yesterday | Detect; offer short recap first | ≤5 min recover |
| Ruslan offline → no approval | SAFE-SAVE draft plan; mark "awaiting approval" | Resume on return |

### F.1.5 Quality focus

- **Time:** complete < 60s end-to-end with approval.
- **Learnability:** новый user понимает ритуал с первого раза через explicit
  4 questions pattern.

---

## §F.2 Voice-memo → wiki flow

### F.2.1 Trigger & preconditions

**Trigger:** Ruslan записал voice-memo → drops в `raw/voice-memos/`. После —
запускает pipeline:

```bash
python3 tools/transcribe.py    # OGG/MP3 → transcript
python3 tools/extract.py       # transcript → items (decisions, tasks, ideas, contacts)
python3 tools/filter.py        # dedup + meta
python3 tools/review_report.py # markdown review in ~/review-latest.md
# ← STOP: Ruslan reviews ~/review-latest.md
# Manually: /ingest per approved item (no automatic distribute)
```

**Preconditions:** Groq Whisper API doступен (SHOULD); distribute.py.bak — disabled
(HUMAN §CLAUDE.md + ADR — human review obligatory).

### F.2.2 Pipeline diagram

```mermaid
flowchart TB
    Voice[("🎤 raw/voice-memos/YYYY-MM-DD-HHMMSS.ogg")]

    subgraph Pipeline["tools/ (Python)"]
        Transcribe["transcribe.py<br/>(Groq Whisper)"]
        Extract["extract.py (Claude)"]
        Filter["filter.py (dedup + meta)"]
        Review["review_report.py"]
    end

    Transcripts["raw/transcripts/YYYY-MM-DD-HHMMSS.txt"]
    Items["Structured items (in-memory JSON)"]
    Filtered["Filtered items"]
    Report["reports/review_YYYY-MM-DD.md<br/>+ ~/review-latest.md"]

    STOP{"🛑 HUMAN GATE<br/>Ruslan reviews"}

    subgraph Manual["Manual routing (by Ruslan, optionally with Claude)"]
        IngestIdeas["/ingest → wiki/ideas/"]
        AddTasks["append tasks/master.md or projects/{x}/tasks.md"]
        AddContacts["append crm/"]
        AddDecisions["append decisions/"]
    end

    Voice --> Transcribe --> Transcripts
    Transcripts --> Extract --> Items
    Items --> Filter --> Filtered
    Filtered --> Review --> Report
    Report --> STOP
    STOP -->|"approved insight"| IngestIdeas
    STOP -->|"approved task"| AddTasks
    STOP -->|"approved contact"| AddContacts
    STOP -->|"approved decision"| AddDecisions

    classDef voice fill:#f9d5e5,stroke:#333;
    classDef raw fill:#c6dcff,stroke:#333;
    classDef stop fill:#ff6b6b,color:white,stroke:#333,stroke-width:3px;
    classDef manual fill:#adf0c7,stroke:#333;
    class Voice voice;
    class Transcripts,Items,Filtered,Report raw;
    class STOP stop;
    class IngestIdeas,AddTasks,AddContacts,AddDecisions manual;
```

### F.2.3 Output locations

- Voice file: remains в `raw/voice-memos/` (immutable).
- Transcript: `raw/transcripts/YYYY-MM-DD-HHMMSS.txt` (UTF-8 russian).
- Review report: `reports/review_YYYY-MM-DD.md` + copy в `~/review-latest.md`.
- After Ruslan routing: varies (wiki/ideas, tasks, crm, decisions).

### F.2.4 Failure modes

| Failure | Response |
|---------|----------|
| Transcription timeout | Retry 1×; if fail → item unprocessed, Ruslan notified |
| `extract.py` malformed JSON | `filter.py` safely drops bad records + logs |
| Review report generation fail | Partial report saved + error note |
| Groq rate limit | Backoff + retry; manual fallback possible (Ruslan types) |

### F.2.5 Metrics

- Voice→transcript latency < 30s for 10-min memo (measurable).
- Extract precision ≥80% (Ruslan reviews, subjective for v1-beta; v1-final golden fixtures).

### F.2.6 Why human gate обязательный

`distribute.py.bak` — disabled намеренно. Claude-выводы **не попадают в KB без
human review**. Rationale:
- Hallucination risk (R-10) → wiki pollution compounding.
- Context-specific routing decisions Ruslan understands better (task vs idea
  vs project).
- "Слоу" (slower) но safer pipeline.

---

## §F.3 External content → wiki (`/ingest <source>`)

### F.3.1 Trigger & preconditions

**Trigger:** Ruslan passes URL or file path к `/ingest`.

**Preconditions:**
- File exists OR URL доступен via WebFetch.
- Git working copy clean (или accepted uncommitted).
- Wiki templates in `wiki/_templates/` loadable.

### F.3.2 Sequence diagram

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant CC as Claude Code
    participant Raw as raw/{type}/{path}
    participant Tmpl as wiki/_templates/
    participant Wiki as wiki/{entity}/
    participant Idx as wiki/index.md
    participant LogMD as wiki/log.md
    participant Edges as wiki/graph/edges.jsonl
    participant Niche as wiki/niches/
    participant Events as shared/events.jsonl
    participant Git as git

    R->>CC: /ingest <path|url>
    CC->>Raw: Read source (or WebFetch + persist to raw/web/)
    CC->>Tmpl: Load relevant entity templates
    CC-->>R: "Parsed. Will create: 1 source, N ideas/claims/concepts. OK?"
    R->>CC: "OK"

    loop For each entity extracted
        CC->>Wiki: Check existence by slug
        alt New
            CC->>Wiki: Create wiki/{type}/{slug}.md with frontmatter
        else Existing
            CC->>Wiki: Append section (with update marker)
        end
    end

    CC->>Wiki: Create wiki/sources/YYYY-MM-DD-{slug}.md (citation + claims extracted)
    CC->>Edges: Append N new edges (derived_from, supports, extends)
    CC->>Idx: Append catalog lines
    CC->>Niche: Update niches/{niche}/README.md backlinks
    CC->>LogMD: Append "YYYY-MM-DD HH:MM | ingest | {slug} | N pages, M edges"
    CC->>Events: Append {"type":"idea.ingested"...}, {"type":"source.added"...}, {"type":"edge.added"...} × M
    CC->>Git: commit "[wiki] ingest: {source_title}"
    CC->>Git: push origin main
    CC-->>R: "Done. N pages, M edges. Niche: {list}. Commit {sha}."
```

### F.3.3 Steps (prose)

1. **Fetch source:** WebFetch (URL) или Read (file path).
2. **Persist raw** in `raw/web/` (if URL) или verify `raw/*` location.
3. **LLM pass:** identify entity types (concept/entity/claim/idea), extract key
   facts, map to 9 types. Apply confidence scores (see invariant I-09):
   - Явная цитата → 0.8-1.0.
   - Inferred → 0.5-0.7.
4. **For each identified entity:**
   - Check existence by slug (wiki already has? `wiki/{type}/{slug}.md`).
   - If new → create with template + frontmatter.
   - If exists → append section, mark update.
5. **Create source card** `wiki/sources/YYYY-MM-DD-{slug}.md`:
   - Citation (URL, author, date).
   - Claims extracted (with confidence).
   - Topics.
6. **Append edges** to `edges.jsonl`:
   ```json
   {"from":"wiki/sources/...","to":"wiki/concepts/...","type":"supports","created":"YYYY-MM-DD","origin":"/ingest","confidence":0.85,"valid_from":"YYYY-MM-DD"}
   ```
7. **Update `index.md`** with new page refs.
8. **Update niche READMEs** (backlinks for niche navigation).
9. **Append `log.md`** event.
10. **Emit events** к `shared/events.jsonl`.
11. **Commit + push.**

### F.3.4 Output summary

- 1 source page + N entity pages + M edges + index entries + log entry.
- Event trail в `shared/events.jsonl`.
- Chat report: "N pages, M edges, niche: {list}, confidence avg {X}".

### F.3.5 Failure modes

| Failure | Response |
|---------|----------|
| WebFetch 403/404 | Report error; ask Ruslan alternative |
| LLM can't parse (corrupted PDF) | Fallback: source-only page + claim "needs manual extraction" |
| Duplicate detected (high similarity) | Suggest `/consolidate`; default merge in-place + notice |
| Malformed content (unexpected format) | Partial ingest + report к Ruslan |
| Git push fail | SAFE-SAVE, note "push pending" |

---

## §F.4 Query + writeback (`/ask <question>`)

### F.4.1 Trigger & preconditions

**Trigger:** Ruslan asks через `/ask` or `./jetix ask "..."`.

**Preconditions:**
- wiki/ populated (index.md, edges.jsonl existent).
- Anthropic API available (else Kay mode: grep-only search + Ruslan reads raw).

### F.4.2 Sequence diagram (with HippoRAG PPR)

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant CC as Claude Code
    participant Idx as wiki/index.md
    participant Sum as wiki/graph/summaries.md
    participant PPR as wiki/graph/PPR index (derived)
    participant Pages as wiki/{entity}/
    participant Comp as wiki/comparisons/
    participant Q as wiki/questions/
    participant Edges as wiki/graph/edges.jsonl
    participant LogMD as wiki/log.md
    participant Events as shared/events.jsonl
    participant Git as git

    R->>CC: /ask "<question>"
    CC->>Idx: Read catalog
    CC->>Sum: Read community digests
    CC->>PPR: Compute seed nodes (keyword match) → PPR → top-20
    CC->>Pages: Load 5-15 selected pages (PPR ranked)
    CC-->>R: [streaming synthesis with citations [[page]] [[page]]...]

    alt Writeback-worthy answer<br/>(new link / contradiction / synthesis 5+ pages / practical insight)
        R->>CC: "save it" (explicit)
        CC->>Comp: Write comparisons/YYYY-MM-DD-{slug}.md
        CC->>Edges: Append new edges
        CC->>Q: Write questions/YYYY-MM-DD-{slug}.md (reverse index)
        CC->>Idx: Append new entries
        CC->>LogMD: Append "comparison.written" event
        CC->>Events: Append event
        CC->>Git: commit "[wiki] ask writeback: {slug}"
        CC->>Git: push
        CC-->>R: "Saved. {N} new edges. Will be referenced в следующем /ask."
    else Just response
        CC-->>R: [answer, no writeback]
    end
```

### F.4.3 Writeback criteria

`comparisons/` write ONLY if ≥1 of:
- **Новая связь** между 2+ pages (создаёт ≥1 new edge).
- **Contradiction detected** → edge type `contradicts`.
- **Синтез по 5+ pages** (summary level).
- **Practical insight** с applicability.

Иначе — просто ответ в чате без writeback.

### F.4.4 HippoRAG PPR (invariant I-27)

**Algorithm (simplified):**
```python
def hipporag_retrieve(question, k=20):
    seeds = keyword_match(question, wiki_index)  # lexical seeds
    pagerank_scores = personalized_pagerank(
        graph=load_edges_jsonl(),
        seeds=seeds,
        damping=0.85,
    )
    top_k = sorted(pagerank_scores.items(), key=lambda x: -x[1])[:k]
    return [page for page, _ in top_k]
```

**Implementation:** `tools/hipporag.py` ~50 LOC (networkx + pagerank).

**Cache:** after each `/build-graph`, precompute PPR for common seed-sets →
`wiki/graph/PPR-cache.json`. Refresh when edges.jsonl grows >10%.

### F.4.5 Reverse index `wiki/questions/` (invariant I-30)

Every `/ask` → save:

```markdown
---
type: question
created: YYYY-MM-DD
times-asked: 1
last-asked: YYYY-MM-DD
similar-to: []  # linked on re-ask
status: answered
---

# Question: {question text}

## Short synth
{2-3 sentences answer summary}

## Top 5 relevant pages
- [[wiki/ideas/focus-theory]]
- [[wiki/claims/brooks-law]]
- ...

## Answer generated at {timestamp}
[full answer, as given to Ruslan]
```

**Repeat query:** detects similar existing entry, inc'its `times-asked`, shows
prior answer + **diff** (what's changed since `last-asked`).

### F.4.6 Failure modes

| Failure | Response |
|---------|----------|
| Vague question | Claude asks clarification |
| No relevant pages | "No wiki support; proceed with uncited opinion? y/n" |
| Rate limit | Partial answer from already-loaded pages + SAFE-SAVE + retry suggestion |
| PPR computation fail | Fallback: lexical match only (degraded quality, documented) |

---

## §F.5 Evening ritual (`/close-day`)

### F.5.1 Trigger & preconditions

**Trigger:** Ruslan runs `./jetix close-day` или `/close-day` (end of work block).

**Preconditions:**
- `daily-log/{today}.md` exists (с morning plan).
- `daily-log/drafts/{today}-*.md` may or may not exist.

### F.5.2 Sequence diagram

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant CC as Claude Code
    participant Day as daily-log/YYYY-MM-DD.md
    participant Drafts as daily-log/drafts/
    participant Proj as projects/{p}/log.md
    participant Wiki as wiki/
    participant CRM as crm/
    participant Health as health/log.md
    participant State as shared/state/focus.json
    participant Events as shared/events.jsonl
    participant Git as git

    R->>CC: /close-day
    CC->>Day: Read plan-of-day + что сделано
    CC->>Drafts: Read today's drafts/

    CC-->>R: 4 questions:<br/>1. Что сделал?<br/>2. Insights?<br/>3. Energy 1-5?<br/>4. На завтра?
    R->>CC: answers

    CC->>Day: Fill closing section (accomplishments, insights, energy, tomorrow)
    CC-->>R: "Анализирую drafts. Предлагаю routing:<br/>— 2 insights → wiki<br/>— 1 contact → crm<br/>— 3 tasks → projects/X<br/>— energy 3 → health<br/>— tomorrow focus = X. OK?"
    R->>CC: "OK"

    par Parallel routing
        CC->>Wiki: Ingest insights (new ideas + edges) via /ingest flow
        CC->>CRM: Append contact (interaction entry)
        CC->>Proj: Append [date] entry к projects/{p}/log.md + update next_action
        CC->>Health: Append energy + state
    end

    CC->>State: Update focus.tomorrow, next_action per project
    CC->>Events: Append {"type":"ritual.evening.closed"...}
    alt Notion active (before δ)
        CC->>NotionDaily: mcp__notion-update-page (Daily Log DB)
    end
    CC->>Git: commit "[daily] close YYYY-MM-DD: {focus} — {N} insights, {M} contacts"
    CC->>Git: push
    CC-->>R: "Day closed. Commit {sha}. Tomorrow /plan-day will pull this."
```

### F.5.3 Steps (prose)

1. **Read today's daily-log** + all `daily-log/drafts/{today}-*.md`.
2. **Ask 4 questions** (canonical):
   - Что сделал? (objective facts)
   - Key insights?
   - Energy level 1-5?
   - Tomorrow priorities?
3. **Fill structured sections** of `daily-log/{today}.md`.
4. **Process drafts** — identify artifact candidates:
   - Insights → `wiki/ideas/{slug}.md` drafts (Ruslan approve).
   - Tasks → `tasks/master.md` or `projects/{p}/tasks.md`.
   - Contacts → `crm/{category}.md`.
   - Decisions → `decisions/...`.
   - State (energy, mood) → `health/log.md`.
5. **Distillate** (GitHub-style): each draft with `promoted-to: [paths]`
   frontmatter → writeback flows.
6. **Update `focus.json`** for tomorrow.
7. **Update projects' `next_action`** per project mentioned today.
8. **Notion sync** (while Фаза < δ): `mcp__notion-update-page` Daily Log DB.
9. **Emit event** `ritual.evening.closed`.
10. **Commit + push.**

### F.5.4 Draft promotion invariant

Each draft should ideally have (optimizer §1.7):

```yaml
---
type: daily-draft
created: YYYY-MM-DD
topic: {topic-slug}
status: raw | distilled
promoted-to: []  # filled at close-day
---
```

At close-day, Claude fills `promoted-to: [wiki/ideas/X.md, crm/partners.md, tasks/master.md]`
showing where content went. Enables reverse-query: "which drafts породили most
wiki content?" (productivity metric).

### F.5.5 Failure modes

| Failure | Response |
|---------|----------|
| Ruslan в спешке, отвечает коротко | Claude accepts minimum (energy only) |
| Skipped close-day вчера | Claude offers quick retrospective (5 min) |
| Notion MCP down (before δ) | SAFE-SAVE; note "notion sync pending" во frontmatter; reconcile позже |
| No drafts, empty day | Records "low-activity day" — still commits Daily Log |

---

## §F.6 Weekly natyagivanie (`/cross`)

### F.6.1 Trigger & preconditions

**Trigger:** Ruslan runs `./jetix review week` или `./jetix cross hypotheses projects`.

**Preconditions:**
- 5-7 daily-log files за неделю.
- `projects/` active > 0.
- `hypotheses/active.md` или related entities.

### F.6.2 Sequence diagram

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant CC as Claude Code
    participant DailyLogs as daily-log/YYYY-MM-DD.md × 7
    participant Proj as projects/
    participant Hyp as hypotheses/active.md
    participant Tasks as tasks/master.md
    participant Report as strategy/life/2026-Wnn-weekly.md
    participant CrossRpt as reports/cross-YYYY-MM-DD.md
    participant Edges as wiki/graph/edges.jsonl
    participant Events as shared/events.jsonl
    participant Git as git

    R->>CC: ./jetix review week (или /cross hypotheses projects)
    CC->>DailyLogs: Read 7 logs
    CC->>Proj: Load overview + strategy для всех active
    CC->>Hyp: Load active hypotheses (12 typical)
    CC->>Tasks: Load open tasks

    Note over CC: Analyze:<br/>— weekly patterns (energy, completion)<br/>— cross: hypotheses × projects<br/>— cross: tasks × projects ("кто кому помогает?")<br/>— blocked + stale items

    CC-->>R: [cross-report draft + suggestions]
    R->>CC: "apply hyp-03 to sales, hyp-07 to ai-tools"

    CC->>Proj: Append projects/sales/hypotheses.md (to-test: hyp-03)
    CC->>Proj: Append projects/ai-tools/hypotheses.md (to-test: hyp-07)
    CC->>Tasks: Create tasks "test hyp-03 in sales context"
    CC->>Edges: Append edges {type: "cross_suggested", ...}
    CC->>Report: Write strategy/life/2026-Wnn-weekly.md (report + plan next week)
    CC->>CrossRpt: Write reports/cross-YYYY-MM-DD.md (natyagivanie trace)
    CC->>Events: Append {"type":"cross.suggested"...} × N + {"type":"ritual.weekly.completed"...}
    CC->>Git: commit "[weekly] W{nn}: cross analysis + plan W{nn+1}"
    CC->>Git: push
    CC-->>R: "Weekly done. Commit {sha}."
```

### F.6.3 Natyagivanie (cross) as primitive (invariant I-28 adopted from optimizer §1.2)

`./jetix cross <A> <B>` — generalized skill. Examples:

| Command | Meaning |
|---------|---------|
| `./jetix cross hypotheses projects` | Apply all hypotheses × each project |
| `./jetix cross tasks projects` | "Who helps whom?" cross-pollination |
| `./jetix cross decisions projects` | Are we violating our own decisions? |
| `./jetix cross strategy-A strategy-B` | Apply project A's strategy onto B |

**Gradient boosting effect (optimizer §1.2):** previous `cross_suggested` edges
are input — system doesn't re-discover same cross-links. Each iteration
builds on residuals.

### F.6.4 Weekly report structure

`strategy/life/2026-Wnn-weekly.md` (templated):

```markdown
---
type: weekly-report
week: 2026-Wnn
start: YYYY-MM-DD
end: YYYY-MM-DD
created: YYYY-MM-DD
---

# Week {nn}, 2026

## What happened (evidence)
- {bullet points from daily logs, chronological}

## Key metrics delta (from METRICS.md)
- wiki edges +N | decisions +N | natyagivaniya +N | unclear-backlog N

## Insights
- {from daily-log reflections + close-day insights distilled}

## Projects status
- quick-money: {progress, blockers}
- research: ...

## Natyagivanie results (this week)
- hypotheses × projects → {N cross-suggestions, {K} adopted}

## Honest retro (what didn't work)
- {reflection-agent-style honest critique, optional}

## Plan for next week
- Focus: {one thing}
- Key actions: 1, 2, 3
- Experiments / hypotheses to test: ...
```

### F.6.5 Failure modes

| Failure | Response |
|---------|----------|
| Data gaps (skipped days) | Mark "data incomplete" — don't fabricate |
| Project logs empty (inactive) | Mark paused/not-updated |
| No active hypotheses | Skip hypotheses × projects cross |
| Analysis depth overflow context | Decompose: 1-pass summary + selective deep dives |

---

## §F.7 Error flow — SAFE-SAVE

### F.7.1 Trigger

Any of:
- Unhandled exception.
- External dependency unavailable (API 529, MCP disconnect).
- Agent confused / doesn't know how to proceed.
- Git conflict (unresolvable automatically).
- Context overflow (≥95% fill).
- Uncertainty about destructive op.

### F.7.2 Sequence diagram

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant Agent as any agent
    participant Scratch as agents/{id}/scratchpad.md
    participant Git as git
    participant Mailbox as comms/mailboxes/human.jsonl
    participant Events as shared/events.jsonl

    Note over Agent: Executing some skill / task
    Agent--xAgent: Error / unclear / conflict / overflow

    Agent->>Scratch: Append SAFE-SAVE block<br/>(trigger, state, completed, remaining, proposed)
    Agent->>Git: git add -A
    Agent->>Git: commit "[{id}] SAFE-SAVE: <reason>"

    alt git push succeeds
        Agent->>Git: push origin main
    else push fails (network)
        Agent->>Scratch: Append "push pending"
    else push fails (conflict)
        Agent->>Scratch: Append "git conflict — await Ruslan"
    end

    Agent->>Mailbox: Append escalation message
    Agent->>Events: Append {"type":"safe-save.fired","actor":"{id}",...}

    alt Subagent
        Agent-->>Parent: return {"status":"safe-saved",...}
    else Central
        Agent-->>R: chat output "SAFE-SAVE. Stopped at X. Commit {sha}. Options: a/b/c?"
    end

    Note over Agent: STOP. Do not continue.<br/>Wait for Ruslan.

    R->>Agent: "вариант b" (or resolves git conflict)
    Agent->>Agent: Resume from scratchpad
```

### F.7.3 SAFE-SAVE guarantees (invariants)

- **Never deletes state** — only fixates.
- **Always commits + pushes** (or notes "push pending").
- **Always reports к Ruslan** через mailbox + chat.
- **Always stops** — не "гадает" resolution.

### F.7.4 Recovery protocols

| Trigger | Recovery path |
|---------|---------------|
| API 529 | Retry 3× backoff; then SAFE-SAVE; Ruslan can try later or switch model (`JETIX_LLM=...`) |
| MCP disconnect | Switch to local dumps (`raw/notion-*`); continue |
| Git conflict | Ruslan resolves manually (NEVER force) |
| Context overflow | Decompose via Task tool OR `/compact` OR session restart |
| Agent confused | Ruslan clarifies; agent resumes with guidance |

---

## §F.8 Notion migration (α/β/γ/δ)

### F.8.1 Phase overview

(Full plan: `design/NOTION-MIGRATION-PLAN.md` 525 lines. Here — synthesis.)

```mermaid
gantt
    title Notion decommission (α / β / γ / δ)
    dateFormat YYYY-MM-DD
    section α (Quick extract) ✅ done
    Ideas sweep (260 unique)           :done, alpha1, 2026-04-16, 1d
    Classify + ingest (199 relevant)   :done, alpha2, 2026-04-16, 1d
    11 system pages                    :done, alpha3, 2026-04-16, 1d

    section β (Migration rules) ✅ done
    Rules in HUMAN §4.6                :done, beta1, 2026-04-17, 1d
    Codified in TECH §7+§F.8           :done, beta2, 2026-04-18, 1d

    section γ (Full extract) 🔜
    Full Notion content fetch          :gamma1, 2026-04-25, 7d
    Ingest remaining 400+ pages        :gamma2, after gamma1, 5d
    Projects DB + Journal extract      :gamma3, after gamma1, 3d

    section δ (Decommission) ⏳
    1 week parallel operation          :delta1, 2026-05-18, 7d
    Update CLAUDE.md + remove MCP refs :delta2, after delta1, 2d
    Notion → read-only                 :delta3, after delta2, 1d
```

### F.8.2 Generic migration flow (per batch)

```mermaid
sequenceDiagram
    actor R as Ruslan
    participant CC as Claude Code
    participant SW as sweep-worker × N (parallel)
    participant MCP as Notion MCP
    participant Raw as raw/notion-*
    participant Wiki as wiki/
    participant Report as reports/notion-{phase}-{date}.md
    participant Events as shared/events.jsonl
    participant Git as git

    R->>CC: ./jetix ingest notion-batch γ batch-size=50

    par 5 parallel sweep-workers (Task tool run_in_background)
        CC->>SW: Spawn worker-1 (batch ids 0..49)
        SW->>MCP: mcp__notion-fetch × 50
        MCP-->>SW: page JSON
        SW->>SW: Classify RELEVANT / IRRELEVANT / UNCLEAR
        SW->>Raw: Write raw/notion-ideas/{id}.md (all)
        SW->>Wiki: /ingest RELEVANT → wiki/{ideas|sources|concepts}
        SW-->>CC: batch-1 complete, {X} relevant / {Y} skipped / {Z} unclear
    and
        CC->>SW: Spawn worker-2 (batch ids 50..99)
        Note right of SW: Similar flow
    end

    CC->>Report: Aggregate batch reports
    CC->>Events: Append {"type":"migration.phase.completed","phase":"γ","ref":"..."}
    CC->>Git: commit "[notion-γ] batch ingest {count}: {relevant} relevant, {unclear} pending review"
    CC->>Git: push

    CC-->>R: Report summary + UNCLEAR queue
```

### F.8.3 Phase-specific details

**Phase α (done):** Quick extract.
- Input: 260 idea sweep + 11 system pages.
- Output: 199 RELEVANT в `wiki/ideas/` + `wiki/sources/`; 11 system pages в `raw/notion-pages/` + wiki.
- Commits: `[notion-α]` prefix.

**Phase β (done):** Rules.
- Migration rules codified в HUMAN §4.6, TECH §7 + §F.8.
- No data migration — doc phase.

**Phase γ (upcoming):** Full extract.
- Input: остальные 400+ idea cards + full DB contents (Projects, Journal of Chats, Daily Log legacy).
- Flow: sweep-worker batches of 50, 5 parallel workers.
- Output: `raw/notion-*` complete archive + wiki/ populated.
- Tag: `notion-gamma-complete-YYYY-MM-DD`.

**Phase δ (final):** Decommission.
- Criteria for cutover (ALL must be TRUE):
  1. Every Notion page has соответствие в wiki/projects/archive.
  2. All 4 DBs fully exported.
  3. All attachments downloaded.
  4. `/ask` answers any system question без Notion MCP.
  5. No agent declared with `mcp__notion-*` tool.
  6. No skill calls Notion MCP.
  7. CLAUDE.md updated (remove "Notion = external truth").
  8. 7 days of parallel operation без new data loss detected.
  9. Ruslan explicit "OK".
- Tag: `notion-decommissioned-YYYY-MM-DD`.

### F.8.4 Idempotency

**Invariant:** `/ingest` skips items with hash match to existing `raw/notion-ideas/{id}.md`.
Prevents re-import.

### F.8.5 Failure modes

| Failure | Response |
|---------|----------|
| Notion MCP down mid-batch | SAFE-SAVE batch state (IDs done); Ruslan resumes when MCP back |
| Anthropic rate limit | sweep-worker pauses + backoff; on persistent fail → SAFE-SAVE + Ruslan resumes |
| Notion API change mid-migration | Report: "X/Y complete, stopped at Z"; Ruslan diagnoses MCP; restart from checkpoint |
| Duplicate edge case | Write to `reports/sweep-conflicts-YYYY-MM-DD.md` for manual reconcile |
| Rich content (tables, toggles, formulas) lost in markdown | Preserve raw JSON в `raw/notion-pages-raw/`; selective reformat in γ |

---

## §F.9 State machines — key entities

### F.9.1 Project lifecycle

```mermaid
stateDiagram-v2
    [*] --> Idea : "первая мысль"
    Idea --> Proposed : "concrete A → B formulated"
    Proposed --> Active : "resources allocated, strategy.md approved"
    Active --> Active : "work → tasks → hypotheses → iterations"
    Active --> Paused : "resource reallocation"
    Paused --> Active : "resumed"
    Active --> Closed : "Point Б achieved"
    Paused --> Abandoned : "no longer relevant / kill-criterion triggered"
    Closed --> [*]
    Abandoned --> [*]

    note right of Proposed : "overview.md with\nbudget-hours, budget-weeks,\nkill-criterion"
    note right of Abandoned : "log why, archive in\nprojects/_archive/"
```

### F.9.2 Task lifecycle

```mermaid
stateDiagram-v2
    [*] --> Backlog
    Backlog --> Today : "pulled for today"
    Today --> InProgress : "started"
    InProgress --> Done : "completed"
    InProgress --> Blocked : "blocker found"
    Blocked --> Today : "unblocked"
    Blocked --> Backlog : "punt"
    Done --> [*]
    Backlog --> Archived : "stale > 30 days, /lint flags"
    Archived --> [*]
```

### F.9.3 Hypothesis lifecycle

```mermaid
stateDiagram-v2
    [*] --> Formulated
    Formulated --> Backlog
    Backlog --> Active : "testing started"
    Active --> Validated : "evidence ✓"
    Active --> Rejected : "evidence ✗"
    Active --> Pending : "inconclusive"
    Pending --> Active : "re-test"
    Active --> Stale : ">90 days without progress"
    Stale --> Rejected : "Ruslan reviews, kills"
    Stale --> Active : "revived"
    Validated --> WikiClaim : "promoted to wiki/claims/"
    Validated --> NewProject : "scope large → project"
    Rejected --> [*]
    WikiClaim --> [*]
    NewProject --> [*]
```

### F.9.4 Decision lifecycle

```mermaid
stateDiagram-v2
    [*] --> Draft : "proposal (strategist, plan mode)"
    Draft --> Rejected : "Ruslan rejects → archive"
    Draft --> Recorded : "Ruslan approves → decisions/{slug}.md"
    Recorded --> InForce : "applied"
    Recorded --> Propagated : "/propagate-decision → agents' strategies.md"
    Propagated --> InForce : "agents aware"
    InForce --> Reviewed : "replay-check run (weekly reflection)"
    Reviewed --> InForce : "still valid"
    Reviewed --> Superseded : "new decision replaces (old keeps history)"
    InForce --> Archived : "no longer relevant"
    Superseded --> [*]
    Archived --> [*]
    Rejected --> [*]

    note right of Recorded : "NEVER deleted.\nOnly appended events:\nreviewed / superseded / archived"
```

### F.9.5 Idea lifecycle

```mermaid
stateDiagram-v2
    [*] --> Captured : "raw mental / voice / notion"
    Captured --> InIdeasPool : "systemic → ideas-pool/inbox.md"
    Captured --> InProject : "linked to specific project"
    InIdeasPool --> Ingested : "/ingest → wiki/ideas/"
    InProject --> Ingested
    Ingested --> Hypothesis : "matured → testable → hypotheses/"
    Ingested --> Project : "big enough → projects/"
    Ingested --> Claim : "evidence emerges → wiki/claims/"
    Ingested --> Archived : "no action > 180 days → stale"
    Hypothesis --> [*]
    Project --> [*]
    Claim --> [*]
    Archived --> [*]
```

### F.9.6 Edge temporal lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created : "{valid_from: YYYY-MM-DD, confidence: C}"
    Created --> Valid : "while valid_until = null"
    Valid --> Expired : "valid_until = YYYY-MM-DD set (when fact updates)"
    Expired --> Historical : "remains в edges.jsonl as history"
    Historical --> [*]

    note right of Valid : "confidence может эволюционировать\nчерез /consolidate updates"
    note right of Expired : "old edge keeps showing\nin time-travel queries"
```

---

## §F.10 Cross-cutting flow invariants

All flows share:

### F.10.1 Provenance enforcement
Every wiki page resulting from ingest carries `sources:` frontmatter
(invariant I-07). Без provenance — `/lint` fails.

### F.10.2 Idempotency
All ingest operations dedup by slug/hash. Prevents accidental re-processing.

### F.10.3 Append-only logs
Each flow appends к:
- `wiki/log.md` (wiki events).
- `shared/events.jsonl` (unified canonical stream).
- Specialized: `decisions/*-log.md`, `projects/{x}/log.md`, mailboxes.

### F.10.4 SAFE-SAVE on failure
Any error → §F.7 pattern. Invariant I-14 non-negotiable.

### F.10.5 Git discipline
Every completed sub-step — commit. Every flow end — push. Invariant I-21.

### F.10.6 Human gate for L3 (strategy + decisions)
No flow автоматически writes к `strategy/`, `decisions/`, `projects/{x}/strategy.md`
without explicit Ruslan approval (invariant I-11).

### F.10.7 Voice pipeline: hard human gate
`~/review-latest.md` — mandatory stop (§F.2). `distribute.py.bak` — disabled
intentionally.

### F.10.8 Writeback compounding
After `/ask` — optional writeback to `comparisons/` + `questions/` + edges
(§F.4). Next `/ask` benefits from prior context. This is the compounding
engine.

### F.10.9 Event emission discipline
Every skill invocation emits to `shared/events.jsonl`. Enables time-travel
queries (`git checkout` + replay), analytics, `./jetix metrics`.

### F.10.10 Semi-manual mode
All flows triggered by Ruslan's explicit command. No cron, no event-driven,
no autonomy budget. Invariant I-19.

---

## §F.11 Flow summary map

```mermaid
flowchart LR
    Ruslan["👤 Ruslan"]

    subgraph Flows["Daily + weekly flows"]
        F1["F1 /plan-day"]
        F2["F2 voice → wiki"]
        F3["F3 /ingest"]
        F4["F4 /ask"]
        F5["F5 /close-day"]
        F6["F6 /cross (weekly)"]
    end

    subgraph Background["Maintenance"]
        Lint["/lint"]
        Consolidate["/consolidate"]
        BuildGraph["/build-graph"]
        Metrics["/metrics"]
    end

    subgraph Errors["Error"]
        F7["F7 SAFE-SAVE"]
    end

    subgraph Migration["One-off"]
        F8["F8 Notion α/β/γ/δ"]
    end

    Ruslan --> F1
    Ruslan --> F2
    Ruslan --> F3
    Ruslan --> F4
    Ruslan --> F5
    Ruslan --> F6
    Ruslan --> Lint
    Ruslan --> Consolidate
    Ruslan --> BuildGraph
    Ruslan --> Metrics
    Ruslan --> F8

    F1 -.->|"on error"| F7
    F2 -.-> F7
    F3 -.-> F7
    F4 -.-> F7
    F5 -.-> F7
    F6 -.-> F7
    F8 -.-> F7

    F3 -->|"feeds"| Lint
    F6 -->|"uses"| BuildGraph
    F4 -->|"uses"| BuildGraph
    F1 -->|"reads"| F5
    F5 -->|"sets up"| F1
    F6 -->|"informs"| F1
```

---

## §F.12 Closing observation

Все flows соблюдают shared pattern:

```
1. git pull (ensure fresh state)
2. Read current state (configs, state files, relevant data)
3. Plan / decompose the operation
4. Execute (with SAFE-SAVE on any error)
5. Emit event to shared/events.jsonl + domain-specific log
6. Commit (with convention message)
7. Push origin main
8. Report to Ruslan (or parent agent)
```

This is **the canonical execution pattern** of Jetix OS. Every new skill /
ritual added **must** follow it. Consistency = debuggability = Q1 Transparency.

---

*End of DATA-FLOWS.md v1-beta. ~900 lines, 8 canonical flows + 6 state machines
+ cross-cutting invariants. Synthesized from both engineer reviews
(Engineer A arc42 Runtime view + Engineer B mermaid-first sequence diagrams).
Writeback / HippoRAG / questions reverse index — optimizer leverage embedded.
Living document — extend when new flows / state machines stabilize.*
