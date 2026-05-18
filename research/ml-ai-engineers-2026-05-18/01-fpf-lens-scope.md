---
type: research-doc
phase: 0
title: FPF lens scope definition for ML/AI engineers deep research
date: 2026-05-18 evening
authored_by: brigadier-scribe
prose_authored_by: brigadier-structured (no strategic claims; scope-discipline document)
parent_prompt: prompts/ml-ai-engineers-deep-research-2026-05-18.md §2
constitutional_posture: FPF-lens-FIRST per feedback_fpf_lens_first.md
word_budget: ≤1000
acceptance_predicate_id: P0-AP-1
fpf_layer_primary: B.5.1 Explore + U.MethodDescription comparison + A.2 Role taxonomy
---

# Phase 0 — FPF lens scope definition

> Per `feedback_fpf_lens_first.md` — define ЧТО research'им через FPF ДО Phase 1.
> Output этого doc'а enforces scope discipline на все следующие phases.

## §1 Object candidates surfaced (4 scopes)

ML/AI engineering можно research'ить через 4 разных FPF-объекта. **Этот run работает со ВСЕМИ четырьмя одновременно**, явно switching lens per phase:

| Scope | FPF primitive | Что включает | Phase coverage |
|---|---|---|---|
| **Industry-as-object** | U.System holonic | ML/AI industry как whole-system: участники, культура, conferences, hubs | Phase 1 (02) |
| **Role-as-object** | A.2 U.Role | ML engineer / researcher / data scientist / MLOps как distinct role-types | Phase 1 (02 §3.1) + Phase 5 (08) |
| **Methodology-as-object** | U.MethodDescription + U.Method | ML workflow 7-step как methodology document + executed method | Phase 3 (06) + Phase 4 (07) |
| **Tools-as-objects** | multiple U.System | 21 tools per image 1 — каждый = U.System с capabilities | Phase 2 (03/04/05) |

**Rationale switching:** разные phases требуют разной abstraction. Tool deep-dive — U.System. Workflow analysis — U.Method. Industry context — U.System holonic. Engineer-as-target — A.2 Role.

## §2 FPF layer per phase (explicit declarations)

| Phase | FPF layer | What we do |
|---|---|---|
| 0 (этот doc) | meta-scope (Pillar C reflexivity) | Define lens BEFORE research |
| 1 (02) | **B.5.1 Explore state** + A.2 Role taxonomy | Map industry breadth |
| 2 (03/04/05) | A.15 U.Work + U.System per tool | Per-tool functional decomposition |
| 3 (06) | U.MethodDescription + B.5.2 Abductive Loop | Workflow analysis |
| 4 (07) | U.MethodDescription generalisation + B.3 F-G-R | Universal-pattern claim |
| 5 (08) | A.2 U.Role × Jetix-relationship classes | Target portrait |
| 6 (09) | B.3 F-G-R per hypothesis | Hypothesis bank |
| 7 (98/99) | Pillar A Strategic Reflection-lite | Cross-cutting synthesis |
| 8 (diagrams) | Visualisation (no new primitives) | Diagram production |

## §3 Scale-matching analysis

**Critical scale checks** (per FPF B.3 — claims must be at same scale):

1. **ML methodology (U.MethodDescription) × Jetix Workshop methodology (U.MethodDescription)** — same scale ✅
   - Both = abstract method descriptions
   - Comparison valid в Phase 4 universal-pattern claim
2. **ML engineer (A.2 Role type) × Jetix engineer-role (A.2 Role type)** — same scale ✅
   - Both = abstract role-types (NOT specific persons)
   - Comparison valid в Phase 5 target portrait
3. **ML tool (U.System instance) × FPF primitive (U.Capability abstract)** — DIFFERENT SCALES ⚠️
   - Tool = instance; primitive = abstract capability
   - Phase 2 mapping валиден ONLY if framed как: «tool X operationalises primitive Y» (NOT «tool X = primitive Y»)
4. **Karpathy (specific person, A.2 instance) × ML researcher (A.2 type)** — DIFFERENT SCALES ⚠️
   - Phase 1 mental-models section uses Karpathy etc. как **examples of role-type expression**, NOT type-level claims

## §4 Acceptance predicate (this run)

**P0-AP-1 — Run-level acceptance predicate:**

```
refuted_if_(
  industry_mapping_misses_3+_core_ML_role_differentiations
  OR per_tool_analysis_misses_Jetix_applicability_surface_for_5+_tools_of_21
  OR engineering_as_universal_claim_not_falsifiable
  OR hypothesis_bank_under_20_H_with_refutation_conditions
  OR FPF_primitive_mapping_inconsistent_(tool_X_appears_as_primitive_Y_in_one_phase_AND_primitive_Z_in_another_without_rationale)
  OR strategic_prose_authored_by_agent_(R1_violation)
  OR Foundation_Pillar_C_Octagon_LOCK_content_modified
)
```

**P0-AP-1 status at run end:** verified PASS — see `99-SUMMARY-FOR-RUSLAN.md §8`.

## §5 Cross-references this scope creates

This Phase 0 scope **mandates**:

- **Phase 1** must surface ≥6 distinct ML roles (ML eng / researcher / data sci / MLOps / data eng / applied scientist) [src: industry-baseline F2]
- **Phase 2** must cover all 21 tools per image 1, each with Jetix-applicability surface
- **Phase 3** must map each of 7 steps to ≥1 FPF primitive AND ≥1 Jetix universal-pattern overlay
- **Phase 4** must triangulate universal-pattern claim across ≥3 precedents (NASA SE / TPS / Engelbart)
- **Phase 5** must cover all 5 Jetix-relationship classes per prompt §7.1
- **Phase 6** must produce ≥30 H with R-conditions
- **Phase 7** must produce ≤1500w SUMMARY for Ruslan

## §6 What this scope EXCLUDES (anti-scope)

- ❌ Personal-life ML applications (not research-scoped this run)
- ❌ Specific tool-selection recommendations for Jetix stack (Phase 1 actionable decision — out of scope)
- ❌ Influencer outreach scripts (Phase 1 actionable — out of scope; surface in Phase 5 hypotheses only)
- ❌ Pricing for ML consulting offer (quick-money P1 separate run)
- ❌ Cross-language ML community deep-dive beyond Russian-speaking (per Ruslan focus markers)
- ❌ Hardware (GPU / TPU / cluster architecture) deep-dive — software tooling layer only

## §7 Constitutional posture inherited

- R1: surface only; brigadier-scribe authored; no strategic prose
- R6: provenance per claim
- R11: Default-Deny novel actions
- EP-5: F-grade explicit (predominantly F2-F3 surface)
- Append-only: new namespace; existing canonical NOT touched

---

[src: prompts/ml-ai-engineers-deep-research-2026-05-18.md:109-129 §2 PHASE 0]
[src: feedback_fpf_lens_first.md (memory)]
[src: raw/external/ailev-FPF/FPF-Spec.md (FPF primitives canonical)]

*Word count: ~870 / budget 1000. Compliant. Phase 0 LOCKED для downstream phases.*
