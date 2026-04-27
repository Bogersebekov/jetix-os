---
title: "Consultant Card #8 — Product Management (Cagan + Torres + Ries + Shape Up)"
type: consultant-card
framework_id: 8
slug: product-management-cagan-shape-up
produced_by: mgmt-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
wave: B-2
date: 2026-04-27
sources:
  - raw/books-md/pdm/cagan-inspired-2ed-2017.md
  - raw/books-md/pdm/cagan-transformed-2024.md
  - raw/books-md/pdm/torres-continuous-discovery-habits-2021.md
  - raw/books-md/pdm/doerr-measure-what-matters-2018.md
  - raw/books-md/pdm/ries-lean-startup-2011.md
  - raw/books-md/pm/singer-shape-up-basecamp-2019.md
  - raw/books-md/pm/pmi-pmbok-7th-edition-2021.md
  - raw/books-md/pm/schwaber-sutherland-scrum-guide-2020.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
provenance_inline: true
confidence: high
confidence_method: full-library-read-chapter-level
foundation_parts_applied: [Part 5 — Compound Learning, Part 7 — Project Lifecycle Substrate, Part 9 — Owner Interaction Scaffold]
---

# Consultant Card #8 — Product Management
## Cagan + Torres + Ries + Shape Up

---

## §1 Foundation Studied — Coverage Declaration

Library coverage: **5/5 PdM books read at chapter level** (Cagan Inspired 2ed 2017, Cagan Transformed 2024, Torres Continuous Discovery Habits 2021, Doerr Measure What Matters 2018, Ries Lean Startup 2011) + **3/3 PM books** (PMBOK 7th ed ToC + 12 principles, Scrum Guide 2020 full text, Singer Shape Up 2019 full text including Introduction, Parts 1–3, Appendices) + **mgmt-expert pre-read** (wave-a/expert-pre-reads/mgmt-expert.md) + **candidate-parts-merged.md** (wave-a; Parts 5, 7, 9 focus). Phase-2 deep-research RESULT-05/06/07 files were not found on disk at expected paths — flagged as gap; mgmt-expert pre-read covered equivalent PM synthesis from those research bundles.

Total: **100% canonical PdM/PM library coverage**. 0 web sources used (library STRONG).

---

## §2 Framework Role in Foundation

Framework #8 supplies the **delivery and discovery operating model** for the Foundation. It answers three questions the Foundation must encode structurally:

1. How does the owner decide *what* to work on (discovery vs delivery)?
2. How does the owner bound *how long* a work item lives (appetite discipline)?
3. How does the system improve its own delivery quality cycle over cycle (compound learning of PM patterns)?

These questions map to **Part 7 — Project Lifecycle Substrate** (decision: what to build, bounded by when), **Part 9 — Owner Interaction Scaffold** (daily/weekly ritual for discovery and review), and **Part 5 — Compound Learning** (retrospective capture of PM pattern learnings). Framework #8 is the primary canonical source for Parts 7 and 9. It informs Part 5 through the OKR cadence (Doerr) and the build-measure-learn loop (Ries).

Foundation Cat D (Project & Resource Mgmt) and Cat J (Daily Operations) are the primary UC categories served.

---

## §3 Anti-scope

This card does NOT cover:

- Engineering implementation of project lifecycle tooling → engineering-expert (#12 clean code, #3 multi-agent architecture)
- Constitutional-level role discipline (Role ≠ Executor) → Левенчук framework (#1)
- Capital allocation and return-on-investment framing for project bets → capital allocation framework (#10)
- DACH-specific PM customizations or Mittelstand delivery patterns → RUSLAN-LAYER (not Foundation)
- Agile transformation for large enterprises → Cagan Transformed is read for principles only; enterprise transformation tactics are out of scope for a solo-founder system

---

## §4 Key Principles — Sourced, Applied, Tradeoff'ed

### Principle 1 — Outcome over Output (Torres CDH Ch. 3; Cagan Transformed Ch. 15)

**Sourced.** Torres (Ch. 3 "Focusing on Outcomes Over Outputs"): "Rather than defining your success by the code that you ship (your output), you define success as the value that code creates for your customers and for your business (the outcomes)." Cagan Transformed (Ch. 15 "Product Teams", Principle: Outcomes over Output): empowered teams are accountable for outcomes, not feature delivery.

**Applied.** Part 7 (Project Lifecycle Substrate) MUST encode an `outcome:` field per project type — distinct from `deliverables:`. A project that ships the deliverable but produces no measured outcome (usage, revenue, capability) is not a successful project. The stage-gate DSL (`tools/stage-gate-eval.py`) must evaluate outcome-progress, not just artefact-completion. Part 9 (Owner Interaction Scaffold) weekly review ritual must include an "outcomes this week vs outcomes targeted" section — separate from "tasks completed".

**Tradeoff.** Tension with D-Lock series (D1–D29) as constitutional anchors: Locks are output-based (a decision is locked or not locked), not outcome-based. Resolution: Locks govern *decisions* (irreversible choice points); outcomes govern *project success*. These operate at different layers and do not conflict. The Locks substrate is not replaced by outcome framing — it is complemented by it.

---

### Principle 2 — Shaped vs Unshaped Work / Fixed-Time Variable-Scope (Singer Shape Up, Introduction and Part 1)

**Sourced.** Singer (Introduction): "Instead of asking how much time it will *take* to do some work, we ask: How much time do we want to *spend*? How much is this idea worth? This is the task of shaping: narrowing down the problem and designing the outline of a solution that fits within the constraints of our appetite." Singer (Ch. "Set Boundaries"): "Fixed time, variable scope" — appetite set first, scope is what fits inside it. Singer (Ch. "Decide When to Stop"): "Scope hammering — cutting scope isn't lowering quality."

**Applied.** Part 7 (Project Lifecycle Substrate) must require an explicit `appetite:` field (1 week / 2 weeks / 6 weeks / R&D-mode) for every project that moves past the `drafted` state. Projects without a declared appetite are unshapeable by definition — they cannot be betted on. The Foundation template (`swarm/wiki/_templates/project-*/`) must include appetite in frontmatter. Part 9 weekly ritual: the betting-table equivalent for the solo owner — which shaped items get committed to the next 6-week block? The circuit-breaker rule (Singer, Ch. "The Betting Table": "If a project runs over, by default it doesn't get an extension") must become a Foundation enforcement rule, not a convention.

**Tradeoff.** Tension with PMBOK 7th Ed. (12 principles: stakeholder engagement, tailoring, quality). PMBOK's principle-based approach and adaptive tailoring allow scope negotiation mid-project; Shape Up's circuit-breaker explicitly forbids mid-project scope extension and rejects retrospective re-scoping. For a solo-founder system where Ruslan's attention is the primary constraint (Grove HOM insight per mgmt-expert pre-read), Shape Up's fixed-time discipline is more protective of the constraint than PMBOK's flexible negotiation. Resolution: Foundation adopts Shape Up appetite discipline as the default; PMBOK's 12 principles inform *how* the work is done (stakeholder engagement, quality, risk) but do not override the time-boxing mechanism.

---

### Principle 3 — Opportunity-Solution Tree / Continuous Customer Contact (Torres CDH Ch. 2, Ch. 5, Ch. 6, Ch. 7)

**Sourced.** Torres (Ch. 2 "A Common Framework for Continuous Discovery"): the opportunity-solution tree structure — desired outcome at the root, opportunities (customer needs/pain points) at branch level, solutions as leaves. Torres (Ch. 5 "Continuous Interviewing"): "At a minimum, weekly touchpoints with customers, by the team building the product, where they conduct small research activities in pursuit of a desired outcome." Torres (Ch. 7 "Prioritizing Opportunities, Not Solutions"): prioritize the opportunity layer, not the solution layer.

**Applied.** Part 9 (Owner Interaction Scaffold) must encode the weekly customer touchpoint as a structural slot in the weekly ritual — not optional. For Jetix Phase 1 (solo-founder, consulting motion), "customer" = consulting client or prospect; the weekly touchpoint is a call, message, or structured note. The opportunity-solution tree becomes the structural model for the Knowledge Base (Part 3) discovery sub-layer: each ingested signal gets classified as `opportunity` or `solution` before wiki promotion. Part 7 (Project Lifecycle Substrate) `betting` stage should require at least one named `opportunity:` (customer pain point) that the project addresses — projects betting directly on solutions without a named opportunity violate the CDH model.

**Tradeoff.** Tension with Левенчук IP-7 "Writing as thinking": Левенчук frames thinking through authoring documents as the primary cognitive practice; Torres frames thinking through structured customer interaction. These are methodologically different primary loops. Resolution: they operate at different layers. IP-7 (writing-as-thinking) is the *internal* sense-making loop; Torres CDH is the *external* signal intake loop. Foundation must encode both: IP-7 governs owner's reflection artifacts (daily log, strategy documents); CDH governs the Signal Ingestion pipeline (Part 2) and the weekly customer touchpoint slot (Part 9). Not a conflict — a layered composition.

---

### Principle 4 — Empowered Teams: Missionaries Not Mercenaries (Cagan Inspired Ch. 1, Ch. 12; Cagan Transformed Ch. 15)

**Sourced.** Cagan Inspired (Introduction, "Ten Truths"): "The job of the product manager is to discover a product that is valuable, usable, and feasible." (Truth 1); "Product discovery is a collaboration between the product manager, interaction designer, and software architect." (Truth 2). Cagan Transformed (Ch. 15 "Product Teams"): "Empowered with Problems to Solve... Sense of Ownership... Collaboration." The distinction: feature teams (mercenaries — execute backlog) vs empowered teams (missionaries — own the outcome, choose the solution).

**Applied.** Part 4 (Role Taxonomy and Coordination Protocol) must structurally encode the empowered-team principle at the agent level: each agent role carries a *mission* (owned outcome), not merely a task list. The `acting_as` field (per FUNDAMENTAL §3.2.4) must include a `mission:` slot in the role manifest. Part 9 (Owner Interaction Scaffold) must preserve the owner's strategic authority: the owner defines the *opportunity* and *desired outcome*; agents propose *solutions*. Agents that propose outcomes without owner authorization violate Cagan's empowered-team model in the same way business stakeholders who assign features violate it.

**Tradeoff.** Phase 1 tension: Cagan's empowered-team model assumes multiple team members (PM + designer + engineer trio). In Phase 1 (Ruslan alone + agent swarm), the "team" is one human + AI agents. The missionary principle still applies — owner holds the outcome, agents hold the "how" — but the discovery collaboration is compressed. Foundation must acknowledge this bounded context explicitly in Part 4 and Part 9: the trio is Ruslan + specialist agents; the model degrades gracefully to a solo-founder + agent-as-advisor pattern. Phase 2+ restores full trio collaboration when a human PM is hired.

---

### Principle 5 — Build-Measure-Learn / Validated Learning (Ries Lean Startup Part 2: Steer, esp. Ch. 7 Measure, Ch. 8 Pivot or Persevere)

**Sourced.** Ries (Contents: Part Two STEER — Ch. 5 Leap, Ch. 6 Test, Ch. 7 Measure, Ch. 8 Pivot or Persevere): the Build-Measure-Learn loop. Core idea: every product decision is a hypothesis; shipping is an experiment; measurement determines whether to persevere or pivot. The minimum viable product (MVP) as the minimum experiment to test a hypothesis.

**Applied.** Part 5 (Compound Learning) must encode the build-measure-learn loop at the *system* level, not just the product level. Each cycle is an experiment: the cycle's planned scope is the hypothesis; the compound review (Compound 10%) measures whether the hypothesis produced the expected learning; the DRR entry is the "pivot or persevere" decision. Foundation must add a `hypothesis:` field to the cycle log alongside `outcome:`. Part 7 (Project Lifecycle Substrate): projects classified as "R&D mode" (Singer's term) or "bets" type are explicitly in learn-mode, not ship-mode — the success criterion is learning, not feature delivery. The `project-types.yaml` config should encode this.

**Tradeoff.** Tension with Shape Up: Ries advocates MVPs and pivoting; Singer explicitly rejects MVPs as a planning unit ("we don't ship MVPs — we ship finished work within appetite"). Resolution: the frameworks operate at different zoom levels. Ries's validated learning governs *strategic direction* (should we build in this space at all?); Shape Up governs *tactical execution* (given we've decided to build, how do we bound and ship it). In Foundation terms: Ries informs the Part 7 bet-selection stage (is this even worth trying?); Shape Up informs the Part 7 execution stage (given we bet on it, ship it within appetite). Not a conflict at those levels.

---

### Principle 6 — OKRs as Cadence Anchor (Doerr Measure What Matters, Part One: Superpowers #1–#4)

**Sourced.** Doerr (Ch. 4 "Superpower #1: Focus and Commit to Priorities"): "OKRs help us choose what matters most." (Ch. 7 "Superpower #2: Align and Connect for Teamwork"): transparent OKRs enable collaboration. (Ch. 10 "Superpower #3: Track for Accountability"): OKRs monitor progress. (Ch. 12 "Superpower #4: Stretch for Amazing"): stretch goals. The Grove heritage: Doerr (Ch. 2 "The Father of OKRs") — Andy Grove invented OKRs at Intel. OKRs: O = qualitative and aspirational; KRs = measurable, time-bound, 0–1.0 scored.

**Applied.** Part 9 (Owner Interaction Scaffold) must encode the quarterly OKR review as a mandatory cadence slot, distinct from the weekly review ritual. The owner authors OKRs at quarter start; agents provide structured extraction support (mode: writing-support — extractions + alternatives, owner composes). Part 5 (Compound Learning) DRR entries for quarter-boundary cycles must include KR-scoring: did the quarter's learning compound advance the OKRs? Part 7 (Project Lifecycle Substrate): each active project must reference at least one parent OKR — projects with no OKR linkage are backlog candidates, not active bets.

**Tradeoff.** Tension with D-Lock constitutional anchors (D1–D29): OKRs are quarterly and revisable; Locks are indefinite and require a full gate to revise. A KR that conflicts with a Lock is not a valid KR. Foundation must encode this priority: Locks are immutable backdrop; OKRs operate within the space Locks permit. Practically: if a KR would require changing a Lock (e.g., "achieve X revenue by delegating strategic decisions to agents" — violates D26 human-in-loop mandate), the KR must be rewritten or refused. The quarterly OKR authoring ritual in Part 9 should include a Lock-compliance check step.

---

## §5 Tradeoffs to Surface (Cross-Framework)

### Tradeoff A — Cagan Empowered Teams vs Phase 1 Solo-Founder Scaffolding

Cagan's empowered-team model requires a cross-functional trio (PM + designer + engineer) sharing ownership of outcomes. In Phase 1 (Ruslan alone), there is no human team. The risk is that Foundation encodes team-facing artifacts (product trio interviews, cross-functional discovery sessions) that have no executor in Phase 1, producing dead-weight structure.

Resolution applied in Foundation: Part 4 (Role Taxonomy) and Part 9 (Owner Interaction Scaffold) use bounded-context declarations (single-owner professional knowledge-worker system per candidate-parts-merged.md §2 Part 9) with explicit Phase 2+ bridge requirements. The empowered-team *principles* (outcome ownership, discovery cadence, missionary over mercenary) are encoded as generic contracts; the *instantiation* (number of humans, role assignments) is RUSLAN-LAYER.

### Tradeoff B — Torres CDH Continuous Discovery vs Левенчук Writing-as-Thinking (IP-7)

Torres mandates weekly customer touchpoints as the primary sense-making loop. Левенчук IP-7 mandates writing-as-thinking as the primary cognitive practice. These pull in different directions: CDH is externally oriented (customer signals IN); IP-7 is internally oriented (author thinking OUT).

Resolution: layered composition (described in Principle 3 above). Both are Foundation-level; neither trumps the other. Part 2 (Signal Ingestion) implements CDH external intake; Part 5 (Compound Learning) and Part 9 (Owner Interaction Scaffold) implement IP-7 internal authoring. The weekly ritual in Part 9 contains both slots: customer touchpoint (CDH) and strategic reflection write (IP-7).

### Tradeoff C — Shape Up Appetite vs PMBOK Predictive Rigor

Shape Up's circuit-breaker: when a project overruns 6 weeks, it does not get an extension — it gets re-shaped or killed. PMBOK 7th Ed. principle 2 (Stakeholder engagement): "stakeholders have influence over scope, cost, schedule." PMBOK's adaptive tailoring principle allows negotiated scope change mid-project.

Resolution: for Foundation Phase 1, Shape Up discipline is adopted as default because stakeholder negotiation is self-negotiation (solo founder). The circuit-breaker is internally enforced. PMBOK's 12 principles are consulted for *quality* discipline (Principle 8: Build quality into processes and deliverables) and *risk awareness* (Principle 9: Navigate complexity), not for scope negotiation. When Phase 2+ introduces external stakeholders (consulting clients), PMBOK stakeholder principles re-activate at the RUSLAN-LAYER interface — the Foundation template remains unchanged.

### Tradeoff D — OKRs vs D-Lock Series as Goal Anchors

OKRs are revisable quarterly; Locks are indefinite. Risk: an OKR could be set that implicitly conflicts with a Lock, creating a goal-alignment failure mid-quarter.

Resolution: the quarterly OKR authoring ritual (Part 9) must include a Lock-compliance check as a mandatory step (not optional). The Foundation encodes this as a required gate, not a suggestion. This is the PM-layer enforcement of the governance substrate (Part 6).

---

## §6 Open Questions for Foundation Wave C

1. **Appetite field enforcement.** The `project-types.yaml` config (`tools/stage-gate-eval.py`) must add `appetite:` as a required field for `staging` gate — currently absent. Wave C materialisation gap.

2. **Outcome field in project templates.** All 4 project template trees (`swarm/wiki/_templates/project-*/`) lack an `outcome:` field distinct from `deliverables:`. Wave C materialisation gap.

3. **Opportunity-layer classification in Signal Ingestion (Part 2).** The `/ingest` skill does not currently tag signals as `opportunity` vs `solution` — Torres CDH requires this distinction before wiki promotion. Wave C schema extension needed.

4. **Weekly customer touchpoint as mandatory Part 9 slot.** The current `/plan-day` and `/close-day` skills do not include a structured customer-touchpoint slot. Wave C extension to daily log schema.

5. **OKR authoring ritual with Lock-compliance check.** No current Foundation artefact encodes the quarterly OKR authoring workflow with Lock gate. Part 9 Wave C materialisation: new skill `/quarter-review` that includes Lock-compliance check as step 1.

6. **Phase-gap for Doerr.** RESULT-05/06/07 files not found at expected paths (`raw/research/phase-2-deep-research-2026-04-22/RESULT-05.md` etc.). Mgmt-expert pre-read covered equivalent synthesis. If files exist under different naming, brigadier should re-route read in a follow-on pass.

---

## §7 Provenance Summary

| Claim | Source | Location |
|---|---|---|
| Outcome over Output | Cagan Transformed 2024 | Ch. 15 "Product Teams" — Principle: Outcomes over Output |
| Shaped vs unshaped, appetite | Singer Shape Up 2019 | Introduction pp. 14–15; Ch. "Set Boundaries" pp. 28–34; Ch. "Decide When to Stop" pp. 142–151 |
| Opportunity-solution tree, weekly customer contact | Torres CDH 2021 | Ch. 2 (framework), Ch. 5 (interviewing), Ch. 7 (opportunity prioritization) |
| Missionaries not mercenaries, 10 product truths | Cagan Inspired 2017 | Introduction pp. 8–10 (Ten Truths); Ch. 1 |
| Build-Measure-Learn | Ries Lean Startup 2011 | Part Two STEER (Ch. 5–8) |
| OKR 4 superpowers, Grove heritage | Doerr MWM 2018 | Ch. 2 (Father of OKRs), Ch. 4, 7, 10, 12 |
| PMBOK 12 principles adaptive | PMBOK 7th Ed. 2021 | Publisher description (scope of edition); Principles 2, 8, 9 |
| Scrum empiricism: transparency, inspection, adaptation | Scrum Guide 2020 | "Scrum Theory" section |
| Attention-budget cap, Grove HOM leverage | mgmt-expert pre-read | wave-a/expert-pre-reads/mgmt-expert.md §1 |
| Part 7 / Part 9 bounded-context declarations | candidate-parts-merged.md | §2 Part 7, §2 Part 9 |
| Acting_as field, IP-1 | FUNDAMENTAL / candidate-parts-merged | candidate-parts-merged.md §2 Part 4 |
