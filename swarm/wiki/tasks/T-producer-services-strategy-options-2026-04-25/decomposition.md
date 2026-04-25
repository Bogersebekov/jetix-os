---
id: decomposition-T-producer-services-strategy-options-2026-04-25
title: "Phase-2 WBS — producer-services strategy-OPTIONS"
type: phase-2-wbs
cycle_id: cyc-producer-services-strategy-options-2026-04-25
task_id: T-producer-services-strategy-options-2026-04-25
created: 2026-04-25
mode: OPTIONS-PAPER
---

# §1 Wave plan

**Wave-A (parallel):** 5 cells dispatched in single message — full parallel, independent drafts.
**Wave-B (brigadier):** integration pass + proposal-language discipline check + Part F verification.
**Wave-C (gate):** AWAITING-APPROVAL packet → HALT.

# §2 Cell assignments

## C1 — mgmt-expert (integrator) — Market + Hypotheses + Proposal

**Output draft:** `swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-mgmt-integrator-market-hypotheses-proposal.md`

**Sections:**
- §2 Market analysis (1500-2500w)
  - Course creators (Kajabi/Teachable/Mighty Networks) — TAM/SAM/SOM
  - YouTube educators / podcasters — production complexity
  - Newsletter operators (Substack / Beehiiv) — pipeline diff
  - Coaches / consultants productizing — knowledge-product transition
  - Specialist-bloggers (deep technical/business/research) — D22 fit
- §3 Hypothesis cards H1-H5 (2000-3500w)
  - Each card: one-line + target customer + acquisition mechanism + pipeline shape +
    pricing tier fit + Phase-1 traction signal + 3-5 pros + 3-5 cons + CAC est + LTV est +
    brigadier rating 1-10 + empirical test 30-60 days
- §7 Brigadier proposal (250-500w) — **proposal-language only**, primary hypothesis +
  acquisition path + pricing tier + 30-day test + decision criteria. NO directive language.

**Constraints:**
- Generate 3-5 hypotheses minimum. May propose H6+ if market analysis surfaces them
- Source from existing repo content + general knowledge synthesis
- Flag in §6 hand-off: «Ruslan has separate market analyses + competitor tables —
  integrate in next dedicated cycle»
- 28 Locks compatibility (D10/D11/D18/D22/D26)
- Provenance inline

## C2 — investor-expert (scalability) — Hypothesis economics + Pricing

**Output draft:** `swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-investor-scalability-economics-pricing.md`

**Sections:**
- §3 hypothesis economics (per H1-H5): CAC + LTV + LTV:CAC + payback + Phase-1 unit-econ check
- §5 Pricing tier hypotheses (500-1000w):
  - L7 §2.2 baseline: Pilot €2-3K / Standard €4-6K / Premium €7-10K
  - Floor adjustment: €3K experimental vs €5K operational — empirical case for each
  - One-time setup fee + retainer (front-load value-prove)
  - Performance bonus tier (% of revenue uplift)
  - Productized 4-week sprint vs ongoing retainer — GM compare

**Constraints:**
- L7 §3.2 baseline: GM 56.3%, 2.0 hrs/€1K, LTV €36K, LTV:CAC 6:1
- Each hypothesis must have unit-econ check (GM ≥40% Phase-1 floor; LTV:CAC ≥3:1)
- Flag if hypothesis fails unit-econ floor
- Provenance inline

## C3 — systems-expert (scalability) — Acquisition paths + Production pipeline

**Output draft:** `swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-systems-scalability-acquisition-pipeline.md`

**Sections:**
- §4 Acquisition path variants (1000-1500w):
  - Cold outreach (LinkedIn / email per L6 §7 templates)
  - Podcast guesting (appear on target audience podcasts)
  - Blogger collaborations (cross-promotion)
  - Referral mechanic (existing network warm intros)
  - Content marketing (case study series public)
  - Discovery call funnel (free strategy session as TOF)
  - Per path: cost (€ + Ruslan-hrs) / time-to-first-signed / conversion hypothesis / risk
- §3 production pipeline shape per hypothesis (research → script → record → edit → repurpose
  variants per H1-H5; feedback loops; client-private KB depth requirements)

**Constraints:**
- Use Meadows leverage points + Ashby variety to distinguish path leverage
- Integrate with §3 cards (handoff to mgmt-expert via shared draft)
- L5 §3.2 §6 pipeline canonical baseline
- Provenance inline

## C4 — philosophy-expert (critic) — Open questions + Strategist-discipline review

**Output draft:** `swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-philosophy-critic-open-questions-discipline.md`

**Sections:**
- §6 Open questions (500-800w):
  - Q-PS-01: Which 1-2 hypotheses to test first 30-60 days?
  - Q-PS-02: Pricing floor — €3K experimental or €5K operational?
  - Q-PS-03: Acquisition path — start with which 2 paths in parallel?
  - Q-PS-04: Voice-preservation gate — manual every cycle or sample-based?
  - Q-PS-05: Existing Ruslan market analyses — when integrate?
  - Q-PS-06: First 2 target accounts — Ruslan provides OR brigadier surfaces?
  - May add Q-PS-07+ if dissent emerges
- Strategist-discipline review (across §1-§7):
  - Flag any directive-language vs proposal-language drift
  - Flag any «accept-this» implicit framing
  - Verify AI-strategist Левенчук hard rule preserved
- Dissent preservation per AP-MGMT-11 / philosophy mode

**Constraints:**
- NO authoritative claims — critic role only
- Mark items needing Ruslan ack explicitly
- Reference Ruslan 25.04 verbatim quote for grounding

## C5 — engineering-expert (integrator) — Production pipeline technical feasibility (lightweight)

**Output draft:** `swarm/wiki/drafts/T-producer-services-strategy-options-2026-04-25-engineering-integrator-pipeline-feasibility.md`

**Sections:**
- §3 production pipeline feasibility per H1-H5:
  - Voice pipeline (transcribe.py → extract.py → filter.py) capacity per hypothesis
  - /ingest multi-format requirements per hypothesis (audio-only vs video vs text)
  - Per-client KB anchor pattern (D28) per hypothesis
  - Tooling delta required (none / minor / major)
  - Pipeline integration risks (compute cost / Ruslan-time / contractor dep)
  - Phase-1 feasibility binary (yes / yes-with-effort / no-without-build)

**Constraints:**
- Lightweight — 600-1000w max
- Reference CLAUDE.md voice pipeline as authoritative substrate
- No code changes proposed
- 28 Locks compatibility (D25 company-as-code / D28 query-driven KB)

# §3 Brigadier integration sequence

1. Wait for all 5 cell drafts complete
2. Read all drafts in single pass
3. Synthesize into `directions/_active/producer-services/strategy-OPTIONS.md`:
   - Pull §2 + §3 + §7 from C1
   - Pull §3 economics + §5 from C2
   - Pull §4 + §3 pipeline from C3 (cross-ref C5 for feasibility)
   - Pull §6 from C4
   - Cross-ref C5 for §3 feasibility column per hypothesis
4. Write §1 TL;DR (brigadier-authored synthesis) + §8 anti-scope (brigadier-authored)
5. Run proposal-language discipline check (per C4 dissent items)
6. Run 28 Locks compatibility check
7. Provenance inline check
8. Word-floor check per section

# §4 Part F verification predicates

- [ ] §1 TL;DR ≥300w with 3-5 hypotheses + proposal + top-3 unknowns
- [ ] §2 Market ≥1500w with 5 sub-segments
- [ ] §3 Hypothesis cards: 3-5 cards, each complete (one-line/target/acq/pipeline/tier/signal/pros/cons/CAC/LTV/rating/test)
- [ ] §4 Acquisition paths: 6 paths × cost/time/conversion/risk
- [ ] §5 Pricing variants: ≥4 variants with empirical case
- [ ] §6 Open questions: 6 Q-PS-XX explicit
- [ ] §7 Brigadier proposal: ≤500w, proposal-language only, no directive
- [ ] §8 Anti-scope: 4+ explicit «NOT» items
- [ ] No «here is THE strategy» language
- [ ] No M&A in scope
- [ ] No Notion writes
- [ ] 28 Locks compatibility verified
- [ ] Provenance inline
- [ ] Total ≥6300w

# §5 Commit cadence (target ~9 commits)

1. `[ps-options] phase-1 intake + phase-2 WBS`
2. `[ps-options] cells dispatched (5 in parallel)`
3. `[ps-options] cell drafts received; integration begins`
4. `[ps-options] §2 market analysis integrated`
5. `[ps-options] §3 hypothesis cards integrated`
6. `[ps-options] §4 acquisition paths + §5 pricing integrated`
7. `[ps-options] §6 open questions + §7 proposal + §8 anti-scope integrated`
8. `[ps-options] §1 TL;DR + Part F verification`
9. `[ps-options] AWAITING-APPROVAL packet; HALT`
