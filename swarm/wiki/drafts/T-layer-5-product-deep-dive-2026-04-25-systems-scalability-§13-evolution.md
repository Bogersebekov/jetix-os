---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: "§13"
title: "§13 Evolution per Gate — Master Table (9 Directions × 5 Gates)"
type: layer-deep-dive-section
mode: scalability
author: systems-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - decisions/JETIX-SYSTEM-OVERVIEW.md
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md
  - decisions/JETIX-PLAN.md
  - decisions/JETIX-VISION.md
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§2-portfolio.md
  - prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md
word_count_estimate: ~1500
confidence: high
confidence_method: gate-decomposition + book-as-frame (Meadows, Beer VSM, Ashby, Kauffman)
antifragility_check: pass
escalations: []
dissents:
  - source: open-question (§L5 §8 Q3 / §2-portfolio dissent)
    claim: "Matchmaker transition from manual to platform belongs at G2 (€200K) not G3 (€1M)"
    F: F4
    ClaimScope: "tension between JETIX-VISION §5 D21 (post-€200K validation) and JETIX-PLAN §5 (Phase-2 €200K→€1M platform features live); does NOT change the master table — both gates are represented; tension flagged for Ruslan ack"
    R: "refuted if consulting revenue at G1 produces repeat matchmaking-fee events that justify productized platform earlier; accepted if Phase-1 matchmaker throughput stays purely manual-Ruslan ceiling through G2"
---

# §13 Evolution per Gate — Master Table (9 Directions × 5 Gates)

---

## §13.1 Introduction — Why This Section Exists

The nine L5 directions are not peers. They occupy different positions in a sequenced architecture: some are the combustion engine of Phase-1 survival; others are latent infrastructure that only becomes viable once earlier directions have accumulated capital, validated demand, and built the specialist pool required to operate them. §13 is the **portfolio-level view** — the cross-section that reveals the sequencing logic across all nine directions simultaneously, rather than inside each direction individually.

What §13 does not do: it does not carry per-direction mechanics, ICP deep-dives, or activation-trigger prose (those live in §3.1–§3.9); it does not carry pricing structure, unit-economics arithmetic, CAC:LTV analysis, or margin detail (those are owned by L7 Business Deep-Dive); and it does not reopen any of the 28 locked decisions. §13 is **structure-and-status**: which direction is active, preparing, deferred, or heading toward sunset at each gate — and why that ordering, not another. [src:decisions/JETIX-SYSTEM-OVERVIEW.md §L5 Evolution path through 5 gates]

---

## §13.2 Master Table — 9 Directions × 5 Gates

Status legend: **active** = live and generating (or designed to generate) revenue or concrete pipeline at this gate | **preparing** = design / architecture / governance work underway, no revenue yet | **deferred** = not activated, bandwidth-constraint or gate-locked | **sunset** = actively wound down or replaced by a successor form

All pricing is deliberately absent from this table — see L7 for that. Status descriptors focus on form and readiness, not unit economics. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §6 Evolution Through 5 Gates]

| Direction | G0–G1 (€0–€50K, Q2 2026) | G1–G2 (€50K–€200K) | G2–G3 (€200K–€1M) | G3–G4 ($1M–$100M) | G4–G5 ($100M–$1T) |
|---|---|---|---|---|---|
| **1. AI Consulting** | **active** — 4-pack offer (session / 10 templates / community chat / billable services); €150/hr baseline; 2 productized contracts/quarter + 233 hours hourly target; sole revenue engine with Продюсерский центр [src:decisions/JETIX-PLAN.md §3.1.1] | **active** — scales from solo to first 2-3 hires; first contractors; consulting BU diversifies (specialization sub-units emerge post-€100K per audio_511); Path A/B/C decision made for productized engagements | **active** (declining share) — team 5-10; consulting becomes one BU among several; productized into USB-C Integration Services as primary delivery vehicle; pure-hours consulting deprioritized | **active** (minority share) — enterprise-tier consulting for Fortune-500-adjacent clients; team 20-50; Ruslan exits direct delivery; consulting is now a sales-motion entry point to broader Jetix ecosystem | **sunset** (replaced) — solo-delivery consulting fully replaced by USB-C standard-layer deployments, Alliance methodology licensing, and roy-replication networks; Jetix no longer bills consulting hours [src:decisions/JETIX-VISION.md §5 D18] |
| **2. Продюсерский центр** | **active** — pilot 1-2 English-speaking infobiz clients; monthly retainer model; AI-enhanced production pipeline (workshop → 10+ derivative artifacts); co-primary with consulting for €50K gate [src:decisions/JETIX-PLAN.md §3.3] | **active** — fully productized; 5-10 recurring clients; content team forming; English-language market (US + UK + international) primary | **active** — 10-30 recurring clients; systematic content factory; first DE/EU-language expansion; revenue-share partnerships emerge | **active** — major content production platform; Alliance members as both clients and co-producers; YouTube-analyzer SaaS feeds content intelligence | **active** — production infrastructure at civilizational scale; contributes to Mittelstand AI Alliance public communications; methodology-as-standard for AI-native content production |
| **3. USB-C Integration Services** | **deferred** — concept locked (D20), not productized; being delivered manually inside consulting engagements; Path A/B/C decision pending [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §USB-C reinforcement] | **preparing** — first productized client engagement (one of 3 Paths per STRATEGIC-INSIGHT §5); client-isolation mechanics designed; GDPR compliance layer sketched; methodology repo V1 stub created | **active** — all 3 Paths (A/B/C) supported; 5-20 client deployments; methodology repo V1 shipped; onboarding automation <2h; patent process prep begins (€200K gate per JETIX-PLAN §3.2) | **active** (scale) — 50-200 client deployments; distilled Mittelstand LLM proof-of-concept (STRATEGIC-INSIGHT §8 rec 7); first licensing income from methodology repo | **active** (standard-layer) — USB-C positioning public (D20); Mittelstand AI Alliance carries protocol; Jetix methodology is the "Windows firmware" for AI-augmented business [src:raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md] |
| **4. Matchmaker Platform** | **active** (manual, informal) — Ruslan personally connects tasks with specialists; AI-agent coordination layer absent; ceiling ~10 matches/week; no contract template yet [src:decisions/JETIX-VISION.md §5 D21] | **preparing** — matchmaker protocol documented; digital portrait template designed; first 5-10 portraits manually filled; AI-agent design begins; informal fee structure explored | **active** (platform MVP) — platform MVP live; machine-readable portraits; L4 agents route first matches; contract-fixing designed; matchmaker fees as formal revenue line | **active** (full platform) — AI agents handle routine matching; Ruslan reviews edge cases only; first external roys use matchmaker; Alliance 100-500 = platform supply pool | **active** (federated) — multi-roy meta-coordination; matchmaker federated across swarms; trust-graph and contribution-history = reputation infrastructure [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.1 Matchmaker mode] |
| **5. Secure Network** | **deferred** — Telegram invite-based chat (5-20 personally known); zero mechanics; «попутно»; no subscription, no governance, no architecture [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §10.1] | **preparing** — architecture design begins (post-€50K gate); thematic sub-channels per 11 archetypes; tool-sharing складчина active; first formal Alliance members; quality-gate protocol designed; €200K hard gate for build-start | **active** (launch) — Secure Network platform live; subscription tiers active; all 11 archetype sub-networks; token economy Phase-2 internal (D23); first merge-backs from Alliance (D27); 200-1000 members | **active** (scale) — international sub-networks; multi-language; 1000-5000 members; fork-community matures; Alliance governance-parliament active | **active** (consortium) — regulatory weight; «Internet of trusted professionals»; token public layer pending D23 ack; Mittelstand AI Alliance formal standards-body conversations [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3] |
| **6. YouTube-analyzer SaaS** | **deferred** — concept only (audio_514 «золотая жила»); no code; no data pipeline; no ICP validation; bandwidth-constrained by Phase-1 consulting delivery [src:reports/review_2026-04-24.md audio_514] | **deferred** — still constrained; reverse-engineering methodology (audio_527) matures in consulting; YT channel analysis done manually as a consulting deliverable | **preparing** — data pipeline design begins; YT API limits/ToS assessed; first internal proof-of-concept using reverse-engineering methodology (D24-adjacent); ICP validation through consulting clients who are YouTube operators | **active** (SaaS launch) — YouTube-analyzer SaaS publicly launched; seat/channel/query pricing tiers; Блогер archetype = primary SaaS user; feeds matchmaker intelligence and Продюсерский центр curation | **active** (scale) — bulk analysis at civilizational scale; integration with Alliance intelligence layer; competitive intelligence as platform feature |
| **7. Educational Products + Investor Programs + Grant Hunting** | **deferred** — methodology must stabilize in Phase-1 first; no courseware designed; D27 fork-and-merge governance TBD [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D27] | **preparing** — Jetix methodology begins crystallizing via consulting deliverables; educational skeleton drafts appear; first grant-hunting contacts mapped (EU funding bodies) | **active** — methodology repo V1 shipped (USB-C Path B prerequisite); first cohort course live; license tier designed; investor program structure drafted; D27 fork-and-merge governance decided | **active** (scale) — course library; cohort programs; methodology licensing to Alliance members; Investor Program as formal revenue line; first EU grants submitted | **active** (ecosystem) — methodology = global standard; university partnerships; open-source docs (Apache 2.0 per L6 ack IP license); commercial tiers proprietary Jetix-Corp |
| **8. Tokens / ICO (D23 Option B)** | **deferred** — $100K self-earned trigger not reached; D23 explicit: «design safe + adequate + thoughtful; NOT crypto-pump» [src:decisions/JETIX-VISION.md §8 D23] | **deferred** — trigger not reached | **preparing** — design begins post-€1M run-rate; internal utility token mechanics designed; specialist compensation scaffold; складчина token logic drafted; regulatory (EU MiCA) pre-assessment | **active** (internal utility) — token Phase-2 internal: specialist compensation, складчина access; NOT public; Alliance members as early holders | **active** (public layer pending ack) — Token Phase-3+ public layer if D23 Option B/C approved by Ruslan; IPO-alternative mechanism; ecosystem incentive layer |
| **9. Smart AI (flagship internal label)** | **active** (internal only) — narrative frame for all 8 directions; not an external product; not locked as D29; «как раньше были телефоны, потом смартфоны» [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §Smart AI] | **active** (internal) — label matures as consulting + producer directions generate client testimonials describable as «Smart AI» outcomes | **active** (internal + selective external) — D29 decision may emerge naturally as external product category language; stays internal until explicit Ruslan ack | **active** (external possible) — IF D29 locked: Smart AI becomes external category name for Jetix methodology; competitive differentiation at scale | **active** (category-defining) — «Smart AI» = category Jetix owns, as Kleenex owns facial tissue; not a product, a paradigm |

---

## §13.3 Per-Gate Narratives

### G0 → G1 — €0 → €50K (Q2 2026, sole committed absolute date)

**What is alive.** Two directions only: AI Consulting and Продюсерский центр. These are not choices — they are the mandatory pair per D11, confirmed in JETIX-PLAN §3 as the €50K gate mechanics [src:decisions/JETIX-PLAN.md §3.1]. Revenue decomposition requires both channels: ~€30K from 2 productized contracts × 2 quarters plus ~€35K from 233 consulting hours (§3.1.1). Without both streams running in parallel, the gate fails even if contract targets are nominally met.

**What is dormant.** Everything else. This is not a failure of ambition; it is a requisite-variety decision (Ashby: controller variety must match the variety it manages). At €0-€50K, Ruslan is a single-operator system with fixed weekly capacity. Activating Secure Network architecture, Matchmaker platform design, or USB-C productization in parallel would exceed the bandwidth budget without producing additional revenue — a Beer VSM Level-1 (operations) overload that would stall the primary revenue loop.

**What the gate crossing enables for the next period.** G1 crossing unlocks GmbH, Stripe, $1000 public experiment, and the Продюсерский центр scaling investment (D15 spend-unlock). Critically, it also unlocks the Secure Network architecture design phase — the €200K gate precondition. Smart AI as internal label operates throughout this phase as the narrative frame for client conversations. Matchmaker remains informal (Ruslan as manual connector, no contract template, no fee structure). [src:decisions/JETIX-SYSTEM-OVERVIEW.md §L5 Evolution path through 5 gates]

**Infrastructure ready for next gate.** The primary systems-level output of G0→G1 is not just revenue: it is **demand validation** (are the ICP archetypes Startupper + Operator-Founder-CEO actually converting?) and **methodology stabilization** (are consulting deliverables converging into repeatable patterns that can become USB-C integration services?). Both are prerequisites for G2.

### G1 → G2 — €50K → €200K (Validation Gate)

**What activates.** Three directions enter preparing mode: USB-C Integration Services (first productized client engagement), Matchmaker Platform (protocol documented + portrait template designed), and Secure Network (architecture design begins). The validation gate is not just a revenue number — it is the proof that the operating model survives beyond solo delivery [src:decisions/JETIX-PLAN.md §4]. First 2-3 hires arrive (D26 team trajectory: Phase-2 entry = sales + ops specialists). GmbH is now operational; legal entity enables formal Alliance discussions.

**What decommissions.** Nothing is explicitly retired, but pure-hours consulting (€150/hr unbundled) is actively productized out: D18 productization path means consulting revenue increasingly comes from packages, not time-tracking. Solo-delivery-only clients who cannot accept productized packages are deprioritized per the L5 §6 retirement table [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §6]. STRATEGIC-INSIGHT §8 recommendation 5 (speed: window NOW — 6-12 months) creates urgency: informal Alliance conversations should begin opportunistically during G1→G2, even if formal legal structure awaits G2+ [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8].

**Key BOSC trigger at this gate.** Trigger is **A (Agency)**: who delivers shifts from solo-Ruslan to first team members. This is the Beer VSM Level-2 (coordination) emergence point — the system crosses the threshold where coordination itself becomes a function, not just execution. If coordination is not made explicit at G2 (contracts, onboarding protocols, role clarity per JETIX-PLAN §3.2 OME Foundation layer), the Agency shift creates fragility rather than scale [src:decisions/JETIX-PLAN.md §3.2].

**Infrastructure ready for G3.** Alliance governance decision (Option A/B/C per L6 ack: Option C Hybrid — Foundation non-profit upstream + Jetix-Corp proprietary downstream) must be made *during* G1→G2, not at G2 arrival — EU legal filing time is 4-12 weeks, and a governance gap creates momentum loss when the G2 gate opens [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.2 Gate G2].

### G2 → G3 — €200K → €1M (Phase 2 Core)

**What activates.** This is the most structurally dense gate: four directions cross from preparing into active simultaneously. Secure Network **launches** (Telegram-based or upgraded; subscription tiers live; 200-1000 members). Matchmaker **platform MVP** deploys (machine-readable portraits; L4 agents routing first matches). USB-C Integration Services **productized** (all 3 Paths A/B/C supported; 5-20 client deployments; methodology repo V1 shipped). Educational Products / methodology repo **V1** live (D27 fork-and-merge governance decided; first cohort course; first license tier). D26 team reaches 5-10 specialists [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D26]. Foundation (Alliance Option C) **incorporated**; Mittelstand AI Alliance begins public EISA-moment positioning per STRATEGIC-INSIGHT §3.

**What decommissions.** Paid-ads campaigns without ROAS ≥3× are retired (per L5 §6 retirement table). The manual-Ruslan matchmaker ceiling (~10 connections/week) is officially replaced by protocol + platform; any matchmaking that remains purely in Ruslan's head is a defect at this gate, not a normal operating mode.

**Dominant systems dynamic.** The feedback structure shifts from a single reinforcing loop (Ruslan consults → earns → reinvests → more capacity) to a **multi-loop architecture**: (+ R1) consulting/producer revenue → team growth → capacity → more revenue; (+ R2) Secure Network members → portraits → matchmaker matches → more value → more members; (- B1) matchmaker quality degrades if portrait-completion rate falls below ~80% as onboarding scales faster than quality protocol. B1 is the dominant limiting loop at G2→G3. Leverage point: portrait-completion as hard gate to premium Secure Network features (Meadows L7 — information flow restructure: tie складчина access to portrait completeness, not payment alone) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.2 Gate G3].

**Infrastructure ready for G4.** YouTube-analyzer SaaS enters preparing mode during G2→G3. Reverse-engineering methodology (audio_527) is being applied to consulting deliverables; the data-pipeline design can begin post-€1M run-rate. Token economy Phase-2 internal begins design (D23 trigger: $100K self-earned reached somewhere in this span). [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §6]

### G3 → G4 — $1M → $100M

**What activates.** YouTube-analyzer SaaS **launches** (seat/channel/query pricing; Блогер archetype as primary SaaS user). Token Phase-2 internal utility **active** (specialist compensation + складчина tokens; not public). Secure Network crosses into international sub-networks with multi-language governance (1000-5000 members). USB-C Integration Services: 50-200 client deployments; first Mittelstand LLM proof-of-concept distilled model (STRATEGIC-INSIGHT §8 rec 7 — "Phoenix BIOS equivalent"). D24 open-source research direction **activates** (€1M+ threshold per JETIX-PLAN §6). Team reaches 20-50; D26 holding structure crystallizes; first replicated roy (D21) at $10M-$100M revenue [src:decisions/JETIX-VISION.md §5 D21].

**What decommissions.** Any business unit below 30% Constellation-style hurdle rate sustained 4 quarters is retired per the L5 §6 table. Solo-founder-dependent service delivery is actively wound down — D26 team + D21 roys absorb delivery. The consulting direction is now a minority revenue share; its primary function shifts to being a **sales-motion entry point** to the broader Jetix ecosystem, not a standalone revenue line.

**Dominant BOSC trigger.** **T (Time)** — cycle-time shifts from quarter-cycle planning to multi-year planning horizon. Beer VSM Level-4 (intelligence/futures) and Level-5 (identity/policy) must be **explicitly instantiated as distinct sub-systems** at this gate; otherwise variety of coordination needs (multi-language, multi-niche, multi-roy) exceeds the capacity of single-brigadier-swarm architecture, violating Ashby requisite variety at the meta-control level [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.2 Gate G4]. MHT event: **Context Reframe** — planning artefacts re-anchored to multi-year horizon; the swarm itself must be audited and potentially split (VSM Level-3 audit function as distinct sub-system) [src:decisions/JETIX-SYSTEM-OVERVIEW.md §0].

### G4 → G5 — $100M → $1T

**What activates.** Token Phase-3+ public layer (if D23 Option B/C approved by Ruslan — this is NOT automatic; it requires explicit ack). Mittelstand AI Alliance at civilizational scale: 1000-5000+ formal members; standards-body conversations (ISO, EU regulatory); regulatory weight. USB-C positioning at full public launch (D20): the protocol is now the standard, not a positioning claim. Multi-roy Federation (D21 at scale): dozens of active Jetix-methodology forks; best mutations return upstream (D27 Linux Foundation analog). Team 50-100 steady-state per D26. Consulting direction sunset: replaced entirely by USB-C standard-layer deployments and Alliance methodology licensing [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md §D26 + §D27].

**What decommissions.** Solo-founder-dependent services (sunset trigger explicit in L5 §6 table). Any direction that cannot scale to federated delivery without Ruslan's direct involvement must either be productized into USB-C/Alliance frameworks or retired. The system's identity (Beer VSM Level-5) is no longer "Ruslan + swarm" but "Jetix methodology as civilizational infrastructure."

**What the gate represents systemically.** Kauffman's adjacent-possible: at $1T, Jetix has exhausted adjacent-possible moves available from the current configuration — it is at the boundary of a new state space. The "Windows firmware for AI-augmented business" metaphor matures from aspiration to fact [src:raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md]. MHT event: **Fusion** — regulators and standards bodies become constituents of the Jetix holon, not externalities.

---

## §13.4 Sequencing Logic — Why This Order and Not Another

The ordering is not arbitrary. It emerges from three compounding constraints applied in sequence.

**Constraint 1: D11 mandates consulting + producer as the Phase-1 revenue core.** [src:decisions/JETIX-VISION.md §5 D11] Without these two running and generating the €50K gate revenue, nothing else in the portfolio activates — the D15 spend-gate is closed. This is not a stylistic choice; it is the physical constraint of zero external funding and a sole-founder operating budget. The two directions that require the least infrastructure (consulting hours + AI-enhanced content production) must go first because they are executable with today's tools and today's team.

**Constraint 2: Platform directions require a network, and networks require nodes.** Matchmaker, Secure Network, and USB-C Integration Services are all network-value products — their quality is a function of the specialist pool and client base that consulting and producer build in Phase-1. Attempting to launch these platforms at G0 would be launching an empty room: zero portraits, zero specialists, zero clients who have validated the value proposition. STRATEGIC-INSIGHT §8 recommendation 2 is explicit: "Moat = Mittelstand knowledge + network + compliance — non-cloneable" [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8]. That moat is accumulated during Phase-1 consulting delivery, not before it.

**Constraint 3: Data-intensive and capital-intensive directions require prior revenue and methodology stability.** YouTube-analyzer SaaS requires a data pipeline, engineering investment, and ICP validation that exceeds Phase-1 capacity (per §2-portfolio dissent: tension between audio_514 «золотая жила» urgency and gate-sequencing reality [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-mgmt-integrator-§2-portfolio.md §2.1 dissent]). Tokens require regulatory compliance work, $100K self-earned trigger, and D23 explicit design-before-build mandate. Educational Products require the methodology to stabilize first — you cannot license what does not yet have stable form. STRATEGIC-INSIGHT §8 recommendation 5 enforces urgency at the top (6-12 months window to capture Mittelstand positioning) but does not override D15 sequencing below it [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8].

The result is a portfolio that behaves like a compound interest system (Senge Fifth Discipline): early revenue from consulting + producer funds the infrastructure required by platform directions; those platforms generate the network effects that justify the SaaS and token directions; and the data + methodology assets from all earlier directions fund the civilizational-scale standard layer. Each gate crossing is a **Phase Promotion** in the MHT catalogue — the system level-shifts rather than just growing, per the BOSC-A-T-X framework.

---

## §13.5 Portfolio Activation Diagram

ASCII representation of direction activation across 5 gates. Status codes: `[A]` = active, `[P]` = preparing, `[D]` = deferred, `[S]` = sunset.

```
Direction                G0–G1      G1–G2      G2–G3      G3–G4      G4–G5
                        (€0-50K)  (50K-200K) (200K-1M)  ($1M-100M)  ($100M-$1T)
──────────────────────────────────────────────────────────────────────────────────
1. AI Consulting          [A]────────[A]────────[A]────────[A]──────────[S]
2. Продюсерский центр     [A]────────[A]────────[A]────────[A]──────────[A]
3. USB-C Integration      [D]────────[P]────────[A]────────[A]──────────[A]
4. Matchmaker             [A*]───────[P]────────[A]────────[A]──────────[A]
5. Secure Network         [D*]───────[P]────────[A]────────[A]──────────[A]
6. YouTube-analyzer       [D]────────[D]────────[P]────────[A]──────────[A]
7. Educational Products   [D]────────[P]────────[A]────────[A]──────────[A]
8. Tokens / ICO           [D]────────[D]────────[P]────────[A*]─────────[A**]
9. Smart AI (label)       [A]────────[A]────────[A]────────[A]──────────[A]
──────────────────────────────────────────────────────────────────────────────────

Key: [A*] = active but manual/informal
     [D*] = deferred but Telegram chat «попутно» live (not a product)
     [A*] G3–G4 Tokens = internal utility only (NOT public)
     [A**] G4–G5 Tokens = public layer ONLY if D23 Option B/C explicitly acked by Ruslan

Active-direction count per gate: 2 → 2 → 5 → 7 → 7 (1 sunset)

BOSC-A-T-X first trigger per gate:
  G0–G1: C+S (Composition + Scale): swarm installs measurement substrate (zero-to-operational)
  G1–G2: A (Agency): first hires; solo → team coordination structure
  G2–G3: C+S (Composition + Scale): 4 directions cross from preparing to active simultaneously
  G3–G4: T (Time): horizon shifts from quarterly to multi-year; VSM L4/L5 instantiated explicitly
  G4–G5: X+B (eXternal + Boundary): regulatory bodies enter system boundary; Fusion MHT event

[src:decisions/JETIX-SYSTEM-OVERVIEW.md §L5 Evolution path + §L6 5 Gates table;
 swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §9]
```

---

## §13.6 Cross-References and L7 Deferral

**What §13 explicitly does not own.** Every pricing figure, tier structure, packaging decision, payment cadence, discounting rule, CAC:LTV ratio, cohort analysis, margin arithmetic, and unit-economic projection for any of the nine directions belongs to **L7 Business Deep-Dive**. §13 declares which direction is active at which gate and in what structural form — it does not say what that activity costs, what margin it produces, or how the unit economics evolve as the direction scales.

Specific deferrals to L7: consulting 4-pack pricing tiers (€150/hr baseline stated here as a gate-marker, not a model); Продюсерский центр retainer range; USB-C Path A/B/C pricing structure; Secure Network subscription tier structure; YouTube-analyzer SaaS seat/query pricing; Educational Products license and cohort economics; Token tokenomics and economic design (also pending D23 explicit ack and EU MiCA regulatory analysis). All of these carry "PLACEHOLDER" status in §2 Portfolio table and remain PLACEHOLDER here.

**Per-direction evolution sub-items.** Each direction's own gate-by-gate mechanic, ICP mapping, and activation-trigger prose lives in §3.1–§3.9. §13 is the summary matrix; §3.1–§3.9 own the depth. On any conflict between the summary status in §13.2 and a per-direction statement in §3.x, the per-direction section is authoritative for that direction's specifics; §13 governs cross-portfolio sequencing logic.

**L6 parallel.** The L6 Community Deep-Dive §11 provides the closest structural parallel to §13: it maps L6 community dimensions across the same 5 gates with the same status-descriptor discipline [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §11.1]. §13 and §11 are designed to be read together: §13 declares what Jetix sells at each gate; §11 declares who is in the ecosystem being sold to and built around that portfolio.

---

*Drafted by systems-expert (×scalability), task T-layer-5-product-deep-dive-2026-04-25, cycle cyc-layer-5-product-deep-dive-2026-04-25. Awaiting brigadier §5.5.5 provenance gate + Ruslan HITL review before promotion to canonical wiki.*
