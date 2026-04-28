---
title: "Strategic Layer — Landscape Research Catalogue (Etap 2 of Генеральная чистка)"
date: 2026-04-28
type: research-output
phase: research-phase-1-landscape
author: Cloud Code (server) — direct integrator-mode synthesis
purpose: >
  Catalogue strategic-document types found across the Jetix corpus
  (14 consultant cards + 391 books в raw/books-md/ + 27 research compilations
  + Strategic Insight files + FUNDAMENTAL Vision LOCKED + Wave A candidate-parts-merged).
  Used as input for Phase 2 filtering (8 criteria → 5-8 PROPOSE types).
F: F2
G: "Strategic Layer scoping for Etap 2; not constitutional. Subject to Ruslan ack."
R: "Refuted if Ruslan walkthrough finds <70% of types in the catalogue traceable to a primary source in the corpus."
inputs:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§1, §6, §7, §8)
  - design/JETIX-FPF.md (skim — IP-1..IP-8, A.14, B.3, F.6 anchors)
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/{product-management-cagan-shape-up,capital-allocation-antifragility,stoic-epistemic,compounding-engineering,levenchuk-shsm-fpf}.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md (§1-§2 Parts 1-10)
  - decisions/STRATEGIC-INSIGHT-* (5 files — exemplars)
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md
  - decisions/JETIX-PLAN.md
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md (skim — Lock format reference)
  - raw/books-md/INDEX.md (skim — corpus orientation)
  - raw/books-md/{pm,mgmt,investing,philosophy-science,philosophy,meta}/ (selective listings)
honest_limits:
  - >
    Memory files declared in brief at `C:\Users\49152\.claude\projects\C--Users-49152-Desktop-jetix-os\memory\`
    are ON THE WINDOWS CLIENT, not on the Linux server. Only `MEMORY.md` + `feedback_no_api_keys.md`
    exist locally. Substituted via inference from STRATEGIC-INSIGHT-* files + FUNDAMENTAL §1 + §7 +
    candidate-parts-merged.md content, which transitively encode the constraints those memories carry
    (sole-strategist; AI-does-not-strategize; hybrid framework; IndieHackers channel; Top Lists factory
    direction; private-library leverage).
  - >
    LJ post corpus (49 posts in raw/books-md/systems/) sampled via 3 research compilations
    (~286K words combined) per Wave B levenchuk card §1 declaration — direct file-by-file LJ
    reads not executed at this scope. Sufficient for type extraction; not sufficient for IP-N
    citation precision.
  - >
    Books-md selective: PM (3) + investing (5) + philosophy-science (4) read at structure level via
    consultant cards; mgmt (`drucker-effective-executive` etc.) skimmed via INDEX titles only;
    biology / complexity / engineering-foundations excluded from this pass (low signal for strategic
    doc types).
---

# Strategic Layer — Landscape Research Catalogue

## §0 What this document is (and is not)

**This is** a catalogue of strategic-document **types** present in the Jetix corpus —
not a proposal of which to adopt (Phase 2), not a hierarchy/cadence definition (Phase 3),
and not content (next sprint).

**Each entry below** captures: canonical name + 1-paragraph description ("what it does") +
origin framework + typical user profile + cadence-in-source + concrete corpus references.

**Ordering:** roughly from constitutional / system-identity layer down through
operating-cadence layer to per-artifact layer. Not a hierarchy claim — that is Phase 3.

---

## §1 Method

Three extraction sweeps:

1. **Bottom-up from corpus** — what strategic-doc types appear as concrete files in
   `decisions/`, `design/`, and `swarm/wiki/cycles/`. These are types Ruslan has
   actually authored or had drafted; they have proven authoring-cost and proven owner-fit.

2. **Top-down from frameworks** — what doc types each consultant card explicitly
   prescribes for the Foundation parts it anchors. PM card → OKRs, Shape Up pitches,
   opportunity-solution-tree notes; Capital card → owner-earnings memos, margin-of-safety
   audits; Stoic-Epistemic card → falsifiable claims, paradigm-bridge notes; Compounding
   card → DRR ledger, Error→Rule→Skill records; Levenchuk card → typed-edge dependency
   manifests, F-G-R-tagged claims.

3. **Cross-reference and dedup** — same function under different names → merge with
   primary canonical naming. Where corpus and framework both name a type, prefer corpus
   naming + cite framework as origin.

**Anti-cargo-cult guardrail (per brief §4):** every type below cites a concrete corpus
source. Types that exist only "in the literature" without a corpus anchor are flagged
as `corpus-anchor: missing` for Phase 2 filtering.

---

## §2 Catalogue (15 strategic document types)

### Type 01 — Constitutional / Foundation Vision

**1-paragraph description.** A constitutional declaration of what the system *is*,
sector-agnostic, person-agnostic, business-agnostic. Defines: main principle (what
the system is FOR), use cases (what it must DO), anti-scope (what it must NEVER do),
roles + agency model, evolution model. Status semantics: `LOCKED` after Ruslan ack,
revisions are vertical-axis (semi-annual+, architectural review required per FUNDAMENTAL
§8.6). Other strategic docs reference but never contradict.

**Origin framework.** Levenchuk FPF (constitutional-document pattern, IP-3 artifacts-over-
conversations); Anthropic Constitutional AI (FUNDAMENTAL §6 anti-scope as Jetix
constitution per Wave B manifest §2 Part 6); Buffett shareholder-letter genre
(owner-mindset, durable principles).

**Typical user profile.** Founder/Architect (FUNDAMENTAL §7.1) — "professional
intellectual worker" with "long-horizon strategic ambitions." Specifically the
single-locus authority who can ack such a document in the first place.

**Cadence in source.** LOCKED → revisable only on architectural review trigger
(pattern accumulation across cycles, external best-practice discovery, incident-driven,
NOT convenience-driven per FUNDAMENTAL §4.7). FUNDAMENTAL §8.2 declares
"semi-annual major release" orientation for foundation evolution. Empirically:
Jetix has produced this type **once** (LOCKED v1.0, 2026-04-27) — N=1 cadence sample.

**Example references.**
- `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (the canonical exemplar — 2624 lines, 30K words, LOCKED)
- `design/JETIX-FPF.md` (3758 lines — adjacent constitutional-spec layer, see Type 02)
- `decisions/JETIX-VISION.md` (predecessor; superseded by FUNDAMENTAL — 28-Locks foundation)
- Wave B manifest §2 (matrix declaring this type as "Foundation declaration" referenced by every other Foundation part)

---

### Type 02 — Constitutional Specification (FPF-class)

**1-paragraph description.** A formal specification document encoding the ontological
+ procedural primitives the system commits to (typed roles, lifecycle states, decision
classes, trust-tag calculus, onboarding cycles). Distinct from Type 01: Type 01 declares
what the system *is*; Type 02 declares the *vocabulary and protocols* the system uses
to talk about itself. Inline patterns are stable identifiers (IP-N, A.14, B.3, F.6)
that other artifacts cite. Often co-evolves with an upstream community spec (FPF
GitHub).

**Origin framework.** Levenchuk FPF — primary; ailev/FPF GitHub upstream + JETIX-FPF
Jetix-adapted layer. Adjacent: ISO 15288 / OMG Essence kernels (referenced indirectly
via FPF research compilations).

**Typical user profile.** Founder + a specialist FPF-Steward function (per IP-4, audit
quarterly). External community contributors if upstream sync is opted into (per D27
Fork-and-merge).

**Cadence in source.** Continuously updated upstream; pulled selectively per Foundation
release. Internally: revisions tracked via line-level pattern IDs so downstream artifacts
keep working. Concrete cadence in Jetix: Wave B manifest declares quarterly check
against ailev/FPF for new patterns.

**Example references.**
- `design/JETIX-FPF.md` (3758 lines, 14 sections; IP-1..IP-8 + A.14 + B.3 + F.6 + 8 true alphas)
- `raw/external/ailev-FPF/FPF-Spec.md` (62K lines, 300+ patterns — upstream)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` §2 (canonical-source enumeration)

---

### Type 03 — Locks Ledger (D-series irreversible decisions)

**1-paragraph description.** Append-only ledger of constitutionally-irreversible
decisions. Each Lock declares: what is locked, when, the reasoning chain, what would
have to change to unlock, and which downstream artifacts depend on it. Locks are
F-tagged (typically F4-F5 per FPF B.3) and serve as the substrate against which
all other strategic docs are checked (see PM card Tradeoff D — every quarterly OKR
authoring ritual must pass a Lock-compliance check).

**Origin framework.** Levenchuk FPF B.3 (trust calculus + verification primitives);
Anthropic CAI (governance-gate + irreversibility discipline); Capital allocation
margin-of-safety (over-engineer where downside is unrecoverable per Capital card P2).

**Typical user profile.** Founder-only authority on Lock creation/reversal; agents may
draft candidate Locks for ack. FPF-Steward (IP-4) audits Lock coherence quarterly.

**Cadence in source.** Event-driven (appears when a decision warrants Lock status);
cadence-of-existence is append-only with addenda. Jetix corpus shows D1-D29 + 4
ADDENDUMs over ~2 months, suggesting ~1-2 new Locks per week during architecture
phases, dropping toward zero in execution phases.

**Example references.**
- `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md`
- `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`
- D1-D29 dispersed across `decisions/JETIX-VISION.md`, `decisions/JETIX-PHILOSOPHY.md`, `decisions/JETIX-PLAN.md`
- Wave B manifest cites D-Lock anchors per Foundation Part (e.g., Part 1 cites D25 — git-as-system-state; Part 2 cites D28 — anchor-mandatory ingest)

---

### Type 04 — Founder-Specific Overlay Vision

**1-paragraph description.** A second-layer Vision Document that overlays the
Constitutional Foundation (Type 01) with current-situation specifics: which archetype(s)
the founder occupies (per FUNDAMENTAL §7.1.1 11-archetype taxonomy), which market
segment, which positioning, which Phase 1 horizon. By construction this overlay is
*replaceable* without touching Type 01 — if the founder pivots niche, only this layer
changes.

**Origin framework.** Two-layer pattern explicit in FUNDAMENTAL §0 ("Двуслойный — Layer 1
+ Layer 2 RUSLAN-LAYER"); Levenchuk IP-2 (bounded context — generic Foundation
declares vocabulary, instance binds it); Cagan Inspired Ch. 1 (compelling product vision
adapted per company stage).

**Typical user profile.** Founder authoring for own use; possibly mentor/advisor as
secondary audience. NOT public-facing.

**Cadence in source.** Annual baseline + event-driven amendments when Phase transitions
or major positioning shifts occur. Jetix-specific binding (RUSLAN-LAYER) noted as next
step after FUNDAMENTAL LOCKED in cross-refs.

**Example references.**
- `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` (the planned overlay — referenced from FUNDAMENTAL cross-refs as "Layer 2")
- `decisions/JETIX-VISION.md` (predecessor — 28-Locks foundation; partially serves overlay function pre-split)
- `decisions/JETIX-PHILOSOPHY.md` (D13 Closed core / Open surface and D11 Investment-fund philosophy — Ruslan-specific positioning)

---

### Type 05 — North Star / Definition-of-Tomorrow (DoT)

**1-paragraph description.** A long-horizon directional pull document: "where we are
going" articulated in compelling, evocative terms (Cagan: "Compelling Product Vision");
distinct from Constitutional Vision (Type 01) which is timeless and from Phase Plan
(Type 08) which is calendared. North Star answers: "if everything goes right, what
does the world look like 3-10 years out, and what is *our* role in it?" Functions as
the gravity well that all quarterly OKRs and project bets pull toward.

**Origin framework.** Cagan Inspired Ch. 26 (compelling product vision); Doerr OKRs
(O = qualitative + aspirational anchor); Naval Almanack ("specific knowledge" filter
+ long-horizon judgment); Левенчук writing-as-thinking IP-7 (the document IS the
strategic thinking, not a record of it).

**Typical user profile.** Founder primary author; mentor/co-founder as occasional
co-thinker; partners/clients as later audience (sanitized version).

**Cadence in source.** Annual review with quarterly soft updates; major rewrite at
Phase transitions (Phase 1 → Phase 2 in Jetix terms). Brief explicitly notes
"JETIX-NORTH-STAR deferred 27.04 morning — DoT page integration; needs 5-chat
methodology" → cadence here is "rare + multi-session", not "weekly capture."

**Example references.**
- Brief §1 explicitly names JETIX-NORTH-STAR as deferred Strategic Layer artifact
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (proto-North-Star — voice brainstorm
  capturing 6-pillar roadmap; tagged `state: draft (awaiting review)`; format heavy on
  pillars + concept fixings)
- Cagan's "compelling product vision" pattern (referenced in PM consultant card §4 P4)

---

### Type 06 — Strategic Insight Memo

**1-paragraph description.** A single-concept crystallization document that captures
*one* large strategic idea in depth — origin, evidence, implications, paths, open
questions, anti-scope. Often born from voice brainstorm + research-trigger combination.
Status field tracks lifecycle: `draft-awaiting-discussion` → `accepted` (potentially
promoted to Lock or new direction) → `deferred-phase-2-plus` → `archived`. Five concrete
exemplars exist in Jetix corpus.

**Origin framework.** Levenchuk IP-7 writing-as-thinking (the document IS the thinking);
Marks Oaktree memo style (single-thesis essays); Capital-allocation second-level
thinking (Marks P3 — first-level "X is true" → second-level "what has the system NOT
priced in?"). Anthropic engineering-blog format (single-topic deep-dive, simplicity-
transparency-trust).

**Typical user profile.** Founder author + Cloud Cowork / Cloud Code synthesis support
(structuring + drafting per AI-augmented IP-7); mentor as possible discussant; agents
as proposers but never deciders (per memory `feedback_ai_does_not_strategize`).

**Cadence in source.** Event-driven — fires when a concept "wants to be written down."
Jetix corpus: 5 exemplars over ~10 days (April 24-26), suggesting ~1-2 per week during
high-insight periods, sparse otherwise. Lifecycle: many enter `deferred-phase-2-plus`
(M&A, Arbitrage Traffic, AI-BIOS, AI-Psy-Led, VISION-NEXT) before potential reactivation.

**Example references.**
- `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` (canonical structure: TL;DR + historical pattern + paradigm fit + 24-Locks reconciliation + 3 implementation paths + open questions + anti-scope + immediate actions)
- `decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md`
- `decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md`
- `decisions/STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md`
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (variant — closer to North Star scaffold than single-thesis insight, but shares the Strategic Insight format DNA)

---

### Type 07 — Direction / Pillar Card

**1-paragraph description.** An ongoing direction (active or deferred) — a *standing*
strategic line of work, distinct from a finite project. Carries: thesis, hypothesis
chain, current bets, gating predicates (when active vs. when deferred), responsible
parties, capital/attention budget, dependencies on Locks or other Directions.
Differentiates from Strategic Insight (Type 06) by being a long-running container vs.
a one-shot crystallization. Memory fragment from brief: "Top Lists Partner Factory
ACTIVE Phase 1+; AI-BIOS Moment Phase 2+ deferred; M&A Phase 2+ deferred…" — six
concrete instances.

**Origin framework.** Cagan empowered-team mission ("each agent role carries a
*mission*, not a task list" per PM card P4); Buffett "circle of competence"
(directions inside circle stay active; outside → deferred); Marks portfolio thesis
(per Capital card §3 + memos referenced in card §4); Shape Up "tracks" (the cycle
+ cooldown + R&D-track structure underpinning the betting table).

**Typical user profile.** Founder defines + activates/deactivates Directions; mini-swarm
or dedicated agent operates within an active Direction (per KM MVP `/project-bootstrap`
mini-swarm pattern); mentor consults at quarterly review.

**Cadence in source.** Quarterly review for activation/deferral; status changes are
event-driven within quarter. Jetix corpus suggests N=6 named Directions live in memory
(per brief §1 "6 Strategic Insights ACTIVE+deferred" framing — but "Strategic Insights"
naming there overlaps with Type 06; the underlying entities are Directions in our
taxonomy).

**Example references.**
- `decisions/STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md` (named "DIRECTION" in title — concrete corpus instance of Type 07; tagged `state: deferred-phase-2-plus`)
- `decisions/STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md`
- `directions/_active/` directory (referenced from CRM CLAUDE.md strategy-hooks section)
- Brief §1 enumerated list (Top Lists / AI-BIOS / VISION-NEXT / AI-Psy-Led / M&A / Arbitrage Traffic)

---

### Type 08 — Phase Plan / Multi-Quarter Plan

**1-paragraph description.** A multi-quarter execution plan organized by *phase* (Jetix
exemplifies: Phase 0 → Phase 1 → Phase 2). Each phase declares: objectives, top-priority
actions, content/marketing pipeline, budget/resources, milestones, and **exit criteria**.
Distinct from Quarterly Plan (Type 09) by horizon (multi-quarter) and by framing (phase
exit instead of period-end). Includes transition sub-plan (e.g., "Phase 1 → Phase 2 €50K
gate" in Jetix-corpus).

**Origin framework.** Watkins *First 90 Days* (phase-of-tenure framing); Grove HOM
(production phases + leverage); Ries *Lean Startup* Build-Measure-Learn at company
strategic-direction zoom (per PM card P5 Tradeoff). Cagan *Transformed* enterprise
phasing.

**Typical user profile.** Founder + ops lead. Phase Plan is the document mentor/advisor
most often reads when assessing "where is the company right now."

**Cadence in source.** Authored once per phase; reviewed quarterly inside phase; rewritten
at phase transition. Jetix-corpus: `decisions/JETIX-PLAN.md` declares Phase 0 / Phase 1 /
Phase 1→2 transition with full action lists + exit criteria — single canonical exemplar.

**Example references.**
- `decisions/JETIX-PLAN.md` (the canonical Phase Plan; structure: objectives + actions + pipeline + budget + milestones + exit criteria, repeated per phase)
- `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` (closely related; cross-phase plan)

---

### Type 09 — Quarterly Plan / OKRs

**1-paragraph description.** Quarterly objective + key-results document. O = qualitative
+ aspirational anchor (1-3 max); KRs = measurable + time-bound + 0–1.0 scored.
Mandatory step in authoring: Lock-compliance check (per PM card Tradeoff D — a KR that
implicitly conflicts with a Lock is invalid). Cross-references: each active project
points at ≥1 parent OKR; each Direction (Type 07) is checked against current quarter's
OKRs for capital-allocation alignment.

**Origin framework.** Doerr *Measure What Matters* (canonical OKR — Superpowers 1-4 per
PM card §4 P6); Grove HOM (Doerr's lineage; OKRs invented at Intel under Grove);
adjacent: Levenchuk IP-5 alpha state machine (KR completion = state transition).

**Typical user profile.** Founder authoring (sole strategist per memory); agents provide
*structured extraction support* in writing-support mode (extractions + alternatives;
owner composes per Cagan empowered-team principle). Mentor reviews at quarter open and
close.

**Cadence in source.** Quarterly — standard 90-day cycle. PM card §4 P6 prescribes
"the quarterly OKR review as a mandatory cadence slot, distinct from the weekly review
ritual." Jetix-corpus: not yet authored (gap explicitly named in PM card §6 OQ-5 —
"no current Foundation artefact encodes the quarterly OKR authoring workflow with Lock
gate").

**Example references.**
- `raw/books-md/pdm/doerr-measure-what-matters-2018.md` (canonical reference)
- PM consultant card §4 P6 + Tradeoff D (Lock-compliance integration)
- Wave A candidate-parts-merged.md §2 Part 9 (Owner Interaction Scaffold) — declares quarterly OKR slot as required

---

### Type 10 — Bet Pitch / Shape-Up Pitch

**1-paragraph description.** A *shaped* time-boxed bet declaration: appetite (1 week / 2
weeks / 6 weeks / R&D-mode) declared up-front; problem framed at the appropriate
elevation (raw idea is unshaped; pitch is shaped); solution sketched at the right
fidelity (rabbit-holes addressed; rabbit-holes flagged); circuit-breaker rule
("if it overruns appetite, it does NOT get an extension — it gets re-shaped or killed"
per PM card §4 P2). The Bet Pitch *precedes* the project; it is what gets *bet on*
at the betting-table ritual.

**Origin framework.** Singer *Shape Up Basecamp 2019* — primary; Doerr OKRs as parent
linkage; Ries Lean Startup MVP-but-only-at-strategic-zoom (per PM card P5 Tradeoff —
strategic zoom = "should we build in this space at all?"; Bet Pitch = "given we've
decided to build, ship within appetite"). Capital card P5 Munger inversion ("design
against failure modes, not toward success cases" — the rabbit-hole flagging in a
Shape Up pitch IS the inversion practice at a project zoom).

**Typical user profile.** Founder + AI-augmented shaping (`shape-it` command pattern
implied); agents draft pitch fragments under owner direction; betting-table ritual
itself owner-only.

**Cadence in source.** Per 6-week cycle (Singer's default) + cooldown 2 weeks. Pitches
authored continuously; betting decisions clustered at cycle boundaries.

**Example references.**
- `raw/books-md/pm/singer-shape-up-basecamp-2019.md` (canonical reference)
- `swarm/wiki/_templates/project-*/` (existing Jetix project templates — already include
  `appetite:` discussions per PM card §6 OQ-1, which flags appetite-field as a
  materialisation gap → Bet Pitch is the upstream artifact to a project)
- PM card §4 P2 + §6 OQ-1 + OQ-2 (canonical statement of Shape Up application to Foundation)

---

### Type 11 — Project Brief

**1-paragraph description.** Per-project initiation document. Frontmatter declares: type
(`consulting | research | product | bets`), priority (P1-P4), status, parent OKR(s)
(per Type 09), parent Direction (per Type 07), client (per `--client=<id>` namespace),
appetite (per Type 10 Shape Up). Body: outcome (distinct from deliverables — per PM
card P1 Outcome over Output), opportunities addressed (per Torres CDH P3 — at least
one named customer pain-point), milestones, exit criteria. Existing Jetix infrastructure
already provides templates per project type via `/project-bootstrap`.

**Origin framework.** Cagan Inspired empowered-team brief; Torres CDH opportunity-
solution-tree linkage; Shape Up appetite imported; PMBOK 12 principles for *quality*
discipline (PM card Tradeoff C Resolution — adopt PMBOK Principles 8 + 9 for quality
+ risk, *not* for scope-negotiation).

**Typical user profile.** Founder ack on project initiation; project mini-swarm or
dedicated agent operates the brief; client (for consulting type) is read-audience for
sanitized variant.

**Cadence in source.** Event-driven (per project initiation); status updates per cycle
or event; closure via `/project-archive`. Jetix corpus shows 8 active projects per
CLAUDE.md, suggesting active steady state ~5-10.

**Example references.**
- `swarm/wiki/_templates/project-consulting/` (9 stub files per CLAUDE.md KM MVP section)
- `swarm/wiki/_templates/project-research/`, `project-product/`, `project-bets/`
- `.claude/config/project-types.yaml` (declarative templates)
- PM card §6 OQ-2 (outcome: field gap in current templates)

---

### Type 12 — Compound Cycle Retrospective / DRR Ledger Entry

**1-paragraph description.** Append-only per-cycle compound-step output: Decision /
Reasoning / Result / Review. Captures one rule-candidate (Error→Rule promotion entry
point) with `rule_slug`, `version`, `ratio: {hits, misses}`, `expected_evolution`
(cycle_10 / cycle_50 / cycle_200 forecasts). Per-agent file: `agents/<expert>/strategies.md`.
Brigadier maintains swarm-level patterns; each domain expert maintains domain-specific.
The compound step itself is gated by Foundation Part 6 (provenance gate refuses
to persist entries lacking `sources[]`).

**Origin framework.** Compounding Engineering (Klaassen / Cherny / Shipper — primary,
per CE consultant card P1-P3); Anthropic self-rewriting tool-description agent (-40%
task time evidence per CE card P1). Adjacent: Левенчук IP-7 writing-as-thinking;
Buffett owner-earnings (the methodology library is owner-earnings of the Foundation
per Capital card P1).

**Typical user profile.** Agents author DRR entries during compound phase; brigadier
writes cycle-close swarm-level DRR; founder reviews periodically (rule-promotion to
Skill in `wiki/` Methodology Library is gated).

**Cadence in source.** Per-cycle (Plan/Work/Review/Compound 40/10/40/10 ratio per CE
P1). Jetix-corpus: `agents/<expert>/strategies.md` already operational (per CE card §3
Foundation Part Mapping).

**Example references.**
- CE consultant card §4 P1-P3 (canonical statement)
- `agents/<expert>/strategies.md` (existing Jetix files per CLAUDE.md per-agent memory section)
- `decisions/MASTER-SYNTHESIS-HOW-TO-BUILD-BEST-SWARM-2026-04-22.md` §1.5, §1.10, §2.1 (compound ledger and provenance gate definition)

---

### Type 13 — Investment / Capital-Allocation Memo

**1-paragraph description.** A capital-allocation decision memo: where to deploy the
scarcest resource (Phase 1: founder time/attention/cognitive bandwidth; Phase 2+: also
money + headcount). Format: thesis (what's the bet); circle-of-competence check (Buffett
P1 — do we have predictive judgment here); margin-of-safety (Graham P2 — over-engineer
where downside is unrecoverable); inversion check (Munger P5 — what would make this
fail?); barbell positioning (Taleb P6/P7 — is this the safe pole or the convex pole?);
exit / kill predicate. Distinct from Bet Pitch (Type 10) by zoom: Memo is "should we
allocate to *this category* at all?"; Bet Pitch is "given we have, ship this specific
shaped piece."

**Origin framework.** Capital allocation consultant card P1-P7 — primary; Marks Oaktree
memo style; Buffett shareholder letters; Taleb Antifragile. Adjacent: Cagan empowered-
team mission (the memo is the mission statement at allocation level).

**Typical user profile.** Founder + investor-expert agent in proposal mode; mentor
discussant at significant allocation decisions (e.g., taking on consulting client →
allocates time/energy → memo trade-off captured).

**Cadence in source.** Event-driven (significant allocation decisions); quarterly
roll-up review of all active allocations (alignment with Type 09 OKRs).

**Example references.**
- Capital allocation consultant card §4 P1-P7 (canonical statement)
- `raw/books-md/investing/buffett-shareholder-letters-collection.md` (genre exemplar)
- `raw/books-md/investing/marks-most-important-thing-illuminated-2013.md` (memo genre)
- `raw/books-md/investing/taleb-antifragile-2012.md` Ch.11 Seneca's Barbell (positioning structure)

---

### Type 14 — Stakeholder / Mentor Briefing Pack

**1-paragraph description.** A read-audience-shaped digest packaging: current Phase
status, current OKRs progress, top 3 active Bets, recent Locks (if mentor is inner
stakeholder per FUNDAMENTAL §7.4 T3 tier), 1-3 named open questions for which mentor's
input is sought. Distinct from internal docs by being **filtered** (not full-context
dump) and **specific-question-anchored** (the mentor knows exactly what response is
sought). Brief §1 explicitly notes "Mentor briefing pack deferred 27.04 evening —
context для Антона" → exists as identified gap.

**Origin framework.** Cagan Inspired empowered-team principle (mentor is "advisor", not
decision-maker — same role-discipline as agent per IP-1); Naval Almanack specific-
knowledge filter (mentor consulted on what only they have specific knowledge in);
Anthropic Building Effective Agents (simplicity-transparency-trust — same triad
applied to human-mentor interaction).

**Typical user profile.** Founder author; mentor (1-3 named individuals like the
"Антон" in brief) read-audience; agents draft sections under owner direction (extraction
+ filtering, owner composes final).

**Cadence in source.** Event-driven (per mentor call) + per-mentor cadence
(weekly / monthly / quarterly depending on relationship). Jetix-corpus: deferred — no
current exemplar.

**Example references.**
- Brief §1 explicit deferral note
- FUNDAMENTAL §7.4 T3-tier access (inner stakeholder)
- Naval Almanack specific-knowledge concept (Stoic-Epistemic card §3 boundary discussion)

---

### Type 15 — Strategic Reflection / Writing-as-Thinking Note

**1-paragraph description.** A periodic founder-only reflection artifact. Captures
recent decisions made, pattern observed, hypotheses forming, anxieties surfacing,
adjustments to Direction or OKR. The document IS the thinking (per Levenchuk IP-7) —
not a record of thinking that happened elsewhere. Format flexible (often diary-prose
or bulleted lattice); audience self-only; status semantic: never `LOCKED`, always
flowing. Acts as upstream feedstock: insights here may graduate into a Strategic
Insight Memo (Type 06), Direction (Type 07), or Lock candidate (Type 03).

**Origin framework.** Levenchuk IP-7 (writing-as-thinking, primary); Holiday Daily
Stoic (discipline of perception via daily reflection); Munger latticework habit
(multi-discipline lookup applied to own decisions).

**Typical user profile.** Founder-only; never agent-drafted (per memory `feedback_ai_does_not_strategize`
+ Levenchuk IP-7 anti-pattern warning: "если и сам текст пишет LLM — исчезает 'мышление
письмом' как когнитивный процесс" per LJ 1769411 cited in Levenchuk consultant card §4 P2).

**Cadence in source.** Weekly or daily — owner-cadence-driven. Jetix-corpus: voice-memo
pipeline produces transcripts that can serve as upstream signal, but the *reflection*
artifact (vs. the transcript) is rare in `decisions/`. `daily-log/` exists but operates
at logging zoom, not reflection zoom.

**Example references.**
- `daily-log/` (adjacent — captures activity, not reflection)
- Levenchuk consultant card §4 P2 ("Artifacts over conversations" + IP-7 anti-pattern warning)
- PM consultant card P3 Tradeoff B Resolution (CDH external + IP-7 internal as layered composition)
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (a *fragment* — voice brainstorm structured into doc, sits between Reflection and Strategic Insight)

---

## §3 Cross-cutting observations

### 3.1 Type relationships (high-level — formalised in Phase 3)

A first sketch of dependency direction (read: "X depends on Y" = X must be coherent
with Y; not "X is constituent-of Y" per FPF A.14):

```
Type 01 Foundation Vision (LOCKED)
   ├─ Type 02 Constitutional Spec (FPF) — co-evolves
   ├─ Type 03 Locks Ledger — operates inside §6 anti-scope of Type 01
   └─ Type 04 Founder Overlay — overlays Type 01

Type 05 North Star — pulls from Type 04 + Type 01 §1 use cases
   ├─ Type 06 Strategic Insight — feeds into / promotes from
   ├─ Type 07 Direction — multiple, each pulls from North Star
   └─ Type 08 Phase Plan — calendarises North Star
       ├─ Type 09 Quarterly Plan / OKRs — calendarises Phase
       │   ├─ Type 10 Bet Pitch — selected at quarterly betting table
       │   │   └─ Type 11 Project Brief — instantiates Bet
       │   │       └─ Type 12 DRR — per-cycle compound learning
       │   └─ Type 13 Capital Memo — memorialises allocation decisions
       └─ Type 14 Stakeholder Brief — synthesises status for mentor
   └─ Type 15 Strategic Reflection — upstream feedstock to all of the above
```

This sketch is **provisional**. Phase 3 will produce a typed dependency graph (FPF A.14
edges) + cadence calendar.

### 3.2 Coverage of FUNDAMENTAL §1 12-categories (Cat A-L)

| FUNDAMENTAL Cat | Most-relevant types | Notes |
|---|---|---|
| **A — Strategic Management** | 01, 04, 05, 07, 08, 09, 13 (7 types directly serve A) | UC-A.4 decisions tracking → Type 03 Locks; UC-A.1 multi-level hosting → Types 01/04/05/08/09 stack |
| **B — Information Lifecycle** | (Foundation Part 2 + Part 3 territory; minimal Strategic Layer overlap) | Not in Strategic Layer scope per brief |
| **C — Self-Improvement** | 12, 15 | DRR + Reflection as compound substrate |
| **D — Project & Resource Mgmt** | 10, 11, 13 | Bet → Project + Capital allocation |
| **E — Agent Swarm Operations** | (Foundation Part 4 territory; minimal overlap) | Out of Strategic Layer scope |
| **F — AI Augmentation Continuity** | (Foundation Part 5 territory; minimal overlap) | Out of Strategic Layer scope |
| **G — Multi-channel Access** | (Foundation Part 2 + Part 9 territory) | Out of scope |
| **H — Foundation & Reliability** | 02, 03 | Constitutional spec + Locks |
| **I — Health & Audit** | (Foundation Part 8 territory) | Out of scope |
| **J — Daily Operations** | 15 | Reflection captures daily-zoom strategic signal |
| **K — CRM / Network** | 14 | Stakeholder brief is read-side of CRM |
| **L — External Integrations** | (Foundation Part 10 territory) | Out of scope |

**Strategic Layer concentrates in Cat A** (7 types directly), with secondary presence
in C / D / H / J / K. Foundation Layer (Parts 1-10) covers B / E / F / G / I / L —
this confirms Strategic Layer is *complementary* to Foundation, not overlapping.

### 3.3 Honest declarations / uncertainty flags

- **Type 05 North Star vs. Type 04 Founder Overlay** — the boundary is **fuzzy**. The
  "VISION-NEXT-STRATEGIC-HORIZON" exemplar shows traits of both; multi-chat methodology
  (memory `methodology_multi_chat_review_for_critical_docs`) is recommended for North
  Star authoring → suggests North Star is heavier than Founder Overlay. Phase 2 needs
  to decide whether to keep both as separate types or merge.

- **Type 06 Strategic Insight Memo vs. Type 07 Direction Card** — the corpus uses the
  prefix `STRATEGIC-INSIGHT-` for both single-thesis crystallizations (AI-BIOS, AI-Psy-Led)
  and ongoing direction declarations (M&A, Arbitrage Traffic). The *content shape* differs
  (one-shot vs. running container) but the *naming convention* conflates them. Phase 2
  should decide whether to formalise the split or keep one type with `lifecycle:` field.

- **Type 14 Mentor Brief** — flagged as deferred in brief but no exemplar in corpus.
  Should it exist as a structural template, or as a generated-on-demand artifact from
  other docs? Phase 2 + Phase 3 to address.

- **Type 15 Strategic Reflection** — risk of overlap with `daily-log/` infrastructure.
  Phase 2 should check whether daily-log already serves this function vs. whether a
  *separate* reflection-zoom artifact warrants its own template.

- **Memory file gap (declared in frontmatter `honest_limits`)** — the Windows-side
  memories named in brief were inferred from STRATEGIC-INSIGHT-* + FUNDAMENTAL §7 +
  candidate-parts-merged.md content. Specifically the constraints encoded in those
  memories (sole-strategist; enterprise baseline always; 5-chat methodology for
  critical docs; AI does not strategize; private-library-as-leverage moat; IndieHackers
  channel; Top Lists factory) all surface in the on-disk corpus. The substitution is
  *defensible* but Ruslan should verify in walkthrough.

### 3.4 Types deliberately NOT included

- **Customer Persona / ICP doc** — already exists at `decisions/JETIX-PHILOSOPHY.md` and
  Notion ICP page (CLAUDE.md key Notion IDs). Not Strategic Layer; Operational Layer.
- **Marketing / Content Pipeline doc** — operational, not strategic.
- **Hiring Plan / Org Chart** — Phase 1 solo-founder context (per memory
  `feedback_no_solo_founder_downgrade` and FUNDAMENTAL §7.1.1 Founder = single locus
  authority); will materialise in Phase 2+. Out of current scope.
- **Risk Register** — typically lives inside Phase Plan (Type 08) and Project Brief
  (Type 11) sections rather than as standalone type. Could be promoted later if signal
  warrants; not in current cohort.
- **Pre-Mortem doc** (Klein 2007 method) — useful but better as a *section* in
  Bet Pitch (Type 10) and Capital Memo (Type 13) than a standalone strategic type.
- **AWAITING-APPROVAL Gate Packet** — gate mechanism, not strategic content; lives in
  Foundation Part 6 territory (governance).
- **Periodic Audit Report** — Foundation Part 8 territory (health monitoring).

---

## §4 Provenance summary

| Type | Primary corpus anchor | Primary framework anchor |
|---|---|---|
| 01 Foundation Vision | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` | Levenchuk FPF + Anthropic CAI + Buffett genre |
| 02 Constitutional Spec | `design/JETIX-FPF.md` + `raw/external/ailev-FPF/FPF-Spec.md` | Levenchuk consultant card §1-§7 |
| 03 Locks Ledger | `decisions/LOCKS-D25-D28-ADDENDUM-*` + D-series | FPF B.3 + CAI + Capital P2 |
| 04 Founder Overlay | `decisions/JETIX-VISION-OF-SYSTEM-2026-04-27.md` (planned) | FUNDAMENTAL §0 two-layer pattern |
| 05 North Star / DoT | brief §1 deferred + `VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` proto | Cagan Ch.26 + Doerr O + Naval |
| 06 Strategic Insight | 5 `STRATEGIC-INSIGHT-*` exemplars | IP-7 + Marks memo + CAI engineering-blog format |
| 07 Direction / Pillar | M&A + Arbitrage Traffic exemplars | Cagan empowered + Buffett circle + Marks portfolio |
| 08 Phase Plan | `decisions/JETIX-PLAN.md` | Watkins + Grove + Ries strategic-zoom |
| 09 Quarterly OKRs | (gap — PM card §6 OQ-5) | Doerr MWM canonical |
| 10 Bet Pitch | `swarm/wiki/_templates/project-*/` adjacent | Singer Shape Up + Munger inversion |
| 11 Project Brief | `swarm/wiki/_templates/project-*/` (4 types) | Cagan + Torres + PMBOK 12 principles (quality only) |
| 12 DRR / Compound Cycle | `agents/<expert>/strategies.md` operational | CE Klaassen P1-P3 + IP-7 |
| 13 Capital Memo | (gap — referenced via investing books genre) | Capital card P1-P7 (Buffett/Munger/Marks/Taleb) |
| 14 Mentor Brief | (gap — brief deferral) | Cagan empowered + Naval specific knowledge + CAI triad |
| 15 Strategic Reflection | `daily-log/` adjacent + IP-7 corpus | Levenchuk IP-7 primary |

**5 of 15 types currently have corpus gaps** (Types 09, 13, 14 fully missing; Types 04
+ 05 partial / planned). These are candidates for Phase 4 template creation if they
survive Phase 2 filtering.

---

## §5 Output handover to Phase 2

Phase 2 receives this catalogue and applies the 8 Jetix-fit criteria per type. Expected
outcomes:
- Most likely **PROPOSE** (high signal in corpus + framework + memory): 01, 03, 06, 07, 09, 10, 11, 12, 15
- Most likely **DEFER Phase B+** (premature for Phase 1 / €50K horizon): 04, 05, 08, 13, 14
- Most likely **SKIP** (already covered by other layers, or scope-creep risk): 02 (already exists, not a Strategic Layer artifact to recreate)

**These are seed predictions only** — Phase 2 will apply criteria rigorously and may
produce different cuts.

---

## §6 Anti-scope (for this Phase 1 document)

- Does **NOT** decide which types Jetix should adopt → Phase 2.
- Does **NOT** define cadence calendar or hierarchy graph → Phase 3.
- Does **NOT** produce template structures → Phase 4.
- Does **NOT** write content for any document → next sprint, with 5-chat methodology per
  memory `methodology_multi_chat_review_for_critical_docs`.

---

## §7 Provenance + commits

- All corpus citations verified by direct file read or by transitive citation through
  consultant cards (which themselves carry library-direct provenance per Wave B
  manifest §1 supplement).
- Word count: ~4.5K (target 3-5K — within range).
- Frontmatter declares F2 (single-author scoping document, not a peer-validated synthesis).

---

*End of Phase 1 landscape catalogue.*
