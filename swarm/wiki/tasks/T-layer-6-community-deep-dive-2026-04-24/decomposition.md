---
id: T-layer-6-community-deep-dive-2026-04-24-wbs
title: "Phase-2 WBS — 13 cells + integration cell for LAYER-6-COMMUNITY-DEEP-DIVE.md"
type: wbs-decomposition
created: 2026-04-24
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
task_id: T-layer-6-community-deep-dive-2026-04-24
parent_intake: ./intake.md
status: planned
total_cells: 14 (13 content + 1 integration)
matrix_invocations_used: 6 of 20 (mgmt-integrator ×5, systems-integrator ×4, philosophy-critic ×2, engineering-integrator ×1, investor-scalability ×3, brigadier-integration ×1)
parallel_waves: 3 (Wave-A: §1+§2+§3+§4+§5; Wave-B: §6+§7+§8+§9+§10+§11; Wave-C: §12+§13+integration)
hd_02_budget: within N=2-3 active cycles (this is single cycle)
---

# Phase-2 WBS — 13 cells + 1 integration cell

> Each cell carries `class: M`, an explicit `cell_acceptance_predicate:`, the
> source-files it must read, the artefact it must produce in `swarm/wiki/drafts/`,
> and the matrix-cell `<domain> × <mode>` prefix per shared-protocols §5.

## Cell C-01 — §1 TL;DR

```yaml
class: M
matrix_cell: mgmt-expert × integrator
expert: mgmt-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S1-tldr.md
target_words: 400-600
wave: C (last — needs all other sections drafted to summarize)
sources_to_read:
  - intake.md
  - all sibling drafts S2..S13 (read after they land)
  - decisions/JETIX-SYSTEM-OVERVIEW.md §0 (TL;DR pattern)
cell_acceptance_predicate: |
  - 400-600 words inclusive
  - Layer 6 описан в 3 предложениях up-front
  - Includes 4 conclusions: ICP filter / Alliance structure pick / outreach mechanism / expected growth
  - Cites brigadier's Alliance recommendation (one of A/B/C)
  - 0 banned phrases per .claude/config/sg-banned-phrases.yaml
```

## Cell C-02 — §2 ICP Trinity (3 portraits)

```yaml
class: M
matrix_cell: mgmt-expert × integrator
expert: mgmt-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S2-icp-trinity.md
target_words: ≥4000 total (S2.1 ≥1500, S2.2 ≥1500, S2.3 ≥1000)
wave: A
sources_to_read:
  - intake.md §6.1 (binding ICP clarification)
  - swarm/wiki/operations/quick-money/icp.md (Tier-1 starting point — supersede)
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L6-business.md §2
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §§2.1-2.2
  - decisions/JETIX-VISION.md §7 (D22 + 11 archetypes)
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §8 (corp partnerships)
  - reports/review_2026-04-24.md (audio_510 corp, audio_515 partnerships, audio_529 Smart AI)
cell_acceptance_predicate: |
  - §2.1 Client ICP ≥1500 words: payment ability filter ($5K/mo or $10K one-shot) + income spectrum
    (millionaires + $100K-$150K+ + предприниматели + блогеры) + 5-criteria filter + Phase-1
    acceptable buyers (broad spectrum) + where to find (channels × archetype) + qualification questions list
  - §2.2 Partner ICP ≥1500 words: corporation partnerships (Porsche/BMW/Apple/Google/Tesla terms:
    партнёрство за долю + безлимитные ресурсы) + vendor partnerships (Anthropic / Groq) +
    co-consultants (McKinsey-platform per USB-C resolution) + Mittelstand AI Alliance potential members
  - §2.3 Team ICP ≥1000 words: 50-100 target per D26 enterprise-fast + 11 archetypes × 5-criteria
    + hires roadmap (Phase 1 → Phase 4) + first 5 roles defined (sales / operations / content / support / tech)
  - Earlier KM-Mat Option-C Tier-1 lock {Предприниматели + Блогеры only} explicitly superseded
  - All prose cites source per non-trivial paragraph
  - F-G-R tags on at least 5 major claims
```

## Cell C-03 — §3 11 Archetypes deep-dive

```yaml
class: M
matrix_cell: mgmt-expert × integrator
expert: mgmt-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S3-archetypes.md
target_words: ≥3000 total (300-500 per archetype × 11)
wave: A
sources_to_read:
  - decisions/JETIX-VISION.md §7.1 (11 archetypes) + §8 (per-archetype angles)
  - intake.md §6.1
cell_acceptance_predicate: |
  - 11 archetypes covered: Startupper/entrepreneur, Блогер/content creator, Исследователь,
    Инженер, Инвестор, Философ, Соединитель/connector, Athlete/disciplined builder, Designer/creative,
    Teacher/educator, Operator/founder-CEO
  - Each archetype 300-500 words: кто / мотивация / что ищет от Jetix / что даёт Jetix /
    canal / message pattern
  - Total 3000-5500 words
  - Each archetype maps to JETIX-VISION §7.1 lineage (where applicable; new archetypes flagged
    as L6-deep-dive additions if they don't directly map)
```

## Cell C-04 — §4 5-Criteria Filter

```yaml
class: M
matrix_cell: systems-expert × integrator
expert: systems-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S4-five-criteria.md
target_words: ≥800
wave: A
sources_to_read:
  - decisions/JETIX-VISION.md §7.2 (D22 5 criteria verbatim)
  - swarm/wiki/operations/quick-money/icp.md (5 criteria applied)
  - intake.md §6.1
cell_acceptance_predicate: |
  - All 5 criteria covered in detail: Startupper / Азарт / Stable / Adequate / Upward-direction
  - Per criterion: how to elicit (questions to ask) + behavioral markers + disqualifiers
  - Self-selection mechanism documented: how criteria work as filter via brand messaging
    («самая большая авантюра века» — predator-outside framing per JETIX-VISION §7.2)
  - References cybernetics / Ashby requisite variety / membrane metaphor (systems-expert lens)
```

## Cell C-05 — §5 Alliance Architecture (3 options)

```yaml
class: M
matrix_cell: systems-expert × integrator (primary) + investor-expert × scalability (peer-input)
expert: systems-expert
mode: integrator
peer_input_from: investor-expert (ROI assessment per option)
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S5-alliance.md
peer_output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S5-alliance-roi.md
target_words: ≥2000 (3 options ≥500 each + recommendation + risks)
wave: A
sources_to_read:
  - intake.md §6.3
  - decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md §3-§9 (Mittelstand AI Alliance / EISA moment / 7 advantages)
  - decisions/JETIX-VISION.md D20 USB-C + D21 Roy-replication
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27 Fork-and-merge
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §2.7
cell_acceptance_predicate: |
  - 3 options each ≥500 words:
    A. Non-profit consortium (Linux Foundation analog) — governance / IP / revenue / membership / Phase fit / risks
    B. For-profit standards body (ARM Holdings analog) — same dimensions
    C. Hybrid (non-profit methodology upstream + for-profit services downstream) — same dimensions
  - investor-expert peer-input draft adds ROI/unit-econ arithmetic per option
  - Brigadier (in integration cell) recommends ONE; preserves dissents
  - Ruslan picks in ack — recommendation must be one paragraph, easily reversible
  - Each option references USB-C positioning + D27 fork-and-merge governance fit
```

## Cell C-06 — §6 Matchmaker Mechanics

```yaml
class: M
matrix_cell: systems-expert × integrator (primary) + investor-expert × scalability (KPI peer-input)
expert: systems-expert
mode: integrator
peer_input_from: investor-expert (KPI targets per gate)
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-integrator-S6-matchmaker.md
peer_output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-investor-scalability-S6-matchmaker-kpis.md
target_words: ≥1500
wave: B
sources_to_read:
  - decisions/JETIX-VISION.md D21 (matchmaker) + §13 phase timeline
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §2.6
  - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md (Voice 2 matchmaker narrative)
cell_acceptance_predicate: |
  - Phase 1 manual mode: Ruslan personally matches — process, metrics, limits documented
  - Phase 2 AI-smoothed coordination: agents help communication — specific mechanism
  - Phase 2+ platform mode: formal matching portal — MVP spec
  - Migration triggers documented: manual → AI-smooth → platform (per revenue gates G1/G2/G3)
  - Match rate / completion rate / NPS KPIs + targets per gate (investor-expert peer-input)
  - Cybernetics / feedback loops lens applied (systems-expert)
```

## Cell C-07 — §7 Outreach Mechanism (READY-TO-USE templates)

```yaml
class: M
matrix_cell: mgmt-expert × integrator
expert: mgmt-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S7-outreach.md
target_words: ≥3000 (templates + script + questions + landings)
wave: B
sources_to_read:
  - intake.md §6.5
  - decisions/JETIX-VISION.md §11 geography + §10 positioning
  - decisions/JETIX-PLAN.md §3 Phase-1 actions (outreach)
  - raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md (USB-C pitch verbatim — sales asset)
  - reports/review_2026-04-24.md audio_507 (3-audience landings) audio_523 (multi-site outreach funnel)
cell_acceptance_predicate: |
  - §7.1 Channels: LinkedIn / Email / YouTube / Partnerships / Warm intros — for each:
    target archetypes, expected response rate (with caveat: bounded estimate, not data),
    tempo (frequency)
  - §7.2 Message templates per archetype: 3-5 templates per channel × archetype = ≥15-20 templates total
    - Realistic wording (not placeholders)
    - Personalization slots clearly marked: {{name}} / {{company_context}} / {{specific_pain}}
    - Call-to-action clear (discovery call invitation / lead magnet / referral ask)
  - §7.3 Discovery call script (15-20 min): Opening / relationship check / problem exploration /
    Jetix fit test / next-step close
  - §7.4 Qualification questions list: 10-15 questions, mapped to D22 5-criteria + payment ability filter
  - §7.5 3-audience landings (per audio_507): авантюристы / инвесторы / работники мечты —
    skeleton structure each + primary CTA
  - All templates incorporate Ruslan voice anchors (USB-C metaphor / «самая большая авантюра» framing)
```

## Cell C-08 — §8 Membership / Invite Filter (TEMPLATE LEVEL)

```yaml
class: M
matrix_cell: mgmt-expert × integrator
expert: mgmt-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S8-membership.md
target_words: 400-800 (TEMPLATE LEVEL — DO NOT over-engineer per Ruslan §6.2)
wave: B
sources_to_read:
  - intake.md §6.2
  - decisions/JETIX-VISION.md §7 (D22 self-selection)
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §2.3 Secure Network membership
cell_acceptance_predicate: |
  - 400-800 words (HARD CAP — exceeds = reject)
  - Skeleton structure: invite-only Phase 1 → open application Phase 2+ → rejection process (humane)
    → anti-spam / anti-toxic mechanics
  - Stub-level future iteration — sub-headers + 1-2 sentences each, not full prose elaboration
  - Explicitly notes: "TEMPLATE LEVEL per Ruslan 2026-04-24 — full Deep Dive deferred"
```

## Cell C-09 — §9 Growth Model (TEMPLATE LEVEL)

```yaml
class: M
matrix_cell: mgmt-expert × integrator
expert: mgmt-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-mgmt-integrator-S9-growth.md
target_words: 400-800 (TEMPLATE LEVEL — DO NOT over-engineer per Ruslan §6.2)
wave: B
sources_to_read:
  - intake.md §6.2
  - decisions/JETIX-PLAN.md §3.5 Phase 1 community
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §6 evolution
cell_acceptance_predicate: |
  - 400-800 words (HARD CAP — exceeds = reject)
  - Skeleton: current 1 → Phase 1 target 5-20 → Phase 2 target 50-200 → Phase 3+ target 1000-5000
  - Quality-first principle (D12) noted
  - Stub-level future iteration; not full elaboration
  - Explicitly notes: "TEMPLATE LEVEL per Ruslan 2026-04-24 — full Deep Dive deferred"
```

## Cell C-10 — §10 Secure Network Architecture

```yaml
class: M
matrix_cell: engineering-expert × integrator
expert: engineering-expert
mode: integrator
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-engineering-integrator-S10-secure-network.md
target_words: ≥1500
wave: B
sources_to_read:
  - intake.md §6.4
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §2.3-2.5
  - reports/review_2026-04-24.md audio_524 (Telegram + Дуров) audio_524 task#464 (digital portrait basis)
  - decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md D27 Fork-and-merge governance
cell_acceptance_predicate: |
  - Telegram-based primary architecture (per audio_524) — concrete: bot architecture, channel structure,
    invite-flow, role permissions
  - Digital portraits: schema (fields), how created (intake form / interview), privacy considerations
    (what's shared with whom, GDPR Art. 13/14 awareness)
  - Moderation model: who moderates / how / what — escalation paths
  - Spam prevention: invite-only + reputation + rate limits
  - Fork-community governance per D27 (как community форкает методологию) — concrete merge-back protocol stub
  - Integration story: Дуров contact = "potential future contact, not assumed" — 1-line aspirational mention
  - Backup options brief: Discord (1 paragraph) + own platform (1 paragraph) — NOT deep
  - Engineering lens: protocol contracts + boundaries + failure modes (no SDK code, description only)
```

## Cell C-11 — §11 Evolution per gate

```yaml
class: M
matrix_cell: systems-expert × scalability
expert: systems-expert
mode: scalability
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-systems-scalability-S11-evolution.md
target_words: ≥1000
wave: B
sources_to_read:
  - decisions/JETIX-PLAN.md §3 Phase 1 + §4-§5 transitions
  - decisions/JETIX-VISION.md §13 phase timeline
  - decisions/JETIX-SYSTEM-OVERVIEW.md §5 trajectory + per-layer evolution paths
  - swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md §6
cell_acceptance_predicate: |
  - Table + narrative: what L6 upgrades at each gate (G1 €50K / G2 €200K / G3 €1M / G4 $100M / G5 $1T)
  - Each gate: ICP scope expansion / outreach channels / Alliance state / matchmaker mode /
    Secure Network state / digital portraits state / membership cardinality
  - Migration triggers explicit (revenue-gated per D15)
  - Scalability lens: bottlenecks identified per gate; mitigation noted
```

## Cell C-12 — §12 Open questions

```yaml
class: M
matrix_cell: philosophy-expert × critic
expert: philosophy-expert
mode: critic
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-philosophy-critic-S12-open-questions.md
target_words: ≥500
wave: C
sources_to_read:
  - all sibling drafts S1..S11 (after they land — read open-question stubs each cell flags)
  - intake.md §4 risks
cell_acceptance_predicate: |
  - At minimum the following open questions surfaced (each with: question / context / why it matters /
    proposed resolution path / who decides):
    1. Alliance option A/B/C decision (Ruslan pick — brigadier recommendation present)
    2. Millionaire-vs-spectrum definition sharpening if needed (post Ruslan §6.1 resolution still has edge cases)
    3. Дуров contact timing
    4. Fork-community governance specifics (IP licensing — MIT / proprietary / dual)
    5. Discovery call format: phone / video / in-person
  - Additional questions surfaced from sibling drafts integrated
  - Each question explicitly assigned a decider (Ruslan / brigadier-future / deferred to L7-research)
```

## Cell C-13 — §13 Preserved dissents + F-G-R tagging + citations

```yaml
class: M
matrix_cell: philosophy-expert × critic
expert: philosophy-expert
mode: critic
output_path: swarm/wiki/drafts/T-layer-6-community-deep-dive-2026-04-24-philosophy-critic-S13-dissents.md
target_words: ≥500
wave: C
sources_to_read:
  - all sibling drafts S1..S11 dissents + claims (after they land)
  - intake.md §4 risks
cell_acceptance_predicate: |
  - All cross-expert dissents preserved per §1d AP-6 (no averaging into consensus)
  - Each dissent: position / reasoning / evidence / F-G-R tag / recommended resolution
  - F-G-R tagging present per major claim across the document (≥10 F-G-R tags total)
  - Citations to source: audio_NNN, decisions/*, wiki/*, raw/* — at least one per non-trivial paragraph
    in canonical document
  - D22 + D26 consistency check passed (no claim contradicts D22 5-criteria or D26 team 50-100)
  - Coherence review: cross-section references resolved (no dangling §X.Y refs)
```

## Cell C-14 — Integration cell (brigadier)

```yaml
class: M
matrix_cell: brigadier (orchestrator integration; NOT a 5×4 matrix invocation)
expert: brigadier
mode: integration
output_path: decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
target_words: 15000-25000 total
wave: C (final — after all S1..S13 land)
sources_to_read:
  - all 13 sibling drafts S1..S13 + investor peer-input drafts S5/S6
  - intake.md (acceptance predicate)
  - decisions/JETIX-SYSTEM-OVERVIEW.md (template/style reference)
cell_acceptance_predicate: |
  - All 13 sections integrated with consistent voice + harmonized cross-references
  - Word count 15000-25000 inclusive
  - All §1 of intake acceptance predicate items met
  - YAML frontmatter complete per swarm/wiki/_templates/decision.md (or equivalent)
  - sources[] populated; provenance_inline: true; F-G-R tags present
  - 0 banned phrases per .claude/config/sg-banned-phrases.yaml
  - 0 wikilinks without related[] entries
  - Brigadier Alliance recommendation present + clearly marked as one of A/B/C
  - Per shared-protocols §1: brigadier writes commit per section landing
```

## §X Wave timing + parallelism plan

| Wave | Cells dispatched in parallel | Reason |
|---|---|---|
| **A** | C-02 (S2 ICP Trinity), C-03 (S3 Archetypes), C-04 (S4 5-Criteria), C-05 (S5 Alliance + investor peer S5-ROI) | Independent; mgmt + systems + investor in parallel; foundation for §1 TL;DR |
| **B** | C-06 (S6 Matchmaker + investor peer S6-KPIs), C-07 (S7 Outreach), C-08 (S8 Membership), C-09 (S9 Growth), C-10 (S10 Secure Network), C-11 (S11 Evolution) | Independent of each other; can read Wave-A drafts as context |
| **C** | C-12 (S12 Open Q), C-13 (S13 Dissents+F-G-R), C-01 (S1 TL;DR), then C-14 (integration) | Wave-C requires all prior drafts as input — sequential after Wave-B |

Brigadier dispatches Wave-A in single message (parallel Task() calls). Awaits all returns. Per shared-protocols §5.5.5 promotes drafts to canonical drafts dir. Then dispatches Wave-B in single parallel-message. Then Wave-C.

## §Y Per-section gate + commit cadence

After EACH cell return:
1. Brigadier runs §5.5.5 provenance gate (§7 §2 of brigadier.md).
2. On pass: commit `[l6-deep-dive] §<N> <title> drafted` and push.
3. On fail: rejection in `swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/decisions/<ts>-rejection-<cell>.md`; re-invoke cell with context:{schema_error}.
4. Per-section gate-learning entry to `agents/brigadier/strategies.md` describing the section landing pattern.

## §Z Compound expectations (per launch §5)

Future brigadier (cycle 6+) reads this WBS + the resulting LAYER-6-COMMUNITY-DEEP-DIVE.md and does
better on Wave-2 deep-dives (L5 Product Directions + L7 Business Trajectory). Capture Wave-1 L6
patterns reusable for Wave-2 L5/L7:
- Cell-decomposition pattern (1 cell per top-level §)
- Wave-A/B/C dispatch sequence (independent → cross-reading → integration)
- Template-level vs Deep-Dive sections distinction (per Ruslan directives)
- Pre-section gate + immediate commit pattern (per shared-protocols)

---

*End of Phase-2 WBS. Brigadier proceeds to Wave-A dispatch.*
