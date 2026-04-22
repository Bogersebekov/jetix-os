---
id: d4-pass1-C-locks-table
title: D4 Pass 1 — Subagent C — 24 Locked Decisions Mapped to Architectural Implications
date: 2026-04-21
type: d4-input
status: draft-pass-1
binding_sources:
  - raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md
  - raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md
---

# D4 Pass 1 — Subagent C — 24 Locked Decisions → Architectural Implications

> **Scope:** Maps each of the 24 locked decisions (8 PRE + 10 Stage 2 + 6 Stage 2B) to its binding architectural
> implication. All rows directive (Stage 6 architects consume as hard constraints).

## Numbering reconciliation note

- **8 PRE-RESOLVED** are referred to in sources as both "Decisions 1-8" AND "Tensions #1-#3 + #1/#2 numbering" — I use the canonical **Decision 1..8** numbering from `TENSIONS-PRE-RESOLVED.md` summary table.
- **10 Stage 2** are referred to as both "T1..T10" AND "Decisions 9-18" — I carry **both** in the table (`T1 → Decision 9`, `T10 → Decision 18`).
- **6 Stage 2B** are referred to as "Decisions 19-24" (no T-prefix in Stage 2B doc). I adopt **Decision 19..24**.
- **Total:** 8 + 10 + 6 = **24 locks.** No merges, no splits — each lock is distinct. Decision 23 has Ruslan-approved **Option B** (internal Phase 2, limited public Phase 3+).

---

## Section 1 — Quick-reference table (all 24 rows)

| # | Lock ID | Short Title | Formula (1 line) | Architectural Implication (1 line) | Source Doc |
|---|---|---|---|---|---|
| 1 | D1 / Tension #3 | Gentleman inside / Predator outside | Civil cooperation inside membrane; aggressive defence/stance toward external world. | System MUST bifurcate behaviour/tone/policy layer by observer-class (inside-member vs outside-world). | TENSIONS-PRE-RESOLVED.md |
| 2 | D2 / Tension #1 | Solo-now-with-team-ready-scaffolding | Operate solo today; infra must absorb 2nd/3rd pilot without refactor. | Document ownership, governance, agent authorship MUST support multi-pilot inheritance from Day 1. | TENSIONS-PRE-RESOLVED.md |
| 3 | D3 / Tension #2 | Closed outside / Open inside (team) | Closed to public; open to team/community who pass the membrane. | Repo + access architecture MUST be private-by-default with selective privileged-access tiers; no public OSS of core. | TENSIONS-PRE-RESOLVED.md |
| 4 | D4 | Name = Jetix | Single brand "Jetix"; "Jackson/Jack" was speech-recognition artefact. | All naming references / brand-objects resolve to single canonical identifier "Jetix"; no alias tooling. | TENSIONS-PRE-RESOLVED.md |
| 5 | D5 | Consulting-first Phase 1 → Secure Network Phase 2+ | Consulting is core revenue Phase 1; community chat → Secure Network is Phase 2+ evolution. | Architecture MUST be extensible from consulting-first minimum into platform without rewrite; optionality pre-wired. | TENSIONS-PRE-RESOLVED.md |
| 6 | D6 | Anton/Vladislav/Rodion — not key | No advisor/mentor layer. Remove from core docs. | No advisor/equity/ownership dependency baked into system; advisory-board slot parked. | TENSIONS-PRE-RESOLVED.md |
| 7 | D7 | Union of 10 archetypes | Merge both lists → 10 diverse archetypes as target cast. | Identity/taxonomy layer MUST support heterogeneous archetype metadata + thematic sub-networks. | TENSIONS-PRE-RESOLVED.md |
| 8 | D8 | Layered identity (multiple faces) | One entity, multiple frames per observer/phase (methodology/agency/network/club/corp/civ-infra). | System MUST support configurable face/frame presentation per observer-class + phase (multi-view rendering). | TENSIONS-PRE-RESOLVED.md |
| 9 | D9 / T1 | Pain primary + Opportunity secondary | Outbound = pain-dominant, opportunity-reinforcing; predator-drive internal only. | Content/outreach pipeline MUST tag messages with frame-type (pain/opportunity) and default pain-primary. | TENSIONS-RESOLVED.md |
| 10 | D10 / T2 | English + US first, Germany Phase 2+ | Phase 1 market = EN + US; DE/DACH activates Phase 2+; patents later. | Architecture MUST support multi-jurisdiction (US+EU) — i18n, legal-tagging, timezone, regulatory slots. | TENSIONS-RESOLVED.md |
| 11 | D11 / T3 | Consulting + Продюс-центр + Investment-fund philosophy | Phase 1 core = consulting + producer-services; investment-fund = Day-1 operating philosophy (Resource-Allocation Engine). | Resource allocation (time/attention/money) MUST be first-class primitive in agent decisions; Phase-2 absorbs ideas-platform + job-matching. | TENSIONS-RESOLVED.md |
| 12 | D12 / T4 | Smart audience + site primary + social max-TOF | Target = smart people; site+templates+PDF+video = mid/deep; social+bloggers+podcasts used at maximum as TOF only. | Content pipeline MUST tag artefacts by tier (TOF/mid/deep) and route per tier to channel; deep stays gated. | TENSIONS-RESOLVED.md |
| 13 | D13 / T5 | Open surface / Closed core | Public = results + frames + demos + templates; closed = prompts + wiki + workflows + FPF-based core. | Documentation/artefact architecture MUST split into surface (public auto-gen) vs core (access-gated) layers. | TENSIONS-RESOLVED.md |
| 14 | D14 / T6 | Research = revenue-instrumental (Phase 1) | Phase 1 research must serve revenue; philosophy/bet queries parked. | Research agents Phase 1 MUST scope-filter to revenue-instrumental queries; broaden Phase 2+. | TENSIONS-RESOLVED.md |
| 15 | D15 / T7 | Revenue-gated spend (phased unlocks) | Heavy-spend unlocks at thresholds: $20-30K → €50K → €200K → €1M. | Governance/finance model MUST enforce checkpoint→unlock pattern with explicit gates; no blank commitments. | TENSIONS-RESOLVED.md |
| 16 | D16 / T8 | Phase 1 simple chat / formal mechanics Phase 2+/3+ | Phase 1 = plain Telegram/Discord chat; Phase 2+ subscription-as-commitment + activity log; Phase 3+ tiered peer-review only if scale forces. | Community subsystem MUST start as minimal chat-adapter; Phase-2+ extends with activity-log + subscription, not scoring. | TENSIONS-RESOLVED.md |
| 17 | D17 / T9 | Filesystem = single source of truth | Git/filesystem authoritative; Notion = collaboration/UI view only. | Sync MUST be one-way (fs → Notion); any bidirectional/Notion-authoritative pattern is forbidden. | TENSIONS-RESOLVED.md |
| 18 | D18 / T10 | Productization over hours (consulting-scaling) | Scale via products/templates/community, NOT hours-billing; no conflict (own-food-eating). | Service-pipeline architecture MUST emit packaged artefacts (templates/frameworks) as first-class outputs, not just hours. | TENSIONS-RESOLVED.md |
| 19 | D19 | Holding-Scale $1T ambition | $100M → $100B → $1T (world-record speed); €50K/€200K gates stay tactical. | Infrastructure MUST be designed so Phase-3 scale requires no rewrite; scalability + observability from Day 1. | TENSIONS-RESOLVED-STAGE-2B.md |
| 20 | D20 | USB-C Positioning + Enterprise-Fast | Jetix = universal connector (AI-agents ↔ businesses ↔ specialists); structure = enterprise-fast (not solopreneur, not bloated, not chaotic). | Architecture MUST expose connector/protocol surfaces (interop interfaces) + enterprise-grade ops (fast + robust + adequate). | TENSIONS-RESOLVED-STAGE-2B.md |
| 21 | D21 | Partnership-Matchmaker + Roy-Replication | Matchmaker layer (tasks ↔ specialists, AI-smoothed) + replicable swarm-of-10 methodology (other roys emerge). | System MUST support matchmaker primitives (task/specialist graph + contract-fixation) + methodology-as-packagable-template for roy reproduction. | TENSIONS-RESOLVED-STAGE-2B.md |
| 22 | D22 | ICP Refinement: Startupper+Azart+Stable+Adequate+Upward | 10 archetypes × 5 qualitative criteria + direction-of-life axis (up only). | ICP/membership system MUST encode 5-criteria filter + direction-of-life axis (vertical up) as gate parameters. | TENSIONS-RESOLVED-STAGE-2B.md |
| 23 | D23 | Token Economy Exploration — Option B | Phase 2 internal tokens (specialist comp + ecosystem utility); Phase 3+ limited public tradeable with explicit membrane rules. | Economic-layer architecture MUST accommodate internal non-transferable tokens Phase 2; Phase 3+ gated public issuance — membrane preservation is hard constraint. | TENSIONS-RESOLVED-STAGE-2B.md |
| 24 | D24 | Open-Source Research Direction (Phase 2+) | Phase 2+ Jetix open-sources research on comms/cooperation/future-economy; core methodology stays closed per D13. | Research subsystem MUST split "open research output" (publishable) vs "closed operational methodology"; distinct pipelines from Phase 2+. | TENSIONS-RESOLVED-STAGE-2B.md |

---

## Section 2 — Detail block per lock (for Section 2 of D4)

---

### Lock 1 (D1 / Tension #3) — Gentleman inside / Predator outside

**Decision (verbatim formula):** Gentleman inside / Predator outside. Inside = civil, cooperative, knowledge-packaging, subscription value-exchange. Outside = defensive, retaliatory, aggressive market posture.

**Rationale:** Ruslan: «джентльмен inside... predator outside. Все это фиксируем». Historical parallels (Venice, Kingsman, Medici) establish that civility-inside + hardness-outside is a viable operational mode, not a contradiction.

**Binding implications for Stage 6 architects:**
- MUST distinguish observer-class at every surface (inside-member vs outside-world) with policy, tone, and access layer diverging by class.
- MUST include a **membrane** component (quality-gate + subscription) as first-class architectural element.
- MUST route messaging / UX / agent-behaviour through this inside/outside switch.
- MUST enable retaliation / defensive posture capability (legal, marketing, counter-move) without polluting inside civility.
- MUST design brand voice as dual-channel (predator voice outside, gentleman voice inside) from Day 1.

**Rules OUT:**
- NO uniform tone/policy/access across inside-outside (e.g. one Slack workspace for everyone).
- NO "always-friendly" or "always-aggressive" monolithic posture.

---

### Lock 2 (D2 / Tension #1) — Solo-now-with-team-ready-scaffolding

**Decision:** Operate solo now, but architecture ready for 2nd/3rd pilot Day 1. Onboarding = quick paste, NOT rewrite.

**Rationale:** Avoids the classic solopreneur trap (refactor-at-scale). Enables Phase-2 partner onboarding with minimal friction.

**Binding implications for Stage 6 architects:**
- Document ownership + strategic-docs governance MUST support multi-pilot inheritance (roles, permissions, co-author).
- Agent-authorship / mailbox / state MUST allow additional pilots without schema migration.
- Onboarding pathway MUST be designed explicitly (checklist, ssh/access, agent delegation).
- Strategic decisions MUST be phrased as first-class objects with permission/influence scoping per partner-per-direction (see D20).

**Rules OUT:**
- NO hard-coded single-user assumptions (e.g. paths like `/home/ruslan/*` in logic).
- NO phased "solo now → team later" migration deferred to Phase 2.

---

### Lock 3 (D3 / Tension #2) — Closed outside / Open inside (team)

**Decision:** Closed to external public. Open "as open-source" but only for privileged-access members who passed membrane. Core is always closed; public OSS of full platform is OFF the table.

**Rationale:** Ruslan: «closed outside, но для команды open». Rhymes with D1 grammar and Secure Network concept.

**Binding implications for Stage 6 architects:**
- Repo architecture MUST default private with tiered privileged-access (member/partner/core).
- Patent track permitted (no conflict with "open inside").
- Membership-gated access model MUST be Dimension D (first-class architectural axis).
- Public/private artefact split MUST be automated (generation pipeline, see D13).

**Rules OUT:**
- NO public GitHub OSS of Jetix core.
- NO "eventually we open-source" sunset clause baked into IP strategy.

---

### Lock 4 (D4) — Jetix is the name

**Decision:** Single brand = "Jetix". "Jackson/Джек" is speech-recognition artefact — always re-read as "Jetix".

**Rationale:** Ruslan explicit: «имя не меняем, это Jetix».

**Binding implications for Stage 6 architects:**
- Canonical brand identifier = "Jetix" across all surfaces.
- Jetix-search-engine feature (Secure Network membrane) exists as sub-feature, but WITHOUT its own brand name.
- Any references to "Jackson/Джек" in raw transcripts resolved to "Jetix" on ingest.

**Rules OUT:**
- NO multi-brand / alias tooling in core naming pipeline.
- NO separate sub-brand for search.

---

### Lock 5 (D5) — Consulting-first Phase 1 → Secure Network Phase 2+

**Decision:** Phase 1 = consulting (€150/hr + templates + services). Community = попутно в чате (simple). Phase 2+ = community evolves into Secure Network as primary product.

**Rationale:** Both "сообщество попутно" (Phase 1) and "Jetix = Secure Network" (Phase 2+) are valid but phase-separated.

**Binding implications for Stage 6 architects:**
- Phase-1 architecture = consulting-operations minimum viable.
- Phase-2 extension pathway MUST NOT require rewrite (community chat → Secure Network evolution).
- Community-infra work priority P3/P4 in Phase 1; rises Phase 2.
- Primary-product abstraction MUST be overridable across phases (consulting-primary → platform-primary).

**Rules OUT:**
- NO platform-first Phase-1 build (over-architect).
- NO "community doesn't matter" posture (it's parked but wired).

---

### Lock 6 (D6) — Anton/Vladislav/Rodion — not key

**Decision:** Not key advisors. Remove from all core docs. Not mentioned.

**Rationale:** Ruslan: «нет, они не ключевые, выкидываем».

**Binding implications for Stage 6 architects:**
- No advisor/mentor layer hardcoded into system.
- Advisory-board dimension PARKED (revisit only when actual advisor materializes).
- Relationships-dimension representation = accurate current reality (no phantom advisors).

**Rules OUT:**
- NO advisory/board structure in v1 architecture.
- NO equity-reservation for absent advisors.

---

### Lock 7 (D7) — Union of 10 archetypes

**Decision:** Union both lists. 10 archetypes: Предприниматели, Ресёрчеры, Инженеры, Инвесторы, Политики, Продавцы, Менеджеры/коммуникаторы, Философы, Разработчики идей, Разработчики жизни.

**Rationale:** Ruslan: «всех объединить, максимальное разнообразие». Balances think-tank depth with business execution.

**Binding implications for Stage 6 architects:**
- Identity/taxonomy layer MUST support heterogeneous 10-archetype metadata.
- Sub-network architecture MUST accommodate thematic sub-channels per archetype.
- Phase-1 ICP = narrow subset (2-3 archetypes, likely Предприниматели + Разработчики жизни); Phase-2+ broadens toward full 10.
- Archetype metadata MUST combine with D22 qualitative filter (5 criteria).

**Rules OUT:**
- NO single-archetype ICP baked in.
- NO "founders-only" / "engineers-only" architecture lock.

---

### Lock 8 (D8) — Layered identity (multiple faces)

**Decision:** Jetix = layered identity. One entity, multiple frames per observer + phase: Methodology (self), Agency (clients), Network (partners), Club (members), Corporation (world), Civ-infra (Phase 3+), Solo-with-team-ready (team Phase 1).

**Rationale:** Rhymes with D1 + D3 — context-adaptive grammar. Per-archetype angles = navigation within D1 Vision, not separate docs.

**Binding implications for Stage 6 architects:**
- System MUST support configurable face/frame presentation per observer-class + phase (multi-view rendering).
- Brand-object MUST be first-class with face/frame field.
- Per-archetype marketing artefacts (pitch-decks/manifestos/tech-briefs) = derived, NOT foundation — generated from D1 Vision.
- Dominant frame MUST be settable per phase (Phase 1 = company face; Phase 2+ = network/platform; Phase 3+ = corporation/civilization).

**Rules OUT:**
- NO monolithic brand identity (single-face presentation).
- NO static frame forever (frame must evolve with phase).

---

### Lock 9 (D9 / T1) — Pain primary + Opportunity secondary

**Decision:** Outbound messaging = pain-primary ("AI accelerates — you fall behind"), opportunity-reinforcing ("here's what's possible"). Predator-drive is internal fuel only, not messaging.

**Rationale:** Layered messaging, not either/or. Rhymes D1 (predator outside = pain messaging; gentleman inside = opportunity frame).

**Binding implications for Stage 6 architects:**
- Content/outreach pipeline MUST tag messages with frame-type (pain/opportunity).
- Default frame = pain-primary for TOF, opportunity for mid/deep.
- Agent outreach templates MUST default pain-primary with opportunity-backing.
- Internal predator-drive NOT emitted externally (metrics / tone moderation layer).

**Rules OUT:**
- NO pure-opportunity marketing (too soft).
- NO pure-predator messaging (alienates inside).

---

### Lock 10 (D10 / T2) — English + US first, Germany Phase 2+

**Decision:** Phase 1 primary market = English + US (includes UK, US, international infobiz). DE/EU = Phase 2+ expansion. DE GmbH can open Phase 1 when triggered ($20-30K) but as legal home, not market.

**Rationale:** Ruslan: «сперва English, America, потом Germany».

**Binding implications for Stage 6 architects:**
- Architecture MUST support multi-jurisdiction (US + EU): i18n, legal-tagging, timezone awareness, US California AI regs + tax.
- Phase-1 content/sales infrastructure defaults to English + US regulatory context.
- DE legal track activates at revenue threshold (see D15).
- Patent track = Phase 2+ (EU focus).

**Rules OUT:**
- NO Germany-first Phase-1 build.
- NO single-jurisdiction hard-coded assumption.

---

### Lock 11 (D11 / T3) — Consulting + Продюс-центр + Investment-fund philosophy

**Decision:** Phase 1 core = consulting + Продюсерский центр (parallel). Investment-fund = operating philosophy Day 1 (Resource-Allocation Engine). Ideas-platform + Job-matching = Phase 2+ Secure Network features.

**Rationale:** Investment-fund is frame, not product — every time/attention/money distribution = investment decision with expected return.

**Binding implications for Stage 6 architects:**
- Resource-allocation (time/attention/money) MUST be first-class primitive in agent decisions.
- Phase-1 directions: `ai-consulting-dach` + `producer-services` launch parallel.
- Secure Network Phase 2+ MUST absorb ideas-platform + job-matching without refactor.
- Every agent task MUST be evaluable via investment-ROI lens (tracking optional, lens mandatory).

**Rules OUT:**
- NO consulting-only Phase-1 scope (producer-services is co-primary).
- NO ideas-platform Phase-1 build (parked to Phase 2+).

---

### Lock 12 (D12 / T4) — Smart audience + site primary + social max-TOF

**Decision:** Target = smart. Core = site + templates + video + PDF. Social used at MAX as TOF (bloggers/podcasts/collabs/ads). "Не создавать свою соцсеть" — use existing social at max.

**Rationale:** Three-layer content: TOF (social, pain-hooks) → mid (site, templates) → deep (manifestos, Secure Network gated).

**Binding implications for Stage 6 architects:**
- Content pipeline MUST tag artefacts by tier (TOF/mid/deep) and route per tier.
- Site = primary content home; social = acquisition channel only (no own-network build).
- Deep content gated behind sign-up / subscription.
- Ad spend budget activates per D15 thresholds.

**Rules OUT:**
- NO Jetix-owned social network as product.
- NO equal-weight distribution across social and site (site must dominate as substance layer).

---

### Lock 13 (D13 / T5) — Open surface / Closed core

**Decision:** Public = cases, frames, demos, 10 free templates, public videos. Closed = prompts, FPF-based wiki, workflows, operational config, client-specific flows.

**Rationale:** Refines D3 specifically for methodology. Rhymes with D1, D12 — one grammar of context-adaptive openness.

**Binding implications for Stage 6 architects:**
- Documentation/artefact architecture MUST split into surface (public auto-gen) vs core (access-gated) layers.
- Every content piece MUST be tagged surface/mid/core at creation.
- Public-facing artefacts auto-generated from core (not duplicated, not hand-maintained in two places).
- Core layer (prompts/wiki/workflows) MUST have stricter access than membership layer.

**Rules OUT:**
- NO raw prompt sharing in public artefacts.
- NO mixing surface and core in same repo without access-gate.

---

### Lock 14 (D14 / T6) — Research = revenue-instrumental (Phase 1)

**Decision:** Phase 1 research MUST serve revenue: ICP, sales, competitors, AI-tools, pricing, industry, patents. Philosophy/civilizational/любопытство research parked.

**Rationale:** Ruslan: «research — servant of revenue, not master» (Phase 1).

**Binding implications for Stage 6 architects:**
- Research agents Phase 1 MUST scope-filter queries (revenue-instrumental whitelist).
- Phase 2+ scope broadens (philosophy, civilizational, open-source research per D24).
- Query router MUST tag research queries with phase-eligibility.

**Rules OUT:**
- NO Phase-1 deep-dives on 200-year vision, Fortune-500 coalitions, civilizational theory.
- NO uncapped research-agent wandering.

---

### Lock 15 (D15 / T7) — Revenue-gated spend (phased unlocks)

**Decision:** Heavy-spend unlocks at thresholds: $0→$20-30K (essentials), →€50K (GmbH, Stripe, legal basic), →€200K validation (patents EU, 1-2 hires), →€1M (revenue-share × 3-5, team 5-10), →€1M+ (investment-fund full scale).

**Rationale:** Ruslan: «revenue-gated spend, подтверждаю». Each unlock = verifiable checkpoint.

**Binding implications for Stage 6 architects:**
- Governance/finance model MUST enforce checkpoint→unlock pattern with explicit gates.
- Every unlock action MUST be checkpoint-bound (no blank commitments).
- System MUST track revenue cumulative and gate-state; agent-proposals block at thresholds.
- Gates: $20-30K, €50K, €200K, €1M — encoded as config.

**Rules OUT:**
- NO pre-revenue heavy commitments (patents, large hires, agency retainer).
- NO skipping checkpoints on optimism.

---

### Lock 16 (D16 / T8) — Phase 1 simple chat / formal mechanics Phase 2+/3+

**Decision:** Phase 1 = Telegram/Discord simple chat, invite-based, no formal anti-free-riding. Phase 2+ = subscription (baseline commitment filter, ~70% free-riding solved) + public contribution visibility + reputation signals + renewal checkpoints. Phase 3+ = tiered peer-review ONLY if scale (1000+) forces it.

**Rationale:** Simpler-first; formalization follows scale forcing-function.

**Binding implications for Stage 6 architects:**
- Community subsystem MUST start as minimal chat-adapter (Telegram/Discord).
- Phase-2+ extension adds activity-log + subscription + renewal hooks — NOT scoring.
- Phase-3+ tiered membership = contingent on scale trigger (do not build preemptively).
- Invite-based gate = Phase 1 membrane mechanism.

**Rules OUT:**
- NO Phase-1 formal reputation/scoring system.
- NO Phase-2+ gamification or point-based ranks.

---

### Lock 17 (D17 / T9) — Filesystem = single source of truth

**Decision:** Git/filesystem = authoritative. Notion = collaboration/planning/UI view only. Conflict → filesystem wins.

**Rationale:** Ruslan: «Notion убирай как Source of Truth». Reflected in CLAUDE.md update.

**Binding implications for Stage 6 architects:**
- Sync MUST be one-way (filesystem → Notion), NEVER bidirectional.
- Notion pages = auto-generated or advisory views, NEVER write-back to fs.
- Onboarding MUST point to git repo, not Notion.
- All D6/D9/ADR/wiki references to "Notion = external truth" REQUIRE Stage 6 architects revisit + update.

**Rules OUT:**
- NO bidirectional Notion↔fs sync tooling.
- NO Notion-authoritative decisions/artefacts.

---

### Lock 18 (D18 / T10) — Productization over hours

**Decision:** Consulting risks (hour-trap / scale / conflict-of-interest) mitigated via productization: templates, 4-pack offer (session + 10 templates + community + services), Phase 2+ Secure Network subscription = recurring. "Ruslan ест свой food" — methodology applied to Jetix-company itself (no conflict).

**Rationale:** Consulting = entry layer; productization = scale layer.

**Binding implications for Stage 6 architects:**
- Service-pipeline architecture MUST emit packaged artefacts (templates, frameworks, PDFs) as first-class outputs.
- Pricing model MUST support multiple tiers (session, template pack, subscription) — NOT hour-only.
- "Own-food-eating" MUST be architectural: Jetix methodology instrumented and applied to Jetix itself (dogfooding loop).
- Skin-in-game / revenue-share partnerships (Phase 2) = wired in.

**Rules OUT:**
- NO hours-billing-only revenue architecture.
- NO consultant-advice-without-dogfooding split.

---

### Lock 19 (D19) — Holding-Scale $1T Ambition

**Decision:** Jetix aims at WORLD-RECORD speed to $1T market cap. Milestones: €50K → €200K → $100K → $100M → $100B → $1T. Tactical gates (Phase 1 €50K / €200K validation) remain; $1T is strategic trajectory informing architecture.

**Rationale:** Backed by real tools, adequate team, infra, founder commitment + roy-replication (D21). XEI precedent ($100B in 2 years).

**Binding implications for Stage 6 architects:**
- Infrastructure MUST be scalable by design — Phase-3 scale requires NO rewrite.
- Observability, governance, agent-orchestration MUST handle 10^3-10^6 scale patterns (not explicit load, but schema-ready).
- Architecture decisions Phase 1 evaluated against "does this allow $1T-scale without refactor?"
- $100M / $100B intermediate milestones encoded as Phase 3 sub-gates.

**Rules OUT:**
- NO "good enough for Phase 1" shortcuts that forbid Phase-3 scale (e.g. SQLite-forever, single-region hardcode).
- NO architecture that caps at boutique-agency scale.

---

### Lock 20 (D20) — USB-C Positioning + Enterprise-Fast

**Decision:** Jetix = USB-C level universal connector in AI-agents ↔ businesses ↔ specialists space. Structure = enterprise-fast corporation (NOT One-Person-Company, NOT One-Million boutique, NOT slow-corporate, NOT chaotic-startup). Scale: мультимиллиарды, international.

**Rationale:** Positioning principle. Enterprise power + startup speed + robustness + adequacy.

**Binding implications for Stage 6 architects:**
- Architecture MUST expose connector/protocol surfaces (interop interfaces) for AI-agent-to-business and B2B coordination.
- Contract-verification layer (humans can't verify AI-to-AI contracts at scale → Jetix tools).
- Ops tier = enterprise-grade (fast + robust + adequate), not solopreneur-grade.
- Interop interfaces MUST be designed so Jetix becomes standards-level (not monopoly).

**Rules OUT:**
- NO solopreneur-style single-agent monolith.
- NO slow-corporate dryness (IBM/McKinsey patterns).
- NO chaotic-startup move-fast-break-things patterns in core infra.

---

### Lock 21 (D21) — Partnership-Matchmaker + Roy-Replication

**Decision:** Jetix = matchmaker (tasks ↔ specialists, AI-smoothed, contract-fixation). Plus: roy (swarm-of-10) replicable methodology — Jetix builds own roy first ($10M-$100M), methodology packaged, other roys emerge in other niches/countries/verticals, inter-roy communication + joint projects, Jetix = meta-coordinator.

**Rationale:** Extends D11 investment-fund philosophy. Each roy = portfolio unit. 100 roys × $10M-$100M = $1B-$10B + methodology multiplier.

**Binding implications for Stage 6 architects:**
- System MUST support matchmaker primitives: task/specialist graph + capability matching + contract fixation.
- Methodology MUST be package-able as replicable template (methodology-as-system).
- Inter-roy communication protocols = first-class Phase 3+ primitive.
- Specialists NOT "owned" by Jetix — portal connection, adequate coordination.
- Talent-magnet pathway (adequate specialists transition into Jetix optional).

**Rules OUT:**
- NO monolithic one-company architecture without swarm abstraction.
- NO hard-coupled specialist employment model.

---

### Lock 22 (D22) — ICP Refinement: Startupper + Azart + Stable + Adequate + Upward-Direction

**Decision:** ICP = 10 archetypes (D7) × 5 qualitative criteria (startupper mindset + предпринимательский азарт + stable + adequate + upward-direction) + direction-of-life axis (vertical up, NOT horizontal topics). NOT mass, NOT motivational-circle. Self-selection via "авантюра века" framing.

**Rationale:** Ruslan explicit: "прям несколько страниц как минимум" in D1. Direction-of-life axis is NEW dimension.

**Binding implications for Stage 6 architects:**
- ICP/membership system MUST encode 5-criteria filter + direction-of-life axis (vertical up) as gate parameters.
- Invite mechanism (Phase 1) + subscription + framing (Phase 2+) as self-selection tools.
- Archetype metadata COMBINES with 5-criteria filter (archetype × quality-filter).
- D1 Vision §7 = multi-page ICP section (Ruslan directive).

**Rules OUT:**
- NO mass-market / Oriflame-style onboarding.
- NO topic-only segmentation (direction-of-life primary over topic).
- NO motivational-circle vibe.

---

### Lock 23 (D23) — Token Economy Exploration (Phase 2+) — Option B default (approved)

**Decision:** Phase 2+ (trigger $100K self-earned): Jetix token/currency exploration for (a) specialist compensation, (b) ecosystem economic layer, (c) alternative-to-IPO liquidity. Safe, adequate, thoughtful — NOT crypto-pump. **Option B approved default:** Phase 2 internal non-transferable tokens; Phase 3+ limited public tradeable with explicit membrane rules.

**Rationale:** Natural instrument for $1T trajectory (D19) + investment-fund (D11). Membrane preservation (D3 + D13) = hard constraint.

**Binding implications for Stage 6 architects:**
- Economic-layer architecture MUST accommodate internal non-transferable tokens Phase 2.
- Phase 3+ public issuance = gated, with economic-claim only, NO governance/community-access rights leaking.
- Token design MUST preserve D3 membrane — blurring is forbidden.
- Distribution rules MUST be safe + specialist-friendly + legally-compliant, jurisdiction-aware.
- $100K trigger = encoded as gate (see D15 pattern).

**Rules OUT:**
- NO crypto-pump / meme-coin / speculation-only design.
- NO public token with governance/community rights bundled (membrane-blurring).
- NO Phase 1 token activity (D14 revenue-instrumental + phase gating).

---

### Lock 24 (D24) — Open-Source Research Direction (Phase 2+)

**Decision:** Phase 2+ activates open-source research: how humans communicate, how companies should cooperate, how future economy should work. Jetix = leading contributor, benefits from first-mover data + thought-leadership + talent attraction. Core methodology (consulting, Продюс-центр, Secure Network ops) STAYS CLOSED per D13.

**Rationale:** Research direction = surface layer (not operationally competitive). Depth of research is natural moat ("мозгового времени хватит" to copy).

**Binding implications for Stage 6 architects:**
- Research subsystem MUST split "open research output" (publishable) vs "closed operational methodology" — distinct pipelines from Phase 2+.
- Open licensing (MIT / Apache / specific open) on research artefacts; NOT on methodology.
- D13 surface/core table MUST be extended (post-approval) to list research-direction as surface item.
- Phase-1 research stays D14 revenue-instrumental; Phase 2+ adds dedicated research-direction team/agents.
- Phase 3+ maturation = possible institutional research direction (papers, conferences, standards).

**Rules OUT:**
- NO Phase-1 open-source research activity (D14 revenue-instrumental only).
- NO open-sourcing of operational methodology (consulting flows, client-specific workflows, Secure Network ops).

---

## Summary counts

- Total locks: **24** (8 PRE + 10 Stage 2 + 6 Stage 2B)
- No merges, no splits — each proposed Decision retained as distinct lock.
- Stage 2B Decision 23 = Option B (approved) locked explicitly.
- All 24 map to directive architectural implications for Stage 6 architects.
