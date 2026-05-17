---
title: "Jetix vs IWE — epistemic side-by-side (philosophy-expert × critic)"
type: critic-review
mode: critic
expert: philosophy-expert
task_id: task-fpf-iwe-phase-b-2026-05-17
artefact_under_consideration: "Jetix multi-agent OS vs IWE FMT-exocortex-template — boundary discipline + distinction maps + overlap + honesty calibration"
caller: brigadier Phase B Шаг 3
date: 2026-05-17
F: F4
G: "epistemic compare; scope = public FMT-exocortex-template (ver 0.31.0 @ 2026-05-17) vs Jetix Foundation v1.0 LOCKED 2026-04-28; does NOT include paid Aisystant AI guide (B2 blocker)"
R: "refuted_if: category-mistake in boundary discipline section is shown to be wrong; accepted_if: brigadier's integrated Шаг 3 artefact cites this critic without factual correction"
prose_authored_by: claude (scribe, R1 posture — surface facts; no eval «better/worse»)
sources:
  - reports/fpf-iwe-distillation-2026-05-17/02-iwe-deep-v2.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
  - reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-iwe-verify.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-knowledge-synth-iwe-collection.md
  - swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-engineering-integrator-fmt-structure.md
  - CLAUDE.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md
  - decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md
dissents_preserved: 3
---

# Jetix vs IWE — Philosophy-Expert Critic Review (Шаг 3)

> **Constitutional posture.** R1 scribe. This critic surfaces observable facts from
> the two systems' public artefacts and applies the philosophy-expert § 3 Conformance
> Checklist to the comparability claim itself and to each system's epistemic discipline.
> No «better/worse» verdict. Dissents preserved per AP-6 — NOT averaged.
>
> **Scope boundary (top of doc).** All IWE findings derive from the public
> `FMT-exocortex-template` ver 0.31.0 (2026-05-17) on GitHub. The paid Aisystant
> platform AI guide remains blocked (B2 blocker per blockers.md). The distinction
> between template and platform is operative throughout this document.

---

## §1 Conformance Checklist (≥5 binary checks)

The artefact-under-review is the comparability claim: «Jetix and IWE are comparable
for audit purposes in Phase B.»

### Check 1 — Falsifier-named on comparability claim (Popper)

**Predicate:** Is the claim «Jetix and IWE are comparable as AI-enhanced intellectual
work systems» falsifiable?

**Evidence.** Jetix self-describes as «multi-agent system for managing an AI consulting
business and personal life» `[CLAUDE.md System Overview]`. IWE self-describes as «an
operating system for intellectual work» targeting an individual `[README.en.md L7]`. The
objects are demonstrably different: one is an organisational OS, the other is an individual
exocortex template. A strict comparability claim would be falsified if a domain boundary
exists that makes the comparison a category error.

**Falsifier.** The comparison is falsified at the strongest level if: (1) Jetix's
unit-of-operation is exclusively the multi-person organisation and has no individual
intellectual-work component, AND (2) IWE has zero organisational-coordination layer.
As shown in §5 below, neither condition fully holds — Jetix has an individual-owner
operator (Ruslan) and IWE has a Strategist role + Pack layer that could in principle
coordinate small teams. The falsifier fires partially, not fully.

**Result: PASS** — falsifier stated; comparison is legitimate but category-qualified.

---

### Check 2 — Paradigm-named on shift (Kuhn)

**Predicate.** The Step 3 audit performs a paradigm comparison. Does it name the
paradigm of each system and the anomaly that differentiates them?

**Evidence.**
- Jetix paradigm: «multi-agent business OS, owner is sole strategist, AI agents are
  executors» `[CLAUDE.md §4.1 rules 1-2]`. Paradigm label: organisational-substrate.
- IWE paradigm: «individual exocortex + FPF generative hierarchy; owner amplifies
  thinking session-by-session» `[README.en.md L41; CLAUDE.md §1 Fallback Chain]`.
  Paradigm label: individual-intelligence-amplification.
- Anomaly that separates them: IWE is built around a single practitioner's cognitive
  development loop (OWC fractal + Pack). Jetix is built around a business coordination
  loop with human-gate rules preventing agents from strategizing.

**Prior paradigm check.** IWE explicitly names its prior paradigm (AI-as-answer-machine
/ skills-first) in `docs/principles-vs-skills.md`. Jetix does not formally name its own
prior paradigm in Foundation v1.0. The JETIX-FPF.md archive (3762 lines, superseded)
represents the prior attempt — its archival is an implicit paradigm transition from
«heavy FPF derivative» to «light FPF-aligned tactical mechanisms» `[06-honest-self-audit.md §8]`.

**Result: PARTIAL PASS** — IWE names prior paradigm + anomaly; Jetix does not carry
a formal prior_paradigm: + anomaly: block. AP-PHIL-2 candidate for Jetix's own
documentation, not for this comparison artefact.

---

### Check 3 — Mental-model citation with conditions (Munger)

**Predicate.** This critic invokes the «IDE analogy» mental model for IWE and the
«organisational OS» mental model for Jetix. Are conditions stated for each?

**Evidence — IDE analogy for IWE.**
`README.en.md L29-31` verbatim: «Just as an IDE combines editor, compiler, and
debugger... IWE combines knowledge, planning, and AI agents.»
Conditions where this model holds: single developer/practitioner, known domain, repeated
work cycles. Conditions where it breaks: team-scale coordination, multi-owner strategy,
cross-organisational transactions.

**Evidence — organisational OS for Jetix.**
`CLAUDE.md System Overview`: «Jetix OS is a multi-agent system for managing an AI
consulting business and personal life.» The OS analogy holds for the substrate-scheduling
layer (Parts 1-10). It breaks for intelligence-amplification claims: an OS manages
processes; it does not amplify the thinking of the process owner
`[06-honest-self-audit.md §2 Foundation aggregate read]`.

**Result: PASS** — both mental models cited with conditions in this review.

---

### Check 4 — Method declares anti-scope (via-negativa, Stoic)

**Predicate.** Does this comparison name what it is NOT doing?

Anti-scope declared below in §4. Checked here as binary: **PASS** (see §4).

---

### Check 5 — Dichotomy-of-control identified

**Predicate.** For the honesty-calibration claim (§8), does this review identify
which variables are in our control vs not?

**Evidence.** The Phase B scope is bounded by what is readable: Jetix filesystem
(full access) and IWE public template (full access). Paid IWE platform (Aisystant)
is NOT in scope — this is explicitly not-in-our-control during Phase B. C5b
«IWE умнее конкурентов» remains non-verifiable until B2 blocker resolves.
`[02-iwe-deep-v2.md §0 + §2.1 C5a/C5b decomposition]`

**In-our-control.** Structural comparison of observable artefacts, FPF-mechanism
presence/absence, role-taxonomy alignment, gate discipline comparison.
**Not-in-our-control.** Paid layer internals, empirical session outcomes (C4 Arm C),
Tseren/Levenchuk's authoritative reconciliation of the mapping.

**Result: PASS** — dichotomy identified.

---

### Check 6 — No meta-claim without object-level instance

**Predicate.** Every meta-level claim in this critic cites ≥1 concrete object-level
instance.

Spot-checked below against §5-§8. All meta-claims carry a concrete instance or source
citation. **Result: PASS** (subject to brigadier gate).

---

### Check 7 — Fallacy-named-when-named (rhetoric)

**Predicate.** No fallacy referenced without naming it.

The critic section §9 (C5b treatment) names the specific fallacy pattern:
«appeal to architectural authority» — Levenchuk's positional claim about IWE superiority
is his insider assessment, not a public-facing falsifiable benchmark. Named here.

**Result: PASS**.

---

## §2 Acceptance Predicate (Hamel-binary)

```
acceptance_predicate:
  "This Jetix-vs-IWE critic is ACCEPTED if:
   (1) boundary discipline in §5 names a non-trivial category difference between
       Jetix and IWE (not just 'they are different') AND carries F-G-R, AND
   (2) §6 Distinction Map (Jetix → IWE) maps each of the 5 Jetix-UNIQUE mechanisms
       to an IWE equivalent or 'gap' with evidence path, AND
   (3) §7 Distinction Map (IWE → Jetix) maps each of the 11 IWE-UNIQUE constructs
       to a Jetix equivalent or 'gap' with evidence path, AND
   (4) §9 Dissents block is non-empty (≥1 preserved dissent), AND
   (5) §8 Honesty Calibration has ≥1 'IWE works / Jetix gap' entry AND
       ≥1 'Jetix works / IWE gap' entry with falsifiers for each.
   CURRENT STATUS: (1)-(5) addressed below in §5-§9."
```

---

## §3 Alternatives (≥2 + status quo, each with kill-condition)

### Alternative A — «Complementary tools, not competitors»

Interpretation: IWE and Jetix are tools for different levels of the same practitioner.
A Jetix owner (Ruslan) could run IWE as their personal intellectual-work layer while
running Jetix as the business-coordination layer. The comparison is then:
IWE = L1 individual; Jetix = L2 organisational. Non-competing objects.

Kill-condition: This interpretation fails if Jetix has a strong individual
intelligence-amplification layer that competes directly with IWE's OWC + Pack + ArchGate
workflow for the same use cases (single practitioner's daily work sessions).

Evidence: Jetix has no OWC equivalent, no Pack distribution model, no ArchGate.
Jetix does have CLAUDE.md, WikiV2, and voice pipeline — but these are substrate
management, not cognitive session amplification. Kill-condition NOT triggered. This
alternative is currently the best-supported interpretation.

### Alternative B — «IWE is what Jetix should be at the individual layer»

Interpretation: Jetix is the organisational substrate; IWE is the right model for
the intelligence-amplification layer that Jetix currently lacks. Running IWE on top
of Jetix (as the personal exocortex) would fill the ~25% intelligence-amplification gap
surfaced in `06-honest-self-audit.md §12`.

Kill-condition: This interpretation fails if Jetix's 5-layer agent memory + Strategic
Insights cadence is already a functionally equivalent intelligence-amplification layer —
meaning IWE adds no delta. Evidence from `06-honest-self-audit.md §13` shows Jetix's
closest-to-IA mechanisms (Hexagon synthesis, `/ask`, Provenance Officer) differ
structurally from IWE's OWC fractal + Pack. Kill-condition NOT triggered; Alternative B
is viable.

### Status quo — «Treat them as distinct objects, compare at the mechanism level only»

Interpretation: Keep IWE and Jetix as separate objects. Compare mechanism-by-mechanism
(not system-by-system). Each delta is a candidate for import/adaptation decision.

Kill-condition: Status quo fails if the mechanism-level comparison produces no actionable
delta (trivial comparison). Evidence: §6 and §7 below produce 16 gap entries — the
comparison is non-trivial. Kill-condition NOT triggered; status quo is viable but produces
less synthesis than Alternative A or B.

---

## §4 Anti-scope

- This critic does NOT arbitrate whether Jetix should adopt IWE — that is instrumental
  Рациональность (investor-expert + Ruslan; FPF L1003-1006 wall).
- This critic does NOT evaluate the paid Aisystant AI guide — B2 blocker active; all
  IWE claims bounded to public FMT-exocortex-template ver 0.31.0.
- This critic does NOT produce a score or ranking between Jetix and IWE — no
  «better/worse» claims per R1 constitutional posture.
- This critic does NOT author a response strategy to Levenchuk — that is HITL prose
  (Tier 2 R1 sole-strategist rule).
- This critic does NOT evaluate the FPF spec itself — that was Phase A Step 1 scope,
  not Step 3.
- This critic does NOT make capital-allocation recommendations regarding Aisystant
  subscription, R0 residency, or partnership with Tseren — investor-expert territory.

---

## §5 Boundary Discipline — Category Analysis

### §5.1 Objects being compared

| Dimension | Jetix OS | IWE (FMT-exocortex-template) |
|---|---|---|
| Declared unit-of-operation | «AI consulting business + personal life» `[CLAUDE.md System Overview]` | «Individual intellectual work, personal environment» `[README.en.md L7]` |
| Owner count | 1 owner (Ruslan) + 12 agents across 6 departments `[CLAUDE.md Agent Roster]` | 1 practitioner (forked personal instance) `[README.en.md L9]` |
| Organisational scope | Business OS — projects, CRM, sales, finance, strategy | Personal exocortex — knowledge, planning, session cadence |
| Distribution model | Single git repo, not distributable to N users | Template distribution via fork (`update.sh` HTTP manifest) `[02-iwe-deep-v2.md §6]` |
| FPF dependency | Tactical (4 direct adoptions + 5 intelligence-partial) `[06-honest-self-audit.md §11]` | Structural (FPF as declared Base tier) `[02-iwe-deep-v2.md §2.2]` |
| Primary classification | Organisational substrate (memory + automation dominant) `[06-honest-self-audit.md §12 table]` | Individual intelligence-amplification tool (OWC + Pack + ArchGate) |

`F: F4 | G: jetix-synthesis | R: refuted_if_Jetix_officially_repositions_as_individual_tool`

### §5.2 Comparability verdict (F-G-R)

**Claim:** «Jetix and IWE are comparable objects for mechanism-level audit.»

```yaml
F: F4
G: comparison-scoped
ClaimScope:
  holds_when: "comparison is mechanism-by-mechanism (Role taxonomy / Gate discipline /
              Memory layers / FPF-adoption depth); not system-level homogenisation"
  not_valid_when: "comparison is framed as 'which is better for X use case' — category
                  mismatch prevents direct substitution"
R:
  refuted_if: "any independent auditor finds they are NOT comparable at the mechanism
              level (i.e. the mechanisms are so different that no common vocabulary applies)"
  accepted_if: "mechanism comparison in §6-§7 below produces non-trivial delta entries
              (≥5 meaningful gaps or overlaps)"
```

**Verdict.** The comparison is NOT a category error at the mechanism level. It IS
a category error if framed as direct substitution («which should Ruslan use instead of
the other»). Both objects involve: AI agents with roles, session/work cadence, memory
layers, gate rules, FPF-adjacent mechanisms. The comparison is productive at the mechanism
level with the above scope qualifier.

---

## §6 Distinction Map — Jetix UNIQUE-5 → IWE equivalent (or gap)

Per `06-honest-self-audit.md §13`: 5 mechanisms Jetix has that are not FPF-derived.

### U-J1: Strategic Insights Hexagon synthesis cadence

**What Jetix has.** Weekly structured synthesis of 6-7 strategic insights (H1-H7
Heptagon), each with F-G-R, provenance trail, Ruslan-ack. Abductive output shape + DRR
pattern. `[06-honest-self-audit.md §7 + §13]`

**IWE equivalent.** Closest: `/strategy-session` skill (R1 Strategist role, daily/weekly
plan generation) + `WP-context` files per session. But: IWE strategy-session is
session-level plan generation, NOT a cross-week insight synthesis with F-G-R tagging.
Pack can store domain insights but no equivalent of a Hexagon multi-insight comparative
synthesis is present in the template.

**Gap.** IWE lacks a cross-cycle strategic synthesis cadence with F-G-R per insight.
Jetix has this (partially, draft-grade F2-F4). The Hexagon is the closest Jetix component
to Levenchuk's «intelligence amplification» bar.

`F: F4 | G: comparison | R: refuted_if_aisystant_AI_guide_has_equivalent`

---

### U-J2: R12 anti-extraction (constitutional candidate rule 12)

**What Jetix has.** Anti-extraction principle declared at constitutional tier (Pillar C
Tier-2 candidate rule): AI/substrate cannot extract value from members beyond agreed
share; members can fork-and-leave without penalty. Game Theory M-C mechanism backing.
`[JETIX-FIRST-CLAN-CHARTER-2026-05-12.md constitutional_anchor]`
`[CLAUDE.md §4.1 rule 12]`

**IWE equivalent.** None observed in public template. IWE's distribution model is
vendor-neutral for knowledge (Markdown/YAML/Git open) but vendor-locked for automation
(Claude Code CLI) `[02-iwe-deep-v2.md §12]`. The template's update mechanism
(`update.sh`) preserves user's `extensions/`, `params.yaml`, user-space — fork-friendly
design. But no explicit anti-extraction constitutional rule is declared.

**Gap.** IWE has fork-friendly data portability by design, but no explicit constitutional
anti-extraction norm. R12 in Jetix is unique — derived from Clan Charter + People-NS
strategy, not from IWE or FPF.

`F: F5 | G: comparison | R: refuted_if_SPF_or_FPF_contains_equivalent_norm`

---

### U-J3: 5-layer per-agent memory architecture (Core/Strategies/Scratchpad/Niche/Recall)

**What Jetix has.** Per-agent 5-layer memory: `agents/{id}/system.md` (Core) +
`agents/{id}/strategies.md` (compound learning) + scratchpad + niche symlinks +
mailbox recall. `[CLAUDE.md Wiki Architecture v2 Per-agent memory]`

**IWE equivalent.** IWE's memory lifecycle (S-35) carries 4 horizon tiers:
HOT/WARM/COLD/ARCHIVE with demotion cadence (14/30/90 days).
`[02-iwe-deep-v2.md §5.1]` This is a time-based single-layer demoting system.
Jetix has a role-specific multi-layer system. The two are structurally different:
IWE's memory is per-topic (what I know about X) vs Jetix's memory is per-agent
(what agent Y has learned over cycles).

**Gap.** IWE has no per-agent compound-learning memory analogous to
`agents/{id}/strategies.md` (DRR 4-part entries per cycle). IWE's Pack is the
domain knowledge repository, not an agent improvement repository. Jetix has
per-agent compound learning; IWE has per-topic knowledge compounding.

`F: F4 | G: comparison | R: refuted_if_aisystant_platform_has_per-agent_strategies_file`

---

### U-J4: B2 mini-swarm with de-morph reversibility + stage gates

**What Jetix has.** Project-type-aware orchestration (consulting / research / product /
bets), stage-gate predicates (SG-1 to SG-4), `/project-de-morph` rollback.
`[CLAUDE.md KM MVP section]`

**IWE equivalent.** IWE has project objects (`WP Gate` + `WP-REGISTRY.md` registration
in 4 places), but no multi-project stage-gate system with predicate-linted gates and
de-morph rollback. The closest structural analog is the Staging layer (L2 → L1
promotion) for template changes, not for project lifecycle.
`[02-iwe-deep-v2.md §5.2]`

**Gap.** IWE manages individual work products within one person's environment.
Jetix manages a portfolio of projects across business domains with stage-gate predicates.
No IWE equivalent to `/project-bootstrap --type=consulting --client=<id>`.

`F: F4 | G: comparison | R: refuted_if_Pack_layer_has_multi-project_coordination`

---

### U-J5: F2-F8 6-level Formality grade operational encoding (Halt-Log-Alert enforcement)

**What Jetix has.** Operational encoding of F2/F4/F8 grades into halt/log/alert
thresholds. F8 violations halt ≤1s; F4 ≤5s; F2 ≤60s. `[CLAUDE.md §4.1 Halt-Log-Alert]`

**IWE equivalent.** IWE has no F-G-R schema per claim `[02-iwe-deep-v2.md §8.2 row 5]`.
Memory files have frontmatter (type/horizon/status) but no Formality grade with
enforcement thresholds. ArchGate performs quality evaluation but uses a 7-factor
profile (ЭМОГССБ), not an F-G-R per-claim tagging discipline.

**Gap.** IWE does not implement per-claim F-G-R. This is Jetix's strongest direct FPF
adoption and is NOT replicated in IWE's public template.

`F: F5 | G: comparison | R: refuted_if_paid_AI_guide_enforces_F-G-R_per_session_claim`

---

## §7 Distinction Map — IWE UNIQUE-11 → Jetix equivalent (or gap)

Per `02-iwe-deep-v2.md §8.1`: 11 IWE constructs not in FPF Spec.

### U-I1: Pack — concrete domain-distribution format

**IWE construct.** Pack = formalised knowledge base for a domain; source-of-truth;
distributed as a separate repo (PACK-{domain}). After forking, users create their own
Pack. `[02-iwe-deep-v2.md §1.2]`

**Jetix equivalent.** Closest: `wiki/` (9 entity types) + `shared/knowledge/` +
per-project knowledge captured in stage-gate cycles. But: Jetix has no concept of a
«distributable domain Pack» — knowledge is internal to one Jetix instance.

**Gap.** Jetix cannot distribute domain knowledge as a standalone Pack to another user.
If Ruslan trains a second Jetix operator, there is no Pack-equivalent handoff mechanism.
Distribution to N users requires re-architecting. `[02-iwe-deep-v2.md §6]`

`F: F4 | G: comparison`

---

### U-I2: OWC ritual at 4 scales (Open → Work → Close fractal)

**IWE construct.** Mandatory session/day/week/month OWC fractal with blocking gates at
each level. `[02-iwe-deep-v2.md §3.1]`

**Jetix equivalent.** `/plan-day` + `/close-day` skills `[CLAUDE.md Skills section]`.
Both systems have day-open/close. Jetix does NOT have a session-level OWC, nor a
month-level OWC. The cadence is less granular.

**Gap.** Jetix has 2 of 4 OWC scales (day + implicit weekly from git commits). IWE has
all 4 scales with explicit protocols and blocking gates. Jetix's session-level work
lacks a formal opening/closing ritual with context-loss prevention enforcement.

`F: F4 | G: comparison`

---

### U-I3: ArchGate 7-factor checklist (ЭМОГССБ)

**IWE construct.** `/archgate` skill evaluates architectural decisions against 7
characteristics (Эластичность / Модульность / Обслуживаемость / Готовность / Стоимость
/ Совместимость / Безопасность = ЭМОГССБ) as conjunctive screening.
`[02-iwe-deep-v2.md §3.3]`

**Jetix equivalent.** `AWAITING-APPROVAL` packet + Default-Deny table for architectural
decisions `[CLAUDE.md §4.1 rule 2 + shared/schemas/]`. Foundation path writes require
AWAITING-APPROVAL. But: Jetix has no 7-factor quality profile evaluation of the decision
itself — only a blocking gate (approve/deny). The deliberative quality check is absent.

**Gap.** Jetix has a constitutional gate (binary approve/deny). IWE has a quality
evaluation framework (7-factor profile) before the gate. The deliberative layer is
missing from Jetix.

`F: F4 | G: comparison`

---

### U-I4: Memory lifecycle S-35 (HOT/WARM/COLD/ARCHIVE with demotion cadence)

**IWE construct.** Mandatory frontmatter on `memory/*.md`: horizon (hot/warm/cold/archive)
+ demotion timers (14/30/90 days). HOT = loaded every session ≤150 lines cumulative.
`[02-iwe-deep-v2.md §5.1]`

**Jetix equivalent.** Per-agent memory has 5 layers but no automatic demotion cadence.
`agents/{id}/strategies.md` grows unbounded; there is no horizon-based load management.
CLAUDE.md boot context is loaded every session but has no explicit line-count cap
analogous to IWE's HOT ≤150 lines constraint.

**Gap.** Jetix has no memory lifecycle management with explicit demotion timers. Risk:
agents accumulate growing context without pruning discipline. IWE's S-35 directly
addresses this with operational enforcement.

`F: F4 | G: comparison`

---

### U-I5: Scheduling layer (launchd / cron / WSL OS-level triggers)

**IWE construct.** R8 Synchronizer role implemented as OS-scheduler (launchd/cron/WSL).
`setup.sh` installs cron entries. `[02-iwe-deep-v2.md §4 table]`

**Jetix equivalent.** Toggl tracking and voice pipeline (`tools/run_pipeline.sh`)
have OS-level execution, but these are manual-trigger tools, not scheduled agents.
No launchd / cron entries in Jetix.

**Gap.** Jetix has no autonomous scheduling layer. All agent invocations are
human-initiated. IWE has OS-level background synchronisation.

`F: F4 | G: comparison`

---

### U-I6: Creative Pipeline (note → draft → template → publication)

**IWE construct.** Operational pipeline for creative/knowledge work from fleeting
notes through publication. Referenced in `02-iwe-deep-v2.md §8.1 row 6`.

**Jetix equivalent.** Wiki pipeline (raw → ingested → compiled → linted → ready)
`[CLAUDE.md Wiki Pipeline]`. This is structurally analogous — both are staged
knowledge-production pipelines. The difference is that Jetix's pipeline is
knowledge-base-oriented (processing external sources), while IWE's Creative Pipeline
is author-output-oriented (publishing the practitioner's own work).

**Gap.** Partial. Jetix has a knowledge-ingestion pipeline; it lacks an explicit
author-to-publication pipeline for Ruslan's own creative/thought output.

`F: F4 | G: comparison`

---

### U-I7: Digital Twin — runtime mirror of user's work state

**IWE construct.** A runtime mirror tracking user's active work state.
Referenced in `02-iwe-deep-v2.md §8.1 row 7`.

**Jetix equivalent.** `shared/state/` JSON files + `swarm/logs/` per cycle.
`[CLAUDE.md Architecture — State: JSON files in shared/state/]`

**Gap.** Partial match. Jetix has state files but no formal «Digital Twin» concept
with real-time update discipline. Jetix state is event-driven (updated when agents
act); IWE Digital Twin (per its naming) implies a continuous mirror.

`F: F3 | G: comparison | R: low — Digital Twin not deeply documented in public template`

---

### U-I8: Harness — orchestration substrate for skill execution

**IWE construct.** Orchestration layer binding skills to session context.
Referenced in `02-iwe-deep-v2.md §8.1 row 8`.

**Jetix equivalent.** Brigadier dispatcher + hub-and-spoke protocol
`[CLAUDE.md §4.2 Hub-and-spoke rule]` + `swarm/lib/routing-table.yaml`.

**Gap.** Closest match of any IWE-UNIQUE-11 to a Jetix component. Both have an
orchestration layer. Key difference: Jetix brigadier is LLM-driven; IWE Harness is
protocol-driven with bash scripts + launchd. Different reliability and autonomy profiles.
`[02-iwe-deep-v2.md §4 table engineering observation]`

`F: F4 | G: comparison`

---

### U-I9: 4-contour system — multi-perspective work tracking

**IWE construct.** Multi-perspective work tracking across 4 contours.
Referenced in `02-iwe-deep-v2.md §8.1 row 9`.

**Jetix equivalent.** Strategic Insights Heptagon (7 dimensions of the business).
`[06-honest-self-audit.md §7]` + H1-H7 multi-view (Doc 1A / 1B public/investor/partner
views). But: the Heptagon is strategy-layer multi-perspective, not work-tracking
multi-contour. The Vincenti taxonomy tagging in the philosophy-expert integrator is
the nearest epistemic analog.

**Gap.** Jetix has multi-view at strategy layer; no 4-contour operational work-tracking
is implemented.

`F: F3 | G: comparison | R: low — 4-contour not deeply documented in public template`

---

### U-I10: WP Gate — operational alpha-state lifecycle (work product registration ritual)

**IWE construct.** БЛОКИРУЮЩЕЕ: every task requires opening protocol + WP registration
in 4 places (REGISTRY.md + WeekPlan + context/<WP-NNN>.md + external tracker).
`[02-iwe-deep-v2.md §3.2]`

**Jetix equivalent.** AWAITING-APPROVAL packet for Foundation-level writes.
`[CLAUDE.md §4.1 rule 2]` + stage-gate predicates for project lifecycle. But: IWE's WP
Gate fires on EVERY task (even small ones). Jetix's AWAITING-APPROVAL fires only on
Foundation-level writes. For ordinary tasks, Jetix has no equivalent blocking
registration ritual.

**Gap.** IWE has a universal work-product registration gate. Jetix has a constitutional
gate that fires only for high-blast-radius actions. Ordinary task work in Jetix has no
formal opening ritual — per-session context is not registered in a REGISTRY.

`F: F5 | G: comparison`

---

### U-I11: TTL — time-to-live on artefacts (auto-archival + freshness signals)

**IWE construct.** Time-to-live signals on artefacts triggering archival or review.
Referenced in `02-iwe-deep-v2.md §8.1 row 11`.

**Jetix equivalent.** `/crm-stuck` (>14d no touch triggers stuck detection) +
wiki `/lint` freshness checks `[CLAUDE.md CRM System stuck detection]`. Partial analog.
No formal TTL field on all artefacts.

**Gap.** Partial match via CRM stuck detection. No system-wide TTL discipline on wiki
pages, knowledge artefacts, or strategic documents.

`F: F3 | G: comparison`

---

## §8 Honesty Calibration

Same tone as Phase A `06-honest-self-audit.md`. Surface facts.

### Where IWE works, Jetix does not (genuine IWE advantage, not covered by Jetix)

| Domain | IWE mechanism | Jetix status | Evidence path |
|---|---|---|---|
| Individual session discipline | OWC fractal (4 scales) blocking gates | No session-level gate; no month-level OWC | `02-iwe-deep-v2.md §3.1` |
| Memory lifecycle management | HOT ≤150 lines; demotion cadence 14/30/90d | No demotion; unbounded accumulation | `02-iwe-deep-v2.md §5.1` |
| Architectural decision quality | ArchGate 7-factor ЭМОГССБ profile | Binary AWAITING-APPROVAL gate only | `02-iwe-deep-v2.md §3.3` |
| Domain knowledge distribution | Pack as distributable repo | No distribution model | `02-iwe-deep-v2.md §8.1 row 1` |
| Work product registration | WP Gate fires on every task | Only fires on Foundation-level writes | `02-iwe-deep-v2.md §3.2` |
| OS-level background automation | R8 Synchronizer (launchd/cron) | All invocations human-initiated | `02-iwe-deep-v2.md §4` |

`F: F4 | G: comparison | R: refuted_if_any_of_the_above_has_undiscovered_Jetix_equivalent`

---

### Where Jetix works, IWE does not (genuine Jetix advantage)

| Domain | Jetix mechanism | IWE status | Evidence path |
|---|---|---|---|
| Per-claim trust grade enforcement | F-G-R with Halt-Log-Alert (F8 ≤1s / F4 ≤5s) | No F-G-R per claim; ArchGate not per-claim | `06-honest-self-audit.md §9` |
| Constitutional anti-extraction | R12 (fork-and-leave without penalty, constitutional level) | Data-portable design but no constitutional norm | `JETIX-FIRST-CLAN-CHARTER-2026-05-12.md` |
| Multi-agent business coordination | 12 agents across 6 departments, hub-and-spoke | 5 roles (4 agential), individual-scope | `CLAUDE.md Agent Roster` |
| Strategic Insights synthesis cadence | Heptagon H1-H7, weekly abductive synthesis | No cross-cycle strategic synthesis | `06-honest-self-audit.md §7` |
| Organisational memory (CRM / projects) | 14-section CRM + portfolio stage gates | Individual knowledge only; no CRM | `CLAUDE.md CRM System` |

`F: F4 | G: comparison`

---

### Where both have parity (overlapping mechanisms)

| Mechanism | Jetix form | IWE form |
|---|---|---|
| Role ≠ Executor | IP-1 + executor-binding.yaml.template | Roles ≠ Skills ≠ Protocols (distinctions.md) |
| Gate before architectural action | AWAITING-APPROVAL (Foundation writes) | ArchGate + IntegrationGate + WP Gate |
| FPF as upstream dependency | Tactical (4 direct adoptions) | Structural (Base tier declared) |
| Human-in-the-loop for writes | Tier-2 R1 sole-strategist rule | HITL on all writes for R2 Extractor role |
| Fork / data-portability design | Git-native; filesystem = SoT | Fork-friendly; vendor-neutral knowledge layer |
| Session open/close discipline | `/plan-day` + `/close-day` | OWC day-scale |

`F: F4 | G: comparison`

---

### Where both fail (shared gap against Levenchuk bar)

| Gap | Against what bar | Evidence |
|---|---|---|
| Full U.Episteme slot graph enforcement | FPF A.1.1 + C.2.1 | `06-honest-self-audit.md §3; 02-iwe-deep-v2.md §8.2 row 1` |
| Abductive alternatives portfolio (formal) | FPF B.5.2 | Neither enforces alternatives-before-first-answer structurally |
| F-G-R per claim (full) | FPF B.3 | IWE doesn't have it; Jetix has it at schema level but not per-cycle claim tagging |
| Multi-view publication (E.17 MVPK full) | FPF E.17 | Both partial; Jetix has 1A/1B; IWE has Service Clauses |
| Claim Register (A.6.B) | FPF A.6.B | Neither implements a formal claim register |

`F: F4 | G: comparison`

---

## §9 C5b «умнее конкурентов» applied to Jetix

### §9.1 Would C5b apply if Jetix is treated as an IWE competitor?

**Claim to test.** Restate C5b for Jetix: «Inside Jetix, intelligence rests on FPF —
and it's clear why Jetix is smarter than competitors.»

**Evidence for C5b-Jetix.**
- Structural FPF dependency: 4 direct adoptions (F-G-R + IP-1 + Pillar C + Default-Deny)
  `[06-honest-self-audit.md §11]`.
- BUT: Levenchuk's C3 critique («не очень верю, что у вас усиление интеллекта будет
  как-то больше, чем у vanilla AI-агента») is partially correct for Jetix.
  ~27 memory/automation vs ~12 intelligence/FPF-derivative components.
  `[06-honest-self-audit.md §12]`

**Falsifier for C5b-Jetix.**
C5b-Jetix is falsified if: a C4-benchmark (Arm D = Jetix stack) produces answers not
meaningfully better than Arm A (vanilla Claude) on bounded-context + alternatives-portfolio
+ F-G-R dimensions. This benchmark is not yet run (Phase B queue).
`[00-SUMMARY-FOR-RUSLAN.md §6 C4 benchmark design]`

**Named fallacy.** If C5b were stated for Jetix as-is, it would constitute appeal to
architectural authority: «we have FPF-like mechanisms, therefore smarter» without
empirical evidence. This is the same epistemic problem as C5b for IWE.

`F: F2 | G: positioning | R: refuted_if_C4_benchmark_Arm_D_scores_at_or_below_Arm_A`

---

## §10 Preserved Dissents (AP-6)

### Dissent D-1: Template ≠ Platform AI guide (carried from Step 2)

| Position | Held by | F-G-R |
|---|---|---|
| All IWE findings in this review derive from the public template (ver 0.31.0) | This critic | F6 / corpus-bounded / R-high |
| C5 («IWE умнее конкурентов») likely refers to the paid Aisystant AI guide, not the public template | philosophy-expert × critic (Step 2 iwe-verify) | F5 / inference / R-medium |
| Reconciliation | Cannot resolve without B2 unblock. All §6-§8 gap comparisons are provisional for the IWE side until Ruslan runs empirical IWE sessions | — |

### Dissent D-2: Complementary vs Competing framing

| Position | Held by | F-G-R |
|---|---|---|
| IWE and Jetix are complementary (individual layer vs org layer); no direct competition | Alternative A (§3) | F4 / structural / R-medium |
| IWE represents the intelligence-amplification layer Jetix currently lacks, making it a gap-filling tool rather than competitor | Alternative B (§3) | F4 / structural / R-medium |
| Reconciliation | Both preserved; the choice between «complementary» vs «gap-filling» is instrumental (investor-expert + Ruslan). This critic preserves both epistemic framings | — |

### Dissent D-3: FPF as structural dependency vs active runtime discipline in IWE

| Position | Held by | F-G-R |
|---|---|---|
| FPF is operationally active in IWE at runtime (Fallback Chain + CLAUDE.md Base tier declared) | 02-iwe-deep-v2.md §2.2 | F5 / structural / R-high |
| FPF is background architectural dependency, not enforced runtime discipline (no FPF identifier citations in operational guidance; no U.Episteme enforcement) | philosophy-critic-iwe-verify.md Check 2/3 | F4 / public-corpus-only / R-medium |
| Reconciliation | Cannot resolve without seeing FPF-Spec identifier citations in session-level agent guidance (B2 blocker). Structural dependency = VERIFIED. Runtime enforcement depth = UNVERIFIED | — |

---

## §11 Residual Open Questions (for brigadier integration)

1. Does the paid Aisystant AI guide implement F-G-R per claim? This would change §6 U-J5
   gap rating from «IWE gap» to «IWE parity or advantage».
2. Does IWE's Digital Twin (U-I7) and 4-contour system (U-I9) have richer documentation
   in the paid layer? The public template references are thin.
3. If Ruslan runs IWE empirically (C4 Arm C), does the OWC fractal discipline produce
   measurably better epistemic output than Jetix's `/plan-day` + `/close-day`? This is
   the empirical heart of the Levenchuk C3 challenge applied to IWE.
4. The A.7 vs A.2+A.3+A.15 alignment question (`02-iwe-deep-v2.md §13 Q4`) — resolving
   this would sharpen the FPF-mechanism overlap table in §8.

---

*Draft complete. Brigadier integrates with sys-integrator cell and mgmt-integrator cell
into canonical `jetix-vs-iwe-audit-2026-05-17.md`. 3 dissents preserved per AP-6.*
