---
title: Phase 0+ — Ruslan acks 17.05 evening (wiki promotions + H8 lock + cleanup + new directions)
date: 2026-05-17 evening
type: deep-prompt
target: server CC (brigadier mode, autonomous, 1-2h)
trigger: Ruslan explicit acks 17.05 evening on voice-pipeline-2026-05-17-batch decisions D-01..D-08 + work plan items
parent_reports:
  - reports/voice-pipeline-2026-05-17-batch/04-detailed-work-plan.md
  - reports/voice-pipeline-2026-05-17-batch/03-fpf-lens-jetix-track.md
  - reports/voice-pipeline-2026-05-17-batch/00-MASTER-INDEX.md
  - reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md
language: russian
---

# DEEP PROMPT — Phase 0+ Ruslan acks execution

> **Ты = brigadier** (per `.claude/agents/brigadier.md`, opus). Multi-agent swarm. Constitutional: Tier 2 R1/R2/R6/R11 + append-only + no API keys.

> **ultrathink** ON.

---

## §0 RUSLAN ACKS 2026-05-17 evening (explicit)

Ruslan прочитал voice-pipeline-2026-05-17-batch + дал acks. Зафиксировано verbatim ниже — это **operational instructions**, не surface options.

### §0.1 Wiki candidates (D-04 + D-07 + general)
- ✅ **ВСЕ wiki candidates Tier A/B/C → ACK PROMOTE.** Промотируй всё что в `reports/voice-pipeline-2026-05-17-batch/05-wiki-candidates.md`. Особенно — все что «может пригодиться». Не дискриминируй по Tier.
- ✅ **D-04 Onboarding hypothesis → wiki claim** (с F-G-R + falsifiable).
- ✅ **NC-1 Trust Infrastructure → wiki entry + concept.** Зафиксировать.
- ✅ **NC-2 «Дорога» → wiki entry / object placeholder.** Зафиксировать.

### §0.2 H8 Hexagon (D-02)
- ✅ **D-02 text_001 trust-mechanism → H8 LOCK как 8-й Strategic Insight.** «Можем вообще брать спокойно, ебашь Hexagon». Это значит:
  - Create `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` (или похожий H8 LOCK name)
  - Format same as 6+1 existing insights (Foundation Model / Partnership / Network State / Tyson / Gamified Platform / People-NS)
  - F-G-R triple, multi-view 1A/1B, provenance trail
  - Update Hexagon → Octagon naming OR resolve Hexagon-vs-Heptagon XD-03 once and for all

### §0.3 Что УДАЛЯЕМ из active work plan (Ruslan: «голову не ебать»)
- ❌ **IA-02 LIVE-FLAG ICP** → УДАЛИТЬ из active blockers. «Pohuy на старое». **НЕ trog'ать Doc 1B LOCKED original** (append-only). Просто:
  - Update Phase 0 master document — remove ICP from §QR-CARD critical blockers
  - Update voice-pipeline work-plan — remove IA-02 from immediate actions
  - Mark CR-01 в kasha-cleanup-flags как `RUSLAN-DEPRIORITIZED-2026-05-17` (НЕ delete entry; mark)
- ❌ **IA-03 Strategic Council status-check** → «послание уже отправлено, pohuy на старое». Mark CR-05 / SA-07 / ST-05 as `RUSLAN-CLOSED-2026-05-17`
- ❌ **IA-04 EP-5 F-grade disclosure patch** → «не понял, удаляй нахуй». **НО:** EP-5 disclosure всё ещё factually correct (Jetix F8 ≠ FPF B.3 F8). Не удалять disclosure из existing docs (append-only). Только remove «patch action» из active work plan. Mark as `RUSLAN-DEPRIORITIZED-2026-05-17`.
- ❌ **ST-04 B2 Aisystant unblock** → memory rule per Ruslan 17.05 «IWE chat rejected, only materials». Mark as **CLOSED-by-decision**.

### §0.4 Что ФИКСИРУЕМ (active week plan)
- ✅ **IA-01 Trust mechanism insight → wiki entry** (folds into D-02 H8 lock workflow)
- ✅ **ST-01 Единый FPF документ для L1** — create skeleton + fix в Notion daily log
- ✅ **ST-02 Существующие планы → FPF translation** — track в week plan
- ✅ **ST-03 Onboarding-via-FPF hypothesis** — описать + затестировать + пример привести. Wiki claim + falsifiable.
- ✅ **ST-06 Human-readable Jetix description (для L1)** — но: **workflow Human → FPF → Human → FPF → ...**. Сперва на человеческом → потом на FPF → потом ещё раз на человеческом. Зафиксировать workflow.

### §0.5 Strategic Directions (D-07 + D-08 + general)
- ✅ **Все SD-01..SD-06 зафиксировать** в `decisions/STRATEGIC-DIRECTIONS-VOICE-17-2026-05-17.md` чтобы НЕ потерялись. Phase C work подойдём к ним позже.
- ✅ **NC-1 Trust Infrastructure** (D-07) — зафиксировать в wiki + Phase 0 inventory candidate (O-21 placeholder с status `Ruslan-acked-as-candidate-pending-architectural-decision`)
- ✅ **NC-2 «Дорога»** (D-08) — зафиксировать как O-05 re-frame candidate

### §0.6 Legacy 12 agents (D-05) — DELETE
- ✅ **«Удалить нахуй»** — Ruslan explicit. Actions:
  - Update `CLAUDE.md` Agent Roster section — mark all 14 legacy agents as `DEPRECATED-2026-05-17` (append-only — НЕ remove section, mark)
  - Move `.claude/agents/*.md` для 12 legacy roster → `.claude/agents/_archived/` (preserve filesystem history per append-only)
  - НЕ touch'ать ROY swarm agents (brigadier / engineering-expert / philosophy-expert / systems-expert / mgmt-expert / investor-expert / autoresearch-brigadier / project-brigadier / quick-money-brigadier / levenchuk-deep-dive-brigadier stub) — они active operational
  - Update routing-table.yaml comments to flag legacy section deprecated
  - **AWAITING-APPROVAL packet** для `CLAUDE.md` change (CLAUDE.md = strategic substrate per Pillar A) — Ruslan ack этого prompt'a = ack packet contents

### §0.7 Phase namespace cleanup (D-06)
- ✅ **«Можно делать сейчас»** — cleanup PH-01..08 collision (Workshop Phase 1/2 vs ACTION-PLAN Phase 1 vs CLAUDE.md Phase 1-4 vs ROY Phase A/B/C). 
- Action: add **prefix convention** в каждом upstream document:
  - Workshop → `Workshop-Phase-N`
  - ACTION-PLAN → `Commercial-Phase-N`
  - CLAUDE.md agent deployment → `Agent-Deploy-Phase-N`
  - ROY swarm → `Swarm-Phase-A/B/C`
- Create `decisions/PHASE-NAMESPACE-CONVENTION-2026-05-17.md` LOCK
- Update affected docs с prefix (append clarification, не replace) — Foundation Parts skip (R2 require packet)

### §0.8 Oscar Hartmann CRM-add
- ✅ **NEW-K-01** Oscar Hartmann → `/crm-add` через standard CRM skill. Status: `cold` / `discovery_call`. Edge type: `partnership-candidate`. Source: audio_673 voice batch 17.05.
- Resource profile fields (capital + audience + networking) per Γ_work mapping

---

## §1 Cell dispatch matrix

| Task | task_shape | Cells |
|---|---|---|
| T1 Wiki promotion (all candidates) | review | eng × critic + phil × critic + mgmt × critic |
| T2 H8 LOCK Strategic Insight | design | mgmt × integrator + phil × critic + eng × integrator |
| T3 Strategic Directions SD-01..06 → decisions/ | review | mgmt × integrator + phil × critic |
| T4 NC-1 Trust Infrastructure + NC-2 «Дорога» fix | design | eng × integrator + phil × critic + sys × integrator |
| T5 Onboarding hypothesis wiki claim (с test design) | design | eng × integrator + mgmt × integrator + phil × critic |
| T6 Delete legacy 12 agents (CLAUDE.md + archive) | review | mgmt × critic + phil × critic + sys × scalability |
| T7 Phase namespace cleanup | review | mgmt × critic + phil × critic |
| T8 Oscar Hartmann CRM-add | (skill direct) | brigadier invokes `/crm-add` |
| T9 Remove deprecated items from work plan | (cleanup) | brigadier scribe |
| T10 Update Phase 0 master + voice-pipeline reports | (cleanup) | brigadier scribe |

Brigadier integrates per AP-6 + §5.5.5 gate перед каждым canonical write.

---

## §2 Output structure

```
wiki/                                          # promoted candidates (Ruslan-acked Tier A/B/C)
  ideas/                                        # new ideas from wiki-candidates
  claims/                                       # onboarding hypothesis etc
  concepts/                                     # trust-infrastructure / road-metaphor / etc

decisions/
  STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md  # ⭐ H8 LOCK
  STRATEGIC-DIRECTIONS-VOICE-17-2026-05-17.md                # SD-01..SD-06
  PHASE-NAMESPACE-CONVENTION-2026-05-17.md                   # naming LOCK

swarm/awaiting-approval/
  legacy-12-agents-deprecation-2026-05-17.md                 # AWAITING-APPROVAL packet (Ruslan ack via prompt)

.claude/agents/_archived/                                    # legacy agents moved here
  manager.md
  personal-assistant.md
  system-admin.md
  sales-lead.md
  sales-researcher.md
  sales-outreach.md
  inbox-processor.md
  crazy-agent.md
  knowledge-synth.md
  strategist.md
  life-coach.md
  meta-agent.md
  staging-writer.md
  sweep-worker.md

crm/people/oscar-hartmann.md                                 # new entry

reports/voice-pipeline-2026-05-17-batch/
  04-detailed-work-plan.md                                   # UPDATED — remove deprecated IA-02/03/04 + ST-04/05
  
reports/phase-0-fpf-scope/
  00-JETIX-FPF-MASTER-2026-05-17.md                          # UPDATED — remove ICP from §QR-CARD blockers; add H8/NC-1/NC-2
  01-jetix-objects-inventory.md                              # APPEND — O-21 Trust Infrastructure (candidate); O-05 NC-2 note
  04-kasha-cleanup-flags.md                                  # UPDATED — CR-01/05/07 marked `RUSLAN-DEPRIORITIZED-2026-05-17`

CLAUDE.md                                                    # UPDATED — legacy 12 agents DEPRECATED-2026-05-17
```

---

## §3 Per-task acceptance

### T1 Wiki promotion
- All 12 wiki candidates (Tier A:1 + B:6 + C:5) → promoted to appropriate wiki/ subdirs
- Each entry has frontmatter (F-G-R / sources / status: `ruslan-acked-2026-05-17`)
- `wiki/index.md` updated
- `wiki/log.md` prepended
- `wiki/graph/edges.jsonl` extended

### T2 H8 Strategic Insight LOCK
- `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` follows existing 6 insights structure (e.g. STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL pattern)
- F8 LOCK status with single-author Ruslan-ack note (EP-5 disclosed)
- 1A/1B multi-view if applicable
- Provenance trail: text_001 + audio_672-673 + 4 cross-cell triangulation evidences
- **Hexagon → Octagon naming resolved** OR explicit decision why оставляем "Hexagon" с count=8

### T3 Strategic Directions doc
- All 6 SD entries preserved verbatim from work-plan §3
- Per SD: Stage gate / dependencies / Phase association
- Status: `surfaced-pending-Ruslan-priority`

### T4 NC-1 + NC-2
- `wiki/concepts/trust-infrastructure-positive-signaling.md` (NC-1)
- `wiki/concepts/jetix-as-road-protocol-infrastructure.md` (NC-2)
- Cross-refs: NC-1 ↔ O-11 R12 (complementary), NC-1 ↔ O-13 Clan, NC-2 ↔ O-05
- Phase 0 inventory APPEND: O-21 Trust Infrastructure (candidate)

### T5 Onboarding hypothesis
- `wiki/claims/onboarding-via-fpf-3h-vs-3-4w.md`
- F-G-R: F3 · onboarding-claim · refuted_if_FPF-loaded-AI-onboarding-takes-longer-than-vanilla-baseline-for-equivalent-task
- Test design section: cohort definition / baseline / measurement / success criteria
- Example: «загрузить FPF в AI + дать Jetix project context → measure time to first useful output vs vanilla AI»

### T6 Legacy 12 agents deprecation
- `swarm/awaiting-approval/legacy-12-agents-deprecation-2026-05-17.md` packet with ack-trail: «Ruslan voice-batch ack 17.05 evening via Cloud Cowork session»
- 14 files moved to `.claude/agents/_archived/` (git mv to preserve history)
- CLAUDE.md Agent Roster section → mark all 14 as `DEPRECATED-2026-05-17 — Ruslan-acked via voice-batch processing`
- ROY swarm agents (brigadier + 5 experts + 4 sub-brigadiers) untouched + section added «Active ROY Swarm»

### T7 Phase namespace
- `decisions/PHASE-NAMESPACE-CONVENTION-2026-05-17.md` LOCK с prefix table
- Affected docs APPEND clarification (Workshop / ACTION-PLAN / CLAUDE.md / ROY)
- Foundation Parts skip (require AWAITING-APPROVAL — not in scope here)
- Kasha-cleanup-flags PH-01..08 marked resolved

### T8 Oscar Hartmann CRM
- `crm/people/oscar-hartmann.md` created via existing `/crm-add` skill format
- Frontmatter: source=audio_673, status=cold, edge=partnership-candidate, role=hartmann-investor-builder
- §7 strategy hooks: offers (FPF-described Jetix capability) / asks (capital + audience access)

### T9 Remove deprecated work-plan items
- `reports/voice-pipeline-2026-05-17-batch/04-detailed-work-plan.md` UPDATE:
  - Remove IA-02 ICP from §1 (Ruslan deprioritized)
  - Remove IA-04 EP-5 patch from §1
  - Remove ST-04 Aisystant from §2
  - Remove ST-05 Strategic Council from §2
  - Add note «Ruslan acks 17.05 evening — these items deprioritized/closed»
  - Append-only — keep original sections, add deprecation markers

### T10 Phase 0 master + reports update
- `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` UPDATE:
  - §QR-CARD critical blockers — remove ICP, EP-5, B2, Strategic Council
  - §5 add H8 LOCK reference
  - Open questions OQ-MASTER-1..10 update (D-01/02/07/08 resolved per acks)
- `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` APPEND O-21 candidate row
- `reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md` UPDATE deprecation markers

---

## §4 Constitutional posture

- **R1** — Ruslan = sole strategist. All actions are **executions of his acks**, не authored. Where ambiguity (e.g. H8 Hexagon rename vs Octagon) — surface as escalation, не auto-decide.
- **R2** — Foundation paths read-only. CLAUDE.md = strategic substrate (Pillar A territory) — Ruslan ack via this prompt counts as AWAITING-APPROVAL packet content. Brigadier creates formal packet doc для audit trail.
- **R6** — provenance per item (audio_NNN:para OR text_001:§N for new items; existing wiki entries inherit source provenance)
- **R11** — Default-Deny still respected for any uncategorized side-effects
- **Append-only** — НЕ delete original LOCKED documents (Doc 1B, Foundation Parts). Только mark deprecated / add clarifications.

---

## §5 Что НЕ делать

- НЕ trog'ать Foundation Parts (`swarm/wiki/foundations/`) без separate AWAITING-APPROVAL
- НЕ delete Doc 1B / Doc 1A / ACTION-PLAN / Charter — append-only, mark only
- НЕ remove EP-5 disclosure from docs где она была (keep historical accuracy); только remove «active patch action» from work plan
- НЕ авторизовать wiki promotion для НЕ-acked items вне current 12 candidates
- НЕ resurrect IA-02/IA-03/IA-04/ST-04/ST-05 — explicitly Ruslan-deprioritized
- НЕ создавать new Strategic Insights помимо H8 (Ruslan acked только H8 here)
- НЕ touch ROY swarm agents

---

## §6 Cost cap

- Daily €10 baseline; halt+ask at €50
- All work через Claude Code Max headless (no external API spend)
- Expected: <€1 (mostly text generation + git ops)

---

## §7 Acceptance criteria

- [ ] T1: 12 wiki entries promoted с frontmatter
- [ ] T2: STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md LOCKED
- [ ] T3: STRATEGIC-DIRECTIONS-VOICE-17-2026-05-17.md captured 6 SDs
- [ ] T4: NC-1 + NC-2 wiki entries + Phase 0 O-21 candidate added
- [ ] T5: Onboarding hypothesis claim wiki entry + test design
- [ ] T6: Legacy 12 agents archived + AWAITING-APPROVAL packet + CLAUDE.md updated
- [ ] T7: PHASE-NAMESPACE-CONVENTION LOCKED + clarifications added к 4 docs
- [ ] T8: Oscar Hartmann CRM entry
- [ ] T9: Work plan deprecation markers
- [ ] T10: Phase 0 master + inventory + kasha-flags updated
- [ ] git commits per Task
- [ ] Final `git push origin main`
- [ ] SUMMARY file: `reports/phase-0-plus/00-SUMMARY-2026-05-17-evening.md` ≤1000 слов

---

## §8 Context files (read first)

- `reports/voice-pipeline-2026-05-17-batch/00-MASTER-INDEX.md` — 8 decisions context
- `reports/voice-pipeline-2026-05-17-batch/04-detailed-work-plan.md` — items being updated
- `reports/voice-pipeline-2026-05-17-batch/05-wiki-candidates.md` — Tier A/B/C list
- `reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md` — Phase 0 master
- `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` — 14 objects table
- `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` — H8 LOCK pattern reference
- `CLAUDE.md` — Agent Roster section to modify
- `.claude/agents/` — files to triage
- `crm/_schema/` — Oscar Hartmann frontmatter format
- `swarm/lib/shared-protocols.md` — §5.5.5 gate

---

**Launch:**

```bash
tmux new -s phase-0-plus
cd ~/Desktop/jetix-os && git pull --rebase origin main && claude --dangerously-skip-permissions
```

Paste:

```
ultrathink. Прочитай prompts/phase-0-plus-ruslan-acks-2026-05-17.md полностью. Ты — brigadier. Все §0 RUSLAN ACKS = explicit operational instructions, не surface options. 10 tasks через cell dispatch (per §1 matrix). T1 wiki promotion / T2 H8 LOCK / T3 strategic directions / T4 NC-1+NC-2 / T5 onboarding hypothesis / T6 legacy 12 agents deprecation (CLAUDE.md + AWAITING-APPROVAL packet) / T7 phase namespace / T8 Oscar Hartmann CRM / T9 work plan cleanup / T10 Phase 0 master update. §5.5.5 provenance gate перед canonical writes. AP-6 dissent preservation если cells disagree. R1+R2+R6 preserved. Действуй автономно 1-2 часа, коммить per task, push origin main в конце.
```

Detach: `Ctrl+B затем D`.
