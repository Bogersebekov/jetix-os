---
title: ROY Brigadier Deep Prompt — Wave C Bundle 4 (Parts 7 + 9 + 10 — Project Lifecycle + Owner Interaction + External Touchpoints) — FINAL Wave C bundle
date: 2026-04-28
type: deep-prompt
target: ROY brigadier (.claude/agents/brigadier.md)
parent_brief: prompts/cloud-code-wave-c-bundle-4-prompt-writing-brief-2026-04-28.md
predecessor_deep_prompt: prompts/wave-c-bundle-3-deep-prompt-2026-04-28.md
predecessor_ack_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
predecessor_ack_bundle_1_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
predecessor_ack_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
predecessor_ack_bundle_3: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 4
final_wave_c_bundle: true
bundle_scope:
  - "Part 7 — Project Lifecycle Substrate (3 bullets — P7.1 schema/state-machine + P7.2 IP-5 whitelist + P7.3 cadence event-driven)"
  - "Part 9 — Owner Interaction Scaffold (3 bullets — P9.1 daily-log + P9.2 weekly-review with draft-disposition + P9.3 SLA taxonomy)"
  - "Part 10 — External Touchpoints & Network Interface (4 bullets — P10.1 adapter stubs + P10.2 C3 phase boundary + P10.3 privacy architecture + P10.4 fork-separation FINAL CLOSURE)"
  - "Inter-Part lite coherence (UND-3 finalization Part 7↔Part 5; Part 10↔Part 1 D27 promotion; Part 9↔Part 6 C4 fix)"
  - "OQ-B1-5 D27 reconciliation_strategy field promotion (END-OF-CYCLE constitutional supplement record analogous to OQ-B2-A pattern)"
estimated_walltime: 4-7h ROY substantive (Bundle 2 = 43min/3 parts at 89% operational; Bundle 3 = ~2h/2 parts at 100%; Bundle 4 = 3 parts ~10 bullets, projected 1-3h at compound velocity, 12h ceiling)
status: ready-for-brigadier-dispatch
constitutional_baseline_bundle_1: 2026-04-28 Ruslan ack of Bundle 1 (RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md) + supplement — F-G-R F8 / Default-Deny F8 / Blast-radius F8 / AWAITING-APPROVAL packet schema F8 with `gate_class` enum / Halt-Log-Alert F8 / Corrigibility F8 / cross-fork-provenance.json schema
constitutional_baseline_bundle_2: 2026-04-28 Ruslan ack of Bundle 2 — Parts 2/3/4 architectures F5 / C1 Joint Design Variant A F5 / routing-table.yaml F4 / task-return-packet.json F4 / WORD COUNT TARGET 10K-20K F8 / message schema v2.0.0 F4
constitutional_baseline_bundle_3: 2026-04-28 Ruslan ack of Bundle 3 — Parts 5/8 architectures F5 / C2 canonical health-signal schema F5 / SLI/SLO schema F5 / TRADEOFF-01 split F8 / OQ-MERGED-2 dissolve-test active (Bundle 3 = Cycle 1 of 3) / OQ-MERGED-5 specify-and-stub held / UND-2 methodology promotion pipeline F5 / UND-3 P5↔P7 stub F2 (Bundle 4 finalises) / Bundle 1 supplement (Part 1 §I.4 enum + commit-format-tokens [swarm-lib]+[health]+[methodology] + K18 upcasting)
mantra: "QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. FINAL-CLOSURE-FORK-SEPARATION (Part 10 esp). EVENT-DRIVEN (Part 7). SINGLE-OWNER-BOUNDED (Part 9). PRIVACY-STRUCTURAL (Part 10). RUSLAN-ACK > BRIGADIER-CONFIDENCE. THIS IS WAVE C CLOSURE."
---

# Wave C Bundle 4 — ROY Brigadier Deep Prompt — FINAL Wave C BUNDLE

## §0 Mission Statement (READ FIRST, INTERNALIZE)

**Bundle 4 closes the Foundation. After Bundle 4 → Wave D integration pass → Wave E LOCKED tag. There is no Bundle 5.** Eight of ten Foundation parts are F5 LOCKED on `claude/jolly-margulis-915d34` HEAD `8be5628`: Part 1 (Bundle 1, supplement-corrected), Part 6a (Bundle 1), Part 6b (Bundle 1), Part 2 (Bundle 2), Part 3 (Bundle 2), Part 4 (Bundle 2), Part 5 (Bundle 3), Part 8 (Bundle 3). **Bundle 4 finalises the remaining three parts and seals the Foundation envelope.**

Bundle 4 wires the three layers that touch the world:

- **Part 7 — Project Lifecycle Substrate** — closes the **execution loop**: every project that the system runs goes through a canonical state machine (`scoped → staged → activated → under-review → closed | archived`) with stage-gate predicates per Part 6b §I.2, appetite declarations per Singer Shape Up, and event-driven cadence per OQ-5 Ruslan ack. Project closure events emit `project-retrospective-packet.json` to Part 5's compound-learning loop — finalising **UND-3** (Bundle 3 set the input contract stub at Part 5 §A; Bundle 4 satisfies the EMIT contract at Part 7 §B). **Without Part 7, the system has projects but no canonical lifecycle — appetite drifts, stage transitions are ad-hoc, retrospectives never feed the compound loop, and the R2 reinforcing loop closed by Part 5 in Bundle 3 starves of inputs.**

- **Part 9 — Owner Interaction Scaffold** — closes the **owner attention loop**: every day the owner runs the system through a canonical interaction shape (morning intent → cycle dispatch → afternoon execution → evening reflection committed) and every week through a weekly review with a draft-disposition table (C2 producer side: how the owner triages accumulated drafts into accept / iterate / discard categories). The 3-tier SLA taxonomy (L1 strategic same-session, L2 tactical weekly batch, L3 routine auto-log) is canonicalised. **Part 9 is single-owner Phase A bounded per FUNDAMENTAL §2.6 + IP-2** — multi-owner Phase B/C requires **F.9 Bridge structural change ≥35%** (per Wave A Ashby BOSC-A-T-X analysis). **Without Part 9, the system has agents but no canonical owner interface — Ruslan's attention budget gets shredded by ad-hoc surfacing patterns and the daily loop never compounds into weekly reflection.**

- **Part 10 — External Touchpoints & Network Interface** — closes the **outside-world loop**: every contact the system maintains, every external action it takes (Linear ticket, GitHub PR, Slack DM, partner email), every intelligence signal it watches (HN, niche sub-Reddits) flows through Part 10's canonical CRM data model + integration adapter pattern (RT-1 read-only intelligence trackers + RT-2 write-ack action coordinators) + privacy invariants. **CRM is OPERATIONAL** — cycle 10 already shipped 24 source files / 35 unit tests / 10 `/crm-*` skills / 4 YAML schemas (`crm/_schema/`). Part 10 **canonicalises** this — does NOT redesign. **Without Part 10, the system has a CRM with no Foundation-level boundary declarations, no privacy structural enforcement, no fork-separation discipline for the ICP-specific RUSLAN-LAYER, and no integration adapter pattern for Phase B scale.**

**Treat with 1 trillion percent responsibility.**

The constitutional contract from Bundles 1+2+3 is permanent. Every Bundle 4 part calls Part 1 §H operations for canonical writes; every emitted artefact carries F-G-R per Part 6a §I.1 F8 schema; every promotion event logs to `swarm/approvals/log.jsonl`; every gate packet conforms to Part 6b `awaiting-approval-packet.json` F8 schema with `gate_class` enum `[stop_gate, stage_gate, draft_promotion]`. **Part 7 stage-gate transitions emit `gate_class: stage_gate`. Part 9 strategic-tier ack events emit `gate_class: stage_gate`. Part 10 external write-ack events emit `gate_class: stage_gate`.** Health emissions (Part 7 stage-transition rate, Part 9 daily-log creation rate, Part 10 external-action latency, integration adapter health) conform to Part 8 §I.1 canonical health-signal schema F5.

> *Ruslan emphasis (verbatim, original Russian, do NOT paraphrase before applying):*
> *«Чтобы вся вот эта мудрость, наработки из книг — они были применены в системе,*
> *если это возможно, если нужно, целесообразно — на 1000% насколько это*
> *целесообразно. Ещё чтобы задавались вопросы как мы можем конкретно добавить,*
> *нахуй, эту штуку, чтобы было ещё отдельный прогон где вся эта залупа даёт*
> *обратную связь — а как мы можем это улучшить с точки зрения такой-то книжки*
> *или с книжки такой-то.»*

The Wisdom Application Loop (§5) is the structural mechanism that operationalizes Ruslan's central directive. **Bundle 4 inherits Bundle 3's ≥85% operational floor.** Part 7 (state machines + appetite declarations + cadence rules) + Part 9 (daily-log/weekly-review/SLA-tier schemas) + Part 10 (CRM data model + integration adapter pattern + privacy structural enforcement) are inherently operational domains — Bundle 4 should easily match Bundle 3's 100% operational achievement. Below 85% is a red flag — investigate.

**Bundle 4 introduces FOUR structural firsts vs Bundle 3:**

1. **NO retroactive supplement first task** — unlike Bundle 3 which had to apply OQ-B2-A retroactive Bundle 1 corrections at Phase 0 before substantive dispatch, Bundle 4 has a **clean substantive start**. Bundle 1 supplement is committed (`ca38be3`); Bundle 3 supplement is committed (Bundle 3 was the supplement source). **OQ-B1-5 D27 `approvals_reconciliation_strategy` field promotion is the END-OF-CYCLE supplement record** (single commit at end of Bundle 4 cycle — analogous to OQ-B2-A pattern but inverted timing — substantive Part 10 work establishes the field promotion need; supplement record commits AFTER all 3 architecture documents land).

2. **FINAL CLOSURE of OQ-MERGED-3 fork-separation** — every Bundle 1+2+3 part has a §X Foundation vs RUSLAN-LAYER section. Bundle 4 is the **last** opportunity to declare fork-separation at the Foundation level. **Part 10 has the highest creep risk** because RUSLAN-LAYER ICP specifics (DACH market, German GDPR config, specific contact lists, Linear/GitHub/Notion auth tokens, DACH-specific intelligence tracker URLs) shade into Foundation-generic CRM mechanics if §X is sloppy. Critic gate auto-rejects ambiguous §X declarations for Part 10 — explicit DACH/GDPR/auth-token examples mandatory.

3. **No Joint Design Phase** — unlike Bundle 2 (C1 BLOCKING contradiction → 2h Joint Design) and Bundle 3 (C2 + UND-3 carry-over → 1h Joint Design lite), Bundle 4's UND-3 is a **lite finalization not a BLOCKING contradiction**: Part 5 §A (Bundle 3) declared input expectations via UND-3-stub.md; Part 7 §B (Bundle 4) FULLY SPECIFIES the EMIT contract. Coherence verified by **M5 inter-Part lite coherence check** (post-integrator, pre-critic, no separate phase).

4. **Three structural autochecks** — (i) **Part 7 cadence MUST be event-driven** per OQ-5 Ruslan ack (declared in §E Laws, NOT cycle-boundary-gated; brigadier autocheck rejects calendar-cron-gated cadence); (ii) **Part 9 IP-2 multi-owner stub fields MUST appear in §I** (declared NOT implemented — Phase B F.9 Bridge work; brigadier autocheck rejects Part 9 omitting multi-owner stub); (iii) **Part 10 privacy MUST be structural not behavioral** — schema fields (`consent_recorded_at`) + lint signals (`/lint --check-protected-inference`) + Default-Deny entries; brigadier autocheck rejects "we promise to be careful" framing prose without structural enforcement.

Read this prompt three times before dispatching. Read every linked constitutional artefact in §3 before composing your first dispatch. When in doubt, ask Ruslan via HITL escalation.

---

## §1 Constitutional Inputs (Bundles 1+2+3 LOCKED — DO NOT re-litigate)

### §1.1 F8 LOCKED schemas (consumed verbatim)

| Constitutional artefact | F-level | Bundle 4 consumption rule |
|---|---|---|
| `f-g-r.json` (Part 6a §I.1) | F8 | Every Bundle 4 architecture document, every emitted project-retrospective-packet / daily-log entry / weekly-review entry / CRM event-log entry / integration-adapter-call carries F-G-R tag. Inline `[F4|G:scope|R-medium]` OR §G table. |
| `awaiting-approval-packet.json` with `gate_class` enum (Part 6b §I.1) | F8 | Part 7 stage-gate transitions = `gate_class: stage_gate`. Part 9 strategic-tier ack events = `gate_class: stage_gate`. Part 10 external write-ack events = `gate_class: stage_gate`. Schema fields FROZEN — consume verbatim. |
| `default-deny-table.yaml` (Part 6b §I.3) | F8 | Part 10 novel external-action classes Default-Deny classified before integration adapter fires. Part 10 protected-inference attempts (race/religion/political/health) Default-Deny classified Tier 0 hard. |
| `blast-radius-table.yaml` 4 tiers (Part 6b §I.4) | F8 | Bundle 4 actions Tiered: Part 7 archive = Tier 1; Part 7 stage transition = Tier 2 (batch ack); Part 9 weekly review = Tier 1; Part 10 external write to GitHub/Linear/Slack = Tier 1; Part 10 forget-request = Tier 1; Part 10 read-only intelligence ingest = Tier 3 (auto-log). |
| Halt-Log-Alert L9 (Part 6b §E) | F8 | Bundle 4 Tier 0 events (e.g., privacy invariant violation attempt) conform to ≤1s halt / ≤5s log / ≤60s alert ordering. |
| Corrigibility (Part 6b §E L9 / Askell HHH Appendix E.2) | F8 | Bundle 4 NEVER locks Ruslan out. Privacy enforcement is Halt+Alert, NOT lock-out — Ruslan can `git revert`, manually edit any record, override any gate. |
| WORD COUNT TARGET 10K-20K (Bundle 2 ack §3) | F8 | Bundle 4 architectures conform. Part 10 likely larger end given CRM canonicalisation + privacy architecture sub-section. |
| `task-return-packet.json` (Part 4 §I.1) | F4 → F5 (Bundle 3 Part 5 consumption validated) | Part 7 `project-retrospective-packet.json` is a SUPERSET (extends task-return-packet with project-specific fields — UND-3 finalization). |
| Canonical health-signal schema (Part 8 §I.1, C2 resolved Variant B) | F5 | Bundle 4 emitter mapping (Part 7 stage-transition rate; Part 9 daily-log creation rate; Part 10 integration-adapter health) conforms — added to Part 8 §I.3 mapping table (optional Wave D housekeeping per OQ-B3-P8-1 deferred). |
| `wiki/methodology/` entity-type (Part 3) + admissibility predicate (Part 3 §E L9) | F4 | Part 7 retrospective patterns may PROMOTE here via Part 5's UND-2 methodology promotion pipeline. |
| Message schema v2.0.0 with `acting_as:` mandatory (Part 4 §H) | F4 | All Bundle 4 messages (Part 7 cycle-dispatch / Part 9 morning-intent emit / Part 10 external-action request) conform. |
| `cross-fork-provenance.json` (Part 1 §I.1 — post Bundle 1 supplement) | F4 | Part 10 §I.1 PROMOTES `approvals_reconciliation_strategy` from `metadata` open field to **top-level** (OQ-B1-5 resolution; constitutional supplement record at end of Bundle 4 cycle). |
| `wiki/graph/edges.jsonl` schema (Part 3) + 9 typed-edge taxonomy + CRM 8 edge types (`crm/_schema/`) | F4 | Part 10 §I CRM edge schema conforms; UND-5 binding. |
| methodology-promotion-event.json (Bundle 3 Part 5 §I.1) | F4→F5 on Bundle 3 ack | Part 7 retrospective candidates may emit this event. |
| sli-slo.json (Bundle 3 Part 8 §I.2) | F4→F5 on Bundle 3 ack | Bundle 4 health emissions conform to canonical schema; SLO targets calibration-grade. |
| PARA-tier mandatory (Bundle 2 P2.2) | F5 | Part 9 daily-log entries tagged `para_tier: Project | Area | Resource | Archive`; Part 10 CRM contacts tagged `para_tier: Project` (active deal) / `Resource` (relationship asset) / `Archive` (deprecated). |

### §1.2 Bundle 4 OQ inputs (from prior Ruslan acks — NO re-litigation)

| OQ | Status | Bundle 4 implication |
|----|--------|----------------------|
| **OQ-MERGED-3** | Wave A scope (per Ruslan ack 2026-04-27) | Bundle 4 §X per part = **FINAL CLOSURE of Foundation vs RUSLAN-LAYER fork-separation**. Part 10 has highest creep risk — explicit DACH ICP / German GDPR / Linear+GitHub+Notion auth-token examples mandatory in §X. |
| **OQ-5** | P7 cadence event-driven (Ruslan ack) | Part 7 §E Laws DECLARES event-driven cadence ("project state transitions trigger on closure events / stage-gate ack events / scope-record updates — NOT on calendar-cron / NOT cycle-boundary-gated"). Brigadier autocheck rejects calendar-cron cadence. |
| **OQ-MERGED-7** | U.System/U.Episteme declarations sufficient | Bundle 4 part-classifications: P7=U.System (project lifecycle is system orchestration); P9=U.System (owner interaction is system substrate); P10=U.System (CRM pipeline + integration adapter pattern is system; CRM **records** are dual: U.Episteme content for the contact-as-knowledge + U.System pipeline for the CRUD + edge graph). |
| **C3 contradiction** | Defer Phase B (LOW severity) | Part 10 §F Anti-scope DECLARES Phase A inbound external = Phase B work; current Phase A = owner-initiated only via Part 2 `/ingest`. |
| **C4 contradiction** | Nomenclature fix `PhaseOf` → `methodologically-uses` (Part 9 → Part 6) | Bundle 4 Part 9 §D applies fix verbatim. Part 9 USES Part 6 gate as service, NOT exclusive pre-gate phase. |
| **UND-3** | P5 → P7 retrospective input contract finalization (Bundle 3 stub set; Bundle 4 Part 7 finalises EMIT) | Part 7 §B Outputs FULLY SPECIFIES `project-retrospective-packet.json` schema (extends Part 4 `task-return-packet.json`). M5 lite coherence: Part 7 §B emit ↔ Part 5 §A input. |
| **UND-5** | CRM edge validation in Bundle 4 (P10 work) | Part 10 §I declares CRM edge schema conforming to Part 3 `wiki/graph/edges.jsonl` typed-edge taxonomy; references existing `crm/_schema/edges.yaml` 8 CRM edge types. |
| **OQ-B1-5** | D27 `approvals_reconciliation_strategy` field promotion to top-level (deferred from Bundle 1) | Part 10 §I.1 update of `cross-fork-provenance.json` (Part 1 §I.1 schema). RESOLVE here via END-OF-CYCLE constitutional supplement record analogous to OQ-B2-A pattern. |
| **OQ-B1-6** | Rules 4 + 7 real-time encoding | Wave D capability gap. Bundle 4 may surface implementation pattern via Part 10 external-action coordination (audit trail = approval log + CRM event log + cross-fork-provenance log). |
| **OQ-MERGED-2** | Part 5 dissolve-test active (Bundle 3 = Cycle 1) | Bundle 4 = **Cycle 2 of 3**. Bundle 4 brigadier MUST log evidence of compound-phase-exclusive operations to `swarm/wiki/cycles/.../bundle-4/dissolve-test-evidence-cycle-2.md` (mirrors Bundle 3's dissolve-test-evidence.md pattern). Threshold check happens at Wave D (Cycle 3). |

### §1.3 Cross-cuts within Bundle 4 (apply throughout)

| Cross-cut | Rule | Where applied |
|---|---|---|
| **F-G-R DOGFOOD per F8 schema** | Every Bundle 4 promoted claim carries F-G-R per Bundle 1 Part 6a §I.1 schema | §G F-G-R Tagging table; inline tags |
| **A.14 typed edges** | Bundle 1 canonical 10-edge reference table consulted; NO new edge types invented; NO generic `depends-on`. **C4 fix applied** (Part 9 §D `methodologically-uses Part 6`, NOT `PhaseOf Part 6`) | §D Dependencies (every entry) |
| **Append-only** | project-retrospective-packets, daily-logs, weekly-reviews, CRM event log, approval log — append-only; corrections via NEW entries with `corrects:` pointer per Reversal Transactions (Young 2010) | §C Side-effects; §I Data schemas |
| **L/A/D/E** | Every §E Boundary section structured per FPF A.6.B Norm Square | §E section per part |
| **Foundation vs RUSLAN-LAYER FINAL CLOSURE** | Explicit §X per part — **Part 10 explicit DACH/GDPR examples MANDATORY**; Bundle 4 = last chance per OQ-MERGED-3 | §X mandatory; critic gate auto-rejects ambiguous |
| **PARA-tier mandatory** | Part 9 daily-log tagged `para_tier: Project | Area | Resource | Archive`; Part 10 CRM contacts tagged via `para_tier:` (Project=active deal, Resource=relationship asset, Archive=deprecated) | Part 9 §C + Part 10 §I |
| **IP-1 Role≠Executor** | Role manifests + integration adapter pattern use role archetype names; NO executor names, model names, agent file paths in Bundle 4 Foundation artefacts | §A / §B / §H / §I per part |
| **IP-2 single-owner bounded** | Part 9 §X explicit declaration; multi-owner stub fields in §I (NOT implemented; Phase B F.9 Bridge structural change ≥35%) | Part 9 §X + §I |
| **IP-5 past-participle states** | Part 7 §I.1 state machine names use past-participle forms (`scoped, staged, activated, under-review, closed, archived`); P7.2 whitelist captures applied corrections (`active` → `activated`; `review` → `under-review`) | Part 7 §I.1 + §X |
| **Operational ratio ≥85%** | Wisdom Loop OPERATIONAL/PHILOSOPHICAL discriminator — Bundle 4 inherits Bundle 3 floor; should easily match given P7+P9+P10 are inherently operational | §M Wisdom Findings table per part |
| **Word count 10K-20K per part** | F8 LOCKED constitutional | §6 Quality bar; Part 10 likely larger end |
| **Part 7 cadence event-driven** | OQ-5 Ruslan ack — declared in §E Laws; NOT calendar-cron; NOT cycle-boundary-gated | Part 7 §E |
| **Part 9 IP-2 multi-owner stub** | §X declares structural change ≥35% required at >10× scale; §I declares stub fields (NOT implemented) | Part 9 §X + §I |
| **Part 10 privacy STRUCTURAL** | Schema fields (`consent_recorded_at`) + lint signals (`/lint --check-protected-inference`) + Default-Deny entries (race/religion/political/health classifier attempts) | Part 10 §I + §H + §F |
| **Part 10 fork-separation FINAL CLOSURE** | Explicit DACH ICP / German GDPR / Linear+GitHub+Notion auth-token examples in §X | Part 10 §X |
| **CRM operational baseline canonicalisation** | Cycle 10 produced: 24 source files / 35 unit tests / 10 `/crm-*` skills / 4 YAML schemas. Part 10 CANONICALISES — does NOT redesign | Part 10 §A + §H + §I + §N |
| **OQ-B1-5 D27 field promotion** | END-OF-CYCLE constitutional supplement record (analogous to OQ-B2-A pattern) — Part 10 §I.1 references; supplement record commits at end of cycle | Part 10 §I.1 + supplement record `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md` |
| **No Joint Design Phase** | UND-3 finalization is M5 lite coherence (post-integrator, pre-critic), NOT separate phase | §4 Phase architecture (skip Joint Design Phase; M5 inline) |

### §1.4 Inter-Part references in Bundle 4 (M5 lite coherence checks)

| Cross-bundle reference | Direction | Where bound |
|---|---|---|
| Part 7 ↔ Part 5 (UND-3 finalization) | Part 7 §B emit contract satisfies Part 5 §A input stub | Part 7 §B + cross-ref Part 5 §A; Bundle 3 UND-3-stub.md updated F2→F4 |
| Part 9 ↔ Part 6b (C4 nomenclature fix) | `methodologically-uses` not `PhaseOf` | Part 9 §D every Part 6 reference |
| Part 9 ↔ Part 5 | Weekly review surfaces methodology promotion candidates from `agents/<id>/strategies.md`; emits AWAITING-APPROVAL `gate_class: draft_promotion` | Part 9 §B Outputs + Part 5 §A reference |
| Part 10 ↔ Part 3 (UND-5) | CRM edges to `wiki/graph/edges.jsonl` schema; references existing `crm/_schema/edges.yaml` 8 CRM edge types | Part 10 §I + cross-ref Part 3 §I |
| Part 10 ↔ Part 1 (OQ-B1-5 D27) | `cross-fork-provenance.json` `approvals_reconciliation_strategy` top-level field promotion | Part 10 §I.1 + Part 1 §I.1 supplement edit |
| Part 10 ↔ Part 2 (C3 deferred Phase B) | Inbound external = Phase B work; routes via Part 2 `/ingest` for Phase A owner-initiated only | Part 10 §F Anti-scope + Part 2 cross-ref |
| Part 10 ↔ Part 6b (privacy Default-Deny) | Protected-characteristic inference attempts Default-Deny classified | Part 10 §F + §H + Part 6b §I.3 reference |
| Part 7 ↔ Part 6b (stage-gate predicates) | Stage transitions emit `gate_class: stage_gate` packets | Part 7 §H + Part 6b §I.2 reference |

---

## §2 Bundle 4 Scope — Three Parts, Ten Bullets

### §2.1 Part 7 — Project Lifecycle Substrate (3 bullets)

**Source**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 7.
**Interface card**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md`.

**Bullet P7.1 — Canonical project schema YAML + 5-state state machine.**
- Output: Part 7 architecture document at `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` (10K-20K words). Schema declared inline at §I.1 + physical file `shared/schemas/project.json` (or `.yaml`) declared (Phase B file generation per OQ-B1-2 + OQ-B1-4 pattern). Required schema content:
  - **5 states (IP-5 past-participle compliant)**: `scoped` (initial — appetite + scope record drafted but not committed) → `staged` (committed — appetite + scope record + stage-gate predicates declared; awaiting activation ack) → `activated` (work in progress — execution cycles dispatched) → `under-review` (closure-of-cycle scope; retrospective drafting) → `closed` (terminal success) | `archived` (terminal — paused/killed/pivoted with rationale).
  - **Stage-gate predicates per Part 6b §I.2 stage-gate registry**: `scoped → staged` requires Ruslan stage-gate ack (`gate_class: stage_gate`); `staged → activated` requires Ruslan stage-gate ack; `activated → under-review` is event-driven (closure event from Part 4 task-return-packet aggregation); `under-review → closed | archived` requires Ruslan stage-gate ack with closure type declared.
  - **Appetite declarations (Singer 2019 Shape Up)**: `appetite_weeks: <integer>` (typically 2-6 weeks per FUNDAMENTAL §2.6); appetite-as-CONSTRAINT not estimate; if appetite exceeded → re-shape OR archive (NOT extend). Cross-ref Part 9 weekly review `appetite_actual_vs_planned` field.
  - **Scope records**: append-only scope-change log within project record; each entry carries `[F-level|G:scope|R:refuted_if]` + `rationale: <text>`.
  - **Resource tracking per project type**: 4 project types per `.claude/config/project-types.yaml` (consulting / research / product / bets) — each type declares baseline resource template (cycle dispatch frequency, expert-archetype mix, cadence rule).
- Acceptance predicate: schema structurally complete; ≥1 synthetic project fixture in each of 5 states; stage-gate transitions fire `gate_class: stage_gate` packets to Part 6b; appetite exceedance triggers re-shape-OR-archive predicate; resource template applies per project type.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack.
- **Reuses existing pattern**: `projects/` directory exists; `.claude/config/project-types.yaml` exists; `swarm/wiki/_templates/project-*/` 4 template trees exist; `/project-bootstrap`, `/project-review`, `/project-archive`, `/project-de-morph`, `/project-promote` skills exist. **CANONICALISE — do NOT reinvent.**
- Source: interface card §A-§B; product-management-cagan-shape-up consultant card §4 P1 appetite-as-constraint + §4 P2 betting-table rhythm + §4 P5 Outcome over Output; levenchuk-shsm-fpf consultant card IP-5 past-participle alpha state machine + A.3 Transformer Quartet for transitions; event-sourcing-cqrs consultant card (Young 2010) project state transitions as events; FUNDAMENTAL §2.6 daily ops; Bundle 1 Part 6b §I.2 stage-gate registry; AUDIT-CURRENT-STATE §3 projects directory current state.

**Bullet P7.2 — IP-5 past-participle exception whitelist.**
- Output: `decisions/policy/ip5-past-participle-whitelist.md` (or `.claude/config/ip5-past-participle-whitelist.yaml` — brigadier picks; YAML preferred for /lint consumption). Required content:
  - Applied corrections declared CANONICAL: `active` → `activated`; `review` → `under-review`. (Both are pre-Bundle-4 informal usage in `projects/` paths; Bundle 4 makes the past-participle form authoritative.)
  - Whitelist of EXCEPTIONS that may use non-past-participle form (e.g., `scoping` if mid-transition is needed; declared per IP-5 with rationale).
  - `/lint --check-ip5-past-participle` Phase B implementation reference (skill spec, NOT delivery code per Bundle 3 §6.8 specify-and-stub pattern).
- Acceptance predicate: file exists; corrections declared; ≥1 exception with rationale; `/lint` skill spec referenced.
- F-G-R: F4 architecture-time → F5 on first /lint --check-ip5-past-participle Phase B run.
- Source: FPF IP-5 past-participle alpha state machine; levenchuk-shsm-fpf consultant card; Bundle 1 Part 1 §I.2 commit-format-tokens.json pattern (config-driven via `.claude/config/`).

**Bullet P7.3 — Cadence alignment declaration — event-driven (OQ-5 Ruslan ack).**
- Output: Part 7 §E Laws section declares cadence verbatim:
  - **L1**: Project state transitions are TRIGGERED on event signals — closure events (cycle-end → Part 4 task-return-packet aggregation), stage-gate ack events (Ruslan ack on AWAITING-APPROVAL `gate_class: stage_gate`), scope-record update events (append-only entry to `projects/<slug>/scope-record.jsonl`).
  - **L2**: Project state transitions are NOT calendar-cron-gated. NOT cycle-boundary-gated. NOT periodic-N-day-polled.
  - **L3**: Cadence tracking SLI = `project-state-transition-latency` (delta between trigger event timestamp and state transition commit timestamp); SLO target Phase B calibration (per OQ-MERGED-5 specify-and-stub).
  - **L4**: Throughput bottleneck-prevention rationale: cycle-boundary-gating creates throughput floor of 1 transition / cycle / project; 8 active projects × 1 cycle/day = 8 transitions max/day; event-driven removes this ceiling per FUNDAMENTAL §3.3.1.
- Acceptance predicate: §E contains 4 laws verbatim; cross-references OQ-5 Ruslan ack.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack.
- Source: OQ-5 Ruslan ack; FUNDAMENTAL §3.3.1; Singer Shape Up (no calendar appetite — appetite expires on shape-up close).

**Special: UND-3 finalization (Part 7 ↔ Part 5 cross-bundle interface)**

Bundle 3 Part 5 set INPUT contract stub at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md`. Bundle 4 Part 7 FINALIZES EMIT pattern:

- Part 7 §B Outputs declares `project-retrospective-packet.json` schema EXTENDS Part 4 `task-return-packet.json` superset. Required additional fields:
  - `project_id` (reference to project schema)
  - `state_transition: {from, to, reason}` (final state transition triggering retrospective emit)
  - `appetite_actual_vs_planned: {planned_weeks, actual_weeks, delta_pct}` (Shape Up appetite reflection)
  - `lessons_learned: [{lesson_text, severity, applies_to_phase}]` (free-form structured)
  - `dr_r_candidates: [{decision_summary, rule_slug?, validation_evidence}]` (Part 5 DRR ledger candidates)
  - `methodology_promotion_candidates: [{rule_slug, evidence_count}]` (Part 5 methodology promotion pipeline candidates)
- Part 7 §J Operational Rituals declares cadence: per project closure event (state transition `under-review → closed | archived`) AND per cycle boundary (within `under-review` state, optional retrospective draft updates).
- Joint reference to Part 5 §A Inputs (cross-bundle coherence verified by **M5 inter-Part lite coherence check** §4.4).
- Bundle 3 UND-3-stub.md updated F2→F4 (Part 7 emit contract finalized; conformance verified).

### §2.2 Part 9 — Owner Interaction Scaffold (3 bullets)

**Source**: wave-c-worklist §2 Part 9.
**Interface card**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md`.

**Bullet P9.1 — Daily-log artefact schema.**
- Output: Part 9 architecture document at `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` (10K-20K words). Schema declared inline at §I.1 + physical file `shared/schemas/daily-log.json` declared (Phase B generation per pattern). Required schema content:
  - **Frontmatter fields (YAML)**: `date: YYYY-MM-DD`, `owner: ruslan` (single-owner Phase A — see §X), `projects_touched: [<slug>...]`, `decisions_made: [{decision_id, decision_summary, projects_touched, rationale}...]`, `ack_events: [{packet_id, gate_class, action_taken}...]`, `attention_budget_used: {tasks_started, tasks_completed, tasks_paused}`, `para_tier: Area`, `f_g_r: [F4|G:per-day|R-low]`.
  - **Content sections**: morning intent (Today's appetite + 1-3 high-leverage tasks); afternoon execution (cycle dispatch summary; surprises); evening reflection (what worked; what got dropped; methodology candidates surfaced).
  - **Cadence**: per day (event-driven on /plan-day OR /close-day skill invocation).
  - **Storage**: `daily-log/YYYY-MM-DD.md` per Bundle 1 Part 1 §H commit interface.
- Acceptance predicate: schema structurally complete; ≥1 synthetic daily-log fixture; commit via Part 1 §H; PARA-tier tagged.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack.
- **Reuses existing pattern**: `daily-log/` directory exists (1 file currently per AUDIT §X); `/plan-day`, `/close-day` skills exist; `shared/state/kanban.json` + `shared/state/priorities.json` exist. **CANONICALISE — do NOT reinvent.**
- Source: interface card §A-§B; FUNDAMENTAL §2.6 daily ops; product-management-cagan-shape-up consultant card §4 P3 Torres CDH continuous-discovery weekly customer touchpoint; levenchuk-shsm-fpf consultant card IP-7 writing-as-thinking; AUDIT-CURRENT-STATE daily-log baseline.

**Bullet P9.2 — Weekly review artefact schema with draft-disposition table (C2 producer side).**
- Output: §I.2 weekly-review schema declared inline + physical file `shared/schemas/weekly-review.json` (Phase B). Required content:
  - **Frontmatter fields**: `week: YYYY-Wnn`, `period_start, period_end`, `daily_logs_referenced: [<date>...]`, `projects_touched: [<slug>...]`, `methodology_candidates_surfaced: [{rule_slug, evidence_count}...]`, `attention_budget_summary: {avg_used, peaks}`, `appetite_actual_vs_planned: [{project_slug, ...}]`.
  - **Draft-disposition table** (C2 PRODUCER SIDE — Bundle 3 set CONSUMER side via Part 8 SLI/SLO; Bundle 4 sets PRODUCER side here):
    ```
    | Draft path | Created | Status | Disposition (accept | iterate | discard) | Rationale | Action taken |
    ```
    - `accept` = promote to canonical via Part 6b `gate_class: draft_promotion`
    - `iterate` = remain as draft for next cycle with append-only revision note
    - `discard` = remove from active queue (NOT delete file; mark archived)
  - **Content sections**: weekly retrospective (5 questions: what worked / what blocked / what got dropped / next-week appetite / methodology candidates); methodology promotion surfacing (cross-ref Part 5 strategies.md); SLA-tier review (cross-ref §I.3).
  - **Cadence**: per week (event-driven on Friday end-of-week OR Sunday start-of-next-week — owner picks; declared in §J).
  - **Storage**: `weekly-reviews/YYYY-Wnn.md` via Part 1 §H.
- Acceptance predicate: schema structurally complete; draft-disposition table per fixture; ≥1 synthetic weekly-review fixture with draft-disposition table populated; methodology promotion surfaced via fixture.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack.
- Source: interface card §A-§B; FUNDAMENTAL §2.5 weekly checkup cadence; sre-observability consultant card §4 P5 blameless postmortem (weekly review = postmortem culture); compounding-engineering consultant card §4 P5 methodology library promotion (weekly surfacing); Part 5 §A Inputs (Bundle 3 — weekly review feeds methodology promotion).

**Bullet P9.3 — 3-tier SLA taxonomy as canonical Foundation artefact.**
- Output: `.claude/config/sla-taxonomy.yaml` (config-driven per Company-as-Code D25 + Bundle 1 §I.2 pattern). Required content:
  - **L1 strategic**: Ruslan ack same-session (target: ≤4h synchronous); event examples (stage-gate ack on AWAITING-APPROVAL packets per FUNDAMENTAL §4.2-§4.3 human-only tasks); blast-radius typically Tier 1.
  - **L2 tactical**: batch ack weekly (target: ≤7 days); event examples (low-severity gate decisions; routine policy edits); blast-radius typically Tier 2.
  - **L3 routine**: auto-log (target: ≤immediate write to log); event examples (read-only intelligence ingest; CRM event log; daily-log commit); blast-radius typically Tier 3.
  - **Cross-references**: Part 6b §I.4 blast-radius 4-tier table (F8 LOCKED); Part 9 §J ritual.
- Acceptance predicate: file exists; 3 tiers declared with target latency + event examples + blast-radius mapping; cross-ref Part 6b.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack.
- Source: FUNDAMENTAL §4.2-§4.3 human-only tasks + 3-tier SLA; sre-observability consultant card §4 P4 toil < 50% owner time; stoic-epistemic consultant card Naval specific-knowledge filter (L1 = strategic; L2/L3 = delegate-able).

**Special: IP-2 single-owner bounded context (CRITICAL)**

Per FUNDAMENTAL §2.6 + Bundle 1 RUSLAN-ACK + FPF IP-2: Part 9 = **single-owner Phase A scope**.

- §X Foundation vs RUSLAN-LAYER MUST declare:
  - **Phase A bounded**: 1 owner (Ruslan); attention budget cap 20 active tasks (RUSLAN-LAYER specific value); all 3 SLA tiers calibrated to single-owner reaction time (RUSLAN-LAYER specific times: L1=≤4h, L2=≤7d, L3=immediate auto-log — these are RUSLAN-LAYER values; Foundation generic = the 3-tier STRUCTURE).
  - **Structural change ≥35% at >10× scale**: per Wave A Ashby BOSC-A-T-X analysis — 1 owner → 2+ owners triggers F.9 Bridge structural change; daily-log schema requires `owner_id` field; weekly review requires multi-owner aggregation; SLA tiers require per-owner calibration; attention-budget cap becomes per-owner.
  - **Phase B activation event**: sustained partner onboarding signal (1 owner → 2+ owners with >2 weeks operational evidence); F.9 Bridge work scoped at that point; Phase A operates SINGLE-OWNER until that event.
- Multi-owner stub fields declared in §I.1 + §I.2 (NOT implemented — Phase B work):
  - `daily-log.json` stub field: `// PHASE-B: owner_id: <ruslan|partner-N>` — commented out in Phase A schema; uncommented + populated in Phase B schema.
  - `weekly-review.json` stub field: `// PHASE-B: owners_aggregated: [<owner_id>...]`.
  - `sla-taxonomy.yaml` stub: `# PHASE-B: per-owner overrides supported via sla-taxonomy.<owner_id>.yaml fork pattern`.
- §X also declares Foundation generic vs RUSLAN-LAYER:
  - **Foundation generic**: daily-log/weekly-review/monthly-reflection schemas; attention-budget cap pattern (cap value = generic param); 3-tier SLA structure (tier names + ordering).
  - **RUSLAN-LAYER**: specific attention budget value (20 active tasks); specific SLA times (L1=≤4h, L2=≤7d, L3=immediate); Ruslan-specific Daily-log content patterns (Russian primary; specific morning-intent template).

**Special: C4 nomenclature fix**

Wave A Part 9 §D used `PhaseOf Part 6` for governance gate dependency. **Correct A.14 type = `methodologically-uses Part 6`** (Part 9 USES gate as service, is NOT exclusive pre-gate phase). Bundle 4 Part 9 §D applies fix verbatim — every Part 6 / Part 6a / Part 6b reference in Part 9 §D uses `methodologically-uses` not `PhaseOf`. Cross-ref dependency-graph §3.4 C4 + brigadier autocheck rejects `PhaseOf Part 6` in Part 9.

### §2.3 Part 10 — External Touchpoints & Network Interface (4 bullets)

**Source**: wave-c-worklist §2 Part 10.
**Interface card**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md`.

**Bullet P10.1 — L.1-L.3 integration adapter stubs.**
- Output: Part 10 architecture document at `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` (10K-20K words; likely larger end given CRM canonicalisation + privacy sub-section). Adapter stubs declared inline at §H + §I:
  - **RT-1 read-only intelligence trackers**: pattern for HN / sub-Reddit / niche newsletter ingest. Adapter shape: poll URL → parse → emit signal to Part 2 `/ingest` triage queue. Read-only side-effect rule: NEVER writes externally. Tier 3 blast-radius (auto-log).
  - **RT-2 write-ack action coordinators**: pattern for Linear / GitHub / Slack / partner email outbound. Adapter shape: receive request → verify CRM consent (`consent_recorded_at` field present) → blast-radius classify → AWAITING-APPROVAL `gate_class: stage_gate` packet to Part 6b → on Ruslan ack → external write → write-ack confirmation logged to CRM event log + approval log + cross-fork-provenance log.
  - **L.1 Linear adapter** stub: ticket creation / comment posting / status update.
  - **L.2 GitHub adapter** stub: issue creation / PR creation / comment posting.
  - **L.3 Slack/email adapter** stub: DM send / channel post / email send.
- All stubs: SPECIFICATION (request shape + response shape + error modes), NOT IMPLEMENTATION (Phase B materialisation per OQ-MERGED-5 specify-and-stub pattern from Bundle 3 Part 8). NO auth tokens hardcoded; auth-token reference points to `private/<service>-auth.yaml` (RUSLAN-LAYER fork; Foundation declares the pattern).
- Acceptance predicate: 5 adapter stubs declared (RT-1 + RT-2 patterns + 3 service-specific L.1/L.2/L.3); each declares request/response/error-mode; blast-radius assignment; consent verification step for RT-2; auth-token externalisation declared.
- F-G-R: F4 architecture-time → F5 on first Phase B integration adapter live.
- Source: interface card §A-§B; anthropic-constitutional-ai consultant card write-ack mandatory before external action; multi-agent-architecture consultant card MCP for tool invocation (A2A inter-agent delegation = OQ-CONFLICT-4 Phase B flag); levenchuk-shsm-fpf consultant card IP-2 bounded context with explicit Bridge F.9.

**Bullet P10.2 — C3 Phase-A boundary clarification.**
- Output: Part 10 §F Anti-scope section declares verbatim:
  - **Phase A inbound external = Phase B work.** Phase A external touchpoints are OWNER-INITIATED ONLY (Ruslan triggers via `/ingest <url>` via Part 2 OR triggers external write via Part 10 RT-2 with explicit ack).
  - **Phase A external system NEVER auto-acts on inbound external signals** — no auto-reply on email; no auto-comment on GitHub; no auto-Linear-status-update from external webhook.
  - **Phase B activation event**: sustained operational maturity signal (Phase A operational ≥3 months; Tier 0 health-integrity events <1 per quarter; methodology library ≥10 entries F5).
  - **Cross-references**: Part 2 `/ingest` is the ONLY Phase A inbound path; Part 6b `gate_class: stage_gate` is mandatory for all RT-2 write-acks.
- Acceptance predicate: §F declares 3 rules verbatim; cross-references C3 dependency-graph + Part 2 §A.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack.
- Source: dependency-graph §3 C3; interface card §F; FUNDAMENTAL §6 anti-scope.

**Bullet P10.3 — Privacy architecture declaration (STRUCTURAL, not behavioral).**
- Output: §I sub-section (preferred — consolidates with main Part 10 architecture) OR companion file `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/privacy-architecture.md` (acceptable; brigadier picks based on length — if §I expansion exceeds 4K words, companion file preferred). Required content per FUNDAMENTAL §6.4:
  - **Privacy invariant 1 — Consent enforcement**: Schema field `consent_recorded_at: <ISO timestamp>` MANDATORY in CRM contact record before any RT-2 write-ack adapter fires. Lint signal `/lint --check-consent` (Phase B implementation; skill spec only). Default-Deny entry: external write attempt without `consent_recorded_at` = HALT + AWAITING-APPROVAL `gate_class: stop_gate` (Tier 1 escalation).
  - **Privacy invariant 2 — Forget-request**: `/crm forget --contact <id>` skill spec (Phase B). Behaviour: purge contact record + propagate to all references (CRM event log entries marked `[REDACTED]`; cross-fork-provenance entries flagged `consent-revoked-cascade`; wiki references stripped via `/lint --check-forget-request-cascade`). Reversal Transactions discipline: forget-request = NEW entry with `corrects: <original-entry-id>` + `redaction_reason: forget-request` (Young 2010 — never delete history; mark redacted).
  - **Privacy invariant 3 — Encryption at rest**: Part 1 substrate level (file-system encryption assumption — NOT Foundation responsibility; declared as PRECONDITION). Foundation responsibility = ensure no plaintext secrets committed (cross-ref Bundle 1 API-key audit pattern in §9 commit discipline).
  - **Privacy invariant 4 — NO inference of protected characteristics**: Lint signal `/lint --check-protected-inference` (Phase B implementation; skill spec). Default-Deny entry per Part 6b §I.3: any classifier on race / religion / political affiliation / health status = Tier 0 hard halt (NEVER Tier 1+ acknowledgeable; structural prohibition not policy preference). Schema-level enforcement: CRM contact record schema has NO field for protected characteristics; lint signal flags any RUSLAN-LAYER fork that adds such fields.
- These are STRUCTURAL (schema fields + lint signals + Default-Deny entries), NOT BEHAVIORAL ("we promise to be careful"). Brigadier autocheck rejects any Part 10 privacy section that uses behavioral framing prose without structural enforcement.
- Acceptance predicate: 4 invariants declared; each has schema field OR lint signal OR Default-Deny entry; behavioral framing prose <10% of section; cross-refs to FUNDAMENTAL §6.4 + Part 6b §I.3.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack; F-level rises F5→F8 on Phase B `/lint --check-protected-inference` first run validating zero violations.
- Source: FUNDAMENTAL §6.4 privacy hard rules; anthropic-constitutional-ai consultant card §5 T3 fail-loud + privacy constraints + hardcoded never-list; Bundle 1 Part 6b §I.3 default-deny F8 LOCKED; Askell HHH (Bundle 1 corrigibility F8).

**Bullet P10.4 — OQ-MERGED-3 fork-separation checklist — FINAL CLOSURE for Foundation.**
- Output: Part 10 §X Foundation vs RUSLAN-LAYER section. **MANDATORY explicit examples** (critic gate auto-rejects ambiguous):
  - **Foundation generic**:
    - CRM data model (contact record schema fields except RUSLAN-LAYER overlay; relationship-edge taxonomy)
    - CRM 8 edge types per `crm/_schema/edges.yaml` (UND-5 binding to Part 3 typed-edge taxonomy)
    - Integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3 stubs at SHAPE level — request/response/error-mode)
    - Privacy invariants (FUNDAMENTAL §6.4 4 invariants — consent / forget / encryption / no-protected-inference)
    - Write-ack discipline (RT-2 mandatory consent verification + AWAITING-APPROVAL `gate_class: stage_gate`)
    - 10 `/crm-*` skills SHAPE (skill names + arg patterns; NOT specific contact-list bindings)
  - **RUSLAN-LAYER (DACH ICP specifics)**:
    - **DACH ICP parameters**: `crm/_schema/icp.yaml` declares "ICP = DACH consulting clients; fintech/insurtech focus; 10-100 employees; English/German" — these are RUSLAN-LAYER values; Foundation generic = the ICP schema STRUCTURE.
    - **German GDPR config**: `crm/_schema/gdpr.yaml` declares "GDPR data-residency = EU; right-to-be-forgotten = explicit /crm forget pathway; data-processor agreements = required for partner forks" — these are RUSLAN-LAYER values per German jurisdiction; Foundation generic = the GDPR schema STRUCTURE + the privacy invariants of §I above.
    - **Specific contact lists**: `crm/people/*.md` and `crm/orgs/*.md` files = RUSLAN-LAYER (own contacts; partner forks have own contacts).
    - **Linear/GitHub/Notion/Slack auth tokens**: `private/<service>-auth.yaml` files = RUSLAN-LAYER; Foundation generic = the auth-token externalisation pattern (path convention; rotation policy; secret-scan compliance).
    - **DACH-specific intelligence tracker URLs**: HN / r/Berlin / r/germany / specific niche newsletter URLs = RUSLAN-LAYER; Foundation generic = the RT-1 adapter pattern.
- Acceptance predicate: §X explicit examples per category (Foundation 6 entries + RUSLAN-LAYER 5 entries); critic gate auto-verifies DACH/GDPR/auth-token/contact-list/intelligence-URL examples present; ambiguous = re-dispatch.
- F-G-R: F4 architecture-time → F5 on Bundle 4 owner ack; **F-level rises F5→F8 only after Phase B partner fork imports Foundation generic + declines RUSLAN-LAYER + reconciliation strategy applied** (per OQ-MERGED-3 closure validation).
- Source: OQ-MERGED-3 Wave A Ruslan ack 2026-04-27; AUDIT-CURRENT-STATE §6 CRM operational baseline; CLAUDE.md CRM section (24 source files / 35 unit tests / 10 skills / 4 schemas).

**Special: OQ-B1-5 D27 reconciliation field promotion (deferred from Bundle 1)**

`cross-fork-provenance.json` (Part 1 §I.1 — Bundle 1 + supplement) currently has `approvals_reconciliation_strategy` in `metadata` open field. Bundle 4 Part 10 §I.1 PROMOTES to top-level + documents reconciliation strategies per partner-fork import scenario:

- **Top-level field**: `approvals_reconciliation_strategy: <enum>` per cross-fork-provenance entry.
- **5 reconciliation strategies declared**:
  1. `parent-wins`: Foundation parent ack supersedes fork's local ack (used for Foundation invariants like privacy + corrigibility + Halt-Log-Alert ordering).
  2. `fork-wins`: Fork's local ack supersedes Foundation parent (used for RUSLAN-LAYER ICP-specific values when partner has different ICP).
  3. `manual-merge`: HITL Ruslan + partner pair-resolve via AWAITING-APPROVAL `gate_class: stage_gate` (used for cross-cutting changes affecting both Foundation + RUSLAN-LAYER).
  4. `decline-import`: Fork explicitly declines Foundation's ack (used for Foundation patterns inappropriate for fork's domain).
  5. `pending-review`: Fork holds ack for next sync window (default state pre-resolution).
- **Phase B explicit**: this schema field is FOUNDATION-LEVEL declarative; reconciliation actions are PHASE B work (no Phase A reconciliation events since Phase A is single-owner with no partner fork).
- **Constitutional supplement record** (END-OF-CYCLE — analogous to OQ-B2-A pattern but inverted timing):
  - File: `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md` (XX = day of completion).
  - Single commit at end of Bundle 4 cycle (after all 3 architecture documents land + AWAITING-APPROVAL packet drafted; commit message `[architecture] Bundle 1 retroactive supplement 2 — cross-fork-provenance.json approvals_reconciliation_strategy field promotion top-level (per OQ-B1-5 RUSLAN-ACK Bundle 1)`).
  - Edits Part 1 §I.1 schema declaration in-place.
- Brigadier autocheck rejects Bundle 4 ship without supplement record landing.

**Special: CRM operational baseline (cycle 10) — canonicalisation NOT redesign**

CRM is OPERATIONAL — cycle 10 already shipped:
- 24 source files in `crm/`
- 35 unit tests (`crm/_tests/`)
- 10 `/crm-*` skills (`/crm-add`, `/crm-show`, `/crm-list`, `/crm-search`, `/crm-touch`, `/crm-update`, `/crm-rebuild-index`, `/crm-dash`, `/crm-stuck`, `/crm-weekly`)
- 4 YAML schemas in `crm/_schema/` (frontmatter / roles / statuses / strategy-hooks; PLUS edges.yaml per UND-5 binding)
- `crm/_scripts/crm.py` + `crm/_scripts/voice_router.py`
- `crm/log.md` append-only event log
- 24 roles / 13 pipeline statuses / 6 strategy-hook offers + 6 strategy-hook asks
- Cross-cutting wiki/graph/edges.jsonl 8 CRM edge types
- Voice integration via `tools/run_pipeline.sh` step 3 (DRAFT-only; promote manual)

Part 10 architecture **CANONICALISES** this existing implementation:
- §A Inputs: lists existing CRM tree + voice pipeline + projects (cross-cutting)
- §B Outputs: lists 10 `/crm-*` skill emit shapes + edges + log entries
- §H Code interfaces: references existing `crm/_scripts/crm.py` + `voice_router.py` API (CANONICALISES — does NOT modify)
- §I Data schemas: references existing 4 YAML schemas (CANONICALISES + adds edges.yaml UND-5 declaration)
- §N Provenance: full citation trail to `crm/README.md` + `crm/PLAN.md` + `swarm/awaiting-approval/cycle-10-crm-build-2026-04-26.md`

**DO NOT REDESIGN.** Brigadier autocheck rejects Part 10 producing alternative CRM data model. If improvements surface from Wisdom Loop → log as OQ-B4-X for Wave D consideration; do NOT re-implement in Bundle 4.

### §2.4 Cross-cuts within Bundle 4 (re-stated for emphasis)

- **F-G-R DOGFOOD per F8 schema** — every architecture claim in Parts 7+9+10 has F-G-R per Part 6a §I.1 schema.
- **A.14 typed edges** — Bundle 1 canonical 10-edge reference table consulted; NO new edge types invented; NO generic `depends-on`. **C4 fix applied** in Part 9 §D verbatim. Bundle 4 specific edge usage examples:
  - Part 7 `creates` Part 5 (project closure → retrospective packet → Part 5 DRR consumption — UND-3 finalization)
  - Part 7 `methodologically-uses` Part 6b (stage-gate transitions → AWAITING-APPROVAL packets)
  - Part 7 `methodologically-uses` Part 4 (cycle dispatch → task-return-packet aggregation)
  - Part 7 `derives-from` Part 1 §H (commits via §H interface)
  - Part 9 `methodologically-uses` Part 6b (C4 FIX — was `PhaseOf` in Wave A; corrected to `methodologically-uses`)
  - Part 9 `methodologically-uses` Part 5 (weekly review surfaces methodology candidates)
  - Part 9 `creates` Part 1 (daily-log + weekly-review committed via Part 1 §H)
  - Part 10 `methodologically-uses` Part 3 (CRM edges to wiki/graph/edges.jsonl — UND-5)
  - Part 10 `methodologically-uses` Part 6b (RT-2 write-ack via stage-gate)
  - Part 10 `methodologically-uses` Part 2 (C3 — inbound external via /ingest)
  - Part 10 `methodologically-uses` Part 1 (cross-fork-provenance + commit interface)
  - Part 10 `creates` Part 1 (CRM events committed; cross-fork-provenance entries committed)
- **Append-only** — project-retrospective-packets / daily-logs / weekly-reviews / CRM event log / approval log — append-only; corrections via Reversal Transactions.
- **L/A/D/E** — every §E section structured per FPF A.6.B Norm Square.
- **§X Foundation vs RUSLAN-LAYER FINAL CLOSURE** — explicit per part. Part 7 Foundation = state-machine + stage-gate predicates + appetite + scope-record schema + resource templates; RUSLAN-LAYER = 8 active project specifics + specific appetite values + specific resource allocations. Part 9 Foundation = daily-log/weekly-review/SLA-tier schemas + attention-budget cap pattern; RUSLAN-LAYER = specific budget=20 + specific SLA times + Russian-primary content patterns. Part 10 Foundation = CRM data model + edge types + adapter pattern + privacy invariants + write-ack discipline; RUSLAN-LAYER = DACH ICP / German GDPR / contact lists / Linear+GitHub+Notion auth tokens / DACH intelligence URLs.
- **PARA-tier mandatory** — Part 9 daily-log / weekly-review entries tagged; Part 10 CRM contacts tagged.
- **OQ-MERGED-2 dissolve-test evidence Cycle 2** — Bundle 4 brigadier MUST log evidence file `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-4/dissolve-test-evidence-cycle-2.md` accumulating compound-phase-exclusive operations observed during Bundle 4 cycle. Threshold check happens at Wave D (Cycle 3).

---

## §3 Required Reading — MANDATORY before first dispatch

Brigadier MUST read these BEFORE any subagent dispatch. Each pre-read MUST be cited in output. Subagent dispatches MUST instruct experts to read RELEVANT subsets only.

### §3.1 Constitutional baseline (full-read mandatory)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0) — esp. **§2.6 daily ops single-owner**, **§3 SLI/SLO 30+ pairs**, **§4.2-§4.3 human-only tasks + 3-tier SLA**, **§6.4 privacy hard rules** (Part 10 P10.3 binding)
2. `design/JETIX-FPF.md` — **IP-2 bounded context** (Part 9 binding), **IP-5 past-participle states** (Part 7 P7.2 binding), **IP-7 writing-as-thinking** (Part 9 daily-log + weekly-review domain), A.6.B L/A/D/E, A.14 typed edges (canonical 10-edge table; **C4 fix Part 9**)
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (**ESPECIALLY §6 CRM section** — Part 10 baseline canonicalisation; §3 projects directory baseline for Part 7; §X daily-log baseline for Part 9)
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (§4.5 deep-study constraint at 10K-20K F8)
5. **All 8 LOCKED architectures (Bundles 1+2+3) — constitutional inputs:**
   - `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (esp. §H commit interface; §I.1 cross-fork-provenance.json — OQ-B1-5 promotion target; §I.2 commit-format-tokens.json; §I.4 task-return-packet stub post-supplement; §K K15+K18 failure modes)
   - `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (F-G-R schema F8 DOGFOOD; approval log; quarterly immune audit framework)
   - `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (gate_class enum F8; Default-Deny F8; blast-radius 4-tier F8; Halt-Log-Alert L9 F8; Corrigibility F8; AWAITING-APPROVAL packet F8)
   - `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` (PARA-tier discipline; anchor-mandatory; STOP-gate; **C3 cross-ref Part 10**)
   - `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` (`wiki/methodology/` entity-type; **wiki/graph/edges.jsonl typed-edge taxonomy — UND-5 Part 10 binding**; accessor pipeline ownership)
   - `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (routing-table.yaml; **task-return-packet.json schema F4 — Part 7 SUPERSET binding via UND-3 finalization**; executor-binding template; message schema v2.0.0)
   - `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` (compound ritual 40/10/40/10; methodology promotion pipeline UND-2; **§A Inputs Part 7 stub — UND-3 finalization target**; dissolve-test condition F3)
   - `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` (canonical health-signal schema F5 §I.1; SLI/SLO schema §I.2; alert-routing stub §H; specify-and-stub scope discipline)
6. **All RUSLAN-ACK records (MANDATORY READ):**
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (§3 F-promotions; §4 Constitutional consequences; §6 hard rules + Default-Deny constitutional anchor)
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` (Part 1 §I.4 enum + commit-format-tokens [swarm-lib]+[health]+[methodology] + K18 upcasting)
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` (esp. **§3 WORD COUNT TARGET 10K-20K F8**; §1 Decisions #1-#7; §2 OQ-B2-A through OQ-B2-F status)
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md` (esp. §1 13 specific decisions; **C2 + UND-2 + UND-3 stub closure**; **TRADEOFF-01 split F8**; OQ-MERGED-2 dissolve-test active; OQ-MERGED-5 specify-and-stub held)
7. Locks D17 (Notion read-only), D26 (hub-and-spoke), **D27 (forkable + ICP external — Part 10 binding)**, D29 (Korp-Startup), most recent `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`

### §3.2 Wave A artefacts (full-read mandatory)

1. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`
2. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md` (esp. §2 P7 + §2 P9 + §2 P10)
3. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` (esp. **§3.3 C3 P10 inbound external** — defer Phase B; **§3.4 C4 P9 PhaseOf → methodologically-uses** — Bundle 4 fix; **§4.3 UND-3** — finalization here; §4.5 UND-5 P10 CRM edges; §6.4 routing structural change risk)
4. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` (esp. **§2 P7** + **§2 P9** + **§2 P10** bullets — sources of truth for the 10 bullets; §3 Bundle composition; §4 cross-bundle dependencies; §6 OQs)
5. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md` (esp. §2 Part 7 verdict + §2 Part 9 verdict + §2 Part 10 verdict; §4 OQ-MERGED-3 fork-separation; OQ-5 cadence event-driven)
6. **Wave A interface cards for Bundle 4 parts:**
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-7-project-lifecycle-substrate.md`
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md`
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-10-external-touchpoints-network-interface.md`
7. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/` (5 files: engineering / investor / mgmt / philosophy / systems)

### §3.3 Wave B consultant cards (per Manifest §2 matrix)

**For Part 7 dispatches** (engineering + philosophy + investor + mgmt + systems):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md` — **PRIMARY** — Shape Up appetite-as-CONSTRAINT (NOT estimate); Outcome over Output; betting-table rhythm; 2-6 week appetite cycles
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-5 past-participle alpha state machine; A.3 Transformer Quartet for transitions; IP-2 bounded context for project ownership
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md` — Young 2010 — project state transitions as events; reversal transactions for scope corrections
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md` — Dichotomy-of-control: project scoped to what Ruslan controls; outcome not guaranteed (anti-pseudo-certainty)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md` — UND-3 retrospective input contract; Plan/Work/Review/Compound main loop

**For Part 9 dispatches** (engineering + philosophy + investor + mgmt + systems):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md` — Torres CDH continuous discovery; weekly customer touchpoint slot; OKR cadence for weekly review
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — **PRIMARY** — IP-7 writing-as-thinking for strategic reflection; **IP-2 bounded context for daily-log scope (single-owner Phase A)**; F.9 Bridge structural change ≥35%
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md` — Naval specific knowledge filter (L1 strategic vs L2/L3 delegate-able); dichotomy-of-control for daily intent
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md` — toil < 50% of owner time; alert delivery path for Tier 1 SLA
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md` — Forte PARA tagging for daily-log entries

**For Part 10 dispatches** (engineering + philosophy + investor + mgmt + systems):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` — **PRIMARY** — Privacy constraints; write-ack mandatory before external action; hardcoded never-list (protected characteristics Default-Deny Tier 0); §5 T3 fail-loud
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-2 bounded context with explicit Bridge F.9; A.14 typed edges for CRM-to-wiki cross-refs (UND-5)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md` — Typed CRM graph edges per wiki/graph/edge-types.md; UND-5 binding to Part 3
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md` — Forte PARA: contacts in Resource (relationship asset) or Project (active deal) tier, NOT KB concepts layer
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md` — A2A open question (MCP for tool invocation vs A2A for inter-agent delegation; OQ-CONFLICT-4 Phase B flag); integration adapter pattern

### §3.4 Wave B Supplement library-direct sources (Bundle 4 critical)

1. **`raw/books-md/anthropic/bai-2022-cai.md`** — Constitutional AI: RLAIF for Part 10 external action self-critique pattern (write-ack draft → CAI critique pass → if violations detected → halt before external action fires)
2. **`raw/books-md/anthropic/askell-2021-hhh.md`** — Helpful-Honest-Harmless: corrigibility (Part 10 NEVER auto-acts on external surfaces without human-ack); hardcoded never-list pattern for protected characteristics
3. **`raw/books-md/event-sourcing/young-cqrs-2010.md`** — Project state transitions as events for Part 7; reversal transactions for scope corrections + privacy forget-request (Part 10)
4. **`raw/books-md/sre/google-sre-book.md`** — Ch.6 monitoring (Part 9 health alerts to owner via SLA-tier routing); Ch.15 postmortems (Part 9 weekly review = postmortem culture)
5. **`raw/books-md/sre/google-srewb-implementing-slos.md`** — Ch.2 burn-rate algebra for Part 9 SLA tiers (analogous; Bundle 3 Part 8 §I.2 already adopted; Part 9 inherits)

### §3.5 Existing operational artefacts (audit reference, do not duplicate)

- **CRM TREE (Part 10 baseline — DO NOT REINVENT):**
  - `crm/` (24 source files)
  - `crm/_schema/` (4 YAML schemas: frontmatter / roles / statuses / strategy-hooks; PLUS edges.yaml UND-5)
  - `crm/_scripts/crm.py` + `crm/_scripts/voice_router.py`
  - `crm/log.md` (append-only event log)
  - 10 `/crm-*` skills (per CLAUDE.md CRM section)
  - 35 unit tests (`crm/_tests/`)
  - `crm/README.md` + `crm/PLAN.md` (authoritative spec)
- **Voice pipeline (Part 2 baseline already canonicalised in Bundle 2):**
  - `tools/transcribe.py` / `extract.py` / `filter.py` / `run_pipeline.sh`
- **Project artefacts (Part 7 baseline):**
  - `projects/` directory
  - `.claude/config/project-types.yaml` (4 types: consulting / research / product / bets)
  - `swarm/wiki/_templates/project-*/` (4 template trees)
  - `/project-bootstrap`, `/project-review`, `/project-archive`, `/project-de-morph`, `/project-promote` skills
- **Owner artefacts (Part 9 baseline):**
  - `daily-log/` directory (1 file currently per AUDIT)
  - `shared/state/kanban.json`
  - `/plan-day`, `/close-day` skills
  - `shared/state/priorities.json`

---

## §4 Phase Architecture (matrix dispatch + Wisdom Loop + critic gate + M-gates)

Standard ROY cycle = **integrator → critic → finalize**. **For Bundle 4, brigadier MUST insert THREE structural phases beyond Bundle 3 patterns: NO retroactive supplement first task (clean substantive start unlike Bundle 3); the Wisdom Application Loop with ≥85% target inherited from Bundle 3 (§5); the M5 inter-Part lite coherence check (post-integrator, pre-critic — NOT separate phase); and the END-OF-CYCLE OQ-B1-5 D27 supplement record commit.**

### §4.0 NO Phase ZERO retroactive supplement (clean substantive start)

Unlike Bundle 3 which had to apply OQ-B2-A retroactive Bundle 1 corrections at Phase 0, Bundle 4 has a **clean substantive start**:

- Bundle 1 supplement is committed (`ca38be3`).
- Bundle 3 supplement is committed (Bundle 3 cycle delivered K18 + commit-format-tokens [swarm-lib]+[health]+[methodology] + Part 1 §I.4 enum alignment).
- **OQ-B1-5 D27 `approvals_reconciliation_strategy` field promotion is END-OF-CYCLE** (commits AFTER all 3 architecture documents land + AWAITING-APPROVAL packet drafted; analogous to OQ-B2-A pattern but inverted timing).

Brigadier proceeds DIRECTLY to Phase A pre-read confirmation. No blocking gate at Phase 0.

### §4.1 Phase sequence per part (sequential by default; parallelisable within HD-02 N=2)

For each Part (7, 9, 10) execute in this order. NOTE: Parts 7 + 9 + 10 are LARGELY INDEPENDENT — UND-3 finalization (Part 7 ↔ Part 5) is M5 lite coherence check (post-integrator); C4 nomenclature fix (Part 9 §D) is autocheck; OQ-B1-5 D27 promotion (Part 10 ↔ Part 1) is END-OF-CYCLE supplement. **Brigadier may dispatch 2 parts in parallel within HD-02 N=2.**

1. **Phase A — Pre-read confirmation** — brigadier reads §3 mandatory; dispatch instructs each expert to read RELEVANT subset only (per §3.3 mapping).
2. **Phase B — Matrix dispatch (5 experts × 4 modes = up to 20 cells)** — per ROY-ALIGNMENT §3 row mapping. Not every cell fires; brigadier picks cells that genuinely add signal. Minimum 8 cells per part.
3. **Phase C — Integrator** — brigadier (or delegated integrator-mode expert) merges cell outputs into draft architecture per §6 quality bar.
4. **Phase C+ — M5 inter-Part lite coherence check** — see §4.4. Verifies UND-3 finalization (Part 7 §B emit ↔ Part 5 §A input); C4 nomenclature fix (Part 9 §D `methodologically-uses Part 6`); OQ-B1-5 D27 schema cross-ref consistency (Part 10 §I.1 ↔ Part 1 §I.1). NO separate phase like Bundle 2 Joint Design — runs inline post-integrator pre-critic.
5. **Phase D — Wisdom Application Loop** — see §5. **Bundle 4 inherits Bundle 3 ≥85% operational floor** (Compound Learning + Health Monitoring achieved 100% — Bundle 4 should match given P7+P9+P10 are inherently operational).
6. **Phase E — Critic gate** — ≥2 experts in critic-mode review draft + Wisdom edits. Stricter cargo-cult check + 3 Bundle 4 autochecks (Part 7 cadence event-driven §6.7; Part 9 IP-2 multi-owner stub §6.8; Part 10 fork-separation FINAL CLOSURE §6.9 + privacy structural §6.10).
7. **Phase F — Finalize** — brigadier promotes draft → canonical at `swarm/wiki/foundations/<part-slug>/architecture.md`.
8. **Phase G — M-gates per part** — M1 smoke, M2 cross-ref. (M3 + M4 + M5 + M6 run at bundle level in §7.)
9. **Phase H — END-OF-CYCLE OQ-B1-5 D27 supplement record** — see §4.5. Single commit at end of cycle; Part 10 §I.1 references; supplement record drafted at `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md`.

### §4.2 Cell selection guidance per part

**Part 7** (Project Lifecycle): engineering (critic — schema integrity + state-machine atomic transitions; clean-code — past-participle naming consistency; integrator; scalability — appetite cap at >10× project count), mgmt (boundary — Part 7 vs Part 4 dispatch ownership; integrator on cadence-event-driven binding; ethics-surface — appetite-as-CONSTRAINT philosophy), philosophy (epistemic audit on Shape Up appetite-as-NOT-estimate; first-principles on event-driven cadence; critic on UND-3 finalization), systems (cybernetics — project lifecycle as Beer VSM S2 coordination; emergence — adjacent-possible projects per Kauffman; integrator on stage-gate-event causality), investor (capital-allocation — appetite as portfolio asset; long-term-compounding — closure events feeding compound loop). **Minimum 9 cells** (heaviest: P7.1 schema + UND-3 finalization).

**Part 9** (Owner Interaction): philosophy (PRIMARY — IP-7 writing-as-thinking; epistemic audit on daily reflection cadence; first-principles on attention-budget-cap discipline; critic on dichotomy-of-control framing), engineering (critic — daily-log/weekly-review schema integrity + IP-2 multi-owner stub fields specification; integrator), mgmt (boundary — Part 9 vs Part 4 cycle dispatch; integrator on 3-tier SLA mapping to blast-radius; ethics-surface — surveillance footprint of daily-log content), systems (cybernetics — Beer VSM S5 owner identity binding; Ashby variety — single-owner attention-budget cap matches Phase A throughput; integrator on F.9 Bridge multi-owner trigger), investor (capital-allocation — owner attention as primary capital; antifragility — weekly review as stressor surfacing; long-term-compounding — methodology promotion via weekly review). **Minimum 9 cells** (heaviest: IP-2 single-owner declaration + multi-owner stub fields + C4 nomenclature fix application).

**Part 10** (External Touchpoints): philosophy (PRIMARY — privacy as STRUCTURAL not behavioral; epistemic audit on protected-characteristic Default-Deny; first-principles on consent enforcement; critic on fork-separation FINAL CLOSURE), engineering (critic — CRM data model canonicalisation, scalability — integration adapter pattern at Phase B scale, integrator — RT-1/RT-2 stub specification), systems (cybernetics — Part 10 as VSM S4 environment scanner; Ashby variety — privacy invariants as structural variety dampener; integrator on UND-5 CRM-to-wiki edge binding), investor (capital-allocation — CRM as relationship asset; antifragility — privacy structural enforcement as stressor-resistant moat; long-term-compounding — CRM event log as compound asset), mgmt (boundary — Part 10 Foundation generic vs RUSLAN-LAYER fork-separation FINAL CLOSURE; integrator — write-ack discipline + AWAITING-APPROVAL stage_gate routing; ethics-surface — DACH GDPR compliance + surveillance footprint). **Minimum 11 cells** (heaviest: P10.3 privacy structural + P10.4 fork-separation FINAL CLOSURE + CRM canonicalisation + OQ-B1-5 D27 cross-ref).

### §4.3 NO Joint Design Phase (M5 inline coherence)

Unlike Bundle 2 (C1 BLOCKING contradiction → 2h Joint Design) and Bundle 3 (C2 + UND-3 carry-over → 1h Joint Design lite), Bundle 4 has NO Joint Design Phase. Reasoning:

- **UND-3 is finalization not BLOCKING contradiction** — Bundle 3 set Part 5 §A input expectations + UND-3-stub.md; Bundle 4 Part 7 §B EMIT contract conforms. M5 lite coherence check (post-integrator, pre-critic) verifies conformance — no joint design needed.
- **C4 nomenclature fix is autocheck not joint design** — Wave A Part 9 §D `PhaseOf Part 6` corrected to `methodologically-uses Part 6`. Brigadier autocheck rejects `PhaseOf Part 6` in Part 9.
- **OQ-B1-5 D27 promotion is END-OF-CYCLE supplement not joint design** — Part 10 §I.1 declares; supplement record commits at end of cycle.

If during Phase B/C unexpected cross-bundle incoherence surfaces (e.g., Part 7 §B emits fields that Part 5 §A doesn't accept; Part 10 §I.1 D27 promotion conflicts with Part 1 §I.1 schema): **escalate to brigadier-mode arbitration**; if unresolved → Ruslan ack required (write `swarm/wiki/foundations/<part-slug>/oq-bundle-4-N.md` and HALT for HITL).

### §4.4 M5 inter-Part lite coherence check (post-integrator, pre-critic)

After Phase C integrator drafts for Part 7 + Part 9 + Part 10 are produced (sequentially OR in parallel HD-02 N=2):

1. **UND-3 finalization check**: Part 7 §B `project-retrospective-packet.json` schema fields are SUPERSET of Part 5 §A expected fields. Brigadier reads Part 5 §A (Bundle 3 LOCKED) + Part 7 §B (Bundle 4 draft) + Bundle 3 UND-3-stub.md. Verifies:
   - Part 5 §A expected fields all present in Part 7 §B (`project_id`, `state_transition`, `appetite_actual_vs_planned`, `lessons_learned`, `dr_r_candidates`)
   - Part 7 §B EXTENDS Part 4 task-return-packet.json (subset relationship F4 LOCKED)
   - Part 7 §J cadence (per closure event + per cycle boundary) compatible with Part 5 §J compound-phase trigger predicate
   - Bundle 3 UND-3-stub.md updated F2→F4 with Part 7 conformance reference
2. **C4 nomenclature fix check**: Part 9 §D every Part 6 reference uses `methodologically-uses` not `PhaseOf`. Brigadier greps `PhaseOf Part 6` + `PhaseOf Part 6a` + `PhaseOf Part 6b` in Part 9 draft → 0 hits required.
3. **OQ-B1-5 D27 cross-ref check**: Part 10 §I.1 references `cross-fork-provenance.json` schema (Part 1 §I.1) with `approvals_reconciliation_strategy` promoted to top-level. Part 1 §I.1 supplement edit drafted (commits at Phase H end-of-cycle). Verifies:
   - Part 10 §I.1 declares 5 reconciliation strategies (parent-wins / fork-wins / manual-merge / decline-import / pending-review)
   - Part 1 §I.1 supplement edit prepared (uncommitted at Phase C+ time; commits at Phase H)
   - Cross-fork-provenance.json physical file Phase B materialisation declared

If any check fails: brigadier returns to integrator with explicit feedback citing the specific incoherence.

### §4.5 Phase H — END-OF-CYCLE OQ-B1-5 D27 supplement record (single commit)

After all 3 architecture documents land + Wisdom Loop applied + critic gate passed + M-gates passed + AWAITING-APPROVAL packet drafted:

1. **Edit Part 1 §I.1** in `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`:
   - Promote `approvals_reconciliation_strategy` from `metadata` open field to top-level field in `cross-fork-provenance.json` schema declaration.
   - Add 5 reconciliation strategy enum values (parent-wins / fork-wins / manual-merge / decline-import / pending-review).
   - Cross-reference Part 10 §I.1 (Bundle 4 declared the strategies operationally).
2. **Create supplement record** `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md` (XX = day of completion):
   ```markdown
   ---
   title: RUSLAN-ACK Wave C Bundle 1 supplement 2 — cross-fork-provenance.json approvals_reconciliation_strategy field promotion top-level (per OQ-B1-5)
   date: 2026-04-XX
   type: ruslan-ack-supplement
   parent_ack: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
   triggered_by: Bundle 4 Part 10 §I.1 + AWAITING-APPROVAL Bundle 4
   status: awaiting-ruslan-ack-with-bundle-4
   ---

   ## §1 Retroactive correction per OQ-B1-5 (applied 2026-04-XX at Bundle 4 cycle end)

   - Part 1 §I.1 cross-fork-provenance.json: `approvals_reconciliation_strategy` promoted from `metadata` open field to top-level field
   - 5 reconciliation strategies declared: parent-wins / fork-wins / manual-merge / decline-import / pending-review
   - Cross-referenced from Part 10 §I.1 (Bundle 4 operational declaration)
   - Commit hash: <new>
   ```
3. **Single commit**:
   ```
   [architecture] Bundle 1 retroactive supplement 2 — cross-fork-provenance.json approvals_reconciliation_strategy field promotion top-level (per OQ-B1-5 RUSLAN-ACK Bundle 1)
   ```
4. **Push** to `claude/jolly-margulis-915d34`.
5. **Update AWAITING-APPROVAL Bundle 4 packet** to reference the supplement commit hash.

### §4.6 Dissent preservation (AP-6)

If any expert in critic-mode produces dissent that integrator could not resolve: preserve in `swarm/wiki/foundations/<part-slug>/dissent.md`. Do NOT silently override expert domain judgment (E-15).

---

## §5 THE WISDOM APPLICATION LOOP (Phase D — central directive)

**This phase is constitutional. Skipping it is a violation.**

After integrator produces draft architecture for Part X (and after M5 inter-Part lite coherence check completes for UND-3 + C4 + D27), brigadier dispatches a dedicated **Wisdom Loop pass**.

### §5.1 Procedure (UNCHANGED from Bundle 1+2+3 — preserve discipline)

For each consultant card relevant to this part (per §3.3 mapping) AND each library-direct supplement source (§3.4):

Ask FIVE questions, in order, in writing, with traceable answers:

1. **Question 1 — Application Gap**: "What does this consultant card say that the current draft DOES NOT yet apply, but would benefit from?"
2. **Question 2 — Cargo-Cult Audit**: "Are there principles from this card we cited but did not actually apply (cargo-cult risk per Manifest §5)?"
3. **Question 3 — Concrete Improvement**: "Is there a concrete improvement to the architecture if we apply principle X from this card?"
4. **Question 4 — Section Impact**: "If we DO apply this improvement — what changes in §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary / §F Anti-scope / §H Code interfaces / §I Data schemas?"
5. **Question 5 — Phase A Justification**: "Is the application JUSTIFIED for current Phase A scope (single-owner, Phase 1 €50K horizon)? Or is it premature optimization for Phase B/C/D scale?"

### §5.2 Bundle 4 inherits Bundle 3 ≥85% operational target

- **Bundle 1 (50/50 mix)**: too much philosophical text — accepted for that bundle's constitutional substrate work.
- **Bundle 2 (≥60% target, achieved 89%)**: explicit operational bias.
- **Bundle 3 (≥85% target, achieved 100%)**: Compound Learning + Health Monitoring inherently operational.
- **Bundle 4 (≥85% target inherited)**: P7+P9+P10 inherently operational (state machines + daily-log/weekly-review schemas + CRM data model + integration adapter + privacy structural). Should easily match Bundle 3's 100%.

If aggregate drops below 85%: red flag — investigate; brigadier may be reverting to philosophical content.

**For Bundle 4, apply same bias as Bundle 3:**

- **PRIORITIZE operational adoptions** — adoptions that change schema fields, add new failure modes, define new SLO targets, add new lint checks, change algorithm, add new edge type, modify code-level interface, OR add new admissibility rule.
- **MINIMIZE philosophical/marketing text** — adoptions that add only "framing prose" without operational consequence.
- **REJECT** any adoption whose "concrete consequence sentence" is purely about how the document reads.

**Wisdom Findings table format (UNCHANGED):**

```markdown
### Wisdom Application Findings — Part X

| Card / Source | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification | Section edited |
|---------------|-----------|---------------|-------------|----------|------------------------------|---------------|----------------|
| #1 PM-Cagan-ShapeUp | appetite-as-CONSTRAINT not estimate | partial in §I.1 | Add `appetite_exceedance_action: re-shape \| archive` field to project schema; binary acceptance predicate | YES | OPERATIONAL | Phase A — schema field with binary action | §I.1 + §K |
| #2 Anthropic CAI | Privacy hardcoded never-list | partial in §I | Add Default-Deny entries: race / religion / political / health classifier attempts → Tier 0 hard | YES | OPERATIONAL | Phase A — structural privacy enforcement | §F + §I + Part 6b §I.3 cross-ref |
| #3 Stoic Dichotomy | "in our control" framing | not applied | Add §F.3 framing prose | NO | PHILOSOPHICAL | No scope-creep risk; pure framing prose; DEFER to Wave D documentation pass | n/a |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

**Aggregate target:**
> Bundle 4 should have YES Adopted ratio of Operational ≥85% (Bundle 3 demonstrated 100% achievable across 2 inherently-operational parts; Bundle 4 has 3 inherently-operational parts).

If Operational ratio < 85% across Parts 7+9+10: investigate. Re-dispatch integrator to convert PHILOSOPHICAL adoptions into OPERATIONAL ones.

### §5.3 Discipline (HARD RULES — preserved from Bundle 1+2+3)

**Brigadier MUST**:
- Run Wisdom Loop AFTER integrator (and after M5 lite coherence for Parts 7+9+10), BEFORE critic gate
- Produce findings table (§M) per part with Operational/Philosophical column
- Apply every "YES Adopted" edit to draft BEFORE critic gate runs
- Critic gate then verifies: did Wisdom edits hold? Anti-cargo-cult check stricter than usual.
- For each YES Adopted entry, the edit MUST be visible in §A-§L diff (not just claimed in table).
- For each NO entry, the justification MUST be one of the legitimate categories (Phase B work / Phase C+ scale / premature optimization / requires RUSLAN-LAYER decision Ruslan hasn't made / domain-orthogonal to this part / pure framing prose without operational consequence).

**Brigadier MUST NOT**:
- Skip Wisdom Loop because "draft seems fine"
- Reject improvement opportunities without explicit justification from legitimate categories
- Adopt every improvement without Phase A justification
- Treat the loop as paperwork
- Adopt PHILOSOPHICAL improvements without scope-creep-prevention or Phase B/C concrete-need justification
- Accept aggregate operational ratio < 85% silently

### §5.4 Failure mode (UNCHANGED)

If Wisdom Application Loop produces 0 "YES Adopted" across all relevant cards for a part: HALT, write `swarm/wiki/foundations/<part-slug>/wisdom-loop-zero-adoption-flag.md` with reasoning, escalate to Ruslan via tmux output before proceeding to critic gate.

DO NOT fabricate YES entries to satisfy the loop.

---

## §6 Quality bar

### §6.1 Document size: 10K-20K per Part (F8 LOCKED)

Each Part architecture document MUST be **10K-20K words**. Bias toward operational content density. Operational adoption ratio target ≥85%.

If draft <10K words: re-dispatch integrator with explicit feedback "you delivered N words; quality bar is 10K-20K — re-dispatch with §A-§N expansion mandate focusing on OPERATIONAL deltas (schema fields / failure modes / SLO targets / lint checks / algorithms / edge types / code-level interfaces / admissibility rules) NOT philosophical framing prose."

If draft >20K words: review for redundancy + cargo-cult padding. Tighten before Wisdom Loop.

**Part 10 specifically** likely lands at the larger end given CRM canonicalisation + privacy architecture sub-section.

### §6.2 Section structure (every part doc has §A-§N + §X)

Same structure as Bundle 1+2+3. Sections: §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary L/A/D/E / §F Anti-scope / §G F-G-R Tagging / §H Code-level interfaces / §I Data schemas / §J Operational rituals / §K Failure modes / §L Wave C work-list bullet status / §M Wisdom Application Findings / §N Provenance / §X Foundation vs RUSLAN-LAYER.

Bundle 4 specifics:
- §I Data schemas: Part 7 §I.1 project schema + state machine; Part 7 §I.2 project-retrospective-packet (UND-3 finalization). Part 9 §I.1 daily-log; §I.2 weekly-review; §I.3 SLA taxonomy. Part 10 §I.1 cross-fork-provenance D27 cross-ref + 5 reconciliation strategies; §I.2 CRM data model (canonicalises existing); §I.3 CRM 8 edge types (UND-5); §I.4 integration adapter pattern; §I.5 privacy schema fields.
- §H Code interfaces: Part 7 §H references Part 1 §H + Part 4 §I.1 + Part 6b §I.2. Part 9 §H references Part 1 §H + Part 5 §A + Part 6b §I.4 (C4 fix). Part 10 §H references Part 1 §H + Part 2 /ingest + Part 3 wiki/graph/edges.jsonl + Part 6b §I.3 (Default-Deny) + existing crm/_scripts/crm.py + voice_router.py.
- §X Foundation vs RUSLAN-LAYER: per part — see §2.4 above. **Bundle 4 NEW §X requirements per §6.7-§6.10**.

### §6.3 Anti-cargo-cult enforcement (CRITICAL)

Per Bundle 1 Part 6a §C citation discipline:
- Every `[src:...]` citation MUST be followed within 200 chars by a concrete consequence sentence.
- `/lint --check-citations` (Bundle 1 P6a.2 — specified, Phase B implementation) is canonical enforcer.
- Critic gate MUST reject any §A-§N section with cargo-cult violations.

### §6.4 Typed A.14 edges everywhere (HARD RULE — Bundle 1 canonical 10-edge table; C4 fix Part 9)

Every §D Dependencies entry MUST be one of: `ComponentOf` / `ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` / `operates-in` / `methodologically-uses` / `constrained-by` / `derives-from`

**NO `depends-on`. NO `uses` generic. Critic gate auto-rejects.**

**C4 FIX**: Part 9 §D every Part 6 / Part 6a / Part 6b reference uses `methodologically-uses` not `PhaseOf`. Brigadier autocheck greps `PhaseOf Part 6` → 0 hits required.

### §6.5 F-G-R on every promoted claim (DOGFOOD)

Every architecture claim MUST have F-G-R tag per Bundle 1 Part 6a §I.1 F8 schema. Inline OR table.

### §6.6 Provenance trail

Every claim → `[src:path]` inline citation → resolves to existing file + section. M2 cross-reference gate verifies 100%.

### §6.7 Special: Part 7 cadence event-driven autocheck (OQ-5 ack)

Per Ruslan ack OQ-5: P7 §E Laws declare event-driven, NOT cycle-boundary-gated.

**Brigadier autocheck procedure (run before §F finalize for Part 7):**

1. Verify §E Laws contains 4 laws verbatim per §2.1 Bullet P7.3.
2. Verify §J Operational Rituals does NOT specify calendar-cron-gated cadence (e.g., "weekly state transition review" is BANNED if it implies state transitions wait for cycle close).
3. Verify §I.1 state-machine transitions trigger on event signals (closure events / stage-gate ack events / scope-record updates) NOT on calendar/cycle.
4. Verify cross-reference to OQ-5 Ruslan ack present.

If any check fails: brigadier returns to integrator with explicit feedback "Part 7 cadence not event-driven per OQ-5. Re-dispatch with §E expansion: 4 laws verbatim + event-driven enforcement + throughput-bottleneck-prevention rationale."

### §6.8 Special: Part 9 IP-2 single-owner bounded autocheck

Per FUNDAMENTAL §2.6 + Bundle 1 RUSLAN-ACK + FPF IP-2: Part 9 = single-owner Phase A bounded.

**Brigadier autocheck procedure (run before §F finalize for Part 9):**

1. Verify §X declares single-owner Phase A bounded with structural change ≥35% at >10× scale (Ashby BOSC-A-T-X reference).
2. Verify §X declares Phase B activation event (sustained partner onboarding signal).
3. Verify §I.1 + §I.2 + §I.3 declare multi-owner stub fields (commented out / declared NOT implemented; Phase B F.9 Bridge work).
4. Verify §X declares Foundation generic vs RUSLAN-LAYER with explicit examples (attention budget cap value 20 = RUSLAN-LAYER; structure = Foundation generic).
5. Verify §D every Part 6 reference uses `methodologically-uses` not `PhaseOf` (C4 fix).

If any check fails: brigadier returns to integrator with explicit feedback "Part 9 IP-2 declaration under-declared OR multi-owner stub fields missing OR C4 fix not applied. Re-dispatch with §X expansion + §I stub fields + §D nomenclature fix."

### §6.9 Special: Part 10 fork-separation FINAL CLOSURE autocheck

Per OQ-MERGED-3 Wave A scope: Bundle 4 = last chance for Foundation-level fork-separation declaration. Part 10 has highest creep risk.

**Brigadier autocheck procedure (run before §F finalize for Part 10):**

1. Verify §X explicitly enumerates Foundation generic categories (CRM data model + edge types + adapter pattern + privacy invariants + write-ack discipline + skill SHAPES).
2. Verify §X explicitly enumerates RUSLAN-LAYER categories with **EXAMPLES MANDATORY**:
   - DACH ICP example (text mentions "DACH" + "consulting clients" + "fintech/insurtech" OR equivalent)
   - German GDPR example (text mentions "GDPR" + "EU data-residency" + "right-to-be-forgotten")
   - Auth-token externalisation example (text mentions "Linear" OR "GitHub" OR "Notion" OR "Slack" + "private/<service>-auth.yaml" path)
   - Specific contact lists example (text mentions "crm/people/" OR "crm/orgs/" + "RUSLAN-LAYER")
   - DACH intelligence URLs example (text mentions specific URL pattern OR "HN" + "r/Berlin" OR equivalent)
3. Verify cross-reference to OQ-MERGED-3 Wave A Ruslan ack 2026-04-27.

If any check fails: brigadier returns to integrator with explicit feedback "Part 10 §X fork-separation under-declared per OQ-MERGED-3 FINAL CLOSURE. Re-dispatch with §X expansion: explicit DACH/GDPR/auth-token/contact-list/intelligence-URL examples MANDATORY."

### §6.10 Special: Part 10 privacy STRUCTURAL autocheck

Per FUNDAMENTAL §6.4: privacy = STRUCTURAL invariants. Implementation = lint signals + schema fields + Default-Deny entries.

**Brigadier autocheck procedure (run before §F finalize for Part 10):**

1. Verify §I + §H + §F declares 4 privacy invariants per §2.3 Bullet P10.3:
   - Consent enforcement (schema field `consent_recorded_at`)
   - Forget-request (skill spec `/crm forget` + Reversal Transactions)
   - Encryption at rest (Part 1 substrate level — declared as PRECONDITION)
   - NO inference of protected characteristics (Default-Deny entries per Part 6b §I.3 + lint signal `/lint --check-protected-inference`)
2. Verify each invariant has STRUCTURAL enforcement (schema field OR lint signal OR Default-Deny entry); NOT behavioral framing prose.
3. Verify §F Anti-scope declares behavioral framing prose <10% of privacy section.
4. Verify Default-Deny entries reference Part 6b §I.3 F8 LOCKED (cross-ref resolves).
5. Verify lint signal skill specs reference Phase B implementation (per OQ-MERGED-5 specify-and-stub pattern).

If any check fails: brigadier returns to integrator with explicit feedback "Part 10 privacy is BEHAVIORAL not STRUCTURAL. Re-dispatch with §I/§H/§F expansion: schema fields + lint signals + Default-Deny entries; behavioral prose <10%."

---

## §7 Verification Gates (M1 / M2 / M3 / M4 / M5 / M6)

### §7.1 M1 Smoke Test (per part, threshold ≥90%)

Same checklist as Bundle 1+2+3:
- [ ] All §A-§N + §X sections populated (no "TBD" placeholders)
- [ ] Word count ≥10K (F8 floor)
- [ ] Word count ≤20K (F8 ceiling)
- [ ] Dependencies (§D) all typed per §6.4
- [ ] F-G-R tags (§G) present on every promoted claim
- [ ] Wave C bullets from §2 all mapped in §L with acceptance predicate ✅/❌
- [ ] §X Fork-separation section explicit
- [ ] No cargo-cult signals (citation without consequence sentence within 200 chars)

Bundle 4 additional checks per part:

**Part 7 specific:**
- [ ] §I.1 5-state state machine declared with IP-5 past-participle naming
- [ ] §I.1 stage-gate predicates per Part 6b §I.2 stage-gate registry
- [ ] §I.1 appetite declarations per Singer Shape Up (`appetite_weeks` + `appetite_exceedance_action`)
- [ ] §I.1 scope record append-only schema
- [ ] §I.1 resource templates per project type (4 types: consulting / research / product / bets)
- [ ] §I.2 `project-retrospective-packet.json` schema EXTENDS task-return-packet.json (UND-3 finalization)
- [ ] §E Laws cadence event-driven (4 laws verbatim per §2.1 P7.3)
- [ ] §6.7 cadence event-driven autocheck PASS
- [ ] P7.2 IP-5 whitelist file created at `decisions/policy/ip5-past-participle-whitelist.md` (or `.claude/config/ip5-past-participle-whitelist.yaml`)

**Part 9 specific:**
- [ ] §I.1 daily-log schema with frontmatter + content sections
- [ ] §I.2 weekly-review schema with **draft-disposition table (C2 producer side)**
- [ ] §I.3 SLA 3-tier taxonomy file at `.claude/config/sla-taxonomy.yaml`
- [ ] §X IP-2 single-owner bounded declaration with F.9 Bridge multi-owner trigger
- [ ] §I multi-owner stub fields declared (NOT implemented; Phase B)
- [ ] §D every Part 6 reference uses `methodologically-uses` not `PhaseOf` (C4 fix)
- [ ] §6.8 IP-2 + C4 autocheck PASS

**Part 10 specific:**
- [ ] §I.1 references `cross-fork-provenance.json` D27 promotion (5 reconciliation strategies)
- [ ] §I.2 CRM data model canonicalises existing (24 source files / 35 unit tests / 10 skills / 4 schemas)
- [ ] §I.3 CRM 8 edge types declared with UND-5 binding to Part 3 wiki/graph/edges.jsonl
- [ ] §I.4 integration adapter pattern (RT-1 + RT-2 + L.1/L.2/L.3 stubs)
- [ ] §I.5 privacy schema fields (`consent_recorded_at` mandatory before RT-2)
- [ ] §F Anti-scope declares C3 Phase A boundary (inbound external = Phase B)
- [ ] §H Default-Deny entries for protected-characteristic inference (cross-ref Part 6b §I.3)
- [ ] §H lint signal skill specs (`/lint --check-consent`, `/lint --check-protected-inference`, `/lint --check-forget-request-cascade`)
- [ ] §X explicit DACH/GDPR/auth-token/contact-list/intelligence-URL examples (FINAL CLOSURE)
- [ ] §6.9 fork-separation autocheck PASS
- [ ] §6.10 privacy structural autocheck PASS

**All parts:**
- [ ] Operational adoption ratio per part ≥85% in §M Wisdom Findings
- [ ] OQ-MERGED-2 dissolve-test evidence cycle 2 logged at `swarm/wiki/cycles/.../bundle-4/dissolve-test-evidence-cycle-2.md`

Pass threshold: ≥90% bullets ticked. Per part. Failure: re-dispatch integrator.

### §7.2 M2 Cross-reference (per part, threshold 100%)

Same as Bundle 1+2+3:
- [ ] Every `[src:...]` resolves to an existing file
- [ ] Every cited section anchor resolves to actual section heading
- [ ] No broken inline citations
- [ ] No dangling typed-edge targets in §D

Bundle 4 additional:
- [ ] Part 7 §B references Part 5 §A + Bundle 3 UND-3-stub.md (resolves)
- [ ] Part 7 §I.2 references Part 4 §I.1 task-return-packet.json (SUPERSET; resolves)
- [ ] Part 9 §D every Part 6 reference uses `methodologically-uses` (C4 fix; resolves)
- [ ] Part 9 §B references Part 5 §A methodology promotion candidates (resolves)
- [ ] Part 10 §I.1 references Part 1 §I.1 cross-fork-provenance.json (resolves; D27 promotion declared)
- [ ] Part 10 §I.3 references Part 3 wiki/graph/edges.jsonl + crm/_schema/edges.yaml (UND-5 binding; resolves)
- [ ] Part 10 §F references Part 2 /ingest (C3 Phase A boundary; resolves)
- [ ] Part 10 §H references Part 6b §I.3 default-deny (privacy structural; resolves)

Pass threshold: 100%. Failure: integrator fixes citations.

### §7.3 M3 Scenario Walkthroughs (bundle-level, 4 scenarios MUST pass)

Run each scenario end-to-end against Bundle 4 + Bundle 1+2+3 interfaces. Document trace in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-4/M3-walkthroughs.md`.

**Scenario 1 — Project full lifecycle (multi-bundle: Parts 7/4/5/6b/1):**
Owner declares project (e.g., "quick-money") via `/project-bootstrap quick-money P1 --type=consulting --client=acme` → Part 7 stage-gate `scoped → staged` (appetite declared 4 weeks; scope record drafted) → AWAITING-APPROVAL `gate_class: stage_gate` → Ruslan ack → `staged → activated` AWAITING-APPROVAL `gate_class: stage_gate` → Ruslan ack → cycle dispatch via Part 4 routing-table.yaml → execution cycles → closure event triggers `activated → under-review` (event-driven per OQ-5) → retrospective drafting → `under-review → closed | archived` AWAITING-APPROVAL `gate_class: stage_gate` → Part 7 emits `project-retrospective-packet.json` (UND-3 finalization) to `comms/mailboxes/` → Part 5 reads RAW packet, does own DRR extraction → strategies.md update committed via Part 1 §H → methodology promotion candidate accumulates → Part 6b `gate_class: draft_promotion` → wiki/methodology/<rule-slug>.md F4→F5.
Tests: Parts 7 + 4 + 5 + 6b + 1; UND-3 finalization (Part 7 §B emit ↔ Part 5 §A input); event-driven cadence (OQ-5); appetite-as-CONSTRAINT discipline; stage-gate predicates F8 LOCKED.

**Scenario 2 — Daily-log + weekly review with methodology promotion (Parts 9/5/6b/1):**
Morning intent → Part 9 daily-log frontmatter populated (date, projects_touched, attention_budget) → cycle dispatch via Part 4 → afternoon execution → evening reflection (committed via Part 1 §H) → Friday weekly review with draft-disposition table (5 drafts categorized accept/iterate/discard) → 2 drafts marked `accept` → Part 9 emits methodology promotion candidates to Part 5 strategies.md → Part 5 admissibility predicate satisfied (2 cycles + rule_slug) → Part 5 emits methodology candidate at `wiki/methodology/<rule-slug>-DRAFT.md` → AWAITING-APPROVAL `gate_class: draft_promotion` → Ruslan ack → wiki/methodology/<rule-slug>.md F4→F5 → SLA tier L1 ack same-session per `.claude/config/sla-taxonomy.yaml`.
Tests: Parts 9 + 5 + 6b + 1; daily-log/weekly-review schemas; SLA 3-tier taxonomy; methodology promotion via weekly review (Part 9 ↔ Part 5 cross-ref); C4 nomenclature fix (Part 9 §D `methodologically-uses Part 6`); IP-2 single-owner bounded.

**Scenario 3 — External action with privacy enforcement (Parts 10/6b/6a/1):**
Ruslan requests CRM contact outreach via `/crm-touch <slug> "follow up on Q2 partnership"` → Part 10 RT-2 write-ack adapter receives request → Part 10 verifies `consent_recorded_at` field present in CRM contact record → blast-radius classify Tier 1 (strategic) → Part 6b `gate_class: stage_gate` packet to enforcement arm → Ruslan ack → Part 10 dispatches external action via Linear adapter (L.1) → write-ack confirmation → log to CRM event log (`crm/log.md` append) + approval log (`swarm/approvals/log.jsonl` Part 6a §C) + cross-fork-provenance log → Part 1 commit `[crm] outreach: <slug> Linear ticket created`.
Tests: Parts 10 + 6b + 6a + 1; consent enforcement (privacy invariant 1); RT-2 adapter pattern; SLA tier L1 ack; AWAITING-APPROVAL `gate_class: stage_gate`; CRM canonicalisation (existing operational baseline preserved).

**Scenario 4 — Fork-separation Phase B import (Parts 10/1; FINAL CLOSURE validation):**
Phase B partner (e.g., "alex-dach-consulting") forks Foundation → imports Part 10 generic CRM schema + integration adapter pattern (RT-1 + RT-2) + privacy invariants (4 invariants from §I) + write-ack discipline → DECLINES RUSLAN-LAYER (DACH ICP parameters; German GDPR config; specific contact lists; Linear/GitHub/Notion auth tokens; DACH-specific intelligence URLs) → fork's local CRM has different ICP (e.g., US fintech) → reconciliation_strategy applied per scenario:
- `parent-wins` for privacy invariants (Foundation Default-Deny entries hold)
- `fork-wins` for ICP parameters (alex-dach-consulting's US fintech ICP supersedes RUSLAN-LAYER DACH)
- `manual-merge` for cross-cutting changes (e.g., new Default-Deny entry needed for US-specific HIPAA classifier prohibition)
- `pending-review` initial state until alex-dach-consulting acks
→ cross-fork-provenance.json conforms with promoted top-level field `approvals_reconciliation_strategy`.
Tests: Parts 10 + 1; FINAL CLOSURE fork-separation per OQ-MERGED-3 (DACH/GDPR/auth-token examples); OQ-B1-5 D27 promotion; reconciliation_strategy enum (5 values); Phase B import pattern.

Pass threshold: 4/4 scenarios trace cleanly with no missing schemas or undefined handoffs. Failure: re-architect specific gaps.

### §7.4 M4 Wisdom Application Loop verification

Per part:
- [ ] §M Wisdom Findings table populated with Operational/Philosophical column
- [ ] Every "YES Adopted" entry has corresponding visible edit in §A-§L (verify by line-number diff trace)
- [ ] Every "NO" entry has explicit justification from legitimate categories
- [ ] No fabricated YES entries
- [ ] All relevant Wave B consultants per §3.3 mapping covered
- [ ] All Wave B Supplement library-direct sources per §3.4 covered
- [ ] **Operational adoption ratio ≥85% per part** (Bundle 4 inherits Bundle 3 floor)
- [ ] No PHILOSOPHICAL adoptions without scope-creep-prevention or Phase B/C concrete-need justification

Pass threshold: all bullets ticked per part + aggregate ≥85% operational across Bundle 4.

### §7.5 M5 Inter-Part lite coherence verification (UND-3 + C4 + D27)

- [ ] Part 7 §B `project-retrospective-packet.json` schema fields are SUPERSET of Part 5 §A expected fields (UND-3 finalization)
- [ ] Part 7 §J cadence (per closure event + per cycle boundary) compatible with Part 5 §J compound-phase trigger predicate
- [ ] Bundle 3 UND-3-stub.md updated F2→F4 with Part 7 conformance reference
- [ ] Part 9 §D every Part 6 reference uses `methodologically-uses` not `PhaseOf` (C4 fix; grep returns 0)
- [ ] Part 10 §I.1 declares 5 reconciliation strategies (parent-wins / fork-wins / manual-merge / decline-import / pending-review)
- [ ] Part 1 §I.1 supplement edit prepared (uncommitted at M5 time; commits at Phase H end-of-cycle)

Pass threshold: all bullets ticked. Failure: re-dispatch integrator.

### §7.6 M6 — Bundle 4 special autochecks

- [ ] Part 7 cadence event-driven (§E Laws 4 laws verbatim; §6.7 autocheck PASS)
- [ ] Part 9 IP-2 single-owner bounded (§X declaration; multi-owner stub fields §I; §6.8 autocheck PASS)
- [ ] Part 10 fork-separation FINAL CLOSURE (§X explicit DACH/GDPR/auth-token examples; §6.9 autocheck PASS)
- [ ] Part 10 privacy STRUCTURAL (schema fields + lint signals + Default-Deny entries; §6.10 autocheck PASS)
- [ ] OQ-B1-5 D27 supplement record drafted at `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md` (uncommitted at M6 time; commits at Phase H end-of-cycle)
- [ ] CRM canonicalisation (existing 24 source files / 35 unit tests / 10 skills / 4 schemas) — Part 10 references; does NOT redesign
- [ ] OQ-MERGED-2 dissolve-test evidence cycle 2 logged

Pass threshold: 7/7. Failure: re-dispatch with specific autocheck failure listed.

---

## §8 Output Expected (exact paths, structures)

### §8.1 Per-part architecture documents

- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` (10K-20K words)
- `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` (10K-20K words)
- `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` (10K-20K words; likely larger end)

Each with §A-§N + §X sections per §6.2.
Each with YAML frontmatter (per Global Rule 1).

### §8.2 Schemas

**Part 7:**
- `shared/schemas/project.json` (or `.yaml`) — declared inline §I.1; physical file generation Phase B
- `shared/schemas/project-retrospective-packet.json` — declared inline §I.2 (UND-3 finalization; extends task-return-packet.json); physical file generation Phase B

**Part 9:**
- `shared/schemas/daily-log.json` — declared inline §I.1; physical file generation Phase B
- `shared/schemas/weekly-review.json` — declared inline §I.2 (with draft-disposition table); physical file generation Phase B

**Part 10:**
- `shared/schemas/health-alert.json` (already declared Bundle 3 P8.4); Part 10 ALERT classes referenced
- CRM data model schema (canonicalises existing 4 YAML schemas in `crm/_schema/` — declared inline §I.2)
- Integration adapter pattern (declared inline §I.4)
- Privacy schema fields (declared inline §I.5; `consent_recorded_at` field; lint signal skill specs)

### §8.3 Configuration files

- `.claude/config/sla-taxonomy.yaml` (P9.3 — 3-tier SLA taxonomy)
- `decisions/policy/ip5-past-participle-whitelist.md` OR `.claude/config/ip5-past-participle-whitelist.yaml` (P7.2 — IP-5 whitelist; brigadier picks)

### §8.4 Privacy architecture (P10.3)

- §I sub-section in main Part 10 architecture (preferred; consolidated)
- OR `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/privacy-architecture.md` (acceptable; brigadier picks based on length)
- `/lint --check-consent`, `/lint --check-protected-inference`, `/lint --check-forget-request-cascade` skill specs (Phase B implementation; specs only)

### §8.5 D27 promotion (OQ-B1-5) — END-OF-CYCLE supplement

- Updated `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` §I.1 (cross-fork-provenance.json `approvals_reconciliation_strategy` promoted to top-level + 5 reconciliation strategies)
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md` (constitutional supplement record analogous to OQ-B2-A pattern)

### §8.6 Updated cross-references

- Wave A interface cards Parts 7/9/10 — SUPERSEDED frontmatter addendum (deferred to Wave D housekeeping commit acceptable per Bundle 2/3 pattern)
- Manifest §2 matrix Bundle 4 rows updated (Parts 7, 9, 10 — adopted cards + Wisdom Loop counts + operational ratio)
- `swarm/lib/routing-table.yaml` extended with Bundle 4 per-role entries (project-lifecycle-orchestrator role; owner-interaction-scaffold role; external-touchpoints-network role)
- Bundle 3 `swarm/wiki/cycles/.../bundle-3/UND-3-stub.md` updated F2→F4 (Part 7 conformance verified)

### §8.7 Walkthroughs trace

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-4/M3-walkthroughs.md` — all 4 scenarios traced

### §8.8 Dissolve-test evidence (Bundle 4 = Cycle 2 of 3)

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-4/dissolve-test-evidence-cycle-2.md` — accumulating compound-phase-exclusive operations observed during Bundle 4 cycle (mirrors Bundle 3 pattern)

### §8.9 Bundle-level dissent (if any)

- `swarm/wiki/foundations/<part-slug>/dissent.md` per part with unresolved critic dissent (AP-6 preservation)

### §8.10 AWAITING-APPROVAL packet (FINAL deliverable — Wave C closure)

- `decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-XX.md` (XX = day of completion)

Structure mirrors Bundle 1+2+3 packets:

```markdown
---
title: AWAITING-APPROVAL — Wave C Bundle 4 (Parts 7 + 9 + 10) — FINAL Wave C bundle
date: 2026-04-XX
type: awaiting-approval
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 4
final_wave_c_bundle: true
parent_packet: decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-28.md
predecessor_ack_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
predecessor_ack_bundle_1_supplement: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md
predecessor_ack_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
predecessor_ack_bundle_3: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md
deep_prompt: prompts/wave-c-bundle-4-deep-prompt-2026-04-28.md
status: awaiting-ruslan-ack
F: F4
ClaimScope: "Holds for the 3 Bundle 4 architecture documents (Parts 7 + 9 + 10) and their declared schemas + configs + privacy architecture + END-OF-CYCLE D27 supplement record. CLOSES Wave C — no more Wave C bundles after this. Does NOT pre-judge Wave D integration pass."
R:
  refuted_if: "Ruslan walkthrough surfaces a constitutional violation, OQ-MERGED-3 fork-separation FINAL CLOSURE under-declared, OQ-5 cadence violation, IP-2 multi-owner stub missing, privacy structural under-implemented, UND-3 finalization gap, OQ-B1-5 D27 supplement gap, OR C4 nomenclature fix not applied"
  accepted_if: "Ruslan acks the 3 architecture documents AND the schema set AND the configs AND the privacy architecture AND the §X Foundation vs RUSLAN-LAYER FINAL CLOSURE separations AND the D27 supplement record AND the IP-2 single-owner declaration AND the cadence event-driven declaration"
next_action: "Ruslan ack of this packet → Wave C COMPLETE → Wave D integration pass dispatch (separate cycle)"
commits:
  - [Bundle 4 Part 7 commit]
  - [Bundle 4 Part 9 commit]
  - [Bundle 4 Part 10 commit]
  - [Bundle 4 AWAITING-APPROVAL commit]
  - [Bundle 1 supplement 2 D27 commit]
---

## §1 Executive Summary
[3-5 paragraphs: Wave C COMPLETE; Foundation 10/10 parts F5; what was built (Parts 7+9+10); key decisions (UND-3 finalization; C4 nomenclature fix; OQ-B1-5 D27 promotion; CRM canonicalisation; privacy structural; IP-2 single-owner bounded; OQ-5 event-driven cadence; OQ-MERGED-3 FINAL CLOSURE); headline numbers]

## §2 Outcomes — F-level changes
[Table: Artefact / F-before / F-after / Drift rationale]

## §3 Wisdom Findings Rollup (with Operational/Philosophical breakdown)
[Aggregate table across Parts 7+9+10]

## §4 Verification Gate Results
- M1 Smoke: Part 7 X% / Part 9 X% / Part 10 X%
- M2 Cross-ref: 100%
- M3 Scenarios: 4/4 PASS
- M4 Wisdom: PASS with operational ratio ≥85%
- M5 Inter-Part lite coherence (UND-3 + C4 + D27): PASS
- M6 Bundle 4 autochecks (cadence event-driven + IP-2 + fork-separation FINAL CLOSURE + privacy structural): PASS

## §5 Open Questions Surfaced By Bundle 4
[Any new OQs beyond those acked at Bundles 1+2+3 — OQ-B4-X numbering; deferred to Wave D]

## §6 Provenance
[List of every source consulted; commits on claude/jolly-margulis-915d34]

## §7 Ruslan Ack Request
[Specific decisions Ruslan must ack:
 - 3 Bundle 4 architecture documents canonical-promoted (Parts 7, 9, 10 → status: ruslan-acked-canonical)?
 - UND-3 finalization accepted (Part 7 §B emit ↔ Part 5 §A input)?
 - C4 nomenclature fix accepted (Part 9 §D `methodologically-uses Part 6`)?
 - OQ-B1-5 D27 supplement accepted (cross-fork-provenance.json approvals_reconciliation_strategy top-level + 5 strategies)?
 - OQ-MERGED-3 fork-separation FINAL CLOSURE accepted (Part 10 §X explicit DACH/GDPR/auth-token examples)?
 - OQ-5 cadence event-driven accepted (Part 7 §E)?
 - IP-2 single-owner bounded accepted (Part 9 §X + multi-owner stub §I)?
 - Privacy STRUCTURAL accepted (Part 10 §I + §H + §F — schema fields + lint signals + Default-Deny entries)?
 - Wave C now COMPLETE → Wave D integration pass dispatch confirmed?
 - Any per-part dissent items: Ruslan resolves]

## §8 STOP — Wave C COMPLETE
Per §11 STOP rule. **THIS IS THE FINAL WAVE C BUNDLE.** Bundle 5 does not exist.
```

### §8.11 STOP

After AWAITING-APPROVAL packet — STOP. **Wave C is now COMPLETE.** Brigadier waits for Ruslan ack of Bundle 4 → next step = Wave D integration pass (separate cycle).

---

## §9 Branch + Commit Discipline

- **Branch**: `claude/jolly-margulis-915d34` (current, same as Bundles 1+2+3). Do NOT create new branches.
- **Commit cadence**: small + frequent. After each major phase per part.
- **Commit message format**: `[architecture] Bundle 4 — <part> — <phase>` examples:
  - `[architecture] Bundle 4 — Part 7 — Phase B + C cells + integrator draft`
  - `[architecture] Bundle 4 — Part 7 — Phase D Wisdom Loop applied (X YES Op / Y YES Phi / Z NO)`
  - `[architecture] Bundle 4 — Part 7 — Phase E critic gate PASS + cadence event-driven autocheck PASS`
  - `[architecture] Bundle 4 — Part 9 — Phase B + C cells + integrator draft`
  - `[architecture] Bundle 4 — Part 9 — Phase D Wisdom Loop + C4 nomenclature fix applied`
  - `[architecture] Bundle 4 — Part 9 — Phase E critic gate PASS + IP-2 + C4 autochecks PASS`
  - `[architecture] Bundle 4 — Part 10 — Phase B + C cells + integrator draft + CRM canonicalisation`
  - `[architecture] Bundle 4 — Part 10 — Phase D Wisdom Loop + privacy structural`
  - `[architecture] Bundle 4 — Part 10 — Phase E critic gate PASS + fork-separation FINAL CLOSURE + privacy structural autochecks PASS`
  - `[architecture] Bundle 4 — M3 walkthroughs 4/4 PASS + M5 lite coherence PASS + M6 autochecks PASS`
  - `[architecture] Bundle 4 AWAITING-APPROVAL — Parts 7 + 9 + 10 architecture, Wave C closure, Wisdom Loop applied, M-gates PASS`
  - `[architecture] Bundle 1 retroactive supplement 2 — cross-fork-provenance.json approvals_reconciliation_strategy field promotion top-level (per OQ-B1-5 RUSLAN-ACK Bundle 1)` (END-OF-CYCLE Phase H)
- **Push cadence**: after each commit. No force-push. No `--amend`. No `--no-verify`.
- **API-key audit**: before each commit run `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|sk-ant-' <staged-files>` → 0 hits required.

---

## §10 Operational Constraints

1. `unset ANTHROPIC_API_KEY` before any provider invocation. Brigadier MUST NOT reference any provider API-key env var in any code path.
2. `ulimit -n 65535` if not already set.
3. **HD-02 rate limiter N=2 normal mode**. Maximum 2 concurrent Task() dispatches. Bundle 4 may dispatch Parts 7+9+10 in parallel within HD-02 N=2 (e.g., Part 7 + Part 9 in parallel; Part 10 sequentially after).
4. **Read tool 32MB limit**: for large PDFs use `pages` parameter; do NOT auto-read full books.
5. **NO auto-execution of Wave D after Bundle 4** — explicit STOP per §11.
6. **No `--amend`, no `--no-verify`, no force-push** — git-native rollback via `git revert` only.
7. **Frontmatter compliance**: every `.md` artefact carries YAML frontmatter per the relevant `swarm/wiki/_templates/<type>.md` template.
8. **Untouchable trees in Phase A**: 14 legacy `.claude/agents/*.md` files and the v2 `wiki/` tree. Bundle 4 EXTENDS routing-table.yaml + adds project + daily-log + weekly-review + CRM canonicalisation; does NOT modify the agent files themselves. Bundle 4 EXTENDS Part 1 §I.1 cross-fork-provenance schema (D27 promotion); does NOT modify other Bundle 1 schemas.
9. **CRM operational baseline UNTOUCHABLE except for canonicalisation**: 24 source files / 35 unit tests / 10 skills / 4 schemas — Part 10 architecture references + canonicalises; does NOT modify implementation.
10. **Security — never touch**: `~/.ssh/`, `/etc/`, any `.env*`, anything under `private/`, Tier-4 closed-core book corpus.
11. **Working directory**: `/home/ruslan/jetix-os/`. Do not `cd` outside.
12. **NO Phase ZERO retroactive supplement**: clean substantive start. Brigadier proceeds DIRECTLY to Phase A pre-read confirmation.
13. **OQ-B1-5 D27 supplement is END-OF-CYCLE**: commits AFTER all 3 architecture documents land + AWAITING-APPROVAL packet drafted (Phase H per §4.5).
14. **Subagent stall fallback acceptable**: if subagents stall on stream watchdog (as in Bundles 2+3), brigadier may switch to direct-write mode; flag in AWAITING-APPROVAL packet §5 Open Questions for Ruslan visibility.

---

## §11 STOP Rule + Ack Mantra

### §11.1 STOP rule

After AWAITING-APPROVAL packet (`§8.10`) is committed and pushed AND OQ-B1-5 D27 supplement record committed and pushed:

**STOP. WAVE C IS COMPLETE.** Bundle 5 does not exist. Wave D integration pass is the next cycle (separate dispatch).

Brigadier waits for HITL signal (Ruslan ack of Bundle 4 AWAITING-APPROVAL packet).

Final action: notify Ruslan via tmux output (or stdout if no tmux):

> «Wave C Bundle 4 complete. **WAVE C IS NOW COMPLETE — all 10 Foundation parts F5.**
> AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-XX.md`.
> OQ-B1-5 D27 supplement committed at end of cycle (commit hash <H1>): cross-fork-provenance.json approvals_reconciliation_strategy promoted to top-level + 5 reconciliation strategies declared.
> Word count summary: Part 7 = N words, Part 9 = N words, Part 10 = N words.
> Wisdom Loop adoption: N YES (Operational X / Philosophical Y) / N NO. Operational ratio: ZZ% (target ≥85%).
> UND-3 finalization: Part 7 §B emit contract conforms to Part 5 §A input (Bundle 3 stub satisfied; UND-3-stub.md F2→F4).
> C4 nomenclature fix: Part 9 §D every Part 6 reference uses `methodologically-uses` not `PhaseOf`.
> OQ-MERGED-3 FINAL CLOSURE: Part 10 §X explicit DACH ICP / German GDPR / Linear+GitHub+Notion auth-token / contact-list / DACH intelligence URL examples declared.
> OQ-5 cadence event-driven: Part 7 §E Laws 4 laws verbatim; NO calendar-cron / NO cycle-boundary-gating.
> IP-2 single-owner bounded: Part 9 §X declaration; multi-owner stub fields §I (NOT implemented; Phase B F.9 Bridge structural change ≥35%).
> Privacy STRUCTURAL: Part 10 §I + §H + §F — 4 invariants (consent / forget / encryption / no-protected-inference) with schema fields + lint signals + Default-Deny entries; behavioral framing prose <10%.
> CRM canonicalisation: existing 24 source files / 35 unit tests / 10 skills / 4 schemas referenced; NOT redesigned.
> M1/M2/M3/M4/M5/M6 gates: PASS / 100% / 4/4 PASS / PASS ≥85% / PASS / PASS.
> Awaiting Ruslan ack before Wave D integration pass dispatch.
> **THIS IS THE FINAL WAVE C BUNDLE.**»

### §11.2 Autocheck — when to halt early

- **Walltime exceeds 12h**: STOP, report status to Ruslan, ask how to proceed. (Bundle 4 = 3 parts vs Bundle 3's 2 — projected 1-3h at compound velocity; 12h ceiling generous.)
- **Subagent first attempt produces low-quality output** (cargo-cult signals, missing sections, under word count, missing event-driven cadence in Part 7 §E, missing IP-2 stub in Part 9 §I, missing fork-separation examples in Part 10 §X, behavioral privacy framing in Part 10 §I instead of structural): re-dispatch ONCE with explicit feedback. Second failure: escalate.
- **Wisdom Application Loop produces 0 "YES Adopted" for a part**: per §5.4, halt + flag + escalate.
- **Operational adoption ratio < 85% across Bundle 4**: investigate; re-dispatch integrator. Persistent: escalate.
- **Part 7 cadence not event-driven**: re-dispatch with §E expansion per §6.7 autocheck.
- **Part 9 IP-2 multi-owner stub missing**: re-dispatch with §I + §X expansion per §6.8 autocheck.
- **Part 9 §D uses `PhaseOf Part 6`**: re-dispatch with C4 fix per §6.8 autocheck.
- **Part 10 §X fork-separation missing DACH/GDPR/auth-token examples**: re-dispatch with §X expansion per §6.9 autocheck (FINAL CLOSURE strict).
- **Part 10 privacy is BEHAVIORAL not STRUCTURAL**: re-dispatch with §I/§H/§F structural enforcement per §6.10 autocheck.
- **Part 7 §B emit contract incoherent with Part 5 §A input**: M5 lite coherence check fails; re-dispatch integrator with UND-3 finalization mandate.
- **Critic gate produces irreconcilable dissent across ≥2 experts**: preserve dissent (AP-6) + escalate to Ruslan via dissent.md.
- **Schema design produces ambiguity that requires RUSLAN-LAYER decision**: pause, write `swarm/wiki/foundations/<part-slug>/oq-bundle-4-N.md`, escalate.
- **OQ-B1-5 D27 supplement does NOT land at end-of-cycle**: AWAITING-APPROVAL packet incomplete; brigadier completes Phase H before notifying Ruslan.
- **CRM canonicalisation drifts into redesign**: Part 10 architecture proposing alternative CRM data model = scope violation; re-dispatch with canonicalisation mandate per §2.3 special.
- **Brigadier subagents stall on stream watchdog** (as in Bundles 2+3): switch to direct-write mode acceptable; flag in AWAITING-APPROVAL packet §5.

### §11.3 Budget

~25-35 subagent dispatches across phases (5×4 matrix × 3 parts × dispatched cells + integrators + Wisdom Loop pass + critic gates + M-gates + Phase H supplement). Budget guard: if dispatch count exceeds 50, audit for redundant cells; if exceeds 60, halt and ask Ruslan.

### §11.4 Mantra (recite before each phase transition)

> **QUALITY > SPEED.**
> **PROVENANCE > VOLUME.**
> **WISDOM-APPLIED > WISDOM-CITED.**
> **OPERATIONAL > PHILOSOPHICAL.**
> **FINAL-CLOSURE-FORK-SEPARATION (Part 10 esp).**
> **EVENT-DRIVEN (Part 7).**
> **SINGLE-OWNER-BOUNDED (Part 9).**
> **PRIVACY-STRUCTURAL (Part 10).**
> **RUSLAN-ACK > BRIGADIER-CONFIDENCE.**
> **THIS IS WAVE C CLOSURE.**
>
> *Bundle 4 closes the Foundation. Without Part 7 the system has projects but no canonical lifecycle. Without Part 9 the system has agents but no canonical owner interface. Without Part 10 the system has a CRM with no Foundation-level boundary declarations + no privacy structural enforcement + no fork-separation discipline. Bundle 4 = LAST OPPORTUNITY for Foundation-level fork-separation declaration per OQ-MERGED-3. Treat with 1 trillion percent responsibility. WAVE C ENDS HERE.*

---

## §12 Pre-flight Checklist (brigadier runs before first dispatch)

- [ ] Read this prompt three times
- [ ] Read all of §3.1 Constitutional baseline (Bundles 1+2+3 LOCKED — DO NOT re-litigate)
- [ ] Read all of §3.2 Wave A artefacts (esp. wave-c-worklist §2 Parts 7/9/10, A-1-critic-gate.md §2 Parts 7+9+10, dependency-graph.md §3.3 C3 + §3.4 C4 + §4.3 UND-3 + §4.5 UND-5)
- [ ] Read relevant subsets of §3.3 (per part — see §3.3 mapping)
- [ ] Read §3.4 Wave B Supplement library-direct sources (Anthropic CAI + Askell HHH critical for P10 privacy; Young 2010 for P7 events; Google SRE Book + Workbook for P9 SLA tiers)
- [ ] Skim §3.5 existing operational artefacts (esp. **CRM TREE 24 source files for P10 baseline**; `projects/` + `.claude/config/project-types.yaml` for P7 baseline; `daily-log/` + `/plan-day` + `/close-day` for P9 baseline)
- [ ] Verify branch `claude/jolly-margulis-915d34` is current and clean
- [ ] Verify `unset ANTHROPIC_API_KEY` (operator should have done this)
- [ ] Verify `swarm/lib/README.md` consulted (Bundle 2 C1 canonical answer)
- [ ] Verify `swarm/lib/routing-table.yaml` consulted (Bundle 2+3: 70 rules; Bundle 4 extends with Bundle 4 role archetypes)
- [ ] Acknowledge §0 Mission Statement and §11.4 Mantra internally before first dispatch
- [ ] Confirm dispatch sequence: Phase A pre-read → Parts 7+9+10 in parallel within HD-02 N=2 OR sequentially → Phase H END-OF-CYCLE D27 supplement
- [ ] Confirm output paths in §8 are mkdir-ready (parent dirs exist or will be created)

When all bullets ticked: dispatch Phase A pre-read confirmation. Then proceed.

---

## §13 Reference — what NOT to do

1. **DO NOT re-litigate Bundles 1+2+3 LOCKED schemas** (F-G-R, Default-Deny, blast-radius, AWAITING-APPROVAL packet schema, Halt-Log-Alert, Corrigibility, Parts 1-6+8 architectures, C1+C2 Joint Design canonical answers, routing-table.yaml, task-return-packet.json, message schema v2.0.0, canonical health-signal schema, SLI/SLO schema, methodology promotion pipeline). Bundle 4 CONSUMES these as F8 / F5 constitutional contracts.
2. **DO NOT skip the M5 inter-Part lite coherence check** (post-integrator, pre-critic). UND-3 finalization + C4 nomenclature fix + OQ-B1-5 D27 cross-ref MUST verify.
3. **DO NOT skip the Wisdom Application Loop.** It is the central directive.
4. **DO NOT auto-launch Wave D.** Always STOP after Bundle 4 AWAITING-APPROVAL.
5. **DO NOT fabricate Wisdom YES entries** to satisfy the loop. Zero adoption with reasoning > fake adoption.
6. **DO NOT use generic `depends-on` edges.** A.14 typed edges only. **C4 fix Part 9 §D `methodologically-uses Part 6` not `PhaseOf Part 6`.**
7. **DO NOT cite without consequence sentence within 200 chars.** Cargo-cult is the failure mode.
8. **DO NOT exceed 20K words per part doc with redundancy padding.** Tighten before critic.
9. **DO NOT come in under 10K words per part doc.** Re-dispatch integrator with operational expansion mandate.
10. **DO NOT silently override expert dissent.** Preserve in dissent.md.
11. **DO NOT touch the Untouchable trees** (§10.8) or Security paths (§10.10).
12. **DO NOT push to `main`.** Branch `claude/jolly-margulis-915d34` only.
13. **DO NOT use `--amend` / `--no-verify` / force-push.**
14. **DO NOT reference any provider API-key env var** in code paths brigadier produces.
15. **DO NOT confuse Foundation with RUSLAN-LAYER.** §X section is mandatory; **Bundle 4 NEW §X requirements per §6.7-§6.10**.
16. **DO NOT include executor names in Bundle 4 Foundation artefacts.** IP-1 strict — model names, agent file paths, instance IDs are RUSLAN-LAYER `executor-binding.yaml` only.
17. **DO NOT make Part 7 cadence calendar-cron-gated or cycle-boundary-gated.** Per OQ-5 Ruslan ack — event-driven only. Throughput bottleneck prevention rationale in §E Laws.
18. **DO NOT omit Part 9 IP-2 single-owner declaration in §X.** Per FUNDAMENTAL §2.6 + IP-2: Phase A single-owner bounded; F.9 Bridge structural change ≥35% at >10× scale; multi-owner stub fields in §I (NOT implemented; Phase B).
19. **DO NOT use `PhaseOf Part 6` in Part 9 §D.** C4 nomenclature fix: `methodologically-uses Part 6`. Brigadier autocheck rejects.
20. **DO NOT make Part 10 privacy BEHAVIORAL.** Per FUNDAMENTAL §6.4: STRUCTURAL — schema fields (`consent_recorded_at`) + lint signals (`/lint --check-protected-inference`) + Default-Deny entries (race/religion/political/health Tier 0 hard); behavioral framing prose <10% of section.
21. **DO NOT leave Part 10 §X fork-separation ambiguous.** Per OQ-MERGED-3 FINAL CLOSURE: explicit DACH ICP / German GDPR / Linear+GitHub+Notion auth-token / contact-list / DACH intelligence URL examples MANDATORY. Critic gate auto-rejects.
22. **DO NOT redesign CRM.** Per §2.3 special: existing 24 source files / 35 unit tests / 10 skills / 4 schemas operational. Part 10 CANONICALISES — does NOT modify implementation. Improvements → log as OQ-B4-X for Wave D.
23. **DO NOT defer OQ-B1-5 D27 supplement past Bundle 4.** Per §4.5 Phase H: END-OF-CYCLE single commit at end of Bundle 4 cycle. Analogous to OQ-B2-A pattern (Bundle 3 inverted timing).
24. **DO NOT propose bullets outside §2 scope.** Bundle 4 = Parts 7+9+10 with the 10 bullets enumerated (3 P7 + 3 P9 + 4 P10). Other parts (1-6+8) are LOCKED Bundles 1+2+3.
25. **DO NOT prematurely lock Phase B work.** C3 Phase A inbound external = Phase B; multi-owner = Phase B F.9 Bridge; live integration adapter implementation = Phase B; live `/lint --check-protected-inference` = Phase B; live calibrated SLI/SLO thresholds = Phase B (per Bundle 3 Part 8 specify-and-stub pattern). Bundle 4 = SCHEMAS + STUB SPECS only for Phase B work.
26. **DO NOT skip Phase H END-OF-CYCLE supplement record.** OQ-B1-5 D27 promotion is constitutional. Single commit at end of cycle.
27. **DO NOT introduce Joint Design Phase like Bundle 2/3.** Bundle 4 has no BLOCKING contradictions — UND-3 is finalization (M5 lite coherence inline).

---

## §14 Final note from Ruslan (paraphrased intent, brigadier internalize)

Bundle 4 is the fourth and final compounding step of Wave C. Bundle 1 froze the constitutional contracts; Bundle 2 wired the productive layers; Bundle 3 closed the compound + observability loops; Bundle 4 closes the world-touching layers:

- **Execution loop (Part 7)**: every project the system runs goes through a canonical state machine (5 states past-participle compliant), with appetite-as-CONSTRAINT per Singer Shape Up, with stage-gate predicates per Part 6b §I.2 F8 LOCKED, with event-driven cadence per OQ-5 (NOT calendar-cron / NOT cycle-boundary-gated), with retrospective emission to Part 5 closing UND-3. **Without Part 7 the system has projects but no lifecycle — appetite drifts, stage transitions ad-hoc, retrospectives starve the compound loop.**

- **Owner attention loop (Part 9)**: every day the owner runs the system through a canonical interaction shape (morning intent → cycle dispatch → afternoon execution → evening reflection committed) and every week through a weekly review with draft-disposition table (C2 producer side complete). The 3-tier SLA taxonomy is canonicalised. **Part 9 = single-owner Phase A bounded per IP-2 + FUNDAMENTAL §2.6** — multi-owner Phase B/C requires F.9 Bridge structural change ≥35%. **Without Part 9 the system has agents but no canonical owner interface — Ruslan's attention budget gets shredded by ad-hoc surfacing patterns.**

- **External world loop (Part 10)**: every contact, every external action, every intelligence signal flows through Part 10's canonical CRM data model + integration adapter pattern (RT-1 + RT-2) + privacy invariants (4 STRUCTURAL invariants — schema fields + lint signals + Default-Deny entries; NOT behavioral framing). **CRM is OPERATIONAL** — cycle 10 already shipped 24 source files / 35 unit tests / 10 `/crm-*` skills / 4 YAML schemas. Part 10 CANONICALISES — does NOT redesign. **OQ-MERGED-3 FINAL CLOSURE for Foundation** — Bundle 4 is last opportunity for fork-separation declaration. Part 10 §X must declare DACH ICP / German GDPR / auth-token / contact-list / intelligence-URL examples explicitly.

From here on:

- Every project the system runs flows through Part 7 state machine with stage-gate predicates → AWAITING-APPROVAL `gate_class: stage_gate` → Ruslan ack → execution cycles → closure events emitting `project-retrospective-packet.json` to Part 5 (UND-3 closed). The execution is closed-loop.
- Every day Ruslan runs the system flows through Part 9 daily-log → cycle dispatch via Part 4 → afternoon execution → evening reflection → weekly review with draft-disposition table → methodology candidates surface to Part 5. The owner attention is closed-loop.
- Every external action the system takes flows through Part 10 RT-2 write-ack → consent verification → blast-radius classify → AWAITING-APPROVAL `gate_class: stage_gate` → Ruslan ack → integration adapter → CRM event log + approval log + cross-fork-provenance log. The external world is closed-loop.
- Every fork (Phase B partner, Phase C product, Phase D org) imports Bundle 4 schemas (project schema + state machine + appetite + scope record + daily-log + weekly-review + SLA taxonomy + CRM data model + integration adapter pattern + privacy invariants + write-ack discipline + reconciliation strategies) as Foundation generics; Ruslan-specific bindings (8 active project specifics + attention budget value 20 + SLA times + DACH ICP + German GDPR + contact lists + auth tokens + DACH intelligence URLs) overlay as RUSLAN-LAYER.

If Bundle 4 is half-baked, Wave D integration pass inherits incomplete execution / owner / external loops. If Bundle 4 over-engineers Phase B/C/D scenarios, Phase A delivery drags.

The right level: **single-owner Phase A €50K horizon, but FORK-READY to scale**. Project lifecycle canonicalised now means Phase B partners inherit a working state machine, not ad-hoc project tracking. Owner interaction schemas declared now means Phase B multi-owner fork starts with explicit F.9 Bridge work, not retroactive multi-owner refactor. CRM canonicalisation + privacy STRUCTURAL + fork-separation FINAL CLOSURE now means Phase B partner forks Foundation generic + declines RUSLAN-LAYER + reconciliation strategy applied via `cross-fork-provenance.json` D27 promotion — clean Phase B import, no merge conflicts, no privacy invariant violations.

This is the architecture document a Phase B partner can read in 60 minutes (matching Bundle 2/3) and import in half a day. Make it the document where the WISDOM IS APPLIED OPERATIONALLY (≥85% per Bundle 4 inherited Bundle 3 floor; should easily match given P7+P9+P10 inherently operational).

**OQ-MERGED-3 FINAL CLOSURE — Bundle 4 = last chance for Foundation-level fork-separation.**
**OQ-5 cadence event-driven held — Part 7 §E Laws verbatim.**
**IP-2 single-owner bounded held — Part 9 §X declaration + multi-owner stub §I.**
**Privacy STRUCTURAL held — Part 10 §I + §H + §F schema fields + lint signals + Default-Deny entries.**
**OQ-B1-5 D27 supplement END-OF-CYCLE — single commit at Phase H.**
**CRM canonicalisation NOT redesign — existing 24 source files / 35 unit tests / 10 skills / 4 schemas referenced.**
**OQ-MERGED-2 dissolve-test Cycle 2 of 3 — evidence accumulator logged.**

**THIS IS WAVE C CLOSURE.** After Ruslan ack of Bundle 4 → Wave C COMPLETE → Wave D integration pass dispatch (separate cycle).

---

*End of deep prompt. Read three times before first dispatch.*
