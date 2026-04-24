---
title: Systems × Scalability — Both Layers 5-Gate Horizon Projection (APEX)
type: horizon-projection
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: medium
confidence_method: expert-judgment-from-peer-integrator-drafts-and-tier1
tier: tier-1
produced_by: systems-scalability
sources:
  - path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md"
    range: "§1-§11 full — Layer-A/B holarchy, federated-holon proof, feedback loops, Janus risk table, dissents"
  - path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md"
    range: "§4 mechanics Tier-1..Tier-4; §5 UC-8 scale preview; §6 isolation model; §9 migration"
  - path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md"
    range: "§4 B.1-B.8 mechanics; §6 UC-9/UC-10 proofs; §7 pros/cons; §8 effort"
  - path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md"
    range: "§2.6 E-6 BOSC-A-T-X + MHT events; §2.7 E-7 shared protocols; §2.8 AP-table"
  - path: "raw/research/knowledge-architecture-deep-research-2026-04-19.md"
    range: "Part G §G.1-§G.5 (scale 557→5K→50K pages)"
  - path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md"
    range: "§0-§9 full — BIOS-moment, Mittelstand AI Alliance, federation scaling"
  - path: "prompts/km-architecture-research-2026-04-24.md"
    range: "§1.2 UC-8 scale; §3.8 UC-8; §6.1 cell #12 systems-scalability"
related: []
binding_scope: km-architecture-systems-scalability-apex
mode: scalability
antifragility_check: fail-at-G4-restructuring-required-then-pass-G5-antifragile
requisite_variety_budget:
  captured: "7 BOSC-A-T-X triggers × 5 gates × 2 layers = 70 system-state transitions modelled; 4 feedback loops with polarity"
  actual_estimate: "Actual system variety ~2× higher at G4/G5 (regulatory, Alliance politics, multi-founder coordination); gap flagged"
---

# Systems × Scalability — Both Layers Horizon Projection (APEX)

This document is the APEX scalability cell of the KM+PM architecture research
cycle. Its scope: project BOTH Layer-A (topic-wiki, Karpathy++ candidate) and
Layer-B (project-wiki, Rich-MiniSwarm candidate) through five horizon gates
(G1–G5), with BOSC-A-T-X trigger per gate, MHT event named, requisite-variety
check (Ashby), federation per-client scaling per gate, and Janus degraded-mode
spec. Engineering and mgmt scalability projections are bound into a coherent
system-view; apparent contradictions are resolved with explicit ordering.

---

## §1 Gate G1 (€50K, ~1K pages, 8 projects, 1-3 clients) — Layer-A + Layer-B + Federation

### §1.1 Layer-A under stress at G1

**Current configuration.** Jetix-central wiki v3: ~557 pages, ~572 typed edges,
single `edges.jsonl`, single brigadier, no active external clients.

**BOSC-A-T-X trigger at G1: C+S (Composition + Scale)**

Composition fires because G1 closes the measurement void: the evaluation harness
(OPP-01 per strategies.md) installs the first live `/lint` counters in `meta/health.md`,
transitioning Layer-A from open-loop (no feedback signal) to closed-loop (health
counters producing signal). This is a structural Composition change — a new
feedback-closure sub-system appears. Scale fires simultaneously because the ~1K
page threshold pushes BFS traversal from trivially-in-memory (~50ms at 572 edges)
toward the first measurable latency budget (Tier-2 grep: 2–5s at 1K pages).

[src: engineering-integrator §5 UC-8 "G1 all 4 retrieval tiers within budget"; systems-integrator §5.1 R1 loop "Ashby check at Phase A G1"]

**MHT event: Phase Promotion.** The wiki system moves from `spec-only` to
`operational`. The health.md counters begin producing signal. Feedback loops
R1 (ingest→retrieval→synthesis→write-back) and B1 (lint→contradiction→supersession)
complete their first full cycle. This is Phase Promotion: the system does not
change its boundary or operation; it activates a loop that was previously
structurally present but signal-less.

**Ashby requisite-variety check at G1:**

| Controller | System |
|---|---|
| Tier-3 BFS (single `edges.jsonl`, networkx in-memory) | Client wiki graph (~572 edges; G1 ceiling ~5K edges) |
| Controller variety: all traversable paths in ≤50ms (572 edges trivial) | System variety: ~572 distinct knowledge-paths |
| **Verdict: BALANCED** | At G1 the controller matches the system without any sharding |

**UC-9 isolation at G1.** Phase-A policy-level: `WIKI_ROOT_CLIENT_ID` env-var +
`granularity: client:<slug>` + `/lint` cross-holon rejection. This is F4
(policy-enforced, not by-construction). Structurally weaker than G2 target.
[src: engineering-integrator §5 UC-9; systems-integrator §4.2 Layer-1]

### §1.2 Layer-B under stress at G1

**BOSC-A-T-X trigger at G1 (Layer-B): C (Composition)**

The mgmt scaffold transition installs the first attention-budget ratchet
(`meta/health.md Δ3`), converting Layer-B from an ad-hoc project list into a
monitored project organism. This is a Composition change: a new regulation
sub-system (ratchet) appears inside the existing Layer-B structure. Scale does
not fire at G1 — 8 projects at P1-P4 with 1-3 clients is within the ≤20 active-task
ceiling without stress.

**MHT event: Phase Promotion (Layer-B).** Project-wiki moves from file-naming
convention to monitored lifecycle state machine. The `_moc.md` state machine
+ `weekly-<Www>.md` cadence + `/project-status` sweep begin producing the Monday
traffic-light. This mirrors Layer-A's Phase Promotion but at the project-operations
level.

**Ashby check at G1 (Layer-B):**

| Controller | System |
|---|---|
| Attention-budget ratchet (Δ3) + canonical brigadier | 8 active projects, ≤20 active-task ceiling |
| Controller variety: {green, amber, red} × {0..20 projects} = 63 distinguishable states | System variety: all project-state combinations at ≤8 projects = 5^8 = ~390K theoretical; but manageable at ≤20 tasks because projects are mostly independent |
| **Verdict: BALANCED** at G1 — the ≤20 cap is a designed Meadows L10 leverage point that constrains system variety to the controller's range |

[src: systems-integrator §5.4 B2 loop; mgmt-integrator §4 B.6]

### §1.3 Federation per-client at G1

At G1, federation is Phase-A policy-level only. 1-3 clients are isolated by
directory namespace (`operations/clients/<slug>/`) + `WIKI_ROOT_CLIENT_ID` +
`granularity: client:<slug>`. No separate git repos. The per-client JSONL shard
(systems-optimizer Delta-5) is declared at G1 but not yet required for BFS
performance — single-file is sufficient below 1K pages/client.

**Federation complexity at G1:** LOW. One brigadier, one repository, directory-level
isolation. Human oversight (Ruslan) spans all clients.

**G1 → G2 transition trigger (binary):** `count(simultaneous external clients) ≥ 1
AND any client KB contains business-sensitive data` → Phase-B separate-repo
model activates. This is the BY-CONSTRUCTION isolation upgrade.

---

## §2 Gate G2 (€200K, ~5K pages, 15 projects, 10 clients) — Layer-A + Layer-B + Federation

### §2.1 Layer-A under stress at G2

**BOSC-A-T-X trigger at G2: A (Agency)**

At €200K, the first external hire or strategic-partner relationship materialises
(Strategic Insight §5 Path B/C; mgmt-integrator §4 B.3 mini-swarm allocation
notes "€200K gate: Role-Lift"). Ruslan is no longer the sole operator of the
brigadier tool. Agency shifts: a second human (or delegated project-brigadier
per client) acquires operational autonomy. This is an Agency trigger — who decides
and who acts changes structurally.

Layer-A structural implication: the Jetix-methodology holon splits from the
per-client operational holons. Jetix-central `swarm/wiki/` becomes the
methodology-provider (A2 architecture); each client's tree becomes a peer-holon
(client-A, client-B). The `holon-ref` (#13 edge, systems-optimizer Delta-1)
becomes mandatory rather than optional — it is the boundary marker that makes
the multi-agent-across-multiple-repos system navigable.

[src: systems-integrator §1.2 View A2; §3.1 holon registry Phase B]

**MHT event: Role-Lift.** Ruslan lifts from sole-operator-brigadier to
methodology-coordinator. The canonical brigadier role within each client's
holon is delegated to a client-brigadier instance. Ruslan retains the 6
non-delegatable functions (per mgmt-integrator §4 B.6: Direction α-5,
roadmap commitments, hiring, public commitments, capital, quarterly review).

**Ashby check at G2 (Layer-A):**

| Controller | System |
|---|---|
| Per-client BFS over shard (Delta-5): client JSONL ~125K edges, ~50MB, networkx in-memory | Each client's knowledge graph: ~5K pages, ~125K edges |
| Controller variety: all traversable paths in client shard within 500ms | System variety: ~125K paths per client |
| **Verdict: BALANCED per client** — per-client JSONL sharding (Delta-5) is the key mechanism that keeps controller variety matched at G2. At G2 without sharding (single shared JSONL): IMBALANCED — BFS over 10 clients × 125K edges = 1.25M edges → multi-second latency, controller variety falls below system variety |

The Delta-5 sharding is therefore an Ashby-mandatory structural change at G2, not
merely a performance optimization. [src: engineering-integrator §5 UC-8 G2 "per-client JSONL stays within 50MB ceiling"]

### §2.2 Layer-B under stress at G2

**BOSC-A-T-X trigger at G2 (Layer-B): A (Agency) — same trigger as Layer-A**

At G2, separate-repo per client activates. Each client-brigadier now operates
within `client-A/swarm/wiki/operations/` — a distinct filesystem tree. The
attention-budget ratchet expands: Ruslan no longer directly counts all active
tasks across all clients; each client-brigadier runs its own `meta/health.md`
counter. The canonical-brigadier oversight surface shrinks from ALL tasks to
Jetix-internal tasks + HITL escalations from client-brigadiers.

**MHT event: Role-Lift (Layer-B parallel).** Project-brigadier delegation from
Ruslan directly to per-client brigadier-instance. This is the same Role-Lift
event as Layer-A — they co-fire at G2, which is the correct architecture:
Layer-A (topic-wiki) and Layer-B (project-wiki) both migrate from Jetix-central
to per-client simultaneously. [src: systems-integrator §7 pairing — "A2/B2 is the Phase B canonical path triggered at €200K gate"]

**Ashby check at G2 (Layer-B):**

| Controller | System |
|---|---|
| Per-client attention-budget ratchet (≤20 tasks per client) + client-brigadier | 15 projects across 10 clients = ~1.5 projects/client average |
| **Verdict: BALANCED** — each client-brigadier controls only its own project set; variety is naturally bounded per client |

### §2.3 Federation per-client at G2

At G2, federation complexity jumps to MEDIUM. Separate git repos per client.
Methodology versioned as git submodule pushed from Jetix-central.
The cross-holon R2 reinforcing loop (client-pattern → methodology-update →
cross-client benefit) activates for the first time — but only via HITL gate
(Ruslan manually promotes anonymised patterns from `local-patterns/` to
`global/`).

**Per-client operational complexity at G2:** 10 clients × (1 brigadier-instance
+ 1 methodology submodule + 1 JSONL shard + 1 holon-root manifest) = 40 active
artefacts under Ruslan's coordination. This is at the upper boundary of solo
management; the G2 Role-Lift event (first hire) is structurally required.

**Antifragility check (G1→G2 10× scale):** 10× clients (1→10), 5× pages/client
(~1K→~5K). Structural changes required: (a) separate-repo per client
(architecture-level), (b) per-client JSONL sharding (engine-level), (c)
methodology submodule (coordination-level). Estimated structural change volume:
~25% of the system's components are new or restructured. **Result: G1→G2 passes
the ≤30% threshold.** Not antifragile (system does not gain capability from the
scale stress itself), but NOT-FRAGILE.

---

## §3 Gate G3 (€1M, ~15K pages, 30 projects, 50 clients) — Layer-A + Layer-B + Federation

### §3.1 Layer-A under stress at G3

**BOSC-A-T-X trigger at G3: S+C (Scale + Composition)**

Scale fires: at 15K pages per-client average (~300 pages) and 50 clients total,
the per-client JSONL at ~200K edges/client approaches the BFS in-memory ceiling
documented in `knowledge-architecture-deep-research §G.2` (threshold ~20K edges
for Neo4j; at 200K edges, networkx in-memory is still viable but slow: 5-20s
for complex multi-hop queries). The PPR index pre-built by `/build-graph` (Delta-5
G3 path) is required.

Composition fires: Layer-A's Tier-3 retrieval must split into shard-specific BFS
(layer-sharding: `edges-L1.jsonl`..`edges-L7.jsonl` per entity-type per client).
This is a new structural layer inside the retrieval sub-system — a Composition
change. The system's components are reorganised internally without changing the
boundary.

**MHT event: Phase Promotion (Layer-A, G3).** The retrieval sub-system is
promoted from unsharded-per-client JSONL to layer-sharded + PPR-indexed graph.
This is a promoted sub-system: the capability exists before G3 (Delta-5 declares
the upgrade path), but it is instantiated as a distinct structural element at G3.

**Engineering vs mgmt contradiction (APEX resolution):**

Engineering (engineering-integrator §5 UC-8) says: G3 needs layer sharding + PPR.
Mgmt (mgmt-integrator §8 effort) says: G3 needs sub-roy split (per §6.1 cell
reference: "€1M gate: S+C triggers VSM Level-3 audit function emergence").
These are NOT contradictory — they address different VSM levels.

**Order of operations at G3:**
1. FIRST: PPR index upgrade + layer sharding (Layer-A, engineering). This is a
   necessary prerequisite: retrieval quality must be maintained as pages grow,
   or Layer-B's project-wiki `/ask` calls degrade. 
2. THEN: VSM Level-3 sub-system emergence (both layers). Once retrieval is stable
   at G3 scale, the audit/optimisation function (meta-agent operating across
   50 clients' health.md summaries) can be materialised as an explicit sub-system
   rather than an informal weekly sweep.

Engineering's G3 upgrade is infrastructure; mgmt's G3 upgrade is governance.
Both are Composition triggers; infrastructure precedes governance by 1-2 cycles.

[src: knowledge-architecture-deep-research §G.1-§G.3; systems-integrator §5.1 "kill-condition on R1 loop: if BFS precision degrades at G3 without PPR upgrade"; mgmt-integrator §4 B.3 note "model changes at €1M gate"]

**Ashby check at G3 (Layer-A):**

| Controller | System |
|---|---|
| PPR index + layer-sharded BFS per client (edges-L1..L7.jsonl) | 50 clients × ~200K edges/client |
| Controller variety: PPR retrieval covers multi-hop paths across 7 layer-shards; query latency 2-5s | System variety: ~200K edges/client; cross-layer patterns require PPR |
| **Verdict: BALANCED** after PPR upgrade. WITHOUT upgrade: IMBALANCED — BFS over unsharded 200K edges degrades to 20+ seconds, controller variety collapses below system variety. AP-SYS-10 (Ashby requisite-variety violation) fires if upgrade is deferred. |

### §3.2 Layer-B under stress at G3

**BOSC-A-T-X trigger at G3 (Layer-B): S+C — same compositional logic**

At 30 projects across 50 clients (~0.6 projects per client on average, but P1
clients may have 3-5 active projects), the client-brigadier attention-budget
ratchet (≤20 active tasks per client) approaches limits for high-engagement
clients. The VSM Level-3 audit function (meta-agent watching 50 health.md
summaries) is now structurally required as an explicit sub-system, not a
Ruslan-scheduled weekly sweep.

**MHT event: Phase Promotion (Layer-B, G3).** The audit function is promoted
from implicit (Ruslan does it manually) to explicit (a dedicated audit sub-system,
likely the meta-agent operating with its own brigadier-instance for the
Jetix-methodology coordination tier). This is the Beer VSM Level-3 emergence:
the audit/optimisation function becomes a distinct node in the system's structure.

**Ashby check at G3 (Layer-B):**

| Controller | System |
|---|---|
| Meta-agent audit sub-system watching 50 clients × health.md | 50 client-brigadier instances × project-state variety |
| Controller variety: meta-agent can receive all 50 health.md summaries in one session | System variety: 50 client-states × {green/amber/red} × {0..20 projects} |
| **Verdict: BALANCED** — meta-agent as VSM L3 explicitly models the variety of 50 clients. Without the explicit Level-3 sub-system, Ruslan's attention would be the controller — and Ruslan's variety is much lower (time-bounded). |

### §3.3 Federation per-client at G3

At G3, federation complexity is HIGH. 50 client repos. Methodology push events
become a coordination burden: updating 50 submodules on a methodology release
requires automation (a `git submodule foreach` loop or a CI/CD methodology-push
pipeline).

**Per-client operational complexity at G3:** Manageable only with the VSM Level-3
audit sub-system in place. Without it, Ruslan loses visibility into which of 50
clients has stale methodology, stale lint, or degraded retrieval.

**Antifragility check (G2→G3 5× scale):** 5× clients (10→50), 3× pages/client
(~5K→~15K). Structural changes: (a) PPR index per client (engine-level), (b)
layer sharding (engine-level), (c) VSM Level-3 audit sub-system (governance-level),
(d) methodology push automation (coordination-level). Estimated structural change
volume: ~20% of components new or restructured. **Result: G2→G3 passes ≤30%.**

---

## §4 Gate G4 ($100M, ~50K pages, 100 projects, 500 clients) — Layer-A + Layer-B + Federation

### §4.1 Layer-A under stress at G4

**BOSC-A-T-X trigger at G4: T (Time)**

At $100M scale, the dominant change is not the number of clients or pages — it
is the time horizon of planning and the time constants of the feedback loops. Per
`knowledge-architecture-deep-research §G.2`: at ~50K pages per client (if a
client at this scale has 50 active projects with rich documentation), the edge
count approaches the 20K threshold per client for Neo4j/persistent graph storage.
But more critically, the R2 reinforcing loop (client-pattern → methodology-update
→ cross-client) has been running for 3-5 years; methodology version cadence shifts
from monthly to quarterly (because methodology is now a stable, well-documented
standard with many clients depending on it — breaking changes are expensive).

This is a Time trigger: the time constants of the dominant feedback loops change.
The quarterly methodology-update ceremony (HITL-gated by Ruslan) becomes a
formal governance event, not an informal weekly sweep.

**MHT event: Context Reframe.** Planning artefacts re-anchor to multi-year horizon.
`swarm/wiki/foundations/swarm-alphas.md` at Jetix-methodology level carries
multi-year Direction artefacts (α-5 state). Client holons' `direction-hypothesis`
artefacts similarly span 12-24 month horizons. The system's temporal structure
is reframed: short-cycle operational wiki remains weekly, but strategic-direction
artefacts operate on quarterly-annual cycles.

**Ashby check at G4 (Layer-A):**

| Controller | System |
|---|---|
| Persistent graph database per client (Neo4j or LightRAG equivalent) + PPR index | 500 clients × 50K pages × ~5 edges/page = ~125M edges total system; per client ~250K edges |
| Controller variety: persistent graph DB provides multi-hop traversal at 250K edges in <2s | System variety: per-client ~250K paths |
| **Verdict: CONDITIONALLY BALANCED** — requires persistent graph upgrade from JSONL+networkx. Without this upgrade: IMBALANCED. The G4 graph upgrade is an Ashby-mandatory structural change analogous to G2's JSONL sharding. |

**Graph upgrade controversy (engineering vs systems):**

Engineering-integrator §5 UC-8 G3 preview notes "Neo4j threshold ~20K edges per
client." At G4, 250K edges per client is firmly in Neo4j territory.
Systems-integrator dissent D3 (cross-client contradiction detection) becomes
moot at G4: with persistent graph per client, the BFS boundary is enforced at
the DB-session level, not file-system level. UC-9 is even stronger at G4 than
at G2 — each client's graph is a separate DB instance (or schema-isolated
namespace in a shared DB with role-based access), not a file that could be
accidentally co-loaded.

[src: knowledge-architecture-deep-research §G.2 "Neo4j/ArangoDB: ~20,000 edges"; §G.3 "50K pages: Hybrid BM25+dense+PPR + GraphRAG communities + Neo4j"]

### §4.2 Layer-B under stress at G4

**BOSC-A-T-X trigger at G4 (Layer-B): T — same temporal-horizon shift**

At $100M, Layer-B's project-brigadier model must span 100 projects across 500
clients. Client-brigadiers are now fully autonomous (no Ruslan involvement in
day-to-day project operations). The meta-agent audit function (VSM Level-3,
promoted at G3) is now operating at VSM Level-4 (intelligence/futures): it
surfaces patterns across 500 client engagement histories to identify methodology
improvements. This requires the meta-agent to have its own dedicated
brigadier-instance and its own knowledge sub-system.

**MHT event: Context Reframe (Layer-B parallel).** The project state machine
acquires multi-year lifecycle states: `{hypothesized, active, paused, pivoted,
tombstoned}` maps cleanly to quarterly planning cycles. Project health sweeps
move from weekly to bi-weekly for strategic projects; quarterly reviews integrate
strategic direction artefacts (α-5 at client level).

**Ashby check at G4 (Layer-B):**

| Controller | System |
|---|---|
| Meta-agent at VSM Level-4 (intelligence/futures) + 500 client-brigadiers | 500 client-brigadiers × project state variety × project count |
| **Verdict: REQUIRES a sub-roi coordination layer.** A single meta-agent reading 500 health.md summaries exceeds any LLM context budget. Sub-grouping required: cluster 500 clients into ~10 regional/sector groups (Mittelstand AI Alliance structure); one coordinator per group feeds the meta-agent. |

**Mgmt's G3 sub-roy claim vs Engineering's G4 Neo4j claim — order resolution:**

Mgmt-integrator (§9 open Q) flags "sub-roy split" as a G3 event; systems-expert
APEX assessment: the sub-roy split fires at G4, not G3. Rationale: at G3 (50
clients), the VSM Level-3 meta-agent can still aggregate all 50 health.md
summaries in a single session (≤200K tokens). At G4 (500 clients), a single
session cannot hold 500 health.md summaries — the context budget collapses.
Therefore: G3 = Phase Promotion of meta-agent to explicit Level-3; G4 = Fission
of meta-agent into sub-coordinators per Alliance cluster. This is the correct
MHT sequence.

[src: Strategic Insight §3 "Mittelstand AI Alliance = EISA moment"; FPF E-6 MHT Fission event]

### §4.3 Federation per-client at G4

At G4, federation complexity is VERY HIGH. 500 client repos + Alliance-level
coordination tier. The Mittelstand AI Alliance (Strategic Insight §8 rec 3)
requires its own holon-root in the registry (systems-integrator §10 Open Q2).
This is a 3-tier federation: Jetix-methodology → Alliance-coordination →
client-holons. The Alliance methodology pool (anonymised patterns from all
members) becomes a distinct knowledge layer.

**Antifragility check (G3→G4 10× scale):** 10× clients (50→500), 3× pages/client
(~15K→~50K). Structural changes: (a) persistent graph DB per client (engine-level),
(b) sub-roy coordinator cluster per Alliance group (governance-level), (c)
Alliance holon-root + methodology pool (federation-level), (d) context-budget
management for meta-agent (architecture-level). Estimated structural change
volume: ~40% of components new or restructured. **Result: G3→G4 FAILS the ≤30%
antifragility threshold.** G3→G4 is FRAGILE to scale. This is the most dangerous
gate transition in the system's lifecycle. It requires proactive structural
preparation starting at G3 (pre-build the persistent graph DB, pre-design the
Alliance holon structure, pre-implement sub-coordinator roles before G4 load hits).

The flag is: **G3 must pre-invest in G4 structural readiness.** If this
preparation is deferred to G4 onset, the system undergoes forced restructuring
under load — the worst conditions for architecture work.

---

## §5 Gate G5 ($1T, ~200K+ pages, 500+ projects, 5000+ clients) — Layer-A + Layer-B + Federation

### §5.1 Layer-A under stress at G5

**BOSC-A-T-X trigger at G5: X+B (eXternal + Boundary)**

At $1T scale, external events dominate: EU AI Act enforcement, GDPR evolution,
BSI C5 certification as a market entry requirement for German clients, potential
regulatory bodies becoming constituents of the methodology standard (not
externalities to it). The system's boundary changes: regulators and standards
bodies are incorporated into the Jetix-methodology holon as stakeholders, not
merely as constraints. This is simultaneously X (external environment shift) and
B (boundary change).

Layer-A's `swarm/wiki/foundations/` now includes regulatory-alignment artefacts
(`eu-ai-act-compliance.md`, `bsi-c5-controls.md`) as first-class knowledge types,
not footnotes in individual client deployments.

**MHT event: Fusion.** Regulators and Alliance members partially fuse into the
Jetix-methodology governance structure. The Alliance is no longer just a
coordination layer — it becomes a standards body with formal membership, voting
rights, and shared R&D investment. This mirrors the EISA consortium becoming a
formal industry body (Strategic Insight §8 rec 3 "Mittelstand AI Alliance как
EISA-момент").

**Ashby check at G5 (Layer-A):**

| Controller | System |
|---|---|
| Distributed persistent graph per client cluster (5000 clients grouped in ~100 Alliance sub-clusters × 50 clients each) + Alliance-level GraphRAG community detection for cross-client methodology synthesis | 5000 clients × 200K pages × 5 edges/page = ~5B edges total system variety; per-cluster ~100M edges |
| **Verdict: CONDITIONALLY BALANCED** — requires GraphRAG community-detection infrastructure (knowledge-arch §G.3 "50K pages: GraphRAG communities") at the per-cluster level, plus distributed graph infrastructure. At this scale, the G2 and G3 infrastructure upgrades (per-client JSONL sharding, PPR index, persistent graph DB) are prerequisites without which G5 is structurally unreachable. |

### §5.2 Layer-B under stress at G5

**BOSC-A-T-X trigger at G5 (Layer-B): X+B — same Fusion**

Layer-B's project-wiki at G5 spans 500+ active Jetix-coordinated projects and
potentially thousands of Alliance-member-operated projects using the Jetix
methodology. The distinction between "Jetix project" and "Alliance-member project"
becomes a governance question, not an architectural one — the architecture
(federated peer-holons, A2/B2 model) handles both identically.

**MHT event: Fusion (Layer-B parallel).** Alliance-member projects adopting the
Jetix methodology standard become a new category: they are not Jetix clients
(no per-client advisory engagement) but they ARE methodology licensees. Their
project-wikis use the same `_moc.md` lifecycle, the same `holon-ref` edges, the
same `granularity: jetix-shared` promotion gates. This is Fusion at the
standards-adoption level.

### §5.3 Federation per-client at G5

At G5, federation is a FULL Alliance structure:

```
L3 Alliance-methodology pool (Jetix-methodology + Alliance contributions)
  L2 Alliance sub-clusters (100 clusters × 50 clients)
    L1 Client holons (5000 peer-holons)
```

The `holon-roots-registry.md` at G5 must support 3 tiers of holon identity.
The Alliance itself requires a holon-root manifest (systems-integrator §10 Q2).

**Antifragility at G5 (G4→G5):** If the G3→G4 pre-investment fired correctly
(persistent graph DB pre-built, Alliance structure pre-designed, sub-coordinator
roles pre-implemented), then G4→G5 is a scale-up of an already-proven structure,
not a re-architecture. Estimated structural change: ~15% (adding Alliance-tier
holon registry, GraphRAG community detection at cluster level, regulatory-alignment
artefact types). **Result: G4→G5 passes ≤30% IF G3→G4 pre-investment completed.**
G4→G5 may demonstrate TRUE antifragility: each new client joining the Alliance
adds to the methodology pool, enriching all members — the system gains capability
from the stress of more members. This is the Phoenix BIOS flywheel at
Alliance-consortium scale (Strategic Insight §8 rec 3; systems-integrator §5.2 R2 loop).

---

## §6 MHT Event Sequence Prediction G1→G5

Predicted order of named MHT events across the 5 gates:

| Gate | MHT Event | Trigger | Layer |
|---|---|---|---|
| **G1** | Phase Promotion — measurement activation | C+S: health.md counters go live; closed-loop feedback begins | Layer-A + Layer-B simultaneously |
| **G2** | Role-Lift — Ruslan→coordinator | A: first external hire; client-brigadier delegation begins | Both layers, A2/B2 architecture activates |
| **G3** | Phase Promotion — VSM Level-3 audit | S+C: meta-agent promoted to explicit audit sub-system | Both layers; engineering PPR upgrade precedes by 1-2 cycles |
| **G3.5** | (Pre-investment event — not a gate) Phase Promotion — persistent graph declared | G4 preparation: Neo4j design + Alliance holon structure pre-specified | Layer-A engineering; must fire BEFORE G4 load |
| **G4** | Context Reframe — multi-year planning horizon | T: time constants of dominant loops shift to quarterly-annual | Both layers |
| **G4** | Fission — meta-agent splits into sub-coordinators | T: context budget collapses at 500 clients; cluster-per-coordinator | Layer-B governance |
| **G5** | Fusion — regulators + Alliance enter Jetix-methodology boundary | X+B: regulatory bodies become methodology constituents | Both layers; standards-body governance |

**Commentary on the sequence.**

The G3.5 pre-investment event is the most operationally critical item in the
sequence. The G3→G4 antifragility failure (40% restructuring under load) is
avoidable only if this pre-investment is treated as a mandatory G3 deliverable,
not a G4 initiative. The systems-expert recommends flagging this as a
`AWAITING-APPROVAL` checkpoint at G3 (Ruslan acks the G4-readiness investment
before the G3 gate closes).

The Fission event at G4 resolves the engineering-mgmt apparent contradiction:
Engineering's "Neo4j upgrade" and Mgmt's "sub-roy split" are both G4 events, but
Neo4j fires on the retrieval path (Layer-A engine) while sub-roy fires on the
coordination path (Layer-B governance). They are independent; Neo4j first (it
is a prerequisite for reliable retrieval that the sub-coordinator uses).

[src: FPF E-6 MHT event catalogue; systems-integrator §6 Janus risk table; Strategic Insight §3; knowledge-architecture-deep-research §G.1-§G.3]

---

## §7 Janus Degraded-Mode Spec (S-A Excess + INT Excess, Per Gate)

### §7.1 Global Janus failure modes for this architecture

**S-A excess (self-assertive excess):** any single sub-system monopolises
decisions or writes without routing through the appropriate coordination layer.
In this architecture, the primary S-A excess risk is Jetix-methodology
brigadier over-writing into client holon spaces (bypassing the peer-holon
separation). Secondary risk: a client-brigadier accumulating patterns without
promoting any to `local-patterns/` or escalating to Ruslan (accumulation without
integration).

**INT excess (integrative excess):** the system is so tightly coupled that no
component can act autonomously. In this architecture, the primary INT excess risk
is the quarterly HITL promotion gate becoming a bottleneck: patterns accumulate
in 50+ clients' `local-patterns/` directories but Ruslan cannot review them all,
so no pattern is ever promoted and the R2 reinforcing loop stalls.

### §7.2 Per-gate Janus degraded-mode table

| Gate | S-A excess symptom | S-A counter-move | Recovery predicate (binary) |
|---|---|---|---|
| **G1** | Brigadier writes to `operations/clients/<slug>/` without `WIKI_ROOT_CLIENT_ID` check | Re-dispatch with explicit forcing clause: "assert WIKI_ROOT_CLIENT_ID before any write; if unset, return escalation" | `count(cross-client writes detected by /lint) == 0 over 2 consecutive cycles` |
| **G2** | Client-brigadier promotes local patterns directly to `swarm/wiki/global/` without HITL gate | Re-dispatch with forcing clause: "all global/ writes require `granularity: jetix-shared` + HITL ack; pattern goes to `local-patterns/` until Ruslan acks" | `count(unapproved writes to global/) == 0 over 2 consecutive cycles` |
| **G3** | Meta-agent VSM Level-3 audit writes directly to client holons without client-brigadier ack | Meta-agent is scoped to read-only access to `meta/health.md` summaries; writes only to Jetix-methodology `global/compound-rules/` with HITL; ANY write to a client holon requires client-brigadier escalation | `count(meta-agent direct writes to client holons) == 0 over 2 cycles` |
| **G4** | Sub-coordinator aggregates client data across cluster and writes cross-client synthesis without content-stripping | Sub-coordinator operates on slug-normalised summaries only (no raw client content); any cross-client synthesis requires content-stripping + HITL ack before write | `count(unanonymised cross-client content in Alliance pool) == 0 over 2 cycles` |
| **G5** | Regulatory-alignment artefacts in Jetix-methodology override client-local decisions without client ack | Regulatory updates are methodology-push-only (clients pull); no regulatory artefact can overwrite a client's existing `decisions.md` entry without client-brigadier HITL | `count(regulatory overrides without client ack) == 0 over 2 cycles` |

| Gate | INT excess symptom | INT counter-move | Recovery predicate (binary) |
|---|---|---|---|
| **G1** | All agent writes require Ruslan ack (system freezes waiting for HITL) | Distinguish autonomous vs requires-approval per §1d decision-rights ritual; brigadier acts autonomously on `proposed_writes[]` within the autonomous tier without waiting for ack on each artefact | `count(AWAITING-APPROVAL packets opened for autonomous-tier actions) == 0 over 2 cycles` |
| **G2** | Per-client HITL promotion gate stalls: 10 clients each accumulate patterns; Ruslan cannot review all 10 in a weekly session | Introduce batched-promotion: Ruslan reviews 1 client/day in a 10-minute slot; meta-agent pre-filters to top-3 eligible patterns per client | `count(patterns promoted per week) ≥ count(pattern-eligible candidates per week) × 0.5` over 2 cycles |
| **G3** | Meta-agent VSM Level-3 reports 50 health.md summaries but Ruslan cannot process them; no escalations acked | Meta-agent issues only RED-flagged escalations (not all 50 summaries); GREEN/AMBER are suppressed from Ruslan surface until sub-coordinator is in place at G4 | `Ruslan attention time on meta-agent escalations ≤ 15 min/week AND 0 RED items unresolved > 7 days` |
| **G4** | Sub-coordinator clusters stall: each cluster's coordinator waits for the other before issuing Alliance-level pattern proposals | Sub-coordinators operate independently per cluster; Alliance methodology pool is updated asynchronously; no coordinator blocks on another's input | `count(cross-cluster blocking dependencies in Alliance pool update) == 0 over 2 cycles` |
| **G5** | Alliance Fusion creates governance deadlock (100 members must vote before any methodology update) | Alliance adopts a "lazy consensus" protocol (methodology updates published, members have 14 days to object; silence = acceptance); Jetix-methodology-holon retains editorial authority on the core spec | `methodology update cycle time ≤ 45 days AND < 20% updates require active member vote` |

### §7.3 Recovery condition (global binary predicate)

```
recovery: count(consecutive_dispatches with valid_acceptance_predicate
  AND ≥1_leverage_point_with_KPI AND gate-appropriate-Janus-counter-move-implemented)
  ≥ 2
```

If this binary holds across 2 consecutive dispatches following a degraded-mode
flag, restore to full-participation mode. If it does not hold within 5 dispatches
post-flag, escalate split-trigger evaluation (per §1d split-trigger conditions).

---

## §8 Provenance + F-G-R + Ashby Per-Gate

### §8.1 F-G-R declarations per major claim

| Claim | F | ClaimScope | R |
|---|---|---|---|
| G1 Phase Promotion event (measurement activation) | F4 | holds for the Karpathy++ + Rich-MiniSwarm pairing; not valid for a non-instrumented wiki variant | medium; refuted if first health.md counters show zero signal after 3 cycles |
| G2 Role-Lift (Ruslan→coordinator) fires at €200K | F3 | holds given solo-founder Phase A model; NOT valid if Ruslan hires earlier (e.g., at €100K gate) | medium; refuted if Ruslan delegates operational brigadier before €200K |
| G3 PPR upgrade is Ashby-mandatory before VSM Level-3 | F4 | holds for the Karpathy++ retrieval architecture at >200K edges per client; not valid for a vector-DB variant | medium; refuted if BFS at 200K edges remains within 2s latency without PPR index |
| G3→G4 antifragility test FAILS (40% restructuring) | F3 | holds for the described 5-gate scaling path; NOT valid if G4 pre-investment fires at G3 | medium; refuted if proactive G4 preparation brings structural change below 30% |
| G4 sub-roy Fission fires at 500 clients (not G3 50 clients) | F4 | holds given 200K token context budget for a single meta-agent session; NOT valid if context budget is extended (1M+ context models become the default) | medium; refuted if a meta-agent operating on 500 health.md summaries fits within session budget without quality degradation |
| G5 Fusion is antifragile if G4 pre-investment completed | F3 | holds for the Alliance flywheel model; NOT valid if Alliance governance becomes adversarial | low-medium; refuted if Alliance members refuse methodology pull updates despite demonstrated quality improvement |
| G2 Ashby balance requires per-client JSONL sharding | F5 | holds for the BFS-over-JSONL retrieval architecture; F5 because the ceiling is calculable from known file-size and networkx in-memory constraints | high; refuted if a 10-client single-JSONL BFS at 1.25M edges completes in <2s on Phase-A hardware |

### §8.2 Ashby summary per gate

| Gate | Controller | System | Verdict | Key mechanism |
|---|---|---|---|---|
| G1 | BFS + single JSONL | ~572 edges | BALANCED | No sharding needed |
| G2 | BFS + per-client JSONL shard | ~125K edges/client | BALANCED (after Delta-5 sharding) | Delta-5 sharding is Ashby-mandatory |
| G3 | PPR index + layer-sharded BFS | ~200K edges/client | BALANCED (after PPR upgrade) | PPR is Ashby-mandatory; precedes VSM L3 |
| G4 | Persistent graph DB + sub-coordinators | ~250K edges/client | CONDITIONALLY BALANCED | Neo4j or equivalent; sub-coordinator fission |
| G5 | Distributed graph + GraphRAG community detection | ~250K+ edges/client | CONDITIONALLY BALANCED | Pre-requires G4 infrastructure; Alliance GraphRAG |

[src: knowledge-architecture-deep-research §G.2 "Neo4j threshold ~20K edges"; systems-integrator §5.1 Ashby check R1 loop; engineering-integrator §5 UC-8 "G2 per-client JSONL ceiling"; FPF E-6 requisite-variety principle]

### §8.3 Tier-1 source provenance (mandatory ≥3 citations)

**[Tier-1 cite 1]** `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md`
§5.1 Ashby check R1: "At Phase B (G2, ~5K pages per client, ~125K edges per
client): Per-client shard: BFS loads only client's file (~125K edges, ~50MB);
balanced within networkx ceiling." This underpins the G2 Ashby-mandatory
Delta-5 sharding claim.

**[Tier-1 cite 2]** `raw/research/knowledge-architecture-deep-research-2026-04-19.md`
§G.2: "Порог для Neo4j/ArangoDB: ~20,000 edges при регулярных multi-hop
queries. До этого `edges.jsonl` + networkx в памяти достаточен." This underpins
the G4 persistent-graph-DB upgrade claim and the G3→G4 antifragility failure
assessment.

**[Tier-1 cite 3]** `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`
§8 rec 3: "Mittelstand AI Alliance = EISA moment — positioning as sovereign
European AI consortium." This underpins the G5 Fusion event and the Alliance
holon-root requirement (systems-integrator §10 Q2).

**[Tier-1 cite 4]** `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md`
§2.6 E-6: "Scalability mode rubric adds MHT-trigger check: for each horizon,
identify which BOSC-A-T-X trigger activates at that scale and what MHT event
the swarm must undergo." Defines the per-gate structural decomposition format
used throughout §§1-6.

**[Tier-1 cite 5]** `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md`
§5 UC-8 G2/G3 ceiling preview: "G3 per-client (8K+ pages, ~200K edges):
layer-sharding fires (edges-L1.jsonl..edges-L7.jsonl) + PPR index pre-built
by /build-graph. This upgrade path is declared; implementation gated at G3 event."
Confirms the G3 layer-sharding + PPR upgrade sequence.

### §8.4 Antifragility summary per gate transition

| Transition | Structural change volume | Verdict | Key condition |
|---|---|---|---|
| G1→G2 (10× clients) | ~25% | NOT-FRAGILE (passes ≤30%) | Delta-5 sharding + separate repos are planned upgrades |
| G2→G3 (5× clients) | ~20% | NOT-FRAGILE (passes ≤30%) | PPR + Layer-sharding pre-declared |
| G3→G4 (10× clients) | ~40% | FRAGILE (fails ≤30%) | Requires G3 pre-investment in persistent graph + Alliance structure |
| G4→G5 (10× clients) | ~15% | TRUE ANTIFRAGILE (if G3→G4 pre-investment done) | Alliance flywheel adds capability from scale stress |

### §8.5 APEX binding — engineering + mgmt projections resolved

| Apparent contradiction | Resolution | Order |
|---|---|---|
| Engineering: G3 needs Neo4j. Mgmt: G3 needs sub-roy split. | Both are G3+ events; Neo4j is infrastructure (Layer-A engine), sub-roy is governance (Layer-B coordination). Independent triggers. | Neo4j upgrade at G3 cycle-1; sub-roy at G4 (context budget collapse at 500 clients, not 50) |
| Engineering: holon-ref is primary UC-9 mechanism. Mgmt: env-var is primary. | Both mechanisms are necessary (defense-in-depth); neither alone is sufficient at multi-client scale. Both are WLNK-preserved. | Phase A: env-var primary + holon-ref complementary. Phase B: filesystem-primary (separate repo) + both become secondary enforcement layers |
| Mgmt: sub-roy fires at G3 (mgmt-integrator §4 B.3 "€1M gate: model changes"). Systems-APEX: sub-roy fires at G4. | Mgmt refers to the emergence of the client-brigadier role (G2 Role-Lift already handles this). Systems-APEX defines sub-roy as meta-agent cluster split (only needed at 500 clients). The mgmt reference is to a different level of delegation. | G2: client-brigadier Role-Lift (mgmt's "model changes"). G4: meta-agent Fission into sub-coordinators (systems-APEX). These are different MHT events at different VSM levels. |

---

*End of systems × scalability APEX draft. Produced by systems-expert, mode:
scalability. Cycle: cyc-km-architecture-2026-04-24. Word count: ~3,450 words.
All 5 gates analysed, BOSC-A-T-X per gate, MHT sequence predicted, Ashby
checked per gate, Janus degraded-mode spec per gate × 2 failure modes,
antifragility per transition, engineering+mgmt contradictions resolved.
Awaiting brigadier integration and Stage-Gated HITL review.*
