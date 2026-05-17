---
title: FPF Describe Jetix System — Phase 1 Plan (Decomposition + Verification Protocol)
date: 2026-05-17
type: brigadier-phase-1-plan
status: brigadier-structured (R1 surface-only)
prose_authored_by: ruslan-via-voice-dictation+brigadier-structured
audience: Ruslan (primary) + Phase 2 cells (dispatch brief) + L1 future readers
parents:
  - prompts/fpf-describe-jetix-system-plan-then-execute-2026-05-17.md
  - vision/00-MASTER-VISION-PLAN-2026-05-17.md
  - vision/09-immediate-steps-current.md
  - decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md
  - raw/voice-memos-2026-05-17-batch/text_004@17-05-2026_23-30.md
F: F3
G: jetix-fpf-describe-phase-1-plan
R: refuted_if_Phase-2_cannot_produce_8_docs_in_3h_OR_L1_reader_does_not_grasp_jetix_in_90min
authority: brigadier (decomposition + verification protocol); Ruslan = sole strategist on content
mandatory_disclosures:
  - EP-5: "Jetix F8" = single-author Ruslan ack ≠ FPF B.3 F8 (independent verification)
  - EP-2: plan describes Phase 2 artefacts (mention); does not assert Phase 2 outputs exist yet
language: russian + english (FPF primitives)
---

# FPF Describe Jetix System — Phase 1 Plan

> **Disclosure EP-5.** Throughout this document «F8 / LOCKED / canonical» = Jetix-internal single-author-ack semantics. NOT FPF B.3 F8 (which requires independent verification). Semantic drift risk noted per Phase 0 OQ-5.
>
> **Disclosure EP-2.** Phase 2 artefacts described below = intended structure (mention of forthcoming files). At Phase 1 commit, only this plan exists; doc 01-07 are TBD in Phase 2.
>
> 10-min read.

## §0 TL;DR

Brigadier декомпозирует L0 «FPF describe Jetix system + interactions» в **8 FPF-described docs** (1 index + 6 main parts + 1 end-to-end synthesis). Логика порядка bottom-up педагогически: Self-OS substrate → Methodology → Virtual Tribe → Corporation → Platform → Clean Internet Layer → End-to-End overview. Каждый artefact проходит **3+ FPF-trained cells verification chain** (eng-integrator drafts → phil-critic + eng-critic review parallel → brigadier integrates с AP-6 → §5.5.5 gate → canonical write + git commit). text_004 (humans-as-info-processing-instruments + virtual tribe) распределяется по 5 placements: PRIMARY в doc 03 + cross-refs в 02/06/07 + H8 extends_via comment + master-vision 1-line ref. Total Phase 2 deliverable: 8 markdown docs + 7 mermaid diagrams + 3 reports + ~24-32 cell drafts в `swarm/wiki/drafts/`. Cost estimate <€3, runtime ~2.5-3.5h autonomous. R1 attribution explicit, R2 Foundation read-only, R6 per-claim provenance, R11 Default-Deny categorized, R12 anti-extraction substrate. АВТОНОМНЫЙ ACK §1.5 fires after this Phase 1 commit → Phase 2 launches without further ack.

[src: prompts/fpf-describe-jetix-system-plan-then-execute-2026-05-17.md §1.3 + §1.5 + §2]

---

## §1 Decomposition — 8 docs (Phase 2 deliverables)

### §1.1 Reading order (bottom-up педагогически)

Логика: individual reflection → method connecting individuals → tribes formed via mutual instrumentation → commercial vehicle → platform interface → network protocol → integrated view.

| # | Slug | Primary anchor | Content focus |
|---|---|---|---|
| **00** | `00-MASTER-INDEX.md` | navigation | Reading order + map + L1 entry guidance |
| **01** | `01-jetix-as-self-os-substrate.md` | O-01 + O-07 + Self-OS spec | Individual info-processing layer (input→filter→digestion→output); reflection baseline; Foundation Parts 1+5+8+9 reference |
| **02** | `02-jetix-as-methodology.md` | O-05 + FPF Spec | FPF as universal language; method distribution mechanics; ШСМ/МИМ overlay; Fork-and-Leave |
| **03** | `03-jetix-as-virtual-tribe-substrate.md` | O-13 + text_004 + H8 cluster | **text_004 PRIMARY HOME** — humans-as-instruments + role-based mutual instrumentation + R12 anti-extraction + Clan activation |
| **04** | `04-jetix-as-corporation.md` | O-02 + Doc 1B | Commercial vehicle; TRM ladder; 3 engagement tiers; LIVE-FLAG (Mittelstand vs Online-first ICP unresolved) |
| **05** | `05-jetix-as-platform.md` | O-14 + Workshop concept | Meta-workshop / мастерская entry; 6-cluster topology; L1 prototype CC 2-day intent (NOT SLA) |
| **06** | `06-jetix-as-clean-internet-layer.md` | O-21 (Trust Infra candidate) + H8 LOCKED + text_002 | New internet layer for engineers; 7-primitive trust cluster (A.2.8 + A.2.9 + A.2.1 + A.10 + B.3 + E.5 + E.17); replaces money-as-trust-medium |
| **07** | `07-jetix-end-to-end-overview.md` | synthesis | Bridging document — L1 entry point combining all 6 parts; centerpiece mermaid with inter-part flows |

### §1.2 Why bottom-up

Alternative top-down ordering (corporation → platform → internet → tribes → method → self → overview) — менее pedagogical: читатель сталкивается с commercial framing до того, как поймёт substrate. Bottom-up: L1 reader строит mental model from substrate outward, finishing с synthesis. Это alignment с Ruslan voice text_003: «L0 = describe Foundation», substrate first.

[src: prompts/...-2026-05-17.md §1.3.1.3 logical-order requirement; vision/00-MASTER-VISION-PLAN §3 layered approach]

---

## §2 Per-doc spec (FPF primitives + cells + verification chain)

### §2.1 Common template

Каждый doc следует структуре:

```yaml
---
title: Jetix as <Part-name> — FPF-Described
date: 2026-05-17
type: jetix-fpf-describe
status: brigadier-structured (R1 surface-only)
prose_authored_by: ruslan-via-voice-dictation+brigadier-structured
audience: L1 (Anatoly + Tseren + MIM) + future Jetix-partners + Ruslan
parents: [list]
F: F3
G: jetix-fpf-describe-<part>
R: refuted_if_<falsifiable_criterion>
cells_dispatched: [eng-integrator, phil-critic, eng-critic, +optional 4th]
dissents_preserved: [count + summary]
mandatory_disclosures: [EP-5, EP-2, LIVE-FLAG if applicable]
language: russian + english (FPF primitives)
---

# Jetix as <Part-name> — FPF-Described

> EP-5 disclosure
> 10-15 min read

## §0 TL;DR (≤200 слов)
## §1 Verbatim source anchors (text_NNN / audio_NNN / doc:line)
## §2 FPF mapping (primitives + bounded contexts + claims+FGR)
## §3 Plain English narrative (L1-friendly)
## §4 FPF formal version
## §5 Mermaid diagram (cool blues + #1a202c contrast)
## §6 Connections / cross-refs (H1-H8 + Phase 0 objects + Foundation Parts)
## §7 Open questions for Ruslan (R1 surface)
## §8 R1 reaffirmation + dissents preserved (AP-6)
```

### §2.2 Per-doc FPF primitive plan

| Doc | Primary FPF primitives | Anchor Phase-0 objects | Cells (min 3, max 4) |
|---|---|---|---|
| 01 self-os | U.System (A.1) + A.4 Temporal Duality + Foundation Parts 1/5/8/9 cluster + P-1..P-10 Self-OS | O-01 (substrate), O-07 (Foundation) | eng-integrator + phil-critic + eng-critic + **sys-integrator** (4th: architecture) |
| 02 methodology | U.MethodDescription (A.3.2) + U.Method (A.3.1) + U.WorkPlan (A.15.2) + B.5.1 Explore | O-05 (methodology) | eng-integrator + phil-critic + eng-critic |
| 03 virtual-tribe | U.Role (A.2) + U.Capability + U.Commitment (A.2.8) + U.SpeechAct (A.2.9) + U.RoleAssignment (A.2.1) + Γ_work (B.1.6) + E.5 Guard-Rails | O-13 (Clan/People-NS), text_004 thesis | eng-integrator + phil-critic + eng-critic |
| 04 corporation | U.PromiseContent (A.2.3) + U.RoleAssignment (A.2.1 — 3 tiers) + B.2 Meta-Holon Transition + E.17 MVPK | O-02 (corp concept), Doc 1B | eng-integrator + phil-critic + eng-critic + **mgmt-integrator** (4th: org context) |
| 05 platform | U.System (A.1 supersystem) + A.1.1 BoundedContext + A.3.1 Method hosting + E.17 MVPK | O-14 (meta-workshop), Workshop concept | eng-integrator + phil-critic + eng-critic + **sys-integrator** (4th: architecture) |
| 06 internet-layer | A.2.8 Commitment + A.2.9 SpeechAct + A.2.1 RoleAssignment + A.10 Evidence Graph + B.3 F-G-R + E.5 Guard-Rails + E.17 MVPK | O-21 candidate (Trust Infra), H8 LOCKED, text_002 | eng-integrator + phil-critic + eng-critic |
| 07 overview | synthesis of above | all 14 Phase-0 objects audit table | eng-integrator + phil-critic + sys-integrator (architecture synthesis) |

### §2.3 Verification chain (per artefact — minimum 3 cells per Ruslan voice)

Per Ruslan voice «несколько FPF-натренированных агентов задроченных по FPF»:

1. **eng × integrator** drafts FPF formal section + primary structure
   → `swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-{slug}-eng-integrator.md`
2. **phil × critic** reviews epistemic integrity + EP-2 use-mention + EP-5 disclosure + R1 attribution
   → `swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-{slug}-phil-critic.md`
3. **eng × critic** verifies FPF primitive selection vs `raw/external/ailev-FPF/FPF-Spec.md`
   → `swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-{slug}-eng-critic.md`
4. For docs 01/04/05: 4th cell (**sys × integrator** OR **mgmt × integrator**)
5. Brigadier integrates с **AP-6 dissent preservation** (when cells disagree, preserve F/ClaimScope/R triple — never average)
6. **§5.5.5 provenance gate** (6 checks: provenance present, inline citations, edges consistent, tier coherence, foundation conditions, non-contradicting H1-H8)
7. **R1 + EP-5 + EP-2 audit** (strategic prose attribution; F8 disambiguation; mention-vs-use)
8. **Mermaid validity check** (cool blues palette + `color:#1a202c` contrast per memory rule)
9. Canonical write → `vision/jetix-fpf-describe/{slug}.md`
10. Mermaid diagram write → `vision/jetix-fpf-describe/diagrams/{NN-slug}.md`
11. `git commit -m "[vision][fpf-describe] {NN} {slug} — {cells} verified"`

### §2.4 Dispatch mechanics

Per `.claude/agents/brigadier.md` §4: Task tool с `subagent_type=<expert>-expert`, first line of prompt = `mode: <name>`. Parallel dispatch когда cells independent (после eng-integrator draft → phil-critic + eng-critic в parallel на том же draft). Cells write только в `swarm/wiki/drafts/`; brigadier promotes в canonical.

[src: .claude/agents/brigadier.md §4.1, §4.2, §5.5]

---

## §3 Logical reading order (already specified §1.1)

L1 reader path: 00 (index 2 min) → 01 → 02 → 03 → 04 → 05 → 06 → 07. Total ~90 min (10-15 min per content doc).

Alternative entry для time-constrained L1: 00 → 07 overview (entry + synthesis) → drill into specific part as needed. Documented in 00-MASTER-INDEX §quick-paths.

---

## §4 End-to-end coverage check

| Requirement | Doc location |
|---|---|
| All Phase 0 14 objects mapped to ≥1 doc | Audit table в 07 §6 + 00 §map |
| All H1-H8 Octagon insights cross-referenced | Per-doc §6 |
| text_004 distributed (5 placements) | Doc 03 primary + 02/06/07 refs + H8 extends_via + Master Vision 1-line |
| L1 reader passes 90 min budget | 00-MASTER-INDEX simulation |
| Cross-references resolved (no dangling) | 07 audit + §5.5.5 gate per doc |
| Vapor / aspirational flagged | Per-doc §0 status + §2 FPF mapping |
| EP-5 disclosed in every doc | Template top |
| R1 attribution explicit | Frontmatter `prose_authored_by:` |

---

## §5 text_004 distribution map (Brigadier autonomous decision per Ruslan ack 23:30)

[src: prompts/...-2026-05-17.md §0 ack «можешь её разбить самостоятельно»; raw/voice-memos-2026-05-17-batch/text_004@17-05-2026_23-30.md]

| Doc / location | text_004 slice | Treatment |
|---|---|---|
| **03 (PRIMARY HOME)** | Full thesis: humans-as-info-processing instruments + role-based mutual instrumentation + virtual tribe outcome + ethical safeguards (R12) | Authored as core narrative; `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured`; verbatim quotes preserved in §1 source anchors |
| 02 (cross-ref) | FPF roles as mutual-instrumentation enabling primitives (U.Role × U.Capability × U.Commitment) | Inline reference + 1 paragraph + cross-link to doc 03 |
| 06 (cross-ref) | Role-based trust attestation = trust infrastructure surface | 1 paragraph cross-reference; do not duplicate primitive cluster |
| 07 (synthesis) | "Virtual tribe = emergent property of platform + methodology + trust infra" — 1 paragraph | Synthesis only |
| `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` H8 | `extends_via:` comment block (R2 — no overwrite) — pointer to doc 03 | Append-only frontmatter `extends_via:` field added — minimal touch |
| `vision/00-MASTER-VISION-PLAN-2026-05-17.md` | Reference link in §4 (no rewrite) | Single line cross-ref appended if §4 supports (else skip) |

**Open question (surface, не decide):** Is text_004 a separate H9 Strategic Insight candidate, or H8 extension only? Defer to Ruslan ack. Surface in §7 + SUMMARY-FOR-RUSLAN. Default посylка — defer to Ruslan via SUMMARY; do NOT auto-promote H9 (R1 violation otherwise).

---

## §6 Cross-cell verification protocol

### §6.1 AP-6 dissent preservation

When ≥2 cells contradict, brigadier NEVER averages. Preserves dissent с (F, ClaimScope, R) triple in canonical doc §8.

Format precedent — `decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md` AP-6 example: 3 dissents preserved (Eng vs Phil on cluster vs single-primitive; Phil affect-mode flag; Mgmt 90-day refutation horizon).

### §6.2 §5.5.5 provenance gate (6 checks)

Per brigadier.md §5.5.5 before each canonical write:
1. Provenance present (≥1 `[src:...]` per claim)
2. Inline citations consistent with `parents:` frontmatter
3. Edges (cross-refs) consistent (no broken links)
4. Tier coherence (F-G-R within Phase 0 framing)
5. Foundation conditions (no Foundation Parts violation R2)
6. Non-contradicting H1-H8 LOCKED Strategic Insights

### §6.3 EP-5 + EP-2 + R1 audit (post-§5.5.5)

- EP-5: «Jetix F8 ≠ FPF B.3 F8» disclosed in §0 of each doc
- EP-2: use-mention discipline (vision claims = mention of artefact, not operational claim)
- R1: `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured` in every doc; no agent-pending strategic prose

### §6.4 Mermaid validity

- Cool blues palette per Variant A
- `color:#1a202c` contrast в classDef (per memory rule — Mermaid text contrast)
- Validate render before commit

---

## §7 Open questions для Ruslan (surface, не decide)

1. **8 docs vs more?** Plan locks at 8. If Phase 2 surfaces strong case for 9th (e.g., «Jetix as R12 Anti-Extraction Governance Layer» как standalone), brigadier surfaces в execution log, defers Ruslan ack. Default: stay at 8.

2. **text_004 = H9 Strategic Insight candidate vs H8 extension?** Plan defers Ruslan. Surface в SUMMARY-FOR-RUSLAN.

3. **Master Vision §4 rewrite vs cross-ref?** Plan locks: 1-line cross-ref only (R2 / append-only respect).

4. **Workshop A.1.1 BoundedContext formalization** (OQ-4 from Phase 0) — surface в doc 05.

5. **OQ-1 from Phase 0** (primary referent for «Jetix» — O-01 / O-04 / O-03 / O-02?) — surface в doc 07 overview.

6. **EP-5 future resolution** — Jetix F8 vs FPF B.3 F8 semantic drift; resolution pending external FPF community review.

---

## §8 Estimated runtime + cost (Phase 2)

- Phase 1 commit: 15-20 min (plan write + git commit)
- Phase 2 execution: 2.5-3.5h autonomous
  - 8 docs × ~3 cells avg = 24-32 Task dispatches
  - Per doc: ~20-25 min (cells parallel + integration + write + commit)
  - Reports + audit + push: ~30 min
- Cost estimate <€3 (text generation only; built-in models; no Whisper / external API)
- Daily cap €10; halt+ask at €50 (not anticipated)

[src: prompts/...-2026-05-17.md §4]

---

## §9 R1 reaffirmation + АВТОНОМНЫЙ ACK

**R1:** Ruslan = sole strategist. Brigadier surfaces, decomposes, organizes verification chain. Strategic prose (Phase-2 docs) `prose_authored_by: ruslan-via-voice-dictation+brigadier-structured`. No agent-pending strategic prose.

**Decomposition authority:** Brigadier organizing structure (8 docs / reading order / cell allocation) — это organizational not strategic. Ruslan ack 23:30 explicit «можешь её [text_004] разбить самостоятельно» + autonomous ack in prompt §1.5 «Действуй автономно. Plan-mode → Ruslan-voiced criteria → execute. НЕ останавливайся на ack между Phase 1 и Phase 2».

→ Phase 2 launches automatically after Phase 1 commit.

**Dissents preserved (Phase 1 plan-level):** None at plan stage; cells будут surface dissents в Phase 2 per-doc.

---

## §10 Phase 1 deliverable status

- [x] Decomposition: 8 docs locked (§1)
- [x] Per-doc FPF primitive plan (§2.2)
- [x] Verification chain protocol (§2.3 + §6)
- [x] Reading order (§1.1)
- [x] End-to-end coverage check (§4)
- [x] text_004 distribution map (§5)
- [x] Cross-cell verification protocol (§6)
- [x] Open questions surfaced (§7)
- [x] Runtime + cost (§8)
- [x] R1 reaffirmation (§9)

→ **Phase 1 commit:** `[plan][L0-fpf-describe] Phase 1 planning — decomposition (8 docs) + verification protocol (3+ cells per artefact) + text_004 distribution map`

→ **АВТОНОМНЫЙ ACK §1.5 fires** → Phase 2 swarm execute launches without further ack.

---

## Appendix A — Cell brief template (for Phase 2 dispatch)

```
mode: <critic|optimizer|integrator|scalability>

Brief:
- task_id: task-fpf-describe-jetix-2026-05-17-{slug}-{cell}
- artefact_under_consideration: <upstream draft path, if review>
- inputs (paths only, no inline content):
  - vision/jetix-fpf-describe-PLAN-2026-05-17.md (this plan)
  - prompts/fpf-describe-jetix-system-plan-then-execute-2026-05-17.md
  - raw/voice-memos-2026-05-17-batch/text_004@17-05-2026_23-30.md
  - vision/00-MASTER-VISION-PLAN-2026-05-17.md
  - decisions/STRATEGIC-INSIGHT-JETIX-TRUST-INFRASTRUCTURE-2026-05-17.md
  - reports/phase-0-fpf-scope/00-JETIX-FPF-MASTER-2026-05-17.md
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - decisions/JETIX-CORPORATION-2026-05-05.md (Doc 1B)
  - decisions/BASE-MANAGEMENT-SYSTEM-2026-05-04.md (Doc 1A)
  - decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
  - decisions/SELF-MANAGEMENT-SYSTEM-SPEC-v0-2026-05-16.md
  - raw/external/ailev-FPF/FPF-Spec.md (vendored, primitive reference)
- acceptance_predicate: <Hamel-binary statement for this cell's deliverable>
- ap_budget: <int turns; typical 3-5>
- expected_return_path: swarm/wiki/drafts/task-fpf-describe-jetix-2026-05-17-{slug}-{cell}.md
- mandatory_disclosures: EP-5 (Jetix F8 ≠ FPF B.3 F8); EP-2 (mention not use); R1 (prose_authored_by)
- constitutional posture: R1 + R2 + R6 + R11 + R12; append-only; AP-6 dissent preservation
```

Per-doc cell deployments tracked в `reports/jetix-fpf-describe-2026-05-17/01-PHASE-2-EXECUTION-LOG.md`.

---

**END Phase 1 plan.** Autonomous ack §1.5 → Phase 2 launches.
