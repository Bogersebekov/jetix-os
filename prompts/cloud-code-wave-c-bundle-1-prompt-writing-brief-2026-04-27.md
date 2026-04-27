---
title: Cloud Code Brief — Write the Wave C Bundle 1 deep prompt for ROY brigadier
date: 2026-04-27
type: meta-brief
target: Cloud Code on server (claude --dangerously-skip-permissions in tmux)
purpose: Server CC reads this brief + all context files, then writes full deep prompt for ROY brigadier to execute Wave C Bundle 1 (Parts 1 + 6a + 6b)
output_required: prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md (committed + pushed)
estimated_walltime: 30-60 min server CC work to write the deep prompt
critical_constraints:
  - DO NOT execute Wave C Bundle 1 itself — only write the prompt. Ruslan reviews deep prompt before launching brigadier.
  - DO NOT skip the "wisdom application loop" — this is Ruslan's central requirement
  - The deep prompt MUST be ~400-700 lines, comprehensive, action-ready for brigadier to copy-paste
---

# Cloud Code Brief — Write Wave C Bundle 1 Deep Prompt

## §0 What you (server CC) are doing

You are NOT executing Wave C Bundle 1. You are writing the **deep prompt** that ROY brigadier will execute later. Your output is a single file:

**`prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md`**

This file should be **400-700 lines, comprehensive, action-ready**. ROY brigadier will copy-paste it into his next session and execute it without further clarification.

Commit + push when done. STOP. Notify Ruslan via tmux output:
> «Wave C Bundle 1 deep prompt written at `prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md`. Ready for Ruslan review before brigadier dispatch.»

---

## §1 Context — what's done, what's blocked

### Current state on `claude/jolly-margulis-915d34` HEAD `4bdad69`

**Cycle 12 Wave A+B + Wave B Supplement** all complete and Ruslan-acked (2026-04-27 evening walkthrough):

- **Wave A Master Plan**: 10 parts identified, dependency graph, 34 Wave C bullets across 4 bundles, M1=90%/M2=conditional/M3=4/4 PASS
- **Wave B Best Practices**: 14 consultant cards, anti-cargo-cult discipline, 8 conflicts resolved
- **Wave B Supplement**: 5 fundamental sources processed (Bai 2022 CAI / Askell 2021 HHH / Young 2010 CQRS / Google SRE Book + SLO Workbook). Cards #5/#6/#13 lifted F3 → F4-F5

### Ruslan's decisions during walkthrough (CONSTITUTIONAL — must be honoured)

**5 OQ blockers ACKED:**
1. ✅ **OQ-MERGED-1: OVERRIDE — SPLIT Part 6** into Part 6a (Provenance Officer) + Part 6b (Human Gate). NOT consolidated. Reasoning: scale-readiness Phase B/C/D, fork-friendly portable provenance standard, independent change cadence.
2. ✅ **OQ-MERGED-2: standalone Part 5** (Compound Learning) — NOT dissolve into Parts 3+4. Engineering-expert dissent preserved with dissolve-test (3 cycles).
3. ✅ **OQ-1 / TRADEOFF-01: Part 8 = audit lead, Part 6 = enforcement arm.** With split: Part 8 invokes Part 6a as service for provenance check; Part 6b owns real-time per-artefact gate.
4. ✅ **OQ-3 / UND-1: Part 5 receives raw task-return packets**, does own DRR extraction. R2 loop ownership clean.
5. ✅ **OQ-MERGED-3: Wave A scope** — fork-separation (Foundation vs RUSLAN-LAYER) declared up-front per part, NOT deferred to Wave C card-by-card.

**Contradictions ACKED:**
- ✅ **C1 — Variant A: shared infra** `swarm/lib/` with named owner. Scripts `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live as infrastructure layer, not in Part 3 or Part 4.
- ✅ C2: Part 8 owns canonical health signal schema; all emitters conform. Bundle 3 work.
- ✅ C3: defer to Phase B (when integrations active). LOW.
- ✅ C4: nomenclature fix `PhaseOf` → `methodologically-uses` for Part 9 → Part 6. Bundle 4.

**Underspec ACKED:**
- ✅ UND-1 resolved (= OQ-3 above)
- ✅ UND-2: methodology promotion pipeline schema → Bundle 3 (P5 work)
- ✅ UND-3: P7 → P5 retrospective schema + cadence → Bundle 3 (joint P5/P7)
- ✅ UND-4: `gate_class` field in STOP gate packet — **Bundle 1 P6b work** (relevant for THIS bundle)
- ✅ UND-5: CRM edge validation → Bundle 4 (P10 work)

**8 non-blocking OQs ACKED** (per brigadier rec). Of relevance to Bundle 1:
- ✅ **OQ-MERGED-6: Default-Deny classifier MUST live in Part 6b** (FUNDAMENTAL §6.1 hard rule). Foundation level, not RUSLAN-LAYER.
- ✅ **OQ-MERGED-5: Part 8 "specify and stub"** Wave C, full impl = Phase B. (Affects how Part 6 references Part 8 audit signals — stub-level.)
- ✅ OQ-4 / UND-4: gate_class field (this bundle).

### Ruslan walkthrough tracker

`decisions/RUSLAN-WALKTHROUGH-CYCLE-12-WAVE-A-2026-04-27.md` on `claude/awesome-gates-bf616d` branch — fetch via `git show origin/claude/awesome-gates-bf616d:<path>`. Read this for full ack record.

---

## §2 Bundle 1 scope — Parts 1 + 6a + 6b

### Part 1 — System State Persistence (3 bullets)

Source: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 1.

**Bullet P1.1** — D27 cross-fork provenance schema stub (`shared/schemas/cross-fork-provenance.json` + `wiki/methodology/d27-fork-discipline.md`)
**Bullet P1.2** — D25 commit-format lint as Foundation artefact (`/lint --check-commit-format` skill spec + pre-commit hook stub)
**Bullet P1.3** — `/company-status` + `/knowledge-diff` offline-first guarantee (Law invariant declared in Part 1 §E + unit test stubs blocking network calls)

### Part 6a — Provenance Officer (NEW, derived from split)

Original Part 6 wave-c-worklist had 4 bullets. Distribute and adapt for Part 6a (~3-4 bullets):

**Bullet P6a.1** — F-G-R schema definition (`shared/schemas/f-g-r.json`) — formal spec for Formality (F0-F9) / G-ClaimScope / Reliability fields. With validation rules.
**Bullet P6a.2** — `[src:filename]` inline citation enforcement scanner (`/lint --check-citations` skill spec) — detect bare claims missing citation, flag cargo-cult signals (citation without "concrete consequence sentence" per Wave B Manifest §5).
**Bullet P6a.3** — Approval log structure (`swarm/approvals/log.md` append-only schema + entry format) — every promotion decision logged.
**Bullet P6a.4** — Quarterly immune audit framework (template at `swarm/audits/quarterly-template.md` + checklist of what to audit). Coordinates with Part 8 audit lead per OQ-1 (Part 8 invokes Part 6a as service).

### Part 6b — Human Gate (NEW, derived from split)

~3-4 bullets:

**Bullet P6b.1** — Stage-gate predicates registry (`shared/schemas/stage-gates.yaml`) — formal predicate definitions (Hamel-binary checklists, not prose) for each promotion class.
**Bullet P6b.2** — Default-Deny classifier (FUNDAMENTAL §6.1) implementation spec (`.claude/config/default-deny-table.yaml`) — every novel action class default-denied unless explicitly whitelisted.
**Bullet P6b.3** — Blast-radius classification table (`.claude/config/blast-radius-table.yaml`) — Tier 0 integrity (auto-halt) / Tier 1 strategic (Ruslan ack) / Tier 2 tactical (batch ack) / Tier 3 routine (auto-log). Per OQ-MERGED-6 Foundation level.
**Bullet P6b.4** — AWAITING-APPROVAL packet schema (`shared/schemas/awaiting-approval-packet.json`) with `gate_class: stop_gate | stage_gate | draft_promotion` field per UND-4.
**Bullet P6b.5** — HITL escalation taxonomy (`.claude/config/escalation-taxonomy.yaml`) — routing rules for L1/L2/L3 SLA tiers (per Part 9 OQ).

### Cross-cuts within Bundle 1

- IP-1 Role≠Executor: Part 6a/6b roles are U.Episteme manifests; executor bindings (which agent enforces) = RUSLAN-LAYER
- A.14 typed edges: every dependency in §D MUST use typed edge (operates-in / methodologically-uses / creates / etc), no generic "depends-on"
- F-G-R: every claim in architecture docs has F-G-R tag (this is dogfooding — Part 6a defines F-G-R, Bundle 1 docs use F-G-R from start)
- Append-only: all log structures (approval log, audit trail) append-only
- L/A/D/E: every interface section structured per FPF A.6.B Boundary Norm Square

---

## §3 Required reading list for ROY brigadier

The deep prompt MUST instruct brigadier to read these BEFORE proposing per-part architecture. Each pre-read MUST be cited in output.

### A. Constitutional baseline (mandatory full-read)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0, ~30K words, 35 UC, 12 categories A-L, 55+ anti-scope)
2. `design/JETIX-FPF.md` (3758 lines, IP-1..IP-8, 14 invariants A.1-A.14, Agency-CHR, F-G-R, L/A/D/E)
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (5758 words — what's already operational)
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (the spec for Wave C — including §4.5 deep-study constraint)
5. **Locks D1-D29 + 4 LOCKS-ADDENDUMs** — focus on D17, D25, D26, D27, D28, D29 (most relevant for Bundle 1)

### B. Wave A artefacts (mandatory)

1. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md` (5569 words — the skeleton)
2. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md`
3. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md`
4. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` (the 34 bullets)
5. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md`
6. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/M1/M2/M3` verification gates
7. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md` (139 lines — Bundle 1)
8. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md` (133 lines — TO BE SPLIT into 6a + 6b in this bundle)
9. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/` (5 expert pre-reads)

### C. Wave B consultant cards (mandatory for Bundle 1 anchors)

Brigadier MUST instruct relevant experts to read RELEVANT cards as pre-read. Per Manifest §2 matrix:

**For Part 1:**
- `consultants/levenchuk-shsm-fpf.md` (P1 anchor — IP-3 artifacts, D25 git-as-event-log)
- `consultants/capital-allocation-antifragility.md` (Lindy substrate)
- `consultants/unix-philosophy.md` (plain-text, everything-is-a-commit)
- `consultants/event-sourcing-cqrs.md` (git-as-event-log, append-only)
- `consultants/clean-code.md` (Ousterhout deep-modules: Part 1 = deep substrate)

**For Part 6a Provenance Officer:**
- `consultants/levenchuk-shsm-fpf.md` (B.3 F-G-R triad, A.14 typed edges, IP-4 FPF-Steward)
- `consultants/anthropic-constitutional-ai.md` (provenance + transparency as constitutional)
- `consultants/mereology-typed-edges.md` (typed edges for provenance graph)

**For Part 6b Human Gate:**
- `consultants/anthropic-constitutional-ai.md` (Default-Deny + hardcoded-never-list, RLAIF self-critique → fail-loud, RSP ASL-tier blast-radius)
- `consultants/levenchuk-shsm-fpf.md` (IP-4 immune system function, Agency-CHR A.13 J-level matrix)
- `consultants/sre-observability.md` (fail-loud P6, error-budget behaviour change for integrity SLOs)
- `consultants/capital-allocation-antifragility.md` (Graham margin-of-safety: over-engineer governance, blast radius unbounded)
- `consultants/stoic-epistemic.md` (Dichotomy-of-control: gate governs what is in Ruslan's control)

### D. Wave B Supplement library-direct sources (MANDATORY per Ruslan emphasis)

These were freshly added 2026-04-27 evening. ROY MUST read and apply:

1. `raw/books-md/anthropic/bai-2022-cai.md` — RLAIF self-critique, 16+16 SL/RL-CAI principles
2. `raw/books-md/anthropic/askell-2021-hhh.md` — HHH framework formal definitions
3. `raw/books-md/event-sourcing/young-cqrs-2010.md` — CQRS canonical (commands-imperative, no-delete via Reversal Transactions, aggregate-id partition, optimistic concurrency)
4. `raw/books-md/sre/google-sre-book.md` — SLI/SLO/error-budget, Four Golden Signals, blameless postmortems, cascading failures
5. `raw/books-md/sre/google-srewb-implementing-slos.md` — burn-rate algebra (1×/6×/14.4×)

### E. Existing operational artefacts (audit reference)

1. `swarm/lib/shared-protocols.md` — current protocol layer
2. Existing `decisions/AWAITING-APPROVAL-*` packets (8 of them) — pattern reference
3. `.claude/config/sg-banned-phrases.yaml` — current 18-entry stage-gate banned list

---

## §4 THE WISDOM APPLICATION LOOP (Ruslan's central requirement)

**This is the most important section of the deep prompt. Do NOT make this lip service.**

Standard cycle = integrator → critic → finalize. **For Wave C Bundle 1, brigadier MUST add a structural Wisdom Application Phase between integrator and critic.** This phase is:

### Phase structure

For each Part (1, 6a, 6b) after integrator produces draft architecture:

**Phase X — Wisdom Application Loop (NEW)**

For each consultant card relevant to this part (per §3.C list above):
1. **Question 1:** "What does this consultant card say that the current draft DOES NOT yet apply, but would benefit from?"
2. **Question 2:** "Are there principles from this card we cited but did not actually apply (cargo-cult risk per Manifest §5)?"
3. **Question 3:** "Is there a concrete improvement to the architecture if we apply principle X from this card?"
4. **Question 4:** "If we DO apply this improvement — what changes in §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary / §F Anti-scope?"
5. **Question 5:** "Is the application JUSTIFIED for current Phase A scope (single-owner, Phase 1 €50K horizon)? Or is it premature optimization for Phase B/C/D scale?"

**Output of Wisdom Application Loop**: structured table per Part:

```markdown
### Wisdom Application Findings — Part X

| Card | Principle | Current draft state | Improvement opportunity | Adopted? | Justification |
|------|-----------|---------------------|--------------------------|----------|---------------|
| #1 Левенчук | IP-3 artifacts-over-conversations | applied | — | n/a | already in §C |
| #5 Event Sourcing | Reversal Transactions | NOT yet applied | Add explicit "no-delete" rule to §F Anti-scope referencing Reversal pattern | YES | Phase A relevant — Foundation must commit to no-delete from start |
| #6 SRE | Four Golden Signals | partial — only latency mentioned | Add traffic / errors / saturation as Part 8 audit signals Part 1 emits | YES | Affects Part 8 cross-ref design (Bundle 3) |
| #13 CAI | ASL-tier blast radius | not applied | Map blast-radius Tier 0-3 to ASL-1 to ASL-4 conceptually for portability | NO | Phase B work — premature now |
| ... | ... | ... | ... | ... | ... |
```

Every "YES Adopted" entry MUST result in concrete edit to the draft architecture.

Every "NO" entry MUST have justification ("Phase B work" / "premature optimization" / "would require RUSLAN-LAYER decision Ruslan hasn't made").

### Why this matters

Ruslan emphasis (verbatim):
> «Чтобы вся вот эта мудрость, наработки из книг — они были применены в системе, если это возможно, если нужно, целесообразно — на 1000% насколько это целесообразно. Ещё чтобы задавались вопросы как мы можем конкретно добавить, нахуй, эту штуку, чтобы было ещё отдельный прогон где вся эта залупа даёт обратную связь — а как мы можем это улучшить с точки зрения такой-то книжки или с книжки такой-то.»

This is **not optional**. This is the structural mechanism that prevents:
- Cargo-cult citation (citing without applying)
- Knowledge sitting unused in `raw/books-md/`
- ROY producing "good enough" architecture that ignores hard-won wisdom

### Discipline

**ROY brigadier MUST**:
- Run Wisdom Application Loop AFTER integrator draft, BEFORE critic gate
- Produce findings table per part
- Apply every "YES Adopted" edit before critic
- Critic gate then verifies: did Wisdom edits hold? Anti-cargo-cult check stricter than usual.

**ROY brigadier MUST NOT**:
- Skip Wisdom Loop because "draft seems fine"
- Reject improvement opportunities without explicit justification
- Adopt every improvement without Phase A justification (Phase B+ ideas DEFER)

---

## §5 Quality bar — deep prompt MUST enforce

### Per Master Plan Brief §4.5 deep-study constraint

Each Part architecture document MUST be **15-25K words minimum**. Not 2-5K. Not "interface card extended". DEEP architecture document covering:

- §A Inputs (data shapes, event triggers, source ownership) — typed and complete
- §B Outputs (data shapes, consumer parts, side-effects) — typed and complete
- §C Side-effects (filesystem writes, schema validations, log entries) — exhaustive list
- §D Dependencies (typed A.14 edges, with rationale per edge — NO "depends-on" generic)
- §E Boundary (L/A/D/E lanes — Laws / Admissibility / Deontics / Effects)
- §F Anti-scope (generic + part-specific — what this part does NOT do)
- §G F-G-R Tagging (table of every artefact emitted with F-G-R values + rationale)
- §H Code-level interfaces (CLI commands, skills, file paths, schemas)
- §I Data schemas (full YAML/JSON specs for any new schema)
- §J Operational rituals (cadence, triggers, exception handling)
- §K Failure modes (what breaks, how detected, how recovered)
- §L Wave C work-list bullet status (each P-bullet from worklist mapped to specific output)
- §M Wisdom Application Findings (table from Phase X — see §4 above)
- §N Provenance (every claim traces to inline `[src:filename]` citation)

### Anti-cargo-cult enforcement (CRITICAL)

Per Wave B Manifest §5 detection rule:
> If a citation appears in an interface card without a "concrete consequence sentence" AND without a specific Wave C work-list bullet that references it → flag as cargo-cult, return for re-dispatch.

**Enforcement in Bundle 1:**
- Every `[src:...]` citation must be followed within 200 chars by a concrete consequence sentence (e.g., "...therefore Part 1 §E Laws state: 'No --amend on canonical branch'")
- `/lint --check-citations` (Bullet P6a.2) must be designed to AUTO-detect cargo-cult signals
- Critic gate MUST reject any §A-§N section with cargo-cult violations

### Typed A.14 edges everywhere

Every §D Dependencies entry MUST be one of:
- `ComponentOf` — part of the whole
- `ConstituentOf` — material constituent
- `PortionOf` — quantitative portion
- `PhaseOf` — temporal phase
- `MemberOf` — class membership
- `AspectOf` — aspect
- `creates` — produces artefact in
- `operates-in` — operates within substrate
- `methodologically-uses` — uses as methodology service
- `constrained-by` — constrained by audit/governance
- `derives-from` — derives state from

NO `depends-on`. Critic gate auto-rejects.

### F-G-R on every promoted claim

Every architecture claim must have F-G-R tag. Format:
- F0-F9 Formality (F0 = personal hunch, F4 = operational convention, F9 = constitutional)
- G ClaimScope ("holds within Phase A single-owner scope")
- R Reliability (R-low / R-medium / R-high / R-certified)

### Provenance trail

Every claim → `[src:path]` inline citation → resolves to exact file + section. M2 cross-reference gate verifies 100% citation resolution.

### Ruslan-LAYER vs Foundation discipline (per OQ-MERGED-3 Wave A scope)

Each Part architecture MUST have explicit §X "Foundation vs RUSLAN-LAYER fork-separation" section declaring:
- What is **generic Foundation** (any forkable Jetix instance)
- What is **RUSLAN-LAYER** (Ruslan's specific config — DACH ICP, executor bindings, German GDPR config, etc.)
- Where the boundary is

For Bundle 1 specifically:
- Part 1 fork-separation: D27 cross-fork provenance schema is GENERIC. Specific repo / branch names are RUSLAN-LAYER.
- Part 6a fork-separation: F-G-R schema GENERIC. Specific governance roles (who's the Provenance Officer human) RUSLAN-LAYER.
- Part 6b fork-separation: Default-Deny classifier framework GENERIC. Specific blast-radius assignments per action class = RUSLAN-LAYER.

---

## §6 Verification gates (M1/M2/M3 + new M4 Wisdom)

Same pattern as cycle 12 wave A:

- **M1 smoke test**: ≥90% pass coverage. Check each Part document has all §A-§N sections populated, no "TBD" placeholders, dependencies typed.
- **M2 cross-reference**: 100% citation resolution. Every `[src:...]` resolves to existing file + section.
- **M3 scenario walkthroughs**: 4 scenarios MUST pass for Bundle 1:
  - **Scenario 1** — full information lifecycle: voice memo → /ingest → STOP gate → Part 6a F-G-R tag → Part 6b gate ack → Part 1 commit → wiki entry. End-to-end via Bundle 1 interfaces.
  - **Scenario 2** — strategic decision: Ruslan ack of AWAITING-APPROVAL packet → Part 6b gate decision → Part 6a approval log entry → Part 1 LOCKED commit. With audit trail reconstructable.
  - **Scenario 3** — quarterly immune audit: Part 8 (stub) invokes Part 6a quarterly audit → Part 6a checks F-G-R compliance across wiki entries → flags drift → Part 6b decides remediation. Cross-bundle reference (P8 stub level).
  - **Scenario 4** — fork-separation test: hypothetical Phase B fork — partner imports Part 1 D27 schema + Part 6a F-G-R schema (generic), declines Part 6b Default-Deny rules (their own). Foundation vs RUSLAN-LAYER boundary holds.
- **M4 Wisdom Application Loop verification (NEW)**: each Part has Wisdom Findings table populated (§M section). Every "YES Adopted" entry has corresponding edit in §A-§L. Every "NO" entry has explicit justification.

---

## §7 ETA + autocheck

**Walltime estimate: 12-18h ROY work** (was 10-12h pre-split, +2-3h for split into 6a+6b, +2-3h for Wisdom Application Loop).

**Autocheck rules** (deep prompt MUST instruct brigadier):
- If walltime exceeds 24h — STOP, report status, ask Ruslan how to proceed
- If any subagent's first attempt produces low-quality output (cargo-cult / missing sections) — re-dispatch with explicit feedback citing this brief's quality bar
- If Wisdom Application Loop produces 0 "YES Adopted" — RED FLAG. Brigadier must verify: are we genuinely applying knowledge, or were the books not actually relevant? If latter — flag for Ruslan rather than fake progress.

**Budget**: ~30-40 subagent dispatches across phases (5×4 matrix expert dispatches + integrator + Wisdom Loop critic + final critic + M-gates).

---

## §8 Output expected from Bundle 1 (deep prompt MUST require)

### Per-part architecture documents

- `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (~15-25K words)

Each with §A-§N sections per quality bar.

### Schemas

- `shared/schemas/cross-fork-provenance.json` (P1.1)
- `shared/schemas/f-g-r.json` (P6a.1)
- `shared/schemas/stage-gates.yaml` (P6b.1)
- `shared/schemas/awaiting-approval-packet.json` (with `gate_class` per UND-4)

### Configuration files

- `.claude/config/default-deny-table.yaml` (P6b.2)
- `.claude/config/blast-radius-table.yaml` (P6b.3)
- `.claude/config/escalation-taxonomy.yaml` (P6b.5)

### Skill specs (stubs, not implementation)

- `/lint --check-commit-format` (P1.2)
- `/lint --check-citations` (P6a.2)
- (skill stubs as `.md` design docs in `swarm/wiki/skills/<skill-name>.md`)

### Updated cross-references

- Wave A interface cards updated: split Part 6 → Part 6a + Part 6b cards
- Master Plan Draft updated: 10 → 11 parts table, dependency graph regenerated
- Manifest §2 matrix: row 6 split into 6a + 6b

### AWAITING-APPROVAL packet

- `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-XX.md`
- §1 Executive summary / §2 Outcomes / §3 Wisdom Findings rollup / §4 Verification gate results / §5 Open questions / §6 Provenance / §7 Ruslan ack request

### STOP

After AWAITING-APPROVAL packet — STOP. Do NOT auto-launch Bundle 2. Notify Ruslan via tmux output.

---

## §9 Branch + commit discipline

- Work on `claude/jolly-margulis-915d34`
- Commit pattern: `[architecture] Bundle 1 — <part> — <phase>` (e.g., `[architecture] Bundle 1 — Part 1 — integrator draft + Wisdom Loop`)
- Push after each major phase
- Final commit: `[architecture] Bundle 1 AWAITING-APPROVAL — Parts 1 + 6a + 6b architecture, Wisdom Loop applied, M-gates passed`

---

## §10 Operational constraints

1. `unset ANTHROPIC_API_KEY` before invoking claude
2. `ulimit -n 65535` if not already set
3. HD-02 rate limiter N=2 normal mode
4. **Read tool 32MB limit**: for large PDFs use `pages` parameter; do NOT auto-read full books, target relevant chapters only
5. **NO auto-execution of Bundle 2 after Bundle 1** — explicit STOP

---

## §11 What server CC does NOW (you reading this brief)

1. Read this brief fully
2. Read `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` (esp. §4.5)
3. Read `decisions/RUSLAN-WALKTHROUGH-CYCLE-12-WAVE-A-2026-04-27.md` (Ruslan's decisions)
4. Read `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md`
5. Read `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 P1 + §2 P6
6. Read existing brigadier system prompt at `.claude/agents/brigadier.md` (to align deep prompt with brigadier's operational style)
7. Optionally skim 1-2 existing AWAITING-APPROVAL packets for output format

Then **write `prompts/wave-c-bundle-1-deep-prompt-2026-04-28.md`** as a 400-700 line action-ready prompt for brigadier. Include:

- Mission statement (what Bundle 1 is, criticality — "this is THE most important Foundation document, treat with 1 trillion percent responsibility")
- Constitutional inputs (Ruslan's 5 OQ ack + C1 + cross-cuts — section §1 of this brief)
- Bundle 1 scope (Parts 1 + 6a + 6b with bullets — section §2)
- Required reading list with exact paths (section §3)
- Wisdom Application Loop instructions (section §4 — VERBATIM, this is critical)
- Quality bar (section §5 — deep-study 15-25K words, anti-cargo-cult, A.14 edges, F-G-R, provenance, fork-separation)
- Verification gates M1/M2/M3/M4 (section §6)
- ETA + autocheck (section §7)
- Output expected (section §8 — exact paths and structures)
- Branch/commit discipline (§9)
- Operational constraints (§10)
- STOP rule + ack mantra

Commit + push when done. STOP. Notify Ruslan.

---

*End of brief. Mantra: QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. RUSLAN-ACK > BRIGADIER-CONFIDENCE. This is the most important architectural document in Jetix history — every decision compounds.*
