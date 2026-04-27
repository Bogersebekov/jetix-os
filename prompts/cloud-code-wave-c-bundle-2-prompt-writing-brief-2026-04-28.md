---
title: Cloud Code Brief — Write the Wave C Bundle 2 deep prompt for ROY brigadier
date: 2026-04-28
type: meta-brief
target: Cloud Code on server (claude --dangerously-skip-permissions in tmux)
purpose: Server CC reads this brief + all context files, then writes full deep prompt for ROY brigadier to execute Wave C Bundle 2 (Parts 2 + 3 + 4 — Information Lifecycle + Agent Coordination)
output_required: prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md (committed + pushed)
estimated_walltime: 30-60 min server CC work to write the deep prompt
critical_constraints:
  - DO NOT execute Wave C Bundle 2 itself — only write the prompt. Ruslan reviews deep prompt before launching brigadier.
  - DO NOT skip the Wisdom Application Loop — Ruslan's central requirement (preserve discipline established in Bundle 1)
  - The deep prompt MUST be ~500-800 lines — Bundle 2 is bigger than Bundle 1 (3 parts vs 3, but more Wave C bullets and C1 BLOCKING contradiction resolution)
  - Apply Bundle 1 lessons: bias toward OPERATIONAL adoptions, minimize purely-philosophical text in architecture documents (Ruslan feedback)
---

# Cloud Code Brief — Write Wave C Bundle 2 Deep Prompt

## §0 What you (server CC) are doing

You are NOT executing Wave C Bundle 2. You are writing the **deep prompt** that ROY brigadier will execute later.

**Output: `prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md`** — 500-800 lines, action-ready.

Commit + push when done. STOP. Notify Ruslan via tmux output.

---

## §1 Context — what's done, what's locked

### Current state on `claude/jolly-margulis-915d34` HEAD `ca52e0a`

**Bundle 1 is COMPLETE and Ruslan-ACKED** (2026-04-28 evening walkthrough):
- Part 1 architecture LOCKED (17,413 words)
- Part 6a Provenance Officer LOCKED (16,448 words)
- Part 6b Human Gate LOCKED (15,015 words)
- All M-gates PASSED (M1=100% / M2=100% / M3=4/4 / M4=3/3)
- 42 Wisdom adoptions verified (no cargo-cult; Ruslan spot-checked 6, all justified)
- 7 Bundle 1 decisions ack'd (split LOCKED, F-G-R F8, Default-Deny F8, blast-radius 4 tiers, AWAITING-APPROVAL schema frozen, HARD GAPS resolved)
- 8 OQ-B1-* surfaced and resolved/deferred per Ruslan ack
- ACK record at `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (created on ack)

### Bundle 2 dependencies are NOW available as constitutional baseline

Bundle 2 (Parts 2 + 3 + 4) builds on Bundle 1 outputs. The following are LOCKED inputs for Bundle 2 architecture:

- **Part 1 commit interface** — every Bundle 2 part calls Part 1 §H operations for canonical writes
- **Part 6a F-G-R schema** (`f-g-r.json` F8 constitutional) — every Bundle 2 emitted artefact must carry F-G-R tags conforming to this schema
- **Part 6a `[src:filename]` enforcement** — every Bundle 2 architecture document follows citation discipline (anti-cargo-cult)
- **Part 6a approval log structure** — Bundle 2 promotion events log to `swarm/approvals/log.jsonl`
- **Part 6b stage-gate predicates** — Bundle 2 promotion classes (draft → reviewed → accepted → canonical) gate-checked
- **Part 6b Default-Deny classifier** — any new action class introduced by Bundle 2 must be classified
- **Part 6b blast-radius 4 tiers** — Bundle 2 actions tiered for HITL escalation
- **Part 6b AWAITING-APPROVAL schema with `gate_class`** — Bundle 2's AWAITING-APPROVAL packet conforms

---

## §2 Bundle 2 scope — Parts 2 + 3 + 4

Per Master Plan §7.1: **Bundle 2 = Parts 2 + 3 + 4 (Information Lifecycle + Agent Coordination)**.

Note: brigadier in Bundle 1 AWAITING-APPROVAL §7 wrote "Bundle 2 = Parts 2 + 7" — this was an ERROR. Correct scope is Parts 2 + 3 + 4 per Master Plan. Verify when reading wave-c-worklist.md §3 (Bundle composition table).

### Part 2 — Signal Ingestion & Triage (3 bullets per wave-c-worklist §2 Part 2)

**Source:** `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 2.

- **P2.1** — STOP gate packet schema with `gate_class` field (UND-4) — coordinate with Part 6b (Bundle 1 already specified the schema in `awaiting-approval-packet.json`; Part 2 emits packets conforming)
- **P2.2** — PARA-tier enforcement (`para_tier: Project | Area | Resource | Archive`) at /ingest level — frontmatter field mandatory before STOP gate ack
- **P2.3** — Multi-owner STOP gate stub (Phase B — declare structural change scope, do not implement)

### Part 3 — Knowledge Base & Methodology Library (4 bullets — C1 BLOCKING resolution required)

**Source:** wave-c-worklist §2 Part 3.

- **P3.1** — **C1 ACCESSOR PIPELINE OWNERSHIP** (BLOCKING resolution per Ruslan ack 2026-04-27 = **Variant A: shared infra `swarm/lib/` with named owner**). Architecture document MUST canonicalize: `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` skills live in `swarm/lib/` as infrastructure layer; Part 3 owns wiki content; Part 4 owns role-manifest content; neither owns the accessor scripts directly
- **P3.2** — Methodology library sub-layer materialisation (`wiki/methodology/` consistently populated; promotion pipeline from Part 5 → Part 3 declared)
- **P3.3** — CRM edge validation schema (UND-5 — when CRM (Part 10) writes typed edges to `wiki/graph/edges.jsonl`, validation rules)
- **P3.4** — `/ask --save` default enforcement (per OQ from Wave A — comparisons are first-class output)

### Part 4 — Role Taxonomy & Coordination Protocol (3 bullets — IP-1 critical + UND-1 binding)

**Source:** wave-c-worklist §2 Part 4.

- **P4.1** — **Routing table as declarative YAML** (`swarm/lib/routing-table.yaml`) — currently embedded in brigadier system prompt; Wave C primary gap. Highest-leverage single investment. ≥20 distinct routing rules per Ashby requisite variety (TRADEOFF-02 resolution per Manifest §4)
- **P4.2** — **C1 ownership decision** materialized in Part 4 (joint with Part 3 P3.1) — Part 4 declares which roles invoke `swarm/lib/` accessor skills; routing table includes accessor-skill invocations
- **P4.3** — **UND-1 DRR message schema** at Part 4 → Part 5 boundary — per Ruslan OQ-3 ack: **Part 5 receives raw task-return packets, does own DRR extraction**. Part 4 §B output schema for `task-return-packet.json` (already stubbed in Bundle 1 Part 1 §I.5 — Bundle 2 Part 4 fully specifies)

### Cross-cuts within Bundle 2

- **IP-1 Role≠Executor** (CRITICAL for Part 4) — role manifests = U.Episteme; executor bindings = RUSLAN-LAYER `executor-binding.yaml`
- **A.14 typed edges** — every dependency uses typed edge (Bundle 1 established 10-edge canonical table; Bundle 2 follows)
- **F-G-R DOGFOOD** — every architecture claim tagged per Bundle 1 Part 6a `f-g-r.json` F8 schema
- **Append-only** — wiki entries / methodology library entries / role manifests append-only
- **L/A/D/E** — every interface section structured per FPF A.6.B
- **Foundation vs RUSLAN-LAYER** — explicit §X per part (per OQ-MERGED-3 Wave A scope)
- **C1 Joint Design** (Part 3 + Part 4) — these two parts must produce coherent answer; brigadier MUST run a Joint Design Phase between them, not just sequential

---

## §3 Required reading list for ROY brigadier

The deep prompt MUST instruct brigadier to read these BEFORE proposing per-part architecture.

### A. Constitutional baseline (mandatory)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0)
2. `design/JETIX-FPF.md` (full constitutional)
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md`
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (esp. §4.5 deep-study constraint)
5. **Bundle 1 Foundation outputs (CONSTITUTIONAL FOR BUNDLE 2):**
   - `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (esp. §B Outputs / §H Code interfaces / §I.5 task-return-packet stub)
   - `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (esp. §I.1 F-G-R schema / §C approval log discipline)
   - `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (esp. §I.1 awaiting-approval-packet schema with gate_class / §I.2 constitutional_never_list / §I.3 blast-radius-table / §I.4 default-deny-table / §E Laws L1-L10)
6. `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (Ruslan's specific ack decisions on F8 promotions)
7. Locks D1-D29 + 4 LOCKS-ADDENDUM (focus on D17, D26, D27, D28 for Bundle 2)
8. `decisions/RUSLAN-WALKTHROUGH-CYCLE-12-WAVE-A-2026-04-27.md` on `claude/awesome-gates-bf616d` — Ruslan's full walkthrough record

### B. Wave A artefacts

1. MASTER-PLAN-DRAFT.md
2. candidate-parts-merged.md
3. dependency-graph.md
4. wave-c-worklist.md (focus §2 P2/P3/P4 + §3 Bundle 2 dependencies)
5. A-1-critic-gate.md
6. M1/M2/M3 verification reference patterns
7. **Wave A interface cards for Bundle 2 parts:**
   - `interface-cards/part-2-signal-ingestion-triage.md`
   - `interface-cards/part-3-knowledge-base-methodology-library.md`
   - `interface-cards/part-4-role-taxonomy-coordination-protocol.md`
8. expert-pre-reads/ (5 files for cross-reference)

### C. Wave B consultant cards (per Manifest §2 matrix)

**For Part 2:**
- `knowledge-management-karpathy-luhmann-matuschak.md` (D28 anchor-mandatory, PARA tier)
- `unix-philosophy.md` (do-one-thing-well per pipeline stage)
- `event-sourcing-cqrs.md` (append-only write, STOP gate as command handler)
- `levenchuk-shsm-fpf.md` (IP-3, permeable filtered boundary A.1)

**For Part 3:**
- `knowledge-management-karpathy-luhmann-matuschak.md` (Karpathy LLM wiki, Luhmann atomicity, typed graph)
- `levenchuk-shsm-fpf.md` (IP-2 bounded context, A.14 typed edges, FPF A.14 dependencies)
- `compounding-engineering.md` (CE populates methodology library; DRR → methodology promotion)
- `clean-code.md` (Ousterhout deep-modules: each wiki concept = atomic unit)
- `mereology-typed-edges.md` (typed edges = Part 3's graph schema canonical)

**For Part 4:**
- `levenchuk-shsm-fpf.md` (IP-1 CRITICAL Role≠Executor, IP-8 F.6 6-step onboarding, L/A/D/E A.6.B)
- `multi-agent-architecture.md` (hub-and-spoke P-2, verification architecture P-5, MAST coverage)
- `anthropic-constitutional-ai.md` (hard-rule anti-scope §6.1, simplicity-transparency-trust)
- `mereology-typed-edges.md` (typed edges for role dependencies)
- `systems-thinking-cybernetics.md` (Ashby requisite variety: brigadier routing variety ≥ task-type variety)

### D. Wave B Supplement library-direct sources

For Bundle 2 specifically, these supplement sources have applicability:
- `raw/books-md/event-sourcing/young-cqrs-2010.md` — for Part 2 (STOP gate as command handler) and Part 4 (DRR as event log)
- `raw/books-md/anthropic/bai-2022-cai.md` — for Part 4 (multi-agent constitutional discipline)
- `raw/books-md/anthropic/askell-2021-hhh.md` — for Part 4 (HHH framing for agent role manifests)

### E. Existing operational artefacts (audit reference)

- `tools/transcribe.py` / `extract.py` / `filter.py` / `run_pipeline.sh` (current voice pipeline — Part 2 references)
- `wiki/` (552 entities, 577 edges — Part 3 current state)
- `.claude/agents/brigadier.md` + 5 expert agents (Part 4 current routing baseline)
- `swarm/lib/shared-protocols.md` (current shared infra layer — destination for accessor skills per C1)
- `comms/mailboxes/*.jsonl` (13 channels — Part 4 messaging baseline)

---

## §4 THE WISDOM APPLICATION LOOP — Bundle 2 refinements

**Continue the discipline established in Bundle 1.** Wisdom Loop is structural, not lip service.

### Phase structure (UNCHANGED from Bundle 1)

For each Part (2, 3, 4) after integrator produces draft architecture, run Wisdom Application Phase:

For each consultant card relevant to this part (per §3.C list above):
1. **Question 1:** "What does this consultant card say that the current draft DOES NOT yet apply, but would benefit from?"
2. **Question 2:** "Are there principles from this card we cited but did not actually apply (cargo-cult risk per Manifest §5)?"
3. **Question 3:** "Is there a concrete improvement to the architecture if we apply principle X from this card?"
4. **Question 4:** "If we DO apply this improvement — what changes in §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary / §F Anti-scope?"
5. **Question 5:** "Is the application JUSTIFIED for current Phase A scope (single-owner, Phase 1 €50K horizon)? Or is it premature optimization for Phase B/C/D scale?"

### Bundle 2 refinements per Ruslan feedback (NEW)

After Bundle 1 walkthrough, Ruslan flagged that some adoptions were "academic boundary text" rather than operational changes (e.g., Stoic Dichotomy of Control, Lindy verdict box). These were KEPT in Bundle 1 but represent **lower priority adoption category**.

**For Bundle 2, apply the following bias:**

- **PRIORITIZE operational adoptions** — adoptions that change schema fields, add new failure modes, define new SLO targets, add new lint checks, etc. (concrete code-level deltas)
- **MINIMIZE philosophical/marketing text** — adoptions that add only "framing prose" (e.g., "this is Lindy-grade", "in our control vs not", "Beer-clean S3 placement") without operational consequence
- **REJECT** any adoption whose "concrete consequence sentence" is purely about how the document reads (e.g., "this makes the architecture more legible") rather than about what the system DOES differently

**Wisdom Findings table format (UPDATED):**

```markdown
### Wisdom Application Findings — Part X

| Card | Principle | Current state | Improvement | Adopted? | Operational vs Philosophical | Justification |
|------|-----------|---------------|-------------|----------|-------------------------------|---------------|
| ... | ... | ... | ... | YES/NO/ALREADY | OPERATIONAL/PHILOSOPHICAL | ... |
```

**New column "Operational vs Philosophical":**
- OPERATIONAL = changes schema field / adds failure mode / defines SLO target / adds new lint check / changes algorithm
- PHILOSOPHICAL = framing prose / boundary text / marketing positioning / academic context

**Adoption thresholds:**
- OPERATIONAL adoption — adopt if Phase A justified (proceed as in Bundle 1)
- PHILOSOPHICAL adoption — adopt ONLY if it prevents a specific scope creep risk OR enables a Phase B/C concrete need; otherwise DEFER to Wave D documentation pass

**Aggregate target:** Bundle 2 should have YES Adopted ratio of Operational > 60% (Bundle 1 was ~50/50; Ruslan asked to bias operational).

---

## §5 Quality bar — deep prompt MUST enforce

### Per Master Plan Brief §4.5 deep-study constraint

Each Part architecture document MUST be **15-25K words minimum** with §A-§N + §X structural completeness (same as Bundle 1).

### C1 BLOCKING contradiction resolution (Bundle 2-specific)

Brigadier MUST:
1. Run a **Joint Design Phase** between Part 3 and Part 4 integrators (NEW phase between A-3 and A-4 of Bundle 1 pattern)
2. Produce a single coherent answer to: "Where do `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live? Who owns them? Who can modify them? How does Part 3 invoke them? How does Part 4 invoke them?"
3. Document the answer in BOTH Part 3 §I and Part 4 §I (DRY violation prohibited — single canonical answer in `swarm/lib/README.md` referenced from both)
4. Per Ruslan ack: **`swarm/lib/` shared infra with named owner**. Named owner = Part 3 lead with Part 4 advisory (proposed; brigadier may refine if better answer surfaces in Joint Design)

### Anti-cargo-cult enforcement

(Same as Bundle 1.) Per Wave B Manifest §5 + Bundle 1 Part 6a §C citation discipline:
- Every `[src:...]` citation must be followed within 200 chars by a concrete consequence sentence
- `/lint --check-citations` (Bundle 1 P6a.2) is the canonical enforcer; until it ships, manual discipline + critic gate

### Typed A.14 edges (Bundle 1 canonical 10-edge table)

Bundle 1 Part 1 §D established the canonical 10-edge reference table. Bundle 2 architecture documents MUST reference this canonical table; no new edge types invented without explicit FPF A.14 anchor.

### F-G-R DOGFOOD per Bundle 1 Part 6a F8 schema

Every Bundle 2 architecture claim must carry F-G-R per `shared/schemas/f-g-r.json` (or its inline definition in Part 6a §I.1). F-levels:
- F0-F2 NEVER canonical
- F3 minimum for canonical write
- F4 = ≥3 cycles applied (per OQ-B1-1 if Ruslan acked the wording refinement)
- F5 = peer-validated methodology
- F6 = cross-cycle reuse evidence
- F8 = constitutional Foundation invariant
- F9 = constitutional axiom (FUNDAMENTAL Vision lock-class)

### Foundation vs RUSLAN-LAYER fork-separation per part

Each Part architecture MUST have explicit §X declaring:
- What is generic Foundation
- What is RUSLAN-LAYER
- Where the boundary is

For Bundle 2 specifically:
- Part 2 fork-separation: anchor-mandatory pattern + STOP gate structure GENERIC. Voice-pipeline tools / specific PARA tier definitions for Ruslan's projects = RUSLAN-LAYER.
- Part 3 fork-separation: wiki accessor pipeline + KB structure GENERIC. Specific wiki content / niche slices / methodology library entries Ruslan-authored = RUSLAN-LAYER.
- Part 4 fork-separation: role-manifest schema + routing table SCHEMA generic. Specific role-manifests + routing-table.yaml entries + executor-binding.yaml = RUSLAN-LAYER.

---

## §6 Verification gates (M1/M2/M3 + M4 Wisdom)

Same pattern as Bundle 1, with Bundle 2 specific scenario adjustments:

### M3 Scenario walkthroughs (4 scenarios, threshold 4/4)

For Bundle 2:

- **Scenario 1** — Voice memo full lifecycle: voice file → /ingest with --anchor → transcribe.py → extract.py → filter.py → review_report.py → STOP gate (Part 6b) → human ack → Part 3 promotion → wiki entry with F-G-R + PARA-tier + provenance (Part 6a). Tests Parts 2/3/6a/6b/1.
- **Scenario 2** — Multi-agent dispatch: brigadier reads task → Part 4 routing-table.yaml selects expert agents → mailbox dispatch via `swarm/lib/` → expert returns task-return-packet → Part 5 stub receives raw → DRR extraction (Bundle 3 stub level). Tests Parts 4/5(stub)/6b.
- **Scenario 3** — Methodology promotion: pattern emerges in 3 cycles (Bundle 3 stub level) → Part 5 stages it → Part 3 promotes to `wiki/methodology/<pattern>.md` → /lint --check-citations passes → committed via Part 1. Tests Parts 5(stub)/3/6a/1.
- **Scenario 4** — C1 invocation: Part 3 query "what is X?" calls `swarm/lib/ask.py` → ask.py reads `wiki/index.md` (Part 3) + `swarm/wiki/comparisons/` → returns synthesis with citations → conform to Part 6a F-G-R discipline. Tests C1 ownership boundary holds.

### M4 Wisdom Application Loop verification

Same as Bundle 1, plus Bundle 2 refinements:
- Operational adoption ratio ≥60% target verified
- No purely-philosophical adoptions without scope-creep-prevention justification
- C1 Joint Design phase output documented

---

## §7 ETA + autocheck

**Walltime estimate: 14-20h ROY work** (Bundle 1 took 2h 41m at 6× compound velocity; Bundle 2 has 3 parts vs 3 but 10 bullets total vs 7, plus C1 Joint Design phase is new).

**Autocheck rules:**
- If walltime exceeds 28h — STOP, report, ask Ruslan
- If C1 Joint Design produces conflicting answers from Part 3 + Part 4 integrators — escalate to brigadier-mode arbitration; Ruslan ack required if answer materially differs from "shared infra `swarm/lib/` with Part 3 lead"
- If Wisdom Loop operational adoption ratio < 60% — investigate: is brigadier reverting to philosophical text? Apply Bundle 2 refinement bias more strictly.

---

## §8 Output expected from Bundle 2

### Per-part architecture documents

- `swarm/wiki/foundations/part-2-signal-ingestion-triage/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-4-role-taxonomy-coordination-protocol/architecture.md` (~15-25K words)

### Schemas / configs (referenced by Bundle 1 schemas where applicable)

- Part 2: STOP gate packet emission spec (conforms to Part 6b `awaiting-approval-packet.json` with `gate_class`)
- Part 3: `swarm/lib/README.md` (C1 ownership + invocation contract)
- Part 4: **`swarm/lib/routing-table.yaml`** (PRIMARY GAP from Wave A — declarative routing rules); `task-return-packet.json` schema (UND-1 binding); `executor-binding.yaml` template

### Joint Design artefact (NEW for Bundle 2)

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-2/C1-joint-design.md` — single coherent answer to C1 ownership question

### Updated cross-references

- Wave A interface cards updated where outdated
- Master Plan Draft Bundle 2 status table updated
- Manifest §2 matrix Bundle 2 rows updated

### AWAITING-APPROVAL packet

- `decisions/AWAITING-APPROVAL-wave-c-bundle-2-2026-04-XX.md` (same structure as Bundle 1 packet)

### STOP

After AWAITING-APPROVAL packet — STOP. NO auto-launch Bundle 3.

---

## §9 Branch + commit + operational

- Branch: `claude/jolly-margulis-915d34`
- Commit pattern: `[architecture] Bundle 2 — <part> — <phase>`
- Push after each major phase
- `unset ANTHROPIC_API_KEY` before claude
- `ulimit -n 65535`
- HD-02 N=2

---

## §10 What server CC does NOW

1. Read this brief fully
2. Read Bundle 1 deep prompt (`prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md`) for structure reference — Bundle 2 prompt is similar pattern with Bundle 2 specifics
3. Read `decisions/RUSLAN-ACK-WAVE-C-BUNDLE-1-2026-04-28.md` (after Ruslan ack creates it)
4. Read 3 Bundle 1 architecture documents (focus §I schemas, §H interfaces — these are constitutional inputs for Bundle 2)
5. Read Wave A interface cards for Parts 2, 3, 4
6. Read Wave A wave-c-worklist §2 P2/P3/P4 + §3 Bundle 2 composition
7. Skim Bundle 1 AWAITING-APPROVAL packet (`decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-28.md`) for AWAITING-APPROVAL output format reference

Then write `prompts/wave-c-bundle-2-deep-prompt-2026-04-28.md` (500-800 lines) with structure mirroring Bundle 1 deep prompt, adapted for Bundle 2 scope:

- Mission statement (Bundle 2 = Information Lifecycle + Agent Coordination, building on Bundle 1 LOCKED foundation)
- Constitutional inputs (Ruslan ack of Bundle 1; F-G-R schema F8; Default-Deny F8; blast-radius 4 tiers; AWAITING-APPROVAL schema frozen; 5 OQ blockers ack from 2026-04-27)
- Bundle 2 scope (Parts 2 + 3 + 4 with bullets — section §2 of this brief)
- Required reading list (section §3)
- C1 Joint Design Phase instructions (section §2 cross-cuts + §5)
- Wisdom Application Loop with Bundle 2 refinements (section §4 — VERBATIM, including OPERATIONAL/PHILOSOPHICAL column + 60% operational target)
- Quality bar (section §5 — deep-study, anti-cargo-cult, A.14 edges, F-G-R DOGFOOD, fork-separation, **bias toward operational adoptions**)
- Verification gates M1/M2/M3/M4 (section §6, with Bundle 2 scenario specifics)
- ETA + autocheck (section §7)
- Output expected (section §8)
- Branch/commit/operational (section §9)
- STOP rule

Commit + push when done. STOP. Notify Ruslan.

---

*End of brief. Mantra: QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. OPERATIONAL > PHILOSOPHICAL. RUSLAN-ACK > BRIGADIER-CONFIDENCE. C1 BLOCKING — Part 3 + Part 4 must agree.*
