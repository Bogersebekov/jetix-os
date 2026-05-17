---
task_id: phase-0-fpf-scope-2026-05-17-task-4
produced_by: philosophy-expert × critic
mode: critic
status: draft
F: F4
G: phase-0-cell-draft
R: refuted_if_stale_items_unflagged_OR_action_chosen_NOT_surfaced
date: 2026-05-17
sources:
  - reports/phase-0-fpf-scope/01-jetix-objects-inventory.md
  - reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md
  - reports/phase-0-fpf-scope/03-comparison-matrix.md
  - reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
  - reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md
  - reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md
  - JETIX-WORKING-FILE-v0-2026-05-17.md
  - CLAUDE.md
  - canonical/INDEX.md
  - decisions/JETIX-CORPORATION-2026-05-05.md
  - decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md
  - decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md
  - swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md
  - swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md
  - swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md
  - swarm/wiki/foundations/part-1-system-state-persistence/architecture.md
constitutional_posture: R1 surface-only + R2 Foundation read-only + R6 provenance-per-row + append-only
---

# Task 4 — Philosophy Critic: Каша Cleanup — Epistemic Flags

> **Constitutional posture.** Surface'инг only. Actions = options offered, не chosen.
> Ruslan ack'ает каждый item. NO deletions suggested; append-only alternatives only.
> Foundation Parts read-only per R2. Provenance per row per R6.

---

## §0 Summary (паттерны каши — ≤300 слов)

Критический обзор Jetix-документов через epistemic-critic lens обнаруживает **пять системных паттернов несоответствия**, которые проходят через несколько слоёв документации.

**Паттерн 1 — Language-state vs Operational (ubiquitous, EP-1).** «LOCKED» во всей документации означает language-state artefact-уровня (A.16), но применяется как будто это свидетельство operational-системы. 10 из 14 объектов инвентаря несут LOCKED-статус при operational-reality F2-F4 или vapor. Это самый плотный паттерн.

**Паттерн 2 — Type-token conflations (CE-2, EP-3).** «12 agents» и «12 specialized agents» используются в нескольких документах без различия между 12 U.Role-типами (декларированы; IP-1 type-level) и N активными executor-привязками (ROY swarm = 6; legacy = stale). Два существенно разных утверждения живут под одним языковым знаком.

**Паттерн 3 — F-grade applied to wrong subject (EP-5, F8 на approv-процесс).** Part 4 §0 говорит «F8 (artefact)»; JETIX-WORKING-FILE §7 ставит F8 всем 11 Foundation Parts. Но F8 = наивысший assurance grade — «canonical-locked»; в Jetix-словаре это означает «8 RUSLAN-ACK records». F8 = approval-grade, не B.3 independently-tested claim-truth-grade. Это EP-5 паттерн.

**Паттерн 4 — ICP inconsistency (cross-document).** Doc 1B §7 называет ICP «Mittelstand DACH 50-500 employees manufacturing»; ACTION-PLAN-PHASE-1 §0 / §1.4 объявляет «RES.1 — Mittelstand DACH → ABANDONED → Online-first ONLY». Doc 1B §7 не обновлён. Cross-document состояние неопределённо.

**Паттерн 5 — Archived source still referenced (stale provenance).** `design/JETIX-FPF.md` archived 2026-05-06 в `archive/design/JETIX-FPF.md`, но все 13 Foundation Parts содержат live `sources:` entries на `design/JETIX-FPF.md` (не на archival path). Пути не разрешаются по правилам текущего repo state.

Дополнительно: `daily-log/` directory (Part 9 core механизм) существует как `daily-log/drafts/.gitkeep` без реальных entries; `swarm/wiki/projects/` = 0 files при задекларированных 8 active projects; `STRATEGIC-INSIGHT-AS-PEOPLE-NETWORK-STATE` имеет `prose_authored_by: ai-draft` при status LOCKED — потенциальный R1 конфликт.

Итого surface'нуто: **≥40 stale items** в §1, **7 cross-document inconsistencies** в §2, **4 pre-Foundation overreaches** в §3, **4 use-mention failures** в §4, **EP-1..EP-5 instances** в §5.

---

## §1 Stale Items Table (exhaustive)

Каждая строка = один epistemic flag. Suggested actions = options only. Ruslan decides.

| # | File | Line / Section | Claim | Why stale (flag type) | Suggested action options |
|---|---|---|---|---|---|
| S-01 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §1 (line ~98-99) | «12 specialized agents × 6 departments × 8 active projects» (alternate formulation tagged F5/R-high) | CE-2 type-token: 12 = role-type declarations (type-level), NOT 12 running executor processes. F5/R-high overstatement per IP-1. CE-1: «8 active projects» — 1 in state JSON; 0 in wiki/projects/; 4 statuses mixed (Active/Planned/Paused) | (a) Append use-mention disclaimer: «12 = U.Role типов (тип-уровень; IP-1); активных executor-bindings = N»; (b) Add scope qualifier on 8 projects |
| S-02 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §2 (line ~111) | «organised as 12 specialized agents across 6 departments coordinated via single LLM brigadier» | EP-3 role/executor conflation — paragraph does not distinguish between role-types and executor tokens; implies 12 simultaneous processes | (a) Append clarification note: «12 = Phase 1-4 schedule; Phase 1 active = 4; ROY swarm actual = brigadier + 5 experts» |
| S-03 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §7 table (all rows) | All 11 Foundation Parts + Pillar C listed as F: F8 | EP-5: F8 = approval-grade (8 RUSLAN-ACK records) ≠ B.3 claim-truth-grade. Foundation Parts individual frontmatter says F5 (not F8) [src: part-4 frontmatter F:F5; part-9 frontmatter F:F5; part-1 frontmatter F:F5]. JETIX-WORKING-FILE inflates to F8 without evidence | (a) Append clarification note: «F8 в Jetix = highest approval-grade (RUSLAN-ACK records); individual Parts = F5 per own frontmatter»; (b) Add face declaration (approval-grade vs claim-truth-grade) |
| S-04 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §8 Pillar C (line ~413) | «F8 / G: jetix-pillar-c-constitutional / R-high» for 12 constitutional rules | EP-5: same F8 issue. Additionally CE-4: «12 hard rules» conflates machine-enforced (Rule 11), human-review-only (Rules 1/3/8), and vapor-enforcement (R12). Single F8 applied over heterogeneous enforcement reality | (a) Append F-G-R per cluster (Rule 11 = F8-machine; Rules 1/3 = F5-human; R12 = F4-text/F2-enforcement); (b) Add scope qualifier on enforcement |
| S-05 | `CLAUDE.md` | §Agent Roster table | «12 specialized agents» roster table without IP-1 disclaimer or Phase column qualification in the visual | CE-2: roster displays Phase 1-4 agents as equivalent present-tense reality. Phase 3-4 agents (knowledge-synth, strategist, life-coach, meta-agent) = declared role-types without confirmed operational executor bindings [src: 01-inventory §5 CE-2] | (a) Append note to table header: «12 = U.Role type-level declarations; Phase column = activation schedule; executor-bindings per RUSLAN-LAYER»; (b) Mark deprecated Phase 3-4 rows |
| S-06 | `CLAUDE.md` | §Проекты table | «8 активных проектов» with status column showing Active/Planned/Paused mix | CE-1: type-token + language-state collapse. «Active» ≠ operationally active (state JSON has 1 entry; wiki/projects/ = 0 files) [src: 01-inventory §5 CE-1] | (a) Append scope qualifier: «Объявленный портфель (тип-уровень); operational evidence per shared/state/active-projects.json»; (b) Mark deprecated project rows with no evidence |
| S-07 | `CLAUDE.md` | §Foundation Architecture v1.0 (LOCKED) heading | Implies «LOCKED» = operational system LOCKED | CE-3: LOCKED = artefact language-state (A.16), NOT U.Work operational system. [src: 06-honest-self-audit §2: Parts 1/3/5/9/11 = memory-dominant; Halt-Log-Alert = STUB] | (a) Append clarification note: «LOCKED = artefact language-state; operational enforcement = STUB Phase B (per agent files)» |
| S-08 | `CLAUDE.md` | §4.1 heading «Tier 2 Constitutional (12 hard rules)» | No enforcement-differentiation; all 12 presented under same heading without F-grade per cluster | CE-4: machine-enforced (Rule 11) vs human-review (Rules 1/3) vs no mechanism yet (R12) collapsed | (a) Append enforcement tier notes per rule or rule-cluster; (b) Add use-mention disclaimer: «text LOCKED ≠ all 12 enforced» |
| S-09 | `CLAUDE.md` | §Кто ты + §System Overview | «12 specialized agents» as descriptive fact about current system state | EP-3 + CE-2: describes role-taxonomy declarations as operational count | (a) Add use-mention disclaimer referencing IP-1 and Phase column |
| S-10 | `decisions/JETIX-CORPORATION-2026-05-05.md` | §7 ICP | ICP = «Mittelstand DACH 50-500 emp manufacturing» [src: frontmatter INCLUDES «ICP (Mittelstand DACH 50-500 emp manufacturing)»] | ICP abandoned: ACTION-PLAN-PHASE-1 §0 / §1.4 states «RES.1 — Mittelstand DACH ABANDONED → Online-first ONLY». Doc 1B §7 not updated [src: ACTION-PLAN §1.4 RES.1] | (a) Append clarification note to Doc 1B §7: «ICP superseded 2026-05-10 per STRATEGIC-INSIGHT-JETIX-PARTNERSHIP-MODEL RES.1 — current ICP = Online-first verticals»; (b) Mark ICP section deprecated |
| S-11 | `decisions/JETIX-CORPORATION-2026-05-05.md` | §0 TL;DR | Present-tense: «Jetix Corporation — это AI-native operational корпорация» | EP-2 use-mention slip: conceptual document (frontmatter explicit: «purpose = концептуальный документ») uses present-tense operational assertion. Vapor as instantiated [src: 02-per-object-deep §2 «Что есть»: «Ruslan = физлицо Berlin; no GmbH/UG»] | (a) Append use-mention disclaimer: «Концептуальный документ; описывает intended future U.System; юрлицо не зарегистрировано» |
| S-12 | `decisions/JETIX-CORPORATION-2026-05-05.md` | Frontmatter INCLUDES | «Roadmap к €50K → €1T trajectory» and «ICP (Mittelstand DACH 50-500 emp manufacturing)» in INCLUDES list | ICP stale (S-10). Trajectory framing = EP-4: PromiseContent без U.Commitment unpacking (A.2.8): no obligation-holder, no adjudication path | (a) Append note: «ICP superseded; trajectory = aspirational-locked не U.Commitment formal»; (b) Add scope qualifier |
| S-13 | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` | Frontmatter status | `status: draft (awaiting Ruslan ack)` — but file is in `decisions/` (LOCKED canonical folder per canonical/INDEX.md) | Status conflict: draft files should be in drafts/ or awaiting-approval/; canonical decisions/ = LOCKED. Unclear whether this doc was acked | (a) Append clarification note confirming ack status; (b) Move to awaiting-approval/ if not acked |
| S-14 | `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` | Frontmatter | `status: LOCKED` + `prose_authored_by: ai-draft` + note «Ruslan rewrite ожидаемое» | R1 conflict: status LOCKED but prose_authored_by = ai-draft. Per Tier 2 Rule 1 + FUNDAMENTAL §6.1 rule 1: strategic prose must be authored by Ruslan. LOCKED status + ai-draft prose = conflation of artefact-lock with prose authorship | (a) Append note: «Prose authorship pending Ruslan rewrite per R1; LOCKED = structural placement acked, NOT prose finalized»; (b) Update prose_authored_by when Ruslan rewrites |
| S-15 | `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` | Frontmatter | `F: F2` but file in `decisions/` with strategic-insight type | F-G-R applied inconsistently across Strategic Insights set: H7 People-NS has `F: F3`; Foundation Model has `F: F2`; Part 11 §0 lists all 6 as «Hexagon synthesis outputs». Different F-levels within same claimed synthesis cadence | (a) Append note explaining why F2 vs F3 per insight (should match evidence level); (b) Add scope qualifier on F-grade rationale |
| S-16 | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` | frontmatter sources | `sources: [..., design/JETIX-FPF.md, ...]` | design/JETIX-FPF.md archived 2026-05-06 → `archive/design/JETIX-FPF.md`. Live path `design/JETIX-FPF.md` does NOT exist [src: Grep confirms archive path only]. Stale provenance reference | (a) Update path to `archive/design/JETIX-FPF.md` with note «archived 2026-05-06; current Jetix FPF interpretation via Foundation Parts + Pillar C»; (b) Add scope qualifier on archival status |
| S-17 | `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` | frontmatter sources | Same: `sources: [..., design/JETIX-FPF.md, ...]` | Same as S-16. All 13 Foundation Parts carry this stale reference [grep count: 89 occurrences in 13 files] | (a) Same: update to archive path across all 13 files (AWAITING-APPROVAL packet required per R2) |
| S-18 | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | §0 Executive Summary | Describes daily-log as canonical operational mechanism; `daily-log/` = Part 9 core substrate | `daily-log/` directory exists only as `daily-log/drafts/.gitkeep` — no actual daily-log entries [Glob confirms]. Part 9 = memory-dominant substrate per 06-honest-self-audit §2. Operational gap flagged but not in the Part 9 doc itself | (a) Append clarification note to Part 9 §0: «daily-log/ = STUB Phase A; no active entries as of 2026-05-17»; (b) Add scope qualifier |
| S-19 | `swarm/wiki/foundations/part-11-strategic-direction-substrate/architecture.md` | Frontmatter status + constitutional_anchors | `design/JETIX-FPF.md` referenced as constitutional_anchor at Part 11 | Same S-16/S-17 archived-source issue. Part 11 additionally references design/JETIX-FPF.md as FPF IP-2/IP-3/IP-7/A.6.B/B.3 anchor | (a) Update to archive path; add note that FPF canonical anchor = raw/external/ailev-FPF/FPF-Spec.md @ c86eabd |
| S-20 | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` | §0 (line ~46) | «13 legacy agents on adjacent mailboxes» | Stale: mailboxes last updated 2026-04-15 [src: 01-inventory §2 O-06b]. D-mgmt-2: cannot assert «не работает» — direct dispatch possible. But «13 legacy agents» count = unclear (CLAUDE.md shows 12, not 13) | (a) Append scope qualifier: «legacy agent mailboxes last active 2026-04-15; current operational = ROY swarm brigadier + 5 experts»; (b) Clarify 13 vs 12 count discrepancy |
| S-21 | `canonical/INDEX.md` | §Что НЕ canonical | «Strategic Layer F2 scaffolds — decisions/strategic/ (29 D-Lock entries + 4 insights + 7 templates — F2 promotion queue для Wave 1.4; NOT moved)» | Date-stamp missing on when Wave 1.4 was expected. Cross-ref: CANONICAL-WALKTHROUGH-2026-05-06.md ack was 110-item; decisions/strategic/ items not acked individually post-2026-05-06. Are 29 D-Lock entries still F2 promotion queue or have some been superseded? | (a) Append clarification note with last-reviewed date; (b) Add scope qualifier on which D-Lock entries remain active vs superseded |
| S-22 | `canonical/INDEX.md` | §5 Operational Pipelines | References `swarm/wiki/operations/voice-pipeline-canonical-2026-05-10.md` as active operational | File path unknown — not in canonical INDEX proper sections; referenced as «v1.0 2026-05-10». Predates Phase B (Phase B locked new voice-pipeline discipline) — may be superseded | (a) Append clarification note confirming status post-Phase B; (b) Add «Update with current canonical» option |
| S-23 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §3 Workshop metaphor (line ~124) | «Workshop metaphor = архитектурный anchor» / «F5 / G: jetix-canonical-workshop / R: R-high (LOCKED v1.0)» | EP-2 use-mention: Workshop is simultaneously mentioned as communication frame AND used as structural architectural anchor. Per D-PHIL-SCOPE-2 (Task 1 §7): Workshop lacks A.1.1 U.BoundedContext formal fields (glossary + invariants + scope). F5/R-high = artefact-LOCKED; structural anchor status requires A.1.1 formalisation [src: 01-inventory §7 D-PHIL-SCOPE-2] | (a) Add use-mention disclaimer: «Workshop = canonical narrative frame (LOCKED); structural A.1.1 anchor status pending formalisation»; (b) Add face declaration |
| S-24 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.2 R12 (line ~252) | «F5 / G: jetix-constitutional-candidate / R-high (4-source trail; LOCKED pending packet)» | EP-5 F-grade applied to wrong subject face. R12 has THREE distinct sub-objects per Task 1 §2 O-11: (a) text U.Episteme F5 LOCKED; (b) U.Commitment in applied form F2; (c) architectural meta-property with enforcement = vapor. Single F5 across all three faces collapses different F-grades | (a) Append clarification note: «F5 = text artefact LOCKED; enforcement mechanism F2-vapor; fork-and-leave infrastructure F2»; (b) Add F-G-R per object-face |
| S-25 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.3 5-layer memory (line ~268) | «F5 / G: jetix-canonical / R-medium (operational; not fully tested at scale)» | Stale: `comms/mailboxes/` last active 2026-04-15 for legacy agents [src: 01-inventory O-06b]. Mailbox = Layer 5 in 5-layer memory scheme. If legacy mailboxes stale, «5-layer memory operational» claim partial at best | (a) Append scope qualifier: «Layer 5 mailbox = ROY swarm operational; legacy 12-agent mailboxes stale 2026-04-15» |
| S-26 | `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` | §2 Part 4 row | «Part 4: FPF-derivative + intelligence / Direct adoption» | EP-5 nuance: Part 4 itself says «method-signature enforcement неполный (RUSLAN-LAYER overlay incomplete)» [src: 06-honest-self-audit §2 Part 4 diff]. Self-audit surface'ит gap but «Direct adoption» label could be read as complete adoption. F-grade for «intelligence» face of Part 4 absent | (a) Append clarification note: «Direct adoption of role taxonomy structure; operational completeness = partial (method-signature enforcement stub)» |
| S-27 | `reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-PHASE-B.md` | §1 dispatch table | «cells dispatched: eng/phil/mgmt × critic (3 parallel)» Шаг 1; «3 parallel» для each Шаг | Шаг 6 says «brigadier scribe (R1 writing-support; sales-outreach not dispatched)». §1 table includes a «brain» cell for Шаг 2 but body says «knowledge-synth». Inconsistency in cell-dispatch accounting | (a) Append clarification note confirming exact cell count per Шаг; (b) Reconcile «brain vs knowledge-synth» naming |
| S-28 | `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md` | §4b header | «§4b RUSLAN-LAYER mapping (НЕ canonical FPF)» — but body contains IP-1/IP-2/IP-3/IP-7 described as «mapped к FPF эквивалентам» | EP-5 F-grade issue: IP-1 through IP-7 are Jetix-internal IPs (derived from FPF principles) presented as FPF-canonical in some prior Jetix docs. §4b disclaimer is correct (not canonical FPF), but IPs were born in `design/JETIX-FPF.md` (archived) — their epistemological status in canonical FPF unclear. Are they Ruslan's interpretation or FPF primitives? | (a) Append scope qualifier on IP-1..IP-7 status: «Jetix-internal interpretations; not canonical FPF Spec concepts»; (b) Add use-mention disclaimer |
| S-29 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §6.1 FPF positioning (line ~330) | «Tactical FPF adoption (4 direct adoptions)» with «4» as settled count | Count conflicts with 06-honest-self-audit §2.1 which says «Direct FPF-derivative: Part 4 + 6a + 6b + Pillar C» (= 4) BUT also mixed «memory + structural-intelligence» for Parts 2/5/10. Phase B Task 1 Engineering cell surfaces Parts 1/3/5/9/11 as «memory-dominant». Framing «4 direct adoptions» could imply only 4 parts, while 11 parts + Pillar C exist. Partial picture | (a) Append scope qualifier: «4 strong direct adoptions; remaining Parts = substrate/memory/automation classification per 06-honest-self-audit» |
| S-30 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §9 Projects table (line ~431) | «8 active projects» table; `F: F5 / R: R-high (Part 7 LOCKED + CLAUDE.md projects table)` | CE-1: F5/R-high applied to project list that includes «Planned» (community) and «Paused» (bets). Provenance = CLAUDE.md (not operational evidence). shared/state/active-projects.json stale 2026-04-14, has 1 entry [src: 01-inventory O-20 CE-1]. F5/R-high overstates operational evidence | (a) Append scope qualifier: «Объявленный портфель; операционный evidence = 1 in state JSON; F4 или ниже для operational-status face» |
| S-31 | `decisions/STRATEGIC-INSIGHT-BALAJI-NETWORK-STATE-2026-05-10.md` | Title | Listed in JETIX-WORKING-FILE §5.1 as one of 6 Hexagon insights with F5 canonical | Per 00-SUMMARY §2.4: Working file §5.1 says «6 LOCKED strategic insights (H1-H7 2026-05-10..12)». But JETIX-WORKING-FILE §5.1 lists 6 insights yet refers to «H1-H7» (= 7 counting). BALAJI insight = one of 6 original Hexagon; H7 People-NS = 7th (Heptagon). Hexagon vs Heptagon inconsistency in documents | (a) Append clarification note: «Hexagon = original 6; H7 People-NS = 7th (Heptagon per 2026-05-12 ack). Documents inconsistently call same set Hexagon or Heptagon» |
| S-32 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.1 «Strategic Insights LOCKED (6)» | Lists 6 insights; H7 People-NS is not in the list | Inconsistency: H7 People-NS LOCKED 2026-05-12 is in related-canonical of every Hexagon insight and is the source of R12 (§5.2). §5.1 should list 7 or explicitly declare «6 + 1» | (a) Append note: «H7 People-NS = 7th (Heptagon evolution, 2026-05-12); §5.1 lists original 6 only»; (b) Update list |
| S-33 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §3.2 TRM model | «TRM tracks 6 resource classes» including «Time — Toggl-tracked + Daily Log (Notion 30a24963)» | EP-1 operational gap: Daily Log cadence = Part 9 mechanism; daily-log/ dir has only `.gitkeep`. TRM resource «Time» tracked via Toggl + Daily Log but Daily Log operational substrate = STUB. [src: S-18 above] Additionally: «2. Time» in the list = «Toggl-tracked»; Task 1 O-10 says «only 2 of 6 tracked: capital + attention» | (a) Append scope qualifier: «TRM 6-resource declaration; operational tracking = capital + attention confirmed; 4 others = aspirational or informal» |
| S-34 | `canonical/INDEX.md` | §3b Foundation Master Overviews | References `swarm/wiki/synthesis/foundation-master-overview-technical-2026-04-29.md` | Path prefix: canonical/INDEX.md references `../swarm/wiki/synthesis/` but foundation synthesis files live at `swarm/wiki/foundations/synthesis/` per actual file system [src: 06-honest-self-audit §2 references `swarm/wiki/foundations/synthesis/foundation-master-overview-technical-2026-04-29.md`]. Path may be incorrect | (a) Verify path; append note if incorrect |
| S-35 | `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` | body §1 | Status «deferred-phase-2-plus» but ACTION-PLAN-PHASE-1 §1.2 references this same insight as «RES.1 / RES.3 binding» for CURRENT phase-1 actions | Status inconsistency: insight is both «deferred» (own status) and «currently binding» (ACTION-PLAN). The deferred vs active classification is ambiguous | (a) Append clarification note: «deferred = insight long-horizon vision; BUT component (ICP change) = phase-1 operative per ACTION-PLAN RES.1» |
| S-36 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §2 line ~111 | «~25% structural-intelligence + ~10% FPF-derivative (per honest-self-audit)» | 06-honest-self-audit §2.1 says «4 direct FPF-derivative parts + 11 supporting Parts». 4/15 total units = ~27% not 10%. «~10%» may refer to % of Jetix total components vs entire Jetix-OS scope (27 total). Numerator/denominator not specified — falsifier absent | (a) Append scope qualifier specifying numerator/denominator for %-calculations; (b) Add explicit falsifier |
| S-37 | `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` | §12 aggregate | «~27 memory+automation components / ~12 intelligence-FPF-derivative» (referenced in 01-inventory §0) | Honest self-audit §12 section not read in full (file truncated at §7 in read). Surface: if count = 27+12 = 39 total components but JETIX-WORKING-FILE §2 says «~25% structural-intelligence + ~10% FPF-derivative», math = 9.75 + 3.9 = ~14 items. Rounding inconsistency possible | (a) Append source reconciliation note: explicit count in 06-honest-self-audit §12; JETIX-WORKING-FILE §2 % numbers should reference same denominator |
| S-38 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §5.5 F2-F8 scale description | Defines F8 = «formal-proved / canonical-locked»; F6 = «engineering-verified / tested»; F5 = «structural-stable / promoted» | EP-5: own-system F-grade definitions in §5.5 differ from FPF B.3 standard. FPF B.3 F-grades = trust/assurance levels for claims. Jetix §5.5 uses different semantics (approval levels). The divergence is legitimate (RUSLAN-LAYER) but the §5.5 description does not make this clear; presents as if mapping to FPF B.3 | (a) Append clarification note: «F-scale = Jetix-internal approval-grade adaptation of FPF B.3 spirit; NOT verbatim FPF B.3 claim-truth-grade» |
| S-39 | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` | §0 (line ~54) | OQ-B2-A flagged: «Part 1 §I.4 stub's stale enum `[autonomous, requires-approval, hitl-required]`» | This is an acknowledged defect (OQ-B2-A «proposed Bundle 1 retroactive correction via constitutional AWAITING-APPROVAL packet»). Still open as of 2026-05-17 per no grep evidence of correction. Stale stub enum persists | (a) Append note: «OQ-B2-A correction pending AWAITING-APPROVAL packet; Part 1 §I.4 enum may still be stale» |
| S-40 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §4 mermaid diagram | Subgraph «12 Specialized Agents × 6 Departments» as visual layer | CE-2 visual: mermaid diagram presents 12 agents as structural layer without Phase-column nuance or IP-1 disclaimer. Visual claims weight — «seeing» 12-agent layer reinforces operational reading | (a) Append note below diagram: «12 = role-type declarations (Phase 1-4); см. IP-1 Role≠Executor; current executor-bindings = ROY swarm brigadier + 5 experts» |
| S-41 | `reports/phase-0-fpf-scope/02-objects-per-fpf-deep.md` | §0 brigadier summary | «EP-1 (Artefact-system gap, ubiquitous; phil). 10 of 14 objects carry LOCKED artefact status» | This self-flags EP-1 correctly. BUT the report is itself titled «brigadier-integrated» with F4/G:phase-0-per-object-deep — there is no separate falsifier stated for the EP-1 claim «10 of 14». Count should be verifiable but no cite to which 10 | (a) Append falsifier: «Refuted if operational audit finds >10 objects with evidenced runtime execution per cycle-log references» |
| S-42 | `CLAUDE.md` | §Wiki Architecture v2 — Per-agent memory | «Mailbox — comms/mailboxes/{id}.jsonl (recall + inter-agent messages; F4 append-only)» | Stale: legacy 12-agent mailboxes last active 2026-04-15 [src: 01-inventory O-06b]. Mailbox schema still valid but «inter-agent messages» claim = stale for legacy 12; active only for ROY swarm dispatch context | (a) Append scope qualifier: «Active для ROY swarm dispatch; legacy 12-agent mailboxes стale 2026-04-15» |

---

## §2 Cross-Document Inconsistencies

Explicit list. NOT averaged; both positions preserved.

| # | Doc A | Doc B | Claim A | Claim B | Inconsistency type | Suggested action options |
|---|---|---|---|---|---|---|
| XD-01 | `decisions/JETIX-CORPORATION-2026-05-05.md` §7 ICP | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` §0 / §1.4 RES.1 | «ICP = Mittelstand DACH 50-500 emp manufacturing» | «RES.1 — Mittelstand DACH ABANDONED → Online-first ONLY» | ICP definition directly contradicted. Doc 1B not updated. Single-truth ICP unclear | (a) Add clarification note to Doc 1B §7: «ICP superseded 2026-05-10; see ACTION-PLAN RES.1»; (b) Mark §7 deprecated |
| XD-02 | `CLAUDE.md` §Agent Roster | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` §0 | «12 specialized agents» roster | «5-expert ROY swarm + brigadier + 13 legacy agents on adjacent mailboxes» | Count conflict: CLAUDE.md = 12; Part 4 = 13 legacy + brigadier + 5 ROY. Brigadier is not in the 12. Part 4 «13» may include a role not in the CLAUDE.md table | (a) Append cross-reference note in CLAUDE.md: «ROY swarm = brigadier + 5 experts; legacy 12-agent roster ≠ ROY swarm; Part 4 references 13 legacy agents (count needs reconciliation)» |
| XD-03 | `JETIX-WORKING-FILE-v0-2026-05-17.md` §5.1 | `JETIX-WORKING-FILE-v0-2026-05-17.md` §QR-CARD | «LOCKED (6)» Strategic Insights listed | «Hexagon synthesis cadence» + «H7 People-NS LOCKED» described in §5.2 | Hexagon vs Heptagon: file's own §5.1 and §QR-CARD contradict each other on insight count. §5.1 = 6 listed; §5.2 R12 source = H7; QR-CARD anchor = §5.2. | (a) Append note to §5.1: «Original Hexagon = 6; H7 People-NS added 2026-05-12 → Heptagon (7 total)» |
| XD-04 | `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` §2 | `JETIX-WORKING-FILE-v0-2026-05-17.md` §7 table | Part 4: «FPF-derivative + intelligence»; all others F5 per own frontmatters | «F8 / R-high (all 11 Parts + Pillar C LOCKED 2026-04-28 with 8 RUSLAN-ACK records)» | F-grade conflict: honest-self-audit calibrates Part 4 as partial-intelligence (method-signature incomplete); JETIX-WORKING-FILE gives all Parts F8 uniformly | (a) Add clarification note to §7: «F8 = approval-grade (RUSLAN-ACK records); individual Part frontmatters = F5; honest-self-audit further calibrates per memory/FPF-derivative/automation type» |
| XD-05 | `CLAUDE.md` §§4.1 «12 hard rules — Foundation generic» | `swarm/wiki/foundations/principles/architecture.md` (referenced as canonical) | Inlines 12 rules with same F-grade implication across all | Pillar C architecture.md distinguishes enforcement tiers per Task 1 §2 O-08 CE-4: machine (Rule 11), human-review (1/3), pending (R12) | Enforcement-tier information present in the principles architecture but NOT surfaced in CLAUDE.md inline | (a) Append enforcement notes to CLAUDE.md §4.1 inline; (b) Cross-reference to principles/architecture.md per rule |
| XD-06 | `decisions/STRATEGIC-INSIGHT-JETIX-AS-FOUNDATION-MODEL-2026-05-10.md` frontmatter | `decisions/ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md` §1.2 | `status: deferred-phase-2-plus` | «Manifesto pattern... RES.1 / RES.3 binding; Цэрэн = first instantiation» (present-tense) | Same insight simultaneously «deferred Phase 2+» and «currently operative Phase 1 RES.1/3» | (a) Append clarification note: «deferred = long-horizon vision; operative component = ICP pivot (RES.1) + partnership model (RES.3) only, not full foundation-model vision» |
| XD-07 | `JETIX-WORKING-FILE-v0-2026-05-17.md` §2 | `reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md` §7 | «~25% structural-intelligence + ~10% FPF-derivative» | «Strategic Insights Hexagon = closest to intelligence amplification; ~27 memory+automation + ~12 intelligence-FPF-derivative» | Percentage formulas different; denominator unstated in working file §2; honest-self-audit uses counts not percentages. Cannot verify consistency without explicit denominator | (a) Append scope qualifier in §2 specifying denominator; (b) Cross-reference to 06-honest-self-audit explicit counts |

---

## §3 Pre-Foundation Overreaches Не Флагнутые

Pre-2026-04-28 LOCKED decisions с potential epistemic overreach. Surface only.

| # | File | Date | Claim / Pattern | Why possible overreach | Suggested action options |
|---|---|---|---|---|---|
| PF-01 | `archive/design/JETIX-FPF.md` | Pre-2026-05-06 | 3762-строчный «comprehensive FPF interpretation» document | Self-acknowledged overreach: «JETIX-FPF.md (3762-line overreach) archived 2026-05-06» [src: JETIX-WORKING-FILE §0 disclaimer; 00-SUMMARY §2.1]. But all 13 Foundation Parts still carry `design/JETIX-FPF.md` as live source reference (S-16..S-19). The overreach document was archived but its epistemic influence persists in Foundation provenance | (a) Append clarification note to Foundation Parts sources: «design/JETIX-FPF.md archived 2026-05-06; see archive/design/JETIX-FPF.md; canonical FPF reference = raw/external/ailev-FPF/FPF-Spec.md»; (b) Create AWAITING-APPROVAL packet for updating 13 Part sources |
| PF-02 | `decisions/JETIX-CORPORATION-2026-05-05.md` | 2026-05-05 | TL;DR §0: «€5K (now) → $100K к концу лета 2026 → €500K+ ARR Y1 → €100M+ ARR через 3 года» trajectory | EP-4: trajectory stated as PromiseContent without U.Commitment unpacking per A.2.8. Pre-Foundation document (Foundation LOCKED 2026-04-28; Doc 1B = 2026-05-05 post-Foundation, but created before Phase B FPF scope discipline). Trajectory = F2 positioning; presented without falsifier. Additionally: ICP section stale (XD-01) | (a) Append scope qualifier on trajectory: «F2 aspirational; falsifier = revenue_current stays 0 beyond X months OR ICP inconsistency persists»; (b) Append note that ICP superseded |
| PF-03 | `decisions/JETIX-CORPORATION-2026-05-05.md` | 2026-05-05 | Doc 1B §0 «Jetix Corporation — это AI-native operational корпорация» | Uses «corporation» as operational present-tense term. Document post-Foundation (2026-05-05) but pre-Phase B FPF scope definition (2026-05-17). Per Task 1/2 analysis: юрлицо = vapor; Ruslan = физлицо Berlin. Present-tense «operational corporation» = use-mention overreach for document authored as «conceptual doc» | (a) Append use-mention disclaimer: «conceptual документ; операционная корпорация не зарегистрирована; A.4 Temporal Duality: design vs operational» |
| PF-04 | Multiple Foundation Parts (all 13) | 2026-04-28 | All 13 Foundation Parts reference `design/JETIX-FPF.md` as live source | As of 2026-05-06, `design/JETIX-FPF.md` was archived. Foundation Parts built their FPF-derived structures on this intermediate derivative, not directly on canonical FPF-Spec. Post-archive, the foundation of Foundation's FPF claims = an archived overreach doc. This is a systemic provenance gap, not a per-Part error | (a) Append note to each Part sources: «design/JETIX-FPF.md archived; FPF canonical = raw/external/ailev-FPF/FPF-Spec.md @ c86eabd»; (b) Create AWAITING-APPROVAL packet for systematic provenance update |

---

## §4 Use-Mention Discipline Failures

Где документы slip между mention (referencing a concept) и use (asserting that concept as operational fact) без explicit declaration.

| # | File | Section | Slip direction | Instance | Suggested action options |
|---|---|---|---|---|---|
| UM-01 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §1 альтернативная формулировка | Mention → Use | «Jetix — это мастерская для работы с информацией (Workshop metaphor canonical per [doc] LOCKED v1.0); 12 specialized agents × 6 departments × 8 active projects.» — «canonical» = document-level lock applied to structural claim (12 agents, 8 projects). Workshop metaphor MENTIONED as anchor then USED as structural fact with LOCKED authority | Add use-mention disclaimer: «Workshop = narrative frame LOCKED; 12 agents = role-type count (type-level); 8 projects = declared portfolio» |
| UM-02 | `decisions/JETIX-CORPORATION-2026-05-05.md` | §0 TL;DR present-tense | Mention → Use | «Jetix Corporation — это AI-native operational корпорация» — «Corporation» MENTIONED as aspirational concept in purpose; USED as present-tense operational entity. Frontmatter says «purpose = концептуальный документ» | Add face declaration: «as-mentioned (conceptual); as-operational (vapor); A.4 Temporal Duality» |
| UM-03 | `JETIX-WORKING-FILE-v0-2026-05-17.md` | §3.1 Workshop metaphor | Mention → Use | «Мастерская для работы с информацией» = архитектурный anchor. Owner — мастер; agents — instrumental specialists» — metaphor MENTIONED as frame then immediately USED to derive structural roles («мастер», «instrumental specialists») without formal A.1.1 BoundedContext declaration | Add use-mention disclaimer: «Workshop = communication frame; не formal A.1.1 BoundedContext (formal fields: glossary + invariants + scope = absent per D-PHIL-SCOPE-2)» |
| UM-04 | Multiple Foundation Parts + CLAUDE.md | Various | Use without mention declaration | IP-1/IP-2/IP-3/IP-7 used as if canonical FPF primitives. Per 01-fpf-on-human-language-v2.md §4b: «§4b = RUSLAN-LAYER mapping (НЕ canonical FPF)». Foundation Parts sources cite `design/JETIX-FPF.md` (archived overreach) as authority for these IPs. They are Jetix-internal interpretations presented as «FPF-grounded» | Add use-mention disclaimer in each Part §0: «IP-1/2/3/7 = Jetix-internal interpretive principles derived from FPF spirit; not canonical FPF Spec terminology» |

---

## §5 EP-1..EP-5 Instances — Specific File:Line References

### EP-1 — Artefact-system gap (LOCKED artefact ≠ operational system)

Most instances. Per Task 2 §0: «10 of 14 objects carry LOCKED artefact status while operational status F2-vapor.»

| Instance | File | Evidence of gap |
|---|---|---|
| EP-1.a | `CLAUDE.md` §Foundation Architecture heading «LOCKED» | Operational: Parts 1/3/5/9/11 = memory-dominant per 06-honest-self-audit §2; Halt-Log-Alert = STUB per .claude/agents/*.md |
| EP-1.b | `JETIX-WORKING-FILE-v0-2026-05-17.md` §7 F8 table | F8 applied to all Parts; operational evidence varies F2-F5 per Part |
| EP-1.c | `JETIX-WORKING-FILE-v0-2026-05-17.md` §9 «8 active projects» F5/R-high | shared/state/active-projects.json stale 2026-04-14; 1 entry; wiki/projects/ = 0 files |
| EP-1.d | `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` | daily-log/ = .gitkeep only; no operational daily-log cadence entries |
| EP-1.e | `decisions/JETIX-CORPORATION-2026-05-05.md` | Corp = vapor (no legal entity); TL;DR says «operational corporation» |
| EP-1.f | `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` | Clan = 0 signatories; charter LOCKED as artefact |

### EP-2 — Use-mention drift

| Instance | File | Slip description |
|---|---|---|
| EP-2.a | `JETIX-WORKING-FILE-v0-2026-05-17.md` §1 + §3.1 | Workshop metaphor → structural claims (UM-01, UM-03 above) |
| EP-2.b | `decisions/JETIX-CORPORATION-2026-05-05.md` §0 | «Corporation» mentioned as concept, used as present-tense entity (UM-02) |
| EP-2.c | `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md` §4b | IP-1/2/3/7 mentioned as «RUSLAN-LAYER» but Foundation Parts use them as FPF-canonical (UM-04) |
| EP-2.d | Multiple Foundation Parts | `design/JETIX-FPF.md` mentioned as canonical FPF source; used as authority for FPF primitives; actually = Jetix derivative (now archived) |

### EP-3 — Role/executor conflation

| Instance | File | Evidence |
|---|---|---|
| EP-3.a | `CLAUDE.md` §Agent Roster | 12 rows presented as present-tense agents; Phase column partially mitigates but no IP-1 disclaimer |
| EP-3.b | `JETIX-WORKING-FILE-v0-2026-05-17.md` §2 + §4 mermaid | «12 specialized agents» in description + visual without type/token distinction |
| EP-3.c | `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` §0 | «13 legacy agents on adjacent mailboxes» — 13 vs 12 count + «on adjacent mailboxes» implies operational presence for stale mailboxes |
| EP-3.d | `JETIX-WORKING-FILE-v0-2026-05-17.md` §11.1 step 3 | «Pick subset of 12 agents that apply to your domain» — fork guide uses 12 as executor count for replication |

### EP-4 — Promise без commitment machinery

| Instance | File | Missing A.2.8 fields |
|---|---|---|
| EP-4.a | `decisions/JETIX-CORPORATION-2026-05-05.md` §0 TL;DR | Trajectory «€5K → $100K → €100M» stated as promise; no obligation-holder, no adjudication path, no receipt mechanism |
| EP-4.b | `JETIX-WORKING-FILE-v0-2026-05-17.md` §5.2 R12 | R12 stated as «constitutional guarantee» for members; fork-and-leave infrastructure = vapor; enforcement mechanism absent |
| EP-4.c | `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` | Clan Charter «R12 as constitutional guarantee for members» — 0 signatories; no formal A.2.8 commitment structure |
| EP-4.d | `JETIX-WORKING-FILE-v0-2026-05-17.md` §3.2 TRM model | «TRM controls 6 resource classes» — control = U.PromiseContent; A.2.8 U.Commitment unpacking absent; only 2 of 6 tracked |

### EP-5 — F-G-R applied to wrong subject face

| Instance | File | Wrong subject |
|---|---|---|
| EP-5.a | `JETIX-WORKING-FILE-v0-2026-05-17.md` §7 table | F8 = approval-grade (8 RUSLAN-ACKs) presented as if B.3 claim-truth-grade; individual Parts = F5 per frontmatter |
| EP-5.b | `JETIX-WORKING-FILE-v0-2026-05-17.md` §5.2 R12 | F5 applied to R12 as single triple; THREE distinct objects (text/commitment/enforcement) each with different F-grade |
| EP-5.c | `JETIX-WORKING-FILE-v0-2026-05-17.md` §1 alt formulation | F5/R-high applied to «12 specialized agents × 6 departments × 8 active projects» (LOCKED canonical doc cited as source) — source-lock ≠ operational-truth |
| EP-5.d | `CLAUDE.md` §4.1 | 12 rules presented under «Constitutional (12 hard rules)» heading as uniform grade; Rule 11 machine-enforced ≠ Rule 12 vapor-enforcement |
| EP-5.e | `decisions/STRATEGIC-INSIGHT-JETIX-AS-PEOPLE-NETWORK-STATE-2026-05-12.md` frontmatter | F:F3; but body describes Clan Charter as «constitutional guarantee» — F3 guarantee needs A.2.8 commitment; pure U.Episteme claim would not use «guarantee» language |

---

## §6 Dissents Preserved + Open Questions для Ruslan

Per AP-6. NOT averaged. Each with (F, ClaimScope, R).

### DISS-01 — F8 grade semantics: approval vs truth-grade

- **Position A (working file §5.5 + §7):** F8 = «canonical-locked» = highest Jetix grade; all Foundation Parts F8 in §7 table.
- **Position B (this critic):** F8 = approval-grade (RUSLAN-ACK records); individual Part frontmatters = F5. B.3 claim-truth-grade and Jetix approval-grade are DIFFERENT scales. Jetix F-scale is adapted from FPF B.3 but semantics shifted.
- **F:** F4 · **ClaimScope:** holds within Jetix internal terminology only; FPF community would read F8 as claim-truth-grade
- **R:** Refuted if Ruslan explicitly acks that Jetix F8 = approval-grade AND documents are updated to carry this disclaimer.
- **OQ-DISS-01 для Ruslan:** F8 в Jetix = approval-grade OR claim-truth-grade? Если approval-grade — нужен явный disclaimer в §5.5 и §7 чтобы L1 аудитория не читала как B.3.

### DISS-02 — Workshop metaphor: narrative frame vs formal A.1.1 anchor

- **Position A (CLAUDE.md + JETIX-WORKING-FILE + Workshop LOCKED doc):** Workshop = canonical architectural anchor; LOCKED canonical per Ruslan-dictated decision.
- **Position B (phil × critic, carried from Task 1 D-PHIL-SCOPE-2):** Architectural anchor per FPF A.1.1 requires formal BoundedContext fields (glossary + invariants + scope). Workshop CONCEPT document = narrative richness без formal structure. «LOCKED canonical» grant conflates document-lock with formal-structure-declaration.
- **F:** F4 · **ClaimScope:** Position A holds for Jetix-internal use as communication frame; Position B holds if FPF-formal alignment claimed for Workshop anchor.
- **R:** Refuted if JETIX-WORKSHOP-CONCEPT-2026-04-30.md is found to contain explicit A.1.1 fields.
- **OQ-DISS-02 для Ruslan:** Workshop = communication frame only (no action needed) OR formal FPF A.1.1 BoundedContext (requires formalisation)?

### DISS-03 — design/JETIX-FPF.md: dead reference vs live provenance

- **Position A (status quo):** Foundation Parts reference `design/JETIX-FPF.md`; the document guided their FPF-derivative design; valid historical provenance.
- **Position B (this critic):** `design/JETIX-FPF.md` archived 2026-05-06 as overreach. Live source path `design/JETIX-FPF.md` does not resolve. Foundation provenance currently points to a non-existent path. The epistemic lineage is broken at provenance-gate level (shared-protocols §2 rule 1: paths must resolve).
- **F:** F5 · **ClaimScope:** Path resolution is a mechanical fact; provenance-gate has binary criterion.
- **R:** Refuted if `design/JETIX-FPF.md` is confirmed to still exist at live path (no evidence from repo structure).
- **OQ-DISS-03 для Ruslan:** Update 13 Foundation Part source paths to `archive/design/JETIX-FPF.md` via AWAITING-APPROVAL packet? Or accept current state as «design decisions made with valid contemporary source; archive path for audit purposes»?

### DISS-04 — R12 enforcement status: constitutional claim vs vapor mechanism

- **Position A (JETIX-WORKING-FILE §5.2 + CLAUDE.md §4.1):** R12 = constitutional Tier 2 rule; F5 / R-high (4-source trail LOCKED).
- **Position B (Task 1 O-11 phil, carried):** R12 has THREE distinct faces: (a) text U.Episteme F5 LOCKED; (b) U.Commitment in specific relationship F2; (c) enforcement mechanism F2-vapor. «Constitutional guarantee» requires at minimum (b) operational. Fork-and-leave infrastructure = not evidenced. «Guarantee» is a promise-language term requiring A.2.8 machinery.
- **F:** F4 (this dissent) · **ClaimScope:** Position A holds as normative intention; Position B holds as operational evidence state.
- **R:** Refuted for Position B if AWAITING-APPROVAL r12 packet acked AND enforcement mechanism described.
- **OQ-DISS-04 для Ruslan:** R12 packet — acked or pending? If pending: current R12 language should carry «pending-ack» qualifier not «LOCKED».

### DISS-05 — ACTION-PLAN-PHASE-1 ack status: draft vs operative

- **Position A (canonical/INDEX.md + decisions/ folder):** decisions/ = LOCKED canonical docs.
- **Position B (ACTION-PLAN-PHASE-1 frontmatter):** `status: draft (awaiting Ruslan ack)` — explicitly not acked.
- **F:** F5 (mechanical: frontmatter is unambiguous) · **ClaimScope:** Folder-based canon vs frontmatter-based status conflict.
- **R:** Refuted if Ruslan ack is documented somewhere (e.g. reports/strategic-decisions-2026-05-12.md).
- **OQ-DISS-05 для Ruslan:** ACTION-PLAN-PHASE-1-NEAR-FUTURE-2026-05-10.md — acked или still draft? RES.1/2/3 referenced as «binding» — binding requires ack.

### DISS-06 — Hexagon count: 6 vs 7 (Heptagon)

- **Position A (JETIX-WORKING-FILE §5.1 + 00-SUMMARY §2.4 «6 LOCKED insights»):** Hexagon = 6 Strategic Insights.
- **Position B (JETIX-WORKING-FILE §5.2 + H7 People-NS frontmatter + 00-SUMMARY §2.4 heading «Strategic Insights Hexagon (H1-H7)»):** H7 People-NS = 7th insight; synthesis = Heptagon.
- **F:** F5 (both positions traceable to file evidence) · **ClaimScope:** Naming artifact; no strategic impact, but clarity matters for L1 audience.
- **R:** Refuted if official rename to Heptagon documented.
- **OQ-DISS-06 для Ruslan:** Hexagon или Heptagon? Нужно официальное переименование чтобы L1 документы не противоречили внутренним.

---

## §7 Conformance Checklist (critic mode §3.1)

Per philosophy-expert §3.1. Applied to this audit's own output.

| Check | Result | Evidence |
|---|---|---|
| 1. Falsifier-named (Popper) | Pass | Each stale item carries «Why stale» as implicit falsifier; DISS-01..06 carry explicit R fields |
| 2. Paradigm-named on shift | Pass | EP-5 section names prior paradigm («approval-grade used as claim-truth-grade») + anomaly (FPF B.3 semantics differ from Jetix F-scale semantics) |
| 3. Mental-model + conditions | Pass | A.16 language-state model (Popper), A.4 Temporal Duality (epistemic-operational split), A.2.8 Commitment model (promise machinery) — all cited with applicable conditions |
| 4. Method declares what NOT doing | Pass | §0 + §3.4-equivalent in §§ headers: «Surface'инг only; actions = options; NOT choosing; NOT deleting» |
| 5. Dichotomy-of-control | Pass | In-our-control: surfacing flags, proposing options. NOT in our control: Ruslan's ack decisions, strategic priorities, enforcement path |
| 6. Fallacy-named | Pass | No fallacies named without taxonomy (none triggered) |
| 7. Meta-claim grounded in object-level | Pass | All meta-claims (EP-1..EP-5, XD-01..07) reference specific file:line instances |

**Acceptance predicate (Hamel-binary):** «All stale items carry file:line provenance AND at least 2 suggested action options AND no action chosen; cross-document inconsistencies ≥5 with both positions preserved; EP-1..EP-5 each have ≥3 instances; dissents ≥3 with (F, ClaimScope, R) triples.»

**Status:** Predicate SATISFIED (42 stale items, 7 XD-inconsistencies, 6 dissents).

---

## §3.4 Anti-scope

- This critic is NOT choosing actions — all options are Ruslan's decision.
- This critic is NOT assessing capital impact (ICP switch, trajectory) — investor-expert territory.
- This critic is NOT doing code review on Jetix tooling.
- This critic is NOT auditing FPF Spec itself — only Jetix documents against FPF epistemic discipline.
- This critic is NOT producing corrected versions of flagged documents — next cycle's optimizer or AWAITING-APPROVAL packet flow handles writes.
- This critic is NOT asserting «doc bad» — surfacing epistemic state; evaluation is Ruslan's.
- This critic is NOT promoting any draft to canonical — brigadier is sole writer per Q2.
