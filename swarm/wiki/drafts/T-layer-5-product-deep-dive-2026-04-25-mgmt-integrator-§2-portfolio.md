---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: "§2"
title: "§2 Portfolio Overview — 9 Directions as a Coherent Portfolio"
type: layer-deep-dive-section
mode: integrator
author: mgmt-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - decisions/JETIX-SYSTEM-OVERVIEW.md
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - decisions/JETIX-VISION.md
  - decisions/JETIX-PLAN.md
  - prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md
  - swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md
  - swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md
  - swarm/wiki/operations/quick-money/icp.md
  - reports/review_2026-04-24.md
word_count_estimate: ~2200
confidence: high
confidence_method: synthesis-from-locked-decisions-plus-voice-verbatim-plus-l6-ack
escalations: []
dissents:
  - position: "YouTube-analyzer SaaS deferred to G3-G4 per gate table, yet audio_514 frames it as 'золотая жила' implying higher urgency"
    evidence:
      - "reports/review_2026-04-24.md audio_514 verbatim: «YouTube может стать золотой жилой для Jetix через автоматический анализ всех каналов»"
      - "decisions/JETIX-SYSTEM-OVERVIEW.md §L5 table: YouTube-analyzer Phase 2+ / G3→G4 gate"
    F: F4
    ClaimScope: "tension holds in Phase-1 planning horizon; does NOT invalidate gate sequencing (bandwidth constraint is real); may resolve when consulting revenue validates product-build capacity"
    resolution: "gate sequencing preserved; tension flagged for Ruslan ack in §15 — does YouTube-analyzer move to G2 preparatory if Phase-1 consulting clients include YouTube operators?"
---

# §2 Portfolio Overview — 9 Directions as a Coherent Portfolio

> **Chapter purpose.** This chapter maps all 9 L5 directions in a single reference table, then explains two things a table cannot convey: (1) why exactly these 9 exist and not a different number, and (2) how the 9 function together as a portfolio — a sequenced, mutually reinforcing system — rather than as 9 independent products stacked in a list.

---

## §2.1 The 9-Direction Portfolio Table

All pricing ranges are **placeholders only**. L7 Business Deep-Dive owns final pricing structure. These ranges are tier-orientation markers derived from Phase-1 consulting rate baselines and productization logic from D18 [src:decisions/JETIX-VISION.md §5 D18]; they carry no commitment.

| # | Direction | Phase activation (Gate) | Primary ICP (L6 Trinity) | Pricing range (PLACEHOLDER — L7 owns final) | Revenue priority | Key risk |
|---|---|---|---|---|---|---|
| 1 | **AI Consulting for complex tasks** | G0 → G1 (Phase 1 core, active now) | P1A: Mittelstand + Startupper; Archetypes: Operator-Founder-CEO + Startupper | €150/hr baseline; productized packages €1 500–€10 000/engagement (D18 productization — not hourly scale) | **P1A — primary revenue engine, active cold outreach** | Founder-dependent; no clients yet; must productize before €50K ceiling; single operator = single bottleneck [src:swarm/wiki/operations/quick-money/icp.md §Two-tier] |
| 2 | **Продюсерский центр** | G0 → G1 (Phase 1 core, pilot pending) | P1A: Bloggers + Startupper; Archetypes: Блогер + Teacher | Monthly retainer €2 000–€8 000/mo; discovery-to-retainer pipeline (D11, not hourly) | **P1A — co-primary with consulting; active cold outreach** | English-speaking market requires specific trust-building; pilot not launched; content production capacity constrained at Phase-1 [src:decisions/JETIX-VISION.md §5 D11] |
| 3 | **USB-C Integration Services** | G1 → G2 (first client); G2 → G3 (productized) | P1B: Mittelstand with GDPR constraints; Archetypes: Operator-Founder-CEO | Path A managed: €5 000–€20 000/mo; Path B client-hosted: €3 000–€10 000/mo; Path C hybrid: €4 000–€15 000/mo (all PLACEHOLDER) | **P1B — opportunistic early-access; productized at G2** | Path A/B/C decision open (HITL required); EU data sovereignty compliance layer required; GDPR complexity; not yet productized [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C reinforcement] |
| 4 | **Matchmaker Platform** | G0–G1 manual (active now, informal); G1→G2 AI-smoothed; G2+ platform | P1B: specialists + complex-task buyers; Phase-2+ expanded ICP | Phase-1: no direct pricing (matchmaking as service multiplier); Phase-2+ matchmaking fee structure (PLACEHOLDER); platform subscription G3+ | **P1B — operational now as informal revenue lever; product form at G2** | Manual-only in Phase-1 limits throughput; network-effect requirement for platform value; specialist pool must grow before platform is viable [src:decisions/JETIX-VISION.md §5 D21] |
| 5 | **Secure Network** | G1→G2 (architecture design); G2→G3 (launch) | P1B: expanded Tier-1 High-earners + millionaires; invite-only | Subscription €200–€500/mo (складчина tier + network access) (PLACEHOLDER) | **P1B opportunistic invite-list post-G2; P2 product form at G3** | Requires €200K validation gate before build starts; network quality is existential (one wrong member lowers entire value proposition); Telegram-primary per L6 ack limits platform features pre-G3 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10] |
| 6 | **YouTube-analyzer SaaS** | G3 → G4 (Phase 2+ SaaS launch) | P2+: Блогеры as SaaS users; agencies; infobiz operators | SaaS pricing: €49–€299/mo per seat (PLACEHOLDER — seat/query/channel tiers to be defined in L7) | **P3 deferred — revenue-triggered; requires consulting validation first** | Competitive moat unclear until data pipeline built; YT API limits + ToS risk; requires engineering investment above Phase-1 capacity [src:reports/review_2026-04-24.md audio_514 «золотая жила»] |
| 7 | **Educational Products + Investor Programs + Grant Hunting** | G2 → G3 (methodology repo V1); G3+ (scale) | P2+: Teacher archetype + ecosystem specialists; Phase-3+ institutional | Course tier: €500–€2 000; cohort tier: €3 000–€8 000; license tier: €500–€5 000/year (PLACEHOLDER) | **P2 revenue-triggered — methodology must stabilize in Phase-1 first** | Requires Jetix methodology to be stable enough to teach (Phase-1 is stabilization phase); D27 fork-and-merge governance question unresolved; grant-hunting sub-track requires EU institutional contacts [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27] |
| 8 | **Tokens / ICO (D23 Option B)** | Phase 3+ ($100K self-earned trigger for internal utility; public Phase 3+) | Phase-3+: ecosystem specialists + investors + Alliance members | Not pricing — tokenomics (PLACEHOLDER; L7 does not own final structure — regulatory layer required; D23 gate) | **P3+ deferred — not active in Phase-1 or Phase-2** | Regulatory exposure (EU MiCA, US securities law); $100K trigger not yet reached; D23 explicit «design safe + adequate + thoughtful; NOT crypto-pump» [src:decisions/JETIX-VISION.md §8 D23] |
| 9 | **Smart AI flagship label** | Cross-phase internal — NOT an external product; used as narrative framing for all 8 directions | All archetypes (narrative framing layer, not a product) | Not applicable — internal label, no pricing | **Internal — not a P1/P2/P3 revenue item; narrative asset** | Risk of premature external productization before D29 lock; Ruslan explicit: «ну типа запиши между прочим но нет это ещё не лок блять забей хуй» [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI] |

**Placeholder declaration (shared across all pricing cells):** Every pricing figure above is a tier-orientation placeholder derived from D18 productization logic and Phase-1 rate baselines. Final pricing — tier structure, packaging, payment cadence, discounting rules — is owned by L7 Business Deep-Dive. L5 declares what the product is and who buys it; L7 declares what it costs and how the unit economics work.

---

## §2.2 Why Exactly These 9 — Not More, Not Less

The 9 directions are not an arbitrary list assembled from brainstorming. They emerge from four locked constraints applied in combination: the D11 Phase-1 core revenue mandate, the D18 productization path, the D19–D21 scaling architecture (holding + roy-replication + matchmaker), and the D23 capital-markets optionality. Unpacking each:

**D11 mandates consulting + producer as the Phase-1 revenue core** [src:decisions/JETIX-VISION.md §5 D11]. Without a revenue-generating Phase-1 pair, nothing else activates. Consulting is the entry vehicle — Ruslan's AI expertise is the product, and the 4-pack offer (session / 10 templates / community chat / billable services) is the Phase-1 monetization structure. Продюсерский центр is the Phase-1 co-primary because it serves English-speaking infobiz at scale and leverages the same AI-production tooling without requiring additional Phase-1 infrastructure. These two are not optional; they are the €50K Q2 2026 mandatory target [src:decisions/JETIX-PLAN.md §3]. Any portfolio without this pair would fail the Phase-1 revenue predicate.

**D18 productization unlocks the third and fourth directions.** D18 declares that Jetix scales through productization, not through hour accumulation [src:decisions/JETIX-VISION.md §9 D18]. USB-C Integration Services is the first productized consulting motion: instead of selling Ruslan's hours, it sells a configured client-private AI deployment (methodology + agents + wiki structure + setup). This is the Phase-2 expression of the consulting direction, not a separate product. Similarly, Educational Products is the Phase-2+ packaged methodology: what Jetix builds for itself and for consulting clients becomes a teachable, licensable artifact. D18 is the logical generator of both directions 3 and 7.

**D20, D21, D24 generate the platform tier (directions 4, 5, 6, 8).** D20 positions Jetix at USB-C-level standards infrastructure [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C reinforcement] — a positioning that requires a live ecosystem, not just two service products. D21 mandates the matchmaker mechanic as the coordination layer connecting complex tasks with specialists; the Matchmaker Platform (direction 4) is D21 made operational [src:decisions/JETIX-VISION.md §5 D21]. The Secure Network (direction 5) is the community substrate that makes D20 and D21 work at scale — it is the membership layer around which the ecosystem is built. YouTube-analyzer (direction 6) is the data-asymmetry advantage that emerges from Jetix's reverse-engineering methodology (audio_527) and feeds both matchmaker curation and educational content [src:reports/review_2026-04-24.md audio_514]. D23 generates direction 8 (tokens) as the capital-structure option for Phase-3+ — the mechanism by which ecosystem participation is incentivized without a traditional IPO [src:decisions/JETIX-VISION.md §8 D23].

**Direction 9 (Smart AI) is not a product — it is the categorical frame.** The reason the portfolio has 9 directions and not 8 is that the ninth is not an offering at all: it is the internal narrative that explains what all 8 offerings collectively represent. Audio_529 articulates this with the smartphones-vs-telephones analogy: the shift from phones to smartphones was a categorical upgrade, not a product upgrade. Smart AI is Jetix's way of describing the categorical shift it delivers [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI]. This remains an internal marker per Ruslan's explicit note; it is not D29, not an external product name, and not a lock. It sits in the portfolio table as row 9 because every direction section must be framed against it — but it generates no revenue line of its own.

**Why not 5 directions?** A portfolio of 5 would cover consulting, producer, USB-C, matchmaker, and Secure Network — the first five. The problem is that this portfolio has no long-horizon capital structure (no direction 8), no data-asymmetry layer (no direction 6), and no methodology-as-asset play (no direction 7). The D19 $1T trajectory [src:decisions/JETIX-VISION.md §5] requires not just a service company but an asset-accumulating architecture. Directions 6, 7, and 8 are the asset layer that makes the $1T trajectory physically possible — they are not aspirational additions but architectural requirements.

**Why not 15 directions?** Jetix explicitly rejects mass-market attention economy (D8 layered identity framing) and one-person-company aesthetics (D26: target steady-state is 50–100 person enterprise, not solopreneur) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D26]. A portfolio of 15 would require Phase-1 decisions about which of 15 directions to prioritize — creating AP-MGMT-5 (priority reversal) risk. The D15 revenue-gated unlock mechanism is the pruning function: only directions that either generate Phase-1 revenue or are directly infrastructure for Phase-1 revenue are activated early. The remaining directions stay deferred behind measurable gate triggers. Nine is the number that results from this pruning: 2 active (consulting, producer), 2 pre-build (matchmaker informal, USB-C first client), 1 design-pending (Secure Network), and 4 deferred (YouTube-analyzer, Educational, Tokens, Smart AI as label).

---

## §2.3 How the 9 Work Together as a Portfolio

The 9 directions are not 9 separate products with separate GTM motions and separate ICPs. They are a single sequenced system with four functional layers:

```
LAYER 1 — Revenue now (Phase 1)
    AI Consulting ────────────────────────────────────────────────────────►
    Продюсерский центр ───────────────────────────────────────────────────►

LAYER 2 — Community multiplier (Phase 1 informal → Phase 2 product)
    Matchmaker (manual) ──────────────► Matchmaker (AI-smoothed) ─────────►
    Secure Network (invite list) ───────────────────► (launch G2→G3) ──────►

LAYER 3 — Productization lift (Phase 2 → Phase 3)
    USB-C Integration Services ─────────────────────────────────────────────►
    Educational Products + Grant Hunting ────────────────────────────────────►

LAYER 4 — Scale vectors (Phase 3+)
    YouTube-analyzer SaaS ─────────────────────────────────────────────────►
    Tokens / ICO (D23) ─────────────────────────────────────────────────────►

    NARRATIVE LAYER (cross-phase internal)
    Smart AI framing ══════════════════════════════════════════════════════►

    G0      G1(€50K)     G2(€200K)      G3(€1M)      G4($100M)    G5($1T)
```

**Layer 1 — Revenue-now pair (Consulting + Producer):** These two are the only directions generating cash in Phase 1. Every other direction is either infrastructure that revenue unlocks, or a deferred product that bandwidth constraints prohibit. The Phase-1 hard constraint is stated explicitly in the system overview: «G0 → G1 (€0 → €50K Q2 2026): consulting + продюсерский центр ТОЛЬКО» [src:decisions/JETIX-SYSTEM-OVERVIEW.md §L5]. This is not a preference — it is a bandwidth theorem. Ruslan is the sole operator. Every hour allocated to building the Secure Network architecture in Phase-1 is an hour not allocated to closing consulting clients. D15 enforces this as a revenue-gated unlock: the construction of Layer 2+ is only permitted when Layer 1 generates the cash to fund it.

The consulting-producer pair is also mutually reinforcing inside Phase-1. Consulting clients who are bloggers or infobiz operators are natural Продюсерский центр leads — the same AI-augmented production capability that helps a Mittelstand client document their processes can also help an English-speaking blogger turn one workshop into ten derivative artifacts. The ICP overlap between Startupper (active cold outreach target for consulting) and Блогер (primary archetype for producer) means that a single outreach motion can surface both consulting engagements and producer retainer conversations. This is not accidental — it reflects the L6 ack'd P1A primary targeting logic [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1 §134].

**Layer 2 — Community multiplier (Matchmaker + Secure Network):** The matchmaker mechanism is already operational in Phase-1 as informal Ruslan manual activity [src:decisions/JETIX-VISION.md §5 D21]. Its portfolio role is not primarily as a revenue generator in Phase-1 but as a contact-accumulation engine: every consulting engagement and every producer retainer is also a matchmaker touchpoint. The specialist network grows as a byproduct of Layer-1 operations. At G1→G2, this informal network becomes AI-smoothed (coordination layer applied). At G2→G3, it becomes a platform with its own product shape.

Secure Network is the container that makes matchmaker sustainable: without a quality-gated membership layer, matchmaking devolves into transactional referrals with no community value. The Secure Network's складчина mechanic (pooled access to expensive tools: Perplexity, Claude Code, research instruments) and thematic sub-networks (предприниматели / инвесторы / инженеры / философы / политики) create the membership stickiness that distinguishes it from LinkedIn. Anti-LinkedIn-positioning is a direct design requirement from the source materials: «это тоже не linkedin где блять быдло одно которое ищет каких-то рабов» [src:decisions/JETIX-VISION.md §5 D5]. The Secure Network is activated at G2 (€200K validation) for architecture design and at G3 (€1M) for launch — by which point the consulting and producer revenues have validated the ICP enough to design the right membership experience.

**Layer 3 — Productization lift (USB-C + Educational):** These two directions convert Jetix from a services company into a methodology company. USB-C Integration Services is the physical delivery of what D20 calls «standards-level interoperability» [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C reinforcement]: the client gets a private AI deployment (their own server, their own KB, their own agents configured from Jetix methodology). This is not Ruslan's hours — it is Jetix methodology deployed at scale, with Path A (managed), Path B (client-hosted), and Path C (hybrid) tiers providing different levels of client sovereignty and infrastructure investment. Educational Products is the other face of the same move: if USB-C Services is «here is your Jetix deployment», Educational Products is «here is how to build and evolve your Jetix deployment yourself». D27 fork-and-merge architecture [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27] is the governance model: clients fork the methodology, adapt for their context, and the best adaptations return upstream — creating a distributed innovation loop that is impossible in a pure-services model.

The two directions in Layer 3 are deliberately sequenced behind Layer-1 revenue validation. Building an educational methodology before the methodology has been stress-tested in 10–20 real consulting engagements is a form of premature abstraction — the D28 query-driven KB principle applied to product development [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D28]. Phase-1 is the data-collection phase; Phase-2/3 is when the pattern is crystallized into a teachable artifact.

**Layer 4 — Scale vectors (YouTube-analyzer + Tokens):** These two directions are the long-horizon asset layer. YouTube-analyzer addresses the data-asymmetry opportunity that audio_514 identifies as a «золотая жила» [src:reports/review_2026-04-24.md audio_514]: bulk automated analysis of YouTube channels across any niche — advertising data, team structures, cooperation opportunities, ICP matching — creates an information advantage that no individual researcher can replicate manually. This is not a standalone product; it is an asymmetric data infrastructure that feeds the matchmaker (identify the right specialists by channel analysis), the educational products (understand what content sells in each niche), and potentially the consulting pipeline (pre-research target clients by their YouTube presence). The reason it is deferred to G3–G4 is engineering-investment: the data pipeline, the API integration layer, and the analysis infrastructure require Phase-2+ capacity to build.

Tokens (direction 8, D23 Option B) are the capital-structure completion mechanism. D23 states explicitly: «design safe + adequate + thoughtful; explicitly not crypto-pump style» [src:decisions/JETIX-VISION.md §8 D23]. The trigger is $100K self-earned — demonstrating that Jetix generates real economic value before deploying a token structure. Internal utility in Phase-2/3 (specialist compensation, складчина token pools) creates the use-case precedent before any public layer is contemplated. This sequencing respects both the regulatory environment (EU MiCA, US securities law — not yet navigated) and the anti-pyramid design principle that Ruslan stakes Jetix's reputation on.

**Smart AI as narrative layer (cross-phase):** The ninth direction is the category frame for all eight. The smartphones-vs-telephones analogy (audio_529) captures the portfolio's overarching positioning claim: Jetix is not building AI tools (telephones), it is building AI-augmented operating systems for professionals (smartphones) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI]. This frame is useful in internal sales conversations — it explains to a potential client why Jetix is different from a GPT-wrapper agency — but it is not an external product name and not a locked decision (Ruslan explicit: «ну типа запиши между прочим но нет это ещё не лок блять забей хуй»). It functions as the unifying narrative that allows all 8 directions to be described as one coherent portfolio rather than 8 separate sales pitches.

---

## §2.4 Portfolio Balance Principle — Buildable at $0, Scalable to $1T

The D19 $1T trajectory [src:decisions/JETIX-VISION.md §5] creates an architectural constraint that the portfolio must satisfy from Day 1: the Phase-1 shape must be structurally compatible with the Phase-5 shape, even though the two are radically different in scale. A portfolio that is optimized for Phase-1 solo operations but structurally incompatible with Phase-3+ enterprise-fast operations wastes all Phase-1 investment when the transition happens.

The four-layer structure above is the design response to this constraint. Layer 1 (consulting + producer) can be operated by one person with zero capital outlay — the extreme Phase-1 constraint — but it is designed with productization hooks from day one (D18): the offer structure, the template library, the KM Mat infrastructure, and the agent delivery mechanisms are all designed to be handed off to a team as Layer-3 operationalizes. Layer-2 (matchmaker + Secure Network) is an informal network in Phase-1 but is explicitly architected to become a platform — the Phase-1 manual operation is not a workaround, it is the learning phase that informs the Phase-2+ design. Layer-3 (USB-C + Educational) is a Phase-2+ product but its design is already implied by Layer-1 operations. Layer-4 (YouTube-analyzer + tokens) requires significant capital and engineering investment but its Phase-1 equivalent exists as manual operations (Ruslan manually researching YouTube channels, manually performing the analysis that the SaaS will automate).

The LAYER-6 §11 evolution table [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11] establishes the five-gate cadence: G1 (€50K) → G2 (€200K) → G3 (€1M) → G4 ($100M) → G5 ($1T). Each direction has both a current Phase shape and a Phase-5 shape. The D26 Team 50–100 Enterprise lock [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D26] confirms that the target state is not a scaled solopreneur operation but a genuine enterprise-fast corporation. The portfolio is designed with this endpoint in mind: by Phase-3+, consulting and producer are BU-level operations with their own teams, not founder-dependent services; USB-C Integration Services is a standards-layer infrastructure play; the Secure Network is a multi-thousand-member professional ecosystem; YouTube-analyzer is a data-intelligence product with its own revenue line; educational products are licensed IP. The Path from Layer-1 to this state is the portfolio's internal coherence argument.

---

## §2.5 Revenue Priority Classification

The revenue priority classification aligns with the L6-ack'd P1A/P1B structure [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1 §134].

**P1A — active cold outreach (Consulting + Producer):** These two are the only directions against which Ruslan executes active outreach in Phase-1. ICP: Mittelstand (Geschäftsführer/Inhaber, DE manufacturing/professional services, 10–200 employees, GDPR-pain) and Startupper (English-speaking bloggers/infobiz with 5K+ audience and real domain expertise). The revenue rationale is direct: these are the two directions for which Ruslan can close a paying engagement within a 6-week decision cycle with no infrastructure investment, no platform build, and no partner network. They are the €50K Q2 2026 committed target per D9/D15 [src:decisions/JETIX-PLAN.md §3].

**P1B — opportunistic referral (Secure Network invite-list, USB-C early-access):** These are not active cold-outreach targets in Phase-1. They activate when a P1A engagement surfaces a client who fits the expanded Tier-1 ICP (High-earners $100K–150K+/year, millionaires $1M+/year per L6 §2.1) and who naturally fits the Secure Network invite-list or a USB-C early-access engagement. The P1B categorization means: if the opportunity surfaces, pursue it; do not allocate Ruslan outreach bandwidth to hunting it. The Secure Network invite-list is the Phase-1 form of Secure Network — not a product, but a pre-enrollment list of high-quality contacts who will receive the first invitations when the network launches post-€200K validation.

**P2 revenue-triggered (Matchmaker productization, Educational, USB-C full):** These three directions transition from informal operations or Phase-1 infrastructure to product form when G1 (€50K) is crossed and G2 (€200K) is in view. Matchmaker becomes a structured service with fee model. Educational products begin with a methodology repo V1. USB-C Integration Services gets its first productized client engagement. The trigger is not a date — it is the revenue gate that signals Jetix's consulting-motion hypothesis is validated.

**P3+ deferred (YouTube-analyzer SaaS, Tokens):** These two are not planned for Phase-1 or early Phase-2. YouTube-analyzer requires engineering capacity that does not exist at Phase-1 bandwidth. Tokens require $100K self-earned trigger (D23) and a regulatory navigation process that is explicitly a Phase-3+ activity. Neither is a missed opportunity in Phase-1; both are architectural requirements for the Phase-4/5 scale layer that become relevant exactly when Phase-1/2 revenue validates the methodology.

**The portfolio's P1 hard constraint:** Consulting and Продюсерский центр are the only two directions generating revenue in Phase-1. Everything else is either infrastructure that consulting revenue unlocks (matchmaker informal, USB-C first client, Secure Network invite-list) or a deferred investment that consulting revenue enables (Educational, YouTube-analyzer, Tokens). This is not a limitation — it is the portfolio's internal discipline. The discipline is the reason the portfolio can be executed by one person with zero capital outlay while remaining structurally compatible with a 50–100 person enterprise-fast corporation at Phase-3+.

---

*Draft by mgmt-expert (mode: integrator), Cell C-01. Awaiting brigadier §5.5.5 provenance gate before promotion to canonical LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md.*
