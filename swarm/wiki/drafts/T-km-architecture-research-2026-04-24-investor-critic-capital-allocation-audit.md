---
title: Investor × Critic — Capital Allocation + Per-Client Unit-Econ Audit
type: critique
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
produced_by: investor-critic
sources:
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/ROY-INFORMATION-DIET.md
  - decisions/JETIX-ARCHITECTURE-BRIEF.md
  - prompts/km-architecture-research-2026-04-24.md
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md
related: []
binding_scope: km-architecture-investor-lens
mode: critic
---

# Investor × Critic — Capital Allocation + Per-Client Unit-Econ Audit

## §1 Conformance Checklist (≥5 binary)

The eight-check rubric from investor-expert §3.1 is applied to the capital-allocation profile
implied by the KM architecture migration decision. The "artefact under review" is not yet a
capital-allocation memo — it is the investment decision embedded in the choice of KM variant and
the hosting-path decision (Path A / B / C). That embedded decision is auditable; the conformance
checks operate on what the brief and strategic-insight documents reveal.

| # | Check | Verdict | F | ClaimScope | R |
|---|---|---|---|---|---|
| **H-1** | Does the existing Max-subscription cost basis provide enough margin-of-safety to deploy 10 Mittelstand clients (€200K gate) without any infrastructure capex >€5K per client? | **NO** | F3 (analytical estimate; no production data at 10-client scale) | Applies to Path A (Jetix-hosted VPS) and Path C (Jetix-hosts agents + secure tunnel). Does NOT apply to Path B (client-hosted, Jetix = methodology provider) | Refuted if: one Path-A or Path-C client deployment causes capex >€5K before €200K revenue gate is crossed. Receipt: spend ledger by Q4 2026. Accepted if: 3 consecutive client deployments clear <€5K capex each AND Max-subscription remains the only Jetix-side compute cost. |
| **H-2** | Is the unit-econ per /ask query (in turns) traceable today such that a 10x usage spike at G2 does not blow the budget unnoticed? | **NO** | F2 (operational observation; no per-query turn-count instrumentation confirmed in source docs) | Applies to Jetix-internal swarm usage. Does NOT yet apply to per-client deployments (per-client instrumentation is a "missing" item per Strategic Insight §6). | Refuted if: a usage spike at G2 goes unnoticed and causes unexpected Max-subscription rate-limiting or quality degradation. Receipt: meta/health.md turn-count tracking activated within 2 weeks of G2 gate. Accepted if: per-query turn budget is logged and surfaced in weekly digest before G2. |
| **H-3** | Does the per-client deployment cost for Path B (client-hosted) bottom out at <€500/month of Jetix time per client, sustaining >70% gross margin at €15K/year per client? | **CONDITIONAL YES** | F3 (estimate; Path B cost structure inferred from Strategic Insight §5 + Brief §3.1.6) | Applies only if Path B is chosen and client has IT infrastructure to self-host. Fails for clients without in-house IT (requires Jetix support overhead that erodes margin). | Refuted if: Path-B support overhead for one non-technical client exceeds €500/month Jetix time. Accepted if: first 3 Path-B clients average <€300/month Jetix time in months 2-6 post-onboarding. |
| **H-4** | Does the Private Library asset (D14 Foundation as Main Asset) have a recurring re-valuation discipline — e.g., quarterly mark-to-market via knowledge-compound metrics? | **NO** | F2 (documents establish the asset's strategic importance but no valuation cadence is defined) | Applies to wiki/foundations/ as the canonical Private Library surface for Phase A. Broader Library (393 books + curated research) is Phase-B Tier-4 fuel. | Refuted if: after two quarterly cycles the Library has no usage-based value metric (e.g., FPAR improvement attributable to Library, citation density growth rate). Accepted if: a quarterly knowledge-compound KPI is defined in meta/health.md by end of Phase A. |
| **H-5** | Does the proposed local-LLM stack (Llama 7B Q4 → Mistral 7B → DeepSeek V3) have a Kelly-like bet-sizing model so that a wrong bet at G2 does not strand €50K of GPU procurement? | **NO** | F3 (the strategic insight names the models; no bet-sizing framework exists for GPU procurement timing) | Applies to Path A (Jetix-hosted) and the on-prem variant of Path C. Does NOT apply to Path B (client buys their own hardware). | Refuted if: Jetix purchases GPU hardware before G2 revenue gate and the use-case fails to materialize. Accepted if: GPU procurement is explicitly gated behind ≥3 paying clients with confirmed offline-first requirement AND budget-approved by HITL. |
| **H-6** (C6 from §3.1) | Is the risk-of-ruin floor named for the infrastructure migration decision — specifically, what happens to Ruslan's runway if the KM architecture bet is wrong? | **NO** | F2 (Brief §3.1.12 names the runway discipline; no explicit KM-architecture-migration risk-of-ruin floor statement exists) | Applies to any scenario where KM architecture choice requires capex (Neo4j license, GPU hardware, dedicated VPS fleet). Does NOT apply to pure Max-subscription + filesystem path (no capex risk). | Refuted if: a downside scenario is named and quantified (e.g., "if all 6 variants fail UC-9 review, Jetix has spent N turns × N cycles with zero productizable output"). Accepted if: a floor is stated as "no hardware capex before €50K gate cleared AND no Neo4j before G2". |
| **H-7** (C7 from §3.1) | Does the migration decision apply second-level thinking — i.e., has it named what is already priced in by the market / consensus before the KM architecture recommendation? | **NO** | F3 (the BIOS-parallel insight in Strategic Insight §1 is first-level; it does not ask "what has the Mittelstand market already priced into local-first AI?") | Applies to the market-positioning thesis. Does NOT apply to the internal architecture choice (where the "market" is internal adoption). | Refuted if: a competitor materializes local-first + client-private KB for Mittelstand before Jetix ships the first Path-B client (i.e., the thesis was already priced in by a faster mover). Accepted if: no competitor at equivalent methodology depth ships to Mittelstand within 12 months. |
| **H-8** (C8 from §3.1) | Is there an invert section — "how does this KM architecture bet fail?" — written before the "how does it succeed?" framing? | **NO** | F2 (Strategic Insight §11 has an anti-scope but no "how does this fail?" section on the capital allocation side) | Applies to the strategic investment thesis in STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md. | Refuted if: a failure analysis is produced and incorporated before the architecture variant decision is locked. Accepted if: the KM variant selection memo includes ≥3 capital-allocation failure modes (see §2 below for the fix). |

**Acceptance predicate result:** C1(H-1)==NO AND C2(H-2)==NO AND C6(H-6)==NO AND C7(H-7)==NO AND C8(H-8)==NO → **FAIL**. H-3 is conditional-pass; H-4, H-5 are outright NO. Zero checks are clean passes against the Hamel-binary rubric. The capital-allocation profile embedded in the KM architecture migration is under-specified by investor standards.

---

## §2 Acceptance Predicates (per "no")

For each failed check, one Hamel-binary fix:

**H-1 fix.** Publish a per-client deployment cost floor before any G2-gate spend is authorized: "Jetix-side capex per Mittelstand client ≤ €3K one-time setup + ≤ €150/month recurring Jetix VPS cost for Path A; ≤ €0 for Path B; ≤ €200/month for Path C tunnel infrastructure. If any client breaches €5K total capex before year-1 revenue is received, pause onboarding and escalate to HITL."

**H-2 fix.** Define a per-session turn-budget for /ask queries and surface it in meta/health.md: "Max-subscription turn budget per week is not metered by Anthropic; however, Jetix self-imposes a per-client soft cap of N sessions × M turns/session per week. When actual usage crosses 2× the soft cap, brigadier fires an alert in the weekly digest." The concrete threshold must be set before G1 closes.

**H-4 fix.** Institute a quarterly knowledge-compound mark-to-market ritual: (a) citation-density growth rate (new typed edges / total pages) compared to prior quarter; (b) FPAR (First-Pass Acceptance Rate per /ask) compared to prior quarter; (c) a qualitative claim: "the Private Library contributed to N closed consulting engagements this quarter via /ask retrieval." These metrics land in meta/health.md §9 (new section). Below FPAR 80% for two consecutive quarters triggers a Library-quality escalation.

**H-5 fix.** Apply a Kelly-like gate to GPU procurement: "GPU hardware may only be procured when (a) ≥3 paying clients with confirmed offline-first requirement exist AND (b) the hardware cost is ≤20% of trailing-3-month Jetix revenue AND (c) HITL explicit approval via swarm/gates/AWAITING-APPROVAL-gpu-procurement-<YYYY-MM-DD>.md." Before that gate, use Ollama on existing hardware (Ruslan's MacBook or a rented ephemeral GPU cloud session per client demo, not owned hardware).

**H-6 fix.** State the risk-of-ruin floor explicitly in the KM variant selection memo: "No KM architecture upgrade requires Jetix capex before the €50K revenue gate is cleared. Any variant requiring Neo4j, dedicated VPS fleet, or GPU hardware before that gate is rejected on capital grounds regardless of technical merit. The downside scenario for a wrong architecture bet is 4-8 weeks of swarm turns (Max-subscription, already sunk) plus re-architecture time. This is bounded and survivable. The unacceptable scenario is purchased hardware or SaaS subscriptions that burn runway."

**H-7 fix.** Write the second-level section: "What has the Mittelstand AI market already priced in? Generic AI consulting (ChatGPT wrappers + Notion AI + basic RAG) is commoditized; that is priced in. What is NOT yet priced in by the market: local-first KB with offline-first inference + EU-sovereign compliance path + methodology-as-licensable-standard. Jetix captures the un-priced portion. But: early-adopter window is 6-12 months per Strategic Insight §8 rec 5 — this is the margin-of-safety clock."

**H-8 fix.** Write the invert section before the architecture recommendation: three failure modes named in §3 below (Alternatives, status-quo kill-conditions).

---

## §3 Alternatives (≥2 per "no")

Applying pattern P4 (Munger inversion) and P5 (Taleb via-negativa): how does this capital bet fail, and what are the alternatives that survive?

### Failure Mode 1 — BM25-only G2 (conservative)

**Capital strategy:** At G2 (€200K, ~5K wiki pages), add only BM25 as secondary retrieval index atop the existing filesystem + HippoRAG PPR baseline. No Neo4j. No vector DB. No GPU procurement. GraphRAG deferred to G3.

- **Kill-condition:** BM25 at 5K pages is insufficient for cross-domain synthesis queries (UC-3, UC-7). Latency for multi-hop queries exceeds 2s p95 per knowledge-architecture-deep-research §G.2. Client satisfaction erodes on /ask quality for complex queries.
- **Capital implication:** Near-zero capex at G2. Max-subscription remains the only cost. Opportunity cost: potentially slower time-to-quality on complex /ask for consulting clients. Margin-of-safety: high (no stranded capital).
- **Second-level check:** BM25 is already "standard" in the Mittelstand-AI market. It does not differentiate. The moat at G2 is the Private Library curation quality + methodology, not the retrieval tier.

### Failure Mode 2 — Neo4j G2 (aggressive)

**Capital strategy:** At G2 trigger (edges.jsonl crosses ~50MB per research §G.2), migrate graph to Neo4j. Add GraphRAG community detection daily cron. Potentially procure GPU for local-LLM inference per client.

- **Kill-condition:** Neo4j license cost + operational overhead (Ruslan or contractor #1 must operate it) erodes gross margin. If Neo4j monthly cost = €200/month × 10 clients = €2K/month infrastructure overhead, it reduces a €15K/year client from 70%+ GM to ~55% GM, failing the H-3 predicate. Additionally, Neo4j requires a dedicated ops investment that is premature at the €200K gate (no contractor #1 yet).
- **Capital implication:** Medium capex risk. Neo4j Community is free; Neo4j Enterprise is not. At G2 scale (8-10 clients, 10-15 agents), Community edition may be sufficient. But operational overhead is a hidden capex. Margin-of-safety: medium.
- **Second-level check:** Neo4j at G2 is over-engineering by the research's own conclusion (knowledge-architecture-deep-research §H.9 anti-pattern #5: "GraphRAG для 557 страниц — переинжиниринг"). At 5K pages the research says "consider Neo4j if latency >5s" — not "migrate immediately." This is a trigger-conditioned action, not a G2-mandatory spend.

### Status quo — Filesystem + PPR, revisit at G3

**Strategy:** Stay on git + markdown + HippoRAG PPR through G2. Add BM25 only when latency threshold is crossed (>2s p95 per H.8 trigger). Revisit Neo4j and vector DB at G3 (~15K pages, €1M gate).

- **Kill-condition:** Status quo fails when /ask latency degrades below client-acceptable threshold AND Jetix cannot add BM25 in <2 weeks. Receipt: meta/health.md latency monitoring must be active at G2. If FPAR drops below 75% for two consecutive weeks, escalate to BM25 addition.
- **Capital implication:** Zero capex through G2. Max-subscription covers all retrieval compute. This is the Buffett "be greedy when others are fearful" posture — resist infrastructure spend when filesystem still works.
- **Second-level check:** The status quo is viable if the 10-client G2 scenario averages ≤1K pages per client (10K total). The research confirms git + markdown + HippoRAG sufficient to ~10K pages (§Conclusion: "достаточен до ~10,000 страниц"). Status quo clears H-1 and H-6. It is the recommended baseline.

---

## §4 Anti-scope

This critique is NOT designing the KM architecture variants. That is the swarm's Phase 3-4 output (engineering × integrator, systems × integrator, etc.).

This critique is NOT recommending which variant Ruslan should pick. That is HITL at the AWAITING-APPROVAL gate (§8 of the execution prompt).

This critique is NOT proposing equity issuance, token economy (D23 Option B is Phase 2+ per JETIX-ARCHITECTURE-BRIEF §2 D23), or external capital raises. Those require explicit α-5 Direction changes and are HITL by spec.

This critique is NOT invoking paid APIs, vector DBs, or any external LLM SDK. The critique was produced using filesystem reads only, consistent with Max-subscription discipline.

This critique is NOT running the engineering code review on ingest/retrieval pipelines. That is cell #1 (engineering × critic).

This critique is NOT arbitrating the epistemic coherence of the local-first moat thesis. That is philosophy × integrator (cell #15).

---

## §5 Per-client deployment cost matrix (Path A / B / C)

Revenue tier assumption: €15K/year per Mittelstand client (explicitly named in the brief). Gross margin target: >70% (i.e., Jetix retains >€10.5K/year per client after costs). Break-even on margin: Jetix cost must be <€4.5K/year = <€375/month per client.

### Path A — Jetix-Hosted (dedicated VPS per client, EU data center)

| Cost item | One-time | Monthly recurring | Annual total |
|---|---|---|---|
| VPS setup + configuration (Jetix time: ~4h × €120/h) | €480 | — | €480 |
| Dedicated EU VPS (e.g., Hetzner CX31 = 4vCPU 8GB RAM, ~€15/month) | — | €15 | €180 |
| Local LLM inference (Ollama on VPS, Llama 7B Q4 — fits 8GB) | — | €0 | €0 |
| Jetix ops overhead (patches, monitoring: ~2h/month × €120/h) | — | €240 | €2,880 |
| Onboarding methodology delivery (8h × €120/h) | €960 | — | €960 |
| **Total year-1** | **€1,440** | **€255** | **€4,500** |
| **Gross margin at €15K revenue** | | | **70.0%** (borderline) |

**Notes.** Path A margin is at the knife-edge of 70%. Ops overhead is the dominant cost. Scaling from 10 to 50 clients requires either (a) contractor #1 at €200K gate to absorb ops, or (b) automation that reduces monthly ops overhead to <€60/client. Without automation, Path A erodes below 70% GM as client count grows past 5. **Capital risk: if Jetix tries to run Path A for 10+ clients solo, Ruslan's time becomes the bottleneck, not the infrastructure.** This is the classic "hours-billing trap" per D18 productization lock.

**UC-9 feasibility at Path A:** Strong — each client is a dedicated VPS = physically isolated OS process. UC-9 is architecturally provable (filesystem permissions at OS level). Cost of isolation: zero incremental (VPS isolation is a VPS property). [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5 Path A]

**UC-10 feasibility at Path A:** Strong — Llama 7B Q4 on Hetzner CX31 (8GB RAM) runs offline-first inference for Tier-Offline queries (fact retrieval, summarization ≤10K tokens, extraction). Tier-Hybrid requires >8GB; upgrade to CX51 (16GB) at ~€35/month = +€240/year per client (still within margin). [src:raw/research/knowledge-architecture-deep-research-2026-04-19.md §H.8]

### Path B — Client-Hosted (Jetix ships methodology + agent configs)

| Cost item | One-time | Monthly recurring | Annual total |
|---|---|---|---|
| Methodology package delivery (documentation + config + onboarding workshop: ~16h × €120/h) | €1,920 | — | €1,920 |
| Remote support (avg 2h/month × €120/h — assuming technically capable client) | — | €240 | €2,880 |
| Annual methodology update push (4h × €120/h) | €480 | — | €480 |
| **Total year-1** | **€2,400** | **€240** | **€5,280** |
| **Gross margin at €15K revenue** | | | **64.8%** (below 70% target) |

**Notes.** Path B gross margin at €15K revenue is below 70% target on Year 1 due to high onboarding cost. Two mitigations: (1) raise year-1 price to €18K (Jetix charges for setup separately at €3K one-time fee, then €15K/year); GM then = 70%+. (2) Reduce onboarding to 8h via productized methodology kit (D18 productization lock). Path B is the most capital-efficient path for Jetix once the methodology is productized — recurring support is low and can scale. [src:decisions/JETIX-ARCHITECTURE-BRIEF.md §2 D18]

**UC-9 feasibility at Path B:** Strongest — client owns the infrastructure. Jetix has zero access to client data post-delivery. Client data never enters Jetix systems by construction. [src:prompts/km-architecture-research-2026-04-24.md §3.9]

**UC-10 feasibility at Path B:** Depends on client hardware. Client must procure a machine capable of running Llama 7B Q4 (16GB RAM minimum). Hetzner root server (AX41 — 64GB RAM, ~€50/month client cost) is within Mittelstand IT budget. **Jetix does not bear this cost.** Jetix provides the setup guide and recommended hardware spec sheet as part of the methodology package. [src:prompts/km-architecture-research-2026-04-24.md §3.10]

### Path C — Hybrid (client KB on client infrastructure; Jetix hosts agent-swarm; secure tunnel)

| Cost item | One-time | Monthly recurring | Annual total |
|---|---|---|---|
| Tunnel setup + configuration (WireGuard or Tailscale; ~6h × €120/h) | €720 | — | €720 |
| Tailscale / WireGuard subscription (Jetix side, shared across clients) | — | €15 | €180 |
| Agent-swarm hosting on Jetix VPS (shared multi-tenant per-client namespace; ~€20/client/month at 10-client density on a single CX51) | — | €20 | €240 |
| Client-side KB setup support (4h × €120/h) | €480 | — | €480 |
| Jetix ops overhead (tunnel monitoring, agent-swarm ops: ~3h/month × €120/h) | — | €360 | €4,320 |
| Onboarding (8h × €120/h) | €960 | — | €960 |
| **Total year-1** | **€2,160** | **€395** | **€6,900** |
| **Gross margin at €15K revenue** | | | **54.0%** (well below 70%) |

**Notes.** Path C gross margin is unacceptable at €15K/year per client at solo-founder Phase A. The ops overhead of running a secure tunnel + per-client agent namespace is too high for a solo operation. Path C becomes viable only when: (a) contractor #1 absorbs ops (€200K gate), AND (b) client count ≥ 8 per Jetix ops FTE (density benefit), AND (c) price raised to €20K+/year per client. **Path C is the Phase 2 default (per Strategic Insight §5 recommendation), not Phase 1.** [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5 Path C]

**Recommended Phase 1 path:** Path B (client-hosted) with productized onboarding kit, premium priced at €18K year-1 / €15K year-2+. Deploy Path A for clients with no IT capability at a premium (€20K+/year). Path C reserved for Enterprise clients at Phase 2 post-€200K.

---

## §6 UC-1..UC-10 cost-coverage assessment (focus UC-8 / UC-9 / UC-10)

**UC-1 (Video Ingest):** No capital cost. /ingest skill runs on Max-subscription Claude Code. Whisper transcription: if Groq API is not available, use Whisper.cpp locally (free, CPU-based). Covered at current cost basis. [src:raw/research/knowledge-architecture-deep-research-2026-04-19.md §A.1]

**UC-2 (Weekly Digest):** No capital cost. /lint + /build-graph runs in-session. Latency target ≤60s at G1 is feasible with filesystem + HippoRAG PPR on ~1K pages. [src:prompts/km-architecture-research-2026-04-24.md §3.2]

**UC-3 (Solve-with-Wiki):** No capital cost at G1. At G2 (5K pages), HippoRAG PPR query latency may approach 2s p95 (knowledge-architecture-deep-research §G.2) — add BM25 as secondary at that trigger. BM25 is filesystem-native, no cost. [src:raw/research/knowledge-architecture-deep-research-2026-04-19.md §H.8]

**UC-4 (Skill Accumulation):** No capital cost. Write-backs to strategies.md + comparisons/ are filesystem writes inside Max-subscription turns. [src:raw/research/knowledge-architecture-deep-research-2026-04-19.md §F.2]

**UC-5 (Project Onboarding):** No capital cost. /ingest fires on project scaffold creation. [src:decisions/JETIX-ARCHITECTURE-BRIEF.md §3.1.13]

**UC-6 (Cross-project Leverage):** No capital cost. edges.jsonl cross-project edges are filesystem writes. [src:raw/research/knowledge-architecture-deep-research-2026-04-19.md §G.1]

**UC-7 (Contradiction Detection):** No capital cost at G1-G2. /lint weekly + contradicts edge type + health.md. At G3+ (15K pages), /lint weekly runtime exceeds 30 min (per UC-8 table); may require sharded /lint — still no paid infrastructure, just longer sessions. [src:prompts/km-architecture-research-2026-04-24.md §3.8]

**UC-8 (Scale Test) — focus:** The UC-8 5-gate cost table from the execution prompt [src:prompts/km-architecture-research-2026-04-24.md §3.8] maps to capital events:

| Gate | Revenue | KM capital event | Cost implication | Investor verdict |
|---|---|---|---|---|
| G1 | €50K | None — filesystem + PPR | €0 capex | Pass — Max-sub covers it |
| G2 | €200K | BM25 secondary (trigger: PPR latency >2s p95); GraphRAG community cron (trigger: global-queries fail FPAR) | €0 capex (BM25 is filesystem-native; GraphRAG cron is in-session Max-subscription turn budget) | Pass — IF BM25 is triggered only on latency threshold, NOT pre-emptively |
| G3 | €1M | Neo4j / ArangoDB trigger at ~20K edges; sharded /lint | ~€100-300/month Neo4j Community (free) or cloud instance; contractor #1 ops overhead | CONDITIONAL — Neo4j Community is free; ops is the real cost; gates behind contractor #1 hire |
| G4 | $100M | Hybrid BM25 + dense + PPR + RRF; dedicated search infra | Vector DB (Qdrant/Chroma self-hosted: ~€200/month at multi-client scale) | DEFERRED — gates behind G3 validation; at $100M revenue, €200/month infra is immaterial (<0.01% revenue) |
| G5 | $1T | Federated wikis + CRDT + per-roy sub-lints | Distributed infra; significant capex — but at $1T scale, any reasonable capex is approved | NOT A PHASE A CONCERN |

**Kelly-like sizing for G2 infrastructure bet.** The choice between conservative (BM25 only) vs aggressive (Neo4j + GraphRAG cron) at G2 is a bet-sizing question. Using the investor-expert Kelly framework:
- Edge (probability G2 clients actually need Neo4j-grade performance): estimated 20% (knowledge-architecture-deep-research says "consider Neo4j if latency >5s" — most 5K-page deployments will not hit this).
- Odds (return if Neo4j is needed and installed proactively): modest (prevents churn from one client with heavy cross-domain queries).
- Kelly fraction: (0.20 / 1.0) × 0.5 (half-Kelly conservatism) = 10% of infrastructure-upgrade budget should go to Neo4j at G2, with 90% staying in BM25-only path.

**Recommendation: BM25 at G2 trigger (latency), Neo4j deferred to explicit need. Never pre-empt the infrastructure spend.**

**UC-9 (Client Isolation) — capital implication:** The architectural isolation model (filesystem namespacing per client, per-client git repo, per-client agent instantiation) has near-zero incremental capex on Path B. Path A adds €15-35/month per client VPS. Path C adds ~€35/month per client (VPS + tunnel). The isolation property itself costs nothing to design; the capital cost is hosting, not isolation logic. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5]

**UC-10 (Offline-First Inference) — capital implication and hardware risk:** This is the highest capital-risk use case in the portfolio. The local-LLM stack (Llama 7B Q4 / Mistral 7B / DeepSeek V3) has a hardware footprint:

| Model | VRAM floor | Recommended hardware | Cost (Hetzner GPU server) | Tier coverage |
|---|---|---|---|---|
| Llama 3.2 3B Q4 | 4 GB | Any modern laptop, VPS with 8GB RAM | €15/month (CX31) | T-Offline only (fact retrieval, short synthesis) |
| Llama 3.1 8B Q4 | 8 GB | VPS with 16GB RAM | €30/month (CX41) | T-Offline + simple T-Hybrid |
| Mistral 7B Q4 | 8 GB | VPS with 16GB RAM | €30/month (CX41) | T-Offline + simple T-Hybrid |
| DeepSeek V3 (full) | 80 GB+ | Dedicated GPU server (H100 80GB) | €2.50/hour on demand (Vast.ai estimate) | Full T-Offline + T-Hybrid |

**Capital risk on UC-10:** Procuring a dedicated GPU server before client demand is confirmed is a ruin-level risk for a Phase A solo-founder. Mitigation: use on-demand GPU rental (Vast.ai, RunPod) for initial client demos at ~€2-5/hour. Procure owned hardware only after ≥3 clients confirm the offline-first requirement AND their hardware budget (Path B: they pay for hardware; Path A: Jetix rents per-client at €30-50/month). **No GPU capex at Phase A. On-demand GPU only, expensed per engagement.** [src:prompts/km-architecture-research-2026-04-24.md §3.10]

**Knowledge-as-leverage moat — asset valuation note.** The Private Library is named as the primary asset in decisions/ROY-INFORMATION-DIET.md §1.6: "Knowledge-as-leverage — главный ров (moat)." From Buffett's owner-earnings framing (investor-expert §2.4 Pattern P1): the Library's value is not the cost of acquisition (393 books × ~€30 = ~€12K nominal) but the earnings it enables — better /ask answers → higher consulting quality → better client retention → more referrals. This is an intangible asset that compounds without incremental capex. The re-valuation discipline proposed in H-4 (FPAR + citation density) converts this intangible into a measurable metric. Without that metric, the Library is an unacknowledged asset — Buffett's "intrinsic value" problem applied to knowledge infrastructure.

---

## §7 Provenance

| Source | Range | Quote |
|---|---|---|
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §5 Path A/B/C | "Path C для Enterprise clients, Path B для self-sufficient technical clients, Path A для low-touch SMB. Один product line с 3 tier pricing." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §6 Missing | "Client-isolation mechanics — how exactly we spawn per-client wiki/agents without cross-contamination" (named as missing) |
| decisions/ROY-INFORMATION-DIET.md | §1.6 | "Knowledge-as-leverage — главный ров (moat). Jetix answers качественнее на порядок при тех же вопросах." |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §2 D18 | "Productization over hours — Scale via products/templates/community, NOT hours; dogfood." |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §2 D19 | "Holding-Scale $1T ambition — Infrastructure MUST scale 7 orders-of-magnitude without re-architecture." |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §2 D21 | "Partnership-Matchmaker + Roy-Replication — Matchmaker + swarm-of-10 template + inter-roy comms." |
| decisions/JETIX-ARCHITECTURE-BRIEF.md | §3.1.12 | Revenue-gated spend gates: "$20-30K → €50K → €200K → €1M" |
| prompts/km-architecture-research-2026-04-24.md | §3.8 UC-8 table | Gate G2: "edges.jsonl in-memory size crosses ~50MB (networkx load) — upgrade: edges split by layer; GraphRAG community detection daily cron" |
| prompts/km-architecture-research-2026-04-24.md | §6.1 cell #17 | "investor × critic — Audit variant candidates for capital allocation… unit-econ check per page / per query; per-client deployment cost for Path A/B/C" |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | Part G §G.2 | "Порог для Neo4j/ArangoDB: ~20,000 edges при регулярных multi-hop queries. До этого edges.jsonl + networkx в памяти достаточен." |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | §H.9 anti-pattern #5 | "GraphRAG для 557 страниц — переинжиниринг с community detection при текущем масштабе." |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | Conclusion | "git + markdown + HippoRAG достаточен до ~10,000 страниц. GraphRAG и vector DB — не сейчас, но runbook готов." |
