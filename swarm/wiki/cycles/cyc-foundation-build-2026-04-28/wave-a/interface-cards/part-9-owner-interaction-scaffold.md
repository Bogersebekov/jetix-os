---
title: "Interface Card — Part 9: Owner Interaction Scaffold"
part: 9
slug: owner-interaction-scaffold
phase: A-2
cycle: cyc-foundation-build-2026-04-28
expert: engineering-expert
mode: integrator
date: 2026-04-27
originating_expert: mgmt-expert
critic_flags_applied:
  - "FLAG-MAJOR resolved: IP-2 bounded context corrected from 'owner cognitive workspace' to explicit single-owner professional knowledge-worker system declaration with F.9 Bridge requirement; per A-1-critic-gate.md §6 item 2"
bounded_context_declaration: "single-owner professional knowledge-worker system; bridge required (F.9, FPF §5.2 U.BoundedContext) for multi-owner or team instantiations"
F: F4
ClaimScope: "Holds for single-owner professional knowledge-worker system; NOT a universal claim; solo-founder context is explicit bounded context, not a default assumption"
R: "Refuted if any Foundation artefact for Part 9 drops the bounded-context declaration and treats solo-founder interaction patterns as universal; accepted when Wave C interface card explicitly includes F.9 Bridge note"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
---

# Interface Card — Part 9: Owner Interaction Scaffold

**Scope sentence.** The structured interface between the system and its human
owner — daily working page creation, draft-to-canonical promotion workflow,
weekly and monthly review rituals, attention-budget cap enforcement, and the
3-tier approval SLA taxonomy — ensuring the owner's interaction load is bounded
and their engagement with the system is structured.

**U.System.** Manages state transitions in the owner's daily workflow (draft →
pending-review → promoted / archived); enforces attention cap; produces committed
daily, weekly, and monthly artefacts.

**Bounded context (IP-2, explicit):** single-owner professional knowledge-worker
system. In this context, the owner's weekly review IS the strategic management
touchpoint (UC-A.1-A.2). F.9 Bridge required for multi-owner or team
instantiations (e.g., a team-based system where multiple people hold strategic
authority). The solo-founder assumption is a bounded-context declaration, not a
universal claim. [A-1-critic-gate.md §6 item 2; FPF §5.2 IP-2; A.1.1 U.BoundedContext]

---

## A. Inputs

- `daily-log/<YYYY-MM-DD>.md` :: daily-page-create event (owner or `/plan-day` skill)
- Draft artefacts from all other parts (agent drafts, project stage-gate proposals, KB synthesis outputs) :: draft-ready events
- Health dashboard from Part 8 :: weekly-health-ready event (feeds weekly review context)
- Project status from Part 7 :: project-status-update events
- Alert recommendations from Part 8 :: recommendation-ready events
- Owner attention budget state from `shared/state/kanban.json` :: cap-enforcement input
- `FUNDAMENTAL §4.2-§4.3` 3-tier approval SLA (L1/L2/L3) :: constitutional gate taxonomy

## B. Outputs

- `daily-log/<YYYY-MM-DD>.md` :: committed daily working page (plan + draft area + EOD record)
- Weekly review artefact `decisions/weekly/<YYYY-WNN>-review.md` :: structured review output (draft disposition + strategic alignment check)
- Monthly reflection artefact `decisions/monthly/<YYYY-MM>-reflection.md` :: strategic document synthesis + compound-learning notes
- Promoted canonical artefacts → forwarded to Part 6 (Governance) for gate processing :: promotion-request events
- Archived draft records (preserved but excluded from active query results) → committed via Part 1 :: archive events
- 3-tier SLA gate classification per pending item (L1 / L2 / L3) → consumed by Part 6 :: gate-classification signal

## C. Side-effects

- git commit `[daily] plan: <YYYY-MM-DD>` at daily-page creation; `[daily] eod: <YYYY-MM-DD>` at EOD per D25
- git commit `[review] weekly: <YYYY-WNN>` at weekly review artefact creation
- Append to `swarm/wiki/log.md` on each committed review artefact (append-only)
- Update `shared/state/kanban.json` WIP count on draft intake and promotion/archive (attention-cap enforcement)
- Trigger Part 6 AWAITING-APPROVAL packet for any item classified as L1 or L2 gate tier
- Write to `shared/state/priorities.json` on weekly review (updated priority stack for the coming week)

## D. Dependencies (typed per FPF A.14)

- `creates` **Part 1** — all interaction artefacts (daily logs, review files, reflection files) are committed files [FPF IP-3; D25]
- `PhaseOf` **Part 6** — promotion workflow forwards artefacts into Part 6's gate mechanism; Part 9 is the pre-gate staging phase for human-initiated promotions [A-1-critic-gate.md §2 Part 9 A.14]
- `methodologically-uses` **Part 5** — monthly reflection is the S4 environment-scanning input to the Compound Learning engine; owner reflection notes feed strategies.md update proposals [FPF IP-7; systems-thinking-cybernetics.md §4 Principle 3 VSM S4]
- `operates-in` health monitoring context of **Part 8** — owner reflection data (attention-budget utilisation, daily log completion rate) are health signals that Part 8 monitors [A-1-critic-gate.md §2 Part 9 A.14]

## E. Boundary (FPF A.6.B L/A/D/E)

**Laws (invariants that MUST hold):**
- IP-7 writing-as-thinking asymmetry: owner authors strategic and reflective content; agents contribute structured extractions only (agents MAY draft the daily structure, but the owner holds authorship authority over strategic content per FPF §5.7 IP-7; FUNDAMENTAL §6.2)
- Attention-budget cap is a hard Law — no agent or automation may add items to the owner's active queue beyond the declared WIP limit without explicit owner ack [FUNDAMENTAL §3.2.6; mgmt-expert.md §3 WIP limit]
- 3-tier approval SLA (L1/L2/L3) classification is mandatory for every item entering the promotion workflow; unclassified items default to L2 (conservative, not aggressive) [FUNDAMENTAL §4.2; mgmt-expert.md §3]
- F.9 Bridge documentation: any deployment in a multi-owner or team context MUST produce a bridge specification before Part 9 functions are exposed to additional human owners [FPF §5.2 U.BoundedContext]

**Admissibility (acceptance criteria for inputs):**
- Daily working page accepted only if it contains: date header, morning plan section, draft area section; minimal structure enforced
- Draft artefacts from other parts accepted only if they carry source provenance (`sources:` frontmatter field, inline `[src:...]` citations) per Part 6 provenance discipline
- Promotion requests accepted only if the item has a 3-tier SLA classification declared

**Deontics (obligations toward consumers):**
- MUST produce a weekly review artefact within 7 days of the prior one; absence triggers a health alert to Part 8 (weekly cadence SLI per FUNDAMENTAL §2.5)
- MUST forward all L1-classified items to Part 6 gate WITHIN the same session (L1 = external commitment or Lock modification — no batching permitted per FUNDAMENTAL §4.2 L1 SLA: immediate)
- MUST NOT auto-promote any item to canonical without owner ack (FUNDAMENTAL §6.2 founder-agency preservation; §4.5 anti-patterns)
- MUST preserve the full text of archived drafts (archive ≠ delete; searchable with provenance per FUNDAMENTAL §1 UC-J.2)

**Effects (measurable outcomes):**
- Daily log creation rate: target ≥5 per working week (daily ops health indicator, FUNDAMENTAL §3.5)
- Weekly review completion rate: target 1 per calendar week (FUNDAMENTAL §2.5 health checkup cadence)
- Draft clearance rate: target ≤20 open drafts at any weekly review point (WIP limit enforcement)
- L1 SLA compliance: 100% of L1 items gated within same-session (FUNDAMENTAL §4.2)

## F. Anti-scope

- Part 9 does NOT make strategic decisions — it scaffolds the owner's strategic engagement; the owner decides (FUNDAMENTAL §6.1, §6.2)
- Part 9 does NOT own the gate mechanism — Part 6 (Governance) owns AWAITING-APPROVAL gate logic; Part 9 pre-stages items and classifies their SLA tier
- Part 9 does NOT substitute for founder agency — it is the primary expression of the system's obligation to SCAFFOLD founder agency (PP-7 per A-1-critic-gate.md §2 Part 9)
- Part 9 does NOT define strategic document content (UC-A.2 strategic document creation assistance is triggered from Part 9's weekly review but authored by the owner per IP-7; agent contribution = structured extraction, not authorship)
- Part 9 does NOT cover CRM or external relationship management (Part 10)
- Part 9 does NOT run project execution — it surfaces project status for owner review; project execution lives in Part 7
- Part 9 does NOT apply universally to multi-owner systems without an F.9 Bridge specification (IP-2 bounded context; solo-owner assumption is explicit, not a silent default) [A-1-critic-gate.md §6 item 2]
- Part 9 is NOT a Torres CDH (Continuous Discovery Habits) implementation — CDH is a specific methodology that belongs in RUSLAN-LAYER methodology library; Foundation encodes only the generic "opportunity intake" sub-function within the weekly review (OQ-MERGED-4 resolution) [A-1-critic-gate.md §4 OQ-MERGED-4]

## G. F-G-R Tagging

| Artefact emitted | F | G (ClaimScope) | R |
|---|---|---|---|
| Daily working page | F2 | That calendar day only | low — draft, mixes planning and exploration |
| Weekly review artefact | F4 | Current week; single-owner system context | medium — owner-reviewed, covers all active parts |
| Monthly reflection artefact | F5 | Trailing month; strategic scope | high — owner-authored strategic reflection, compound-learning input |
| Promoted canonical artefact | F5 (post-gate) | Artefact's own claim scope | high — Part 6 gate passed, human ack recorded |
| L1/L2/L3 gate classification | F4 | Single item, single session | medium — heuristic classification, correctible by owner |

## H. Originating Expert + Critic Flags

**Originating expert.** Mgmt-expert (Part 2: Operational Rhythm Layer). UC-A.1-A.3 Strategic Management gap absorbed here — no expert proposed a standalone strategic management part; the weekly/monthly reviews ARE the strategic touchpoints in a single-owner system (this is a bounded-context declaration, not a universal claim). [candidate-parts-merged.md §2 Part 9; mgmt-expert.md §2 Part 2]

**Critic flags applied:**
- FLAG-MAJOR (IP-2 bounded context): "owner's cognitive workspace" framing replaced with explicit single-owner professional knowledge-worker bounded-context declaration + F.9 Bridge requirement. [A-1-critic-gate.md §6 item 2; FPF §5.2 IP-2]

**UC-A.1-A.3 strategic touchpoints note.** In a single-owner system architecture, the weekly review is the structural home of UC-A.1 (strategic management touchpoints) and UC-A.2 (strategic document creation). UC-A.3 (strategic alignment enforcement) is owned by Part 6 (Governance); Part 9 provides the interaction surface through which the owner reviews and enforces alignment during the weekly cadence. [A-1-critic-gate.md §5 UC-A review]

**Wave C bullets (preview).**
- Define daily-log artefact schema (YAML frontmatter + required sections: plan, drafts, EOD) — S effort; engineering-expert integrator + mgmt-expert critic
- Define weekly review artefact schema with draft-disposition table and strategic alignment check sections — M effort; mgmt-expert integrator
- Canonicalise 3-tier SLA taxonomy (L1/L2/L3 definitions + examples) as Foundation artefact — S effort; philosophy-expert critic (agency-CHR compliance check)
- Wire attention-budget cap enforcement to `shared/state/kanban.json` — S effort; engineering-expert integrator
- Document F.9 Bridge specification stub for multi-owner instantiation — S effort; philosophy-expert integrator
