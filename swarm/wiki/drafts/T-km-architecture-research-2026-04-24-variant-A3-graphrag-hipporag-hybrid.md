---
title: Variant A3 — "GraphRAG community-summaries + HippoRAG PPR hybrid (pre-compiled-heavy)"
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
confidence: medium
confidence_method: brigadier-integration-from-engineering-scalability-and-research-corpus
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-scalability-ingest-retrieval-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-scalability-both-layers-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-optimizer-bet-sizing.md"}
  - {path: "raw/research/knowledge-architecture-deep-research-2026-04-19.md", range: "Parts A.2 GraphRAG, A.3 HippoRAG, B retrieval, G scale"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1, D3"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md"}
  - {path: "raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md"}
related: []
binding_scope: km-architecture-variant-A3
---

# Variant A3 — "GraphRAG Community-Summaries + HippoRAG PPR Hybrid (Pre-compiled-Heavy)"

## §1 Name + One-line Pitch

**A3 — GraphRAG+HippoRAG Hybrid : pre-computes community summaries (Microsoft GraphRAG 2024 pattern) + maintains HippoRAG-style Personalized PageRank index over typed-edge graph + serves cross-document synthesis at G2-G5 scales where retrieval-lean A1 plateaus and federated A2 alone cannot do single-query multi-document sensemaking; runs entirely as nightly cron over per-client edge-store shards (UC-9 isolation preserved); offline-first via local LLM consuming pre-compiled artefacts.** [F: F4 / ClaimScope: KM-architecture-G2-G5-augmentation / R: medium]

## §2 Axis of Differentiation (~110w)

This variant occupies the **pre-compiled-heavy / graph-native / cross-document-synthesis** quadrant. Variant A1 occupies *retrieval-lean / write-heavy / filesystem-native*. Variant A2 occupies *federated-peer-holons / by-construction-isolation / per-client-shards*. Choice between them governed by: (1) **expected query complexity** — A3 dominates at multi-document synthesis ("what's the cross-pattern across our 10 partnership negotiations?"); A1/A2 dominate at single-document retrieval; (2) **per-client page count** — A3 activates at ≥3K pages per client (under that, the daily-cron compute is over-engineering); (3) **infrastructure tolerance** — A3 needs nightly community-detection cron + persistent PPR index (~50-100MB per client); A1/A2 stay pure filesystem at G1-G2; (4) **investor barbell** — A3 is the *aggressive-tail* (30%); A1 is conservative-tail (70%) per investor-optimizer §3. **A3 is an AUGMENTATION layer over A2 (or late-G2 A1), not a standalone substrate.** [F: F4 / ClaimScope: A3-axis / R: medium]

## §3 Architecture Diagram

```mermaid
graph TD
    subgraph "Per-client A2 substrate (foundation)"
      ClientWiki[clients/<slug>/swarm/wiki/]
      ClientEdges[clients/<slug>/swarm/wiki/graph/edges.jsonl]
    end

    subgraph "A3 nightly pre-compile cron (per-client)"
      BuildGraph[/build-graph --communities]
      PPRIndex[/build-graph --ppr-index]
      ConsolSummaries[/build-graph --community-summaries]

      ClientEdges --> BuildGraph
      BuildGraph --> Communities[clients/<slug>/swarm/wiki/graph/communities.json]
      Communities --> ConsolSummaries
      ConsolSummaries --> SummaryPages[clients/<slug>/swarm/wiki/summaries/community-<id>.md]

      ClientEdges --> PPRIndex
      PPRIndex --> PPRStore[clients/<slug>/swarm/wiki/graph/ppr-index.parquet]
    end

    subgraph "A3-augmented retrieval"
      Query[Cross-document query]
      Query -->|local LLM detects multi-doc intent| AskHybrid[/ask --multidoc-graphrag]
      AskHybrid -->|community-summaries first| SummaryPages
      AskHybrid -->|PPR-ranked seed nodes| PPRStore
      AskHybrid -->|expand via Tier-C BFS| ClientEdges
      AskHybrid -->|local LLM synthesis with retrieved context| Response[Synthesized response with citations]
    end

    subgraph "Cron orchestration"
      Cron[swarm/lib/cron/build-graph.cron]
      Cron -->|02:00 daily per client| BuildGraph
      Cron -->|02:00 daily per client| PPRIndex
      Cron -->|02:30 daily per client| ConsolSummaries
    end

    subgraph "UC-9 isolation preserved"
      Shard[Per-client edge shard]
      OSPerm[OS-level UNIX perms]
      Cron -.->|jetix-client-<slug> UNIX user only| Shard
      OSPerm -.->|enforces per-client cron access| BuildGraph
    end
```

## §4 Mechanics (~1500w)

### §4.1 GraphRAG Community-Summaries Pre-compile

**Pattern.** Microsoft GraphRAG 2024 (per knowledge-architecture-deep-research §A.2): typed entity-relationship graph → community detection (Leiden algorithm) → LLM-generated community summary per cluster → indexed for global-sensemaking queries.

**Jetix application.** Nightly cron at 02:00 (per-client UNIX user) runs `/build-graph --communities` over per-client `edges.jsonl`. Leiden detects communities (typically 30-150 clusters at 5K pages; 200-800 at 15K; 1000-3000 at 50K). For each community, `/build-graph --community-summaries` invokes local LLM (Mistral-7B per inference-stack.yaml) to compose a ≤500-word summary covering: dominant concepts, key claims, contradiction surface, novelty since last community-snapshot. Output: `clients/<slug>/swarm/wiki/summaries/community-<id>.md` with frontmatter `type: summary`, `pipeline: compiled`, `produced_by: /build-graph`, `sources:` listing all member pages.

**Latency profile.** At G2 (5K pages, ~5,700 edges): ~10 minutes per client cron run. At G3 (15K pages, ~50K edges): ~1 hour per client. At G4 (50K pages, ~500K edges per client): ~6 hours per client — runs overnight without user-visible impact. [F: F3 / ClaimScope: A3-graphrag-cron-latency / R: medium / refuted_if: cron exceeds 8 hours at G4 — fallback to community-detection only every 3 days]

**Storage.** ~50-100MB per client at G2 (~150 community summary pages × ~500w each); ~500MB at G3; ~3GB at G4. Acceptable on standard client filesystem.

### §4.2 HippoRAG PPR Index

**Pattern.** HippoRAG / HippoRAG 2 (per knowledge-architecture-deep-research §A.3): hippocampus-inspired LLM + KG + Personalized PageRank (PPR) over typed-edge graph; indexes "entry node importance" for any seed query, enabling 1-hop-expansion retrieval that beats pure dense embeddings on multi-hop reasoning benchmarks.

**Jetix application.** Nightly cron runs `/build-graph --ppr-index` over per-client `edges.jsonl`. Output: `clients/<slug>/swarm/wiki/graph/ppr-index.parquet` (compressed columnar; ~30-50MB at G2; ~200MB at G3; ~1.5GB at G4). At query time, `/ask --multidoc-graphrag` first runs PPR seeded by query-derived entity-list (extracted via local LLM); top-K PPR-ranked nodes (K=30 default) become starting points for typed-BFS expansion; expanded subgraph + community summaries serve as context for final synthesis.

**Why parquet not in-memory networkx.** PPR index is read-mostly (computed nightly; queried throughout day); parquet allows partial column reads (PPR scores per entity-id); Python+pyarrow loads sub-second per query. Avoids the G3 50MB networkx ceiling that breaks A1.

**Open-source PPR libraries (Phase-B implementation gate).** Options: `python-igraph` (BSD; reference); `networkx` (BSD; slow at >10K nodes); `graph-tool` (LGPL; fast but C++ build); `scipy.sparse` + manual PPR loop (BSD; Phase-A acceptable). Phase-B engineering decision per AWAITING-APPROVAL gate. [F: F3 / ClaimScope: A3-ppr-storage / R: medium]

### §4.3 A3-augmented Retrieval Path

`/ask --multidoc-graphrag` (skill extension; new mode flag, not new skill — D11 governance preserved):

**Step 1: Multi-doc intent detection.** Local LLM (Mistral-7B) classifies query: "single-doc retrieval" vs "multi-doc synthesis" vs "global-sensemaking". For multi-doc/global, route to GraphRAG path; otherwise standard A1 Q1 4-tier.

**Step 2: PPR-seeded entity extraction.** Local LLM extracts query entities ("DACH", "outreach", "regulatory"); PPR ranks all per-client entities by importance to query-seed.

**Step 3: Community-summaries first-pass.** Top-3 communities by PPR-ranked entity overlap → load their summary pages → check if summaries answer query directly (≤500 words each; sub-second LLM read).

**Step 4: Typed-BFS expansion.** If summaries insufficient, expand from PPR-top-K nodes via Tier-C typed-BFS depth-2 (per A1 baseline); fetched pages added to context.

**Step 5: Local LLM synthesis.** Combined context (community summaries + expanded pages) → Mistral-7B synthesis (≤2K-word response with inline citations).

**Quality.** GraphRAG benchmarks (knowledge-architecture-deep-research §A.2): 60-90% improvement on global-sensemaking vs flat-RAG baseline. HippoRAG benchmarks (§A.3): 7-30% improvement on multi-hop QA vs naive RAG. Combined: substantial improvement on Jetix's UC-3 + UC-6 query types (apply / cross-project synthesis).

### §4.4 Lifecycle (community summaries as α-2 artefacts)

Community summaries are α-2 artefacts with `type: summary`, `pipeline: compiled`, `state: drafted` (initial) → `accepted` (after first verification by /lint sweep — community-stable for 3+ nights consecutively). When community boundary shifts (Leiden re-clusters), old summaries get `state: superseded`; new summaries `state: drafted`. Audit trail in `swarm/wiki/log.md`. [F: F4 / ClaimScope: A3-summary-lifecycle / R: medium]

### §4.5 Refresh Cadence

A3 builds on A2's per-client wiki + edge-shard substrate. Refresh is nightly (cron). Manual override via `/build-graph --client=<slug> --force-rebuild`. Methodology-push from Jetix-central includes A3 cron config + skill extensions; clients opt in to A3 (some Mittelstand clients may prefer A2-only for simpler ops).

## §5 Use-case Walkthrough (UC-1..UC-10)

### UC-1 — Video Ingest

Same as A2 (per-client). New concept pages + edges added to `clients/<slug>/swarm/wiki/`. **A3 advantage:** new concepts will be community-clustered + PPR-ranked overnight; available in cross-document synthesis from next day. [F: F3 / ClaimScope: UC-1-A3 / R: medium]

### UC-2 — Weekly Digest

A3 enriches digest with COMMUNITY-LEVEL synthesis: "this week, the 'partnership-negotiations' community gained 8 new pages; community summary now covers..." Latency: ≤60s first byte (cached community summaries are pre-computed); ≤90s complete (vs A1's ≤180s). **A3 advantage:** scale-invariant digest latency through G3. [F: F3 / ClaimScope: UC-2-A3-G3 / R: medium]

### UC-3 — Solve-with-Wiki (A3 strength)

Multi-doc synthesis query: *"What's the cross-pattern across our 10 partnership negotiations?"* A3 path: Step-1 detects multi-doc intent → Step-2 PPR ranks "partnership", "negotiation", "objection" entities → Step-3 loads top-3 community summaries (e.g., "vendor-objections-cluster", "regulatory-concerns-cluster", "pricing-pushback-cluster") → Step-4 expands via BFS for specifics → Step-5 Mistral-7B synthesis: *"Recurring objections across 10 negotiations: (1) compliance-uncertainty in 7/10 cases; (2) integration-complexity in 5/10; (3) pricing-anchor against incumbent in 6/10. Pattern: [analysis with 12 inline citations]."* This kind of cross-document reasoning is **architecturally unreachable for A1 and operationally weak for A2 alone** — A3's GraphRAG community pre-compile + PPR index are required. [F: F4 / ClaimScope: UC-3-A3-strength / R: medium]

### UC-4 — Skill Accumulation

A3-augmented: skill validation runs faster because cross-pattern detection is built into community summaries. When Jetix brigadier observes a new decomposition pattern, A3 community-clustering surfaces whether the pattern aligns with existing decomposition-cluster or constitutes a new community. Promotion to `swarm/wiki/global/compound-rules/` informed by community-evidence. [F: F3 / ClaimScope: UC-4-A3 / R: medium]

### UC-5 — Project Onboarding (A3 contribution)

New project's `_moc.md` pulls relevant community summaries (not just individual concept pages) into `related[]`. Onboarding gets richer "what does the wiki know about this domain?" via ≥3 community summaries. ≤30min UC-5 floor preserved (community summaries are pre-computed; lookup is sub-second). [F: F3 / ClaimScope: UC-5-A3 / R: medium]

### UC-6 — Cross-project Insight Transfer (A3 strength)

Pattern in `quick-money-DACH` informs `research-thesis-validation`. A3 community-summaries detect the pattern's community membership; if pattern's community spans BOTH projects' subgraphs, surface as cross-project insight in next weekly digest (per-client; cross-CLIENT only via opt-in case-study). [F: F4 / ClaimScope: UC-6-A3-strength / R: medium]

### UC-7 — Contradiction Detection (A3-augmented)

A3 community summaries explicitly include "contradiction surface" section per §4.1. `/lint` Q5 signal #4 reads community-summary contradiction-surface entries — surfaces contradictions earlier than A1's explicit `contradicts` edge sweep (which depends on prior `/lint` having ingested the contradicting page). Reduces contradiction-detection lag from up-to-1-week (A1) to up-to-overnight (A3). [F: F3 / ClaimScope: UC-7-A3 / R: medium]

### UC-8 — Scale Test (A3 zone of value)

A3's value zone is G2-G5 cross-document synthesis. At G1, over-engineering (cron compute > value); A3 should NOT activate at G1. At G2 (5K pages per client), A3 starts paying off for multi-doc queries; ROI positive. At G3-G4-G5, A3 is mandatory for any query involving >5 documents. [F: F4 / ClaimScope: UC-8-A3-zone / R: medium]

### UC-9 — Client Isolation (A3 inherits A2 STACK; ≥200w)

A3 runs ENTIRELY within per-client UNIX user scope. Cron jobs: `02:00 jetix-client-<slug> /usr/local/bin/build-graph --client=<slug>`. The cron user has read-only access to `clients/<slug>/swarm/wiki/edges.jsonl` + write access to `clients/<slug>/swarm/wiki/summaries/` + `clients/<slug>/swarm/wiki/graph/communities.json` + `ppr-index.parquet`. **Cross-client cron jobs cannot exist** — a `jetix-client-a` UNIX user lacks read on `/clients/client-b/`. A3 community summaries reference per-client pages only; PPR index per-client only. Inheriting A2's defense-in-depth STACK fully (Layer-1 OS perms; Layer-2 separate-repo; Layer-3 13th `holon-ref` edge with `/lint` rejection — community summaries get `holon-ref → client-holon-root` edges; Layer-4 `granularity:client:<slug>` frontmatter on every summary page).

**Pen-test scenario.** Hostile actor compromises Client-A's cron job (e.g., shell injection in skill body). Result: cron user `jetix-client-a` can read client-A's wiki only. Even if attacker writes a malicious community-summary citing fake "client-B leaked" content, the page lives in `clients/client-a/swarm/wiki/summaries/` (Client-A's own tree) — no client-B data is exposed (because attacker cannot read it). Audit log + GPG-signed commits expose the tampering for incident response. [F: F4 / ClaimScope: UC-9-A3 / R: high — inherits A2 / refuted_if: pen-test reveals cross-client read via cron compromise]

### UC-10 — Offline-First Inference (A3 inherits A2 + Mistral-7B; ≥200w)

A3 reads pre-compiled artefacts (community summaries + PPR index) at query time + local LLM synthesis. ENTIRELY OFFLINE for client-private data. The community-summary GENERATION step (nightly cron) uses local LLM (Mistral-7B summarizing each community in 5-10 minutes). The PPR computation is pure numerics (no LLM; sub-second per community). The query-time path is local LLM consuming local artefacts. **Zero outbound network calls for any T-Offline OR T-Hybrid query against client-private data.**

**T-Cloud-only opt-in (optional augmentation).** For benchmark / SOTA / open-source-research queries, client may opt in to T-Cloud-only path that uses cloud LLM with public-data inputs. Never touches client-private data.

**Network-disconnect test.** Client environment: detach NIC overnight before cron runs at 02:00. Cron uses local LLM (Mistral-7B); produces community summaries + PPR index without network. Daytime queries work offline. tcpdump verifies zero outbound network events 24h. [F: F4 / ClaimScope: UC-10-A3 / R: medium / refuted_if: any A3 cron or query session shows outbound TCP to provider endpoint]

## §6 UC-9 + UC-10 Co-located Proof Section (≥400w)

A3 inherits A2's UC-9 + UC-10 architectural commitments and adds two specific A3-flavored mechanisms:

**A3-specific UC-9 mechanism: per-client cron isolation.** Cron jobs are scoped per-client UNIX user (`jetix-client-<slug>` runs `/build-graph --client=<slug>` overnight). The cron config lives at `clients/<slug>/swarm/lib/cron/build-graph.cron` — per-client, not Jetix-central. Client-A's cron job cannot read client-B's edges.jsonl (OS denies). Community summaries + PPR index land only in client-A's `swarm/wiki/`. **Even compromised cron jobs cannot exfiltrate cross-client.** Methodology-push delivers the cron config template; clients opt in to A3 (some may prefer simpler A2-only). The cron orchestration itself is open-source (Linux cron; documented playbook); the per-client INSTANCES are isolated.

**A3-specific UC-10 mechanism: pre-compiled artefacts as offline-synthesis substrate.** Community summaries are PRE-COMPUTED (nightly local-LLM); query-time synthesis reads them as filesystem files (no network). PPR index is PRE-COMPUTED (nightly numerics); query-time PPR scoring reads parquet (no network). The HARDEST offline-first challenge — high-quality multi-document synthesis — is solved by SHIFTING the LLM compute from query-time to overnight-time, where local LLM has 6+ hours of unattended compute budget. This is structurally MORE offline-friendly than A1's on-demand synthesis (which has tighter latency budget at query time) and EQUIVALENT to A2's on-demand-local-LLM (since A3 also uses local LLM).

**Local-LLM family supported.** Same as A2: ollama + Mistral 7B Q4_K_M (default; Apache 2.0); Llama 3.1-8B Q4_K_M alt. **A3-specific consideration:** community-summary generation benefits from larger-context LLM (Mistral 7B = 32K context; Llama 3.1-8B = 128K context — better for large communities). Community-summary quality may benefit from Mixtral-8x7B Q4 (24GB VRAM; longer-context; expert-mixture). Hardware floor: Mistral 7B (16GB GPU); preferred for A3: Llama 3.1-8B+ (24GB GPU) for richer summaries; aspirational: Llama 3.1-70B Q4 (48GB A100) for benchmark-quality summaries (€15K capex per investor §4 — gated by 3-paying-clients + HITL).

**Hosting model alignment.** A3 inherits A2's Path A/B/C support. A3-specific consideration: cron compute is overnight (low-cost rental window; €0.50-1.50/hour per client A100 vs €4-6/hour daytime). For Path B (client-hosted), cron runs on client's hardware (free incremental capex if hardware exists). For Path A (Jetix-hosted VPS in EU), cron runs on shared GPU pool with per-client time-slicing (Hetzner GPU server €350-450/month per A100 amortizes across 5-10 clients).

**Tier split per query.** Same as A1/A2 (T-Offline / T-Hybrid / T-Cloud-only). A3 specifically expands T-Offline coverage to include multi-document synthesis (which without A3 might fall back to T-Hybrid for quality).

**EU compliance alignment.** Same as A2 (GDPR Art. 22 + 32; EU AI Act Art. 14; BSI C5 / ISO 27001 alignment target). A3-specific consideration: the COMMUNITY-SUMMARIES are themselves processed personal data (under GDPR if they reference identifiable individuals); Phase-B clients require an AI-processing data-protection-impact-assessment (DPIA) per GDPR Art. 35 if community summaries contain PII. Mitigation: per-client `tools/redact-pii.sh` runs on summaries before they're read by `/ask`. Phase-B engineering work; Mittelstand-finance clients first to require this. [F: F4 / ClaimScope: UC-9+UC-10-A3-co-located / R: medium]

## §7 Pros / Cons / Tradeoffs

**Pros.** (a) **Best-in-class cross-document synthesis quality** at G2-G5 scales — GraphRAG benchmarks 60-90% improvement on global-sensemaking; HippoRAG 7-30% on multi-hop. (b) **Sub-second query latency at all scales** — pre-compute amortizes the cost. (c) **Fully offline** — community summaries + PPR index + local LLM all run without network. (d) **Inherits A2 UC-9 STACK** — adding cron compute does not weaken isolation. (e) **Anti-fragility through G5** — A3-augmented A2 is the only combination that scales to $1T trajectory without fundamental re-architecture (per systems-scalability §5 + investor-scalability §1).

**Cons.** (a) **Over-engineering at G1** — cron compute compute > value below 3K pages per client; should NOT activate at G1. (b) **Operational complexity** — daily cron jobs across N clients = N cron monitorings; ops engineer overhead. (c) **Storage overhead** — community summaries + PPR index + per-client = 50-500MB per client at G2-G3 (acceptable but non-zero). (d) **Methodology coupling** — community-detection algorithm choice (Leiden vs Louvain vs Infomap) is methodology-shared; client opting out of A3 still pulls the cron config template. (e) **PPR computation on dynamic graphs** — daily re-compute is expensive; incremental PPR is research-grade (Phase-B+ engineering work).

**Tradeoffs.** (1) Pre-compute-cost vs query-latency: A3 trades nightly compute for sub-second daytime queries — almost always Kelly-positive at G2+. (2) Storage vs synthesis-quality: A3 trades 50-500MB per client storage for 60-90% better global-sensemaking — Kelly-positive for any client doing >10 multi-doc queries/week. (3) Operational complexity vs scaling: A3 requires CI cron monitoring + per-client storage budget; pays back at G3-G5 where A1/A2 alone fail. (4) Stand-alone vs augmentation: A3 alone insufficient for UC-9 isolation (needs A2 substrate); A3 is best understood as A2-augmentation-layer.

## §8 Effort Estimate

- **Bootstrap (Day 1 scaffolding):** 1-2 weeks. Limited by: cron infrastructure + `/build-graph` skill extensions for `--communities` + `--community-summaries` + `--ppr-index` flags; parquet storage layer; Leiden algorithm integration (python-igraph or graph-tool).
- **UC-1..UC-4 live (per-client):** 2-3 weeks (after A2 substrate operational + first client at G2). Limited by: first community-summary cron run (overnight) + first PPR index build + local-LLM-summary quality validation against Ruslan-rated golden set.
- **UC-5..UC-8 stable:** 4-6 weeks. Limited by: cross-client A3 deployment + per-client PII-redaction tools (Phase-B GDPR Art. 35 compliance) + Mittelstand-finance client-specific community-summary review.
- **UC-9 + UC-10 live (pen-test + network-disconnect verified):** 2-3 weeks. Limited by: per-client cron isolation pen-test + PII-redaction tool development + offline-LLM community-summary quality benchmarking.

## §9 Migration Path from Current State

A3 builds on A2 (which builds on A1's Phase-A primitives). A3 is activated PER CLIENT at G2 trigger (≥3K pages per client). Migration steps:

1. **Author** `swarm/lib/cron/build-graph.cron` template (per-client cron config).
2. **Extend** `.claude/skills/build-graph.md` with `--communities` + `--community-summaries` + `--ppr-index` flags (engineering Phase-B work).
3. **Add** parquet storage dependency (pyarrow); document in `.claude/config/dependencies.md` (Phase-B AWAITING-APPROVAL gate per cycle-2 OPP-04 dependency-change discipline).
4. **Author** Leiden community-detection wrapper (python-igraph baseline).
5. **Author** PPR computation (scipy.sparse baseline).
6. **Extend** `.claude/skills/ask.md` with `--multidoc-graphrag` flag invoking GraphRAG path.
7. **Author** per-client PII-redaction tool `tools/redact-pii.sh` (NER-based; Phase-B engineering).
8. **Test** community-summary quality against Ruslan-rated golden set (≥20 queries; require ≥80% acceptable per Ruslan-binary).

**Staging order.** Steps 1-3 (config + deps) parallel. Steps 4-5 sequential (PPR depends on community detection). Step 6 sequential after step 5. Step 7 parallel with steps 4-6. Step 8 sequential.

**Rollback.** Each client may opt out of A3 (cron disabled); falls back to A2 standalone retrieval. Worst-case rollback: delete `clients/<slug>/swarm/wiki/summaries/` + `graph/communities.json` + `graph/ppr-index.parquet`; clients reverts to A2.

## §10 Horizon Projection (≥600w; 5 gates)

| Gate | Pages/client | Clients | A3 active | Physical failure | Upgrade path | MHT event | BOSC-A-T-X | Janus risk | Per-client compute |
|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | ~500 | 1 | NO | A3 over-engineering at <3K pages; cron compute > value | A3 deactivated | — | — | — | none (A1/A2 sufficient) |
| **G2 €200K** | ~5,000 | 10 | YES (selectively per-client) | community summary generation at 10 clients × 1h cron = 10h overnight if serialized; storage ~50MB/client = 500MB total | parallel cron (jobs run concurrently per-client UNIX user); shared GPU pool with time-slicing; cap A3 activation to clients with ≥10 multi-doc queries/week | Phase Promotion (cron from manual to scheduled); first emergence of pre-compile pattern | Operation + Composition | medium INT (clients dependent on cron-availability); medium S-A (Jetix-central monopoly on community-detection algorithm choice) | Mistral-7B-Q4 nightly (3-6h per client) on rented GPU pool €0.50-1.50/h overnight |
| **G3 €1M** | ~10,000 | 50 | YES (default for most) | nightly cron orchestration overhead; PPR re-compute on full graph each night = expensive; Leiden community-shift creates summary-supersession churn | Incremental PPR (research-grade — Phase-B+); community-stability heuristic (only re-compute when significant edge-delta); CI cron monitoring at portfolio level | Role-Lift (cron orchestration becomes a sub-roy responsibility per Lock 21); Phase Promotion of community-detection method (algorithm choice elevated to methodology decision) | Composition + Operation + Scale | high INT (50 clients all dependent on Jetix-central cron config); medium S-A (sub-roy autonomy on PPR algorithm choice) | per-client GPU procurement gate (≥3 paying clients per GPU pool segment); aggregate ~50 GPU-hours nightly = €150-250/night = €4-7K/month at G3 (acceptable per investor §4) |
| **G4 $100M** | ~30,000 | 500 | YES (mandatory) | cron compute at 500 clients × 6h = 3000 GPU-hours nightly; storage ~3GB/client × 500 = 1.5TB total; community-summary supersession rate at scale; methodology version coherence on community-detection algorithm | Distributed cron orchestration (Kubernetes / Nomad); per-region GPU pools (EU East, EU West, EU North per data-residency); Mittelstand-LLM (per Strategic Insight §8 rec 7) replaces Mistral-7B as Alliance-blessed default | Fission (per-region cron orchestration separates from Jetix-central); Continuous Phase-Promotion of summary-detection algorithm | eXternal + Composition + Operation + Agency | pervasive (mitigated by quarterly Alliance methodology parliament + per-region sub-roy autonomy) | Mittelstand-LLM 13B-equivalent (€50-100/h GPU rental at G4 scale aggregated; ~€20-30K/month total) |
| **G5 $1T** | ~80,000 | 5000+ | YES (Alliance standard) | per-Alliance-member full-stack autonomy creates per-roy methodology drift; community-detection algorithm fragmentation across roys; PPR coherence challenged at federated scale | Federated cron orchestration; Alliance methodology parliament adjudicates community-detection algorithm version; statistical convergence on community-summary quality across roys (philosophy-scalability §6 outcome-telemetry) | Continuous Fusion (Alliance-shared community-detection methodology); Re-Phase-Promotion at every Alliance methodology release | eXternal + Composition + Agency + Time | pervasive (mitigated by Alliance parliament + statistical telemetry convergence + outcome-level falsification) | per-Alliance-member sovereign compute; Mittelstand-LLM 70B+ default; aggregate ~10K GPU-hours/day across federation |

**Antifragility verdict.** A3 is the **MOST antifragile variant at G3-G5 cross-document synthesis use cases** (community-summary quality improves with scale because more pages → richer communities → better summaries). At G1-G2 it is over-engineering and should NOT activate. **Optimal sequencing: A1 Phase-A → A2 Phase-B at G2 → A2+A3 hybrid at G3.** [F: F4 / ClaimScope: A3-horizon / R: medium]

## §11 Anti-Fragility Assessment (≥400w)

**Verdict: TRUE ANTIFRAGILE at G3-G5; OVER-ENGINEERED at G1-early-G2.**

**Mechanism for true antifragility G3-G5.** Per Kauffman adjacent-possible (systems-expert §9): each new client's wiki contributes new communities + new PPR-significant entities; the community-detection algorithm's quality COMPOUNDS with graph density. At G3 (50 clients × 10K pages), the methodology-level community-detection algorithm sees more variety than at G1; tunable parameters (Leiden resolution; PPR teleportation factor) optimize via outcome telemetry across clients. The synthesis quality GETS BETTER with scale, not just survives. **This is the GraphRAG / HippoRAG research community's central claim**: pre-compiled retrieval-augmentation patterns are antifragile to graph density beyond a threshold (~3K nodes per cluster).

**Mechanism for over-engineering at G1.** Below 3K pages per client, community detection produces ≤10 trivial clusters (e.g., "concepts" / "sources" / "comparisons"); summaries are mere category labels; PPR rankings are dominated by raw degree (no information beyond grep+BFS). Compute cost (~30 min nightly cron) > value. **A3 should NOT activate at G1.**

**Pressure tests.**

(1) **Community boundaries shift overnight (Leiden re-cluster).** Old summaries get `state: superseded`; new summaries `state: drafted`. `/lint` detects supersession; updates `meta/health.md` summary-version count. Daytime queries use new summaries. **Antifragile because:** the transition is auditable; old summaries archived for rollback; supersession churn rate bounded by community-stability heuristic (re-cluster only when edge-delta >5% per night).

(2) **Cron job fails on one client (e.g., GPU OOM at G4).** That client's community summaries stale by 1 day; PPR index stale; query latency increases (falls back to A2 standalone). Operator pages alert from per-client `meta/health.md`. **Antifragile because:** failure is bounded per-client (OS isolation per UC-9); other clients unaffected; failure surfaces signal (need bigger GPU OR algorithm tweak).

(3) **Methodology v1.6 changes community-detection algorithm Leiden→Louvain.** Each client opts in (HITL gate per methodology-push protocol). Some clients opt in immediately; some wait. After 4 weeks, telemetry shows Louvain produces 15% better summary quality on Mittelstand-finance clients but 5% worse on consulting clients. Methodology v1.7 makes algorithm per-client-configurable. **Antifragile because:** algorithm-choice variation across clients SURFACES the trade-off; methodology evolves to capture it.

(4) **Adversarial query: "Find all clients with deals over €100K"** (cross-client by intent). A3 cannot answer — cron isolation prevents cross-client community summaries. UC-9 by construction holds. **Antifragile because:** the adversarial query SURFACES the boundary; product-marketing redirects to opt-in case-study mode (anonymized). [F: F4 / ClaimScope: A3-anti-fragility / R: high]

## §12 Open Questions for Ruslan

1. **A3 activation gate per client:** automatic at first 3K-pages crossover, OR manual opt-in per client?
2. **Community-detection algorithm default:** Leiden (best per knowledge-architecture-deep-research) OR Louvain (faster but lower-quality) OR Infomap (information-theoretic; experimental)? Authorize Phase-B benchmarking?
3. **PPR library default:** python-igraph (BSD; reference) OR scipy.sparse (lighter; manual implementation) OR graph-tool (LGPL; fastest but C++ build)?
4. **GPU rental vs owned for A3 nightly cron:** rental at G2 (€0.50-1.50/h overnight); owned at G3+ (€15K capex per A100 amortized across 5-10 clients per investor §4)?
5. **A3 community summaries as PII risk:** acknowledge GDPR Art. 35 DPIA requirement for clients where summaries may contain identifiable individuals; commit to per-client PII-redaction tool Phase-B?
6. **A3 vs A2-only choice per client:** default A2-only (lighter) for SMB Path-B clients; A3 default for enterprise Path-A/Path-C clients with multi-doc query volume?

— brigadier (Phase-5 variant draft), 2026-04-24
