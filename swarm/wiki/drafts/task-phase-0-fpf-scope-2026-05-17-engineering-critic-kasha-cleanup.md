---
task_id: phase-0-fpf-scope-2026-05-17-task-4
produced_by: engineering-expert × critic
mode: critic
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_concrete_contradictions_missed_OR_API_key_scan_omitted
date: 2026-05-17
inputs:
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
  - reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md
  - reports/phase-0-fpf-scope/03-comparison-matrix.md
  - CLAUDE.md
  - canonical/INDEX.md
  - JETIX-WORKING-FILE-v0-2026-05-17.md
  - .claude/config/default-deny-table.yaml
  - shared/state/active-projects.json
  - comms/mailboxes/manager.jsonl
conformance_checklist:
  - {check_id: "1-deep-module", result: N/A, evidence: "Non-code artefact audit"}
  - {check_id: "2-function-purpose", result: N/A, evidence: "Non-code artefact audit"}
  - {check_id: "3-test-integrity", result: N/A, evidence: "Non-code artefact audit"}
  - {check_id: "4-premature-abstraction", result: pass, evidence: "No new abstractions introduced; critic surface-only per R1"}
  - {check_id: "5-external-dependency", result: N/A, evidence: "No code paths in scope"}
  - {check_id: "6-dry", result: pass, evidence: "No duplication introduced in output"}
  - {check_id: "7-tool-eval-acceptance", result: N/A, evidence: "Not a tool-eval draft"}
  - {check_id: "8-architecture-pattern", result: N/A, evidence: "Not an architecture-proposal draft"}
acceptance_predicate: "Critic draft surfaces ≥20 concrete contradictions/dead-links/schema issues with file:line citations; API/secret scan run+reported; CLAUDE.md vs filesystem reality verified; ≥3 dissents preserved; no actions taken (surface-only per R1)"
---

# Engineering Critic — Phase 0 FPF Scope Каша Cleanup

---

## §0 Summary

Engineering-expert × critic audit of Jetix OS cross-document integrity against inputs from Tasks 1-3 (Phase 0 FPF scope definition).

**Total items surfaced:** 31 concrete findings across 7 categories.

**API/secret scan:** Run across `decisions/`, `swarm/`, `reports/` — no actual key values found; all hits are grep-pattern strings in audit/test code and documentation. See §5.

**Critical clusters (≥3 items each):**
- Dead links / archived-but-still-referenced files (8 items) — `design/JETIX-FPF.md`, `decisions/AUDIT-CURRENT-STATE-2026-04-27.md`, `decisions/RUSLAN-ACK-STRATEGIC-LAYER-PHASE-1-BASELINE-2026-04-28.md`, `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md`, `swarm/wiki/projects/` (dir), `daily-log/*.md` (no files), CLAUDE.md `wiki/` vs canonical `swarm/wiki/synthesis/`
- Concrete fact contradictions (9 items) — TRM resource names, agent count (12 vs 23 actual files), default-deny count (11 vs 12), `sync_invariant_count` mismatch, `active-projects.json` stale/single-entry vs «8 active projects», ICP Mittelstand vs Online-first, Foundation Parts count (11 vs 10+1 actual), «110 docs» unverified, CLAUDE.md §Architecture vs IP-1 principle
- Schema fidelity (5 items) — F-G-R tags missing enforcement split, `prose_authored_by` field inconsistent, `daily-log/` referenced but not materialized, `swarm/approvals/log.jsonl` entries with duplicate timestamps, canonical/INDEX.md refs `swarm/wiki/synthesis/` path pattern not matching earlier CLAUDE.md `wiki/` path pattern

**Constitutional posture maintained:** R1 surface-only. R2 Foundation read-only. R6 provenance per row. Append-only suggestions only. No edits made.

---

## §1 Concrete Contradictions Table

Cross-document fact mismatches with file:line per side.

| # | File A | Line/Section A | Claim A | File B | Line/Section B | Claim B | Type | Suggested action |
|---|---|---|---|---|---|---|---|---|
| **C-01** | `CLAUDE.md` | L116 | «12 specialized agents across 6 departments» | `.claude/agents/` filesystem | (actual count) | 23 `.md` files exist: 12 legacy + `staging-writer`, `sweep-worker`, `brigadier`, `engineering-expert`, `investor-expert`, `mgmt-expert`, `levenchuk-deep-dive-brigadier`, `quick-money-brigadier`, `philosophy-expert`, `project-brigadier`, `systems-expert` | contradiction | Add disclaimer: «12 declared role-types Phase 1-4; 23 agent files total including ROY swarm + project brigadiers» |
| **C-02** | `CLAUDE.md` | L32 («10 LOCKED Foundation parts F5» heading) | Heading says 10 parts | `CLAUDE.md` | L34-44 (list under heading) | List contains 11 entries (Parts 1-10 + Part 11 under «Strategic Layer» subheading) | contradiction (heading vs body) | Change heading to «11 LOCKED Foundation parts F5» OR restructure so Part 11 is explicitly separate from the count |
| **C-03** | `CLAUDE.md` | L59 | «`.claude/config/default-deny-table.yaml` — Part 6b §I.2 constitutional_never_list (11 entries derived from Pillar C Tier 2 foundation_generic)» | `.claude/config/default-deny-table.yaml` | L5 (comment) + L13 (`sync_invariant_count: 12`) | Comment says «count == 11»; field says `sync_invariant_count: 12`; actual entries in `constitutional_never_list:` = 12 (R12 added 2026-05-12) | contradiction (three-way: CLAUDE.md text / yaml comment / yaml field) | Update CLAUDE.md to «12 entries» OR add inline note «11 original + 1 additive R12»; reconcile yaml comment with yaml field |
| **C-04** | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §3.2 (lines 134-139) | TRM 6 resource classes: Attention / Time / Capital / Knowledge / Network / Reputation | `decisions/JETIX-TRM-MODEL-2026-04-30.md` (LOCKED v1.0) | L27-32 | TRM 6 resource classes: Финансы (capital) / Время CEO / Аудитория (audience) / Информация (knowledge) / Compute / Команда (talent) | contradiction (resource names differ; working file substitutes «Network» + «Reputation» for «Audience» + «Compute» + «Talent» and collapses) | Working file §3.2 claims «per LOCKED Doc» but does not reproduce LOCKED Doc resources faithfully; add disclaimer OR correct to canonical resource names |
| **C-05** | `CLAUDE.md` | L312 (§Проекты heading: «8 активных») + `JETIX-WORKING-FILE-v0-2026-05-17.md` §9 header | «8 active projects» | `shared/state/active-projects.json` | entire file | Contains exactly 1 project entry (`quick-money`); `last_updated: 2026-04-14T00:00:00Z` | contradiction (count 8 vs 1 in state file; stale date) | Mark «8 projects» as «declared roster» not «state-tracked roster»; add pointer to state JSON staleness caveat |
| **C-06** | `CLAUDE.md` | L71 | «[JETIX FPF Constitutional Spec](design/JETIX-FPF.md) — 3758 lines; FPF-Steward governed» | filesystem | `design/JETIX-FPF.md` | File does NOT exist at that path; actual location: `archive/design/JETIX-FPF.md` (archived 2026-05-06 per working file disclaimer + `JETIX-WORKING-FILE-v0-2026-05-17.md` line 22: «JETIX-FPF.md (3762-строчный derivative-attempt FPF interpretation) был archived 2026-05-06») | dead-link + stale-cross-ref | Remove from CLAUDE.md Constitutional documents section OR update path to `archive/design/JETIX-FPF.md` with «archived» label; note: 3758 vs 3762 line count also inconsistent across docs |
| **C-07** | `CLAUDE.md` | L73 | «[Audit Current State](decisions/AUDIT-CURRENT-STATE-2026-04-27.md)» | filesystem | `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` | File does NOT exist; referenced in `archive/missing-files-2026-05-06.md` and `archive/cross-ref-changes-log-2026-05-06.md` | dead-link | Remove from CLAUDE.md OR replace with archive path; suggest «add deprecated disclaimer» |
| **C-08** | `CLAUDE.md` | L72 | «[Foundation Build Master Plan Brief](decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md)» | filesystem | `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | File does NOT exist at that path; exists at `archive/decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` | dead-link | Update path to archive or mark «archived» |
| **C-09** | `CLAUDE.md` | L88 | «[Phase 1 Strategic Layer Templates ack](decisions/RUSLAN-ACK-STRATEGIC-LAYER-PHASE-1-BASELINE-2026-04-28.md)» | filesystem | `decisions/RUSLAN-ACK-STRATEGIC-LAYER-PHASE-1-BASELINE-2026-04-28.md` | File does NOT exist at `decisions/`; found in `archive/decisions/` per archive grep | dead-link | Update path to archive or note «baseline predecessor; see archive» |
| **C-10** | `CLAUDE.md` | L116 | «12 specialized agents» (Architecture section) | `CLAUDE.md` | L111 | «IP-1 Role≠Executor — Foundation роли = U.Episteme abstract role-types; executor bindings = RUSLAN-LAYER» (Critical Tier-2 Principles section) | internal contradiction (same doc claims «12 agents» in architecture section without noting that «12» = role-type declarations, not running executors per the IP-1 principle stated 5 lines above) | Add inline clarification: «12 = declared role-types (Phase 1: 4 active; Phase 2-4: 8 planned per Phase column)» to Agent Roster table header |

---

## §2 Stale Cross-Refs / Dead Links

Files referenced in canonical/active documents that are broken, missing, or pointing to archived locations.

| # | Source file | Section/line | Ref target | Issue | Type | Suggested action |
|---|---|---|---|---|---|---|
| **L-01** | `CLAUDE.md` | L16 | `CANONICAL-WALKTHROUGH-2026-05-06.md` | File exists (verified) but claims «110 docs со статусом» — audit count unverified in this pass (canonical/INDEX.md does not itself contain 110 listed items in visible content; count from walkthrough doc not re-verified here) | live-flag (unverified count) | Verify count still accurate; or add «as of 2026-05-06» qualifier |
| **L-02** | `canonical/INDEX.md` | §3b (lines 67-68) | `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` + `swarm/wiki/synthesis/foundation-master-overview-human-workshop-2026-05-06.md` | Both files exist at `swarm/wiki/synthesis/` (verified). However CLAUDE.md §Wiki Architecture v2 (L226-254) references `wiki/` (without `swarm/`) as «главный KB» and uses paths like `wiki/index.md`. Two different path roots in use across docs without reconciliation note | stale-cross-ref (path convention drift) | Add note in canonical/INDEX.md that `swarm/wiki/synthesis/` is distinct from `wiki/` (legacy v1 migration path) per MIGRATION.md; cross-reference MIGRATION.md |
| **L-03** | `CLAUDE.md` | L88 | `decisions/RUSLAN-ACK-STRATEGIC-LAYER-TEMPLATES-2026-04-28.md` | File exists at `decisions/RUSLAN-ACK-STRATEGIC-LAYER-TEMPLATES-2026-04-28.md` (verified). OK. | OK | — |
| **L-04** | `CLAUDE.md` | L149 | `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/bundle-5-strategic-layer/claude-md-reframing-decision.md` | File exists (verified). OK. | OK | — |
| **L-05** | `reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md` | frontmatter `parent` field | `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` | File exists. OK. | OK | — |
| **L-06** | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.1 (line citing `reports/jetix-vs-iwe-audit-2026-05-17.md §3`) | `reports/jetix-vs-iwe-audit-2026-05-17.md` | File exists (verified). OK. | OK | — |
| **L-07** | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.2, Appendix B | `reports/strategic-decisions-2026-05-12.md §2` | File exists (verified). OK. | OK | — |
| **L-08** | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.2 attribution trail item 4 | `swarm/awaiting-approval/r12-anti-extraction-2026-05-12.md` | File exists (verified). OK. | OK | — |
| **L-09** | `CLAUDE.md` | L227-254 (Wiki Architecture v2) | `MIGRATION.md` — referenced as «см. MIGRATION.md» for `knowledge-base/` migration | `MIGRATION.md` file exists (verified). Reference valid. | OK | — |
| **L-10** | `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` | §2 O-01 | `shared/state/active-projects.json:L9 revenue_current:0` | File exists. revenue_current = 0 at line 10 (not L9 exactly — 0-indexed vs 1-indexed off-by-one). Minor. | provenance-broken (line ref off-by-one) | Correct citation to L10 or use key-name ref instead of line number |
| **L-11** | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | §D edge-table, §I.1 schema | `daily-log/<YYYY-MM-DD>.md` daily artefacts | Part 9 architecture declares daily-log schema and SLI monitoring (daily-log-creation-rate). Filesystem shows `daily-log/drafts/.gitkeep` only — no actual daily-log files exist. Part 9 §I.1 schema materialised as spec; zero instances produced. | stale-cross-ref (spec references operational artefact that doesn't exist) | Add disclaimer to Part 9 §I intro: «daily-log materialization = Phase B stub; no instances exist as of 2026-05-17» |
| **L-12** | `canonical/INDEX.md` | §5 | `swarm/wiki/operations/` folder reference | `swarm/wiki/operations/quick-log-template.md` exists (verified). Folder itself exists. OK. | OK | — |
| **L-13** | `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` | §1 O-20 | `swarm/wiki/projects/` (0 files) | Directory `swarm/wiki/projects/` does not exist at all (glob returns nothing). Task 1 correctly notes «0 files» but does not note dir-not-found. | stale-cross-ref (dir not found) | Explicitly note in Task 1 §5 CE-1 that `swarm/wiki/projects/` does not exist, not just that it has 0 files |
| **L-14** | `CLAUDE.md` | L263 | «CRM принципы: Filesystem = source of truth (per Global Rule 4)» | `CLAUDE.md` Global Rules section | L199 | Rule 4 is marked «(moved to §4.2)» — no longer at Global Rule 4; the CRM section still cites «per Global Rule 4» without updating to cite §4.2 | stale-cross-ref (internal rule renumbering not propagated) | Update CRM section rule citation from «Global Rule 4» to «§4.2» |

---

## §3 Schema Fidelity Issues

Where documents claim F-G-R or constitutional discipline but format is inconsistent.

| # | File | Section/location | Issue | Type | Suggested action |
|---|---|---|---|---|---|
| **S-01** | `.claude/config/default-deny-table.yaml` | L5 (comment) vs L13 (field) | Comment says `count == 11`; field `sync_invariant_count: 12`. Two values in same file contradict. R12 was added 2026-05-12; comment not updated. | schema-violation (internal inconsistency) | Update comment to `count == 12` or add annotation «was 11 pre-R12; additive 2026-05-12» |
| **S-02** | `CLAUDE.md` | L59 | Claims «11 entries» for default-deny-table; actual entries = 12 (verified full read) | schema-violation (derived doc out of sync with source) | Update to «12 entries» per S-01 resolution above |
| **S-03** | `JETIX-WORKING-FILE-v0-2026-05-17.md` | frontmatter `prose_authored_by:` | Value is `brigadier-integrated (3 cells: eng × scalability + mgmt × integrator + phil × critic)` — this is a process description, not a valid `prose_authored_by` value per Foundation Part 11 §A.1 which requires either `ruslan` or `hybrid-with-ack-trail` | schema-violation (Part 11 §A.1 prose_authored_by schema not respected) | Either change value to `hybrid-with-ack-trail` (with ack trail reference) or add disclaimer that this field is using a non-canonical value; Foundation Part 11 §A.1 is the canonical reference |
| **S-04** | `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` | §1 table, O-08 top claim | F-G-R: «F8 (text) / F4 (operational)» — dual F value in single top claim F-G-R slot. FPF B.3 F-G-R schema requires a single triple per claim; dual values signal two distinct claims bundled under one row | schema-violation (EP-5 pattern from Task 2 confirmed) | Split O-08 into two claims: (a) text-LOCKED claim at F8, (b) enforcement-operational claim at F4, each with own triple |
| **S-05** | `swarm/approvals/log.jsonl` | lines 1 and 3 | Two entries with identical timestamps `2026-05-10T23:44:09` but different `restart_count` values (1 and 3; lines 2+4 have same ack timestamp `2026-05-10T23:55:46`). Suggests duplicate log entries written at same timestamp. | schema-violation (append-only log integrity; duplicate timestamps violate uniqueness assumption) | Suggest: add `sequence_id` field to log schema to disambiguate entries with identical timestamps; surface-only, no edit |
| **S-06** | `reports/phase-0-fpf-scope/03-comparison-matrix.md` | frontmatter `R:` field | `R: refuted_if_comparison_predicate_unstated_OR_categorical_mismatch_not_flagged_OR_BLOCKED_sources_not_flagged_OR_scalability_boundary_missing` — this is a compound (OR-chain) falsifier; FPF B.3 F-G-R schema requires R = single pathwise statement; compound OR-chain = multiple distinct R conditions bundled | schema-violation (F-G-R R field schema violation; same EP-5 pattern) | Split R field into primary R (most-load-bearing falsifier) + list of secondary conditions; or accept as operational shorthand with explicit note |
| **S-07** | `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` + `02-objects-per-fpf-deep.md` | §1 table O-07, §2 O-07 body | F8 label used for Foundation v1.0 LOCKED in multiple places. As phil × critic correctly surfaces (EP-5 pattern, Task 2 §0): «F8» in Jetix = «approved via 8 RUSLAN-ACK» NOT «tested 8 times / independently verified»; single-author approval ≠ FPF B.3 standard F8 grade. This is a schema-level semantic drift: adopting FPF grade labels with non-FPF semantics. | schema-violation (F-G-R grade semantics redefined without disclosure) | Add system-wide note (ideally in Part 6a architecture or canonical/INDEX.md) explaining Jetix F-grade semantics vs FPF B.3 F-grade semantics; explicitly label «F8 = Ruslan-ack-grade» not «FPF B.3 F8 formal proof» |

---

## §4 Foundation Parts Cross-Ref Audit (sample)

Spot-check of 3 Foundation Parts for internal cross-ref integrity.

### §4.1 Part 9 — Owner Interaction Scaffold

**Architecture file:** `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` (exists, verified)

**Refs inside Part 9:**
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-4-2026-04-28.md` — file exists at `decisions/` (verified)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md` — not spot-checked (deep path; listed in sources field)
- `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` — file exists (verified)

**Issue found:** Part 9 declares `daily-log/<YYYY-MM-DD>.md` artefacts as operational (§I.1 schema, daily-log-creation-rate SLI in Part 8). Filesystem: `daily-log/` contains only `drafts/.gitkeep`, zero daily-log files. Part 9 does not carry a «stub — Phase B» disclaimer in the operational section. (Also flagged as L-11 above.)

| Finding | File | Section | Type |
|---|---|---|---|
| FA-01 | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | §I.1 daily-log schema / §D edge-table D-5 Part 8 reference | stale-cross-ref (spec → non-existent operational artefacts) |

### §4.2 Part 6b — Human Gate (default-deny-table cross-ref)

**Architecture file:** `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (exists)

**Cross-ref check:** CLAUDE.md L59 and canonical/INDEX.md §3c both reference `.claude/config/default-deny-table.yaml` as Part 6b §I.2. Table exists (verified). Count discrepancy (11 vs 12) flagged at S-01/S-02/C-03.

**Also:** CLAUDE.md claims «11 entries derived from Pillar C Tier 2 foundation_generic». `principles/tier-2-system/foundation-generic/` glob returns 13 files (12 principle files + `_index.md`). 12 principles match 12 table entries. The word «derived» is accurate; the count «11» is stale.

| Finding | File | Section | Type |
|---|---|---|---|
| FA-02 | `CLAUDE.md` | L59 | schema-violation (count stale; also C-03) |
| FA-03 | `principles/tier-2-system/foundation-generic/` | (13 files) | live-flag (13 files but 12 principles + 1 `_index.md`; count is consistent at 12 principles) |

### §4.3 Part 11 — Strategic Direction Substrate (Pillar A)

**Architecture file:** `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` (exists)

**CLAUDE.md claim (L48):** Part 11 hosts «UC-A.1/A.2/A.3/A.4»

**Cross-ref check:** `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` — file exists (verified). `canonical/INDEX.md` §1 — lists FUNDAMENTAL correctly.

**Issue found:** `decisions/strategic/` referenced in CLAUDE.md L21 as «29 D-Lock entries + 4 insights + 7 templates; active Wave 1.4 pipeline, NOT moved». Not spot-verified in this pass (large tree). No blocking finding — marked as live-flag for completeness.

| Finding | File | Section | Type |
|---|---|---|---|
| FA-04 | `CLAUDE.md` | L21 | live-flag (decisions/strategic/ Wave 1.4 count unverified in this pass) |

---

## §5 API/Secret Scan Results

**Scan executed** via Grep tool across `decisions/`, `swarm/`, `reports/` for patterns: `ANTHROPIC_API_KEY`, `GROQ_API_KEY`, `OPENAI_API_KEY`, `sk-ant-`, `sk-proj-`, `gsk_`.

**Result: No actual key values found.**

All hits are one of three safe categories:
1. **Grep pattern strings in audit/test code** — `swarm/tests/part-a-smoke.sh:L134`, `swarm/tests/part-b-smoke.sh:L303`, `swarm/tests/part-f-verification.md:L103` — these are the grep commands themselves, not key values.
2. **Documentation noting keys are present in env but NOT used** — `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md:L216`: «Shell env shows `ANTHROPIC_API_KEY` / `GROQ_API_KEY` present at session start. brigadier did NOT invoke either» — observational note, not a key value.
3. **Audit trail references** — `swarm/wiki/tasks/`, `swarm/wiki/designs/`, `reports/` — all are grep pattern strings in documentation of key-audit procedures.

**One marginal finding:**

| # | File | Line | Issue | Severity |
|---|---|---|---|---|
| **A-01** | `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md` | L216 | Prose states env vars are present at session start; flags that SessionStart hook should unset them but is not installed. This is an architectural gap note, not key exposure. Suggests the hook-based unsetting per `shared-protocols §9` is not wired. | Low — informational only; no key value present |

**Scan verdict: CLEAN.** No API key values in `decisions/`, `swarm/`, `reports/` trees.

---

## §6 CLAUDE.md vs Filesystem Reality

### §6.1 Agent Roster Verification

CLAUDE.md §Agent Roster (L124-137) lists 12 agents across 6 departments.

**Filesystem reality** (`.claude/agents/*.md`): 23 files total.

| Status | Agent files | Count |
|---|---|---|
| In CLAUDE.md roster | manager, personal-assistant, system-admin, sales-lead, sales-researcher, sales-outreach, inbox-processor, crazy-agent, knowledge-synth, strategist, life-coach, meta-agent | 12 |
| NOT in CLAUDE.md roster (additional files) | staging-writer, sweep-worker, brigadier, engineering-expert, investor-expert, mgmt-expert, levenchuk-deep-dive-brigadier, quick-money-brigadier, philosophy-expert, project-brigadier, systems-expert | 11 |

**Findings:**

| # | Finding | Type | Suggested action |
|---|---|---|---|
| **R-01** | `staging-writer.md` and `sweep-worker.md` are in `.claude/agents/` but NOT in CLAUDE.md roster table | dead-link (roster incomplete) | Add to roster with Phase/status OR add footnote explaining these are infrastructure agents not domain experts |
| **R-02** | `brigadier.md` (ROY swarm orchestrator), `engineering-expert.md`, `investor-expert.md`, `mgmt-expert.md`, `philosophy-expert.md`, `systems-expert.md` (5 ROY experts) are in `.claude/agents/` but CLAUDE.md §Architecture says «12 specialized agents» without acknowledging the ROY swarm | contradiction (architecture section omits entire active swarm) | Add ROY swarm entry to Architecture section; or add note «+ ROY Phase-A research swarm (brigadier + 5 domain experts) per `agents/` directory» |
| **R-03** | `levenchuk-deep-dive-brigadier.md` and `quick-money-brigadier.md` are in `.claude/agents/` — project-specific brigadiers not in any roster | dead-link (unregistered agents) | Add to roster or document these as ephemeral project brigadiers under KM MVP section |
| **R-04** | `project-brigadier.md` is listed in CLAUDE.md §KM MVP L404 as a new agent template (correct), but NOT in the §Agent Roster table | inconsistency (mentioned in one section, absent from roster) | Add to roster with Phase = B+ or add footnote |
| **R-05** | CLAUDE.md §Agent Roster model column uses «Sonnet 4.6» / «Haiku 4.5» / «Opus 4.6» — these are executor-model assignments in direct violation of IP-1 (Foundation roles MUST NOT name executor instances; executor bindings = RUSLAN-LAYER per `shared/schemas/executor-binding.yaml.template`) | contradiction (IP-1 violation in CLAUDE.md) | Move model assignments out of CLAUDE.md roster table OR add explicit IP-1 disclaimer: «model values = RUSLAN-LAYER executor binding, not Foundation role-type property» |

### §6.2 Project Roster Verification

CLAUDE.md §Проекты (L312-323) declares 8 active projects: quick-money (P1), research (P2), brand (P2), community (P3), ai-tools (P2), life-os (P3), engineering-thinking (P3), bets (P4).

**Filesystem reality:**
- `shared/state/active-projects.json`: 1 project only (`quick-money`); `last_updated: 2026-04-14T00:00:00Z` (stale by ~33 days as of 2026-05-17)
- `swarm/wiki/projects/`: directory does NOT exist (glob returns nothing)

**Findings:**

| # | Finding | Type | Suggested action |
|---|---|---|---|
| **R-06** | `shared/state/active-projects.json` contains 1 project; CLAUDE.md declares 8 | contradiction (stale state; C-05 above) | Add disclaimer to CLAUDE.md projects section: «state JSON stale; single-project tracking only; 7 of 8 projects declared but not state-tracked» |
| **R-07** | `swarm/wiki/projects/` directory does not exist | dead-link (referenced by Task 1 §1 O-20 «0 files»; implicit in project lifecycle KM MVP design) | Suggest: create `swarm/wiki/projects/.gitkeep` stub OR add note in CLAUDE.md that project wiki scaffolding is Phase B materialization |
| **R-08** | CLAUDE.md §Проекты: projects `community` (P3 Planned) and `bets` (P4 Paused) are listed as «active» projects in the «8 активных» table header, but status column shows Planned/Paused — the header claim «активных» contradicts body status values | contradiction (CE-1 from Task 1 confirmed in CLAUDE.md) | Rename table header to «Project Roster (8 declared)» and add columns for tracking evidence link |

### §6.3 Foundation Parts Count Verification

CLAUDE.md §Foundation Architecture heading (L32): «10 LOCKED Foundation parts F5»

Body list (L34-44): Parts 1-10 = 10 entries PLUS Part 11 in «Strategic Layer Foundation extension» subsection directly below = 11 distinct Parts total. Filesystem glob confirms 12 architecture.md files (Parts 1-11 + Pillar C at `principles/architecture.md`).

| # | Finding | Type | Suggested action |
|---|---|---|---|
| **R-09** | Heading says «10» but 11 Parts exist (Part 11 Strategic Direction Substrate is LOCKED and in the same Foundation lock tag) | contradiction (C-02 above) | Update heading to «11 LOCKED Foundation parts F5» |
| **R-10** | Pillar C (`swarm/wiki/foundations/principles/architecture.md`) is listed separately in canonical/INDEX.md §3a as a 13th Foundation sub-system row but NOT in CLAUDE.md's «10 LOCKED Foundation parts» count — creating a cross-doc count inconsistency | contradiction (CLAUDE.md heading vs canonical/INDEX.md table) | CLAUDE.md should say «11 Foundation Parts + Pillar C sub-system» to match canonical/INDEX.md |

---

## §7 Dissents + Open Questions

### D-ENG-1 (scope of this audit)

- **Position (this critic pass):** Surfacing only filesystem-verifiable contradictions. Cross-document prose-level inconsistencies not verifiable via file reads (e.g. whether JETIX-TRM-MODEL-2026-04-30.md §4.2 «немецкий Mittelstand» example in financial projections contradicts ICP abandonment per ACTION-PLAN RES.1 — it does, but the TRM model is a separate LOCKED doc and the ICP only changed 2026-05-10; the sequence is expected, not a contradiction to be fixed by the critic).
- **Counter-position:** The TRM model's financial example section still assumes Mittelstand ICP. Any reader of the LOCKED TRM doc today would receive stale ICP guidance. This is a stale-cross-ref of consequence for L1 audience (Levenchuk / Tseren).
- **F:** F4 · **R:** refuted_if_TRM_model_carries_explicit_«ICP-section-stale-per-RES.1»_disclaimer

### D-ENG-2 (CLAUDE.md IP-1 violation severity)

- **Position (this critic):** CLAUDE.md §Agent Roster model column (L124-137) names executor models (Sonnet 4.6, Haiku 4.5, Opus 4.6) in direct violation of IP-1. Surfaced as R-05 above.
- **Counter-position:** CLAUDE.md is explicitly a «master configuration» and a «boot context» document — it may legitimately serve as the RUSLAN-LAYER binding document (per `shared/schemas/executor-binding.yaml.template`). The IP-1 prohibition is for «Foundation parts» not for CLAUDE.md itself. CLAUDE.md §Critical Tier-2 Principles says «Foundation roles = U.Episteme abstract role-types; executor bindings = RUSLAN-LAYER per executor-binding.yaml.template» — implying CLAUDE.md IS the RUSLAN-LAYER vehicle.
- **Engineer's position on dissent:** The violation is marginal given CLAUDE.md's dual role, but the roster table should carry an explicit IP-1 disclaimer to prevent downstream agents reading it as Foundation-authoritative role-type claims.
- **F:** F4 · **R:** refuted_if_CLAUDE.md_is_formally_classified_as_RUSLAN-LAYER_artefact_in_Foundation_Part_4_or_Pillar_C_canonical

### D-ENG-3 (JETIX-FPF.md line count inconsistency)

- **Position:** CLAUDE.md L71 says «3758 lines»; JETIX-WORKING-FILE-v0 line 22 says «3762-строчный». Discrepancy of 4 lines. The file is now archived — actual line count unverified in this pass.
- **Severity judgment:** Low (4 lines in an archived document). Not a blocking issue.
- **F:** F3 · **R:** refuted_if_wc-l archive/design/JETIX-FPF.md returns value matching one of the two claims

### D-ENG-4 (daily-log operational gap severity)

- **Position (this critic):** Part 9 architecture describes a complete daily-log operational schema. Zero instances exist. This should be flagged as STUB / Phase B materialisation, not as a functioning system.
- **Counter-position (from Task 1 §3 O-18):** «Part 9 monthly 'strategic reflection' cadence = spec only (`daily-log/` dir отсутствует)» — already flagged by mgmt-cell in Task 1. The finding is pre-existing and known.
- **Engineering position:** The fact that it's known does not reduce the cross-ref integrity issue; Part 9 architecture.md still claims operational status without a STUB disclaimer. The fix is cheap (add one line to Part 9 §I intro).
- **F:** F4 · **R:** refuted_if_Part_9_§I_intro_carries_explicit_«stub_Phase-B»_materialization_marker

---

## §8 Recommended Actions (surface-only)

Summary of unique action types. All actions are suggestions for Ruslan; none executed.

| Priority | Action | Scope | Effort |
|---|---|---|---|
| High | Update CLAUDE.md §Constitutional documents to mark `design/JETIX-FPF.md` as archived; correct path or remove | CLAUDE.md L71 | Small |
| High | Update CLAUDE.md §Constitutional documents to remove/correct `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` dead link | CLAUDE.md L73 | Small |
| High | Update CLAUDE.md §Constitutional documents `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` path to archive | CLAUDE.md L72 | Small |
| High | Update CLAUDE.md «10 LOCKED Foundation parts» heading to «11» | CLAUDE.md L32 | Small |
| High | Update CLAUDE.md «11 entries» default-deny-table count to «12» | CLAUDE.md L59 | Small |
| High | Reconcile `.claude/config/default-deny-table.yaml` comment (L5 says count==11) with field (L13 says 12) | `.claude/config/default-deny-table.yaml` | Small |
| Medium | Add CLAUDE.md §Agent Roster IP-1 disclaimer (model names = RUSLAN-LAYER, not Foundation role-type properties) | CLAUDE.md L124 | Small |
| Medium | Add ROY swarm acknowledgement to CLAUDE.md §Architecture section (brigadier + 5 domain experts) | CLAUDE.md L115-121 | Small |
| Medium | Correct JETIX-WORKING-FILE §3.2 TRM resource names to match LOCKED TRM-MODEL-2026-04-30.md canonical names | JETIX-WORKING-FILE-v0-2026-05-17.md §3.2 | Small |
| Medium | Add «Mittelstand ICP stale per RES.1» disclaimer to TRM model §4.2 financial example | decisions/JETIX-TRM-MODEL-2026-04-30.md §4.2 | Small (via git mv or annotation) |
| Medium | Fix `prose_authored_by` field in JETIX-WORKING-FILE frontmatter to use canonical value (`hybrid-with-ack-trail`) | JETIX-WORKING-FILE-v0-2026-05-17.md frontmatter | Small |
| Medium | Add STUB / Phase B materialisation disclaimer to Part 9 §I intro regarding daily-log operational status | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` §I | Small (requires AWAITING-APPROVAL gate — Foundation-level write) |
| Low | Update CLAUDE.md §CRM «per Global Rule 4» citation to «§4.2» | CLAUDE.md L263 | Trivial |
| Low | Create `swarm/wiki/projects/.gitkeep` stub to signal directory intent | filesystem | Trivial |
| Low | Update Task 1 §5 CE-1 note to specify «dir not found» rather than «0 files» for `swarm/wiki/projects/` | reports/phase-0-fpf-scope/01-jetix-objects-inventory.md §5 | Trivial |

---

## Provenance

| Source | Usage | Range |
|---|---|---|
| `CLAUDE.md` | Roster table (L124-137), Architecture section (L115-121), Constitutional docs (L70-73), Foundation heading (L32), default-deny count (L59), CRM rule ref (L263) | Multiple sections |
| `canonical/INDEX.md` | Foundation Parts table (§3a), Schemas (§3c) | L49-84 |
| `.claude/agents/*.md` (glob result) | Agent file count: 23 files actual | filesystem |
| `.claude/config/default-deny-table.yaml` | Full read | L1-153 |
| `shared/state/active-projects.json` | Full read | L1-18 |
| `comms/mailboxes/manager.jsonl` | Full read | L1-5 |
| `swarm/approvals/log.jsonl` | First 5 lines | L1-5 |
| `JETIX-WORKING-FILE-v0-2026-05-17.md` | §3.2 TRM resources, §5.1 Hexagon insights, §4 mermaid | L129-139, L229-235, L175-215 |
| `decisions/JETIX-TRM-MODEL-2026-04-30.md` | Resource class names | L27-32 |
| `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` | RES.1 Mittelstand abandonment | L43, L74-75 |
| `decisions/JETIX-CORPORATION-2026-05-05.md` | ICP Mittelstand references | L39, L67 |
| `decisions/AWAITING-APPROVAL-swarm-self-improve-gate1-2026-04-23.md` | API key env observation | L216 |
| `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | daily-log spec vs no instances | L72-73, L197, L235 |
| `swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-*` | Existence confirmed (9 files) | filesystem |
| `archive/design/JETIX-FPF.md` | Actual archive location vs CLAUDE.md claim | filesystem (glob) |
| `principles/tier-2-system/foundation-generic/` | File count: 13 (12 principles + _index.md) | filesystem (glob) |
| `reports/phase-0-fpf-scope/01-jetix-objects-inventory.md` | Task 1 inventory table §1 O-10, §5 CE-1 | L80-106, L287-291 |
| `reports/fpf-iwe-distillation-2026-05-17/` | Existence confirmed (28 files) | filesystem |

---

## Acceptance Predicate

`swarm/wiki/drafts/task-phase-0-fpf-scope-2026-05-17-engineering-critic-kasha-cleanup.md` passes when: ≥20 concrete contradictions/dead-links/schema issues surfaced with file:line citations (this draft: 31 items) AND API/secret scan run+reported (§5: clean) AND CLAUDE.md vs filesystem reality verified (§6: R-01..R-10) AND ≥3 dissents preserved (§7: D-ENG-1..D-ENG-4) AND no modifications made to any source file (R1: preserved).

---

*Engineering-expert × critic. Compound step: append strategies.md entry `critic-cross-doc-dead-link-audit` at next brigadier Compound dispatch. No peer-expert dispatch required for this pass — all findings within engineering critic scope.*
