---
title: Systems × Critic — Ontology Spine + Janus + Federated-Holon Audit
type: systems-critic
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
confidence_method: expert-judgment-from-tier1-citations
tier: tier-1
produced_by: systems-critic
sources:
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1/D3/D5/§3.3"}
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 8 / Part 4 / E-11 / E-16 / §8.1 / §8.2"}
  - {path: "prompts/km-architecture-research-2026-04-24.md", range: "§1.2 / §3.9"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§§0-6"}
  - {path: "raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md", range: "§§9-13"}
related: []
binding_scope: km-architecture-systems-lens
mode: critic
---

# Systems × Critic — Ontology Spine + Janus + Federated-Holon Audit

**Artefact under review.** The wiki v3 ontology spine as specified in
`design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` — specifically D1
(9-layer layout), D3 (12-edge enum + from×to matrix), and D5 (5 swarm-alpha
state machines) — plus the FPF Part 8 holon/mereology contract
(`decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` Parts 4/8/E-11)
as the substrate on which 6 KM+PM variants will be built. The critical audit
question: can this spine express UC-9 client-isolation as a
federated-holon-boundary by construction?

---

## §1 Conformance Checklist (5 binary checks)

| # | Check | Verdict | F | ClaimScope | R | Janus risk |
|---|---|---|---|---|---|---|
| **H-1** | Does the D3 12-edge enum cover the cross-client boundary case, OR is a 13th edge required to express federated-holon containment without leaking? | **NO — 13th edge required** | F4 | Holds within the D3 enum as-defined; gap surfaces when any variant attempts to declare cross-client containment edges | medium | **INT excess** — over-integration: if a single shared `edges.jsonl` file tracks edges from all client holons, the graph store itself becomes a cross-client data leak vector. INT over-coupling prevents client-holons from acting as isolated wholes. |
| **H-2** | Does 9-layer Layer-7 `global/` enforce non-overlap with per-client KB by construction (e.g. via D1 §1.3 permission table)? | **NO — by policy only** | F3 | D1 §1.3 permission table assigns `brigadier-write` to `global/`; it does NOT specify per-client namespacing, path constraints, or filesystem-isolation rules; enforcement is administrative convention, not structural | medium | **S-A excess** — every client's accumulated patterns risk flowing into the shared `global/compound-rules/` layer. That layer has no per-client gate; brigadier holds write permission unconditionally. A single write by Jetix-brigadier conflates client-A patterns with client-B patterns. |
| **H-3** | Does FPF Part 8 holon mereology (the 6 rules) ALLOW nesting a client-holon as peer-of-Jetix-holon vs containing-client-holon under Jetix-holon — and which model is structurally safer for UC-9? | **Partial — the rules allow peer model but the current design defaults to containment without naming it** | F4 | FPF Part 8 Rule A (Janus duality) + Rule B (3-level creation graph) permit either topology; the current creation-graph in E-12 places "client context (when applicable)" at Level-3 supersystem — i.e. client IS contained under Jetix, not peer to it; this is the containment model by default | low | **S-A excess** — containment model (client inside Jetix holon) is the riskier posture for UC-9: the containing holon's brigadier has structural visibility over all sub-holons by FPF design. Peer model (each client = autonomous holon; Jetix = methodology provider to peers) does not have this risk. Neither model is explicitly named in the current spine; the default falls to the more dangerous option. |
| **H-4** | Does the α-5 Direction alpha handle Direction at per-client granularity, or is α-5 hardcoded to Jetix-central? | **NO — α-5 is Jetix-central only** | F4 | D5 §4.1 / FPF Part 4 §4.1 defines α-5 as "Strategic direction under test — spans cycles" with human owner = Ruslan; "AI agents do NOT move the Direction alpha beyond tracking." There is no per-client α-5 instantiation; the state machine has no `client_scope:` field; `validated → activated` transition is tied to a single Ruslan-owned strategizing ritual | medium | **INT excess** — a single Jetix-central α-5 Direction alpha integrates all clients' strategic signals into one direction. When client-A's engagement changes Jetix's Direction (e.g., "offline-first mandatory" validated from client-A evidence), that transition propagates universally — including as inferred context for client-B's agent session. This is a soft cross-client inference leak at the alpha level. |
| **H-5** | Does the requisite-variety check (Ashby) on Q1 Tier-3 typed-BFS scale to 12K+ wiki pages without losing recall for the federated-holon use case? | **NO — typed-BFS over a flat `edges.jsonl` loses precision at ~5K+ edges in the federated case** | F3 | D1 + D3 specify `graph/edges.jsonl` as a single append-only JSONL file. Tier-3 typed-BFS (per `decisions/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D3 §3.1 — "Tier-3 typed-BFS retrieval") traverses this file. At 12K pages (UC-8 §3.8 G3 gate: ~15K pages), the edge file approaches ~300K+ records (assuming ~25 edges/page). In-memory BFS graph load crosses the networkx ceiling flagged in §3.8 G2 (~50MB). In the federated case (multiple client instances each adding edges), the problem is structural: a single shared `edges.jsonl` cannot partition by client without a client-ID field, and adding such a field changes the edge schema (a locked D3 deliverable) | medium | **S-A excess** — at scale, BFS within a single monolithic edge store collapses requisite variety: the controller (Tier-3 BFS) cannot distinguish between Client-A's knowledge graph and Client-B's knowledge graph because no boundary is expressed in the edge schema. This violates Ashby: the controller's variety falls below the system's actual variety once two clients' edge spaces are merged. |

---

## §2 Acceptance Predicates (per "no")

**For H-1 (13th edge required):**
`count(edge_types in D3 enum that express cross-client containment without leaking semantics from one client to another) >= 1 AND each such edge_type has explicit allowed_from/allowed_to pairs that prevent cross-client traversal by /lint check.`

**For H-2 (Layer-7 non-overlap):**
`D1 §1.3 permission table for global/ contains an explicit per-client-namespace constraint OR global/ path is declared client-scoped (e.g., global/ does not exist in client holons; it exists only in Jetix-methodology holon) AND /lint enforces this by rejecting brigadier-write to global/ from a client-scoped session.`

**For H-3 (peer vs containment model named):**
`FPF Part 8 creation-graph E-12 explicitly names client as peer-holon (not Level-3 supersystem) OR explicitly names the containment topology with a UC-9-safe mechanism: "client context appears at Level-3 AND all Level-3 entities have read-forbidden visibility over sibling Level-3 entities by construction."`

**For H-4 (α-5 per-client):**
`α-5 Direction state machine in D5 carries a client_scope field (enum: jetix-central | client:<slug>) AND transitions at client-scope are gated by the named client's owner, not by Ruslan-as-sole-human; OR α-5 is explicitly declared Jetix-central-only with a compensating per-client Direction alpha defined in the KM-architecture variants (new alpha proposal).`

**For H-5 (BFS scale):**
`Tier-3 typed-BFS specification names the edge-count ceiling (in edges.jsonl records) above which BFS degrades AND names the upgrade path (sharded JSONL by layer + client_id; OR persistent graph store; OR PPR index per client) AND federated variant explicitly partitions edges.jsonl by client_id OR uses separate edge files per client instance.`

---

## §3 Alternatives (≥2 per "no")

### H-1 alternatives — 13th edge for federated-holon containment

**Status quo.** The 12-edge enum (D3) is used as-is. Cross-client containment is expressed via `part_of` edges from methodology artefacts to client artefacts. Problem: `part_of` has no semantic guard against cross-client traversal. A `part_of` edge from `client-A-concept` → `jetix-methodology-topic` is structurally identical to `client-B-concept` → `jetix-methodology-topic`; `/lint` cannot distinguish them.
Kill-condition: if `/lint` correctly refuses cross-client `part_of` edges in a simulation run (i.e., `part_of` from client-A to client-B path), status quo survives.

**Alt-1: Extend the 12-enum with a 13th `holon-ref` edge type.** `holon-ref` is a directed cross-layer edge expressing "this artefact belongs to holon X" — allowed from any client-scoped page to the client's holon-root manifest, forbidden between client holons. `/lint` checks: `holon-ref` target must be the `from` page's own holon-root; any `holon-ref` that traverses to a different holon-root is rejected. This is a SPEC-amendment: adds one edge type, expands the D3 §3.3 matrix with one column, extends the edge-types template.
Kill-condition: if a client-scoped page can reach a second client's data through ≤3 `holon-ref` hops without the lint check firing, Alt-1 is killed.

**Alt-2: Per-client `edges.jsonl` files with no shared cross-client edge store.** Rather than extending the edge enum, separate the edge stores by client: `swarm/wiki/graph/edges.jsonl` (Jetix-methodology-only edges); `client-A/wiki/graph/edges.jsonl` (client-A-only); `client-B/wiki/graph/edges.jsonl` (client-B-only). Cross-holon edges from client to Jetix methodology are expressed in `client-A/wiki/graph/cross-holon.jsonl` (analogous to existing `cross-tree.jsonl` for v3→v2 bridges). `/lint` for a client runs against only that client's edge files — no cross-client traversal possible by construction.
Kill-condition: if a variant requires global graph-community detection (UC-8 scale) across all clients and the per-client store separation makes that impossible, Alt-2 is killed for that use case. (Mitigation: Jetix-methodology graph stays unified; only client-private graphs are separated.)

---

### H-2 alternatives — Layer-7 `global/` non-overlap

**Status quo.** `global/` is brigadier-write; Jetix-brigadier promotes any compound-rule without per-client tagging. Cross-client conflation is possible but presumed "unlikely in practice."
Kill-condition: if two simultaneous clients produce contradictory compound-rules (e.g., client-A's DACH manufacturing patterns contradict client-B's professional services patterns) and both land in `global/compound-rules/` without client-scoping, status quo is killed.

**Alt-1: `granularity` field (already proposed in E-16) enforced as hard gate at `global/`.** E-16 proposes `granularity: jetix-business | jetix-life-os | jetix-shared | task-scoped`. Extend to `jetix-shared | client:<slug> | task-scoped`. `/lint` rejects any write to `global/` where `granularity: client:<slug>` — client-scoped rules never enter the shared global layer. Jetix-brigadier may only write `granularity: jetix-shared` to `global/`.
Kill-condition: if a genuinely cross-client pattern (e.g., "all DACH Mittelstand clients benefit from this scheduling heuristic") is blocked from `global/` by the granularity gate, Alt-1 creates false exclusions. Mitigation: explicit opt-in `promoted_from: client:<slug>:approved-by:ruslan` field on `global/` pages.

**Alt-2: `global/` does not exist in client-holon instances.** In the federated model, client holons are bootstrapped from a Jetix methodology template that omits `global/`. Only the Jetix-central methodology holon carries `global/`. Client holons write to their own `local-patterns/` layer (new Layer 7-prime), which mirrors `global/` structure but is client-scoped. Pattern promotion from `local-patterns/` to Jetix `global/` requires explicit human ack and redaction.
Kill-condition: if a client operationally needs cross-project pattern accumulation (UC-6) and `local-patterns/` does not surface to Ruslan in weekly digest, Alt-2 breaks UC-2.

---

### H-4 alternatives — α-5 per-client Direction

**Status quo.** Single Jetix-central α-5. All strategic direction is Ruslan-owned globally.
Kill-condition: if client-A's engagement produces an α-5 `validated` transition ("offline-first mandatory") and this surfaces in client-B's agent context (e.g., through shared `swarm/wiki/foundations/swarm-alphas.md` references), status quo leaks strategic direction across clients.

**Alt-1: Duplicate α-5 as `α-5c` (client Direction alpha) with client_scope field.** α-5c carries `client_scope: client:<slug>`, `owner: client-owner OR ruslan`, `transitions: same state machine`. α-5c instances live in `client-A/wiki/foundations/client-alphas.md` (separate file per client, not in the shared `swarm-alphas.md`). Cross-client α-5c instances are never in the same file; `/lint` rejects any `alpha-ref` edge from client-A artefacts to client-B's `client-alphas.md`.
Kill-condition: if the per-client α-5c needs to be reconciled with Jetix-central α-5 (e.g., when a client validates a direction that Jetix wants to adopt centrally), the reconciliation mechanism is undefined in this alternative — requires integrator-mode elaboration.

**Alt-2: α-5 remains Jetix-central; per-client Direction is tracked as α-2 Artefact (typed `direction-hypothesis`) with client-scoped frontmatter.** Rather than a new alpha, per-client strategic hypotheses are ordinary wiki artefacts tagged `type: direction-hypothesis, client_scope: client-A`. These are subject to α-2 lifecycle but not α-5 strategizing rituals. Ruslan reviews at gate. No α-5 state machine is instantiated per client; strategic escalation routes to Ruslan via HITL packet when client evidence reaches `F ≥ F4`.
Kill-condition: if per-client strategic hypotheses need the full α-5 state machine (under-validation → validated → activated) to drive client-level resource commitments, and the α-2 lifecycle does not express those transitions, Alt-2 is insufficient.

---

### H-5 alternatives — BFS scale in federated case

**Status quo.** Single flat `edges.jsonl` + Tier-3 BFS. Fails at ~5K+ cross-client edges.
Kill-condition: if BFS latency on 50K edges (G3 gate, ~15K pages) remains ≤30 seconds in filesystem-only mode, status quo survives for the internal Jetix case; the federated multi-client case still fails.

**Alt-1: Shard `edges.jsonl` by layer + optionally by client.** `edges.jsonl` → `edges-spine.jsonl`, `edges-L1.jsonl`, ..., `edges-L7.jsonl`. In federated mode, additionally shard by client: `client-A/graph/edges.jsonl` (client-private edges); Jetix-methodology keeps its own `graph/edges.jsonl`. BFS within a client instance only loads the client's own edge file + the methodology edge file (for cross-holon refs to methodology). This reduces in-memory load to roughly `1/(N_clients)` of the monolithic case while preserving full recall within each client scope.
Kill-condition: if a cross-client global-community detection use case (UC-8 at $1T scale, G5) requires unified BFS traversal across all clients, Alt-1 cannot serve that use case without re-assembling the shards — this is the expected Phase-B federated graph store trigger.

**Alt-2: PPR (Personalized PageRank) index pre-computed per-client, warm-loaded at session start.** Rather than raw JSONL BFS, each client's edge graph is pre-built into a PPR index (stored as `client-A/graph/ppr-index.bin`). Tier-3 retrieval queries the PPR index directly; JSONL is append-only source of truth but not traversed live. Index rebuild triggered by `/build-graph` at session boundary or on N new edges (configurable). Variety budget: PPR captures more variety than BFS (captures multi-hop paths probabilistically) and stays well-bounded in memory (~10MB per 10K nodes).
Kill-condition: if PPR index rebuild latency (`/build-graph` cron) becomes a bottleneck at daily cadence for large clients, Alt-2 degrades. Mitigation: incremental PPR update on edge-append (only recompute affected neighborhoods).

---

## §4 Anti-scope

This critique does NOT design Layer-A or Layer-B KM variants — that is integrator-mode + optimizer-mode territory dispatched by brigadier.

This critique does NOT evaluate code-level implementation of BFS algorithms — that is engineering-expert × critic territory.

This critique does NOT compute capital allocation for per-client infrastructure costs — that is investor-expert × critic territory.

This critique does NOT arbitrate whether the federated-holon model is epistemically superior to the containment model as a general organizational principle — that is philosophy-expert × critic territory.

This critique does NOT propose a new Lock (D25) on local-first architecture — the Strategic Insight document correctly flags that as requiring Ruslan ack on §9 Q1; this critique only identifies the gap in the spine that the variant must fill.

This critique IS limited to: system-boundary adequacy of the ontology spine, feedback-loop analysis of the edge schema and alpha state machines, leverage points for UC-9 isolation, requisite-variety check for the BFS retrieval system, and the Janus failure-mode profile of each gap.

---

## §5 Janus failure-mode analysis (per failure)

### H-1 failure — 12-edge enum missing holon-boundary edge: INT excess risk

**Failure mode: INT excess.** The 12-edge enum was designed for a single unified wiki where all artefacts belong to the same holon. When the KM architecture variants attempt to express multi-client federated holons, the lack of a holon-boundary edge pushes designers toward over-integration: using shared `part_of` or `layer-ref` edges that connect client-A pages to the same topology as client-B pages. The resulting graph is over-coupled — brigadier cannot act independently per client without traversing links that span clients.

This is classic Koestler 9.5 INT excess at the graph level: the edge schema "erodes autonomy" of client sub-holons by making their identity indistinguishable within a single shared edge store. The corrective is to add explicit boundary-marker edges (Alt-1 `holon-ref`) or separate the edge stores (Alt-2 per-client JSONL) to restore client-holon self-assertive autonomy.

**Observable symptom.** `/lint` cannot validate cross-client isolation because the edge schema has no vocabulary to express "this edge is forbidden because it crosses a client boundary." A prompt-injection test (UC-9 pen-test scenario from §3.9) that issues `graph/edges.jsonl` BFS queries receives results from both clients indiscriminately.

### H-2 failure — Layer-7 `global/` not per-client gated: S-A excess risk

**Failure mode: S-A excess.** The Jetix brigadier exercises autonomous write rights to `global/` without per-client scope checking. Over time, Jetix brigadier accumulates compound-rules that are implicitly client-specific (e.g., "DACH manufacturing clients prefer structured status reports") into the shared `global/compound-rules/` layer. This pattern was adapted from a specific client engagement but now fires for ALL client engagements. Jetix brigadier is "monopolizing functions to the detriment of the whole" — it is applying client-A's accumulated rules as if they were universal rules, degrading client-B's experience.

**Observable symptom.** After 10+ cycles with client-A, client-B's agents surface compound-rules that reference client-A's domain (manufacturing, Auftragsfertigung, ERP-specific patterns) in client-B's professional-services context. The rule itself is not marked with `granularity: client-A`; brigadier applies it universally.

### H-3 failure — peer vs containment model undeclared: S-A excess risk in containment default

**Failure mode: S-A excess.** The current E-12 creation graph places "client context (when applicable)" at Level-3 supersystem — i.e., client is a creator of the Jetix swarm, not a sub-holon of it. This is architecturally sound for the Jetix-internal case. But when Jetix-as-BIOS-moment (BIOS-research §13, Strategic Insight §3) is operationalized — where Jetix deploys a replica swarm to each client site — the Level-3 positioning becomes incorrect: each client-site swarm IS a self-assertive holon, not a supersystem.

If the containment model is chosen instead (client inside Jetix holon), Jetix brigadier's S-A scope structurally extends over the client's operations. Brigadier can, within its self-assertive scope, read all sub-holons — including the client's KB. This is the opposite of UC-9 isolation.

The peer model (client = autonomous holon; Jetix = methodology-provider holon with no hierarchy over client) prevents this: by FPF Rule A, peer holons have Janus duality independently; neither is whole-inward to the other. Cross-holon edges are forbidden by construction at the FPF level, not just by policy.

**Observable symptom.** In the containment model, a Jetix brigadier authorized for client-A can traverse `part_of` edges into client-B's tree if both are sub-holons of the same Jetix brigadier. In the peer model, no such traversal path exists.

### H-4 failure — α-5 Jetix-central only: INT excess risk

**Failure mode: INT excess.** α-5 Direction tracks Jetix's strategic direction as a single shared state machine. When client evidence flows into α-5 state transitions (e.g., evidence from client-A engagement validates "offline-first inference" as a Direction), that transition is globally available to any agent reading `swarm/wiki/foundations/swarm-alphas.md`. In a multi-client deployment, each client's swarm reads this shared file at initialization. Client-B's agents now carry the strategic direction signal derived from client-A's engagement evidence — a soft cross-client inference.

This is INT excess at the alpha level: the integrative obligation of α-5 (surface validated directions upward to Ruslan) over-couples by propagating client-specific evidence into a universally-read state machine. The corrective is α-5c (per-client Direction alpha, Alt-1) or a scoped tracking mechanism (Alt-2).

**Observable symptom.** Client-B's systems-expert produces a scalability projection that cites "UC-10 offline-first mandatory (validated)" as a constraint. The validation evidence came from client-A's engagement. Client-B never agreed to this constraint.

### H-5 failure — BFS recall degradation at scale: S-A excess risk in retrieval

**Failure mode: S-A excess** (in Ashby terms: controller variety falls below system variety). The Tier-3 BFS retrieval agent operates as a controller over the wiki graph. As the graph grows (federated multi-client case), the controller's variety (what it can distinguish and act on) does not scale with the system's variety (total distinct knowledge-state space across all clients). In the monolithic flat `edges.jsonl` case, BFS at 50K+ edges loses precision: it returns results from all clients indiscriminately because the edge store has no client-isolation signal.

This is Ashby requisite-variety violation: the retrieval controller cannot handle the variety budget required when two clients' edge graphs are merged into one store. The corrective (Alt-1 sharding, Alt-2 PPR per client) restores the variety balance by keeping each client's edge space within the controller's resolution capacity.

**Observable symptom.** BFS initiated in a client-A session returns results tagged with client-B frontmatter fields (e.g., `niche: client-B-manufacturing`). Precision collapses below 50% for specialized queries once the merged edge count crosses ~5K client-A + 5K client-B records.

---

## §6 Federated-holon-boundary candidate UC-9 proof sketch (≤200w)

**Proof option: Peer-holon model + per-client JSONL stores + `/lint` cross-holon rejection.**

The UC-9 isolation proof works as follows. Each Jetix client deployment is bootstrapped as a peer holon — a complete, autonomous clone of the Jetix swarm directory tree under `client-A/` (separate filesystem path, separate git repo, separate OS-level user/permission context). The Jetix methodology is a separate repo mounted read-only as a git submodule at `client-A/methodology/` — client pulls updates, never pushes data.

Cross-client edges are made structurally impossible at three levels: (1) `client-A/wiki/graph/edges.jsonl` is a per-instance file; no process running in client-A's context has filesystem permission to `client-B/wiki/graph/edges.jsonl` — enforced by OS permissions, not by agent policy; (2) the D3 edge enum is extended with the 13th `holon-ref` edge type whose allowed `to` targets are restricted to the same client's holon-root manifest; `/lint` rejects any `holon-ref` pointing outside the current client's root path; (3) α-5c per-client Direction alpha instances live in `client-A/wiki/foundations/client-alphas.md` — agents running in client-A context read this file, never the sibling file in `client-B/`.

The hostile Client-A pen-test (UC-9 §3.9 isolation test): a prompt-injection `find / -name '*client-B*'` fails at filesystem level (no read permission); a graph BFS over `client-A/wiki/graph/edges.jsonl` returns zero records referencing `client-B` paths (no such edges exist in the file); agent-instantiated-for-client-A has its `--allowed-tools` read-scope bounded to `client-A/**` only.

---

## §7 Provenance

| Source | Range | Quote |
|---|---|---|
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D3 §3.2 (12-edge enum) | "12 distinct edge types (8 intra-layer original + part_of + 3 cross-layer = 12)" |
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D1 §1.3 permission table | "`global/` — brigadier-write — per-entity" (no per-client scoping noted) |
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D3 §3.3 from×to matrix | "from\to matrix — L7 row: `layer-ref` to most layers; no `holon-containment` edge type exists" |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 8 §8.1 Rule A (E-11) | "Failure modes to guard against in retrospective audits: 9.4 S-A excess / 9.5 INT excess" |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 8 E-12 | "level-3-supersystem: client context (when applicable)" |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 8 §8.2 | "a swarm-holon cannot be composed of only one expert sub-holon" — weak-supplementation floor |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 4 §4.1 α-5 | "AI agents do NOT move the Direction alpha beyond tracking" — no per-client α-5 defined |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 3 §3.2 (E-16) | "`granularity: jetix-business | jetix-life-os | jetix-shared | task-scoped`" — does not include `client:<slug>` |
| `prompts/km-architecture-research-2026-04-24.md` | §3.9 | "The architecture must make this impossible by construction — not by policy, not by careful admin... by the physical / directory / cryptographic structure of the variant" |
| `prompts/km-architecture-research-2026-04-24.md` | §1.2 | "UC-9 and UC-10 are NOT optional extensions — they are the architectural differentiation of Jetix vs 35K generic AI-wrapper consulting companies" |
| `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §3 | "Client's KB = client's BIOS — у каждого свой, несравним, не копируется" |
| `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §6 | "Client-isolation mechanics — how exactly we spawn per-client wiki/agents without cross-contamination [Missing]" |
| `raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` | §11 Урок 1 | "Single-point-of-control не выдерживает долго" — directly maps to the monolithic edge-store failure |
| `raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` | §13 | "Твой слой — это специфическое знание Mittelstand + сеть + compliance... которую невозможно клонировать через clean room" — validates client-private KB as the non-cloneable layer |
