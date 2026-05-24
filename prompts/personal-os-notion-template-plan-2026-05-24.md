---
title: Personal OS Notion Template Design Plan — universal fork-friendly lighter Foundation + voice-first + Claude Code integration
date: 2026-05-24
type: autonomous-execution-prompt
phase_count: 9
ack_source: Ruslan voice 24.05 evening «сейчас делаем шаблон в Notion / на фундаменте 11 pillars / lighter version / fork-friendly под любую нишу / Claude Code подключать / voice fill / tracking что хочу узнать / шаблон анализа недели + месяца / красота невообразимо круто / прям плотнейший / на базе нашей философии»
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2-F3
G: personal-os-notion-template-plan
R: refuted_if_R1_strategic_prose_authored_OR_LOCK_modified_OR_jargon_heavy_OR_lt_6_mermaid_OR_auto_create_notion_OR_fork_friendly_missing_OR_filesystem_source_of_truth_violated
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame + IP-1 STRICT + EP-5 + AP-6 + append-only
estimated_runtime: 4-6h autonomous (design synthesis + per-DB schema + mermaid + plain prose)
estimated_cost: <€3
language: russian primary + plain conversational
priority: ⭐⭐⭐ Personal OS template = daily-use cornerstone + fork-friendly distribute
parent_substrate:
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
  - swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md
  - swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md
  - swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
  - swarm/wiki/foundations/part-6b-human-gate/architecture.md
  - swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md
  - swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md
  - swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md
  - swarm/wiki/foundations/principles/architecture.md
  - swarm/wiki/concepts/notion-mvp-bypass-pattern.md (O-158)
  - swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md
  - crm/README.md + crm/PLAN.md
  - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/
  - decisions/strategic/PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md
  - decisions/strategic/POINT-A-CURRENT-STATE-2026-05-23.md (Phase 5 Notion inventory)
  - decisions/strategic/CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md (plain-language style + 7 принципов)
  - decisions/strategic/EXECUTION-PLAN-FIXATION-2026-05-24.md (5 templates trigger order)
  - decisions/strategic/RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24.md (O-176..O-185)
  - CLAUDE.md Key Notion IDs (existing pages inventory)
  - 4 LOCKED canonical (Method V2 / Strategic Plan / Economic V10 / AI Market PLAN)
  - PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md (style anchor)
ram_constraint: low-medium (design synthesis + schema spec)
mode: DESIGN-PLAN SYNTHESIS (Notion template design plan; NO Notion API calls; NO auto-create pages)
explanation_file: _EXPLAIN-personal-os-notion-template-plan-2026-05-24.md
---

# 🗂️ Personal OS Notion Template — Design Plan

> **Trigger:** Ruslan voice 24.05 evening — «сейчас делаем шаблон в Notion / на фундаменте 11 pillars / lighter version / fork-friendly / Claude Code подключать / voice fill / tracking что хочу узнать / шаблон анализа недели + месяца / на базе нашей философии».
>
> **Mode:** **DESIGN-PLAN SYNTHESIS** — спроектировать universal Personal OS Notion template который:
> - Облегчённая версия Foundation 11 pillars для повседневной personal usage
> - Fork-friendly — любой человек duplicate'нул + кастомизировал под свою нишу за 30-60 min
> - Voice-first — Wispr Flow / voice → CC → distributed entries automatically
> - Claude Code integration — CC reads / suggests / processes Notion content
> - Reviews built-in (week / month / quarter / annual / project / hypothesis)
> - Plain-language, без jargon, conversational
>
> **Стиль:** `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` + `CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md` (plain Russian conversational).

---

## §0 Pre-flight

1. **Memory read mandatory:**
   - `feedback_constitutional.md` — R1 surface only
   - `feedback_no_unsolicited_alternatives.md` — facts, не recommendations
   - `feedback_max_density_max_tokens.md` — apply (major strategic deliverable)
   - `feedback_research_pool_pattern.md` — surface candidates, не auto-launch
   - `feedback_prompt_explanation_required.md` — explanation file done (`_EXPLAIN-personal-os-notion-template-plan-2026-05-24.md`)
   - `feedback_fpf_lens_first.md` — FPF lens scope в Phase 0 обязательно
2. **Substrate read FULL** (см. frontmatter parent_substrate — это ~25 файлов)
3. **Existing Notion inventory check:** POINT-A Phase 5 + CLAUDE.md Key Notion IDs (Command Center / Daily Log DB / Projects DB / Journal of Chats / Банк идей / ICP / Research Hub / Life OS)
4. **Style anchors:**
   - `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md`
   - `CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md`
5. **Plain language constraint MANDATORY:**
   - НЕТ constitutional jargon (R12 / IP-1 / EP-5 / FPF / etc.) без translation на human
   - НЕТ academic vocabulary без объяснения
   - ДА — conversational Russian, прямо

---

## §0.1 ⚠️ §17.0 CRITICAL IMPORTANCE MANDATE (per memory feedback_max_density_max_tokens)

Universal Personal OS Notion template = **daily-use cornerstone** + **fork distribution artefact** (любой партнёр / cohort member receives как template). Качество определяет:
- Ежедневную productivity Ruslan'a
- First impression любого fork'нувшего человека
- Whether Jetix philosophy «работает» на personal level (proof point)

Поэтому:

1. **ROY swarm на 500%** — brigadier orchestrates:
   - engineering-expert (DB schema + system architecture + frontmatter mirror discipline)
   - systems-expert (cybernetic feedback loops в reviews + daily-weekly-monthly cadence)
   - mgmt-expert (workflow + cadence + attention budget design)
   - methodology-engineer (Foundation 11 pillars → Notion translation + method composition)
   - influence-ethics-expert cross-consult (R12 fork-and-leave embedded в Layer 1 design)
   - + recruitment-dynamics-expert cross-consult Phase 7 (niche overlay examples)
2. **Use MAX tokens × 3** — depth > brevity для substantive sections (Phase 1 / 2 / 3 / 7 — main payload)
3. **Per-database schema MUST be concrete** — properties (type + default + required) / views (filter + sort + group) / relations (target DB + cardinality)
4. **Niche overlay examples — minimum 3, optimum 5** — engineer / researcher / entrepreneur / educator / humanitarian; per example: full Layer 2 specification (projects taxonomy / CRM roles / hypotheses themes / cadence adjustments)
5. **Voice intake matrix MUST be exhaustive** — каждый возможный voice content type → routing decision (≥7 content types × ≥8 destinations)
6. **Analysis templates MUST be ready-to-use** — full questions list / pre-filled structure / output expected
7. **Плотность everywhere** — каждый section substantive (not bullets-only); каждая mermaid dense ≥10 nodes; каждый template — minimum 8-12 questions / properties
8. **Не stopover at minimum** — produce best work possible
9. **Если можно add 1 more niche / property / template question → add**

**Reverse caveat:** balance density с **plain prose mandate** — это conversational human-language design doc, не academic specification. Density через **concrete specs + named examples**, не через jargon.

---

## §1 9 Phases

| # | Phase | Output |
|---|---|---|
| **0** | Pre-flight + FPF lens scope + substrate + existing Notion inventory | `reports/personal-os-notion-template-plan-2026-05-24/phase-0-substrate.md` |
| **1** | ⭐⭐⭐ **Foundation 11 pillars → Notion lighter mapping** | `01-foundation-lighter-mapping.md` (~500 lines) — see §2 |
| **2** | ⭐⭐⭐ **Top-level structure** (10-12 databases + Command Center) | `02-top-level-structure.md` (~400 lines) — see §3 |
| **3** | ⭐⭐⭐ **Per-database schema** (properties + views + relations) | `03-per-database-schema.md` (~800 lines) — see §4 |
| **4** | ⭐⭐ **Voice intake routing** (Wispr → CC → distribution matrix) | `04-voice-intake-routing.md` (~400 lines) — see §5 |
| **5** | ⭐⭐ **Analysis templates** (week / month / quarter / annual / project / hypothesis / call) | `05-analysis-templates.md` (~600 lines) — see §6 |
| **6** | ⭐⭐ **Claude Code ↔ Notion integration** (sync patterns + suggestion flow) | `06-claude-code-integration.md` (~400 lines) — see §7 |
| **7** | ⭐⭐⭐ **Fork-friendly architecture** (Layer 1 universal + Layer 2 niche + fork instructions + 3-5 examples) | `07-fork-friendly-architecture.md` (~700 lines) — see §8 |
| **8** | ⭐⭐ **6-7 mermaid + Main consolidated + Roadmap + Summary + push** | `08-mermaid-schemes.md` + `diagrams/_INDEX.md` + `decisions/strategic/PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md` (~10-15K plain prose) + `00-SUMMARY-FOR-RUSLAN.md` (≤500w) — see §9 |

---

## §2 Phase 1 — Foundation 11 pillars → Notion lighter mapping ⭐⭐⭐

**Source:** 11 Foundation Parts architecture.md + Pillar C principles + O-158 Notion-MVP-bypass + POINT-A Phase 5 existing Notion.

**Per-Part mapping (mandatory all 11):**

For each Part 1-11 + Pillar C — produce 1 table row:

| Part | What it does (Foundation) | Notion lighter equivalent | What survives | What dropped/simplified | Why |
|---|---|---|---|---|---|

### §2.A Sample mappings (full table в output):

- **Part 1 State Persistence** → Файловая система + Notion как mirror. Frontmatter mandatory.
- **Part 2 Signal Ingestion** → Voice intake (Wispr) + email forwarding + DRAFT queue.
- **Part 3 KB & Methodology** → Knowledge DBs (concepts / sources / claims / hypotheses).
- **Part 4 Role Taxonomy** → Personal-OS = user-driven (no agents); roles dropped for personal use; surfaces back if multi-agent setup (advanced fork).
- **Part 5 Compound Learning** → Reviews DBs (week / month / quarter / annual).
- **Part 6a/6b Provenance + Gate** → Daily review + decision queue + frontmatter R6 cite.
- **Part 7 Project Lifecycle** → Projects DB с 4 types (consulting / research / product / bets) + Stage Gates lighter.
- **Part 8 Health Monitoring** → Life Pulse DB (energy / health / relationships / finance pulse).
- **Part 9 Owner Interaction Scaffold** → Command Center hub page (single entry point).
- **Part 10 External Touchpoints** → CRM (people + orgs).
- **Part 11 Strategic Direction** → Strategic DB (POINT A / POINT B / annual plan / quarter / decision queue).
- **Pillar C Tier 2 (12 rules)** → Notion guardrails layer (frontmatter constraint check / DRAFT-only / no API key exposure / etc.).

### §2.B For each — explicit philosophy translation

«Что survives» = что переживает упрощение и остаётся даже в lightest Notion версии (e.g., frontmatter mandatory / append-only logs / DRAFT-only voice).

«Что dropped» = что для personal use не нужно (e.g., 17 ROY agents → user-driven; AWAITING-APPROVAL packets → simple decision queue).

«Что simplified» = что adapt'ируется (e.g., Stage Gates 4 SG-levels → simplified 3-level checkpoints for personal projects).

---

## §3 Phase 2 — Top-level structure (10-12 databases + Command Center) ⭐⭐⭐

**Source:** POINT-A Phase 5 + KM MVP design + CRM + Wiki v2 + Plan-Mode Plan C.

### §3.A 10-12 databases list (R1 surface — pool, Ruslan picks final list)

Кандидаты (full design — choose-later by Ruslan):

1. **Daily Log** — entries DB, append-only, voice-fed primary
2. **Projects** — 4 types (consulting / research / product / bets) + Stage Gates lighter (3-level)
3. **Tasks** — actionable items linked к Projects
4. **Knowledge — Concepts** — wiki-style concept entries (Karpathy LLM Wiki analog)
5. **Knowledge — Sources** — books / articles / videos / podcasts ingested
6. **Knowledge — Claims** — verified statements with R6 provenance
7. **Knowledge — Hypotheses** — «что хочу узнать» tracking with acceptance predicate
8. **Ideas Bank** — Tier A/B/C surface entries before promotion
9. **CRM People** — contacts (per CRM 24 roles structure)
10. **CRM Orgs** — organizations (per CRM)
11. **Reviews** — week / month / quarter / annual entries (unified DB с type property)
12. **Strategic** — POINT A / POINT B / annual plan / quarter plan / decision queue
13. **Life Pulse** — energy / health / relationships / finance entries (daily/weekly check-ins)
14. **Reference** — templates / scripts / configs / personal canon

### §3.B Consolidation options (Ruslan picks)

- **Option Lite (8 DBs):** Daily Log / Projects+Tasks consolidated / Knowledge consolidated (concepts+sources+claims) / Hypotheses / CRM (people+orgs unified) / Reviews / Strategic / Life Pulse
- **Option Standard (10-12 DBs):** as above split
- **Option Full (14 DBs):** maximum separation

Pool с trade-offs. NO recommendation. Ruslan picks.

### §3.C Command Center hub page (single dashboard)

- **Top section:** Today's focus (Daily Log latest + active projects)
- **Quick capture:** Voice-intake widget / inbox
- **Active state:** Top 3 projects + top 3 hypotheses + top 5 contacts (warm)
- **Reviews due:** Week / month / quarter / annual reminder
- **Strategic anchor:** POINT B + next quarter plan refs
- **Life pulse:** Last energy / health / relationships scores

### §3.D Page hierarchy

```
Personal OS Workspace (root)
├── 🎯 Command Center (hub)
├── 📅 Daily Log
├── 🚀 Projects
├── 📚 Knowledge
│   ├── Concepts
│   ├── Sources
│   ├── Claims
│   └── Hypotheses
├── 💡 Ideas Bank
├── 🤝 CRM
│   ├── People
│   └── Orgs
├── 🔄 Reviews
├── 🧭 Strategic
├── ❤️ Life Pulse
└── 📂 Reference
```

### §3.E Relations graph

(Phase 8 mermaid NT-2 will visualize)

- Project ↔ Tasks (1:N)
- Project ↔ Daily Log entries (N:N — entries reference active projects)
- Hypothesis ↔ Projects (N:N — hypotheses test in project context)
- Hypothesis ↔ Sources / Claims (N:N — evidence accumulation)
- CRM Person ↔ Projects (N:N — collaborators)
- CRM Person ↔ Orgs (N:N — affiliation)
- Reviews ↔ Projects + Hypotheses + Life Pulse (1:N — period rollup)
- Daily Log ↔ Life Pulse (1:1 daily — pulse score)

---

## §4 Phase 3 — Per-database schema (full spec) ⭐⭐⭐

**Source:** POINT-A Phase 5 + CRM schema + Wiki v2 frontmatter + KM MVP designs.

**Per DB — FULL specification:**

### §4.A Daily Log DB

**Properties:**
| Property | Type | Default | Required | Notes |
|---|---|---|---|---|
| Title | Text | — | Y | YYYY-MM-DD format |
| Date | Date | today | Y | sortable |
| Energy | Select (1-10) | 5 | N | morning self-check |
| Focus area | Multi-select [active projects] | active | N | linked relations |
| Voice draft? | Checkbox | N | N | DRAFT marker |
| Entries | Rich text | — | N | append-only daily entries |
| Reflections | Rich text | — | N | end-of-day |
| Tomorrow trigger | Rich text | — | N | next-day plan seed |
| Linked Projects | Relation Projects DB | — | N | mentioned today |
| Linked Hypotheses | Relation Hypotheses DB | — | N | tested today |
| Pulse score | Number 1-10 | — | N | overall day |

**Views:**
- Today (filter: date=today)
- This week (rolling 7 days)
- Voice drafts review (filter: voice draft=Y)
- Weekly digest (grouped by week)

### §4.B Projects DB

**Properties:**
| Property | Type | Default | Required | Notes |
|---|---|---|---|---|
| Title | Text | — | Y | kebab-slug |
| Type | Select (consulting/research/product/bets) | — | Y | KM MVP taxonomy |
| Priority | Select (P1-P4) | P3 | Y | |
| Status | Select (active/planned/paused/archived) | planned | Y | |
| Stage | Select (SG-1/SG-2/SG-3/SG-4) | SG-1 | N | lighter Stage Gates |
| Owner | Person | self | Y | |
| Collaborators | Relation CRM People | — | N | |
| Start date | Date | — | N | |
| Target date | Date | — | N | |
| Last touched | Date (auto) | — | — | system-maintained |
| Linked hypotheses | Relation Hypotheses | — | N | |
| Linked sources | Relation Sources | — | N | |
| Active flag | Formula (status=active AND last_touched within 14d) | — | — | for stuck detection |
| Description | Rich text | — | N | one-paragraph |
| Stage Gate notes | Rich text | — | N | per-SG predicates |

**Views:**
- Active P1-P2 (priority kanban)
- By type (4 columns)
- Stuck (active + last_touched > 14d)
- Archived (separate view)

### §4.C ... (continue all DBs in output Phase 3)

Each DB MUST have:
- Full property list (≥10 properties)
- Default values + required flags
- ≥3 views (use cases)
- Relations to other DBs
- Filesystem mirror discipline (.md frontmatter equivalent)

### §4.D Frontmatter mirror discipline

**Mandate (Global Rule 4 — Filesystem = source of truth):**
- Each Notion DB row ↔ filesystem .md file (in `personal-os/<db>/<slug>.md`)
- Frontmatter YAML matches Notion properties (auto-sync script Phase 6)
- Notion edits → script → filesystem update
- Filesystem edits → script → Notion update
- **Conflict resolution: filesystem wins** (Global Rule 4)

### §4.E Naming conventions

- DB names: PascalCase or Kebab-Case (consistent)
- Property names: snake_case Russian/English mix ok
- Slugs: kebab-case (`my-cool-project`)
- Dates: YYYY-MM-DD ISO format

---

## §5 Phase 4 — Voice intake → distribution routing ⭐⭐

**Source:** Voice pipeline canonical + CRM voice integration + O-158 Notion-MVP-bypass.

### §5.A Voice content type → destination matrix

(Comprehensive routing — Phase 4 main payload)

| Voice content type | Destination DB | Property fill | Required review? | Trigger |
|---|---|---|---|---|
| Mentions person (new or existing) | CRM People | Name + draft note + last touch | Y (DRAFT-only) | name detected |
| Mentions org | CRM Orgs | Name + draft note | Y (DRAFT-only) | org keyword |
| Idea / hypothesis germ | Ideas Bank (Tier C default) | Title + body + voice ref | Y (Tier promotion) | «идея / а что если / гипотеза» triggers |
| Hypothesis explicit | Hypotheses DB | Statement + how-to-test draft | Y | «гипотеза + test» pattern |
| Project status update | Projects (last_touched + body append) | Last touched timestamp + entry | N (auto append) | active project name mentioned |
| Decision moment | Strategic (decision queue) | Title + rationale + date | Y | «решил / выбираю / акаю» |
| Reflection / journal | Daily Log (today entry append) | Reflections rich-text append | N (auto) | reflection patterns |
| Energy / health check | Life Pulse (today entry) | Pulse score + note | N (auto) | «энергия / здоровье / отношения» |
| Source mention (book / article / video) | Sources DB | Title + status=mentioned + draft notes | Y | «читаю / смотрел / послушал X» |
| Claim verified | Claims DB | Statement + source ref + F-G-R draft | Y | explicit «факт что X per Y» |
| Task / action item | Tasks DB | Title + project link + priority draft | Y (DRAFT) | «нужно / сделать / напомни» |
| Reference material | Reference | Title + content | N | explicit save command |
| Strategic anchor change | Strategic DB | New POINT B revision draft | Y (high gate) | «vision changed / новый POINT B» |

### §5.B DRAFT-only discipline (R12 + Voice canon)

- **NEVER** auto-overwrite prod records
- Voice → DRAFT entry с marker (e.g., `_voice_draft: true` property)
- Ruslan reviews DRAFT → promotes manually → DRAFT marker cleared
- Voice → existing record: append-only (no field replacement без manual review)

### §5.C Wispr Flow → CC pipeline

1. Wispr Flow voice → text (local)
2. Text → `tools/voice_intake.py` (CC helper)
3. CC parses content → classifies → routes to appropriate DB(s)
4. CC creates DRAFT entries (Notion API)
5. CC writes summary log to `daily-logs/voice-intake-YYYY-MM-DD.md`
6. Ruslan reviews next morning / end-of-day → promotes

### §5.D Fallback handling

- Content doesn't fit any pattern → Ideas Bank as Tier C default + manual classification
- Ambiguous content → DRAFT in suggested DB + flag for Ruslan choice
- Sensitive content (financial / health detail) → encryption marker + restricted property

---

## §6 Phase 5 — Analysis templates ⭐⭐

**Source:** POINT-B-FOCUSED-WEEK-1 + Method V2 §H meta-control + Foundation Part 5 compound learning.

**Per template — full structure (≥8 questions / pre-filled).**

### §6.A Weekly review template

**Questions (every Sunday evening):**
1. Что сделано на этой неделе? (top 5 wins)
2. Какие hypotheses протестированы? (closed / still open / pivoted)
3. Где friction / blockers? (top 3)
4. Energy / health / relationships pulse — динамика недели?
5. Project velocity per active P1-P2 — на трэке?
6. Что carried на следующую неделю?
7. Что выбросить / archived?
8. Top 3 для next week (Шаги priority)
9. Strategic alignment check — на POINT B trajectory?

**Auto-fill:** Daily Log entries last 7 days / active hypotheses tested / project last_touched data / life pulse rolling.

**Output:** Reviews DB row type=week + linked entries.

### §6.B Monthly review template

**Questions (last day of month):**
1. Project velocity по 4 типа — где velocity high / low?
2. Hypothesis closure rate — closed vs surfaced ratio?
3. Strategic anchor alignment — POINT B на горизонте?
4. Financial pulse — burn rate / income trajectory?
5. Community / partnership progress — Wave N status?
6. Health / energy trends — sustainable cadence?
7. Books / sources ingested — depth vs breadth balance?
8. Compound learning — какие patterns emerged?
9. Anti-patterns / friction — что нужно eliminate?
10. POINT B revision needed?

**Auto-fill:** Reviews week × 4 / Project status changes / Hypothesis closure / Life Pulse aggregate / Financial DB.

### §6.C Quarterly review template

(Deeper strategic — POINT B revision considered / relationships review / vision check / decision queue audit.)

### §6.D Annual review template

(Vision revision / values reflection / life-direction / next year POINT B authoring.)

### §6.E Project review template

**Per active project — quarterly:**
1. Stage Gate predicate status?
2. Velocity / blockers?
3. Last 3 commits / updates significance?
4. Linked hypotheses — testing or stalled?
5. Collaborator status / friction?
6. Archive criteria check (kill / pivot / continue)?
7. Next 3 actions?

### §6.F Hypothesis test design template

(Per hypothesis when created):
1. Statement (one sentence falsifiable)
2. Acceptance predicate (how do we know it's confirmed)
3. Falsification design (what proves it wrong)
4. Test method (what experiment / observation)
5. Time budget
6. Linked sources / supporting evidence
7. F-G-R draft (Formality / Group-scope / Reliability)
8. Linked projects (which projects this affects)

### §6.G Discovery call template

(Per scheduled call с partner / client):
1. R12 paired-frame 8-item pre-check
2. Their pain / goal / context (from prior research)
3. Top 5 questions to ask (Bloom-progression)
4. What we offer (3 options)
5. What we ask (proportional to relationship depth)
6. Anti-CTAs to avoid (manipulation / MLM / lock-in / Bloom violation)
7. Post-call action items expected

### §6.H Voice → daily entries template

(Auto-populated daily; manually edited end-of-day):
- Morning intent
- Mid-day pulse
- Evening reflection
- Tomorrow trigger
- Gratitude / friction notes

---

## §7 Phase 6 — Claude Code ↔ Notion integration ⭐⭐

**Source:** Notion API patterns + O-158 Notion-MVP-bypass + voice pipeline + CRM voice integration + Global Rule 4.

### §7.A Sync patterns

**Filesystem = source of truth (Global Rule 4 STRICT)**

- Notion = view layer (collaborative + UI + voice intake destination)
- Filesystem = canonical (.md per DB row + frontmatter mirror)
- Conflict resolution: filesystem wins; Notion gets corrected on sync

**Sync directions:**

1. **CC → Notion (push):**
   - Daily: filesystem changes (commits) → Notion mirror update
   - Periodic: project status / hypothesis updates / new entries
   - On-demand: bulk import / new DB creation
2. **Notion → CC (pull):**
   - Voice intake: Notion DRAFTs → CC processes → filesystem .md
   - Manual edits: user edits Notion → daily pull → filesystem update
   - Comments / collaborator additions
3. **Bidirectional resolution:**
   - Filesystem timestamp > Notion → filesystem wins, push update
   - Notion timestamp > Filesystem → notify user, ask resolution
   - Conflict → DRAFT both versions, manual resolve

### §7.B What CC suggests vs what user picks

**CC ALLOWED:**
- Suggest entries based on voice
- Surface candidates for promotion (Tier C → Tier B → Tier A)
- Suggest hypothesis links based on content
- Suggest project assignments based on context
- Pre-fill review templates with relevant data

**CC NEVER:**
- Auto-overwrite prod records (DRAFT-only mandate)
- Authoring strategic prose (R1 — user only)
- Force property changes без user ack
- Auto-decide Tier promotions
- Auto-archive projects

### §7.C Required tools (Phase 6 output specifies)

- `tools/notion_export.py` — Filesystem → Notion sync
- `tools/notion_import.py` — Notion → Filesystem sync
- `tools/voice_intake_router.py` — Voice → DB classification + DRAFT creation
- `tools/notion_audit.py` — Conflict detection + drift report
- `tools/template_instantiate.py` — Create new DB rows from templates

### §7.D Skills (CC commands user can invoke)

(Notion-specific — addition to existing /crm-* / /ingest / etc.):
- `/notion-sync` — bidirectional sync trigger
- `/notion-audit` — drift / conflict detection
- `/notion-template <type>` — instantiate template (week-review / month-review / discovery-call / etc.)
- `/notion-voice-process` — process voice intake batch
- `/notion-promote <draft-id>` — promote DRAFT to prod record

### §7.E Anti-patterns

- ❌ NO direct API key in Notion property
- ❌ NO Notion-only persistence (always filesystem mirror)
- ❌ NO auto-execution actions (no «CC fills out / submits / decides»)
- ❌ NO third-party integrations без user explicit setup

---

## §8 Phase 7 — Fork-friendly architecture ⭐⭐⭐

**Source:** Foundation 11 pillars + Pillar C tier 2 + ruslan_layer_overrides analog + IP-1 STRICT.

### §8.A 2-layer architecture

**Layer 1 — Universal Foundation (generic, fork'нется любому):**
- 10-12 databases topology
- Property types + naming conventions (generic — no «Ruslan's» in DB names)
- Voice intake routing matrix (universal classifications)
- Review templates structure (generic questions — adaptable)
- Claude Code integration patterns
- Filesystem mirror discipline
- DRAFT-only voice discipline
- R12 fork-and-leave compliance built-in

**Layer 2 — Niche overlay (instance-specific, customized per fork):**
- Projects taxonomy (4 types fixed Layer 1 + niche-specific subtypes Layer 2)
- CRM roles (24 generic Layer 1 + niche-specific Layer 2 overlay)
- Hypotheses themes (universe-specific to the forking user)
- Active project list (instance)
- Active contacts list (instance)
- Personal review questions adjustments
- Specific Notion page IDs (instance)

### §8.B Fork instructions (step-by-step)

**Setup time: 30-60 min for someone competent.**

1. **Duplicate workspace:** Notion duplicate Universal Personal OS template (1-click)
2. **Rename root:** «<Your Name> Personal OS» or workspace-appropriate
3. **Layer 1 untouched:** keep all DB structures / property types / views as-is
4. **Layer 2 customize:**
   - Adjust projects taxonomy (add subtypes specific to your domain)
   - Adjust CRM roles (add niche-specific роли — e.g., «co-founders», «advisors», «students»)
   - Adjust hypotheses themes (your research questions universe)
   - Seed Strategic DB с your POINT A / POINT B / annual plan
5. **Claude Code setup:**
   - Install CC (per Anthropic docs)
   - Clone scaffolding repo (`git clone jetix-os-personal-os-scaffold`)
   - Configure Notion API token in `.env`
   - Run `/notion-sync --bootstrap` to initialize
6. **First entries:**
   - Daily Log: today first entry
   - Strategic: POINT A current state (1 paragraph)
   - CRM: 5-10 top relationships imported
   - Hypotheses: 3-5 active «что хочу узнать»
7. **Voice setup:**
   - Install Wispr Flow / similar
   - Configure voice intake script
   - Test with 1 voice memo

### §8.C 3-5 niche overlay examples

**Per niche — full Layer 2 spec:**

#### Niche 1 — Engineer / IC contributor (Karpathy-tier)

- **Projects taxonomy Layer 2:** code-projects / research-papers / open-source / production-systems / experiments
- **CRM roles Layer 2:** co-contributors / peer-reviewers / managers / domain-experts
- **Hypotheses themes:** technical-architecture / performance / scalability / new-paradigms
- **Cadence:** weekly tech digest review / monthly project velocity check
- **Voice patterns:** «commit / pr / bug / refactor» auto-routes to Tasks

#### Niche 2 — Researcher / PhD-track

- **Projects taxonomy Layer 2:** papers-in-progress / experiments / literature-reviews / collaborations / conferences
- **CRM roles Layer 2:** advisors / committee / collaborators / reviewers / lab-mates
- **Hypotheses themes:** research-questions / methodology / replication / theoretical-frameworks
- **Cadence:** weekly literature digest / monthly experiment review
- **Voice patterns:** «paper / experiment / hypothesis / data» routing

#### Niche 3 — Entrepreneur / solo-founder

- **Projects taxonomy Layer 2:** clients / products / marketing / operations / fundraising
- **CRM roles Layer 2:** customers / investors / advisors / partners / hires
- **Hypotheses themes:** market-validation / pricing / channels / unit-econ
- **Cadence:** weekly sales review / monthly cohort retention
- **Voice patterns:** «call / lead / deal / metric» routing

#### Niche 4 — Educator / methodologist (Левенчук-tier)

- **Projects taxonomy Layer 2:** courses / cohorts / methodology-development / writing / consulting
- **CRM roles Layer 2:** students / co-teachers / methodologists-peers / clients
- **Hypotheses themes:** pedagogy / curriculum-design / outcome-measurement
- **Cadence:** per-cohort retention check / per-course outcome review
- **Voice patterns:** «cohort / session / outcome / feedback» routing

#### Niche 5 — Humanitarian / life-management (Дмитрий-style)

- **Projects taxonomy Layer 2:** relationships / health / personal-finance / hobbies / family
- **CRM roles Layer 2:** family / close-friends / professionals (doctors / accountants / advisors)
- **Hypotheses themes:** lifestyle-design / health-protocols / relationship-quality
- **Cadence:** weekly life pulse / monthly relationship audit
- **Voice patterns:** «health / relationship / pulse / decision» routing

### §8.D Anti-patterns при fork

- ❌ Over-customize Layer 1 (breaks fork-friendly + future updates)
- ❌ Strip provenance fields (breaks Foundation discipline)
- ❌ Break frontmatter mirror (breaks CC sync)
- ❌ Remove DRAFT-only voice discipline (R12 violation)
- ❌ Hardcode Notion page IDs in Layer 1 templates
- ❌ Add lock-in mechanics (R12 anti-extraction)
- ❌ Skip Strategic DB seeding (Foundation Part 11 reduces value if missing)
- ❌ Naming with personal identifiers in Layer 1 («My Daily Log» instead of «Daily Log»)

### §8.E Update / migration discipline

- Layer 1 updates from upstream (Jetix maintains universal template)
- Fork merges Layer 1 updates without overwriting Layer 2
- Migration script: `tools/personal_os_upgrade.py`
- Backward compatibility mandate (Layer 1 v2 reads v1 data)

### §8.F R12 compliance in fork-friendly design

- **No lock-in:** user owns own data; export anytime to filesystem .md
- **No extraction:** Jetix gets NO data from forked instances (separate workspaces)
- **Fork-and-leave:** user can stop using template anytime; data stays in their Notion workspace
- **Data portability:** filesystem .md = portable canonical
- **Updates voluntary:** Layer 1 updates opt-in, not forced

---

## §9 Phase 8 — 6-7 mermaid + Main consolidated + Roadmap + Summary

### §9.A 6-7 mermaid schemes

| # | Topic | Style | Nodes |
|---|---|---|---|
| **NT-1** | Foundation 11 pillars → Notion lighter mapping | Bipartite | 12-15 |
| **NT-2** | Top-level Notion structure (DBs + Command Center hub + relations) | Graph | 15-20 |
| **NT-3** | Voice intake → distribution routing matrix | Flow | 14-18 |
| **NT-4** | Claude Code ↔ Notion sync pattern (bidirectional + conflict resolution) | Sequence | 10-14 |
| **NT-5** | Fork-and-customize workflow (Universal Layer 1 + niche Layer 2 overlay) | Layered | 12-15 |
| **NT-6** | Implementation roadmap (Week 1 → 2 → 3 → 4 sequencing) | Gantt-style | 14-18 |
| **NT-7 (optional)** | Daily/weekly/monthly/quarterly review cadence loop | Cyclic | 10-12 |

**Style mandate:** colours mild (#fafafa background, dark text), readable WITHOUT extension required, 10-20 nodes max per diagram, no jargon labels.

### §9.B Main consolidated doc — Sections

Format: PARTNER-OFFERING-HUMAN-LANG / CONSOLIDATED-HUMAN-LANGUAGE-PLAN style — sections с emoji, plain prose, conversational tone, mermaid inline, ~10-15K words total.

1. 🎯 Главная мысль (1 paragraph)
2. 📌 Что такое Personal OS Notion template — фундамент простыми словами
3. 🧱 11 кирпичей фундамента — что survives в lighter версии
4. 🗂️ 10-12 баз данных — overview structure
5. 📝 Что в каждой базе (per-DB schema plain prose)
6. 🎤 Voice fill — что куда автоматически (routing matrix plain prose)
7. 🔄 Анализ недели / месяца / квартала / года — готовые шаблоны
8. 🤖 Claude Code подключение — как работает sync + suggestions
9. 🍴 Fork-friendly — как любой человек может взять и адаптировать под свою нишу
10. 🚀 Implementation roadmap — что делаем сначала / потом / в каком порядке
11. ⚠️ Что НЕ делаем (anti-patterns)
12. 🎨 6-7 mermaid схем (inline)
13. ✅ R1 decisions surface (Ruslan picks)
14. 🔗 Cross-refs к deep substrate

### §9.C 00-SUMMARY-FOR-RUSLAN.md — ≤500 words

3-4 min quick read:
- **Что строим** (2 sentences)
- **10-12 баз** (table 2 cols)
- **Voice fill** (3 bullets)
- **Шаблоны анализа** (4 bullets)
- **Fork-friendly** (3 bullets)
- **Implementation order** (5 bullets Week 1-4)
- **R1 picks** (3-5 decisions)
- **К чему ведёт** (2 sentences)

### §9.D Implementation roadmap (Week 1 → 4)

**Week 1 (priority 1):**
- Create workspace + 5 core DBs (Daily Log / Projects / CRM People / Hypotheses / Strategic)
- Seed first entries (today daily / 3 active projects / 5 top contacts / 3 hypotheses / POINT A)
- Command Center hub page

**Week 2:**
- 4-5 secondary DBs (Knowledge / Reviews / Life Pulse / Ideas Bank / Reference)
- First review (week 1 retrospective)
- CC bootstrap setup (filesystem mirror)

**Week 3:**
- Voice intake script setup
- First voice → DRAFT → promote cycle test
- Analysis templates instantiation
- Discovery call template ready (for Wave 1)

**Week 4:**
- Fork niche overlay first example (Дмитрий?)
- Hand-off attempt — first fork by another person
- Iterate based on first fork feedback

### §9.E R1 decisions surface (для Ruslan picks)

1. Final DB count — Lite 8 / Standard 10-12 / Full 14?
2. Voice intake intensity — auto-DRAFT всё OR manual review queue?
3. Niche overlay examples — какие 3-5 (recommend Engineer + Researcher + Entrepreneur + Educator + Humanitarian)?
4. Implementation order — DBs first OR Command Center hub first?
5. CC integration — Notion API vs manual setup для baseline?
6. Layer 1 update mechanism — manual notify OR auto-pull script?
7. Fork distribution channel — public template URL / private invite / git repo scaffolding?
8. Strategic DB schema — single POINT A/POINT B entries OR full Strategic Layer Phase 1 templates analog?

---

## §10 Acceptance criteria

- ✅ 9 phases (0-8) per-phase commit + push (`[notion-os-plan] Phase N`)
- ✅ **Plain language THROUGHOUT** — никакого constitutional jargon / academic vocabulary without translation
- ✅ Russian primary + conversational
- ✅ 6-7 mermaid схем (readable without extension, 10-20 nodes per)
- ✅ Main doc ~10-15K words (concise dense)
- ✅ Стиль = PARTNER-OFFERING-HUMAN-LANG + CONSOLIDATED-HUMAN-LANGUAGE-PLAN reference
- ✅ Cross-refs к deep substrate в footnotes / отдельной секции (не inline mid-prose)
- ✅ R1 surface only — Ruslan picks §9.E decisions
- ✅ Constitutional posture preserved (R1/R2 STRICT/R6/R11/R12 paired-frame/IP-1 STRICT/EP-5/AP-6/append-only)
- ✅ NO LOCK modifications
- ✅ NO Notion API calls / no auto-create pages / no template instantiation (plan only)
- ✅ Per-DB schema concrete (≥10 properties / ≥3 views / explicit relations)
- ✅ Fork-friendly architecture explicit + 3-5 niche overlay examples (full Layer 2 spec each)
- ✅ Voice routing matrix exhaustive (≥7 content types × ≥8 destinations)
- ✅ Analysis templates ready-to-use (≥8 questions per template)
- ✅ Filesystem = source of truth principle preserved (Global Rule 4)
- ✅ DRAFT-only voice discipline preserved

---

## §11 Operational

- Per-phase commit + push
- Russian primary + conversational tone
- R6 provenance cross-refs к existing deliverables (минимально inline, основное в §14 cross-refs)
- NO new research (synthesis only)
- NO R1 strategic prose authoring beyond scaffold
- Pool result only
- ROY swarm dispatch: brigadier + engineering-expert + systems-expert + mgmt-expert + methodology-engineer + influence-ethics-expert cross-consult (R12 fork-and-leave Phase 7) + recruitment-dynamics-expert cross-consult (Phase 7 niche overlays)

---

## §12 Final push

```bash
git add reports/personal-os-notion-template-plan-2026-05-24/ decisions/strategic/PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md
git commit -m "[notion-os-plan] Phase 8 Main + Summary + final push (9 phases / Personal OS Notion template design plan / Foundation 11 pillars lighter mapping / 10-12 databases + Command Center hub / per-DB schema full spec / voice intake routing matrix ≥7 content types × ≥8 destinations / 7 analysis templates ready-to-use / Claude Code ↔ Notion sync filesystem=truth / fork-friendly Layer 1 universal + Layer 2 niche overlay + 5 niche examples Engineer/Researcher/Entrepreneur/Educator/Humanitarian / implementation roadmap Week 1-4 / 6-7 mermaid / main ~10-15K plain Russian prose 13-14 sections style PARTNER-OFFERING-HUMAN-LANG / 8 R1 decisions surface / R12 fork-and-leave embedded / IP-1 STRICT Layer separation / filesystem=truth Global Rule 4)"
git push origin main
```

---

## §13 What this prompt does NOT do

- ❌ NOT new research (synthesis-only)
- ❌ NOT R1 strategic prose authoring
- ❌ NOT Notion API calls / page creation / template instantiation (plan only)
- ❌ NOT modify LOCKED content
- ❌ NOT auto-create skills / tools / scripts (Phase 6 specifies tools but не creates them)
- ❌ NOT jargon-heavy academic language
- ❌ NOT named individuals in Layer 1 (IP-1 — Layer 2 has examples only)
- ❌ NOT third-party integration setup beyond Notion + CC + Wispr
- ❌ NOT skip Layer 2 niche overlay examples (≥3 mandatory)

---

## §14 К чему ведёт

После finish:
- Ruslan reads **00-SUMMARY** (3-4 min) → high-level overview
- Ruslan reads **PERSONAL-OS-NOTION-TEMPLATE-PLAN-2026-05-24.md** main (~45-60 min) → полная картина
- **8 R1 decisions** §9.E picks → implementation order finalized
- Затем →:
  - **Implementation start** — Ruslan picks Option A (manual) / B (CC scripts) / C (Hybrid)
  - **Week 1 build:** 5 core DBs + Command Center + seed entries
  - **Week 2-3:** secondary DBs + voice intake + analysis templates
  - **Week 4:** first fork attempt (Дмитрий или peripheral) → iterate
- **После Personal OS template ready:**
  - Use daily personally (Ruslan)
  - Hand to Дмитрий (T3 audience tester per execution-plan Phase 3 Direction A)
  - Fork to Wave 1 partner candidates as substrate template
  - Возвращаемся к execution-plan Phase 5 sequencing (видео / Wave 1 send / etc.)

---

## §15 Constitutional summary

- ✅ R1 surface only (Ruslan = strategist для DB final list / niche overlays / implementation order)
- ✅ R2 STRICT (no Foundation modifications; reads Foundation as substrate)
- ✅ R6 (cross-refs к Foundation Parts per design claim)
- ✅ R11 (Default-Deny preserved — no auto-creation / API calls / pool result only)
- ✅ R12 paired-frame embedded в Layer 1 design (no lock-in / fork-anytime / data-portability)
- ✅ IP-1 STRICT (Foundation roles abstract; instance specifics = Layer 2 overlay separate)
- ✅ EP-5 (F2 Foundation substrate + F3 derivative Notion mapping)
- ✅ AP-6 (3-5 niche overlay examples preserve options, no premature selection)
- ✅ Append-only (new prompt + new design doc; existing untouched)
- ✅ Global Rule 4 — Filesystem = source of truth preserved

---

*Prompt closure 2026-05-24 evening. Per Ruslan voice ack «шаблон в Notion / на фундаменте 11 pillars / lighter / fork-friendly под любую нишу / Claude Code подключать / voice fill / шаблон анализа недели и месяца / красота невообразимо круто / прям плотнейший / на базе нашей философии». Per MAX-density mandate (universal Personal OS template = daily-use cornerstone + fork distribution artefact). Per memory feedback_prompt_explanation_required satisfied via `_EXPLAIN-personal-os-notion-template-plan-2026-05-24.md`.*
