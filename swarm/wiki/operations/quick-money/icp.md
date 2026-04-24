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
