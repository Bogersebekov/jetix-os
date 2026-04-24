---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §15
type: layer-deep-dive-section
mode: critic
author: philosophy-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "§3-§8 full"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md", range: "C-02 through C-12 acceptance predicates"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.3-usb-c.md", range: "§10 Open Questions + frontmatter dissents D-USB-C-1/D-USB-C-2"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.4-matchmaker.md", range: "§10 Open Questions + frontmatter dissents D-match-1/D-match-2"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.5-secure-network.md", range: "§10 Open Questions + Integrator synthesis"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md", range: "§10 Open Questions + frontmatter dissents"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md", range: "§10 Open Questions + frontmatter dissents"}
  - {path: "swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-critic-§3.8-tokens.md", range: "§10 Open Questions + frontmatter dissents"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§12 Preserved Dissents 1-5"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§12 Open Questions Q-01..Q-15 + §12.4 Conflict Flags"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25-D28 full + Smart AI internal note"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path A/B/C"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 D23 + §7 archetypes + §14 Note 5"}
  - {path: "decisions/JETIX-PLAN.md", range: "§1 revenue-gated unlocks + §3 Phase-1 + §4 transition"}
word_count_estimate: ~1050
confidence: high
confidence_method: direct-consolidation-from-cell-drafts-and-prior-cycle-dissents
escalations: []
dissents:
  - claim: "Token D23 Option B should never launch — consulting + educational + licensing fund Jetix growth sufficiently"
    held_by: investor-expert × critic (cell C-10)
    F: F4
    ClaimScope: "applies if $100M+ ARR achieved through consulting/product/alliance without specialist-compensation friction becoming operational blocker"
    R:
      refuted_if: "Phase-3 lawyer consultation confirms MiCA/Howey risk manageable AND specialist compensation friction above $10M ARR cannot be solved without token infrastructure"
      accepted_if: "Phase-3 review at $100K self-earned threshold returns go/no-go = no-go from legal counsel; or consulting ARR alone sustains all specialist comp by G3"
  - claim: "Smart AI promotion to D29 external lock should remain indefinitely internal"
    held_by: philosophy-expert × critic (cell C-11)
    F: F3
    ClaimScope: "applies for Phase-1/2; re-evaluate at G2 with outreach-response-rate delta evidence"
    R:
      refuted_if: "outreach responses consistently reference 'Smart AI' framing as the hook; empirical data collected at G2"
      accepted_if: "Smart AI removed from external materials causes no detectable outreach conversion drop after A/B test of landing pages"
---

# §15 Open Questions + Preserved Dissents + F-G-R Tagging

> Cell C-12. philosophy-expert × critic. Wave C.
> Consolidates per-direction open questions from C-02 through C-11, preserved dissents from
> prior cycles, Lock tensions flagged but not overridden, and identifies which questions
> block Phase 3 strategic documents (ai-consulting-dach/strategy.md, producer-services/strategy.md,
> JETIX-COMPASS, ai-consulting-dach/strategy.md) versus which can wait.

---

## §15.1 Introduction

This section is the epistemic-consolidation layer for the entire L5 deep-dive. Its purpose is
not to resolve open questions — that authority belongs to Ruslan — but to name them precisely
in falsifiable form, to assign each an F-level and a ClaimScope, and to specify which require
HITL ack before Phase 3 strategic documents can be drafted. Consolidation draws from nine
direction-section drafts (C-02 through C-11), three prior-cycle preserved dissents from
KM-ARCHITECTURE-VARIANTS §12, the inherited question-set from LAYER-6 §12 (partially acked,
partially carried forward), and five Lock tensions surfaced during L5 drafting. The top five
questions requiring Ruslan ack before Phase 3 are identified in §15.2 by two criteria: (1) the
answer materially changes the design of a Phase 3 strategic document, and (2) no empirical
resolution path exists within Phase 1 / Phase 2 operations alone.
[src:swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md#§3]
[src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12]

---

## §15.2 Top 5 Questions for Ruslan Ack

The five questions below are explicitly blocking. Phase 3 strategic documents
(`ai-consulting-dach/strategy.md`, `producer-services/strategy.md`, Phase 4 outreach message)
cannot be finalized without Ruslan's stated position on each. Brigadier recommendations are
offered as the default if Ruslan defers; an explicit ack is preferred.

---

### Q1 — Path A / B / C Phase-A default for USB-C integration services + consulting hybrid engagements

**Source.** §3.3 USB-C draft dissent D-USB-C-1 [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.3-usb-c.md#frontmatter] +
KM-ARCHITECTURE-VARIANTS §12 Dissent 3 (inherited) [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12] +
STRATEGIC-INSIGHT §5 [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5].

**Positions preserved.**

- Position A — Strategic Insight §5 + systems-integrator: Path C (hybrid: client data +
  Jetix-agents tunnel) is the recommended architecture for enterprise-grade, compliance-strict
  clients. Reasoning: maximum data-sovereignty story + Mittelstand GDPR narrative.
- Position B — investor-critic + KM-ARCHITECTURE-VARIANTS Dissent 3: Path B (client-hosted,
  €3K onboarding + €15K/yr recurring) achieves 70.7% GM yr1, satisfying the Phase-A 70% GM
  floor. Path C in Phase A (54% GM) fails the floor without a first contractor hire.
  Reasoning: solo-founder Phase-A economics require Path B discipline.

**F-G-R.**
- Position A: F3 / ClaimScope: enterprise clients with compliance-strict GDPR IT departments /
  R: refuted if first Mittelstand contract shows Path C GM ≥70% yr1.
- Position B: F4 / ClaimScope: Phase-A first 1-3 client deployments, solo-founder unit-econ /
  R: accepted if Path B achieves consistent 70%+ GM in first 2 deployments; receipt in
  `swarm/wiki/operations/clients/<slug>/financials.md`.

**Blocks.** Phase 3 `ai-consulting-dach/strategy.md` offer structure; Phase 4 outreach
"what do we sell and at what price tier" message. Without a stated default, the strategy
document cannot commit to a delivery model.

**Brigadier recommendation.** Path B as Phase-A default for first 3-5 contracts (investor
unit-econ discipline). Re-evaluate at G2 with empirical unit-econ data from first contracts.
Path C becomes the enterprise option post-G2 when first contractor/hire exists.

**How to ack.** In AWAITING-APPROVAL packet: choose Path B (default) / Path C (default) /
Path A (default) / "empirical resolution — first contract decides" / "Path B default with
Path C for any contract >€30K ARR."

---

### Q2 — YouTube-analyzer Phase-2 activation pull-forward vs gate-sequencing discipline

**Source.** §3.6 YouTube-analyzer dissent + §2 Portfolio dissent (investor) [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md#frontmatter] +
audio_514 "золотая жила" urgency [src:reports/review_2026-04-24.md#rows-684-689].

**Positions preserved.**

- Position A — portfolio / gate-sequencing: YouTube-analyzer activates at Phase 3 (G3→G4,
  $100M trajectory). Phase 1 and Phase 2 are occupied by consulting and Продюсерский центр.
  Diluting Phase-1 focus is a risk-of-ruin trigger for the €50K gate.
- Position B — audio_514 urgency: "золотая жила" framing suggests the asymmetric opportunity
  is NOW. If Phase-1 consulting clients include YouTube operators who organically pull for the
  tool, the empirical signal exists to pull forward to Phase 2 manual-delivery stage.

**F-G-R.**
- Both positions: F4 / ClaimScope: applies only at Phase-2 activation decision point /
  R: Position B refuted if no Phase-1 consulting client ever requests YouTube analysis as a
  deliverable; Position A refuted if ≥1 Phase-1 client requests YouTube analysis + is willing
  to pay ≥$2K.

**Blocks.** §3.6 activation timing; bandwidth-allocation Phase-2 capital plan. The §14 Tools
Roadmap (C-13) cannot specify YouTube-analyzer engineering investment without this decision.

**Brigadier recommendation.** Defer to G2 preparatory (manual analyst-template), launch MVP
at G3. Exception trigger: if ≥1 Phase-1 consulting client explicitly requests YouTube
channel intelligence + willing to pay ≥$2K, pull forward as empirical-signal override.
Set this trigger explicitly so Phase 2 capital allocation can respond without HITL.

**How to ack.** Accept brigadier recommendation / set explicit pull-forward trigger condition
/ defer entirely to Phase 3.

---

### Q3 — Smart AI promotion to D29 lock: when and under what evidence?

**Source.** §3.9 Smart AI draft (C-11) + D25-D28 addendum "Smart AI internal note" [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI] + audio_529 [src:reports/review_2026-04-24.md#audio_529].

**Positions preserved.**

- Position A — philosophy-expert (epistemically grounded): Smart AI should remain an internal
  narrative label indefinitely through Phase 2. The risk of reification before the concept
  has empirical support (outreach response data) is an over-claim anti-pattern. "Smart AI"
  as an external brand name without a falsifiable claim attached to it violates AP-PHIL-1.
- Position B — graduation case: Smart AI could become D29 external brand at Phase 3 based
  on empirical outreach signal (response-rate delta between materials that name it vs those
  that do not). This keeps optionality open without committing to a brand that may not
  resonate in DACH Mittelstand context.

**F-G-R.**
- Position A: F3 (philosophical stance, not empirical) / ClaimScope: Phase-1/2 pre-data /
  R: refuted if outreach A/B test shows "Smart AI" framing generates higher response rate
  in DACH Mittelstand ICP.
- Position B: F4 / ClaimScope: Phase-3 re-evaluation gate; not applicable Phase-1/2 /
  R: refuted if A/B test at G2 confirms Smart AI framing has zero conversion delta.

**Blocks.** External-facing materials design — landing pages, sales decks, DACH outreach
templates. If Smart AI is not an external brand in Phase 3, landing pages designed around
it must be rebuilt.

**Brigadier recommendation.** Remain internal through Phase 2; Ruslan re-evaluates at G2
with outreach-response-rate data.

**How to ack.** Keep internal (current) / graduate to D29 external lock / set A/B test
at G2 as re-evaluation trigger with explicit decision criterion.

---

### Q4 — Educational products at G2→G3 launch: cohort-first vs self-serve-first

**Source.** §3.7 Educational dissent [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md#frontmatter + §10].

**Positions preserved.**

- Position A — cohort-first: higher margin per learner ($2K-$5K vs €499-€1,499);
  stronger relationships; fork-and-merge workshop as live session; creates Secure Network
  member pipeline. Cost: Ruslan direct instruction time caps at 1-2 cohorts per quarter
  until instructor certification exists.
- Position B — self-serve-first: scales without proportional Ruslan time; lower margin per
  learner; weaker learner accountability; harder to build fork-and-merge culture async.
  Advantage: lower barrier to first revenue at G2 before methodology is fully documented
  for live cohort delivery.

**F-G-R.** Both: F4 / ClaimScope: applies at G2→G3 launch decision / R: cohort-first
refuted if cohort margin < self-serve at 3x scale; self-serve-first refuted if
cohort format validated with 2+ paying cohorts showing cohort NPS >40 and margin >€3K/learner.

**Blocks.** Phase 3 `educational-strategy.md` document. Format decision changes platform
choice (Teachable vs custom), pricing architecture, instructor pipeline plan, and Ruslan
time-allocation for Phase 3.

**Brigadier recommendation.** Cohort-first at G2→G3 (2-3 cohorts to validate methodology
teachability); self-serve as concurrent lower-cost tier; enterprise license as the scale
path beyond G3+. Ack or override; L7 pricing cycle owns the final structure.

**How to ack.** Cohort-first / self-serve-first / parallel launch / delegate to L7 pricing.

---

### Q5 — Token D23 Option B: Phase-3+ launch vs deprecate if consulting+educational+licensing
funds growth sufficiently

**Source.** §3.8 Tokens draft preserved dissent (investor-critic, cell C-10)
[src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-critic-§3.8-tokens.md#frontmatter + §10 Q5].

**Positions preserved.**

- Position A (default per D23): D23 Option B is Phase-3+ optionality. Launch the internal
  utility token (JCU) at G3→G4 when specialist-compensation friction becomes operational and
  Alliance Foundation is incorporated (L6 Option C acked). Retire optionality formally only
  if Phase-3 legal counsel returns a risk-benefit ratio exceeding the opportunity cost of
  competing capital uses.
- Position B (investor-critic primary dissent): The token should never launch if consulting
  + educational + Alliance membership fees fund Jetix growth sufficiently by $100M ARR. Token
  infrastructure (€100K-€500K legal + engineering capex at Phase-3) competes with other
  capital priorities. The retirement condition must be stated explicitly and Ruslan must ack it.

**F-G-R.**
- Position A: F4 / ClaimScope: Phase-3+ design optionality; not active Phase-1/2 /
  R: refuted if Phase-3 legal review returns prohibitive MiCA/Howey risk-benefit ratio.
- Position B: F4 / ClaimScope: holds if $100M ARR achieved without specialist-compensation
  friction becoming an operational blocker / R: refuted if cross-border specialist payment
  friction above $10M ARR blocks operations and no non-token solution exists.

**Blocks.** Phase 4+ capital planning. More precisely: any Phase 3 investor program document
(§3.7) that describes Jetix capital structure must acknowledge whether D23 Option B is active
or deprecated. Investor outreach materials cannot be ambiguous on this.

**Brigadier recommendation.** Preserve as optionality through Phase 3 review. Explicit
retirement condition: if $100K self-earned threshold is reached and Phase-3 lawyer confirms
consulting ARR can sustain all specialist compensation without token infrastructure, deprecate
D23 Option B formally via a LOCKS-D23-DEPRECATION document (brigadier authors on Ruslan ack).

**How to ack.** Accept-optionality (current default) / plan-to-launch at explicit trigger /
deprecate-D23-option-B now / "revisit at $100K self-earned threshold."

---

## §15.3 Secondary Questions (Not-Blocking, for Context)

These 12 questions are open and documented in per-direction drafts. They do not block Phase 3
strategic documents but will surface as design constraints at Phase 2 or Phase 3 execution.
Each is cited with F-level and source cell.

1. **ISO 27001 / BSI C5 certification timing: Phase 1 vs Phase 2.** Cost €30K-€80K + 6-9
   months. If deferred to G2, gap window while competing without certification.
   F3. [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.3-usb-c.md#§10-Q2]

2. **Underlying LLM default for Path A managed deployments: Mistral 7B Q4_K_M (Apache 2.0,
   cleanest commercial license) vs Llama 3.1-8B (broader community support, better
   mixed-language quality).** Resolves via 20-query DACH golden-set evaluation (separate
   task, not yet authorized). F3. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12-Dissent-2]

3. **DACH data-center for Phase-2 vs Phase-3.** BSI C5-grade EU compute (Hetzner/Cloudflare EU)
   for client KB hosting. Phase-2 immediate need for compliance-strict clients vs Phase-3
   capex trigger. F3. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5]

4. **Match-fee structure: task-side-only vs both-sides (task + specialist success-fee).**
   Anti-commodity argument favors task-side-only Phase-2; standard B2B marketplace logic
   favors both sides. Preserved as Dissent D-match-1 in §3.4 draft.
   F4. [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.4-matchmaker.md#§10-Q1]

5. **Matchmaker platform MVP at G2 (€200K) vs G3 (€1M).** G3 preferred (Secure Network
   liquidity ≥100 active members as hard precondition). Counter: a minimal G2 task-posting
   UI stakes the UX territory before competitors. Preserved as Dissent D-match-2.
   F4. [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.4-matchmaker.md#§10-Q2]

6. **Telegram backup path: Discord vs own-platform vs Matrix protocol.** Engineering dissent
   S10-D1 (F4) from LAYER-6 §13: migration-readiness escape hatch must be locked before
   Phase-2 Secure Network launch, not deferred to Phase 3.
   F4. [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.5-secure-network.md#§10-Q1]

7. **Digital portrait data-residency: Hetzner self-hosted EU-sovereign vs client-private KB
   pattern applied at person-level.** Requires legal review before Phase-2 launch. GDPR
   data-deletion caveat documented in L6 §10.2. F3.
   [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.5-secure-network.md#§10-Q2]

8. **Складчина ToS compliance: flat subscription vs usage-tiered vs free-for-contributors.**
   L7 Business Deep-Dive owns final pricing architecture.
   F3. [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-systems-integrator-§3.5-secure-network.md#§10-Q3]

9. **YouTube-analyzer build vs license: white-label existing platform + Jetix methodology
   layer vs greenfield SaaS build.** Capital-superior at G2 (white-label); may not hold at
   G3+ where moat differentiation matters. Preserved dissent in §3.6 frontmatter.
   F4. [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.6-youtube.md#frontmatter]

10. **Strategic investor round (equity) vs self-funded through Phase-3.** JETIX-PLAN §3.8
    confirms self-funded discipline through Phase-1. Phase-3+ equity decision deferred to G3.
    Preserved dissent in §3.7 frontmatter. F4.
    [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-scalability-§3.7-educational.md#frontmatter]

11. **Token jurisdiction: Switzerland vs Liechtenstein vs Germany vs Malta for Foundation
    entity.** Switzerland (Ethereum Foundation precedent) or Liechtenstein (Blockchain Act 2020)
    strongest on crypto legal clarity; Germany (BaFin) stronger on Mittelstand credibility.
    Phase-3 lawyer decides. F2.
    [src:swarm/wiki/drafts/T-layer-5-product-deep-dive-2026-04-25-investor-critic-§3.8-tokens.md#§10-Q2]

12. **Smart AI cross-lingual standardization: RU / DE / EN alignment.** Audio_529 is in
    Russian (смартфон/телефон framing). The DACH Mittelstand pitch uses EN primary (D10).
    Whether "Smart AI" concept translates cleanly to DE market without losing the analogy
    requires copywriting validation before Phase-3 external materials launch.
    F3. [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]

---

## §15.4 Preserved Dissents from Prior Cycles (Inherited — Not Re-Litigated)

These four dissents originate in KM-ARCHITECTURE-VARIANTS §12 and one from LAYER-6 §12.
They are carried forward by reference only. Philosophy-expert critic mode does NOT re-adjudicate
them — that was done in the originating cycle with Ruslan's ack on record. They surface here
because they constrain L5 design choices named in §15.2 and §15.3.

**KM-ARCHITECTURE-VARIANTS Dissent 1** (Engineering vs Systems on Phase-A UC-9 isolation level).
Phase-A policy+config layer (engineering position) vs Phase-B by-construction isolation at
first paying client onset (systems position). Both honored via sequenced trajectory. Surfaces in
§3.3 USB-C delivery architecture. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12-Dissent-1]
F4 / both positions.

**KM-ARCHITECTURE-VARIANTS Dissent 2** (Mistral 7B vs Llama 3.1-8B as offline-LLM default).
License simplicity (investor: Mistral Apache 2.0) vs community support and quality
(engineering: Llama 3.1-8B). Surfaces in §15.3 item 2 above. Resolution path: 20-query DACH
golden-set evaluation (separate task, not yet executed). [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12-Dissent-2]
F3 / both positions.

**KM-ARCHITECTURE-VARIANTS Dissent 3** (Path B vs Path C Phase-A default). This is the direct
parent of Q1 above. Investor-critic's Path B (70.7% GM yr1) vs Strategic Insight §5 Path C
(enterprise-grade, 54% GM Phase-A). Carried forward unresolved into Q1 for Ruslan ack.
[src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12-Dissent-3] F4 (Position B) / F3 (Position A).

**KM-ARCHITECTURE-VARIANTS Dissent 4** (B1 portfolio-brigadier aggregation vs full B2 migration
at G3). Mgmt-integrator: forced B2 at G3. Mgmt-scalability: B1 survives G3 with
portfolio-brigadier aggregation (defers full B2 to G4). Conditional default: B2 mandatory
at G2 first paying client onset. Does not block L5 directly but constrains §14 Tools Roadmap
Phase-2+ tooling architecture. [src:decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md#§12-Dissent-4]
F3 / both positions.

**LAYER-6 §12 Q-01 through Q-12 inherited** (Alliance Option A/B/C; payment edge-case;
Дуров timing; IP licensing; discovery format; archetype additions; D15 vs ≤€2000 legal).
Acked by Ruslan 2026-04-25 with Q-01 = Option C Hybrid acked. Remaining Q-02 through Q-12
that were not individually acked are carried into Phase-3 operational design. Brigadier
tracks ack status in `swarm/gates/AWAITING-APPROVAL-layer-6-community-deep-dive-2026-04-24.md`.
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§12]

---

## §15.5 Lock Tensions Flagged, Not Overridden

The following tensions between Locks D1-D28 and L5 direction content were observed during
drafting. Per anti-scope: philosophy-expert names them, does not resolve them. Brigadier routes
any requiring Ruslan adjudication via AWAITING-APPROVAL.

**Tension T1: D10 (English-primary external content) vs DACH Mittelstand blogger opportunity.**
§3.2 Продюсерский центр serves infobiz creators per D10 English-primary. But the Mittelstand
(§3.3 primary ICP) communicates in German. The producer center's English-language value
proposition may not land in DACH cold outreach. The tension is not a Lock violation — D10
applies to output language, not audience language. But the sales motion for Mittelstand
requires German touchpoints. Flagged for Phase 3 DACH-strategy to address explicitly.
[src:decisions/JETIX-VISION.md#D10] [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§3]

**Tension T2: D15 (self-funded discipline; no heavy spend before €200K) vs Phase-2 certification
and legal costs.** ISO 27001 (€30K-€80K), Alliance Foundation legal (≤€2000 from L6 §12 Q-12),
token legal (€100K-€500K at Phase-3). D15 scope remains ambiguous for amounts ≤€2000 (open as
L6 §12 Q-12 pending ack). For Phase-3 legal costs, the D15 lock explicitly gates to €200K+.
No override proposed; flagged for Ruslan ack at Q-12 resolution.
[src:decisions/JETIX-PLAN.md#D15] [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§12-CF-02]

**Tension T3: D18 (productization-over-hours) vs Phase-1 hourly consulting operational reality.**
Phase-1 revenue plan (JETIX-PLAN §3.1) includes 233 hourly consulting hours at €150/hr. D18
locks productized retainers as the model. The tension is temporal: D18 is the trajectory target,
not the Phase-1 constraint. The 4-pack offer bridges the two. Flagged as trajectory-vs-reality
tension; not a contradiction requiring ack. Brigadier resolves in §3.1 Consulting section prose.
[src:decisions/JETIX-VISION.md#D18] [src:decisions/JETIX-PLAN.md#§3.1]

**Tension T4: D20 (USB-C positioning: standards-level market presence) vs §3.9 Smart AI
(internal narrative label, NOT external brand).** USB-C is the external positioning metaphor;
Smart AI is the category-level internal descriptor of what Jetix builds. Potential confusion
if sales materials use both without distinction: "we build Smart AI using a USB-C standards
approach" risks conflating two distinct claim levels. Flagged for §3.9 Smart AI section prose
to maintain explicit separation. Not a Lock conflict — a communication discipline gap.
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D20] [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#Smart-AI]

**Tension T5: D26 (team 50-100 enterprise trajectory) vs bandwidth constraints in Phase-1
across multiple §3.N cells.** D26 locks the target steady-state as 50-100 team. Multiple
§3.N direction drafts (§3.3 USB-C, §3.4 Matchmaker, §3.5 Secure Network) note bandwidth
constraints on Ruslan solo in Phase-1. This is not a contradiction — D26 defines the
trajectory endpoint, and Phase-1 is explicitly solo-with-team-ready-infrastructure (D2).
The tension is that some §3.N gate timings may be optimistic given Phase-1 solo bandwidth.
Flagged; resolved by gate-sequencing discipline in §13 Evolution master table (C-07 draft).
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D26] [src:decisions/JETIX-VISION.md#D2]

---

## §15.6 F-G-R Tagging Rubric Reminder

The F-G-R framework from FPF E-5 / philosophy-expert §5.1 applies to every claim in the
L5 canonical document. Three fields per claim:

- **F (Formality):** F1 rumour → F5 tacit-but-grounded → F9 formal proof. In this document:
  F2 = preliminary assessment (not yet verified), F3 = substantive with evidence (open
  question remains), F4 = substantive with high uncertainty preserved, F5 = D-locked decision.
- **ClaimScope:** Explicit boundary — where the claim holds (phase, context, ICP segment,
  gate) and where it explicitly does NOT apply.
- **R (Reliability / Refutation-Receipt):** What would refute the claim; what would confirm it;
  where to look for evidence (path to receipt).

Per §15.2 above, all five Q1-Q5 claims carry full F-G-R triples. Per §15.3 secondary
questions, F-levels are abbreviated but present. Any claim in the canonical document without
F-G-R tagging is flagged by philosophy-expert critic as AP-PHIL-1 (claim-without-falsifiability).
[src:.claude/agents/philosophy-expert.md#§3.1]

---

## §15.7 Sequencing — What Blocks What

### Phase 3 strategic docs — blocked until Ruslan ack

| Question | Phase 3 doc blocked | Why |
|---|---|---|
| Q1 — Path A/B/C default | `ai-consulting-dach/strategy.md` | Offer structure, pricing tier, delivery model cannot be drafted without a stated default |
| Q2 — YouTube-analyzer pull-forward | `ai-consulting-dach/strategy.md` + §14 Tools Roadmap capex | If pull-forward to Phase 2, engineering budget allocation changes |
| Q5 — Token D23 Option B launch vs deprecate | Investor program materials + Phase-4 capital narrative | Investor outreach cannot be ambiguous on whether D23 is active optionality or formally retired |

### Can wait (Phase 2 execution, not Phase 3 docs)

| Question | Resolution path | Gate |
|---|---|---|
| Q3 — Smart AI D29 promotion | A/B test of outreach materials at G2; no doc blocked | G2 €200K |
| Q4 — Cohort-first vs self-serve | Phase 3 `educational-strategy.md` can declare both options with triggers; L7 pricing owns | G2→G3 |
| §15.3 items 1-12 | Operational design, Phase-2 execution, or legal counsel at appropriate gate | G2 or G3 per item |

### Inherited from LAYER-6 (carry-forward status)

Q-01 Alliance Option C — acked. Remaining L6 Q-02..Q-12: operational design, brigadier-
resolvable or Phase-2+ data-dependent. None block L5 canonical document completion; they
surface in per-direction Phase-3 execution. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§12]

---

*Drafted by philosophy-expert (mode: critic), cell C-12, cycle cyc-layer-5-product-deep-dive-2026-04-25.
Draft status only. Awaiting brigadier §5.5.5 provenance gate + Ruslan HITL review before
promotion to canonical layer in decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md.*
