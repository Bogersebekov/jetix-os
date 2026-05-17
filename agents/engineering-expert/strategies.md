---
title: engineering-expert — Strategies (System Prompt Learning)
agent: engineering-expert
created: 2026-04-23
last_modified: 2026-04-23
state: scaffolding
confidence: N/A-scaffolding
expected_evolution:
  cycle_10: 5–10 refactor-rules accumulated; critic false-positive rate baselined; ≥1 entry on optimizer-vs-critic mode-confusion observed-in-cycle
  cycle_50: First mode-confusion audit; §3/§4 rubrics refined from observed critic-vs-optimizer drift; Ousterhout deep-module checklist adjusted on per-domain feedback
  cycle_200: Split-trigger evaluation per §1d — consider splitting into code-expert + architecture-expert if artefact-mix >60/40 sustained over 3 consecutive cycle_50 windows AND dispatch-rate >20 cells/week × 3 weeks
---

# Strategies — engineering-expert

## Entry Format

Each entry uses 4-part DRR per FPF E-9 §2.9 with the documented
swarm-wide translation (critic-gate1 M-2 of Шаг 2.2.4):

1. **Decision** — what was decided
2. **Reasoning** — why (≈ FPF `context`)
3. **Result** — observed outcome (alternatives subsumed in Reasoning's
   why-not rationale)
4. **Review** — validated | refuted | partial (≈ FPF `review-checkpoint`)

Plus Evolution sub-block per FPF §3.5.

## Entries

### 2026-05-17 — A.2.9 context-policy cross-reference must be self-declared, not delegated to a pending sibling doc

1. **Decision:** When a doc uses U.SpeechAct (A.2.9) with the «institutes» semantic, it must declare the context-policy for that speech act directly in its own A.1.1 BoundedContext section (or equivalent §2.1 expansion). Delegating the policy declaration to another doc via a cross-reference is not sufficient — especially when the referenced section does not yet exist. The phantom-reference pattern (citing «doc X §4.1.4» before doc X has been revised to contain that section) is a provenance gate failure.
2. **Reasoning:** cycle task-fpf-describe-jetix-2026-05-17; Doc 06 (Clean Internet Layer) §2.2 A.2.9 row claimed «Clan-context policy declared in doc 03 §4.1.4». Doc 03 critic (FAIL-2, FAIL-3) had already found that doc 03 has no formal A.1.1 BoundedContext and no §4.1.4. Doc 06 integrator was written anticipating a doc 03 structure that did not yet exist, creating a phantom cross-reference. FPF A.2.9:4.1 normative: absent explicit context-policy, SpeechAct is treated as communicative Work occurrence only — not institutional. Secondary pattern: §4.1 formal section mapped SpeechAct to `publish(F_grade, G_scope, R_condition)` — an F-G-R publication act — contradicting the §2.2 description of SpeechAct as trust-constituting. F-G-R is B.3, not A.2.9 content.
3. **Result:** FAIL-1 blocking correction raised (moderate); D-DOC06-ENG-4 + D-DOC06-ENG-5 dissents introduced. RC-1 fix: self-declare the trust-infrastructure context-policy in doc 06 §2.1; fix §4.1 SpeechAct formal expression to use actType + institutes fields (CommitmentIdRef, RoleAssignmentRef). Effort: medium.
4. **Review:** partial — fix not yet applied; pending revision cycle. Pattern confirmed across two cycles (doc 03 + doc 06). Promote to §3.1 Conformance Checklist as check #9 candidate if it fires in doc 07.

#### Evolution
- changelog:
  - 2026-05-17 — created from task-fpf-describe-jetix-2026-05-17-internet-eng-critic
- last-review: 2026-05-17
- expected-evolution:
  - cycle_10: Check doc 07 (E2E Overview) for same phantom-cross-reference pattern. If fires ≥1 more time, promote to §3.1 Conformance Checklist check #9 (FPF-primitive-policy-self-declared).
  - cycle_50: If the self-declaration pattern becomes standard across all 7 docs, mark validated and add to critic briefing template.

### 2026-05-17 — Formal section aspirational-tag discipline: §4 formal ≠ §2 honest-status

1. **Decision:** When a doc's §2 primitive table correctly tags a primitive as F2/aspirational (e.g. A.10 Evidence Graph = stub), the §4 formal section must carry the same aspirational tag on any expression involving that primitive. Formally expressing `A.10.EvidenceGraph(A, trail)` as a callable binary predicate when the §2 table says «formal Evidence Graph = aspirational» is an internal inconsistency — the formal section overstates operational status.
2. **Reasoning:** cycle task-fpf-describe-jetix-2026-05-17; Doc 06 §2.2 and §3.8 correctly state A.10 Evidence Graph formal schema = stub; git log = primitive implementation (F2). However, §4.1 TrustFormation predicate uses `A.10.EvidenceGraph(A, observed_work_trail)` without aspirational annotation — as if the Evidence Graph is queryable. This inconsistency could mislead a reader into thinking TrustFormation is currently computable. The fix is a one-line annotation: `[aspirational; current primitive: A.10_primitive(A) = git_log_entries(A)]`.
3. **Result:** FAIL-3 minor correction raised. Effort: small. Pattern: formal sections often inherit implicit operational framing from pseudocode style; aspirational tags must be explicitly imported from the honest-status section.
4. **Review:** partial — pending revision. Generalizable pattern: whenever §2 says «aspirational» or «F2 primitive», check §4 for implicit operational framing.

#### Evolution
- changelog:
  - 2026-05-17 — created from task-fpf-describe-jetix-2026-05-17-internet-eng-critic
- last-review: 2026-05-17
- expected-evolution:
  - cycle_10: Check doc 07 §4 formal sections for same aspirational-tag gap. If fires ≥1 more time, add to critic Conformance Checklist check.
  - cycle_50: Consider a generic rule: «§4 formal sections must carry honest-status annotations matching §2 table F-grades».

### 2026-05-17 — FPF primitive misuse detection: U.WorkPlan vs U.MethodDescription vs U.Episteme

1. **Decision:** When a doc uses `U.WorkPlan (A.15.2)` to classify a set of heuristic principles or rules-of-thumb, check the A.15.2:4.1 definition (planned windows + intended performers + resource budgets + acceptance targets + dependencies). If those structural elements are absent, the correct primitive is `U.MethodDescription (A.3.2)` (recipe for how) or `U.Episteme` (surfaced candidate), not `U.WorkPlan`. OQ-style caveats in the same document that acknowledge "Ruslan не ack'нул" are a signal that the primitive is not yet U.WorkPlan — catch these early in critic mode.
2. **Reasoning:** cycle task-fpf-describe-jetix-2026-05-17; Self-OS P-1..P-10 classified as U.WorkPlan in §2.1/§4 of eng-integrator draft. A.15.2:4.3 lexical sanity table explicitly distinguishes "workflow/recipe" (MethodDescription) from "schedule/calendar/plan" (WorkPlan). The draft's own OQ-DOC01-4 said "до ack — они = surfaced candidates, не confirmed U.WorkPlan" — internal contradiction the critic surfaced. Source: FPF-Spec.md A.15.2:4.1, A.15.2:4.3.
3. **Result:** Blocking correction R-1 raised; D-DOC01-ENG-1 dissent introduced. Fix = replace U.WorkPlan with U.MethodDescription candidate. Effort: small.
4. **Review:** partial — fix not yet applied; pending revision cycle. Validate at next cycle when revised draft is reviewed.

#### Evolution
- changelog:
  - 2026-05-17 — created from task-fpf-describe-jetix-2026-05-17-self-os-eng-critic
- last-review: 2026-05-17
- expected-evolution:
  - cycle_10: Check if U.WorkPlan misuse recurs in Doc 02 (Methodology) or Doc 03 (Tribe); if pattern repeats ≥2 more times promote to AP-ENG table.
  - cycle_50: If U.MethodDescription candidate → Ruslan ack flow works without recurrence, mark this rule validated.

### 2026-05-17 — A.4 Temporal Duality: "simultaneous modes" is a spec violation

1. **Decision:** When an FPF-described doc states a holon "exists in two modes simultaneously" (design-time + run-time), flag it as A.4:4 temporal invariant violation. The invariant `Tᴰ ∩ Tᴿ = ∅` is explicit. The correct framing is "alternates between" or "currently in run-time (with Foundation frozen as design artifact)." The confusion is common because Foundation LOCKED looks like both: it is a design artifact (Tᴰ output) that the run-time system relies on (Tᴿ).
2. **Reasoning:** cycle task-fpf-describe-jetix-2026-05-17; §0 TL;DR of eng-integrator draft used "существует в двух режимах одновременно." A.4:4 specifies Tᴰ ∩ Tᴿ = ∅ and CC-A.4.1 requires tagging with current scope. Source: FPF-Spec.md A.4:4, CC-A.4.4.
3. **Result:** Blocking correction R-2 raised; D-DOC01-ENG-2 dissent introduced. Fix = one sentence replacement. Effort: small.
4. **Review:** partial — pending revision. Validate when revised draft reviewed.

#### Evolution
- changelog:
  - 2026-05-17 — created from task-fpf-describe-jetix-2026-05-17-self-os-eng-critic
- last-review: 2026-05-17
- expected-evolution:
  - cycle_10: Check for same pattern in Doc 04 (Corporation) and Doc 07 (E2E Overview) where Foundation-as-design vs cycles-as-runtime is described. If catches ≥2 instances, add to §3.1 Conformance Checklist as check #9.

### 2026-05-17 — FPF A.1.1 BC-2: U.BoundedContext containment is a spec violation

1. **Decision:** When a doc models a U.System supersystem as compositionally containing U.BoundedContext instances (workshop BoundedContexts inside a platform U.System), flag it as FPF A.1.1 BC-2 (Flat Context Map) violation. Correct modeling: (a) workshops = U.System sub-holons inside a platform U.System (valid A.1 holarchic composition), each with an *associated* U.BoundedContext that is peer-level to the Platform context via explicit Bridges — OR (b) platform and each workshop = peer U.BoundedContexts connected only by Bridges (BC-5). Never model BoundedContext-inside-BoundedContext or U.System-compositionally-containing-BoundedContext.
2. **Reasoning:** cycle task-fpf-describe-jetix-2026-05-17; Doc 05 (Platform) §4 FPF formal version declared `composition: set_of(WorkshopBoundedContext_N)` with workshops typed as U.BoundedContext (A.1.1). FPF A.1.1:4.3 BC-2 explicit: "No U.BoundedContext is modeled as inheriting from, containing, or being contained by another U.BoundedContext." A.1.1:4.3 also states contexts have no is-a or containment relations; cross-context relationships via Bridges only. The Mermaid diagram's subgraph nesting reinforced the violation visually. [src: FPF-Spec.md lines 1375, 1385, 1419]
3. **Result:** FAIL-1 blocking correction raised. Fix options: R-1A (workshops as U.System sub-holons + peer BoundedContexts via Bridges) or R-1B (all as peer BoundedContexts via Bridges). Effort: medium.
4. **Review:** partial — fix not yet applied; pending revision cycle. Validate when revised Doc 05 draft reviewed.

#### Evolution
- changelog:
  - 2026-05-17 — created from task-fpf-describe-jetix-2026-05-17-platform-eng-critic
- last-review: 2026-05-17
- expected-evolution:
  - cycle_10: Check Doc 06 (Clean Internet Layer) and Doc 07 (E2E Overview) for same U.BoundedContext containment pattern. If fires ≥2 more times, promote to §3.1 Conformance Checklist as check #9.
  - cycle_50: If OQ-4 (Workshop = BoundedContext vs brand-layer) resolves, update this rule with canonical Ruslan decision as the normative reference.

### 2026-05-17 — FPF A.3.1: U.Method is enacted, not hosted; run-time instance is U.Work

1. **Decision:** When a doc uses "hosting" as the relationship between a platform U.System and U.Methods from participating workshops, flag it as FPF A.3.1 misuse. FPF A.3.1:4.1 defines U.Method as an abstract transformation type that is **enacted** by a U.System bearing a TransformerRole to produce U.Work. A platform provides the substrate enabling enactment, not a "hosting" container. Additionally, the run-time occurrence of a method is U.Work (dated, spatiotemporally bounded enactment), not a "method occurrence" — that conflates design-time (U.Method) with run-time (U.Work).
2. **Reasoning:** cycle task-fpf-describe-jetix-2026-05-17; Doc 05 (Platform) §2.1 and §4 used "platform_role: infrastructure_for_method_occurrence" and "Method hosting (A.3.1)". FPF A.3.1:4.1: "U.Method is described by U.MethodDescription and enacted by a U.System bearing a TransformerRole to produce U.Work." FPF A.3.1:4.7: "U.Method is local to a U.BoundedContext." No FPF primitive called "hosting" or "method occurrence" exists. The enactment chain is the canonical pattern: TransformerRole → enacts → U.Method (via MethodDescription) → produces → U.Work. [src: FPF-Spec.md lines 5833-5837, 5900]
3. **Result:** FAIL-2 blocking correction raised. Fix = replace "hosting" framing with "enactment substrate" + replace "method occurrence" with "U.Work instances." Effort: small.
4. **Review:** partial — fix not yet applied; pending revision cycle. Validate when revised Doc 05 draft reviewed.

#### Evolution
- changelog:
  - 2026-05-17 — created from task-fpf-describe-jetix-2026-05-17-platform-eng-critic
- last-review: 2026-05-17
- expected-evolution:
  - cycle_10: Check Doc 02 (Methodology) for same Method/MethodDescription/Work conflation pattern. If fires ≥2 more times, add to §3.1 Conformance Checklist as check #9.
  - cycle_50: If method-hosting language persists in L1-audience docs for pedagogical reasons, consider creating an approved "simplified FPF" glossary note that maps platform-as-enactment-substrate to "hosting" with explicit caveat.

### 2026-04-27 — cyc-foundation-build-2026-04-28 (Wave A+B) — interface-card batch dispatch + A.14 typed-edge architectural decisions

1. **Decision**: For Phase A-2 interface card authoring, accept 3-4 cards per single dispatch (vs 1 card = 1 dispatch). Total 10 cards in 3 dispatches (Parts 1-3 / 4-6 / 7-10). Each card §A-§H with A.14 typed dependency edges (NO generic "depends-on") + L/A/D/E lanes per FPF A.6.B + F-G-R per B.3.
2. **Reasoning**: Each card 200-400 words; 3-4 cards per dispatch = 600-1600 words output per agent invocation. Within Opus 4.7 context budget. Single agent maintains coherence across related parts (info-flow / agent+governance / operations+ext themes). 3 dispatches vs 10 = 3.3× speedup with no coherence loss.
3. **Result**: 10 cards landed in ~10 min wall-clock (3 parallel dispatches). Substantive architectural decisions made within engineering integrator scope: Part 1 dependency edges = `operates-in` (not `creates`) — container persists independently of content; STOP gate placed in Laws lane (constitutional, not Deontics); D28 anchor as leading constraint at ingest, not lagging lint warning.
4. **Review**: VALIDATED. 3-4-cards-per-dispatch is the right batch size for A-2-style interface card authoring. Adopt as default.

**Evolution**: When future work requires N>5 interface-card-shaped artefacts, batch by theme into 3-4 per dispatch. Update §3 Integrator mode-section with batch-sizing heuristic.

### 2026-04-27 — cyc-foundation-build-2026-04-28 — agent tool-inventory mismatch defect

1. **Decision**: Brigadier dispatched engineering-expert + philosophy-expert for 4 consultant cards needing WebFetch (Anthropic CAI #13 / Event Sourcing #5 / SRE #6 / Mereology #14). Agents declared F4-NOT-LIVE-FETCHED honestly because their frontmatter excludes WebFetch.
2. **Reasoning**: Brigadier didn't pre-check agent toolset vs task requirement. Assumed all agents have WebFetch; in fact only general-purpose + brigadier do.
3. **Result**: 4 consultant cards have F4 quality flags; brigadier surfaces in AWAITING-APPROVAL §5 as known limitation. Honest declaration preserved trust + provenance gate integrity.
4. **Review**: VALIDATED honesty pattern; REFUTED brigadier dispatch discipline. Compound: maintain agent-tool-inventory-matrix in `swarm/wiki/brigadier/how-to-manage-agents/`. Pre-check before dispatch.

**Evolution**: When future work requires WebFetch / Bash / Task / specific MCP — verify target agent has tool BEFORE dispatch. Use general-purpose or brigadier-direct for tool-gap cases.

### 2026-04-23 — Optimizer-mode: bundle hypotheses by LOC invariant to eliminate sequence overhead

---
rule_slug: optimizer-bundle-by-loc-invariant
version: 0.1.0
created: 2026-04-23
last_review: 2026-04-23
status: active
ratio: {hits: 1, misses: 0}
expected_evolution:
  cycle_10: Validate that Bundle-1 (H-1+H-4+H-9) executor sprint reduced brigadier review
    turns by ≥4 vs the 3-separate-PR alternative. If confirmed, ratio.hits +1 and promote
    the "shared Bash helper" pattern to a second rule.
  cycle_50: Assess whether the LOC-bundling heuristic generalises beyond hook/script work
    (e.g. does it apply to documentation-only bundles?). If yes, widen ClaimScope.
  cycle_200: Evaluate whether automated dependency-graph analysis could replace manual
    LOC bundling (i.e. does a tool find better bundles than human-judgment bundling?).
---

- **Decision:** When optimizing a hypothesis set, group hypotheses by LOC invariant (same
  target files or same output directory) into execution bundles. Extract shared helpers
  (Fowler Extract Function / Extract Class) when two scripts share the same data-parsing
  pattern. Isolate HITL-gated hypotheses into a dedicated bundle so they do not block the
  autonomous bundles.
- **Reasoning:** cyc-swarm-self-improve-v1 optimizer pass over engineering-critic-01.md (10
  hypotheses). H-1 (settings.json hooks), H-4 (write-scope-guard.sh), H-9 (provenance-gate.sh)
  all wrote to `swarm/lib/hooks/` + `.claude/settings.json`. Sequencing them as 3 PRs adds 3
  brigadier-review turns; bundling to 1 PR saves 2 turns. H-4 and H-9 both parse frontmatter
  field `write_scope_glob` — Fowler Extract Function produces `parse-frontmatter-field.sh` and
  removes the DRY violation before it is written. H-3 and H-5 share the `swarm/evals/schema.md`
  format — Fowler Extract Class removes a second file from the effort budget. H-6 and H-10
  require HITL decisions; isolating them prevents them from blocking H-1..H-5 execution.
  Source: engineering-optimizer-01.md §3, §4.
- **Result:** 10 hypotheses → 4 bundles. Total effort: 17 → 16 points (direct). Sequence
  overhead: 10 brigadier-review cycles → 4. Net execution overhead reduction: 32% (6 fewer
  brigadier turns). Shared schema file: −1 file. Shared Bash helper: identified pre-emptively
  (not yet written; DRY violation prevented). All 5 invariants declared per bundle.
- **Review:** partial — optimizer pass complete; execution has not started. Review at Bundle-1
  completion: if Bundle-1 lands in ≤2 brigadier turns (vs 6 for 3 separate PRs), this rule
  is validated. Update ratio.hits at that point.

#### Evolution
- changelog:
  - 2026-04-23 — created from cyc-swarm-self-improve-v1 optimizer pass
- last-review: 2026-04-23
- expected-evolution: see frontmatter

---

### 2026-04-23 — Scaffolding placeholder

- **Decision:** scaffold `agents/engineering-expert/strategies.md` per
  Шаг 2.2.4 Part C.
- **Reasoning:** Layer-2 self-write rule per CLAUDE.md; FPF E-9 + D12
  mandate empty-but-structured strategies.md from day zero.
- **Result:** file lint-valid, Phase A bootstrap unblocked.
- **Review:** scaffolding only; first real entry on first cycle this
  expert participates in.

#### Evolution
- changelog:
  - 2026-04-23 — created (scaffolding)
- last-review: 2026-04-23
- expected-evolution: see frontmatter
