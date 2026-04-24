---
title: Systems × Optimizer — Minimal Ontological-Spine Extensions
type: systems-optimizer
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
confidence_method: expert-judgment-from-critic-draft-and-tier1
tier: tier-1
produced_by: systems-optimizer
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md", range: "§1-§6"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1 §1.2-§1.3, D3 §3.2-§3.5, D5 §4.1-§4.2"}
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 4 §4.1, Part 8 §8.1-§8.2, E-11, E-12, E-16"}
  - {path: "prompts/km-architecture-research-2026-04-24.md", range: "§3.9, §6.4, §7.2"}
related: []
binding_scope: km-architecture-systems-optimizer-deltas
mode: optimizer
invariants:
  WLNK: preserved
  MONO: preserved
  IDEM: preserved
  COMM: preserved
  LOC: preserved
---

# Systems × Optimizer — Minimal Ontological-Spine Extensions

**Default posture: ZERO extensions.** Per optimizer-mode §4 rubric, the
locked spine (D1 9-layer, D3 12-edge enum, D5 5-alphas) is extended ONLY
where the critic's conformance failures are demonstrably impossible to close
without touching the spine. Each delta below carries an invariant pre-check,
a before/after snapshot, a named feedback loop, an Ashby requisite-variety
check, and a Janus risk flag. Method-changes are refused and escalated.

---

## §1 Invariant pre-check (before any delta)

Per FPF E-4 / systems-expert §4.1 — five Gamma-operator invariants evaluated
before each delta ships.

| Invariant | Applies? | Preserved across all proposed deltas? | Notes |
|---|---|---|---|
| WLNK (causal-link preservation) | yes | yes | No existing causal link between sub-systems in D3 is severed. `holon-ref` (Delta-1) adds a new link type; it does not remove any existing one. `granularity: client:<slug>` (Delta-extras) adds a frontmatter value; it touches no existing edge semantics. |
| MONO (leverage-point ordering preserved) | yes | yes | Meadows ladder ordering of proposed deltas: Delta-1 sits at L9 (information flows — adding a missing channel without changing any existing flow); Delta-2 sits at L8 (rules — naming the peer model makes an implicit rule explicit); Delta-5 sits at L9 (sharding mechanism changes information routing without inverting the leverage order). No delta proposes an intervention that re-ranks existing leverage points. |
| IDEM (re-apply yields same result) | yes | yes | Each delta is a pure extension (new enum value, new field value, new sentence). Re-applying the delta to a spine that already contains it leaves the spine unchanged. `holon-ref` applied twice to an already-extended enum = no-op by enum-dedup rule in `edge-types.md`. |
| COMM (order-independence) | yes | yes | Delta-1 and Delta-5 touch different substrates (edge enum vs edge-store sharding directive); their application order does not affect the outcome. Delta-extras (E-16 extension) touches frontmatter schema only; commutes with Deltas 1, 2, 5. |
| LOC (locality — delta confined to declared boundary) | yes | yes | Each delta is confined to its named spine component: D3 `edge-types.md` for Delta-1; D1 `§1.3` permission table sentence for Delta-2; D3 retrieval-scale guidance for Delta-5; D2 frontmatter enum for Delta-extras. No delta touches the other two locked components (D5 alphas untouched; D1 layer tree untouched for Deltas 1/2/extras/5). |

All five invariants preserved across all proposed deltas. Proceed.

---

## §2 Delta proposals

### Delta-1 — Close H-1: 13th edge `holon-ref` added to D3 enum

**Critic finding (H-1).** The D3 12-edge enum has no edge type that expresses
cross-holon containment without leaking cross-client semantics. The closest
candidate — `part_of` — has no semantic guard against cross-client traversal.
`/lint` cannot distinguish a `part_of` edge from client-A's concept to a
Jetix-methodology topic from a `part_of` edge from client-B's concept to the
same topic. The union graph becomes unpartitionable by client identity.
[src: systems-critic-ontology-audit §1 H-1, critic §3 H-1 alt-1]

**Why a 13th edge rather than reusing existing enum?**

All 12 existing edge types lack the holon-boundary semantic needed for UC-9.
Specifically:

- `part_of` (intra-layer #9): mereological; no cross-holon guard; `/lint`
  rule only checks target is `topics/<slug>-hub.md` or `foundations/` — no
  client-ID constraint.
  [src: ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D3 §3.2.9]
- `layer-ref` (cross-layer #2): generic cross-layer; `from.layer != to.layer`
  constraint only; no cross-holon constraint.
  [src: ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D3 §3.2.11]
- `alpha-ref` (cross-layer #1): wiki entity → alpha tracker; directionality
  and allowed-from/to are specific to alpha tracking, not holon-root pointing.
  [src: ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D3 §3.2.10]

No reuse path avoids the gap. Delta-1 is the minimal extension: one new edge
type with tightly constrained `/lint` rule.

**Proposed delta (minimal wording for `edge-types.md` extension):**

```
## 3.2.13 `holon-ref` (cross-layer #4 — federated-holon boundary)

- Definition. A directed edge from a client-scoped wiki page to that
  client's holon-root manifest file. Expresses "this artefact belongs to
  holon X" without traversing into any other holon's tree.
- Cardinality. N:1 (many artefacts per client → one holon-root).
- Directionality. Directed (client-artefact → client-holon-root manifest).
- Inverse. `has_member` (derivative; not stored in edges.jsonl; computed
  by /build-graph within the client's own edge store only).
- Allowed `from`. Any page in the client's wiki tree (path prefix
  `client-<slug>/wiki/` OR, for Jetix-internal, `swarm/wiki/` — any page
  whose holon root is declared in the holon-root manifest).
- Allowed `to`. The client's holon-root manifest file only (e.g.,
  `client-<slug>/wiki/foundations/holon-root.md`). Cross-holon-root targets
  are forbidden.
- Cross-layer flag. Yes — crosses the layer boundary between the client's
  artefact layer and the foundations layer.
- /lint rule. REJECT any `holon-ref` record where `to` path is NOT the
  `from` page's own holon-root (determined by longest-path-prefix match
  against the registered holon-roots manifest at `swarm/wiki/foundations/
  holon-roots-registry.md`). REJECT any `holon-ref` where `to` resolves to
  a different client's holon-root. Emit WARN if an artefact in a client tree
  has no `holon-ref` outgoing (orphaned artefact — does not declare holon
  membership).
- Example. {"from":"client-A/wiki/concepts/erp-pattern","to":"client-A/wiki/
  foundations/holon-root","type":"holon-ref","ts":"2026-04-24","confidence":"high"}
```

**Supporting file: `swarm/wiki/foundations/holon-roots-registry.md`** (new
spine file, brigadier-write, singleton). Lists all registered holon roots
(one row per client deployment + Jetix-central). `/lint` reads this file to
validate `holon-ref` targets. Bootstrap state: contains one row
(`jetix-central: swarm/wiki/foundations/holon-root.md`).

**Before/after snapshot:**

| Metric | Baseline | Proposed | Delta | Method |
|---|---|---|---|---|
| Edge types in D3 enum | 12 | 13 | +1 | Add `holon-ref` with constrained lint rule |
| Cross-client leakage paths via edge traversal | unguarded (lint has no cross-client rule) | 0 (lint rejects cross-holon-root `holon-ref` targets by construction) | -∞ (structural elimination) | `holon-ref` lint rule + holon-roots-registry |
| Existing edge semantics changed | — | 0 | 0 | All 12 existing edge types unchanged |
| from×to matrix rows affected | — | 1 new row added (holon-root column) | +1 row | Delta confined to D3 §3.3 extension |

**Refusal check.** Does this delta change a Method (capital M)? No. The
retrieval method (Tier-3 typed-BFS) is unchanged; the BFS now has one
additional edge type it can traverse but is not required to. The edge-store
format (JSONL) is unchanged. The lint enforcement mechanism (path-prefix
comparison) is an execution parameter within the existing `/lint` method, not
a method change. Delta-1 ships.

---

### Delta-2 — Close H-3: peer-holon model named in D1 §1.3 permission table

**Critic finding (H-3).** FPF Part 8 permits both peer-holon and containment
topologies, but the current spine defaults to the containment model (client
appears at Level-3 supersystem in E-12). For UC-9, the containment model is
structurally dangerous: brigadier's self-assertive scope extends over all
sub-holons, including client sub-holons. The peer model is safer: each client
is an autonomous holon, Jetix is a methodology-provider with no hierarchy
over the client's data.
[src: systems-critic-ontology-audit §1 H-3, §5 H-3 Janus analysis, §6 proof sketch]
[src: FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md Part 8 §8.1 Rule A (E-11), E-12]

**Why a single sentence in D1 §1.3 rather than a fuller revision?**

The peer-model preference is a naming clarification, not a structural change
to the permission table. The 9-layer layout is unchanged; no directory moves.
The clarification makes the implicit safe default explicit, which is what
the optimizer owes to the KM-architecture cycle designers who will act on the
spine. This is the minimum intervention that satisfies the acceptance predicate
for H-3.

**Proposed delta (one sentence appended to D1 §1.3 permission table footnote):**

> **Holon topology (UC-9 positioning).** In the federated multi-client
> deployment model, each client deployment is a **peer holon** — an
> autonomous swarm instance with its own `swarm/wiki/` tree, its own
> brigadier process, and its own `foundations/holon-root.md` manifest.
> Jetix-central is a **methodology-provider holon**, not a parent-holon.
> The containment model (client as sub-holon of Jetix brigadier) is
> explicitly disallowed for UC-9 deployments; `/lint` in a client instance
> MUST reject any `holon-ref` edge pointing to a Jetix-central holon-root
> as its `to` target (cross-holon-root crossing). This topology is governed
> by FPF Part 8 Rule A (Janus duality per holon): each client holon has
> independent self-assertive scope; Jetix brigadier has no structural read
> access to any client holon's wiki tree.

**Before/after snapshot:**

| Metric | Baseline | Proposed | Delta | Method |
|---|---|---|---|---|
| Holon topology named in D1 | not named (defaults implicitly to containment via E-12 Level-3 placement) | explicitly named as peer-holon for federated deployments | named vs unnamed | one-sentence addition to D1 §1.3 footnote |
| UC-9 isolation leakage via brigadier | unguarded at topology level (containment allows brigadier cross-client read) | structurally prevented (peer model: Jetix brigadier has no structural path to client's tree) | -1 leakage path (topology-level) | naming the correct topology + holon-root lint rule from Delta-1 |
| FPF Part 8 compliance | Rule A (Janus) not applied to federated topology | applied: each peer holon is whole-inward (client) + part-outward (uses Jetix methodology) | compliant | per FPF E-11 Janus duality |

**Refusal check.** Does this delta change the Method? No. The permission
table's write-authority logic is unchanged. The layer topology (9 layers)
is unchanged. The sentence names which FPF-permitted topology applies to
the federated case; this is an execution parameter (which topology to
instantiate) within the existing FPF Part 8 method, not a method-change.
Delta-2 ships.

---

### Delta-5 — Close H-5: BFS scale directive for per-client edge-store sharding

**Critic finding (H-5).** The current spec defines a single monolithic
`swarm/wiki/graph/edges.jsonl`. At 12K+ pages across multiple federated
clients, this file approaches 300K+ records. In-memory BFS graph load
crosses the ~50MB networkx ceiling (UC-8 G2 gate at ~5K edges). In the
federated case, a single shared edge store cannot partition by client
without a client-ID field — adding such a field would change the D3
record schema (a locked deliverable).
[src: systems-critic-ontology-audit §1 H-5, §3 H-5 alt-1, §5 H-5 Janus analysis]
[src: ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D3 §3.2, UC-8 G2 gate]

**Why a sharding directive rather than a client-ID field?**

Adding a `client_id` field to the edge schema changes the D3 record shape
(a locked deliverable per the brief). That is a method-change on the edge
storage format — refused per §5 below. The alternative (Alt-1 from the
critic: per-client edge-store files) avoids touching the record schema:
each client's JSONL file contains only that client's edges, using the same
12 (now 13 with Delta-1) edge types and identical record shape. The Jetix-
methodology JSONL stores methodology-level edges. BFS within a client session
loads only the client's file + the methodology file — reducing in-memory load
by approximately 1/N_clients while preserving full recall within scope.

**Proposed delta (add one sub-section to D3 §3.1 Storage specification):**

> **3.1.3 Federated deployment — per-client edge-store sharding.** In
> federated multi-client deployments, each client instance maintains its
> own `client-<slug>/wiki/graph/edges.jsonl` file (same record shape as
> the Jetix-central `swarm/wiki/graph/edges.jsonl`; same 13-type enum).
> Jetix-central maintains `swarm/wiki/graph/edges.jsonl` for methodology-
> level edges only (templates, foundations, shared patterns). Cross-holon
> edges from a client page to a Jetix methodology page use `holon-ref`
> (Delta-1) and are stored in the **client's** edge file, not in Jetix-
> central's file — this preserves the "methodology push, data no pull"
> invariant (UC-9 §3.9). Jetix-central's edge file MUST NOT contain any
> edge whose `from` or `to` path resolves to a client's wiki tree.
>
> **Ceiling and upgrade path:** single-client edge file at ~5K pages yields
> ~125K records (25 edges/page estimate). In-memory BFS at 125K records
> remains within the ~50MB networkx ceiling for sessions lasting ≤30 minutes.
> When a single client's edge file approaches 200K records (UC-8 G3 gate,
> ~8K+ pages for that client), the upgrade path fires: shard by layer within
> the client's edge store (`edges-L1.jsonl` through `edges-L7.jsonl`), and
> pre-compute a PPR (Personalized PageRank) index per client for Tier-3
> retrieval. This upgrade path is declared here; implementation is gated by
> the UC-8 G3 event (not Phase A).

**Before/after snapshot:**

| Metric | Baseline | Proposed | Delta | Method |
|---|---|---|---|---|
| Edge-store architecture | single monolithic `swarm/wiki/graph/edges.jsonl` | per-client JSONL files + Jetix-central methodology JSONL | federated shards | per-client JSONL (Alt-1 from critic); no record schema change |
| In-memory BFS load at 12K pages (federated, 2 clients) | ~300K records (both clients merged) | ~150K records per client (client loads only own shard + methodology) | -50% per-client load | per-client edge-store separation |
| Controller variety vs system variety (Ashby) | controller (BFS) cannot distinguish client-A from client-B edges | controller loads only client-scoped shard; variety matches client's knowledge graph | balanced | shard boundary = client-holon boundary |
| Record schema (D3 locked format) | unchanged | unchanged | 0 | record shape identical; only storage file changes |

**Refusal check.** Does this delta change the Method? No. The BFS traversal
method is unchanged (same typed-BFS over JSONL). The record schema is
unchanged. The sharding directive is an operational parameter (which file to
load) within the existing `/build-graph` and Tier-3 BFS method, not a method
replacement. Delta-5 ships.

---

### Delta-extras — Close granularity gap: `client:<slug>` added to E-16 enum

**Critic finding (H-2 partial).** FPF E-16 proposes:

```yaml
granularity: jetix-business | jetix-life-os | jetix-shared | task-scoped
```

[src: FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md Part 8 §8.1 Rule F (E-16)]

This enum has no value for per-client artefacts. Without it, `/lint` cannot
gate `global/` writes by client scope: a compound-rule derived from client-A's
engagement can enter `global/compound-rules/` without being tagged as
client-A-specific. This is the S-A excess leak at the Layer-7 level identified
in H-2.
[src: systems-critic-ontology-audit §1 H-2, §5 H-2 Janus analysis]

**Proposed delta (extend E-16 enum with one new value):**

```yaml
granularity: jetix-business | jetix-life-os | jetix-shared | task-scoped | client:<slug>
```

Where `client:<slug>` is a parametric value with `<slug>` being the client's
kebab-slug identifier (e.g., `client:acme-dach`, `client:beta-ps`). The slug
matches the same `client-<slug>` convention used in the per-client filesystem
paths.

**Operative /lint rule addition:**

> `/lint` REJECTS any write to `swarm/wiki/global/` where the page's
> `granularity` field is `client:<slug>` — client-scoped artefacts are
> forbidden in the shared global layer by construction, not by policy.
> Pages with `granularity: client:<slug>` may only reside in the client's
> own wiki tree under `client-<slug>/wiki/`. Pattern promotion from a
> client's tree to Jetix-central `global/` requires: (a) explicit field
> change to `granularity: jetix-shared`, (b) Ruslan ack (HITL packet), (c)
> redaction audit. This enforces the "methodology push, data no pull"
> invariant at the artefact frontmatter level.

**Before/after snapshot:**

| Metric | Baseline | Proposed | Delta | Method |
|---|---|---|---|---|
| `granularity` enum values | 4 values; no client scope | 5 values; `client:<slug>` added | +1 parametric value | E-16 enum extension; no change to other fields |
| `global/` write protection for client-specific patterns | by policy only (brigadier expected to tag correctly) | by construction (`/lint` rejects `client:<slug>` to `global/`) | structurally enforced | lint rule on granularity value × write path |
| Cross-client pattern conflation risk in `global/` | present (client-A patterns can enter `global/` untagged) | zero (client-tagged pages cannot enter `global/` without promotion ack) | eliminated | granularity gate |

**Refusal check.** Does this delta change the Method? No. The E-16
granularity field remains a single frontmatter field with the same semantic
function (scoping artefacts by context). Adding one parametric value extends
the enum within the existing method's parameters. Delta-extras ships.

---

### REFUSED — H-4 per-client alpha (method-change escalation)

**Critic finding (H-4).** α-5 Direction is Jetix-central only. A per-client
Direction alpha (`α-5c`) would require a new alpha state machine with
`client_scope` field.
[src: systems-critic-ontology-audit §1 H-4, §3 H-4 alt-1]

**Refusal rationale.** Adding `α-5c` as a per-client Direction alpha is a
Method-change: it adds a 6th alpha instance type to the D5 5-alpha design,
introducing a new state machine with per-client ownership semantics and a
new `client_scope` field on alpha transitions. Per FPF E-4 + systems-expert
§4.3, the optimizer cannot optimize a Method (capital-M). The 5-alpha design
(α-1..α-5) is a locked D5 deliverable.

**Preferred alternative (no Method change).** Per critic §3 H-4 Alt-2:
per-client strategic hypotheses are tracked as ordinary wiki artefacts
(`type: direction-hypothesis`, `granularity: client:<slug>` — covered by
Delta-extras). These participate in α-2 Artefact lifecycle, not α-5 Direction.
Escalation to α-5 strategizing occurs via HITL packet when client evidence
reaches F ≥ F4. This involves no new alpha, no new state machine, no D5
modification.

**This refusal plus the preferred alternative is the optimizer's recommendation.
The integrator-mode cell (systems × integrator) may synthesize this across
expert views.**

```yaml
escalations:
  - trigger: method-change
    description: "H-4 requires adding per-client α-5c Direction alpha — a 6th
      alpha state machine with client_scope field. This modifies the locked D5
      5-alpha design. Optimizer refuses per §4.3."
    suggested_routing: systems-expert × integrator OR HITL (brigadier decides
      whether to keep α-5 Jetix-central + introduce per-client direction-hypothesis
      artefacts via α-2, or open a Phase-B D5-extension gate)
    alternative_no_method_change: "Per-client direction hypotheses tracked as
      type: direction-hypothesis, granularity: client:<slug> artefacts in α-2
      lifecycle. Route to α-5 only via HITL when evidence reaches F ≥ F4."
```

---

## §3 Feedback loops per delta

The optimizer is required to name the feedback loop each delta touches.

| Delta | Loop touched | Polarity | Loop description |
|---|---|---|---|
| Delta-1 (`holon-ref` edge) | R1 — ingest → retrieval → synthesis → writeback → ingest | reinforcing (+) | Delta-1 adds a boundary-marker edge that prevents the R1 loop from traversing into cross-client territory. The loop remains reinforcing within each client's knowledge graph; the `holon-ref` lint rule acts as a balancing gate at the boundary (converts unbounded R1 into bounded R1 per client). |
| Delta-1 (secondary) | B1 — lint → contradiction → supersession → stability | balancing (−) | `holon-ref` lint rule adds a new cross-holon rejection check to the B1 lint loop. B1 gains one more contradiction type to surface: "cross-holon-root `holon-ref` detected." No change to loop polarity; the balancing loop becomes more precise. |
| Delta-2 (peer-holon naming) | B2 — brigadier-scope → client-read → isolation-violation → HITL | balancing (−) | Delta-2 closes the B2 loop by removing the structural path that allows brigadier to read client sub-holons in the containment model. The balancing loop no longer needs to detect a violation that is now architecturally impossible. B2 becomes a detection loop for peer-model violations (e.g., an agent mis-configured with containment-model paths). |
| Delta-5 (edge-store sharding) | R2 — retrieval variety → BFS precision → synthesis quality → KB growth → retrieval variety | reinforcing (+) | Per-client edge-store sharding ensures the BFS controller's variety matches the client's knowledge graph variety (Ashby). As the client's KB grows (R2 loop), the sharded edge store keeps BFS precision high. Without sharding, R2 degrades at scale: more KB → more merged edges → lower BFS precision → worse synthesis → R2 becomes a balancing drag. |
| Delta-extras (`client:<slug>` granularity) | B3 — global/compound-rules accumulation → cross-client rule pollution → agent output degradation | balancing (−) | Delta-extras closes B3 by making the `/lint` rejection a structural gate. Without it, B3 runs unbalanced: Jetix brigadier accumulates client-specific rules into `global/compound-rules/` indefinitely, degrading every client's output. With the lint rule, B3 is a tight balancing loop: any write attempt with `granularity: client:<slug>` to `global/` triggers immediate rejection. |

---

## §4 Requisite-variety checks (Ashby)

For each delta that affects a scale-relevant mechanism, the optimizer confirms
that controller variety remains ≥ system variety post-delta.

| Delta | Controller | System | Controller variety | System variety | Balance verdict |
|---|---|---|---|---|---|
| Delta-1 (`holon-ref`) | `/lint` cross-holon validator | federated client graph (N clients × M pages each) | High: lint rule checks every `holon-ref` target against holon-roots-registry; variety = number of registered holon roots (grows linearly with client count; registry lookup is O(1) per edge) | High: system variety = number of distinct cross-holon paths that could be attempted; bounded by N_clients × max_edges_per_client | BALANCED. Lint variety (registry-based lookup) scales with client count exactly as system variety does. No variety gap opens at scale. |
| Delta-5 (edge-store sharding) | Tier-3 BFS retrieval agent (per-session) | client's knowledge graph (pages + edges) | Per-client shard: BFS loads only client's JSONL; controller variety = number of distinct edge paths within the client's shard (~25 × page_count) | System variety = actual distinct knowledge paths in the client's graph | BALANCED per client. At 5K pages per client: ~125K edges, ~50MB — within networkx ceiling. Upgrade path (layer-sharding → PPR index) declared at ~8K pages/200K edges, maintaining balance at larger scales. |
| Delta-extras (`client:<slug>`) | `/lint` global-write gate | `global/compound-rules/` write surface (N artefacts per cycle) | Lint variety = binary check on `granularity` field value + `to` path prefix; O(1) per write attempt | System variety = number of distinct artefact types that could be written to `global/` with client-specific content | BALANCED. The lint check's variety equals the system's write-attempt variety; the gate doesn't degrade with scale. |
| Delta-2 (peer-holon naming) | FPF Part 8 Rule A (Janus duality; structural) | client-facing deployment topology | Structural: peer-holon model assigns independent Janus duality to each client; no controller needed because structural isolation prevents the violation rather than detecting it | System variety = number of possible topology mis-configurations | BALANCED by construction. The peer model eliminates the variety gap: there is no cross-holon read path for brigadier to control, so the controller variety question becomes moot. This is the preferred Ashby resolution — reduce system variety rather than increase controller variety. |

---

## §5 Refusals (method-change escalations)

### H-4 per-client α-5c: refused

Adding a 6th alpha (`α-5c`) with a `client_scope` field is a method-change
on the D5 5-alpha design — a locked deliverable. The optimizer refuses and
returns the escalation packet documented in §1 above.

```yaml
escalations:
  - trigger: method-change
    description: "H-4: adding per-client Direction alpha (α-5c) modifies D5 locked design"
    suggested_routing: "systems-expert × integrator OR HITL"
    alternative_no_method_change: "direction-hypothesis artefacts in α-2 lifecycle with granularity: client:<slug>"
```

No other refusals. H-1, H-2 (partial), H-3, H-5 are closeable by the
deltas above without Method changes.

**H-2 partial note.** The critic's H-2 finding (Layer-7 `global/` not
per-client gated) is partially closed by Delta-extras (`client:<slug>`
granularity gate). The remaining portion of H-2 — whether `global/`
should be absent from client-holon instances entirely (critic's Alt-2) —
is a Method choice (redesigning the 9-layer layout for client instances vs
Jetix-central), and the optimizer refuses to decide it. That choice is for
integrator-mode or HITL.

```yaml
escalations:
  - trigger: method-change
    description: "H-2 residual: whether client-holon instances should omit Layer-7 global/ entirely
      (critic Alt-2 — a new 'local-patterns' Layer 7-prime) is a structural Method choice
      that changes the 9-layer layout for client instances. Optimizer refuses."
    suggested_routing: "systems-expert × integrator OR brigadier HITL gate"
```

---

## §6 Janus risk delta (S-A vs INT excess flag)

| Delta | S-A delta | INT delta | Net Janus effect |
|---|---|---|---|
| Delta-1 (`holon-ref`) | S-A reduced: each client holon gains an explicit boundary-marker edge that makes it legible as a self-assertive whole. `/lint` now enforces the client's autonomy boundary structurally. | INT reduced: the integrative over-coupling (shared edge store treating all clients as one system) is broken. Jetix brigadier's INT obligation no longer structurally extends over client data. | Janus balance improved. Both S-A and INT excess risks reduced. The dominant prior risk was INT excess (9.5: over-integration of client data into a single shared graph); Delta-1 directly corrects it. |
| Delta-2 (peer-holon naming) | S-A increased (desired): naming the peer model increases the formal self-assertive scope of each client holon. The client holon is now explicitly declared whole-inward, not a sub-holon under Jetix. | INT reduced: the containment model's INT risk (Jetix brigadier reads client sub-holons) is eliminated at the topology-naming level. | Janus balance improved. S-A increase is the correct direction for UC-9 (client autonomy); INT reduction prevents the prior containment-model leak. |
| Delta-5 (edge-store sharding) | S-A increased (desired): per-client edge store means each client holon's knowledge graph is self-contained and can act autonomously (offline-first inference over its own shard). | INT reduced at the edge level: no cross-client graph community detection possible from a single monolithic store. Cross-client pattern synthesis routes through Ruslan HITL (deliberate INT gate). | Janus balance improved. The INT reduction is intentional: cross-client synthesis should require human judgment, not automated BFS traversal. |
| Delta-extras (`client:<slug>` granularity) | S-A neutral: the granularity field is per-artefact, not per-holon. Client artefacts can now be explicitly tagged as client-scoped; this supports their self-assertive identity at the artefact level. | INT reduced: the gate prevents client-specific patterns from flowing into `global/` without HITL ack. Reduces the automatic INT pull that compresses client-specific learning into universal rules. | Janus balance improved. The INT reduction is the primary effect; S-A effect is minor but positive. |
| H-4 refusal (no α-5c) | S-A protected: refusing to add a per-client α-5 avoids proliferating the strategizing ritual across client deployments, which would diffuse Ruslan's self-assertive strategic authority. | INT protected: keeping α-5 Jetix-central preserves the integrative function of Jetix's strategic direction as a coherent whole, rather than fragmenting it into N per-client Direction machines. | Janus balance maintained by refusal. The preferred alternative (direction-hypothesis artefacts in α-2) expresses per-client strategic signals without fragmenting the α-5 strategizing ritual. |

---

## §7 F-G-R summary per delta

| Delta | F | ClaimScope | R |
|---|---|---|---|
| Delta-1 (`holon-ref` edge needed) | F4 (operational convention: all 12 existing edge types inspected; none carry cross-holon boundary semantics) | Holds for any federated multi-client deployment of the 9-layer wiki v3 spine; does not apply to the Jetix-internal single-tenant case (no additional edge needed there) | Refuted if `/lint` can correctly reject cross-client `part_of` traversal using only the existing 12-type enum and no new edge type — this would require an existing edge type to carry cross-holon guard semantics, which the D3 spec does not assign to any of them [src: ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md D3 §3.2.1-§3.2.12] |
| Delta-2 (peer-holon naming in D1) | F4 (operational convention grounded in FPF Part 8 Rule A; the peer model is a permitted topology per E-11; the containment model is the implicit default per E-12 Level-3 placement) | Holds for the federated multi-client deployment design decision; does not prescribe which topology Ruslan must choose for future clients — only names which one is UC-9 safe | Refuted if FPF Part 8 can be shown to forbid peer-holon topology for the client-Jetix relationship, or if a containment model with an explicit read-barrier mechanism (not currently defined) can provide equivalent UC-9 isolation [src: FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md Part 8 §8.1 Rule A E-11, E-12] |
| Delta-5 (per-client edge-store sharding) | F3 (multi-case pattern: per-client JSONL is structurally analogous to the existing `cross-tree.jsonl` separation for v3-vs-v2 edges; the pattern is proven within the current spec; the federated extension follows the same pattern) | Holds within the Phase A + G1/G2 scale gates (≤5K pages per client, ≤2 active clients); at G3+ (≥8K pages per client or ≥5 clients), the per-layer shard and PPR index upgrade path must fire | Refuted if BFS latency on 50K edges in a single monolithic file remains ≤30 seconds per query under federated load — this would eliminate the variety mismatch that motivates the sharding [src: UC-8 G2 gate specification, ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md UC-8] |
| Delta-extras (`client:<slug>` E-16 extension) | F4 (operational convention: the `granularity` field already exists in E-16; the enum extension follows the same parametric pattern as the existing 4 values; the `/lint` gate mechanism is the same as the existing `niche-edge invariant` lint rule) | Holds for any artefact that originates in a client engagement and should not propagate to Jetix-central `global/` without explicit promotion; does not affect artefacts tagged `granularity: jetix-shared` (they continue to flow freely to `global/`) | Refuted if a cross-client pattern is demonstrably universal (applies to all Jetix clients regardless of context) and the `granularity: client:<slug>` gate incorrectly blocks it — in which case the promotion path (HITL ack + redaction + `granularity: jetix-shared` change) provides the release valve [src: FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md E-16] |

---

## §8 Coverage matrix

| Critic finding | Delta proposed | Closes fully? | Residual |
|---|---|---|---|
| H-1 (13th edge for cross-holon boundary) | Delta-1 (`holon-ref`) | Yes — structural cross-holon guard added; lint enforces | None |
| H-2 (Layer-7 `global/` not per-client gated) | Delta-extras (`client:<slug>` granularity gate) | Partial — artefact-level gate added; topology-level question (omit `global/` from client instances?) is a Method choice | Residual escalated: systems × integrator OR HITL decides whether client-holon instances omit `global/` entirely (critic Alt-2) |
| H-3 (peer-holon model not named) | Delta-2 (one sentence in D1 §1.3) | Yes — peer model named; containment forbidden for UC-9; lint rule from Delta-1 enforces cross-holon-root rejection | None |
| H-4 (α-5 Jetix-central only; no per-client Direction alpha) | REFUSED (method-change) | No — refused. Preferred alternative: direction-hypothesis artefacts in α-2 with `granularity: client:<slug>` | Escalated to systems × integrator OR HITL |
| H-5 (BFS recall degradation at federated scale) | Delta-5 (per-client JSONL + upgrade path declaration) | Yes for Phase A + G1/G2 scale; G3+ upgrade path declared | G3+ upgrade (layer-shard + PPR index) is declared, not implemented in Phase A |

---

## §9 Provenance

| Source | Range | Quote |
|---|---|---|
| `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md` | §1 H-1 | "13th edge required — H-1 fails: 12-edge enum has no edge type that expresses cross-client containment without leaking semantics" |
| `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md` | §6 federated-holon proof sketch | "Per-client `edges.jsonl` is a per-instance file; no process running in client-A's context has filesystem permission to `client-B/wiki/graph/edges.jsonl` — enforced by OS permissions, not by agent policy" |
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D3 §3.2.9 `part_of` | "Allowed `to`: `topics` (hub→children pattern), `foundations` (sub-foundation → over-foundation). Cross-layer flag: No." — no cross-holon guard |
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D3 §3.3 from×to matrix | "from×to matrix — L7 row: `layer-ref` to most layers; no `holon-containment` edge type exists" |
| `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D3 §3.5 edge-types.md content | "Adding or modifying an edge type requires AWAITING-APPROVAL escalation (D6 §4)" — confirms path for Delta-1 |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 8 §8.1 Rule A (E-11) | "Failure modes to guard against in retrospective audits: 9.4 S-A excess / 9.5 INT excess" |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 8 E-12 | "level-3-supersystem: client context (when applicable)" — confirms containment-model default |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 4 §4.1 α-5 | "AI agents do NOT move the Direction alpha beyond tracking" — confirms α-5 is Jetix-central; per-client α-5c would violate the single-strategizing-ritual discipline |
| `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md` | Part 8 §8.1 Rule F (E-16) | "`granularity: jetix-business \| jetix-life-os \| jetix-shared \| task-scoped`" — no `client:<slug>` value; gap confirmed |
| `prompts/km-architecture-research-2026-04-24.md` | §3.9 UC-9 | "The architecture must make this impossible by construction — not by policy, not by careful admin... by the physical / directory / cryptographic structure of the variant" |
| `prompts/km-architecture-research-2026-04-24.md` | §3.9 UC-9 | "cross-client edges in `graph/edges.jsonl` are FORBIDDEN; the only edges from Client-A KB point to Jetix methodology repo, not to other clients" |
| `prompts/km-architecture-research-2026-04-24.md` | §3.8 UC-8 G2 gate | "edges.jsonl in-memory size crosses ~50MB (networkx load)" — confirms the BFS ceiling that motivates Delta-5 |
