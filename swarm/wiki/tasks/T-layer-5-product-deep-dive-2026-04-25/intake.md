---
id: intake-T-layer-5-product-deep-dive-2026-04-25
task_id: T-layer-5-product-deep-dive-2026-04-25
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
type: task-intake
phase: 1
state: drafted
created: 2026-04-25
produced_by: brigadier
launch_prompt: prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md
operating_mode: Stage-Gated
deep_dive_policy: APPLIES (15-25K words, no compression)
full_auto_authorized: false
max_subscription: true
target_output: decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md
word_target: 15000-25000
section_count: 15
direction_count: 9
sources:
  - {path: "prompts/swarm-launch-brigadier-l5-product-deep-dive-2026-04-25.md", range: "§1-§14 full"}
  - {path: "decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md", range: "§2 ICP Trinity + §3 Archetypes + §5 Alliance Option C + §7 Outreach templates"}
  - {path: "decisions/JETIX-SYSTEM-OVERVIEW.md", range: "§L5 Product & Services 9-direction table + Gates evolution"}
  - {path: "swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-investor-integrator-L5-products.md", range: "full ~1800w L5 system-overview draft"}
  - {path: "decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md", range: "Deep Dive Policy + Phase 2 Wave 2"}
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", range: "D25 Company-as-Code, D26 Team 50-100, D27 Fork-and-Merge, D28 Query-driven KB, USB-C reinforcement"}
  - {path: "decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md", range: "§3 buying frictions + §5 Path A/B/C + §8 7 recommendations"}
  - {path: "decisions/JETIX-VISION.md", range: "§5 D11 producer center + D5 Secure Network + D21 matchmaker + D23 tokens + §7 archetypes"}
  - {path: "decisions/JETIX-PLAN.md", range: "§3 Phase 1 (€50K Q2 2026) + §4 Phase 1→2 transition + §5 Phase 2 Secure Network + §6 Phase 3"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "Dissent 3 Path B vs Path C Phase-A default"}
  - {path: "raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md", range: "Voice 2 USB-C verbatim pitch — sales asset"}
  - {path: "reports/review_2026-04-24.md", range: "audio_508/510/511/514/515/524/527/528/529 ICP+Smart AI+tokens+YouTube-analyzer"}
  - {path: "swarm/wiki/operations/quick-money/icp.md", range: "current Tier-1 consulting ICP (superseded by L6 §2 expanded spectrum)"}
  - {path: "swarm/wiki/operations/quick-money/pipeline.md", range: "current pipeline state-machine + SG-5 predicate"}
  - {path: "CLAUDE.md", range: "project roster + 28 Locks quick reference + KM MVP skills"}
---

# Intake — LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md

## §1 Task framing

Write **`decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md`** — Phase 2 Wave 2 foundation document, 15-25K words, 15 sections, describing all 9 product directions of Jetix's L5 product portfolio, mapping each to the L6-ack'd ICP Trinity + archetypes + Alliance Option C, laying out phase activation triggers, offer structures, delivery mechanisms, evolution per 5 gates, cross-direction synergies, and a Tools Roadmap per phase.

**Revenue-critical placement in plan.** L6 (acked 2026-04-25 01:00 CET) defined the ICP Trinity and Alliance structure — *whom* to sell to. L5 (this document) answers *what* to sell. L7 (next cycle) will answer *how much + how scaled*. Without L5, Phase 3 strategic documents (`ai-consulting-dach/strategy.md`, `producer-services/strategy.md`) cannot describe offer structure; Phase 4 outreach cannot pitch a concrete product.

## §2 Ack'd constraints from L6 (MANDATORY context, do not re-litigate)

L6 Community Deep-Dive was ack'd with seven binding decisions brigadier must apply verbatim in L5:

1. **ICP expanded spectrum:** Tier-1 = payment-ability filter **$5K/mo recurring OR $10K one-shot** + three income categories (millionaires $1M+/year / high-earners $100-150K+/year / предприниматели-блогеры revenue-variable). Income is not a gate; payment-ability is the gate. [src:LAYER-6 §2.1]
2. **P1A primary (active cold outreach) = Mittelstand + Startupper** (legacy KM-Mat Tier-1, proven hypothesis).
3. **P1B opportunistic (referral-driven) = High-earners + миллионеры**.
4. **Alliance = Option C Hybrid** (Foundation non-profit upstream + Jetix-Corp proprietary downstream; Mozilla/Red Hat analog). [src:LAYER-6 §5 + ack]
5. **IP license = Apache 2.0 docs + LGPL-equivalent software Foundation; proprietary Jetix-Corp core**.
6. **Phase-1 archetypes primary buyers** = 4 of 11: **Startupper / Блогер / Operator-Founder-CEO / Teacher**.
7. **Matchmaker cadence: Phase-1 = manual Ruslan; Phase-2 = AI-smoothed coordination; Phase-2+ = platform MVP**.

**Implication for L5:** every direction section must map to the relevant L6 archetype(s) and specify the payment-ability filter fit. Direction priority order reflects P1A/P1B distinction (consulting + producer are P1A-facing; Secure Network/tokens serve P1B and partner segments at later gates).

## §3 The 9 directions (MANDATORY — 1500-2000 words each, §3.1-§3.9)

Per system-overview §L5 table + investor-integrator L5 draft + voice-memos:

| # | Direction | Phase activation | Primary audio ref |
|---|---|---|---|
| 1 | AI Consulting for complex tasks | Phase 1 core (G0→G1) | audio_511 + 4-pack offer |
| 2 | Продюсерский центр | Phase 1 core (G0→G1) | audio_508 + JETIX-VISION §9 D11 |
| 3 | USB-C Integration Services | Phase 2+ productized (G1→G2 first client; G2→G3 productized) | audio_508 + Voice 2 + STRATEGIC-INSIGHT Path A/B/C |
| 4 | Matchmaker Platform | Phase 1 manual (Ruslan); Phase 2+ AI-smoothed; Phase 2+ platform | audio_514 + D21 |
| 5 | Secure Network | Phase 2+ (G1→G2 design; G2→G3 launch) | audio_510 + audio_524 + LAYER-6 §10 Telegram-primary |
| 6 | YouTube-analyzer SaaS | Phase 2+ (G3→G4 SaaS launch) | audio_514 "золотая жила" + audio_527 reverse-engineering |
| 7 | Educational Products + Investor Programs + Grant Hunting | Phase 2+ (G2→G3 methodology repo V1) | audio_524 + audio_527 + JETIX-VISION §7 + D27 |
| 8 | Tokens / ICO (D23 Option B) | Phase 3+ ($100K threshold internal utility; public Phase 3+) | audio_511 + audio_527 + D23 |
| 9 | Smart AI flagship label | Cross-phase internal narrative, NOT D29 lock | audio_529 + D25-D28 addendum |

Each direction section uses the **mandatory template** from launch prompt §4: Mission / Phase activation / Target ICP mapping (uses L6 Trinity) / Value proposition / Offer structure / Delivery mechanism / Competitive positioning / Evolution per gate / Cross-direction dependencies / Open questions.

## §4 15 sections structure (for WBS)

- **§1 TL;DR** (400-600w) — 9 directions + Phase-1 active + Smart AI flagship narrative
- **§2 Portfolio overview** (1500-2000w) — 9×5 matrix table + portfolio logic narrative + "why these 9"
- **§3.1** AI Consulting (1500-2000w)
- **§3.2** Продюсерский центр (1500-2000w)
- **§3.3** USB-C Integration Services (1500-2000w)
- **§3.4** Matchmaker Platform (1500-2000w)
- **§3.5** Secure Network (1500-2000w)
- **§3.6** YouTube-analyzer SaaS (1500-2000w)
- **§3.7** Educational Products + Investor Programs + Grant Hunting (1500-2000w)
- **§3.8** Tokens / ICO (1500-2000w)
- **§3.9** Smart AI flagship narrative (1500-2000w — note: internal label treatment + audio_529 смартфон/телефон framing)
- **§12 Cross-direction synergy + conflict matrix** (1000-1500w)
- **§13 Evolution per gate master table** (1000-1500w)
- **§14 Tools Roadmap per phase** (1500-2500w) — §14.1 Phase-1 have/need / §14.2 Phase-2 / §14.3 Phase-3+ / §14.4 Cross-phase
- **§15 Open questions + preserved dissents + F-G-R tagging** (500-1000w)

**Total floor:** 15 × 1500 (conservative) = 22 500 words core + 3 meta sections ≈ **23-25K words** total. Hits Deep Dive policy.

## §5 Deep Dive policy compliance

Per `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` Deep Dive Policy locked by Ruslan 2026-04-24 23:50 CET:

- **15-25K слов minimum** — WBS allocates explicit word floors per cell
- **No compression / no summary mode** — each direction gets full template coverage (10 sub-items)
- **Diagrams** — ASCII/Mermaid required for §13 master evolution table + §12 synergy graph + §14 tools roadmap
- **Evolution per gate expanded** — each direction §3.N has per-gate shape; §13 is the master cross-section
- **Preserved dissents + F-G-R tagging** — §15 consolidation
- **Citations** — inline `[src:<path>#<section>]` per non-trivial paragraph per shared-protocols §2
- **Open questions** — §15 consolidated from per-direction sections
- **Ruslan approval gate** — AWAITING-APPROVAL after Part F verification; Full-Auto NOT authorized

## §6 Anti-scope (enforced via /lint + §5.5.5 gate)

- **NO reopening 28 Locks** (D1-D28) — flag conflict in §15 Open Questions, do not override
- **NO final pricing decisions** — L7 Business Deep-Dive owns pricing; L5 proposes **placeholder ranges** only (€X-€Y tier markers ok; absolute commitments not)
- **NO strategic docs writing** (`directions/_active/ai-consulting-dach/strategy.md`, `directions/_active/producer-services/strategy.md`) — those are Phase 3 separate cycles
- **NO Phase 4 outreach execution** — Ruslan manual
- **NO implementation of tools** — §14 is spec + roadmap only; revenue-triggered Phase 4 cycles build
- **NO Notion writes** (D17 filesystem-SoT)
- **NO provider-key env-var literal references** (Max-subscription discipline; only Whisper pipeline exception per shared-protocols §9)
- **NO D29 Smart AI promotion** — Ruslan explicit «ну типа запиши между прочим но нет это ещё не лок блять забей хуй» [src:D25-D28 §Smart AI]; §3.9 treats Smart AI as internal narrative framing, not external product name lock

## §7 Cell distribution (preview — WBS detail in decomposition.md)

Per launch prompt §6:

- **mgmt-expert (integrator):** §2 Portfolio + §3.1 Consulting + §3.2 Producer + §12 Cross-direction synergy — revenue-primary directions
- **systems-expert (integrator + scalability):** §3.3 USB-C + §3.4 Matchmaker + §3.5 Secure Network + §13 Evolution per gate master table
- **investor-expert (scalability + critic):** §3.6 YouTube SaaS + §3.7 Educational + §3.8 Tokens + pricing placeholder validation
- **philosophy-expert (critic):** §3.9 Smart AI flagship + §15 Open questions + overall coherence review + D14/D22/D26 consistency check
- **engineering-expert (integrator):** §14 Tools Roadmap + §1 TL;DR (integration-adjacent — after all drafts land)

Wave structure (for parallelism within shared-protocols §5 tool-permission matrix):

- **Wave A (parallel 3 cells):** §2 Portfolio + §3.1 Consulting + §3.2 Producer → mgmt-expert 3 cells
- **Wave B (parallel 7 cells):** §3.3 USB-C + §3.4 Matchmaker + §3.5 Secure Network + §13 (systems 4) + §3.6 YouTube + §3.7 Educational + §3.8 Tokens (investor 3)
- **Wave C (parallel 4 cells):** §3.9 Smart AI + §15 Open Q (philosophy 2) + §14 Tools Roadmap (engineering 1) + §12 Synergy (mgmt 1, depends on Wave-A + Wave-B)
- **Wave D (integration cell, sequential):** §1 TL;DR drafted last by brigadier integrator after all drafts land; integration pass + canonical doc write

## §8 Phase-2 entry checklist (brigadier gate)

Before dispatch:
- [x] 11 input sources read (§12 launch prompt §13)
- [x] L6 ack'd constraints extracted (§2 above)
- [x] 15 sections scoped with word floors (§4 above)
- [x] Deep Dive policy compliance verified (§5 above)
- [x] Anti-scope enumerated (§6 above)
- [x] Cell distribution pre-agreed with launch prompt §6 (§7 above)

Phase-2 WBS (15 cells + class:M + cell_acceptance_predicate per cell) is the next artefact at `decomposition.md`.

---

*Intake produced by brigadier 2026-04-25. Proceeds to Phase-2 WBS immediately.*
