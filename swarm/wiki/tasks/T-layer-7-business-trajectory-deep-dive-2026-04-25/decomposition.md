---
id: T-layer-7-business-trajectory-deep-dive-2026-04-25-decomposition
title: "LAYER-7 Business Deep-Dive — Phase-2 WBS (14 cells × 3 waves)"
type: phase-2-decomposition
cycle_id: cyc-layer-7-business-trajectory-deep-dive-2026-04-25
task_id: T-layer-7-business-trajectory-deep-dive-2026-04-25
created: 2026-04-25
class: M-structural
total_cells: 14
parallel_waves: 3
mode_distribution: integrator (5) / critic (4) / scalability (3) / brigadier-synth (2)
---

# Phase-2 WBS — LAYER-7 Business & Trajectory Deep-Dive

## §1 Decomposition rationale

14 sections from launch prompt §3 → 14 cells. 3 waves to honour dependency ordering:

- **Wave A (parallel × 5 cells):** sections that do not depend on any other L7 cell.
  Pricing finalization (§2) and unit-econ (§3) are co-equal; revenue streams (§6)
  builds on §2; evolution per gate master (§13) requires L5 §13 + L6 §11 references
  but no L7 dependencies; 5-gate triggers (§4) reads SYSTEM-OVERVIEW §5 trajectory.
  All five cells can run in parallel from Wave-A inputs (L5 + L6 acked).

- **Wave B (parallel × 5 cells):** sections that depend on Wave-A outputs.
  Cash flow (§7) consumes §3 unit-econ; investor relations (§9) consumes §3 + §6;
  compensation model (§10) consumes §6 + §13; tools per phase (§12) consumes §13;
  patents (§8) consumes §13 + IP layer; миллионер reconciliation (§5) is independent
  of cell numbers but requires §2 pricing tiers + §3 income-floor arithmetic.

- **Wave C (parallel × 3 cells):** consolidating sections that synthesize Wave-A + Wave-B.
  Risk register (§11) consolidates risk surface from §2-§10 + §13. Open questions (§14)
  consolidates dissents + F-G-R tagging from all sections. TL;DR (§1) is brigadier-
  synth after all 13 substantive sections drafted.

**Integration pass (after all waves):** brigadier synthesizes 14 drafts → master canonical
document with cross-section reconciliation. Critical: pricing in §2 must match unit-econ
in §3 must match cash flow in §7 must match risk register §11.

## §2 Cells (14 total)

### Wave A (5 cells, parallel)

#### Cell C-01 — §2 Pricing Finalization (9 directions × tiers)

- **Owner:** investor-expert × integrator (primary) + critic-mode validation
- **Output:** `swarm/wiki/drafts/T-layer-7-business-trajectory-deep-dive-2026-04-25-investor-integrator-§2-pricing.md`
- **Word floor:** 3000-4500 words
- **Acceptance predicate:**
  - 9 directions × per direction: floor / standard / premium tiers all in concrete €/$
  - Path A/B/C tiers concrete for §3.3 USB-C (per L5 ack: B default, C enterprise>€30K, A Phase-2 SMB)
  - Phase-1 vs Phase-2+ pricing differentiated where applicable
  - Discount policy (first 2-3 case-study clients per L6 §7)
  - Currency: EUR primary; USD optional Phase-2+
  - L5 placeholder ranges resolved with rationale
  - L6 payment-ability filter ($5K/mo OR $10K one-shot) cited as constraint
  - Conflicts between aspirational pricing and €50K Phase-1 reach flagged as preserved
    dissent
  - F-G-R tagging on every pricing claim
- **Inputs:** L5 §3.1-§3.9 placeholders + L6 §2.1 payment filter + audio_452 (€150/hr) +
  audio_470 ($20-50K/mo)

#### Cell C-02 — §3 Unit-Econ per Direction

- **Owner:** investor-expert × scalability (primary) + critic validation
- **Output:** `swarm/wiki/drafts/...-investor-scalability-§3-unit-econ.md`
- **Word floor:** 2500-3500 words
- **Acceptance predicate:**
  - Per direction: revenue/engagement (avg) + COGS direct + allocated overhead +
    contribution margin €/$ + GM% + CAC + payback period + LTV + LTV:CAC ratio
  - Ruslan-hours per €1K revenue quantified per direction (productization scoring metric)
  - GM% target ≥70% per D18 productization (≥75% capital-light ideal); flag any
    direction below floor
  - LTV:CAC ≥3:1 healthy; flag any direction below
  - Compute cost (Anthropic Max + Groq voice-only) treated as fixed overhead per direction
  - 9 directions covered (Smart AI = narrative label, no unit-econ — note in section)
  - F-G-R per claim
- **Inputs:** L5 §3.1-§3.9 + §2 pricing (Wave-A sibling, will use placeholder mid-cell
  then reconcile at integration)

#### Cell C-03 — §4 5-Gate Migration Triggers Detailed

- **Owner:** systems-expert × scalability (primary)
- **Output:** `swarm/wiki/drafts/...-systems-scalability-§4-gate-triggers.md`
- **Word floor:** 2500-3500 words
- **Acceptance predicate:**
  - 5 gate transitions (G0→G1, G1→G2, G2→G3, G3→G4, G4→G5) detailed per gate:
    trigger condition (revenue + secondary signals) / what unlocks (per direction +
    per layer L1-L9 cite SYSTEM-OVERVIEW §5) / what sunsets / capital allocation shift /
    team changes (D26 trajectory) / risk threshold (rejection criteria) / estimated
    calendar timing (months from start, explicit ranges)
  - Master table: 5 gates × 14 layers (L0-L9 + L-R / L-C / L-B / L-P) state at each gate
    (cite SYSTEM-OVERVIEW §5)
  - Reconciles with L6 §11 evolution + L5 §13 evolution table — no contradictions
  - F-G-R per claim
- **Inputs:** SYSTEM-OVERVIEW §5 + L5 §13.2 + L6 §11.1 + JETIX-PLAN Phase 0/1/2/3

#### Cell C-04 — §6 Revenue Streams Ranking + Portfolio Diversification

- **Owner:** mgmt-expert × integrator (primary)
- **Output:** `swarm/wiki/drafts/...-mgmt-integrator-§6-revenue-streams.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - Phase-1 ranking: primary streams (≥40% revenue each: consulting + producer);
    secondary (5-20% each); risk concentration thresholds (no single client >30% per L6)
  - Phase-2 ranking: subscription (Secure Network складчина) + Path A/B/C contracts +
    educational cohort + matchmaker AI-smoothed fees
  - Phase-3+ ranking: methodology licensing royalties + Token economy (D23 if launched) +
    holding investment returns + M&A advisory (Phase-2+ optionality, brief mention)
  - Diversification logic: portfolio Sharpe-equivalent thinking — correlation analysis
    (which streams correlate with macro vs anti-correlate)
  - F-G-R per claim
- **Inputs:** L5 §2 portfolio + L5 §13 evolution + JETIX-PLAN §3-§6

#### Cell C-05 — §13 Evolution per Gate Master Table

- **Owner:** mgmt-expert × scalability (primary)
- **Output:** `swarm/wiki/drafts/...-mgmt-scalability-§13-evolution.md`
- **Word floor:** 1000-1500 words
- **Acceptance predicate:**
  - Master table format: 5 gates × [revenue / team size / direction priority / cash burn /
    cash reserve / KPIs / sub-systems active]
  - Cite SYSTEM-OVERVIEW §5 trajectory table
  - Reconcile L7 financial detail to layered evolution (L5 §13 + L6 §11)
  - Per-gate narrative paragraph (~200w each, 5 gates = 1000w narrative):
    capital allocation decision rules at each gate / team trajectory / direction
    portfolio rebalancing
  - M&A direction Phase-2+ optionality mention (per Ruslan 25.04 directive)
  - F-G-R per claim
- **Inputs:** SYSTEM-OVERVIEW §5 + L5 §13.2 + L6 §11.1 + L7 §4 (Wave-A sibling)

### Wave B (5 cells, parallel)

#### Cell C-06 — §5 Миллионер Reconciliation

- **Owner:** philosophy-expert × critic (primary)
- **Output:** `swarm/wiki/drafts/...-philosophy-critic-§5-millionaire.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - Resolves audio_529 ($1M+) vs audio_470 ($240-600K) vs audio_452 (€150/hr operational)
  - Floor ICP income-wise for Phase-1 P1A (active outreach) defined
  - Ceiling for P1B opportunistic (referral-only) defined
  - Miljonaire-tier (>$1M/year) classified: real Phase-1 segment OR Phase-2+ aspirational
  - Reconciles with L5 §3 pricing tiers (which clients afford which tier)
  - Mittelstand €5M revenue company budget feasibility quantified
  - Output: explicit income-floor table per archetype × phase × pricing-tier compatibility
  - F-G-R per claim
- **Inputs:** L7 §2 pricing (Wave-A) + L6 §2.1 payment filter + audio_452/470/529

#### Cell C-07 — §7 Cash Flow Phase-1 Model

- **Owner:** investor-expert × integrator (primary) + critic validation
- **Output:** `swarm/wiki/drafts/...-investor-integrator-§7-cashflow.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - Concrete monthly model Q1-Q2 2026 → €50K target (6-month table)
  - Per month: revenue (consulting / producer / matchmaker breakdown) + cumulative +
    burn (Ruslan draw / tools / legal) + net cash + cash position
  - Starting cash: ~$5K founder context
  - Burn assumptions: minimal personal draw + €200-400/mo Claude/tools + €1-2K legal
    upfront (GmbH + contracts)
  - Revenue ramp realistic: M1-2 €0-€2K (outreach build), M3-4 €5-12K (first signed),
    M5-6 €15-25K (acceleration)
  - Stress test: first paying client slips M4 instead M3 → cash runway sufficient?
  - Trigger to pause/re-strategize: <€2K runway = halt-and-strategize
  - Compute ledger model per P7.2: Anthropic Max-sub + Groq voice-only + zero paid APIs
    = ~€200-400/mo Phase-1
  - F-G-R per claim
- **Inputs:** L7 §3 unit-econ (Wave-A) + JETIX-PLAN §3.8 budget + audio_500 финансовая
  инфра + audio_452

#### Cell C-08 — §9 Investor Relations Roadmap

- **Owner:** investor-expert × integrator (primary)
- **Output:** `swarm/wiki/drafts/...-investor-integrator-§9-investor-relations.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - Phase-1 (€0-€200K): NO investor outreach. Self-funded only. Period.
  - Phase-2 transition (€200K validation): first investor conversations possible —
    strategic angels, family offices in DACH, sovereign EU funds. NOT mass-market VCs.
  - Investor profile: D11 + D19 $1T trajectory believer + D22 ICP-aligned values
  - Phase-2 €200K-€1M: optional strategic round €1-3M EUR for roy-replication seed +
    Mittelstand AI Alliance formalization + EU patent portfolio + first 2-3 hires
  - Phase-3+ (€1M+): larger rounds optional; depends on token economy decision (D23
    Option B can substitute equity round)
  - Concrete: target investors (NRW.BANK / KfW / Bayern Innovativ / EU family offices /
    ex-McKinsey / ex-Roland Berger / ex-Mittelstand CEOs)
  - Materials Phase-2 ready: pitch deck / data room / financial model — stub-ready,
    deployed only when activated
  - Valuation framework: investment-fund logic (management fee + carry equivalent +
    roy-replication multiplier); Phase-2 €5-15M plausible; Phase-3 €50-150M
  - F-G-R per claim
- **Inputs:** L7 §3 unit-econ + L7 §6 revenue streams + JETIX-PLAN §3.8 + D11 + D19

#### Cell C-09 — §10 Compensation Model

- **Owner:** mgmt-expert × integrator (primary)
- **Output:** `swarm/wiki/drafts/...-mgmt-integrator-§10-compensation.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - Phase-1 (solo + Cloud Cowork): no formal salary / no cap-table; Ruslan personal draw
    = consulting+producer revenue after tooling+legal essentials; Cloud Cowork = AI agent
    no human cost
  - Phase-2 first hires (2-3 people, €200K-€1M): salary base €60-90K/year DACH market
    rate per role (sales / ops / engineering); equity 0.5-2% per hire 4-year vest
    1-year cliff (founder retains ≥85%); bonus discretionary 10-20%; token allocation
    optional (D23 Phase-2 internal utility)
  - Phase-3 team 5-10: standard tech-startup comp; senior hires (heads-of-X) 1-3% equity
  - Phase-3+ team 20-100: holding structure + roy participation rights; roy-leader
    compensation = equity stake in roy + Jetix-Corp parent + token allocation (significant)
  - Founder economics: Phase-1 minimal draw / Phase-2 sustainable salary + equity
    preservation / Phase-3+ dividend rights + token allocation primary income
  - Skin-in-game preservation per D11/D22: comp structure ensures upward-direction
    startupper-mindset (D22 5-criteria), not corporate hires
  - F-G-R per claim
- **Inputs:** D26 + D11 + D22 + L6 §2.3 team ICP

#### Cell C-10 — §12 Tools per Phase Financial Tracking

- **Owner:** systems-expert × integrator (primary)
- **Output:** `swarm/wiki/drafts/...-systems-integrator-§12-tools.md`
- **Word floor:** 800-1200 words
- **Acceptance predicate:**
  - Phase-1: manual bank statement → CSV → Notion/spreadsheet (Ruslan personal review);
    Stripe dashboard (post-GmbH); compute-ledger.yaml per P7.2 (Anthropic Max-sub
    turn-count tracking + Groq scoped voice-only); cash runway alert (manual: <€2K
    halt-and-strategize)
  - Phase-2: proper accounting software (Lexware / DATEV / Sage — DACH standard);
    per-direction P&L (consulting / producer / Path A/B/C / matchmaker); investor
    reporting templates; compute-ledger expanded multi-provider
  - Phase-3+: holding-level consolidation (parent + roys); Kelly portfolio optimization
    across roy investments; token economy ledger (if D23 Phase-2+ launched);
    multi-jurisdiction tax + transfer pricing
  - Cross-references L5 §14 (no duplication: L5 = product/service tooling; L7 §12 =
    financial tracking specifically)
  - Spec + roadmap only — NOT implementation
  - F-G-R per claim
- **Inputs:** L5 §14.1-§14.3 (no duplication) + JETIX-ARCHITECTURE-BRIEF §3.1.5 +
  §3.1.12

#### Cell C-11 — §8 Patents Strategy + IP Licensing

- **Owner:** engineering-expert × integrator (primary)
- **Output:** `swarm/wiki/drafts/...-engineering-integrator-§8-patents.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - Phase-1 (€0-€50K): D14 revenue-instrumental — NO patent filing budget; defensive
    measures only (atomic git commits with provenance per D25, copyright on methodology
    docs)
  - Phase-1→2 transition (€50K-€200K): patent landscape research budget €500-€1500
    (lawyer consultation only); identify 3-5 patentable Jetix Innovations from D6
    inventory
  - Phase-2 (€200K+): patent application EU primary — €2000-€3500 per OT4; Trademark
    Jetix vs Disney clarification (parked P5 per TENSIONS-RESOLVED)
  - Phase-3+: patent portfolio + licensing program per D27 fork-and-merge (Foundation
    publishes methodology Apache 2.0 + LGPL software; Jetix-Corp proprietary tools
    licensed €500-€5K/year per practitioner per L5 §3.7; co-consultant network
    revenue-share)
  - IP audit: enumerate Jetix's defensible IP (FPF-grounded methodology + 9 Jetix
    Innovations from ADR-Chunk-8 Area 2); per-item protection mechanism
  - F-G-R per claim
- **Inputs:** D13 + D14 + D24 + D25 + D27 + L5 §3.7 educational

### Wave C (3 cells, after Wave-A + Wave-B inputs available)

#### Cell C-12 — §11 Risk Register + Mitigation

- **Owner:** philosophy-expert × critic (primary)
- **Output:** `swarm/wiki/drafts/...-philosophy-critic-§11-risk-register.md`
- **Word floor:** 1500-2000 words
- **Acceptance predicate:**
  - 15 risks per layer-impact analysis
  - Per risk: ID / description / probability / impact / mitigation / kill criteria /
    owner / phase
  - Mandatory inclusions (15 named in launch §3 §11):
    1. Phase-1 €50K miss (medium/high)
    2. Path A/B/C wrong default (low-medium/medium)
    3. Co-founder dependency M&A Phase-2+ (medium/medium for optionality)
    4. Compute cost spike Anthropic (low-medium/medium)
    5. Mittelstand AI-adoption window closes 2027-28 (medium/medium for M&A direction)
    6. GDPR / EU AI Act compliance gap (medium/high)
    7. Single-client concentration >50% (medium/high)
    8. Founder burnout (medium/catastrophic)
    9. Tooling lock-in Anthropic (low-medium/medium)
    10. Token D23 legal prohibitive MiCA/Howey (medium/low — D23 retirement clause)
    11. Talent acquisition Phase-2 D22 fail (medium/medium)
    12. Mittelstand AI Alliance Foundation legal complexity (medium/medium)
    13. Smart AI brand confusion A/B G2 (medium/low)
    14. Reputational risk early case study failure (medium/high)
    15. Macro recession DACH 2026-27 (medium-high/medium)
  - Risk dashboard concept per OME L7 inspired — monthly review, threshold alerts
  - Top-3 risks bolded for §1 TL;DR
  - F-G-R per claim
- **Inputs:** §2-§10 + §13 (all prior cells)

#### Cell C-13 — §14 Open Questions + Preserved Dissents + F-G-R Tagging

- **Owner:** philosophy-expert × critic (primary)
- **Output:** `swarm/wiki/drafts/...-philosophy-critic-§14-open-questions.md`
- **Word floor:** 500-1000 words
- **Acceptance predicate:**
  - Tier-1 BLOCKING (must resolve before Phase 3 docs writable):
    - Phase-1 income-floor resolution per archetype (миллионеры P1 active or P1B
      referral-only?)
    - Patent priority list (which 3-5 of 9 Jetix Innovations file Phase-2 first?)
    - Investor profile narrowing (sovereign funds vs family offices vs strategic
      angels — Phase-2 priority)
    - D23 token compensation Phase-2 internal utility (launch concrete proposal or
      wait Phase-3+?)
  - Tier-2 PHASE-2+ BACKLOG (defer to Phase-2 planning cycle):
    - M&A direction activation timing (Phase-2+ deferred per Ruslan 25.04)
    - M&A co-founder profile + compensation finalization
    - Path A/B/C empirical validation timeline
    - Educational platform choice (Teachable vs custom — Phase-2 first sale trigger)
  - Per question: F-level + ClaimScope + R (refutation receipt)
  - Brigadier recommendation per Tier-1 question
  - Sequencing — what blocks what (mirrors L5 §15.7 and L6 §12)
  - Coherence check across all sections (no Lock violations)
- **Inputs:** All prior cells + L5 §15 + L6 §12

#### Cell C-14 — §1 TL;DR

- **Owner:** brigadier × integrator (synthesis)
- **Output:** integrated directly into canonical document; draft preserved at
  `swarm/wiki/drafts/...-brigadier-§1-tldr.md`
- **Word floor:** 400-600 words
- **Acceptance predicate:**
  - 9 directions revenue role: Phase-1 primary (consulting + producer) / Phase-2 unlocks /
    Phase-3+ deferred
  - Phase-1 €50K = revenue mix decomposition (concrete € per direction)
  - 5 gates trajectory headline numbers
  - Top-3 risk register items (from §11 Wave-C output)
  - M&A direction Phase-2+ optionality flag
- **Inputs:** all 13 prior cells

## §3 Cell distribution summary

| Cell | Section | Wave | Owner | Mode | Word floor |
|------|---------|------|-------|------|------------|
| C-01 | §2 Pricing | A | investor-expert | integrator | 3000-4500 |
| C-02 | §3 Unit-Econ | A | investor-expert | scalability | 2500-3500 |
| C-03 | §4 5-gate triggers | A | systems-expert | scalability | 2500-3500 |
| C-04 | §6 Revenue streams | A | mgmt-expert | integrator | 1500-2000 |
| C-05 | §13 Evolution master | A | mgmt-expert | scalability | 1000-1500 |
| C-06 | §5 Миллионер reconcile | B | philosophy-expert | critic | 1500-2000 |
| C-07 | §7 Cash flow Phase-1 | B | investor-expert | integrator | 1500-2000 |
| C-08 | §9 Investor relations | B | investor-expert | integrator | 1500-2000 |
| C-09 | §10 Compensation | B | mgmt-expert | integrator | 1500-2000 |
| C-10 | §12 Tools financial | B | systems-expert | integrator | 800-1200 |
| C-11 | §8 Patents + IP | B | engineering-expert | integrator | 1500-2000 |
| C-12 | §11 Risk register | C | philosophy-expert | critic | 1500-2000 |
| C-13 | §14 Open questions | C | philosophy-expert | critic | 500-1000 |
| C-14 | §1 TL;DR | C | brigadier | integrator | 400-600 |

**Total floor:** 23 700-32 100 words. Fits 15-25K Deep Dive policy floor; ceiling
controlled by integration prune if exceeds 25K (preserves quality, removes redundancy).

## §4 Mode coverage check

- **integrator:** 8 cells (C-01, C-04, C-07, C-08, C-09, C-10, C-11, C-14) ✓
- **critic:** 4 cells (C-01-validation, C-06, C-12, C-13) ✓
- **scalability:** 3 cells (C-02, C-03, C-05) ✓
- **brigadier-synth:** 1 cell (C-14) + integration pass

5 experts × 4 role-modes = 20 invocation-cells per ROY-ALIGNMENT §3 (mgmt / investor /
philosophy / systems / engineering). All 5 experts covered. All 4 modes covered.
Integrator dominant for foundational sections; critic dominant for risk + open questions;
scalability dominant for evolution + unit-econ scaling.

## §5 Integration responsibilities (brigadier)

After all 14 cells return drafts:

1. **Cross-section number reconciliation:**
   - Pricing in §2 ⇄ unit-econ in §3 (revenue per engagement consistent)
   - Unit-econ §3 ⇄ cash flow §7 (monthly contribution margin consistent)
   - Cash flow §7 ⇄ risk register §11 (cash runway < threshold = R-1 mitigation trigger)
   - Pricing §2 ⇄ миллионер reconciliation §5 (income-floor per archetype × tier)
   - 5-gate triggers §4 ⇄ evolution master §13 (timing ranges consistent)
   - Compensation §10 ⇄ team trajectory in §13 (D26 50-100 cardinality)
   - Patents §8 ⇄ §13 (Phase-2 EU filing in evolution table)
   - Investor relations §9 ⇄ §13 (Phase-2 €5-15M valuation in evolution table)

2. **Lock compatibility audit:**
   - 28 Locks D1-D28 — no violations
   - Conflicts flagged in §14, NOT overridden

3. **Provenance audit:**
   - Every non-trivial paragraph carries `[src:<path>#<section>]`
   - L5 + L6 + SYSTEM-OVERVIEW + voice-memo references verified

4. **F-G-R audit:**
   - Every claim carries F-level + ClaimScope + R
   - F2 (preliminary) flagged honestly; no F0/F1 (rumour) shipped

5. **Word count audit:**
   - Each section meets word floor
   - Total 15-25K target

## §6 Commit cadence (target 16-18 commits)

```
1.  [l7-deep-dive] phase-1 intake + phase-2 WBS
2-15. [l7-deep-dive] §N <name> drafted
16. [l7-deep-dive] integration pass complete
17. [l7-deep-dive] Part F verification; awaiting Ruslan ack
```

Per shared-protocols §8: atomic per-section. No `--amend`, no `--no-verify`.

## §7 Stage-Gated discipline

- **NO** Full-Auto Phase 7 compound
- AWAITING-APPROVAL packet at `swarm/gates/AWAITING-APPROVAL-layer-7-business-trajectory-deep-dive-2026-04-25.md`
- After Ruslan ack → Phase 7 compound + Phase 8 archive

→ Wave A dispatch begins now (5 cells parallel).
