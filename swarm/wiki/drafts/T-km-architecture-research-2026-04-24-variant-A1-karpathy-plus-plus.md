---
title: Variant A1 — "Karpathy++ (filesystem-resident, retrieval-lean, write-heavy)"
type: variant-draft
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
confidence_method: brigadier-integration-from-engineering-integrator-and-tier1
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-optimizer-pipeline-deltas.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-scalability-ingest-retrieval-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-optimizer-frg-discipline.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1, D2, D3, D6, D7"}
  - {path: "raw/research/knowledge-architecture-deep-research-2026-04-19.md", range: "Parts A.1, B, F, G"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§§3, 5"}
  - {path: "raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md", range: "§11, §13"}
related: []
binding_scope: km-architecture-variant-A1
---

# Variant A1 — "Karpathy++ (filesystem-resident, retrieval-lean, write-heavy)"

## §1 Name + One-line Pitch

**A1 — Karpathy++ : extends the Karpathy LLM-Wiki gist (2026-04) with typed edges, Private-Library-per-expert pool-first slices, scheduled `/consolidate` daily + `/lint` weekly + `/build-graph` post-wave as the self-reinforcement trio, and per-client filesystem-namespacing for UC-9 isolation + on-demand `OFFLINE_MODE=1` synthesis for UC-10.** [F: F4 / ClaimScope: KM-architecture-Phase-A / R: medium]

## §2 Axis of Differentiation (~110w)

This variant occupies the **retrieval-lean / write-heavy / filesystem-native** quadrant. Variant A2 occupies *ontology-layered / federated-peer-holons / by-construction-isolation*. Variant A3 occupies *pre-compiled-heavy / GraphRAG-community-summaries+HippoRAG-PPR / cross-document-synthesis*. Choice between them governed by: (1) **expected query volume** — A1 supports ~50-200 queries/day low-latency; (2) **operational team size** — A1 fits solo-now-team-ready (D2 Lock 2); A3 needs daily-cron maintainer at G2+; (3) **infrastructure appetite** — A1 stays pure filesystem+grep through G2; A2 requires per-client repos at G2+; A3 requires nightly community-detection cron + persistent PPR index at G2+. A1 is the **conservative-tail position** in investor's barbell (70%); A3 the aggressive-tail (30%). [F: F3 / ClaimScope: A-variants-axis-of-diff / R: medium]

## §3 Architecture Diagram

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TD
    Ruslan[Ruslan voice/text/Telegram] -->|/ingest| Ingest[/ingest skill]
    Ingest --> Sources[swarm/wiki/sources/]
    Ingest --> Concepts[swarm/wiki/concepts/]
    Ingest --> Edges[swarm/wiki/graph/edges.jsonl]
    Ingest --> Niche[swarm/wiki/niches/<niche>/ symlinks]

    Query[Expert/Ruslan query] -->|/ask| Ask[/ask Q1 4-tier]
    Ask -->|Tier-A direct path| Niche
    Ask -->|Tier-B index+grep| Index[swarm/wiki/index.md + ripgrep]
    Ask -->|Tier-C typed-BFS depth-2| Edges
    Ask -->|Tier-D long-context fallback| LongCtx[bounded niche dir read]
    Ask -->|filing loop| Comparisons[swarm/wiki/comparisons/]

    Brigadier[brigadier] -->|promotes drafts→canonical| Spine[swarm/wiki/{themes,foundations,global,...}/]
    Experts[5 domain experts] -->|strategies.md| Strategies[agents/<expert>/strategies.md]
    Strategies -->|W-5 Level-2 promote validated| Improvements[swarm/wiki/meta/agent-improvements/]
    Improvements -->|≥10 uses + 3:1 ✓/✗| Global[swarm/wiki/global/compound-rules/]

    subgraph "UC-9 isolation (Phase A)"
      WikiRoots[.claude/config/wiki-roots.yaml]
      EnvVar[WIKI_ROOT_CLIENT_ID env var]
      ClientDir[swarm/wiki/operations/clients/<slug>/]
      WikiRoots --> EnvVar
      EnvVar --> ClientDir
    end

    subgraph "UC-10 offline-first (Phase A)"
      OffMode[OFFLINE_MODE=1]
      StructExtract[/ask Tier-D structured-excerpt path]
      OffMode --> StructExtract
    end

    subgraph "UC-10 offline-first (Phase B)"
      InfStack[swarm/lib/inference-stack.yaml]
      Ollama[ollama + GGUF Mistral-7B-Q4]
      InfStack --> Ollama
    end
```

## §4 Mechanics (~1500w)

### §4.1 Ingest Pipeline (6 source types)

For each input source type, A1 specifies skill + dedup + niche routing + frontmatter + edge derivation:

**(a) Voice memo (.ogg/.mp3 in `inbox/voice/`).** `tools/transcribe.py` (existing pipeline, scoped Whisper window per CLAUDE.md voice-pipeline) → transcript MD in `raw/transcripts/<YYYY-MM-DD>/<slug>.md`. Then `/ingest raw/transcripts/<...>` fires: extract entities via in-session LLM (no embeddings), check `swarm/wiki/concepts/<slug>.md` for each: absent → create with frontmatter per D2 §2.3 (`pipeline: ingested`, `state: drafted`, `niche` per content classifier, `sources: [{path: raw/transcripts/..., range: '<start>-<end>'}]`), present → append to `sources[]` + emit `derived_from` edge. Append to `swarm/wiki/log.md` + `swarm/wiki/index.md`. [F: F4 / ClaimScope: ingest-voice / R: high]

**(b) Article URL (Ruslan paste in chat).** `/ingest <url>` fires: WebFetch into `raw/articles/<YYYY-MM-DD>-<slug>.md` (Phase-A: brigadier-only Bash; Phase-B: scoped skill); same dedup+route as (a).

**(c) YouTube video (UC-1).** Existing `/ingest <url>` triggers transcription path (operator opens scoped Whisper window per shared-protocols §9.1 — explicitly NOT used in this cycle's execution per Anti-scope §9). Output: `raw/videos/<YYYY-MM-DD>-<slug>-transcript.md`; same routing.

**(d) Book excerpt (Tier-4 Private Library).** `/ingest raw/books-md/<slug>.md` (operator-driven; Phase-B sweep). Extract via pool-first-query-second (master synthesis §4.6.2): expert reads ≤2 books per cycle, distillation lands in `agents/<expert>/strategies.md` + `wiki/foundations/<expert-domain>/`. NEVER fresh-read in this cycle (Phase-A lock).

**(e) Peer-reviewed paper (PDF in `raw/papers/`).** `/ingest raw/papers/<slug>.pdf` → text extraction (Phase-B skill) + same routing as (a). Tier-1 source frontmatter (`tier: tier-1`).

**(f) Ruslan Telegram note (manual paste / inbox-processor).** `/ingest <text>` (terminal stdin) → routing same as (a) but lower confidence (`F: F2 / R: low` defaults until critic-mode validates).

**Dedup logic.** Slug-collision check via existing `swarm/wiki/concepts/<slug>.md` fs-test; conflict → `/consolidate` invocation (semantic-overlap check via Tier-A direct-path read of both pages + LLM in-session synthesis decides merge vs distinct). Sub-second on filesystem at G1 scale (1K pages); <5s at G2 (5K pages).

**Niche routing.** `niche:` frontmatter field per CLAUDE.md L70 6-niche enum; ingest skill auto-classifies by content keyword + Ruslan-overrideable. Niche symlinks (per CLAUDE.md "Per-agent memory layer") give each expert a filtered view.

### §4.2 Retrieval Q1 4-tier + offline-first augmentation

**Tier-A Direct path.** Read by exact path when known. ≤50ms at any scale. Used by experts who know exactly which page they need (e.g., systems-expert reading `wiki/foundations/systems/levenchuk-fpf.md`).

**Tier-B Index+grep.** Walk `swarm/wiki/index.md` (frontmatter tag filter) → `rg` over matching layer/niche dirs. ≤200ms at G1 (1K pages); ≤500ms at G2 (5K pages); degrades to ~2s p95 at G3 (15K pages) — engineering-scalability flagged this as the G3 physical failure mode for A1; upgrade trigger fires (BM25 secondary + per-niche shards).

**Tier-C Typed-BFS over `edges.jsonl`.** Start from seed page, expand via specific edge types per D3 (e.g., `extends`, `supports`, `derived_from`). Depth-2 default; depth-3 on `--deep` flag. ≤300ms at G1; ≤1s at G2 (~5,700 edges); 50MB in-memory ceiling at G3 (~50K edges) — engineering-scalability §2.3 trigger: split edges by layer + per-niche shards + GraphRAG community-detection daily cron (transition trigger to A3).

**Tier-D Long-context fallback.** Bounded to current-niche dir; do not load full wiki. **OFFLINE-FIRST AUGMENTATION (UC-10):** when `OFFLINE_MODE=1` env-var is set, Tier-D substitutes structured-excerpt synthesis (engineering-optimizer Δ2): instead of cloud LLM, the skill returns the top 5-10 `Tier-A/B/C` results as a structured excerpt list with citations, no LLM synthesis. Latency: 1-3s. Quality: T-Offline (fact retrieval; classification; extraction against known schema; short synthesis ≤500 words). Higher-quality synthesis requires T-Hybrid (HITL gate for cloud-augmentation with redacted PII) OR T-Cloud-only (public-data queries; never client-private). [F: F4 / ClaimScope: UC-10-Phase-A / R: medium / refuted_if: any session with OFFLINE_MODE=1 makes any TCP connection to provider endpoints (tcpdump verifies)]

### §4.3 Write-back W-5 Two-level CE

**Level-1 (per-expert).** When an expert successfully completes a non-trivial task pattern, brigadier dispatches a `<expert> × integrator` cell with `mode: writing-support` → cell returns extractions; brigadier composes the 4-part DRR entry (philosophy-optimizer canonical template at 80w/part floor: Context / Decision / Alternatives-considered / Review-checkpoint per FPF E-9). Brigadier appends to `agents/<expert>/strategies.md` (Layer-2 personal memory; per shared-protocols §1 expert self-write exception NOT used — brigadier is sole writer here per Q2 + R6 collapse D12). [F: F4 / ClaimScope: W-5-Level-1 / R: high]

**Level-2 (cross-expert).** When 2+ experts surface the same pattern (or a Level-1 entry achieves α-3 `active → validated` predicate: ≥10 uses + ✓/✗ ≥ 3:1), brigadier promotes to `swarm/wiki/global/compound-rules/<slug>.md` per D1 §1.3 + D12 collapse. Promotion is gated by §5.5.5 provenance check + brigadier-attested (or ruslan-attested for foundation-grade promotions per D2 §2.3 confidence_method enum). [F: F4 / ClaimScope: W-5-Level-2 / R: high]

### §4.4 Refresh Cadence (Private Library distillation per W-3 + Pillar 2)

**Cadence.** Every ~10 closed cycles (≈ monthly at Phase-A pace), brigadier dispatches a Tier-4 sweep: each domain expert reads 1-2 books from its allocated subset (per ROY-ALIGNMENT §2 expert allocation), updates strategies.md + foundations/<expert-domain>/. Operator-driven; brigadier does NOT initiate (Tier-4 closed-core book corpus is Phase-B fuel per `.claude/agents/brigadier.md §1a`; current cycle: Phase-A lock = pool-first-query-second, no fresh reads). [F: F3 / ClaimScope: refresh-cadence / R: medium]

**Audit trail.** Each book-distillation entry carries `produced_by: <expert>-writing-support`, `human_composed_at: <YYYY-MM-DD>` (FPF E-10 + Phase-B `/lint` enforcement). `meta/health.md` surfaces "Tier-4 distillation count this quarter" as a knowledge-compounding metric (per investor-integrator §2 quarterly mark-to-market — Δ-H4 from investor-optimizer).

### §4.5 Lifecycle (α-2 Artefact transitions)

`drafted → reviewed → revised → accepted → referenced → superseded → retired → tombstoned` per D5 + critic-gate1 spec extension. Movers per row: brigadier moves drafted→reviewed (via dispatched critic cell); cells move reviewed→revised (re-write own draft); brigadier moves revised→accepted (§5.6 promotion via provenance gate); other artefacts moving in supersedes references → automatic; tombstoned by HITL only (per D5). [F: F4 / ClaimScope: α-2-lifecycle / R: high]

**Invariants preserved per WLNK/MONO/IDEM/COMM/LOC.** Wikilinks consistent through transitions (WLNK); never decrement state monotonically (MONO ratchet); same input → same transition (IDEM); transition-pairs commute when independent (COMM); transition affects only the artefact + edges, not unrelated pages (LOC). [F: F5 / ClaimScope: artefact-lifecycle-invariants / R: high]

## §5 Use-case Walkthrough (UC-1..UC-10)

### UC-1 — Video Ingest (Meadows 1999 "Leverage Points")

Input: `inbox/videos/2026-04-24-meadows-leverage-points.mp4` (45-min YouTube via yt-dlp). Operator opens scoped Whisper window (NOT in this cycle), runs `tools/transcribe.py` → `raw/transcripts/2026-04-24-meadows-leverage-points.md`. Then `/ingest raw/transcripts/2026-04-24-meadows-leverage-points.md`:

1. Extract entities: "leverage point", "feedback loop", "systems archetype shifting-the-burden", "stocks and flows", "paradigm shift", "self-organization", "sub-optimization". (≥7 candidates; targets ≥5 concept pages.)
2. For each: check `swarm/wiki/concepts/<slug>.md`. None exist (G1 fresh start). Create 7 pages with frontmatter (`pipeline: ingested`, `state: drafted`, `niche: meta`, `produced_by: /ingest`, `sources: [{path: raw/transcripts/2026-04-24-meadows-leverage-points.md, range: '0-2700s'}]`).
3. Emit ≥8 typed edges in `graph/edges.jsonl`: `{from: source/meadows-1999-leverage-points, to: concept/leverage-points, type: supports}`; `{from: concept/leverage-points, to: concept/feedback-loop, type: extends}`; `{from: concept/feedback-loop, to: concept/stocks-and-flows, type: extends}`; etc.
4. Drop `niches/meta/` symlinks → systems-expert sees pages on next invocation.
5. Append `swarm/wiki/log.md` + `swarm/wiki/index.md` entries.
6. Failure modes: 45-min transcript fits Opus 4.7 1M-context easily; Sonnet 4.6 200K may OOM — `/ingest` chunks at 100K-token boundaries. Existing slug `concept/feedback-loop` (compiled from prior cycle) → append `sources[]` entry + `derived_from` edge. URL unreachable later → `/lint` flags `sources[]` resolution failure as warning. [F: F4 / ClaimScope: UC-1-A1 / R: medium]

### UC-2 — Weekly Digest Query

Monday 8:00 CET. Ruslan: *"Что нового в wiki за прошлую неделю?"*. `/ask --weekly` fires: walks `swarm/wiki/log.md` for last-7d entries grouped by 6 niches (personal/business/sales/life/tech/meta). For each niche, top-5 by edge-degree (page with most inbound `supports` + `derived_from` edges in past week). Cross-link count per niche. Emergent themes via `/build-graph` weekly community summaries (D1 §1.2 + Microsoft GraphRAG pattern lite — implemented as edge-clustering sweep, not full GraphRAG community detection — A3 territory). Latency: ≤60s first byte at G1; ≤120s complete. Citations: every claim cites wiki page id + frontmatter slug. Empty week: explicit "no new pages this week" marker. Drafts excluded from digest (canonical only — engineering-critic H-7 partial flag preserved). [F: F4 / ClaimScope: UC-2-A1-G1 / R: medium]

### UC-3 — Solve-with-Wiki

Ruslan: *"Как применить systems-thinking к нашему outreach-процессу в DACH?"*. `/ask` Q1 retrieval: Tier-B `index+grep` on niches `meta` (systems content) + `sales` (DACH outreach) returns 12 candidates. Tier-C typed-BFS depth-2 expands to 24. Tier-D structured-excerpt synthesis (T-Offline) returns top 8 cited excerpts; OR Tier-D LLM synthesis (T-Hybrid, opt-in) returns 400-word plan: "stocks and flows: lead → prospect → qualified → closed; feedback loops: response-rate ↔ template-quality; leverage point: calibration step BEFORE outreach rather than volume AFTER (per Meadows 1999 §5)". Plan cites ≥4 wiki pages: 2 from `themes/systems/` + 2 from `niches/sales/`. Filing-loop write-back (per D1 §1.3): novel synthesis → `wiki/comparisons/2026-04-24-apply-systems-thinking-to-outreach.md`; F-G-R: `F: F2 / ClaimScope: dach-outreach-quick-money / R: medium / refuted_if: A/B test on 50 prospects shows no response-rate lift after 4 weeks of leverage-point-applied templates`. Failure mode: 50+ candidate retrieval → Tier-D bounds to current-niche; contradiction between systems and sales niches → preserve dissent + route to HITL. [F: F4 / ClaimScope: UC-3-A1-G1 / R: medium]

### UC-4 — Skill Accumulation (Compound Loop)

Brigadier completes a novel task decomposition (e.g., "first-time Layer-A vs Layer-B paired-axis decomposition" — this very cycle). Pattern extraction: brigadier dispatches `engineering × integrator` with `mode: writing-support` → cell returns 4-part DRR extractions. Brigadier composes: appends to `agents/brigadier/strategies.md` (4-part DRR per philosophy-optimizer template). Mirror to `swarm/wiki/brigadier/how-to-decompose-tasks/<slug>.md` per D1 §1.3 (brigadier-write Layer 2). After ≥10 uses + ✓/✗ ≥ 3:1 (α-3 `active → validated`), promotion to `swarm/wiki/global/compound-rules/<slug>.md` (per D12 + W-5 Level-2). Next-cycle query: brigadier intakes similar task → §3 Decomposition preamble reads `agents/brigadier/strategies.md` + `swarm/wiki/brigadier/how-to-decompose-tasks/` (Q1 Tier-A niche=meta filter). Failure modes: simultaneous-cycle conflicting patterns → Q2 single-writer brigadier mitigates via integration at α-4 close; Ruslan-only patterns (require human voice judgment) → tag `produced_by: ruslan-attested`. [F: F4 / ClaimScope: UC-4-A1 / R: high]

### UC-5 — Project Onboarding

Brief (Layer-A handles peripherally; full ownership in Layer-B variant chosen). A1 contributes: at project bootstrap, project-wiki reads `wiki/themes/<theme>/README.md` per ICP fit (e.g., consulting → `themes/business/`); `related[]` entries appear in project `_moc.md` frontmatter. Topic-wiki provides foundational concept pages; project-wiki accumulates execution state. UC-5 traced fully in Layer-B variants. [F: F3 / ClaimScope: UC-5-A1-stub / R: medium]

### UC-6 — Cross-project Insight Transfer

Pattern in `quick-money` ("DACH enterprise responds 3× to German-language opening"): project-brigadier appends pattern to `wiki/operations/quick-money/history.md`. Meta-agent weekly sweep (mgmt-optimizer Δ7 alternative) detects pattern repetition → proposes promotion to `wiki/global/compound-rules/dach-german-opening.md`. Edge type: `derived_from` (existing 12-enum suffices; no 13th edge needed for cross-project transfer per A1 — that's `holon-ref` for cross-CLIENT, different scope). Filing loop creates `wiki/comparisons/2026-05-XX-dach-pattern-applied-to-research.md` when systems-expert applies the pattern to research-thesis-validation interviews. Philosophy F-G-R: pattern `R: medium / refuted_if: 5 research interviews show no response-rate lift`. [F: F4 / ClaimScope: UC-6-A1 / R: medium]

### UC-7 — Contradiction Detection

`/lint` Q5 signal #4 fires on contradiction between `wiki/concepts/private-library-moat.md` (cycle-3 entry: "primary moat") and `wiki/concepts/matchmaker-roy-replication.md` (cycle-4 derivative: "matchmaker is equally primary"). Bidirectional `contradicts` edges per D3 §3.2.2 + critic-gate1 H-fix. `meta/health.md` contradiction section increments. Affected pages: `stance: contested` per D2 claims schema. Ruslan prompted at next gate: edit / supersede / tombstone / preserve-both-conditional with bounded ClaimScope. Multi-hop semantic-equivalence: `/consolidate` heuristic keyword overlap + `/ask`-backed LLM synthesis (T-Hybrid opt-in) OR Ruslan-manual. **UC-7×UC-9 federated**: per philosophy-integrator §4 protocol, per-client `/lint` runs scoped to client-holon; Jetix-central `/lint` runs over methodology-only; cross-client contradictions surface ONLY in opt-in case-study mode (HITL ack required). [F: F4 / ClaimScope: UC-7-A1 / R: high]

### UC-8 — Scale Test (preview; full in §10 horizon)

A1's gate behavior: G1 (1K pages, ~600 edges, 6 agents): grep+BFS sub-second; nothing breaks. G2 (5K pages, ~5,700 edges): in-memory acceptable; `/build-graph` full rebuild ~5min/week tolerable. G3 (15K pages, ~50K edges): in-memory >50MB; grep p95 ~2s — **A1 fragile, forced migration to A2 federated peer-holons OR A3 GraphRAG-augmented**. Engineering-scalability §3 confirms: A1 standalone caps at G2; pre-investment in A2 substrate at G2 enables clean G3 transition. [F: F4 / ClaimScope: UC-8-A1 / R: high]

### UC-9 — Client Isolation (architectural proof; ≥200w)

A1 proof BY CONSTRUCTION via three stacked Phase-A mechanisms (defense-in-depth per philosophy-integrator §3 Lakatos protective-belt endorsement):

**Layer 1 — Session-level env-var (engineering-optimizer Δ1).** `.claude/config/wiki-roots.yaml` gains a `clients:` stanza:
```yaml
clients:
  client-a: { root: clients/client-a/swarm/wiki/, methodology_remote: jetix-methodology-repo }
  client-b: { root: clients/client-b/swarm/wiki/, methodology_remote: jetix-methodology-repo }
default: { root: swarm/wiki/ }
```
Skill startup resolves `$WIKI_ROOT` via D7 §7.4 algorithm + `WIKI_ROOT_CLIENT_ID` env-var. Brigadier instance for Client-A is a separate process with `WIKI_ROOT_CLIENT_ID=client-a`. **All 5 skills (`/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph`) already resolve `$WIKI_ROOT`** — the env-var path requires zero skill-body rewrites.

**Layer 2 — Directory namespace + frontmatter granularity (mgmt-optimizer Δ4 + systems-optimizer Δ-extras E-16 ext).** Per-client artefacts live under `swarm/wiki/operations/clients/<client-slug>/<project-slug>/`. Every artefact carries `granularity: client:<slug>` per FPF E-16 extension. `/lint` enforces: any artefact in `wiki/global/` with `granularity: client:*` triggers a hard error (cross-client global-write FORBIDDEN).

**Layer 3 — Phase-B graph-level (systems-optimizer Δ1, AWAITING-APPROVAL per D3 §3.5).** 13th edge type `holon-ref` with hard `/lint` rule: any `holon-ref` edge whose target lies in a different client-holon-root is a lint violation.

**Pen-test scenario.** Hostile Client-A employee crafts prompt-injection targeting `/ask` to "read /clients/client-b/swarm/wiki/concepts/strategy.md". Result: skill resolves `$WIKI_ROOT=clients/client-a/swarm/wiki/`; the path resolution rejects (client-b is outside the resolved root). Even if attacker bypasses skill abstraction by directly invoking Read tool with absolute path, the OS filesystem permission (Phase-B: separate UNIX user per client) denies. **Acceptance predicate:** any session with `WIKI_ROOT_CLIENT_ID=client-a` successfully reading any file under `clients/client-b/` fails the proof; refute the variant. [F: F4 / ClaimScope: UC-9-A1-Phase-A / R: medium / refuted_if: pen-test reveals cross-client read]

### UC-10 — Offline-First Inference (architectural proof; ≥200w)

A1 proof via two-tier mechanism:

**T-Offline (Phase A, operational).** `/ask --offline` (or `OFFLINE_MODE=1` env-var) routes Tier-D to structured-excerpt synthesis (engineering-optimizer Δ2 +31 LoC in `.claude/skills/ask.md`). No cloud LLM call. Returns top 5-10 retrieval results as a structured excerpt list with citations. Latency: 1-3s. Quality tier: T-Offline-sufficient queries (fact retrieval; classification; extraction against known schema; short synthesis ≤500w). For T-Hybrid queries, `/ask --offline --hybrid-gate` fires HITL gate file requesting cloud-augmentation approval with redacted PII.

**T-Hybrid + T-Cloud-only (Phase B, future).** `swarm/lib/inference-stack.yaml` (engineering-optimizer Δ4 manifest) declares: primary stack = ollama; primary model = Mistral 7B Q4_K_M (Apache 2.0 — investor-optimizer §4 cleanest-license recommendation); alternative = Llama 3.1-8B Q4_K_M (Llama Community License; needs DACH golden-set evaluation per dissent D-2). Hardware floor: 16GB GPU (RTX 4080 €1500 capex if owned; €120/month rental Vast.ai). T-Cloud-only path serves public-data queries only (benchmark research; SOTA citations); never touches client-private data.

**Network-disconnect test.** Client environment: detach network interface; issue `/ask --offline "Summarize Q1 partnership negotiations and extract recurring objections"`. Expected: local-only response; citations to client-KB pages; tcpdump verifies zero outbound network events. **Acceptance predicate:** OFFLINE_MODE=1 invocation makes any TCP connection to provider endpoints (`api.anthropic.com`, `api.openai.com`, etc.) → variant refuted. [F: F4 / ClaimScope: UC-10-A1-Phase-A / R: medium / refuted_if: tcpdump shows outbound provider connection in OFFLINE_MODE=1 session]

## §6 UC-9 + UC-10 Co-located Proof Section (≥400w)

**Isolation model: filesystem-namespaced (Phase A) → separate-repo (Phase B).**

The A1 variant's UC-9 architectural proof rests on the fact that **the existing 5 skills (`/ingest`, `/ask`, `/lint`, `/consolidate`, `/build-graph`) already resolve `$WIKI_ROOT` via the D7 §7.4 algorithm**. No skill-body rewrite is required to enable per-client isolation; only a configuration extension (`clients:` stanza in `wiki-roots.yaml`) and an env-var convention (`WIKI_ROOT_CLIENT_ID`). This is the smallest-LOC architectural change in any of the 6 variants for UC-9 — engineering-optimizer Δ1 confirmed +13 LoC + 1 row to `swarm/lib/shared-protocols.md §5 role-tool-matrix`.

**Phase-B by-construction strengthening.** Each client deployment becomes a separate `clients/<slug>/` git repository, OS-level UNIX user, and (optionally) separate VM/container. Cross-client reads are physically impossible — OS denies. The defense-in-depth STACK adds graph-level (13th `holon-ref` edge with hard `/lint` cross-holon rejection per systems-optimizer Δ1) and frontmatter-level (`granularity:client:<slug>` per E-16 extension; `/lint` global-write FORBIDDEN check) safeguards. Philosophy-integrator §3 endorsed the STACK over single-mechanism per Lakatos protective-belt logic: multiple thin layers > single thick layer for strategic moat preservation. [F: F4 / ClaimScope: UC-9-defense-in-depth / R: high]

**Local-LLM family supported.** Default: ollama + Mistral 7B Q4_K_M (Apache 2.0; 8GB VRAM floor; €700-1K capex if owned; €60-120/month Vast.ai rental; 3-6s p95 latency for 500-token synthesis). Alternative: Llama 3.1-8B Q4_K_M (Llama Community License; requires ≤700M MAU compliance attestation; 16GB VRAM floor; 4-8s latency). Pending evaluation: DeepSeek V3 Lite (license review on "non-competing applications" clause for Mittelstand commercial deployment; 24GB VRAM; 5-10s latency). Phi-3-mini and Qwen 2.5 noted as future evaluation candidates.

**Hosting model alignment.** Path B (Client-hosted; Jetix ships methodology) is the Phase-A default per investor-optimizer Δ-H3 (€3K onboarding + €15K/yr recurring → 70.7% GM yr1, clears 70% floor). Path A (Jetix-hosted VPS in EU) is the low-touch SMB fallback (~70% GM at €15K/yr; knife-edge). Path C (Hybrid: Jetix agent-swarm + client KB tunnel) deferred to post-contractor-#1 (54% GM at €15K/yr fails Phase-A floor; viable at €50K enterprise tier per investor §4). All 3 paths preserve UC-9 by construction at Phase-B; Phase-A Path B + Path A only.

**Tier split (T-Offline / T-Hybrid / T-Cloud-only).**
- **T-Offline (default for all client-private queries):** fact retrieval; summarization ≤10K tokens; classification; extraction against known schema; short synthesis ≤500 words. Phase-A: structured-excerpt path. Phase-B: ollama+Mistral local LLM.
- **T-Hybrid (HITL opt-in):** synthesis across 10+ documents; novel reasoning over domain edge cases; long composition ≥2000 words. Per-query cloud augmentation with redacted-input (NER + pattern-match PII redaction; audit log records redaction delta).
- **T-Cloud-only (public-data queries, never client-private):** benchmark comparisons; SOTA citation lookup; open-source code search.

**EU compliance alignment.** GDPR Art. 22 (automated decision-making — local LLM keeps data on-prem) + Art. 32 (security of processing — OS-level UNIX permissions + signed git commits as ambient attestation). EU AI Act Art. 14 (human oversight — HITL gate on T-Hybrid opt-in). BSI C5 / ISO 27001 alignment target: signed `sources[]` provenance + `/lint` signature validation extending Q5 signal set per investor-critic §6 Δ-H6 future delta. [F: F4 / ClaimScope: UC-9+UC-10-co-located / R: high]

## §7 Pros / Cons / Tradeoffs

**Pros.** (a) **Lowest infra complexity** of the 3 Layer-A variants; pure filesystem+grep through G2; zero capex; Max-subscription only at G1. (b) **Fastest UC-9 + UC-10 to operational state** — Phase-A primitives ship in 1-2 weeks (env-var + directory namespace + structured-excerpt offline path). (c) **Karpathy-LLM-Wiki direct prior art** — well-understood pattern; debuggability is high (filesystem inspection); aligns with Cherny "Don't box the model in" + Yan "Share FULL traces". (d) **Conservative-tail position in investor barbell (70%)** — risk-of-ruin floor preserved.

**Cons.** (a) **Fragile at G3** — engineering-scalability confirms grep p95 >2s + in-memory edges.jsonl >50MB at G3 (15K pages, 50K edges); forces migration to A2 or A3 augmentation. (b) **Phase-A UC-9 isolation is policy+config layer**, not by-construction at OS-level until Phase-B separate-repos; engineering-critic §6 flagged this as a residual gap (preserved as dissent D-1: engineering vs systems on Phase-A iso level). (c) **Cross-document synthesis at scale weak** — without GraphRAG community summaries (A3 territory), multi-document synthesis quality plateaus at G2-G3. (d) **Refresh cadence operator-driven** — Tier-4 distillation requires manual sweep initiation; not autonomous.

**Tradeoffs.** (1) infra-complexity vs synthesis-quality: A1 chooses low complexity at the cost of weaker cross-document synthesis at G3+. (2) Phase-A speed vs Phase-B by-construction-rigor: A1 ships Phase-A in 2 weeks; A2 ships in 4-6 weeks but is by-construction at OS level immediately. (3) Solo-founder fit vs team-fit: A1 fits solo+team-ready; A2 needs ≥2 ops engineers at G2+ for per-client repo provisioning. (4) Methodology-push fan-out: A1 trivial at 1-3 clients; manual at 10+ clients (CI automation = G2-G3 engineering investment per engineering-scalability §8).

## §8 Effort Estimate

- **Bootstrap (Day 1 scaffolding):** 4-8 hours. Limited by: extending `wiki-roots.yaml` clients: stanza + writing `inference-stack.yaml` manifest + adding 1 row to `shared-protocols.md §5`. No skill-body rewrites needed.
- **UC-1..UC-4 live (ingestion + weekly digest + solve-with-wiki + skill accumulation):** 2-3 days. Limited by: existing wiki v3 substrate already supports — A1 adds structured-excerpt offline path (~31 LoC in `/ask`).
- **UC-5..UC-8 stable (project onboarding + cross-project transfer + contradiction detection + scale-tested at G1):** 3-4 weeks. Limited by: Layer-B integration; mgmt-expert ownership of project-bootstrap skill (delegated to Layer-B variant choice).
- **UC-9 + UC-10 live (client-isolation pen-test + offline-first demo on local LLM):** 2-3 weeks separate. Limited by: per-client setup automation (first client ~2 days manual; subsequent ≤2 hours via script per engineering-optimizer); ollama+Mistral GGUF stack integration on client hardware; isolation pen-test scenario authoring.

## §9 Migration Path from Current State

`swarm/wiki/` v3 is bootstrapped per D1 §1.4 (day-one state confirmed by my Phase-1 inspection). Legacy `wiki/` v2 coexists per Q9 + R3 (untouched per Anti-scope). A1 changes:
1. **Extend** `.claude/config/wiki-roots.yaml` with `clients:` stanza (Δ1; +13 LoC).
2. **Extend** `swarm/lib/shared-protocols.md §5 role-tool-matrix` with WIKI_ROOT_CLIENT_ID env-var row (+1 row).
3. **Patch** `.claude/skills/ask.md` Step 2 + Step 4 with OFFLINE_MODE=1 conditional + structured-excerpt synthesis branch (Δ2; +31 LoC).
4. **Create** `swarm/lib/inference-stack.yaml` manifest (Δ4; ~110 lines; Phase-B implementation gated AWAITING-APPROVAL).
5. **Extend** D2 frontmatter `granularity:` enum to include `client:<slug>` value (Δ-extras; 1 enum value + `/lint` signal `L-CROSS-CLIENT-GLOBAL`).
6. (Phase-B) **Add** D3 13th edge `holon-ref` (systems-optimizer Δ1; AWAITING-APPROVAL per D3 §3.5; new `/lint` signal `L-CROSS-HOLON-REF`).

**Staging order (parallelizable).** Steps 1-2 in parallel (config). Step 3 after step 1 (depends on `WIKI_ROOT` resolution). Step 4 in parallel with steps 1-3 (manifest only). Step 5 in parallel. Step 6 Phase-B AWAITING-APPROVAL.

**Rollback point.** Each step is a single git commit; revert by `git revert <sha>`. Step 3 (skill body change) is the only step touching active code path; staged behind `OFFLINE_MODE=1` env-var (default off) so existing online flow is unaffected. WLNK preserved across all steps; MONO ratchet on `state:` transitions; IDEM on retry; COMM across steps 1-2-4-5; LOC violated only in step 3 by intent (cross-skill change documented per engineering-optimizer §1.1).

## §10 Horizon Projection (≥600w; 5 gates)

| Gate | Pages | Projects | Clients | Physical failure | Upgrade path | MHT event | BOSC-A-T-X | Janus risk | Offline-LLM HW |
|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | ~1,000 | 8 | 1-3 | none — grep+BFS sub-second; in-memory edges.jsonl <2MB | none required | — | Time | low (S-A: solo-founder context-monopoly, mitigated by mailbox logging) | on-demand GPU rental Vast.ai €60-120/mo (Mistral-7B); structured-excerpt path Phase-A |
| **G2 €200K** | ~5,000 | 15 | 10 | `/build-graph` full rebuild >5min weekly; methodology-push fan-out manual at 10+ clients | incremental `/build-graph` cron + CI automation methodology-push (engineering-scalability §8) | Phase Promotion (`/lint` weekly→nightly; `/build-graph` weekly→daily) | Scale + Operation | medium S-A (engineering owns edge-derivation alone — mitigated by /build-graph determinism) | ollama+Mistral-7B Q4 owned hardware (€700-1K capex) feasible at this scale; first paying client triggers T-Offline mandatory |
| **G3 €1M** | ~15,000 | 30 | 50 | grep p95 ~2s; in-memory edges.jsonl ~50MB; contradictions surface rate >3/week; `/lint` weekly takes >30min | persistent graph (networkx → ArangoDB); sharded `/lint`; **pre-investment in A2 substrate (federated peer-holons) MANDATORY**; per-client JSONL sharding (Δ-5); BM25 secondary index (Kelly half-bet 27% of upgrade budget per investor-optimizer §2) | Fission (graph tier separates from filesystem; sub-brigadier per niche optional) | Composition + Scale + Operation | high INT excess (experts defer all edge-curation to brigadier — mitigated by W-5 Level-2 promotion automation) | per-client GPU procurement gate (≥3 paying clients + ≤20% trailing-3mo revenue + HITL ack per investor-optimizer §1) — €15K capex per A100-equivalent if Mistral-7B insufficient for client-load |
| **G4 $100M** | ~50,000 | 100 | 500 | Q1 Tier-D long-context fallback exceeds budget; cross-niche edges overwhelm manual review; brigadier attention budget blown across 100 projects | hybrid BM25+dense+PPR+RRF (A3 GraphRAG augmentation MANDATORY); automated contradiction clustering; sub-roy per portfolio (consulting / infra / research per Lock 21); CI methodology-push to 500 client repos (full automation) | Role-Lift (per-niche sub-brigadiers; per-portfolio sub-roys); Context Reframe (each client-roy a peer to Jetix-roy) | Boundary + Agency + Composition | S-A or INT per sub-roy; pervasive risk requires Janus degraded-mode spec at every sub-roy boundary | Each client owns its inference stack (16GB GPU minimum); Mittelstand AI Alliance methodology-license dominant revenue (per investor-scalability §4) |
| **G5 $1T** | ~200,000+ | 500+ | 5000+ (Mittelstand AI Alliance) | distributed wiki across roys; merge-conflict rate >1/hour at Jetix-central methodology repo; per-roy ontologies drift | federated wikis + CRDT for edges; per-roy sub-lints; Alliance methodology parliament with adversarial mandate (philosophy-scalability §7 Lakatos hardcore safeguard); statistical convergence as $1T peer-review equivalent | Fusion (multi-roy meta-wiki); Continuous re-Phase-Promotion | eXternal + Composition + Agency | S-A pervasive (per-roy ontologies drift away from Jetix-central) — mitigated by quarterly Alliance methodology parliament + outcome-level telemetry convergence | Per-Alliance-member owns inference stack; Jetix-central owns methodology + standards; Token economy Option B (D23) tie-in plausible per investor-scalability §5 (gated by 4 pre-conditions + HITL) |

**Antifragility verdict.** A1 standalone is **robust through G2, fragile at G3, requires A2 substrate pre-investment by G2 to remain operative through G4-G5.** As a Phase-A entry point, A1 is correct; as a steady-state architecture, A1 is an 18-month bridge to A2/A3 hybrid. [F: F4 / ClaimScope: A1-horizon / R: medium]

## §11 Anti-Fragility Assessment (≥400w)

**Verdict: ROBUST through G2; FRAGILE at G3; requires substrate migration.**

**Mechanism for robustness G1-G2.** A1's Karpathy++ pattern survives 2K → 10K pages because grep+BFS scales near-linearly until the in-memory edges.jsonl hits ~50MB ceiling (per knowledge-architecture-deep-research §G.2). Below that ceiling, every retrieval is sub-second, every write is atomic (filesystem semantics), and every commit is auditable (git). The system gets MARGINALLY better with each ingest because: (a) more edges → richer typed-BFS reach (Tier-C improves); (b) more `derived_from` cycles → Lakatos protective belt thickens around the moat thesis. This is operative (not aspirational) antifragility through G2.

**Mechanism for fragility G3.** Above G3 (15K pages, 50K edges), three failure modes compound:
- **Grep-degradation:** rg over `swarm/wiki/` linear-scales; at 15K pages p95 latency hits 2-3s — UC-2 weekly-digest latency floor (180s) breaks because Tier-B is the bulk of retrieval.
- **In-memory edges:** networkx load of >50MB JSONL takes ~10s per `/lint` invocation; weekly `/lint` blows 30min budget.
- **Methodology-push fan-out:** at 30 client repos, manual git-push is ~2h/week of operator time — unsustainable without CI.

A1 standalone CANNOT close these failure modes within its own architectural axis. The only graceful migration is to A2 substrate (per-client JSONL shards + federated peer-holons restoring Ashby variety balance per systems-scalability §3) OR A3 augmentation (GraphRAG community summaries pre-computed daily — engineering-scalability §4). **A1 transitioning to A2/A3 hybrid is itself antifragile** because the migration triggers (latency p95 / `/lint` runtime / methodology-push hours) are MEASURABLE in `meta/health.md` and the migration steps are PRE-PLANNED in this variant doc — under stress, the system EXECUTES a known migration, not improvises.

**Pressure tests.**

(1) **Cross-niche edges double overnight (e.g., a major research-deep-dive cycle adds 2× edges).** A1 absorbs at G1 (1K → 2K edges = nothing); at G2 (~10K edges) `/build-graph` weekly cron extends to ~10min — still tolerable. At G3 (~100K edges) load fails. **Mitigation pre-planned:** Δ-5 per-client JSONL sharding + nightly `/build-graph` migration trigger.

(2) **Domain expert replaced (engineering-expert prompt rewritten Phase-B).** A1 unaffected — agent prompts are orthogonal to KM substrate. Expert's `agents/<expert>/strategies.md` migrates intact (filesystem-native; expert ownership).

(3) **Project forked into parallel directions (e.g., quick-money splits into "quick-money-DACH" + "quick-money-NL").** A1 handles via two `wiki/operations/<slug>/` namespaces with `derived_from` edges; no architectural change. Mgmt-integrator B-variant manages the lifecycle.

(4) **Hostile prompt-injection on `/ask` (UC-9 attack).** Per §5 UC-9: defense-in-depth STACK rejects at session-level (env-var) + graph-level (Phase-B `holon-ref` lint) + frontmatter-level (`granularity:client:<slug>` global-write FORBIDDEN). Recovery predicate: `/lint` audit log shows zero cross-client read attempts succeeded over rolling 100 queries. [F: F4 / ClaimScope: A1-anti-fragility / R: medium]

## §12 Open Questions for Ruslan

1. **A1 standalone vs A1→A2 migration trigger:** ack the migration plan at G2 first paying client onset (auto-trigger in `meta/health.md`)? OR ack at G3 latency/edges crossover?
2. **Mistral-7B-Q4 vs Llama-3.1-8B-Q4 default for ollama:** authorize 20-query DACH golden-set evaluation as resolution mechanism for D-2 dissent?
3. **Path B €3K onboarding + €15K/yr default vs Path A €15K/yr-only:** Phase-A default Path B per investor-optimizer Δ-H3, OR Path A for solo-founder simplicity at first 1-2 clients?
4. **Tier-4 Private Library refresh cadence:** every 10 cycles (≈monthly) per A1 §4.4, OR per quarter via investor-optimizer Δ-H4 quarterly mark-to-market trigger?
5. **`OFFLINE_MODE=1` default behavior:** off (cloud LLM by default; opt-in offline) OR on (offline by default; opt-in cloud)? Strategic positioning answer per Strategic Insight §4 = ON for client deployments; OFF for Jetix-internal Phase-A development.

— brigadier (Phase-5 variant draft), 2026-04-24
