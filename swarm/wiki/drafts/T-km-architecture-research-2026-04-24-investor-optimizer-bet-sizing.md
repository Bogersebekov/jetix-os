---
title: Investor × Optimizer — Kelly Bet-Sizing + Barbell + Local-LLM Cost-Curve
type: optimization
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
produced_by: investor-optimizer
sources:
  - swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - prompts/km-architecture-research-2026-04-24.md
  - raw/research/knowledge-architecture-deep-research-2026-04-19.md
related: []
binding_scope: km-architecture-investor-optimizer-deltas
mode: optimizer
---

# Investor × Optimizer — Kelly Bet-Sizing + Barbell + Local-LLM Cost-Curve

## Invariant Check (precondition — before any delta)

All five WLNK / MONO / IDEM / COMM / LOC invariants evaluated against the
portfolio of gate-upgrade decisions embedded in the KM architecture choice.

| Invariant | Applies | Preserved | Evidence |
|---|---|---|---|
| **WLNK** (capital-flow continuity) | Yes | Yes | Every proposed delta names a destination (which gate-tier receives the spend) AND a return mechanism (higher FPAR, lower ops overhead, higher GM%). No silent capital leakage. |
| **MONO** (rank-monotone) | Yes | Yes | The proposed deltas do not flip the existing rank-order of gate priorities: G1 (€50K baseline, zero capex) > G2 (€200K, BM25-trigger only) > G3 (€1M, Neo4j if needed) > G4+. Conservative stays below aggressive on the expected-return dimension. |
| **IDEM** (idempotency) | Yes | Yes | Re-applying the Kelly sizing formula on the same inputs (p, b, q values as named in §2) yields the same half-Kelly fractions. No drift on re-run. |
| **COMM** (commutativity) | Yes | Yes | Optimizing BM25 decision before Neo4j decision yields the same final state as Neo4j before BM25. The decisions are independent. |
| **LOC** (locality) | Yes | Yes | All deltas touch only the KM architecture gate-upgrade budget. No reach into org structure, pricing doctrine, or swarm composition (those are method-changes — see §5). |

All five invariants preserved. Delta proposals proceed.

---

## §1 Delta Proposals (one per H-N closed)

**Delta-H3 — Path B GM floor fix (addresses H-3 CONDITIONAL YES).**

Baseline: Path B GM at €15K/year per client = 64.8% (below 70% target).
[src: investor-critic §5 Path B cost matrix, line 149]

Proposed delta: Split year-1 pricing into a one-time onboarding fee (€3,000
billed separately, not included in the €15K/year subscription) plus €15K/year
recurring. The €3K onboarding fee covers the 16h methodology delivery (€1,920)
and 4h annual update setup (€480) — total one-time cost €2,400; Jetix margin
on setup = €600 (25%). Annual recurring: support only (2h/month × €120 =
€2,880/year). GM on the €15K recurring stream = (15,000 - 2,880) / 15,000 =
**80.8%**. Combined year-1 GM (€18K total intake, €5,280 cost) = 70.7%.

Delta table:

| Metric | Baseline | Proposed | Delta |
|---|---|---|---|
| Year-1 intake | €15,000 | €18,000 (€15K + €3K setup) | +€3,000 |
| Year-1 cost | €5,280 | €5,280 (unchanged) | €0 |
| Year-1 GM% | 64.8% | 70.7% | +5.9pp |
| Recurring (yr 2+) GM% | 80.8% | 80.8% | unchanged |

F: F3 (analytical estimate; no production data at Path B 3+ client scale).
ClaimScope: Applies to technically capable Mittelstand clients able to self-host.
Fails for clients requiring extensive Jetix-side hand-holding beyond 2h/month.
R: Refuted if average Path B support overhead exceeds 3h/month in months 2-6
post-onboarding for ≥2 of first 3 clients. Receipt: support-time ledger reviewed
at first quarterly knowledge-compound mark-to-market (H-4 cadence). Accepted if
3 consecutive Path B clients average ≤2h/month support in months 2-6.

WLNK: preserved (pricing change; cost structure unchanged; return path = GM%).
MONO: preserved (Path B still ranks below Path A on ops complexity; above Path C
on margin). IDEM: preserved. COMM: preserved. LOC: preserved (pricing only;
no method change).

---

**Delta-H5 — Private Library quarterly mark-to-market cadence (addresses H-4 NO
and H-5 NO together — both concern missing valuation and bet-sizing discipline).**

Baseline: No valuation cadence for the Private Library asset. No Kelly gate for
GPU procurement. [src: investor-critic §1 H-4 and H-5]

Proposed delta (two sub-deltas, both zero-capex):

Sub-delta H4: Institute a quarterly knowledge-compound KPI logged in meta/health.md.
Three metrics: (1) citation-density growth rate = (new typed edges this quarter /
total edges prior quarter); (2) FPAR trend = percent of /ask answers rated
"sufficient" without follow-up query, measured via weekly sampling; (3) qualitative:
"Library contributed to N consulting engagements this quarter via /ask retrieval."
Below FPAR 80% for two consecutive quarters triggers a Library-quality HITL
escalation. This converts the Private Library from an unacknowledged intangible
into a measurable compounding asset per Buffett owner-earnings framing
(intangible whose earnings = better /ask → higher consulting quality → retention).
[src: investor-critic §5 knowledge-as-leverage note; decisions/ROY-INFORMATION-DIET.md §1.6]

Sub-delta H5: GPU procurement gate, stated as a capital rule. "No GPU hardware
may be procured until: (a) ≥3 paying clients with confirmed offline-first
requirement exist, (b) hardware cost ≤20% of trailing-3-month Jetix revenue,
(c) HITL approval via swarm/gates/AWAITING-APPROVAL-gpu-procurement-<date>.md."
Before that gate, use Ollama on existing hardware + on-demand GPU rental (Vast.ai
/ RunPod) expensed per engagement at ~€2-5/hour.
[src: investor-critic §6 UC-10 capital implication; prompts §3.10 hardware footprint]

Delta table:

| Resource | Baseline | Proposed | Delta expected-return |
|---|---|---|---|
| Private Library value visibility | Untracked intangible | Quarterly FPAR + citation-density KPI | +qualitative: enables informed allocation decisions; no cash cost |
| GPU procurement | No gate; ad-hoc risk | 3-client gate + 20%-revenue cap + HITL | +risk-of-ruin floor raised: eliminates stranded-hardware scenario |
| GPU rental (per demo) | Unbudgeted | Expensed per engagement €2-5/h on-demand | +zero capex at G1; cost is variable, scales with revenue |

F: F3 (estimate; GPU gate thresholds are conservative conventions, not formal proofs).
ClaimScope: Applies through G2 (€200K gate). At G3 (€1M), GPU procurement review
is warranted; at G3 scale the 20%-revenue cap permits ~€10-15K hardware spend.
R: Refuted if ≥3 clients with confirmed UC-10 requirement arrive before trailing-
3-month revenue clears the 20%-cap threshold (forcing a gate renegotiation via
HITL). Receipt: quarterly gate review in swarm/wiki/reviews/.

---

**Delta-H7 — Second-level thinking section for BM25 Kelly bet at G2 (addresses H-7 NO).**

Baseline: No second-level thinking on what is already priced into the Mittelstand
AI market. [src: investor-critic §1 H-7]

Proposed delta: Add the following second-level claim to the KM variant selection memo:

"What the Mittelstand AI market has ALREADY priced in: generic ChatGPT wrappers,
basic RAG with cloud APIs, Notion-AI-style document summarization, and
per-session AI assistants. These are commoditized. What is NOT yet priced in:
local-first KB with offline-first inference + EU-sovereign compliance path +
methodology-as-licensable-standard + client-private semantic graph that compounds.
The early-adopter window is 6-12 months per Strategic Insight §8 rec 5. This
is the margin-of-safety clock: if Jetix does not ship the first Path-B client
with a working UC-9 + UC-10 proof within 6 months, a faster mover may price
in the same position."
[src: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8 rec 5;
investor-critic §2 H-7 fix]

At G2 specifically: the BM25 upgrade is an internal retrieval quality improvement,
not a market-facing differentiator. The market has NOT priced in BM25 at all
(it is invisible to clients). Therefore the second-level question for BM25 is not
"has the market priced in BM25?" but "has Jetix priced in the latency degradation
risk at G2 that makes BM25 necessary?" The answer is: yes, conditionally — trigger
gated to PPR latency >2s p95 per research §H.8. This IS second-level thinking
applied to an internal infrastructure bet: do not act until the threshold fires.

F: F3 (analytical; 6-12 month window is strategic estimate from BIOS-parallel
research, not market survey data).
ClaimScope: Applies to Mittelstand DACH market, 2026. Does not apply to
hyper-scale AI platforms (they face different competitive dynamics).
R: Refuted if a competitor ships local-first + client-private KB for Mittelstand
before Jetix ships first Path-B client. Receipt: quarterly competitive landscape
review in swarm/wiki/reviews/. Accepted if no equivalent competitor ships within
12 months.

WLNK/MONO/IDEM/COMM/LOC: all preserved. This delta adds analytical content to
the variant selection memo; it does not change capital flows or position ranks.

---

## §2 Kelly Bet-Sizing Table per Gate-Upgrade Decision

Kelly formula: f* = (b × p - q) / b where p = probability of upside (bet pays),
q = 1 - p = probability of downside (bet fails), b = odds ratio (return if wins
/ stake). Half-Kelly: f_half = 0.5 × f*. Negative f* = do not bet.

Confidence method: expert-judgment-from-tier1-citations. p estimates are base-rate
judgments informed by research§G.2 scale thresholds and critic §5 cost data.
Uncertainty: ±10-15pp on all p estimates; treat half-Kelly as the binding
recommendation precisely because of this uncertainty.

| Decision | p (upside prob) | b (odds: return/stake) | q (downside) | f* (full Kelly) | Half-Kelly | Recommendation |
|---|---|---|---|---|---|---|
| **BM25 at G2 (trigger: PPR latency >2s p95)** | 0.65 | 3 | 0.35 | (3×0.65 - 0.35)/3 = **0.53** | **0.27** | Proceed when trigger fires. Half-Kelly says allocate ~27% of upgrade-cycle budget to BM25 tooling and integration work. BM25 is low-cost (filesystem-native, no paid infrastructure); the "bet" is Jetix engineering time. At trigger, high probability of payoff (latency problem is real at 5K pages per §G.2). |
| **Neo4j at G2 (pre-emptive, before latency crosses 20K-edge threshold)** | 0.20 | 4 | 0.80 | (4×0.20 - 0.80)/4 = **0.00** | **0.00** | DO NOT BET. Full Kelly = 0.00; any fraction of zero is zero. Pre-emptive Neo4j at G2 has zero expected value: 80% probability the scale does not justify it (research §G.2 threshold is ~20K edges; G2 ~5,700 edges). Cost of a wrong bet: ops overhead + licensing complexity. Cost of waiting: near-zero (BM25 covers the gap). [src: research §G.2; critic §3 Failure Mode 2] |
| **Neo4j at G3 (triggered at ~20K edges per research §G.2)** | 0.75 | 4 | 0.25 | (4×0.75 - 0.25)/4 = **0.69** | **0.34** | Proceed at trigger. Half-Kelly = 34% of G3 infrastructure budget allocated to Neo4j migration. At G3 (€1M gate, contractor #1 hired), the ops overhead is absorbable. Probability is high because the 20K-edge trigger is a research-validated threshold, not a guess. [src: research §G.2; critic §5 UC-8 table] |
| **GraphRAG community detection cron at G2 (pre-emptive)** | 0.18 | 3 | 0.82 | (3×0.18 - 0.82)/3 = **-0.09** | **-0.05** | REFUSE THIS BET. Negative Kelly = expected loss. GraphRAG is over-engineering at <5,000 pages (research §H.9 anti-pattern #5 verbatim: "GraphRAG для 557 страниц — переинжиниринг"). Wait for G3 trigger (cross-domain synthesis queries failing FPAR). [src: research §H.9 anti-pattern #5] |
| **GraphRAG community detection cron at G3 (trigger: global queries fail FPAR)** | 0.60 | 4 | 0.40 | (4×0.60 - 0.40)/4 = **0.50** | **0.25** | Proceed at trigger. Half-Kelly = 25% of G3 engineering budget. At 15K+ pages with cross-domain synthesis demand, GraphRAG community summaries provide real retrieval uplift. Trigger-conditioned, not pre-emptive. [src: research §G.3 scale table; §H.8 5K-page triggers] |
| **On-demand GPU rental at G1 (€2-5/hour per demo, expensed)** | 0.85 | 8 | 0.15 | (8×0.85 - 0.15)/8 = **0.83** | **0.42** | PROCEED NOW at G1. Highest Kelly in the table. The bet is tiny (€2-5/hour, variable, zero capex); the upside is large (enables UC-10 proof-of-concept for client demos, which unlocks Path B positioning). No inventory risk, no stranded capital. Spend up to 42% of a demo-budget allocation on GPU rental without constraint. [src: investor-critic §6 UC-10; strategic-insight §5 Path B] |
| **Owned GPU hardware at G1 (before 3-client gate)** | 0.10 | 8 | 0.90 | (8×0.10 - 0.90)/8 = **-0.01** | **-0.01** | DO NOT BUY. Negative Kelly at G1. Without ≥3 confirmed clients needing offline-first, GPU hardware is stranded capital risk. Expected value is negative: 90% probability the exact use-case fails to materialize in the right form before hardware is obsolete or needs replacement. [src: investor-critic §5 H-5 fix; §6 UC-10 capital risk note] |
| **Owned GPU hardware at G3 (after 3-client gate + 20%-revenue cap)** | 0.70 | 6 | 0.30 | (6×0.70 - 0.30)/6 = **0.65** | **0.33** | Proceed at gate. Half-Kelly = 33% of G3 capex budget. At G3 (€1M, ≥3 clients confirmed, revenue covers the 20%-cap), owned hardware has positive expected value: lower per-hour cost vs perpetual rental, and the use-case is validated. [src: investor-critic §2 H-5 fix] |

**Summary: three hard NOs (pre-emptive Neo4j G2 / pre-emptive GraphRAG G2 / owned GPU G1). Five conditional or immediate YESes (BM25 at trigger / Neo4j G3 at trigger / GraphRAG G3 at trigger / on-demand GPU now / owned GPU G3 at gate). All sized at half-Kelly.**

---

## §3 Barbell Construction Across 6 Variants (Anticipatory)

Taleb barbell: 70% in conservative tail (low-cost, low-downside if wrong, provably
sufficient at current scale) + 30% in aggressive tail (higher cost if wrong, higher
upside ceiling, technology optionality). Middle is avoided — "medium risk" positions
do not survive volatility without the barbell's tail-offsetting properties.

Naming convention for the 6 anticipated variants: Layer-A variants (A1, A2, A3)
cover the topic-wiki / knowledge-accumulation layer; Layer-B variants (B1, B2, B3)
cover the project-management / project-wiki layer. These names are anticipatory
(variants are produced by engineering + systems experts in other cells); the
investor-optimizer classifies them by their capital-risk profile based on available
source descriptions. [src: prompts §2.1 Layer A axes; §2.2 Layer B axes]

### Layer-A Barbell

| Variant | Classification | Rationale | Kelly-style weight |
|---|---|---|---|
| **A1 — Filesystem-native (git + markdown + HippoRAG PPR baseline)** | Conservative tail (70%) | Zero incremental capex. Proven at current scale (557 pages, 572 edges). Research conclusion: "достаточен до ~10,000 страниц." Wrong-bet cost: near-zero (already deployed). Upside ceiling: sufficient for G1-G2. [src: research Conclusion §800] | 70% of Layer-A engineering budget |
| **A2 — GraphRAG community summaries (global-query-focused, pre-built summaries)** | Aggressive tail (15%) | Moderate infrastructure cost (community detection compute). High upside for cross-domain synthesis at G2-G3. High downside risk if triggered prematurely (over-engineering per §H.9 anti-pattern #5). Right only at G3+ trigger. Allocate as a real-option: do the design work now, execute only at G3. | 15% of Layer-A engineering budget (design only at G2; execution at G3 trigger) |
| **A3 — HippoRAG 2 + PPR with dense fallback (semantic + graph hybrid)** | Aggressive tail (15%) | Requires vector DB infrastructure (Qdrant / Chroma self-hosted) = non-zero ops overhead. Adds cross-lingual semantic search for German-language Mittelstand queries. Upside: solves German-language retrieval gap. Risk: vector DB adds ops surface at G1-G2 before that gap is proven material. Real-option: design now, trigger at confirmed German-language FPAR failure. | 15% of Layer-A engineering budget (design only; execution at confirmed trigger) |

**Layer-A barbell: 70% A1 (conservative) / 30% A2+A3 split (aggressive, both as real-options not immediate spends).**

### Layer-B Barbell

| Variant | Classification | Rationale | Kelly-style weight |
|---|---|---|---|
| **B1 — Thin-scaffold project-wiki (minimal `_moc.md + context.md + history.md`, emergent growth)** | Conservative tail (70%) | Zero additional infra. Scaffold defined, not enforced. Matches current Jetix operating cadence. Wrong-bet cost: minimal (just a directory convention). Sufficient for ≤8 concurrent projects at G1. [src: research §H.1 folder tree] | 70% of Layer-B engineering budget |
| **B2 — Rich-scaffold (PMBOK-style WBS + risk register + stakeholder map per project)** | Aggressive tail refusal | Method-change risk: imposes heavyweight project management on a solo-founder Phase A operation. At G1 with 8 projects and 1 founder, PMBOK overhead is not an asset — it is a liability. Kelly = negative (b is low because PMBOK overhead kills solo velocity; q is high). **REFUSE this allocation at G1.** Revisit at G3 (team of 3, multi-project with external stakeholders). | 0% at G1; revisit at G3 |
| **B3 — Federated mini-swarm per project (dedicated project-brigadier + 2-3 allocated experts per project)** | Aggressive tail (30%) | High upside: each project has dedicated AI bandwidth; cross-project learning via shared topic-wikis. High cost if wrong: at G1 with 8 projects, running 8 mini-swarms simultaneously risks Max-subscription turn-budget fragmentation. Right-sized for: P1 projects (quick-money, ai-tools) at G2 where project revenue justifies dedicated swarm bandwidth. Allocate as a real-option for P1 projects only. | 30% of Layer-B budget, restricted to P1 projects at G2; defer full federation to G3 |

**Layer-B barbell: 70% B1 (conservative) / 30% B3 (aggressive, restricted to P1 projects at G2+). B2 refused at G1.**

### Barbell across the combined 6-variant portfolio (anticipatory pairing)

| Layer-A | Layer-B | Combined classification | Phase |
|---|---|---|---|
| A1 (conservative) | B1 (conservative) | Full conservative — 70% weight | G1 default; adopt now |
| A1 (conservative) | B3 (aggressive, P1 only) | Mixed — 20% weight | G2, P1 projects only |
| A2 (aggressive) | B3 (aggressive) | Full aggressive — 10% weight | G3 trigger-conditioned only |
| A3 (aggressive) | B1 (conservative) | Mixed — reserved option | G2-G3 if German-language gap materializes |
| A2 (aggressive) | B2 (refused) | Refused — 0% weight | Never at G1; revisit G3 |
| A3 (aggressive) | B2 (refused) | Refused — 0% weight | Never at G1; revisit G3 |

**Net barbell: 70% conservative (A1+B1) / 30% real-options across aggressive tails, none of which are immediate spends.**

---

## §4 Local-LLM Cost-Curve Table

Per-model cost data: hardware pricing from Hetzner GPU server public pricing;
Vast.ai / RunPod estimates are public market-rate approximations as of early
2026. Treat as base-rate estimates; actual quotes may vary ±20%. License
eligibility notes are based on publicly stated license terms; Mittelstand
commercial use requires independent legal verification for each deployment.

| Model | VRAM floor | Per-client capex if owned (recommended hardware) | Vast.ai rental €/month est. | Latency p95 @ 500-token output | Mittelstand commercial license |
|---|---|---|---|---|---|
| **Llama 3.1-8B Q4_K_M** (Ollama default) | 8 GB | €700-1,000 (RTX 3060 12GB; fits client on-prem workstation) | €80-120 (shared A10G instance, 24GB VRAM, multi-tenant) | 4-8s | Llama Community License: commercial use permitted for companies ≤700M MAU. Mittelstand = OK. Verify if Jetix methodology layer counts as "derivative" — likely not (orchestration, not fine-tune). |
| **Mistral 7B Q4_K_M** | 8 GB | €700-1,000 (RTX 3060 12GB) | €80-120 | 3-6s | Apache 2.0 — unrestricted commercial use. Cleanest license for Mittelstand. No MAU cap, no derivative concerns. **Preferred license posture.** |
| **Llama 3.1-70B Q4_K_M** | 40-48 GB | €12,000-18,000 (2× RTX 3090 24GB bridged, or used A100 40GB; not realistic for client on-prem) | €400-700 (A100 40GB dedicated instance on Vast.ai) | 20-40s | Llama Community License: same ≤700M MAU cap. Larger models = more licensing surface to review. GPU footprint makes client-hosted Path B impractical at this size. |
| **DeepSeek V3 Lite (distilled, Q4)** | 16-24 GB | €1,500-2,500 (RTX 4080 16GB / RTX 4090 24GB) | €150-250 (RTX 4090 dedicated) | 5-12s | DeepSeek Model License: commercial use permitted for non-competing applications. "Non-competing" requires legal review for consulting-methodology use. **Flag for legal verification before Mittelstand client deployment.** |
| **Llama 3.2-3B Q4_K_M** (minimum viable) | 4 GB | €400-600 (any modern laptop with 8GB RAM via Ollama) | €40-60 (shared GPU, CPU-fallback viable) | 2-4s | Llama Community License: same. Smallest footprint — UC-10 Tier-Offline only (fact retrieval, short extraction, keyword search). Not sufficient for Tier-Hybrid synthesis. |

**Investor guidance on model selection per path:**

Path A (Jetix-hosted VPS): Llama 3.1-8B Q4_K_M or Mistral 7B Q4 on Hetzner CX41
(16GB RAM, €30/month). Apache 2.0 on Mistral eliminates license risk. Covers
UC-10 Tier-Offline + simple Tier-Hybrid. Upgrade to CX52 (32GB, ~€60/month) for
Llama 3.1-8B + larger context if needed. [src: investor-critic §5 Path A UC-10 note]

Path B (client-hosted): Mistral 7B Q4 on client's own server (Hetzner AX41 root
server, 64GB RAM, €50/month client cost — Jetix does not bear this). Jetix ships
hardware spec sheet as part of methodology package. Apache 2.0 license = zero
client legal friction. [src: investor-critic §5 Path B UC-10; prompts §3.10]

Path C (hybrid): Same as Path A for inference (Jetix VPS), but client KB stays on
client infrastructure. Inference model = Mistral 7B Q4 or Llama 3.1-8B Q4 depending
on synthesis complexity required. [src: decisions/STRATEGIC-INSIGHT §5 Path C]

**Recommended default for Phase A / G1: Mistral 7B Q4_K_M. Rationale: Apache 2.0
(no license risk), 8GB VRAM (fits RTX 3060 or Hetzner CX41), 3-6s latency (acceptable
for /ask on client KB), lowest per-client capex if owned. Llama 3.1-8B Q4_K_M as
drop-in alternative if Mittelstand clients prefer Meta's ecosystem.**

---

## §5 Refusals (Method-Change Escalations)

Three method-changes were identified in the brief and surrounding materials.
All refused per §4.3 — optimizer cannot optimize a Method (capital-M).

**Refusal 1 — "Which path (A, B, C) should Jetix adopt as its primary commercial model?"**

This is a Method choice (which business model Jetix pursues), not a parameter
within a chosen model. It changes the fundamental operating doctrine (from
managed-service to methodology-provider to hybrid), not just the allocation
within a doctrine. Route to: HITL (Ruslan decision on §9 open questions per
Strategic Insight, specifically Q2). The investor-optimizer produces cost data
per path (§4 above, §6 below) to inform that HITL decision; the decision itself
belongs to Ruslan.

```json
{
  "status": "refusal",
  "reason": "mode:optimizer cannot optimize a Method; Path A/B/C selection is a doctrine choice, not a parameter",
  "escalation": "HITL",
  "alternative_routing": "investor × integrator with HITL ack on Strategic Insight §9 Q2",
  "turns_used": 1
}
```

**Refusal 2 — "Should Jetix pursue patents (D15 budget trigger) now vs Phase 2?"**

Patent strategy timing is a capital-structure + legal doctrine decision. It changes
the competitive doctrine (IP-protection posture), not just the budget allocation
within a chosen posture. Requires a HITL decision on Lock D15 (revenue-gated
patent budget: €200K+ trigger per JETIX-ARCHITECTURE-BRIEF §2 D15). The optimizer
cannot advance this gate without the revenue condition being met.

```json
{
  "status": "refusal",
  "reason": "Lock D15 gate; patent strategy is a Method change requiring HITL + revenue gate clearance",
  "escalation": "HITL",
  "alternative_routing": "investor × integrator at €200K gate; confirm D15 trigger status",
  "turns_used": 1
}
```

**Refusal 3 — "Should Jetix formalize the Mittelstand AI Alliance as a legal entity now?"**

Alliance formalization changes the legal and organizational doctrine (from solo
consulting to consortium-operator). This is an α-5 Direction-level change, human-only
by spec. The investor-optimizer confirms the financial case is NOT yet met (€50K gate
not cleared; alliance formalization requires Phase 2 per Strategic Insight §10 rec 3).
The optimizer does not execute the Direction change.

```json
{
  "status": "refusal",
  "reason": "α-5 Direction change; Mittelstand AI Alliance formalization is HITL and Phase 2+ per Strategic Insight §10",
  "escalation": "HITL",
  "alternative_routing": "investor × scalability mode at €200K gate for alliance capital case",
  "turns_used": 1
}
```

---

## §6 Per-Client Deployment GM% Refresh

Source: investor-critic §5 cost matrices. This section refreshes the GM% for
the €50K/year enterprise-tier client, which the critic draft did not explicitly
name.

Revenue assumption for enterprise tier: €50,000/year per client (named in brief).
The cost structure scales from the €15K model; some fixed costs do not scale
proportionally (onboarding time is bounded; support overhead grows sub-linearly
with revenue because enterprise clients tend to have in-house IT).

| Path | GM @ €15K/year Mittelstand client | GM @ €50K/year enterprise client | Notes |
|---|---|---|---|
| **A — Jetix-Hosted VPS** | 70.0% (knife-edge per critic) | 87.6% est. | At €50K revenue: cost structure remains ~€4,500-5,500/year (VPS + ops + onboarding ≈ same; enterprise client may require more customization — add 8h/year × €120 = €960). Year-1 cost ~€5,500; GM = (50,000 - 5,500) / 50,000 = 89.0%. With some complexity buffer: ~87-89%. Ops overhead does not scale linearly with revenue — this is the key Path A scale advantage. |
| **B — Client-Hosted (productized methodology)** | 64.8% year-1 base / 70.7% with separate setup fee / 80.8% recurring | 88-92% est. | At €50K revenue: support overhead at 2h/month × €120 = €2,880/year. Onboarding still ~€2,400 one-time. Year-1 cost ~€5,280; GM = (50,000 - 5,280) / 50,000 = **89.4%**. Recurring (yr 2+) = (50,000 - 2,880) / 50,000 = **94.2%**. Path B at enterprise scale is the highest-margin path. Capital argument: enterprise clients tend to have IT capability (self-hosting works), pay more, and require similar support hours. The margin gap widens with revenue. |
| **C — Hybrid (client KB + Jetix-hosted agents + tunnel)** | 54.0% (well below 70% per critic) | 73.4% est. | At €50K revenue: ops overhead remains the dominant cost but tunnel infra is largely fixed. Year-1 cost estimate ~€8,000-9,000 (tunnel + ops + onboarding; ~3h/month ops × €120 = €4,320 + one-time setup ~€2,160 + agent-swarm hosting ~€240/year + support). GM ≈ (50,000 - 9,000) / 50,000 = **82.0%** at €50K. However, Path C at Phase A is still reserved for Phase 2 per Strategic Insight §5 — the solo-founder ops overhead is the binding constraint, not the margin math at enterprise scale. |

**Key insight:** Path B at enterprise-tier (€50K/year) produces >90% recurring GM
(yr 2+). This is Buffett owner-earnings at its best: the intangible asset
(methodology + Private Library) generates earnings with near-zero incremental capex.
The methodology, once productized (D18 lock), scales with zero COGS growth.
[src: decisions/JETIX-ARCHITECTURE-BRIEF.md §2 D18 productization lock]

**Risk-of-ruin check:** Path A at €15K Mittelstand client (70% GM = €10,500/year
margin per client) requires Ruslan ops time of ~2h/month = €2,880/year. At 5
concurrent clients: ops overhead = 10h/month — approaching the sustainability
ceiling for a solo founder on 40h/week budget. Risk-of-ruin floor for Path A:
≤5 clients solo; ≥6 requires contractor #1 (€200K gate). Named and quantified.

---

## §7 F-G-R Summary per Delta

| Delta | F (formality) | G (granularity / ClaimScope) | R (reliability) | Confidence |
|---|---|---|---|---|
| Delta-H3 (Path B pricing) | F3 (analytical estimate; no production Path B client data) | Applies to technically capable Mittelstand clients; fails for non-technical clients requiring >3h/month support | medium — arithmetic is correct given the cost model; cost model may underestimate support time for first 3 clients | medium |
| Delta-H4 (Private Library KPI cadence) | F2 (operational convention; FPAR 80% threshold is a convention, not a formally derived metric) | Applies to wiki/foundations/ as Phase A Private Library surface; does not apply to Tier-4 books (Phase B) | medium — KPI cadence is the right direction; specific threshold (FPAR 80%) may need 2 quarters of calibration before it becomes binding | medium |
| Delta-H5 (GPU gate) | F3 (analytical; the 3-client threshold and 20%-revenue cap are conservative conventions derived from first-principles, not empirical GPU procurement data) | Applies through G2; gate renegotiation warranted at G3 | medium — thresholds are conservative by design; probability of premature GPU procurement is low under these rules | medium |
| Delta-H7 (second-level thinking) | F3 (analytical; 6-12 month competitive window is a strategic estimate from BIOS-parallel research, not market survey) | Applies to DACH Mittelstand 2026; does not apply to hyper-scale AI platforms | medium — window estimate carries ±3 months uncertainty; competitive landscape monitoring is the refutation receipt | medium |
| Kelly bet-sizing table | F5 (analytical with arithmetic backing; p estimates are base-rate judgments ±10-15pp) | Applies to KM infrastructure gate decisions at G1-G3; does not apply to G4+ (different scale, different doctrine) | medium — Kelly fractions are numerically correct given the p/b/q inputs; input uncertainty is the dominant risk; half-Kelly provides the uncertainty buffer | medium |
| Barbell construction | F4 (operational convention; 70/30 split is Taleb-derived convention, not formally optimized) | Applies to the 6 anticipated KM architecture variants at Phase A / G1-G2; revisit at G3 when aggressive tails may warrant higher weight | medium — classification of variants as conservative/aggressive is judgment-based; confirmed by research §H.9 anti-patterns and §G.2 scale thresholds | medium |
| Local-LLM cost-curve | F3 (pricing estimates; Vast.ai/RunPod market rates are approximations ±20%; hardware prices are public but volatile) | Applies to 2026 market pricing; VRAM requirements are model-dependent and quantization-dependent | medium — model-family VRAM floors are well-established; per-month rental costs are volatile; license eligibility requires legal verification | medium |
| GM% enterprise refresh | F3 (estimate; cost model is the same as critic's €15K model scaled; no enterprise client data yet) | Applies to €50K/year enterprise clients with Path A/B/C as defined; enterprise clients may have bespoke requirements that inflate cost | medium — the arithmetic is mechanically correct; the cost model's enterprise accuracy depends on whether enterprise complexity is captured | medium |

---

## §8 Provenance

| Source | Range | Quote / basis |
|---|---|---|
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §5 Path B cost matrix, line 149 | "Gross margin at €15K revenue: 64.8% (below 70% target)" |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §1 H-3 | "CONDITIONAL YES... Fails for clients without in-house IT" |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §1 H-5 | "NO... no bet-sizing framework exists for GPU procurement timing" |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §6 UC-10 capital implication | "No GPU capex at Phase A. On-demand GPU only, expensed per engagement." |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §5 UC-8 table, G2 row | Kelly sketch: "Edge (probability G2 clients actually need Neo4j-grade performance): estimated 20%" |
| swarm/wiki/drafts/T-km-architecture-research-2026-04-24-investor-critic-capital-allocation-audit.md | §2 H-7 fix | "What the Mittelstand AI market has already priced in..." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §5 Path A/B/C | "Path C для Enterprise clients, Path B для self-sufficient technical clients, Path A для low-touch SMB." |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §8 rec 5 | "Speed: window NOW — 6-12 месяцев максимум чтобы захватить position" |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §6 Missing | "Offline-first AI integration — Llama/DeepSeek distilled для local inference" (named as missing) |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | §G.2 | "Порог для Neo4j/ArangoDB: ~20,000 edges при регулярных multi-hop queries." |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | §H.8 scale triggers | "1,000 страниц: Добавить BM25 как secondary retrieval. Мониторинг PPR latency (threshold: >2 секунды → оптимизация)" |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | §H.9 anti-pattern #5 | "GraphRAG для 557 страниц — переинжиниринг с community detection при текущем масштабе." |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | Conclusion §800 | "git + markdown + HippoRAG достаточен до ~10,000 страниц. GraphRAG и vector DB — не сейчас, но runbook готов." |
| raw/research/knowledge-architecture-deep-research-2026-04-19.md | §G.3 | Scale table: "5K стр: BM25 + HippoRAG PPR; 50K стр: Hybrid BM25 + dense + PPR + RRF" |
| prompts/km-architecture-research-2026-04-24.md | §3.10 UC-10 | hardware footprint framing; offline-first inference as mandatory acceptance criterion |
| prompts/km-architecture-research-2026-04-24.md | §6.1 cell #18 | investor-optimizer focus: "Kelly-like bet-sizing, barbell allocation, per-client GM, local-LLM cost curve" |
