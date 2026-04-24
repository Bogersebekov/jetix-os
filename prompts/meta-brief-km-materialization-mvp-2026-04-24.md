---
title: Meta-Brief — KM Architecture Materialization MVP (A1 + B2 + B3-merged + Company-as-Code)
date: 2026-04-24
type: meta-brief
author: Cloud Cowork (short brief; deep execution prompt to be written by CC on server)
target_executor_this_pass: Claude Code on server (writes the deep execution prompt)
target_executor_next_pass: fresh CC session (physically implements MVP over 7 days per Stage-Gated checkpoints)
output_this_pass: prompts/km-materialization-mvp-execution-2026-04-XX.md (deep execution prompt, 1800-2800 lines, 1000% depth)
output_next_pass: physical MVP in repo + decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-XX.md (≥3000-word execution report)
estimated_duration_this_pass: 1-2h (prompt-writing only)
estimated_duration_next_pass: ~7 days across 5 Stage-Gated phases (≤20-30h swarm work + 4-6 Ruslan review gates)
precedes: first quick-money P1 project bootstrap → first Mittelstand outreach batch
relates_to:
  - decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md (source — 6 variant analysis)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md (local-first / client-private positioning)
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md (Pillars 2+3)
  - memory/project_jetix_private_library_knowledge_leverage.md (moat philosophy)
locked_decisions_referenced: [D13, D17, D18, D19, D20, D21, D24, W-5, HD-01, HD-02]
m_class_budget_impact: 1 structural M-task (this materialization); leaves 1 slot open for M3 or companion
---

# META-BRIEF — KM Architecture Materialization MVP

## §0 Your task in THIS session

Write a **deep execution prompt** (1800-2800 lines, 1000% depth) that a **separate next Claude Code session will execute** over ~7 days to PHYSICALLY materialize Ruslan's chosen KM architecture MVP in the repo. You are NOT implementing anything this session. Stop after prompt committed + pushed.

**Output path:** `prompts/km-materialization-mvp-execution-2026-04-<XX>.md`

## §1 Why this split

Per Ruslan's durable rule (memory/feedback_cc_writes_own_deep_prompts.md): Cloud Cowork specifies short briefs; CC on server writes deep prompts with sub-agents + 1M context + full repo access. Separate fresh CC session executes. This meta-brief is the short brief.

## §2 Ruslan's Gate-2 decision on KM Architecture Variants (2026-04-24)

After reading `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` and the 6 variant drafts, Ruslan's materialization shape:

| Variant | Decision | Rationale |
|---|---|---|
| **A1 Karpathy++** | **ADOPT FULL** as wiki substrate | Lowest cost; ready today; supports UC-9 Phase-A policy + UC-10 via structured citations |
| A2 Federated peer holons | **DEFERRED** — activate on trigger "first paying client signed" | Not needed at €0; keep knowledge for Phase-B |
| A3 GraphRAG+HippoRAG | **DEFERRED** — activate on trigger "3K+ pages per client" | Over-engineering at G1 |
| B1 Thin namespaces | **REJECTED** — not enough structure for Jetix needs | Confirmed too thin |
| **B2 Rich mini-swarm** | **ADOPT FULL** as project-management pattern | Cagan + PMBOK + mini-swarm = right shape for Jetix serious projects |
| **B3 Adaptive stage-gates** | **MERGE INTO B2** as internal mechanic | Keep stage-gate predicates + reversibility for `bets`/`research` tiers + intra-B2 promotion |

**Cross-cutting principle Ruslan made explicit:** *"в режиме GitHub работала — компания как код, знания как код, чтобы это вместе соединить"*. Everything git-versioned, declarative config in `.claude/config/*.yaml`, atomic commits, real rollback via `git revert`, every KB change = commit. This is the operational manifestation of D17 filesystem-SoT + W-5 Two-level CE + knowledge-as-moat.

## §3 What the execution prompt must make the next session physically build

### Part A — A1 Karpathy++ substrate (Days 1-2)

1. `.claude/config/wiki-roots.yaml` enhanced with `clients:` section supporting `WIKI_ROOT_CLIENT_ID` env-var for per-client namespacing (Phase-A policy-based isolation; physical-isolation via A2 deferred)
2. `swarm/wiki/edges.jsonl` populated beyond current 4-line stub — real typed edges emerging from existing content (minimum 50 edges across existing pages)
3. `/ingest` skill fully functional for: YouTube URLs (transcript extraction via yt-dlp), web articles (readability parsing), PDF files, plain markdown files → creates 5-8 concept pages per ingest + 8-15 new edges + appears in `wiki/log.md`
4. `/ask` skill with `OFFLINE_MODE=1` path: when flag set, returns top-10 structured citations from wiki (no LLM synthesis call) — proves UC-10 offline path without requiring local LLM
5. **Optional (time-permitting):** ollama + Mistral-7B-Q4 (Apache 2.0) setup documented in `swarm/lib/offline-llm/README.md` + integration into `/ask --local-llm` path
6. `/consolidate --weekly` cron-ready skill: Sunday 21:00 generates `wiki/digests/<ISO-week>.md` covering new concepts + new edges + emergent themes
7. `/build-graph` skill operational — rebuilds community clusters using existing edges.jsonl; output to `wiki/graph/communities.jsonl`
8. `/lint` check extended: reports dangling edges, orphan concepts, missing frontmatter, duplicated slugs

### Part B — B2 Rich mini-swarm (Days 3-5)

1. `.claude/config/project-types.yaml` declarative templates for 4 project types: `consulting` (9 files including icp.md + pipeline.md + leads/ + offline-inference-spec.md), `research` (6 files including hypotheses.md + sources.md), `product` (7 files including problem-explored.md + solution-hypothesis.md + validation.md), `bets` (adaptive 3-file starting scaffold from B3 mechanic)
2. `/project-bootstrap <slug> <priority> --type=<type> [--client=<client-id>] [--adaptive]` skill creates project directory in `swarm/wiki/operations/<slug>/` OR `clients/<client-id>/swarm/wiki/operations/<slug>/`
3. **Mandatory frontmatter fields** in every project `_moc.md`:
   - `problem_statement:` (Cagan — empty → `/lint` fails)
   - `kill_criteria:` (Hamel-binary — empty → `/lint` fails)
   - `kpi_targets:` (measurable — empty → `/lint` fails on P1/P2)
   - `project_type:` (enum)
   - `priority:` (P1/P2/P3/P4)
   - `state:` (state machine: active | paused | pivoted | tombstoned | killed)
   - `pmbok_phase:` (Initiated | Planned | Executing | Monitoring | Closed)
4. **Mini-swarm spawning** for P1/P2 projects: `.claude/agents/project-brigadier.md` template + 2 default experts per project_type (consulting → mgmt + sales-researcher; research → systems + philosophy; product → engineering + philosophy; bets → investor + philosophy)
5. Project-brigadier has its OWN `≤7 active tasks` limit (vs canonical brigadier's ≤20) — no attention competition
6. `agents/<project-slug>-brigadier/strategies.md` auto-created as empty scaffold
7. `/project-review <slug>` skill produces weekly digest per project (Monday 08:00 cron): light-signal (🟢🟡🔴), progress since last week, open blockers, stage-gate status
8. `/project-archive <slug> --reason=<killed|closed|pivoted>` moves to `swarm/wiki/operations/_archived/<slug>/` with reason + final state preserved

### Part C — B3 stage-gate mechanic merged into B2 (Day 5)

1. `_moc.md` frontmatter supports optional `stage_gates:` block declaring Hamel-binary predicates:
   ```yaml
   stage_gates:
     SG-1: "count(leads/*.md) >= 3"
     SG-2: "count(hypotheses.md:supported) >= 2"
     SG-3: "contract_signed_count >= 1"
     SG-4: "cycle_count >= 5 AND active_tasks_avg >= 5"
   ```
2. `/lint --check-stage-gates` daily cron evaluates each predicate; on fire → writes event to `<project>/history.md` + notifies brigadier
3. **Auto-spawn protocol** for adaptive projects: SG fires → create files/folders per `project-types.yaml` promotion rule (e.g., SG-1 fires on `bets` project → auto-spawn `leads/` + `pipeline.md`, promote from adaptive to consulting template)
4. `/project-de-morph <slug> --rollback-to=<SG-N>` skill: reversibility — removes files spawned after specified SG, updates history.md
5. **Promotion trigger:** when `bets` or `research` project hits SG-4 + has mini-swarm criteria → can promote to full B2 scaffold via `/project-promote <slug>` (Ruslan ack'd one-line command)
6. `philosophy-expert` reviews each new SG predicate in `.claude/config/project-types.yaml` for "is this really Hamel-binary?" — prevents predicate drift

### Part D — Company-as-code / Knowledge-as-code principle enforcement (cross-cutting, all days)

1. Every single file creation/modification committed with structured commit message: `[<area>] <verb> <what> (<why>)` — e.g. `[km-mvp] create quick-money project scaffold (materialize first B2 P1 project)`
2. `.claude/config/*.yaml` files are declarative source-of-truth — NO hardcoded Jetix-specific paths in skill code; everything configurable
3. `git log --follow` must give clean provenance for any file; no force-pushes, no amends after push, no --no-verify
4. `/company-status` skill produces compact git-based system snapshot: active projects / active clients / recent ingests / open SGs / health.md counters — all from git + filesystem, no external deps
5. `/knowledge-diff <from-date> <to-date>` skill: shows what wiki/concepts changed between two dates via `git log`
6. `CLAUDE.md` updated post-materialization reflecting new skills, new project structure, new config files, new KM principles

### Part E — Apply MVP to real Jetix work (Days 6-7)

1. **Bootstrap `quick-money` project** via new infrastructure: `/project-bootstrap quick-money P1 --type=consulting` — materialize with real Jetix context (ICP: DACH Mittelstand AI-curious, 50-500 employees; offer: consulting + productizing 10 templates)
2. **Populate initial `quick-money/icp.md`** from existing `decisions/JETIX-VISION.md` D22 ICP 5 criteria + D22 11 archetypes
3. **Spawn mini-swarm** for quick-money: project-brigadier + mgmt-expert + sales-researcher
4. **Run one end-to-end workflow demo:** `/ingest` a reference Mittelstand AI article → concept pages created → `/ask "как применить [concept] к quick-money ICP"` → answer with citations → insight written to `quick-money/history.md`
5. **Bootstrap one `research` project adaptively:** `/project-bootstrap levenchuk-deep-dive P3 --type=research --adaptive` — 3-file start, demonstrate stage-gates + reversibility mechanism empty but live
6. **Weekly digest demo run:** `/consolidate --weekly` produces first digest file for Cloud Cowork + Ruslan to review

### Part F — Verification + Stage-Gated Pause

After Parts A-E complete, before Part G report:
- Verification matrix (per-part smoke checks + integration tests)
- Specific bash commands: test /ingest against a known YouTube URL, test /ask with OFFLINE_MODE=1, test /project-bootstrap creating each of 4 project types, test stage-gate firing on a test fixture, test `/project-de-morph` reversibility
- `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>.md` packet
- Halt for Ruslan review

### Part G — Execution Report + Compound Step

After Ruslan ack:
- `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md` (≥3000 words):
  - Per-Part summary (what built / where / how verified)
  - Adaptations made (any place spec was ambiguous)
  - Emergent insights / surprises
  - Quick-money first project bootstrap results — real content review
  - Research project adaptive bootstrap results
  - Verification matrix with evidence
  - Lessons for next cycle
  - Recommended next M-class tasks (likely: M3 solo-vs-matrix, or A2 trigger-check infrastructure, or first client outreach kickoff)
- Compound step: 4-part DRR rules → `agents/brigadier/strategies.md`; agent-improvements entries for all 5 experts (what each learned about KM patterns)
- Cycle-archive entry

## §4 Critical framing for the deep prompt

Include verbatim (or equivalent-strength) in §1 Mission of written execution prompt:

> **This materialization is THE moment Jetix stops planning and starts compounding.** Every file you create lives for years — wiki entries accumulate, project scaffolds become templates for future clients, the first `quick-money` project bootstrap is the seed for €50K Q2 2026 trajectory. Shallow wiring = broken KB forever.
>
> 1000% depth. No "good enough". Every skill you write must: pass `bash -n` + executable bit + shebang + `set -euo pipefail` + 1-line purpose comment; every frontmatter complete per CLAUDE.md conventions; every config file declarative + git-versioned + no Jetix-specific hardcoding.
>
> Ruslan's Gate-2 context: 6 variants analyzed, 3 adopted with specific shapes (A1 full, B2 full, B3 merged into B2), cross-cutting "company-as-code / knowledge-as-code" principle. Honor every choice. Do not re-litigate variant decisions. Do not add A2/A3/B1 elements — they are explicitly deferred.

## §5 What the MVP must enable CONCRETELY (use cases to work day-1)

Deep prompt must demand each of these works end-to-end before Part F:

- **UC-INGEST-1:** Ruslan shares YouTube lecture URL → `/ingest <url>` produces 5-8 concept pages + ≥10 edges + appears in `wiki/log.md` + triggers dedup check
- **UC-ASK-1:** Ruslan asks `/ask "how does systems-thinking apply to Mittelstand outreach"` → answer synthesized from wiki with ≥3 citations + insight written back to wiki/insights/
- **UC-ASK-OFFLINE:** Same query with `OFFLINE_MODE=1` → top-10 structured citations returned, no external LLM call (verifiable via tcpdump: zero outbound TCP on :443)
- **UC-DIGEST:** `/consolidate --weekly` produces `wiki/digests/2026-W17.md` with real content from the week's ingests
- **UC-PROJECT-CONSULTING:** `/project-bootstrap quick-money P1 --type=consulting` creates full 9-file scaffold + spawns mini-swarm + rejects if `problem_statement` or `kill_criteria` missing
- **UC-PROJECT-ADAPTIVE:** `/project-bootstrap test-bet P4 --type=bets --adaptive` creates 3-file scaffold; SG-1 fires when 3 test lead files created → auto-spawn `leads/` folder
- **UC-REVERSE:** `/project-de-morph test-bet --rollback-to=SG-0` removes auto-spawned files, updates history.md
- **UC-REVIEW:** `/project-review quick-money` produces weekly status with 🟢🟡🔴 + blockers
- **UC-ISOLATION-DEMO:** Agent with `WIKI_ROOT_CLIENT_ID=demo-client-a` attempts to read `clients/demo-client-b/wiki/...` → filesystem-level denial (different directory) + config-level denial (wiki-roots.yaml) → demonstrable via bash audit script
- **UC-COMPANY-STATUS:** `/company-status` produces compact snapshot: "8 active projects / 1 active client (demo) / 12 ingests this week / 3 open SGs"

If any UC fails before Part F — stop, fix, re-verify. Do not ship broken.

## §6 Artefact sources executor MUST read (full list, treat as authoritative)

- `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` (Ruslan Gate-2 anchor)
- 6 variant drafts under `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-*.md` (especially A1, B2, B3 for direct implementation spec)
- `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` (local-first / client-private positioning — UC-9/10 rationale)
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (Pillars 2+3 kernel)
- `decisions/JETIX-VISION.md` D22 ICP 5 criteria + 11 archetypes (for quick-money bootstrap)
- `decisions/JETIX-PLAN.md` D3 Phase 1 targets (€50K Q2 2026, consulting + producer center)
- `decisions/JETIX-ARCHITECTURE-BRIEF.md` D4 foundation layer
- `swarm/lib/shared-protocols.md` (9-section runtime contract)
- `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` (existing wiki v3)
- `.claude/agents/brigadier.md` (canonical brigadier for reference; project-brigadier template derives)
- `CLAUDE.md` (project conventions, file structure)

## §7 Locked decisions honored (non-negotiable)

- **D13** Open surface / Closed core — templates/methodology published; client KB stays closed
- **D17** Filesystem = SoT — all materialization in git, Notion optional view only
- **D18** Productization over hours — `/project-bootstrap` is productization of Jetix's project-spawning know-how
- **D19** $1T trajectory — architecture must not preclude G2/G3/G4 migration paths (A2 deferred, not impossible)
- **D20** USB-C positioning — wiki works with any underlying LLM (OpenAI/Anthropic/Llama/DeepSeek) via `$LLM_BACKEND` abstraction
- **D21** Matchmaker + roy-replication — mini-swarms are "baby roys"; each project gets its own
- **D24** Open-source research — research-type projects may be published externally; consulting/product stay closed
- **W-5** Two-level Compounding Engineering — compound DRR at Part G
- **HD-01** €50K gate referenced in project kpi_targets where applicable
- **HD-02** N=2 M-class — this materialization = 1 M-slot; leaves 1 slot for M3 or emergency structural fix
- **24 Locks + W-1..W-12 + FPF E-1..E-18 + shared-protocols 9 sections** unchanged
- **Legacy coexistence:** 14 legacy agents + v2 `wiki/` untouched; all new work under `swarm/` + new skills in `.claude/skills/`
- **Max-subscription discipline:** `unset ANTHROPIC_API_KEY` before every launch; no paid API calls anywhere
- **No amend, no --no-verify, no force-push**

## §8 Operating mode: Stage-Gated with intra-phase checkpoints

The 7-day sprint has 5 natural phases (Parts A/B/C/D/E). Executor may flow between them continuously but **MUST write intra-phase commits + push** so Ruslan can peek at progress via commits.

Between Part E completion and Part F verification → brief checkpoint (not blocking pause). Between Part F verification pass and Part G report writing → **mandatory Stage-Gated pause** with `AWAITING-APPROVAL` packet. Full-Auto NOT authorized for Part G.

Commit cadence: per-skill creation or per-logical-unit (not per-file). Target: ~15-25 commits across the 7 days.

## §9 Anti-scope (deep prompt must enforce)

- **NO implementing A2 Federated peer holons** — deferred to trigger "first paying client"
- **NO implementing A3 GraphRAG / HippoRAG / PPR / community summaries** — deferred to trigger "3K+ pages per client"
- **NO implementing B1 Thin namespaces** — rejected variant
- **NO promoting variant drafts out of `swarm/wiki/drafts/`** — they stay as reference; MVP is fresh implementation based on variant specs
- **NO touching legacy** `wiki/` v2, 14 legacy agents, or v1 knowledge-base/ migration
- **NO Notion writes from executor** — D17 filesystem-SoT; Ruslan updates Notion as he sees fit
- **NO M3 execution** — deferred per HD-02 companion slot
- **NO hardcoded Jetix-specific paths in skill code** — everything through config
- **NO API-key references in any committed file** — grep-test must return 0 hits
- **NO "good enough" attitude** — if UC fails, fix

## §10 What the written execution prompt should look like

- **Length:** 1800-2800 lines
- **Structure:** §1 Mission + critical framing / §2 Scope (Parts A-G with per-day breakdown) / §3 Use-cases that must work (UC-INGEST-1 through UC-COMPANY-STATUS) / §4 Artefact sources / §5 Locked decisions / §6 Commit cadence / §7 Verification protocol / §8 Stage-Gated pause spec / §9 Part G report format / §10 Anti-scope / §11 Escalation / §12 Definition of done / §13 Executor-facing cheat sheet
- **Style:** Imperative, numbered, file paths in backticks, bash snippets where relevant
- **Depth markers:** per-Part word-count floors where quality matters (e.g. "Part G report per-Part summary: ≥300 words each")
- **Executor-facing cheat sheet §13:** condensed one-pager with ORDER / KEY DON'TS / KEY DOs / COMMITS target / ESCALATION path

## §11 Definition of done for THIS session (Cloud Cowork brief)

1. `prompts/km-materialization-mvp-execution-2026-04-<XX>.md` written (1800-2800 lines)
2. Committed to `claude/jolly-margulis-915d34` + pushed to origin
3. Brief reply to Ruslan: file path + line count + 3-sentence summary + ready-to-launch command snippet + estimated execution duration

## §12 Escalation

If while writing the execution prompt you hit:
- Contradictions between variant drafts (e.g. B2 draft assumes A2 substrate; Ruslan decision reshapes B2 atop A1)
- Ambiguity on stage-gate predicate DSL
- Uncertainty on mini-swarm agent file format (copy brigadier.md template? minimal subset?)
- How to merge B3 adaptive mechanic into B2 without doubling complexity

→ Stop, write `prompts/AMBIGUITY-km-materialization-<date>.md` with contradiction, notify via commit. Do not guess.

---

*End of meta-brief. Execute.*
