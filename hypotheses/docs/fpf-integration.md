---
title: FPF F-G-R integration in hypotheses substrate (Layer 5)
date: 2026-05-20
type: documentation
parent_layer: 5
sources:
  - raw/external/ailev-FPF/FPF-Spec.md (Part B.3, C.2.2, C.2.3, A.2.6)
  - hypotheses/_schema/hypothesis.schema.yaml
  - hypotheses/_schema/fgr-triple.yaml
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: hypotheses-fpf-integration-docs
R: low
---

# Layer 5 — FPF F-G-R Integration

> Layer 5 of 7. Каждая гипотеза в substrate carries FPF B.3 F-G-R triple
> как **mandatory frontmatter** — обеспечивает Foundation-compatible primitives
> для уровня доверия / scope / reliability.

## §1 What is F-G-R

Из FPF Spec Part B.3 — Trust & Assurance Calculus:

- **F (Formality)** — C.2.3 — F-scale F0..F9 (мы используем F2..F8 subset). Степень формальности утверждения: от surface observation до constitutional invariant.
- **G (ClaimScope / Group)** — A.2.6 USM — scope в котором утверждение применимо. Set-valued; точно определяет boundary of generalization.
- **R (Reliability)** — C.2.2 — warrant / evidence-bound degree of trust. Propagates через transport / composition / aggregation; weakest-link arithmetic.

**Together (F, G, R) = "trust triple" per claim.** Hypothesis = claim-in-formation; F-G-R растёт по mere lifecycle activity.

## §2 Mapping hypothesis lifecycle → F-G-R progression

| Lifecycle stage | Typical F | Typical R | Notes |
|---|---|---|---|
| Newly surfaced (status=active, just `/hypothesis-add`) | F2 | low | Surface observation; pre-test |
| Conceptual with reasoning (active, with method documented) | F3 | low | Argument-based; not yet empirically supported |
| Testing in progress (status=testing) | F3 | low → medium | R rises as evidence accumulates |
| Preliminary confirmed (status=confirmed, single context) | F4 | medium | First successful test corroboration |
| Cross-context confirmed (status=confirmed, replicated) | F4 → F5 | high | Ready для promotion candidate |
| Foundation-promoted (post-promote к wiki/foundation) | F5 | high | LOCKED primitive; cross-Foundation reusable |
| Constitutional (Pillar C Tier-2 promotion) | F8 | high | Reserved для constitutional invariants; rare |

**F never downgrades implicitly.** R can shift both directions (corroboration ↑ / counter-evidence ↓).

## §3 Group scope (G) — common values

`fpf_G:` field accepts free-form string. Common values для Jetix substrate:

| G value | Domain |
|---|---|
| `jetix-foundation` | Foundation Parts 1-11 substrate |
| `jetix-platform-v2` | Platform v2 32-resource framework |
| `outreach-pipeline` | Outreach process |
| `personal-dev` | Ruslan personal development |
| `intellect-stack` | Левенчук Intellect-stack |
| `founding-circle` | Founding circle org form |
| `clan-substrate` | Clan / Network State substrate |
| `ai-substrate` | AI agent infrastructure |
| `method-systems-thinking` | meta-method scope |
| `fpf-extension` | FPF spec extensions |
| `<custom>` | Free-form; recommend documenting в `_schema/fgr-triple.yaml` common_values если используется repeatedly |

## §4 Reliability progression (R)

Per FPF C.2.2 R is **warrant-bound** + **weakest-link**:

- `low` — single observation supports; could easily be wrong; не corroborated
- `medium` — multi-observation / corroborated within scope; could still be wrong but evidence mounting
- `high` — replicated / cross-context corroborated / quasi-canonical

**Transport rule (per FPF Bridge-only reuse):** if H-NNN with R=high gets reused в new scope G' ≠ G, R **does NOT auto-carry**. Must re-test or attach Bridge claim per FPF A.6.

## §5 Mandatory validation (Layer 5 invariant)

`hypotheses/_schema/hypothesis.schema.yaml` requires:
- `fpf_F`: required, enum [F2,F3,F4,F5,F6,F8]
- `fpf_G`: required, string
- `fpf_R`: required, enum [low,medium,high]

`/hypothesis-add` halts если any of three missing.
`/hypothesis-update` allows monotonic F upgrade (downgrade requires `--allow-downgrade`).

## §6 F-grade thresholds — when to upgrade

### F2 → F3
- Hypothesis has documented reasoning chain (not just observation)
- `test_method` field filled with concrete steps
- Action: `/hypothesis-update H-NNN --fpf-F F3 --reason "method documented"`

### F3 → F4
- At least one successful test corroborating
- `outcome` field reflects first confirmation
- Action: paired with `/hypothesis-close --outcome confirmed` OR mid-test upgrade

### F4 → F5
- Replicated across multiple contexts OR single high-stakes context with strong evidence
- Cross-link к relevant wiki concept OR foundation Part
- Action: `/hypothesis-update H-NNN --fpf-F F5 --fpf-R high --reason "replicated cross-context"`
- **Promotion candidate alert:** `/hypothesis-close` prints suggestion: «Consider /ingest к wiki/concepts/ OR Foundation update via AWAITING-APPROVAL packet»

### F5 → F6
- Inter-Foundation consistent (compatible с multiple Foundation Parts)
- Used by another Foundation Part
- Action: requires AWAITING-APPROVAL packet (R2 Foundation-level constraint)

### F6 → F8
- Constitutional level
- Reserved для Pillar C Tier-2 candidate rules
- Action: requires Ruslan ack + Pillar C Tier-2 packet (R12 + Default-Deny constitutional)

## §7 Cross-schema consistency

`shared/schemas/` Foundation contracts:
- `briefing.schema.json` — uses F-G-R imports (если present); compatible
- `task.schema.json`, `decisions-db.json` — могут extend F-G-R per artefact
- `strategic-direction-doc.json` — Pillar A strategic docs F5 LOCKED carry F-G-R

**Consistency rule:** если same claim appears in hypothesis AND в wiki concept AND в Foundation Part, F-grade в wiki/foundation may exceed F-grade в hypothesis (post-promotion). Hypothesis F-grade ≠ canonical reference; F-grade в wiki/foundation = canonical.

## §8 Example F-G-R per sample hypothesis (Phase 8 reference)

| Sample | fpf_F | fpf_G | fpf_R | Rationale |
|---|---|---|---|---|
| H-001 meta-method cross-domain | F3 | jetix-foundation | medium | Conceptual with reasoning; partial substrate support via wiki §APPEND batch-8 |
| H-002 partnership-frame vs cheatcode | F2 | outreach-pipeline | low | Newly surfaced; pre-test |
| H-003 3-tier funnel 3-6mo optimal | F2 | jetix-business-model | low | Newly surfaced |
| H-004 imagination as intellect component | F2 | intellect-stack | low | Surface observation from O-101 Tier B |
| H-005 method-as-1st-class-object recursive | F3 | jetix-foundation | medium | Conceptual with Левенчук cross-cite + audio_703 + batch-8 substrate |

## §9 Anti-patterns

- ❌ **F-grade inflation** — assigning F5 без evidence (silently fails Foundation invariant)
- ❌ **R-grade based on author confidence** — R is evidence-bound, NOT belief-bound
- ❌ **G left vague** — «all» / «universal» violates A.2.6 USM; must be bounded
- ❌ **F-grade transport без Bridge** — copying H-NNN F=F5 to new scope without re-test or Bridge claim

## §10 Cross-refs

- **FPF spec:** `raw/external/ailev-FPF/FPF-Spec.md` Part B.3 (Trust & Assurance Calculus) + B.3.1-B.3.5 + C.2.2 + C.2.3 + A.2.6
- **Hypothesis schema:** `hypotheses/_schema/hypothesis.schema.yaml` (mandatory triple)
- **F-G-R reference:** `hypotheses/_schema/fgr-triple.yaml`
- **Foundation Part 5:** Compound learning (learning_extracted feeds F-promotion)
- **Pillar C §4.1 rule 11:** Default-Deny — F-G-R missing triggers halt
- **Memory:** `feedback_fpf_lens_first.md` — Phase 0 mandatory
