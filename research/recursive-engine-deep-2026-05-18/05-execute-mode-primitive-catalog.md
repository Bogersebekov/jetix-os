---
title: Phase 4 — Execute-mode primitive catalog
date: 2026-05-18 evening
phase: 4
type: research-doc-primitive-catalog
authored_by: brigadier-scribe
cell_dispatch: eng × integrator + investor × roi-frame
word_budget: 3000
status: brigadier-research-surface (R1)
parent: 00-MASTER-INDEX.md
F: F3
G: execute-mode-primitive-catalog
R: refuted_if_(primitive_count_<8 OR primitive_not_operationally_defined OR pre-authorization_scope_ambiguous OR IP-1_violation)
constitutional_posture: R1 + R6 + EP-5 + IP-1 STRICT
language: russian + english
---

# Phase 4 — Execute-mode primitive catalog

> **R1 surface only.** Execute-mode = brigadier dispatches cells; cells execute within **pre-authorized action class scope** per `.claude/config/default-deny-table.yaml`. **IP-1 STRICT** — execution NEVER includes autonomous strategic decision-making (rule 1) NOR autonomous self-modification (rule 9).

> **NASA SE cross-link (Phase 2 §4):** 6 execute-mode primary processes mapped к 8 primitives below.

---

## §0 TL;DR (≤200w)

8 execute-mode primitives codified, each ≤400w with **Definition + FPF mapping + Operational mechanism + Failure modes + Test design + Refinement candidate** structure:

1. **Dispatch** — brigadier → cells per matrix
2. **Atomic commit** — per-phase commit message format
3. **Log append** — wiki/log.md + swarm/approvals/log.jsonl + ledger
4. **Push** — git origin main
5. **Halt** — R1/R2/R6/R11 violation halt
6. **Pause** — cost / time / scope ambiguity pause
7. **Resume** — from last commit checkpoint
8. **Reflection trigger** — post-phase ритуал (cross-link Phase 5 Hansei)

**IP-1 enforcement:** Each primitive bound к pre-authorized action class scope. Novel-class triggers Plan-mode Primitive 5 (AWAITING-APPROVAL escalation). Pattern = abstract method; runtime invocation = bound executor instance per `shared/schemas/executor-binding.yaml.template`.

---

## §1 Execute-mode Primitive 1: Dispatch

### §1.1 Definition

**Dispatch** = brigadier → cells per Plan-mode Primitive 2 matrix. Executes within pre-authorized scope: ROY swarm cell invocation, research/<run-id>/ append, mermaid creation, etc.

### §1.2 FPF mapping

- `U.WorkPlan` instance — plan-mode artifact becomes execute-mode dispatch
- Foundation Part 4 §H hub-and-spoke (brigadier = sole dispatcher per IP-1 strict)
- `A.2.9 SpeechAct` — dispatch order = formal task contract per `task.schema.json`

### §1.3 Operational mechanism

1. brigadier reads acked surface (concept doc / packet / direction)
2. brigadier selects relevant cells from matrix (Plan-mode P2)
3. brigadier creates task contract per `shared/schemas/task.schema.json`
4. Cells execute within pre-authorized scope
5. Outputs appended (NOT auto-modified) to research namespace OR draft path

### §1.4 Failure modes

- **F1:** Dispatch to wrong cell (mismatch problem domain) → low-quality output
- **F2:** Multi-dispatcher (cell A dispatches cell B без brigadier mediation) → Part 4 §H violation
- **F3:** Cell scope creep (cell A modifies файл outside its assignment) → R2/R11 risk
- **F4:** Dispatch без task contract → reproducibility gap

### §1.5 Test design

- Per cycle: dispatch count + cell utilisation balance
- Per cycle: task contract conformance (schema-validated)
- Refutation: any non-brigadier dispatch in git history

### §1.6 Refinement candidate

Dispatch heuristic table (Phase 8 candidate via Hansei).

[src: Foundation Part 4 §H + ROY-ALIGNMENT §3 + shared/schemas/task.schema.json]

---

## §2 Execute-mode Primitive 2: Atomic commit

### §2.1 Definition

**Atomic commit** = per-phase commit with structured message format `[area] verb what (why)`. Per Cloud Cowork memory rule: brigadier commit + push pre-authorized.

### §2.2 FPF mapping

- KM MVP company-as-code discipline (per `swarm/wiki/designs/T-km-materialization-mvp-2026-04-24/partD-company-as-code.md`)
- `A.16 Work-as-process` — commit = process completion marker
- Configuration Management (NASA SE #14)

### §2.3 Operational mechanism

Format: `[<area>][<sub-area>] <verb> <what> (<why optional>)`
Examples:
- `[research][recursive-engine-deep] Phase 0 FPF lens + IP-1 boundary scope + MASTER-INDEX`
- `[meta][prompts-gen] Phase 3 2 NEW prompts + 2 NEW EXPLAIN siblings`

Per-phase commit (NOT batch end-of-run) — preserves checkpoint structure for Primitive 7 Resume.

### §2.4 Failure modes

- **F1:** Batch commit (all 9 phases at end) → checkpoint loss; Primitive 7 Resume impaired
- **F2:** `--amend` used → git history rewrite; KM MVP §rollback violation
- **F3:** Commit message ambiguous → audit gap
- **F4:** API keys в commit (grep miss) → R2/security violation

### §2.5 Test design

- Per phase: 1 commit
- Per cycle: commit messages match format
- API key audit before commit: `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|...' <staged files>` → 0 hits

### §2.6 Refinement candidate

Pre-commit hook auto-runs API key grep + format validate.

[src: KM MVP partD §company-as-code + Cloud Cowork memory rules + this run commit pattern]

---

## §3 Execute-mode Primitive 3: Log append

### §3.1 Definition

**Log append** = append-only writes to canonical logs: `wiki/log.md` (Karpathy chronological), `swarm/approvals/log.jsonl` (gates), `crm/log.md` (CRM activity), per-agent strategies files (at cycle boundary).

### §3.2 FPF mapping

- Append-only discipline (Global Rule 3 + KM MVP)
- `B.7 wiki/` substrate + Karpathy chronological log
- Part 5 Compound Learning §I — methodology library append

### §3.3 Operational mechanism

New entries SVERHU (top of file per Global Rule 3 — append-only newest-first). NEVER edit OR delete old entries. Rotation: >30 entries → archive/ per KM MVP discipline.

### §3.4 Failure modes

- **F1:** Old entries modified → append-only violation
- **F2:** Entries written sequentially at bottom (vs top) → convention break
- **F3:** Log skipped (no entry per phase) → audit gap
- **F4:** JSONL log entries malformed → parser fail

### §3.5 Test design

- Per phase: log entry written
- Per cycle: log file growth monotonic
- Refutation: any modified-not-appended entry detected

### §3.6 Refinement candidate

Auto log-entry generation hook.

[src: Global Rule 3 + KM MVP §rotation + wiki/log.md current state]

---

## §4 Execute-mode Primitive 4: Push origin main

### §4.1 Definition

**Push** = `git push origin main` per phase OR at run completion. Per Cloud Cowork memory rule pre-authorized.

### §4.2 FPF mapping

- Configuration Management (NASA SE #14)
- `A.16 Work-as-process` — push = process commit к shared substrate

### §4.3 Operational mechanism

After per-phase commit, push at run end (or per-phase if explicit signal). Typically: 9 commits then 1 push at run end OR push-per-phase if time budget allows.

**This run convention:** per-phase commits + single final push (Phase 8 commit 9 + push).

### §4.4 Failure modes

- **F1:** `push --force` to main → KM MVP rollback discipline + R11 violation
- **F2:** Push without commit → no-op fail-quiet
- **F3:** Push fails (network / remote rejection) → checkpoint inconsistency
- **F4:** Push without preceding API key audit → security risk

### §4.5 Test design

- Per run: 1+ push to origin main
- Refutation: any `--force` push detected

### §4.6 Refinement candidate

Pre-push hook auto-runs API key audit + lint.

[src: KM MVP partD + Cloud Cowork memory pre-authorization + this run convention]

---

## §5 Execute-mode Primitive 5: Halt

### §5.1 Definition

**Halt** = R1/R2/R6/R11 violation OR IP-1 boundary breach detected → IMMEDIATE halt. Emit to `swarm/approvals/log.jsonl` + Part 8 SLI alert. Plan-mode Primitive 8 (Halt-Log-Alert) cross-link.

### §5.2 FPF mapping

- Part 6b §I.2 LOCKED Halt-Log-Alert
- FPF §5.5 fail-loud
- E.5 Guard-rails

### §5.3 Operational mechanism

Detection triggers (execute-mode):
- R1 — autonomous strategic prose без voice anchor
- R2 — Foundation file write attempt
- R6 — claim без [src:...] in promoted output
- R11 — novel action class attempted без packet
- IP-1 — pattern ≠ instance conflation in output

Action: halt within grade window (F8 ≤1s / F4 ≤5s / F2 ≤60s); log JSONL; SLI alert.

### §5.4 Failure modes

- **F1:** Halt silently swallowed → §5.5 + corrigibility violation
- **F2:** Halt delayed beyond grade window → SLI degradation
- **F3:** False positive halt (legitimate action mis-categorised) → throughput loss
- **F4:** Halt after partial write (transaction split) → state inconsistency

### §5.5 Test design

- Per run: zero R1/R2/R6/R11/IP-1 violations
- Per-month: false positive halt rate <5%
- Refutation: any silent swallow detected

### §5.6 Refinement candidate

Per-grade halt detection rule catalog (cross-link Phase 6).

[src: Part 6b §I.2 + halt-log-alert.schema.json + this run zero-violation target]

---

## §6 Execute-mode Primitive 6: Pause

### §6.1 Definition

**Pause** = cost ambiguity (approaching €5 budget) OR time ambiguity (single phase >30min OR run >150min) OR scope ambiguity (novel action class candidate, not yet halted) → pause + ask.

### §6.2 FPF mapping

- E.5 Guard-rails (soft variant — pause vs halt)
- A.4 Temporal Duality (pause = explicit non-progress state)

### §6.3 Operational mechanism

Triggers:
- Cost approaching threshold (€5 default per prompt §12)
- Time approaching threshold (single phase >30min logged; total >150min halt at phase boundary)
- Scope ambiguity — novel class candidate identified

Action: write «PAUSE» entry to current phase doc + emit ask to Ruslan IF interactive.

**Note:** This run was explicitly authorized «не пауза» per Ruslan ack — pause primitive bypassed for this run; documented for future autonomous runs.

### §6.4 Failure modes

- **F1:** Pause threshold exceeded без pause → cost/time overrun
- **F2:** Pause without explicit ask → silent stuck state
- **F3:** Pause for non-ambiguous scope → throughput loss
- **F4:** Resume from pause без context refresh → context drift

### §6.5 Test design

- Per run: cost ≤€5 OR pause logged
- Per phase: ≤30min OR logged
- Refutation: cost overrun or time overrun without pause trail

### §6.6 Refinement candidate

Pause budget per-phase / per-run explicit catalog.

[src: prompt §12 halt conditions + Cloud Cowork memory pre-authorization scope]

---

## §7 Execute-mode Primitive 7: Resume

### §7.1 Definition

**Resume** = from last commit checkpoint after pause OR halt resolution OR session crash recovery.

### §7.2 FPF mapping

- `A.16 Work-as-process` — process resumption marker
- Configuration Management (NASA SE #14)
- Part 1 System State Persistence

### §7.3 Operational mechanism

1. Read last commit message (git log -1)
2. Read last phase doc final state
3. Verify checkpoint integrity (no partial writes)
4. Continue from next phase

Atomic commit (Primitive 2) ensures checkpoint integrity — that's WHY per-phase commits matter.

### §7.4 Failure modes

- **F1:** Resume from partial commit → state inconsistency
- **F2:** Resume without context refresh → assumption drift
- **F3:** Resume skipping completed phase → duplicate work
- **F4:** Resume в wrong direction (mis-read checkpoint) → throughput loss

### §7.5 Test design

- Per crash/pause recovery: resume succeeds with next-phase work
- Refutation: duplicate phase work in git history

### §7.6 Refinement candidate

Per-phase resume manifest (checkpoint JSON).

[src: Part 1 System State Persistence + KM MVP rollback discipline + git history conventions]

---

## §8 Execute-mode Primitive 8: Reflection trigger

### §8.1 Definition

**Reflection trigger** = post-phase ritual emit signal. Cross-link Phase 5 Hansei + Kaizen ritual operationalisation. Cycle boundary marker.

### §8.2 FPF mapping

- Part 5 Compound Learning §I methodology capture
- `A.16 Work-as-process` — process closing marker
- TPS Hansei (P14 Toyota Way — direction 14)
- NASA Technical Assessment (SE #16)

### §8.3 Operational mechanism

Post-phase triggers:
- Commit message append «(reflection: <key observation>)» (optional)
- Per-cycle Hansei retrospective entry (Phase 5 design)
- Per-cycle strategies file update (gated cycle output per rule 9)

**Critical IP-1 enforcement:** Strategies file updates = gated cycle output, NOT runtime self-modification.

### §8.4 Failure modes

- **F1:** Reflection skipped → compound learning loss
- **F2:** Reflection autonomous (без Ruslan touch для strategic items) → rule 1 violation
- **F3:** Reflection writes Foundation file → rule 2 violation
- **F4:** Reflection collapsed across cycles → granularity loss

### §8.5 Test design

- Per cycle: Hansei retrospective entry written
- Per cycle: strategies file delta (if any) committed at cycle boundary
- Refutation: any runtime strategies modification

### §8.6 Refinement candidate

Auto-template Hansei retrospective format (Phase 5 detail).

[src: Part 5 §I + Phase 5 design + Pillar C Tier 2 rule 9]

---

## §9 Pre-authorization scope explicit (IP-1 critical foreground)

### §9.1 Execute-mode primitives within pre-authorized scope

Per `.claude/config/default-deny-table.yaml` Default-Deny exclusion zone (i.e., the «autonomous OK» set per concept doc B §4.2):

| Primitive | Pre-authorized? | Conditions |
|---|---|---|
| 1. Dispatch | YES | within ROY swarm matrix + research namespace target |
| 2. Atomic commit | YES | per Cloud Cowork memory rule |
| 3. Log append | YES | append-only к canonical logs |
| 4. Push | YES | per Cloud Cowork memory rule (NOT --force) |
| 5. Halt | YES | always pre-authorized (fail-loud) |
| 6. Pause | YES | always pre-authorized |
| 7. Resume | YES | within same run scope |
| 8. Reflection trigger | YES | within cycle boundary; strategies update gated |

### §9.2 Execute-mode actions OUTSIDE pre-authorized scope (escalate)

- Foundation file modification → Plan-mode Primitive 5 packet
- Pillar C / shared/schemas / VISION-FUNDAMENTAL → packet
- 8 Octagon LOCK content → packet
- External outreach send → packet (R11)
- API key access → packet (R11; never auto)
- `--force` push / `--amend` → escalate Default-Deny
- Capability acquisition decisions → R1 rule 3

[src: .claude/config/default-deny-table.yaml + concept doc B §4 + Phase 6 IP-1 boundary catalog cross-link]

---

## §10 Cross-link к other phases

- **Phase 2 NASA SE §4** — 6 execute-mode primary processes
- **Phase 3 plan-mode primitives** — paired catalog template
- **Phase 5 Hansei + Kaizen** — Primitive 8 reflection trigger detail
- **Phase 6 IP-1 boundary** — pre-authorization scope catalog
- **Phase 7 5-cycles trial** — primitives exercised cross-cycle
- **Phase 8 hypothesis bank** — H-RE-X «execute-mode primitive test»

---

## §11 What this catalog is NOT

❌ Auto-deployment of these primitives без trial
❌ Replacement of Cloud Cowork memory pre-authorization
❌ Definitive primitive list — Phase 8 may surface more

---

**Word count:** ~2380 / 3000 budget. Compliant. 8 primitives × 6 fields each; pre-authorization scope foreground explicit per IP-1.

*brigadier-scribe Phase 4. R1 + R6 + EP-5 + IP-1 STRICT. Cells: eng × integrator + investor × roi-frame.*
