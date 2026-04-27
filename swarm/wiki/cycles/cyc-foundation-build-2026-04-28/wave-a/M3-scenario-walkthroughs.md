---
title: M3 Scenario Walkthroughs — 4 use cases traced through Foundation graph
date: 2026-04-27
phase: A-5-M3
expert: mgmt-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
gate_threshold: 4/4 scenarios PASS
gate_verdict: PASS — 4/4 scenarios complete end-to-end; gaps documented below do not block completion
F: F4
ClaimScope: "Holds for the 10-part Foundation decomposition as specified in Wave-A interface cards. Gaps identified are Wave C materialisation items, not scenario blockers — unless noted HARD GAP."
R:
  refuted_if: "Any of the 4 scenarios is demonstrated to be technically uncompletable even with Wave C work — i.e., a structural impossibility, not a missing schema field"
  accepted_if: "Wave C Bundle 1+2 completion does not produce contradictions with the traces below; and no HARD GAP (structural blockage) is discovered in Bundle 1 build cycle"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-2-signal-ingestion-triage.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-3-knowledge-base-methodology-library.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-4-role-taxonomy-coordination-protocol.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-5-compound-learning-methodology-capture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-9-owner-interaction-scaffold.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/MANIFEST-DRAFT.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/multi-agent-architecture.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md
---

# M3 Scenario Walkthroughs

> **Purpose.** Trace 4 representative use cases end-to-end through the proposed
> 10-part Foundation graph. Per scenario: parts traversed in sequence, file-level
> side-effects, gate events, citation to the relevant interface card section. Gaps
> recorded honestly; PASS/FAIL declared per scenario using the rule: FAIL only if
> the scenario cannot complete even with Wave C work done — structural impossibility,
> not missing schema.

---

## Scenario 1 — Information Lifecycle

**Use case.** Owner records a voice memo during a walk (a random thought about consulting
pricing strategy). Three days later, owner asks `/ask "what did I think about pricing
strategy recently?"` and gets a response citing the original memo.

---

### Trace

**Step 1 — Owner action: voice memo dropped**

- File created: `inbox/audio_NNN.ogg`
- Event trigger: file-create in `inbox/`
- Part traversed: **Part 2 (Signal Ingestion & Triage)** — boundary permeable for owner-supplied
  raw signals per Part 2 §A Inputs.
- [src:part-2-signal-ingestion-triage.md:§A]

**Step 2 — Pipeline execution (Part 2 internal)**

- `tools/transcribe.py` → transcript at `raw/transcripts/<slug>.md`
- `tools/extract.py` → structured items extracted
- `tools/filter.py` → dedup + meta-analysis
- `tools/review_report.py` → `reports/review_YYYY-MM-DD.md` + `~/review-latest.md`
- Each stage produces a committed file through **Part 1 (System State Persistence)**:
  `[ingest] transcribe audio_NNN` commit with format per D25.
- Part 2 §C Side-effects: "transcript write: `raw/transcripts/<slug>.md` — committed
  via Part 1 at transcription stage."
- Part 2 §E Laws: "every pipeline stage output is a committed file; no ephemeral-only
  processing."
- AUDIT: `tools/transcribe.py, extract.py, filter.py, run_pipeline.sh` are operational
  (AUDIT artefact confirmed in MASTER-PLAN §6.4 P2 row).
- [src:part-2-signal-ingestion-triage.md:§C; part-1-system-state-persistence.md:§B;
  MASTER-PLAN-DRAFT.md:§6.4 Part 2]

**Step 3 — STOP gate (Part 2 + Part 6 interaction)**

- `reports/review_YYYY-MM-DD.md` committed; owner reads `~/review-latest.md`.
- **STOP gate is STRUCTURAL** — Part 2 §E Laws: "no draft candidate reaches `wiki/`
  without a human-ack timestamp."
- This instantiates Part 6's (Governance) J-Approve decision class. Part 2 §D:
  "`methodologically-uses Part 6` — the STOP gate is an instance of Part 6's HITL
  escalation discipline."
- Owner decides which items to ingest. Items not selected: stay in `raw/` only.
  Items selected: owner runs `/ingest --anchor=consulting-pricing`.
- **GAP-S1-A** (non-blocking, Wave C item): the STOP gate packet does not yet carry
  a `gate_class: stop_gate` field (UND-4, MASTER-PLAN §5.2); the human ack timestamp
  field `human_acked_at:` is specified but not yet schema-enforced at the ingest
  boundary. Wave C Bundle 2 Part 2 work item.
- [src:part-2-signal-ingestion-triage.md:§C, §D, §E;
  part-6-governance-provenance-human-gate.md:§A]

**Step 4 — Ingest and anchor (Part 2 output → Part 3 input)**

- D28 anchor is MANDATORY: `--anchor=consulting-pricing` parameter validated
  non-null at ingest boundary. Without it, pipeline rejects with stderr error per
  Part 2 §E Laws.
- PARA-tier tag written (`para_tier: Project`) to draft frontmatter at triage stage.
- Draft candidate `inbox/<slug>-DRAFT.md` committed via Part 1.
- **GAP-S1-B** (non-blocking): PARA-tier enforcement is specified (Part 2 §C Side-effects
  and §E Deontics) but not yet a lint-enforced check at ingest boundary today. Wave C
  Bundle 2 work item.
- [src:part-2-signal-ingestion-triage.md:§A Inputs D28 anchor; §C PARA-tier tag;
  MASTER-PLAN-DRAFT.md:§6.4 P2 gap row]

**Step 5 — Promotion to KB (Part 3)**

- Part 2 §B Outputs: "promoted draft candidate (.md with anchor, PARA-tier tag,
  `human_acked_at:` frontmatter, `sources:` provenance block) passed to Part 3."
- Part 3 §E Admissibility: "source must be a Part 2 promoted draft with
  `human_acked_at:` populated."
- **Part 3 (Knowledge Base & Methodology Library)** receives the draft:
  - Entity file written: `wiki/concepts/<slug>.md` with YAML frontmatter
    (`pipeline: ingested`, `F: F2`, `ClaimScope:`, `R:`, `sources:`).
  - Graph edge appended: `wiki/graph/edges.jsonl` — typed A.14 edge (e.g.,
    `PhaseOf information-lifecycle` link to source).
  - Index updated: `wiki/index.md` entry appended.
  - Log appended: `wiki/log.md` — new entry at top (append-only per CLAUDE.md).
- All writes routed through **Part 1** (git commit: `[wiki] add concept consulting-pricing-NNN`).
- Part 3 §E Laws: "every entity in `wiki/` carries YAML frontmatter with: `pipeline:`
  stage, at least one `sources:` entry, F-G-R fields, and a typed A.14 edge in
  `wiki/graph/edges.jsonl`."
- [src:part-3-knowledge-base-methodology-library.md:§C, §E;
  part-1-system-state-persistence.md:§B]

**Step 6 — Three days later: retrieval via /ask (Part 3 + Part 9)**

- Owner asks: `/ask "what did I think about consulting pricing strategy recently?"`
- **Part 3** accessor service (`/ask`) queries `wiki/index.md`, matches anchor
  `consulting-pricing`, retrieves the entity file, and returns synthesis with inline
  citations: `[src:wiki/concepts/<slug>.md:§body]`.
- The entity file's `sources:` frontmatter carries the raw transcript path
  `raw/transcripts/<slug>.md`, which in turn references `inbox/audio_NNN.ogg`.
  Citation chain reconstructs back to original memo.
- Part 3 §E Deontics: "this part MUST answer queries via `/ask` with inline citations
  (`[src:path:section]`) — no synthesis without citation."
- **Part 9 (Owner Interaction Scaffold)** context: the query is owner-initiated from
  the daily working page; response is surfaced in the owner's interaction layer.
  Part 9 §A Inputs includes "agent drafts from all other parts."
- **GAP-S1-C** (non-blocking): `/ask --save` default (filing synthesis to
  `wiki/comparisons/`) is specified (Part 3 §E Deontics) but the `--no-save`
  explicit-override is not yet enforced; the default-save behaviour is Wave C
  materialisation item. Does not block query response.
- Accessor pipeline ownership (C1 contradiction): Part 3 §D notes the pipeline
  (`/ask`, `/ingest` etc.) is "owned by Part 4 or shared infrastructure" but Part 4
  interface card does not explicitly accept ownership. This is Contradiction C1
  (BLOCKING for Wave C, MASTER-PLAN §3.4). At Phase A this does not block scenario
  completion — the skills work operationally today. It becomes a structural block in
  Wave C Bundle 2.
- [src:part-3-knowledge-base-methodology-library.md:§B, §E Deontics;
  part-9-owner-interaction-scaffold.md:§A; MASTER-PLAN-DRAFT.md:§3.4 C1]

**Step 7 — Governance audit trail (Part 6 + Part 1)**

- The promotion event at Step 5 generates an audit-log entry in Part 6's approval-log
  (committed via Part 1): artifact path, gate timestamp, human-ack timestamp.
- F-G-R compliance: the promoted entity carries `F: F2` (single-cycle observation,
  AI-extracted, human-acked). Part 6 §E Laws: "every canonical artifact MUST carry
  F-G-R frontmatter fields."
- [src:part-6-governance-provenance-human-gate.md:§B, §C, §E]

### Gaps identified

| Gap ID | Description | Severity | Wave C fix |
|--------|-------------|----------|------------|
| GAP-S1-A | STOP gate packet lacks `gate_class: stop_gate` field (UND-4); `human_acked_at:` not schema-enforced at ingest boundary | Non-blocking today | Bundle 2 Part 2 Bullet 1 |
| GAP-S1-B | PARA-tier enforcement not yet a lint-checked gate; specified but not enforced | Non-blocking today | Bundle 2 Part 2 Bullet 2 |
| GAP-S1-C | `/ask --save` default to `wiki/comparisons/` not yet enforced; manual only | Non-blocking today | Bundle 2 Part 3 Bullet 4 |
| GAP-S1-D | C1 accessor pipeline ownership (Part 3 vs Part 4 vs shared infra) — BLOCKING for Wave C design, not for Phase A operations | BLOCKING for Wave C only | Bundle 2 joint Part 3+4 |

### Verdict: PASS

**Reasoning.** The scenario completes end-to-end today with operational tooling:
voice pipeline (`transcribe.py → extract.py → filter.py`) is live; `/ingest` skill
works; `wiki/` has 552 entities retrievable via `/ask`. The STOP gate is structurally
present (human reads `~/review-latest.md` before any `/ingest` call). The citation
chain back to the original memo exists through the `sources:` frontmatter chain. Gaps
are schema-enforcement and ownership-declaration issues, not structural impossibilities.
The scenario cannot fail even without Wave C work — it just runs with weaker schema
guarantees. [src:MASTER-PLAN-DRAFT.md:§6.4 P2 AUDIT artefacts; P3 AUDIT artefacts]

---

## Scenario 2 — Strategic Management

**Use case.** Owner makes a decision (e.g., "focus Quick-Money on DACH manufacturing
sector only for Q2"). Decision is recorded. One month later, a strategic doc references
it. Six months later, an anti-recurrence check verifies the rationale hasn't been
silently reversed.

---

### Trace

**Step 1 — Decision made and recorded (Part 9 + Part 6 + Part 1)**

- Owner in daily working page (`daily-log/YYYY-MM-DD.md`) notes the decision.
- **Part 9 (Owner Interaction Scaffold)** §E Laws: "IP-7 writing-as-thinking
  asymmetry: owner authors strategic and reflective content."
- This decision is a strategic commitment — Part 9 §B Outputs: "promoted canonical
  artefacts forwarded to Part 6 (Governance) for gate processing."
- SLA classification applied: this is an L1 or L2 item (external scope commitment /
  Lock-adjacent). Part 9 §E Laws: "L1 items gated within same session (FUNDAMENTAL
  §4.2 L1 SLA: immediate)."
- **Part 6 (Governance & Human Gate)** receives promotion request:
  - AWAITING-APPROVAL packet written: `swarm/awaiting-approval/<cycle>-decision-quick-money-dach-focus.md`
  - Owner acks (self-ack — in solo-owner system, Ruslan is both the decision-maker
    and the approver).
  - LOCKED tag applied; decision promoted to `decisions/JETIX-DECISION-DACH-FOCUS-2026-05.md`
    (canonical decisions/ path).
  - Approval-log entry committed (append-only) via **Part 1**.
- Part 6 §C Side-effects: "writes LOCKED canonical decision (D-series) — canonical
  decisions after human ack."
- Part 6 §E Laws: "human ack is the TERMINAL decision point for every canonical
  promotion."
- [src:part-9-owner-interaction-scaffold.md:§B, §E;
  part-6-governance-provenance-human-gate.md:§B, §C, §E;
  part-1-system-state-persistence.md:§B]

**Step 2 — Decision enters UC-A.4 tracking (Part 9 + Part 3)**

- The LOCKED decision file at `decisions/` is the canonical record.
- Part 9 weekly review (next weekly review artefact `decisions/weekly/YYYY-WNN-review.md`)
  references the decision: "Decision DACH-FOCUS made; owner confirmed rationale; no
  contradicting signals."
- **Part 3 (KB)** may optionally ingest the decision as a KB entry if it contains
  reusable strategic knowledge (e.g., `wiki/claims/dach-manufacturing-focus-rationale.md`).
  This is owner-discretionary — the decision file itself is the authoritative record.
- **GAP-S2-A** (non-blocking): the UC-A.4 tracking mechanism ("next month's strategic
  doc references it") is specified through Part 9's weekly review schema, but the
  weekly review artefact schema is not yet a canonical Foundation artefact (Wave C
  Part 9 Bullet 2). The schema exists behaviourally today (`decisions/weekly/`
  directory exists) but field-level structure is informal.
- [src:part-9-owner-interaction-scaffold.md:§B Outputs;
  MASTER-PLAN-DRAFT.md:§6.4 P9 gap row]

**Step 3 — One month later: strategic doc references decision (Part 9 + Part 5 + Part 3)**

- Owner produces a strategic document (e.g., Q2 consulting-direction memo) during the
  monthly review. **Part 9** §B Outputs: "Monthly reflection artefact
  `decisions/monthly/<YYYY-MM>-reflection.md` — strategic document synthesis."
- IP-7 discipline: owner authors; agents produce structured extractions only.
  `[src:part-5-compound-learning-methodology-capture.md:§E Laws]`
- The monthly reflection cites the LOCKED decision file:
  `[src:decisions/JETIX-DECISION-DACH-FOCUS-2026-05.md]`
- This is a provenance link — the decision is the upstream canonical source.
- **Part 5 (Compound Learning)** at compound phase may extract a DRR entry:
  "Decision: focus DACH manufacturing. Reasoning: competitive moat hypothesis.
  Result: TBD at cycle close. Review: Q3 2026."
  The DRR entry is committed to `agents/mgmt-expert/strategies.md` via Part 1.
- [src:part-5-compound-learning-methodology-capture.md:§B Outputs;
  part-9-owner-interaction-scaffold.md:§B; part-1-system-state-persistence.md:§B]

**Step 4 — Six months later: anti-recurrence check (Part 6 + Part 8 + Part 5)**

- **Part 8 (Health Monitoring)** — the anti-recurrence check is an instance of the
  quarterly immune audit function (IP-4). MASTER-PLAN §1 Part 8: "methodology-
  freshness tracking, and periodic self-preservation integrity checks."
- Part 6 §E Laws: "IP-1 enforcement is a Part 6 quarterly audit function" — the audit
  asks: has this decision been silently reversed or contradicted by a newer decision
  without explicit gate?
- Mechanism: Part 6's periodic audit (constrained by Part 8 signals) scans `decisions/`
  for contradictions. If newer decision contradicts the DACH-focus lock without an
  explicit supersession gate, this fires as a constitutional-violation signal.
- **Part 5** DRR entry from Step 3 carries `Review: Q3 2026` — the review date triggers
  the compound-phase retrospective to re-evaluate the decision rationale.
- The anti-recurrence check "passes" if: (a) no contradicting decision is present in
  `decisions/` without explicit supersession; (b) the DRR entry review date is reached
  and the entry is updated (not silently expired).
- **HARD GAP — S2-B** (BLOCKED on TRADEOFF-01): Part 8's SLI/SLO schema, the weekly
  health dashboard, and the quarterly immune audit are ALL Wave C work items — and they
  are BLOCKED on TRADEOFF-01 (VSM S3 authority designation between Parts 6 and 8,
  MASTER-PLAN §5.1 OQ-1). Today there is no systematic Part 8 anomaly-detection
  mechanism (`shared/state/system-health.json` "reports all green — no computation
  mechanism" per MASTER-PLAN §6.4 P8 AUDIT artefact row). The anti-recurrence check
  is currently manual — owner must remember to revisit the decision.
- However: the LOCKED decision file in `decisions/` is permanent (append-only; git
  commits are the anti-recurrence mechanism). A manual grep `git log --oneline decisions/`
  suffices to verify no contradicting lock. This is an F3-level (informal, manual)
  anti-recurrence mechanism, not the F5-level automated mechanism Wave C targets.
- [src:MASTER-PLAN-DRAFT.md:§6.4 P8 AUDIT artefacts; §5.1 OQ-1 TRADEOFF-01;
  part-6-governance-provenance-human-gate.md:§E Laws IP-1;
  part-5-compound-learning-methodology-capture.md:§B Outputs; §E Laws]

### Gaps identified

| Gap ID | Description | Severity | Wave C fix |
|--------|-------------|----------|------------|
| GAP-S2-A | Weekly review artefact schema not yet canonical Foundation artefact; structure informal | Non-blocking | Bundle 4 Part 9 Bullet 2 |
| GAP-S2-B | Part 8 automated anti-recurrence / methodology-freshness check absent; quarterly immune audit not implemented; BLOCKED on TRADEOFF-01 | HARD GAP — scenario step 4 runs at F3 (manual) not F5 (automated) | Bundle 3 Part 8 (ALL bullets BLOCKED on TRADEOFF-01 Ruslan ack) |
| GAP-S2-C | DRR review-date enforcement: no automated trigger fires the review at the declared `Review: Q3 2026` date; owner must track manually | Non-blocking | Bundle 3 Part 5 Bullet 1 (compound ritual as canonical Foundation artefact) |

### Verdict: PASS (with degraded automation on Step 4)

**Reasoning.** Steps 1-3 complete fully: decision is LOCKED in `decisions/` (AUDIT
confirms 29 D-Locks already operational); strategic doc references it via provenance
link; DRR entry is committed to strategies.md. Step 4 (anti-recurrence) completes at
F3/manual level today — `git log decisions/` + owner review is a real mechanism, just
not automated. This is explicitly below the Wave C target (automated health monitoring)
but not a structural impossibility. TRADEOFF-01 blocks automation but not the capability.
Scenario is PASS because the use case "is the rationale still intact six months later?"
has a verifiable answer via git history at any time. [src:MASTER-PLAN-DRAFT.md:§6.4 P6
AUDIT artefacts — 8 confirmed gate documents, D1-D29 LOCKED decisions; P5 — strategies.md
8 files, 19 strategy entries]

---

## Scenario 3 — Agent Swarm Operations

**Use case.** Brigadier dispatches 3-expert review (engineering, mgmt, philosophy) on
the same delivery-plan draft. Each expert returns a structured packet. Brigadier runs
the provenance gate. Canonical promotion occurs.

---

### Trace

**Step 1 — Brief preparation and dispatch (Part 4 + Part 1)**

- Brigadier has a delivery-plan draft at `swarm/wiki/drafts/<task-id>-draft-delivery-plan.md`
  (produced in a prior cell).
- **Part 4 (Role Taxonomy & Coordination Protocol)** dispatches 3 Task() invocations:
  - `mode: critic` to engineering-expert, mgmt-expert, philosophy-expert
  - Each brief carries: `task_id`, `mode: critic`, `inputs[]` (disk paths only,
    not inlined bodies per AP-1), `acceptance_predicate` (Hamel-binary), `ap_budget`.
  - `acting_as:` field mandatory in every message (Part 4 §E Laws: FUNDAMENTAL §3.2.4).
  - Dispatch is hub-and-spoke: brigadier dispatches all three; experts do not communicate
    peer-to-peer. Part 4 §F Anti-scope: "does NOT allow agents to negotiate contradictions
    autonomously."
- Dispatch event commits to `comms/mailboxes/<role>.jsonl` (append via Part 1).
- [src:part-4-role-taxonomy-coordination-protocol.md:§A, §B, §C, §E;
  multi-agent-architecture-consultant:§P-2 hub-and-spoke enforcement]

**Step 2 — Each expert runs critic mode and returns structured packet (Part 4 + Part 6)**

- Each expert reads: their own system.md + shared-protocols.md + strategies.md +
  the brief's named input paths (file-reference only).
- Each expert returns YAML packet: `summary`, `proposed_writes[]`, `provenance[]`,
  `confidence`, `escalations[]`, `dissents[]`.
- Packets are COMPRESSED (not raw traces) per context budget discipline.
  [src:multi-agent-architecture-consultant:§P-3 context budget; §Conflict-2 resolution]
- **Part 4** §B Outputs: dispatch packets returned to brigadier mailbox.
- Side-effect: cycle-event entry produced for **Part 5** (compound learning DRR extraction).
  Part 4 §B: "DRR coordination patterns from cycle retrospective — structured extraction."
- [src:part-4-role-taxonomy-coordination-protocol.md:§B; part-5-compound-learning-methodology-capture.md:§A]

**Step 3 — Brigadier collects and runs provenance gate check (Part 6)**

- Brigadier runs the provenance gate (shared-protocols §2 / §5.5.5) on each returned
  packet:
  - `proposed_writes[]` non-empty: checked.
  - `provenance[]` non-empty with inline `[src:...]` citations: checked.
  - F-G-R frontmatter fields present on the draft: checked.
  - Acceptance predicate is Hamel-binary (not prose): checked.
- **Part 6 (Governance & Human Gate)** §E Admissibility: "Draft artifact is accepted
  into gate review only if: (a) `proposed_writes[]` non-empty, (b) `provenance[]`
  non-empty with inline `[src:...]` citations, (c) F-G-R frontmatter fields present,
  (d) acceptance predicate is Hamel-binary."
- Dissents from experts are preserved (not averaged). Per shared-protocols §3 and
  Part 6 §E Laws: contradicting claims must surface in `dissents[]` with (F, ClaimScope, R).
- **GAP-S3-A** (non-blocking): F-G-R compliance enforcement is NOT yet a systematic
  Part 6-owned automated function. Current state: F-G-R tags exist on some artefacts
  but no automated scan + exception-to-HITL routing exists. Part 6 §H Wave C primary
  gap: "build F-G-R compliance checker as a Part 6 service." Wave C Bundle 1 (Bullet 2
  in Part 6 partial work) addresses this.
- [src:part-6-governance-provenance-human-gate.md:§E Admissibility, §H;
  MASTER-PLAN-DRAFT.md:§6.4 P6 gap row]

**Step 4 — Integration of 3 expert returns (Part 5 + Part 3 + Part 6)**

- Brigadier runs integrator-mode synthesis (or dispatches mgmt-expert in integrator mode)
  on the 3 critic packets.
- Dissents preserved: engineering-expert dissent on timeline vs mgmt-expert dissent on
  delivery-commitment both surfaced with (F, ClaimScope, R) in the integrated draft.
  Per shared-protocols §3 AP-6 prevention.
- Integrated draft written to `swarm/wiki/drafts/<task-id>-integrated-delivery-plan.md`
  via **Part 1**.
- **GAP-S3-B** (non-blocking): the routing table as declarative YAML (`swarm/lib/routing-table.yaml`)
  does not yet exist — currently embedded in brigadier system prompt. Part 4 §H Wave C
  note: "Primary materialisation gap is the routing table as declarative YAML artifact."
  Today brigadier dispatches by ad-hoc reading of its own system prompt rules. This
  works operationally but is not auditable as a standalone Foundation artefact.
  [src:part-4-role-taxonomy-coordination-protocol.md:§C Side-effects; §H]

**Step 5 — AWAITING-APPROVAL gate and canonical promotion (Part 6 + Part 1 + Part 3)**

- Integrated draft submitted to **Part 6** human gate.
- AWAITING-APPROVAL packet written: `swarm/awaiting-approval/<cycle>-delivery-plan.md`
- Owner (Ruslan) reviews and acks: `state: acked` in the gate document frontmatter.
- **Part 6** applies LOCKED tag; canonical write executed via **Part 1**
  (git commit: `[wiki] promote delivery-plan <task-id>`).
- If the artefact is a wiki entity, it transitions in **Part 3** (`pipeline: ready`).
  Typed edge appended to `wiki/graph/edges.jsonl`.
- Approval-log entry committed (append-only) via Part 1.
- Part 6 §C Side-effects: "writes approval-log entry (append-only)."
- Part 6 §E Deontics: "Part 6 MUST NOT make canonical promotion decisions autonomously
  — human ack is architecturally mandatory." [src:anthropic-constitutional-ai.md:§4 P6]
- [src:part-6-governance-provenance-human-gate.md:§B, §C;
  part-1-system-state-persistence.md:§C;
  part-3-knowledge-base-methodology-library.md:§C]

**Step 6 — Compound phase update (Part 5)**

- At cycle close, **Part 5** compound phase extracts DRR entries from the 3-expert
  review cycle events (received from Part 4 at Step 2).
- DRR entries appended to per-role `agents/*/strategies.md` files via Part 1.
- Health metric `compound-application-rate` updated in `swarm/wiki/meta/health.md`.
- Part 5 §C Side-effects: "writes to `agents/<role>/strategies.md` — append-only DRR
  entries; no in-place edits of prior entries."
- [src:part-5-compound-learning-methodology-capture.md:§B, §C]

### Gaps identified

| Gap ID | Description | Severity | Wave C fix |
|--------|-------------|----------|------------|
| GAP-S3-A | F-G-R compliance scanner not yet implemented as Part 6 automated service; manual inspection only | Non-blocking | Bundle 1+3 Part 6 Bullets 1, 3 |
| GAP-S3-B | Routing table not yet a declarative YAML artefact (`swarm/lib/routing-table.yaml`); embedded in brigadier system prompt | Non-blocking today (works behaviourally) | Bundle 2 Part 4 Bullet 1 |
| GAP-S3-C | Dissent preservation enforcement: no automated check that `dissents[]` is non-empty when ≥2 inputs disagreed; relies on expert discipline | Non-blocking | Bundle 2 Part 4 Bullet 1 (routing table schema) + Part 5 |
| GAP-S3-D | Handshake schema for Task() dispatch (task_dispatched → task_received_ack → packet_returned) does not exist; long-horizon tasks have no mid-flight observability | Phase B risk, non-blocking Phase A | Bundle 2 Part 4 (OQ-Conflict#4 / A2A schema slot) |

### Verdict: PASS

**Reasoning.** All 5 operational steps complete today: brigadier dispatches via Task();
experts return structured YAML packets; provenance gate runs via shared-protocols §2;
AWAITING-APPROVAL gate mechanism is operational (AUDIT: 8 confirmed gate documents);
canonical promotion via git commit is live. The 4 gaps are schema-enforcement gaps
and declarative-YAML materialisation items — not structural impossibilities. The
3-expert review cycle has run successfully across Cycles 1-11 already. [src:MASTER-PLAN-DRAFT.md:
§6.4 P4 AUDIT artefacts — brigadier.md + 5 expert .md files; comms/mailboxes (13 channels);
shared-protocols.md operational; P6 — 8 confirmed gate documents]

---

## Scenario W — Wave-B Consultant Invocation (Scenario W)

**Use case.** Wave C task: "design agent communication protocol" (Part 4 interface card,
Bundle 2). Which consultants are invoked? What principles applied? Where do they conflict?

---

### Trace

**Step 1 — Wave C author identifies relevant consultants (Part 4 + MANIFEST-DRAFT §2)**

The Wave C author for Part 4 (Role Taxonomy & Coordination Protocol) consults the
MANIFEST-DRAFT §2 matrix:

Part 4 primary anchor frameworks: **#1 Левенчук ШСМ + FPF** (IP-1 Role≠Executor,
IP-8 F.6 onboarding, L/A/D/E for interfaces) + **#3 Multi-Agent Architecture**
(hub-and-spoke P-2, verification architecture P-5, MAST coverage).

Secondary: **#13 Constitutional AI** (hard-rule anti-scope §6.1, simplicity-transparency-trust),
**#14 Mereology** (typed edges for role dependencies), **#2 Systems thinking**
(Ashby requisite variety: brigadier routing variety ≥ task-type variety).

From MANIFEST-DRAFT §2 Part 4 row:
- "Tradeoffs to surface: TRADEOFF-02: Ashby requisite variety vs Anthropic context-
  engineering simplicity — resolution: variety lives in routing YAML, not prompt prose."
- "CrewAI personification vs IP-1 — FPF wins."
[src:MANIFEST-DRAFT.md:§2 Part 4 row]

**Step 2 — Consultant #1 (Левенчук) invoked for IP-1 and interface structure**

Principles applied:

**P1 — Role ≠ Executor (IP-1).** Every role-manifest is U.Episteme (passive archetype);
every agent binding is a separate `executor-binding.yaml` (U.System). Concrete consequence
for Part 4 design: no executor name (e.g., "claude-sonnet-4-6", "brigadier") appears
as a Foundation Part 4 constituent. Routing table YAML names roles, not executor
instances. Detection mechanism: AP-L2 (search role.md Block 1 `role_name` for
model-specific strings; any match = violation). [src:levenchuk-shsm-fpf.md:§4 P1;
part-4-role-taxonomy-coordination-protocol.md:§E Laws IP-1]

**P6 — L/A/D/E boundary norm square (A.6.B).** The Part 4 → Part 5 interface
(cycle events feeding DRR) MUST be described in L/A/D/E lanes. L-lane: what constitutes
a valid cycle-event packet (DRR precursor). A-lane: acceptance criteria (must carry
`task_id`, `acting_as:`, `outcome:`). D-lane: Part 4's obligation to emit a cycle-event
per dispatched task at completion. E-lane: DRR entry appears in `agents/<role>/strategies.md`
at next compound phase.
[src:levenchuk-shsm-fpf.md:§4 P6; MANIFEST-DRAFT.md:§2 Part 4 cell]

**P7 — F.6 six-step agent onboarding (IP-8).** Every `executor-binding.yaml` carries
M1-M6 onboarding block. Concrete consequence for protocol design: the routing table
must reference the F.6 evidence shape (M5) for each role to confirm the executor was
properly onboarded before receiving dispatches.
[src:levenchuk-shsm-fpf.md:§4 P7; part-4-role-taxonomy-coordination-protocol.md:§E Admissibility]

**Step 3 — Consultant #3 (Multi-Agent Architecture) invoked for hub-and-spoke and verification**

Principles applied:

**P-2 — Hub-and-spoke, never peer-to-peer.** Routing table must mechanically enforce
"no cell-to-cell direct invocation." Every inter-cell communication routes through
brigadier's Task(). The `acting_as:` field in every message header makes the routing
path auditable. Concrete consequence: Part 4's routing table must have a "no-bypass"
rule — if a cell discovers it needs to invoke another cell, that is a routing-table
gap, not a signal to add a peer-to-peer channel. [src:multi-agent-architecture.md:§4 P-2;
MANIFEST-DRAFT.md:§4 C-05 Kim vs Anthropic resolution]

**P-5 — Verification architecture (MAST coverage).** Part 4's escalation taxonomy must
address all 3 MAST failure-mode categories:
- System Design Issues → covered by typed `mode:` prefix, `acceptance_predicate`,
  `ap_budget` in brief schema.
- Inter-Agent Misalignment → covered by hub-and-spoke (no peer-to-peer).
- Task Verification → covered by provenance gate + Hamel-binary acceptance predicate.
[src:multi-agent-architecture.md:§4 P-5]

**P-3 — Context budget discipline.** Task briefs must pass disk paths, not inlined
bodies. Subagent output is compressed (proposed_writes[] + provenance[] + escalations[])
— not raw traces. [src:multi-agent-architecture.md:§4 P-3]

**Step 4 — Consultant #13 (Constitutional AI) invoked for safety constraints**

Principles applied:

**P3 — Hardcoded never-list.** Part 4's dispatch schema must structurally block
agents from: self-modifying their own role-manifests, strategizing on Method choices,
calling peer agents directly, auto-promoting to canonical without human ack. These are
the "never" category per FUNDAMENTAL §6.1. Constitutional AI P3 rationale: "absolute
behaviors that remain constant regardless of any instruction." [src:anthropic-constitutional-ai.md:§4 P3]

**P6 — Transparency and corrigibility.** Part 4 must NOT make canonical promotion
decisions autonomously. Every escalation is a packet to brigadier, never a unilateral
action. The routing table must be legible (YAML, not embedded in prompt prose) to
maintain transparency. [src:anthropic-constitutional-ai.md:§4 P6;
part-4-role-taxonomy-coordination-protocol.md:§E Deontics]

**Step 5 — Conflicts between consultants surfaced**

**Conflict A (OPEN — TRADEOFF-02): Ashby requisite variety vs Anthropic simplicity.**

- Ashby (Consultant #2, Systems): brigadier routing variety must be ≥ task-type
  variety. As task types grow, the routing table must grow. More routing rules =
  more variety = required for the system to handle novel tasks.
- Anthropic (Consultant #3): "Start with simple prompts... add complexity only when
  needed." System prompt ≤2000 tokens. More routing rules = more complexity = context
  budget pressure.
- Resolution path: variety lives in routing YAML (a file read on demand, not in
  context permanently), not in system prompt prose. The routing table is a declarative
  artefact with many rules; the system prompt is a short executable. Wave C must verify
  brigadier routing table has ≥20 distinct routing rules AND system prompt ≤2000 tokens.
  [src:MANIFEST-DRAFT.md:§4 TRADEOFF-02; multi-agent-architecture.md:§5 Conflict-1]

**Conflict B (RESOLVED — C-05): Kim scaling vs Anthropic multi-agent gains.**

- Kim: "more agents = diminishing returns" when single-agent baseline exceeds 45%.
- Anthropic research: "+90.2% gain" with multi-agent research system.
- Resolution: task-decomposition type determines which applies. `parallel-independent`
  tasks (multi-expert on different domains) = warranted. `sequential-pipeline` tasks
  (critic then optimizer on same artefact) = pipeline, not parallelism. Part 4 routing
  table must encode `task_decomposition_type: parallel-independent | sequential-pipeline`.
  [src:MANIFEST-DRAFT.md:§4 C-05; multi-agent-architecture.md:§5 Conflict-3]

**Conflict C (RESOLVED — C-06): Cognition "share full traces" vs Anthropic "compress output".**

- Cognition: share full traces to prevent context fragmentation.
- Anthropic: compress to 1000-2000 token summaries per subagent.
- Resolution: compress within subagent (expert returns compressed packet); brigadier
  integrates all expert summaries into authoritative context (never receives raw traces).
  Brigadier holds integrated context; experts compress. [src:multi-agent-architecture.md:§5 Conflict-2]

**Conflict D (OPEN — OQ-Conflict#4): MCP tool-invocation vs A2A agent-delegation protocol.**

- MCP (current): Task() is a tool call; brigadier calls an expert as a tool.
  No acknowledgement handshake; no mid-flight observability.
- A2A (Google DeepMind, 2025): standardised inter-agent delegation with
  `task_dispatched → task_received_ack → task_in_progress → packet_returned` schema.
- Current Jetix state: Task() is proto-A2A. Long-horizon tasks (>30 min expert sessions)
  have no mid-flight observability. Part 4 must design an explicit handshake schema
  slot (even if not implemented in Phase A). [src:multi-agent-architecture.md:§5 Conflict-4;
  MANIFEST-DRAFT.md:§6 OQ-4]

**Step 6 — Wave C author produces Part 4 interface card with explicit resolution table**

- Per MANIFEST-DRAFT §4 Conflict Resolution Rules: "Tradeoff documentation mandatory.
  Silent compromise prohibited. Every conflict resolved in a Wave C card must appear in
  the card's §5 Tradeoffs section with explicit resolution and `what changes in this Part` clause."
- Part 4 interface card §5 must include: TRADEOFF-02 resolution, C-05 task-type
  discrimination, C-06 compression contract, OQ-4 A2A handshake slot.
- Part 4 §D Dependencies: all typed A.14 edges per Levenchuk P4 (no generic "depends-on").
- Routing table YAML named as primary Wave C deliverable. [src:MANIFEST-DRAFT.md:§5 Anti-cargo-cult]

### Conflicts summary (Scenario W)

| Conflict | Status | Resolution | Applicable Part |
|----------|--------|------------|-----------------|
| TRADEOFF-02: Ashby variety vs Anthropic simplicity | OPEN — Wave C must verify | Variety in routing YAML, not prompt prose | Part 4 |
| C-05: Kim scaling vs Anthropic multi-agent gains | RESOLVED | Encode task_decomposition_type in routing table | Part 4 |
| C-06: Cognition full traces vs Anthropic compression | RESOLVED | Compress within subagent; brigadier integrates summaries | Part 4 (packet schema) |
| OQ-4: MCP tool vs A2A delegation protocol | OPEN — Phase B flag | Design handshake schema slot in Phase A; do not implement | Part 4 |
| CrewAI hierarchical vs IP-1 | RESOLVED | IP-1 wins; coordination = routing table, not manager LLM | Part 4 |

### Gaps identified

| Gap ID | Description | Severity | Wave C fix |
|--------|-------------|----------|------------|
| GAP-SW-A | Routing table not a declarative YAML artefact today (C1 partial) | Non-blocking today | Bundle 2 Part 4 Bullet 1 |
| GAP-SW-B | TRADEOFF-02 unresolved — routing table size vs system prompt budget not verified | Non-blocking (Phase A swarm is small) | Bundle 2 Part 4 Wave C work + Ruslan ack on TRADEOFF-02 |
| GAP-SW-C | A2A handshake schema slot absent in Part 4 design — no mid-flight observability for long-horizon tasks | Phase B risk | Bundle 2 Part 4 Bullet 2 (C1 + OQ-4 joint work) |
| GAP-SW-D | MAST failure-mode coverage not formally verified against Part 4 escalation taxonomy today | Non-blocking | Bundle 2 Part 4 Bullet 1 (routing table as testable artefact) |

### Verdict: PASS

**Reasoning.** Scenario W is a Wave C design-time scenario, not a runtime operational
scenario. The question "which consultants invoked, what principles applied, where do
they conflict" is fully answerable from Wave B artefacts. The MANIFEST-DRAFT §2 matrix
cell for Part 4 names the primary/secondary frameworks, the resolved conflicts (C-05,
C-06), and the open conflicts (TRADEOFF-02, OQ-4). The consultant cards contain the
primary-source citations, applied consequences, and anti-cargo-cult examples. Wave C
author has a complete, non-contradictory brief. [src:MANIFEST-DRAFT.md:§2 Part 4 row;
§4 conflicts table; multi-agent-architecture.md:§4, §5; levenchuk-shsm-fpf.md:§4]

---

## §5 Coverage Calculation

| Metric | Value |
|--------|-------|
| Total scenarios | 4 |
| PASS | 4 |
| FAIL | 0 |
| Gate threshold | 4/4 PASS |
| **Gate verdict** | **4/4 PASS — gate threshold met** |

**Qualification.** One scenario (S2) has a HARD GAP on Step 4 (automated anti-recurrence
check, blocked on TRADEOFF-01). The scenario still PASSES because the use case is
completable at F3/manual level. The HARD GAP tag signals that Wave C Bundle 3 (Part 8)
must be prioritised once TRADEOFF-01 is acked by Ruslan — the manual fallback is not
a target state.

---

## §6 Cross-Cutting Findings

**Finding 1 — Part 1 (git substrate) is the rock.** Every scenario traverses Part 1
multiple times. Every state change in every scenario produces a committed file. Part 1's
AUDIT artefacts are fully operational (571 commits in 30 days, per AUDIT §0). This part
is the most robust in the graph and correctly serves as Layer 0.
[src:MASTER-PLAN-DRAFT.md:§6.4 P1 AUDIT]

**Finding 2 — STOP gate in Part 2 is structural and working, but schema-light.**
The STOP gate successfully prevents auto-promotion in Scenarios 1 and 3. The mechanism
works today (`~/review-latest.md` → owner review → `/ingest`). The gap is schema
formality: `gate_class: stop_gate` field and `human_acked_at:` enforcement are specified
but not machine-verified. Wave C must close this or the STOP gate weakens under
automation pressure. [src:part-2-signal-ingestion-triage.md:§E Laws; MASTER-PLAN §5.2 UND-4]

**Finding 3 — Part 6 is the convergence point for all scenarios.** Every scenario routes
through Part 6 for canonical promotion. The gate mechanism is operational (8 confirmed
AWAITING-APPROVAL gate documents). The F-G-R compliance scanner (audit automation) is the
single most impactful Wave C deliverable for Part 6 — all 4 scenarios would benefit from
it. [src:part-6-governance-provenance-human-gate.md:§H Wave C primary gap]

**Finding 4 — Part 8 is the structural weak point.** Scenario 2 Step 4 and the
anti-recurrence check expose Part 8 as the only part with near-zero operational
implementation today (`system-health.json` reports "all green — no computation
mechanism"). TRADEOFF-01 must be resolved before Bundle 3 begins. Until then, health
monitoring is fully manual. [src:MASTER-PLAN-DRAFT.md:§6.4 P8 AUDIT; §5.1 OQ-1]

**Finding 5 — C1 (accessor pipeline ownership) is the most consequential blocking
contradiction.** Surfaces in Scenarios 1 and 3. Part 3 disowns `/ask`, `/ingest`, etc.;
Part 4 does not yet explicitly own them. At Phase A this does not break operations (skills
work). At Wave C it becomes a BLOCKING design gap: Part 4's routing table cannot be
authoritative if it does not name the accessor pipeline's ownership. Bundle 2 MUST resolve
C1 as joint Part 3 + Part 4 work before either part's Wave C interface card is locked.
[src:MASTER-PLAN-DRAFT.md:§3.4 C1; §5.2 C1 additional OQ]

**Finding 6 — Consultant framework conflicts are well-mapped; only two remain open.**
Scenario W trace confirms the Wave B consultant system is mature. Resolved: C-01 through
C-08 in MANIFEST-DRAFT §4. Open: TRADEOFF-01 (S3 authority) and TRADEOFF-02 (Ashby
variety vs simplicity). Both need Ruslan ack, not design decisions. The consultant cards
carry explicit resolution paths and "what changes in this Part" clauses — the anti-cargo-cult
discipline is in place. [src:MANIFEST-DRAFT.md:§4; §6]

**Finding 7 — DRR / compound-phase feedback loop shows up in every scenario.**
Scenario 1 (KB entries feed future queries), Scenario 2 (DRR review dates), Scenario 3
(cycle events → strategies.md), Scenario W (Part 4 design choices feed Part 5 compound
patterns). Part 5 is the glue across scenarios. The OQ-MERGED-2 dissent (engineering-expert:
"Part 5 dissolves into Parts 3+4") would be a significant structural change if accepted
— the scenario traces show residual compound-phase-exclusive work in every scenario.
Recommendation: preserve Part 5 standalone and note this as evidence for the OQ-MERGED-2
dissolve-condition test. [src:part-5-compound-learning-methodology-capture.md:§H dissent]

---

## §7 Recommendations for AWAITING-APPROVAL §5 (Defects / Known Limitations)

Items where Wave A is "specified but not implemented" — explicitly deferred to Wave C
with reason.

| Item | Status | Deferred to | Reason for deferral |
|------|--------|-------------|---------------------|
| STOP gate packet `gate_class` field (UND-4) | Specified, not implemented | Wave C Bundle 2 Part 2 Bullet 1 | Schema field definition requires Part 6 gate packet schema to be canonicalised first |
| `human_acked_at:` machine-enforced at ingest boundary | Specified, not enforced | Wave C Bundle 2 Part 2 Bullet 1 | Enforcement requires pre-commit hook update; hook layer is Phase B target |
| F-G-R compliance scanner as Part 6 automated service | Specified, not implemented | Wave C Bundle 1+3 Part 6 Bullets 1, 3 | Scanner requires agreed field names across all parts (depends on C2 health signal schema resolution) |
| Routing table as declarative YAML (`swarm/lib/routing-table.yaml`) | Specified, not materialised | Wave C Bundle 2 Part 4 Bullet 1 | Requires C1 ownership decision first |
| Part 8 SLI/SLO schema, weekly health dashboard, quarterly immune audit | Specified, not implemented | Wave C Bundle 3 Part 8 (all bullets) | BLOCKED on TRADEOFF-01 Ruslan ack — entire Bundle 3 gated |
| Weekly review artefact schema as canonical Foundation artefact | Specified informally | Wave C Bundle 4 Part 9 Bullet 2 | Depends on Bundle 3 SLI schema (Part 8 signals needed for weekly template revision) |
| DRR review-date automated trigger | Specified (Part 5 compound ritual) | Wave C Bundle 3 Part 5 Bullet 1 | Requires compound ritual as canonical Foundation artefact |
| A2A handshake schema slot in Part 4 (OQ-4) | Specified as Phase B need | Wave C Bundle 2 Part 4 Bullet 2 | Phase A Task() is sufficient; slot must exist in design without implementation |
| Methodology library sub-layer consistently populated in Part 3 | Specified, partially operational | Wave C Bundle 2 Part 3 Bullet 2 | Requires UND-3 methodology promotion pipeline |

**Priority ordering (by dependency and scenario impact):**

1. TRADEOFF-01 Ruslan ack — unblocks Bundle 3 entirely (Part 8 + Part 5 Bullet 3).
2. C1 resolution (Part 3 + Part 4 joint) — unblocks routing table YAML and accessor ownership.
3. Bundle 1 (Part 1 + Part 6 partial) — no blockers; start immediately after Ruslan ack.

---

## §8 Provenance

| Claim / trace step | Source card section |
|---------------------|---------------------|
| S1 Step 1-2: voice pipeline operational artefacts | MASTER-PLAN-DRAFT.md §6.4 P2 AUDIT; part-2 §C, §A |
| S1 Step 3: STOP gate structural + J-Approve decision class | part-2 §D, §E Laws; part-6 §A |
| S1 Step 4: D28 anchor mandatory, PARA-tier | part-2 §A, §C, §E |
| S1 Step 5: wiki entity write protocol | part-3 §C, §E Laws |
| S1 Step 6: /ask citation chain + C1 contradiction | part-3 §B, §E Deontics; MASTER-PLAN §3.4 C1 |
| S2 Step 1: LOCKED decision flow | part-9 §B, §E; part-6 §B, §C, §E; part-1 §B |
| S2 Step 3: monthly reflection + DRR entry | part-9 §B; part-5 §B, §E Laws |
| S2 Step 4: anti-recurrence check / Part 8 HARD GAP | MASTER-PLAN §6.4 P8 AUDIT; §5.1 OQ-1; part-6 §E IP-1 |
| S3 Step 1: hub-and-spoke dispatch schema | part-4 §A, §E Laws; multi-agent-consultant §P-2 |
| S3 Step 2: compressed packet return | part-4 §B; multi-agent-consultant §P-3, §Conflict-2 |
| S3 Step 3: provenance gate checks | part-6 §E Admissibility; part-6 §H Wave C gap |
| S3 Step 4: dissent preservation; routing table gap | shared-protocols §3; part-4 §C, §H |
| S3 Step 5: canonical promotion flow | part-6 §B, §C; part-1 §C; part-3 §C |
| SW Step 1-2: MANIFEST §2 matrix + Левенчук principles | MANIFEST-DRAFT §2 Part 4 row; levenchuk §4 P1, P6, P7 |
| SW Step 3: Multi-agent P-2, P-5, P-3 | multi-agent-consultant §4 P-2, P-5, P-3 |
| SW Step 4: Constitutional AI P3, P6 | anthropic-constitutional-ai §4 P3, P6 |
| SW Step 5: Conflicts A-D | MANIFEST-DRAFT §4 TRADEOFF-02; multi-agent-consultant §5 Conflict-2,3,4 |
| GAP-S2-B HARD GAP declaration | MASTER-PLAN §6.4 P8 row; dependency-graph §2.2 TRADEOFF-01 |
| C1 as most consequential contradiction | MASTER-PLAN §3.4 C1; §5.2 C1 additional OQ; dependency-graph §3 |
