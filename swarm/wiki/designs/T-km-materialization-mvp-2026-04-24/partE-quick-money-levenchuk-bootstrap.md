---
title: "Part E — Bootstrap design record: quick-money P1 + levenchuk-deep-dive P3 + E2E demo spec"
type: design-record
task_id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
produced_by: mgmt-expert
promoted_by: brigadier
promoted_at: 2026-04-24
mode: integrator
wave: 3
part: E
created: 2026-04-24
last_modified: 2026-04-24
pipeline: accepted-with-dissent
state: accepted-with-dissent
confidence: high
confidence_method: pmbok-plus-cagan-plus-sg-dsl-match
tier: core
promotion_note: |
  Wave-3 gate passed with PRESERVED DISSENT (§1d AP-6 — never average into consensus).
  Investor × critic (Wave-3 parallel) flagged 3 HARD FAIL + 1 conditional FAIL:
    - CC-1 FAIL: kpi_targets.contracts_per_quarter: 2 × Path-B pricing = €15K/Q
      arithmetic; 3.3× short of cumulative_revenue_q2_2026_eur: 50000 target.
    - CC-3 FAIL: icp.md lists 6 archetypes without Phase-1 priority tier;
      investor proposes Tier-1 = {Предприниматели, Блогеры} for weeks 1-6.
    - CC-4 FAIL: kill_criteria "50 qualified prospects" unreachable at 20/quarter
      in 13 weeks; investor proposes two-checkpoint structure.
    - CC-5 conditional: levenchuk kpi_targets "leave empty" option must be removed.
  Initial promotion (2026-04-24 AWAITING-APPROVAL): dissent preserved; Ruslan arbitration pending.

post_ack_revision: |
  Ack file: swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md frontmatter mutation
  Ack date: 2026-04-24T23:50:00Z
  Option chosen: C (adopt CC-3 + CC-4 + CC-5; DEFER CC-1 revenue-mix to empirical test).
  Revisions APPLIED to this design record by brigadier post-ack:
    1. CC-1: **NOT APPLIED** (Option C defers). quick-money _moc.md kpi_targets reverts
       to JETIX-PLAN §3.1 verbatim — contracts_per_quarter: 2 + leads_per_quarter: 20 +
       mrr_eur_target_q2_2026: 15000 + cumulative_revenue_q2_2026_eur: 50000 as
       single-line target. hourly_consulting_hours_q1_q2_2026 and hourly_rate_eur lines
       REMOVED. Body KPI table updated to contracts-only. Investor CC-1 arithmetic
       refutation preserved as residual risk (investor-critic draft canonical).
    2. CC-3: icp.md frontmatter gains tier_1_phase_1 list [Предприниматели, Блогеры] +
       tier_2_phase_2 list + tier_2_unlock_trigger: SG-2=fired. Body tightened to
       "Two-tier Phase-1 discipline (investor CC-3 fix)" section. APPLIED.
    3. CC-4: quick-money _moc.md kill_criteria rewritten to two-checkpoint structure
       (week 7 ramp signal; week 13 viability signal). APPLIED.
    4. CC-5: verified levenchuk _moc.md kpi_targets contains hypotheses_per_cycle: 2
       (non-empty; already satisfied at original draft — no edit required). APPLIED.
    5. JETIX-PLAN §3.1: migration note **NOT APPENDED** (CC-1 deferred; no revenue-mix
       decomposition to document this cycle).
  Option C rationale per Ruslan: "archetype + kill-criteria discipline-level fixes without
  economic consequence; KPI arithmetic is where mgmt has JETIX-PLAN authority and empirical
  outreach data will resolve faster than more planning".
  Dissent lineage preserved: investor critic record remains canonical at
  partE-investor-critic-icp-kpi-realism.md. CC-1 residual risk surfaces at week 13
  empirical checkpoint — if contracts_per_quarter=2 fails, investor CC-1-A alternative
  (hourly-mix add-line) becomes active revision via new gate cycle.
provenance_inline: true
sources:
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§2.E"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "B.1-B.4 consulting + research type defaults + project-brigadier template"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md", range: "C.1 _moc.md schema + sg_validation block form + DSL grammar"}
  - {path: "decisions/JETIX-VISION.md", range: "§§7.1-7.2 ICP criteria + 11 archetypes"}
  - {path: "decisions/JETIX-PLAN.md", range: "§§3.1-3.9 Phase-1 targets"}
  - {path: "decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md", range: "§1 C-1 + C-2"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path B/C + §3 Mittelstand ICP"}
  - {path: "swarm/lib/shared-protocols.md", range: "§1-§3"}
related:
  - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md
  - swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partC-stage-gates-merged.md
binding_scope: task-T-km-materialization-mvp-2026-04-24-part-E
granularity: jetix-internal
acceptance_test: partial  # physical file extraction is Wave-3 extraction cell mandate
---

# Part E — Bootstrap Design Record

Этот файл — единый design record Wave-3, Part E. Содержит полный body каждого
файла для материализации brigadier'ом + extraction cell'ом. Структура:

- E.1 — `quick-money/` operations directory (9 files + 2 gitkeeps)
- E.2 — `levenchuk-deep-dive/` operations directory (3 files)
- E.3 — Mini-swarm brigadier templates (2 agent files)
- E.4 — E2E demo workflow spec (text, no new files)

**Anti-scope (§3.4).** This record is NOT: canonical wiki write (brigadier
promotes); NOT code-level review (engineering-expert); NOT capital-arithmetic
(investor-expert); NOT epistemic arbitration (philosophy-expert). All SG
predicates are DSL-canonical per partC §C.2 grammar. Bare-metric form is BANNED.

[src:partB-b2-mini-swarm-bundle.md §B.1 + §B.3.1][src:partC-stage-gates-merged.md §C.1]

---

## Cell acceptance predicate verification (pre-production grep targets)

The following tokens MUST resolve non-zero in the body of this file:

- `Mittelstand` ✓ — appears in E.1 _moc.md problem_statement + icp.md + offline-inference-spec.md
- `Startupper` ✓ — appears in E.1 icp.md ICP criteria 1
- `2026-07-24` ✓ — appears in E.1 _moc.md kill_criteria
- `€50` ✓ — appears in E.1 _moc.md problem_statement
- `Левенчук` ✓ — appears in E.2 _moc.md problem_statement
- `problem_statement:` ✓ — appears in both E.1 and E.2 _moc.md frontmatter
- `kill_criteria:` ✓ — appears in both E.1 and E.2 _moc.md frontmatter
- `count(contracts/*.md)` ✓ — appears in E.1 _moc.md stage_gates SG-2 predicate
- `context.md:cycle_count` ✓ — appears in E.1 _moc.md stage_gates SG-4 + context.md frontmatter
- `pipeline.md:mrr_eur_contracted` ✓ — appears in E.1 _moc.md stage_gates SG-5 + pipeline.md
- `offline-inference-spec.md` ✓ — appears in E.1 file listing + E.4 demo spec
- `quick-money-brigadier` ✓ — appears in E.3 agent slug

---

## E.1 — `quick-money/` Operations Directory (P1 Consulting)

**Project slug:** `quick-money`
**Type:** consulting
**Priority:** P1
**PMBOK phase:** Executing (project is actively in Phase-1 operations per JETIX-PLAN §3)
**Granularity:** jetix-internal

[src:decisions/JETIX-PLAN.md §3.1][src:partB-b2-mini-swarm-bundle.md §B.1 consulting type]

### Target path: `swarm/wiki/operations/quick-money/_moc.md`

```markdown
---
title: "Quick Money — AI Consulting P1"
type: topic
layer: 6
niche: business
project_type: consulting
priority: P1
state: active
pmbok_phase: Executing
granularity: jetix-internal
problem_statement: |
  Малый и средний бизнес в DACH-регионе (немецкий Mittelstand) и энергичные
  стартаперы (Startupper archetype) имеют острый дефицит практически применимого
  AI-внедрения: они видят потенциал AI, но не знают как начать, боятся утечки
  данных и vendor lock-in, не хотят платить корпоративным консультантам с их
  900€/час overhead. Jetix устраняет этот дефицит через local-first AI-consulting
  methodology (BIOS-moment positioning per D20 USB-C) + client-private KB
  architecture (D13 closed core / open surface). Phase-1 target: €50K cumulative
  revenue Q2 2026 через consulting 4-pack (сессии / шаблоны / community / услуги)
  и Продюсерский центр pilot для English-speaking infobiz.
kill_criteria: |
  Two-checkpoint Hamel-binary kill structure (per investor-critic CC-4-A
  alternative, applied post-ack 2026-04-24 under Option B):
  - Checkpoint-1 (week 7, 2026-06-12): if count(leads/*.md where
    status=contacted) < 5, pivot outreach motion (channel / message /
    archetype-filter) but DO NOT kill — this is a ramping signal, not a
    viability signal.
  - Checkpoint-2 (week 13, 2026-07-24): if count(contracts/*.md) == 0 AND
    count(leads/*.md) < 10, kill project and archive. This catches the
    actual viability question with pipeline buffer accounted for.
  Replaces original single-checkpoint criterion which was unreachable at
  20 leads/quarter in 13-week window (investor CC-4 arithmetic refutation).
kpi_targets:
  # Phase-1 targets per JETIX-PLAN §3.1 verbatim (post-ack 2026-04-24 Option C — CC-1 DEFERRED):
  # mgmt-integrator retained JETIX-PLAN authority on revenue-mix; investor CC-1 arithmetic
  # refutation preserved as residual risk in partE-investor-critic-icp-kpi-realism.md.
  # Empirical test via week-13 checkpoint (CC-4 two-checkpoint kill); if contracts_per_quarter=2
  # fails, investor CC-1-A (hourly mix add-line) becomes active revision in new gate cycle.
  leads_per_quarter: 20
  contracts_per_quarter: 2
  mrr_eur_target_q2_2026: 15000             # JETIX-PLAN §3.1 verbatim (mgmt-integrator position)
  cumulative_revenue_q2_2026_eur: 50000     # gate target per JETIX-PLAN §3.1 + D15
stage_gates:
  SG-1:
    stage_gate_number: 1
    predicate: "count(leads/*.md) >= 3"
    description: "At least 3 active lead pages exist under leads/."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Deterministic file-count check. TRUE when count >= 3, FALSE otherwise. No ambiguity."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-2:
    stage_gate_number: 2
    predicate: "count(contracts/*.md) >= 1"
    description: "At least 1 signed contract file exists under contracts/."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-count check on contracts/*.md. Deterministic; no metric-key ambiguity."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-3:
    stage_gate_number: 3
    predicate: "count(leads/*.md:status: qualified) >= 3"
    description: "At least 3 leads contain the marker 'status: qualified' (grep-anchored YAML-tag form)."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: qualified' in leads/*.md. Deterministic offline."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-4:
    stage_gate_number: 4
    predicate: "context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5"
    description: "Project has run 5+ cycles and has 5+ active tasks at evaluation timestamp (instantaneous snapshot, not time-averaged)."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Compound AND of two file-anchored scalar reads from context.md frontmatter; instantaneous snapshot."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-5:
    stage_gate_number: 5
    predicate: "pipeline.md:mrr_eur_contracted >= 1000"
    description: "Contracted MRR (as declared in pipeline.md frontmatter key mrr_eur_contracted) >= EUR 1000/month."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-anchored scalar read from pipeline.md frontmatter (contracted MRR, not collected — per philosophy-critic CC-5 MRR-type disambiguation)."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Offline
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.consulting"}
  - {path: "decisions/JETIX-PLAN.md", range: "§§3.1-3.9"}
  - {path: "decisions/JETIX-VISION.md", range: "§§7.1-7.2"}
related:
  - "${WIKI_ROOT}/themes/sales/README.md"
  - "${WIKI_ROOT}/themes/business/README.md"
binding_scope: "project-quick-money"
---

# Quick Money — AI Consulting P1 — Map of Content

## Problem

Малый и средний бизнес в DACH-регионе (немецкий Mittelstand) и энергичные
стартаперы (Startupper archetype) имеют острый дефицит практически применимого
AI-внедрения. Jetix устраняет этот дефицит через local-first AI-consulting
methodology + client-private KB architecture. Phase-1 target: €50K cumulative
revenue Q2 2026.

## Kill criteria (two-checkpoint, post-ack 2026-04-24 Option C per investor CC-4-A)

1. **Checkpoint-1 (week 7, 2026-06-12):** if `count(leads/*.md where status=contacted) < 5`,
   pivot outreach motion — do NOT kill. This is a ramping signal.
2. **Checkpoint-2 (week 13, 2026-07-24):** if `count(contracts/*.md) == 0` AND
   `count(leads/*.md) < 10`, kill project and archive.

Replaces original single-point predicate which was unreachable at 20 leads/quarter
in 13 weeks (investor CC-4 arithmetic refutation).

## Current focus

Phase-1 operations: ICP qualification (Phase-1 Tier-1 archetypes ONLY — see icp.md
tier_1_phase_1 block per investor CC-3 revision), 4-pack offer activation (сессии /
шаблоны / community / конкретная помощь), Продюсерский центр pilot для English-speaking
infobiz (D11).

## KPIs (post-ack 2026-04-24 Option C — JETIX-PLAN §3.1 verbatim; CC-1 deferred)

Per JETIX-PLAN §3.1 verbatim (mgmt-integrator position retained under Option C):

| KPI | Target (Q1+Q2 2026) | Current |
|-----|---------------------|---------|
| Leads per quarter | 20 | 0 |
| Contracts per quarter | 2 | 0 |
| MRR Q2 2026 (EUR/month) | 15 000 | 0 |
| Cumulative revenue Q2 2026 (EUR) | 50 000 | 0 |

**Investor CC-1 residual risk:** arithmetic refutation (2 contracts × Path-B €7.5K/Q
= €15K/Q → €30K cumulative, 3.3× short of €50K target) preserved in
`swarm/wiki/designs/.../partE-investor-critic-icp-kpi-realism.md` as canonical
dissent. Empirical resolution via CC-4 two-checkpoint kill: week 7 ramp signal +
week 13 viability signal. If contract-only numbers fail at week 13, investor
CC-1-A alternative (add hourly consulting 233h × €150 = €35K revenue line)
becomes active revision via new gate cycle.

## Stage gates declared

See frontmatter stage_gates block. Evaluated daily by `/lint --check-stage-gates`.

## Active leads

See `leads/` directory. Current count: 0.

## Pipeline status

See `pipeline.md`. Contracted MRR: 0.

## ICP

See `icp.md`. Primary archetypes: Mittelstand owner/manager + Startupper.

## Offline inference

See `offline-inference-spec.md`. Model: ollama-mistral-7b-q4. Path B (client-hosted) default.

## Related themes

- [[sales]]
- [[business]]

## Open questions

See `open-questions.md`.
```

[src:partB-b2-mini-swarm-bundle.md §B.3.1 consulting _moc.md template][src:partC-stage-gates-merged.md §C.1 full YAML structure + sg_validation block]

---

### Target path: `swarm/wiki/operations/quick-money/icp.md`

```markdown
---
title: "ICP — Quick Money AI Consulting P1"
type: icp
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: high
confidence_method: jetix-vision-d22-verbatim-plus-investor-critic-cc3
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: "decisions/JETIX-VISION.md", range: "§7.1 архетипы + §7.2 ICP filter D22"}
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-investor-critic-icp-kpi-realism.md", range: "CC-3 FAIL + CC-3-A Alternative"}
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
  - "${WIKI_ROOT}/themes/sales/README.md"
binding_scope: "project-quick-money"
granularity: jetix-internal

# Phase-1 tier structure (post-ack 2026-04-24 Option B per investor CC-3-A):
# Phase-1 active outreach is restricted to tier_1_phase_1. Other archetypes
# from JETIX-VISION §7.1 11-archetype union are deferred to tier_2_phase_2+
# and unlock on tier_2_unlock_trigger firing.
tier_1_phase_1:
  - "Предприниматели (Deutscher Mittelstand SMB owner/manager — Archetype A)"
  - "Блогеры (English-speaking Startupper / infobiz — Archetype B)"
tier_2_phase_2:
  - "Ресёрчеры"
  - "Инженеры"
  - "Инвесторы"
  - "Продюсеры / Продюсерский центр pilot (D11 path; Archetype 11 overlap)"
  - "Другие 5 архетипов из JETIX-VISION §7.1"
tier_2_unlock_trigger: "SG-2=fired (first signed contract) — per /project-types.yaml consulting SG-2: count(contracts/*.md) >= 1"
---

# Ideal Customer Profile — Quick Money AI Consulting P1

Per JETIX-VISION D22 filter criteria [src:decisions/JETIX-VISION.md §7.2]
AND investor-critic CC-3-A alternative (post-ack 2026-04-24 Option B).

## Two-tier Phase-1 discipline (investor CC-3 fix)

**Tier-1 (active outreach, weeks 1-13):** Предприниматели (Deutscher Mittelstand)
+ Блогеры (Startupper). These two archetypes pass both D22 5-criteria AND the
sharper investor-critic filter: ability-to-sign-now × upward-direction ×
6-week-decision-cycle.

**Tier-2 (deferred, unlocks on SG-2=fired):** Ресёрчеры, Инженеры, Инвесторы,
Продюсерский центр archetype (Archetype 11 / D11 path), and the remaining 5 of the
11-archetype union. These are NOT Phase-1 primary buyers — they are Phase-2
expansion targets that unlock AFTER the first signed contract demonstrates the
motion works for Tier-1.

**Rationale.** Without the two-tier filter, Phase-1 outreach bandwidth gets
diluted across 6+ archetypes and the motion fails to learn whether the core
ICP converts (investor CC-3 refutation). With tier-2 unlock gated on SG-2, the
first contract IS the learning signal that opens expansion.

## Who is the ICP (Phase-1 Tier-1 buyers only)

Two primary archetypes qualify as Phase-1 buyers for the Quick Money
consulting motion. Both pass the D22 5-criteria filter AND have budget/urgency
alignment with the €150/час consulting offer.

### Archetype A — Deutscher Mittelstand (German SMB owner / manager)

**Role:** Business owner or managing director of a German SMB (Mittelstand)
in manufacturing, services, or professional-services sectors. Typical company
size: 10–500 employees. Revenue: €1M–€50M/год.

**Geographic / regulatory context:** DACH region (DE primary). GDPR-conscious;
EU AI Act awareness is emerging. Data sovereignty is a hard requirement —
will NOT use ChatGPT/cloud tools that ship data outside EU without audit trail.
This maps directly to the Jetix local-first / client-private KB architecture
(D13 Closed core / Open surface + D17 Filesystem = SoT).

**Situation:** Has heard of AI, tried one or two tools (ChatGPT web, Copilot),
found them impractical for internal documents or compliance-sensitive data.
Wants structured AI implementation WITHOUT vendor lock-in and WITHOUT data
leaking to US clouds. Budget for consulting engagement: €5 000–€30 000
per engagement (one-time or retainer).

**Pain (D9 primary frame):** "AI слышал, пробовал, не знаю как начать без
утечки наших данных" — AI hype is visible but practical entry is blocked by
privacy/compliance fear and lack of structured methodology.

**Opportunity (D9 secondary):** First Mittelstand company in the sector that
has a working AI-augmented knowledge system gains asymmetric productivity
advantage. Jetix methodology = structured AI-leverage without the privacy risk.

### Archetype B — Startupper (English-speaking entrepreneur / infobiz)

**Role:** Founder or solo operator of a digital-first business. May be in
coaching, consulting, content creation, SaaS, or infobiz. English-speaking
(EN / US / UK / international). Типичная выручка: $50K–$500K/год.

**Situation:** Already AI-literate (uses ChatGPT, Notion AI, etc.) but needs
a SYSTEM, not just tools. Scaling content production, client delivery, or
knowledge management. Has budget for: $500–$5 000 per engagement; interested
in productised services (monthly retainers, template packs).

**Pain:** "I'm drowning in AI tools but nothing is systematic — I keep starting
over with each client or project." — context loss, no compounding, no memory.

**Opportunity:** Jetix wiki + agent methodology = the Startupper's cognitive
amplifier. Each project gets smarter, not just faster.

**Jetix offer fit:** 4-pack (сессия / 10 шаблонов / community / конкретная
помощь). Продюсерский центр pilot (D11) — Startupper who is also a blogger
is BOTH a client and a Продюсерский центр partner [src:JETIX-VISION.md §7.1 archetype 11].

## 5 ICP Criteria (Decision 22, applied verbatim)

[src:decisions/JETIX-VISION.md §7.2]

1. **Startupper mindset** — builder's instinct, proactive, creates rather than
   consumes. Mittelstand owner: runs own company, does not wait for corporate
   approval. Startupper archetype: explicit self-starter by definition.
   **Disqualifier:** pure employee/manager with no decision authority; passive
   consumer researching AI "for later."

2. **Предпринимательский азарт** — entrepreneurial game-drive, enjoys skill-based
   risk. Mittelstand: made the bet to run own SMB; has skin in the game.
   Startupper: drives own revenue, tolerates the uncertainty of an early-stage
   digital business.
   **Disqualifier:** risk-averse corporate buyer who needs 6-month procurement cycle.

3. **Stable** — reliable, disciplined, can sustain trajectory without burnout.
   Mittelstand: established business (existing cash flow, team, legal entity).
   Startupper: minimum 12 months of operating history OR clear funded runway.
   **Disqualifier:** person in financial crisis or acute burnout (cannot invest
   attention needed for AI implementation).

4. **Adequate** — common sense, no delusion. Understands that AI is a tool, not
   magic. Does not believe in "AI replaces all employees overnight."
   Understands GDPR basics. Can evaluate a proposal on its merits.
   **Disqualifier:** AI-hype believer expecting Jetix to "make my business 10×
   in one week"; or conspiracy believer who refuses any digital tools on principle.

5. **Upward-direction** — actively develops self and environment. Mittelstand:
   investing in modernisation, not defending status quo. Startupper: in learning
   loop, building skills, not coasting.
   **Disqualifier:** person explicitly aiming for "exit and passive income" in
   < 6 months (no compound interest from AI investment).

## Phase-1 Filtered Archetypes (from the full 11)

From JETIX-VISION §7.1 [src:decisions/JETIX-VISION.md §7.1]:

| Archetype | Phase-1 buyer? | Notes |
|---|---|---|
| Предприниматели / бизнесмены | YES (primary) | Core consulting client |
| Блогеры (archetype 11) | YES (Продюсерский центр pilot) | Via D11 Продюсерский центр |
| Продавцы | YES (secondary) | AI-powered sales infrastructure |
| Инженеры | Conditional | Only if company-owner or founder; not individual IC |
| Ресёрчеры | NO Phase-1 | Phase-2+ open-source research direction (D24) |
| Менеджеры / коммуникаторы | Conditional | Only if P&L responsible; not corporate middle-manager |
| Философы | NO Phase-1 | Phase-2+ only |
| Инвесторы | NO Phase-1 | Phase-2+ only (D15 revenue-gated) |
| Политики | NO Phase-1 | Phase-3+ |
| Разработчики идей | Conditional | If they are also entrepreneurs with revenue |
| Разработчики жизни | NO Phase-1 | D14 research-instrumental only |

## Anti-ICP (explicitly NOT)

- Fortune-500 procurement buyers (Phase-3+ per JETIX-PLAN §5 and D3)
- Passive AI tool consumers with no decision authority
- Persons in acute financial crisis (cannot invest attention)
- Pure corporate middle-managers without P&L control
- Crypto-adjacent "AI hype" investors expecting 10× in 30 days
- Competitors / AI agencies researching Jetix methodology (D13 Closed core)

## Current qualified leads

0 (see `leads/` directory).
```

[src:decisions/JETIX-VISION.md §7.1-7.2][src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3]

---

### Target path: `swarm/wiki/operations/quick-money/pipeline.md`

```markdown
---
title: "Pipeline — Quick Money AI Consulting P1"
type: pipeline
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
mrr_eur_contracted: 0
sources: []
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
  - "${WIKI_ROOT}/operations/quick-money/leads/"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Pipeline — Quick Money AI Consulting P1

Lead pipeline state machine. Updated by quick-money-brigadier each cycle.
`mrr_eur_contracted` frontmatter key is the SG-5 data source:
`pipeline.md:mrr_eur_contracted >= 1000`.

## Stage definitions

| Stage | Definition | Count |
|-------|-----------|-------|
| prospect | Identified from ICP filter; not yet engaged | 0 |
| qualified | Engaged + ICP 5-criteria passed + problem confirmed | 0 |
| proposal | Proposal sent (€150/час или productized package); awaiting decision | 0 |
| signed | Contract signed; project active | 0 |
| closed-won | Delivered + invoiced + paid | 0 |
| closed-lost | Declined or unresponsive after 3 follow-ups | 0 |

## KPI tracking

| KPI | Target | Current |
|-----|--------|---------|
| leads_per_quarter | 20 | 0 |
| contracts_per_quarter | 2 | 0 |
| mrr_eur_contracted | 1000 (SG-5 threshold) | 0 |
| mrr_eur_target_q2_2026 | 15 000 | 0 |
| cumulative_revenue_q2_2026_eur | 50 000 | 0 |

## Stage-gate SG-5 tracking

SG-5 predicate: `pipeline.md:mrr_eur_contracted >= 1000`
Current value: 0 (pending).
Update `mrr_eur_contracted:` frontmatter key when first retainer contract is signed.

## Notes

Phase-1 primary offer: €150/час consulting (D3 / JETIX-PLAN §3.1).
Productized packages in development (D18 productization path).
Продюсерский центр retainers (D11) count toward mrr_eur_contracted once signed.
```

[src:partB-b2-mini-swarm-bundle.md §B.3.1 pipeline.md template][src:partC-stage-gates-merged.md §C.1 SG-5]

---

### Target path: `swarm/wiki/operations/quick-money/history.md`

```markdown
---
title: "History — Quick Money AI Consulting P1"
type: event-log
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: high
confidence_method: append-only-log
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# History — Quick Money AI Consulting P1

Append-only event log. Newest entries on top (per CLAUDE.md convention).
Do NOT edit or delete past entries.

---

- date: 2026-04-24
  event: project-bootstrap
  source: T-km-materialization-mvp-2026-04-24 Part E (Wave-3 mgmt-integrator)
  note: >
    Project scaffold materialised via KM-materialization cycle Wave-3.
    Mini-swarm quick-money-brigadier spawned with default experts
    [mgmt-expert, sales-researcher]. ICP populated from JETIX-VISION §7.1-7.2.
    Stage gates SG-1..SG-5 declared. Kill criteria: cumulative_revenue_eur < 5000
    by 2026-07-24.
```

---

### Target path: `swarm/wiki/operations/quick-money/decisions.md`

```markdown
---
title: "Decisions — Quick Money AI Consulting P1"
type: decision-log
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: high
confidence_method: 4-part-drr
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Decisions — Quick Money AI Consulting P1

4-part DRR entries per FPF E-9. Labels: Decision / Reasoning / Result / Review.
Appended by quick-money-brigadier. Newest entries on top.

---

### 2026-04-24 — Bootstrap: ICP scoped to Mittelstand + Startupper for Phase-1

- **Decision:** Restrict Phase-1 active outreach to two archetypes: (A) Deutscher
  Mittelstand SMB owner/manager; (B) English-speaking Startupper/infobiz.
  All other archetypes from JETIX-VISION §7.1 deferred to Phase-2+.
- **Reasoning:** Phase-1 revenue constraint (€50K Q2 2026) and solo-operator
  capacity require a single coherent ICP with clear pain-framing and short sales
  cycle. Mittelstand has budget + data-sovereignty urgency (BIOS-moment insight
  §3). Startupper has AI-literacy + speed to close. Both pass D22 5-criteria
  filter and have Phase-1 budget fit (€150/час + productized packages).
- **Result:** ICP.md populated verbatim from JETIX-VISION §7.1-7.2 with
  Phase-1 filter table. Leads will be qualified against this ICP by
  sales-researcher expert.
- **Review:** At SG-1 firing (3+ leads), verify that qualified leads are
  actually from these two archetypes. If majority come from another archetype
  (e.g. Продавцы), update ICP and this decision entry.
```

---

### Target path: `swarm/wiki/operations/quick-money/open-questions.md`

```markdown
---
title: "Open Questions — Quick Money AI Consulting P1"
type: open-questions
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Open Questions — Quick Money AI Consulting P1

Pending HITL decisions. Cleared (strikethrough + resolution date) when Ruslan acks.
Newest entries on top.

---

- id: OQ-3
  question: >
    Onboarding format for first Mittelstand client: full-day workshop (€1 500–3 000)
    vs 4-session sprint (€600/session × 4 = €2 400) vs pure async (wiki setup +
    video walkthrough, €800 flat)? Which format fits the Mittelstand buyer's
    calendar and trust pattern best?
  added: 2026-04-24
  priority: P2
  resolved: null
  resolution: null

- id: OQ-2
  question: >
    Archetype prioritisation for first 90 days: lead outreach primarily to
    Mittelstand (DE-language, slower to close, higher contract value) vs
    Startupper (EN-language, faster to close, lower contract value)?
    Which sequencing maximises probability of hitting SG-1 (3 leads) fastest?
  added: 2026-04-24
  priority: P1
  resolved: null
  resolution: null

- id: OQ-1
  question: >
    Pricing path B vs C for Phase-1 Mittelstand clients: Path B (client-hosted,
    Jetix = methodology + tooling only, lower margin but maximum data sovereignty)
    vs Path C (hybrid — client owns data, Jetix hosts agents, mTLS tunnel).
    Path B is easier to sell but harder to support remotely. Path C is more
    defensible technically but requires secure tunnel setup (engineering complexity).
    Which path to lead with for first 3 Mittelstand engagements?
  added: 2026-04-24
  priority: P1
  resolved: null
  resolution: null
```

[src:decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5 Path A/B/C]

---

### Target path: `swarm/wiki/operations/quick-money/offline-inference-spec.md`

```markdown
---
title: "Offline Inference Spec — Quick Money AI Consulting P1"
type: offline-inference-spec
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: uc-10-alignment
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: "swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partB-b2-mini-swarm-bundle.md", range: "§B.3.1 offline-inference-spec.md template + UC-10"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§5 Path B/C"}
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Offline Inference Spec — Quick Money AI Consulting P1

Per UC-10 Phase-A offline-first architecture
[src:partB-b2-mini-swarm-bundle.md §B.3.1 offline-inference-spec.md].
Validated by engineering-expert before first client deployment.

## Model choice

**Default:** ollama + Mistral 7B Q4_K_M (Apache 2.0 license; cleanest for
Mittelstand commercial deployment per KM-ARCHITECTURE-VARIANTS §12 Dissent 2).

**Alternative:** ollama + Llama 3.1-8B Q4_K_M (pending DACH golden-set evaluation).

**Rationale for Mistral default:** Mittelstand clients require verifiable license
for commercial deployment. Apache 2.0 is unambiguous; Llama commercial terms have
thresholds and exceptions that require legal review. For Phase-1 speed, Mistral wins.

## Hardware requirements

| Requirement | Spec |
|---|---|
| VRAM floor | 8 GB (Mistral 7B Q4_K_M) |
| RAM (system) | 16 GB minimum |
| Storage | ~4 GB model file + ~500 MB per-project KB index |
| OS | Linux (Ubuntu 22.04+ recommended); ollama daemon running |
| GPU | Optional (CUDA/Metal acceleration if available; CPU-only ≈ 3–5× slower) |

## Hosting path

- **Path B (default for Phase-1):** client-hosted; Jetix ships methodology
  + agent configs + ollama setup scripts. Client hosts on own infrastructure
  (on-prem mini-PC or dedicated VPS in EU). Jetix provides remote consulting
  and support only. Data never leaves client. Maximum data sovereignty.
  [src:STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §5 Path B]

- **Path C (enterprise clients):** client owns KB on their infrastructure;
  Jetix hosts agent-swarm with mTLS tunnel. Requires GDPR audit trail per
  client. Activates at €200K validation gate per JETIX-PLAN §4.

**Selected path for quick-money Phase-1:** Path B (client-hosted).

## 5-question acceptance test

Per UC-10 spec. All 5 must return TRUE before client handover.

```
Q1: Does `/ask "Summarize our Q1 sales report"` return an answer with >= 3
    [src:...] citations from the client's own wiki within 5 seconds p95 on
    client hardware?
    PASS criterion: TRUE

Q2: Does the local model operate with OFFLINE_MODE=1 (no cloud LLM calls)
    and still return a structured response?
    PASS criterion: TRUE

Q3: Does `ollama list` show mistral:7b-q4_k_m as the active model?
    PASS criterion: TRUE

Q4: Does `/ingest <client-document>` complete without errors and produce
    >= 1 wiki page under the client's operations/<slug>/ tree?
    PASS criterion: TRUE

Q5: Does the entire ingest+ask round-trip complete in < 120 seconds on
    client mini-PC hardware (Intel N100 or equivalent; no GPU)?
    PASS criterion: TRUE
```

**Golden-set:** 20 queries representative of the first Mittelstand client's
knowledge domain. Pass criterion: >= 80% of queries return >= 3 [src:...]
citations in <= 5 seconds p95 latency on client hardware.

## Phase-A fallback

If local LLM not yet provisioned: use `OFFLINE_MODE=1` structured-excerpt
path in `/ask` skill (retrieval-only; zero cloud LLM calls per UC-10
Phase-A proof). All wiki ingest and retrieval are filesystem-only.

## Fixture path for hermetic testing

`swarm/tests/fixtures/km-mvp/` — seeded corpus for CI validation.
```

[src:partB-b2-mini-swarm-bundle.md §B.3.1 offline-inference-spec.md template]

---

### Target path: `swarm/wiki/operations/quick-money/context.md`

```markdown
---
title: "Context — Quick Money AI Consulting P1"
type: context-snapshot
project: quick-money
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
cycle_count: 0
active_tasks_current: 0
sources: []
related:
  - "${WIKI_ROOT}/operations/quick-money/_moc.md"
binding_scope: "project-quick-money"
granularity: jetix-internal
---

# Context — Quick Money AI Consulting P1

Updated by quick-money-brigadier each cycle. Snapshot of current project state.
`cycle_count` and `active_tasks_current` are the SG-4 data sources:
`context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`.

## Current PMBOK phase

Executing (Phase-1 active operations per JETIX-PLAN §3).

## ICP summary

Two Phase-1 archetypes: (A) Deutscher Mittelstand SMB owner/manager (DACH,
data-sovereignty requirement, Path B offline deployment); (B) English-speaking
Startupper / infobiz (EN/US/UK, AI-literate, fast close). See `icp.md` for
full criteria and filter table.

## Offer

4-pack consulting offer (per JETIX-PLAN §3.3):
- Сессия/консультация: €150/час baseline
- 10 шаблонов (lead magnet): free entry point
- Community chat: Telegram invite-based (5–20 members, простой Phase-1)
- Конкретная помощь: AI-agent pipeline setup, wiki/KB architecture,
  consulting retainers, productized-service engagements

Продюсерский центр pilot (D11): research → script → footage → edit → repurpose
pipeline for English-speaking bloggers/educators. Monthly retainer model.

## Pricing

€150/час consulting baseline. Productized packages в разработке (D18).
Продюсерский центр: monthly retainer TBD at first pilot client close.
Mittelstand engagement range: €5 000–€30 000 per project.

## Active lead count

0 (as of 2026-04-24).

## Last cycle summary

Bootstrap cycle (Wave-3 of T-km-materialization-mvp-2026-04-24).
Project scaffold created. ICP populated. Stage gates declared. No leads yet.
```

---

### Target path: `swarm/wiki/operations/quick-money/leads/.gitkeep`

```
# This file keeps the leads/ directory tracked by git.
# Per-lead pages: leads/<lead-slug>.md
# Frontmatter required: status: prospect|qualified|proposal|signed|lost
# SG-1 predicate: count(leads/*.md) >= 3
# SG-3 predicate: count(leads/*.md:status: qualified) >= 3
# Created by KM-materialization Part E (Wave-3).
```

---

### Target path: `swarm/wiki/operations/quick-money/contracts/.gitkeep`

```
# This file keeps the contracts/ directory tracked by git.
# Per-contract pages: contracts/<client-slug>-<YYYY-MM-DD>.md
# SG-2 predicate: count(contracts/*.md) >= 1
# Created by KM-materialization Part E (Wave-3).
```

---

## E.2 — `levenchuk-deep-dive/` Operations Directory (P3 Research Adaptive)

**Project slug:** `levenchuk-deep-dive`
**Type:** research (adaptive bootstrap — bets-style stage gates)
**Priority:** P3
**PMBOK phase:** Planned
**Adaptive:** true (P3 project; no mini-swarm; expert dispatch via canonical brigadier on-demand)

[src:partB-b2-mini-swarm-bundle.md §B.1 research type + bets adaptive mechanic]

### Target path: `swarm/wiki/operations/levenchuk-deep-dive/_moc.md`

```markdown
---
title: "Levenchuk Deep Dive — Systems Thinking Research P3"
type: topic
layer: 6
niche: meta
project_type: research
priority: P3
state: active
pmbok_phase: Planned
adaptive: true
granularity: jetix-internal
problem_statement: |
  Анатолий Левенчук (ШСМ — Школа системного мышления) создал один из наиболее
  глубоко проработанных корпусов по системному мышлению, онтологии и
  трансдисциплинарному образованию. Корпус включает книги «Системное
  мышление», «Образование для образованных», «Онтологика» и связанные тексты.
  Цель проекта: systematic deep-dive в этот корпус для личного knowledge-synthesis
  Руслана, с последующей интеграцией концептов в работу systems-expert агента
  и потенциальным Phase-2+ исследовательским вкладом в тему AI × systems-thinking.
  Проект относится к Pillar 2 (topic-wikis per domain expert) из
  VISION-NEXT-STRATEGIC-HORIZON §1 C-1.
kill_criteria: |
  if count(hypotheses.md:status: supported) < 1 AND
  count(hypotheses.md:status: refuted) < 1 by 2026-10-24,
  kill project and archive
  (6-month horizon; indicates no falsifiable engagement with the corpus).
kpi_targets:
  hypotheses_per_cycle: 2
stage_gates:
  SG-0:
    stage_gate_number: 0
    predicate: "context.md:cycle_count >= 3"
    description: "Research has survived 3+ cycles without kill — triggers HITL review (continue | deepen | archive)."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "File-anchored scalar read from context.md frontmatter. cycle_count is an integer; >= 3 is deterministic."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-rd-1:
    stage_gate_number: 1
    predicate: "count(hypotheses.md:status: supported) >= 2"
    description: "At least 2 lines in hypotheses.md contain marker 'status: supported' — meaningful corpus engagement."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: supported' in hypotheses.md. Deterministic offline check."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
  SG-rd-2:
    stage_gate_number: 2
    predicate: "count(hypotheses.md:status: refuted) >= 1"
    description: "At least 1 line in hypotheses.md contains 'status: refuted' — Popperian refutation event demonstrating real engagement."
    state: pending
    declared_at: "2026-04-24"
    fired_at: null
    spawned_paths: []
    sg_validation:
      verdict: hamel-binary
      rationale: "Grep-count with marker 'status: refuted'. Popperian refutation event; deterministic offline."
      validated_at: "2026-04-24T00:00:00Z"
      validator: philosophy-expert
inference_stack: ollama-mistral-7b-q4
default_inference_tier: T-Hybrid
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
confidence: medium
confidence_method: bootstrap-adaptive
tier: tier-internal
produced_by: "/project-bootstrap"
sources:
  - {path: ".claude/config/project-types.yaml", range: "types.research + types.bets adaptive mechanic"}
  - {path: "decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md", range: "§1 C-1 topic-wikis per domain expert"}
related:
  - "${WIKI_ROOT}/themes/systems/README.md"
binding_scope: "project-levenchuk-deep-dive"
---

# Levenchuk Deep Dive — Systems Thinking Research P3

## Problem

Систематическое исследование корпуса Левенчука (ШСМ) для personal knowledge-synthesis
и интеграции в работу systems-expert агента Jetix OS.

## Kill criteria

if count(hypotheses.md:status: supported) < 1 AND
count(hypotheses.md:status: refuted) < 1 by 2026-10-24, kill project and archive.

## Current focus

Adaptive bootstrap. Baseline 3-file scaffold. Reading begins when Ruslan
directs first corpus file into `/ingest`. Hypotheses accumulate from reading.

## Hypotheses

See `hypotheses.md`. Current: 0 supported / 0 refuted / 0 pending.

## Stage gates (adaptive — bets-style)

SG-0: `context.md:cycle_count >= 3` — HITL review trigger (continue | deepen | archive).
SG-rd-1: `count(hypotheses.md:status: supported) >= 2` — meaningful engagement signal.
SG-rd-2: `count(hypotheses.md:status: refuted) >= 1` — Popperian engagement confirmed.

## Related themes

- [[systems]]
```

[src:partB-b2-mini-swarm-bundle.md §B.3.2 research _moc.md template][src:partC-stage-gates-merged.md §C.1]

---

### Target path: `swarm/wiki/operations/levenchuk-deep-dive/history.md`

```markdown
---
title: "History — Levenchuk Deep Dive P3"
type: event-log
project: levenchuk-deep-dive
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: high
confidence_method: append-only-log
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "${WIKI_ROOT}/operations/levenchuk-deep-dive/_moc.md"
binding_scope: "project-levenchuk-deep-dive"
granularity: jetix-internal
---

# History — Levenchuk Deep Dive P3

Append-only event log. Newest entries on top (per CLAUDE.md convention).
Do NOT edit or delete past entries.

---

- date: 2026-04-24
  event: project-bootstrap
  source: T-km-materialization-mvp-2026-04-24 Part E (Wave-3 mgmt-integrator)
  note: >
    Adaptive 3-file baseline scaffold materialised. P3 project — no mini-swarm.
    Expert dispatch via canonical brigadier on-demand (systems-expert +
    philosophy-expert per project-types.yaml research defaults).
    Kill horizon: 2026-10-24. SG-0/SG-rd-1/SG-rd-2 declared.
```

---

### Target path: `swarm/wiki/operations/levenchuk-deep-dive/open-questions.md`

```markdown
---
title: "Open Questions — Levenchuk Deep Dive P3"
type: open-questions
project: levenchuk-deep-dive
created: "2026-04-24"
last_modified: "2026-04-24"
pipeline: drafted
state: active
confidence: medium
confidence_method: bootstrap
tier: tier-internal
produced_by: "/project-bootstrap"
sources: []
related:
  - "${WIKI_ROOT}/operations/levenchuk-deep-dive/_moc.md"
binding_scope: "project-levenchuk-deep-dive"
granularity: jetix-internal
---

# Open Questions — Levenchuk Deep Dive P3

Pending HITL decisions. Cleared (strikethrough + resolution date) when Ruslan acks.
Newest entries on top.

---

- id: OQ-3
  question: >
    Publication format for synthesised insights: (a) wiki pages under
    ${WIKI_ROOT}/wiki/systems-thinking/ (Pillar 2 topic-wiki); (b) standalone
    essays in levenchuk-deep-dive/drafts/; (c) direct contribution to
    systems-expert agent's strategies.md (operational integration); or (d) all
    three in sequence? Which format serves the primary goal (systems-expert
    augmentation) vs secondary goal (potential Phase-2+ research contribution)?
  added: 2026-04-24
  priority: P3
  resolved: null
  resolution: null

- id: OQ-2
  question: >
    Falsification criterion for a "digested" topic from Левенчук corpus: what
    does it mean for a concept to be "fully digested" in the context of this
    research project? Options: (a) hypothesis about the concept has been
    either supported or refuted (Popperian — matches SG-rd-2); (b) concept
    page exists in wiki/systems-thinking/ with >= 3 citations from corpus;
    (c) concept has been applied in at least one swarm cycle artefact.
    Which criterion is Hamel-binary and operationally tractable?
  added: 2026-04-24
  priority: P2
  resolved: null
  resolution: null

- id: OQ-1
  question: >
    Which subset of Левенчук corpus to begin with? Candidate starting texts:
    (a) «Системное мышление» (core methodology); (b) «Образование для
    образованных» (epistemology + learning); (c) «Онтологика» (foundational
    ontology). Which text has the highest leverage for systems-expert
    agent augmentation given its current system prompt gaps?
  added: 2026-04-24
  priority: P1
  resolved: null
  resolution: null
```

---

## E.3 — Mini-Swarm Brigadier Templates

P1/P2 projects get a mini-swarm brigadier per `/project-bootstrap` §8 algorithm.
`quick-money` is P1 → mini-swarm spawned.
`levenchuk-deep-dive` is P3 → no mini-swarm; canonical brigadier on-demand only.

[src:partB-b2-mini-swarm-bundle.md §B.4 project-brigadier.md template + §B.2 Step 8]

### Target path: `.claude/agents/quick-money-brigadier.md`

```markdown
---
name: "quick-money-brigadier"
description: |
  Mini-swarm orchestrator for project quick-money. Scoped to
  operations/quick-money/ subtree (jetix-internal; no --client flag).
  Dispatches 2 default experts: mgmt-expert + sales-researcher.
  Budget: <=7 active tasks (vs canonical brigadier <=20).
  Instantiated by KM-materialization Part E (Wave-3) per /project-bootstrap §8.
  Per-project manifest; reads _moc.md + history.md + open-questions.md each cycle.
model: sonnet
tools: [Read, Write, Edit, Grep, Glob, Task]
granularity: project-scoped
owner: ruslan
created: "2026-04-24"
last_modified: "2026-04-24"
primary_alpha: task
secondary_alphas: [cycle, artefact]
domains: [project-task-decomposition, project-mini-swarm-dispatch, project-integration]
active_task_limit: 7
scope_subtree: "operations/quick-money/"
default_experts:
  - mgmt-expert
  - sales-researcher
sole_writer_of: "operations/quick-money/"
---

# Project-Brigadier — quick-money

Mini-swarm orchestrator scoped to project `quick-money`. Derived from canonical
brigadier (`.claude/agents/brigadier.md`) with narrower scope and tighter task
budget. Does NOT carry orchestration authority over other projects.

## §1 Scope

**Write scope:** `operations/quick-money/` subtree (jetix-internal; no --client).
This agent may WRITE only within scope_subtree. Attempting to write outside
scope is a hard violation — escalate to canonical brigadier via escalations[].

**Read scope:** may READ anything under `${WIKI_ROOT}` (Q1 4-tier retrieval).

**Task budget:** <=7 active tasks at any time. Hard ratchet via
`${WIKI_ROOT}/meta/health.md` mini_swarm_active_tasks counter.
At 7 tasks: no new tasks dispatched until one closes.

**Escalation to canonical brigadier (mandatory for):**
- Cross-project read-for-promotion (within-client cross-project leverage)
- Method change or foundation revision
- Contradiction with a canonical foundation (escalations[]{trigger: contradiction-with-foundation})
- Budget overrun (>7 active tasks)
- SG-4 fires and promotion to full type is eligible (HITL-gate required)
- Kill criteria met: `cumulative_revenue_eur < 5000 by 2026-07-24`
  → escalations[]{trigger: kill-criteria-met, project: quick-money}

## §2 Cycle responsibilities

Every project cycle:
1. Read `operations/quick-money/_moc.md` — verify state=active; check kill_criteria.
   If `cumulative_revenue_eur < 5000` AND date >= `2026-07-24`: STOP;
   emit escalations[]{trigger: kill-criteria-met} to canonical brigadier.
2. Read `operations/quick-money/history.md` (last 5 entries) + `open-questions.md`.
3. Decompose next project task per canonical brigadier §3 (Decompose-or-Chat gate E-17).
4. Dispatch 1-2 default_experts via Task() with `<domain> × <mode>` prefix.
5. Integrate expert returns per canonical brigadier §5 (dissent preservation AP-6).
6. Prepend to `operations/quick-money/history.md` (newest-on-top).
7. Write 4-part DRR entries to `operations/quick-money/decisions.md` if decision made.
8. Append to `agents/quick-money-brigadier/strategies.md` if new rule extracted.
9. Run `/lint --project=quick-money` before weekly digest.
10. Check stage_gates in _moc.md. If any SG predicate evaluates TRUE: follow §5.

## §3 Mini-swarm dispatch schema

Default experts for quick-money (from project-types.yaml consulting type):

- **mgmt-expert** — prioritization, delivery-plan, stakeholder-map, ICP critique,
  pipeline review, stage-gate evaluation
- **sales-researcher** — lead research, ICP qualification, outreach scripts,
  prospect profiling, competitive intelligence for Mittelstand + Startupper segments

Task() invocation schema (per canonical brigadier §4):
```yaml
mode: <critic|optimizer|integrator|scalability>
brief:
  task_id: <id>
  cycle_id: <id>
  cell_id: "quick-money-brigadier-<mode>-<slug>"
  artefact_under_consideration: <path>
  ap_cost: <estimate>
  ap_budget: <limit>
inputs: [<path-list>]
expected_return_path: "operations/quick-money/drafts/<id>-<mode>-<slug>.md"
```

On-demand experts (other than mgmt-expert + sales-researcher): escalate
`escalations[]{trigger: peer-input-needed, requested: "<expert> × <mode> on <topic>"}` to
canonical brigadier. Do NOT call non-default experts directly from this agent.

## §4 Strategies memory (Level-1 per W-5)

Personal memory: `agents/quick-money-brigadier/strategies.md`

4-part DRR entry format: {Decision, Reasoning, Result, Review}.
Append new entries after each cycle where a rule is extracted.

## §5 Stage-gate interaction (B3 merged into B2)

When `/lint --check-stage-gates` fires for quick-money:
1. Read `_moc.md` stage_gates block. Verify which SG predicate evaluated TRUE.
2. Consult `project-types.yaml` promotion_rules for matching trigger.
3. Auto-spawn (requires_hitl=false): copy template files into operations/quick-money/
   subtree (additive only; never overwrite). Append to history.md. Commit.
4. HITL-required (requires_hitl=true, e.g. SG-4 + type promotion): emit
   escalations[]{trigger: sg-promotion-eligible, sg: <SG-N>, project: quick-money}
   to canonical brigadier. Await HITL ack.
5. Update `_moc.md` stage_gates.<SG-N>.state = "fired"; set fired_at; populate
   spawned_paths.

**SG-5 special note:** When `pipeline.md:mrr_eur_contracted >= 1000` fires,
quick-money-brigadier updates `pipeline.md` frontmatter key `mrr_eur_contracted`
each cycle from actual signed retainer/contract data. Never updates it speculatively.

## §6 Output contract

- Commit frequency: per logical unit (not per file).
- Commit message format: `[quick-money] <verb> <what>`
- Never: `git commit --amend`, `--no-verify`, force-push.
- Every draft written to `operations/quick-money/` carries YAML frontmatter per
  shared-protocols §2 provenance gate.

## §7 Shared-protocols import (by reference)

Imports all 9 sections of `swarm/lib/shared-protocols.md` per agent system prompt §7.
Key constraints for this project scope:
- §1 wiki-write: sole-writer of operations/quick-money/; canonical brigadier handles wiki spine.
- §4 HITL: kill-criteria-met + sg-promotion-eligible + method-change require HITL ack.
- §9 Max-sub: no provider API-key env vars; no paid embeddings; no third-party SDKs.
```

---

### Target path: `.claude/agents/levenchuk-deep-dive-brigadier.md`

```markdown
---
name: "levenchuk-deep-dive-brigadier"
description: |
  STUB — P3 project. No mini-swarm spawned at bootstrap per /project-bootstrap §8
  algorithm (P3/P4: no mini-swarm; expert dispatch via canonical brigadier on-demand).
  This file is a routing stub only. If project reaches SG-4 momentum threshold
  and HITL promotes to P2, /project-bootstrap --promote will instantiate a real
  mini-swarm agent. Until then: canonical brigadier dispatches systems-expert +
  philosophy-expert on-demand per open-questions.md items.
model: sonnet
tools: [Read, Write, Edit, Grep, Glob]
granularity: project-scoped
owner: ruslan
created: "2026-04-24"
last_modified: "2026-04-24"
primary_alpha: task
secondary_alphas: [cycle, artefact]
domains: [project-task-routing-stub]
active_task_limit: 0
scope_subtree: "operations/levenchuk-deep-dive/"
default_experts:
  - systems-expert
  - philosophy-expert
sole_writer_of: "operations/levenchuk-deep-dive/"
stub: true
stub_reason: "P3 project; mini-swarm requires P1/P2. Upgrade path: HITL acks SG-4 + /project-promote."
---

# Project-Brigadier Stub — levenchuk-deep-dive

P3 research project. No active mini-swarm per `/project-bootstrap §8`
(P3/P4 projects → no mini-swarm spawned).

## Routing for on-demand expert dispatch

When Ruslan or canonical brigadier needs work done on this project:
1. Canonical brigadier reads `operations/levenchuk-deep-dive/_moc.md` + `open-questions.md`.
2. Dispatches `systems-expert × <mode>` OR `philosophy-expert × <mode>` on-demand.
3. Outputs land under `operations/levenchuk-deep-dive/drafts/<id>-<mode>-<slug>.md`.

Default experts (from project-types.yaml research type):
- **systems-expert** — feedback loops, system archetypes, Левенчук ШСМ primary reader
- **philosophy-expert** — Popperian hypothesis critique, epistemic audit, first-principles reset

## Upgrade path (P3 → P2 promotion)

If SG-4 fires (`context.md:cycle_count >= 5 AND context.md:active_tasks_current >= 5`):
1. Canonical brigadier emits escalations[]{trigger: sg-promotion-eligible, sg: SG-4, project: levenchuk-deep-dive}.
2. HITL (Ruslan) acks: promote to P2 via `/project-promote levenchuk-deep-dive --to=P2`.
3. Mini-swarm instantiated: real `levenchuk-deep-dive-brigadier.md` replaces this stub.
4. This stub file is archived to `agents/levenchuk-deep-dive-brigadier/stub-archived-<date>.md`.

## Write scope

`operations/levenchuk-deep-dive/` subtree only.
Canonical brigadier is sole commit authority.
```

---

## E.4 — End-to-End Demo Workflow Spec

**Type:** text spec (no new files created by this section).
**Purpose:** describes the E2E ingest+ask+writeback demo for the KM-materialization
MVP acceptance test. References `quick-money/` as the target project context.

[src:prompts/km-materialization-mvp-execution-2026-04-24.md §2.E.4]

---

### E.4.1 Demo overview

The demo proves that the full KM stack (ingest → wiki pages → ask → citations →
writeback) operates end-to-end with the materialised `quick-money/` project tree.
It uses `offline-inference-spec.md` UC-10 acceptance test as the pass criterion.

**Hermetic fallback:** if the URL or local document is unreachable, use
`swarm/tests/fixtures/km-mvp/` as the seeded corpus. The fixture path provides
a deterministic input for CI validation.

---

### E.4.2 Step 1 — Ingest

**Skill invoked:** `/ingest <URL-or-local-path>`

**Concrete example (Mittelstand use-case):**
```
/ingest swarm/tests/fixtures/km-mvp/mittelstand-ai-primer.md
```
OR with a real URL (if network available):
```
/ingest https://example.com/mittelstand-ai-use-cases-2026.html
```

**Expected outputs:**
- `>= 1` wiki page created under `${WIKI_ROOT}/operations/quick-money/` OR
  under `${WIKI_ROOT}/wiki/business/` (depending on ingest routing).
- `${WIKI_ROOT}/log.md` prepended with new ingest event (newest-on-top).
- `${WIKI_ROOT}/index.md` updated with new page entry.
- `${WIKI_ROOT}/wiki/graph/edges.jsonl` updated with typed edges from new page.

**Pass criterion (N):** `>= 1` wiki page produced per ingest call.
Inline citations `[src:...]` present in produced page body.

**OFFLINE_MODE=1 path:** if local ollama not provisioned, ingest runs in
retrieval-only mode: extracts structured excerpts from source document,
writes them as wiki pages WITHOUT cloud LLM calls. Pages carry
`confidence_method: retrieval-only` in frontmatter.

---

### E.4.3 Step 2 — Ask

**Skill invoked:** `/ask "<question>"`

**Concrete example:**
```
/ask "What are the main AI implementation barriers for Mittelstand companies
      and how does Jetix's local-first architecture address them?"
```

**Expected outputs:**
- Synthesized answer with `>= 3` `[src:...]` citations drawn from the
  previously ingested wiki pages.
- Citations must reference actual files in `${WIKI_ROOT}/`, not fabricated paths.
- Answer body `<= 800 words` (concise synthesis, not dump).
- Optional: if `/ask` is run with `--writeback` flag, a comparison entry is
  appended to `${WIKI_ROOT}/wiki/comparisons/`.

**Pass criterion:** answer contains `>= 3` distinct `[src:<path>#<section>]` citations.
All cited paths must resolve to existing files under `${WIKI_ROOT}/`.

**Offline path:** if `OFFLINE_MODE=1`, retrieval is filesystem grep-only.
Answer is constructed as structured excerpts from matching wiki pages,
not LLM synthesis. Citations are still mandatory.

---

### E.4.4 Step 3 — Writeback

**Target:** `swarm/wiki/operations/quick-money/history.md`

**Trigger:** any `/ask` that produces a synthesized insight relevant to the
`quick-money` project context should generate a history entry.

**Format (appended as newest-on-top entry):**
```yaml
- date: <ISO-DATE>
  event: km-insight
  source: /ask "<question-slug>"
  citations:
    - "<path>#<section>"
    - "<path>#<section>"
    - "<path>#<section>"
  note: >
    <1-2 sentence summary of the insight and its relevance to quick-money ICP
    or pipeline or offer>
```

**Pass criterion:** `>= 1` entry with event: `km-insight` in `history.md`
after demo run. Entry carries `citations:` list with `>= 3` items.

---

### E.4.5 Acceptance test summary (E2E)

| Step | Pass criterion | Hermetic fallback |
|---|---|---|
| `/ingest` | >= 1 wiki page produced; [src:...] citations present | `swarm/tests/fixtures/km-mvp/` seeded corpus |
| `/ask` | answer contains >= 3 [src:...] citations; all paths resolve | retrieval-only mode (OFFLINE_MODE=1) |
| Writeback | history.md gains >= 1 km-insight entry with >= 3 citations | manual entry acceptable for first demo |
| offline-inference-spec.md 5-question test | All 5 pass on client hardware | Path A (Jetix-hosted VPS) as fallback if mini-PC not available |

---

## Dissents and escalations (§5.2 integrator obligation)

```yaml
dissents: []
# No peer input contradictions surfaced in this wave.
# The ICP KPI targets (leads_per_quarter: 20, contracts_per_quarter: 2,
# mrr_eur_target_q2_2026: 15000, cumulative_revenue_q2_2026_eur: 50000)
# are sourced directly from JETIX-PLAN §3.1 D3 without investor-expert
# cross-validation in this cell. If investor-expert × critic produces
# a contrasting capital-arithmetic view on these targets, brigadier
# should run investor × critic on quick-money/_moc.md kpi_targets
# before the first cycle closes.
escalations:
  - trigger: peer-input-needed
    requested: "investor-expert × critic on quick-money/_moc.md kpi_targets (leads_per_quarter, mrr_eur_target_q2_2026, cumulative_revenue_q2_2026_eur)"
    reason: >
      KPI targets are sourced from JETIX-PLAN §3.1 (F4 operational convention,
      ClaimScope: holds for Phase-1 solo-founder; unknown for Phase-2 managed-team).
      investor-expert has domain authority over capital-arithmetic and horizon
      projections. This mgmt-integrator cell does NOT produce horizon arithmetic.
      Recommend brigadier dispatch investor × critic as a post-Wave-3 follow-up
      to validate that the 50K/15K MRR targets are consistent with the
      gross-margin arithmetic in STRATEGIC-INSIGHT §5 Path B/C.
    priority: P2
    blocking: false
```

---

## Provenance summary

| Claim / artefact | Source | Range | F level |
|---|---|---|---|
| quick-money _moc.md problem_statement (Mittelstand + Startupper framing) | JETIX-VISION.md | §7.1-7.2 | F4 |
| quick-money _moc.md kill_criteria (€5000 by 2026-07-24) | JETIX-PLAN.md | §3.1 + §3.9 M1.1 | F4 |
| quick-money kpi_targets (50K cumulative, 15K MRR) | JETIX-PLAN.md | §3.1 Phase-1 objectives | F4 |
| quick-money stage_gates SG-1..SG-5 predicates | partB-b2-mini-swarm-bundle.md | §B.1 consulting default_stage_gates | F4 |
| quick-money stage_gates sg_validation blocks | partC-stage-gates-merged.md | §C.1 canonical schema | F4 |
| icp.md 5 criteria verbatim | JETIX-VISION.md | §7.2 D22 verbatim | F5 (decision-locked) |
| icp.md Phase-1 archetype filter (Mittelstand + Startupper primary) | JETIX-VISION.md + JETIX-PLAN.md | §7.1 + §3.7 | F4 |
| offline-inference-spec.md Path B default | STRATEGIC-INSIGHT §5 | Path B Pros/Cons | F3 (draft insight, not locked) |
| offline-inference-spec.md 5-question acceptance test | partB-b2-mini-swarm-bundle.md | §B.3.1 offline-inference-spec.md template + UC-10 | F4 |
| levenchuk _moc.md problem_statement | VISION-NEXT §1 C-1 | topic-wikis per domain expert | F4 |
| levenchuk kill_criteria (2026-10-24 6-month horizon) | partB-b2-mini-swarm-bundle.md | §B.1 bets adaptive mechanic | F4 |
| levenchuk stage_gates (SG-0 / SG-rd-1 / SG-rd-2) | partB-b2-mini-swarm-bundle.md | §B.1 research type defaults | F4 |
| quick-money-brigadier default_experts [mgmt-expert, sales-researcher] | partB-b2-mini-swarm-bundle.md | §B.1 consulting default_experts | F4 |
| levenchuk-deep-dive-brigadier stub (P3 no mini-swarm) | partB-b2-mini-swarm-bundle.md | §B.2 Step 8 P3/P4 rule | F4 |
| E2E demo writeback format | prompts/km-materialization-mvp-execution-2026-04-24.md | §2.E.4 | F4 |

---

## Anti-scope (§3.4)

- This design record does NOT write canonical wiki — brigadier promotes.
- This design record does NOT perform physical file extraction — Wave-3 extraction cell mandate.
- This design record does NOT contain capital-arithmetic on KPI targets — investor-expert territory.
- This design record does NOT critique code craft — engineering-expert territory.
- This design record does NOT arbitrate epistemic claims about Левенчук corpus content — philosophy-expert territory.
- SG predicates are DSL-canonical only: `count(<glob>)`, `count(<glob>:<marker>)`, `<file.md>:<key> OP <n>`. No bare-metric forms.
- No provider API-key environment variable references.
- No hardcoded `/home/ruslan/jetix-os/` paths — all paths use `${WIKI_ROOT}` or relative forms.
- No Notion writes.
