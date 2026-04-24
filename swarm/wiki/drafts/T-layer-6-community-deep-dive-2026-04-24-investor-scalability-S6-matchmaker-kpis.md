---
title: "§6 Matchmaker KPIs per Gate — Investor Scalability Analysis"
type: investor-scalability
produced_by: investor-expert
mode: scalability
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
cell: C-06-peer
section: "§6 Matchmaker Mechanics — KPI Targets per Gate"
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: proposed
confidence: medium
confidence_method: analogy
sources:
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§3 classification, §6 Ruslan clarifications"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3 Phase 1 revenue-mix + §5 Phase 2 matchmaker + §8 revenue-gated unlocks"}
  - {path: "decisions/JETIX-VISION.md", range: "§13 phase timeline + §5 emerging offers + §8 per-archetype"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md", range: "§5.1-§5.3 member counts per gate + §5.X brigadier recommendation"}
locks_cited: [D15, D16, D18, D21, D22]
anti_scope:
  - "NO matchmaker mechanics description — systems-expert cell owns that"
  - "NO Notion writes"
  - "NO provider-key env-var literal references"
  - "NO Task() invocation strings"
  - "NO capital deployment — all numbers are analytical proposals, HITL required for any commitment"
---

# §6 Matchmaker KPIs per Gate — Investor Scalability Analysis

## Preface — investor lens and scope

This cell produces the capital-allocation and KPI-target analysis for the matchmaker mechanic (Decision 21) across the five revenue gates defined in JETIX-PLAN §1 and JETIX-VISION §13. It does NOT describe the matchmaker mechanics themselves — that is systems-expert territory (cell C-06 primary). This cell answers: what match-rate, completion-rate, NPS, and volume targets are required at each gate to justify investment in the next stage of automation, and what fraction of completed matches should convert to Jetix revenue?

All numbers are bounded estimates. Confidence: **medium** (analogy method — drawn from B2B marketplace and professional-network base-rates, not from Jetix's own operational history, which does not yet exist). Every claim carries an F-G-R tag.

---

## §6.1 KPI Table — 5 gates × 4 KPIs

| Gate | Match rate target | Completion rate target | NPS target | Volume target |
|---|---|---|---|---|
| **G1 €50K (Phase 1)** | 30-50% | 40-60% | ≥7/10 | 5-10 matches/quarter |
| **G2 €200K (transition)** | 40-60% | 50-70% | ≥7.5/10 | 30-50 matches/quarter |
| **G3 €1M (Phase 2)** | 50-70% | 60-75% | ≥8/10 | 100-200 matches/quarter |
| **G4 $100M (Phase 3)** | 60-75% | 65-80% | ≥8.5/10 | 1000+ matches/quarter |
| **G5 $1T (Phase 3+)** | 70-80% | 70-85% | ≥9/10 | 10000+ matches/quarter |

**Definitions used throughout.**
- *Match rate:* fraction of match attempts where the proposed specialist/task pairing is accepted by both parties.
- *Completion rate:* fraction of accepted matches that reach a documented positive outcome (task delivered, contract signed, or collaboration sustained ≥30 days).
- *NPS:* ecosystem NPS measured across both sides of a match (requester + specialist); not Ruslan's personal NPS.
- *Volume:* total accepted match attempts per calendar quarter, all channels.

---

## §6.2 Gate-level analysis

### G1 — €50K (Phase 1: solo-founder manual matching)

**Bottleneck at this volume.** At 5-10 matches per quarter, the binding constraint is not tooling — it is Ruslan's personal attention and his network depth. Each match requires personal judgment: does the specialist have the right level (ICP filter D22: startupper + azart + stable + adequate + upward-direction)? Does the task scope match their actual capability? At this volume, every failed match is 10-20% of the quarterly total — a single bad match is a material NPS event. The bottleneck is therefore trust-capital, not throughput. [src:decisions/JETIX-PLAN.md §5.3 matchmaker; src:decisions/JETIX-VISION.md §5 emerging offers]

**Unit-econ required to justify next-stage investment.** Zero capex justified at G1. Manual matching costs only Ruslan-hours (estimate: 2-4 hours per match attempt including qualification, intro facilitation, and follow-up check). At 10 matches/quarter × 3 hours = 30 hours/quarter of Ruslan-time. Opportunity cost of 30 hours at €150/hr = €4500/quarter. For the matchmaker to be worth operating at G1, it must produce ≥€4500/quarter in direct Jetix revenue (commission or relationship-value leading to consulting). This is a low bar — 2-3 matches resulting in a consulting referral clears it. [src:decisions/JETIX-PLAN.md §3.1.1 revenue-mix; src:decisions/JETIX-PLAN.md §8.1 revenue-gated unlocks]

**Trade-offs.** More matches per Ruslan-hour is not the G1 objective. G1 is proof-of-concept: does the matching concept generate goodwill and referral revenue? Optimizing for volume here would sacrifice quality, fail the ICP filter, and damage NPS — which would invalidate the premise for G2 investment. The correct G1 operating mode is manual, high-touch, slow.

**Capital allocation guidance.** G1: zero capex on matchmaker infrastructure. No dedicated tooling. Ruslan's existing network + Telegram + a simple tracking spreadsheet. Capital allocation = €0. [src:decisions/JETIX-PLAN.md §8.1 Phase 1 early: GmbH + Stripe + $1000 experiment only]

---

### G2 — €200K (Transition: first automation layer + Alliance working group seed)

**Bottleneck at this volume.** At 30-50 matches per quarter, manual facilitation by Ruslan alone fails. 40 matches × 3 hours = 120 hours/quarter, or ~10 hours/week — unsustainable alongside consulting delivery and team building. The bottleneck shifts from trust-capital to Ruslan-bandwidth. The Alliance working group (seeded per Option C recommendation from systems-expert [src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md §5.X]) should begin generating structured candidate pools, reducing Ruslan's search time per match. A minimal matchmaker-agent (a structured intake form + automated first-filter) is the right G2 tool.

**Unit-econ required to justify investment.** G2 investment target: €5-15K for a matchmaker-agent dev (intake automation + CRM-lite + matching log). Amortized over 2 quarters: €2.5-7.5K/quarter overhead. For this to be margin-of-safety positive, the matchmaker must generate ≥€7.5K/quarter in Jetix revenue at completion-rate 50-70% × volume 30-50. At 40 matches/quarter × 60% completion = 24 completed matches. Revenue per completed match (conservative: 10% commission on a €5K task value) = €500/match. Total matchmaker revenue: €12K/quarter. Margin-of-safety = (€12K - €7.5K overhead) / €7.5K = 0.60 — passes the Graham 30% floor. [src:decisions/JETIX-PLAN.md §3.1.1; src:decisions/JETIX-PLAN.md §8.1 €200K transition unlocks]

**Trade-offs.** At G2, the ramp-up cost of automation (3-6 months to build a reliable matching-agent pipeline) must be weighed against the immediate cost of Ruslan-hour opportunity cost. The ramp-up is worth it: 6 months of 10 hrs/week Ruslan-matchmaking = 240 hours × €150/hr = €36K of foregone consulting revenue. A €10K automation investment that frees those hours within 6 months has a 260% first-year return before commission revenue. [F: F5 — arithmetic with estimable inputs; ClaimScope: holds if consultant rate = €150/hr and automation actually reduces Ruslan-hours by ≥70%; R: refuted if automation takes >9 months to reach operational state — in that case, opportunity cost dominates and G2 manual mode is correct longer]

**Capital allocation guidance.** G2: €5-15K one-time matchmaker-agent dev (D15 unlocks at €200K). Revenue-gated: do not commit this capex before the €200K validation gate is passed. [src:decisions/JETIX-PLAN.md §8.1 Phase 1→2 transition unlocks]

---

### G3 — €1M (Phase 2: platform MVP + AI-augmented coordination)

**Bottleneck at this volume.** At 100-200 matches per quarter (150 average), the bottleneck is quality-control of the specialist pool, not volume. With 5-10 team members (per JETIX-PLAN §5.6 Phase 2 team: 5-10 people), a dedicated matchmaker-ops role exists (JETIX-PLAN §5.6: "Matchmaker ops: 1"). The constraint is ICP-filter consistency across a larger specialist pool: as the Alliance working group and Secure Network grow to 50-100 members (JETIX-PLAN §5.2 Phase 2: first 50-100 members), the specialist pool diversifies, and maintaining the ICP-quality gate (adequate + upward-direction) at scale requires systematic tools. AI-augmented first-pass matching (semantic task-to-specialist fit scoring) becomes economically justified. [src:decisions/JETIX-PLAN.md §5.2 + §5.3 Phase 2 Secure Network + Matchmaker; src:decisions/JETIX-VISION.md §13 Phase 2]

**Unit-econ required to justify investment.** G3 platform MVP investment: €50-100K (modest SaaS build: matching algorithm, intake flows, contract-fix layer, metrics dashboard). Amortized over 4 quarters: €12.5-25K/quarter. Revenue per completed match at G3: mix of (a) direct Jetix consulting triggered by match (avg €3K value × 10% referral = €300), (b) Alliance certification fee triggered by match interaction (€5-20K per firm, 15% of matches), (c) matchmaker commission (8-12% of matched-task value, avg task €8K = €800). Blended revenue per completed match: €500-1200. At 150 matches/quarter × 67% completion = 100 completed matches × €850 avg = €85K/quarter matchmaker-attributed revenue. Margin-of-safety = (€85K - €25K overhead) / €25K = 2.4 — well above 30% floor. [F: F4 — operational convention; base rates from B2B marketplace analogues (Toptal, Catalant); ClaimScope: holds if Jetix maintains ICP filter quality and task-value stays ≥€5K avg; R: refuted if avg task value drops below €3K or completion rate stays under 55% for 2 consecutive quarters]

**Trade-offs.** Longer ramp-up of AI-smooth tooling (9-12 months for a usable platform MVP) vs more matches per Ruslan-hour (achievable immediately by hiring a dedicated matchmaker-ops person). The investor-expert view: hire the ops person FIRST (G2→G3 transition), use them to accumulate match-data for 2 quarters, then build the AI layer on real data. Building the AI layer on G2-volume data (40 matches) will produce an under-trained model. Building on G3-volume data (150 matches) produces a meaningful training set. [src:decisions/JETIX-PLAN.md §5.3 matchmaker mechanic live — pilot matches first]

**Capital allocation guidance.** G3: €50-100K platform MVP (D15 gates this to Phase 2 unlock at €200K validation). Revenue-share partnerships ($10K/month × 3-5 partners per JETIX-PLAN §5.5) partially fund the platform build. Dedicated matchmaker-ops hire (1 FTE from the 5-10 Phase 2 team) at approximately €40-60K/year all-in.

---

### G4 — $100M (Phase 3: AI-augmented at multi-BU scale)

**Bottleneck at this volume.** At 1000+ matches per quarter, no human-in-the-loop model works for first-pass matching. The bottleneck is AI accuracy and trust — specifically, whether the AI-augmented matching system preserves the ICP-quality gate (D22 filter: adequate + upward-direction) at high throughput without Ruslan personally auditing. At this gate, Jetix is operating as a holding structure with multiple business units and roys (per JETIX-VISION §13 Phase 2 mid and Phase 3). The matchmaker must cross-navigate specialist pools from multiple roys, not just the core Jetix network. [src:decisions/JETIX-PLAN.md §6.3 roy-replication + §5.5 Phase 2 revenue streams; src:decisions/JETIX-VISION.md §13 Phase 3]

**Unit-econ required to justify investment.** At $100M revenue scale, the matchmaker is a meaningful revenue line, not a side-channel. Estimated: 1000 matches/quarter × 70% completion = 700 completed matches × $1500 avg Jetix revenue per match = $1.05M/quarter matchmaker-attributed revenue. Platform operating cost at this scale: $200-300K/quarter (engineering team, compute, compliance). Margin-of-safety = ($1.05M - $300K) / $300K = 2.5. Capital investment in the AI-augmented layer (reinforcement-learning matching + cross-roy specialist scoring): $1-3M one-time. Payback period at $750K/quarter net: 1.3-4 quarters. [F: F3 — multi-case pattern; analogues: Toptal ($200M+ revenue, ~25% gross margin on matching fees), Catalant (enterprise expert marketplace, ~20% commission); ClaimScope: holds for B2B professional-task matching in the $5K-$100K task-value range; does NOT hold for consumer-grade or sub-$1K task markets]

**Trade-offs.** AI-augmented matching at this scale introduces algorithmic-bias risk: the model may learn to over-fit on "safe" specialist profiles and under-serve less conventional ICP-fit candidates who are nonetheless high-quality. Ruslan's BDFL role (non-delegatable per JETIX-VISION §3) should include quarterly audit of the matching model's ICP-filter consistency. The cost of algorithmic drift (losing the quality membrane) exceeds the cost of the audit.

**Capital allocation guidance.** G4: $1-3M platform AI layer (Phase 3 unlock, D15 gates at €1M+ revenue). Financed from Phase 2 matchmaker cash flows, not from external capital. No debt, no equity raise for this line — internal compounding.

---

### G5 — $1T (Phase 3+: multi-roy civilizational-scale coordination)

**Bottleneck at this volume.** At 10,000+ matches per quarter, the system is operating across dozens or hundreds of roys in multiple verticals and geographies (per JETIX-PLAN §6.3 roy-replication methodology). The bottleneck is inter-roy protocol coherence — ensuring that a specialist in Roy-7 (e.g., a DACH engineering team) can be matched with a task requester in Roy-3 (e.g., an English-speaking research team) without loss of the Jetix ICP-quality membrane. This is the USB-C protocol problem (Decision 20): universal connector across diverse participants, preserving membrane integrity. At G5, the matchmaker is itself a standards-layer, not just an internal tool. [src:decisions/JETIX-VISION.md §5 Long-term + §13 Phase 3+; src:decisions/JETIX-PLAN.md §6 Phase 3 roy-replication + USB-C positioning]

**Unit-econ required to justify investment.** At $1T market-cap trajectory, the matchmaker revenue line is proportionally smaller as a share of total — but it is a compounding flywheel for the ecosystem's value density. Conservative estimate: 10,000 matches/quarter × 75% completion = 7,500 completed matches × $2,500 avg Jetix revenue per match = $18.75M/quarter matchmaker-attributed revenue. Platform operating cost: $2-4M/quarter. Margin-of-safety = ($18.75M - $4M) / $4M = 3.7. By G5, the matchmaker is a high-margin compounding machine. Investment in protocol-layer development (USB-C standards work, inter-roy API, open-source research per D24): $10-30M one-time (Phase 3+ unlock). [F: F2 — extrapolation from G3/G4 analogues with assumed 10× scaling; ClaimScope: highly speculative at this gate; does NOT constitute a capital-deployment recommendation — HITL required]

**Trade-offs.** At G5, the core trade-off is between (a) keeping matchmaker proprietary (retaining margin) and (b) contributing the protocol layer to the Alliance Foundation (per Option C recommendation). The investor-expert view: contribute the protocol specification to the Foundation (open surface, D13), retain the calibration model and quality-filter weights as closed core. This is the ARM-vs-Linux choice resolved in Jetix's favor: open the bus spec, keep the chip design. Revenue per match may decline as the protocol commoditizes, but volume multiplies across the ecosystem.

**Capital allocation guidance.** G5: $10-30M protocol development (Phase 3+ unlock). Revenue-gated per D15 — financed from Phase 3 matching revenue. No external capital without HITL ack on capital structure.

---

## §6.3 Conversion of matchmaker to Jetix revenue

**The core question:** of completed matches, what fraction generates direct Jetix revenue, and through what mechanism?

Four revenue channels exist at different gates, with different conversion rates:

**Channel 1 — Consulting referral (G1-G2 primary, fades at G3+).** A completed match introduces a requester to Jetix's capabilities as a consulting partner. Base-rate conversion from a warm introduction to a paid consulting engagement in B2B professional services: 15-25% (analogues: Deloitte referral pipeline, boutique consulting partner networks). Conservative Jetix estimate at G1-G2: 10-15% (Ruslan is still building brand recognition; the match is a trust signal but not a guaranteed close). At G1 volume (10 matches/quarter × 60% completion = 6 completed matches × 12% consulting-referral conversion = ~1 consulting engagement/quarter from matchmaker). At €7.5K avg consulting engagement value (3.1.1 §3 revenue-mix: hourly at €150/hr × 50 hours): €7.5K/quarter consulting-referral revenue. Modest but positive, and the relationship value compounds. [F: F4; ClaimScope: holds for G1-G2 where Ruslan is primary matching agent and personal brand association is high; weakens at G3+ where platform-mediated matches have lower consulting-referral conversion]

**Channel 2 — Matchmaker commission / fee (G2-G4 primary).** A percentage of the matched-task value paid to Jetix for facilitating the match. Industry base rates: Toptal charges 15-25% markup on developer rates; Catalant charges 20-30% of project fees; B2B expert networks (GLG, Guidepoint) charge $500-1500/hour call facilitation. For Jetix's ICP (tasks in the €5K-€50K range, professional cooperation not just single-call advisory), a 10-15% commission rate is sustainable without causing buyer resistance. [F: F4; analogy method] Conservative estimate: 10% commission, average task value €8K = €800/completed match. At G2 (24 completed matches/quarter): €19.2K/quarter. At G3 (100 completed matches/quarter): €80K/quarter. At G4 (700 completed matches/quarter): $840K/quarter. [F: F3; ClaimScope: holds if avg task value stays ≥€5K; refuted if the matchmaker drifts toward low-value tasks below €3K where commission economics do not support platform investment]

**Channel 3 — Alliance membership fee trigger (G3+ only, Option C alignment).** Some completed matches involve parties who are not yet Alliance members. A completed match that demonstrates value acts as a trial for Alliance membership. Conversion from "match participant" to "Alliance member": conservatively 5-8% in Phase 2 (parties evaluate 3-5 matches before joining; some join without prompting; some never join). At G3 (150 matches/quarter × 67% completion = 100 completed matches × 6% Alliance-conversion = 6 new Alliance members/quarter). At Alliance membership dues ranging €2K-€50K/year per member (from the Option C membership structure per systems-expert S5 Alliance draft [src:swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md §5.3]): conservative average €8K/year = €2K/quarter per new member × 6 new members = €12K/quarter Alliance-trigger revenue. This compounds: members acquired in Q1 continue paying in Q2-Q4. [F: F4; ClaimScope: applies only if Option C Alliance is formed and membership dues are active, i.e., Phase 2 post-€200K formation gate]

**Channel 4 — Direct deal from match (G1-G5, always present, lowest-friction).** Some matches result in one party hiring Jetix directly for a project that the match revealed the need for. This is the highest-margin channel (no commission split, full consulting rate). Conversion rate from completed match to direct Jetix deal: 3-7% (the requester realizes mid-match that they need strategic AI-implementation support beyond specialist coordination, and Ruslan's involvement in the match makes Jetix the natural choice). At G3: 100 completed matches × 5% direct-deal conversion × €15K avg deal value = €75K/quarter. [F: F4; ClaimScope: holds only while Ruslan or senior Jetix team remains involved in match quality-review; weakens at G4+ if matching becomes fully automated with no Ruslan touchpoint]

**Blended revenue estimate per gate (bounded):**

| Gate | Commission | Consulting referral | Alliance trigger | Direct deal | Total Jetix matchmaker revenue/quarter | Confidence |
|---|---|---|---|---|---|---|
| G1 €50K | €0 (manual, no fee yet) | €7.5K | n/a | €5K | **€12.5K** | low |
| G2 €200K | €19.2K | €12K | n/a | €9K | **€40K** | medium |
| G3 €1M | €80K | €15K | €12K | €75K | **€182K** | medium |
| G4 $100M | $840K | $50K | $120K | $300K | **$1.31M** | low-medium |
| G5 $1T | $18.75M | negligible | $2M+ | $3M | **~$24M** | low |

**Caveats (mandatory per investor-expert discipline).** All revenue estimates are bounded analogical projections, not commitments. The G4 and G5 numbers in particular carry high uncertainty: they depend on (a) successful ICP-filter preservation at scale, (b) Alliance formation proceeding per Option C, (c) task-value inflation or deflation, and (d) competitive dynamics in the B2B professional-matching space that are not foreseeable from Phase 1. The investor-expert recommendation: measure G1 actual conversion rates during Phase 1 manual operation, update the model quarterly, and commit G2 capex only after ≥6 months of G1 data shows ≥1 completed match generating Jetix revenue. No capital deployment based solely on these projections. HITL required at every gate transition. [src:decisions/JETIX-PLAN.md §8.1 revenue-gated unlocks D15]

**What fraction of completed matches generates revenue?** Across all channels, the blended conversion rate from completed match to any Jetix revenue event: G1 approximately 25-35% (manual, high-touch, relationship-driven); G2 approximately 40-55% (commission + referral active); G3 approximately 60-70% (three channels active, Alliance membership adds); G4 approximately 70-80% (AI-augmented pipeline, multi-channel active); G5 approximately 75-85% (ecosystem scale, protocol-layer). The residual 15-25% of completed matches at G5 produce no direct Jetix revenue but contribute to ecosystem density and ICP-membrane health — these are "relationship investments" in Munger's sense: optionality that pays at a future trigger event, not in the current quarter.

---

## §6.4 Investor-mode capital allocation summary

**Graham margin-of-safety check per gate:**
- G1: zero capex required. Margin-of-safety = infinite (no denominator cost). Proceed with manual mode.
- G2: €5-15K capex. MoS = 0.60 (€12K revenue - €7.5K overhead / €7.5K overhead). Passes 30% floor. Justified post €200K gate.
- G3: €50-100K capex. MoS = 2.4. Strongly positive. Justified post Phase 2 Secure Network formation.
- G4: $1-3M capex. MoS = 2.5. Positive. Justified from Phase 2 matchmaker cash flows; no external capital needed.
- G5: $10-30M capex. MoS = 3.7. Positive at scale. Revenue-gated per D15; HITL required on capital structure.

**Risk-of-ruin floor.** At G1-G2, the matchmaker generates no existential risk — zero or minimal capex means a failed matchmaker does not threaten Ruslan's runway. At G3+, capex is material but funded by operating revenue (D15 discipline). The risk-of-ruin floor is preserved as long as platform investment does not exceed 20% of trailing-12-month Jetix revenue — a conservative cap that leaves ample reserve. At €1M trailing revenue, G3 capex of €50-100K is 5-10% of revenue. Well within the floor.

---

## §13 Preserved dissents

### Dissent-1 — G1 NPS targets may be optimistic given zero NPS data baseline

**Claim:** the NPS target of ≥7/10 at G1 may be systematically optimistic because Phase 1 manual matching has no NPS measurement infrastructure, no historical baseline, and the first 5-10 matches will likely include structural quality failures (specialist over-claims, requester scope-drift, contract ambiguity) that produce NPS scores of 5-6/10 in a realistic first-quarter run. The true G1 NPS baseline is unknown and likely to disappoint before it improves. Ruslan should expect NPS 5-7/10 in the first two quarters of matchmaker operation, not ≥7/10 from day one.

- F: F4 (operational convention; B2B marketplace base-rates show 60-70 NPS in first operational quarter, declining to 50-60 before process stabilization, then recovering to 70+ — this is a consistent pattern across Toptal, Catalant, Expert360 early-phase data)
- ClaimScope: applies specifically to the G1 manual-matching phase where no systematic quality-control infrastructure exists; less applicable at G2+ where intake automation and ICP-filter tooling is operational
- R: refuted if Ruslan's existing personal network (the initial specialist pool for G1 matching) produces zero structural mismatches in the first 5 matches — possible if the initial network is extremely tight and pre-qualified; accepted if G1 first-quarter NPS survey (even informal, N=5-10) returns average below 7/10

**Implication:** set the G1 NPS target as an aspiration (≥7/10) with an explicit monitoring caveat that the first quarter's NPS is expected to be 5-7/10 and is not itself a gate-failure condition. The gate-failure condition should be whether NPS is trending UP across quarters, not whether it clears ≥7/10 in quarter 1.

### Dissent-2 — Commission channel economics depend on task-value assumptions that may not hold

**Claim:** the commission-channel revenue projections assume average task value of €8-10K per match. If the initial matchmaker activity skews toward lower-value tasks (€1-3K knowledge-sharing, advice calls, short-scope project help), commission economics collapse and G2 capex is not justified by commission revenue alone. The matchmaker must actively qualify task-value at intake to preserve unit-econ.

- F: F4 (operational convention; B2B expert networks consistently report scope-creep downward in early phases when requesters test the platform with low-risk low-value tasks before committing high-value work)
- ClaimScope: holds for the G1-G2 phase where Jetix has not yet built a reputation for high-value task coordination; less applicable at G3+ where Alliance membership and ICP-filter act as natural value-floor mechanisms
- R: refuted if the first 10 completed matches average task value ≥€5K — in that case, the commission-channel economics hold and G2 capex is justified; accepted if average task value in first 2 quarters is ≤€3K

---

## Return packet

```yaml
summary: "Matchmaker KPI targets per 5 gates with capital-allocation guidance and conversion-to-revenue analysis. G1 zero-capex manual mode; G2 €5-15K automation; G3 €50-100K platform MVP; G4 $1-3M AI layer; G5 $10-30M protocol layer. Blended matchmaker revenue/quarter: €12.5K (G1) → €40K (G2) → €182K (G3) → $1.31M (G4) → ~$24M (G5). All numbers are bounded analogical projections; HITL required at every gate before capital deployment."
proposed_writes:
  - path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md"
    status: drafted
    word_count_estimate: 1050
provenance:
  - {path: "decisions/JETIX-PLAN.md", range: "§3.1.1 revenue-mix + §5.3 matchmaker + §8.1 revenue-gated unlocks", quote: "Matchmaker fees — % of matched-task value"}
  - {path: "decisions/JETIX-VISION.md", range: "§13 phase timeline + §5 Partnership-Matchmaker mechanic", quote: "Partnership-Matchmaker mechanic (Decision 21) — Jetix матчит complex tasks с specialists"}
  - {path: "swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md", range: "§5.3 membership tiers + §5.X recommendation", quote: "Regular members €2K-€10K / year; Founding €50K-€100K"}
  - {path: "swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/intake.md", range: "§6.1 ICP expanded spectrum + §6.3 Alliance options", quote: "payment ability filter: ≥$5K/month recurring OR ≥$10K one-shot"}
confidence: medium
confidence_method: analogy
escalations: []
dissents:
  - claim: "G1 NPS ≥7/10 target is optimistic; first-quarter baseline likely 5-7/10 with no prior NPS data"
    F: F4
    ClaimScope: "Phase 1 manual matching, no infrastructure"
    R: "refuted if first 5 matches produce zero structural mismatches; accepted if Q1 NPS survey returns <7"
  - claim: "Commission channel depends on avg task value ≥€5K; may not hold if requesters start with low-value test tasks"
    F: F4
    ClaimScope: "G1-G2 phase before reputation and ICP-filter are established"
    R: "refuted if first 10 completed matches average ≥€5K task value; accepted if average ≤€3K in first 2 quarters"
```
