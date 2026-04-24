---
title: "ACK — LAYER-5 Product Directions Deep-Dive"
type: gate-ack
gate_parent: swarm/gates/AWAITING-APPROVAL-layer-5-product-deep-dive-2026-04-25.md
cycle_id: cyc-layer-5-product-deep-dive-2026-04-25
task_id: T-layer-5-product-deep-dive-2026-04-25
canonical_doc: decisions/LAYER-5-PRODUCT-DIRECTIONS-DEEP-DIVE.md
acked: true
acked_by: ruslan
acked_at: 2026-04-25T11:10:00Z
chosen:
  Q-01: A-with-override      # Path B Phase-A default + Path C enterprise override + Path A Phase-2 SMB
  Q-02: A                    # Defer to G3 MVP; empirical Phase-2 pull-forward trigger specified
  Q-03: A-with-clarification # Smart AI internal only; explicit A/B test params required in Phase 7 compound
  Q-04: A-with-validation    # Cohort-first G2→G3 with NPS >40 + margin >€3K/learner gates; self-serve G3→G4
  Q-05: A-with-retirement    # Preserve D23 optionality; explicit retirement clause for MiCA/Howey or $100M ARR
state: acked
---

# ACK — LAYER-5 Product Directions Deep-Dive

All 5 blocking questions ack'd per brigadier recommendations with Q-01/Q-03/Q-04/Q-05 clarifications. Brigadier proceeds to Phase 7 compound + Phase 8 archive.

---

## Q-01: Path A/B/C Phase-A default — ACK (Option A with override specificity)

**Chosen:** Brigadier recommendation — Path B default.

**Override specificity (Ruslan clarification 2026-04-25 11:10):**
- **Path B default Phase-A** per investor unit-econ floor (70.7% GM yr1)
- **Path C enterprise override** triggered at revenue tier **>€30K contract + explicit GDPR audit requirement**
- **Path A Phase-2 SMB optionality** — reserved for low-touch SMB segment, Phase-2 activation

**Downstream implications for Phase 3 strategic docs:**
- `directions/_active/ai-consulting-dach/strategy.md` sizes three-Path offer structure with Path B as default Phase-1 sales motion
- Path C enterprise script requires compliance-package add-on ($15K-$40K/mo placeholder per §3.3)
- Path A SMB launch deferred to Phase-2 — no Phase-1 effort

## Q-02: YouTube-analyzer activation — ACK (Option A as specified)

**Chosen:** Defer SaaS to G3 MVP.

**Empirical Phase-2 pull-forward trigger (confirmed):**
- First Phase-1 consulting client **explicit request** for YouTube-analysis
- AND **willing-to-pay ≥$2K one-shot**
- → Activates **Phase-2 manual reporting service** (NOT SaaS)
- SaaS build remains G3 gate (MVP at €200K→€1M)

**Downstream:** §3.6 direction preserved as-drafted; no strategic doc required Phase-1 (pre-manual-reporting-service trigger).

## Q-03: Smart AI D29 status — ACK (Option A with clarification)

**Chosen:** Smart AI remains internal label; NOT D29 lock.

**Clarification (Ruslan 2026-04-25 11:10):** Explicitly spec A/B test parameters NOW before G2 review. Parameters to include in Phase 7 compound entry:
1. **Materials scope** — which outreach materials get A/B tested (LinkedIn DMs / discovery email / landing page hero / pitch deck)
2. **ICP segments tested** — which archetypes (Startupper / Operator / Mittelstand / Блогер) — minimum 2 segments
3. **Response-rate delta threshold** — specific numeric delta (e.g., ≥25% relative uplift) triggering promote-vs-stay decision
4. **Sample size + duration** — minimum N per variant, minimum test window
5. **Confounding-variable controls** — hold everything-else constant

Brigadier Phase 7 compound will produce this spec as a testable `swarm/wiki/tests/smart-ai-ab-test-spec.md` entry.

## Q-04: Educational cohort-vs-selfserve — ACK (Option A with validation gates)

**Chosen:** Cohort-first G2→G3.

**Validation gates (Ruslan 2026-04-25 11:10):**
- **2-3 cohorts required** at G2→G3
- **NPS > 40** average across cohorts
- **Margin > €3K / learner** average
- BOTH metrics must be met before self-serve launch
- **Self-serve launch gated at G3→G4 minimum** (€1M-to-$100M transition)

**Downstream:** §3.7 Educational direction §8 evolution table updated to reflect explicit validation gates. Strategic doc (Phase 3) will operationalize NPS + margin tracking.

## Q-05: Tokens D23 Option B — ACK (Option A with retirement clause)

**Chosen:** Preserve D23 Option B optionality.

**Explicit retirement clause (Ruslan 2026-04-25 11:10):**

D23 Option B **deprecates formally** if EITHER condition fires:
- **Condition A:** Phase-3 legal review returns prohibitive MiCA/Howey risk-benefit ratio (per §3.8 regulatory surface; lawyer-attested via written memo)
- **Condition B:** **$100M ARR achieved** without specialist-compensation friction becoming operational blocker

**Deprecation mechanism:** `LOCKS-D23-DEPRECATION` task opened (separate cycle) that formally retires D23 Option B and updates 28 Locks → 27 Locks (or adds D-30+ Deprecation-D23 as successor).

Brigadier Phase 7 compound adds retirement-conditions entry to `agents/brigadier/strategies.md` so future cycles track trigger conditions.

---

## Ruslan ack signoff

All 5 decisions ack'd with clarifications. Brigadier proceeds to:
- **Phase 7 compound:** strategies entries + per-expert agent-improvements + emergent insights (incl. Q-03 A/B spec + Q-05 retirement clause tracking)
- **Phase 8 archive:** cycle-log + DRR entry + canonical doc `state: accepted` transition

*Ack issued by Ruslan 2026-04-25 11:10 CET.*
