---
title: ROY Brigadier Deep Prompt — Wave C Bundle 1 (Parts 1 + 6a + 6b)
date: 2026-04-28
type: deep-prompt
target: ROY brigadier (.claude/agents/brigadier.md)
parent_brief: prompts/cloud-code-wave-c-bundle-1-prompt-writing-brief-2026-04-27.md
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
bundle_scope: [Part 1 — System State Persistence, Part 6a — Provenance Officer, Part 6b — Human Gate]
estimated_walltime: 12-18h
status: ready-for-brigadier-dispatch
constitutional_baseline: 2026-04-27 Ruslan walkthrough ack on `claude/awesome-gates-bf616d`
mantra: QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. RUSLAN-ACK > BRIGADIER-CONFIDENCE.
---

# Wave C Bundle 1 — ROY Brigadier Deep Prompt

## §0 Mission Statement (READ FIRST, INTERNALIZE)

**This is the most important Foundation document in the history of Jetix.**

Bundle 1 builds the **load-bearing substrate** for everything Phase B / Phase C / Phase D.
Every decision compounds. Every schema you define here becomes a permanent contract
that future ROY cycles, future swarm cells, and future forks must conform to. A weak
F-G-R schema in Part 6a contaminates every promoted claim in the wiki forever. A weak
Default-Deny classifier in Part 6b lets a cargo-cult action slip past the human gate
and corrupt the audit trail. A weak D27 cross-fork provenance in Part 1 makes every
future Phase B partner integration brittle.

**Treat with 1 trillion percent responsibility.**

Read this prompt three times before dispatching any subagent. Read every linked
constitutional artefact in §3 before composing your first dispatch. When in doubt,
ask Ruslan via HITL escalation. When NOT in doubt, ask anyway — overdetermination
is a virtue here.

> *Ruslan emphasis (verbatim, original Russian, do NOT paraphrase before applying):*
> *«Чтобы вся вот эта мудрость, наработки из книг — они были применены в системе,*
> *если это возможно, если нужно, целесообразно — на 1000% насколько это*
> *целесообразно. Ещё чтобы задавались вопросы как мы можем конкретно добавить,*
> *нахуй, эту штуку, чтобы было ещё отдельный прогон где вся эта залупа даёт*
> *обратную связь — а как мы можем это улучшить с точки зрения такой-то книжки*
> *или с книжки такой-то.»*

This is the central directive. The Wisdom Application Loop (§5) is the structural
mechanism that operationalizes it. Skipping or perfunctorily executing the Wisdom
Loop is a constitutional violation.

---

## §1 Constitutional Inputs (Ruslan walkthrough ack 2026-04-27 — IMMUTABLE)

These decisions are LOCKED. Do not re-litigate. Implement.

### §1.1 OQ blockers ACKED (5)

1. **OQ-MERGED-1 — OVERRIDE: SPLIT Part 6** into:
   - **Part 6a — Provenance Officer** (F-G-R, citation enforcement, approval log, quarterly immune audit)
   - **Part 6b — Human Gate** (stage-gate predicates, Default-Deny classifier, blast-radius, AWAITING-APPROVAL packet schema, escalation taxonomy)
   - Reasoning: scale-readiness Phase B/C/D, fork-friendly portable provenance standard, independent change cadence.
   - Implication for Bundle 1: TWO architecture documents in §C scope, NOT one.

2. **OQ-MERGED-2 — Part 5 standalone** (Compound Learning) — engineering-expert dissolve dissent preserved with 3-cycle dissolve-test deferred. **Not Bundle 1, but cross-ref in dependency edges.**

3. **OQ-1 / TRADEOFF-01 — Part 8 = audit lead, Part 6 = enforcement arm.** With split:
   - Part 8 invokes **Part 6a as a service** for provenance check (methodologically-uses edge).
   - Part 6b owns **real-time per-artefact gate** (constrained-by edge from emitters).
   - Bundle 1 references Part 8 at **stub level only** (Part 8 is "specify and stub" Wave C per OQ-MERGED-5).

4. **OQ-3 / UND-1 — Part 5 receives raw task-return packets**, does own DRR extraction.
   - R2 loop ownership clean. Part 1 archives raw packets in append-only log; Part 5 (later bundle) consumes.
   - Bundle 1 implication: Part 1 §B Outputs MUST emit raw task-return packets in stable schema for Part 5 consumption. Schema name placeholder: `task-return-packet.json` (defined in Bundle 3 alongside Part 5 work; Bundle 1 declares the OUTPUT SLOT exists with a frozen field stub).

5. **OQ-MERGED-3 — Wave A scope: fork-separation declared up-front per part**, NOT deferred to Wave C card-by-card.
   - Bundle 1 deliverable: each Part architecture doc has explicit `§X Foundation vs RUSLAN-LAYER` section.

### §1.2 Contradictions ACKED (4)

- **C1 — Variant A: shared infra `swarm/lib/`** with named owner. Scripts `/ingest`, `/ask`, `/consolidate`, `/build-graph`, `/lint` live as **infrastructure layer**, not in Part 3 or Part 4. **Bundle 1 implication**: when Part 6a defines `/lint --check-citations` (Bullet P6a.2) and Part 1 defines `/lint --check-commit-format` (Bullet P1.2), both are described as **extensions of `swarm/lib/`-owned `/lint`**, not as new owned skills. The §H Code-level Interfaces section MUST clarify this.
- **C2 — Part 8 owns canonical health signal schema.** Bundle 3 work. Bundle 1 emitters (Part 1) declare "we emit health signals" but DO NOT specify the schema — that is Part 8 territory. Use placeholder edge `methodologically-uses Part 8.health-signal-schema (specified Bundle 3)`.
- **C3 — Defer to Phase B** (when integrations active). LOW priority. Skip.
- **C4 — Nomenclature fix `PhaseOf` → `methodologically-uses` for Part 9 → Part 6.** Bundle 4. Bundle 1 dependency-graph entries for Part 6a/6b → Part 9 use the new typed edge — do not regress to `PhaseOf`.

### §1.3 Underspec ACKED (5, of which UND-4 is in-scope for THIS bundle)

- **UND-1** = OQ-3 (resolved above)
- **UND-2** — methodology promotion pipeline schema → Bundle 3 (P5 work). Reference at stub level only.
- **UND-3** — P7 → P5 retrospective schema + cadence → Bundle 3 (joint P5/P7). Reference at stub level only.
- **UND-4 — `gate_class` field in STOP gate packet — Bundle 1 P6b work (IN SCOPE).**
  - `gate_class: stop_gate | stage_gate | draft_promotion`
  - Defined in `shared/schemas/awaiting-approval-packet.json` (Bullet P6b.4).
- **UND-5** — CRM edge validation → Bundle 4 (P10 work). Out of scope.

### §1.4 Non-blocking OQs ACKED relevant to Bundle 1

- **OQ-MERGED-6 — Default-Deny classifier MUST live in Part 6b** (FUNDAMENTAL §6.1 hard rule). **Foundation level, not RUSLAN-LAYER.** This is constitutional — generic Foundation owns the FRAMEWORK; specific blast-radius assignments per action class = RUSLAN-LAYER.
- **OQ-MERGED-5 — Part 8 "specify and stub" Wave C, full impl = Phase B.** Bundle 1 MUST treat Part 8 cross-references as stub-level (placeholder schema names, not full specifications).
- **OQ-4 / UND-4** — gate_class field (already covered above).

### §1.5 Cross-cuts within Bundle 1 (apply throughout)

| Cross-cut | Rule | Where applied |
|-----------|------|---------------|
| **IP-1 Role≠Executor** | Part 6a/6b roles are U.Episteme manifests. Executor bindings = RUSLAN-LAYER. | §A Inputs source-ownership; §X fork-separation |
| **A.14 typed edges** | Every dependency uses typed edge. NO generic `depends-on`. | §D Dependencies (every entry) |
| **F-G-R on every claim** | F0-F9 / G ClaimScope / R Reliability tag on every promoted claim. | §G F-G-R Tagging table; inline tags throughout |
| **Append-only logs** | Approval log, audit trail, raw task-return archive — append-only. | §C Side-effects; §I Data schemas; §K Failure modes |
| **L/A/D/E** | Every interface section structured per FPF A.6.B Boundary Norm Square. | §E Boundary (Laws / Admissibility / Deontics / Effects) |
| **Dogfooding** | Bundle 1 docs use F-G-R from start (Part 6a defines, Bundle 1 uses). | §G; §N Provenance |

---

## §2 Bundle 1 Scope — Three Parts, Twelve Bullets

### §2.1 Part 1 — System State Persistence

**Source**: `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` §2 Part 1.
**Interface card**: `.../interface-cards/part-1-system-state-persistence.md` (139 lines).

**Bullet P1.1 — D27 cross-fork provenance schema stub**
- Output: `shared/schemas/cross-fork-provenance.json` + `wiki/methodology/d27-fork-discipline.md`
- Acceptance predicate: schema validates against fork-import test fixture (synthetic Phase B partner case).
- F-G-R: F4 operational convention, G holds-within-Foundation-scope, R-medium.

**Bullet P1.2 — D25 commit-format lint as Foundation artefact**
- Output: `/lint --check-commit-format` skill spec (`swarm/wiki/skills/lint-check-commit-format.md`) + pre-commit hook stub (`tools/git-hooks/pre-commit-format.sh`).
- Acceptance predicate: lint run on last 50 commits produces 0 false positives + flags any malformed commit per D25.
- F-G-R: F3 design-time draft becoming F4 on Ruslan ack, G holds-within-Foundation-scope.

**Bullet P1.3 — `/company-status` + `/knowledge-diff` offline-first guarantee**
- Output: Law invariant declared in Part 1 §E + unit test stubs blocking network calls (`tools/tests/test-offline-guarantee.sh`).
- Acceptance predicate: stubs intercept any `curl|wget|http` syscall during skill execution and assert-fail.
- F-G-R: F4 operational convention, G holds-within-Foundation-scope, R-high (testable).

### §2.2 Part 6a — Provenance Officer (NEW from split)

**Bullet P6a.1 — F-G-R schema definition**
- Output: `shared/schemas/f-g-r.json`
- Fields: Formality (F0..F9 with semantic anchors per FPF), G-ClaimScope (free text + structured `holds_within: [scope-token]`), Reliability (R-low / R-medium / R-high / R-certified).
- Validation rules: every promoted claim in `swarm/wiki/` (canonical) MUST carry F-G-R; drafts MAY omit. Validator script stub.

**Bullet P6a.2 — `[src:filename]` inline citation enforcement scanner**
- Output: `/lint --check-citations` skill spec (`swarm/wiki/skills/lint-check-citations.md`).
- Detect: bare claims missing citation; cargo-cult signals (citation present but no "concrete consequence sentence" within 200 chars per Manifest §5).
- Acceptance predicate: scanner correctly flags 8/10 synthetic cargo-cult test cases.

**Bullet P6a.3 — Approval log structure**
- Output: `swarm/approvals/log.md` append-only schema + entry format spec.
- Every promotion decision logged with: timestamp, actor (Ruslan / brigadier-with-ack), packet-id, gate_class, F-G-R delta, reversibility class.

**Bullet P6a.4 — Quarterly immune audit framework**
- Output: `swarm/audits/quarterly-template.md` + checklist of what to audit (F-G-R drift, citation health, dangling edges, stale claims, cargo-cult signals).
- Coordinates with Part 8 (stub): Part 8 invokes Part 6a as service via `methodologically-uses` edge.

### §2.3 Part 6b — Human Gate (NEW from split)

**Bullet P6b.1 — Stage-gate predicates registry**
- Output: `shared/schemas/stage-gates.yaml`
- Formal predicate definitions (Hamel-binary checklists, NOT prose) for each promotion class (draft → reviewed, reviewed → accepted, accepted → canonical, etc.).
- Aligned with `.claude/config/sg-banned-phrases.yaml` (existing 18 entries — extend if needed).

**Bullet P6b.2 — Default-Deny classifier (FUNDAMENTAL §6.1)**
- Output: `.claude/config/default-deny-table.yaml`
- Every novel action class default-denied unless explicitly whitelisted.
- Foundation framework GENERIC; specific whitelisted action classes for Ruslan = RUSLAN-LAYER.

**Bullet P6b.3 — Blast-radius classification table**
- Output: `.claude/config/blast-radius-table.yaml`
- Tier 0 integrity (auto-halt) / Tier 1 strategic (Ruslan ack) / Tier 2 tactical (batch ack) / Tier 3 routine (auto-log).
- Per OQ-MERGED-6 Foundation level — framework generic.

**Bullet P6b.4 — AWAITING-APPROVAL packet schema**
- Output: `shared/schemas/awaiting-approval-packet.json`
- Fields: `gate_class: stop_gate | stage_gate | draft_promotion` (per UND-4), packet-id, timestamp, actor, summary, outcomes, provenance, ack_request, reversibility_class, blast_radius_tier.

**Bullet P6b.5 — HITL escalation taxonomy**
- Output: `.claude/config/escalation-taxonomy.yaml`
- Routing rules for L1/L2/L3 SLA tiers (per Part 9 OQ).
- Foundation framework; specific SLA values RUSLAN-LAYER.

---

## §3 Required Reading — MANDATORY before first dispatch

Brigadier MUST read these files BEFORE any subagent dispatch. Each pre-read MUST be cited in output. Subagent dispatches MUST instruct experts to read RELEVANT subsets (do NOT dump all to every expert — that triggers cargo-cult).

### §3.1 Constitutional baseline (full-read mandatory)

1. `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0, ~30K words, 35 UC, 12 categories A-L, 55+ anti-scope) — esp. **§6.1 hard rules** (Default-Deny anchor)
2. `design/JETIX-FPF.md` (3758 lines) — IP-1..IP-8, 14 invariants A.1-A.14, Agency-CHR, F-G-R, L/A/D/E **(all dogfooded in Bundle 1 dogfooded — read carefully)**
3. `decisions/AUDIT-CURRENT-STATE-2026-04-27.md` (5758 words) — what's already operational; do not duplicate
4. `decisions/JETIX-FOUNDATION-BUILD-MASTER-PLAN-BRIEF-2026-04-27.md` — esp. **§4.5 deep-study constraint** (15-25K words per part doc)
5. **Locks D1-D29 + 4 LOCKS-ADDENDUMs** — focus on:
   - **D17** (FPF anchor)
   - **D25** (commit-format law — Bullet P1.2)
   - **D26** (offline-first — Bullet P1.3)
   - **D27** (cross-fork provenance — Bullet P1.1)
   - **D28** (gates discipline)
   - **D29** (most recent addendum — `decisions/LOCKS-D29-ADDENDUM-2026-04-26.md`)

### §3.2 Wave A artefacts (full-read mandatory)

1. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md` (5569 words, 428 lines)
2. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md`
3. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md`
4. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/wave-c-worklist.md` (705 lines, 34 bullets) — esp. §2 Part 1 (lines 60-98) + §2 Part 6 (lines 300-360)
5. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md`
6. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/M1-smoke-test.md` / `M2-cross-reference.md` / `M3-scenario-walkthroughs.md` (gate templates)
7. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-1-system-state-persistence.md` (139 lines)
8. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/interface-cards/part-6-governance-provenance-human-gate.md` (133 lines) — **TO BE SPLIT into 6a + 6b in this bundle**
9. `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/` (5 files: engineering, investor, mgmt, philosophy, systems)

### §3.3 Wave B consultant cards (Bundle 1 anchors — see Manifest §2 matrix)

**For Part 1 dispatches** (engineering + investor + systems experts):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-3 artifacts-over-conversations, D25 git-as-event-log
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md` — Lindy substrate, margin-of-safety
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/unix-philosophy.md` — plain-text, everything-is-a-commit
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/event-sourcing-cqrs.md` — git-as-event-log, append-only, Reversal Transactions
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/clean-code.md` — Ousterhout deep-modules

**For Part 6a Provenance Officer dispatches** (philosophy + investor + engineering):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — B.3 F-G-R triad, A.14 typed edges, IP-4 FPF-Steward
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` — provenance + transparency as constitutional
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/mereology-typed-edges.md` — typed edges for provenance graph

**For Part 6b Human Gate dispatches** (mgmt + philosophy + engineering + investor + systems):
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/anthropic-constitutional-ai.md` — Default-Deny + hardcoded-never-list, RLAIF self-critique → fail-loud, RSP ASL-tier blast-radius
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/levenchuk-shsm-fpf.md` — IP-4 immune system function, Agency-CHR A.13 J-level matrix
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/sre-observability.md` — fail-loud P6, error-budget behaviour change for integrity SLOs
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/capital-allocation-antifragility.md` — Graham margin-of-safety: over-engineer governance, blast radius unbounded
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/stoic-epistemic.md` — Dichotomy-of-control: gate governs what is in Ruslan's control

### §3.4 Wave B Supplement library-direct sources (MANDATORY per Ruslan emphasis)

These 5 sources were freshly added 2026-04-27. **ROY MUST read and apply** in the Wisdom Loop. Lifted cards: #5 (Event Sourcing) F3→F4, #6 (SRE) F3→F5, #13 (CAI) F3→F4. Lifts must be carried into architecture.

1. `raw/books-md/anthropic/bai-2022-cai.md` — RLAIF self-critique, 16+16 SL/RL-CAI principles
2. `raw/books-md/anthropic/askell-2021-hhh.md` — HHH framework formal definitions
3. `raw/books-md/event-sourcing/young-cqrs-2010.md` — CQRS canonical (commands-imperative, **no-delete via Reversal Transactions**, aggregate-id partition, optimistic concurrency)
4. `raw/books-md/sre/google-sre-book.md` — SLI/SLO/error-budget, **Four Golden Signals**, blameless postmortems, cascading failures
5. `raw/books-md/sre/google-srewb-implementing-slos.md` — burn-rate algebra (1×/6×/14.4×)

**Read tool 32MB limit**: for the larger SRE Book, use `pages` parameter to target relevant chapters; do NOT auto-read full book. Target: Chap 4 (SLOs), Chap 6 (Monitoring), Chap 15 (Postmortems), Chap 22 (Cascading Failures).

### §3.5 Existing operational artefacts (audit reference, do not duplicate)

1. `swarm/lib/shared-protocols.md` — current protocol layer (C1 shared infra owner)
2. Existing `decisions/AWAITING-APPROVAL-*` packets (8 of them) — pattern reference for §8 output:
   - `decisions/AWAITING-APPROVAL-foundation-master-plan-cycle-12-wave-a-2026-04-28.md` (canonical recent example)
   - `decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md` (most recent, 7-section structure)
3. `.claude/config/sg-banned-phrases.yaml` — current 18-entry stage-gate banned list (extend in P6b.1 if needed)
4. **Walkthrough tracker** (Ruslan ack record, on different branch):
   - `git show origin/claude/awesome-gates-bf616d:decisions/RUSLAN-WALKTHROUGH-CYCLE-12-WAVE-A-2026-04-27.md`

---

## §4 Phase Architecture (matrix dispatch + Wisdom Loop + critic gate)

Standard ROY cycle = **integrator → critic → finalize**. **For Bundle 1, brigadier MUST insert a structural Wisdom Application Phase between integrator and critic, per §5.** Per part. Three parts × full-cycle = three full passes.

### §4.1 Phase sequence per part

For each Part (1, 6a, 6b) execute in this order:

1. **Phase A — Pre-read confirmation** — brigadier reads §3 mandatory; dispatch instructs each expert to read RELEVANT subset only (per §3.3 mapping).
2. **Phase B — Matrix dispatch (5 experts × 4 modes = up to 20 cells)** — per ROY-ALIGNMENT §3 row mapping. Not every cell fires; brigadier picks cells that genuinely add signal. Minimum 8 cells per part.
3. **Phase C — Integrator** — brigadier (or delegated integrator-mode expert) merges cell outputs into draft architecture per §6 quality bar.
4. **Phase D — Wisdom Application Loop** — see §5. **THIS IS THE CRITICAL NEW PHASE.**
5. **Phase E — Critic gate** — ≥2 experts in critic-mode review draft + Wisdom edits. Stricter cargo-cult check.
6. **Phase F — Finalize** — brigadier promotes draft → canonical at `swarm/wiki/foundations/<part-slug>/architecture.md`.
7. **Phase G — M-gates per part** — M1 smoke, M2 cross-ref. (M3 + M4 run at bundle level in §7.)

### §4.2 Cell selection guidance per part

**Part 1**: engineering (critic + scalability + integrator), investor (long-term-compounding), systems (cybernetics + emergence), mgmt (boundary), philosophy (epistemic audit). Minimum 8 cells.

**Part 6a**: philosophy (epistemic audit + first-principles), investor (capital-allocation), engineering (clean-code + critic), systems (Meadows leverage), mgmt (delivery boundary). Minimum 8 cells.

**Part 6b**: mgmt (prioritization + ethics-surface + integrator), philosophy (Stoic dichotomy + ethics surface + critic), engineering (scalability), investor (margin-of-safety + critic), systems (requisite-variety). Minimum 10 cells (this is the heaviest part — Default-Deny is constitutional FUNDAMENTAL §6.1).

### §4.3 Dissent preservation (AP-6)

If any expert in critic-mode produces dissent that integrator could not resolve: preserve in `swarm/wiki/foundations/<part-slug>/dissent.md` with the structure (claim / dissenter / reason / proposed-resolution). Do NOT silently override expert domain judgment (E-15).

---

## §5 THE WISDOM APPLICATION LOOP (Phase D — central directive)

**This phase is constitutional. Skipping it is a violation.**

After integrator produces draft architecture for Part X, brigadier dispatches a dedicated **Wisdom Loop pass**. This pass is:

### §5.1 Procedure

For each consultant card relevant to this part (per §3.3 mapping) AND each library-direct supplement source (§3.4):

Ask FIVE questions, in order, in writing, with traceable answers:

1. **Question 1 — Application Gap**: "What does this consultant card say that the current draft DOES NOT yet apply, but would benefit from?"
2. **Question 2 — Cargo-Cult Audit**: "Are there principles from this card we cited but did not actually apply (cargo-cult risk per Manifest §5)?"
3. **Question 3 — Concrete Improvement**: "Is there a concrete improvement to the architecture if we apply principle X from this card?"
4. **Question 4 — Section Impact**: "If we DO apply this improvement — what changes in §A Inputs / §B Outputs / §C Side-effects / §D Dependencies / §E Boundary / §F Anti-scope?"
5. **Question 5 — Phase A Justification**: "Is the application JUSTIFIED for current Phase A scope (single-owner, Phase 1 €50K horizon)? Or is it premature optimization for Phase B/C/D scale?"

### §5.2 Output format — Wisdom Findings table per part

Embedded in §M of the part architecture document:

```markdown
### Wisdom Application Findings — Part X

| Card / Source | Principle | Current draft state | Improvement opportunity | Adopted? | Justification | Section edited |
|---------------|-----------|---------------------|--------------------------|----------|---------------|----------------|
| #1 Левенчук SHSM-FPF | IP-3 artifacts-over-conversations | already applied | — | n/a | already in §C | n/a |
| #5 Event Sourcing (Young 2010) | Reversal Transactions (no-delete) | NOT applied | Add explicit no-delete law to §F Anti-scope referencing Reversal pattern; commits use `git revert` not `git reset --hard` | YES | Phase A — Foundation must commit to no-delete from start | §F + §E Laws |
| #6 SRE Book | Four Golden Signals | partial (only latency mentioned) | Add traffic / errors / saturation as Part 8 audit signals Part 1 emits | YES | Affects Part 8 cross-ref design (Bundle 3 stub) | §B + §D |
| #6 SRE Workbook | Burn-rate algebra (1×/6×/14.4×) | not applied | Use burn-rate triggers in P6b.3 blast-radius classification | YES (P6b only) | Phase A — burn-rate is testable now | §H schema |
| #13 CAI (Bai 2022) | RLAIF self-critique | partial | Add RLAIF-style self-critique to /lint --check-citations BEFORE flagging cargo-cult, to reduce false positives | YES | Phase A — improves Bullet P6a.2 directly | §H skill spec |
| #13 CAI | ASL-tier blast radius | not applied | Map blast-radius Tier 0-3 to ASL-1..ASL-4 conceptually for portability | NO | Phase B work — premature now | n/a |
| #14 Stoic | Dichotomy-of-control | applied | — | n/a | gate scope already aligned to Ruslan's locus | n/a |
| ... library-direct ... | ... | ... | ... | ... | ... | ... |
```

### §5.3 Discipline (HARD RULES)

**Brigadier MUST**:
- Run Wisdom Loop AFTER integrator, BEFORE critic gate
- Produce findings table (§M) per part
- Apply every "YES Adopted" edit to draft BEFORE critic gate runs
- Critic gate then verifies: did Wisdom edits hold? Anti-cargo-cult check stricter than usual.
- For each YES Adopted entry, the edit MUST be visible in §A-§L diff (not just claimed in table).
- For each NO entry, the justification MUST be one of the legitimate categories: `Phase B work` / `Phase C+ scale` / `premature optimization` / `requires RUSLAN-LAYER decision Ruslan hasn't made` / `domain-orthogonal to this part`. Vague "not applicable" is INSUFFICIENT.

**Brigadier MUST NOT**:
- Skip Wisdom Loop because "draft seems fine"
- Reject improvement opportunities without explicit justification from the legitimate categories
- Adopt every improvement without Phase A justification (Phase B+ ideas DEFER, do not balloon scope)
- Treat the loop as paperwork — every YES is a real edit, every NO is a real reasoned defer.

### §5.4 Failure mode

**If Wisdom Application Loop produces 0 "YES Adopted" across all relevant cards for a part:**
RED FLAG. This is highly unlikely if cards are genuinely relevant. Brigadier MUST verify:
- Are we genuinely applying knowledge, or did integrator pre-empt the loop by applying principles in Phase C? (acceptable — but make the table reflect "already applied" with traceable §C entry)
- OR: were the books not actually relevant? (rare — flag for Ruslan rather than fake progress)
- DO NOT fabricate YES entries to satisfy the loop. False positives in Wisdom Loop are worse than zero adoption — they corrupt the audit trail.

If genuinely 0 adoption: **HALT, write `swarm/wiki/foundations/<part-slug>/wisdom-loop-zero-adoption-flag.md` with reasoning, escalate to Ruslan via tmux output before proceeding to critic gate.**

### §5.5 Why this matters

This loop is the structural mechanism that prevents:
- Cargo-cult citation (citing without applying — books sit unread on the shelf)
- Knowledge sitting unused in `raw/books-md/` despite being processed in Wave B Supplement
- ROY producing "good enough" architecture that ignores hard-won wisdom from 14 consultant cards + 5 library-direct sources

Ruslan invested 2 cycles building Wave B + Wave B Supplement specifically so this wisdom is available. Bundle 1 is the FIRST bundle to consume it. Setting the precedent here defines the discipline for Bundles 2/3/4.

---

## §6 Quality bar (per Master Plan Brief §4.5 deep-study constraint)

### §6.1 Document size

Each Part architecture document MUST be **15-25K words minimum** (~150-250KB markdown). Not 2-5K. Not "interface card extended". DEEP architecture document.

If draft comes in under 15K words: brigadier returns to integrator with explicit feedback "you delivered N words; quality bar is 15-25K — re-dispatch with §A-§N expansion mandate."

If draft comes in over 25K words: review for redundancy + cargo-cult padding. Tighten before Wisdom Loop.

### §6.2 Section structure (every part doc has §A through §N)

| Section | Content | Notes |
|---------|---------|-------|
| **§A Inputs** | data shapes, event triggers, source ownership | typed and complete |
| **§B Outputs** | data shapes, consumer parts, side-effects | typed and complete |
| **§C Side-effects** | filesystem writes, schema validations, log entries | exhaustive list |
| **§D Dependencies** | typed A.14 edges, with rationale per edge | NO `depends-on` generic |
| **§E Boundary** | L/A/D/E lanes — Laws / Admissibility / Deontics / Effects | per FPF A.6.B |
| **§F Anti-scope** | generic + part-specific — what this part does NOT do | explicit |
| **§G F-G-R Tagging** | table of every artefact emitted with F-G-R values + rationale | dogfooded |
| **§H Code-level interfaces** | CLI commands, skills, file paths, schemas | concrete |
| **§I Data schemas** | full YAML/JSON specs for any new schema | inline + linked |
| **§J Operational rituals** | cadence, triggers, exception handling | concrete |
| **§K Failure modes** | what breaks, how detected, how recovered | exhaustive |
| **§L Wave C work-list bullet status** | each P-bullet from worklist mapped to specific output | acceptance predicate ✅/❌ |
| **§M Wisdom Application Findings** | table from Phase D (see §5) | full table |
| **§N Provenance** | every claim traces to inline `[src:filename]` citation | M2-verified |
| **§X Foundation vs RUSLAN-LAYER** | fork-separation declared explicitly per OQ-MERGED-3 | required |

### §6.3 Anti-cargo-cult enforcement (CRITICAL)

Per Wave B Manifest §5 detection rule:
> If a citation appears in an interface card without a "concrete consequence sentence" AND without a specific Wave C work-list bullet that references it → flag as cargo-cult, return for re-dispatch.

**Bundle 1 enforcement**:
- Every `[src:...]` citation MUST be followed within 200 chars by a concrete consequence sentence. Example: "...therefore Part 1 §E Laws state: 'No --amend on canonical branch' [src:design/JETIX-FPF.md L1234]". The consequence sentence is the operational change driven by the source.
- `/lint --check-citations` (Bullet P6a.2) MUST be designed to AUTO-detect cargo-cult signals — this is dogfooded enforcement for future cycles.
- Critic gate MUST reject any §A-§N section with cargo-cult violations and return to integrator with line-number-specific feedback.

### §6.4 Typed A.14 edges everywhere (HARD RULE)

Every §D Dependencies entry MUST be one of the canonical edge types (per A.14 invariant + C4 fix):

| Edge type | Meaning | Example use in Bundle 1 |
|-----------|---------|--------------------------|
| `ComponentOf` | part of the whole | Part 6a is ComponentOf Part 6 (parent governance role) |
| `ConstituentOf` | material constituent | F-G-R schema is ConstituentOf canonical wiki entries |
| `PortionOf` | quantitative portion | (rare in Bundle 1) |
| `PhaseOf` | temporal phase | (forbidden for Part 9 → Part 6 per C4) |
| `MemberOf` | class membership | Part 6b is MemberOf governance-cluster |
| `AspectOf` | aspect | citation enforcement is AspectOf provenance discipline |
| `creates` | produces artefact in | Part 1 `creates` raw-task-return-packet for Part 5 |
| `operates-in` | operates within substrate | Part 1 `operates-in` git substrate (D27) |
| `methodologically-uses` | uses as methodology service | Part 8 `methodologically-uses` Part 6a quarterly audit framework |
| `constrained-by` | constrained by audit/governance | every emitter `constrained-by` Part 6b gate |
| `derives-from` | derives state from | `/knowledge-diff` derives-from git log |

**NO `depends-on`. NO `uses` generic. Critic gate auto-rejects.**

### §6.5 F-G-R on every promoted claim (dogfooded)

Every architecture claim MUST have F-G-R tag. Format: `[F4|G:holds-within-Foundation-scope|R-medium]` inline OR table entry in §G.

- F0-F9 Formality (F0 = personal hunch, F4 = operational convention, F9 = constitutional)
- G ClaimScope (e.g., "holds within Phase A single-owner scope" / "holds within Foundation scope" / "holds within RUSLAN-LAYER")
- R Reliability (R-low / R-medium / R-high / R-certified)

This is dogfooding — Part 6a.1 defines F-G-R, but Bundle 1 docs use F-G-R from start. Coordinate so the schema in §I matches the inline tags.

### §6.6 Provenance trail

Every claim → `[src:path]` inline citation → resolves to existing file + section. M2 cross-reference gate (§7.2) verifies 100% citation resolution. No broken citations allowed.

### §6.7 Foundation vs RUSLAN-LAYER discipline (per OQ-MERGED-3)

Each Part architecture MUST have explicit **§X Foundation vs RUSLAN-LAYER fork-separation** section declaring:

- What is **generic Foundation** (any forkable Jetix instance — partner, alumni, hypothetical Phase B fork)
- What is **RUSLAN-LAYER** (Ruslan's specific config — DACH ICP, executor bindings, German GDPR config, branch names, Notion IDs, etc.)
- Where the boundary is (interfaces, plug-points, config tokens that an importer must override)

For Bundle 1 specifically:
- **Part 1 fork-separation**: D27 cross-fork provenance schema is GENERIC. Specific repo/branch names = RUSLAN-LAYER.
- **Part 6a fork-separation**: F-G-R schema GENERIC. Specific governance roles (who is the Provenance Officer human) = RUSLAN-LAYER.
- **Part 6b fork-separation**: Default-Deny classifier framework GENERIC. Specific blast-radius assignments per action class = RUSLAN-LAYER. AWAITING-APPROVAL packet schema GENERIC. SLA values in escalation taxonomy = RUSLAN-LAYER.

---

## §7 Verification Gates (M1 / M2 / M3 / M4)

### §7.1 M1 Smoke Test (per part, threshold ≥90%)

Check each Part architecture doc:
- [ ] All §A-§N + §X sections populated (no "TBD" placeholders, no "to be filled later")
- [ ] Word count ≥15K (not under bar)
- [ ] Dependencies (§D) all typed per §6.4
- [ ] F-G-R tags (§G) present on every promoted claim
- [ ] Wave C bullets from §2 all mapped in §L with acceptance predicate ✅/❌
- [ ] §X Fork-separation section explicit
- [ ] No cargo-cult signals (citation without consequence sentence within 200 chars)

Pass threshold: ≥90% bullets ticked. Per part. Failure: re-dispatch integrator with specific gap list.

### §7.2 M2 Cross-reference (per part, threshold 100%)

- [ ] Every `[src:...]` resolves to an existing file
- [ ] Every cited section anchor resolves to an actual section heading
- [ ] No broken inline citations
- [ ] No dangling typed-edge targets in §D (every edge target exists)

Pass threshold: 100%. Failure: integrator fixes citations OR escalates if cited file missing.

### §7.3 M3 Scenario Walkthroughs (bundle-level, 4 scenarios MUST pass)

Run each scenario end-to-end against the Bundle 1 interfaces. Document trace in `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/M3-walkthroughs.md`.

**Scenario 1 — Full information lifecycle:**
voice memo → `/ingest` → STOP gate (Part 6b) → Part 6a F-G-R tag assignment → Part 6b gate ack (AWAITING-APPROVAL packet) → Part 1 commit (D25 format-checked) → wiki entry (with citation) → Part 6a citation lint pass.
End-to-end via Bundle 1 interfaces. Verify each handoff schema is defined.

**Scenario 2 — Strategic decision:**
Ruslan ack of AWAITING-APPROVAL packet → Part 6b gate decision (gate_class=stage_gate) → Part 6a approval log entry → Part 1 LOCKED commit. Audit trail reconstructable: from log entry, reconstruct who decided what when on which packet referencing which sources at which F-G-R levels.

**Scenario 3 — Quarterly immune audit:**
Part 8 (stub) invokes Part 6a quarterly audit (`methodologically-uses` edge) → Part 6a checks F-G-R compliance across wiki entries → flags drift (e.g., F4 claims drifting to R-low without R re-audit) → Part 6b decides remediation (Default-Deny override or proceed). Cross-bundle reference (Part 8 stub level acceptable).

**Scenario 4 — Fork-separation test:**
Hypothetical Phase B fork — partner imports Part 1 D27 schema + Part 6a F-G-R schema (generic), declines Part 6b Default-Deny rules (their own Default-Deny). Foundation vs RUSLAN-LAYER boundary holds: every Foundation-tagged artefact imports cleanly; every RUSLAN-LAYER-tagged artefact is replaceable by partner config.

Pass threshold: 4/4 scenarios trace cleanly with no missing schemas or undefined handoffs. Failure: re-architect specific gaps; do NOT paper over with TODO stubs.

### §7.4 M4 Wisdom Application Loop verification (NEW for Bundle 1)

Per part:
- [ ] §M Wisdom Findings table populated (not empty, not 0 adoption — see §5.4)
- [ ] Every "YES Adopted" entry has corresponding visible edit in §A-§L (verify by line-number diff trace)
- [ ] Every "NO" entry has explicit justification from legitimate categories (§5.3)
- [ ] No fabricated YES entries (cross-check: edit actually exists in target section)
- [ ] All 14 Wave B consultants + 5 supplement sources covered for at least one of {Part 1, Part 6a, Part 6b} (no card silently skipped)

Pass threshold: all bullets ticked per part. Failure: re-run Wisdom Loop with specific gap list.

---

## §8 Output Expected (exact paths, structures)

### §8.1 Per-part architecture documents

- `swarm/wiki/foundations/part-1-system-state-persistence/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-6a-provenance-officer/architecture.md` (~15-25K words)
- `swarm/wiki/foundations/part-6b-human-gate/architecture.md` (~15-25K words)

Each with §A-§N + §X sections per §6.2.
Each with YAML frontmatter (per Global Rule 1, conventions in `_meta/conventions.md`).

### §8.2 Schemas (canonical artefacts)

- `shared/schemas/cross-fork-provenance.json` (P1.1) — JSON Schema draft-07
- `shared/schemas/f-g-r.json` (P6a.1) — JSON Schema draft-07
- `shared/schemas/stage-gates.yaml` (P6b.1) — Hamel-binary checklists
- `shared/schemas/awaiting-approval-packet.json` (P6b.4) — with `gate_class` enum per UND-4

### §8.3 Configuration files

- `.claude/config/default-deny-table.yaml` (P6b.2) — generic framework
- `.claude/config/blast-radius-table.yaml` (P6b.3) — generic framework
- `.claude/config/escalation-taxonomy.yaml` (P6b.5) — generic framework

### §8.4 Skill specs (design docs, not implementations)

- `swarm/wiki/skills/lint-check-commit-format.md` (P1.2)
- `swarm/wiki/skills/lint-check-citations.md` (P6a.2)

Skill specs are `.md` design documents covering: trigger, inputs, outputs, side-effects, failure modes, fork-separation. NOT implementations.

### §8.5 Pre-commit hook stub (P1.2)

- `tools/git-hooks/pre-commit-format.sh` — stub script invoking `/lint --check-commit-format` against staged commit message.

### §8.6 Test stubs (P1.3)

- `tools/tests/test-offline-guarantee.sh` — stub blocking network calls during `/company-status` + `/knowledge-diff`.

### §8.7 Templates (P6a.4)

- `swarm/audits/quarterly-template.md` — quarterly immune audit checklist template.

### §8.8 Updated Wave A artefacts

- Wave A interface cards updated: split `interface-cards/part-6-governance-provenance-human-gate.md` → `interface-cards/part-6a-provenance-officer.md` + `interface-cards/part-6b-human-gate.md`.
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/MASTER-PLAN-DRAFT.md` updated: 10 → 11 parts table, dependency graph regenerated.
- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/dependency-graph.md` updated to reflect split.
- Wave B Manifest §2 matrix: row 6 split into 6a + 6b.

### §8.9 Walkthroughs trace

- `swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-c/bundle-1/M3-walkthroughs.md` — all 4 scenarios traced.

### §8.10 Bundle-level dissent (if any)

- `swarm/wiki/foundations/<part-slug>/dissent.md` per part with unresolved critic dissent (AP-6 preservation).

### §8.11 AWAITING-APPROVAL packet (FINAL deliverable)

- `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-XX.md` (XX = day of completion).

Structure (per §8.11.1) — match the format of `decisions/AWAITING-APPROVAL-wave-b-supplement-2026-04-27.md`:

#### §8.11.1 AWAITING-APPROVAL packet structure

```markdown
---
title: AWAITING-APPROVAL — Wave C Bundle 1 (Parts 1 + 6a + 6b)
date: 2026-04-XX
type: awaiting-approval
cycle: cyc-foundation-build-2026-04-28
wave: C
bundle: 1
status: awaiting-ruslan-ack
---

## §1 Executive Summary
[3-5 paragraphs: what was built, key decisions, headline numbers (word counts, schemas defined, edges typed, F-G-R tags applied), Wisdom Loop adoption count.]

## §2 Outcomes — F-level changes
[Table: Artefact / F-before / F-after / Drift rationale]

## §3 Wisdom Findings Rollup
[Aggregate table across Parts 1 + 6a + 6b: Total YES Adopted / Total NO with reason categories / Per-card coverage matrix]

## §4 Verification Gate Results
- M1 Smoke: Part 1 X% / Part 6a X% / Part 6b X%
- M2 Cross-ref: 100% (or list broken citations)
- M3 Scenarios: 4/4 PASS (or list failures)
- M4 Wisdom: PASS (or gap list)

## §5 Open Questions Surfaced By Bundle 1
[Any new OQs beyond the 5 ACKED — with proposed resolution / defer rationale]

## §6 Provenance
[List of every source consulted, with F-G-R, with consequence sentences cross-ref]

## §7 Ruslan Ack Request
[Specific decisions Ruslan must ack before Bundle 2 dispatches:
 - Part 6 split into 6a + 6b: schemas locked? F-G-R schema canonical?
 - Default-Deny framework Foundation level confirmed?
 - Blast-radius tier definitions confirmed?
 - AWAITING-APPROVAL packet schema (with gate_class) frozen for all future packets?
 - Any per-part dissent items: Ruslan resolves]

## §8 STOP — Do not auto-launch Bundle 2
Per §11 STOP rule.
```

---

## §9 Branch + Commit Discipline

- **Branch**: `claude/jolly-margulis-915d34` (current). Do NOT create new branches.
- **Commit cadence**: small + frequent. After each major phase (Phase B per part / Phase C per part / Phase D per part / Phase F finalize per part / M-gates / AWAITING-APPROVAL packet).
- **Commit message format**: `[architecture] Bundle 1 — <part> — <phase>` examples:
  - `[architecture] Bundle 1 — Part 1 — Phase C integrator draft`
  - `[architecture] Bundle 1 — Part 1 — Phase D Wisdom Loop applied (5 YES / 3 NO)`
  - `[architecture] Bundle 1 — Part 6a — Phase E critic gate PASS`
  - `[architecture] Bundle 1 — Part 6b — Phase F finalized + M1/M2 PASS`
  - `[architecture] Bundle 1 — M3 walkthroughs 4/4 PASS`
  - `[architecture] Bundle 1 AWAITING-APPROVAL — Parts 1 + 6a + 6b architecture, Wisdom Loop applied, M-gates PASS`
- **Push cadence**: after each commit. No force-push. No `--amend`. No `--no-verify`.
- **API-key audit**: before each commit run `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY|sk-ant-' <staged-files>` → 0 hits required (per CLAUDE.md KM MVP discipline).

---

## §10 Operational Constraints

1. `unset ANTHROPIC_API_KEY` before any provider invocation. Operator unsets at session start; brigadier MUST NOT reference any provider API-key env var in any code path it produces.
2. `ulimit -n 65535` if not already set (high file-handle ceiling for parallel Task() dispatches).
3. **HD-02 rate limiter N=2 normal mode**. Maximum 2 concurrent Task() dispatches. Sequential is fine for safety.
4. **Read tool 32MB limit**: for large PDFs use `pages` parameter; do NOT auto-read full books, target relevant chapters only. Chapter targets for SRE Book given in §3.4.
5. **NO auto-execution of Bundle 2 after Bundle 1** — explicit STOP per §11.
6. **No `--amend`, no `--no-verify`, no force-push** — git-native rollback via `git revert` only.
7. **Frontmatter compliance**: every `.md` artefact carries YAML frontmatter per the relevant `swarm/wiki/_templates/<type>.md` template. No exceptions.
8. **Untouchable trees in Phase A**: 14 legacy `.claude/agents/*.md` files (crazy-agent / inbox-processor / knowledge-synth / life-coach / manager / meta-agent / personal-assistant / sales-* / staging-writer / strategist / sweep-worker / system-admin) and the v2 `wiki/` tree. v2↔v3 bridge is `cross-tree-ref` edge type only (D3 §3.2.12), recorded in `swarm/wiki/graph/cross-tree.jsonl`.
9. **Security — never touch**: `~/.ssh/`, `/etc/`, any `.env*`, anything under `private/`, Tier-4 closed-core book corpus.
10. **Working directory**: `/home/ruslan/jetix-os/`. Do not `cd` outside.

---

## §11 STOP Rule + Ack Mantra

### §11.1 STOP rule

After AWAITING-APPROVAL packet (`§8.11`) is committed and pushed:

**STOP. DO NOT auto-launch Bundle 2.**

Bundle 2 (Parts 2 + 7) will only dispatch AFTER Ruslan reviews and acks Bundle 1 AWAITING-APPROVAL packet. Brigadier waits for HITL signal.

Final action: notify Ruslan via tmux output (or stdout if no tmux):

> «Wave C Bundle 1 complete. AWAITING-APPROVAL packet at `decisions/AWAITING-APPROVAL-wave-c-bundle-1-2026-04-XX.md`.
> Word count summary: Part 1 = N, Part 6a = N, Part 6b = N. Wisdom Loop adoption: N YES / N NO.
> M1/M2/M3/M4 gates: PASS / PASS / 4/4 PASS / PASS.
> Awaiting Ruslan ack before Bundle 2 dispatch.»

### §11.2 Autocheck — when to halt early

Per Master Plan Brief autocheck rules:

- **Walltime exceeds 24h**: STOP, report status to Ruslan, ask how to proceed. Do NOT push through past 24h without ack.
- **Subagent first attempt produces low-quality output** (cargo-cult signals, missing sections, under word count): re-dispatch ONCE with explicit feedback citing this prompt's quality bar. If second attempt also fails: escalate to Ruslan.
- **Wisdom Application Loop produces 0 "YES Adopted" for a part**: per §5.4, halt + flag + escalate. Do NOT fabricate YES entries.
- **Critic gate produces irreconcilable dissent across ≥2 experts**: preserve dissent (AP-6) + escalate to Ruslan via dissent.md. Do not silently override.
- **Schema design produces ambiguity that requires RUSLAN-LAYER decision**: pause, write `swarm/wiki/foundations/<part-slug>/oq-bundle-1-N.md`, escalate.

### §11.3 Budget

~30-40 subagent dispatches across phases (5×4 matrix × 3 parts × dispatched cells + integrators + Wisdom Loop pass + critic gates + M-gates). Budget guard: if dispatch count exceeds 50, audit for redundant cells; if exceeds 60, halt and ask Ruslan.

### §11.4 Mantra (recite before each phase transition)

> **QUALITY > SPEED.**
> **PROVENANCE > VOLUME.**
> **WISDOM-APPLIED > WISDOM-CITED.**
> **RUSLAN-ACK > BRIGADIER-CONFIDENCE.**
>
> *This is the most important architectural document in Jetix history. Every decision compounds for Phase B/C/D. Treat with 1 trillion percent responsibility.*

---

## §12 Pre-flight Checklist (brigadier runs before first dispatch)

- [ ] Read this prompt three times
- [ ] Read all of §3.1 Constitutional baseline
- [ ] Read all of §3.2 Wave A artefacts
- [ ] Read relevant subsets of §3.3 (per part — see §3.3 mapping)
- [ ] Read §3.4 Wave B Supplement library-direct sources (5 files; SRE Book pages-targeted)
- [ ] Skim §3.5 existing operational artefacts
- [ ] Verify branch `claude/jolly-margulis-915d34` is current and clean (or carries only intended modifications)
- [ ] Verify `unset ANTHROPIC_API_KEY` (operator should have done this; verify no env var leakage in code paths brigadier produces)
- [ ] Verify `swarm/lib/shared-protocols.md` consulted (re-read at start of each Task() per brigadier core memory rule)
- [ ] Acknowledge §0 Mission Statement and §11.4 Mantra internally before first dispatch
- [ ] Confirm dispatch sequence: Part 1 → Part 6a → Part 6b (or parallel within HD-02 N=2 cap)
- [ ] Confirm output paths in §8 are mkdir-ready (parent dirs exist or will be created)

When all bullets ticked: dispatch Phase A pre-read confirmation. Then proceed.

---

## §13 Reference — what NOT to do

This section is short but constitutional. Read carefully.

1. **DO NOT skip the Wisdom Application Loop.** It is the central directive. Skipping it is a violation, not a shortcut.
2. **DO NOT auto-launch Bundle 2.** Always STOP after Bundle 1 AWAITING-APPROVAL.
3. **DO NOT fabricate Wisdom YES entries** to satisfy the loop. Zero adoption with reasoning > fake adoption.
4. **DO NOT use generic `depends-on` edges.** A.14 typed edges only.
5. **DO NOT cite without consequence sentence within 200 chars.** Cargo-cult is the failure mode this whole architecture exists to prevent.
6. **DO NOT exceed 25K words per part doc with redundancy padding.** Tighten before critic.
7. **DO NOT come in under 15K words per part doc.** Re-dispatch integrator.
8. **DO NOT silently override expert dissent.** Preserve in dissent.md.
9. **DO NOT touch the Untouchable trees** (§10.8) or Security paths (§10.9).
10. **DO NOT push to `main`.** Branch `claude/jolly-margulis-915d34` only.
11. **DO NOT use `--amend` / `--no-verify` / force-push.**
12. **DO NOT reference any provider API-key env var** in code paths brigadier produces (Operator security policy).
13. **DO NOT confuse Foundation with RUSLAN-LAYER.** §X section is mandatory.
14. **DO NOT defer UND-4 (`gate_class` field).** This bundle owns it.
15. **DO NOT specify Part 8 health-signal schema.** That is Bundle 3 work. Stub-level reference only.

---

## §14 Final note from Ruslan (paraphrased intent, brigadier internalize)

Bundle 1 is the inflection point. From here on:
- Every Foundation document is judged against the standard Bundle 1 sets.
- Every Wisdom Loop in future bundles is benchmarked against Bundle 1's adoption discipline.
- Every fork (Phase B partner, Phase C product, Phase D org) imports the schemas Bundle 1 freezes.

If Bundle 1 is half-baked, every downstream bundle compounds the weakness. If Bundle 1 is over-engineered with Phase B concerns, Phase A delivery drags.

The right level: **single-owner Phase A €50K horizon, but FORK-READY to scale**. F-G-R schema canonical. Default-Deny framework constitutional. AWAITING-APPROVAL packet schema permanent contract. D27 cross-fork provenance opens the door for partners without forcing premature commitment.

This is the architecture document Ruslan will reread for years. Make it the document a Phase B partner can read in 90 minutes and import in a day. Make it the document a future ROY cycle can extend without re-architecting. Make it the document that proves Wave B + Wave B Supplement wisdom was actually applied — not cited.

---

*End of deep prompt. Brigadier dispatch begins after §12 pre-flight checklist passes.*

*Mantra (final): QUALITY > SPEED. PROVENANCE > VOLUME. WISDOM-APPLIED > WISDOM-CITED. RUSLAN-ACK > BRIGADIER-CONFIDENCE. This is THE Foundation document. 1 trillion percent.*
