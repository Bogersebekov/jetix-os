---
title: Cloud Code Brief — Write the Wave C Bundle 4 deep prompt for ROY brigadier
date: 2026-04-28
type: meta-brief
target: Cloud Code on server (claude --dangerously-skip-permissions in tmux)
purpose: Server CC reads this brief + all context files, then writes full deep prompt for ROY brigadier to execute Wave C Bundle 4 (Parts 7 + 9 + 10 — Project Lifecycle + Owner Interaction + External Touchpoints) — FINAL Wave C bundle
output_required: prompts/wave-c-bundle-4-deep-prompt-2026-04-28.md (committed + pushed)
estimated_walltime: 30-60 min server CC work to write the deep prompt
critical_constraints:
  - DO NOT execute Wave C Bundle 4 itself — only write the prompt
  - This is the FINAL Wave C bundle — closure of all 10 Foundation parts
  - Apply established discipline: word count target 10K-20K (F8 LOCKED), operational ratio ≥85% target (Bundle 3 = 100%)
  - Bundle 4 has NO retroactive supplement (unlike Bundle 3) — clean substantive start
  - Three parts have OQ-MERGED-3 fork-separation FINAL CLOSURE — esp. Part 10 (highest creep risk)
---

# Cloud Code Brief — Write Wave C Bundle 4 Deep Prompt

## §0 What you (server CC) are doing

You are NOT executing Wave C Bundle 4. You are writing the **deep prompt** that ROY brigadier will execute later.

**Output: `prompts/wave-c-bundle-4-deep-prompt-2026-04-28.md`** — 600-900 lines, action-ready (Bundle 4 has 3 parts + 10 bullets — slightly larger than Bundle 3's 2 parts + 7 bullets).

Commit + push when done. STOP. Notify Ruslan via tmux output:
> «Wave C Bundle 4 deep prompt written at <path>. Lines: <N>. Ready for Ruslan review.»

---

## §1 Context — what's LOCKED, what's last

### **THIS IS THE FINAL BUNDLE OF WAVE C.** After Bundle 4 → Wave D integration pass → Wave E LOCKED tag.

### Bundles 1 + 2 + 3 LOCKED state on `claude/jolly-margulis-915d34` HEAD `8be5628`

**8/10 Foundation parts COMPLETED + LOCKED at F5:**
- Part 1 — System State Persistence (Bundle 1)
- Part 2 — Signal Ingestion & Triage (Bundle 2)
- Part 3 — KB & Methodology Library (Bundle 2)
- Part 4 — Role Taxonomy & Coordination Protocol (Bundle 2)
- Part 5 — Compound Learning & Methodology Capture (Bundle 3)
- Part 6a — Provenance Officer (Bundle 1)
- Part 6b — Human Gate (Bundle 1)
- Part 8 — Health Monitoring & System Integrity (Bundle 3)

### F8 constitutional schemas (CANNOT re-litigate)

| Artefact | Status | Bundle 4 consumption rule |
|---|---|---|
| `f-g-r.json` (Part 6a §I.1) | F8 LOCKED | All Bundle 4 emitted artefacts carry F-G-R |
| `awaiting-approval-packet.json` with `gate_class` (Part 6b §I.1) | F8 LOCKED | Part 7 stage-gate transitions emit `gate_class: stage_gate`. Part 9 strategic decisions `gate_class: stage_gate`. Part 10 external write-ack `gate_class: stage_gate` |
| `default-deny-table.yaml` (Part 6b §I.3) | F8 LOCKED | Novel action classes Default-Deny classified |
| `blast-radius-table.yaml` 4 tiers (Part 6b §I.4) | F8 LOCKED | Bundle 4 actions Tiered for HITL escalation |
| Halt-Log-Alert L9 (Part 6b §E) | F8 LOCKED | Failure modes conform |
| Corrigibility (Part 6b §E L9) | F8 LOCKED | Bundle 4 NEVER locks Ruslan out |
| WORD COUNT TARGET 10K-20K (Bundle 2 ack §3) | F8 LOCKED | Bundle 4 architectures conform |
| `task-return-packet.json` (Part 4 §I.1) | F4 → F5 (Bundle 3 Part 5 consumption validated) | Part 7 emit pattern conforms (UND-3 finalization) |
| Canonical health-signal schema (Part 8 §I.1, C2 resolved) | F5 | Bundle 4 emitter mapping (optional — OQ-B3-P8-1 deferred Wave D) |
| `wiki/methodology/` entity-type (Part 3) + admissibility predicate | F4 | Part 7 retrospective patterns may promote here |
| Message schema v2.0.0 with `acting_as:` mandatory | F4 | All Bundle 4 messages conform |

### Bundle 1+2+3 contracts Bundle 4 calls

- **Part 1 §H commit interface** — every Bundle 4 part canonical write
- **Part 6a `[src:filename]` enforcement** — citation discipline
- **Part 6a approval log** (`swarm/approvals/log.jsonl`) — promotion events
- **Part 6b stage-gate predicates** — Part 7 stage-gate transitions; Part 9 strategic ack; Part 10 external write-ack
- **Part 4 routing-table.yaml + task-return-packet.json** — Part 7 cycle dispatch + retrospective emit
- **Part 5 methodology promotion pipeline** (P5.2) — Part 7 retrospectives feed
- **Part 5 dissolve-test 3-cycle window** — Bundle 4 = SECOND of 3 cycles (after Bundle 3)
- **Part 8 SLI/SLO schema + alert-routing stub** — Bundle 4 emitters tie in
- **Part 3 `wiki/methodology/`** — Part 7 retrospective patterns consumed
- **PARA-tier mandatory** — Bundle 4 ingest entries conform
- **C1 `swarm/lib/`** — Bundle 4 may invoke accessor skills

### Bundle 4 OQ inputs (from prior Ruslan acks)

| OQ | Status | Bundle 4 implication |
|----|--------|----------------------|
| **OQ-MERGED-3** | Wave A scope (per Ruslan ack 2026-04-27) | Bundle 4 §X per part = FINAL CLOSURE of Foundation vs RUSLAN-LAYER fork-separation. Part 10 has highest creep risk (DACH ICP, German GDPR config) |
| **OQ-5** | P7 cadence event-driven (Ruslan ack) | Part 7 §E Laws declare event-driven, NOT cycle-boundary-gated |
| **OQ-MERGED-7** | U.System/U.Episteme declarations sufficient | Bundle 4 part-classifications: P7=U.System, P9=U.System, P10=U.System (CRM records dual: U.Episteme content + U.System pipeline) |
| **C3 contradiction** | Defer Phase B (LOW severity) | Part 10 declares Phase A inbound = Phase B work; current = owner-initiated only |
| **C4 contradiction** | Nomenclature fix `PhaseOf` → `methodologically-uses` (Part 9 → Part 6) | Bundle 4 Part 9 §D applies fix |
| **UND-3** | P5 → P7 retrospective input contract finalization | Part 7 §B Outputs FULLY SPECIFIES retrospective emit; Part 5 stub from Bundle 3 satisfied |
| **UND-5** | CRM edge validation in Bundle 4 (P10 work) | Part 10 §I declares CRM edge schema conforming to Part 3 wiki/graph/edges.jsonl |
| **OQ-B1-5** | D27 `approvals_reconciliation_strategy` field promotion to top-level | Part 10 §I.1 update of `cross-fork-provenance.json` (defer from Bundle 1) — RESOLVE here |
| **OQ-B1-6** | Rules 4 + 7 real-time encoding | Wave D capability gap — Bundle 4 may surface implementation pattern via Part 10 external action coordination |

### Word count target (F8 LOCKED)

- **Floor: 10K words**
- **Ceiling: 20K words**
- **Bias: operational content density over verbosity**

### Operational adoption ratio target

- ≥85% (Bundle 3 = 100%)
- Bundle 4 should match — Part 7 (state machines) + Part 9 (rituals) + Part 10 (CRM operations) inherently operational

---

## §2 Bundle 4 scope — Parts 7 + 9 + 10

### Part 7 — Project Lifecycle Substrate (3 bullets per wave-c-worklist §2 P7)

**Source:** wave-c-worklist §2 Part 7.

- **P7.1** — Canonical project schema YAML (`shared/schemas/project.json` or `.yaml`) — full state machine with 5 states (`scoped → staged → activated → under-review → closed | archived`), stage-gate predicates per Part 6b, appetite declarations (Shape Up — Singer 2019), scope records, resource tracking per project type
- **P7.2** — IP-5 past-participle exception whitelist (`decisions/policy/ip5-past-participle-whitelist.md`) — applied corrections (`active` → `activated`, `review` → `under-review`) declared canonical
- **P7.3** — Cadence alignment declaration — event-driven (NOT cycle-boundary-gated) per OQ-5 Ruslan ack; documented in §E Laws

**Special: UND-3 finalization (Part 7 ↔ Part 5 cross-bundle interface)**

Bundle 3 Part 5 set INPUT contract stub. Bundle 4 Part 7 finalizes EMIT pattern:
- Part 7 §B Outputs declares `project-retrospective-packet.json` schema (extends Part 4 `task-return-packet.json` superset)
- Part 7 §J Operational Rituals declares cadence: per project closure event + per cycle boundary
- Joint reference to Part 5 §A Inputs (cross-bundle coherence verified by M5-style coherence check, lite)

### Part 9 — Owner Interaction Scaffold (3 bullets per wave-c-worklist §2 P9)

**Source:** wave-c-worklist §2 Part 9.

- **P9.1** — Daily-log artefact schema (`shared/schemas/daily-log.json`) — frontmatter fields (date, projects-touched, decisions-made, ack-events) + content sections (morning intent, afternoon execution, evening reflection)
- **P9.2** — Weekly review artefact schema (`shared/schemas/weekly-review.json`) with **draft-disposition table** (C2 producer side) — categorizes accumulated drafts into accept/iterate/discard
- **P9.3** — 3-tier SLA taxonomy as canonical Foundation artefact (`.claude/config/sla-taxonomy.yaml`) — L1 strategic (Ruslan ack same-session), L2 tactical (batch ack weekly), L3 routine (auto-log)

**Special: IP-2 single-owner bounded context (CRITICAL)**

Per FUNDAMENTAL §2.6 + Bundle 1 RUSLAN-ACK: Part 9 = **single-owner Phase A scope**.
- §X Foundation vs RUSLAN-LAYER MUST declare: structural change ≥35% at >10× scale (per Ashby BOSC-A-T-X analysis Wave A); Phase B/C multi-owner = F.9 Bridge structural change required
- Phase B activation event = sustained partner onboarding signal (1 owner → 2+ owners)
- Multi-owner stub fields declared in §I (NOT implemented — Phase B work)

**Special: C4 nomenclature fix**

Wave A Part 9 §D used `PhaseOf Part 6` for governance gate dependency. Correct A.14 type = `methodologically-uses Part 6` (Part 9 USES gate as service, is NOT exclusive pre-gate phase). Bundle 4 Part 9 §D applies fix.

### Part 10 — External Touchpoints & Network Interface (4 bullets per wave-c-worklist §2 P10)

**Source:** wave-c-worklist §2 Part 10.

- **P10.1** — L.1-L.3 integration adapter stubs — read-only intelligence trackers (RT-1) + write-ack action coordinators (RT-2). Adapter pattern declared; Phase B implementation
- **P10.2** — C3 Phase-A boundary clarification — Part 10 inbound external = Phase B work; Phase A = owner-initiated only via Part 2 `/ingest`. Documented in §F Anti-scope
- **P10.3** — Privacy architecture declaration (`swarm/wiki/foundations/part-10-privacy-architecture.md` or §I sub-document) — FUNDAMENTAL §6.4 STRUCTURALLY enforced: consent, forget-request, encryption at rest, NO inference of protected characteristics (race / religion / political affiliation / health status)
- **P10.4** — OQ-MERGED-3 fork-separation checklist — **FINAL CLOSURE for Foundation**. Foundation = generic CRM pipeline + integration adapter pattern + privacy invariants. RUSLAN-LAYER = DACH ICP parameters, German GDPR config, specific contact lists, Linear/GitHub/etc auth tokens

**Special: OQ-B1-5 D27 reconciliation field promotion (deferred from Bundle 1)**

`cross-fork-provenance.json` (Part 1 §I.1 Bundle 1) currently has `approvals_reconciliation_strategy` in `metadata` open field. Bundle 4 Part 10 §I.1 promotes to top-level + documents reconciliation strategies per partner-fork import scenario (Phase B explicit).

**Special: CRM operational baseline (cycle 10)**

CRM is OPERATIONAL — 24 source files in `crm/`, 35 unit tests, 10 `/crm-*` skills, 4 YAML schemas in `crm/_schema/`, `crm/_scripts/crm.py`, `crm/_scripts/voice_router.py`, `crm/log.md`. Part 10 architecture **canonicalizes** this existing implementation (NOT redesigns) + declares Foundation-generic boundaries vs RUSLAN-LAYER ICP specifics.

### Cross-cuts within Bundle 4

| Cross-cut | Rule | Where applied |
|---|---|---|
| **F-G-R DOGFOOD** | Every claim per Part 6a F8 schema | §G tables; inline tags |
| **A.14 typed edges** | Bundle 1 canonical 10-edge table | §D Dependencies |
| **Append-only** | project-retrospective-packets, daily-logs, CRM event log — append-only | §C Side-effects |
| **L/A/D/E** | Per FPF A.6.B | §E Boundary |
| **Foundation vs RUSLAN-LAYER** | **FINAL CLOSURE** per OQ-MERGED-3 (Bundle 4 = last chance for declaration) | §X mandatory; Part 10 highest creep |
| **PARA-tier** | Daily-log entries / methodology promotions tagged | Part 9 §C |
| **Operational ≥85%** | Wisdom Loop OPERATIONAL/PHILOSOPHICAL discriminator | §M |
| **Word count 10K-20K** | F8 LOCKED constitutional | §6 Quality bar |
| **No Joint Design** | Unlike Bundle 2 (C1) — Bundle 4 has UND-3 lite (Part 7 ↔ Part 5 cross-bundle finalization) but no BLOCKING contradiction | §4 Phase architecture (skip Joint Design Phase) |

### Inter-Part references in Bundle 4 (lite coherence checks)

- **Part 7 ↔ Part 5** (UND-3 finalization) — Part 7 emit contract satisfies Part 5 input stub
- **Part 9 ↔ Part 6b** (C4 nomenclature fix) — `methodologically-uses` not `PhaseOf`
- **Part 9 ↔ Part 5** — Weekly review surfaces methodology promotion candidates from `agents/<id>/strategies.md`
- **Part 10 ↔ Part 3** (UND-5) — CRM edges to `wiki/graph/edges.jsonl` schema
- **Part 10 ↔ Part 1** (OQ-B1-5 D27) — `cross-fork-provenance.json` `approvals_reconciliation_strategy` field promotion
- **Part 10 ↔ Part 2** (C3 deferred Phase B) — inbound external = Phase B routing to Part 2

---

## §3 Required reading list for ROY brigadier

### A. Constitutional baseline

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (focus §2.6 daily ops; §3 SLI/SLO; §4.2-§4.3 human-only tasks + 3-tier SLA; §6.4 privacy hard rules)
2. `design/JETIX-FPF.md` (focus IP-2 bounded context; IP-5 past-participle states; IP-7 writing-as-thinking; A.6.B L/A/D/E; A.14 typed edges)
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (ESPECIALLY §6 CRM section — Part 10 baseline)
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (§4.5 deep-study constraint at 10K-20K)
5. **All 8 LOCKED architectures (Bundles 1+2+3) — constitutional inputs:**
   - Part 1 (esp. §H interfaces, §I.1 cross-fork-provenance.json — OQ-B1-5 promotion target)
   - Part 6a (F-G-R schema, approval log, quarterly audit)
   - Part 6b (gate predicates, default-deny, blast-radius, AWAITING-APPROVAL packet)
   - Part 2 (PARA-tier discipline, anchor-mandatory)
   - Part 3 (wiki/methodology/, accessor pipeline ownership)
   - Part 4 (routing-table.yaml, task-return-packet.json, executor-binding template)
   - Part 5 (compound ritual, methodology promotion pipeline, UND-3 input contract stub)
   - Part 8 (SLI/SLO schema, health-signal canonical, alert-routing stub)
6. **All RUSLAN-ACK records:**
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md`
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2026-04-28.md`
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-2-2026-04-28.md`
   - `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-3-2026-04-28.md`
7. Locks D17 (Notion read-only), D26 (hub-and-spoke), D27 (forkable + ICP external), D29 (Korp-Startup)

### B. Wave A artefacts

- MASTER-PLAN-DRAFT.md
- candidate-parts-merged.md (esp. §2 P7 + §2 P9 + §2 P10)
- dependency-graph.md (esp. P7→P5 retrospective; P9 SLA tiers; P10→P3 CRM edges)
- wave-c-worklist.md (esp. §2 P7 + §2 P9 + §2 P10 bullets)
- Wave A interface cards: part-7-project-lifecycle-substrate.md + part-9-owner-interaction-scaffold.md + part-10-external-touchpoints-network-interface.md

### C. Wave B consultant cards (per Manifest §2 matrix for P7+P9+P10)

**For Part 7:**
- `product-management-cagan-shape-up.md` (PRIMARY — Shape Up appetite-as-constraint, Outcome over Output, betting-table rhythm)
- `levenchuk-shsm-fpf.md` (IP-5 alpha state machine past-participle states, A.3 Transformer Quartet for transitions)
- `event-sourcing-cqrs.md` (project state transitions as events; Part 7 does NOT need full CQRS but events pattern applies)
- `stoic-epistemic.md` (Dichotomy-of-control: project scoped to what Ruslan controls; outcome not guaranteed)

**For Part 9:**
- `product-management-cagan-shape-up.md` (Torres CDH continuous discovery, weekly customer touchpoint slot; OKR cadence)
- `levenchuk-shsm-fpf.md` (IP-7 writing-as-thinking for strategic reflection; IP-2 bounded context for daily-log scope)
- `stoic-epistemic.md` (Naval specific knowledge filter; dichotomy-of-control)
- `sre-observability.md` (toil < 50% of owner time; alert delivery path)

**For Part 10:**
- `anthropic-constitutional-ai.md` (PRIMARY — privacy constraints; write-ack mandatory before external action; hardcoded never-list)
- `levenchuk-shsm-fpf.md` (IP-2 bounded context with explicit Bridge F.9; A.14 edges typed for CRM-to-wiki cross-refs)
- `mereology-typed-edges.md` (typed CRM graph edges per wiki/graph/edge-types.md; UND-5 binding)
- `knowledge-management-karpathy-luhmann-matuschak.md` (Forte PARA: contacts in Resource or Project tier, NOT KB concepts layer)
- `multi-agent-architecture.md` (A2A open question — MCP for tool invocation vs A2A for inter-agent delegation; OQ-CONFLICT-4 Phase B flag)

### D. Wave B Supplement library-direct sources (Bundle 4 critical)

1. `raw/books-md/anthropic/bai-2022-cai.md` — RLAIF for Part 10 external action self-critique pattern
2. `raw/books-md/anthropic/askell-2021-hhh.md` — corrigibility; Part 10 NEVER auto-acts on external surfaces without human-ack
3. `raw/books-md/event-sourcing/young-cqrs-2010.md` — project state transitions as events for Part 7
4. `raw/books-md/sre/google-sre-book.md` — Ch.6 monitoring (Part 9 health alerts to owner) + Ch.15 postmortems (Part 9 weekly review postmortem culture)
5. `raw/books-md/sre/google-srewb-implementing-slos.md` — burn-rate algebra for Part 9 SLA tiers (analogous)

### E. Existing operational artefacts (audit reference)

- **CRM TREE (Part 10 baseline — DO NOT REINVENT):**
  - `crm/` (24 source files)
  - `crm/_schema/` (4 YAML schemas)
  - `crm/_scripts/crm.py` + `voice_router.py`
  - `crm/log.md`
  - 10 `/crm-*` skills + 35 unit tests
- **Voice pipeline (Part 2 baseline already canonicalized in Bundle 2):**
  - `tools/transcribe.py` / `extract.py` / `filter.py` / `run_pipeline.sh`
- **Project artefacts (Part 7 baseline):**
  - `projects/` directory
  - `.claude/config/project-types.yaml`
  - `swarm/wiki/_templates/project-*/` (4 template trees)
  - `/project-bootstrap`, `/project-review`, `/project-archive`, `/project-de-morph`, `/project-promote` skills
- **Owner artefacts (Part 9 baseline):**
  - `daily-log/` directory (1 file currently)
  - `shared/state/kanban.json`
  - `/plan-day`, `/close-day` skills
  - `shared/state/priorities.json`

---

## §4 Wisdom Application Loop — Bundle 4 (preserve discipline)

**Same structure as Bundle 2/3** with OPERATIONAL/PHILOSOPHICAL discriminator.

**Bundle 4 expectations:**

- Operational ratio ≥85% (Bundle 3 = 100% — Bundle 4 should match)
- Cards covered: PM-Cagan-ShapeUp full mining for P7+P9; CAI full mining for P10 privacy; Mereology for P10 CRM edges (UND-5 binding); KM for P9 daily-log discipline
- Reject philosophical adoptions without Phase B/C-concrete-need or scope-creep-prevention justification

---

## §5 Quality bar

### Word count: 10K-20K per Part (F8 LOCKED)

- Part 7 architecture: 10K-20K
- Part 9 architecture: 10K-20K
- Part 10 architecture: 10K-20K (likely larger end given CRM baseline canonicalization + privacy architecture sub-section)

### Anti-cargo-cult enforcement

(Same.) Citation + concrete consequence sentence within 200 chars.

### Typed A.14 edges

Canonical 10-edge table from Bundle 1. NO `depends-on`. C4 fix applied (Part 9 → Part 6: `methodologically-uses`).

### F-G-R DOGFOOD per F8 schema

### Foundation vs RUSLAN-LAYER fork-separation — **FINAL CLOSURE**

**This is Bundle 4's most important quality bar — last chance to declare per OQ-MERGED-3 Wave A scope.**

For Part 7:
- Foundation generic: state machine 5 states, stage-gate predicates, appetite declarations Shape Up, scope record schema, resource tracking pattern
- RUSLAN-LAYER: 8 active project specifics (quick-money / research / brand / etc), specific appetite values, specific resource allocations

For Part 9:
- Foundation generic: daily-log/weekly-review/monthly-reflection schemas, attention-budget cap pattern (cap value generic param), 3-tier SLA structure
- RUSLAN-LAYER: specific attention budget value (20 active tasks), specific SLA times (L1=same-session, L2=weekly batch, L3=auto-log durations), Ruslan-specific Daily-log content patterns

For Part 10 (HIGHEST CREEP RISK):
- Foundation generic: CRM data model + edge types, integration adapter pattern, privacy invariants (FUNDAMENTAL §6.4), write-ack discipline
- RUSLAN-LAYER: DACH ICP parameters, German GDPR config, specific contact lists, Linear/GitHub/Notion auth tokens, specific intelligence tracker URLs

**§X separation MUST be explicit in each part. Critic gate auto-rejects ambiguous declarations.**

### Special: Part 7 cadence event-driven (OQ-5 ack)

Per Ruslan ack: P7 §E Laws declare event-driven, NOT cycle-boundary-gated. Avoid throughput bottlenecks.

### Special: Part 9 IP-2 single-owner bounded context

Multi-owner = Phase B F.9 Bridge structural change ≥35%. Bundle 4 Part 9 §X declares + multi-owner stub fields in §I (NOT implemented).

### Special: Part 10 privacy NOT behavioral

FUNDAMENTAL §6.4 privacy = STRUCTURAL invariants. Examples:
- Consent enforcement = schema field `consent_recorded_at: <timestamp>` mandatory before external action
- Forget-request = `/crm forget --contact <id>` skill purges record + propagates to all references
- Encryption at rest = Part 1 substrate level (file-system encryption assumption)
- NO inference of protected characteristics = lint signal `/lint --check-protected-inference` + Part 6b Default-Deny default for any classifier on race/religion/political/health

These are structural, not "we promise to be careful." Implementation = lint signals + schema fields + Default-Deny entries.

### Special: D27 reconciliation field promotion (OQ-B1-5)

Part 10 §I.1 updates Part 1 `cross-fork-provenance.json` schema:
- `approvals_reconciliation_strategy` promoted from `metadata` open field to top-level
- 3-5 reconciliation strategies declared (parent-wins / fork-wins / manual-merge / decline-import / etc)

This is RETROACTIVE Bundle 1 modification — handled via constitutional supplement record analogous to OQ-B2-A pattern (single commit at end of Bundle 4 cycle).

---

## §6 Verification gates

### M1 Smoke Test (per part, ≥90%)

Same 9 checks (with Bundle 4-specific):
- All §A-§N + §X populated
- Word count 10K-20K
- A.14 typed (with C4 Part 9 fix verified)
- F-G-R DOGFOOD
- Wave C bullets §L mapped
- §X **Foundation vs RUSLAN-LAYER FINAL CLOSURE** explicit (Bundle 4-specific stricter check — Part 10 esp.)
- No cargo-cult signals
- Bundle 4-specific: P7 cadence event-driven; P9 IP-2 multi-owner stub declared; P10 privacy structural; OQ-B1-5 D27 reconciliation promoted
- Inter-Part lite coherence: Part 7 emit ↔ Part 5 input; Part 10 CRM edges ↔ Part 3 schema

### M2 Cross-Reference (100%)

Spot-check 10+ critical citations including all Bundle 1+2+3 architectures + 5 Wave B cards per part + 5 supplement sources + ACK records.

### M3 Scenario Walkthroughs (4/4)

Bundle 4 scenarios:

1. **Project full lifecycle** — owner declares project → Part 7 stage-gate `scoped → staged` (appetite + scope record) → activated → execution cycles → under-review → closed → Part 7 emits retrospective packet → Part 5 consumes → methodology promotion. Tests P7/P5/P6b/P1.
2. **Daily-log + weekly review** — Part 9 morning intent → cycle dispatch via Part 4 → afternoon execution → evening reflection (committed) → Friday weekly review with draft-disposition table → Part 5 methodology candidate surfaced → Part 6b draft_promotion gate → wiki/methodology/. Tests P9/P5/P6b.
3. **External action with privacy** — Ruslan requests CRM contact outreach → Part 10 verifies `consent_recorded_at` present → blast-radius classify (Tier 1 strategic) → Part 6b stage_gate ack required → Ruslan ack → Part 10 dispatch external action via integration adapter (write-ack pattern) → log to CRM event log + approval log. Tests P10/P6b/P6a/P1.
4. **Fork-separation Phase B import** — partner forks Foundation → imports Part 10 generic CRM schema + integration adapter pattern + privacy invariants → declines RUSLAN-LAYER (DACH ICP / German GDPR config) → reconciliation_strategy declared (`fork-wins` for ICP-specific; `parent-wins` for privacy invariants) → cross-fork-provenance.json conforms with promoted top-level field. Tests P10/P1 + final fork-separation closure.

### M4 Wisdom Application Loop verification

(Same as Bundle 2/3.)
- Operational ratio ≥85% per part
- All Wave B consultants + supplement covered

### M5 Inter-Part lite coherence (Bundle 4-specific, lighter than Bundle 2 Joint Design)

- Part 7 §B emit contract satisfies Part 5 §A input stub (UND-3 finalization)
- Part 10 §I.1 D27 promotion verified consistent with Part 1 §I.1
- Part 9 §D `methodologically-uses Part 6` (C4 fix applied)

---

## §7 ETA + autocheck

**Walltime estimate: 4-7h ROY work** (Bundle 2 = 43min for 3 parts at 89% operational; Bundle 3 = 2h for 2 parts + supplement at 100% operational — Bundle 4 = 3 parts ~10 bullets, projected 1-3h likely at compound velocity).

**Autocheck rules:**
- If walltime exceeds 12h — STOP, report
- If Part 10 §X fork-separation ambiguous — re-dispatch with explicit DACH/GDPR examples
- If Part 9 omits IP-2 multi-owner stub — re-dispatch
- If Part 7 cadence not event-driven — re-dispatch (OQ-5 ack violation)
- If Wisdom Loop operational ratio <85% — investigate
- If brigadier subagents stall on stream watchdog — direct-write fallback acceptable (per Bundle 2/3 precedent)

---

## §8 Output expected from Bundle 4

### Per-part architecture documents

- `swarm/wiki/foundations/part-7-project-lifecycle-substrate/architecture.md` (10K-20K words)
- `swarm/wiki/foundations/part-9-owner-interaction-scaffold/architecture.md` (10K-20K words)
- `swarm/wiki/foundations/part-10-external-touchpoints-network-interface/architecture.md` (10K-20K words; likely larger end)

### Schemas

- `shared/schemas/project.json` (or `.yaml`) (P7.1)
- `shared/schemas/project-retrospective-packet.json` (P7 emit, UND-3 finalization — extends task-return-packet)
- `shared/schemas/daily-log.json` (P9.1)
- `shared/schemas/weekly-review.json` (P9.2)

### Configuration files

- `.claude/config/sla-taxonomy.yaml` (P9.3)
- `.claude/config/ip5-past-participle-whitelist.yaml` (P7.2)

### Privacy architecture (P10.3)

- `swarm/wiki/foundations/part-10-privacy-architecture.md` OR §I sub-section in main Part 10 architecture (brigadier decides; either acceptable)
- `/lint --check-protected-inference` skill spec (Phase B implementation)

### D27 promotion (OQ-B1-5)

- Updated `shared/schemas/cross-fork-provenance.json` (defined inline in Bundle 1 Part 1 §I.1; brigadier writes constitutional supplement record analogous to OQ-B2-A pattern)
- `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-supplement-2-2026-04-XX.md` (constitutional supplement record for D27 field promotion)

### Updated cross-references

- Wave A interface cards Parts 7/9/10 SUPERSEDED frontmatter
- Manifest §2 matrix Bundle 4 rows updated

### AWAITING-APPROVAL packet

- `decisions/AWAITING-APPROVAL-wave-c-bundle-4-2026-04-XX.md` (same structure)

### STOP

After AWAITING-APPROVAL packet — STOP. **Wave C is now COMPLETE.** Brigadier waits for Ruslan ack of Bundle 4 → next step = Wave D dispatch (separate cycle).

---

## §9 Branch + commit + operational

- Branch: `claude/jolly-margulis-915d34`
- Commit pattern: `[architecture] Bundle 4 — <part> — <phase>`
- Push after each major phase
- `unset ANTHROPIC_API_KEY` before claude
- `ulimit -n 65535`
- HD-02 N=2

---

## §10 What server CC does NOW

1. Read this brief fully
2. Read Bundle 3 deep prompt for structure reference
3. Read all 4 RUSLAN-ACK records + supplement record (Bundle 1 + 1-supplement + 2 + 3)
4. Read all 8 LOCKED architectures (constitutional inputs)
5. Read Wave A interface cards Parts 7 + 9 + 10
6. Read wave-c-worklist §2 P7 + §2 P9 + §2 P10
7. Read 4-5 Wave B consultant cards per part (PM/Levenchuk/Stoic/CAI/Mereology/KM/MultiAgent)
8. Read 5 Wave B Supplement library-direct sources
9. **Read AUDIT-CURRENT-STATE §6 CRM section** (Part 10 operational baseline — DO NOT REINVENT)
10. Skim Bundle 1 + 2 + 3 AWAITING-APPROVAL packets for output format

Then write `prompts/wave-c-bundle-4-deep-prompt-2026-04-28.md` (600-900 lines):

- Mission statement (Bundle 4 = FINAL Wave C bundle; closure of all 10 Foundation parts; consume 8 LOCKED architectures; treat with 1 trillion percent responsibility)
- Constitutional inputs (Bundle 1+2+3 LOCKED; F8 schemas; Word count 10K-20K F8; OQ inputs)
- Bundle 4 scope: Part 7 (3 bullets) + Part 9 (3 bullets) + Part 10 (4 bullets); UND-3 finalization (P7↔P5 lite); OQ-B1-5 D27 promotion (Part 10); CRM operational baseline canonicalization
- Required reading (constitutional + LOCKED architectures + ACK records + Wave A + Wave B + Supplement + AUDIT CRM)
- Wisdom Application Loop with OPERATIONAL/PHILOSOPHICAL (≥85% target)
- Quality bar (word count F8 / anti-cargo-cult / A.14 with C4 fix / F-G-R DOGFOOD / **§X FINAL CLOSURE fork-separation strict** / P7 event-driven / P9 IP-2 / P10 privacy structural / D27 promotion supplement)
- Verification gates M1/M2/M3/M4/M5 (Bundle 4 scenarios; M5 inter-Part lite coherence)
- ETA + autocheck (4-7h estimate; fork-separation autocheck; multi-owner stub autocheck; cadence event-driven autocheck)
- Output expected (3 architectures + 4 schemas + 2 configs + privacy doc + D27 supplement + AWAITING-APPROVAL)
- Branch/commit/operational
- STOP rule (Wave C COMPLETE on Ruslan ack)

Commit + push when done. STOP. Notify Ruslan.

---

*End of brief. Mantra: QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. FINAL-CLOSURE-FORK-SEPARATION (Part 10 esp). EVENT-DRIVEN (Part 7). SINGLE-OWNER-BOUNDED (Part 9). PRIVACY-STRUCTURAL (Part 10). RUSLAN-ACK > BRIGADIER-CONFIDENCE. **THIS IS WAVE C CLOSURE.***
