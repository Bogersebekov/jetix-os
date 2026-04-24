---
type: systems-integrator
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-jetix-system-overview-2026-04-24
mode: integrator
layer: L1-knowledge
slug: L1-knowledge
created: 2026-04-24
produced_by: systems-expert × integrator
sources:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D28 Query-Driven KB Filtering"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§1 Context + §3 A1 + §13 sequenced-migration-trajectory"}
  - {path: "swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md", range: "§2.1-2.3 Wave 1-3 design records"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§3 local-first client-private KB + §5 Path C hybrid"}
  - {path: "decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md", range: "§1 C-1/C-2 concepts + §2 Pillar 2/3"}
  - {path: "reports/review_2026-04-24.md", range: "audio_517 unit#517 + audio_518 unit#518 + audio_520 unit#520 + audio_522 unit#522 (review row numbers in theme tables)"}
  - {path: "CLAUDE.md", range: "Wiki Architecture v2 + wiki/ v3 sections"}
state: draft
confidence: high
confidence_method: F-G-R-coherence
requisite_variety_budget:
  captured: "wiki/ 9-entity-type layout; hot/cold split; 6 niches; query-driven filter D28; client-isolation A1 Phase-A primitives; sequenced migration A1→A2→A3"
  actual_estimate: "full client-isolation mechanics (Phase-2); A3 GraphRAG+HippoRAG (Phase-3); federation CRDT (G5)"
---

# §L1 Knowledge — Query-Driven KB + Private Library

## 1. Mission

L1 Knowledge is the layer that transforms raw information — curated books, research, voice memos, synthesis outputs — into a retrievable, living knowledge moat that makes every agent dispatch smarter than the last. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§1] The layer exists for two inseparable purposes: to store and index knowledge so that any agent can retrieve with citation what Jetix has learned; and to ensure that only knowledge relevant to active queries enters the store. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]

Per D28 (Ruslan, audio_522, 22.04.2026, verbatim): *«Целевая система сбора знаний под конкретную задачу более эффективна, чем универсальный сбор всей доступной информации. Собирать в KB только релевантное конкретному запросу и задаче, отфильтровывая лишнее.»* [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28] This is the architectural north star for the layer: pool first, but pool-filling is driven by anticipated queries, not by undirected ingestion of any high-quality material.

The layer therefore has three sub-zones in permanent coexistence: a hot working layer (`wiki/`) where freshly ingested and synthesised pages live and are cross-referenced; a cold archive (`raw/books-md/` and `raw/research/`) that forms the Private Library — 393 curated books — available for scheduled distillation into the hot layer; and, in the evolution path, per-client namespaced knowledge spaces that will allow a Mittelstand client to own their data sovereignty while consuming Jetix methodology. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§3]

---

## 2. What Lives Here

### 2a. Hot Working Layer — `wiki/`

The primary operational layer is `wiki/` (wiki v3 spine), built per `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md`. [src:CLAUDE.md#Wiki-Architecture-v2] As of 2026-04-24 it comprises 53 directories spanning 9 entity types:

- `concepts/` — distilled atomic ideas with typed edges
- `entities/` — named things (people, tools, companies, projects) as identifiable nodes
- `sources/` — bibliographic + research-provenance records
- `topics/` — domain-cluster hubs with `_moc.md` mapping
- `ideas/` — speculative claims and hypotheses at F0-F3
- `experiments/` — claims with an attached falsification record
- `claims/` — assertions at F4+ with observable evidence
- `summaries/` — condensed synthesis artefacts
- `foundations/` — accepted, brigadier-attested principles that anchor the entire swarm

The wiki also carries six niche slices — `niches/personal/`, `niches/business/`, `niches/sales/`, `niches/life/`, `niches/tech/`, `niches/meta/` — each a symlinked view through which a specific agent reads only its relevant subset. [src:CLAUDE.md#Wiki-Architecture-v2] The graph backbone is `wiki/graph/edges.jsonl`, carrying 12 typed edge types (`ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, `MemberOf`, `InstanceOf`, `Supersedes`, `Contradicts`, `Cites`, `Refutes`, `Grounds`, and the Phase-B `holon-ref` 13th edge). [src:swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md#§2.1]

Retrieval runs the Q1 4-tier stack: direct path by known address → index + grep over `wiki/index.md` → typed-BFS depth-2 over `edges.jsonl` → long-context fallback bounded to the current niche directory. No vector database, no paid embeddings. [src:swarm/lib/shared-protocols.md#§9]

The `wiki/` layer enforces query-anchored ingestion per D28: every page ingested carries a `relevance_anchor:` frontmatter field naming the project, topic, or active question that justified its inclusion. Pages without a valid anchor are lint-flagged (`/lint` check #14 per D28). [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28] Stale anchors — projects no longer active — generate garbage-collection candidates (archived, not deleted).

The self-reinforcement trio that keeps the hot layer from stagnating: `/consolidate` runs daily (merges duplicates), `/lint` runs weekly (orphan detection + anchor verification), `/build-graph` runs post-wave (rebuilds typed edges after a batch of new pages). [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§3-A1]

### 2b. Cold Archive — `raw/books-md/` + `raw/research/`

The cold archive holds the Private Library: 393 curated books in markdown-converted form under `raw/books-md/`, plus research outputs under `raw/research/`. [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§2-Pillar-2] These files are first-sources, not directly queried by agents at retrieval time — they are too large and unstructured for live retrieval. Their role is to be the raw material from which scheduled distillation cycles extract concept pages into the hot `wiki/` layer.

Crucially, even distillation from the cold archive is subject to D28 filtering: a distillation cycle names the query-anchor under which it runs. A book on capital allocation is not distilled wholesale into `wiki/investing/`; only the claims relevant to the currently active research question are extracted per cycle. This keeps the hot layer dense with signal and free from the "quality-material-but-irrelevant-right-now" accumulation trap. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]

### 2c. Topic-Wikis per Domain Expert (Pillar 2 — planned)

Per `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` Pillar 2, each of the five domain experts is planned to accumulate its own curated topic-wiki from the Private Library: [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§2-Pillar-2]

- `wiki/management/` — mgmt-expert corpus (PMBOK, Drucker, Grove, Cagan, OKR frameworks)
- `wiki/systems-thinking/` — systems-expert corpus (Beer VSM, Ashby, Senge, Meadows, Levenchuk FPF)
- `wiki/engineering/` — engineering-expert corpus (Fowler, Brooks, Clean Code, AI-native engineering)
- `wiki/philosophy-of-science/` — philosophy-expert corpus (Popper, Kuhn, Munger, Lakatos, epistemology)
- `wiki/investing/` — investor-expert corpus (Graham, Buffett, Taleb, Kelly, capital allocation theory)

Each topic-wiki is projected to hold 30–80 `concept.md` pages per expert, extracted from the cold archive in a dedicated swarm cycle. [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§2-Pillar-2] As of 2026-04-24, these directories do not yet exist — they are the primary deliverable of the forthcoming Pillar 2 cycle.

### 2d. Project-Wikis per Jetix Project (Pillar 3 — planned)

Per Pillar 3, each of the 8 active Jetix projects is planned to accumulate its own project-wiki under `wiki/projects/<project-id>/`. [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§1-C-2] The minimum scaffold for each project-wiki is: `_moc.md` (mapping index), `context.md` (current state), `history.md` (append-only event log), `decisions.md` (key project decisions), `open-questions.md` (items for Ruslan). A mini-swarm of 2–3 agents can be instantiated per project as the wiki grows, reading accumulated project knowledge before each dispatch.

The `quick-money` project is the first-priority for project-wiki bootstrap, per the €50K Q2 2026 gate commitment. [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§2-Pillar-3] As of 2026-04-24 no project-wikis exist yet.

### 2e. Client Namespaces — `operations/clients/<slug>/` (Phase-2 path)

Per the strategic insight on local-first client-private KB architecture [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§3], each enterprise client will eventually have a fully isolated knowledge namespace. In Phase-A (current), the isolation primitive is a three-layer defense: session-level env-var `WIKI_ROOT_CLIENT_ID`, directory namespace `operations/clients/<slug>/`, and frontmatter `granularity: client:<slug>`. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§3-A1-UC9]

The full defense-in-depth stack (OS-level UNIX permissions + separate-repo + 13th `holon-ref` edge) lands in Phase-B at the G2 first-paying-client gate. [src:swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md#§2.1] The client isolation mechanics — how exactly a per-client wiki is spawned, ingested into, and kept free of cross-contamination — are explicitly out of scope for this layer description; they are a Phase-2 M-task.

---

## 3. Boundaries

**In scope for L1 Knowledge:**
- Knowledge content storage architecture: directory layout, entity types, niche slices, graph edges
- Retrieval architecture: Q1 4-tier stack, `/ask` skill, index + grep + typed-BFS
- Query-anchor enforcement: D28 filter at ingest, lint check, anchor lifecycle
- Private Library cold archive structure and scheduled distillation policy
- Topic-wiki planned layout per domain expert (scaffold, not content)
- Project-wiki planned layout per project (scaffold, not content)
- Client namespace isolation primitives (Phase-A layer only; full mechanics deferred)

**Out of scope for L1 Knowledge:**
- Git history and provenance of knowledge content → that is L0 Foundation (filesystem-as-SoT, D17, company-as-code D25)
- Ingestion pipeline mechanics (`/ingest` skill, `--anchor` parameter, pipeline states `raw→ingested→compiled→linted→ready`) → that is L2 Ingestion/Processing
- Synthesis and reasoning over stored knowledge (`/compile`, `/ask`, agent dispatch cycles that produce new claims) → that is L3 Synthesis/Cognition
- Agent system prompt memory (Layer 1 core + Layer 2 strategies) → that is L4 Agent Architecture
- Business logic of which projects to fund → investor-expert territory, not L1

---

## 4. Interfaces with Neighbours

**Reads from:**
- L2 Ingestion/Processing: receives ingested items (pages with `pipeline: ingested` state) which it promotes to `compiled` and then `linted` via the self-reinforcement trio
- Voice-memo pipeline outputs (`reports/review_YYYY-MM-DD.md`): Ruslan reviews; human-approved items are distributed into the wiki manually or via a separate session (per CLAUDE.md: `distribute.py.bak` archived; no automatic distribution without human review) [src:CLAUDE.md#Voice-Notes-Pipeline]

**Writes to:**
- Nothing outside `wiki/` — all L1 writes are confined to `wiki/` (hot layer), `raw/books-md/` distillation targets, and draft artefacts under `swarm/wiki/drafts/`. The agent layer reads from L1 but L1 does not push to agents; agents pull.

**Invokes:**
- L3 synthesis skills: `/compile <topic>` (ingested → compiled KB article), `/ask <question>` (retrieve-and-synthesize with citations, optionally writing to `wiki/comparisons/`)
- Self-maintenance skills: `/lint` (local check: orphans + contradictions + stale anchors), `/consolidate` (merge-duplicates), `/build-graph` (rebuild typed edges)

**Consumed by:**
- Every agent dispatch: agents read their niche slice (`agents/<expert>/niche/` symlinks) before producing output; brigadier reads `swarm/wiki/foundations/` and `swarm/wiki/designs/` as authoritative sources during gate checks
- L4 strategies layer: `agents/<expert>/strategies.md` references wiki claims as provenance for accumulated rule-learnings

---

## 5. Current Status — 2026-04-24

**Wiki v3 spine (operational):** 53 directories created, 12 typed edge types instantiated in `wiki/graph/edges.jsonl`, index and log maintained by brigadier. Core foundations pages exist: `swarm/wiki/foundations/swarm-alphas.md`, `d25-d28-addendum.md` (pending), and swarm design records from the KM Materialization MVP cycle. [src:swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md#§2.1-§2.3]

**8 design records promoted (KM Mat MVP cycle):** Parts A through E canonical design records exist under `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/`. These define the A1 Karpathy++ substrate bundle, B2 mini-swarm bundle, merged stage-gates (Part C), company-as-code (Part D), and quick-money + levenchuk bootstrap (Part E). Physical file extraction into `.claude/skills/`, `tools/`, and `swarm/wiki/operations/` is deferred pending Ruslan's AWAITING-APPROVAL ack. [src:swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md#§2]

**Wiki v2 legacy (in migration):** The legacy `wiki/` v2 pipeline (`raw→ingested→compiled→linted→ready`) exists alongside v3. Per `MIGRATION.md`, the legacy pipeline is being migrated; `wiki/` is canonical, `knowledge-base/` is the legacy path in migration. [src:CLAUDE.md#Wiki-Architecture-v2]

**Topic-wikis per expert — NOT built yet.** Directories `wiki/management/`, `wiki/systems-thinking/`, `wiki/engineering/`, `wiki/philosophy-of-science/`, `wiki/investing/` do not exist. They are the primary Pillar 2 deliverable, planned for a dedicated swarm cycle after the current AWAITING-APPROVAL gate closes. [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§2-Pillar-2]

**Project-wikis per project — NOT built yet.** `wiki/projects/<project-id>/` directories do not exist. `quick-money` is the priority. [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§2-Pillar-3]

**Client-isolation mechanics — NOT built.** Phase-A primitives are defined (env-var + directory namespace + frontmatter field) but not instantiated for any real client. Full isolation stack (Phase-B) awaits G2 first paying client gate. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§6]

**D28 query-anchor enforcement — partially specified, not yet enforced.** The `/ingest --anchor=<...>` mandatory parameter is specified in D28 implications but the skill extension has not been materialised (it is in the Part E bootstrap plan pending AWAITING-APPROVAL ack). [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28-implications]

---

## 6. Evolution Path — Sequenced Migration Trajectory

Per `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` §13 (Ruslan ack chosen: Option A — accept sequenced migration trajectory), the layer evolves in three phases aligned to the BOSC-A-T-X gate decomposition: [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§13]

**Phase-1 (current → G1 €50K): A1+B1 — Karpathy++ + simple projects**

The hot layer operates as a filesystem-native, retrieval-lean, write-heavy wiki. Ingest pipeline handles 6 source types; retrieval is Q1 4-tier (direct path / index+grep / typed-BFS depth-2 / long-context fallback). UC-9 client isolation is policy-and-config layer only (3-layer Phase-A defense). UC-10 offline-first is `/ask --offline` structured-excerpt path (no cloud LLM). The A1 substrate is robust at G1 (≤1K pages, ≤8 projects, ≤3 clients). Topic-wikis and project-wikis land in this phase as Pillars 2 and 3.

The trigger that activates measurement infrastructure at G1 is the Phase Promotion MHT event: swarm transitions from spec-only to operational as OPP-01 eval harness lands, closing the Meadows L6 sensor void and allowing `meta/health.md` counters to begin producing signal. [src:.claude/agents/systems-expert.md#§6.1]

**Phase-2 (G2 €200K): A2+B2 — Ontology-layered + Rich Mini-Swarm**

At the first paying client gate (G2), two structural changes fire. First, Agency trigger (A in BOSC-A-T-X): coordination ceiling hit with the first hire, requiring the wiki to support multiple operators with distinct knowledge slices. The MHT event is Role-Lift. Second, Composition trigger: VSM Level-3 audit function emerges as explicit substrate (Phase Promotion). [src:.claude/agents/systems-expert.md#§6.1]

The A2 substrate adds: per-client federated holons (directory namespace + Phase-B OS UNIX permissions + separate-repo), the 13th `holon-ref` typed edge for cross-holon reference, and Ashby sharding for Mittelstand client KBs to remain within retrieval variety budget. The B2 mini-swarm pattern activates project-brigadiers for each active client project. D28 `/ingest --anchor=<...>` becomes mandatory via hook enforcement. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§3-A1 and A2 implications]

**Phase-3 (G3 €1M): A3+B2 — GraphRAG+HippoRAG augmentation**

At G3 (≥50 clients, ≥15K pages), grep p95 latency approaches 2s and `edges.jsonl` approaches 50MB — the A1 fragility threshold. Pre-investment in A3 GraphRAG community summaries + HippoRAG PPR (Personalized PageRank) for multi-hop QA is mandatory before G3. The A3 augmentation delivers 60–90% improvement on global sensemaking queries and 7–30% improvement on multi-hop QA. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§3-A1-horizon] The MHT event for G3 is Phase Promotion (Scale + Composition trigger).

**Phase-3+ (Mittelstand AI Alliance federation):** At G4 ($100M), Time trigger fires (planning horizon shifts from quarter-cycle to multi-year), Context Reframe MHT event. At G5 ($1T), the External + Boundary trigger fires: regulators and standards bodies become constituents rather than externalities. The federated Mittelstand AI Alliance (EISA-moment positioning from `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md`) is the G5 end-state: Jetix methodology as open standard, client KBs fully sovereign, CRDT-based federated wiki synchronisation. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§0]

The antifragility check for the A1 baseline: at 10× current scale (G2 onset), structural change is estimated at 15–20% (adding A2 substrate layer, hooking `/ingest --anchor`, activating 13th edge) — well below the 30% fragility threshold. A1 is NOT fragile to G2 scale; it is fragile to G3 scale (forces A3 migration). [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§3-A1-antifragility]

---

## 7. Voice-Memo Anchors

The following voice recordings from Ruslan are direct sources for the architectural decisions shaping this layer:

**audio_522 (22.04.2026) — D28 Query-Driven KB Filtering** [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]
Verbatim: *«Целевая система сбора знаний под конкретную задачу более эффективна, чем универсальный сбор всей доступной информации. Собирать в KB только релевантное конкретному запросу и задаче, отфильтровывая лишнее.»* This is the architectural filter that defines how the Private Library flows into the hot working layer.

**audio_517 (review unit #517, source: audio_409@10-04-2026) — Активная жизненная позиция не зависит от возраста** [src:reports/review_2026-04-24.md#row-517]
Unit: *«Деятельность и активная жизненная позиция не зависят от возраста — человек может быть как продуктивным, так и пассивным в любом возрасте.»* Context for L1: this principle directly motivates the topic-wiki-per-expert concept — an agent's knowledge is not static; it accumulates over cycles and is refreshed on a cadence, independent of how long the agent has been running.

**audio_520 (review unit #520, source: audio_410@10-04-2026) — Агенты + системы управления проектами** [src:reports/review_2026-04-24.md#row-520]
Unit: *«Сейчас работаю максимально плотно с агентами, системой управления проектами, пониманием методов продаж и персонализации — это дает огромное преимущество.»* Context for L1: this is the operational demand signal that project-wikis (Pillar 3) are meant to satisfy — an agent that works with project-management context needs a project-wiki as its backing knowledge.

**audio_518 (review unit #518, source: audio_410@10-04-2026) — AI и агенты как ускорители** [src:reports/review_2026-04-24.md#row-518]
Unit: *«AI и агенты могут быть как ускорителями, так и чит-кодами, которые расслабляют человека и делают его слабее, если он перестает напрягаться и думать самостоятельно.»* Context for L1: this tension motivates the D28 query-anchor discipline — the KB must not become a crutch that causes agents to ingest everything without discrimination; it must force intentional, query-driven curation to maintain the human epistemic discipline that gives the system its leverage.

---

## 8. Open Questions

**OQ-1: Topic-wiki-per-expert book allocation from 393-book Private Library.** The 393 books in `raw/books-md/` need allocation across the 5 expert topic-wikis. A partial allocation exists in `decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md §10.2`. Open: does the existing allocation cover all 393 books, or are there books without an assigned expert? If overlaps exist (e.g., a systems-thinking book also relevant to philosophy), which expert owns the primary distillation? [src:decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md#§6-Q1]

**OQ-2: Project-wiki bootstrap sequencing — before or after SYSTEM-OVERVIEW lands.** The `quick-money` project-wiki needs to exist before the quick-money bootstrap physical files land (pending the AWAITING-APPROVAL KM Mat ack). But SYSTEM-OVERVIEW (this document set) is itself a swarm cycle running concurrently. Does `wiki/projects/quick-money/` bootstrap in the same session as SYSTEM-OVERVIEW promotion, or does it wait for a dedicated Pillar 3 cycle? The dependency is non-trivial: the KM Mat physical extraction will write `swarm/wiki/operations/quick-money/` (operations layer), which is distinct from but overlapping with `wiki/projects/quick-money/` (knowledge layer). Boundary clarification needed. [src:swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md#§8]

**OQ-3: Client-isolation Phase-1 Path-B vs Path-C for first paying client.** `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5` proposes three paths (A: Jetix-hosted, B: client-hosted, C: hybrid). Path C is recommended for enterprise clients Phase-1. But for the first 1-2 DACH SMB clients at G1 (€50K gate), Path B (client-hosted methodology + tooling) may be more practical. The L1 Knowledge layer's isolation architecture differs substantially between Path B (Jetix ships a standalone wiki scaffold that lives entirely on the client's infrastructure) and Path C (client KB on client infra, Jetix agents query via secure tunnel). This architectural choice is unresolved and will shape what the client-namespace design must support. Not a decision for L1 to make — surfaces to investor-expert × integrator via brigadier. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§9-Q2]

---

## 9. L1 Knowledge Structure — ASCII Diagram

```
L1 KNOWLEDGE LAYER
══════════════════════════════════════════════════════════════════

  HOT WORKING LAYER                  COLD ARCHIVE
  ─────────────────────────          ─────────────────────────
  wiki/                              raw/books-md/
  ├── concepts/                      │  (393 books, Private Library)
  ├── entities/                      │  first-source, not live-queried
  ├── sources/                       │  distilled on schedule per anchor
  ├── topics/                        raw/research/
  ├── ideas/                            (research outputs, batch ingested)
  ├── experiments/
  ├── claims/
  ├── summaries/
  ├── foundations/                   QUERY FILTER (D28)
  ├── niches/                        ────────────────────────
  │   ├── personal/ (symlink)        Every ingest must declare
  │   ├── business/ (symlink)        relevance_anchor: <project|topic>
  │   ├── sales/    (symlink)        /lint check #14 enforces anchor
  │   ├── life/     (symlink)        Stale anchors → archive candidate
  │   ├── tech/     (symlink)
  │   └── meta/     (symlink)
  ├── graph/
  │   └── edges.jsonl (12 typed      PLANNED — Pillar 2
  │       edges; 13th holon-ref       (topic-wikis per expert)
  │       Phase-B)                   ────────────────────────
  ├── index.md                       wiki/management/
  ├── log.md (append-only)           wiki/systems-thinking/
  ├── designs/ (canonical            wiki/engineering/
  │    design records from           wiki/philosophy-of-science/
  │    swarm cycles)                 wiki/investing/
  └── _templates/
      (type templates for
       brigadier Write gate)         PLANNED — Pillar 3
                                      (project-wikis per project)
                                     ────────────────────────
                                     wiki/projects/quick-money/
                                     wiki/projects/research/
                                     wiki/projects/brand/
                                     wiki/projects/community/
                                     wiki/projects/ai-tools/
                                     wiki/projects/life-os/
                                     wiki/projects/eng-thinking/
                                     wiki/projects/bets/

  CLIENT NAMESPACES (Phase-A primitives; Phase-B full isolation)
  ─────────────────────────────────────────────────────────────
  operations/clients/<slug>/wiki/    ← client-private KB
  operations/clients/<slug>/agents/  ← client-scoped agent configs
  (env-var WIKI_ROOT_CLIENT_ID + dir-namespace + frontmatter
   granularity:client:<slug>)
  Phase-B adds: OS UNIX permissions + separate-repo + 13th edge

  RETRIEVAL STACK (Q1 4-tier, no vector DB)
  ─────────────────────────────────────────
  T1 Direct path  ──→  T2 Index+grep  ──→  T3 Typed-BFS(edges.jsonl)
                                                    ↓
                                     T4 Long-context (niche-bounded)

  SELF-REINFORCEMENT TRIO
  ────────────────────────
  /consolidate (daily)  →  merge duplicates
  /lint (weekly)        →  orphans + contradictions + anchor check
  /build-graph (post-wave) → rebuild edges.jsonl communities
```

---

## Synthesis Claims (F / ClaimScope / R)

- claim: "The primary leverage point of L1 Knowledge is the query-anchor discipline (D28) — it determines signal-to-noise ratio across all retrieval operations and forces intentional curation over greedy accumulation."
  F: F4
  ClaimScope: "Holds for the A1 Phase-A substrate at ≤1K pages; at G3 (≥15K pages) additional leverage shifts to A3 graph-structure (community summaries pre-computation), but anchor discipline remains the prerequisite."
  R: "Refuted if retrieval precision (defined as fraction of retrieved pages relevant to the query) does not measurably exceed a no-anchor baseline within the first 10 cycles of anchor-enforced ingestion. Accepted if precision ≥ 0.70 sustained over 10 `/ask` invocations with anchor-aligned wiki content."

- claim: "The three-zone architecture (hot/cold/client) is antifragile to G2 scale — it requires <30% structural change at 10× current page count."
  F: F4
  ClaimScope: "Holds for G1→G2 transition (≤5K pages, ≤10 clients). Does NOT hold for G1→G3 transition (≥15K pages, ≥50 clients) — A1 fragility threshold crossed, A3 augmentation mandatory."
  R: "Refuted if adding A2 substrate at G2 requires removing or rewiring >30% of existing wiki layout. Accepted if the A2 migration is additive (new edge type + env-var hook + directory namespace) without restructuring existing concept/entity/claim pages."

## Dissents Preserved

- source: investor-expert × critic (swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-investor-critic-icp-kpi-realism.md)
  claim: "Path B (client-hosted, Jetix as methodology provider) yields higher gross margin at G1 (70.7% GM yr1 per €3K+€15K pricing) than Path C (hybrid, Jetix-hosted agents query client KB via tunnel); Path C networking complexity is a Phase-2 risk, not a Phase-1 feature."
  F: F4
  ClaimScope: "Holds at G1 ≤3 clients under Path B pricing assumptions; may not hold at G2 if Mittelstand enterprise clients require Path C as table-stakes for GDPR compliance."
  R: "Refuted if first 2 paying clients require Path C as a precondition for signing. Accepted if Path B closes G1 contracts with ≥1 client before G2 gate."

- source: systems-expert × integrator (systems integrator APEX cell, swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md)
  claim: "The dominant reinforcing feedback loop in the knowledge layer is the 'expert-reads-wiki → produces-better-output → output-feeds-wiki' cycle; the dominant balancing loop is the query-anchor filter (D28) which constrains wiki growth rate. These two loops determine the layer's equilibrium; the anchor filter must be tuned to avoid strangling the reinforcing loop."
  F: F4
  ClaimScope: "Holds at Phase-A scale; loop dominance shifts at G3 when community-summary pre-computation (A3) changes the information structure."
  R: "Refuted if wiki growth rate declines without improvement in retrieval precision (anchor filter over-constraining). Accepted if wiki growth rate correlates with improved retrieval precision over 10 cycles of anchor-enforced operation."

---

*End of L1 Knowledge section draft. Provenance complete per shared-protocols §2. All claims carry F / ClaimScope / R triples. Dissents preserved. No capital allocation calls made; no code-level quality scores issued; no epistemic arbitration on paradigm correctness.*
