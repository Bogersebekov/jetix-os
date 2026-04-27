---
title: ROY Brigadier Deep Prompt — Wave C Bundle 3 (Parts 5 + 8 — Compound Learning + Health Monitoring)
date: 2026-04-28
type: deep-prompt
target: ROY brigadier (.claude/agents/brigadier.md)
parent_brief: prompts/cloud-code-wave-c-bundle-3-prompt-writing-brief-2026-04-28.md
predecessor_deep_prompt: prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md
predecessor_ack_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
predecessor_ack_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
bundle_scope:
  - "FIRST TASK — OQ-B2-A retroactive Bundle 1 supplement (~30 min)"
  - "Part 5 — Compound Learning & Methodology Capture"
  - "Part 8 — Health Monitoring & System Integrity"
estimated_walltime: 4-7h (3-6h ROY substantive + 30 min retroactive supplement + verification gates)
status: ready-for-brigadier-dispatch
constitutional_baseline_bundle_1: 2026-04-28 Ruslan ack of Bundle 1 (RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md) — F-G-R F8 / Default-Deny F8 / Blast-radius F8 / AWAITING-APPROVAL packet schema F8 / Halt-Log-Alert F8 / Corrigibility F8
constitutional_baseline_bundle_2: 2026-04-28 Ruslan ack of Bundle 2 (RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md) — Parts 2/3/4 architectures F5 / C1 Joint Design Variant A F5 / routing-table.yaml F4 / task-return-packet.json schema F4 / WORD COUNT TARGET 10K-20K F8 / message schema v2.0.0 F4
mantra: "QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. SPECIFY-AND-STUB > LIVE-IMPLEMENTATION (Part 8). STANDALONE-PRESERVED > DISSOLVE (Part 5 — until evidence). RUSLAN-ACK > BRIGADIER-CONFIDENCE."
---

# Wave C Bundle 3 — ROY Brigadier Deep Prompt

## §0 Mission Statement (READ FIRST, INTERNALIZE)

**Bundle 3 wires the compound-learning loop and the observability substrate atop the Bundle 1 + Bundle 2 layers.**

Bundle 1 produced the constitutional substrate (Part 1 System State, Part 6a Provenance Officer, Part 6b Human Gate). Bundle 2 produced the information lifecycle and agent coordination layers (Part 2 Signal Ingestion, Part 3 KB & Methodology Library, Part 4 Role Taxonomy & Coordination). Both bundles are LOCKED-canonical. F8 schemas are immutable. F5 architectures are stable. **Bundle 3 CONSUMES — never re-litigates.**

Bundle 3's two parts close two of the most consequential feedback loops in the system:

- **Part 5 — Compound Learning & Methodology Capture** — closes the **R2 reinforcing loop** (Senge): every cycle's execution becomes input to the next cycle's improved execution. The 40/10/40/10 ritual (FUNDAMENTAL §2.2) is canonicalised here. The DRR ledger that lives in `agents/<id>/strategies.md` is given a structured intake schema. The methodology promotion pipeline (UND-2) that rises validated patterns from per-agent `strategies.md` to `wiki/methodology/<rule-slug>.md` canonical entries is fully specified. **Without Part 5, the system learns nothing across cycles — it executes brilliantly once, then re-derives the same lessons next cycle.**

- **Part 8 — Health Monitoring & System Integrity** — closes the **immune-system loop** (Beer VSM S3 Audit/Optimisation): the system surfaces silent degradation before it becomes catastrophic. SLI/SLO schema, error-budget burn-rate triad (1×/6×/14.4× per SRE Workbook Ch.2 already embedded in Part 1 §J), weekly health dashboard, quarterly immune audit. Per OQ-MERGED-5 ack: **"specify and stub" — schemas + templates + stub alert routing; NOT live metrics implementation.** Live calibration is Phase B (2-3 month operational data accumulation). **Without Part 8, the system has no eyes — drift is invisible until catastrophe.**

**Treat with 1 trillion percent responsibility.**

The constitutional contract from Bundle 1 + Bundle 2 is permanent. Every Bundle 3 part calls Part 1 §H operations for canonical writes; every emitted artefact carries F-G-R per Part 6a §I.1 F8 schema; every promotion event logs to `swarm/approvals/log.jsonl`; every gate packet conforms to Part 6b `awaiting-approval-packet.json` F8 schema with `gate_class` enum `[stop_gate, stage_gate, draft_promotion]`. Methodology promotions invoke Part 6b with `gate_class: draft_promotion`. Tier 0 health-integrity events route through Part 6b with `gate_class: stop_gate`. Part 5 consumes the raw `task-return-packet.json` schema (F4 LOCKED in Bundle 2 Part 4 §I.1) and does its own DRR extraction (per UND-1 Ruslan ack). Part 8 consumes Part 1 §B Four Golden Signals and per-Part health emissions per the canonicalised health-signal schema.

Read this prompt three times before dispatching. Read every linked constitutional artefact in §3 before composing your first dispatch. When in doubt, ask Ruslan via HITL escalation.

> *Ruslan emphasis (verbatim, original Russian, do NOT paraphrase before applying):*
> *«Чтобы вся вот эта мудрость, наработки из книг — они были применены в системе,*
> *если это возможно, если нужно, целесообразно — на 1000% насколько это*
> *целесообразно. Ещё чтобы задавались вопросы как мы можем конкретно добавить,*
> *нахуй, эту штуку, чтобы было ещё отдельный прогон где вся эта залупа даёт*
> *обратную связь — а как мы можем это улучшить с точки зрения такой-то книжки*
> *или с книжки такой-то.»*

The Wisdom Application Loop (§5) is the structural mechanism that operationalizes Ruslan's central directive. **Bundle 3 raises the operational adoption ratio target from Bundle 2's ≥60% floor to ≥85%** because Compound Learning + Health Monitoring are inherently operational domains (DRR schemas / SLI/SLO triads / lint check definitions / failure-mode tables — not philosophical framing prose). If aggregate ratio drops below 85%, that is a red flag — investigate; brigadier may be reverting to philosophical content despite the Bundle 2 lesson.

**Bundle 3 introduces three structural firsts:**

1. **A retroactive supplement phase** — before substantive Bundle 3 dispatch, ROY MUST execute the OQ-B2-A retroactive Bundle 1 fix (~30 min). This aligns Part 1 §I.4 stub `gate_class` enum to Part 6b §I.4 F8 LOCKED `[stop_gate, stage_gate, draft_promotion]`, adds `[swarm-lib]` token to commit-format-tokens.json, and introduces NEW K15 upcasting failure mode for legacy v1.0.0 messages. **First task, single commit. THEN Bundle 3 substantive work begins.**

2. **A dissolve-test declaration window** — Bundle 3 is the first cycle of the OQ-MERGED-2 dissolve-test window. Part 5 §X MUST explicitly declare the dissolve-test condition with engineering-expert dissent preserved. Threshold: ≥3 distinct compound-phase-exclusive operations across Bundle 3 + Bundle 4 + Wave D = standalone preserved; <3 = dissolve hypothesis activates and the Wave D ack cycle decides whether Part 5 dissolves into Parts 3+4. **Brigadier does NOT decide this in Bundle 3. Brigadier DECLARES the test condition.**

3. **A scope-creep autocheck for Part 8 ("specify and stub")** — Part 8 Wave C output is SLI/SLO schema + health signal schema canonicalisation + template authoring + alert-routing stub. NOT live metrics implementation. NOT calibrated thresholds. If brigadier produces "live implementation spec" — that is scope creep. The autocheck is structural: §K Failure Modes section MUST declare "K-PartB — over-implementation drift" as a self-monitored failure mode, and brigadier MUST verify §I schemas reference FUNDAMENTAL §3 30+ SLI/SLO pairs as **calibration parameters with explicit calibration-cadence and starter-value-label fields**, not as production-grade thresholds.

---

## §1 Constitutional Inputs (Bundle 1 + Bundle 2 LOCKED — DO NOT re-litigate)

### §1.1 F8 LOCKED schemas (consumed verbatim)

| Constitutional artefact | F-level | Bundle 3 consumption rule |
|---|---|---|
| `f-g-r.json` (Part 6a §I.1) | F8 | Every Bundle 3 architecture document, every emitted DRR / methodology / health snapshot / immune-audit artefact carries F-G-R tag per OQ-B1-1 anchor wording (F4="≥3 cycles applied"; F6="cross-cycle reuse evidence"; F8="FUNDAMENTAL Vision lock-class"). Inline `[F4|G:scope|R-medium]` OR §G table. |
| `awaiting-approval-packet.json` with `gate_class` enum (Part 6b §I.1) | F8 | Part 5 methodology-promotion packets use `gate_class: draft_promotion`; Part 8 Tier 0 health-integrity events use `gate_class: stop_gate`; Part 8 stage-bound observability changes use `gate_class: stage_gate`. Schema fields are FROZEN — consume verbatim. |
| `default-deny-table.yaml` (Part 6b §I.3) | F8 | Part 8 alert classes that are novel = Default-Deny classified into Tier 0/1/2/3 before alert routing fires. |
| `blast-radius-table.yaml` 4 tiers (Part 6b §I.4) | F8 | Part 8 maps every alert class to Tier 0 (auto-halt) / 1 (Ruslan ack) / 2 (batch ack) / 3 (auto-log). Halt-Log-Alert ordering enforced. |
| Halt-Log-Alert primitive (Part 6b §E Law L9) | F8 | Part 8 alert delivery conforms to ≤1s halt / ≤5s log / ≤60s alert ordering invariant for Tier 0 events. |
| Corrigibility (Part 6b §E Law L9 / Askell HHH Appendix E.2 verbatim) | F8 | NO Bundle 3 mechanism may lock Ruslan out of override. Part 8 health-integrity halt is Halt+Alert, NOT lock-out — Ruslan can `git revert` any health snapshot, manually edit any audit report, override any alert. |

### §1.2 F5 LOCKED architectures (consumed as canonical contracts)

| Architecture | F-level | Bundle 3 consumption rule |
|---|---|---|
| Part 1 §B Four Golden Signals + §J burn-rate table 1×/6×/14.4× | F5 | Part 8 §A Inputs lists Part 1 as primary signal source; Part 8 §I.1 SLI/SLO schema adopts Part 1's burn-rate algebra without re-derivation. |
| Part 1 §H commit interface | F5 | Part 5 strategies.md updates committed via Part 1 §H; Part 8 health snapshots committed via Part 1 §H; methodology promotions committed via Part 1 §H. |
| Part 1 §I.4 task-return-packet stub (post-retroactive-supplement) | F5 | Part 5 §A Inputs declares Part 4 as upstream emitter; consumes the FULL schema canonicalised in Part 4 §I.1 (UND-1 binding). |
| Part 6a §I.1 F-G-R schema | F8 | Every Bundle 3 promoted claim carries F-G-R; every methodology entry post-promotion carries F5+; every health snapshot carries F-G-R. |
| Part 6a §C approval log structure (`swarm/approvals/log.jsonl`) | F5 | Every Bundle 3 promotion event (methodology / health audit / alert) logs entry. |
| Part 6a quarterly immune audit framework | F5 | Part 8 quarterly immune audit INVOKES Part 6a as service for F-G-R compliance check (TRADEOFF-01 split materialised — Part 8 audit lead, Part 6a audit support, Part 6b enforcement arm). |
| Part 6b §I.2 stage-gates registry | F8 | Part 5 methodology promotion (draft_promotion gate) checks against this registry. |
| Part 3 §E L9 methodology promotion admissibility predicate | F5 | Part 5 emits methodology candidates conforming to (≥1 DRR `result: validated` from ≥2 cycles + `rule_slug:` + F4→F5 rise on owner ack). Part 5 owns the EMISSION; Part 3 owns the ADMISSION. |
| Part 3 §I.2 `wiki/methodology/` entity-type | F5 | Part 5 promoted artefacts land at `wiki/methodology/<rule-slug>.md` with `entity_type: methodology` frontmatter. |
| Part 4 §I.1 `task-return-packet.json` FULL schema (UND-1 binding) | F4 | Part 5 §A Inputs CONSUMES raw packets per Ruslan ack OQ-3 ("Part 5 receives raw task-return packets, does own DRR extraction"). F4→F5 rises on Bundle 3 Part 5 consumption validation. |
| Part 4 §H message schema v2.0.0 (`acting_as:` mandatory) | F4 | Part 5 + Part 8 outputs use v2.0.0 schema — `acting_as:` field populated on every emit. |
| Part 4 §I `executor-binding.yaml` template | F4 | Part 5 + Part 8 reference role archetypes only (IP-1 strict — NO executor names in Bundle 3 Foundation artefacts; executor bindings live exclusively in RUSLAN-LAYER `executor-binding.yaml`). |
| `swarm/lib/README.md` (C1 Joint Design canonical) | F4 | Part 5 invokes accessor skills via swarm/lib/ per Part 3 LEAD + Part 4 ADVISORY ownership; Part 8 `/lint` extensions land in swarm/lib/ following same governance. |
| `swarm/lib/routing-table.yaml` ≥67 routing rules | F4 | Part 5 + Part 8 add their per-role entries (compound-phase orchestration role; health-monitor role) to routing-table.yaml as Bundle 3 deliverable extension. |
| PARA-tier mandatory frontmatter (Bundle 2 P2.2) | F5 | Part 5 methodology entries tagged `para_tier: Resource` (reusable patterns) or `para_tier: Archive` (deprecated patterns). Part 8 health snapshots tagged `para_tier: Area` (ongoing operational concern). |

### §1.3 Bundle 3 OQ inputs (from prior Ruslan acks — NO re-litigation)

| OQ | Status | Bundle 3 implication |
|----|--------|----------------------|
| **OQ-MERGED-2** | Part 5 STANDALONE preserved (dissolve-test active) — engineering-expert dissolve dissent preserved | Bundle 3 = first cycle of dissolve-test window. Part 5 §X MUST declare dissolve-test condition explicitly. Threshold: ≥3 distinct compound-phase-exclusive operations across Bundle 3 + Bundle 4 + Wave D = standalone preserved. Engineering-expert dissent linked from Part 5 §X to original interface card §H + consultant card cross-ref. |
| **OQ-1 / TRADEOFF-01** | Part 8 = AUDIT LEAD; Part 6a = audit SUPPORT (service invocation); Part 6b = ENFORCEMENT ARM | Part 8 quarterly immune audit invokes Part 6a as a service for F-G-R compliance check across wiki entries; Part 6b receives any drift-detected remediation gate. Beer VSM S3 split clean — Part 8 owns audit cadence + scope; Part 6a owns the F-G-R check primitive (Bundle 1 quarterly framework); Part 6b owns the enforcement gate. |
| **OQ-MERGED-5** | Part 8 "specify and stub" Wave C; full impl Phase B | Bundle 3 Part 8 = SLI/SLO schema + health signal schema + template authoring + alert-routing stub. NOT live metrics implementation. NOT calibrated thresholds. FUNDAMENTAL §3 30+ SLI/SLO pairs = starter values requiring 2-3 months Phase B calibration. |
| **C2 contradiction (Bundle 1 carry-over)** | Part 8 owns canonical health signal schema; Bundle 1 + 2 emitters align | Bundle 3 Part 8 §I.1 CANONICALIZES the health signal schema; Parts 1 + 2 + 3 + 4 emitter shapes already declared at stub level (Part 1 §I.5; Part 3 §I.6; Part 4 §I.4). Bundle 3 Part 8 §I.1 declares whether emitters retroactively align (mapping table referenced) or Part 8 explicitly accepts current heterogeneous emitter shapes with mapping declared. **Brigadier decision in Joint Design lite session §4.3.** |
| **UND-2** | Methodology promotion pipeline schema (P5 work) | Bundle 3 Part 5 §I — schema for `wiki/methodology/<rule-slug>.md` admissibility entry format + promotion event format; Part 5 §J ritual declaring promotion sequence at compound phase boundary (cross-ref to Part 3 §I.2 promotion sequence — DRY enforced). |
| **UND-3** | P7 → P5 retrospective schema + cadence (joint Bundle 4 work) | Bundle 4 Part 7 work. Bundle 3 Part 5 §A Inputs declares Part 7 as upstream source with **stub schema reference** (`task-return-packet.json` superset OR `project-retrospective-packet.json` TBD); marked Phase 2 (Bundle 4) finalization. Avoid premature lock — Part 7 will conform to Part 5's input contract in Bundle 4. |
| **UND-1** | Part 5 receives RAW task-return packets, does own DRR extraction | Bundle 3 Part 5 §B specifies CONSUMPTION pattern: Part 5 reads RAW packets from `comms/mailboxes/`; performs DRR extraction (Decision / Reasoning / Result / Review per Compounding-Engineering §2 P2); writes DRR entries to `agents/<id>/strategies.md`. Part 4 §I.1 schema is upstream FROZEN contract. |

### §1.4 OQ-B2-A retroactive Bundle 1 fix (FIRST TASK before substantive dispatch)

**~30 min effort. Single commit at start of Bundle 3 cycle. BLOCKING — substantive Bundle 3 work does NOT begin until this completes and pushes.**

Three coordinated edits to Bundle 1 + Bundle 2 architectures:

1. **Part 1 §I.4 stub `gate_class` enum alignment.** Current stub state: `enum: ["autonomous", "requires-approval", "hitl-required"]` (stale; pre-Bundle-1 nomenclature). Target state: `enum: ["stop_gate", "stage_gate", "draft_promotion"]` (Part 6b §I.4 F8 LOCKED schema). Edit `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` §I.4. Cross-reference Part 6b §I.4 in inline citation. Update §G F-G-R table if affected.

2. **`[swarm-lib]` token added to Part 1 §I.2 commit-format-tokens.json schema.** Current state: token list does not include `swarm-lib` (per Bundle 2 P3.1 + P4.2 C1 Joint Design canonical, accessor pipeline lives in `swarm/lib/` — Bundle 2 commits used `[swarm-lib]` informally; canonicalise it now per OQ-B2-D ack). Edit `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` §I.2. Add token entry. Cross-reference Bundle 2 C1 Joint Design canonical answer.

3. **NEW K15 upcasting failure mode added to Part 1 §K.** Per Bundle 2 Decision #6: message schema v1.0.0 → v2.0.0 BREAKING change with `acting_as:` mandatory + `from:` enum extended. Part 1 commit substrate may receive legacy v1.0.0 messages from pre-Bundle-2 cycles in operational use. K15 specifies behaviour: detect schema_version field; if v1.0.0, upcast to v2.0.0 by injecting `acting_as: <inferred-from-from-field>` OR reject with specific error if upcast cannot be inferred. Hamel-binary acceptance predicate: every legacy message either upcasts cleanly or rejects with named field; no silent acceptance of malformed v1.0.0 messages.

**Update record:** Append retroactive correction note to `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` §6 ("retroactive corrections per OQ-B2-A applied at Bundle 3 cycle start; commit hash: <new>") OR create supplement file `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md` with the retroactive note (brigadier picks based on file size convention).

**Single commit:**
```
[architecture] Bundle 1 retroactive supplement — Part 1 §I.4 gate_class enum + commit-format-tokens.json [swarm-lib] token + K15 upcasting (per OQ-B2-A + OQ-B2-D RUSLAN-ACK Bundle 2)
```

**Push.** Then proceed to substantive Bundle 3 dispatch. NO substantive Part 5 / Part 8 cell dispatch BEFORE this commit lands.

### §1.5 Cross-cuts within Bundle 3 (apply throughout)

| Cross-cut | Rule | Where applied |
|---|---|---|
| **F-G-R DOGFOOD per F8 schema** | Every Bundle 3 promoted claim carries F-G-R per Bundle 1 Part 6a §I.1 schema | §G F-G-R Tagging table; inline tags |
| **A.14 typed edges** | Bundle 1 canonical 10-edge reference table consulted; NO new edge types invented; NO generic `depends-on` | §D Dependencies (every entry) |
| **Append-only** | strategies.md / methodology entries / health snapshots / immune-audit reports / alert log — append-only | §C Side-effects; §I Data schemas |
| **L/A/D/E** | Every §E Boundary section structured per FPF A.6.B Norm Square (Laws / Admissibility / Deontics / Effects) | §E section per part |
| **Foundation vs RUSLAN-LAYER fork-separation** | Explicit §X per part | §X mandatory |
| **PARA-tier mandatory** | Methodology entries (Part 5) tagged `para_tier: Resource` (reusable) or `Archive` (deprecated); health snapshots (Part 8) tagged `para_tier: Area` | Part 5 emit rule + Part 8 emit rule |
| **IP-1 Role≠Executor** | Role manifests + routing-table.yaml entries use role archetype names; NO executor names, model names, agent file paths in Bundle 3 Foundation artefacts | §A / §B / §H / §I per part |
| **Operational ratio ≥85% (Bundle 3 stricter target)** | Wisdom Loop OPERATIONAL/PHILOSOPHICAL discriminator — Bundle 3 should easily exceed (compound learning + observability are inherently operational) | §M Wisdom Findings table per part |
| **Word count 10K-20K per part** | NEW constitutional target per RUSLAN-ACK Bundle 2 §3 F8 | §6 Quality bar |
| **Part 5 dissolve-test declaration** | Part 5 §X MUST declare OQ-MERGED-2 dissolve-test condition with explicit threshold | Part 5 §X mandatory |
| **Part 8 "specify and stub" scope** | Part 8 = schemas + templates + stub routing; NOT live metrics; FUNDAMENTAL §3 starter values labeled calibration-grade | Part 8 §I + §J + §K + §X |
| **TRADEOFF-01 split materialisation** | Part 8 audit lead invokes Part 6a service for F-G-R compliance check; Part 6b enforcement arm | Part 8 §H + §I + §J |
| **C2 health signal schema canonicalisation** | Part 8 §I.1 owns canonical health signal schema; Bundle 1 + 2 emitter shapes mapping declared | Part 8 §I.1 + retroactive supplement (if needed) |
| **UND-2 methodology promotion pipeline** | Part 5 §I declares schema; Part 3 §I.2 promotion sequence cross-referenced (DRY) | Part 5 §I + cross-ref to Part 3 |
| **UND-3 P7↔P5 stub** | Part 5 §A Inputs declares Part 7 as Phase 2 finalization upstream — stub reference, no premature lock | Part 5 §A + §I + cross-ref artefact `swarm/wiki/cycles/.../bundle-3/UND-3-stub.md` |

---

## §2 Bundle 3 Scope — Two Parts, Seven Bullets (after retroactive supplement)

### §2.1 Part 5 — Compound Learning & Methodology Capture (3 bullets, ~M total)

**Source**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 5.
**Interface card**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` (123 lines).

**Bullet P5.1 — Compound ritual as canonical Foundation artefact (40/10/40/10).**
- Output: Part 5 architecture document at `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` (10K-20K words) declaring the compound ritual as a discrete Foundation artefact. Required content: (a) cadence definition (Plan 40% / Work 10% / Review 40% / Compound 10% with ±10pp drift tolerance per FUNDAMENTAL §3.3.1); (b) mandatory compound-phase outputs (DRR entry in `agents/<id>/strategies.md` PLUS at least one methodology pattern candidate when applicable); (c) compound-phase trigger predicate (event-driven on cycle close OR scheduled at week boundary — brigadier picks one explicitly with rationale); (d) health SLI "compound-application-rate ≥ 80%" as acceptance predicate (cross-ref Part 8 §I.1 for canonical SLI/SLO schema).
- DRR schema: 4-part entry (Decision / Reasoning / Result / Review) + `rule_slug:` for deduplication + `validated_in_cycles: [<cycle-id>]` accumulator + `ratio: {hits, misses}` counter + `created_at:` + `last_validated_at:`.
- Acceptance predicate: synthetic fixture of 3 cycle-close events; Part 5 emits 3 DRR entries (or 3×N if multiple roles have learnings); `agents/<id>/strategies.md` updates committed via Part 1 §H; compound-application-rate metric ≥0.8 in test fixture.
- F-G-R: F4 architecture-time → F5 on Bundle 3 owner ack; cadence ratio inherits F5 from FUNDAMENTAL §2.2 constitutional value (already F5).
- **Reuses existing pattern**: `agents/<id>/strategies.md` files already exist (8 of them per AUDIT §4); 19 strategy entries already accumulated per `swarm/wiki/meta/health.md`. **Canonicalise — do NOT reinvent.**
- Source: interface card §A-§B; Compounding-Engineering §2 (Plan/Work/Review/Compound main loop) + §4 P2 (DRR ledger as append-only compound memory); FUNDAMENTAL §2.2 + §3.3.1; systems-thinking-cybernetics consultant card §4 R2 reinforcing loop (5-10 cycle delay before compound effect detectable).

**Bullet P5.2 — Methodology promotion pipeline (UND-2 binding).**
- Output: Part 5 §I.1 — schema for methodology promotion pipeline. Pipeline stages: (1) DRR entry accumulates in `agents/<id>/strategies.md`; (2) `validated_in_cycles` accumulator reaches ≥2 entries with `result: validated`; (3) `rule_slug` populated and unique (or merging into existing entry per `supersedes:` pointer); (4) Part 5 emits methodology candidate at `wiki/methodology/<rule-slug>-DRAFT.md` with `pipeline: ingested`; (5) brigadier (or owner) emits AWAITING-APPROVAL packet with `gate_class: draft_promotion` to Part 6b; (6) owner acks; (7) entity moves to `wiki/methodology/<rule-slug>.md` with `pipeline: ready`, F4→F5 promotion, `human_acked_at:` populated; (8) `swarm/approvals/log.jsonl` (Part 6a §C) entry; (9) `wiki/index.md` updated.
- Cross-reference: Part 3 §E L9 admissibility predicate (≥1 DRR `result: validated` from ≥2 cycles + `rule_slug:` + F4→F5 rise) — Part 5 §I.1 references Part 3 §E L9 + §I.2 promotion sequence. **DRY enforced**: Part 5 owns the EMISSION schema; Part 3 owns the ADMISSION schema; both reference each other; do NOT duplicate.
- Acceptance predicate: synthetic fixture of methodology candidate carrying ≥2 validated DRR markers + rule_slug; AWAITING-APPROVAL `gate_class: draft_promotion` packet emitted; Part 6b ack simulated; entity at `wiki/methodology/<slug>.md` with F5 + ClaimScope + `refuted_if`; passes Part 3 `/lint`; `swarm/approvals/log.jsonl` entry visible.
- F-G-R: F4 architecture-time → F5 on Bundle 3 owner ack; promoted methodology entries themselves carry F5 post-promotion.
- Source: dependency-graph §4.3 UND-3 (joint Part 3 + Part 5 — Part 3 side resolved Bundle 2; Part 5 side resolved Bundle 3); part-5 §G F-G-R "methodology pattern promoted: F4→F5 on promotion"; Compounding-Engineering §5 (validated pattern threshold) + §4 P2 DRR ledger; KM consultant §6 Part 3 item 1 (Karpathy wiki proves itself by accumulating validated entries).

**Bullet P5.3 — OQ-MERGED-2 dissolve-test condition declaration in §X.**
- Output: Part 5 §X Foundation vs RUSLAN-LAYER section declares the dissolve-test condition explicitly. Required content: (a) DISSOLVE-TEST CONDITION verbatim — "If Bundle 3 + Bundle 4 + Wave D show <3 distinct compound-phase-exclusive operations (operations Parts 3+4 cannot capture without invoking Part 5 logic), dissolve hypothesis activates and Wave D ack cycle decides whether Part 5 dissolves into Parts 3+4."; (b) ENGINEERING-EXPERT DISSENT preserved with cross-reference to original dissent record in Wave A interface card §H + cross-reference to systems-thinking-cybernetics consultant card §4 R2 reinforcing loop counter-argument; (c) BUNDLE 3 = FIRST CYCLE OF 3-CYCLE WINDOW declaration; (d) STANDALONE PRESERVATION threshold (≥3 distinct compound-phase-exclusive operations across the 3-cycle window) — Part 5 stays standalone canonical; (e) DISSOLVE PATH if threshold not met — Wave D ack packet redirects compound-phase ownership; engineering-expert dissolve hypothesis re-evaluated; if accepted, bundle redesign initiated before Wave D Part 5 cycle runs.
- Companion artefact: `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` mirrors the §X declaration as a standalone policy file (D25 Company-as-Code — committed canonical artefact).
- Acceptance predicate: §X section non-empty; dissolve threshold numerically declared (≥3 vs <3); engineering-expert dissent linked; companion policy file exists.
- F-G-R: F3 (proposed dissolve-test condition; not validated until Wave D evidence accumulates) → F4 on Bundle 3 owner ack of the test condition itself.
- Source: candidate-parts-merged.md §6 OQ-MERGED-2; part-5 §H "dissent preserved — dissolve path held open contingent on OQ-MERGED-2 Ruslan ack"; A-1-critic-gate.md §4 OQ-MERGED-2; dependency-graph.md §2.4 P4↔P5 R2 reinforcing loop note.

### §2.2 Part 8 — Health Monitoring & System Integrity (4 bullets, ~M-L total)

**Source**: wave-c-worklist §2 Part 8.
**Interface card**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md` (138 lines).

**Bullet P8.1 — SLI/SLO schema definition + canonical health signal schema (C2 resolution).**
- Output: Part 8 architecture document at `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` (10K-20K words). Two schemas in §I:
  - §I.1 — canonical health signal schema (`shared/schemas/health-signal.json`): the unified shape every Foundation part emits health signals in. Required fields per signal: `signal_name`, `emitter_part` (e.g., "part-1"), `emitter_section` (e.g., "§J burn-rate"), `value` (numeric), `unit`, `cadence` (event-driven | periodic-Nm | periodic-Nh | periodic-Nd), `measurement_method`, `created_at`, `cycle_id`, `f_g_r` (per Part 6a §I.1 F8). C2 RESOLUTION: Part 8 §I.1 declares canonical schema; Parts 1+2+3+4 emitter shapes (Part 1 §I.5 / Part 3 §I.6 / Part 4 §I.4 — currently heterogeneous stubs) align via mapping table in Part 8 §I.1. **Brigadier decision in Joint Design lite session §4.3**: either retroactively align Bundle 1+2 emitters to Part 8 schema (preferred — DRY) OR Part 8 accepts current emitter shapes with mapping table (fallback if retroactive alignment exceeds 1h budget).
  - §I.2 — SLI/SLO schema (`shared/schemas/sli-slo.json`): formal spec for SLI (Service Level Indicator) + SLO (Objective) + error-budget + burn-rate behaviour-change rule. Required SLI fields: `name`, `signal_ref` (cross-ref to a health-signal definition), `measurement_method`, `cadence`, `starter_value` (with `starter_value_label: "calibration-grade"` mandatory per OQ-MERGED-5), `calibration_trigger` (the cycle/data condition that promotes starter→calibrated value), `calibration_cadence` (e.g., monthly review). Required SLO fields: `name`, `sli_ref`, `target_value`, `error_budget` (1 - target_value), `burn_rate_thresholds: {1x, 6x, 14.4x}` per SRE Workbook Ch.2 (already adopted in Part 1 §J). Required behaviour-change-rule fields: per burn-rate tier, `required_action`. **First 8-10 SLI entries** (one per major health domain — git substrate / triage pipeline / KB freshness / mailbox cycle time / DRR write rate / gate-open count / project state distribution / daily log creation rate). All starter values explicitly labeled.
- Acceptance predicate: both schemas structurally complete; ≥8 SLI entries in §I.2 with starter_value_label = "calibration-grade"; mapping table in §I.1 maps Part 1+2+3+4 emitter shapes to canonical schema; synthetic fixture of 5 health signals (Part 1 burn-rate / Part 2 triage backlog / Part 3 lint orphan count / Part 4 mailbox queue depth / Part 5 compound-application-rate) all validate against canonical schema.
- F-G-R: F4 architecture-time → F5 on Bundle 3 owner ack of schemas; SLI starter values F3 until calibrated (per part-8 §G F-G-R interface card mapping).
- Source: FUNDAMENTAL §3 30+ SLI/SLO pairs (calibration parameters); part-8 §E Laws "SLI/SLO values MUST be labeled starter/calibration"; part-8 §G F-G-R "SLI/SLO schema F5 once schema acked"; dependency-graph §3.2 C2; SRE consultant card §4 P1 SLI/SLO/error-budget triad + §4 P7 burn rate behaviour-change; SRE Workbook Ch.2 burn-rate algebra (1×/6×/14.4× already adopted Part 1 §J Bundle 1).

**Bullet P8.2 — Health signal schema per emitting part (C2 resolution — producer side).**
- Output: §I.3 mapping table cross-referencing Bundle 1 + 2 emitters to canonical health-signal schema (P8.1 §I.1). Each Foundation part's §B Outputs row for "Part 8 health signal" mapped to schema field. Specific entries: Part 1 (commit-error-rate, hook-failure-rate, fsck-object-errors, repo-growth, latency-p95) → mapped fields; Part 2 (triage-backlog, STOP-gate-acked-rate, para-tier-coverage) → mapped fields; Part 3 (orphan-anchor-count, stale-claims-count, edges-per-entity-avg, contradicts-supports-density, methodology-admissibility-violations, comparisons-emptiness-flag, malformed-crm-edges) → mapped fields; Part 4 (mailbox-queue-depth, cycle-time-avg, escalation-rate, routing-variety-count, message-schema-version-distribution) → mapped fields; Part 5 (drr-write-rate, compound-application-rate, methodology-promotion-rate, dissolve-test-evidence-count) → mapped fields; Part 6a (approval-log-write-rate, fg-r-compliance-pct, citation-resolution-pct) → mapped fields; Part 6b (gate-open-count, gate-acked-rate, default-deny-classified-pct, blast-radius-distribution) → mapped fields.
- §B Outputs of each Bundle 1 + 2 architecture is referenced (not modified — F5 LOCKED per RUSLAN-ACK records); the mapping table in Part 8 §I.3 is the canonical adapter.
- Acceptance predicate: every Bundle 1 + 2 part has ≥1 row in mapping table; each row populated with canonical-schema field projection; mapping table has F-G-R tag.
- F-G-R: F4 architecture-time → F5 on cross-Bundle reuse evidence (Bundle 4 + Wave D consume).
- Source: dependency-graph §3.2 C2 "no agreed schema — MEDIUM severity"; part-8 §A Inputs (lists per-Part signals); SRE consultant card §4 P3 Three Pillars (logs/metrics/traces).

**Bullet P8.3 — Weekly health dashboard + quarterly immune audit templates.**
- Output: two committed templates as Bundle 3 deliverables.
  - `swarm/audits/weekly-health-template.md` — required sections: Period (Week WNN) + SLI Snapshot Per Domain (table: SLI name / current value / starter value / drift / status) + Anomalies (table: anomaly-type / detected-at / affected-part / severity-tier / recommended-action / J-level-authority-required) + Recommendations ("look here" list per FUNDAMENTAL §1 UC-I.3) + Next-week appetite signals (cross-ref Part 9 weekly review schema Bundle 4) + F-G-R compliance summary (cross-ref Part 6a service invocation result).
  - `swarm/audits/quarterly-immune-audit-template.md` (extends Part 6a Bundle 1 quarterly template) — required sections: Quarter (YYYY-QN) + F-G-R Compliance Sweep (cross-ref Part 6a service invocation; per §I.4 F-G-R compliance check primitive) + Alpha Classification Drift (IP-5 past-participle exception whitelist check) + Role-Manifest Freshness (IP-6 audit) + Methodology Library Staleness (entries with `last_validated_at:` >90d flagged) + Strategies.md Staleness (per-role DRR entry decay) + TRADEOFF-01 Verification (Part 8 → Part 6a service invocation log; Part 6b enforcement gate log) + Drift Remediation Gate Packet (if drift detected, AWAITING-APPROVAL `gate_class: stage_gate` to Part 6b).
- Templates committed at `swarm/audits/` directory; sample populated test row demonstrating fixture compatibility.
- Acceptance predicate: both templates exist with required sections; weekly template populated with synthetic Week-NN row demonstrating SLI snapshot shape; quarterly template populated with synthetic Q-N row demonstrating Part 6a service invocation result shape (TRADEOFF-01 split materialised).
- F-G-R: F4 architecture-time + templates → F5 on first quarterly audit run (Phase B).
- Source: part-8 §H "Wave C bullets: weekly health dashboard template — S effort; quarterly immune audit — M effort; philosophy-expert integrator cited"; part-8 §E Deontics "MUST produce weekly health dashboard for Part 9"; FUNDAMENTAL §2.5 health checkup cadence; SRE consultant card §4 P5 blameless postmortem culture; Part 6a Bundle 1 quarterly framework.

**Bullet P8.4 — Alert-routing stub to Part 6b (Tier 0/1/2/3 mapping).**
- Output: §H.1 alert-routing stub config — mapping table per alert class (per anomaly type from canonical health signal schema) → blast-radius Tier (0/1/2/3 per Part 6b §I.4 F8 LOCKED 4-tier table) → routing target (Part 6b enforcement gate for Tier 0; batch ack queue for Tier 2; auto-log for Tier 3; same-session HITL ack for Tier 1). Halt-Log-Alert ordering enforced for Tier 0 (≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9 F8). Alert packet schema: `anomaly_type`, `severity_tier` (per Tier 0/1/2/3), `affected_part`, `affected_signal`, `recommended_action`, `j_level_authority_required`, `created_at`, `cycle_id`, `f_g_r`.
- Cross-reference: Part 6b §I.4 blast-radius table F8 LOCKED + §I.3 default-deny table F8 LOCKED. Novel alert classes Default-Deny classified (Tier 1+ default; manual classification required to assign Tier 0 or Tier 2/3).
- Stub-level enforcement: this is the routing **specification**, not the routing **implementation**. Live alert delivery infrastructure (Slack / mailbox / email / SMS / page) = Phase B materialisation per OQ-MERGED-5.
- Acceptance predicate: alert-routing stub config exists; ≥10 alert classes mapped (one per major anomaly type — git fsck error / hook bypass / orphan-anchor / stale-claim / mailbox queue overflow / methodology admissibility fail / DRR write rate drop / fg-r compliance drift / gate approval-lag SLI burn / commit-format violation); every class assigned Tier 0/1/2/3 + routing target; Halt-Log-Alert ordering enforced for Tier 0 entries.
- F-G-R: F4 architecture-time → F5 on first Phase B live alert routing.
- Source: part-8 §H "stub alert-routing interface to Part 6 — S effort"; part-6b §E Deontics "MUST surface every gate failure with specific reason"; anthropic-constitutional-ai consultant §5 T3 "fail-loud: anomaly → committed alert record within one monitoring cycle"; Part 6b §I.3 + §I.4 F8 LOCKED.

### §2.3 Cross-cuts within Bundle 3 (re-stated for emphasis)

- **F-G-R DOGFOOD per F8 schema** — every architecture claim in Parts 5 + 8 has F-G-R per Part 6a §I.1 schema.
- **A.14 typed edges** — Bundle 1 canonical 10-edge reference table consulted; NO new edge types invented; NO generic `depends-on`. Bundle 3 specific edge usage examples: Part 5 `creates` Part 3 (compound outputs create methodology library entries — UND-2 binding); Part 5 `methodologically-uses` Part 4 (compound phase draws on coordination cadence); Part 5 `creates` Part 1 (DRR + methodology committed via Part 1 §H); Part 8 `operates-in` `[Part 1, Part 2, Part 3, Part 4, Part 5, Part 6a, Part 6b]` (monitoring is observability context for entire Foundation per VSM S3); Part 8 `methodologically-uses` Part 1 (health snapshots committed via Part 1 §H); Part 8 `methodologically-uses` Part 6a (TRADEOFF-01: invokes Part 6a as F-G-R compliance service); Part 8 `methodologically-uses` Part 6b (TRADEOFF-01: alert routing through enforcement arm); Part 8 `derives-from` Part 1 §J burn-rate (consumes burn-rate algebra without re-derivation).
- **Append-only** — strategies.md / methodology entries / health snapshots / immune-audit reports — all append-only; corrections via NEW entries with `corrects:` pointer per Reversal Transactions discipline (Young 2010).
- **L/A/D/E** — every §E section structured per FPF A.6.B Norm Square.
- **§X Foundation vs RUSLAN-LAYER** — explicit per part:
  - Part 5: 40/10/40/10 ritual structure + DRR schema + methodology promotion pipeline GENERIC. Specific patterns Ruslan promoted (which methodology slugs; which DRR entries) = RUSLAN-LAYER. **Plus dissolve-test condition declaration (per P5.3).**
  - Part 8: SLI/SLO schema framework + 4-tier blast-radius mapping + Beer VSM S3 placement + canonical health signal schema GENERIC. Specific SLI thresholds + alert routing destinations + immune audit checklist contents = RUSLAN-LAYER.
- **PARA-tier mandatory** — Part 5 methodology entries `para_tier: Resource | Archive`; Part 8 health snapshots `para_tier: Area`.
- **TRADEOFF-01 split materialised** — Part 8 audit lead invokes Part 6a service for F-G-R compliance check across wiki entries; Part 6b enforcement arm gates remediation. Beer VSM S3 split clean: Part 8 owns audit cadence + scope; Part 6a owns the F-G-R compliance check primitive; Part 6b owns the gate.

### §2.4 Special: Part 5 ↔ Part 7 (Bundle 4) cross-bundle interface (UND-3)

Part 7 is Bundle 4 work. Bundle 3 Part 5 must specify the **input contract** ("Part 5 expects retrospective input from Part 7 in format X with cadence Y") without finalizing how Part 7 emits. Bundle 4 Part 7 will then conform.

**Brigadier action**: in Part 5 §A Inputs declare Part 7 as upstream source with **stub schema reference** (`task-return-packet.json` superset OR project-retrospective-packet.json TBD); marked Phase 2 (Bundle 4) finalization. Cross-bundle interface artefact created at `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` with required content: (a) Part 5 expectations (what fields Part 5 expects from Part 7 retrospective output); (b) Part 7 emission contract placeholder (Bundle 4 finalises); (c) cadence expectations (per project closure event OR per cycle close — TBD by Part 7); (d) defer rationale (Part 7 is Bundle 4 — joint Design lite avoids premature lock).

Avoid premature lock. Do NOT finalise Part 7's emission contract here.

### §2.5 Special: Part 5 ↔ Part 4 already finalised (UND-1)

Part 4 §I.1 `task-return-packet.json` is F4 (rises to F5 on Bundle 3 Part 5 consumption validation). Bundle 3 Part 5 §B specifies CONSUMPTION pattern: Part 5 reads RAW packets from `comms/mailboxes/` (per Ruslan ack OQ-3), does own DRR extraction (Decision / Reasoning / Result / Review per Compounding-Engineering §2 P2), writes DRR entries to `agents/<id>/strategies.md` via Part 1 §H commit interface.

**No re-litigation of Part 4 schema.** Bundle 2 Decision #4 LOCKED the schema; Bundle 3 consumes verbatim.

---

## §3 Required Reading — MANDATORY before first dispatch

Brigadier MUST read these BEFORE any subagent dispatch. Each pre-read MUST be cited in output. Subagent dispatches MUST instruct experts to read RELEVANT subsets only.

### §3.1 Constitutional baseline (full-read mandatory)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0) — esp. **§2 Compound flows**, **§3 SLI/SLO 30+ pairs** (calibration parameters anchor), **§5 reliability 3-2-1 backup**, **§6 anti-scope** + **§6.1 hard rules** (Default-Deny anchor)
2. `design/JETIX-FPF.md` — IP-3 Artifacts-over-conversations, IP-4 Quarterly Immune Audit, IP-7 Writing-as-thinking (Part 5 owner reflection domain), IP-8 6-step onboarding (M1-M6), A.6.B L/A/D/E, B.3 F-G-R, A.13 Agency-CHR, A.14 typed edges canonical 10-edge table
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (esp. §4 agents/<id>/strategies.md current state — 19 entries; §5 swarm/wiki/meta/health.md compound-application-rate counter; §6 voice pipeline; §8 wiki current state)
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` — esp. **§4.5 deep-study constraint** (UPDATED to 10K-20K per Bundle 2 ack §3 F8 constitutional refinement)
5. **Bundle 1 LOCKED Foundation outputs (CONSTITUTIONAL FOR BUNDLE 3 — post retroactive supplement):**
   - `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (esp. §B Four Golden Signals — Part 8 input source; §J burn-rate table 1×/6×/14.4× — Part 8 inherits; §I.4 task-return-packet stub AFTER retroactive supplement; §K K15 upcasting AFTER retroactive supplement; §H commit interface — Part 5 + Part 8 callers)
   - `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (esp. §I.1 F-G-R schema F8 — DOGFOOD; §C approval log structure; quarterly immune audit framework — Part 8 invokes as service per TRADEOFF-01)
   - `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (esp. §I.1 awaiting-approval-packet F8 with `gate_class` enum; §I.3 default-deny table F8; §I.4 blast-radius 4-tier F8 — Part 8 alert routing maps to tiers; §E Laws L1-L10 esp. **L9 Halt-Log-Alert + Corrigibility F8**)
6. **Bundle 2 LOCKED Foundation outputs (CONSTITUTIONAL FOR BUNDLE 3):**
   - `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` (esp. §B Outputs Part 8 health signals; §I.1 STOP gate packet emission)
   - `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` (esp. **§E L9 methodology promotion admissibility predicate F5 — Part 5 P5.2 BINDING**; §I.2 `wiki/methodology/` entity-type F5 + promotion sequence — DRY cross-ref from Part 5 §I.1; §I.6 health signal schema for Part 8 consumption)
   - `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (esp. **§I.1 task-return-packet.json FULL schema F4 — UND-1 / Part 5 P5.1 + P5.2 BINDING**; §H message schema v2.0.0; §I.4 health signal schema for Part 8 consumption)
7. **Ack records (MANDATORY READ):**
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (esp. §3 F-promotions table; §4 Constitutional consequences; §6 hard rules + Default-Deny constitutional anchor)
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` (esp. **§3 WORD COUNT TARGET UPDATE 10K-20K F8 constitutional**; §1 Decisions #1-#7; §2 OQ-B2-A through OQ-B2-F status; §6 next action — OQ-B2-A retroactive Bundle 1 fix as Bundle 3 first task)
8. Locks D1-D29 + 4 LOCKS-ADDENDUM (focus **D17 FPF anchor**, **D25 Company-as-Code** (Part 5 + Part 8 commits), **D26 hub-and-spoke**, **D29 Korp-Startup**, most recent `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`)

### §3.2 Wave A artefacts (full-read mandatory)

1. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`
2. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md` (esp. §2 Part 5; §2 Part 8)
3. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` (esp. §2.4 P4↔P5 R2 reinforcing loop; §3.2 C2 health signal schema; §3.4 C4 nomenclature; §4.3 UND-3 P7→P5 cadence; §6.4 routing structural change risk; §7 OQ-1 TRADEOFF-01 BLOCKING acked)
4. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` (esp. **§2 Part 5** lines 249-296, **§2 Part 8** lines 404-460, §3 Bundle composition, §4 cross-bundle dependencies, §6 OQs)
5. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md` (esp. §2 Part 5 verdict CLEAN + §4 OQ-MERGED-2; §2 Part 8 verdict CLEAN + TRADEOFF-01 surfaced)
6. **Wave A interface cards for Bundle 3 parts:**
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md` (123 lines — Part 5 §A-§H baseline + frontmatter dissent record)
   - `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-8-health-monitoring-system-integrity.md` (138 lines — Part 8 §A-§H baseline + TRADEOFF-01 Open Q + Wave C bullets preview)
7. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/` (5 files: engineering / investor / mgmt / philosophy / systems)

### §3.3 Wave B consultant cards (per Manifest §2 matrix)

**For Part 5 dispatches** (engineering + philosophy + investor + mgmt + systems):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/compounding-engineering.md` — **PRIMARY** — §2 main loop 40/10/40/10 + §4 P1 per-cycle Compound + §4 P2 DRR ledger + §4 P3 Error→Rule→Skill pipeline + §4 P4 strategies.md persistent memory + §4 P5 methodology library promotion + §4 P6 anti-cargo-cult + §4 P7 reversibility via git
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-7 writing-as-thinking (owner reflection domain — Ruslan-authored; agents contribute structured extractions); IP-3 artifacts-over-conversations (DRR MUST be committed files, not chat-only)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/product-management-cagan-shape-up.md` — OKR cadence; Ries build-measure-learn at system level; Singer 2019 Shape Up appetite for compound phase
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md` — Popper falsifiability as rule-promotion gate (DRR `result: validated` requires R `refuted_if:` predicate)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` — **R1 vs R2 reinforcing loop distinction** (Part 5 = R2 — knowledge compound across cycles, 5-10 cycle delay before compound effect detectable; counter-argument to engineering-expert dissolve dissent)

**For Part 8 dispatches** (engineering + systems + investor + philosophy + mgmt):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md` — **PRIMARY** — §4 P1 SLI/SLO/error-budget triad; §4 P2 observability vs monitoring (unknown unknowns); §4 P4 toil reduction; §4 P5 blameless postmortem; §4 P6 fail-loud; §4 P7 error-budget-burn behaviour-change
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md` — Beer VSM S3 audit function (TRADEOFF-01 split); Ashby requisite variety for monitor (≥30 SLI/SLO pairs to match FUNDAMENTAL §3 failure-mode count); Meadows L7 information-flows leverage point
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md` — Marks second-level thinking (moat = drift discipline); antifragile via stressors (Part 8 detects stressors — health-snapshot evidence is moat asset)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-4 quarterly immune-system audit cadence (Part 8 quarterly audit binding)
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` — integrity violations = absolute halt (Tier 0 routing); softcoded degradation for velocity SLIs (graceful degrade for non-Tier-0 burns); §5 T3 fail-loud anomaly→committed alert record within one monitoring cycle

### §3.4 Wave B Supplement library-direct sources (Bundle 3 critical)

1. **`raw/books-md/sre/google-sre-book.md`** — Ch.4 Service Level Objectives (full read for Part 8 §I.2); Ch.6 Monitoring Distributed Systems (P8.3 templates); Ch.15 Postmortem Culture: Learning from Failure (Part 5 + Part 8 P5 blameless postmortem); Ch.22 Addressing Cascading Failures (Part 8 alert routing K-failure-modes)
2. **`raw/books-md/sre/google-srewb-implementing-slos.md`** — Ch.2 Implementing SLOs (burn-rate algebra 1×/6×/14.4× — already adopted Part 1 §J Bundle 1; Part 8 §I.2 inherits)
3. `raw/books-md/event-sourcing/young-cqrs-2010.md` — Reversal Transactions for compound history (no-delete; corrections = new entries with `corrects:` pointer)
4. `raw/books-md/anthropic/bai-2022-cai.md` — RLAIF self-critique pattern (Part 8 audit signal generation analog — health snapshots as self-critique artefacts)
5. `raw/books-md/anthropic/askell-2021-hhh.md` — Corrigibility Appendix E.2 verbatim (Part 8 NEVER locks owner out — already F8 LOCKED Bundle 1 Part 6b)

### §3.5 Existing operational artefacts (audit reference, do not duplicate)

- `agents/<id>/strategies.md` files (8 of them — current strategy entries, R2 loop input baseline) — Bundle 3 Part 5 EXTENDS schema, does NOT regenerate content
- `swarm/wiki/meta/health.md` (current informal health doc — Part 8 will canonicalise via §I.1 + §I.2 schemas)
- `swarm/wiki/meta/agent-improvements/` (existing pattern improvements queue — feeds Part 5 methodology candidate detection)
- `swarm/evals/` (3/20 cells seeded — eval system stub — feeds Part 8 health signals at Phase B)
- `shared/state/system-health.json` (currently "all green" hardcoded — Part 8 §I.1 specifies real computation contract; live computation Phase B)
- `shared/state/metrics/agent-performance.json` + `task-log.jsonl` (current metrics — Part 8 mapping table §I.3 maps to canonical schema)

---

## §4 Phase Architecture (matrix dispatch + Joint Design lite + Wisdom Loop + critic gate)

Standard ROY cycle = **integrator → critic → finalize**. **For Bundle 3, brigadier MUST insert THREE structural phases beyond Bundle 1 + Bundle 2 patterns: a retroactive supplement phase BEFORE substantive dispatch (§4.1), a Joint Design lite phase for C2 + UND-3 (§4.3), and the Wisdom Application Loop with OPERATIONAL/PHILOSOPHICAL discriminator + ≥85% target (§5).**

### §4.0 Phase ZERO — OQ-B2-A retroactive Bundle 1 supplement (BLOCKING)

**Trigger**: brigadier dispatch start.

**Procedure**:
1. Read `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` §6 Next action.
2. Edit `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md`:
   - §I.4 task-return-packet stub `gate_class` enum: `["autonomous", "requires-approval", "hitl-required"]` → `["stop_gate", "stage_gate", "draft_promotion"]` (Part 6b §I.4 F8 LOCKED). Update inline comment + §G F-G-R tag if affected.
   - §I.2 commit-format-tokens.json: add `swarm-lib` to allowed area tokens. Update inline comment + cross-ref Bundle 2 C1 Joint Design canonical answer.
   - §K Failure Modes: add **K15 — Legacy v1.0.0 message upcasting** entry. Detection: `schema_version` field = "1.0.0" on ingest. Policy: detect `acting_as:` field; if missing, attempt upcast (inject from `from:` field per role-archetype mapping); if upcast cannot be inferred, REJECT with named-field error. Cross-ref Bundle 2 message schema v2.0.0 (P4.1) Decision #6.
3. Append retroactive correction note to `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (or create supplement file `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md`):
   ```
   ## §6.1 Retroactive corrections per OQ-B2-A (applied 2026-04-28 at Bundle 3 cycle start)
   - Part 1 §I.4 stub gate_class enum aligned to Part 6b §I.4 F8 LOCKED [stop_gate, stage_gate, draft_promotion]
   - Part 1 §I.2 commit-format-tokens.json [swarm-lib] token added per OQ-B2-D
   - Part 1 §K K15 upcasting failure mode added per Bundle 2 message schema v2.0.0 BREAKING change
   - Commit hash: <new>
   ```
4. Single commit:
   ```
   [architecture] Bundle 1 retroactive supplement — Part 1 §I.4 gate_class enum + commit-format-tokens.json [swarm-lib] token + K15 upcasting (per OQ-B2-A + OQ-B2-D RUSLAN-ACK Bundle 2)
   ```
5. Push to `claude/jolly-margulis-915d34`.

**Acceptance gate**: commit lands; push succeeds; `git diff` shows the three edits + the ack-record append. **THEN** Bundle 3 substantive dispatch begins. NO substantive Part 5 / Part 8 cell dispatch BEFORE this commit lands.

### §4.1 Phase sequence per part (sequential by default)

For each Part (5, 8) execute in this order. Note: Parts 5 + 8 share a Joint Design lite phase (§4.3) for C2 health signal schema canonicalisation + UND-3 Part 5↔Part 7 stub.

1. **Phase A — Pre-read confirmation** — brigadier reads §3 mandatory; dispatch instructs each expert to read RELEVANT subset only (per §3.3 mapping).
2. **Phase B — Matrix dispatch (5 experts × 4 modes = up to 20 cells)** — per ROY-ALIGNMENT §3 row mapping. Not every cell fires; brigadier picks cells that genuinely add signal. Minimum 8 cells per part.
3. **Phase C — Integrator** — brigadier (or delegated integrator-mode expert) merges cell outputs into draft architecture per §6 quality bar.
4. **Phase C+ — Joint Design lite Phase (Parts 5 + 8 — C2 + UND-3)** — see §4.3. Resolves canonical health signal schema (C2) + Part 5↔Part 7 stub interface (UND-3); produces single coherent answer documented in mapping table + UND-3 stub artefact.
5. **Phase D — Wisdom Application Loop** — see §5. **Bundle 3 refinement: ≥85% operational target (stricter than Bundle 2's ≥60%) — given Part 5 + Part 8 are inherently operational domains.**
6. **Phase E — Critic gate** — ≥2 experts in critic-mode review draft + Joint-Design + Wisdom edits. Stricter cargo-cult check + dissolve-test condition declaration check (Part 5 §X) + scope-creep check (Part 8 "specify and stub" not "live impl") + TRADEOFF-01 split materialisation check (Part 8 invokes Part 6a service; Part 6b enforcement arm visible in §H or §I).
7. **Phase F — Finalize** — brigadier promotes draft → canonical at `swarm/wiki/foundations/<part-slug>/architecture.md`.
8. **Phase G — M-gates per part** — M1 smoke, M2 cross-ref. (M3 + M4 + M5 run at bundle level in §7.)

### §4.2 Cell selection guidance per part

**Part 5** (Compound Learning): engineering (critic — DRR schema integrity + Error→Rule→Skill pipeline + scalability — strategies.md scaling; clean-code — atomic DRR entries; integrator), philosophy (epistemic audit on R `refuted_if:` Popper-falsifiability for DRR validated marker; first-principles on dissolve-test condition declaration; critic on dissent preservation discipline), investor (capital-allocation — methodology library as compound asset, Marks moat = drift discipline; long-term-compounding — DRR ledger as F4→F5 codification with cross-cycle reuse evidence), systems (cybernetics — R2 reinforcing loop counter-argument to dissolve dissent; emergence — methodology promotion as adjacent-possible per Kauffman), mgmt (boundary on Part 5 vs Part 3 promotion ownership — Part 5 owns EMISSION; Part 3 owns ADMISSION; integrator on cadence enforcement). **Minimum 9 cells** (P5.3 dissolve-test declaration is heaviest — preserves engineering-expert dissent + integrator counter-argument from systems-expert).

**Part 8** (Health Monitoring): engineering (critic — schema integrity, scalability — 30+ SLI/SLO Phase B feasibility, integrator — alert routing stub, scalability — alert delivery infrastructure deferred), systems (cybernetics — Beer VSM S3 split; Ashby requisite variety check ≥30 SLI/SLO pairs match failure-mode variety; emergence — adjacent-possible Part 8 audit drives next cycle improvement; integrator on TRADEOFF-01 split materialisation), investor (capital-allocation — health-snapshot evidence as moat asset; antifragility — Part 8 detects stressors before catastrophic; long-term-compounding — quarterly immune audit as F-G-R drift sink), philosophy (epistemic audit on starter-value-label calibration discipline — OQ-MERGED-5 scope-creep prevention; first-principles on canonical health signal schema canonicalisation — C2 resolution choice; critic on Corrigibility — Part 8 NEVER locks owner out), mgmt (boundary — Part 8 vs Part 6 enforcement split; ethics-surface — health snapshot creates surveillance footprint; integrator — quarterly audit template). **Minimum 10 cells** (heaviest: TRADEOFF-01 split + scope-creep autocheck + canonical schema canonicalisation + ≥85% operational target).

### §4.3 Joint Design lite Phase (C2 health signal schema + UND-3 Part 5↔Part 7 stub)

**Trigger**: After Phase C integrator drafts for Part 5 AND Part 8 are produced (both sequentially or in parallel within HD-02 N=2).

**Procedure**:

1. Brigadier convenes a **C2 + UND-3 resolution session** dispatching engineering-expert (integrator-mode) + systems-expert (critic-mode VSM S3 + Ashby variety lens) + philosophy-expert (boundary-clarity lens) jointly on TWO questions:

   **Question 1 (C2 — health signal schema canonicalisation):** "Bundle 1 + 2 emitters declared health signal stubs (Part 1 §I.5; Part 3 §I.6; Part 4 §I.4 — currently heterogeneous). Part 8 §I.1 owns canonical health signal schema. Choice: (A) retroactively align Bundle 1 + 2 emitter shapes to Part 8 canonical schema (preferred — DRY); OR (B) Part 8 §I.1 explicitly accepts current heterogeneous shapes with a mapping table (fallback if retroactive alignment exceeds 1h budget). Pick one with rationale."

   **Question 2 (UND-3 — Part 5↔Part 7 stub):** "Part 7 is Bundle 4 work. Part 5 §A Inputs declares Part 7 as upstream retrospective source. What is the stub schema reference (task-return-packet.json superset OR project-retrospective-packet.json TBD) and how is the cadence expectation declared without premature lock?"

2. The session reads Part 5 §I draft + Part 8 §I draft + Part 1 §I.5 + Part 3 §I.6 + Part 4 §I.4 + the C2 contradiction record (dependency-graph §3.2) + the UND-3 stub guidance (§2.4 above).

3. Output 1: Part 8 §I.3 mapping table — canonical health signal schema fields mapped to Bundle 1 + 2 emitter shapes. Each Foundation part's emitter shape projected onto canonical schema. If Variant A (retroactive align) chosen: brigadier issues retroactive supplement edits to Bundle 1 + 2 architectures (mirroring §4.0 retroactive supplement pattern; single commit at end of Joint Design Phase). If Variant B (mapping table) chosen: Part 8 §I.1 explicitly accepts heterogeneous shapes with mapping in §I.3.

4. Output 2: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` — single coherent stub artefact. Required sections:
   - **Part 5 input expectations**: what fields Part 5 expects from Part 7 retrospective output (e.g., `project_id`, `state_transition`, `appetite_actual_vs_planned`, `lessons_learned[]`, `dr_r_candidates[]`).
   - **Part 7 emission contract placeholder**: Bundle 4 Part 7 finalises; Bundle 3 Part 5 specifies expectations only.
   - **Cadence expectations**: per project closure event OR per cycle close — TBD by Part 7.
   - **Defer rationale**: Part 7 is Bundle 4; Joint Design lite avoids premature lock; Part 7 conforms to Part 5's input contract in Bundle 4.
   - **Cross-references**: Part 5 §A Inputs + §I + future Bundle 4 Part 7 §B Outputs.

5. Both Part 5 §A + §I and Part 8 §I sections REFERENCE these documents (DRY enforcement — single canonical answer; cross-references not duplications).

6. If Joint Design lite produces conflicting answers (e.g., Variant A retroactive align vs Variant B mapping table — and disagreement persists): **escalate to brigadier-mode arbitration**; if answer materially differs from "Variant A retroactive align preferred OR Variant B fallback" → Ruslan ack required (write `swarm/wiki/foundations/<part-slug>/oq-bundle-3-N.md` and HALT for HITL).

**Why this matters**: C2 is a Bundle 1 carry-over contradiction. UND-3 is a cross-bundle interface. Sequential design produces incoherent answers; Joint Design lite forces coherence at design-time, not at integration-time when re-architecture is expensive.

**This is "Joint Design lite" (not full like Bundle 2's C1)**: scope is narrower (schema canonicalisation + stub interface), so the session is shorter (~1 hour vs Bundle 2's 2 hours).

### §4.4 Dissent preservation (AP-6)

If any expert in critic-mode produces dissent that integrator could not resolve: preserve in `swarm/wiki/foundations/<part-slug>/dissent.md`. Do NOT silently override expert domain judgment (E-15).

**Special for Part 5**: engineering-expert dissent on dissolve-test (originally preserved in Wave A interface card §H frontmatter) MUST be re-cited in Part 5 §X declaration. This is NOT new dissent — it is the canonical preserved Wave A dissent now formalised in Foundation architecture.

---

## §5 THE WISDOM APPLICATION LOOP (Phase D — central directive)

**This phase is constitutional. Skipping it is a violation.**

After integrator produces draft architecture for Part X (and after Joint Design lite Phase completes for Parts 5 + 8 C2 + UND-3), brigadier dispatches a dedicated **Wisdom Loop pass**.

### §5.1 Procedure (UNCHANGED from Bundle 1 + Bundle 2 — preserve discipline)

For each consultant card relevant to this part (per §3.3 mapping) AND each library-direct supplement source (§3.4):

Ask FIVE questions, in order, in writing, with traceable answers:

1. **Question 1 — Application Gap**: "What does this consultant card say that the current draft DOES NOT yet apply, but would benefit from?"
2. **Question 2 — Cargo-Cult Audit**: "Are there principles from this card we cited but did not actually apply (cargo-cult risk per Manifest §5)?"
3. **Question 3 — Concrete Improvement**: "Is there a concrete improvement to the architecture if we apply principle X from this card?"
4. **Question 4 — Section Impact**: "If we DO apply this improvement — what changes in §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary / §F Anti-scope / §H Code interfaces / §I Data schemas?"
5. **Question 5 — Phase A Justification**: "Is the application JUSTIFIED for current Phase A scope (single-owner, Phase 1 €50K horizon)? Or is it premature optimization for Phase B/C/D scale?"

### §5.2 Bundle 3 refinement — OPERATIONAL/PHILOSOPHICAL ≥85% target (stricter than Bundle 2)

Bundle 2 demonstrated 89% operational adoption ratio across 3 architecture documents averaging 10.2K words each. Bundle 3 inherits and TIGHTENS the floor:

- **Bundle 1 (50/50 mix)**: too much philosophical text — accepted for that bundle's constitutional substrate work.
- **Bundle 2 (≥60% target, achieved 89%)**: explicit operational bias per Ruslan feedback.
- **Bundle 3 (≥85% target)**: Compound Learning + Health Monitoring are inherently operational. If aggregate drops below 85%, that is a red flag — investigate; brigadier may be reverting to philosophical content despite the Bundle 2 lesson.

**For Bundle 3, apply the following bias:**

- **PRIORITIZE operational adoptions** — adoptions that change schema fields, add new failure modes, define new SLO targets, add new lint checks, change algorithm, add new edge type, modify code-level interface, OR add new admissibility rule.
- **MINIMIZE philosophical/marketing text** — adoptions that add only "framing prose" (e.g., "this is Beer-clean S3 placement", "Lindy verdict") without operational consequence.
- **REJECT** any adoption whose "concrete consequence sentence" is purely about how the document reads.

**Wisdom Findings table format (UNCHANGED from Bundle 2 — Operational/Philosophical column mandatory):**

```markdown
### Wisdom Application Findings — Part X

| Card / Source | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification | Section edited |
|---------------|-----------|---------------|-------------|----------|------------------------------|---------------|----------------|
| #1 Compounding-Engineering | DRR ledger as append-only compound memory | partial in §B | Add `ratio: {hits, misses}` counter to DRR schema + tombstone rule when ratio.misses > ratio.hits×2 | YES | OPERATIONAL | Phase A — operational decay signal | §I.1 + §K |
| #2 SRE Workbook Ch.2 | Burn-rate algebra 1×/6×/14.4× | Part 1 §J already adopted | Part 8 §I.2 inherits from Part 1 §J — no re-derivation | n/a (already applied) | OPERATIONAL | Already in §I.2 inheritance | n/a |
| #3 Stoic Dichotomy | "in our control" framing | not applied | Add §F.3 framing prose | NO | PHILOSOPHICAL | No scope-creep risk; no Phase B/C concrete need; pure framing prose; DEFER to Wave D documentation pass | n/a |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

**Aggregate target:**
> Bundle 3 should have YES Adopted ratio of Operational ≥85% (Bundle 2 demonstrated 89% achievable).

If Operational ratio < 85% across Parts 5 + 8: investigate. Is brigadier reverting to philosophical text? Apply refinement bias more strictly. Re-dispatch integrator to convert PHILOSOPHICAL adoptions into OPERATIONAL ones (e.g., a Stoic Dichotomy adoption that was prose becomes a §F Anti-scope rule with a `/lint` check).

### §5.3 Discipline (HARD RULES — preserved from Bundle 1 + 2)

**Brigadier MUST**:
- Run Wisdom Loop AFTER integrator (and after Joint Design lite for Parts 5 + 8), BEFORE critic gate
- Produce findings table (§M) per part with Operational/Philosophical column
- Apply every "YES Adopted" edit to draft BEFORE critic gate runs
- Critic gate then verifies: did Wisdom edits hold? Anti-cargo-cult check stricter than usual.
- For each YES Adopted entry, the edit MUST be visible in §A-§L diff (not just claimed in table).
- For each NO entry, the justification MUST be one of the legitimate categories: `Phase B work` / `Phase C+ scale` / `premature optimization` / `requires RUSLAN-LAYER decision Ruslan hasn't made` / `domain-orthogonal to this part` / `pure framing prose without operational consequence` (Bundle 2 PHILOSOPHICAL deferral category).

**Brigadier MUST NOT**:
- Skip Wisdom Loop because "draft seems fine"
- Reject improvement opportunities without explicit justification from the legitimate categories
- Adopt every improvement without Phase A justification (Phase B+ ideas DEFER)
- Treat the loop as paperwork — every YES is a real edit, every NO is a real reasoned defer
- Adopt PHILOSOPHICAL improvements without scope-creep-prevention or Phase B/C concrete-need justification
- Accept aggregate operational ratio < 85% silently — investigate, re-dispatch, OR escalate

### §5.4 Failure mode (UNCHANGED from Bundle 1 + 2)

If Wisdom Application Loop produces 0 "YES Adopted" across all relevant cards for a part: HALT, write `swarm/wiki/foundations/<part-slug>/wisdom-loop-zero-adoption-flag.md` with reasoning, escalate to Ruslan via tmux output before proceeding to critic gate.

DO NOT fabricate YES entries to satisfy the loop. False positives in Wisdom Loop are worse than zero adoption — they corrupt the audit trail.

### §5.5 Why this matters (re-emphasize)

This loop prevents:
- Cargo-cult citation (citing without applying)
- Knowledge sitting unused in `raw/books-md/` despite Wave B Supplement processing
- ROY producing "good enough" architecture that ignores hard-won wisdom from 14 consultant cards + 5 library-direct sources
- Bundle 3 reverting to philosophical text after Bundle 2's explicit operational bias

---

## §6 Quality bar (per Bundle 2 ack §3 F8 constitutional refinement)

### §6.1 Document size: 10K-20K per Part (NEW constitutional)

Each Part architecture document MUST be **10K-20K words** (~100K-200KB markdown). Bias toward operational content density. Operational adoption ratio target ≥85%.

If draft comes in under 10K words: brigadier returns to integrator with explicit feedback "you delivered N words; quality bar is 10K-20K — re-dispatch with §A-§N expansion mandate focusing on OPERATIONAL deltas (schema fields / failure modes / SLO targets / lint checks / algorithms / edge types / code-level interfaces / admissibility rules) NOT philosophical framing prose."

If draft comes in over 20K words: review for redundancy + cargo-cult padding. Tighten before Wisdom Loop. Pure framing prose without operational consequence is the failure mode.

### §6.2 Section structure (every part doc has §A through §N + §X)

Same structure as Bundle 1 + 2. Sections: §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary L/A/D/E / §F Anti-scope / §G F-G-R Tagging / §H Code-level interfaces / §I Data schemas / §J Operational rituals / §K Failure modes / §L Wave C work-list bullet status / §M Wisdom Application Findings / §N Provenance / §X Foundation vs RUSLAN-LAYER.

Bundle 3 specifics:
- §I Data schemas: Part 5 §I.1 declares methodology promotion pipeline schema (UND-2 binding); Part 8 §I.1 declares canonical health signal schema (C2 resolution); Part 8 §I.2 declares SLI/SLO schema; Part 8 §I.3 declares mapping table for Bundle 1+2 emitters.
- §H Code interfaces: Part 5 §H references Part 1 §H commit interface (DRR + methodology committed via Part 1) and Part 4 §I.1 task-return-packet schema (UND-1 consumption); Part 8 §H references Part 1 §H + Part 6a quarterly immune audit framework (TRADEOFF-01 service invocation) + Part 6b §I.4 blast-radius (alert routing).
- §X Foundation vs RUSLAN-LAYER: per part — see §2.3 above for explicit declarations. **Part 5 §X MUST declare OQ-MERGED-2 dissolve-test condition (Bullet P5.3).** **Part 8 §X MUST declare "specify and stub" scope discipline + FUNDAMENTAL §3 starter values labeled calibration-grade (OQ-MERGED-5 scope-creep prevention).**

### §6.3 Anti-cargo-cult enforcement (CRITICAL — same as Bundle 1 + 2)

Per Bundle 1 Part 6a §C citation discipline:
- Every `[src:...]` citation MUST be followed within 200 chars by a concrete consequence sentence. Example: "...therefore Part 5 §I.1 declares: 'methodology candidate emitted only after ≥1 DRR result: validated marker from ≥2 distinct cycles' [src:swarm/wiki/cycles/.../wave-b/consultants/compounding-engineering.md:§5 validated pattern threshold]". The consequence sentence is the operational change driven by the source.
- `/lint --check-citations` (Bundle 1 P6a.2 — specified, Phase B implementation per OQ-B1-2) is the canonical enforcer; until it ships, manual discipline + critic gate.
- Critic gate MUST reject any §A-§N section with cargo-cult violations and return to integrator with line-number-specific feedback.

### §6.4 Typed A.14 edges everywhere (HARD RULE — Bundle 1 canonical 10-edge table)

Every §D Dependencies entry MUST be one of the canonical edge types per Bundle 1 Part 1 §D 10-edge reference table:

`ComponentOf` / `ConstituentOf` / `PortionOf` / `PhaseOf` / `MemberOf` / `AspectOf` / `creates` / `operates-in` / `methodologically-uses` / `constrained-by` / `derives-from`

**NO `depends-on`. NO `uses` generic. Critic gate auto-rejects.**

Bundle 3 specific edge usage (per §2.3 above):
- Part 5 `creates` Part 3 (UND-2 — methodology library entries)
- Part 5 `creates` Part 1 (DRR + methodology committed)
- Part 5 `methodologically-uses` Part 4 (compound phase draws on coordination cadence per §I.1 task-return-packet schema)
- Part 8 `operates-in` `[Parts 1-7]` (Beer VSM S3 audit context spans entire Foundation)
- Part 8 `methodologically-uses` Part 1 (health snapshots committed)
- Part 8 `methodologically-uses` Part 6a (TRADEOFF-01 — invokes F-G-R compliance service)
- Part 8 `methodologically-uses` Part 6b (TRADEOFF-01 — alert routing through enforcement arm)
- Part 8 `derives-from` Part 1 §J (consumes burn-rate algebra without re-derivation)

### §6.5 F-G-R on every promoted claim (DOGFOOD — same as Bundle 1 + 2)

Every architecture claim MUST have F-G-R tag per Bundle 1 Part 6a §I.1 F8 schema. Inline: `[F4|G:holds-within-Foundation-scope|R-medium]` OR table entry in §G.

Use Bundle 1 OQ-B1-1 anchor wording:
- F4 = "≥3 cycles applied"
- F6 = "cross-cycle reuse evidence"
- F8 = "FUNDAMENTAL Vision lock-class"

### §6.6 Provenance trail (same as Bundle 1 + 2)

Every claim → `[src:path]` inline citation → resolves to existing file + section. M2 cross-reference gate (§7.2) verifies 100% citation resolution. No broken citations allowed.

### §6.7 Foundation vs RUSLAN-LAYER fork-separation discipline (per OQ-MERGED-3)

Each Part architecture MUST have explicit **§X Foundation vs RUSLAN-LAYER fork-separation** section. See §2.3 above for Bundle 3 explicit declarations.

**Bundle 3 NEW §X requirements:**

- **Part 5 §X MUST contain OQ-MERGED-2 dissolve-test condition declaration** (Bullet P5.3 binding) — verbatim test condition + engineering-expert dissent preserved + 3-cycle window threshold.
- **Part 8 §X MUST contain "specify and stub" scope discipline declaration** — verbatim acknowledgment that Bundle 3 Part 8 = schemas + templates + stub routing; FUNDAMENTAL §3 30+ SLI/SLO pairs labeled calibration-grade with explicit calibration-cadence; live metrics implementation = Phase B materialisation.

### §6.8 Special: Part 8 "specify and stub" scope-creep autocheck

Per OQ-MERGED-5 ack: Part 8 Wave C output = SLI/SLO schema + canonical health signal schema + template authoring + alert-routing stub. NOT live metrics implementation. NOT calibrated thresholds.

**Brigadier autocheck procedure (run before §F finalize for Part 8):**

1. Verify §I.2 SLI/SLO schema entries every starter value labeled `starter_value_label: "calibration-grade"`. Any unlabeled starter value = violation.
2. Verify §J Operational Rituals does NOT specify live metric collection cadence below daily granularity (calibration cadence is monthly review per OQ-MERGED-5).
3. Verify §K Failure Modes contains "K-PartB — over-implementation drift" entry as self-monitored failure mode.
4. Verify §X explicit acknowledgment of "specify and stub" scope.
5. Verify alert-routing §H is a STUB (specification of routing rules + alert packet schema), NOT an implementation (no Slack/email/SMS delivery code; Phase B materialisation declared).

If any check fails: brigadier returns to integrator with explicit feedback "Part 8 produced live implementation spec — that's scope creep per OQ-MERGED-5. Re-dispatch with stub-level mandate: schemas + templates + routing rules; NOT delivery code; NOT calibrated thresholds; FUNDAMENTAL §3 starter values labeled calibration-grade."

### §6.9 Special: Part 5 standalone preservation autocheck

Per OQ-MERGED-2 ack: Part 5 standalone preserved (dissolve-test active). Bundle 3 = first cycle of dissolve-test window.

**Brigadier autocheck procedure (run before §F finalize for Part 5):**

1. Verify §X contains DISSOLVE-TEST CONDITION verbatim with ≥3 distinct compound-phase-exclusive operations threshold.
2. Verify §X cross-references engineering-expert dissent (Wave A interface card §H frontmatter dissent record) + systems-thinking-cybernetics consultant card §4 R2 reinforcing loop counter-argument.
3. Verify companion artefact `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` exists with mirror declaration.
4. Verify Bundle 3 = FIRST CYCLE OF 3-CYCLE WINDOW declaration.
5. Verify dissolve path declared (Wave D ack packet redirects compound-phase ownership if threshold not met).

If any check fails: brigadier returns to integrator with explicit feedback "Part 5 §X dissolve-test condition under-declared per OQ-MERGED-2 Bullet P5.3. Re-dispatch with §X expansion: verbatim condition + engineering-expert dissent preserved + 3-cycle window threshold + dissolve path declared."

---

## §7 Verification Gates (M1 / M2 / M3 / M4)

### §7.1 M1 Smoke Test (per part, threshold ≥90%)

Same checklist as Bundle 1 + 2:
- [ ] All §A-§N + §X sections populated (no "TBD" placeholders)
- [ ] Word count ≥10K (NEW Bundle 3 floor per Bundle 2 ack §3)
- [ ] Word count ≤20K (NEW Bundle 3 ceiling per Bundle 2 ack §3)
- [ ] Dependencies (§D) all typed per §6.4
- [ ] F-G-R tags (§G) present on every promoted claim
- [ ] Wave C bullets from §2 all mapped in §L with acceptance predicate ✅/❌
- [ ] §X Fork-separation section explicit
- [ ] No cargo-cult signals (citation without consequence sentence within 200 chars)

Bundle 3 additional checks per part:
- [ ] **(Part 5)** §X contains OQ-MERGED-2 dissolve-test condition declaration with verbatim threshold
- [ ] **(Part 5)** §X cross-references engineering-expert dissent (Wave A interface card §H) + systems-thinking-cybernetics consultant card §4 R2 counter-argument
- [ ] **(Part 5)** Companion artefact `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` exists
- [ ] **(Part 5)** §I.1 methodology promotion pipeline schema declares full UND-2 binding (admissibility + emission + promotion event format)
- [ ] **(Part 5)** §A Inputs declares Part 4 §I.1 task-return-packet as upstream FROZEN contract (UND-1)
- [ ] **(Part 5)** §A Inputs declares Part 7 (Bundle 4) as Phase 2 finalization upstream — stub reference (UND-3)
- [ ] **(Part 5)** UND-3 stub artefact `swarm/wiki/cycles/.../bundle-3/UND-3-stub.md` exists
- [ ] **(Part 8)** §I.1 declares canonical health signal schema (C2 resolution)
- [ ] **(Part 8)** §I.2 declares SLI/SLO schema with ≥8 starter SLI entries; every starter value labeled `starter_value_label: "calibration-grade"`
- [ ] **(Part 8)** §I.3 mapping table maps Bundle 1+2 emitter shapes (Parts 1, 2, 3, 4) to canonical schema
- [ ] **(Part 8)** §H.1 alert-routing stub maps ≥10 alert classes to Tier 0/1/2/3 + Halt-Log-Alert ordering
- [ ] **(Part 8)** §J quarterly immune audit ritual references Part 6a service invocation (TRADEOFF-01 split materialised)
- [ ] **(Part 8)** §K Failure Modes contains "K-PartB — over-implementation drift" self-monitored failure mode
- [ ] **(Part 8)** §X explicit "specify and stub" scope declaration
- [ ] **(Part 8)** Templates exist at `swarm/audits/weekly-health-template.md` + `swarm/audits/quarterly-immune-audit-template.md`
- [ ] **(Both)** Operational adoption ratio per part ≥85% in §M Wisdom Findings

Pass threshold: ≥90% bullets ticked. Per part. Failure: re-dispatch integrator.

### §7.2 M2 Cross-reference (per part, threshold 100%)

Same as Bundle 1 + 2:
- [ ] Every `[src:...]` resolves to an existing file
- [ ] Every cited section anchor resolves to an actual section heading
- [ ] No broken inline citations
- [ ] No dangling typed-edge targets in §D

Bundle 3 additional:
- [ ] Part 5 §I.1 references Part 3 §E L9 + §I.2 promotion sequence (DRY enforced; resolves)
- [ ] Part 5 §A Inputs references Part 4 §I.1 (UND-1) + UND-3 stub artefact (resolves)
- [ ] Part 8 §I.1 references Part 1 §J burn-rate (inheritance; resolves)
- [ ] Part 8 §I.3 mapping references Part 1 §I.5 + Part 3 §I.6 + Part 4 §I.4 (post-supplement; resolves)
- [ ] Part 8 §J quarterly audit references Part 6a §I.1 F-G-R compliance check primitive (TRADEOFF-01; resolves)
- [ ] Part 8 §H alert routing references Part 6b §I.4 blast-radius F8 LOCKED (resolves)
- [ ] Bundle 1 retroactive supplement edits (Part 1 §I.4, §I.2, §K K15) referenced from Bundle 3 documents (resolves)

Pass threshold: 100%. Failure: integrator fixes citations OR escalates if cited file missing.

### §7.3 M3 Scenario Walkthroughs (bundle-level, 4 scenarios MUST pass)

Run each scenario end-to-end against Bundle 3 + Bundle 1 + 2 interfaces. Document trace in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/M3-walkthroughs.md`.

**Scenario 1 — Cycle compound full lifecycle (multi-bundle: Parts 4/5/3/6a/6b/1):**
cycle ends → Part 4 emits task-return-packets (per Part 4 §I.1 UND-1 schema) to `comms/mailboxes/` → Part 5 reads RAW packets (per UND-1 ack — Part 5 does own DRR extraction) → DRR extraction (Decision / Reasoning / Result / Review per Compounding-Engineering §2 P2) → strategies.md update committed via Part 1 §H → admissibility check: candidate accumulates `validated_in_cycles` ≥2 + `rule_slug` populated → Part 5 emits AWAITING-APPROVAL `gate_class: draft_promotion` to Part 6b → Part 6b acks per F8 LOCKED schema → entity moves to `wiki/methodology/<rule-slug>.md` with F4→F5 promotion + `human_acked_at:` populated → `swarm/approvals/log.jsonl` (Part 6a §C) entry → Part 1 commit `[methodology] promote: <slug> (F5 codified rule)` → `wiki/index.md` updated.
Tests: Parts 5 + 4 + 3 + 6a + 6b + 1; UND-1 binding (raw packet consumption); UND-2 binding (methodology promotion pipeline); F4→F5 rise on promotion; gate_class enum F8 LOCKED.

**Scenario 2 — Health anomaly detection + escalation (Parts 1 / 8 / 6b):**
Part 1 commit-error-rate burns 14.4× over 1h window → Part 1 emits health signal (per canonical schema Part 8 §I.1 — Bundle 3 mapping table) → Part 8 detects (per SLI/SLO schema §I.2 burn-rate threshold) → Part 8 classifies via blast-radius (Tier 0 — git substrate integrity per Part 6b §I.4 F8 LOCKED) → Part 8 alert-routing stub maps to Tier 0 → ALL canonical writes halted (per Part 1 K8 policy) → Halt-Log-Alert ordering enforced (≤1s halt / ≤5s log / ≤60s alert per Part 6b §E Law L9 F8) → AWAITING-APPROVAL `gate_class: stop_gate` packet emitted to Part 6b enforcement arm → Ruslan ack required before any new commits → Part 1 §H commit `[meta] postmortem: 14.4x burn 2026-04-XX` after recovery.
Tests: Parts 8 + 1 + 6b; canonical health signal schema (C2 resolution); SLI/SLO schema burn-rate inheritance from Part 1 §J; Halt-Log-Alert F8 LOCKED; Corrigibility (Ruslan can override).

**Scenario 3 — Quarterly immune audit (TRADEOFF-01 split verified) (Parts 8 / 6a / 6b / 1):**
Part 8 cadence trigger (quarterly per part-8 §J) → Part 8 audit lead invokes Part 6a service for F-G-R compliance check across wiki entries (TRADEOFF-01 audit support) → Part 6a F-G-R compliance check primitive runs (per Part 6a Bundle 1 quarterly framework) → drift detected (e.g., 3 wiki entries missing `R.refuted_if:` field) → Part 8 quarterly immune audit report committed at `swarm/audits/<quarter>/p8-quarterly-immune-audit-YYYY-QN.md` (template from Bullet P8.3) → Part 8 emits AWAITING-APPROVAL `gate_class: stage_gate` packet to Part 6b enforcement arm (TRADEOFF-01 enforcement) → Part 6b acks remediation gate → Part 1 commit `[health] quarterly immune audit YYYY-QN: 3 entries remediated` → `swarm/approvals/log.jsonl` entries (Part 6a §C; one per remediated entry).
Tests: Parts 8 + 6a + 6b + 1; TRADEOFF-01 split materialisation (Part 8 audit lead + Part 6a service + Part 6b enforcement); quarterly immune audit template (P8.3 deliverable); F-G-R compliance check primitive.

**Scenario 4 — Methodology promotion via R2 reinforcing loop (Parts 5 / 3 / 6a / 6b / 1):**
pattern emerges in cycle N (e.g., "always run /lint --check-citations after /ingest") → Part 5 DRR entry written to `agents/<id>/strategies.md` with `validated_in_cycles: [cyc-N]` + `rule_slug: ingest-lint-after` + `result: validated` → cycles N+1 + N+2 validate (DRR entries accumulated; `validated_in_cycles: [cyc-N, cyc-N+1, cyc-N+2]`) → Part 5 admissibility predicate satisfied (≥2 distinct cycles + rule_slug + F-level rises target F5) → Part 5 emits methodology candidate at `wiki/methodology/ingest-lint-after-DRAFT.md` with `pipeline: ingested` → AWAITING-APPROVAL `gate_class: draft_promotion` packet to Part 6b → Ruslan acks per F8 LOCKED schema → entity moves to `wiki/methodology/ingest-lint-after.md` with F5 codified rule + ClaimScope + `refuted_if: <Popperian>` → `swarm/approvals/log.jsonl` entry → Part 1 commit → `wiki/index.md` updated → next cycle uses pattern → R2 reinforcing loop closure (5-10 cycle delay before compound effect detectable per systems-thinking-cybernetics §4).
Tests: Parts 5 + 3 + 6a + 6b + 1; UND-2 methodology promotion pipeline; F4→F5 rise; R2 reinforcing loop closure (Part 5 standalone evidence — counter to dissolve dissent).

Pass threshold: 4/4 scenarios trace cleanly with no missing schemas or undefined handoffs. Failure: re-architect specific gaps; do NOT paper over with TODO stubs.

### §7.4 M4 Wisdom Application Loop verification

Per part:
- [ ] §M Wisdom Findings table populated with Operational/Philosophical column (not empty, not 0 adoption — see §5.4)
- [ ] Every "YES Adopted" entry has corresponding visible edit in §A-§L (verify by line-number diff trace)
- [ ] Every "NO" entry has explicit justification from legitimate categories (§5.3)
- [ ] No fabricated YES entries (cross-check: edit actually exists in target section)
- [ ] All relevant Wave B consultants per §3.3 mapping covered for each part (no card silently skipped)
- [ ] All Wave B Supplement library-direct sources per §3.4 covered
- [ ] **Operational adoption ratio ≥85% per part** (Bundle 3 stricter target than Bundle 2's ≥60%)
- [ ] No PHILOSOPHICAL adoptions without scope-creep-prevention or Phase B/C concrete-need justification

Pass threshold: all bullets ticked per part + aggregate ≥85% operational across Bundle 3. Failure: re-run Wisdom Loop with specific gap list; if persistent under-85%, investigate brigadier reverting to philosophical text.

### §7.5 M5 — Joint Design lite coherence verification (C2 + UND-3)

- [ ] Part 8 §I.1 canonical health signal schema declared
- [ ] Part 8 §I.3 mapping table maps Bundle 1+2 emitter shapes (Parts 1, 2, 3, 4) to canonical schema
- [ ] Variant chosen explicitly (A retroactive align OR B mapping table fallback) with rationale
- [ ] If Variant A: retroactive supplement edits to Bundle 1+2 emitter §I sections committed (single commit at end of Joint Design Phase)
- [ ] If Variant B: mapping table fully populated; no orphan emitter shapes
- [ ] UND-3 stub artefact `swarm/wiki/cycles/.../bundle-3/UND-3-stub.md` exists with required sections
- [ ] Part 5 §A Inputs references UND-3 stub artefact (DRY enforced)
- [ ] No conflicting health signal shape statements between Bundle 1+2 and Part 8 §I.1 (semantic check by integrator)

Pass threshold: all bullets ticked. Failure: re-dispatch Joint Design lite Phase.

### §7.6 M6 — Bundle 3 special autochecks

- [ ] Part 5 §X contains OQ-MERGED-2 dissolve-test condition declaration verbatim (per §6.9)
- [ ] Part 5 companion policy artefact `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` exists
- [ ] Part 8 §I.2 every starter SLI value labeled `starter_value_label: "calibration-grade"` (per §6.8)
- [ ] Part 8 §J does NOT specify live metric collection cadence below daily granularity (calibration cadence ≥monthly per OQ-MERGED-5)
- [ ] Part 8 §K contains "K-PartB — over-implementation drift" self-monitored failure mode
- [ ] Part 8 §X explicit "specify and stub" scope declaration
- [ ] Part 8 §H alert-routing is STUB (specification + alert packet schema; NO delivery code)
- [ ] OQ-B2-A retroactive supplement commit landed at Bundle 3 cycle start (per §4.0)
- [ ] All retroactive supplement edits visible: Part 1 §I.4 enum + §I.2 [swarm-lib] token + §K K15 + RUSLAN-ACK Bundle 1 supplement note

Pass threshold: 9/9. Failure: re-dispatch with specific autocheck failure listed.

---

## §8 Output Expected (exact paths, structures)

### §8.1 Per-part architecture documents

- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` (10K-20K words)
- `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` (10K-20K words)

Each with §A-§N + §X sections per §6.2.
Each with YAML frontmatter (per Global Rule 1).

### §8.2 Schemas (specify-and-stub level for Part 8)

**Part 5:**
- Methodology promotion pipeline schema (UND-2 binding) — declared inline in Part 5 §I.1; physical file `shared/schemas/methodology-promotion-event.json` declared (Phase B file generation per OQ-B1-2 + OQ-B1-4 pattern)

**Part 8:**
- `shared/schemas/health-signal.json` — canonical health signal schema (C2 resolution; declared inline in Part 8 §I.1; physical file generation Phase B)
- `shared/schemas/sli-slo.json` — SLI/SLO + error-budget formal spec (declared inline in Part 8 §I.2; physical file generation Phase B; ≥8 starter SLI entries with calibration-grade labels)
- Health signal mapping table (Part 8 §I.3 — maps Bundle 1+2 emitter shapes)

### §8.3 Templates (Bundle 3 deliverables)

- `swarm/audits/weekly-health-template.md` (Bullet P8.3 — populated synthetic Week-NN row)
- `swarm/audits/quarterly-immune-audit-template.md` (Bullet P8.3 — extends Part 6a Bundle 1 quarterly template; populated synthetic Q-N row demonstrating TRADEOFF-01 service invocation result shape)

### §8.4 Configuration files

- Alert-routing stub (Part 8 §H.1 — declared inline; ≥10 alert classes mapped to Tier 0/1/2/3; Halt-Log-Alert ordering enforced)

### §8.5 Joint Design lite artefacts

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` (Part 5 input contract from Part 7; defer Bundle 4 finalization)
- (If Variant A retroactive align chosen for C2 resolution): retroactive supplement edits to Bundle 1+2 emitter §I sections (committed at end of Joint Design lite Phase)

### §8.6 Companion policy artefacts

- `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md` (Bullet P5.3 — mirrors Part 5 §X dissolve-test declaration)

### §8.7 Updated cross-references

- Wave A interface cards Parts 5 / 8 — SUPERSEDED frontmatter addendum (deferred to Bundle 4 housekeeping commit acceptable per Bundle 2 pattern)
- Manifest §2 matrix Bundle 3 rows updated (Parts 5, 8 — adopted cards + Wisdom Loop counts + operational ratio)
- `swarm/lib/routing-table.yaml` extended with Part 5 + Part 8 per-role entries (compound-phase orchestration role; health-monitor role)

### §8.8 Walkthroughs trace

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/M3-walkthroughs.md` — all 4 scenarios traced

### §8.9 Bundle-level dissent (if any)

- `swarm/wiki/foundations/<part-slug>/dissent.md` per part with unresolved critic dissent (AP-6 preservation)
- **Special**: engineering-expert dissent on Part 5 dissolve-test re-cited in Part 5 §X (NOT new dissent — canonical preserved Wave A dissent now formalised in Foundation architecture)

### §8.10 AWAITING-APPROVAL packet (FINAL deliverable)

- `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-XX.md` (XX = day of completion)

Structure mirrors Bundle 1 + 2 packets:

```markdown
---
title: AWAITING-APPROVAL — Wave C Bundle 3 (Parts 5 + 8)
date: 2026-04-XX
type: awaiting-approval
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 3
parent_packet: decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-28.md
predecessor_ack_bundle_1: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md
predecessor_ack_bundle_2: decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md
deep_prompt: prompts/wave-c-bundle-3-deep-prompt-2026-04-28.md
status: awaiting-ruslan-ack
F: F4
ClaimScope: "Holds for the 2 Bundle 3 architecture documents and their declared schemas + templates + retroactive supplement. Does NOT pre-judge Bundle 4 work."
R:
  refuted_if: "Ruslan walkthrough surfaces a constitutional violation, OQ-MERGED-2 dissolve-test under-declared, OQ-MERGED-5 scope-creep, TRADEOFF-01 split incoherence, C2 health signal schema gap, UND-2 methodology pipeline gap, UND-3 P5↔P7 stub leak, or Halt-Log-Alert ordering violation in either of the 2 architecture documents"
  accepted_if: "Ruslan acks the 2 architecture documents AND the schema set AND the templates AND the alert-routing stub AND the §X Foundation vs RUSLAN-LAYER separations AND the Bundle 1 retroactive supplement AND the OQ-MERGED-2 dissolve-test condition declaration"
next_action: "Ruslan ack of this packet → brigadier dispatches Wave C Bundle 4 (Parts 7 + 9 + 10)"
---

## §1 Executive Summary
[3-5 paragraphs: what was built, key decisions (OQ-B2-A retroactive supplement; UND-2 methodology promotion pipeline materialised; UND-3 P5↔P7 stub; C2 canonical health signal schema; TRADEOFF-01 split materialised; OQ-MERGED-2 dissolve-test condition declared; OQ-MERGED-5 specify-and-stub scope held); headline numbers (word counts, schemas defined, edges typed, F-G-R tags applied, SLI entries, alert classes routed, Wisdom Loop adoption count, Operational vs Philosophical ratio).]

## §2 Outcomes — F-level changes
[Table: Artefact / F-before / F-after / Drift rationale — including Part 5 architecture F4→F5, Part 8 architecture F4→F5 (or held at F4 if "specify and stub"), shared/schemas/health-signal.json F0→F4, shared/schemas/sli-slo.json F0→F4, shared/schemas/methodology-promotion-event.json F0→F4]

## §3 Wisdom Findings Rollup (with Operational/Philosophical breakdown)
[Aggregate table across Parts 5 + 8: Total YES Adopted with Operational/Philosophical split / Total NO with reason categories / Per-card coverage matrix / Operational ratio achieved (target ≥85%)]

## §4 Verification Gate Results
- M1 Smoke: Part 5 X% / Part 8 X%
- M2 Cross-ref: 100% (or list broken citations)
- M3 Scenarios: 4/4 PASS (or list failures)
- M4 Wisdom: PASS with operational ratio ≥85% (or gap list)
- M5 Joint Design lite (C2 + UND-3) coherence: PASS (or list incoherence findings)
- M6 Bundle 3 autochecks (dissolve-test + scope-creep + retroactive supplement): PASS (or list failures)

## §5 Open Questions Surfaced By Bundle 3
[Any new OQs beyond those acked at Bundle 1 + 2 ack — with proposed resolution / defer rationale; OQ-B3-X numbering]

## §6 Provenance
[List of every source consulted, with F-G-R tags, with consequence sentences cross-ref; commits on claude/jolly-margulis-915d34 — including OQ-B2-A retroactive supplement commit]

## §7 Ruslan Ack Request
[Specific decisions Ruslan must ack before Bundle 4 dispatches:
 - 2 Bundle 3 architecture documents canonical-promoted (status: ruslan-acked-canonical)?
 - OQ-B2-A retroactive Bundle 1 supplement accepted (Part 1 §I.4 enum + §I.2 [swarm-lib] + §K K15)?
 - OQ-MERGED-2 dissolve-test condition declaration accepted (Bundle 3 = first cycle of 3-cycle window)?
 - OQ-MERGED-5 specify-and-stub scope held for Part 8 (no live metrics; calibration-grade labels)?
 - TRADEOFF-01 split materialised (Part 8 audit lead + Part 6a service + Part 6b enforcement)?
 - C2 canonical health signal schema accepted (Variant A retroactive align OR Variant B mapping table fallback)?
 - UND-2 methodology promotion pipeline schema accepted?
 - UND-3 P5↔P7 stub artefact accepted (Bundle 4 finalises Part 7 emission)?
 - Templates (weekly health + quarterly immune audit) accepted?
 - Alert-routing stub config accepted?
 - shared/schemas/health-signal.json + sli-slo.json + methodology-promotion-event.json acceptable as schemas (physical file generation Phase B)?
 - Any per-part dissent items: Ruslan resolves]

## §8 STOP — Do not auto-launch Bundle 4
Per §11 STOP rule.
```

### §8.11 STOP

After AWAITING-APPROVAL packet — STOP. NO auto-launch Bundle 4.

---

## §9 Branch + Commit Discipline

- **Branch**: `claude/jolly-margulis-915d34` (current, same as Bundle 1 + 2). Do NOT create new branches.
- **Commit cadence**: small + frequent. After each major phase per part.
- **Commit message format**: `[architecture] Bundle 3 — <part> — <phase>` (after retroactive supplement) examples:
  - `[architecture] Bundle 1 retroactive supplement — Part 1 §I.4 gate_class enum + commit-format-tokens.json [swarm-lib] token + K15 upcasting (per OQ-B2-A + OQ-B2-D RUSLAN-ACK Bundle 2)` (FIRST commit of Bundle 3 cycle)
  - `[architecture] Bundle 3 — Part 5 — Phase B + C cells + integrator draft`
  - `[architecture] Bundle 3 — Part 5 — Phase D Wisdom Loop applied (X YES Op / Y YES Phi / Z NO)`
  - `[architecture] Bundle 3 — Parts 5 + 8 — Phase C+ Joint Design lite (C2 canonical health signal schema + UND-3 P5↔P7 stub)`
  - `[architecture] Bundle 3 — Part 8 — Phase B + C cells + integrator draft`
  - `[architecture] Bundle 3 — Part 8 — Phase D Wisdom Loop applied (operational ≥85% target)`
  - `[architecture] Bundle 3 — Part 5 — Phase E critic gate PASS + dissolve-test declaration verified`
  - `[architecture] Bundle 3 — Part 8 — Phase E critic gate PASS + scope-creep autocheck PASS + TRADEOFF-01 split verified`
  - `[architecture] Bundle 3 — M3 walkthroughs 4/4 PASS + M5 Joint Design lite coherence PASS + M6 autochecks PASS`
  - `[architecture] Bundle 3 AWAITING-APPROVAL — Parts 5 + 8 architecture, Wisdom Loop applied (operational ≥85%), C2 + UND-3 resolved, dissolve-test declared, M-gates PASS`
- **Push cadence**: after each commit. No force-push. No `--amend`. No `--no-verify`.
- **API-key audit**: before each commit run `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|sk-ant-' <staged-files>` → 0 hits required.

---

## §10 Operational Constraints

1. `unset ANTHROPIC_API_KEY` before any provider invocation. Brigadier MUST NOT reference any provider API-key env var in any code path.
2. `ulimit -n 65535` if not already set.
3. **HD-02 rate limiter N=2 normal mode**. Maximum 2 concurrent Task() dispatches.
4. **Read tool 32MB limit**: for large PDFs use `pages` parameter; do NOT auto-read full books.
5. **NO auto-execution of Bundle 4 after Bundle 3** — explicit STOP per §11.
6. **No `--amend`, no `--no-verify`, no force-push** — git-native rollback via `git revert` only.
7. **Frontmatter compliance**: every `.md` artefact carries YAML frontmatter per the relevant `swarm/wiki/_templates/<type>.md` template.
8. **Untouchable trees in Phase A**: 14 legacy `.claude/agents/*.md` files and the v2 `wiki/` tree. Bundle 3 EXTENDS routing-table.yaml + adds new methodology entries through canonical promotion gate; does NOT modify the agent files themselves.
9. **Security — never touch**: `~/.ssh/`, `/etc/`, any `.env*`, anything under `private/`, Tier-4 closed-core book corpus.
10. **Working directory**: `/home/ruslan/jetix-os/`. Do not `cd` outside.
11. **Bundle 3 OQ-B2-A retroactive supplement is BLOCKING**: NO substantive Part 5 / Part 8 dispatch BEFORE retroactive supplement commit lands and pushes (per §4.0).
12. **Subagent stall fallback acceptable**: if subagents stall on stream watchdog (as observed in Bundle 2), brigadier may switch to direct-write mode; flag in AWAITING-APPROVAL packet §5 Open Questions for Ruslan visibility.

---

## §11 STOP Rule + Ack Mantra

### §11.1 STOP rule

After AWAITING-APPROVAL packet (`§8.10`) is committed and pushed:

**STOP. DO NOT auto-launch Bundle 4.**

Bundle 4 (Parts 7 + 9 + 10) will only dispatch AFTER Ruslan reviews and acks Bundle 3 AWAITING-APPROVAL packet. Brigadier waits for HITL signal.

Final action: notify Ruslan via tmux output (or stdout if no tmux):

> «Wave C Bundle 3 complete. AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-XX.md`.
> OQ-B2-A retroactive Bundle 1 supplement applied at cycle start (commit hash <H1>).
> Word count summary: Part 5 = N words, Part 8 = N words. Wisdom Loop adoption: N YES (Operational X / Philosophical Y) / N NO. Operational ratio: ZZ% (target ≥85%).
> OQ-MERGED-2 dissolve-test condition declared at Part 5 §X + companion policy `decisions/policy/oq-merged-2-dissolve-test-2026-04-28.md`.
> OQ-MERGED-5 specify-and-stub scope held: Part 8 §I.2 ≥8 starter SLI entries with calibration-grade labels.
> TRADEOFF-01 split materialised: Part 8 audit lead invokes Part 6a service (verified Scenario 3); Part 6b enforcement arm.
> C2 canonical health signal schema declared (Variant <A|B>); mapping table covers Bundle 1+2 emitter shapes.
> UND-2 methodology promotion pipeline materialised in Part 5 §I.1; UND-3 P5↔P7 stub at `swarm/wiki/cycles/.../bundle-3/UND-3-stub.md`.
> Templates: `swarm/audits/weekly-health-template.md` + `swarm/audits/quarterly-immune-audit-template.md`.
> Alert-routing stub maps N alert classes to Tier 0/1/2/3 (Halt-Log-Alert ordering enforced for Tier 0).
> M1/M2/M3/M4/M5/M6 gates: PASS / PASS / 4/4 PASS / PASS / PASS / PASS.
> Awaiting Ruslan ack before Bundle 4 dispatch.»

### §11.2 Autocheck — when to halt early

- **Walltime exceeds 12h**: STOP, report status to Ruslan, ask how to proceed. Do NOT push past 12h without ack. (Bundle 3 is 2 parts vs Bundle 2's 3 — projected 4-7h; 12h ceiling is generous.)
- **Subagent first attempt produces low-quality output** (cargo-cult signals, missing sections, under word count, missing dissolve-test declaration in Part 5 §X, Part 8 produces "live implementation spec" instead of stub): re-dispatch ONCE with explicit feedback citing this prompt's quality bar. Second attempt also fails: escalate.
- **Wisdom Application Loop produces 0 "YES Adopted" for a part**: per §5.4, halt + flag + escalate.
- **Operational adoption ratio < 85% across Bundle 3 after Wisdom Loop**: investigate; re-dispatch integrator to convert PHILOSOPHICAL adoptions into OPERATIONAL ones. If persistent: escalate to Ruslan.
- **Part 8 produces "live implementation spec"** instead of stub-level (delivery code, calibrated thresholds, sub-daily metric collection cadence): scope creep; re-dispatch with stub-level mandate per §6.8 autocheck.
- **Part 5 omits dissolve-test condition declaration** in §X: re-dispatch with §X expansion per §6.9 autocheck.
- **Joint Design lite produces conflicting answers** (C2 Variant A vs Variant B with persistent disagreement): escalate to brigadier-mode arbitration; if unresolved → Ruslan ack required.
- **Critic gate produces irreconcilable dissent across ≥2 experts**: preserve dissent (AP-6) + escalate to Ruslan via dissent.md.
- **Schema design produces ambiguity that requires RUSLAN-LAYER decision**: pause, write `swarm/wiki/foundations/<part-slug>/oq-bundle-3-N.md`, escalate.
- **OQ-B2-A retroactive supplement does NOT land at cycle start** (substantive Bundle 3 dispatch attempted before retroactive supplement commit): IMMEDIATE HALT; brigadier returns to Phase ZERO.
- **Brigadier subagents stall on stream watchdog** (as in Bundle 2): switch to direct-write mode is acceptable; flag in AWAITING-APPROVAL packet §5 for Ruslan visibility.

### §11.3 Budget

~20-30 subagent dispatches across phases (5×4 matrix × 2 parts × dispatched cells + integrators + Joint Design lite Phase + Wisdom Loop pass + critic gates + M-gates). Budget guard: if dispatch count exceeds 40, audit for redundant cells; if exceeds 50, halt and ask Ruslan.

### §11.4 Mantra (recite before each phase transition)

> **QUALITY > SPEED.**
> **PROVENANCE > VOLUME.**
> **WISDOM-APPLIED > WISDOM-CITED.**
> **OPERATIONAL > PHILOSOPHICAL.**
> **SPECIFY-AND-STUB > LIVE-IMPLEMENTATION (Part 8).**
> **STANDALONE-PRESERVED > DISSOLVE (Part 5 — until evidence accumulates across 3-cycle window).**
> **RUSLAN-ACK > BRIGADIER-CONFIDENCE.**
>
> *Bundle 3 wires the compound-learning loop (R2 reinforcing) + observability substrate (Beer VSM S3) atop the Bundle 1 + 2 layers. Without Part 5 the system learns nothing across cycles. Without Part 8 the system has no eyes. Every decision compounds for Phase B/C/D. Treat with 1 trillion percent responsibility.*

---

## §12 Pre-flight Checklist (brigadier runs before first dispatch)

- [ ] Read this prompt three times
- [ ] Read all of §3.1 Constitutional baseline (Bundle 1 + 2 LOCKED — DO NOT re-litigate F-G-R, Default-Deny, AWAITING-APPROVAL packet schema, blast-radius, Halt-Log-Alert, Corrigibility, Parts 2/3/4 architectures, C1 Joint Design canonical, routing-table.yaml, task-return-packet.json schema, message schema v2.0.0)
- [ ] Read all of §3.2 Wave A artefacts (esp. wave-c-worklist §2 Parts 5/8, A-1-critic-gate.md §2 Parts 5+8, dependency-graph.md §3.2 C2 + §4.3 UND-3 + §7 OQ-1 TRADEOFF-01)
- [ ] Read relevant subsets of §3.3 (per part — see §3.3 mapping)
- [ ] Read §3.4 Wave B Supplement library-direct sources (Google SRE Book + Workbook critical for P8; Compounding-Engineering implicit-direct via consultant card for P5; Young 2010 + Bai 2022 + Askell 2021 already F8 from Bundle 1)
- [ ] Skim §3.5 existing operational artefacts (esp. `agents/<id>/strategies.md` baseline for P5; `swarm/wiki/meta/health.md` baseline for P8; `shared/state/system-health.json` baseline for P8 §I.1 schema)
- [ ] Verify branch `claude/jolly-margulis-915d34` is current and clean
- [ ] Verify `unset ANTHROPIC_API_KEY` (operator should have done this)
- [ ] Verify `swarm/lib/README.md` consulted (Bundle 2 C1 canonical answer)
- [ ] Verify `swarm/lib/routing-table.yaml` consulted (Bundle 2 P4.1 deliverable; Bundle 3 extends with Part 5 + Part 8 entries)
- [ ] Acknowledge §0 Mission Statement and §11.4 Mantra internally before first dispatch
- [ ] **Confirm Phase ZERO retroactive supplement BLOCKING**: NO substantive Part 5 / Part 8 dispatch BEFORE retroactive supplement commit lands and pushes
- [ ] Confirm dispatch sequence: Phase ZERO retroactive supplement → Part 5 → Part 8 (with Joint Design lite Phase between Part 5 + Part 8 integrators per §4.3)
  - Alternative: Parts 5 + 8 in parallel within HD-02 N=2 (both integrator phases can run in parallel; Joint Design lite Phase synchronises them)
- [ ] Confirm output paths in §8 are mkdir-ready (parent dirs exist or will be created)

When all bullets ticked: dispatch Phase ZERO retroactive supplement. Then Phase A pre-read confirmation. Then proceed.

---

## §13 Reference — what NOT to do

1. **DO NOT skip Phase ZERO retroactive supplement.** OQ-B2-A is BLOCKING — first task of Bundle 3 cycle.
2. **DO NOT re-litigate Bundle 1 + 2 LOCKED schemas** (F-G-R, Default-Deny, blast-radius, AWAITING-APPROVAL packet schema, Halt-Log-Alert, Corrigibility, Parts 2/3/4 architectures, C1 Joint Design canonical, routing-table.yaml, task-return-packet.json schema, message schema v2.0.0). Bundle 3 CONSUMES these as F8 / F5 constitutional contracts.
3. **DO NOT skip the Joint Design lite Phase.** C2 + UND-3 cannot be designed sequentially-in-isolation.
4. **DO NOT skip the Wisdom Application Loop.** It is the central directive.
5. **DO NOT auto-launch Bundle 4.** Always STOP after Bundle 3 AWAITING-APPROVAL.
6. **DO NOT fabricate Wisdom YES entries** to satisfy the loop. Zero adoption with reasoning > fake adoption.
7. **DO NOT use generic `depends-on` edges.** A.14 typed edges only.
8. **DO NOT cite without consequence sentence within 200 chars.** Cargo-cult is the failure mode.
9. **DO NOT exceed 20K words per part doc with redundancy padding.** Tighten before critic.
10. **DO NOT come in under 10K words per part doc.** Re-dispatch integrator with operational expansion mandate.
11. **DO NOT silently override expert dissent.** Preserve in dissent.md.
12. **DO NOT touch the Untouchable trees** (§10.8) or Security paths (§10.9).
13. **DO NOT push to `main`.** Branch `claude/jolly-margulis-915d34` only.
14. **DO NOT use `--amend` / `--no-verify` / force-push.**
15. **DO NOT reference any provider API-key env var** in code paths brigadier produces.
16. **DO NOT confuse Foundation with RUSLAN-LAYER.** §X section is mandatory; Bundle 3 NEW §X requirements per §6.7 (P5 dissolve-test + P8 specify-and-stub scope).
17. **DO NOT include executor names in Bundle 3 Foundation artefacts.** IP-1 strict — model names, agent file paths, instance IDs are RUSLAN-LAYER `executor-binding.yaml` only.
18. **DO NOT produce "live implementation spec" for Part 8.** Per OQ-MERGED-5: schemas + templates + stub routing only. NO delivery code. NO calibrated thresholds. NO sub-daily metric collection cadence. Calibration-grade labels mandatory.
19. **DO NOT omit dissolve-test condition declaration in Part 5 §X.** Per OQ-MERGED-2 Bullet P5.3: verbatim condition + engineering-expert dissent preserved + 3-cycle window threshold + dissolve path declared.
20. **DO NOT bias toward PHILOSOPHICAL adoptions** in Wisdom Loop. Bundle 3 explicit operational ≥85% bias per Bundle 2 demonstration + Compound Learning + Health Monitoring being inherently operational.
21. **DO NOT propose bullets outside §2 scope.** Bundle 3 = Parts 5 + 8 with the 7 bullets enumerated (3 P5 + 4 P8). Other parts (7, 9, 10) are Bundle 4.
22. **DO NOT prematurely lock UND-3 Part 7 emission contract.** Part 5 declares INPUT EXPECTATIONS; Bundle 4 Part 7 finalises EMISSION.
23. **DO NOT duplicate the Part 3 §E L9 admissibility predicate in Part 5 §I.1.** Part 5 owns EMISSION schema; Part 3 owns ADMISSION schema; both reference each other; DRY enforced.
24. **DO NOT split TRADEOFF-01 incoherently.** Part 8 = audit lead; Part 6a = audit support (service invocation); Part 6b = enforcement arm. Beer VSM S3 split must be visible in Part 8 §H + §I + §J.

---

## §14 Final note from Ruslan (paraphrased intent, brigadier internalize)

Bundle 3 is the third compounding step. Bundle 1 froze the constitutional contracts; Bundle 2 wired the productive layers; Bundle 3 closes the two most consequential feedback loops:

- **R2 reinforcing loop (Part 5)**: every cycle's execution becomes input to the next cycle's improved execution. The DRR ledger that lives in `agents/<id>/strategies.md` already accumulated 19 entries pre-Bundle-3. Bundle 3 canonicalises the 40/10/40/10 ritual, the methodology promotion pipeline (UND-2), and the dissolve-test condition (OQ-MERGED-2). **Without Part 5 the system executes brilliantly once, then re-derives the same lessons next cycle.** Bundle 3 = first cycle of dissolve-test window; engineering-expert dissent preserved.

- **Immune-system loop (Part 8)**: Beer VSM S3 audit function. SLI/SLO + error-budget + burn-rate triad. Quarterly immune audit invoking Part 6a as F-G-R compliance service per TRADEOFF-01 split. Alert-routing stub mapped to Part 6b enforcement arm via blast-radius Tier 0/1/2/3. **Without Part 8 the system has no eyes — drift is invisible until catastrophe.** Bundle 3 scope = "specify and stub" per OQ-MERGED-5; live calibration is Phase B (2-3 month operational data).

From here on:

- Every cycle close flows through Part 4 (task-return-packet) → Part 5 (DRR extraction + methodology promotion) → Part 6b (gate) → Part 3 (canonical methodology entry). The compound is closed-loop.
- Every silent degradation flows through Part 1 (Four Golden Signals) → Part 8 (canonical health signal schema + SLI/SLO + burn-rate detection) → Part 6b (alert routing per Tier 0/1/2/3 + Halt-Log-Alert) → Ruslan ack. The observability is closed-loop.
- Every fork (Phase B partner, Phase C product, Phase D org) imports the Bundle 3 schemas (DRR schema, methodology promotion pipeline, canonical health signal schema, SLI/SLO triad, alert-routing stub, weekly + quarterly templates) as Foundation generics; Ruslan-specific bindings (specific DRR entries, specific SLI thresholds, specific alert destinations) overlay as RUSLAN-LAYER.

If Bundle 3 is half-baked, Bundle 4 (Part 7 project lifecycle + Part 9 owner interaction + Part 10 external touchpoints) inherits weak compound and weak observability signals. If Bundle 3 over-engineers Phase B/C/D scenarios, Phase A delivery drags.

The right level: **single-owner Phase A €50K horizon, but FORK-READY to scale**. Compound Learning ritual canonicalised now means Phase B partners inherit a working learning loop, not a documentation pile. Health Monitoring schemas declared now means Phase B calibration starts from named SLIs with defined error budgets, not from aspirational "all green" hardcoded JSON. TRADEOFF-01 split materialised now means Beer VSM S3 oscillation risk is structurally avoided.

This is the architecture document a Phase B partner can read in 60 minutes (matching Bundle 2 — Bundle 3 is "everyday operations + system immune system") and import in half a day. Make it the document where the WISDOM IS APPLIED OPERATIONALLY (≥85% per Bundle 3 stricter target — Compound Learning + Health Monitoring are inherently operational; if drops below 85% that is a red flag and brigadier investigates).

**OQ-MERGED-2 dissolve-test active — Bundle 3 = first cycle of 3-cycle window.**
**OQ-MERGED-5 specify-and-stub held — Part 8 = schemas + templates + routing stub, NOT live impl.**
**TRADEOFF-01 split materialised — Part 8 audit lead + Part 6a service + Part 6b enforcement arm.**
**OQ-B2-A retroactive supplement BLOCKING — first task at cycle start before substantive dispatch.**

---

*End of deep prompt. Brigadier dispatch begins after §12 pre-flight checklist passes — first action is Phase ZERO retroactive supplement per §4.0.*
