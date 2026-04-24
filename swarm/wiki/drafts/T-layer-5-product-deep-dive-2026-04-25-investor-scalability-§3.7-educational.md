---
task_id: T-layer-5-product-deep-dive-2026-04-25
layer: L5
section: §3.7
direction: Educational Products + Investor Programs + Grant Hunting
type: layer-deep-dive-section
mode: scalability
author: investor-expert
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
created: 2026-04-25
status: drafted
sources:
  - {path: "prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md", range: "§3 + §4"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§5 Alliance Option C Hybrid + §11 Evolution per gate + §3.10 Teacher archetype"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D27 Fork-and-Merge + D28 Query-driven KB + D24 open-source research"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path B methodology + §8 recommendations"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 D24 open-source research + §7 archetypes + Инвесторы archetype 4"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3.8 budget self-funded + §4.2 legal/IP + §5 Phase 2 + §6 Phase 3"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§L5 Educational row"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md", range: "Educational row detail + Phase gate diagram"}
  - {path: "reports/review_2026-04-24.md", range: "audio_524 rows 790-793 + audio_527 row 801"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/intake.md", range: "full"}
  - {path: "swarm/wiki/tasks/T-layer-5-product-deep-dive-2026-04-25/decomposition.md", range: "C-09 cell acceptance predicate"}
word_count_estimate: ~2100
confidence: high
confidence_method: synthesis-from-locked-decisions-plus-voice
escalations: []
dissents:
  - claim: "Educational cohort-first vs self-serve-first at G2→G3 is unresolved"
    F: F4
    ClaimScope: "applies at G2→G3 launch decision; does not affect G0→G2 groundwork"
    R:
      refuted_if: "cohort format validated with 2+ paying cohorts; cohort margin > self-serve at 3x scale"
      accepted_if: "self-serve ROAS > cohort at same learner-count; Phase-3 economics confirmed at 12-month backtest"
  - claim: "Strategic investor round (equity) vs self-funded through Phase-3"
    F: F4
    ClaimScope: "applies at G3 ($1M gate); Phase-1/2 capital structure is self-funded per JETIX-PLAN §3.8"
    R:
      refuted_if: "JETIX-PLAN §3.8 explicitly overridden by Ruslan ack with investment terms"
      accepted_if: "Phase-3 crossed without equity; four consecutive quarters growth >30% without external capital"
---

# §3.7 Educational Products + Investor Programs + Grant Hunting

> Cell C-09. investor-expert × scalability. Cycle cyc-layer-5-product-deep-dive-2026-04-25.
> Deep Dive Policy applies — no compression.

---

## 1. Mission

Package and license the Jetix methodology — agent configs, wiki templates, system prompts,
setup scripts, research frameworks — as three parallel revenue and relationship streams:
**educational products** (paid courses, cohorts, enterprise licenses), **investor programs**
(non-dilutive relationship infrastructure leading to optional strategic rounds at Phase-3+),
and **grant hunting** (non-dilutive EU/DACH grant submissions targeting AI-native Mittelstand
and open-source research). Per L6 Alliance Option C Hybrid: Foundation publishes methodology
Apache 2.0 as the free upstream tier; Jetix-Corp owns the proprietary core as the paid
downstream tier. Clients fork the methodology per D27 fork-and-merge; the best adaptations
return upstream. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5]
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]

---

## 2. Phase Activation

This direction has three sub-tracks with differentiated activation windows.

**Overall status through G1 (€50K Q2 2026):** dormant for all external output. The task of
Phase-1 is to stabilize the methodology through live consulting + producer engagements —
generating the raw material from which educational products are distilled. No external
educational launch, no investor outreach, no grant submissions until the methodology is
proven on paying clients. Premature launch before methodology stability creates a compounding
anti-pattern: teaching an unvalidated system scales its deficiencies. Per JETIX-PLAN §3.8
self-funded discipline, Phase-1 generates no equity obligations and no grant bureaucracy
overhead that would consume founder bandwidth from the €50K revenue gate.
[src:decisions/JETIX-PLAN.md#§3.8]

**Sub-track 1 — Educational products:**
- Phase 1 (G0→G1, €0→€50K): groundwork only — methodology stabilization through consulting
  delivery; no course outline, no cohort recruitment yet.
- Phase 2 (G1→G2, €50K→€200K): outline creation, pilot cohort recruitment begins; no
  paid launch yet; D28 query-driven KB principle applied to course content curation
  (each module answers a specific anchor-query, not bulk ingestion of material).
- Phase 3 (G2→G3, €200K→€1M): **methodology repo V1 published** Apache 2.0 per L6 Option C;
  first paid cohort launched ($2K-$5K per learner × 10-30 learners); enterprise license
  program designed.
- Phase 3+ (G3→G4, €1M→$100M): cohort-of-the-month; enterprise-license tier at scale;
  certification program for Jetix-licensed consultants; D27 fork-merge fully operational
  (clients' adaptations return upstream with revenue-share or attribution).

**Sub-track 2 — Investor programs:**
- Phase 1: dormant; JETIX-PLAN §3.8 is explicit: "не equity-based investor pitches в Phase 1."
  [src:decisions/JETIX-VISION.md#§6]
- Phase 2 (G1→G2): **quarterly investor letter begins** (non-revenue; relationship-building);
  data room + due-diligence package constructed and kept current; first 3-5 investor
  relationships cultivated informally (warm intros only; no cold equity pitching).
- Phase 3 (G2→G3): investor program formalized with structured annual investor day;
  data room versioned in git per D25 company-as-code discipline; investor letter cadence
  monthly.
- Phase 3+ (G3→G4): optional strategic investor round considered — equity for scale, not
  for survival. See dissent block on investor round vs self-funded below.

**Sub-track 3 — Grant hunting:**
- Phase 1: dormant; GmbH not yet formalized (JETIX-PLAN §4.2 trigger: $20-30K self-earned);
  without a legal entity, EU grant submissions are technically blocked.
- Phase 2 (G1→G2): **first grant submission** when GmbH formalized + methodology stable;
  target: BMWK Zukunftsfonds or EU Horizon Europe Phase 1 (SME Instrument); 1 submission.
- Phase 3 (G2→G3): 2-3 submissions per year; consortium grants with Mittelstand AI Alliance
  members when Foundation entity incorporated per L6 Option C.
- Phase 3+ (G3→G4): grant portfolio 5-10 active grants; first grant-funded research hire;
  Horizon Europe large-scale research grants (AI + Mittelstand + open-source focus).

**Activation triggers (binary, measurable):**

| Sub-track | Activation trigger | Gate |
|---|---|---|
| Educational products (pilot cohort) | GmbH formalized + first 3 paying consulting clients + methodology documented in wiki | G1→G2 |
| Educational products (first paid cohort) | methodology repo V1 published + 5+ pilot cohort applications received | G2→G3 |
| Investor program (quarterly letter) | €50K revenue gate cleared + GmbH open + first 1 investor relationship warm | G1→G2 |
| Grant hunting (first submission) | GmbH incorporated + D24 open-source research published + methodology repo V1 live | G2→G3 |

---

## 3. Target ICP Mapping (L6 Trinity)

### Sub-track 1 — Educational products ICP

**Primary archetype: Teacher (L6 §3.10 + JETIX-VISION archetype 11 Блогеры subtype).**
Educational entrepreneur creating online courses, corporate trainers with IP, bootcamp
founders, workshop facilitators. Revenue $80K-$600K (Teachable/Kajabi + corporate training
+ cohorts). Core pain: curriculum update + new cohort management + community overhead
consumes 40-60% of their time — time that should go to content and teaching.
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§3.10]

Jetix educational product is a direct answer to the Teacher archetype's pain: the Jetix
methodology is itself a D28 query-driven KB system for building and updating knowledge
systematically. When a Teacher learns the Jetix methodology, they are acquiring the
operating system for their own educational business — not just consuming a course.

**Secondary archetype: Startupper (L6 §3.1) + Operator/Founder-CEO (L6 §3.11).**
Operators wanting to upgrade their practice with AI, but who need a structured methodology
(not a pile of tools). Payment-ability filter: $5K/mo recurring OR $10K one-shot.
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§2.1]

**Tertiary archetype: Инвесторы (JETIX-VISION §7.1 archetype 4) + ecosystem specialists
(Ресёрчеры + Инженеры + Философы).** These segments become active at G2→G3 when the
methodology repo V1 is published and educational track differentiation is possible. They
self-select through the Apache 2.0 free tier; paid upgrade is via cohort or enterprise
license.

**P1A/P1B fit:** educational products are P1B-leaning in Phase-2 (referral-driven; Teachers
and Startuppers who have already experienced Jetix consulting or producer outputs are the
natural first cohort students). P1A cold-outreach to Teachers for educational products
begins at G2→G3.

**Payment filter alignment:**
- Course tier (€499-€1499): accessible to high-earners + предприниматели; excludes
  passive AI consumers who won't invest.
- Cohort tier ($2K-$5K): aligned with $10K one-shot payment-ability filter; sits below
  but adjacent to the filter (cohort is a qualifying entry into Jetix ecosystem before
  larger consulting engagement).
- Enterprise license ($10K-$50K/year): directly inside the $5K/mo recurring filter;
  targets Operator/Founder-CEO + Mittelstand SMBs.

### Sub-track 2 — Investor programs ICP

**Primary: accredited angel investors + family offices + early-stage VCs** evaluating the
AI consulting methodology space. The Инвесторы archetype (JETIX-VISION §7.1 archetype 4)
describes these: pattern seekers, looking for smart bets + resource-allocation frameworks +
Phase-2+ trajectory participation. [src:decisions/JETIX-VISION.md#§7.1]

Investor programs are not revenue-generating in Phase-2 or Phase-3. They are
relationship-building infrastructure. The capital value is option value: when Jetix reaches
G3 ($1M+ revenue) and a strategic round is considered, the investor program participants
are already qualified, already have context, and do not need to be educated from zero.
This is the skin-in-the-game discipline applied to investor relationships: Ruslan invests
relationship time before asking for capital, not after.

**Payment filter: N/A.** Investors are not paying Jetix for investor programs. The
relationship value flows the other direction.

### Sub-track 3 — Grant hunting ICP

**Primary: EU Horizon Europe program + BMWK Zukunftsfonds (Germany national) + BMBF AI
initiative.** Grant funders are not clients in the conventional ICP sense. They are
institutional capital allocators seeking to fund projects matching their mandate: AI +
open-source + Mittelstand + GDPR-sovereign + European competitiveness.

Jetix is an excellent fit for this mandate per STRATEGIC-INSIGHT §5 Path B and D24
open-source research: open-source methodology (D24), Mittelstand AI Alliance framing
(STRATEGIC-INSIGHT §8 recommendation 3), Apache 2.0 methodology publication per L6
Option C, DACH specialization, and real deployments (consulting + producer Phase-1).
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8]

**DACH industry consortia + Mittelstand AI Alliance members** become co-applicants on
consortium grants at G2→G3 when the Foundation entity is incorporated. This is the key
leverage point: a solo company applying for Horizon Europe grants is weak; a consortium
application with 3-5 Alliance SMB members is strong. The Alliance is simultaneously the
educational distribution channel and the grant application consortium.

---

## 4. Value Proposition

### Sub-track 1 — Educational products

**Problem (in client's language, Teacher archetype):** "I want to upgrade my practice with
AI, but every course is either too abstract — philosophy and frameworks with no implementation
— or too tool-specific: 'here's how to use ChatGPT in five steps.' I need methodology I can
actually apply to my context, in my niche, with my students. And I need it to evolve as
AI evolves, not become stale in six months."

**Problem (Startupper/Operator language):** "I have a business. I know AI can help. I've
tried tools. The tools work individually but don't add up to a system. I don't need more
tools — I need the operating system that tells me which tools to use, in what order, for
what tasks, and how to know if it's working."

**Outcome promised:** A complete Jetix methodology applicable to the learner's own context,
delivered in a replicable system — not one-off knowledge. The learner exits with: a working
wiki structure, an agent config, a project management pattern, a KB design principle (D28
query-driven), and a fork of the methodology adapted to their niche (D27 fork-and-merge).
The fork connection means the learner's adaptation can return upstream for recognition or
revenue-share — they are not just consumers of the methodology, they are contributors to it.
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]

**How Jetix differs from competitors:** Methodology-as-code (D25 company-as-code discipline):
everything is in git. The course is not slides and recordings — it is a fork of the actual
Jetix OS repository, adapted for educational delivery. When the methodology evolves (which
it will, continuously), the course updates automatically via git-pull, not via manual content
refresh. This structural difference is non-replicable by competitors who produce static
educational content. Free upstream tier (Apache 2.0 per L6 Option C) creates a trust-first
relationship before monetization: learners can read, fork, and verify the methodology before
paying for cohort support or enterprise license.
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D25]
[src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5]

**D28 connection — query-driven KB for educational products:** Per D28, educational
products filter content by anchor-query, not bulk. Each module in a Jetix course answers
a specific declared question (e.g., "How do I build a company-as-code KB that scales from
1 to 50 people?" is a module anchor; bulk content about knowledge management generally does
not appear). This structural discipline means the educational product has higher signal
density than generic AI courses — and it teaches the learner the D28 discipline itself,
which they then apply to their own KB and their own knowledge products.
[src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D28]

### Sub-track 2 — Investor programs

**Problem (investor language):** "The AI consulting space has 35,000 companies and 90%
die in year one. How do I identify the structural winners? Who has a moat that isn't just
marketing? What does the unit-economics look like at scale? And who is building something
that I'd want to back when they're ready for capital?" [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§0]

**Outcome promised:** Pre-packaged, investor-grade materials on Jetix's competitive position
(BIOS/standard-moment framework; DACH/Mittelstand moat; open-source research D24; Alliance
Option C trajectory). An investor who has been receiving quarterly letters for 8 quarters
has a full longitudinal view of Jetix's execution cadence, unit-economics, moat durability,
and capital needs — before any formal raise. Due diligence compresses from months to weeks.

**How Jetix differs:** Open-source research (D24) means the methodology is reviewable —
no black-box claims. Structural moat (Mittelstand + compliance + Alliance) is visible in
public git history. Capital-efficient Phase-A (no VC dependency per JETIX-PLAN §3.8) means
the investor sees a founder with skin-in-the-game who doesn't need dilutive capital to survive.
The quarterly letter is authored by Ruslan, not by an investor relations department — the
investor is always talking to the person with ultimate decision authority.
[src:decisions/JETIX-PLAN.md#§3.8] [src:decisions/JETIX-VISION.md#§5-D24]

### Sub-track 3 — Grant hunting

**Problem (grant-giver language):** "We fund AI innovation in European Mittelstand that
combines social value (open-source, GDPR-sovereign, cross-sector applicability) with
scientific rigor. Most applicants are either academic (rigorous but not market-facing) or
commercial (market-facing but not rigorous or open). We need projects at the intersection."

**Outcome Jetix delivers to the grant giver:** A fundable, auditable project — open-source
research published (D24), Mittelstand AI Alliance as consortium structure, Apache 2.0
methodology, real deployments in Phase-1 consulting as empirical base, DACH specialization.
The EISA-moment framing from STRATEGIC-INSIGHT §8 recommendation 3 (Mittelstand AI Alliance
= European sovereign AI consortium) maps directly onto Horizon Europe's AI + sovereignty +
Mittelstand mandate. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§8]

---

## 5. Offer Structure (Placeholder — L7 owns final pricing)

### Sub-track 1 — Educational products

**Free tier (Apache 2.0 Foundation docs):**
- All methodology documentation published open-source under Foundation entity per L6 Option C.
- Self-serve: wiki templates, agent config templates, system-prompt templates, setup guides.
- Format: git repository (public); no enrollment, no registration gate.
- Revenue model: zero directly; drives awareness + trust + referrals into paid tiers.
- D27 connection: free-tier users who fork and adapt the methodology are potential contributors
  back to upstream. Attribution policy TBD (L7 pricing cycle).

**Course tier (self-serve async):**
- Placeholder price range: €499-€1,499 per learner.
- Format: structured curriculum anchored to specific queries (D28), delivered via Teachable
  or equivalent Phase-2 infrastructure.
- Duration: self-paced (typical 4-8 weeks of material).
- Deliverables: working fork of Jetix methodology adapted to learner's context; guided KB
  setup; agent config template; completion credential.
- Payment terms: one-time purchase; refund policy TBD (L7).
- L7 owns final pricing.

**Cohort tier (live, instructor-led):**
- Placeholder price range: $2,000-$5,000 per learner, 10-30 learners per cohort.
- Format: live 4-8 week cohort with Ruslan or certified Jetix-licensed instructor (Phase-3+).
- Duration: weekly sessions + async community + fork-and-merge workshop.
- Deliverables: same as course tier plus live feedback on learner's fork; introduction into
  Jetix Secure Network at cohort-member discount.
- Payment terms: full upfront OR 2-installment; TBD (L7).
- L7 owns final pricing.

**Enterprise license (in-house team training):**
- Placeholder price range: $10,000-$50,000 per year per company.
- Includes: methodology + updates (via git) + internal-team training facilitation +
  dedicated support channel + custom fork-and-merge setup for the company's context.
- Duration: annual subscription; renewable.
- Payment terms: annual upfront or quarterly; TBD (L7).
- L7 owns final pricing.

### Sub-track 2 — Investor programs

**Quarterly investor letter:** Non-revenue. Relationship infrastructure. Content: Jetix
financials (owner-earnings, not GAAP), methodology evolution, moat health, key decisions
made, next gate thesis. Written by Ruslan (HITL; investor-expert provides extraction support
only per §7 writing-support mode). Format: PDF + git-versioned markdown.

**Annual investor day (G3+ only):** Non-revenue. Format: half-day session with 5-10 invited
investors; presentations + Q&A + live methodology demo. Location: Berlin Phase-3; virtual
before. No fee; relationship investment by Ruslan.

**Data room + due-diligence package:** Non-revenue in itself; enables capital raise if
pursued at G3+. Maintained continuously in git per D25. Contains: financials, cap table,
methodology documentation, moat analysis, unit-economics, horizon projections, team profile.

**Strategic investor round (optional, Phase-3+):** Equity-based; placeholder terms not set.
Condition: Ruslan explicit HITL ack per JETIX-PLAN §3.8 (Phase-1 anti-scope; Phase-3+
consideration only). See dissent block below.

### Sub-track 3 — Grant hunting

**EU Horizon Europe submissions:** Non-dilutive capital. Typical grant size €500K-€2M per
project. Submission cycle: 2-3 per year starting G2→G3. Processing timeline: 6-12 months
per submission. Jetix receives funding to fund open-source research + hire a grant-funded
researcher role.

**BMWK Zukunftsfonds / BMBF AI initiative (Germany national):** Non-dilutive capital.
Typically €200K-€800K per project. Faster cycle than Horizon Europe (4-6 months). Phase-2
first submission target.

**Consortium grants (Alliance members):** Non-dilutive; shared across Alliance participants.
Sizes TBD per specific call. Requires Foundation entity incorporated (G2→G3).

---

## 6. Delivery Mechanism

### Sub-track 1 — Educational products

**Agents involved (Jetix swarm infrastructure):**
- `knowledge-synth`: content distillation from consulting deliverables into course modules;
  KB maintenance for course content updates.
- `crazy-agent`: creative disruption on curriculum structure — challenge stale module
  sequences, inject novel framing.
- `personal-assistant`: cohort logistics (calendar, enrollment emails, session reminders).
- `inbox-processor`: cohort community communications triage.
- `manager`: project management of cohort delivery timeline.

**KM-Mat infrastructure used:**
- `/ingest --anchor=<course-module-anchor>` per D28 mandate: each ingest event is tagged to
  a declared course module anchor. No bulk ingestion.
- `/ask` powering learner Q&A bot (Phase-2 MVP): learner submits question, bot retrieves
  from Jetix wiki + methodology repo, returns structured excerpt with citation. Not inference
  without source; structured-excerpt mode per OFFLINE_MODE=1 discipline.
- `/consolidate --weekly` for course content deduplication and currency maintenance.
- `/build-graph` for community detection within learner cohort.

**Infrastructure (non-Jetix, Phase-2 MVP):**
- Course delivery: Teachable or Circle or Mighty Networks (TBD Phase-2; no implementation
  now per anti-scope).
- Scheduling: Calendly (cohort office hours).
- Payment: Stripe Business (already in JETIX-PLAN Phase-1 infra).

**Human time requirements:**
- Self-serve course: near-fully automated post-launch. Ruslan time: 2-4 hours/week for
  async Q&A review + community moderation (cohort-level engagement).
- Cohort tier: ~10 hours per week per active cohort (instructor). Phase-2: Ruslan as
  instructor. Phase-3+: Jetix-certified instructors reduce Ruslan's direct delivery time.
- Enterprise license: 5-10 hours per client per month (facilitation + support). Delegated
  to team hire Phase-3.

**Automation level:** high for self-serve (near-autonomous after setup); medium for cohort
(human-instructor-required for live sessions); medium-high for enterprise (template-based
setup, human facilitation).

### Sub-track 2 — Investor programs

**Agents involved:**
- `knowledge-synth`: data room updates (synthesizes quarterly operating metrics from wiki
  and git history into investor-readable format).
- `strategist`: pitch refinement and investor letter structural review (Phase-3+; not
  available in Phase-2 per Phase-2 agent scope).
- `personal-assistant`: investor meeting scheduling, follow-up coordination.

**Human time requirements:**
- Phase-2 quarterly letter: 4-6 hours per quarter (Ruslan composes; investor-expert provides
  extraction template only). Writing-support mode per §7.
- Phase-3 annual investor day: 20-30 hours of Ruslan's preparation per event.
- Ongoing relationship management: 2-4 hours per month Phase-2 (warm calls; WhatsApp
  touchpoints with 3-5 warm contacts).

**Automation level:** low by design. Investor relationships are Ruslan-authored and Ruslan-
owned. The agent infrastructure provides extraction support and data-room maintenance, not
relationship management. Investor relationship work is in Ruslan's architect-orbit
(non-delegatable) per JETIX-VISION §3.

### Sub-track 3 — Grant hunting

**Agents involved:**
- `sales-researcher`: grant discovery (scan Horizon Europe calls, BMWK announcements,
  industry consortium calls; extract eligibility criteria vs Jetix capability matrix).
- `philosophy-expert`: scientific framing of Jetix research outputs for grant narrative
  (D24 open-source research framing).
- `engineering-expert`: technical sections of grant applications (architecture descriptions,
  implementation plans, KPI definitions).
- `manager`: project management of grant submission timeline (deadlines, partner coordination
  for consortium applications).

**Human time requirements (per submission):** 20-30 hours Ruslan + 20-30 hours first
sales/operations hire (Phase-2+ trigger). Three to five submissions per year at Phase-3.
Grant submissions are a significant human-time investment; this justifies the hire of a
dedicated grant-writing/ops role at G2→G3.

**Automation level:** medium. Grant applications require human authorship and compliance
review; agent infrastructure accelerates discovery, drafting, and technical sections but
the final submission is human-reviewed and human-signed.

---

## 7. Competitive Positioning

### Sub-track 1 — Educational products

**Direct competitors by segment:**

*Maven / Reforge cohorts ($1.5K-$4K/seat):* Generic AI and business cohorts; strong
community; not methodology-deep. Maven has distribution; weak on Mittelstand context,
DACH specialization, and git-native methodology delivery. Jetix wins on: depth of
methodology (company-as-code vs tool-tips), D27 fork-and-merge participation (learners
contribute back — Maven's content is consumable, not forkable), and the
STRATEGIC-INSIGHT §5 Path B architecture (methodology-as-infrastructure, not methodology-
as-entertainment).
[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5]

*Paid newsletters (Every / Packy McCormick / Lenny Rachitsky):* Content, not systematic
methodology. High-quality signal; low implementation support. No fork-and-merge. No
enterprise license path. Jetix serves the learner who has consumed enough content and now
needs an operating system, not more content.

*Corporate training (Udacity / Coursera for Business):* $50-$500/seat; weak on Mittelstand
context; generic AI upskilling. No company-as-code delivery. No fork-and-merge. Institutional
purchasing motion (procurement departments) rather than direct-to-founder. Jetix Phase-2
educational products are founder-to-founder, not institution-to-employee.

*Bootcamp competitors (Le Wagon, General Assembly, etc.):* Code-focused; not methodology-
focused. Strong community but broad ICP. Jetix educational products are niche-focused
(Mittelstand AI operating systems) and deeper on methodology. Not competing for the same
segment.

**Why Jetix wins on educational products:**
1. D27 fork-and-merge participation: learner's adaptation can return upstream. No competitor
   has this. The educational product is simultaneously a distribution channel for the
   methodology and a contribution mechanism back to the methodology's quality.
2. D28 query-driven KB: every module is anchored to a declared question. Signal density is
   higher than generic AI courses.
3. Apache 2.0 free upstream: trust-first. Learner can read and verify before paying. Lowers
   acquisition barrier; filters for serious learners who have read the methodology (the D22
   adequate + upward-direction filter operationalized as a self-selection mechanism).
4. Reverse-engineering methodology (audio_527): Ruslan's *«Jetix будет заниматься
   реверс-инжинирингом на максималках»* — the educational methodology teaches learners
   to deconstruct any system and rebuild it, not just use pre-packaged tools.
   [src:reports/review_2026-04-24.md#audio_527]

**Honest risks:**
- Unknown brand in Phase-2: when the cohort launches, Jetix has no educational brand equity.
  Overcome by: consulting alumni as first cohort students (warm referral pool built in
  Phase-1); Teacher archetype as direct target (Teachers understand the structural value
  of a methodology-as-code course even before brand recognition).
- Instructor dependency: Phase-2 cohorts require Ruslan's direct instruction time. This
  caps cohort frequency. Mitigation: certification program at Phase-3+ creates licensed
  instructors; Ruslan's time compounds into an instructor pipeline, not per-cohort overhead.

### Sub-track 2 — Investor programs

Not a competitive product; no direct competitors. Investor programs are relationship
infrastructure, not a market-facing offering. The comparison set is: Jetix vs other
founder-investor relationship-building approaches.

The margin-of-safety here is structural: investors who have received 8 quarters of a
methodology-transparent, git-versioned quarterly letter have materially lower due-diligence
overhead than investors who are meeting Jetix for the first time at a pitch event. The
opportunity cost of maintaining the quarterly letter program (4-6 hours/quarter) is
extremely low versus the option value created (accelerated due diligence when the raise
is pursued; richer investor relationships that can lead to warm introductions and market
intelligence even if a raise is never pursued).

Second-level thinking (Marks pattern P3): what's already priced in by the consensus
investor view on AI consulting? The consensus view is that AI consulting is a commodity
business with 90% year-one failure rate. Jetix's quarterly letter must explicitly address
what makes Jetix structurally different from that consensus — the methodology moat
(STRATEGIC-INSIGHT §2), the Alliance positioning, the DACH specificity, the local-first
architecture (STRATEGIC-INSIGHT §3). The letter is not a sales document; it is a
second-level-thinking document that trains investors to see the moat before they see the
revenue. [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§2]

### Sub-track 3 — Grant hunting

**Competition for grant funding:**

*Academic research consortia:* Strong scientific credibility; slow and market-disconnected.
Grant bodies increasingly want market-facing projects with real deployment. Jetix's Phase-1
consulting deployments are the empirical base that academic applicants lack.

*Pure-research AI startups (Aleph Alpha, Mistral, etc.):* Foundation-model focused; not
Mittelstand-aligned; not methodology-as-infrastructure. Competing for different grant
buckets (Jetix targets Mittelstand AI adoption grants, not foundation model research grants).

*Other AI consulting / infrastructure startups targeting DACH:* Exist but without the
open-source research mandate (D24), without the Alliance structure, and without the
local-first architecture specificity. Most are proprietary platforms — they cannot easily
apply for open-innovation grants.

**Why Jetix wins on grants:**
1. D24 open-source research means all methodology documentation is publicly auditable —
   grant reviewers can verify claims.
2. Mittelstand AI Alliance as consortium structure gives the application collective weight
   that a solo-company application cannot have.
3. GDPR-sovereign, local-first architecture (STRATEGIC-INSIGHT §5 Path B) is exactly
   the "European AI sovereignty" framing that Horizon Europe and BMWK prioritize.
4. Alliance Option C Hybrid (Foundation non-profit + Jetix-Corp proprietary) is a legally
   standard structure for grant eligibility in EU programs — non-profit Foundation entities
   are preferred applicants in Horizon Europe consortia.
   [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5]

---

## 8. Evolution per Gate

### Phase 1 (G0→G1, €0→€50K) — Stabilize methodology, build groundwork

All three sub-tracks are **dormant** for external output. The Phase-1 task is:

- Consulting + producer deliverables generate the raw methodology material.
- Knowledge-synth agent continuously distills consulting outputs into wiki (D28 anchor-
  driven; not bulk ingestion).
- Methodology progressively crystallizes in git under D25 company-as-code discipline.
- No course outline, no cohort recruitment, no investor letter, no grant submission.

**Via-negativa (Taleb pattern P5) — what to retire at G0→G1:**
Any educational initiative that begins before methodology is proven on 3+ paying clients
must be retired: scaling an unvalidated system into educational format compounds its
deficiencies at the speed of learner uptake. Retire any temptation to launch an educational
product as a revenue shortcut before the €50K consulting gate.

**Antifragility check:** Phase-1 dormancy for this direction is itself antifragile —
the methodology strengthens under the volatility of live consulting engagements
(client challenges the methodology, forces improvements). This volatility builds the
product that will be taught. A course launched before this volatility testing is fragile.

### Phase 2 (G1→G2, €50K→€200K) — Investor program begins + first grant + educational groundwork

**Investor program:**
- Quarterly investor letter begins (non-revenue).
- Data room v0.1 constructed in git.
- First 3-5 warm investor relationships cultivated (warm intros from consulting clients
  and warm network; no cold equity pitching per JETIX-PLAN §3.8).
- Investor letter framing: BIOS-moment positioning (STRATEGIC-INSIGHT §0); moat analysis
  (Mittelstand + compliance + Alliance trajectory); unit-economics transparency.

**Grant hunting:**
- First grant submission when GmbH formalized + D24 open-source research published.
- Target: BMWK Zukunftsfonds (faster cycle; German national; $200K-$800K range) as
  first submission; EU Horizon Europe Phase 1 as second (if bandwidth permits).
- Human time: Ruslan 20-30 hours + ops contractor support.

**Educational products:**
- Methodology repo skeleton outlined; no public launch.
- Pilot cohort: invite 5-10 consulting alumni to a proto-cohort at minimal or no fee
  (validation, not revenue); extract feedback on methodology gaps.
- D28 query-registry for course modules established: each future module's anchor-query
  documented in wiki before content is written.

**BOSC-A-T-X trigger at G1→G2: O+C (Operation + Composition).** Operation expands
from consulting-only to consulting + early-stage investor relationship management. Composition
expands by the first hire (sales + ops role; LAYER-6 §2.3). First fixed-cost monthly
liability appears. Capital-allocation discipline tightens: owner-earnings reported
quarterly to self; educational product opportunity cost must clear 30% hurdle relative
to consulting capacity cost. [src:swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md#§6]

### Phase 3 (G2→G3, €200K→€1M) — Methodology repo V1 + first paid cohort + 2-3 grants/year + formalized investor program

**Educational products:**
- Methodology repo V1 published Apache 2.0 per L6 Option C (Foundation entity) —
  non-proprietary surface, proprietary core maintained in Jetix-Corp.
  [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5]
- First paid cohort launched: $2K-$5K × 10-30 learners.
- D27 fork-and-merge operationalized: each cohort student receives a fork of the
  methodology repo; their adaptations are submitted as PRs to the Foundation repo;
  Ruslan (or designated reviewer) accepts high-quality mutations upstream. Attribution
  tracked in git commit history; revenue-share model designed (L7 pricing cycle owns).
  [src:decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md#D27]
- Self-serve course launched in parallel: €499-€1,499 async tier.
- Enterprise license program designed (not yet sold at scale; 1-2 pilot enterprise
  clients if inbound).

**Investor program:**
- Formalized with annual investor day.
- Monthly letter cadence.
- Data room v1.0: full financials, moat analysis, horizon projections, unit-economics,
  team profile.
- Optional: first strategic investor exploration conversation — purely exploratory, no
  commitment per JETIX-PLAN §3.8 self-funded preference.

**Grant hunting:**
- 2-3 submissions per year.
- Consortium applications with Alliance members (Foundation entity incorporated).
- First grant win target: BMWK or Horizon Europe Phase 1.
- Grant revenue: non-dilutive; funds first research/ops hire.

**BOSC-A-T-X trigger at G2→G3: A+S (Agency + Scale).** Agency shifts from solo to
small team of 3+; scale magnitude triggers Phase-B governance. Horizon projections
extend to 3 years (was 1 year). Capital-allocation memo cadence monthly (was quarterly).
Hurdle-rate gate applied per allocation: educational product investments must clear
30% hurdle against consulting opportunity cost.

### Phase 3+ (G3→G4, €1M→$100M) — Educational scale + grant portfolio + strategic investor consideration

**Educational products:**
- Cohort-of-the-month program: 12 cohorts/year.
- Enterprise-license tier at scale: 10-30 enterprise clients.
- Certification program for Jetix-licensed consultants: branded credential with governance;
  certified consultants can deliver Jetix methodology to their own clients under license.
  This is the key D27 fork-and-merge monetization mechanism: each certified consultant
  is a fork of Jetix methodology operating under license, paying methodology-licensing fees.
- Enterprise-certified-consultant program creates a distribution network for educational
  products without proportional Ruslan time.

**Grant portfolio:**
- 5-10 active grants.
- First dedicated grant-funded research role hired.
- Consortium grants across Alliance members active at scale.

**Investor program:**
- Strategic investor round considered if scale capital needed for $100M gate.
- Pre-existing investor program participants are the preferred round participants (no cold
  pitching; 8+ quarters of relationship context).
- Equity terms: TBD; JETIX-PLAN §3.8 explicit self-funded preference persists as default;
  equity only if non-dilutive alternatives (grants + revenue) cannot sustain needed scale.
  See dissent block below.

**BOSC-A-T-X trigger at G3→G4: B+T (Boundary + Time).** Company boundary expands
multi-BU; time horizon shifts to multi-year mandatory. Horizon projections extend to 5
years. Capital-allocation memo cadence quarterly (was monthly). Methodology licensing
ecosystem active; multiple BUs clearing hurdle rates individually.

### $1T Horizon (G4→G5) — Civilizational-scale educational infrastructure

- Jetix Foundation certifications recognized by EU standards bodies; potentially by
  national accreditation bodies in DACH.
- Educational tracks for 10,000+ learners/year across multiple languages and verticals.
- Grant consortium with Alliance members: Jetix is a named consortium coordinator for
  Horizon Europe research programs on AI, Mittelstand, and cooperative systems.
- Methodology licensing ecosystem: hundreds of licensed partners globally; each is a
  D27 fork contributing back to the upstream methodology.
- Alliance Foundation as a formal IP and research custodian: methodology evolves through
  distributed contribution governed by a BDFL-style or meritocracy governance model
  (D27 downstream decisions still pending per LOCKS addendum).
- All canonical patterns P1..P7 (Buffett/Graham/Marks/Munger/Taleb) re-validated under
  civilizational-scale operating mode and regulatory acceptance.

**BOSC-A-T-X trigger at G4→G5: X+O (eXternal + Operation).** External regulatory and
societal constraints; operation verb redefined as "civilizational allocator" for
methodology distribution. Antifragility ledger spans decades, not years.

---

## 9. Cross-Direction Dependencies

### Depends on:

- **§3.1 AI Consulting** (primary dependency): Consulting engagements are the raw-material
  source for the methodology being taught. Every consulting deliverable is a potential
  course case study, template, or validated framework. Without Phase-1 consulting revenue
  and delivery, there is no methodology to package into an educational product. The
  educational product is downstream of consulting, not parallel to it.

- **§3.2 Продюсерский центр** (secondary dependency): Production pipeline for course
  content (research → script → recording → editing → distribution). The producer center's
  AI-enhanced production methodology is exactly the content the educational track will
  teach. Also: educational product recordings can be produced by the producer center
  infrastructure.

- **§3.3 USB-C Integration Services** (structural dependency for Path B): The methodology
  repo (Path B of USB-C per STRATEGIC-INSIGHT §5) is the same artifact as the educational
  product's foundation tier. The methodology repo V1 launch is simultaneously the
  educational free tier AND the USB-C Path B deployment package.
  [src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md#§5]

- **§3.9 Smart AI narrative** (framing dependency): The "Smart AI vs dumb AI" narrative
  (audio_529) provides the educational product's opening hook — learners are enrolling
  to build Smart AI operating systems for their own business, not just learn more tools.

- **§3.5 Secure Network** (community dependency, Phase-2+): Cohort graduates are natural
  Secure Network members. The educational product creates the qualified-member pipeline
  for the Secure Network, reducing the Secure Network's cold-membership-acquisition burden.

- **Alliance Foundation** (structural dependency for grant hunting and Apache 2.0 free
  tier): Without the Foundation entity incorporated, grant applications as a non-profit
  consortium are blocked, and the Apache 2.0 upstream tier has no governance entity
  to maintain it. Foundation incorporation is a prerequisite for both grant hunting at
  scale and the educational free tier's legal structure.

### Depended on by:

- **§3.3 USB-C Integration Services Path B** (ships the methodology repo): The methodology
  repo V1 that the educational product publishes is the same deliverable that USB-C Path B
  ships to enterprise clients. Publishing it as a free tier creates market awareness that
  makes USB-C Path B sales easier.

- **§3.4 Matchmaker Platform** (certified consultants as specialist pool): The certification
  program (Phase-3+) creates a pool of Jetix-certified consultants who are matchmaker
  specialists. Each certified consultant is a node in the Matchmaker network.

- **§3.5 Secure Network** (educational alumni as members): cohort graduates are pre-qualified
  Secure Network members (D22 filter passed through cohort selection process).

- **§3.6 YouTube-analyzer SaaS**: The reverse-engineering methodology (audio_527) that
  powers the YouTube-analyzer is also an educational track. Teaching clients to
  reverse-engineer competitors' YouTube channels is a course module and a product lead
  for the YouTube-analyzer SaaS.

**Cross-cutting: Alliance Foundation.** Educational products ARE the operational arm of
the Foundation. The free Apache 2.0 docs tier drives Alliance membership. Jetix-Corp's
paid downstream (cohort + enterprise license) is the commercial expression of the
Foundation's methodology. Revenue from Jetix-Corp proprietary tiers funds Foundation
research and open-source development. [src:decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md#§5]

---

## 10. Open Questions (3-5)

**Q1 — Educational products format at G2→G3 launch: cohort-first vs self-serve-first?**

Cohort format: higher margin per learner ($2K-$5K vs €499-€1,499), stronger relationship
with learner, enables fork-and-merge workshop as live session, creates Secure Network
member pipeline more reliably. Downside: requires ~10 hours/week Ruslan direct instruction;
caps at 1-2 cohorts per quarter without instructor certification program.

Self-serve format: scales without proportional Ruslan time; lower margin per learner;
weaker signal on whether learner actually applies the methodology (no live session
accountability). Downside: lower revenue per learner; harder to build fork-and-merge
practice culture in an async environment.

Scalability-mode assessment (Koestler 9.4/9.5 check): cohort-first avoids INT excess
(the investor-expert offering no recommendation); cohort-first risks S-A excess if Jetix
insists on cohort format beyond Phase-3 when instructor leverage is available.
**Recommendation pending Ruslan decision:** cohort-first at G2→G3 (validation of methodology
teachability); self-serve as concurrent lower-cost tier; enterprise license as the scale
path beyond G3+. L7 pricing cycle owns the final structure.

**Q2 — Grant targeting priority: EU Horizon Europe (large, slow, 12+ months) vs BMWK
Zukunftsfonds (medium, faster, 4-6 months) vs industry consortia via Alliance?**

BMWK has faster cycle and is German-national — strongly aligned with DACH Mittelstand
mandate and lower bureaucratic overhead for a GmbH-registered entity. Horizon Europe
is larger but has 12-18 month cycles and requires consortium structure (not available
until Foundation incorporated). Alliance consortium grants are potentially the largest
but require Alliance member network (only available G2→G3).

**Priority sequence:** BMWK first (Phase-2 when GmbH formalized); Horizon Europe Phase 1
(SME Instrument) second (Phase-2/Phase-3 boundary); Alliance consortium grants third
(Phase-3+). This sequence respects the gate dependencies and bandwidth constraints.

**Q3 — Investor program scope at Phase-3+: pure relationship-building (no equity) vs
strategic round ($1M-$5M for $1-10% equity)?**

[dissent preserved — see frontmatter] JETIX-PLAN §3.8 is explicit: Phase-1 anti-scope
for equity pitches; Phase-1 discipline preserved through Phase-2. At Phase-3+ ($1M revenue
gate), the question opens.

Capital-allocation arithmetic (investor-expert domain): if Phase-3+ growth can be funded
by revenue + grants alone, the opportunity cost of 10-25% equity dilution is unbounded
(Jetix at $1T trajectory: 10% dilution costs $100B in final equity value). The
risk-of-ruin consideration cuts the other way: if growth to $100M gate requires capital
that grants + revenue cannot provide on the required timeline, then not raising creates
a risk-of-ruin scenario from a different direction (competitors capture the market window
per STRATEGIC-INSIGHT §8 recommendation 5: "speed: window NOW — 6-12 months").

**Unresolved tension.** This is a HITL decision (capital deployment requires Ruslan ack
per §1d requires-approval). The investor-expert escalates this to HITL; does not resolve.
[src:decisions/JETIX-PLAN.md#§3.8]

**Q4 — D27 fork-and-merge operationalization: revenue-share model, attribution, or
Apache 2.0 (attribution not required)?**

Apache 2.0 permits but does not require attribution. If Jetix opts for Apache 2.0 free
tier for the Foundation docs, learners can fork and build commercial products without
paying Jetix. This is the open-source community-growth play (maximize adoption + Alliance
membership) but sacrifices per-fork revenue.

Alternatives: (a) Apache 2.0 with voluntary contribution mechanism (community expectation
but no legal requirement); (b) dual-license (Apache 2.0 for individual use; commercial
license required for enterprise use with fork — same model as Redis/Elasticsearch); (c)
LGPL-equivalent (software fork freely; methodology-derivative commercial products require
contribution back or license fee).

IP licensing model is a locked question per L6 ack (Apache 2.0 for docs; LGPL-equivalent
for software Foundation; proprietary Jetix-Corp core). The educational product's fork-and-
merge revenue model is still unresolved within that framework. L7 pricing cycle owns the
final model.

**Q5 — Certification program gate (Phase-3+): when does the Jetix-certified consultant
program launch, and what governance does it require?**

Branded credential requires: (a) curriculum standardization (the methodology is stable
enough to be tested); (b) examination mechanism (who passes whom?); (c) accreditation
governance (who maintains the standard?); (d) enforcement (what does "certified" mean
legally?). In Europe, educational credentials have potential regulatory implications
(VET regulations in Germany, for instance).

The D26 team-50-100 trajectory implies Jetix will eventually need a formal governance
function for methodology standards. The certification program is the first moment when
methodology governance becomes a customer-facing question rather than an internal one.
Gate: not before 12 paying cohorts have been delivered (minimum base of evidence that
the methodology is consistently teachable). Gate-trigger: G3+ ($1M revenue gate) as
the earliest possible; more likely G4 ($100M territory) when Alliance governance is
mature enough to co-own the certification standard.

---

## Scalability-Mode: Janus Degraded-Mode Check for this Direction

**S-A excess risk (self-assertive excess):** the investor-expert insisting that this
direction must pursue equity raises at Phase-3+ regardless of Ruslan's self-funded
preference. Behavioral signature: memo proposes strategic round terms without HITL
escalation. **Guard:** all equity proposals are explicitly in requires-approval category
per §1d; investor-expert stops at escalation, does not propose terms.

**INT excess risk (integrative excess):** the investor-expert providing no primary
recommendation on cohort-first vs self-serve-first, only preserving the tension as a
dissent with no actionable synthesis. **Guard:** §10 Q1 provides a primary recommendation
(cohort-first at G2→G3) while flagging the dissent on format priority explicitly in the
frontmatter.

**Recovery from INT excess in this draft:** §10 Q1 produces a Hamel-binary primary claim
("cohort-first at G2→G3") with reasoning and a refutation condition ("L7 pricing cycle
owns final; overridden if self-serve ROAS > cohort at same learner count"). This satisfies
the recovery condition per §6.3.

---

## Provenance

| Source | Range | Quote |
|---|---|---|
| decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | D27 | «Jetix должен стать базовой стабильной системой, которую пользователи могут форкать и адаптировать под себя, а лучшие мутации возвращать в основную ветку» |
| decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md | D28 | «Целевая система сбора знаний под конкретную задачу более эффективна, чем универсальный сбор всей доступной информации» |
| decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md | §5 Alliance Option C | Foundation non-profit upstream (Apache 2.0 docs + LGPL-equivalent software) + Jetix-Corp proprietary downstream; Mozilla/Red Hat analog |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §5 Path B | «Jetix ships methodology + agent configs + wiki templates + setup scripts. Client hosts on own infrastructure» |
| decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md | §8 rec 3 | «Mittelstand AI Alliance = EISA moment — positioning as sovereign European AI consortium» |
| decisions/JETIX-VISION.md | §7.1 archetype 4 | Инвесторы: «pattern seekers, ищут smart bets + resource-allocation frameworks + Phase 2+ token economy + Phase 3+ $1T trajectory participation» |
| decisions/JETIX-PLAN.md | §3.8 | «не equity-based investor pitches в Phase 1. Skin-in-game (self-funded $20-30K earned) + D15 revenue-gated unlocks» |
| reports/review_2026-04-24.md | audio_524 rows 790-793 | «Люди без цифровых портретов фактически не существуют в современном мире» — educational product need; Secure Network quality-gate |
| reports/review_2026-04-24.md | audio_527 row 801 | «Jetix будет заниматься реверс-инжинирингом на максималках для своего развития и развития общества» — reverse-engineering methodology basis |
| decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md | §3.10 Teacher | «Jetix строит систему, которая превращает их в масштабируемые образовательные продукты без роста твоих часов» |
| swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md | §6 Gate diagram | G2→G3 Educational repo V1 activation; G3→G4 scale gate |

---

*Drafted by investor-expert (mode: scalability), Cell C-09, cycle cyc-layer-5-product-deep-dive-2026-04-25. Status: drafted. Awaiting brigadier §5.5.5 provenance gate + integration pass (Wave D). No Notion writes. No capital deployment. No equity terms set. HITL required for strategic investor round question (§10 Q3). L7 pricing cycle owns final offer pricing.*
