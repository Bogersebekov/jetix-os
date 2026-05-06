---
title: Deferred Docs INDEX — preserved-but-not-active navigation
date: 2026-05-06
type: index
status: active
parent_walkthrough: ../CANONICAL-WALKTHROUGH-2026-05-06.md
parent_cleanup_prompt: ../prompts/server-cc-canonical-cleanup-2026-05-06.md
authority: Ruslan walkthrough ack 110-item checklist (2026-05-06)
---

# Deferred Docs INDEX (2026-05-06)

> Документы которые помним но не используем активно. Не trash, не canonical.
> Возможна re-activation в Phase 2+.
>
> Каждый doc имеет frontmatter поля: `status: deferred-phase-2-plus` (или existing
> equivalent), `deferred_at: 2026-05-06`, `deferred_reason: ...`, `moved_by:
> canonical-cleanup-2026-05-06`.

---

## §1 Strategic Insights — deferred Phase-2+

> Pre-Phase-1 strategic exploration / not active focus / preserved для future
> activation после €200K validation gate.

| Doc | Original location | Trigger / context |
|-----|-------------------|-------------------|
| [STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25](STRATEGIC-INSIGHT-MA-DIRECTION-2026-04-25.md) | `decisions/` | M&A Advisory + ETA как future direction (Ruslan 25.04 directive) |
| [STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25](STRATEGIC-INSIGHT-ARBITRAGE-TRAFFIC-DIRECTION-2026-04-25.md) | `decisions/` | Arbitrage Traffic как future Phase-2+ direction (Ruslan 25.04 directive) |
| [STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24](STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md) | `decisions/` | Jetix as AI-era BIOS/Standard Moment (local-first, client-private KB architecture) |
| [STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26](STRATEGIC-INSIGHT-AI-PSY-LED-DESIGN-2026-04-26.md) | `decisions/` | AI Psy-Led Design Principle (D14 conflict requires Phase 2+ deferral) |

> **Note:** A 5th Strategic Insight `STRATEGIC-INSIGHT-TOP-LISTS-PARTNER-FACTORY-2026-04-26.md`
> was listed in the prompt §1.2 but was not present on `main` at execution time
> (anticipated per §8 obs O3). See [archive/missing-files-2026-05-06.md](../archive/missing-files-2026-05-06.md).

## §2 Active WIP — companion to FUNDAMENTAL

| Doc | Original location | State |
|-----|-------------------|-------|
| [JETIX-VISION-OF-SYSTEM-2026-04-27](JETIX-VISION-OF-SYSTEM-2026-04-27.md) | `decisions/` | Layer 2 RUSLAN-LAYER overlay над FUNDAMENTAL — §1 filled (35 use cases), §2-§10 pending; preserved for next iteration cycle |

---

## §3 Linked, NOT moved (Strategic Layer F2 promotion queue)

These remain in their original location — they are F2 mechanical scaffolds
participating в active Wave 1.4 promotion pipeline. Moving would break the
pipeline. Not canonical (per CLAUDE.md "not canonical" list), not deferred,
not archived.

- [decisions/strategic/lock-entries/](../decisions/strategic/lock-entries/) — D-01..D-29 lock entries (29 files)
- [decisions/strategic/strategic-insights/](../decisions/strategic/strategic-insights/) — 4 insight scaffolds
- [decisions/strategic/_templates/](../decisions/strategic/_templates/) — 7 templates (structural references for Pillar A architecture §I)

---

## Provenance

- Authority: Ruslan walkthrough ack via 110-item checklist
- Cleanup prompt: [../prompts/server-cc-canonical-cleanup-2026-05-06.md](../prompts/server-cc-canonical-cleanup-2026-05-06.md)
- Move discipline: `git mv` preserves history; frontmatter additions append fields without deleting existing
