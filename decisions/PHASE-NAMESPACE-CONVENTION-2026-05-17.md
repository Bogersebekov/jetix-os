---
title: Phase Namespace Convention LOCK — prefix discipline для 4 distinct phase vocabularies
date: 2026-05-17
type: convention-lock
status: LOCKED
authored_by: brigadier scribe per Ruslan ack §0.7 («можно делать сейчас»)
prose_authored_by: brigadier (convention; Ruslan ack accepts pattern)
ack_record:
  - date: 2026-05-17
    ack_type: explicit-ack-via-prompt
    ack_text: "Ruslan §0.7: «Можно делать сейчас — cleanup PH-01..08 collision (Workshop Phase 1/2 vs ACTION-PLAN Phase 1 vs CLAUDE.md Phase 1-4 vs ROY Phase A/B/C). ... add prefix convention в каждом upstream document.»"
    ack_source: prompts/phase-0-plus-ruslan-acks-2026-05-17.md §0.7
F: F5
G: phase-namespace-convention-lock
R: refuted_if_collision_persists_after_clarification_OR_documents_unaffected_use_bare_Phase_N_post_2026-05-18
parent_problem:
  - reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md PH-01..PH-08 (Pattern P-6 phase namespace collision)
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md OQ-MASTER-10
constitutional_posture: R1 surface (convention proposed; Ruslan ack); R2 Foundation Parts skip (require AWAITING-APPROVAL separately); append-only clarifications NOT replacements
language: russian + english
---

# Phase Namespace Convention LOCK — prefix discipline

> **Status.** LOCKED 2026-05-17 per Ruslan ack §0.7. Naming convention для resolution of PH-01..PH-08 collision flagged в Phase 0 kasha cleanup.
>
> **Scope.** 4 distinct phase vocabularies share «Phase 1/2/3» labels — L1 reader sees one label, four meanings. This LOCK introduces required prefix convention.
>
> **Append-only discipline.** Existing documents get clarification *added* (NOT replaced retroactively). Foundation Parts (R2 protected) skip; require separate AWAITING-APPROVAL packet to update sources[] frontmatter.

---

## §1 Problem statement

Per Phase 0 caña §2 PH-01..PH-08 (`reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md`):

> 4 distinct phase vocabularies sharing «Phase 1/2/3» labels:
> - Workshop Concept: Phase 1 «мастерская одного владельца» / Phase 2 «команда»
> - ACTION-PLAN: Phase 1 «commercial near-future (May 2026, $100K target)»
> - CLAUDE.md §Agent Roster: Phase 1/2/3/4 = agent deployment phases
> - Phase B summary: Phase A/B/C = swarm operational phases (FPF research)

L1 audience читает один label, four meanings. Cleanup blocking L1 outreach legibility per ST-01 voice batch ack.

---

## §2 Convention LOCK — prefix table

Going forward, **all references к Phase N must use prefix form:**

| Original vocabulary | Required prefix form | Scope |
|---|---|---|
| Workshop Concept «Phase N» | **`Workshop-Phase-N`** | мастерская maturity (1=solo / 2=team / 3=multi-instance) |
| ACTION-PLAN «Phase N» | **`Commercial-Phase-N`** | revenue milestone (1=$100K near-future / 2=$1M / 3=$10M+) |
| CLAUDE.md Agent Roster «Phase N» | **`Agent-Deploy-Phase-N`** | DEPRECATED-2026-05-17 (роль archived; см. T6); legacy artifact only |
| ROY swarm «Phase A/B/C» | **`Swarm-Phase-A/B/C`** | substrate operational maturity (A=Phase A bootstrap / B=materialisation / C=cooperation infrastructure) |
| Phase 0 FPF research | **`Phase-0-FPF-Scope`** | one-off scoping cycle 2026-05-17 (this batch); no Phase 1 continuation under this label |
| Phase 0+ (этот batch follow-up) | **`Phase-0-Plus`** | acks execution batch 2026-05-17 evening |

**Backward compatibility:** Existing documents с bare «Phase N» preserved per append-only. New docs / new sections / new commits MUST use prefix form.

---

## §3 Affected documents — clarifications added (append-only)

**In scope этого LOCK (T7 execution):**

| Document | Action |
|---|---|
| `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` | APPEND §N+1 «Naming clarification 2026-05-17» — references к Workshop Phase N now use `Workshop-Phase-N` prefix |
| `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` | APPEND clarification — «Phase 1» в этом document = `Commercial-Phase-1` per LOCK 2026-05-17 |
| `CLAUDE.md` ## Active ROY Swarm | Already updated T6 — no Phase reference for ROY; bare «Phase A+» в text replaced with `Swarm-Phase-A+` in next pass |
| `swarm/wiki/foundations/synthesis/foundation-master-overview-technical-2026-04-29.md` | NOT IN SCOPE — Foundation territory; requires AWAITING-APPROVAL packet separately (R2) |
| `reports/voice-pipeline-2026-05-17-batch/04-detailed-work-plan.md` | Already references «Phase C» / «Phase B» / «Phase D» — convention OK (Swarm-Phase-* aligned) |

**Foundation Parts SKIP** (per R2):
- `swarm/wiki/foundations/part-*/architecture.md` — Foundation namespace; future cleanup requires AWAITING-APPROVAL packet (not in scope этого LOCK)

---

## §4 Resolution markers for kasha PH-01..PH-08

Per `reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md`:

- **PH-01..PH-08 RESOLVED** by this LOCK + T10 kasha-cleanup-flags update entry
- Resolution method: convention LOCK established + 2 affected docs append clarification + Foundation Parts deferred к separate AWAITING-APPROVAL packet (R2 protected)
- Status enum: `RESOLVED-by-LOCK-2026-05-17` для PH-01..PH-08; Phase 0 kasha cleanup-flags marked accordingly в T10 update

---

## §5 Enforcement

- **Author discipline:** All new commits / docs / wiki entries use prefix form
- **Lint candidate:** Future `/lint --check-phase-namespace` rule (Phase B materialization) — flags bare «Phase N» appearance outside `_archived/` или append-only history sections
- **Documentation:** This LOCK = reference; CLAUDE.md cross-link added в next CLAUDE.md update cycle (NOT this batch)

---

## §6 Decision boundaries

- **Brigadier authored convention** — Ruslan ack via §0.7 explicit «можно делать сейчас» suffices per R1 (operational naming не strategic); НЕ requires Ruslan re-author prose
- **Foundation skipping** — R2 strict; separate AWAITING-APPROVAL packet required для Foundation Parts re-naming (out of scope этого LOCK)
- **Append-only preserved** — historic «Phase N» bare references kept (NOT rewritten); only new content uses prefix

---

## §7 Filing

| Where | Why |
|---|---|
| `decisions/PHASE-NAMESPACE-CONVENTION-2026-05-17.md` (this file) | LOCK record per Ruslan ack §0.7 |
| `decisions/JETIX-WORKSHOP-CONCEPT-2026-04-30.md` (append §clarification) | Workshop docs — convention applies |
| `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` (append §clarification) | Commercial docs — convention applies |
| `reports/phase-0-fpf-scope/04-kasha-cleanup-flags.md` (T10 update) | Mark PH-01..PH-08 RESOLVED |

---

*Brigadier scribe convention LOCK. §5.5.5 gate: prefix table ✓ / 4 affected docs identified ✓ / Foundation R2 skip noted ✓ / append-only discipline preserved ✓ / Ruslan ack §0.7 explicit ✓.*


## §APPEND-2026-05-19 — Hackathon-Phase namespace addition (RUSLAN-ACKED Option A)

**Ack:** Ruslan 2026-05-19 evening — packet `swarm/awaiting-approval/pillar-a-hackathon-mode-extension-2026-05-18.md` Option A acked.

### NEW namespace: `Hackathon-Phase-N`

Added to existing 4 phase vocabularies (Workshop-Phase / Commercial-Phase / Agent-Deploy-Phase / Swarm-Phase):

**Hackathon-Phase-T1** = day-rhythm online micro-hackathons (5-20 participants)
**Hackathon-Phase-T2** = weekend-rhythm online standard hackathons (20-100 participants)
**Hackathon-Phase-T3** = week-rhythm hybrid hackathons (50-200 participants)
**Hackathon-Phase-T4** = week-month-rhythm onsite Berlin Workshop hackathons (20-100 participants)
**Hackathon-Phase-T5** = quarter-year-rhythm offline major projects (100-500 participants)

### Usage convention

When referring к hackathon Tier event:
- ✓ «Hackathon-Phase-T1 (day-rhythm bloggers + sponsor)»
- ✓ «Hackathon-Phase-T4 (Berlin Workshop Grundstück week-month)»
- ✗ Bare «Phase 1 hackathon» (ambiguous with Commercial-Phase-1 / Workshop-Phase-1)

### Cross-refs

- `decisions/strategic/JETIX-AS-HACKATHON-PLATFORM-2026-05-18.md` (concept doc parent)
- `research/hackathon-platform-deep-2026-05-18/04-hackathon-mechanics-progression.md` (5-Tier spec)
- `reports/jetix-platform-v2-2026-05-19/04-hackathon-mechanics-progression.md` (Platform v2 hackathon Tier)

[src: swarm/awaiting-approval/pillar-a-hackathon-mode-extension-2026-05-18.md Option A + Platform v2 §3]

---

*§APPEND-2026-05-19 Ruslan ack Option A — Hackathon-Phase namespace addition. R1 + R2 Pillar A LOCK content preserved + R11 + EP-5 + append-only.*
