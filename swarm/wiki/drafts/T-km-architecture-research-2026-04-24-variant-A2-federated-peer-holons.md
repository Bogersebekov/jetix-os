---
title: Variant A2 — "Federated peer-holons (per-client autonomous holons + Jetix-methodology-holon)"
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
confidence_method: brigadier-integration-from-systems-integrator-and-tier1
tier: tier-1
produced_by: brigadier
sources:
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-integrator-layerA-layerB-holarchy.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-optimizer-minimal-extensions.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-systems-scalability-both-layers-horizon.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-engineering-integrator-layerA-candidate.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-philosophy-integrator-epistemic-overlay.md"}
  - {path: "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-integrator-moat-synthesis.md"}
  - {path: "design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md", range: "D1, D3 §3.5, D5"}
  - {path: "decisions/FPF-ENHANCEMENT-FOR-DOMAIN-EXPERTS-2026-04-23.md", range: "Part 8 holon mereology, E-11 Janus, E-12 graph-of-creation"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§§3-6"}
  - {path: "raw/research/2026-04-24-bios-clone-wars-jetix-ai-parallel.md", range: "§11 Урок 1, §13 Mittelstand applications"}
related: []
binding_scope: km-architecture-variant-A2
---

# Variant A2 — "Federated Peer-Holons (per-client autonomous holons + Jetix-methodology-holon)"

## §1 Name + One-line Pitch

**A2 — Federated Peer-Holons : each Jetix client deployment is a structurally-autonomous peer holon (own swarm/wiki/, own edges.jsonl, own agent instances), federated to a Jetix-methodology-holon via push-only methodology-update protocol, with cross-holon edges architecturally forbidden via 13th `holon-ref` edge type + hard `/lint` rejection, OS-level filesystem permissions, and per-client JSONL edge-store sharding (Ashby requisite-variety).** [F: F4 / ClaimScope: KM-architecture-Phase-B-production / R: medium]

## §2 Axis of Differentiation (~110w)

This variant occupies the **ontological-layered / federated-peer-holons / by-construction-isolation** quadrant. Variant A1 occupies *retrieval-lean / write-heavy / filesystem-native (single-tenant default)*. Variant A3 occupies *pre-compiled-heavy / graph-native (community summaries + PPR index)*. Choice between them governed by: (1) **client-count expectation** — A2 mandatory at ≥2 simultaneous paying clients; (2) **isolation rigor** — A2 is the only variant providing UC-9 by construction at OS+graph+filesystem layers (defense-in-depth STACK per philosophy-integrator §3); (3) **operational team** — A2 needs ≥2 ops engineers at G2+ for per-client repo provisioning + CI methodology-push fan-out; (4) **horizon trajectory** — A2 antifragile through G4 (per systems-scalability §4), aligning with $1T trajectory (D19) without re-architecture. [F: F4 / ClaimScope: A-variants-axis-of-diff / R: high]

## §3 Architecture Diagram

```mermaid
graph TD
    subgraph "Jetix-methodology-holon (closed-implementation, open-interface)"
      MethRepo[jetix-methodology-repo<br/>swarm/wiki/themes/<br/>swarm/wiki/foundations/<br/>swarm/lib/<br/>.claude/agents/<br/>.claude/skills/]
      MethRepo -->|push-only| ClientA
      MethRepo -->|push-only| ClientB
      MethRepo -->|push-only| ClientN[...]
    end

    subgraph "Client-A holon (autonomous)"
      ClientA[clients/client-a/<br/>own swarm/wiki/<br/>own edges.jsonl shard<br/>own agent instances<br/>OS user: jetix-client-a]
      ClientA --> ClientALLM[ollama+Mistral-7B local]
      ClientA --> ClientAOps[Path B: client-hosted<br/>OR Path A: Jetix VPS EU]
    end

    subgraph "Client-B holon (autonomous)"
      ClientB[clients/client-b/<br/>own swarm/wiki/<br/>own edges.jsonl shard<br/>own agent instances<br/>OS user: jetix-client-b]
      ClientB --> ClientBLLM[ollama+Mistral-7B local]
    end

    subgraph "Cross-holon protections"
      Lint[/lint signal L-CROSS-HOLON-REF<br/>rejects 13th holon-ref edges<br/>across client-holon-roots]
      OSPerms[OS-level permissions<br/>jetix-client-a CANNOT read /clients/client-b/]
      AlphaScope[α-2 artefacts only — no cross-client α-5 Direction]
    end

    Lint -.->|enforces| ClientA
    Lint -.->|enforces| ClientB
    OSPerms -.->|enforces| ClientA
    OSPerms -.->|enforces| ClientB
    AlphaScope -.->|enforces| ClientA
    AlphaScope -.->|enforces| ClientB

    Optional[Optional opt-in case-study<br/>HITL-mediated anonymized<br/>methodology contribution] -.->|opt-in only| MethRepo
```

## §4 Mechanics (~1500w)

### §4.1 Holarchy Structure

A2 declares a **peer-holon topology** (per FPF Part 8 §8.1 Rule A + systems-integrator §1.2 A2 view). The topology has two holon-classes:

**Class-1: Jetix-methodology-holon.** Single instance. Contents: `swarm/wiki/themes/`, `swarm/wiki/foundations/`, `swarm/lib/` (shared-protocols + hooks), `.claude/agents/` (5 expert prompts + brigadier), `.claude/skills/` (5 in-scope skills), `decisions/` (Tier-1 spec docs), `raw/research/` (open-research distillations). The methodology-holon is what Jetix versions, ships, and maintains. **No client data here.** Maps to BIOS analogue: the published methodology-API spec + reference implementation (BIOS-research §13 Решение 2: "documentation + IP/licensing"). [F: F4 / ClaimScope: holarchy-class-1 / R: high]

**Class-2: Client-holon (one per Jetix client).** Multiple instances. Contents: per-client `swarm/wiki/` tree (concepts, sources, claims, comparisons, ideas, experiments, summaries, foundations — all client-specific), per-client `edges.jsonl` shard (NOT shared with any other client), per-client agent instances (separate process per `WIKI_ROOT_CLIENT_ID`), per-client `meta/health.md`, per-client `agents/<expert>/strategies.md`. Maps to BIOS analogue: each motherboard's BIOS implementation — published interface (Jetix methodology), closed implementation (client-private KB) per Strategic Insight §4. [F: F4 / ClaimScope: holarchy-class-2 / R: high]

**Mereology semantics.** Per FPF Part 8 6 rules:
- Rule A (peer holons): Jetix-methodology-holon is a PEER of every client-holon (NOT a parent). A1 default would have placed clients as Level-3 supersystem — A2 explicitly REJECTS containment per systems-critic H-3 + Strategic Insight §3 rationale.
- Rule B (atomicity): each holon is atomic at its boundary; cross-holon access requires explicit `methodology-push-supersedes` channel (one direction only).
- Rule C (recursion): each client-holon may itself spawn sub-holons (project-holons per Layer-B B2 variant), recursively.
- Rule D (autonomy): each client-holon's α-1..α-4 alphas are scoped within the holon; α-5 Direction is HITL-mediated within the holon (no cross-client α-5 — per systems-optimizer H-4 refusal preserved).
- Rule E (identity): each holon has a unique slug + signing key (Phase-B GPG-signed git commits).
- Rule F (boundary): cross-holon edges of any type other than `methodology-push-supersedes` are FORBIDDEN per `/lint` L-CROSS-HOLON-REF signal.

### §4.2 13th Edge Type `holon-ref` + `/lint` enforcement

Per systems-optimizer Δ1 (AWAITING-APPROVAL per D3 §3.5; gate file landed in this cycle's Ruslan packet), A2 introduces the 13th edge type:

```yaml
holon-ref:
  semantics: directed edge from a client-scoped wiki page to that client's holon-root manifest file
  cardinality: many-to-one (many pages → one holon-root)
  lint_signal: L-CROSS-HOLON-REF
  lint_rule: REJECT any holon-ref edge whose target lies outside the source's resolved client-holon-root
```

**Why a 13th edge (not reuse of `derived_from`):** semantic fidelity. `derived_from` is general; `holon-ref` is specifically isolation-bearing. At G4 (50K cross-client merged edges in any flat store), filters on `granularity` become performance-pathological — Ashby variety mismatch (per systems-critic H-5). The 13th edge passes critic survival per philosophy-integrator §3 (semantically distinct from existing 12-enum). [F: F4 / ClaimScope: 13th-edge-justification / R: medium / refuted_if: pen-test confirms alternative `derived_from` + `granularity` filter restores Ashby balance at G4]

### §4.3 Per-client JSONL Edge-store Sharding

Per systems-optimizer Δ-5 (Ashby requisite-variety mandate), A2 stores edges per-client:
- Jetix-methodology-holon: `swarm/wiki/graph/methodology-edges.jsonl`
- Client-A holon: `clients/client-a/swarm/wiki/graph/edges.jsonl`
- Client-B holon: `clients/client-b/swarm/wiki/graph/edges.jsonl`

**Sharding rationale.** At G2 (10 clients × 5K pages × 5,700 edges/client = 57K total edges), a flat store crosses the 50MB networkx ceiling; sharded stores stay <6MB per client (sub-second BFS per shard). At G4 (500 clients × 10K edges/client = 5M edges), flat store is impossible; sharded stays sub-second per query because retrievals are scoped to client-holon-root. Same record schema as 12-enum + 13th `holon-ref`; no record-format change. [F: F4 / ClaimScope: sharding-rationale / R: high]

### §4.4 Methodology-push Protocol (one-way)

Jetix releases methodology updates as versioned snapshots (e.g., `jetix-methodology@v1.4.0` git tag). Each client-holon pulls (or has pushed via CI) the new version into a `methodology/` submodule (or sibling repo). The pull triggers a per-client `/lint --methodology-update` sweep: validates that new methodology version preserves WLNK/MONO/IDEM/COMM/LOC against prior; flags any deprecated edges/templates/skills. Client opts in to apply (HITL gate per critic-gate1 H-fix; never auto-apply). **No reverse data flow:** client's wiki content NEVER pushed back to Jetix-methodology-holon. Optional opt-in case-study: anonymized abstract pattern (no client content) goes to Jetix-methodology-holon's `case-studies/` with explicit HITL ack per UC-7×UC-9 protocol. [F: F4 / ClaimScope: methodology-push / R: high]

### §4.5 Per-client Agent Instances

Each client-holon gets its own brigadier + 5 expert instances. **Different process** per `WIKI_ROOT_CLIENT_ID`. Separate `agents/brigadier/strategies.md` (Layer-2 personal memory accumulates client-specific patterns — but never leaks to other client-holons because filesystem isolation). Separate `swarm/mailboxes/`, `swarm/logs/`, `swarm/gates/`. **No shared mutable state.** Exception: methodology updates flow ONE-WAY from Jetix-methodology-holon's `.claude/agents/` to client-holon's `.claude/agents/` via methodology-push (§4.4). [F: F4 / ClaimScope: per-client-agent-instances / R: high]

### §4.6 Lifecycle (α-2 + α-3 + α-5 per client-holon scope)

**α-2 Artefact:** scoped within client-holon. Drafts under `clients/<slug>/swarm/wiki/drafts/`; canonical under client's spine. No cross-holon promotion.

**α-3 Strategies-Rule:** per-client `agents/<expert>/strategies.md`. Promotion to client's `swarm/wiki/global/compound-rules/` per W-5 Level-2 (within-holon only). Cross-client promotion REQUIRES anonymized abstraction + HITL ack (per §4.4 case-study protocol).

**α-5 Direction:** per-client. NOT shared with Jetix-central. Per philosophy-scalability §3 / systems-optimizer H-4: per-client α-5c not added as new alpha (D5 method-change refusal); instead, per-client direction-hypothesis tracked as `type: direction-hypothesis` in α-2 artefact lifecycle with `granularity: client:<slug>` field. Methodology-shared direction (Jetix-central) remains canonical α-5 in Jetix-methodology-holon. [F: F4 / ClaimScope: per-client-alphas / R: medium]

## §5 Use-case Walkthrough (UC-1..UC-10)

### UC-1 — Video Ingest (per-client)

Client-A's Ruslan-equivalent ingests a Mittelstand-DACH-specific lecture (e.g., "BSI C5 compliance for SaaS"). `/ingest raw/transcripts/2026-04-XX-bsi-c5-overview.md` runs in client-A's brigadier process (`WIKI_ROOT_CLIENT_ID=client-a`). Concept pages + edges land in `clients/client-a/swarm/wiki/concepts/` + `clients/client-a/swarm/wiki/graph/edges.jsonl`. Methodology-update mechanism unchanged — Jetix-central never sees this content. [F: F4 / ClaimScope: UC-1-A2 / R: high]

### UC-2 — Weekly Digest (per-client)

Client-A's Monday digest queries client-A's wiki only. No cross-client aggregation. Latency same as A1 (sub-second BFS at G1; ~500ms at G2 per shard). Citations reference client-A pages only. [F: F4 / ClaimScope: UC-2-A2 / R: high]

### UC-3 — Solve-with-Wiki (per-client + opt-in cross-methodology)

Client-A asks: *"Apply systems-thinking to our DACH outreach"*. Q1 retrieval scoped to client-A holon + Jetix-methodology-holon's `themes/systems/` + `themes/sales/` (READ-ONLY across methodology boundary; no client-A pages flow to methodology-holon). Synthesis local LLM (Mistral-7B); response cites client-A's outreach pages + Jetix methodology pages. Filing-loop write-back to `clients/client-a/swarm/wiki/comparisons/`. [F: F4 / ClaimScope: UC-3-A2 / R: high]

### UC-4 — Skill Accumulation (per-client + methodology-back via opt-in)

Client-A's brigadier discovers a novel decomposition pattern. Pattern accumulates in `clients/client-a/agents/brigadier/strategies.md`. After ≥10 uses + ✓/✗ ≥ 3:1 within client-A, promotion to `clients/client-a/swarm/wiki/global/compound-rules/`. **Cross-client/back-to-methodology:** Ruslan opts in (HITL gate); pattern abstracted (no client-specific data) → submitted as case-study to Jetix-methodology-holon's `case-studies/<anonymous-id>.md`; Jetix brigadier reviews + may promote to methodology version v1.5 if widely applicable. [F: F4 / ClaimScope: UC-4-A2-cross-methodology / R: high]

### UC-5 — Project Onboarding (per-client per-project)

New client-A project (e.g., "Q3 partnership negotiations"). Client-A's brigadier dispatches `mgmt × integrator` (Layer-B B2 specifies the per-project scaffold). New `clients/client-a/swarm/wiki/operations/q3-partnerships/` namespace with mini-swarm allocation (per B2). ≤30 min scaffold + thesis draft + topic-wiki links to client-A's `themes/business/`. UC-5 traced fully in B2. [F: F3 / ClaimScope: UC-5-A2-stub / R: medium]

### UC-6 — Cross-project (within-client only by default)

Pattern in client-A's `quick-money-DACH` informs client-A's `research-thesis-validation`. Within-client cross-project transfer via existing `derived_from` edge + filing-loop. Cross-CLIENT transfer FORBIDDEN by construction (no `holon-ref` edge crosses client-holon-roots; `/lint` rejects). Optional case-study mode: HITL-mediated anonymized contribution to Jetix-methodology-holon, which other clients may then pull via methodology-push. [F: F4 / ClaimScope: UC-6-A2 / R: high]

### UC-7 — Contradiction Detection (per-client + methodology-only Jetix-central)

Per philosophy-integrator §4 contradiction-handling protocol: per-client `/lint` runs scoped to client-holon (e.g., client-A's contradictions surface in client-A's `meta/health.md`); Jetix-central `/lint` runs over methodology-only artefacts (Jetix-methodology-holon's `themes/` + `foundations/` + `decisions/`). Cross-client contradictions surface ONLY in opt-in case-study mode. **UC-7×UC-9 tension dissolved** per philosophy-scalability §6 outcome-level vs content-level distinction: methodology claims testable across clients via anonymized acceptance-predicate telemetry; per-client KB content never crosses holon boundary. [F: F4 / ClaimScope: UC-7-A2 / R: high]

### UC-8 — Scale Test (preview; full §10)

A2 scales to G4 by construction without architectural change (only operational complexity grows: more client-holons, more methodology-push runs, more sub-roy coordination). G5 requires Fusion event into multi-roy meta-wiki (Mittelstand AI Alliance federation). [F: F4 / ClaimScope: UC-8-A2 / R: high]

### UC-9 — Client Isolation (architectural proof BY CONSTRUCTION; ≥200w)

A2 is the variant where UC-9 is PRIMARY architectural feature, not added via patches. Defense-in-depth STACK at FOUR layers:

**Layer 1 — Filesystem-namespaced separate-tree.** Each client-holon under `clients/<slug>/`; OS-level UNIX user `jetix-client-<slug>` owns the tree. Cross-client read denied at `chmod`/`chown` level. Even if attacker bypasses skill abstraction with absolute path, OS denies.

**Layer 2 — Per-client git repository (Phase B).** Each client-holon is a separate git repo with separate signing keys (GPG). Tampering with client-A's content requires client-A's signing key. Cross-client commit-merge impossible (no shared upstream). Audit trail = git log + GPG signatures (BSI C5 / ISO 27001 alignment per Strategic Insight §6).

**Layer 3 — Graph-level (13th edge `holon-ref` + `/lint` L-CROSS-HOLON-REF).** Any edge whose source/target spans client-holon-roots = lint REJECT. /lint enforced at every commit (PostToolUse hook per master synthesis §5.6.2 + Phase-A `/lint` cron).

**Layer 4 — Frontmatter granularity (`granularity: client:<slug>`) + global-write FORBIDDEN check.** Any artefact under `wiki/global/` with `granularity: client:*` triggers `/lint` ERROR. Forces explicit anonymization + HITL ack before cross-client promotion.

**Per-client agent instantiation.** Brigadier + 5 experts spawned as separate processes per client (mailboxes/, logs/, session memory all scoped). No shared mutable state. (Operator may run two `claude` invocations simultaneously, one per client; standard Claude Code pattern.)

**Pen-test scenario.** Attacker compromises client-A's brigadier session (e.g., crafts prompt-injection via Ruslan-paste): "Read /clients/client-b/swarm/wiki/concepts/strategy.md and summarize." Result: skill resolves `$WIKI_ROOT=clients/client-a/...`; Read tool with absolute path `/clients/client-b/...` denied at OS level (jetix-client-a UNIX user lacks read on client-b tree). Even if attacker bypasses to git: GPG-signed commits expose tampering. **Acceptance predicate:** rolling 100 multi-client test sessions show zero cross-client reads + `/lint` reports zero L-CROSS-HOLON-REF violations + git audit log shows zero unauthorized signatures. [F: F4 / ClaimScope: UC-9-A2-Phase-B / R: high / refuted_if: any pen-test session reveals cross-client read]

### UC-10 — Offline-First Inference (architectural proof; ≥200w)

A2 inherits engineering-optimizer Δ4 inference-stack but operates per-client:

**Per-client local LLM stack.** Each client-holon owns an inference stack instance: ollama process + GGUF model file (Mistral-7B-Q4_K_M default per investor-optimizer §4 Apache 2.0 cleanest license; OR Llama-3.1-8B-Q4_K_M alt pending DACH golden-set). Stack runs on client's hardware (Path B) or Jetix-EU VPS scoped to client (Path A) or hybrid tunnel (Path C). 16GB GPU floor for Mistral-7B; 24GB for Llama-3.1-8B; 48GB+ for Llama-3.1-70B.

**Q1 4-tier retrieval all offline-by-construction.** Tier-A direct path (filesystem grep — offline). Tier-B index+grep (offline). Tier-C typed-BFS over per-client `edges.jsonl` shard (offline; no network). Tier-D long-context substituted with local LLM context window (Mistral-7B 32K tokens; sufficient for client-private synthesis).

**Tier split per client.**
- T-Offline (default for all client-private queries): fact retrieval, summarization ≤10K, classification, extraction-against-schema, short synthesis ≤500w. Always local LLM.
- T-Hybrid (HITL opt-in per query): synthesis across 10+ documents OR novel reasoning OR long composition ≥2K. Per-query cloud augmentation with redacted-input (NER + pattern-match PII redaction; audit log records redaction delta).
- T-Cloud-only (public-data queries; never client-private): SOTA citations, benchmark lookups, open-source code search.

**Network-disconnect test.** Client environment: detach NIC. Issue substantive query: "Summarize Q1 partnership negotiations and extract recurring objections." Local LLM synthesis from per-client wiki retrieval. Expected: response with citations to client-A pages. tcpdump verifies zero outbound network events.

**Acceptance predicate.** Per-client inference stack returns synthesis to substantive query against client-private data with zero outbound network calls (tcpdump-verified). [F: F4 / ClaimScope: UC-10-A2 / R: high / refuted_if: tcpdump shows outbound provider connection during T-Offline query]

## §6 UC-9 + UC-10 Co-located Proof Section (≥400w)

A2 is the variant where UC-9 + UC-10 are **structurally inevitable**, not architecturally bolted on. The peer-holon topology IS the isolation mechanism; the per-client local-LLM stack IS the offline-first mechanism. Both follow from the same architectural commitment: each client deployment is a structurally-autonomous system with a well-defined federation interface (methodology-push) but no shared runtime state.

**Isolation model: federated peer-holon (Phase-B by-construction at OS+graph+filesystem layers).** Phase-B onset is the gate for full A2 — Phase-A operates A1 with policy+config layer (env-var + directory-namespace + frontmatter granularity). The transition trigger is "first paying client onboarding" (G2 entry per investor-optimizer §3 + mgmt-scalability §1). At Phase-B onset, Jetix-central spawns the first client-holon: `clients/<first-client-slug>/` git repo + UNIX user + ollama instance. Methodology-push is established. /lint cross-holon rejection activates. UC-9 by construction at all 4 stack layers from this moment.

**Local-LLM family supported.** Default: ollama + Mistral 7B Q4_K_M (Apache 2.0 — cleanest license for Mittelstand commercial deployment per investor-optimizer §4 §dissent-D-2 resolution path; 8GB VRAM floor; €700-1K capex if owned; €60-120/month Vast.ai rental; 3-6s p95 latency for 500-token synthesis). Alternative: Llama 3.1-8B Q4_K_M (Llama Community License with ≤700M MAU clause — verify per client; 16GB VRAM floor; 4-8s latency; pending 20-query DACH golden-set evaluation). Future evaluation: DeepSeek V3 Lite (license review on "non-competing applications"; 24GB VRAM; 5-10s latency); Phi-3-mini (Microsoft license review; 4GB VRAM; faster); Qwen 2.5 (Alibaba license review). Stack manifest: `clients/<slug>/swarm/lib/inference-stack.yaml` per-client (allows client-specific model choice).

**Hosting model alignment.** A2 supports all 3 paths cleanly:
- **Path A (Jetix-hosted VPS in EU; Hetzner / OVH):** Jetix operates one VM per client; each VM has separate UNIX user; each runs ollama + per-client wiki repo. ~70% GM at €15K/yr per investor §4 (knife-edge; viable for low-touch SMB).
- **Path B (Client-hosted; preferred Phase-A default per investor Δ-H3):** Client owns hardware; Jetix ships methodology; 70.7% GM at €3K onboarding + €15K/yr recurring (clears 70% floor); 80.8% GM recurring yr 2+. Best fit for self-sufficient technical clients.
- **Path C (Hybrid: Jetix agent-swarm + client KB tunnel):** Jetix operates swarm in EU VPS; client's KB stays on client's filesystem; secure (mTLS) tunnel between. 54% GM at €15K/yr (fails Phase-A floor — viable from G2 post-contractor-#1 per investor §6); 82% GM at €50K enterprise tier. Best fit for compliance-strict enterprise clients (Mittelstand finance / health / defense).

**Tier split (T-Offline / T-Hybrid / T-Cloud-only).** Per UC-10 §5; same as A1 but per-client.

**EU compliance alignment.**
- **GDPR Art. 22** (automated decision-making): local LLM keeps client data on-prem; no automated decision-making by Jetix-central on client data.
- **GDPR Art. 32** (security of processing): OS-level UNIX permissions + GPG-signed commits as ambient attestation + audit trail in per-client `swarm/logs/` + `meta/health.md`.
- **EU AI Act Art. 14** (human oversight): HITL gate on T-Hybrid opt-in cloud-augmentation.
- **EU AI Act Art. 9, 10, 13** (risk classification): Mittelstand consulting workflows = limited-risk; client-specific risk classification documented in per-client `wiki/foundations/<slug>/risk-classification.md`.
- **BSI C5 / ISO 27001 alignment target:** signed `sources[]` provenance + `/lint` signature validation extending Q5 signal set (investor-critic Δ-H6 future delta); per-client audit log; access-control via OS UNIX permissions; data residency (EU-only deployment) ; encryption-at-rest on client filesystem + transport encryption (TLS).

**Pen-test + network-disconnect tests outlined in §5 UC-9 + UC-10.** Both produce binary acceptance-predicates verifiable via standard tools (tcpdump, audit log, /lint runs). [F: F4 / ClaimScope: UC-9+UC-10-A2-co-located / R: high]

## §7 Pros / Cons / Tradeoffs

**Pros.** (a) **Only variant antifragile through G4 by construction** — per systems-scalability §4. Each new client adds a holon instance reusing ≥70% of methodology template with zero schema modification. (b) **UC-9 by construction at OS+graph+filesystem+frontmatter layers** — defense-in-depth STACK preferred by philosophy-integrator §3. (c) **EISA-moment alignment** — A2's federation topology IS the BIOS clean-room/EISA structural analog (Strategic Insight §3-§4). (d) **Auditability** — per-client GPG-signed commits + audit log = compliance-ready Phase B.

**Cons.** (a) **Highest setup overhead at G1** — per-client repo provisioning + OS user + ollama install: ~2 days for first client (subsequent ≤2h via script per engineering-scalability §8). (b) **CI methodology-push fan-out is the G2-G3 critical engineering investment** — manual git-push to 10+ client repos = ~2h/week operator time; CI automation = ~1-2 weeks engineering work. (c) **Higher per-client ops cost than A1** — separate ollama process per client (~€60-120/month rental), separate VPS (Path A) or client-hardware (Path B). (d) **Cross-client insight transfer FORBIDDEN by default** — case-study opt-in mode is HITL-mediated; novelty-extraction across clients slower than A1 cross-project.

**Tradeoffs.** (1) Setup-overhead vs by-construction-isolation: A2 chooses 2-day first-client setup for permanent UC-9 guarantee. (2) Centralized-knowledge-pool vs federated-autonomy: A2 sacrifices Jetix-central's "knowledge-pool grows with every client" for the strategic moat of "client KB never leaves client's server." (3) Operational simplicity vs compliance-readiness: A2's per-client audit trail is BSI C5 / ISO 27001 ready — but operationally heavier than A1's single-tenant. (4) Phase-A activation cost vs Phase-B antifragility: pre-investment in A2 substrate at G2 (rather than G3 forced migration) is Kelly-positive per investor-optimizer §2.

## §8 Effort Estimate

- **Bootstrap (Day 1 scaffolding):** 12-20 hours. Limited by: per-client repo template authoring + UNIX user provisioning script + ollama install playbook + GPG signing-key bootstrap + methodology-push CI pipeline scaffold.
- **UC-1..UC-4 live (per-client):** 1-2 weeks (after first client-holon spawned). Limited by: per-client wiki bootstrap + initial methodology-push + first sync.
- **UC-5..UC-8 stable (per-client + cross-client federation):** 6-8 weeks. Limited by: ≥3 client-holons operational + first methodology-update cycle (push v1.0 → v1.1 → client opt-in apply) + first opt-in case-study extraction.
- **UC-9 + UC-10 live (pen-test + network-disconnect verified):** 3-4 weeks. Limited by: pen-test scenario authoring + tcpdump verification + Llama vs Mistral DACH golden-set evaluation (resolves dissent D-2) + Phase-B 13th edge AWAITING-APPROVAL gate ack + `/lint` L-CROSS-HOLON-REF + L-CROSS-CLIENT-GLOBAL signal authoring.

## §9 Migration Path from Current State

A2 builds on A1's Phase-A primitives; A2 IS the Phase-B target state. Concrete migration steps (all scheduled at G2 first-paying-client onset):

1. **Create** Phase-B AWAITING-APPROVAL packet for D3 §3.5 13th edge `holon-ref` (systems-optimizer Δ1).
2. **Create** Phase-B AWAITING-APPROVAL packet for `/lint` signal extensions: L-CROSS-HOLON-REF + L-CROSS-CLIENT-GLOBAL.
3. **Author** per-client repo template at `templates/client-holon/` (skeleton swarm/wiki/ + per-client agents/ + per-client meta/health.md).
4. **Author** UNIX user provisioning script (`tools/provision-client-holon.sh <client-slug>`).
5. **Author** ollama install playbook (`tools/install-inference-stack.sh`) per `swarm/lib/inference-stack.yaml`.
6. **Author** methodology-push CI pipeline (GitHub Action / GitLab CI / cron job — pushes versioned methodology snapshot to each client repo).
7. **Author** per-client `meta/health.md` template + cross-client aggregation tool (Jetix-central observability over methodology-only metrics, not client content).
8. **Test** pen-test scenario + network-disconnect test on first client-holon before going live.

**Staging order.** Steps 1-2 (gate) parallel; steps 3-7 in parallel after gate ack; step 8 sequential.

**Rollback.** Each client-holon is independent; rolling back one client doesn't affect others. Methodology-push v1.4 → v1.3 = client pulls older version. Worst-case rollback: deactivate client-holon (set `state: paused`); preserve content; re-activate when fix deployed.

## §10 Horizon Projection (≥600w; 5 gates)

| Gate | Pages/client | Clients | Total holons | Physical failure | Upgrade path | MHT event | BOSC-A-T-X | Janus risk | Per-client HW |
|---|---|---|---|---|---|---|---|---|---|
| **G1 €50K** | ~500 (Jetix) | 0-1 | 1-2 | none — A1 substrate operates Jetix-central | none required | — | Time | low | optional Mistral-7B GPU rental (€60-120/mo) for demo |
| **G2 €200K** | ~5,000 | 10 | 11 (1 methodology + 10 clients) | manual methodology-push fan-out (~2h/week ops); per-client ollama install ~2h first time | CI methodology-push automation; ollama install playbook script; **A2 substrate now MANDATORY** for next-client onboarding | Phase Promotion (per-client agent instantiation; Role-Lift of methodology-push to CI-managed) | Operation + Composition | medium INT excess (clients dependent on Jetix methodology-push cadence); medium S-A excess (Jetix-central monopoly on methodology updates) | Mistral-7B-Q4 (16GB GPU rental ~€100/mo per client) at scale; first paying client triggers ollama install on client hardware |
| **G3 €1M** | ~10,000 | 50 | 51 (Jetix + 50 clients) | per-client `meta/health.md` aggregation latency >5s per client; 50 ollama instances coordination overhead; methodology-version skew (some clients on v1.3, others on v1.4) | Sub-roy split (consulting / infra / research); per-client portfolio-brigadier; methodology-version-skew tracker in Jetix-central; per-client GPU procurement gate (≥3 paying clients + ≤20% trailing-3mo revenue + HITL ack per investor-optimizer §1) | Fission (Jetix brigadier into sub-roy coordinators per portfolio; meta-agent into per-cluster meta-agents); Context Reframe (each portfolio is a peer-roy of Jetix-central) | Composition + Agency + Operation | high INT excess (per-client autonomy creating coordination overhead); high S-A excess (sub-roy autonomy needs methodology-parliament checks per philosophy-scalability §7) | client-owned GPU (RTX 4080+ €1500-2500 capex) increasingly common at this scale |
| **G4 $100M** | ~30,000 | 500 | 501+ (Jetix + 500 + Alliance peers) | per-client coordination overhead exceeds Ruslan-attention budget (×500); Mittelstand AI Alliance governance not yet structured; methodology-version coherence breaks (>3 active versions) | Mittelstand AI Alliance formal entity; methodology-license revenue (replaces deployment revenue per investor-scalability §4 — Wintel licensing precedent BIOS §10); Alliance methodology parliament (philosophy-scalability §7); per-Alliance-member sub-roys | Role-Lift (Alliance governance committee); Context Reframe (Jetix-central as standards-body, like EISA per Strategic Insight §3-§4); Fusion (Alliance methodology versions as canonical) | eXternal + Composition + Agency | pervasive S-A risk (per-roy ontologies drift from Jetix-central); INT risk (Alliance bureaucracy stifles innovation) — both mitigated by quarterly methodology parliament + outcome-level telemetry | each member owns inference stack; Mittelstand-LLM (Phoenix-BIOS-equivalent per Strategic Insight §8 rec 7) emerges as default Alliance-blessed model |
| **G5 $1T** | ~80,000 | 5000+ | thousands (Alliance federation) | Distributed wiki across roys; merge-conflict rate >1/hour at Jetix-central methodology repo; per-roy ontologies drift; statistical convergence as $1T peer-review per philosophy-scalability §6 | Federated wikis + CRDT for edges; per-roy sub-lints; Alliance methodology parliament with adversarial mandate; statistical convergence outcome-telemetry as peer-review proxy; Token economy Option B (D23) tie-in plausible per investor-scalability §5 | Continuous Fusion + Re-Phase-Promotion (always-evolving methodology v∞); Fission per regional Alliance chapter | eXternal + Composition + Agency | pervasive (mitigated by Alliance parliament + statistical telemetry convergence + outcome-level falsification per philosophy-scalability §6) | Per-Alliance-member full-stack autonomy; Mittelstand-LLM common standard; Jetix-central owns methodology-license revenue + brand + standards |

**Antifragility verdict.** A2 is the **only Layer-A variant antifragile through G4 by construction.** Each new client adds capability (per BIOS-research §11 Урок 4: distributed evolved systems gain capability from stress of scale). G5 antifragility requires Alliance governance + methodology parliament — explicit Phase-B+ work. [F: F4 / ClaimScope: A2-horizon / R: high]

## §11 Anti-Fragility Assessment (≥400w)

**Verdict: TRUE ANTIFRAGILE through G4; CONDITIONAL ANTIFRAGILE at G5 (requires Alliance governance Phase-B+ work).**

**Mechanism for true antifragility G2-G4.** Per Kauffman adjacent-possible + Kelly out-of-control patterns (systems-expert §9 lens), each new client-holon adds an independent variation source. Methodology-push is one-way (Jetix → client); but every client's anonymized opt-in case-study is a SIGNAL that informs methodology v(n+1). With 50 clients (G3), Jetix sees 50 independent stress tests of its methodology weekly; with 500 (G4), 500. The methodology gets BETTER with each client because the variation in challenges (Mittelstand vendor compliance vs healthcare regulatory vs financial-services audit) exercises corner cases A1's single-tenant could never surface. **This IS the EISA-moment compounding mechanism per Strategic Insight §4 + investor-integrator §4.**

**Mechanism for conditional antifragility G5.** At 5000+ clients, the variation source becomes overwhelming: methodology-version skew + per-roy ontology drift + governance bureaucracy risk INT-excess. The conditional safeguard: Alliance methodology parliament (philosophy-scalability §7) with adversarial mandate (Lakatos protective belt). If parliament is structured well (rotating sub-roy leadership; outcome-telemetry-driven decisions), G5 stays antifragile. If parliament ossifies into committee-bureaucracy (S-A excess of methodology-monopoly), G5 fragility emerges. Phase-B+ governance design = Ruslan + Alliance founders' work; cannot be prescribed in this cycle.

**Pressure tests.**

(1) **Methodology v1.4 → v1.5 push BREAKS 3 client-holons.** Each affected client's `/lint --methodology-update` flags incompatibility; client opts NOT to apply (HITL gate prevents auto-apply); Jetix-central rolls back v1.5 → v1.5.1 with fix; clients re-test. **Antifragile because:** the 3 broken clients SIGNAL the bug before it propagates to the other 47 clients. A1 single-tenant would have shipped the bug to its only deployment.

(2) **Hostile pen-test on Layer 1 (UNIX permissions bypass via sudo escalation).** Audit log shows the attempt; sudo logs show the user; HITL alert fires. Recovery: revoke sudo for `jetix-client-<slug>` UNIX user; re-image VM (Path A) or instruct client to re-image (Path B). UC-9 STACK Layers 2-4 still hold (graph-level + frontmatter + repo-isolation). **Antifragile because:** STACK = no single-point-of-failure; Layer 1 breach surfaces but is contained.

(3) **Domain expert prompt rewritten Phase-B (engineering-expert v2 with new mode).** Methodology-push delivers new prompt to all 50 client-holons. Each client opts in. NO per-client retraining required (filesystem-native + KM substrate orthogonal to agent prompts). **Antifragile because:** capability propagates without coordination overhead.

(4) **Project forked into parallel directions across CLIENTS (e.g., 3 clients independently build "DACH outreach playbooks").** Each client's playbook stays in client-holon. Jetix-central sees the pattern via opt-in case-studies (3 clients submit anonymized abstracts); methodology v1.6 includes a "DACH-outreach-playbook" template; pushed to all 50 clients; future client-onboardings include it. **Antifragile because:** decentralized exploration → centralized methodology consolidation = best of both worlds. [F: F4 / ClaimScope: A2-anti-fragility / R: high]

## §12 Open Questions for Ruslan

1. **G2 first-paying-client onset trigger:** ack the "spin up A2 substrate" auto-trigger when first client-acceptance-predicate-pass arrives in `meta/health.md`? OR ack manually for first 3 clients?
2. **D3 §3.5 13th edge `holon-ref` AWAITING-APPROVAL gate:** ack now (Phase-A pre-stage) OR at G2 (alongside first paying client)?
3. **Path A/B/C default per client tier:** Path B for self-sufficient technical clients (default per investor-optimizer §6); Path A for low-touch SMB (default per Strategic Insight §5); Path C for compliance-strict enterprise post-G2 (per investor §6). Confirm tier-routing criteria?
4. **Mistral-7B-Q4 vs Llama-3.1-8B-Q4 default model:** authorize 20-query DACH golden-set evaluation as resolution mechanism for D-2 dissent? Run before first-paying-client onset OR at G2?
5. **Methodology-push cadence:** weekly methodology-version snapshot (jetix-methodology@v1.x.0)? Or per-cycle (auto-tagged at every brigadier α-4 close)?
6. **Per-client GPG signing key authority:** Jetix-central holds master keypair AND each client holds delegated subkey? OR fully separate keypairs per client (highest isolation; highest ops overhead)?

— brigadier (Phase-5 variant draft), 2026-04-24
