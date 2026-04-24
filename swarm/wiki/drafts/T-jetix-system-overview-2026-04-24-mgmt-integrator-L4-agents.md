---
title: "§L4 Agent Layer — Holding-Style Intelligent Workforce"
type: integrated-synthesis
produced_by: mgmt-expert
mode: integrator
cycle_id: cyc-2026-04-24-km-mat-mvp
task_id: T-jetix-system-overview-2026-04-24
section_id: L4
sources:
  - {path: ".claude/agents/brigadier.md", range: "§1a-§1d"}
  - {path: ".claude/agents/engineering-expert.md", range: "§1a-§1b"}
  - {path: ".claude/agents/mgmt-expert.md", range: "§1a-§2.5"}
  - {path: ".claude/agents/systems-expert.md", range: "§1a-§1b"}
  - {path: ".claude/agents/philosophy-expert.md", range: "frontmatter + §1"}
  - {path: ".claude/agents/investor-expert.md", range: "§1a"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D26 Team 50-100"}
  - {path: "swarm/lib/shared-protocols.md", range: "§1-§6"}
  - {path: "CLAUDE.md", range: "Agent Roster"}
  - {path: ".claude/agents/strategist.md", range: "frontmatter"}
  - {path: ".claude/agents/knowledge-synth.md", range: "frontmatter"}
  - {path: ".claude/agents/manager.md", range: "frontmatter"}
  - {path: ".claude/agents/life-coach.md", range: "frontmatter"}
  - {path: ".claude/agents/personal-assistant.md", range: "frontmatter"}
  - {path: ".claude/agents/inbox-processor.md", range: "frontmatter"}
  - {path: ".claude/agents/sales-lead.md", range: "frontmatter"}
  - {path: ".claude/agents/sales-researcher.md", range: "frontmatter"}
  - {path: ".claude/agents/sales-outreach.md", range: "frontmatter"}
  - {path: ".claude/agents/meta-agent.md", range: "frontmatter"}
  - {path: ".claude/agents/crazy-agent.md", range: "frontmatter"}
  - {path: ".claude/agents/system-admin.md", range: "frontmatter"}
  - {path: ".claude/agents/staging-writer.md", range: "frontmatter"}
  - {path: ".claude/agents/sweep-worker.md", range: "frontmatter"}
  - {path: "reports/review_2026-04-24.md", range: "decisions #119 (audio_510 Team 50-100)"}
provenance_inline: true
confidence: high
confidence_method: structured-rubric
created: 2026-04-24
layer: L4
layers_above: [L5-knowledge, L6-cycles, L7-swarm-protocols, L8-decisions, L9-HITL]
layers_below: [L3-strategies, L2-corpus, L1-wiki, L0-git]
related: []
pipeline: drafted
state: drafted
---

# §L4 — Agent Layer: Holding-Style Intelligent Workforce

## 1. Mission

Layer 4 is the **intelligent workforce** of Jetix OS. It implements the
holding-with-agents model locked in D26 [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]:
Jetix is not a one-person company. The target is 50–100 humans working
as a holding — and from day 1, software agents fill every role that does
not yet have a human counterpart.

Concretely, L4 today contains 20 agents divided into two populations:

- **ROY swarm (6 agents):** brigadier + 5 domain experts, built
  2026-04-23, operating on the ROY-ALIGNMENT 5×4 dispatch matrix.
  These are the primary production machinery.
- **Legacy tier (14 agents):** the original Jetix OS crew, defined in
  `.claude/agents/` and listed in CLAUDE.md, untouchable in Phase A
  per brigadier §1a discipline [src:.claude/agents/brigadier.md#§1a].

The architectural principle: **domain authority, not orchestration
authority.** Every agent has a bounded scope. Brigadier holds routing.
Experts hold domain judgment. No agent overrides another's domain
silently — the only resolution path is dissent-preservation (AP-6) or
HITL escalation [src:swarm/lib/shared-protocols.md#§4].

Per D25 company-as-code, every agent's behaviour is declared in a
versioned `.claude/agents/<name>.md` file, committed, attributable,
and rollback-able [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25].
The agent is the code; the code is the company.

## 2. What Lives Here — Complete Agent Roster (20 agents)

### ROY Swarm — Phase A (6 agents, built 2026-04-23)

| Agent | Model | Dept / Niche | Layer residence | Status Phase A |
|---|---|---|---|---|
| **brigadier** | Opus | Meta / swarm-wide | L4 + dispatches L6 cycles | Active — sole canonical writer (Q2) |
| **engineering-expert** | Sonnet 4.6 | Engineering | L4 draft-cell | Active — 4 modes |
| **mgmt-expert** | Sonnet 4.6 | Management | L4 draft-cell | Active — 4 modes |
| **systems-expert** | Sonnet 4.6 | Systems | L4 draft-cell | Active — 4 modes |
| **philosophy-expert** | Sonnet 4.6 | Philosophy / epistemics | L4 draft-cell | Active — 4 modes |
| **investor-expert** | Sonnet 4.6 | Investing / capital | L4 draft-cell | Active — 4 modes |

### Legacy Tier — Phase A (14 agents, untouchable per brigadier §1a)

| Agent | Model | Dept / Niche | Layer residence | Status Phase A |
|---|---|---|---|---|
| **manager** | Sonnet 4.6 | MGMT / operations | L4 legacy | Untouchable — not integrated into ROY matrix |
| **personal-assistant** | Haiku 4.5 | OPS / productivity | L4 legacy | Untouchable |
| **system-admin** | Haiku 4.5 | OPS / infrastructure | L4 legacy | Untouchable |
| **sales-lead** | Sonnet 4.6 | Sales / pipeline | L4 legacy | Untouchable |
| **sales-researcher** | Haiku 4.5 | Sales / intelligence | L4 legacy | Untouchable |
| **sales-outreach** | Haiku 4.5 | Sales / outreach | L4 legacy | Untouchable |
| **inbox-processor** | Haiku 4.5 | Brain / triage | L4 legacy | Untouchable |
| **crazy-agent** | Sonnet 4.6 | Meta / creative | L4 legacy | Untouchable |
| **knowledge-synth** | Sonnet 4.6 | Brain / synthesis | L4 legacy | Untouchable |
| **strategist** | Opus 4.6 | MGMT / strategy | L4 legacy | Untouchable — strategic decisions pre-ROY |
| **life-coach** | Sonnet 4.6 | Life / wellness | L4 legacy | Untouchable |
| **meta-agent** | Sonnet 4.6 | Meta / audit | L4 legacy | Untouchable |
| **staging-writer** | Sonnet 4.6 | Task-scoped / writer | L4 task-scoped | Untouchable |
| **sweep-worker** | Sonnet 4.6 | Task-scoped / batch | L4 task-scoped | Untouchable |

**CLAUDE.md reconciliation note.** CLAUDE.md Agent Roster lists 12 agents
by name; actual `.claude/agents/` directory contains 20 files. The 8 not
listed in CLAUDE.md are: the 6 ROY swarm agents (built post-CLAUDE.md),
staging-writer, and sweep-worker (task-scoped additions). The CLAUDE.md
Roster is a legacy snapshot and has not been updated to reflect ROY
construction. This is an open question (see §11).

## 3. The 5×4 Dispatch Matrix

The core machinery of the ROY swarm is a 5 domain experts × 4 role-modes
matrix = **20 invocation cells** [src:swarm/lib/shared-protocols.md#§1]:

```
          critic    optimizer   integrator  scalability
engineering  [E×C]    [E×O]       [E×I]      [E×S]
mgmt         [M×C]    [M×O]       [M×I]      [M×S]
systems      [S×C]    [S×O]       [S×I]      [S×S]
philosophy   [P×C]    [P×O]       [P×I]      [P×S]
investor     [I×C]    [I×O]       [I×I]      [I×S]
```

Brigadier sits **outside** the matrix. It dispatches cells via `Task()`
with mandatory `<domain> × <mode>` prefix on every prompt. A cell
receives the brief, reads its system file + shared-protocols +
strategies.md, produces a structured draft, and returns a YAML packet
per shared-protocols §3. Brigadier integrates cell returns, runs the
§5.5.5 provenance gate, and promotes to canonical `swarm/wiki/`.

Mode semantics per cell:
- **critic** — conformance check against acceptance predicate; ≥5 binary
  pass/fail checks; ≥2 alternatives + kill-conditions
- **optimizer** — delta over existing baseline; invariant-check
  (WLNK/MONO/IDEM/COMM/LOC); before/after measurable delta
- **integrator** — per-claim (F, ClaimScope, R) triples; dissent preservation
  (never averaged); residual open-questions enumerated
- **scalability** — BOSC-A-T-X projection per horizon gate; MHT events;
  Janus degraded-mode spec; antifragility check

No cell can call another cell directly. Cross-cell knowledge flows only
through `swarm/wiki/` reads — the cross-cell-reference-protocol
[src:swarm/lib/shared-protocols.md#§6]. Peer input needs are expressed via
`escalations[]{trigger: peer-input-needed}` returned to brigadier, which
then dispatches the second cell.

## 4. Five-Layer Per-Agent Memory

Every agent in L4 operates a structured 5-layer memory stack per CLAUDE.md
wiki architecture:

| Layer | Path | What lives here | Who writes |
|---|---|---|---|
| **L1 Core** | `.claude/agents/<name>.md` | System prompt — identity, domain, modes, anti-patterns | Brigadier (ROY); legacy authors (14) |
| **L2 Strategies** | `agents/<name>/strategies.md` | Accumulated 4-part DRR rules; per-rule hit/miss ratios | Expert self-writes (Layer-2 exception per shared-protocols §1) |
| **L3 Scratchpad** | `agents/<name>/scratchpad.md` | Working memory for current task; ephemeral | Expert writes |
| **L4 Niche** | `agents/<name>/niche/` | Symlinks into `wiki/niches/{niche}/` — each agent's slice of the shared wiki | Brigadier maintains symlinks |
| **L5 Recall** | `comms/mailboxes/<name>.jsonl` | Append-only message log; per-agent inbox | Brigadier + peers write; agent reads |

The memory architecture has a key principle: **agents do not have
isolated knowledge bases.** The shared `swarm/wiki/` (v3) is the single
truth layer; each agent reads its relevant slice via niche symlinks. This
prevents knowledge silos and means every compounded insight in `strategies.md`
eventually propagates to all agents through wiki promotion.

For ROY experts, strategies.md carries 4-part DRR entries:
`Decision / Reasoning / Result / Review` with per-rule SemVer versioning
and `ratio: {hits, misses}` counters harvested at each Compound step.

## 5. Holding-with-Agents — The D26 Architecture

D26 explicitly defines the Jetix target structure: a holding of 50–100
humans, not a solopreneur operation [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26].
Verbatim: *"Jetix будет не one person company, а команда из 50-100 человек,
работающая как холдинг."* [src:reports/review_2026-04-24.md#decision-119-audio_510]

In this model, agents are not assistants — they are **holding subsidiaries**
with declared domain authority. The organizational topology is:

```
                        ┌─────────────────────────────────┐
                        │        Ruslan (HITL)             │
                        │  direction-setting / approvals   │
                        └──────────────┬──────────────────┘
                                       │
                              ┌────────▼────────┐
                              │   brigadier     │
                              │  (orchestrator) │
                              └────┬──────┬─────┘
           ┌──────────┬────────────┼───────┼────────────────┐
           ▼          ▼            ▼       ▼                 ▼
    [engineering] [mgmt]    [systems] [philosophy]    [investor]
     × 4 modes  × 4 modes  × 4 modes  × 4 modes       × 4 modes
       (draft cells — write to swarm/wiki/drafts/)

           ┌──────────────────────────────────────────────┐
           │   Legacy ring (14 agents — Phase A frozen)   │
           │  manager / personal-assistant / system-admin │
           │  sales-lead / sales-researcher / sales-       │
           │  outreach / inbox-processor / crazy-agent /  │
           │  knowledge-synth / strategist / life-coach / │
           │  meta-agent / staging-writer / sweep-worker  │
           └──────────────────────────────────────────────┘
```

The holding analogy maps as follows: brigadier is the corporate HQ
(routing, governance, consolidation); domain experts are wholly-owned
subsidiaries with defined charters (scope walls); legacy agents are
independent operating units with their own protocols (hub-and-spoke
per CLAUDE.md global rule 8). The holding's single-writer discipline
(Q2 lock) ensures one entity — brigadier — consolidates knowledge into
canonical wiki, exactly as a holding's treasury consolidates financials.

Cross-cell interaction uses the cross-cell-reference-protocol: cells
read each other's promoted wiki pages, never invoke each other directly.
When a cell requires peer analysis, it returns an escalation to brigadier,
which dispatches the peer cell in a subsequent turn. This prevents
circular authority claims and preserves the holding's clear chain of
reporting [src:swarm/lib/shared-protocols.md#§6].

## 6. Boundaries

**In-scope for L4:**
- Agent definitions (identity, domain footprint, modes, memory)
- The 5×4 matrix structure and dispatch contract
- Per-agent memory layers (Core → Strategies → Scratchpad → Niche → Recall)
- Agent population: ROY 6 + Legacy 14 = 20 total
- D26 holding-with-agents model as organizational frame

**Out-of-scope for L4 (belongs to adjacent layers):**
- Routing logic itself → L9 shared-protocols (§§1–9 runtime contract)
- Compound step mechanics → L6 cycles (how learnings are extracted)
- Storage / wiki architecture → L1 wiki (D3–D6 specs)
- HITL gate mechanics → L9 AWAITING-APPROVAL protocol (shared-protocols §4)
- Per-agent domain knowledge (frameworks, patterns, heuristics) → each agent's Core memory file

## 7. Interfaces

**Reads from:**
- L0 git state (branch `claude/jolly-margulis-915d34` — all agents read
  current-branch state as their operational context)
- L1 wiki (`swarm/wiki/` — canonical source for inter-cell knowledge; also
  legacy `wiki/` via cross-tree-ref edge type only)
- L3 strategies (`agents/<name>/strategies.md` — each agent re-reads own
  strategies at every Task invocation before acting)

**Writes to:**
- L1 via brigadier: brigadier is the sole writer to `swarm/wiki/<canonical>/`;
  expert cells write only to `swarm/wiki/drafts/<task-id>-<expert>-*`
- Own strategies.md: expert self-write exception per shared-protocols §1
- L6 cycle logs: brigadier writes `swarm/logs/<cycle-id>/cycle-log.md`
  at cycle-close

**Invokes:**
- L9 AWAITING-APPROVAL gates: any agent that encounters a `requires-approval`
  condition returns an escalation packet; brigadier writes the gate file
  to `swarm/gates/AWAITING-APPROVAL-<id>-<YYYY-MM-DD>.md`; Ruslan acks

## 8. Current Status — 2026-04-24

- **ROY swarm:** 6 agents live and operational as of 2026-04-23.
  brigadier, engineering-expert, mgmt-expert, systems-expert,
  philosophy-expert, investor-expert — each with full §1–§9 Core memory
  and initialized `agents/<name>/strategies.md`.
- **Cycles compounded:** 3 cycles completed under the ROY matrix; each
  cycle produced compounded DRR entries in per-agent strategies files;
  brigadier's `agents/brigadier/strategies.md` holds the cross-agent
  improvement proposals.
- **Single-writer discipline:** Q2 lock active; brigadier is sole writer
  to `swarm/wiki/<canonical>/`; all 6 ROY agents write drafts only.
- **Legacy ring:** 14 agents per `.claude/agents/` — untouchable in Phase A
  per brigadier §1a. No modifications, no integrations into ROY matrix.
  They operate on their original hub-and-spoke model (CLAUDE.md global rule 8).
- **v2 wiki:** untouchable. Cross-references from v3 go through
  `cross-tree-ref` edge type (D3 §3.2.12) recorded in
  `swarm/wiki/graph/cross-tree.jsonl`.
- **CLAUDE.md roster:** lists 12 agents; actual count is 20 (12 legacy
  + 6 ROY + 2 task-scoped). Reconciliation is an open question (§11).

## 9. Evolution Path: Phase 1 → Phase 3+

Aligned with D26 target trajectory and brigadier §1d split-trigger rules:

| Phase | Revenue gate | Agent Layer state |
|---|---|---|
| **Phase 1 (current)** | €0 → €50K | Sole founder + 20 agents. ROY swarm as primary production machinery. Legacy 14 as auxiliary / parallel track. 3 cycles compounded. |
| **Phase 2** | €200K | First 2–3 human hires join core team alongside agents. Each hire gets an onboarding protocol (mgmt-expert Watkins 90-day pattern, Phase B procurement). Humans and agents share L4; humans write directly to wiki (as brigadier-proxied contributors). |
| **Phase 2b** | ~€1M | PM split trigger may fire (mgmt-expert §1d split_trigger): pm-expert + people-expert. First 20 team members. Sub-domains may warrant specialized expert cells (e.g. sales-expert). Legacy 14 migration decision surfaces: migrate to ROY format or retire. |
| **Phase 3** | ~$100M revenue | 50–100 humans per D26. Multiple parallel swarm instances per business direction (Lock-22 ICP-5). Sub-brigadiers per direction. Each direction has its own L4 stack under `swarm/wiki/directions/<slug>/`. Fission event per mgmt-expert scalability §6.1. |
| **Phase 3+** | $1T trajectory | roy-replication per D21 to external client swarms. D27 fork-and-merge architecture activates: each client fork carries their own agent definitions; best mutations return upstream to Jetix canonical. Jetix becomes the "firmware" (USB-C positioning, D20 reinforcement) — the agent layer that runs on every AI-augmented business. |

brigadier split-trigger per brigadier §1d: when intake rate exceeds
brigadier's sustainable decomposition rate (Phase B signal), a sub-
brigadier is proposed via AWAITING-APPROVAL; Ruslan acks; new brigadier
instance is instantiated per direction.

## 10. Voice-Memo References

The holding-with-agents architecture derives directly from Ruslan's
voice recordings:

- **audio_510** (2026-04-21 15:21 CET): source of D26 Team 50-100 lock —
  "Jetix будет не one person company, а команда из 50-100 человек,
  работающая как холдинг" [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26]
- **audio_514** (2026-04-21 16:40 CET): methodology for AI-agent work
  systems — "разработать методологию, систему и правила для работы с
  AI-агентами в различных сферах применения" — anchors the 5×4 matrix
  as the formalized methodology [src:reports/review_2026-04-24.md#task-448]
- **audio_521** (2026-04-22 20:23 CET): Jetix as corporation with modular
  management system — "сделать упор на настройки именно Jetix как
  корпорации — создать систему управления" and "логика взаимного
  усиления: люди помогают людям, агенты помогают агентам, агенты
  усиливают людей, люди усиливают агентов" — anchors the mutual-
  amplification design of L4 [src:reports/review_2026-04-24.md#tasks-457-459]
- **audio_529** (2026-04-24): confirmation of Smart AI direction —
  internal marker for what the agent layer represents operationally;
  noted as non-lock per D25-D28 addendum [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#smart-ai]

## 11. Open Questions

1. **Legacy-14 fate:** should the 14 legacy agents be migrated to ROY
   format (Core memory + strategies.md + 4-mode dispatch) or retired in
   Phase 2? Migration would unify the two populations; retirement would
   simplify L4. Neither path is decided. Current state: frozen in Phase A,
   decision deferred to Phase 2 onset.

2. **CLAUDE.md roster reconciliation:** CLAUDE.md lists 12 agents; actual
   count is 20. The 8 unlisted agents (6 ROY + staging-writer +
   sweep-worker) are operationally active. CLAUDE.md should be updated
   to reflect the full roster — or a separate `swarm/wiki/foundations/agents-manifest.md`
   should become the authoritative count. This is a brigadier-level update
   requiring no HITL but should be scheduled as a low-priority compound
   task.

3. **Per-human team-member onboarding-to-swarm protocol (Phase 2):**
   when the first human hire joins, what is their entry point into L4?
   Do they receive a `agents/<human-name>/system.md`? How does their
   work integrate with brigadier's dispatch? The Watkins 90-Day pattern
   (mgmt-expert §2.3, procurement-gap) governs the onboarding arc but
   the swarm-integration protocol for humans is not yet specified.
   Flagged for Phase-2 design.

## 12. Visual — Matrix + Legacy-Ring + Brigadier Center

```
                              RUSLAN (HITL)
                                   |
                            ┌──────▼──────┐
                            │  BRIGADIER  │  <-- sole canonical writer (Q2)
                            │  (Opus)     │      routing + gate + compound
                            └──┬──┬──┬───┘
                               |  |  |
           ┌───────────────────┘  |  └────────────────────┐
           |           ┌──────────┘           ┌───────────┘
           ▼           ▼                       ▼
     ┌──────────┐ ┌──────────┐          ┌──────────┐
     │engineering│ │  mgmt   │   ...    │ investor │
     │  ×critic  │ │  ×critic│          │ ×critic  │
     │ ×optimizer│ │×optimizer│         │×optimizer│
     │×integrator│ │×integrat│          │×integrat │
     │×scalabilit│ │×scalabil│          │×scalabil │
     └──────────┘ └──────────┘          └──────────┘
     [20 cells total — each writes to swarm/wiki/drafts/]

     ┌────────────────────────────────────────────────────┐
     │               LEGACY RING (14 agents)              │
     │  ┌──────────┐ ┌───────────┐ ┌──────────────────┐  │
     │  │ manager  │ │strategist │ │ knowledge-synth  │  │
     │  └──────────┘ └───────────┘ └──────────────────┘  │
     │  ┌──────────┐ ┌───────────┐ ┌──────────────────┐  │
     │  │personal- │ │system-    │ │  sales-lead      │  │
     │  │assistant │ │admin      │ │  sales-researcher│  │
     │  └──────────┘ └───────────┘ │  sales-outreach  │  │
     │  ┌──────────┐ ┌───────────┐ └──────────────────┘  │
     │  │life-coach│ │meta-agent │ ┌──────────────────┐  │
     │  └──────────┘ └───────────┘ │inbox-processor   │  │
     │  ┌──────────┐ ┌───────────┐ └──────────────────┘  │
     │  │crazy-    │ │staging-   │ ┌──────────────────┐  │
     │  │agent     │ │writer     │ │  sweep-worker    │  │
     │  └──────────┘ └───────────┘ └──────────────────┘  │
     │     [Phase A: untouchable — hub-and-spoke model]   │
     └────────────────────────────────────────────────────┘

     MEMORY STACK (per ROY expert):
     ┌─────────────────────────────┐
     │ L1 Core  (.claude/agents/)  │  <- system prompt, identity, domain
     │ L2 Strategies (agents/<>/…) │  <- accumulated DRR rules
     │ L3 Scratchpad               │  <- working memory, ephemeral
     │ L4 Niche (wiki/niches/<>/)  │  <- agent's slice of shared wiki
     │ L5 Recall (mailboxes/<>.jsonl)│ <- append-only message log
     └─────────────────────────────┘
```

---

*Synthesis confidence: high. All 20 agents read directly from
`.claude/agents/`. D26 verbatim from LOCKS-D25-D28-ADDENDUM-2026-04-24.md.
Matrix structure from shared-protocols §1–§6. Memory model from CLAUDE.md
wiki architecture + brigadier §1a. Open questions surfaced, not invented.*
