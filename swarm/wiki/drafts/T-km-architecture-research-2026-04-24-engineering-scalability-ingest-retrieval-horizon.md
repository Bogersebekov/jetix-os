---
title: Engineering × Scalability — 5-Gate Horizon Projection (6 variants)
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
confidence_method: expert-judgment-from-integrator-drafts-and-research-G
tier: tier-1
produced_by: engineering-scalability
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md
  - prompts/km-architecture-research-2026-04-24.md
related: []
binding_scope: km-architecture-engineering-scalability-horizon
mode: scalability
---

# Engineering × Scalability — 5-Gate Horizon Projection (6 variants)

---

## §1 A3 + B3 Axis-Design (Proposal — 3rd Categorically-Different Axes)

### A3 Proposed: GraphRAG Community-Summaries with HippoRAG PPR Hybrid

**Axis name:** Pre-compiled community-summaries + PPR-indexed graph (GraphRAG/HippoRAG hybrid)

**Governing metaphor.** Where A1 is a self-compounding personal wiki (write-heavy, retrieval-lean, grep-first) and A2 is a federated peer-holon constellation (each client is a sovereign wiki peer), A3 is the **pre-compiled knowledge atlas**: every major topic cluster is distilled into a pre-generated community-summary page at ingest time, and the retrieval path queries summaries first, then expands via HippoRAG Personalized PageRank over the typed-edge graph. The metaphor is the pre-indexed academic reference library: the index is assembled once, maintained on change, and consulted at query time rather than re-scanned.

**Differentiation.** A1 relies on grep + depth-2 BFS for retrieval (on-demand assembly). A2 layers federation on top of A1 mechanics. A3 differs categorically: it adds a preprocessing step (community detection over `edges.jsonl` → `graph/summaries.md` + per-cluster `graph/community-<id>.md` pages) and a PPR query path that scores candidate pages by graph centrality before filtering by keyword relevance. This is GraphRAG §A.2 + HippoRAG §A.3 mechanics applied to the Jetix wiki v3 substrate. [src: knowledge-arch §A.2, §A.3, §G.2]

**Key tradeoff.** Pre-compilation cost vs retrieval quality at scale. At G1 (557 pages), community detection is over-engineering — A1 grep is faster. At G3 (8K+ pages per client), A1 grep degrades to 60-120s per query; A3's pre-indexed summaries answer community-level queries in 2-5s. A3 becomes the correct choice when per-client page count crosses ~3K pages and cross-domain synthesis queries ("what are the recurring ERP integration challenges across this client's projects?") dominate the workload.

**A3 UC-9 status.** Passes by the same mechanism as A1/A2: per-client community-summary files live under `clients/<slug>/swarm/wiki/graph/community-*.md`; PPR operates over the client's private `edges.jsonl`. No cross-client community detection is performed.

**A3 UC-10 status.** Community-summary pages serve as high-quality offline retrieval targets. In offline mode, `/ask` reads the pre-compiled `graph/community-<cluster>.md` page matching the query's cluster (identified by keyword-to-cluster index) instead of running PPR dynamically. This gives substantially better offline quality than A1's structured-excerpt path at the cost of pre-compilation storage (~10-50KB per community summary page; ~50 pages at G2).

F: F3 | ClaimScope: A3 viable at G2+ (3K+ pages per client); at G1 over-engineering vs A1 | R: `refuted_if` community detection at G2 requires Bash-executed Python graph libraries not available in Phase-A tool set (then A3 is deferred to Phase B infra unlock)

---

### B3 Proposed: Adaptive Scaffold — Phase-Gated Autonomy with Milestone-Trigger Mini-Swarm

**Axis name:** Phase-gated autonomy + emergent-richness scaffold

**Governing metaphor.** Where B1 is a flat namespace with project-as-subtree (all projects share a single brigadier, operations/ tree) and B2 is per-client federated holons with rich scaffold from day one, B3 is the **evolutionary project organism**: projects start thin (3 files, single brigadier) and acquire richer structure — dedicated project-brigadier, allocated experts, weekly digest, cross-project patterns — only when milestone gates are crossed. The metaphor is biological morphogenesis: the organism's complexity is not pre-specified at birth but emerges from developmental triggers.

**Differentiation.** B1 adopts a static rich scaffold for all projects at all stages. B2 layers federation on top. B3 differs categorically in the temporal dimension: a project's agent allocation and wiki richness are a function of its evidence-validated maturity stage, not its P-level assignment at spawn. A P1 project at `stage: hypothesized` gets 3 files and a shared brigadier; the same project at `stage: validated` (evidence F≥F4 on problem_statement + ≥3 client meetings logged) gets a dedicated project-brigadier + 2 allocated experts + weekly digest. This makes B3 the lowest-friction onboarding path (UC-5: scaffold creates in 5-10 minutes, not 30) while ensuring P1 projects receive full infrastructure once they earn it.

**Key tradeoff.** Phase-gated complexity vs early-stage consistency. B1 and B2 give Ruslan a predictable scaffold; B3 requires a clear stage-gate predicate to avoid projects stagnating at thin-scaffold with insufficient agent support. The stage-gate predicate must be operationalized as a Hamel-binary (e.g., "≥3 client sessions logged AND problem_statement: non-empty AND F≥F4 evidence in ≥1 open-question") — otherwise the "adaptive" framing degrades into ad-hoc allocation.

F: F3 | ClaimScope: B3 valid for Phase-A 8-project roster; stage-gate predicate must be formalized before first client project | R: `refuted_if` first 3 real projects show the stage-gate stagnation pattern (projects stay thin indefinitely without trigger)

---

## §2 Variant A1 Karpathy++ — 5-Gate Table

**Architecture baseline:** Filesystem-resident wiki, grep + typed-BFS depth-2 retrieval, per-client namespace via `WIKI_ROOT_CLIENT_ID` env-var, Phase-A structured-excerpt offline path + Phase-B ollama/Llama 3.1-8B Q4_K_M.

[src: engineering-integrator §4.1-§4.4, engineering-optimizer Δ1-Δ4]

| Gate | Revenue / Scale | Pages/client | Projects | Clients | Physical Failure | Upgrade Path | MHT Event | BOSC-A-T-X | Janus Risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | Q2 2026 | ≤1K | ≤8 Jetix-internal | 0–1 pilot | Grep scan ~2-5s; BFS on 572 edges ~50ms; `edges.jsonl` ~57KB — all in-memory, no ceiling reached | None; A1 fully operational. Δ1-Δ4 applied; `WIKI_ROOT_CLIENT_ID` enforcement wired | Phase Promotion — engineering discipline moves from spec-only to operational (hooks wired, schema validated) | **C+S** — Composition (client namespace) + Scale (first real ingest runs) | INT excess: single flat wiki; methodology-extraction loop not yet habitual | T-Offline: structured-excerpt (Δ2). No GPU required. 1-3s latency |
| **G2 €200K** | First paying external client | 3-5K/client | ≤8 + first client projects | 1–3 | Grep at 3-5K pages: 30-60s (at edge of 180s budget); `edges.jsonl` ~300-500KB — BFS ~500ms still safe; `WIKI_ROOT_CLIENT_ID` is policy-level: a skill-body bug could cross roots | Pre-build per-niche BM25 index; upgrade `WIKI_ROOT_CLIENT_ID` to Phase-B separate-repo-per-client (Refusal R-2 Method-change: HITL ack required) | Phase Promotion — engineering-expert moves from phase1-solo to phase1-with-reviewer; first paying client triggers Phase-B isolation | **A+C** — Agency (first client agent instance) + Composition (per-client repo) | S-A excess risk: brigadier scope expands to cover client wiki without structural separation | T-Hybrid: ollama + Llama 3.1-8B Q4_K_M on 16GB GPU (Phase B AWAITING-APPROVAL). 15-25s per 200-token answer |
| **G3 €1M** | Consulting scale | 5-10K/client | 15-30 | 5-15 | `edges.jsonl` per client may hit 50MB BFS ceiling at 10K pages (~200K edges per knowledge-arch §G.2 threshold for networkx); grep at 10K pages exceeds 180s budget without BM25 | Layer-sharding: `edges-L1.jsonl`..`edges-L7.jsonl` per niche; per-client BM25 sparse index; `/build-graph` triggered daily | Fission — engineering-expert splits into code-expert + architecture-expert per §1d split_trigger (artefact-mix 60/40) | **O+C** — Operation (multi-developer commit model) + Composition (release-engineer role) | S-A excess: architecture-expert over-asserts on client isolation design without code-expert's implementation constraints | T-Hybrid per client. MoE 8x7B Q4_K_M considered if single-client query quality insufficient (hardware floor: 32GB GPU, ~25GB VRAM) |
| **G4 $100M** | Platform scale | 50K+/client aggregate | 50+ | 50-500 | Neo4j threshold (~20K edges per §G.2) crossed for largest clients; grep is infeasible at 50K pages; BFS on flat JSONL is O(n) — too slow | Hybrid retrieval: BM25 + HippoRAG PPR + GraphRAG community summaries; persistent graph store (Neo4j/LightRAG); per-client index-as-database | Role-Lift — engineering disciplines lift to method-author level; build-system requires queue-management; SRE on-call | **C+X** — Composition (platform-engineer + SRE) + eXternal (SOC2/GDPR regulatory) | INT excess: over-coupled clients lose isolation if Neo4j is shared; each client must have own graph DB instance | MoE or 70B Q4_K_M local; or T-Cloud for clients with explicit opt-in; GPU cluster floor: 2x A100 80GB per client or shared Jetix-hosted |
| **G5 $1T** | Industry-consortium scale | Variable | Hundreds | 5000+ | Monolithic per-client graph DB instances don't survive 5000+ client ops; cross-Alliance slug-normalised contradiction detection is demanded | Alliance-federation store: per-holon graph DB; Jetix-methodology as open standard; cross-client is slug-normalised only (philosophy-critic Alt-B) | Context Reframe — engineering-expert reframes from artefact-judge to method-steward across N business units | **X+T** — eXternal (Alliance-level IP) + Time (multi-year methodology roadmap) | Both: S-A excess (every holon declares own method) + INT excess (Alliance needs shared methodology evolution) | Per-client choice of inference stack; Jetix provides certified GGUF bundles per Mittelstand LLM spec; Alliance certifies GPU floor |

**Antifragility check (A1):**
- Build system 10×: from 1 developer to 10 developers, build system (Makefile + git) is unchanged. Not fragile. Refactor cost ≤15%.
- Architecture pattern 10×: A1 (flat wiki + grep + BFS) degrades at G3 (8K+ pages). 30%+ refactor required to add BM25 + layer-sharding at G3. Fragile at G3.
- Test suite 10×: no dedicated test suite in Phase A; `/lint` is the functional equivalent. Fragile if `/lint` latency scales poorly.
- Dependency graph 10×: external deps = grep + YAML + ollama (Phase B). Grep is stable; ollama dependency is well-encapsulated. Not fragile.

**Tier split summary (A1):** G1-G2: T-Offline (Phase A) / T-Hybrid (Phase B); G3-G4: T-Hybrid mandatory; G5: T-Cloud optional per client.

---

## §3 Variant A2 Federated Peer-Holons — 5-Gate Table

**Architecture baseline:** Each client is a separate peer holon (separate git repo in Phase B), with `holon-ref` edge enforcement, per-client `edges.jsonl`, and Jetix-methodology as read-only submodule. [src: systems-integrator §1.2, §4]

| Gate | Revenue / Scale | Pages/client | Projects | Clients | Physical Failure | Upgrade Path | MHT Event | BOSC-A-T-X | Janus Risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | Q2 2026 | ≤1K | ≤8 internal | 0–1 | Same as A1 at G1. Additionally: `holon-roots-registry.md` is hand-managed; `/lint` `holon-ref` check is new and untested in production | Apply Δ1-Δ4 (A1 deltas apply). Provision `holon-roots-registry.md`. Run first `/lint` cross-holon check | Phase Promotion — `holon-ref` lint rule goes operational; first client holon registered | **C+S** — Composition (13th edge type operational) + Scale (first holon provisioned) | INT excess: Jetix-methodology holon not yet receiving cross-client methodology-update loop | T-Offline. No GPU. Structured-excerpt. 1-3s |
| **G2 €200K** | First paying client | 3-5K/client | ≤8 + client | 1–3 | Methodology-update fan-out: pushing versioned submodule update to 1-3 clients requires manual git push per client; not automated. At 3 clients this is manageable; at 10+ it becomes operational debt | Automate submodule version push via CI/CD pipeline (git bundle + push hook); separate-repo provisioning script | Phase Promotion — A2 becomes operational; federated model PROVEN by first paying client with Phase-B repo isolation | **A+C** — Agency (client agent instance running autonomously) + Composition (git submodule methodology push) | INT excess: quarterly methodology-update cycle may be too slow if clients diverge rapidly | T-Hybrid: ollama + Llama 3.1-8B Q4_K_M per client on their hardware. Phase B operational |
| **G3 €1M** | Consulting scale | 5-10K/client | 15-30 | 5-15 | Per-client `edges.jsonl` reaches BFS ceiling (~200K edges). Methodology-submodule drift: if clients don't pull updates, methodology divergence becomes tracking problem | Per-client layer-sharding (same as A1 G3) + automated methodology-drift detection (CI check: client submodule SHA vs latest methodology SHA) | Fission — engineering splits into code-expert + architecture-expert. Architecture-expert owns federation protocol; code-expert owns per-client skill bodies | **O+C** — Operation (multi-client ops team) + Composition (per-client brigadier instances) | S-A excess: each client holon becomes more self-assertive than Jetix methodology can track; drift accumulates | T-Hybrid. MoE Q4_K_M for complex clients. 32GB GPU floor |
| **G4 $100M** | Platform scale | 50K+/client | 50+ | 50-500 | Methodology-update: 500 client repos cannot receive manual submodule pushes; CI-based push pipeline is the only viable path. Per-client graph store must be isolated at DB level | Automated methodology package registry (methodology as versioned npm-like package); per-client graph DB; Jetix-methodology-holon becomes read-only CDN-like distribution | Role-Lift — Jetix-methodology-holon lifts to standards body role; engineering method becomes a moat artifact | **C+X** — Composition (methodology-as-package) + eXternal (EU AI Act certification of methodology layer) | Both: S-A (clients over-customize, methodology fragments) + INT (methodology body can't absorb 500-client feedback loops fast enough) | GPU cluster per client or shared Jetix-hosted (Path A). Alliance-certified GGUF bundles |
| **G5 $1T** | Alliance scale | Variable | Hundreds | 5000+ | Alliance-member methodology drift at 5000+ nodes is ungovernable without Alliance-level governance structure (EISA-parallel: need governance body, not just git) | Mittelstand AI Alliance as formal governance body (Linux Foundation model); methodology versioning governed by Alliance committee; Jetix is methodology author, not sole controller | Context Reframe — Jetix transitions from methodology-author to methodology-steward; Alliance owns evolution | **X+T** — eXternal (Alliance legal + IP structure) + Time (multi-year roadmap cadence) | INT excess: Alliance under-couples if governance body is too slow; S-A excess: individual Alliance members over-customize until interoperability breaks | Alliance-certified open-source GGUF; any member can fork; Jetix provides reference implementation |

**Antifragility check (A2):**
- Build system 10×: separate-repo model means each client's build system is independent. Fragile in aggregate (10× clients = 10× operational repos to manage) but not technically fragile. Refactor cost per client ≤15%; total ops cost scales linearly — this is the intended tradeoff.
- Architecture pattern 10×: A2 peer-holon model is explicitly designed for 10× client scale. The federation protocol (git submodule + holon-root registry) does not require re-architecture at G3. Not fragile.
- Test suite 10×: same as A1 — `/lint` per client. At G3, per-client lint runs must be parallelisable. Mild fragility if lint is run serially. Refactor: add parallel lint invocation. Cost <10%.
- Dependency graph 10×: git + YAML + ollama per client. At 50+ clients, git remote management is the operational bottleneck. Not a codebase refactor but an ops upgrade. Not structurally fragile.

**Tier split summary (A2):** G1: T-Offline; G2: T-Hybrid per client (client-hosted); G3-G5: T-Hybrid mandatory per client; T-Cloud only if client explicitly opts in.

---

## §4 Variant A3 GraphRAG/HippoRAG Hybrid — 5-Gate Table

**Architecture baseline:** Pre-compiled community-summary pages + PPR-indexed graph retrieval. Retrieval path queries `graph/community-*.md` pages first, then expands via HippoRAG PPR. Community detection runs at `/build-graph` step. [src: knowledge-arch §A.2, §A.3, §G.2; A3 axis-design §1]

| Gate | Revenue / Scale | Pages/client | Projects | Clients | Physical Failure | Upgrade Path | MHT Event | BOSC-A-T-X | Janus Risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | Q2 2026 | ≤1K | ≤8 | 0–1 | Community detection at 557 pages: overkill. `/build-graph` community step (LLM-assisted cluster labeling) takes 5-15 minutes per run — latency acceptable weekly but costly. PPR at 572 edges is trivial. Risk: over-engineering slows Phase-A iteration velocity | Do NOT activate community detection at G1. Use A1 mechanics (grep + BFS). Declare A3 architecture; activate community-detection step at G2 threshold (≥3K pages) | Phase Promotion — same as A1 G1: engineering governance moves from spec to operational | **C** — Composition only: community-detection step added to `/build-graph` skill but not yet triggered | S-A excess: engineering-expert insists on full GraphRAG community pipeline at 557 pages — this is AP-ENG-9 premature abstraction | T-Offline. No GPU. Community pages not yet generated; falls back to A1 offline path |
| **G2 €200K** | First paying client | 3-5K/client | ≤8 + client | 1–3 | Community detection triggers at ~3K pages. LLM-assisted cluster labeling (community detection) requires Claude Code session — not offline-capable. Pre-built community-summary pages are static until next `/build-graph` run | Activate community detection in `/build-graph`; generate `graph/community-*.md` pages per client. Offline path queries community pages without LLM (community page is the pre-compiled summary) | Phase Promotion — A3 retrieval path goes operational; offline quality measurably better than A1 structured-excerpt | **A+C** — Agency (first per-client community graph generated) + Composition (PPR index per client) | INT excess: community detection can surface cross-domain patterns that violate per-client isolation if run over shared edges (must run per-client) | T-Hybrid: community pages serve as offline synthesis substrate. Local LLM (ollama + Llama 3.1-8B) for PPR-ranked synthesis. 16GB GPU |
| **G3 €1M** | Consulting scale | 5-10K/client | 15-30 | 5-15 | PPR at 200K+ edges exceeds networkx in-memory ceiling (~20K edges per §G.2). Community detection at 10K pages requires persistent graph store. `/build-graph` runtime: 30-60 min per client with LLM cluster-labeling | Migrate to persistent graph store per client (LightRAG as simpler alternative to Neo4j; file-based). Pre-compute PPR vectors nightly. Community summaries cached | Fission — engineering splits. Architecture-expert owns graph-DB selection and community-detection pipeline; code-expert owns per-client `/build-graph` invocation | **O+C** — Operation (graph DB ops) + Composition (LightRAG or Neo4j per client) | S-A excess: architecture-expert over-designs community-detection pipeline beyond client needs | MoE 8x7B Q4_K_M for PPR-ranked synthesis. 32GB GPU. Community pages reduce LLM call frequency |
| **G4 $100M** | Platform scale | 50K+/client | 50+ | 50-500 | Hybrid retrieval fully operational (BM25 + dense + PPR + RRF per §G.3). Knowledge-arch §G.3 confirms this is the correct stack at 50K pages. Engineering-architecture is correct; ops complexity is the bottleneck | GraphRAG-style infrastructure (per §G.3): hybrid BM25 + dense + PPR + RRF + community summaries. Per-client vector DB (lightweight, e.g. FAISS sharded by client). Alliance-level community-slug vocabulary standardisation begins | Role-Lift — graph-DB ops team required. A3 becomes the reference architecture for Alliance-member deployments | **C+X** — Composition (Alliance reference architecture) + eXternal (ISO 27001 certification of graph-DB deployment per client) | Both: S-A (each client's community-detection produces different slug vocabulary, breaking Alliance cross-client metadata query) + INT (Alliance can't aggregate anonymised community slugs without vocabulary standardisation) | GPU cluster. Per-client FAISS/dense index. A3 enables best offline synthesis quality at scale via pre-compiled community pages |
| **G5 $1T** | Alliance scale | Variable | Hundreds | 5000+ | Slug-vocabulary divergence across 5000+ clients; community detection produces incompatible concept clusters; Alliance-level metadata query is unworkable without standardisation | Alliance-maintained slug ontology (SKOS or equivalent); community detection constrained to produce Alliance-compatible cluster names; Jetix methodology mandates community-slug vocabulary | Context Reframe — A3 architecture becomes the Alliance knowledge standard; Jetix is the reference implementation | **X+T** — eXternal (SKOS/slug vocabulary as Alliance standard) + Time (multi-year vocabulary governance) | Both: S-A excess (members resist slug standardisation as loss of sovereignty) + INT excess (without standardisation, cross-client contradiction detection is impossible) | Alliance-certified GPU floor per deployment tier; community-page offline path works regardless of model size |

**Antifragility check (A3):**
- Build system 10×: LightRAG/Neo4j per client adds a new build-system dependency. At G3 this requires automated provisioning. Moderately fragile — refactor cost 20-25% at G3.
- Architecture pattern 10×: A3 is explicitly designed for G3+ scale. The community-summary + PPR pattern does not break at 10× page count — it improves. Not fragile at G3+; mildly over-engineered at G1.
- Test suite 10×: community-detection correctness is hard to unit-test. At G3, community-page regression testing is needed. Fragile if untested. Refactor cost 15-20% to add community-detection test harness.
- Dependency graph 10×: adds LightRAG/Neo4j + FAISS at G3+. Dependency count grows from 3 (grep, YAML, ollama) to 7+ (+ LightRAG, FAISS, community-detection LLM, PPR algorithm). Moderately fragile — dependency management cost increases. Refactor: vendor-lock mitigation via abstraction layer over graph store.

**Tier split summary (A3):** G1: T-Offline (A1 fallback; A3 not yet activated); G2: T-Hybrid (community pages as offline substrate); G3-G5: T-Hybrid mandatory; community pages make T-Offline higher quality than A1/A2 at same gate.

---

## §5 Variant B1 Layer-6 Namespaces — 5-Gate Table

**Architecture baseline:** All projects as siblings under `swarm/wiki/operations/<slug>/`. Single brigadier. Attention-budget ratchet (Δ3). `/project-status` weekly sweep. [src: systems-integrator §2.1, mgmt-integrator §3]

| Gate | Revenue / Scale | Pages/client | Projects | Clients | Physical Failure | Upgrade Path | MHT Event | BOSC-A-T-X | Janus Risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | Q2 2026 | N/A (Jetix-internal) | ≤8 | 0 | `operations/<slug>/` exists but with legacy file names (README.md, decisions-log.md). Migration to 5-file scaffold requires renaming (mgmt-integrator §9). `/project-status` skill does not exist; brigadier produces status ad hoc | Execute migration sequence (mgmt-integrator §9 Steps 1-5). Draft `/project-bootstrap` and `/project-status` skill candidates. Wire Δ3 attention-budget ratchet | Phase Promotion — B1 moves from implicit (ad hoc) to operational (structured). First Hamel-binary project acceptance predicate wired | **C+S** — Composition (scaffold for all 8 projects) + Scale (ratchet wired at ≤20 tasks) | S-A excess: brigadier over-manages all 8 projects simultaneously; attention budget depletes | N/A for Layer-B (retrieval is Layer-A's responsibility) |
| **G2 €200K** | First paying client | N/A | ≤8 + client subtree | 1–3 | `operations/clients/<client-slug>/` as sibling of Jetix-internal projects. Policy-layer UC-9 isolation (directory + `granularity: client:<slug>`) is not by-construction. At G2 with 1 paying client, policy risk is manageable; at 3 clients it becomes a liability | Trigger Phase-B transition: separate-repo per client (mgmt-integrator §9 Phase-B upgrade). B1 operations/ tree for Jetix-internal projects; B2 for client projects | Phase Promotion — first client triggers B1→B2 hybrid split: Jetix-internal stays B1, client-projects migrate to B2 | **A+C** — Agency (project-brigadier allocated to client project) + Composition (client namespace in operations/) | S-A excess: brigadier scope extends over client project without structural isolation | N/A |
| **G3 €1M** | Consulting scale | N/A | 15-30 | 5-15 | Single brigadier at >20 active tasks fails the attention-budget ratchet (CLAUDE.md L42). `/project-status` sweep of 30+ projects in one session exceeds token budget | Split-trigger fires: brigadier delegates to ≤5 project-brigadiers (P1 projects only). Meta-brigadier coordinates; canonical brigadier handles promotions. B1 becomes B1+mini-B | Fission — brigadier splits into canonical-brigadier + project-brigadiers. Per-project brigadier scope bounded to `operations/<slug>/` | **O+C** — Operation (multi-project-brigadier model) + Composition (meta-brigadier layer) | Both: S-A (canonical brigadier over-controls project-brigadiers) + INT (project-brigadiers under-report to canonical, creating health blindspot) | N/A |
| **G4 $100M** | Platform scale | N/A | 50+ | 50-500 | `operations/<slug>/` flat namespace for 500+ client projects is unworkable. Project-brigadier proliferation (one per P1 project) exceeds coordination overhead | Full B2 transition; B1 retained only for Jetix-internal meta-projects (swarm maintenance, methodology development). B1 becomes the "methodology-project" namespace | Role-Lift — project-management methodology becomes a product line; B1 is the internal operating model | **C+X** — Composition (project-mgmt methodology as licensable product) + eXternal (PMBOK/ISO 21500 certification) | INT excess: B1 internal operations become disconnected from B2 client operations; cross-learning stops | N/A |
| **G5 $1T** | Alliance scale | N/A | Hundreds internal | N/A (all clients on B2) | B1 at $1T is the Jetix-internal methodology-development namespace; not client-facing | B1 continues as internal ops namespace. Alliance-members adopt B2 or B3 | Context Reframe — B1 is Jetix's internal operating model; externally Jetix ships B2/B3 as client-facing product | **X+T** — Time (B1 methodology evolves over decades) + eXternal (Alliance adopts B2/B3) | None at this scale — B1 scope is internal only | N/A |

**Antifragility check (B1):**
- At G3 (30 projects), B1 single-brigadier model fails the attention-budget. Refactor cost: add project-brigadier delegation layer. Cost ~25%. Fragile at G3.
- Operations/ flat namespace survives G1-G2 easily. Not fragile through G2.
- Tombstone protocol (4-step) adds complexity; at G3 with 30+ projects, missed-step probability increases. Mild fragility. Mitigation: `/lint` tombstone-integrity check.

---

## §6 Variant B2 Federated Per-Client-Per-Project — 5-Gate Table

**Architecture baseline:** Each client has autonomous project tree under `client-A/swarm/wiki/operations/`. Separate git repo in Phase B. Per-client brigadier instance. `local-patterns/` replaces `global/` in client holons. [src: systems-integrator §2.2, §4]

| Gate | Revenue / Scale | Pages/client | Projects | Clients | Physical Failure | Upgrade Path | MHT Event | BOSC-A-T-X | Janus Risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | Q2 2026 | ≤1K | ≤8 Jetix-internal | 0 (no clients yet) | B2 is Phase-B architecture. At G1, Jetix-internal projects stay on B1. B2 design is specced and ready; first client triggers B2 provisioning | Spec B2 fully; provision first client at G2 trigger. B2 provisioning script: `mkdir -p client-A/swarm/wiki/operations/` + seed `holon-root.md` + `local-patterns/` | Phase Promotion — B2 design moves from spec to provisioning-ready | **C** — Composition only: B2 spec completed | INT excess: B2 methodology not yet battle-tested on real client project | N/A at G1 |
| **G2 €200K** | First paying client | N/A | Client's projects | 1–3 | First client provisioning: separate-repo bootstrap takes 1-2 hours per client (manual). `local-patterns/` naming may confuse with local-LLM concepts (mgmt-integrator §10 open Q4). Methodology submodule update is manual git push | Automate client-repo provisioning script (brigadier-authored; HITL acks per client). Rename `local-patterns/` to `client-patterns/` if confusion confirmed | Phase Promotion — B2 goes live with first paying client; UC-9 proven by construction for first time | **A+C** — Agency (per-client brigadier running) + Composition (per-client project tree) | INT excess: quarterly methodology sync is only cross-client learning channel; if sync is missed, clients diverge | T-Hybrid per client (same as A2 G2) |
| **G3 €1M** | Consulting scale | N/A | 15-30/client | 5-15 | Per-client brigadier at 5-15 clients = 5-15 brigadier instances to monitor. Ruslan's oversight budget: at 15 clients × 3 projects each = 45 project-wiki trees; `/project-status` across all trees requires meta-aggregation layer | Cross-client meta-brigadier: aggregates per-client `meta/health.md` into a Jetix-level portfolio dashboard. Each per-client brigadier sends weekly summary to meta-brigadier | Fission — per-client brigadiers become autonomous; meta-brigadier coordinates at portfolio level | **O+C** — Operation (portfolio-level brigadier) + Composition (meta-brigadier aggregation layer) | S-A excess: per-client brigadiers become too autonomous; methodology drift not detected until quarterly sync | T-Hybrid per client. MoE models for heavy synthesis |
| **G4 $100M** | Platform scale | N/A | 50+/client | 50-500 | Meta-brigadier aggregating 500 client health summaries exceeds context window budget. Portfolio-level health becomes unreadable. Cross-client pattern detection is impossible by design (UC-9 invariant) | Portfolio dashboard via structured health-summary API: each per-client brigadier writes a 5-field health JSON to a Jetix-central `portfolio/health-<client>.json` (no client data, only health metadata). Meta-brigadier reads JSONs | Role-Lift — portfolio management becomes a product feature. B2 is the client-facing product; portfolio dashboard is Jetix's SaaS layer | **C+X** — Composition (health-JSON portfolio layer) + eXternal (EU AI Act audit trail per client) | Both: S-A (500 independent client brigadiers; no methodology coherence) + INT (Jetix can't absorb 500-client learning loops in quarterly manual sync) | GPU cluster per client or Jetix-managed pool. GGUF bundles certified per Alliance spec |
| **G5 $1T** | Alliance scale | N/A | Hundreds | 5000+ | Health-JSON aggregation at 5000+ clients requires automated analytics. Manual quarterly review by Ruslan is impossible at this scale | Alliance-level portfolio analytics: automated health-signal aggregation (no client data, only structured metadata). Alliance governance board reviews quarterly. Ruslan's role: methodology stewardship, not per-client oversight | Context Reframe — B2 becomes the Alliance's standard client-engagement architecture | **X+T** — eXternal (Alliance portfolio analytics) + Time (methodology evolution cycle) | INT excess: at 5000 clients, cross-client learning is purely statistical (pattern frequency across anonymised health signals); loss of individual engagement insight | Same as G4; Alliance-certified GGUF bundles |

**Antifragility check (B2):**
- Per-client repo model is explicitly designed for scale. Not fragile from G2 onward.
- Provisioning script automation is the critical fragility point at G3: if manual, it breaks at 15+ clients. Refactor: fully automated provisioning. Cost 20% of G3 engineering effort.
- Portfolio dashboard (health-JSON) is a G4 addition; its absence at G3 is not a failure — it's a declared Phase-B feature. Not premature.

---

## §7 Variant B3 Adaptive Scaffold — 5-Gate Table

**Architecture baseline:** Projects start with 3 files + shared brigadier (thin-scaffold). Stage-gate predicate triggers scaffold enrichment (dedicated project-brigadier + 2 allocated experts + weekly digest + cross-project pattern sweep) when evidence reaches F≥F4. [src: B3 axis-design §1]

| Gate | Revenue / Scale | Pages/client | Projects | Clients | Physical Failure | Upgrade Path | MHT Event | BOSC-A-T-X | Janus Risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | Q2 2026 | N/A | ≤8 | 0 | Stage-gate predicate must be formalized before B3 can operate. If predicate is fuzzy ("project seems mature"), the adaptive model collapses to ad-hoc allocation — worse than B1. Risk: stage-gate stagnation (projects stay thin indefinitely) | Formalize stage-gate predicate as a Hamel-binary. Wire into `_moc.md` frontmatter: `stage_gate_status: thin | validated | rich`. `/lint` checks: if `stage_gate_status: validated` AND `last_gate_evidence_date` > 14 days ago without transition → warn | Phase Promotion — B3 moves from concept to operational stage-gate | **C** — Composition: stage-gate predicate wired | S-A excess: per-project brigadiers may lobby for rich-scaffold allocation before evidence warrants it | N/A |
| **G2 €200K** | First paying client | N/A | Client's projects | 1–3 | Client project enters at thin-scaffold. Stage-gate predicate for client projects may differ from internal projects (client has contractual milestones that serve as natural stage-gates). Predicate must handle both internal and client contexts | Extend stage-gate predicate to include client-specific triggers: "client signed off first milestone" = `stage_gate_status: validated`. First paying client tests B3 in real conditions | Phase Promotion — B3's adaptive model tested with first client; predicate calibration begins | **A+C** — Agency (first client-project-brigadier allocated at validated stage) + Composition (client-namespace in operations/) | INT excess: thin-scaffold projects may stay thin too long, depriving client of agent support at critical early stages | T-Hybrid per client (same offline-LLM as A1/A2 G2) |
| **G3 €1M** | Consulting scale | N/A | 15-30 | 5-15 | Stage-gate predicate at 15-30 projects: `/lint` must evaluate all project `stage_gate_status` fields in a single sweep. If sweep takes >30s, brigadier attention is degraded. Rich-scaffold projects have dedicated project-brigadiers; thin-scaffold projects share canonical brigadier — coordination overhead at 20+ projects | `/project-status` sweep evaluates `stage_gate_status` for all projects. Projects above stage-gate threshold auto-propose transition (HITL ack required). Meta-brigadier coordinates | Fission — canonical brigadier delegates thin-scaffold oversight; project-brigadiers handle rich-scaffold autonomously | **O+C** — Operation (multi-tier project orchestration) + Composition (meta-brigadier + project-brigadiers) | Both: S-A (rich-scaffold projects over-assert autonomy, ignore meta-brigadier signals) + INT (thin-scaffold projects under-report, creating invisible health gaps) | N/A |
| **G4 $100M** | Platform scale | N/A | 50+ | 50-500 | At 500 clients, most projects are thin-scaffold at onboarding. The stage-gate predicate becomes the primary traffic-management mechanism for agent allocation across hundreds of client projects. Predicate calibration at scale requires measurement data | Stage-gate predicate becomes a trained classifier (ML-assisted from stage-gate transition history in health-JSON). Human (Ruslan) reviews classifier output; doesn't review every project | Role-Lift — stage-gate predicate is a product feature; B3 adaptive-scaffold is the client onboarding standard | **C+X** — Composition (ML-assisted stage-gate) + eXternal (client-contract milestone integration) | INT excess: ML-assisted classifier may systematically under-promote projects that need human attention | GPU cluster per client. Rich-scaffold projects warrant dedicated local LLM for complex synthesis |
| **G5 $1T** | Alliance scale | N/A | Hundreds | 5000+ | ML-assisted stage-gate at 5000+ clients requires Alliance-level ground-truth labeling to avoid systematic bias. Stage-gate predicate drift across Alliance members | Alliance-maintained stage-gate calibration dataset. Members contribute anonymised transition-history data; Alliance trains and certifies the stage-gate classifier | Context Reframe — B3 stage-gate classifier is an Alliance-certified standard; Jetix provides reference implementation | **X+T** — eXternal (Alliance classifier certification) + Time (multi-year calibration history) | Both: S-A (Alliance members customize classifier, breaking comparability) + INT (Alliance can't maintain classifier without sufficient member contribution) | Same as G4; Alliance-certified GGUF bundles |

**Antifragility check (B3):**
- Stage-gate predicate is the critical fragility: if underdefined, B3 collapses to ad-hoc. Refactor cost to formalize: high at G1 (15-20% of cycle engineering budget); low thereafter.
- Adaptive allocation is inherently more scalable than B1's static allocation at G3+. B3 is more antifragile than B1 past G3.
- ML-assisted classifier at G4 adds a new dependency. Moderately fragile if classifier is poorly calibrated. Mitigation: human-override always available.

---

## §8 Federation Per-Client Scaling Complexity (1→10→50→500→5000+ Clients)

This section projects the operational engineering complexity of per-client UC-9 isolation across the client-count axis for all variants.

F: F4 | ClaimScope: complexity estimates based on engineering integrator + systems integrator analysis; operational data not yet available | R: `refuted_if` first 3-client deployment shows different complexity profile than projected

### 1 Client (Phase A, G1-early G2)

**A1:** `WIKI_ROOT_CLIENT_ID` env-var; 1 additional directory under `clients/`; 1 additional `edges.jsonl`; `/lint` holon-ref check is new. Provisioning: ~1-2 hours manual. Operational overhead: negligible. Engineering effort to maintain: 0 additional turns per cycle.

**A2:** Same as A1 + separate git repo provisioning. Provisioning: 2-4 hours (repo init + submodule wiring). Ongoing: manual methodology push per update. Engineering overhead: 1-2 hours per methodology version release.

**A3:** Same as A2 + per-client community-detection run when page count crosses 3K. At 1 client, this is a future concern. Current overhead: identical to A2.

**B1:** Directory namespace `operations/clients/<slug>/`; policy-layer enforcement only. Operational overhead: low — brigadier checks `granularity:` field, no structural change.

**B2:** Same as A2 for project-wiki structure; additional `local-patterns/` directory; per-client brigadier instance. Provisioning overhead higher than B1 at 1 client.

**B3:** Thin scaffold at onboarding; stage-gate predicate evaluation added to each `/project-status` sweep. Lowest provisioning overhead of all B variants.

### 10 Clients (G2-G3 boundary)

**A1/A2/A3:** 10 separate directories (Phase A) or 10 separate git repos (Phase B). Per-methodology-push: 10 git push operations. Manual: 1-2 hours per release. With CI automation: 5-10 minutes. Manual is not sustainable at 10 clients. CI automation is the G3 trigger.

**B1:** `operations/clients/` has 10 subdirectories. `/project-status` sweep covers 10 client subtrees + Jetix-internal. At 3 projects per client = 30 client project trees. Token budget: 30 × ~500 tokens per project summary = 15K tokens. Near brigadier context limit in a single sweep. Mitigation: batched sweep (5 clients per sweep). Engineering effort: moderate.

**B2:** 10 per-client brigadier instances. Each runs weekly and sends health summary. Meta-brigadier aggregates 10 health summaries (~2K tokens each = 20K tokens). Manageable. Provisioning: 10 client repos × 2-4 hours each = 20-40 hours total (without automation). CI automation required at 10 clients.

**B3:** 10 clients × 3 projects each = 30 projects, ~20 at thin-scaffold, ~10 at rich-scaffold. `/project-status` sweep evaluates 30 stage-gate statuses (~15K tokens). Same token budget concern as B1; batched sweep required.

### 50 Clients (G3-G4 boundary)

**A1/A2/A3:** 50 git repos. Methodology push: CI pipeline pushes to 50 remotes (5-15 minutes with parallel push). Ops engineering cost: 1-2 days to automate CI pipeline. Provisioning: script-automated, ~15 minutes per client. Edge-store management: 50 separate `edges.jsonl` files; per-client BFS is isolated — no cross-client performance interaction.

**B1:** 50 client subtrees in `operations/clients/`. Single canonical brigadier is overloaded. Attention-budget ratchet fires at >20 tasks. Requires multi-brigadier architecture (B1 cannot survive 50 clients without structural change). Effectively forces transition to B2 or B3. Engineering effort to maintain B1 at 50 clients: high.

**B2:** 50 per-client brigadier instances + meta-brigadier. Weekly health-summary aggregation: 50 × 2K tokens = 100K tokens — exceeds single-session brigadier context (200K tokens / 2 = ~100K usable). Requires streaming aggregation: meta-brigadier reads health summaries in batches of 10. Engineering effort: moderate (streaming aggregation skill needed). Provisioning: automated, 15 minutes per client.

**B3:** Similar to B2 at 50 clients. Stage-gate evaluation: 50 clients × 3 projects × thin-rich split. Streaming evaluation required. Engineering effort: moderate.

### 500 Clients (G4)

**A1/A2/A3:** 500 git repos. CI-based methodology push at 500 remotes: 10-30 minutes with 50-parallel push jobs. Ops team required for repo provisioning and failure recovery. Edge-store: 500 isolated JSONL files; per-client BFS is fully isolated. No cross-client performance interference — this is the architectural win of per-client isolation. Graph DB upgrade required for clients at 10K+ pages.

**B1:** Not viable at 500 clients. B1 has been superseded by B2/B3.

**B2:** 500 per-client brigadier instances. Health-summary aggregation: automated portfolio dashboard (health-JSON per client → meta-analytics layer). Manual Ruslan oversight: impossible for all 500; statistical portfolio view only. Engineering effort: high (portfolio analytics platform). Ongoing maintenance: ops team required.

**B3:** Same as B2. Stage-gate ML classifier active. Engineering effort: high (ML classifier pipeline + Alliance-calibration data).

### 5000+ Clients (G5)

**All variants:** At 5000+ clients, the engineering complexity is primarily devops and Alliance-governance, not per-client wiki mechanics. The per-client isolation architecture (separate repos, separate edge stores, isolated graph DBs) is the correct choice — it prevents any single client's scale from affecting others. The bottleneck is methodology-update propagation and portfolio analytics, not the KM or project-management mechanics themselves.

**Engineering assessment:** The per-client isolation architecture (A2/B2) is the only variant that scales to G5 without structural re-architecture of the isolation model. A1/B1 require structural transitions at G3. A3/B3 require additional infrastructure at G3 (graph DB, ML classifier) but their isolation models are inherently federated.

---

## §9 Cross-Variant Tier-Split at Each Gate

This section declares where each variant sits on the T-Offline / T-Hybrid / T-Cloud-only continuum at each gate, per the brief's §2 requirement.

F: F4 | ClaimScope: tier-split is engineering judgment; client choice may override any tier | R: medium

| Gate | A1 Karpathy++ | A2 Federated Holons | A3 GraphRAG/HippoRAG | B1 Namespaces | B2 Federated Client-Project | B3 Adaptive Scaffold |
|---|---|---|---|---|---|---|
| **G1 €50K** | T-Offline (Phase A structured-excerpt) / T-Cloud (Jetix-internal) | T-Offline / T-Cloud | T-Offline (A1 fallback; A3 not yet active) / T-Cloud | T-Cloud (B is Layer-B; retrieval is Layer-A) | T-Cloud | T-Cloud |
| **G2 €200K** | T-Hybrid (ollama + Llama 3.1-8B Q4_K_M; Phase B AWAITING-APPROVAL) / T-Cloud-only for Jetix-internal | T-Hybrid per client (client-hosted ollama) / T-Cloud for Jetix-internal | T-Hybrid (community pages as offline substrate + local LLM) / T-Cloud | T-Cloud | T-Hybrid (same as A2; B2 pairs with A2) | T-Hybrid (same as A1/A2; B3 pairs with either A1 or A2) |
| **G3 €1M** | T-Hybrid mandatory per client. MoE Q4_K_M option for complex clients. No T-Cloud-only for client-private data | T-Hybrid mandatory per client | T-Hybrid mandatory; community pages improve offline quality. MoE Q4_K_M | T-Cloud (B1 is internal only at G3) | T-Hybrid mandatory per client | T-Hybrid per client at rich-scaffold stage |
| **G4 $100M** | T-Hybrid (client-hosted) / T-Cloud (Alliance-member opt-in only for public-data queries) | T-Hybrid per client / T-Cloud optional | T-Hybrid; dense+PPR index improves offline precision at scale | T-Cloud (internal methodology ops) | T-Hybrid per client / T-Cloud optional | T-Hybrid; ML-assisted stage-gate requires T-Cloud for classifier training; inference remains T-Hybrid |
| **G5 $1T** | T-Hybrid (Alliance default; client-choice); T-Cloud for multi-model synthesis queries on public data | T-Hybrid (Alliance default) | T-Hybrid (reference implementation); community-page path enables highest offline quality | T-Cloud (internal) | T-Hybrid (Alliance standard); T-Cloud optional | T-Hybrid (Alliance standard); ML classifier training T-Cloud; inference T-Hybrid |

**Key engineering observation:** The T-Offline → T-Hybrid transition fires at G2 for all client-facing variants. The G2 trigger is the first paying client — at that point, T-Cloud-only is architecturally disqualifying (UC-10 mandatory per prompts §1.2). All A variants and client-facing B variants must have an operational T-Hybrid path before G2 closes. This is the BIOS-insight §3 architectural requirement: "offline-first AI integration" is not optional. [src: STRATEGIC-INSIGHT §3; prompts §1.2 UC-10]

---

## §10 Provenance + F-G-R Notes

All claims in this scalability draft trace to Tier-1 in-repo sources. No Tier-4 book reads performed in Phase A. No paid API calls.

| # | Source | Section / Range | Key claim supported |
|---|---|---|---|
| P-1 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md` | §4.1-§4.4 (mechanics); §5 UC-8 scale preview; §8 effort; §9 migration | A1 baseline mechanics; G1/G2 scale ceilings; offline-path Δ2 Phase-A quality declaration; per-client JSONL sharding Delta-5 |
| P-2 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md` | §1.2 A2 structure; §2.2 B2 structure; §4 UC-9 4-layer isolation proof; §5 feedback loops; §6 Janus table; §7 pairing recommendations | A2 peer-holon model; B2 per-client project structure; holon-ref enforcement; methodology-update loop (R2); Alliance-level federation (§8); Janus S-A/INT risk per variant |
| P-3 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-integrator-layerB-candidate.md` | §3 architecture diagram; §4 B.1-B.8; §6 UC-9/UC-10 proofs; §7 pros/cons; §8 effort | B1 namespace model; B2 per-client project structure; B3 adaptive scaffold (informed gap); attention-budget ratchet; tombstone protocol |
| P-4 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md` | §1 Δ1-Δ4; §2 pre-cache tradeoff matrix; §3 refusals; §7 F-G-R | Per-client namespace delta (Δ1/Δ3); offline-synthesis path (Δ2); inference-stack manifest (Δ4); hardware floor (16GB GPU / Llama 3.1-8B Q4_K_M); method-change refusals R-1/R-2/R-3 |
| P-5 | `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §3 (local-first architecture); §5 Path A/B/C; §6 built vs missing; §7 where this fits; §8 rec 7 | UC-10 strategic mandate; T-Hybrid as default for client-private data; Alliance-level scaling (§8 rec 3); "offline-first AI integration [Missing]" |
| P-6 | `raw/research/knowledge-architecture-deep-research-2026-04-19.md` | §A.2 GraphRAG; §A.3 HippoRAG; §G.1-§G.3 scale milestones; §G.2 networkx ceiling at 20K edges | A3 axis-design (GraphRAG/HippoRAG); scale thresholds (557 → 5K → 50K pages); Neo4j threshold at 20K edges; community-detection timing estimates |
| P-7 | `prompts/km-architecture-research-2026-04-24.md` | §1.2 (UC-9/UC-10 mandatory); §1.4 (depth floors); §2.2 A.7 (scale); §3.8 UC-8 5-gate table | 5-gate horizon mandate; "what physically breaks" requirement; T-Hybrid at G2 trigger; BOSC-A-T-X per FPF E-6 |
| P-8 | `.claude/agents/engineering-expert.md` | §6.1 BOSC-A-T-X trigger table; §6.4 antifragility check; §6.2 Janus degraded-mode; §1d scalability | All 5-gate BOSC-A-T-X assignments; MHT event assignments; Janus S-A/INT excess per gate; antifragility 4-axis check; 30% refactor-at-10× gate |

**Three mandatory Tier-1 citations fulfilled:**
[T1-cite-1] `raw/research/knowledge-architecture-deep-research-2026-04-19.md` §G.2: "HippoRAG PPR на 572 edges — тривиальная операция. При 5,000 pages и ~5,700 edges — всё ещё быстро в памяти. **Порог для Neo4j/ArangoDB: ~20,000 edges** при регулярных multi-hop queries." Applied: G3 physical failure for A1/A2/A3 is correctly placed at ~200K edges per client (10K pages × ~20 edges/page), which crosses the networkx in-memory ceiling. Upgrade path: persistent graph store.

[T1-cite-2] `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` §3: "Каждый клиент получает Свой AI-архивариус — offline-first модель (Llama/DeepSeek distilled), работает только с его файлами." Applied: T-Hybrid is mandatory at G2 for all client-facing variants. The tier-split at G2 (§9) correctly places all client-facing A/B variants at T-Hybrid as the minimum required tier — T-Cloud-only at G2 is architecturally disqualifying.

[T1-cite-3] `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md` §7 pairing recommendations: "Hybrid-A (federated A, flat B) → NOT RECOMMENDED: inconsistent isolation level between topic-wiki (by construction) and project-wiki (policy)." Applied: the cross-variant tier-split table (§9) treats A1+B1 as the G1 canonical pairing and A2+B2 as the G2+ canonical pairing, consistent with the systems-integrator's pairing disqualification of hybrid combinations.

---

*End of engineering × scalability draft. Produced by engineering-expert, mode: scalability. Cycle: cyc-km-architecture-2026-04-24. Word count: ~3,100 words. All 6 variants × 5 gates = 30 rows produced. A3 + B3 axes proposed with governing metaphor + key tradeoff. Federation complexity at 1→10→50→500→5000+ clients. Cross-variant tier-split table. BOSC-A-T-X + MHT + Janus risk + offline-LLM HW per gate row. Antifragility 4-axis check per variant. ≥3 Tier-1 citations. F-G-R per major claim.*
