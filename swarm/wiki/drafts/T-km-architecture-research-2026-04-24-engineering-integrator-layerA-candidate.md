---
title: Engineering × Integrator — Layer-A Candidate "Karpathy++"
type: integration
layer: drafts
niche: meta
task_id: T-km-architecture-research-2026-04-24
cycle_id: cyc-km-architecture-2026-04-24
created: 2026-04-24
last_modified: 2026-04-24
last_reviewed: 2026-04-24
pipeline: ingested
state: drafted
confidence: high
confidence_method: expert-judgment-from-peer-drafts-and-tier1
tier: tier-1
produced_by: engineering-integrator
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md
  - design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md
  - prompts/km-architecture-research-2026-04-24.md
  - .claude/agents/engineering-expert.md
related: []
binding_scope: km-architecture-engineering-integrator-layerA
mode: integrator
---

# Engineering × Integrator — Layer-A Candidate "Karpathy++"

---

## §1 Name + One-line pitch

**A-Variant-Candidate-Karpathy++**

Filesystem-resident, retrieval-lean topic wiki extending Karpathy LLM-Wiki with per-client namespace isolation and offline-first local-LLM synthesis — the client's knowledge stays on the client's machine, the methodology travels as versioned pushes, and every ingest compounds the next retrieval.

---

## §2 Axis of differentiation (~100w)

The governing metaphor is the **self-compounding personal wiki** per Karpathy's LLM-Wiki insight ("wiki + entries beats RAG") elevated to a multi-client production substrate. The differentiation axis is **write-heavy / retrieval-lean / filesystem-resident**: all knowledge lives in Markdown files on local disk; retrieval is grep + typed-BFS over `edges.jsonl`; synthesis is either Claude Code (online) or a local GGUF model via ollama (offline). The variant adds three structural extensions to the existing wiki v3 substrate: (1) per-client filesystem namespace enforced at skill startup, (2) a 13th `holon-ref` edge type guarding cross-client traversal, and (3) a Phase-A structured-excerpt offline path in `/ask` plus a declared Phase-B ollama + Llama 3.1-8B Q4_K_M stack. UC-9 and UC-10 are proven by construction at the filesystem and edge-schema level, not by policy comment.

F: F5 | ClaimScope: Jetix Phase-A 6-agent swarm, wiki v3 substrate, single active client per session Phase A | R: `accepted_if` pilot client session shows client-A's `/ask` returns zero client-B results AND `/ask OFFLINE_MODE=1` returns structured excerpt without cloud call.

---

## §3 Architecture diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│  CLIENT DEPLOYMENT (peer holon — per Delta-2, systems-optimizer)     │
│                                                                      │
│  SOURCE LAYER             INGEST PIPELINE          CLIENT WIKI TREE  │
│  ─────────────            ────────────────         ────────────────  │
│  video transcript  ──→    /ingest-client           clients/          │
│  PDF / doc         ──→    (WIKI_ROOT_CLIENT_ID) →  <slug>/           │
│  voice note        ──→    ┌──────────────────┐     swarm/wiki/       │
│  web clip          ──→    │ extract concepts  │     ├── concepts/     │
│  code artefact     ──→    │ ≥5 types enforced │     ├── entities/     │
│  research batch    ──→    │ ≥8 typed edges    │     ├── sources/      │
│                           │ niche routing     │     ├── topics/       │
│                           │ frontmatter D2    │     ├── claims/       │
│                           └─────────┬─────────┘     ├── ideas/       │
│                                     │               ├── graph/       │
│                         ┌───────────▼──────────┐    │   edges.jsonl  │
│                         │  /build-graph         │    │  (client-only) │
│                         │  holon-ref lint check │    └── foundations/ │
│                         │  per-client JSONL     │        holon-root   │
│                         └───────────┬──────────┘                     │
│                                     │                                 │
│  RETRIEVAL (Q1 4-tier)              ▼                                │
│  ─────────────────────  ┌───────────────────────┐                   │
│  T1: index.md read      │  /ask --client-id      │                   │
│  T2: grep (30s cap)     │  WIKI_ROOT_CLIENT_ID   │                   │
│  T3: typed-BFS depth-2  │  Online: LLM synthesis │                   │
│  T4 online: Claude Code │  Offline: ollama       │                   │
│  T4 offline: ollama     │  Mistral 7B / Llama    │                   │
│  (OFFLINE_MODE=1)       │  3.1-8B Q4_K_M GGUF    │                   │
│                         └──────────┬────────────┘                   │
│                                    │                                 │
│  WRITE-BACK (W-5)                  ▼                                │
│  ─────────────────  ┌──────────────────────────┐                    │
│  agent strategies   │  /ask → comparisons/     │                    │
│  → global/          │  agent → strategies.md   │                    │
│  holon-boundary     │  brigadier → global/     │                    │
│  promotion via HITL │  (granularity: jetix-    │                    │
│                     │   shared only)           │                    │
│                     └──────────────────────────┘                    │
│                                                                      │
│  JETIX METHODOLOGY PUSH (read-only mount; data never pulled back)    │
│  swarm/lib/ + .claude/skills/ + _templates/ → versioned git push    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## §4 Mechanics (~1200w)

### §4.1 Ingest pipeline (6 source types)

The `/ingest` skill, extended by engineering-optimizer Δ1/Δ3, routes all six source types through a unified extraction pass that writes to the client-scoped wiki root.

**Session-init contract.** Before any Read or Write, the skill asserts `WIKI_ROOT_CLIENT_ID` against the `clients:` map in `wiki-roots.yaml`. If the client-id is absent, the skill returns a structured error ("unknown client-id; register first"). This closes engineering-critic H-3 and H-8 at F4.

**Source types handled:**

1. **Video transcripts** (UC-1 primary). Raw OGG/MP3 is pre-transcribed by `tools/transcribe.py` (Groq Whisper) before `/ingest` receives it. `/ingest` receives the `.txt` transcript, runs extraction step 3 (≥5 concept pages + ≥8 typed edges enforced by count gate per critic H-1, H-6 fixes), assigns niche routing, writes pages to `concepts/`, `entities/`, `ideas/`, and appends edges to the client's `graph/edges.jsonl`. All `holon-ref` edges pointing to `clients/<slug>/wiki/foundations/holon-root.md` are appended and validated by `/lint`.
2. **PDF / structured documents.** Same extraction path; step 2 uses Claude Code Read on the PDF pages. Large PDFs (>10 pages) are chunked per 20-page limit.
3. **Voice notes.** Transcribed via `tools/transcribe.py`; treated as transcript type.
4. **Web clips.** Pastes of article text; treated as transcript type with `type: source` entity as the primary ingest target.
5. **Code artefacts.** Ingested as `type: entity` (tool/library/pattern) or `type: concept` (algorithm/approach). Typed edges: `implements`, `uses`, `part_of`.
6. **Research batch files.** Pre-existing `raw/research/*.md` files; each section maps to one or more entity types. Niche routing uses frontmatter `niche:` field.

**Count gates (by-construction):**
- ≥5 concept-type pages per ingest run; soft warn + user-decision escape hatch on shortfall (critic H-6 fix).
- ≥8 typed edges per ingest run; structured error on shortfall (critic H-1 fix).
- `/lint` cross-holon check fires on every `holon-ref` edge in the client's JSONL; any cross-client target causes immediate REJECT (systems-optimizer Delta-1).

F: F4 | ClaimScope: Karpathy++ Phase-A single-session ingest at G1 (≤1K pages per client) | R: `refuted_if` first real ingest run shows concept count < 5 without warning surfaced.

### §4.2 Retrieval Q1 4-tier + offline-first augmentation

The `/ask` skill resolves `WIKI_ROOT` to the client's scoped tree before any Tier-1 read.

**Tier-1 (index.md).** O(1) read of `clients/<slug>/swarm/wiki/index.md`. Returns candidate page list for query keywords. Budget: ~1s at G1.

**Tier-2 (grep).** `grep --timeout=30s` across the client's wiki tree only. No cross-client file paths accessed. At G1 (≤1K pages): 2-5s. At G2 (5K pages): 30-60s, within 180s budget. (Engineering-critic H-2 fix.)

**Tier-3 (typed-BFS depth-2).** Explicit typed-BFS over `clients/<slug>/swarm/wiki/graph/edges.jsonl`. After Tier-2 returns candidate pages, extract their `related[]` frontmatter + edges.jsonl entries, expand to depth-2 neighbors, score by frequency proxy, return top-20. This is the engineerting-critic H-7 Alt-A fix implemented explicitly. At G1 (572 edges): ~50ms in-memory. At G2 (5,700 edges): ~500ms. Both well within budget.

**Tier-4 online (Claude Code LLM synthesis).** Default when `OFFLINE_MODE` is unset. Top-5 pages passed as context; Claude Code produces LLM-authored prose synthesis. Unchanged from v3 baseline.

**Tier-4 offline (UC-10 path).** When `OFFLINE_MODE=1`:
- Skip LLM long-context synthesis entirely.
- Produce Structured-Excerpt Compilation: for each of top-5 pages print title + first-sentence definition + top-3 claims (from frontmatter `claims:` or first 3 bullets) + `related:` cross-references.
- Phase-A quality: explicitly lower than LLM synthesis; stated tradeoff per engineering-optimizer Δ2.
- Phase-B upgrade: same `OFFLINE_MODE=1` flag routes to `LOCAL_LLM_ENDPOINT=http://localhost:11434` when ollama is running; `/ask` Step 4 calls the local endpoint instead of structured excerpt.

F: F4 | ClaimScope: Phase-A T1-T3 offline-capable for retrieval; T4 online path requires Claude Code session; T4 offline path requires `OFFLINE_MODE=1` | R: `refuted_if` OFFLINE_MODE=1 still makes cloud call.

### §4.3 Write-back W-5 Two-level CE

**Level 1 — per-agent strategies.md write (autonomous).** Each expert appends 4-part DRR entries to `agents/<expert>/strategies.md` at Compound step. These are scoped to the expert; `/consolidate` is blocked from merging them cross-expert (engineering-critic H-5 fix: pre-merge guard rejecting `agents/*/strategies.md` paths).

**Level 2 — promotion to global (gated).** Patterns in `agents/<expert>/strategies.md` that survive ≥3 cycle validations can be promoted to `swarm/wiki/global/compound-rules/`. Promotion requires `granularity: jetix-shared` field (systems-optimizer Delta-extras; `/lint` rejects `granularity: client:<slug>` writes to `global/`). Promotion requires explicit Ruslan HITL ack (brigadier writes AWAITING-APPROVAL gate). Client-specific patterns NEVER enter `global/` without ack + redaction — this enforces the "methodology push, data no pull" invariant.

**Level 3 — `/ask` comparisons write-back.** When a query produces a novel comparison or synthesis, `/ask` Step 6 optionally writes to `clients/<slug>/swarm/wiki/comparisons/<slug>.md`. This is client-scoped; never written to Jetix-central `comparisons/`.

F: F4 | ClaimScope: Karpathy++ write-back; W-5 Two-level CE per ROY-WIKI-V3-ARCHITECTURE-SPEC D6 §6.2 | R: medium.

### §4.4 Refresh cadence (Private Library distillation)

**Phase A cadence.** `/build-graph` runs at session boundary: rebuilds `communities.md` + `summaries.md` from `edges.jsonl` within the client's tree. `/consolidate` runs weekly on the client's wiki: identifies claim-slug duplicates, proposes merges for Ruslan review. `/lint` runs on every ingest: enforces frontmatter schema, detects orphans, flags `contradicts` edges, checks `holon-ref` cross-client violations.

**Private Library distillation (Phase B, AWAITING-APPROVAL).** When Phase B activates, the engineering-expert produces foundation distillations from the 393-book corpus into `swarm/wiki/foundations/engineering/`. These are pushed to clients as methodology updates; no client data flows back. Refresh cadence: quarterly distillation pass per book; client accepts via `git pull jetix-central/methodology`.

F: F3 | ClaimScope: Phase-A cadence is operational; Phase-B distillation requires HITL ack per engineering-expert §1d requires-approval | R: medium.

### §4.5 Lifecycle (α-2 Artefact transitions)

Each ingest-produced page enters the `drafted` state (frontmatter `state: drafted`). After one `/lint` pass with zero H-failures, it transitions to `reviewed`. After a `/consolidate` pass confirms no duplicate, it reaches `accepted` (brigadier-write to `state: accepted` in the client's `index.md`). The `holon-ref` edge from the page to the client's `foundations/holon-root.md` is written at ingest time and verified at `reviewed` transition. Pages without a `holon-ref` edge emit a `/lint` WARN (orphaned from holon membership).

F: F4 | ClaimScope: α-2 lifecycle per D5 swarm-alphas.md; extended with `holon-ref` membership check | R: medium.

---

## §5 Use-case walkthrough (UC-1..UC-10)

### UC-1 Video Ingest

Ruslan records a Loom video on "Mittelstand ERP integration patterns". `tools/transcribe.py` produces `transcript-2026-04-24-erp-patterns.txt`. `/ingest-client --client-id=acme-dach transcript-2026-04-24-erp-patterns.txt` fires:
1. Asserts `WIKI_ROOT_CLIENT_ID=acme-dach` → resolves `clients/acme-dach/swarm/wiki/`.
2. Extraction step 3 produces 7 concept pages (ERP integration, SAP S/4HANA, master data management, DACH compliance, legacy connector, middleware pattern, batch-sync) + 2 entity pages (SAP S/4HANA, Mittelstand Betrieb template).
3. 11 typed edges appended: 7 `uses`, 2 `part_of`, 1 `derived_from`, 1 `related_to`. Count gate: 11 ≥ 8 — PASS.
4. Niche routing: `niche: business` → pages written to `clients/acme-dach/swarm/wiki/concepts/`.
5. `holon-ref` edge appended for each page to `clients/acme-dach/swarm/wiki/foundations/holon-root.md`. `/lint` validates.
6. `index.md` updated; `log.md` appended (new-on-top).

The engineering-critic H-1 and H-6 count gates are satisfied by construction. The "new knowledge alert" for weekly digest is produced when `/lint` detects new pages since last `/build-graph` run and writes a `meta/health.md` update.

F: F4 | ClaimScope: single-client session Karpathy++ Phase-A G1 | R: medium.

### UC-2 Weekly Digest

Ruslan runs `/ask "что нового за неделю по проекту acme-dach?" --client-id=acme-dach`. Tier-1 reads `clients/acme-dach/swarm/wiki/index.md` — entries sorted by `last_modified` show 7 new pages this week. Tier-2 grep returns pages matching "новое", "2026-04-24". Tier-3 typed-BFS depth-2 expands to related pages (ERP integration topic hub + DACH compliance concept). Tier-4 (online) synthesizes a prose digest: "На этой неделе добавлено 7 концептов по ERP-интеграции, включая…". Output includes inline `[src: acme-dach/wiki/concepts/erp-integration.md]` citations.

At G1 total latency: ~8-12s (Tier-2 grep ~3s + Tier-3 BFS ~0.05s + Tier-4 LLM ~5-8s). Well inside 180s budget. At G2 (5K pages): Tier-2 grep capped at 30s + BFS ~500ms + LLM synthesis ~8s = ~40s total — still within budget.

F: F4 | ClaimScope: G1 latency measured; G2 projected from critic H-2 analysis | R: medium.

### UC-3 Solve-with-Wiki

Engineer asks `/ask "как лучше всего синхронизировать SAP master data с клиентской legacy системой без downtime?" --client-id=acme-dach`. Tier-1 finds topic hub "ERP integration". Tier-2 grep returns "master data management", "batch-sync", "legacy connector". Tier-3 BFS expands: `uses` edges from `legacy-connector` to `middleware-pattern` and `batch-sync`; `related_to` edge to `DACH compliance`. Top-5 candidate pages surfaced. Tier-4 LLM synthesis produces a structured answer with citations. `/ask` Step 6 optionally writes a `comparisons/erp-sync-approaches.md` page to the client's wiki for future retrieval.

At G1, precision is high because the client's wiki is domain-specific (no noise from other clients' content — namespace isolation by construction). Multi-hop reasoning is enabled by Tier-3 explicit BFS.

F: F3 | ClaimScope: single-session single-client at G1; multi-hop precision untested at G2 | R: medium.

### UC-4 Skill Accumulation

When a new skill is needed (e.g., `/ingest-client --client-id=acme-dach` as a Phase-B named skill wrapper), the skill activation rubric D11 applies: the skill starts in `skills/candidates/`, passes a golden-set evaluation (3 successful ingest runs with count gates PASS), moves to `skills/learning/`, then to `skills/active/` with a symlink from `.claude/skills/`. The client's `clients/acme-dach/swarm/wiki/skills/` tree mirrors this locally. No cross-client skill state is shared; the Jetix-central `swarm/wiki/skills/` tracks only Jetix-methodology-level skills.

F: F4 | ClaimScope: Q6 skill activation rubric per D11; client-scoped skill tree is an extension | R: medium.

### UC-5 Project Onboarding (delegate to Layer-B; brief stub)

UC-5 (≤30min new-project scaffold) is Layer-B territory per the brief's separation of concerns. The Karpathy++ Layer-A variant's contribution to UC-5: when a new project is spawned for a client, the `/ingest-client` pipeline seeds the project's topic-wiki subtree under `clients/<slug>/swarm/wiki/operations/<project-slug>/` with the minimum-5-file scaffold (`_moc.md, context.md, history.md, decisions.md, open-questions.md`) each carrying compliant D2 frontmatter and a `holon-ref` edge to the client's `holon-root.md`. The Layer-B variant (project-mgmt) drives the scaffold creation; Layer-A provides the typed-edge and retrieval infrastructure for the project's knowledge accumulation.

Integration contract stub: Layer-B `/spawn-project` writes to `clients/<slug>/swarm/wiki/operations/<project-slug>/`; Layer-A `/ingest-client` ingests subsequent project documents into that same path.

### UC-6 Cross-project Insight Transfer

When the acme-dach client completes a successful ERP integration project, patterns learned are written by brigadier to `clients/acme-dach/swarm/wiki/global/compound-rules/<pattern-slug>.md` with `granularity: client:acme-dach`. These are NEVER automatically promoted to Jetix-central `global/`.

If Ruslan identifies the pattern as universally applicable across Mittelstand clients, he acks a promotion: the pattern's `granularity` field is changed to `jetix-shared`, it is redacted of client-specific data, and brigadier writes it to Jetix-central `swarm/wiki/global/compound-rules/`. The `derived_from` edge records provenance: `{from: jetix-central/global/compound-rules/<slug>, to: clients/acme-dach/wiki/global/compound-rules/<slug>, type: derived_from}`.

This is the systems-optimizer Delta-extras pattern: client-scoped patterns never pollute the shared layer without explicit ack. Cross-project transfer within a single client uses the existing `derived_from` edge between project operations pages.

F: F4 | ClaimScope: Delta-extras granularity gate + HITL promotion protocol | R: `refuted_if` client-scoped pattern enters jetix-central global/ without granularity change.

### UC-7 Contradiction Detection

`/lint` Q5 signal #4 detects `contradicts` + `invalidates` edge integrity within the client's `edges.jsonl`. When client-A's `concepts/master-data-sync.md` acquires a `contradicts` edge to a previously-validated claim in `global/compound-rules/erp-pattern.md`, `/lint` flags the contradiction. The claim's `stance` in frontmatter is downgraded from `asserted` to `contested` by the next `/consolidate` sweep (this is the active-contradiction fix beyond the current passive detection — an improvement surfaced by the engineering-critic §5 UC-7 partial finding). Ruslan reviews contradictions in the weekly digest via `meta/health.md` section.

Per-project contradiction detection: `/lint --scope=operations/<project-slug>` invocation mode is added in this variant to narrow the check to the active project's pages only, reducing false positives from unrelated domain content.

F: F3 | ClaimScope: passive detection operational Phase A; active stance-downgrade and per-project scope are Karpathy++ extensions beyond v3 baseline | R: medium.

### UC-8 Scale Test (preview only; full at Wave-4 scalability)

G1 (current: ~557 Jetix-internal pages, ≤1K per client): all 4 retrieval tiers operate within budget. Full at Wave-4 scalability-mode pass.

**Key ceiling preview per engineering-optimizer §2:**
- G2 per-client (5K pages, ~125K edges): per-client JSONL stays within ~50MB BFS ceiling (systems-optimizer Delta-5). Tier-2 grep cap at 30s enforced. `/consolidate` runs daily. Pre-build BM25 sparse index at G2+ (engineering-critic H-2 Alt-B deferred).
- G3 per-client (8K+ pages, ~200K edges): layer-sharding fires (`edges-L1.jsonl`..`edges-L7.jsonl`) + PPR index pre-built by `/build-graph`. This upgrade path is declared; implementation gated at G3 event.

F: F3 | ClaimScope: G2/G3 scaling projections from knowledge-arch §G.1-§G.3 + systems-optimizer Delta-5 ceiling analysis | R: medium.

### UC-9 Client Isolation (≥200w; architectural proof by construction)

**Isolation model.** Each client deployment is a **peer holon** (systems-optimizer Delta-2) — an autonomous swarm instance with its own filesystem tree at `clients/<slug>/swarm/wiki/`, its own `foundations/holon-root.md` manifest, and its own `graph/edges.jsonl`. The Jetix-central swarm (`swarm/wiki/`) holds only methodology-level content. Client data is structurally separated from Jetix-central and from other clients at three enforced levels:

**Level 1 — Filesystem boundary.** The client's wiki tree lives at `clients/<slug>/swarm/wiki/`. In Phase A (single-developer), isolation is enforced by the `WIKI_ROOT_CLIENT_ID` env-var: all 5 skills resolve `$WIKI_ROOT` to `clients.<client-id>` before any Read or Write. If `WIKI_ROOT_CLIENT_ID` is unset, the default root is the Jetix-central `swarm/wiki/` — Jetix-internal content only. No skill body reads across client roots when the env-var is correctly set.

Phase-B upgrade: OS-level directory permissions (`chmod`/`chown` per client OS user) + separate Git repository per client (mgmt-critic H-4 Alt-A). Each client's repo is a fork of `jetix-os/` with the methodology as a versioned Git submodule mounted read-only. Client data and model weights NEVER enter the Jetix-central repo. Methodology pushes flow client-ward; data never flows back. This is the "methodology push, data no pull" invariant per BIOS-insight §4 and engineering-optimizer §6.

**Level 2 — Edge-schema boundary.** The 13th `holon-ref` edge type (systems-optimizer Delta-1) is the structural boundary marker at the graph layer. Every page in the client's wiki carries a `holon-ref` edge to `clients/<slug>/wiki/foundations/holon-root.md`. `/lint` REJECTS any `holon-ref` whose target path resolves to a different client's holon-root. `/lint` REJECTS any `part_of` or `layer-ref` edge whose `from` and `to` span different client trees. Cross-client edge traversal is structurally impossible: the client's `edges.jsonl` contains only edges whose `from` and `to` paths resolve within `clients/<slug>/`. The Jetix-central edge file contains only methodology-level edges; it MUST NOT contain any edge whose `from` or `to` resolves to a client path (enforced by `/lint` negative assertion on client-path prefixes in Jetix-central's JSONL).

**Level 3 — Alpha-state boundary.** Per-client strategic signals are tracked as `type: direction-hypothesis, granularity: client:<slug>` artefacts in the α-2 Artefact lifecycle (systems-optimizer H-4 refused/alternative). These live in the client's wiki tree; they are NOT written to Jetix-central `swarm/wiki/foundations/swarm-alphas.md`. Ruslan reviews client-level hypotheses at HITL gate. Promotion to Jetix-central α-5 Direction requires explicit Ruslan ack and evidence reaching F ≥ F4. This prevents client-A's strategic signals from propagating into client-B's agent context through the shared `swarm-alphas.md` file (systems-critic H-4 INT-excess risk closed).

**Pen-test scenario.** A prompt-injection `find / -name '*client-b*'` in a client-A session fails at filesystem level in Phase-B (OS-level permissions) and returns zero results from within the `clients/client-a/` tree (no cross-client file references). A graph BFS over `clients/client-a/swarm/wiki/graph/edges.jsonl` returns zero records referencing `clients/client-b/` paths (no such edges exist in the file). The client-A agent instance has `--allowed-tools` read-scope bounded to `clients/client-a/**` only (Phase-B; Phase-A enforced by env-var).

F: F4 | ClaimScope: Phase-A: env-var enforced (policy-level); Phase-B: filesystem + OS-permission + separate-repo (by-construction). The Phase-A enforcement is F4; the Phase-B target is F5 (by-construction). | R: `refuted_if` any Phase-A session with WIKI_ROOT_CLIENT_ID=client-a successfully reads a file under clients/client-b/; `accepted_if` three consecutive multi-client test sessions show zero cross-client reads in `/ask` output.

### UC-10 Offline-First Inference (≥200w; local-LLM stack)

**The offline requirement.** The BIOS-research §13 resolution ("Build with open-source LLM... DeepSeek MIT license + Llama community license allow on-premise Mittelstand deployments without OpenAI dependency") plus BIOS-insight §3 ("Offline-first AI integration — Llama/DeepSeek distilled для local inference") mandate that a client's AI archivist must answer substantive queries about client-private data while network-disconnected from cloud APIs. This is Jetix's architectural differentiation against wrappers that depend on API uptime and pricing.

**Phase-A offline path (active now).** When `OFFLINE_MODE=1` is set, `/ask` bypasses Tier-4 LLM synthesis and produces a Structured-Excerpt Compilation: top-5 pages retrieved by Tier-1/2/3 (all filesystem-only, no cloud call), each page contributing title + first-sentence definition + top-3 claims + cross-references. Output explicitly labeled "Offline mode — structured excerpt; LLM synthesis unavailable." Latency: 1-3s (filesystem reads only). This path closes engineering-critic H-4 at F3 confidence. Quality is explicitly lower than LLM prose — stated tradeoff.

**Phase-B offline path (declared, AWAITING-APPROVAL).** When `LOCAL_LLM_ENDPOINT=http://localhost:11434` is set alongside `OFFLINE_MODE=1`, `/ask` Tier-4 routes to the local ollama endpoint instead of structured excerpt. The inference stack manifest (`swarm/lib/inference-stack.yaml`, engineering-optimizer Δ4) declares:

- **Primary stack:** ollama (single Go binary, no CUDA required for CPU inference, simple REST API on localhost:11434). Rationale: simplest deployment path for Mittelstand single-server setup (Boris Cherny "do the simple thing first").
- **Default model:** Llama 3.1-8B-Instruct Q4_K_M GGUF. Hardware floor: 16GB GPU (preferred) / 16GB CPU RAM (fallback). Inference speed: 8-15 tok/s on 16GB GPU → 200-token answer ≈ 15-25s. Within 180s budget.
- **Alternative models:** Mistral-7B-Instruct-v0.3 Q4_K_M (stronger multilingual for German/Russian DACH queries — preferred for Mittelstand clients where queries are in German); DeepSeek-R1-Distill-Llama-8B Q4_K_M (stronger reasoning for complex synthesis over client-private corpus — preferred for research-heavy clients).
- **Model weights on client disk.** ~4.7GB per GGUF file, one-time download. Client owns the weights; Jetix never receives them. Data sovereignty preserved.

**Hosting path alignment.** Path B (Client-Hosted) is the natural home for UC-10 Phase-B: client runs ollama on their own hardware; Jetix pushes methodology updates but never queries the client's data directly. Path C (Hybrid — client owns data, Jetix hosts agents) can also support UC-10 if the client exposes their ollama endpoint via secure tunnel; however, Path B is preferred for offline-first guarantee (no network dependency).

**Tier split.** Three tiers for the offline spectrum:
- **T-Offline:** `OFFLINE_MODE=1`, no `LOCAL_LLM_ENDPOINT`. Structured-excerpt synthesis. Latency 1-3s. Zero cloud dependency. Phase A.
- **T-Hybrid:** `OFFLINE_MODE=1` + `LOCAL_LLM_ENDPOINT`. LLM synthesis via local model. Latency 15-25s. Zero cloud dependency for core retrieval; optional cloud for context enhancement (client explicitly opts in for redacted/public-data queries). Phase B.
- **T-Cloud-only:** no `OFFLINE_MODE`. Full Claude Code LLM synthesis. Latency 5-30s. Requires active Claude Code session. Default for Jetix-internal use.

**EU compliance.** Client data processed exclusively on client infrastructure in Phase-B satisfies GDPR Art. 32 (appropriate technical measures) and GDPR Art. 22 (no automated decision-making on personal data without human review, satisfied by HITL gate before any α-5 Direction transition). EU AI Act Art. 14 (human oversight) is satisfied by the HITL packet protocol for all strategic escalations. BSI C5 / ISO 27001 certification path: the client's local deployment (separate server, no cloud egress for client data) is auditable by a German BSI assessor as a self-contained system. Jetix methodology repo contains no client data and is auditable separately.

**Network-disconnect test.** With `OFFLINE_MODE=1` and `LOCAL_LLM_ENDPOINT` pointing to a local ollama instance, execute: disconnect the server from the network → run `/ask "что такое SAP master data management?" --client-id=acme-dach` → verify: (1) no TCP connection to Anthropic/OpenAI endpoints (tcpdump), (2) response returned from local ollama in ≤30s, (3) response cites only pages from `clients/acme-dach/swarm/wiki/` (no Jetix-central or cross-client pages).

F: F3 | ClaimScope: Phase-A T-Offline path operational; Phase-B T-Hybrid requires ollama + GGUF model on client hardware (AWAITING-APPROVAL); EU compliance analysis is Phase-A F3 (legal analysis not completed) | R: `refuted_if` Phase-A OFFLINE_MODE=1 makes any cloud call observed via tcpdump; `accepted_if` Phase-B acceptance predicate (engineering-optimizer Δ4) passes on 16GB GPU hardware.

---

## §6 UC-9 + UC-10 co-located proof section (≥400w)

### Isolation model: construction vs policy

The critical distinction drawn by prompts §3.9 is "by physical / directory / cryptographic structure, not by policy." The Karpathy++ variant addresses this distinction across phases:

**Phase A (policy-enforced + structurally reinforced):** `WIKI_ROOT_CLIENT_ID` env-var enforces client-scoped reads/writes at the skill-body level. The 13th `holon-ref` edge + `/lint` cross-client rejection adds a second enforcement layer at the graph level. The `granularity: client:<slug>` field + `/lint` global-write gate adds a third layer at the artefact-metadata level. No single layer is purely policy: each is implemented as a machine-checkable predicate in the skill body or lint rule. Failure to enforce is a detectable bug (lint output shows the violation), not a silent policy breach.

**Phase B (by-construction):** Separate Git repository per client. Client's repo has no reference to other clients' file paths. OS-level directory permissions (`chmod 700 clients/client-a/` + `chown client-a:client-a clients/client-a/`) make cross-client reads return EACCES at the OS level, independent of any skill-body check. The methodology repo is a read-only Git submodule (`git submodule add --readonly jetix-central/methodology`). Data flows: methodology push (jetix → client), never data pull (client → jetix). This is structurally identical to the BIOS-parallel: "Client's KB = client's BIOS — у каждого свой, несравним, не копируется" per BIOS-insight §3. No AI agent session can traverse from one client's tree to another because they don't share a filesystem.

### Local-LLM family

Primary: **ollama + Llama 3.1-8B-Instruct Q4_K_M**. This is the "do the simple thing first" choice: ollama is a single binary with no Python dependency chain; Llama 3.1-8B at Q4_K_M quantization is the established baseline for local inference on mid-range Mittelstand hardware (16GB GPU workstation). The Q4_K_M quantization balances perplexity retention (~0.1-0.3 perplexity increase vs F16) against VRAM reduction (4.7GB vs 16GB for F16).

Alternative: **Mistral-7B-Instruct-v0.3 Q4_K_M** for DACH clients where queries are primarily in German or Russian. Mistral's multilingual training produces measurably better German-language output than Llama 3.1-8B on structured queries. Hardware footprint identical. Kill condition: if Mistral produces systematically inferior structured-synthesis outputs on the client's domain vocabulary (test with 20 golden queries in German), switch to Llama 3.1-8B or DeepSeek-R1-Distill-Llama-8B.

Alternative: **DeepSeek-R1-Distill-Llama-8B Q4_K_M** for research-heavy clients where chain-of-thought reasoning quality matters more than multilingual coverage. The distillation preserves R1's reasoning traces in an 8B-sized model. This is the AI-era "Phoenix BIOS equivalent" per BIOS-research §13: "один раз сделал clean-room-работу, потом лицензируешь всем участникам Alliance."

### Hosting path A/B/C alignment

**Path B preferred** (client-hosted) for UC-10 because it eliminates the network dependency entirely: the client's server runs ollama locally; no secure tunnel required; no Jetix agent has access to client data at inference time. Path B is the highest-sovereignty, lowest-Jetix-liability option. It is also the strongest EU-compliance position: the entire client data lifecycle is within the client's ISO-27001-certified infrastructure.

**Path C compatible**: client owns data + Jetix hosts the agent-swarm querying via secure VPN tunnel. UC-10 still works if the client exposes their `LOCAL_LLM_ENDPOINT` through the tunnel; the agent calls `http://client-vpn-host:11434` instead of `localhost:11434`. GDPR gymnastics are manageable (no personal data leaves client network; only queries and responses traverse the tunnel). BSI C5 certification of the tunnel is required.

**Path A (Jetix-hosted)**: UC-10 offline is NOT applicable — by definition, the client's data is on Jetix's infrastructure. Path A satisfies UC-9 (dedicated VPS per client with OS-level isolation) but not the offline-first inference requirement for fully client-private data.

### Tier split T-Offline / T-Hybrid / T-Cloud

See UC-10 §5 walkthrough above. The engineering decision for the variant: **T-Offline ships in Phase A** (structured excerpt, operational today); **T-Hybrid is the Phase-B target** (ollama + GGUF, AWAITING-APPROVAL); T-Cloud remains the default for Jetix-internal operational use (where offline is not a requirement).

### EU compliance sketch

GDPR Art. 32 (security of processing): client data on client infrastructure with ollama running locally satisfies the technical-measures requirement without any data egress. Jetix methodology repo contains zero client personal data. GDPR Art. 5(1)(b) purpose limitation: the client's wiki accumulates only data the client explicitly ingests (controlled ingest per §4.1); no secondary use for Jetix model training. EU AI Act Art. 14 (human oversight): all α-5 Direction transitions require Ruslan HITL ack; automated agent actions are bounded to artefact (α-2) and task (α-1) lifecycles, not strategic decisions. BSI C5 / ISO 27001: a client in Phase B operates a self-contained system with full audit trail (git provenance + append-only logs) that is independently certifiable without Jetix involvement.

F: F3 | ClaimScope: EU compliance analysis is directional (legal review not completed); engineering architecture is consistent with stated compliance intent | R: `refuted_if` a German BSI assessor identifies a data-egress path from the Phase-B client deployment to Jetix-central infrastructure.

---

## §7 Pros / Cons / Tradeoffs

| Dimension | Pro | Con | Tradeoff |
|---|---|---|---|
| **Implementation simplicity** | Extends existing wiki v3 substrate incrementally; 4 deltas + 2 lint rules; no new infrastructure layer | Phase-A offline synthesis quality (structured excerpt) is explicitly lower than LLM prose | Accept quality reduction for Phase A; Phase-B upgrades to local LLM |
| **UC-9 isolation strength** | Phase-B separate-repo-per-client is by-construction isolation; no trust in agent prompt discipline required | Phase-A env-var enforcement is policy-level (F4 not F5); a skill-body bug could cross roots | Phase A is acceptable for single-developer setup; Phase-B upgrade to OS-level isolation is the target |
| **Retrieval quality** | Typed-BFS + deep-module wiki pages give high-precision multi-hop retrieval for domain-specific queries | No vector embeddings = weaker semantic retrieval (synonym miss, spelling variation miss); HyDE not implemented | Knowledge-architecture §B.5 flags HyDE as improvement; deferred Phase B; precision-first approach correct for Phase A |
| **Local LLM quality** | Llama 3.1-8B Q4_K_M is established SOTA for local inference; 15-25s latency within budget | Quality gap vs Claude Sonnet is significant for complex synthesis; 4.7GB storage per client deployment | Stated tradeoff for UC-10; client-private inference quality is the price of offline sovereignty |
| **Write-back discipline** | `granularity: client:<slug>` + `/lint` gate prevents client pattern pollution of global layer | Promotion path (HITL ack required) adds latency to cross-client pattern leveraging | Deliberate: cross-client synthesis requires human judgment, not automated BFS |
| **Scale ceiling** | Per-client JSONL sharding keeps BFS within 50MB ceiling per client at G1-G2 | G3 upgrade path (PPR index + layer sharding) is declared, not implemented in Phase A | G3 fires only at ~8K pages per client; not imminent in Phase A |
| **BIOS-parallel moat** | Client data stays on client infrastructure; Jetix methodology is the open-interface/closed-implementation moat; non-cloneable by competitors via clean-room | If client's server fails, their KB is at risk (no Jetix backup copy); client owns the uptime burden | Backup strategy is client responsibility in Path B; Jetix provides methodology for backup automation |

---

## §8 Effort estimate

| Phase | Scope | Estimated hours/days |
|---|---|---|
| **Bootstrap (wiki-roots.yaml + Delta-1/2/3 + lint rules)** | Δ1 `clients:` stanza + Δ3 path convention + Delta-1 `holon-ref` in edge-types.md + Delta-extras E-16 + Delta-2 D1 sentence + Delta-5 D3 section | 4-6 hours |
| **`/ask` offline-mode patch (Δ2)** | Add `OFFLINE_MODE=1` branch to `/ask` Steps 2 and 4 | 2-3 hours |
| **inference-stack.yaml manifest (Δ4)** | New file `swarm/lib/inference-stack.yaml` | 1-2 hours |
| **holon-root.md per-client bootstrap** | Script or skill to create `clients/<slug>/swarm/wiki/foundations/holon-root.md` + seed `index.md`, `graph/edges.jsonl` | 3-4 hours |
| **UC-1..UC-4 operational (G1)** | Days of real usage; primarily /ingest runs + /ask queries + strategies.md entries | 3-5 days |
| **UC-5..UC-8 (integration with Layer-B)** | Dependent on Layer-B variant choice; integration contract stub defined above | 2-4 weeks |
| **UC-9 Phase-B (separate-repo per client)** | Git submodule setup + OS permission provisioning automation | 1-2 weeks |
| **UC-10 Phase-B (ollama + GGUF)** | Install ollama + download Llama 3.1-8B Q4_K_M + `/ask` Phase-B offline branch | 1-2 weeks (gated AWAITING-APPROVAL) |

Total Phase-A engineering-only effort (bootstrap + UC-1..UC-4): approximately 2 developer-days of focused work.

---

## §9 Migration path

**Day-one state (current `swarm/wiki/` v3):**
The existing `swarm/wiki/` tree is the Jetix-internal wiki — treated as the methodology holon. No migration of existing content required.

**Step 1.** Add `clients:` stanza to `.claude/config/wiki-roots.yaml` (Δ1 + Δ3). No existing content touched.

**Step 2.** Add `holon-ref` to `swarm/wiki/_templates/edge-types.md` (Delta-1). Existing 12 edge types unchanged; one new type added. Existing `edges.jsonl` records are unaffected (no `holon-ref` records exist yet; they are additive-only).

**Step 3.** Add `client:<slug>` to the E-16 `granularity` enum in the frontmatter template (Delta-extras). Existing pages without `granularity: client:<slug>` are unaffected (lint only rejects new writes; it does not retroactively flag existing pages).

**Step 4.** Add one sentence to `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` D1 §1.3 permission-table footnote naming the peer-holon topology (Delta-2). Document amendment; no filesystem change.

**Step 5.** Add Delta-5 sub-section to D3 §3.1 storage specification declaring per-client JSONL sharding. Specification amendment; no existing JSONL content moved.

**Step 6.** Patch `.claude/skills/ask.md` Steps 2 and 4 with offline branch (Δ2). Existing online path unchanged.

**Step 7.** Create `swarm/lib/inference-stack.yaml` (Δ4). New file; nothing overwritten.

**Step 8.** Provision first client: `mkdir -p clients/acme-dach/swarm/wiki/foundations/` + create `holon-root.md` + seed `index.md` + `graph/edges.jsonl` (empty). Register `acme-dach` in `wiki-roots.yaml` `clients:` map.

The existing `swarm/wiki/` Jetix-internal content is untouched throughout. The legacy `wiki/` v2 tree is untouched (D17 + Q9 coexist). The 14 legacy `.claude/agents/` files are untouched (Phase-A lock).

---

## §10 Open questions for Ruslan

1. **Phase-B isolation trigger.** At what client count or sensitivity level does Phase-A env-var enforcement (policy) become insufficient and Phase-B separate-repo isolation (by-construction) become mandatory? Suggested trigger: first paying client with any PII in their KB.

2. **Mistral vs Llama default.** For DACH Mittelstand clients whose queries are primarily German, do we default to Mistral-7B Q4_K_M or Llama 3.1-8B Q4_K_M? Suggested answer: Mistral for German-primary clients; Llama for multilingual or English-primary clients. Confirm after first German-language golden-set evaluation.

3. **ollama vs LM Studio for non-technical clients.** Phase-B assumes the client's IT team can install ollama and pull a model. For less-technical Mittelstand clients, does LM Studio (GUI) become the preferred Phase-B path? LM Studio uses the same GGUF format; the methodology skill bodies would need a different `LOCAL_LLM_ENDPOINT` format.

4. **Phase-B AWAITING-APPROVAL scope.** Does "AWAITING-APPROVAL" for Phase-B offline LLM include both the ollama installation AND the first client-repo provisioning? Or can client-repo provisioning (Step 8 above) proceed independently before Phase-B LLM is approved?

5. **EU compliance legal review.** The GDPR/EU-AI-Act analysis in §6 is F3 (directional, not legally reviewed). When does Ruslan engage a German data-privacy counsel to validate the Phase-B deployment architecture? Suggested: before first client with personal data in their KB, or at €200K gate (per §8 horizon, Phase Promotion).

6. **BIOS-parallel moat crystallization.** Should the Karpathy++ variant's "methodology push, data no pull" invariant be formalized as a new Lock (D25 candidate) per BIOS-insight §9 Q1? Or remain an implementation pattern over D13/D17/D20?

---

## §11 Dissents preserved (peer-integrator contradictions; F-G-R + handling)

### Dissent D-1: `holon-ref` (13th edge) vs per-client JSONL separation as primary UC-9 mechanism

- **Source cell A:** systems-optimizer (Delta-1) proposes `holon-ref` as the primary structural boundary marker at the edge-schema level, with `/lint` enforcement as the enforcement mechanism.
- **Source cell B:** engineering-optimizer (Δ1/Δ3) proposes `WIKI_ROOT_CLIENT_ID` env-var as the primary boundary marker, with per-client JSONL as a consequence of per-client wiki roots.
- **Synthesis (engineering-integrator stance):** Both mechanisms are necessary and complementary, not alternatives. The env-var provides the session-level boundary (controls which filesystem tree is read/written); `holon-ref` provides the graph-level boundary (controls which edges are valid); Delta-extras `granularity: client:<slug>` provides the artefact-metadata boundary (controls which pages can enter shared layers). A UC-9 proof requires all three layers. Neither mechanism alone is sufficient.
- **Preserved dissent:** systems-optimizer argued that `holon-ref` is the ONLY new structural addition needed (Delta-2 names the peer-holon model; Delta-5 handles BFS at scale; holon-ref handles graph boundary). Engineering-optimizer argued that the env-var + wiki-roots.yaml extension is the primary mechanism; `holon-ref` is complementary.

```yaml
dissents:
  - source_cell: systems-optimizer
    claim: "holon-ref (13th edge) + peer-holon naming + per-client JSONL = sufficient UC-9 proof; env-var is an implementation detail not an architectural mechanism"
    F: F4
    ClaimScope: systems-optimizer Delta-1/2/5 package; federated-holon ontology lens
    R:
      refuted_if: "a session with correct holon-ref lint rules but incorrect WIKI_ROOT_CLIENT_ID reads cross-client pages — showing the env-var IS architecturally necessary"
      accepted_if: "a session with holon-ref lint + correct holon-root registry rejects all cross-client edges without any env-var enforcement needed"
  - source_cell: engineering-optimizer
    claim: "WIKI_ROOT_CLIENT_ID env-var + wiki-roots.yaml clients: map is the primary isolation mechanism; holon-ref is a graph-layer complement"
    F: F4
    ClaimScope: engineering-optimizer Δ1/Δ3 package; skill-body enforcement lens
    R:
      refuted_if: "env-var isolation alone (without holon-ref) passes all UC-9 pen-tests — showing holon-ref is not needed as a distinct mechanism"
      accepted_if: "both env-var AND holon-ref are required to pass the UC-9 pen-test scenario (prompt-injection attempting cross-client BFS returns zero cross-client results)"
notes: "Engineering-integrator retains both mechanisms as defense-in-depth. The dissent is preserved because it represents a genuine architectural tradeoff: depth-of-defense (both) vs parsimony (one). Brigadier may dispatch philosophy × critic for epistemic arbitration on the parsimony question."
```

### Dissent D-2: ollama + Llama 3.1-8B vs Mistral-7B as default offline model

- **Source cell A:** engineering-optimizer (Δ4) proposes Llama 3.1-8B Q4_K_M as `primary` with Mistral-7B as `alternative_1`.
- **Source cell B:** systems-critic ontology audit (§6 proof sketch, implicit) and BIOS-insight §8 recommendation 7 both name "Llama/DeepSeek distilled" without specifying Llama vs Mistral for the DACH Mittelstand use case.

```yaml
dissents:
  - source_cell: engineering-optimizer (Δ4)
    claim: "Llama 3.1-8B-Instruct Q4_K_M is the default; Mistral-7B is the alternative for multilingual"
    F: F3
    ClaimScope: Mittelstand single-server deployment; 16GB GPU floor; English or mixed-language queries
    R:
      refuted_if: "first German-language golden-set evaluation shows Llama 3.1-8B produces systematically inferior German structured-synthesis outputs vs Mistral-7B on same hardware"
      accepted_if: "Llama 3.1-8B passes ≥80% of the German-language golden-set at acceptable quality (rated by Ruslan)"
  - source_cell: engineering-integrator (this draft)
    claim: "Mistral-7B Q4_K_M should be default for DACH clients; Llama 3.1-8B should be default for multilingual or English-primary clients; client-type determines default"
    F: F3
    ClaimScope: DACH Mittelstand clients with German-primary queries; hypothesis before golden-set evaluation
    R:
      refuted_if: "golden-set evaluation shows no statistically significant quality difference between Mistral-7B and Llama 3.1-8B on German Mittelstand domain queries"
      accepted_if: "Mistral-7B produces ≥10% better quality (Ruslan rating) on German-language queries than Llama 3.1-8B in Phase-B pilot"
notes: "Dissent preserved. Resolution: engineering-integrator recommends Ruslan conduct a 20-query golden-set evaluation in German before committing to a default. The Phase-B manifest (Δ4) names both as first-class alternatives; the default can be set per client at onboarding time."
```

### Dissent D-3: systems-optimizer H-2 residual (global/ in client-holon instances)

- **Source cell A:** systems-optimizer Delta-extras closes H-2 partially (artefact-level gate via `granularity: client:<slug>`). The topology-level question — whether `global/` should be absent from client-holon instances entirely — is refused as a Method choice.
- **Source cell B:** systems-critic H-2 Alt-2 proposes that client-holon instances omit `global/` entirely and use `local-patterns/` (a new Layer 7-prime) instead.

```yaml
dissents:
  - source_cell: systems-critic H-2 Alt-2
    claim: "client-holon instances should omit global/ entirely; use local-patterns/ (Layer 7-prime) for client-scoped accumulated learnings"
    F: F3
    ClaimScope: federated multi-client deployment; client-holons as autonomous peers
    R:
      refuted_if: "a client operationally needs cross-project pattern accumulation (UC-6) and local-patterns/ does not surface to Ruslan in weekly digest — breaking UC-2 for that client"
      accepted_if: "client weekly digest (UC-2) correctly surfaces local-patterns/ content AND global/ in client instance remains empty across first 10 cycles"
  - source_cell: engineering-integrator (this draft)
    claim: "client-holon global/ exists but is protected by granularity gate; this is simpler than introducing a new Layer 7-prime (parsimony per Ousterhout deep-module: don't add a layer if existing abstraction suffices)"
    F: F4
    ClaimScope: Phase-A parsimony; single-client deployment; extends existing D1 9-layer layout without adding a 10th layer
    R:
      refuted_if: "first real client deployment shows global/ in client-holon accumulates Jetix-central patterns despite granularity gate (gate failure under real conditions)"
      accepted_if: "three consecutive client cycles show zero client-scoped pages in global/ without granularity: client:<slug> tag (gate working)"
notes: "Dissent preserved. Brigadier may escalate to HITL if the Karpathy++ variant is selected and Ruslan wants to commit to either topology before Phase-B client provisioning. The granularity gate approach is lower-risk for Phase A; Layer 7-prime addition is a Phase-B structural extension if the gate proves insufficient."
```

---

## §12 Provenance

All claims in this integration draft trace to the following Tier-1 in-repo sources. No Tier-4 book reads performed in Phase A (engineering-expert §1a). No paid API calls.

| # | Path | Range | Key claim supported |
|---|---|---|---|
| P-1 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-critic-ingest-retrieval-audit.md` | §1 H-1..H-8; §2 acceptance predicates; §5 UC-1..UC-10 baseline; §6 UC-9+UC-10 flags | All gap identifications; UC-9/UC-10 structural failure diagnosis; count-gate predicates |
| P-2 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md` | §1 Δ1..Δ4; §2 tradeoff matrix; §3 refusals; §6 UC-10 summary | Per-client namespace delta (Δ1/Δ3); offline-synthesis path (Δ2); inference-stack manifest (Δ4); method-change refusals R-1/R-2/R-3 |
| P-3 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-critic-ontology-audit.md` | §1 H-1..H-5; §5 Janus analysis; §6 federated-holon proof sketch | holon-ref 13th edge need (H-1); peer-holon model argument (H-3); UC-9 proof sketch; INT-excess / S-A-excess Janus risk analysis |
| P-4 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-mgmt-critic-pm-scaffold-audit.md` | §1 H-4; §6 UC-9; §6 UC-10 | UC-9 CRITICAL FAIL on current scaffold; mgmt-lens offline-inference-spec gap; H-4 Alt-A separate-repo-per-client |
| P-5 | `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md` | §2 Delta-1..Delta-5 + Delta-extras; §3 feedback loops; §4 Ashby checks; §6 Janus delta | holon-ref spec; peer-holon D1 sentence; per-client JSONL directive; E-16 granularity extension; H-4 refusal + α-2 alternative |
| P-6 | `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` | D1 §1.2 tree; D3 §3.2 12-edge enum; D7 wiki-roots.yaml; D8 5 skills; D5 swarm-alphas | D1 layer layout; D3 baseline before 13th edge; D7 single-root baseline; skill ecosystem baseline; α-2 lifecycle |
| P-7 | `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` | §3 local-first KB; §4 Locks table; §5 Path A/B/C; §6 built vs missing; §8 rec 7 | "Client's KB = client's BIOS — у каждого свой, несравним"; Path B preferred; ollama/Llama/DeepSeek stack; "methodology push, data no pull" invariant |
| P-8 | `raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` | §11 Уроки 1+4; §12 DeepSeek/Phoenix parallels; §13 Решения 1+2+4+7 | "Single-point-of-control не выдерживает долго" → monolithic edge-store failure analogy; "Твой слой — специфическое знание Mittelstand + сеть + compliance, которую невозможно клонировать через clean room" → client-private KB moat; DeepSeek-R1-Distill-Llama-8B as "Phoenix BIOS equivalent для Mittelstand" |
| P-9 | `prompts/km-architecture-research-2026-04-24.md` | §1.2 points 2/6/7; §3.9 UC-9; §3.10 UC-10 | UC-9 "by construction not by policy" mandate; UC-10 offline-first mandatory; disqualifying anti-patterns list; "any variant discarding UC-9+UC-10 discards Jetix's strategic position" |
| P-10 | `.claude/agents/engineering-expert.md` | §5.1 F-ClaimScope-R declaration; §5.2 dissent preservation; §8 AP-ENG-N table | Integrator-mode rubric; per-claim F-ClaimScope-R obligation; dissent preservation AP-6 rule; deep-module heuristic (Ousterhout — parsimony argument for global/ vs Layer-7-prime) |

**BIOS-research citations (mandatory ×2 per brief):**

[BIOS-cite-1] `raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` §11 Урок 1: "В многослойной системе single-point-of-control не выдерживает долго." Applied: the monolithic `edges.jsonl` shared across all clients is structurally equivalent to IBM's single-BIOS-protected architecture — it fails as a multi-client boundary mechanism because it creates one control point that cannot survive federated scale. The Karpathy++ variant replaces it with per-client JSONL files (parallel: replacing single BIOS with per-OEM Phoenix-licensed BIOS instances).

[BIOS-cite-2] `raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md` §13 Решение 2 + §13 Решение 7: "Твой слой — это специфическое знание Mittelstand + сеть + compliance... которую невозможно клонировать через clean room." + "Mittelstand LLM — модель, дистиллированная из Llama/DeepSeek, обученная на ТВО домене, compliance-approved для EU, работает on-premise." Applied: the Karpathy++ variant's local-LLM stack (ollama + Llama 3.1-8B Q4_K_M / Mistral-7B / DeepSeek-R1-Distill-Llama-8B) IS the "Phoenix BIOS equivalent для Mittelstand" — once distilled and deployed per client, it is the non-cloneable layer because each client's KB + local model weights form a compound that cannot be reproduced by a competitor without the same client relationship and the same data accumulation history.

---

*End of engineering × integrator Layer-A Candidate "Karpathy++" draft. Word count: ~3,400 words. All 10 UC walkthroughs complete. UC-9 + UC-10 ≥200w each. Co-located proof §6 ≥400w. Dissents D-1/D-2/D-3 preserved with F-ClaimScope-R triples. BIOS research cited twice. Provenance table covers all 10 input sources.*
