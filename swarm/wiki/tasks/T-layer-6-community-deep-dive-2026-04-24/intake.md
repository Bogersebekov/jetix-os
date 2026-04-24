---
id: T-layer-6-community-deep-dive-2026-04-24
title: "Phase-1 Intake — Layer 6 Community Deep-Dive (ICP Trinity + Alliance + Matchmaker + Secure Network + Outreach)"
type: task-intake
created: 2026-04-24
cycle_id: cyc-layer-6-community-deep-dive-2026-04-24
brigadier_session: 5
prior_cycles: [swarm-self-improve-v1, km-architecture-research, km-materialization-mvp, jetix-system-overview]
operating_mode: Stage-Gated
deep_dive_policy: APPLIES (15-25K words, no compression) — EXCEPT §8 Membership + §9 Growth (template-level per Ruslan 2026-04-24 24:00)
full_auto_authorized: false
hitl_gate: AWAITING-APPROVAL before Part G compound/archive
task_class: M-structural (Method-development; Phase 2 Wave 1 revenue-critical)
niche: business
target_output: decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md
estimated_duration: 4-8 hours swarm parallel (may span 2 brigadier sessions via resume pattern)
status: phase-1-complete
---

# Phase-1 Intake — Layer 6 Community Deep-Dive

## §1 Acceptance predicate (Hamel-binary)

The cycle is **complete** when ALL of the following hold:

1. `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` exists, total word count between **15 000 and 25 000 words inclusive** (§8 Membership + §9 Growth contribute template-level 400-800 words each — counted toward the 15-25K total but not held to 1500-3000w per-section floor).
2. The document contains all 13 sections per §3 of launch prompt (`prompts/swarm-launch-brigadier-l6-community-deep-dive-2026-04-24.md`):
   - §1 TL;DR (400-600w)
   - §2 ICP Trinity (≥4K total: §2.1 Client ≥1500w; §2.2 Partner ≥1500w; §2.3 Team ≥1000w)
   - §3 11 Archetypes (≥3K total; 300-500w each)
   - §4 5-Criteria Filter (≥800w)
   - §5 Alliance Architecture (≥2K, 3 options ≥500w each + brigadier recommendation)
   - §6 Matchmaker Mechanics (≥1500w)
   - §7 Outreach Mechanism (≥3K + ≥15-20 ready-to-use message templates + discovery script + qualification questions + 3-audience landing skeletons)
   - §8 Membership / Invite Filter (400-800w — TEMPLATE LEVEL)
   - §9 Growth Model (400-800w — TEMPLATE LEVEL)
   - §10 Secure Network Architecture (≥1500w; Telegram primary; digital portraits; moderation; fork-community per D27; backup options brief)
   - §11 Evolution per gate (≥1K; G1 €50K → G2 €200K → G3 €1M → G4 $100M → G5 $1T)
   - §12 Open questions (≥500w)
   - §13 Preserved dissents + F-G-R tagging + citations (≥500w)
3. ICP expanded spectrum is honored verbatim per Ruslan 2026-04-24 24:00 CET clarification:
   - **Payment ability filter:** ≥$5K/month recurring OR ≥$10K one-shot engagement
   - **Income spectrum acceptable:** millionaires ($1M+/year), high-earners ($100K-$150K+/year), предприниматели + блогеры
   - Earlier KM-Mat Option-C Tier-1 lock {Предприниматели + Блогеры only} is **superseded**: Tier-1 is now broader per expanded spectrum
   - Tier-2 unlock trigger SG-2 first signed contract — **kept as-is**
4. Alliance §5 presents 3 options (non-profit consortium / for-profit standards body / hybrid) — each ≥500w with governance / IP / revenue / membership tiers / Phase-1 vs Phase-2+ fit / risks; brigadier recommends one; Ruslan picks in ack.
5. Outreach §7 produces ready-to-use templates Ruslan can immediately use:
   - 3-5 templates per archetype × LinkedIn/Email/Referral channels (minimum 15-20 templates total)
   - Realistic wording (not placeholders), `{{name}}` / `{{company_context}}` slots clearly marked
   - 15-20 min discovery call script structure
   - 10-15 qualification questions list
   - 3-audience landing skeletons (авантюристы / инвесторы / работники мечты per audio_507)
6. Secure Network §10 documents Telegram-based primary architecture (per audio_524) + digital portraits mechanic + moderation + fork-community governance per D27 + backup options (Discord / own platform — brief, not deep). Дуров contact marked "potential future contact", not assumed.
7. Per-section gate-learning entries written to `agents/brigadier/strategies.md`; per-expert learnings to `swarm/wiki/meta/agent-improvements/*.md`; emergent insights to `swarm/wiki/insights/`.
8. F-G-R tagging present per major claim; citations to source (audio_NNN / decisions/* / wiki/*) present per non-trivial paragraph.
9. AWAITING-APPROVAL packet at `swarm/gates/AWAITING-APPROVAL-layer-6-community-deep-dive-2026-04-24.md` written with: 1-line summary per section, Alliance Option A/B/C recommendation, open questions for Ruslan. **Brigadier HALTS** until ack.
10. Commit cadence: per shared-protocols §1, one commit per section landing; push after each. Target 15-18 commits total. Branch: `claude/jolly-margulis-915d34`. No `--amend`, `--no-verify`, or force-push.

## §2 Anti-scope (per launch §7)

- **NO** reopening the 28 Locks — flag conflict in §12 open questions, do not override.
- **NO** writing Phase 3 strategic documents (consulting-DACH / producer / JETIX-COMPASS) — those are separate M-tasks.
- **NO** writing Phase 4 outreach execution (actual outreach) — that is manual by Ruslan.
- **NO** max-depth §8 Membership / §9 Growth — template-level per Ruslan clarification.
- **NO** implementation code — description only.
- **NO** Notion writes (D17 filesystem-SoT).
- **NO** provider-key env-var references (Max-subscription discipline; literal env-var names elided per shared-protocols §9 to keep grep over `swarm/wiki/` clean).

## §3 Classification

- **PMBOK alpha-state:** α-1 task = `intaked` (transitioning to `planned` after WBS lands).
- **Operating-mode:** Stage-Gated. Full-Auto NOT authorized.
- **Task-class:** M (Method-development) — designing the foundation document for Phase-3 strategic docs + Phase-4 revenue. Matrix invocation 13+ cells across 5 experts. HITL gate at completion mandatory.
- **Niche:** business (per CLAUDE.md L70 6-niche lock).

## §4 Risks identified at intake

1. **Word-count overrun risk.** 15-25K words across 13 sections × 5 experts requires careful integration to avoid duplication and to stay within window. Mitigation: §3 acceptance predicate enumerates per-section floors; integration cell deduplicates and harmonizes.
2. **Alliance option drift.** Without Ruslan ack, brigadier could recommend an Option that doesn't match Ruslan's risk appetite (non-profit vs for-profit). Mitigation: §5 cell preserves all 3 options at full depth + dissents; brigadier recommendation is one paragraph, easily reversible by Ruslan.
3. **Outreach template realism.** Templates may sound generic if not anchored in Ruslan's actual voice (USB-C pitch, "самая большая авантюра века" framing). Mitigation: §7 cell instructed to weave in verbatim Ruslan voice anchors from `raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md` + JETIX-VISION §7-8.
4. **ICP $1M floor vs expanded spectrum tension.** L6 prior draft uses $1M+/year as Phase-1 buyer qualifier; new clarification expands to $100K-150K+/year + payment ability filter. Mitigation: §2.1 cell explicitly resolves this — payment-ability-as-filter (≥$5K/mo or ≥$10K one-shot), income spectrum is wider proof-of-ability (not gating criterion). Earlier KM-Mat Option-C Tier-1 lock superseded.
5. **Membership/Growth scope creep.** Risk that experts treat §8 + §9 as full Deep Dive. Mitigation: WBS cell acceptance predicate explicitly caps each at 800 words.
6. **Missing input source.** `reports/delta-506-529-2026-04-24.md` referenced in launch §11 does not exist on filesystem. Mitigation: cells use `reports/review_2026-04-24.md` (audio_506-529 references confirmed present at lines 105-291 + 245-295) as substitute. Flag in §12 open questions for Ruslan.
7. **Дуров contact assumption risk.** Launch §2.4 explicitly says "potential future contact, don't assume engagement". Mitigation: §10 cell instructed to mention as one-line aspirational, not actionable.
8. **Brigadier session context budget.** 13 cells × 5 experts × Deep Dive depth may exceed single brigadier session budget. Mitigation: per shared-protocols, brigadier can write `swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/resume-state.md` and continue in fresh session if approaching budget.

## §5 Inputs read (Phase-1 intake)

Per launch §11, in order:

1. ✅ `decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md` — Deep Dive Policy §0 + Phase 2 §4 confirmed
2. ✅ `decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md` — D25/D26/D27/D28 + USB-C reinforcement + Smart AI internal note
3. ✅ `decisions/JETIX-SYSTEM-OVERVIEW.md` (TOC + §6 USB-C/McKinsey resolution + §0 TL;DR)
4. ✅ `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L6-business.md` (full)
5. ✅ `swarm/wiki/drafts/T-jetix-system-overview-2026-04-24-mgmt-integrator-L8-people-alliance.md` (full)
6. ✅ `decisions/JETIX-VISION.md` §7 (D22 archetypes + 5-criteria filter) + §8 (per-archetype angles)
7. ✅ `decisions/JETIX-PLAN.md` §3 (Phase 1 pricing + 5-gate trajectory)
8. ✅ `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` (full — Alliance positioning §4-5)
9. ✅ `reports/review_2026-04-24.md` — targeted grep for audio_506-529 references (1858 units / 141 memo)
10. ⚠️ `reports/delta-506-529-2026-04-24.md` — **DOES NOT EXIST** on filesystem (flag in §12)
11. ✅ `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` (TOC; full content not required for L6)
12. ✅ `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partE-quick-money-levenchuk-bootstrap.md` (Option C ack confirmed; Tier-1 superseded by new ICP spectrum)
13. ✅ `swarm/wiki/operations/quick-money/icp.md` — existing ICP draft (Tier-1 starting point)

## §6 Ruslan clarifications 2026-04-24 24:00 CET (binding for cycle)

### §6.1 ICP expanded spectrum

> *«люди кто может платить от 5000 долларов в месяц или за раз от 10000, или миллионеры, но и те кто 100000-150000 зарабатывают в год. Предприниматели блогеры. Спектр довольно обширный.»*

Resolution: payment-ability-as-filter (≥$5K/mo or ≥$10K one-shot), income spectrum (millionaires + $100K-150K+/year + предприниматели + блогеры) is wider proof-of-ability, NOT income-floor-as-filter. Audio_529 $1M+ and audio_470 $240-600K tension resolved via this reframe.

### §6.2 Membership / Growth model template-level

> *«membership прямо сейчас growth model — ну как шаблон ещё можно иметь да по приколу. Окей давай попробуем хули нет.»*

§8 + §9 each 400-800 words structured skeleton, ready for future iteration. DO NOT over-engineer.

### §6.3 Alliance — 3 options with tradeoffs

3 legal-structure options proposed (non-profit consortium Linux Foundation analog / for-profit standards body ARM Holdings analog / hybrid). Each option presents governance + IP + revenue + membership tiers + Phase-1 vs Phase-2+ fit. Brigadier recommends one; Ruslan picks in ack.

### §6.4 Secure Network — Telegram-based primary

Per audio_524. Digital portraits mechanic designed. Backup options (Discord / own platform) noted briefly, not deep-dive. Дуров contact marked as "potential future contact", don't assume engagement.

### §6.5 Outreach templates — ready-to-use

§7 must produce templates Ruslan can immediately use: 3-5 per archetype × LinkedIn/Email/Referral channels = ≥15-20 total; realistic wording (not placeholders); discovery call script (15-20 min structure); qualification questions list (10-15).

## §7 Decision-rights ritual (per brigadier §1d)

| Action | Category | Authorization |
|---|---|---|
| Decompose into WBS cells (≤20 cap) | autonomous | proceed |
| Dispatch Task() to 5×4 matrix cells | autonomous | proceed |
| Integrate returned drafts (preserve dissents) | autonomous | proceed |
| Run §5.5.5 provenance gate | autonomous | proceed |
| Promote drafted → reviewed → accepted via gate | autonomous | proceed |
| Write `swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/*` | autonomous | proceed |
| Write `decisions/LAYER-6-COMMUNITY-DEEP-DIVE.md` (foundation-level Phase-2 deep-dive) | requires-approval | AWAITING-APPROVAL packet at completion |
| Compound learnings to `agents/brigadier/strategies.md` | autonomous | proceed (after Ruslan ack) |
| Cycle close → `swarm/logs/cyc-layer-6-community-deep-dive-2026-04-24/cycle-log.md` | autonomous | proceed (after Ruslan ack) |
| Notion writes / external comms / API key references | never | refuse |

## §8 Phase-1 → Phase-2 transition

Phase-1 intake complete. Transition to Phase-2 WBS at `swarm/wiki/tasks/T-layer-6-community-deep-dive-2026-04-24/decomposition.md` with 13 cells + integration cell, each carrying `class: M` and `cell_acceptance_predicate:`.

---

*End of Phase-1 intake. Brigadier proceeds to Phase-2 WBS.*
