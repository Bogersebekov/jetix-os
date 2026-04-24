---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.4
direction: matchmaker-platform
type: layer-deep-dive-section
mode: integrator
author: systems-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
  - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md
  - decisions/JETIX-VISION.md
  - decisions/JETIX-SYSTEM-OVERVIEW.md
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md
  - decisions/JETIX-PLAN.md
  - reports/review_2026-04-24.md
  - swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md
word_count_estimate: ~2100
confidence: high
confidence_method: multi-source-synthesis-with-locked-decisions
escalations: []
dissents:
  - id: D-match-1
    claim: "Match-fee should be charged to task-side only (buyer pays), not to specialist-side"
    F: F3
    ClaimScope: "Holds under anti-commodity positioning logic; fails if Jetix needs faster specialist-pool growth (specialists resist any fee before track record)"
    R: "Refuted if task-side-only pricing leads to specialist oversupply + task undersupply over 3 cycles; accepted if task-side-only NPS specialist >= 8.5 sustained 2 quarters post Phase-2 launch"
  - id: D-match-2
    claim: "Platform MVP should gate at G3 (€1M), not G2 (€200K)"
    F: F4
    ClaimScope: "Holds under Secure Network liquidity prerequisite logic (matchmaker needs member pool); contested by opportunity-cost argument that delaying MVP beyond G2 lets competitors occupy matching UX"
    R: "Refuted if a competitor launches an AI-smoothed matching product for the D22-filtered audience before Jetix G3; accepted if Secure Network at G2-end provides >=100 active members making G3 Platform MVP launch viable"
---

# §3.4 — Matchmaker Platform Direction

## 1. Mission

The Matchmaker platform connects people carrying complex cross-disciplinary tasks with the specialists capable of resolving them. The connecting act itself is lubricated by an AI-agent coordination layer that reduces friction in context transfer, introduction drafting, scheduling, and post-match documentation. Over time — and this is the compounding mechanic that distinguishes it from a generic marketplace — specialists who deliver well gradually graduate into deeper participation in the Jetix ecosystem.

The mission statement is grounded directly in a locked decision and a verbatim founder voice. D21 (Roy-replication) declares the matchmaker as a structural primitive of Jetix's network: every specialist who enters through a match is a candidate node in the emerging Roy-replication network [src:decisions/JETIX-VISION.md §5 D21]. The mechanic itself was articulated by Ruslan in Voice 2 on 2026-04-24 as a seven-step process:

> *«ищутся какие-то сложные вопросы задачи и находятся люди которые их могут решить и вот это блять вместе соединяется — надо какой-то сложный клиент другому это подрядчик — это всё агентами искусственным интеллектом смазывается происходит быстрее качественнее адекватнее — плюс ещё фиксируется всё адекватно — и вот так вот понемногу нарастают контакты — сперва людям помогаем помогаем потом это нарастает мясом — потихоньку специалисты начинают работать с нами переходят к нам»*
> [src:raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md §Voice 2]

This passage is not aspirational framing — it is the canonical mechanic specification: task-finding, specialist-finding, connection, AI-smoothing, outcome-fixing, network-accumulation, ecosystem-graduation. Every phase-level design choice in this section traces back to this seven-step verbatim sequence. The L5 productization layer built here answers the question L6 §6 intentionally left open: how does this mechanic become a paid, scalable product tier, rather than remaining a goodwill service that Ruslan runs manually?

Systemically, the matchmaker occupies Beer VSM System-3 (audit/optimisation coordinator) within the Alliance's viable system. Without it, the Alliance degrades into an uncoordinated contact list. With it, each additional member increases the network's coordination value super-linearly, following Metcalfe dynamics [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6 Systems frame]. The productization question is therefore also a VSM architectural question: at which scale threshold does System-3 need to be formalized, budgeted, and partially self-financing rather than gifted from Ruslan's attention?

## 2. Phase Activation

The L6 §6 ack established three mandatory cadences. L5 inherits them without re-litigation and adds the productization layer — the offer structure, the pricing posture, and the gate-triggered commercial activation that transforms each cadence from an operational mode into a revenue-bearing product.

**Phase 1 — manual Ruslan (G0 → G1, €0 → €50K).** Already running per L6 §6.1. Not productized. Ruslan mentally scans his network, identifies relevant specialists, initiates an introduction (Telegram / email / WhatsApp), and tracks the result informally. The system limit is approximately 10 connection-events per week before cognitive overhead degrades match quality [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.1]. This phase is deliberately non-monetized: the strategic rationale is goodwill investment, relationship depth, and consulting-funnel feeding. Every successful match is a proof-of-concept for the platform phases that follow. The Phase-1 leverage point (Meadows L5, information flows) is simply to start recording each match — task, parties, status, outcome — in a lightweight scoreboard. Without that data, Phase-2 AI-smoothing has no training signal and no baseline metric against which improvement can be measured [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.1 Leverage point].

**Phase 2 — AI-smoothed coordination (G1 → G2, €50K → €200K).** The trigger fires when match volume consistently exceeds 10 connection-events per week for two consecutive months — meaning Ruslan's manual bandwidth is structurally saturating. At that point, the matchmaker-agent (L4 brigadier-orchestrated) takes over intake structuring, candidate scoring, introduction drafting, scheduling coordination, and outcome recording. Ruslan remains in the loop as final approver — the HITL gate is non-negotiable because relationship nuances and strategic placement judgments require founder judgment that no portrait-scoring algorithm replaces [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.2]. The commercial activation in this phase is a match-fee tier: task-side pays $500–$2,000 per successful match (complexity-tiered; see §5 for the offer structure), and a retainer option unlocks for repeat task-side clients. This is the first moment the direction generates direct revenue rather than serving as a consulting-funnel feeder. Two hard preconditions must hold before Phase-2 launches: (a) digital portraits exist for at least 15 Alliance participants (§10 Secure Network infrastructure per L6), and (b) Phase-1 scoreboard contains at least 30 completed matches with outcome data [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.4 Trigger 1].

**Phase 2+ — Platform mode (G2 → G3, €200K → €1M).** The trigger fires when Alliance exceeds 100 active members and match-events exceed 30 per month stably, AND Ruslan's HITL-approval queue creates a wait of more than 3 days — meaning even AI-assisted Human-in-Loop approval is the new bottleneck. At this point the direction requires formalized governance of the matching function: a public (Alliance-internal) matching portal with structured task posting, reputation scoring, bid mechanics, and escrow. The commercial tier upgrades: subscription access for task-side ($500–$1,500/month), transaction fees, and Secure Network membership gate for match initiation (only paying members can initiate). Final pricing is L7-owned; all figures here are structural placeholders [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.3 + §6.4 Trigger 2].

**Sunset:** none. At Phase 5 (G4–G5, $100M → $1T) the matchmaker scales into multi-roy meta-coordination: each sub-roy runs its own matchmaker instance federated through Jetix canonical, with fork-and-merge (D27) governance of the protocol layer itself [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27].

## 3. Target ICP Mapping (L6 Trinity)

The matchmaker is a two-sided market. The L6 Trinity maps differently onto each side, and the D22 5-criteria filter applies asymmetrically.

**Task-side (buyers of the match).** These are the people who bring the complex cross-disciplinary problems. From the L6 ICP spectrum: consulting clients overlapping with §3.1 (who already passed D22 and payment-ability filters); Mittelstand entrepreneurs with projects requiring combinations of technical, legal, creative, and strategic capabilities that no single firm delivers; high-earner solopreneurs who need specialized collaborators but lack the network density to find them quickly. Payment-ability filter: task-side must clear $5K/month recurring OR $10K one-shot, per the L6 binding ack [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1]. The four Phase-1 primary-buyer archetypes (Startupper / Блогер / Operator-Founder-CEO / Teacher) all qualify as task-side: each faces compound challenges (Startupper needs tech + legal + sales simultaneously; Teacher needs curriculum research + production + distribution; Operator-Founder-CEO needs governance + specialist capabilities; Блогер needs research + filming + editing + repurposing) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §3 Archetypes table].

**Specialist-side (sellers of expertise).** These are the people who resolve the complex tasks. The four primary L6 archetypes also appear here — especially Startupper, Designer, Engineer, and Researcher — but Phase-2+ extends to all seven remaining archetypes from JETIX-VISION §7.1 (Инженеры / Ресёрчеры / Философы / Инвесторы / Продавцы / Менеджеры / Дизайнеры) when they pass the D22 5-criteria filter. Specialist-side pays nothing in Phase-1: they supply expertise, and the match creates goodwill plus a portfolio entry. Phase-2+ introduces a success-fee (10–15% of the first engagement value post-match) or an optional «certified specialist» badge within the Secure Network [src:decisions/JETIX-VISION.md §8 per-archetype angles]. The D22 filter is a prerequisite for any specialist entering the pool — not for quality aesthetics, but because an unstable or deluded specialist degrades match quality and, per the Stable criterion, «without this quality all others are devalued» [src:decisions/JETIX-VISION.md §7.2 D22].

**Anti-LinkedIn positioning.** The two-sided market is explicitly not a general labor market. Ruslan's L6 framing — *«не LinkedIn где быдло одно которое ищет каких-то рабов»* [src:decisions/JETIX-VISION.md §10] — describes the system boundary: the matchmaker's inclusion criterion is D22 plus payment-ability, which at projected pass-rates of 0.1–1% of LinkedIn-scale populations creates a high-density small market rather than a low-density large one. This is Ashby's requisite-variety principle applied to market design: the controller (the matching mechanism) must have variety at least equal to the problem space it coordinates; a high-D22-pass-rate network achieves this with far fewer nodes than a general marketplace requires [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §4.6].

## 4. Value Proposition

**Task-side problem statement.** A Mittelstand Geschäftsführer running a precision engineering company needs simultaneous input from an AI-systems engineer, a GDPR compliance specialist, and a change-management consultant to implement an internal AI workflow. LinkedIn recruiting takes months and produces candidates optimized for permanence, not project depth. Upwork produces commodity pricing and no context alignment. Asking friends produces biased recommendations based on social proximity rather than capability fit. The problem is not finding people; it is finding pre-qualified, contextually aligned people quickly enough that the decision window does not close [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §2.1 + §6 Systems frame].

**Specialist-side problem statement.** An experienced researcher-consultant wants substantive projects where the client has already done the thinking, articulates the problem precisely, and can act on the output. Most platforms send commodity RFQs. Even warm referrals arrive without context. The specialist spends 30–50% of billable time on intake, alignment, and expectation management — structural overhead that reduces effective hourly rates and creative bandwidth.

**What Jetix Matchmaker delivers to both sides.** Time-to-connect drops from weeks to days because the candidate pool is pre-filtered by D22. Both sides enter the first conversation aligned because the AI-smoothing layer drafts a context packet — task summary, parties' relevant backgrounds, expected next step — before the introduction. The match event is recorded with provenance (D25 company-as-code: every match is a commit with attribution and outcome) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D25]. Over time, the specialist's track record accumulates in their digital portrait, making each subsequent match both faster and higher-quality through reputation scoring.

**How Jetix differs from alternatives.** Against Upwork: Jetix is not a commodity labor market and does not compete on price; it competes on qualification depth and context transfer quality. Against Toptal: Toptal curates top-down through an internal vetting process that is expensive and opaque; Jetix's D22 self-selection is transparent and philosophically justified. Against Slack communities: there is no coordination layer in an unmoderated Slack; the AI-smoothing layer is the structural differentiator. Against agency middlemen: an agency captures 40–50% margin while intermediating the relationship; Jetix charges a match-fee and then steps aside, with the relationship belonging to the parties. Against LinkedIn: the structural anti-spam design — D22 filter plus payment-ability gate plus Secure Network membership requirement — eliminates the spray-and-pray dynamic [src:decisions/JETIX-VISION.md §10 + decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §7.3].

**USB-C connection.** The matchmaker is how USB-C positioning (D20) manifests at the human-network layer. If the consulting direction (§3.1) and USB-C integration services (§3.3) are the technical connector, the matchmaker is the social connector: a protocol for people-to-people coordination that works regardless of which niche or discipline the parties come from [src:decisions/JETIX-VISION.md §5 D20 + swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md §2 matchmaker row].

## 5. Offer Structure (3-Tier per Cadence + Productization Layer)

**Phase 1 — free / manual.** Not monetized. Ruslan personally initiates introductions using three template types (Telegram / email / WhatsApp, per L6 §6.1 Phase-1 action list). The goodwill investment logic: every match serves as a relationship-building event that strengthens Ruslan's position in the network, feeds consulting pipeline, and accumulates the scoreboard data required for Phase-2 AI training. There is no fee, no contract, no formal terms. The cost is Ruslan's attention — approximately 45–60 minutes per match-event at Phase-1 volume [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.5 KPI table].

**Phase 2 — match-fee tier (placeholder pricing, L7 owns final).** Task-side pays per successful match. Complexity tiers:
- Standard match (one specialist, defined brief): $500–$800
- Complex match (multi-specialist coordination, cross-disciplinary): $1,200–$2,000
- Retainer option (match-on-demand, repeat task-side clients): $2,000/month flat

Specialist-side: no upfront fee in Phase-2-early. Success-fee of 10–15% of first engagement value post-match introduced in Phase-2-mid (when specialist reputation data is sufficient to justify the ask without triggering specialist churn).

All Phase-2 pricing is a structural placeholder. L7 Business Deep-Dive owns the unit-economics verification: margin-of-safety calculation, TAM sizing, and competitor pricing analysis. The structural rationale for the placeholder ranges is that $500–$2,000 sits comfortably within the task-side $5K/month payment-ability filter (a single match fee is less than half a month's payment-ability threshold), and 10–15% success-fee is below agency markup rates, making the specialist-side economics favorable relative to alternatives [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.6 Capital allocation + L6 §2.1 payment-ability filter].

**Phase 2+ — platform tier.** Subscription $500–$1,500/month task-side access. Transaction fee layer (percentage of escrow release). Secure Network membership gate: only paying Secure Network members can initiate platform-mode matches. This gate is not purely commercial — it is a variety-control mechanism: only D22-filtered, membership-paying participants interact, preserving the network's density and quality properties as it scales [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.3 Platform Mode].

## 6. Delivery Mechanism

**Agents involved across phases.** The L4 agent layer orchestrated by brigadier carries the operational load. In Phase-2 AI-smoothed mode: brigadier (orchestration); sales-researcher (specialist-side profiling — building and maintaining digital portraits); sales-outreach (task-side intake — structured intake form processing, qualification against D22); knowledge-synth (context packet drafting — summarizing task brief + both parties' profiles into introduction document); manager and personal-assistant (scheduling coordination, reminder cadence, outcome logging) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.2 Цикл Phase 2].

**KM-Mat infrastructure.** Each matchmaker project bootstraps via `/project-bootstrap --type=consulting --client=matchmaker-<id>`. Per-task markdown files under a `leads/` directory track each task-side request. A `specialists.md` file per specialist maintains their portrait — this is the digital-portrait substrate required for Phase-2 AI scoring, per the precondition in L6 §6.4 Trigger 1. Match-events are logged as structured commits (D25 company-as-code: every match = a commit with provenance — parties, task, outcome, timestamp) [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D25]. The `/ask` skill queries the specialist KB via query-driven search (D28) when a new task arrives and the agent needs to identify candidate specialists from the portrait pool [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D28 reference in intake]. `wiki/graph/edges.jsonl` records the typed edges between match-events, specialists, tasks, and clients — building the provenance graph that enables reputation scoring at Phase-2+.

**Seven-step mechanic (mandatory verbatim-grounded list).** The Voice 2 sequence maps onto the delivery as follows:

1. **Task posted and qualified.** Task-side submits request (Telegram DM in Phase-1; structured intake form in Phase-2+). Sales-outreach agent applies D22 5-criteria check and payment-ability verification. Unqualified tasks are declined with a redirect to the consulting direction (§3.1) for clients who need foundational AI work before a specialist match is productive.

2. **Specialist pool queried.** In Phase-1 Ruslan mentally scans. In Phase-2 the sales-researcher agent queries the specialist portrait KB via D28 query-driven search, scoring candidates on skill-fit, archetype-fit (from the 11 L6 archetypes), availability, and prior collaboration history.

3. **AI drafts context packet.** knowledge-synth agent produces a structured introduction document: task summary with key constraints, both parties' relevant background excerpts from their portraits, expected next step (15-minute call within 48 hours). This packet is what makes both sides enter the first conversation contextually aligned — not cold [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.2 step 4].

4. **Ruslan delivers final judgment on the match.** HITL gate. The D13 principle applies: the AI layer is open surface (sees portraits, scores candidates, drafts context); the closed core (relationship nuances, strategic placement, trust calibration) remains with Ruslan until Phase-3 when formal governance distributes this function. No match ships without Ruslan approval in Phase-1 and Phase-2 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.2 step 3].

5. **Introduction and coordination AI-smoothed.** The context packet is sent. The personal-assistant agent coordinates scheduling (proposes calendar slots, sends reminders, follows up if no response after 48 hours). Ruslan's time-per-match drops from 45–60 minutes (Phase-1) to 5–10 minutes HITL review in Phase-2 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.5 KPI table].

6. **Match-event recorded with provenance.** Outcome logged (initiated / meeting held / delivered / fell through) as a structured commit per D25. The `wiki/graph/edges.jsonl` edge created: `task-X → specialist-Y → outcome-Z`. This edge is the foundation of the reputation score at Phase-2+ and the training signal for next-round AI scoring [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D25 + decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.1 Phase-1 Leverage point].

7. **Specialist graduates into Jetix ecosystem.** Over multiple successful matches, a specialist's portrait accumulates a reputation score, demonstrates alignment with D22 criteria in action (not just in screening), and becomes a candidate for deeper Jetix participation: Alliance Strategic membership, roy-replication role (D21), or Secure Network featured specialist status [src:decisions/JETIX-VISION.md §5 D21 Roy-replication + decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6 Matchmaker mechanic].

## 7. Competitive Positioning

The matchmaker sits in a competitive space defined by adjacent coordination products, none of which combine the specific dimensions Jetix deploys simultaneously.

**Upwork / Fiverr.** Commodity labor marketplace. Task-side finds price competition creates race-to-bottom quality. Specialist-side sees volume-driven, low-context requests. No AI coordination layer. No D22 filtering. Kill-condition for this positioning: if Upwork launches a D22-equivalent quality filter AND an AI-smoothed context-transfer product before Jetix reaches Phase-2 platform scale.

**LinkedIn.** General professional network optimized for employment and broad network maintenance. No coordination layer for project-specific matching. The «рабов ищущих рабов» critique is a systems diagnosis, not a moral judgment: LinkedIn's feedback loop (larger network → more signal → more connections → larger network) optimizes for volume, which drives quality dilution over time [src:decisions/JETIX-VISION.md §10]. Kill-condition: if LinkedIn launches an invite-only, quality-gated matching product with AI context transfer.

**Toptal / Andela.** Top-down curated talent networks with internal vetting. Expensive ($150–300/hour floor), not complex-task focused (optimized for engineering and design), opaque vetting process. Kill-condition: if Toptal opens multi-disciplinary matching with transparent criteria and client-side self-service.

**Slack / Discord communities.** Unmoderated coordination with no infrastructure. High noise-to-signal, no reputation layer, no escrow. Kill-condition: if a well-resourced community-platform startup (e.g., Circle.so) builds D22-equivalent filtering plus AI matching on top of their existing community infrastructure.

**Agency middlemen.** 40–50% margin capture, long lead times, client lacks direct specialist relationship. Kill-condition: if agencies build technology that makes their process transparent and fast enough to compete on total cost (fee + time).

**Core Jetix advantage differential.** The unique combination — D22 filter + AI-smoothed context transfer + D25 provenance recording + Roy-replication graduation path — is not replicable by any single competitor in the current competitive landscape because it requires the entire upstream system (Alliance, Secure Network, wiki KB architecture, brigadier L4 agent layer) to exist as the substrate. A competitor can copy any one element; replicating the system requires replicating Jetix's entire operating infrastructure [src:decisions/JETIX-VISION.md §10 What makes Jetix un-reproducible].

**Risks.** Cold-start (two-sided market needs liquidity — specialist pool without task flow, or task flow without specialist pool, creates a chicken-and-egg dynamic). Quality policing at scale (D22 filter requires human judgment in Phase-1; automating it without degradation is Phase-2 design challenge). Regulatory surface (cross-border coordination of independent contractors creates EU classification risk, VAT/USt on match fees, data transfer compliance under GDPR — Phase-2 lawyer consult required before fee-charging begins in DE/EU). Consulting cannibalization (a match that could have remained inside §3.1 consulting leaks to an external specialist, reducing §3.1 revenue; needs explicit qualification: matchmaker serves tasks that require a capability Jetix does not have internally, not tasks Jetix could close directly).

## 8. Evolution per Gate

**G0 → G1 (€0 → €50K, Phase 1 current).** Manual Ruslan-only mode. Objective: 3–10 cumulative matches by Q2 2026. All free. Primary function: relationship depth + consulting-funnel feeding + scoreboard data accumulation. Key deliverable before G1 closes: Phase-1 scoreboard with at least 30 match records (task type, parties, status, outcome) and at least 15 specialist digital portraits. These two artefacts are the preconditions for Phase-2 AI-smoothing and are therefore critical-path items for the direction's commercial activation [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.4 Trigger 1 preconditions].

**G1 → G2 (€50K → €200K, Phase 2 early).** AI-smoothing design begins at G1; production deployment at G2 trigger. Agent infrastructure built: matchmaker-agent intake + portrait scoring + introduction drafting. Match-fee tier launched ($500–$2,000 per match, complexity-tiered). Target: 30–100 cumulative matches. Capex: €5–15K for agent development per L6 §6.6 capital allocation [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.6]. The Senge «Shifting the Burden» risk activates here: Ruslan must continue personally meeting each new Alliance participant (≤30 minutes) even as the agent takes over operational coordination, to prevent the human relationship network from degrading behind a technically functional but relationally shallow matching engine [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.2 Senge risk].

**G2 → G3 (€200K → €1M, Platform MVP).** Trigger: Alliance >100 active + ≥30 connection-events/month stable + HITL queue >3 days. Platform MVP launches: structured task-posting form, reputation scoring, bid mechanics, escrow integration, Secure Network membership gate for match initiation. Capex: €50–100K per L6 §6.6 [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.6]. Subscription tier activated. Cross-direction integration deepens: §3.3 USB-C client deployments become match-sources (clients with Jetix-installed local KB generate tasks for specialist placement); §3.5 Secure Network provides the member liquidity the platform requires; §3.7 Educational direction becomes the graduation pathway for specialists moving from «matched once» to «licensed Jetix methodology partner» [src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md §3 §3.4 dependencies].

**G3 → G4 ($1M → $100M, Platform scale).** Multi-language and multi-region platform. Specialist-side reputation layer with work-product provenance (D25 git-backed match-event trail becomes public — within Alliance — reputation artefact). Alliance Foundation integration: matchmaking may offer subsidized or zero-fee matching for Alliance non-profit referrals as a membership benefit. Integration with §3.5 Secure Network becomes architectural: matching is the relational engine that drives Secure Network engagement, and Secure Network is the liquidity pool from which specialists are drawn. Per-gate revenue estimate (analogical projection from L6 investor peer): approximately $1.31M blended matchmaker revenue per quarter at G4 scale [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.6].

**G4 → G5 ($100M → $1T, Multi-roy meta-coordination).** Per D21 Roy-replication: each sub-roy in its niche runs its own matchmaker instance federated through Jetix canonical. D27 fork-and-merge governance: individual roy matchmaker instances fork the canonical protocol, adapt for their niche (sector-specific qualification criteria, regional escrow law compliance, language), and best mutations merge back upstream. Ruslan maintains System-5 (identity/policy) authority via the Foundation technical-steward role; roy matchmaker instances operate as System-1/System-2 functions under the canonical protocol [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27 + decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5.3 Option C VSM mapping]. At this scale the matchmaker per-quarter revenue reaches approximately $24M (investor peer bounded estimate from L6 §6.6) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.6].

## 9. Cross-Direction Dependencies

The matchmaker is the relational infrastructure binding four directions simultaneously. It both consumes from and produces value for each.

**Depends on §3.1 Consulting.** Phase-1 task pipeline comes almost entirely from consulting clients. A client engaged in a §3.1 retainer identifies a specialist need that Ruslan cannot fill internally → this surfaces as a match task. The consulting relationship provides the context depth required for a high-quality match. Without an active consulting pipeline there are no qualified task-side inputs in Phase-1. The dependency is mutual: consulting clients who receive a successful match are more likely to renew retainers, creating a reinforcing loop between §3.1 and §3.4.

**Depends on §3.5 Secure Network.** Phase-2+ platform requires specialist portrait infrastructure and a verified-member pool. Both are provided by Secure Network architecture: digital portraits live in Secure Network profiles; membership verification enforces D22 filter at the Secure Network layer, so any Secure Network member is already pre-qualified for the specialist pool. Without Secure Network, Phase-2+ platform has no addressable specialist inventory. The Platform MVP G3 trigger explicitly requires Secure Network liquidity (≥100 active members) [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.3 + §6.4 Trigger 2].

**Depended on by §3.2 Producer Center.** The Producer Center direction needs niche specialists — videographers, scriptwriters, domain-expert commentators, audio engineers — that Ruslan's network alone cannot supply at scale. The matchmaker, once its specialist pool deepens through G1 and G2, becomes the sourcing mechanism for producer engagements. This creates a secondary use-case for matchmaker Phase-1: Ruslan can begin matching Producer Center clients to relevant specialists even before the commercial fee tier launches, deepening the scoreboard data while supporting §3.2 delivery.

**Depended on by §3.3 USB-C Integration Services.** Client deployments at Mittelstand companies (§3.3) generate recurring needs for specialist capabilities: the client has an AI-agent system installed, but needs a domain expert to configure their knowledge base for their industry, or a legal specialist to validate their GDPR compliance implementation. Each §3.3 deployment is a potential recurring match-task source, creating a structural feed into §3.4. At scale, every client in the §3.3 fleet is a latent task-side matchmaker participant.

**Depended on by §3.7 Educational.** The specialist graduation path (Voice 2 step 7: «специалисты начинают работать с нами переходят к нам») leads through the Educational direction: specialists who complete multiple successful matches and demonstrate D22 alignment become candidates for Jetix methodology licensing. The Educational direction (§3.7) is the formal packaging of this graduation; §3.4 is the pipeline that identifies the graduates [src:decisions/JETIX-VISION.md §8 per-archetype Для Предпринимателя — growth path «client → partner → roy-leader → methodology-replicator»].

**Cross-cutting role.** The matchmaker is the relational-glue direction: §3.1, §3.2, §3.3, and §3.5 all both consume matchmaker output and feed matchmaker input. It is the direction most dependent on the other directions existing and least able to grow in isolation. This makes it the highest-connectivity node in the §3-direction graph — which in systems terms means it is both a critical leverage point (fix it and multiple directions benefit) and a systemic fragility point (starve it of inputs and multiple directions degrade simultaneously).

## 10. Open Questions

**Q1 — Match-fee economics: task-side only vs both sides.** The current placeholder assumes fees from both sides (task-side per-match fee + specialist-side success-fee). The anti-commodity positioning argument favors task-side-only: specialists who pay before they have a track record will resist adoption, slowing specialist-pool formation exactly when pool size is the binding constraint. Conversely, both-sides fees are standard in B2B marketplace economics and signal that Jetix is not subsidizing the specialist side indefinitely. Resolution requires a Phase-2 experiment: launch Phase-2 with task-side-only fee for first 3 months, then introduce specialist success-fee and observe pool-size and NPS changes. This is preserved as Dissent D-match-1 in frontmatter. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6 + L6 §2.1 payment filter]

**Q2 — Platform MVP gate: G2 (€200K) or G3 (€1M).** L6 §6 left this open. The L5 preference expressed in the mandatory template is G3, on the grounds that Secure Network liquidity (≥100 active members) is a hard precondition. The counter-argument: delaying Platform MVP to G3 means 18–24 months without a matchmaking UX, during which a competitor could occupy the matching-UX space for the D22-filtered audience. A hybrid resolution: launch a minimal self-service task-posting interface at G2 (without full escrow or reputation scoring) to stake the UX territory, then build full Platform MVP at G3. This is preserved as Dissent D-match-2 in frontmatter. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.3 + §6.4]

**Q3 — Specialist vetting mechanism scalability.** Phase-1 vetting is entirely Ruslan-personal (knows every specialist). Phase-2 AI scoring against digital portraits handles scale, but the D22 5-criteria battery contains dimensions (Stable, Adequate) that are poorly captured by portrait data and require human judgment. Phase-3+ peer-vetting via D27 fork-community is the emergent solution — Alliance members collectively vet new specialist candidates through a structured review process. The design of this peer-vetting process is unresolved; it needs a Phase-2 spec before Platform MVP launch. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §4.6 + D27]

**Q4 — Alliance Foundation integration: match-fee discounts for Alliance members.** Per L6 §5.3 Option C, Alliance membership provides commercial benefits through Jetix-Corp. Should Alliance-member task-side clients receive reduced or zero match fees as a membership benefit? This would accelerate Alliance member adoption of the matchmaker and deepen the Alliance value proposition. The risk: revenue dilution if Alliance membership becomes primarily valuable as a matchmaker-fee discount rather than as a governance and peer-learning vehicle. Requires explicit Ruslan ack. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §5.3 Option C revenue model]

**Q5 — Cross-border regulatory surface.** Match fees collected from Mittelstand clients in DE/EU for matches with specialists in non-EU jurisdictions create: (a) independent contractor classification risk under DE Scheinselbständigkeit rules; (b) VAT/USt on the match-fee service (B2B reverse-charge vs B2C direct), especially complex when task-side is in DE and specialist is in US; (c) GDPR compliance for storing specialist portrait data and sharing it with task-side clients during the introduction step. Phase-2 requires a lawyer consult before any fee-charging activates in the EU jurisdiction. Defer to Phase-2; budget for it in the €5–15K G2 capex allocation. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md §6.6]

---

## Integration Synthesis — Claims with F / ClaimScope / R

The following claims synthesize the multi-source inputs for this direction:

**Claim 1.** The matchmaker's primary leverage point in Phase-1 is starting the scoreboard (recording outcomes), not building the agent or launching the fee tier.
- F: F4 (operational convention; grounded in Meadows L5 information-flow pattern + L6 §6.1 explicit diagnosis)
- ClaimScope: holds for Phase-1 at Alliance size ≤20; at 20+ members the leverage point shifts to Phase-2 preconditions (portrait infrastructure)
- R: Refuted if Phase-2 launches without a 30-match scoreboard and achieves equivalent AI-scoring quality; accepted if Phase-2 AI scoring outperforms Phase-1 manual matching only when pre-trained on ≥30 match records

**Claim 2.** The Phase-2+ platform should gate behind Secure Network membership (not be publicly accessible), because the D22 filter is the structural source of the matchmaker's competitive advantage and requires the Secure Network as its enforcement mechanism.
- F: F4 (operational convention; Ashby requisite-variety + L6 §6.3 platform design)
- ClaimScope: holds as long as Secure Network membership is the D22-enforcement mechanism; fails if Secure Network fails to scale to ≥100 active members before G2-end
- R: Refuted if a public-access (non-Secure-Network-gated) matchmaker achieves equal or better D22 filter compliance via alternative mechanisms (e.g., reputation scoring alone); accepted if Secure Network-gated platform shows higher match NPS than any publicly tested comparable over 2 quarters

**Dissent preserved (D-match-1 + D-match-2).** See frontmatter dissents block. Both are active tensions with no current resolution; both require Phase-2 observational data to resolve. Neither is averaged — both claims and their counterparts are retained with bounded ClaimScope and explicit R predicates per integrator protocol.
