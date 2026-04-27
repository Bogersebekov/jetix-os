---
title: Cloud Code Brief — Write the Wave C Bundle 3 deep prompt for ROY brigadier
date: 2026-04-28
type: meta-brief
target: Cloud Code on server (claude --dangerously-skip-permissions in tmux)
purpose: Server CC reads this brief + all context files, then writes full deep prompt for ROY brigadier to execute Wave C Bundle 3 (Parts 5 + 8 — Compound Learning + Health Monitoring)
output_required: prompts/wave-c-bundle-3-deep-prompt-2026-04-28.md (committed + pushed)
estimated_walltime: 30-60 min server CC work to write the deep prompt
critical_constraints:
  - DO NOT execute Wave C Bundle 3 itself — only write the prompt
  - Apply Bundle 2 lessons: word count target 10K-20K (UPDATED from 15K-25K per Ruslan ack constitutional refinement F8)
  - Operational adoption ratio target ≥60% (Bundle 2 demonstrated 89% achievable — preserve)
  - Bundle 3 first task = OQ-B2-A retroactive Bundle 1 fix (~30 min) BEFORE substantive Part 5/8 dispatch
---

# Cloud Code Brief — Write Wave C Bundle 3 Deep Prompt

## §0 What you (server CC) are doing

You are NOT executing Wave C Bundle 3. You are writing the **deep prompt** that ROY brigadier will execute later.

**Output: `prompts/wave-c-bundle-3-deep-prompt-2026-04-28.md`** — 500-800 lines, action-ready.

Commit + push when done. STOP. Notify Ruslan via tmux output:
> «Wave C Bundle 3 deep prompt written at <path>. Lines: <N>. Ready for Ruslan review.»

---

## §1 Context — what's done and LOCKED

### Bundles 1 + 2 LOCKED state on `claude/jolly-margulis-915d34` HEAD `7bcd19a`

**6/10 Foundation parts COMPLETED + LOCKED:**
- Part 1 — System State Persistence (Bundle 1, F5 LOCKED, 17K words)
- Part 6a — Provenance Officer (Bundle 1, F5 LOCKED, 16K words)
- Part 6b — Human Gate (Bundle 1, F5 LOCKED, 15K words)
- Part 2 — Signal Ingestion & Triage (Bundle 2, F5 LOCKED, 12K words)
- Part 3 — KB & Methodology Library (Bundle 2, F5 LOCKED, 9K words)
- Part 4 — Role Taxonomy & Coordination Protocol (Bundle 2, F5 LOCKED, 9K words)

### F8 constitutional schemas (CANNOT re-litigate)

| Artefact | Status | Bundle 3 consumption rule |
|---|---|---|
| `f-g-r.json` (Part 6a §I.1) | F8 LOCKED | Part 5 + Part 8 emitted artefacts MUST carry F-G-R per F4="≥3 cycles applied" / F6="cross-cycle reuse evidence" / F8="lock-class" anchor wording |
| `awaiting-approval-packet.json` with `gate_class` enum (Part 6b §I.1) | F8 LOCKED | Part 5 promotion of methodology entries uses `gate_class: draft_promotion`. Part 8 health alert escalation uses `gate_class: stop_gate` for Tier 0 integrity events |
| `default-deny-table.yaml` (Part 6b §I.3) | F8 LOCKED | Part 8 alert routing — novel alert classes Default-Deny classified |
| `blast-radius-table.yaml` 4 tiers (Part 6b §I.4) | F8 LOCKED | Part 8 mapping anomalies → Tiers 0-3 + escalation per tier |
| Halt-Log-Alert L9 (Part 6b §E) | F8 LOCKED | Part 8 alert delivery conforms to ≤1s halt / ≤5s log / ≤60s alert ordering |
| Corrigibility (Askell HHH Appendix E.2 / Part 6b §E L9) | F8 LOCKED | Part 8 monitoring NEVER locks Ruslan out of override |

### Bundle 1 + 2 contracts Bundle 3 calls

- **Part 1 §H commit interface** — Part 5 strategies.md updates committed; Part 8 health snapshots committed
- **Part 1 §B Four Golden Signals** — Part 8 consumes signals emitted by Part 1 (latency-p95 / cadence-per-day / hook-failure-rate / repo-growth)
- **Part 6a `[src:filename]` enforcement** — every Bundle 3 architecture document follows citation discipline
- **Part 6a approval log structure** (`swarm/approvals/log.jsonl`) — every Bundle 3 promotion event logs entry
- **Part 6b stage-gate predicates** — methodology promotion (Part 5) gate-checked
- **Part 4 `task-return-packet.json` schema** — Part 5 CONSUMES raw packets per UND-1 (Ruslan-acked: P5 raw, does own DRR extraction)
- **Part 3 `wiki/methodology/` entity-type + L9 admissibility predicate** (≥1 DRR validated marker from ≥2 cycles + rule_slug + F4→F5 rise) — Part 5 promotes patterns into this namespace
- **PARA-tier mandatory frontmatter** — Part 5 methodology entries tagged
- **Message schema v2.0.0** (with `acting_as:` mandatory) — Part 5 + Part 8 outputs use v2.0.0

### Bundle 3 OQ inputs (from prior Ruslan acks)

| OQ | Status | Implication |
|----|--------|-------------|
| **OQ-MERGED-2** | Part 5 STANDALONE preserved (dissolve-test active) | If 3 Wave C cycles show zero residual compound work → reconvene. Bundle 3 = first cycle of dissolve-test window. Engineering-expert dissent preserved. |
| **OQ-1 / TRADEOFF-01** | Part 8 = AUDIT LEAD, Part 6a = audit support, Part 6b = enforcement arm | Bundle 3 Part 8 architecture canonicalizes audit cadence + invokes Part 6a as service for F-G-R compliance check. Beer VSM S3 split clean. |
| **OQ-MERGED-5** | Part 8 "specify and stub" Wave C; full impl Phase B | Bundle 3 Part 8 = SLI/SLO schema + template authoring; NOT live metrics implementation. FUNDAMENTAL §3 starter values need 2-3 months Phase B calibration. |
| **C2 contradiction** | Part 8 owns canonical health signal schema; all emitters conform | Bundle 3 Part 8 §I.1 canonicalizes schema; emitters in Bundle 1 + 2 architectures (Parts 1, 2, 3, 4) align in retroactive supplement OR Part 8 §I.1 explicitly references current emitter shapes |
| **UND-2** | Methodology promotion pipeline schema (P5 work) | Bundle 3 Part 5 §I — schema for `wiki/methodology/<pattern>.md` admissibility + promotion event format |
| **UND-3** | P7 → P5 retrospective schema + cadence | Part 7 is Bundle 4. Bundle 3 Part 5 specifies WHAT P5 EXPECTS from P7 (input contract); Bundle 4 Part 7 specifies HOW P7 EMITS (output contract). Joint Design lite (defer cross-bundle finalization to Bundle 4 Part 7 work) |

### Word count target (NEW constitutional F8 per Ruslan ack Bundle 2)

- **Floor: 10K words** (down from 15K)
- **Ceiling: 20K words** (down from 25K)
- **Bias: operational content density over verbosity**

If draft <10K: re-dispatch with §A-§N expansion mandate focusing on OPERATIONAL deltas (schema fields / failure modes / SLO targets / lint checks / algorithms). NOT philosophical framing prose.

### Operational adoption ratio (per Bundle 2 demonstration)

- Target ≥60%
- Bundle 2 achieved 89%
- Bundle 3 should match or exceed (Compound Learning is _intrinsically_ operational — this should be easy)

---

## §2 Bundle 3 scope — Parts 5 + 8

### FIRST TASK (before substantive Part 5/8 dispatch): OQ-B2-A retroactive Bundle 1 fix

**~30 min effort. Single commit at start of Bundle 3 cycle.**

1. **Part 1 §I.4 stub `gate_class` enum** — align to Part 6b §I.4 F8 LOCKED `[stop_gate, stage_gate, draft_promotion]` (was stale `[autonomous, requires-approval, hitl-required]`)
2. **`[swarm-lib]` token** — add to Part 1 §I.2 commit-format-tokens.json schema (per OQ-B2-D ack)
3. **NEW K15 upcasting failure mode** — add to Part 1 §K (handles legacy v1.0.0 messages → upcast or reject per Part 4 schema_version_history)
4. **Update RUSLAN-ACK Bundle 1 record** — append retroactive correction note OR create supplement file

Commit: `[architecture] Bundle 1 retroactive supplement — Part 1 §I.4 gate_class enum + commit-format-tokens.json [swarm-lib] token + K15 upcasting`. Push. Then proceed to substantive Bundle 3 work.

### Part 5 — Compound Learning & Methodology Capture (3 bullets per wave-c-worklist §2 P5)

- **P5.1** — Compound ritual (40/10/40/10 Plan/Work/Review/Compound) as canonical Foundation artefact (architecture document + ritual spec + cadence). Currently informal in cycles 11-12; Wave C formalizes.
- **P5.2** — Methodology promotion pipeline (UND-2): from `agents/<id>/strategies.md` → admissibility check (Part 3 §E L9 predicate) → Part 6b draft_promotion gate → `wiki/methodology/<pattern>.md` canonical. Schema + flow.
- **P5.3** — OQ-MERGED-2 dissolve-condition declaration: explicit criterion "if 3 Wave C cycles show zero residual compound-phase-exclusive work, dissolve test fires; engineering-expert dissolve hypothesis re-evaluated". Documented in Part 5 §X (Foundation vs RUSLAN-LAYER) AND in `decisions/policy/`.

### Part 8 — Health Monitoring & System Integrity (4 bullets per wave-c-worklist §2 P8)

- **P8.1** — SLI/SLO schema definition (`shared/schemas/sli-slo.json`) — formal spec for SLI (Service Level Indicator) + SLO (Objective) + error-budget + burn-rate behaviour-change rule. Per SRE Workbook §12 burn-rate algebra (1×/6×/14.4× — already adopted in Part 1 §J Bundle 1).
- **P8.2** — Health signal schema per emitting part (C2 resolution) — Part 8 §I.1 canonicalizes signal shape; Bundle 1 + 2 emitters (Parts 1, 2, 3, 4) align in retroactive supplement at Bundle 3 cycle (or Part 8 explicitly accepts current heterogeneous emitter shapes with mapping table)
- **P8.3** — Weekly health dashboard template + quarterly immune audit template
- **P8.4** — Alert-routing stub to Part 6b — Tier 0/1/2/3 mapped per blast-radius-table.yaml; Halt-Log-Alert ordering enforced

### Cross-cuts within Bundle 3

| Cross-cut | Rule | Where applied |
|---|---|---|
| **F-G-R DOGFOOD** | Every claim in P5/P8 architecture has F-G-R per Part 6a F8 schema | §G Tagging table; inline tags |
| **A.14 typed edges** | Bundle 1 canonical 10-edge table referenced; no new edge types invented | §D Dependencies |
| **Append-only** | strategies.md / methodology entries / health snapshots / audit reports — append-only | §C Side-effects |
| **L/A/D/E** | Every interface section structured per FPF A.6.B | §E Boundary |
| **Foundation vs RUSLAN-LAYER** | Explicit §X per part | §X mandatory |
| **PARA-tier** | Methodology entries (Part 5) tagged `para_tier: Resource` (reusable) or `Archive` (deprecated) | Part 5 emit rule |
| **Operational ≥60%** | Wisdom Loop OPERATIONAL/PHILOSOPHICAL discriminator — Bundle 3 should easily exceed (compound learning + observability are inherently operational domains) | §M Wisdom Findings |
| **Word count 10K-20K** | NEW constitutional target | §6 Quality bar in deep prompt |
| **C2 health signal schema joint with emitters** | Part 8 §I.1 canonicalizes; brigadier decides whether Bundle 1+2 emitters need retroactive alignment | Part 8 §I.1 + retroactive supplement (if needed) |

### Special: Part 5 ↔ Part 7 (Bundle 4) cross-bundle interface (UND-3)

Part 7 is Bundle 4 work. Bundle 3 Part 5 must specify the **input contract** ("Part 5 expects retrospective input from Part 7 in format X with cadence Y") without finalizing how Part 7 emits. Bundle 4 Part 7 will then conform.

Brigadier action: in Part 5 §A Inputs declare Part 7 as upstream source with **stub schema reference** (`task-return-packet.json` superset OR project-retrospective-packet.json TBD); marked as Phase 2 (Bundle 4) finalization. Avoid premature lock.

### Special: Part 5 ↔ Part 4 already finalized (UND-1)

Part 4 §I.1 `task-return-packet.json` is F4 (rises to F5 on Bundle 3 Part 5 consumption validation). Bundle 3 Part 5 §B specifies CONSUMPTION pattern: Part 5 reads RAW packets from `comms/mailboxes/` (per Ruslan ack OQ-3), does own DRR extraction, writes DRR entries to `agents/<id>/strategies.md`.

---

## §3 Required reading list for ROY brigadier

### A. Constitutional baseline

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (focus §2 Compound flows + §3 SLI/SLO 30+ pairs + §5 reliability 3-2-1 + §6 anti-scope)
2. `design/JETIX-FPF.md` (focus IP-3 / IP-4 / IP-7 / IP-8; A.6.B L/A/D/E; B.3 F-G-R)
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (current cycle artefacts)
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (§4.5 deep-study constraint — UPDATED to 10K-20K per Bundle 2 ack)
5. **Bundle 1 architectures (constitutional inputs):**
   - `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (esp. §B Four Golden Signals; §J burn-rate table; §I.4 task-return-packet stub; §K K15 upcasting AFTER retroactive supplement)
   - `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (esp. §I.1 F-G-R schema; §C approval log; quarterly audit framework)
   - `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (esp. §I.1 awaiting-approval-packet; §I.3 default-deny; §I.4 blast-radius; §E L9 Halt-Log-Alert + Corrigibility)
6. **Bundle 2 architectures:**
   - `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md`
   - `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` (esp. §E L9 methodology promotion admissibility; §I `wiki/methodology/` entity-type)
   - `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (esp. §I.1 task-return-packet schema; §I.2 routing-table.yaml; §I.3 executor-binding template)
7. **Ack records:**
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md`
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md` (esp. §3 WORD COUNT TARGET UPDATE 10K-20K F8)
8. Locks D1-D29 + 4 LOCKS-ADDENDUMs (focus D26 hub-and-spoke; D29 Korp-Startup)

### B. Wave A artefacts

- MASTER-PLAN-DRAFT.md
- candidate-parts-merged.md (esp. §2 P5 + §2 P8 parts)
- dependency-graph.md (esp. P5 ↔ P4/P3/P8 + P8 ↔ P6a/P6b/all)
- wave-c-worklist.md (esp. §2 P5 + §2 P8 bullets)
- M3-scenario-walkthroughs.md (Bundle 1 baseline)
- Wave A interface cards: part-5-compound-learning-methodology-capture.md + part-8-health-monitoring-system-integrity.md

### C. Wave B consultant cards (per Manifest §2 matrix for P5 + P8)

**For Part 5:**
- `compounding-engineering.md` (PRIMARY — 40/10/40/10 ritual; DRR ledger; Error→Rule→Skill pipeline)
- `levenchuk-shsm-fpf.md` (IP-7 writing-as-thinking — Ruslan reflection domain; IP-3 artifacts-over-conversations)
- `product-management-cagan-shape-up.md` (OKR cadence; Ries build-measure-learn at system level)
- `stoic-epistemic.md` (Popper falsifiability as rule-promotion gate)
- `systems-thinking-cybernetics.md` (R1 knowledge compound loop — 5-10 cycle delay)

**For Part 8:**
- `sre-observability.md` (PRIMARY — SLI/SLO/error-budget triad; fail-loud P6; toil reduction P4)
- `systems-thinking-cybernetics.md` (Beer VSM S3 audit function; Ashby variety for monitor; Meadows L7 information-flows leverage)
- `capital-allocation-antifragility.md` (Marks second-level: moat = drift discipline; antifragile via stressors)
- `levenchuk-shsm-fpf.md` (IP-4 quarterly immune-system audit function)
- `anthropic-constitutional-ai.md` (integrity violations = absolute halt; softcoded degradation for velocity SLIs)

### D. Wave B Supplement library-direct sources (Bundle 3 critical)

1. `raw/books-md/sre/google-sre-book.md` — full Ch.4 SLO / Ch.6 Monitoring / Ch.15 Postmortems / Ch.22 Cascading
2. `raw/books-md/sre/google-srewb-implementing-slos.md` — Ch.2 burn-rate algebra
3. `raw/books-md/event-sourcing/young-cqrs-2010.md` — Reversal Transactions for compound history (no-delete)
4. `raw/books-md/anthropic/bai-2022-cai.md` — RLAIF self-critique pattern (Part 8 audit signal generation analog)
5. `raw/books-md/anthropic/askell-2021-hhh.md` — corrigibility (Part 8 NEVER locks owner out)

### E. Existing operational artefacts (audit reference)

- `agents/<id>/strategies.md` files (8 of them — current strategy entries, R2 loop input)
- `swarm/wiki/meta/health.md` (current informal health doc — Part 8 will canonicalize)
- `swarm/wiki/meta/agent-improvements/` (existing pattern improvements queue)
- `swarm/evals/` (3/20 cells seeded — eval system stub)
- `shared/state/system-health.json` (currently "all green" hardcoded — Part 8 will replace with real computation spec)
- `shared/state/metrics/agent-performance.json` + `task-log.jsonl` (current metrics)

---

## §4 Wisdom Application Loop — Bundle 3 (preserve Bundle 2 discipline)

**Same structure as Bundle 2** (with OPERATIONAL/PHILOSOPHICAL discriminator):

For each Part (5, 8) after integrator produces draft:

| Card | Principle | Current state | Improvement | Adopted? | Operational/Philosophical | Justification |
|------|-----------|---------------|-------------|----------|----------------------------|---------------|
| ... | ... | ... | ... | YES/NO/ALREADY | OPERATIONAL/PHILOSOPHICAL | ... |

**Bundle 3 expectations:**

- Operational ratio ≥60% target (Bundle 2 = 89% — Bundle 3 should be >85% given Part 5 + Part 8 are inherently operational domains)
- Compounding Engineering full mining for Part 5 (40/10/40/10, DRR, R2 loop, Error→Rule→Skill pipeline — direct constitutional content)
- SRE Book + Workbook full mining for Part 8 (SLI/SLO/error-budget triad is structural backbone)
- Reject any adoption whose "concrete consequence sentence" is purely about how the document reads

**Aggregate target:** Bundle 3 ≥85% operational (higher than Bundle 2's 89% because Compound + Health are intrinsically operational; if drops below 85% → red flag, brigadier investigates).

---

## §5 Quality bar

### Word count: 10K-20K per Part (NEW constitutional)

- Part 5 architecture: 10K-20K
- Part 8 architecture: 10K-20K

If <10K: brigadier returns to integrator with §A-§N OPERATIONAL expansion mandate.
If >20K: review for redundancy + cargo-cult padding.

### Anti-cargo-cult enforcement

(Same as Bundle 1 + 2.) Every `[src:...]` citation followed within 200 chars by concrete consequence sentence. /lint --check-citations is enforcer (Phase B blocking; Phase A advisory).

### Typed A.14 edges (canonical 10-edge table from Bundle 1)

No new edge types. NO `depends-on` outside Prohibited declarations.

### F-G-R DOGFOOD per F8 schema

Every Bundle 3 claim has F-G-R per Part 6a §I.1 schema.

### Foundation vs RUSLAN-LAYER fork-separation

For Bundle 3:
- **Part 5 fork-separation:** 40/10/40/10 ritual structure + DRR schema + methodology promotion pipeline GENERIC. Specific patterns (which methodologies Ruslan promoted; which DRR entries) = RUSLAN-LAYER.
- **Part 8 fork-separation:** SLI/SLO schema framework + 4-tier blast-radius mapping + Beer VSM S3 placement GENERIC. Specific SLI thresholds + alert routing destinations + immune audit checklist contents = RUSLAN-LAYER.

### Special: Part 8 "specify and stub" enforcement

Per OQ-MERGED-5 ack: Part 8 Wave C output = SLI/SLO schema + template authoring + alert-routing stub. NOT live metrics implementation. NOT calibrated thresholds.

Phase B work: 2-3 months calibration of FUNDAMENTAL §3 starter values; live metrics emission; alert delivery infrastructure; immune audit execution.

If brigadier produces "live implementation spec" for Part 8 — that's scope creep. Reject and re-dispatch with stub-level mandate.

### Special: Part 5 standalone preservation (OQ-MERGED-2 dissolve test)

Bundle 3 = first cycle of dissolve-test window. Part 5 §X MUST declare:
- Dissolve test condition: "if Bundle 3 + Bundle 4 + Wave D show zero residual compound-phase-exclusive work, dissolve hypothesis activates"
- Engineering-expert dissent preserved (linked to consultant-systems-thinking-cybernetics.md or original cell file)
- Threshold for declaring dissolve-test PASSED (= Part 5 is correctly standalone): ≥3 distinct compound-phase-exclusive operations in Bundle 3 + Bundle 4 + Wave D

---

## §6 Verification gates

### M1 Smoke Test (per part, threshold ≥90%)

Same 9 checks as Bundle 1 + 2:
1. All §A-§N + §X populated (16 sections)
2. Word count 10K-20K (NEW target)
3. Dependencies §D typed per A.14
4. F-G-R tags on every promoted claim
5. Wave C bullets §L mapped with acceptance predicate ✅
6. §X Fork-separation explicit
7. No cargo-cult signals
8. Bundle 3-specific: P5 dissolve-test condition declared in §X; P8 "specify and stub" scope verified
9. Part 8 specific: TRADEOFF-01 split materialized (Part 8 audit lead invoking Part 6a service; Part 6b enforcement arm)

### M2 Cross-Reference (100% citation resolution)

Spot-check sample of 10+ critical files (constitutional + Bundle 1+2 architectures + 5 Wave B cards + 5 Wave B Supplement library-direct).

### M3 Scenario Walkthroughs (4/4)

Bundle 3 scenarios:

1. **Cycle compound full lifecycle**: cycle ends → Part 4 emits task-return-packets → Part 5 reads raw → DRR extraction → strategies.md update → admissibility check (Part 3 §E L9) → Part 6b draft_promotion gate → wiki/methodology/<pattern>.md canonical → Part 6a F-G-R tag + log entry → Part 1 commit. Tests P5/P3/P6a/P6b/P1.
2. **Health anomaly detection + escalation**: Part 1 commit-error-rate burns 14.4× → Part 1 emits health signal → Part 8 detects (per SLI/SLO schema) → blast-radius classify Tier 0 → Halt-Log-Alert via Part 6b enforcement arm → all canonical writes halted. Tests P8/P6b/P1.
3. **Quarterly immune audit (TRADEOFF-01 verified)**: Part 8 cadence trigger → Part 8 audit lead invokes Part 6a service for F-G-R compliance check across wiki entries → drift detected → Part 6b remediation gate → Part 1 commit + Part 6a log. Tests P8/P6a/P6b/P1.
4. **Methodology promotion via R2 reinforcing loop**: pattern emerges in cycle N → DRR entry → cycles N+1, N+2 validate → Part 5 admissibility predicate satisfied → Part 6b draft_promotion ack → wiki/methodology/<pattern>.md canonical with F4→F5 rise → next cycle uses pattern → R2 loop closure. Tests P5/P3.

### M4 Wisdom Application Loop verification

Same as Bundle 2:
- §M Wisdom Findings table populated
- Every YES Adopted has corresponding §A-§L edit
- Every NO entry justified
- Operational ratio ≥85% per part (Bundle 3 stricter target than Bundle 2's ≥60%)
- All major Wave B consultants + supplement sources covered

---

## §7 ETA + autocheck

**Walltime estimate: 3-6h ROY work** at Bundle 2 compound velocity (Bundle 2 done 43min for 3 parts; Bundle 3 = 2 parts = ~30-45 min projected). Plus retroactive Bundle 1 fix ~30 min at start. Plus Wisdom Loop + critic + verification gates.

**Autocheck rules:**
- If walltime exceeds 12h — STOP, report
- If Part 8 produces "live implementation spec" — scope creep, re-dispatch with stub-level mandate
- If Part 5 omits dissolve-test condition declaration — re-dispatch with §X expansion
- If Wisdom Loop operational ratio <85% — investigate + re-strict
- If brigadier subagents stall on stream watchdog (as in Bundle 2) — switch to direct-write mode is acceptable; flag in AWAITING-APPROVAL packet

---

## §8 Output expected from Bundle 3

### Per-part architecture documents

- `swarm/wiki/foundations/part-5-compound-learning-methodology-capture/architecture.md` (10K-20K words)
- `swarm/wiki/foundations/part-8-health-monitoring-system-integrity/architecture.md` (10K-20K words)

### Schemas (specify-and-stub level for Part 8)

- Part 5: methodology promotion pipeline schema (UND-2 binding)
- Part 8: `shared/schemas/sli-slo.json` (SLI/SLO + error-budget formal spec)
- Part 8: health signal schema (C2 resolution — Part 8 §I.1 canonicalizes)

### Templates

- Part 8: weekly health dashboard template at `swarm/audits/weekly-health-template.md`
- Part 8: quarterly immune audit template (extends Part 6a quarterly template from Bundle 1)

### Configuration files

- Part 8: alert-routing stub config (mapping Tier 0/1/2/3 → escalation paths via Part 6b)

### Joint Design lite (Part 5 ↔ Part 7 Bundle 4 interface)

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-3/UND-3-stub.md` (Part 5 input contract from Part 7; defer Bundle 4 finalization)

### Updated cross-references

- Wave A interface cards Parts 5 / 8 SUPERSEDED frontmatter
- Manifest §2 matrix Bundle 3 rows updated

### AWAITING-APPROVAL packet

- `decisions/AWAITING-APPROVAL-wave-c-bundle-3-2026-04-XX.md` (same structure as Bundle 1 + 2 packets)

### STOP

After AWAITING-APPROVAL packet — STOP. No auto-launch Bundle 4.

---

## §9 Branch + commit + operational

- Branch: `claude/jolly-margulis-915d34`
- Commit pattern: `[architecture] Bundle 3 — <part> — <phase>` (after retroactive supplement)
- Push after each major phase
- `unset ANTHROPIC_API_KEY` before claude
- `ulimit -n 65535`
- HD-02 N=2

---

## §10 What server CC does NOW

1. Read this brief fully
2. Read Bundle 2 deep prompt (`prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md`) for structure reference — Bundle 3 prompt is similar pattern
3. Read RUSLAN-ACK Bundle 1 + Bundle 2 records (esp. ACK Bundle 2 §3 WORD COUNT TARGET 10K-20K constitutional)
4. Read Bundle 1 + Bundle 2 architecture documents for constitutional inputs (focus §I schemas, §H interfaces, §E Laws — these are inputs Bundle 3 consumes)
5. Read Wave A interface cards Parts 5 + 8 + dependency-graph + wave-c-worklist §2 P5 + §2 P8
6. Read 5 Wave B consultant cards for P5 + 5 cards for P8
7. Read 5 Wave B Supplement library-direct sources (Google SRE Book + Workbook critical for P8)
8. Skim Bundle 1 + 2 AWAITING-APPROVAL packets for output format reference

Then write `prompts/wave-c-bundle-3-deep-prompt-2026-04-28.md` (500-800 lines) with structure mirroring Bundle 1 + 2 deep prompts, adapted for Bundle 3 scope:

- Mission statement (Bundle 3 = Compound Learning + Health Monitoring; building on 6 LOCKED parts; Treat with 1 trillion percent responsibility)
- Constitutional inputs (Ruslan acks + F8 schemas + Bundle 1+2 architectures + WORD COUNT TARGET 10K-20K + operational ≥85% target)
- Bundle 3 scope: **FIRST TASK** retroactive Bundle 1 supplement (~30 min), THEN Part 5 (3 bullets) + Part 8 (4 bullets)
- Required reading list (constitutional + Bundle 1+2 + Wave A + Wave B + Wave B Supplement library-direct)
- Wisdom Application Loop with OPERATIONAL/PHILOSOPHICAL discriminator (target ≥85% operational, given P5+P8 inherently operational)
- Quality bar (10K-20K words / anti-cargo-cult / A.14 edges / F-G-R DOGFOOD / fork-separation / Part 8 "specify and stub" scope-creep prevention / Part 5 standalone dissolve-test declaration)
- Verification gates M1/M2/M3/M4 with Bundle 3 scenarios (cycle compound lifecycle / health anomaly detection / quarterly immune audit TRADEOFF-01 verified / methodology promotion R2 closure)
- ETA + autocheck (3-6h estimate; Part 8 scope-creep autocheck; Part 5 dissolve-test autocheck; subagent stall fallback to direct-write)
- Output expected (2 architectures + Part 8 schemas + templates + UND-3 stub + AWAITING-APPROVAL packet)
- Branch/commit/operational
- STOP rule

Commit + push when done. STOP. Notify Ruslan.

---

*End of brief. Mantra: QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. SPECIFY-AND-STUB > LIVE-IMPLEMENTATION (Part 8). STANDALONE-PRESERVED > DISSOLVE (Part 5 — until evidence). RUSLAN-ACK > BRIGADIER-CONFIDENCE.*
