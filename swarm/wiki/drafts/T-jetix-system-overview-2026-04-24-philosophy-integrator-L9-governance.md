---
id: T-jetix-system-overview-2026-04-24-philosophy-integrator-L9-governance
title: "JETIX-SYSTEM-OVERVIEW §L9 — Governance & Evolution (philosophy × integrator draft)"
type: section-draft
task_id: T-jetix-system-overview-2026-04-24
produced_by: philosophy-expert × integrator
mode: integrator
layer: L9
created: 2026-04-24
pipeline: drafted
state: draft
confidence: high
confidence_method: sourced-from-locked-decisions-and-canonical-swarm-files
sources:
  - {path: "decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md", note: "D25-D28 canonical; acked Ruslan 2026-04-24"}
  - {path: "decisions/JETIX-PHILOSOPHY.md", note: "operating principles; 24 locked decisions binding"}
  - {path: "raw/research/architecture-variants-2026-04-22/TENSIONS-PRE-RESOLVED.md", note: "D1-D8"}
  - {path: "raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED.md", note: "D9-D18"}
  - {path: "raw/research/architecture-variants-2026-04-22/TENSIONS-RESOLVED-STAGE-2B.md", note: "D19-D24"}
  - {path: "swarm/lib/shared-protocols.md", range: "§4 HITL + AWAITING-APPROVAL"}
  - {path: "reports/review_2026-04-24.md", range: "audio_519-528 sections"}
  - {path: ".claude/agents/brigadier.md", range: "§1d decision-rights matrix + §6 gate-check"}
  - {path: "agents/brigadier/strategies.md", note: "live DRR accumulation; 8+ entries"}
  - {path: "swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md", note: "active gate example"}
anti_scope:
  - "Does NOT re-open any of the 28 Locks"
  - "Does NOT propose a new Lock (Ruslan-only authority)"
  - "Does NOT contain the 28-Lock cross-reference-per-layer table (that is top-level §3 work for brigadier integration)"
  - "Does NOT arbitrate instrumental Рациональность — that is investor-expert territory (FPF L1003-1006)"
  - "Does NOT write canonical wiki — brigadier promotes on gate pass"
dissents: []
---

# §L9 — Governance & Evolution

## L9.1 Mission of this layer

Layer 9 governs Jetix's own rules for changing itself. It is the
**meta-constitutional** layer — the set of constraints, mechanisms, and
disciplines that sit above operational execution, above product-gates,
above resource-tracking. Every other layer (L1 through L8, L-R) operates
within the envelope L9 defines. Where a lower layer asks "what do we do
next?", L9 asks "what are the rules for deciding how any rule can be
changed?"

This is not an abstract philosophical posture. It is an operational
discipline with concrete file locations, concrete gate mechanics, and
concrete escalation paths. The mission of L9 is threefold:

1. **Lock the constitutional layer.** Twenty-eight locked decisions
   (D1-D28) define non-negotiable constraints. Any work anywhere in
   the system that would contradict a Lock must stop, flag, and route
   to a foundation-revision gate. Locks cannot be overridden by
   swarm-autonomous action.

2. **Provide the mechanism for managed evolution.** The system changes.
   New phases bring new capabilities, new team members, new paradigms.
   L9 provides the mechanism: the AWAITING-APPROVAL gate, the
   sandbox-черновик principle, the мета-описания-first filter, the
   fork-and-merge architecture, the beta-first policy. These are not
   suggestions — they are enforced by the brigadier §1d decision-rights
   matrix and the shared-protocols §4 HITL rules.

3. **Compound learning cross-cycle.** The brigadier strategies.md is
   the living artifact of governance evolution — every cycle deposits
   DRR entries that reshape how the swarm operates in the next cycle.
   L9 contains the rules for that accumulation.

**Epistemic note on constitutional vs operational distinction.** This
section carries a philosophy-expert obligation to name this boundary
explicitly. The 28 Locks are **constitutional constraints** in Popper's
falsifiability sense: they are the hard core of the research programme
(Lakatos P3), protected by a belt of operational policies. Overriding a
Lock is a paradigm-shift event (Kuhn P2) requiring HITL, not a parameter
adjustment. Operational policies — beta-first, не переспрашивать, sandbox-
черновик — are belt-level: they can be revised through the gate mechanism
without touching the core. Mechanism specifications — the AWAITING-APPROVAL
packet format, the brigadier §1d matrix — are instrumental knowledge
(Vincenti category: theoretical tools) that instantiate the constitutional
and operational layers in executable form.

Conflating these three strata is the governance anti-pattern. A change
to the gate-packet YAML format is a mechanism change; it does not require
foundation revision. A change to Lock D25 (Company-as-Code) is a
constitutional change; it requires full HITL with explicit Ruslan
re-ack. A change to the beta-first policy is an operational change; it
requires an AWAITING-APPROVAL gate but not a Lock amendment.

---

## L9.2 What lives here

### L9.2.1 decisions/ directory

All canonical strategic artefacts that bind the swarm and Ruslan's
decisions live under `decisions/`. The directory is not a log — it is
an authoritative state. Key contents:

- **D1-D28 locked decisions** across four source documents:
  `TENSIONS-PRE-RESOLVED.md` (D1-D8), `TENSIONS-RESOLVED.md` (D9-D18),
  `TENSIONS-RESOLVED-STAGE-2B.md` (D19-D24), and
  `LOCKS-D25-D28-ADDENDUM-2026-04-24.md` (D25-D28).
- **JETIX-PHILOSOPHY.md** — operating principles derivative of the 24
  prior locks; now extended by D25-D28.
- **Master plan, strategic-insight, cycle-reports** — these are
  decisions about how to execute, not constitutional constraints.
- **Frontmatter protocol**: every file carries `acked_by: ruslan` and
  an `acked_at:` timestamp when Ruslan has acknowledged it. Files
  without this field are not binding.

The directory is a **git-versioned constitutional record**. D25
(Company-as-Code) makes this explicit:

> *«строить инфраструктуру Company as a Code с самого начала,
> способную выдержать масштабирование до триллиона капитализации»*
> [audio_510; D25]

Every decisions/ write is a commit with attribution. Every historical
state is reconstructable via `git log`. This is not an operational
nicety — it is the foundation for D19's $1T-readiness claim.

### L9.2.2 The 28 Locks: non-negotiable constitutional constraints

The 28 Locks (D1-D28) are the hardest layer of Jetix's governance. They
are **non-negotiable for all downstream work**; any prose, design, or
system-prompt change that conflicts with them must stop and flag.

Summary of Lock domains (full cross-reference table is §3 of
SYSTEM-OVERVIEW, not L9 body):

| Group | Locks | Domain |
|---|---|---|
| Identity + Scale | D1, D19, D26 | Jetix vision, $1T trajectory, team 50-100 |
| Architecture | D2, D4, D25 | Solo-with-team-ready, tech stack, company-as-code |
| Phase gates | D3 | Plan and phase sequencing |
| Epistemics | D6 | FPF as meta-methodology |
| Community | D7, D8, D12, D16 | Network design, Secure Network, anti-attention |
| Revenue model | D5, D9, D10, D11, D14 | Consulting, Layer-9 trigger, product-first |
| Differentiation | D13, D15, D20, D21 | Closed core, Mittelstand, USB-C, roy-replication |
| Operations | D17, D18, D22, D23, D24 | Filesystem SoT, git workflow, Compound Engineering |
| New (2026-04-24) | D25, D26, D27, D28 | Company-as-code, enterprise team, fork-and-merge, query-driven KB |

D26 explicitly supersedes earlier "one-person company" framing:

> *«Jetix будет не one person company, а команда из 50-100 человек,
> работающая как холдинг»* [audio_510; D26]

D27 introduces fork-and-merge as an architectural evolution primitive:

> *«Jetix должен стать базовой стабильной системой, которую
> пользователи могут форкать и адаптировать под себя, а лучшие
> мутации возвращать в основную ветку»* [audio_519; D27]

Overriding any Lock requires a **foundation-revision gate** (shared-
protocols §4, trigger 1). The gate cannot be acked by swarm-autonomous
action; only Ruslan acks. This is the hard-stop: the wall between the
swarm's self-improvement and the constitutional layer.

### L9.2.3 AWAITING-APPROVAL gate mechanism

Source: `swarm/lib/shared-protocols.md` §4; active example:
`swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md`.

The gate is the primary mechanism by which L9 governs all other layers.
Nine triggers are enumerated in shared-protocols §4:

1. Foundation revision (create or supersede `swarm/wiki/foundations/*`)
2. Layer-9 activation (Q8 3-AND trigger: `meta/health.md`)
3. Contradiction with accepted foundation without obvious resolution
4. Budget overrun (`maxTurns` or token budget hit)
5. Retry limit (draft rejected 2× consecutively)
6. α-5 Direction state change (AI agents never move α-5)
7. Method exhaustion (same AP >5× across cycles)
8. Irreversible decision (architecture commit, dependency change, protocol mod)
9. `split_trigger` fires in an expert manifest

When any trigger fires, brigadier writes a gate packet under
`swarm/gates/AWAITING-APPROVAL-<id>-<YYYY-MM-DD>.md` with frontmatter
`{title, type: gate, gate_type, escalator: brigadier, escalated_at,
state: open}` and body sections: Context, Options (1-4),
Recommendation, Risk, Proposed file paths, How Ruslan acks.

The km-materialization-mvp gate (2026-04-24) is the current live
example. It illustrates triggers 3, 8, and a complex multi-option
arbitration: investor × critic surfaced arithmetic FAIL findings that
brigadier cannot resolve without averaging dissent (AP-6 — never
average). Gate fires; brigadier halts; Ruslan picks Option A-D.

**Ack mechanism.** Ruslan writes `<id>-ack.md` with `acked: true`,
`chosen: <letter>`, `notes:`. On detection, brigadier moves α-1
`gated → approved` and α-4 `gated → compounded`.

### L9.2.4 Sandbox-черновик принцип

Source: `reports/review_2026-04-24.md` audio_519, audio_520.

> *«Принцип работы с системами: создавать отдельный черновик для
> работы, не трогая верхнеуровневые системы, подтверждать или
> отклонять изменения только после завершения работы»* [audio_520]

> *«Метод Jetix должен четко ограничивать систему перед началом
> работы — описывать границы, что входит и не входит в область
> работы, чтобы более адекватно углубляться в решение задач»*
> [audio_520]

The sandbox-черновик principle governs how L9 handles every proposed
change to the canonical system: changes flow through drafts → review →
ack → canonical. No bypass is permitted. This applies to:

- Wiki writes (brigadier Q2 single-writer; cells write only to
  `swarm/wiki/drafts/`; brigadier promotes after §5.5.5 gate)
- System-prompt changes (no agent modifies its own core prompt
  autonomously; proposals are DRR entries in strategies.md that
  brigadier compiles into improvement packets)
- Agent revisions (any change to `.claude/agents/*.md` that
  would modify a mode-allowlist, decision-rights row, or accepted
  foundation requires AWAITING-APPROVAL)

The principle encodes via-negativa discipline (Stoic P5): name what is
NOT touched before working on what IS touched. audio_520 makes this
explicit:

> *«Перед началом работы четко разграничивать и понимать: что
> делаешь и не делаешь, на чем фокусируешься и не фокусируешься,
> что берешь в работу и что оставляешь»* [audio_520]

### L9.2.5 Мета-описания as first filter

Source: `reports/review_2026-04-24.md` audio_519.

> *«Jetix должен быть построен как модульная система из подсистем:
> основная система, управление, обучение, сбор данных/знаний, каждая
> с четким описанием входов, выходов и процессинга»* [audio_519]

Every system component carries a мета-описание — a structured
description of what it is, what goes in, what comes out, and what it
does not do. This мета-описание is read FIRST before any work begins on
or with that component. The pattern is operationalized in the swarm as:

- Agent system prompts: the `##§1 Identity` + `##§1b Ontological` blocks
  are the мета-описание. Every invocation re-reads them.
- AWAITING-APPROVAL gate packets: the `Context` section is the мета-
  описание of the open question before options are considered.
- The 28 Locks themselves: each lock begins with a verbatim Ruslan
  quote (the intent signal) followed by the implications (the мета-
  описание of what this constraint means operationally).

The function of мета-описания as first filter is epistemic discipline:
it prevents interpretation drift. If an agent or human approaches a
component without reading its мета-описание, the risk is that their
mental model of the component diverges from its actual design intent.
This is the anti-pattern that locks and meta-descriptions guard against.

### L9.2.6 Fork-and-merge upstream-controller

Source: D27; `LOCKS-D25-D28-ADDENDUM-2026-04-24.md`.

D27 installs a GitHub-style evolution architecture on the methodology
itself:

> *«Jetix должен стать базовой стабильной системой, которую
> пользователи могут форкать и адаптировать под себя, а лучшие
> мутации возвращать в основную ветку»* [D27, audio_519]

The structure:
- **Canonical Jetix** = stable upstream (curated, governed)
- **Each client / partner / ecosystem participant** = fork + adaptations
- **Best mutations** = merge-back to upstream via PR-style contribution
- **Upstream** = maintains quality bar and integration

This intersects with D13 (Closed core / Open surface), D21 (Roy-
replication), and D20/D25 (USB-C + Company-as-Code). Together: the
methodology evolves through distributed contribution, not central
dictation. The canonical upstream is the constitutional layer — forks
cannot alter the 28 Locks of their upstream; they can add policy above
that floor.

**Governance model remains TBD per D27 §Downstream.** The mechanism is
locked; the governance question (BDFL / committee / meritocracy) is not.
This is an explicit open question (see §L9.5).

### L9.2.7 Beta-first / не переспрашивать / не даунгрейдить policies

Source: `reports/review_2026-04-24.md` audio_528.

> *«Разрабатывать все качественно, ответственно и глубоко,
> заставлять инструменты точно так же работать и следить за
> качественной работой команды с самых первых дней»* [audio_528]

Three operational disciplines that audio_528 signals and that are not
yet formally written up (see §L9.5):

1. **Beta-first.** Every new capability launches as explicitly labelled
   beta. No production-grade claim before beta validation. The label
   is not cosmetic — it gates the AWAITING-APPROVAL trigger 8
   (irreversible action); beta capabilities have not yet crossed
   the irreversibility threshold.

2. **Не переспрашивать (не задавать одинаковый вопрос дважды).**
   Once a question has been asked and answered — by Ruslan ack,
   by AWAITING-APPROVAL resolution, by a DRR entry — the swarm does
   not re-litigate it in a subsequent cycle. The DRR entry in
   strategies.md is the receipt. Re-litigating a resolved question is
   method-exhaustion (AP trigger 7).

3. **Не даунгрейдить (no product degradation after beta).** Once a
   capability has passed beta validation and is in production, the
   system does not roll it back to a lesser state without an explicit
   AWAITING-APPROVAL gate (trigger 8: irreversible). Downgrade is
   treated as irreversible because it signals a paradigm failure —
   something that worked was broken by a change, requiring root-cause
   analysis, not silent revert.

### L9.2.8 Brigadier §1d decision-rights matrix

Source: `.claude/agents/brigadier.md` §1d.

The brigadier §1d matrix is the operational enforcement mechanism for
L9. It is the table that maps each possible action to one of four
categories: `autonomous / requires-approval / never / split-trigger`.
The matrix is non-negotiable; the decision-rights ritual is executed
before every Write, Bash, Task dispatch, or commit.

Selected rows that are governance-critical:

| Category | Row |
|---|---|
| autonomous | Intake a well-formed task with acceptance-predicate |
| autonomous | Dispatch Task() to any cell in the 5×4 matrix |
| autonomous | Integrate returned drafts with dissent-preservation |
| autonomous | Promote drafted → reviewed → accepted under shared-protocols §2 |
| autonomous | Write per-task pages under swarm/wiki/tasks/<task-id>/ |
| autonomous | Write own strategies (agents/brigadier/strategies.md) |
| autonomous | Write meta/agent-improvements/<expert>-improvements.md |
| requires-approval | Foundation revision (create or supersede swarm/wiki/foundations/*) |
| requires-approval | Layer-9 activation (Q8 3-AND trigger) |
| requires-approval | Any irreversible decision |
| requires-approval | Any α-5 Direction state change |
| never | Self-strategizing (method selection for the swarm itself) |
| never | Primary writing (weekly review, quarterly letter) |
| never | Average dissent into consensus |
| never | Override an expert's domain judgment directly |
| split-trigger | Sustained task-intake rate >10/week for 3 consecutive weeks |
| split-trigger | 2+ concurrent α-4 cycles needed |
| split-trigger | Accountability items >7 |

The `never` rows name the via-negativa of orchestration: what the
brigadier will NOT do regardless of what it is asked. `self-strategizing`
is the hardest prohibition — the swarm does not choose its own Method
(capital-M); that is HITL-only.

### L9.2.9 Compound protocol — strategies.md as governance evolution

Source: `agents/brigadier/strategies.md`; brigadier §8.

Every swarm cycle ends with a Compound step: each agent writes DRR
entries (Decision / Reasoning / Result / Review) to its strategies.md.
Brigadier's strategies.md currently holds 8+ entries from two cycles
(km-architecture-research and km-materialization-mvp). These entries are
the **living governance evolution mechanism** — each entry reshapes how
the swarm will run the next cycle.

Examples from the current record:

- *"Sequenced-migration-trajectory framing beats single-variant pick
  when N≥3 variants per layer"* — now a validated rule.
- *"Design record → extraction cell two-stage pattern"* — now the
  default for implementation M-tasks.
- *"Critic-in-parallel, apply-fixes-in-integration is cheaper than
  critic-after, retry-draft"* — now the standard Wave-1 dispatch shape.

Compound is the only mechanism by which swarm behavior evolves without
an AWAITING-APPROVAL gate. Its scope is strictly within the `autonomous`
column: the swarm may learn to execute better; it may not learn to
change its Method. When a Compound step surfaces a pattern that would
require a method change, it writes a `meta/agent-improvements/` entry
and escalates to HITL.

---

## L9.3 Boundaries

**In-scope for L9:**
- Rules about Jetix itself — constitutional constraints (28 Locks),
  operational policies (beta-first, sandbox-черновик, etc.), and the
  mechanisms that enforce them (gate packets, decision-rights matrix)
- Meta-level discipline — мета-описания, DRR accumulation, dissent
  preservation (AP-6), first-principles reset triggers
- HITL gate mechanics — when Ruslan must ack, what an AWAITING-APPROVAL
  packet contains, how ack detection works
- Governance evolution — compound protocol, strategies.md, fork-and-merge
  as a methodology-evolution substrate

**Out-of-scope for L9:**
- Operational execution specifics (L3 execution layer, L4 tools)
- Product-gate mechanics for specific directions (L6)
- Resource tracking and financial planning (L-R)
- Domain expertise — L9 does not say HOW to build a product; it says
  by what rules product design decisions can be changed

---

## L9.4 Interfaces

**Reads from:** ALL layers. Governance is cross-cutting. L9 reads
decisions/, swarm/wiki/foundations/, swarm/lib/shared-protocols.md,
agents/*/strategies.md, and meta/health.md to assess whether a gate
trigger has fired.

**Writes to:** ALL layers — but only via AWAITING-APPROVAL gates and
the sandbox-черновик flow. L9 does not directly mutate another layer's
state. It authorizes mutation via ack.

**Invokes:** HITL Ruslan for all ack. No autonomous L9 state change
can promote a foundation, activate Layer-9, or accept an irreversible
decision without Ruslan's explicit signal.

**Brigadier is the sole mechanical enforcer of L9.** The brigadier §1d
matrix is L9's runtime representation. Violations of the matrix
are L9 violations. The brigadier cannot enforce the matrix against
itself — that is why `self-strategizing` is in the `never` column and
why Ruslan is the closure of the creation graph (§1c L3).

---

## L9.5 Current status — 2026-04-24

**28 Locks in force.** D1-D24 locked before 2026-04-22; D25-D28 locked
and acked by Ruslan 2026-04-24 22:45 CET. All 28 are the non-negotiable
floor for all downstream work.

**Gates closed historically:**
- `swarm-self-improve-gate2` — acked
- `cycle-2-impl` (HD-01 Option C) — acked
- `km-architecture-variants` — acked (Option A, sequenced migration
  trajectory accepted)

**Gate currently AWAITING:**
- `AWAITING-APPROVAL-km-materialization-mvp-2026-04-24` — open as of
  2026-04-24; investor × critic vs mgmt × integrator dissent on
  quick-money parameters; brigadier HALTED; Ruslan ack pending.

**Governance mechanisms partially formalized:**
- Fork-and-merge (D27): mechanism locked; governance model
  (BDFL/committee/meritocracy) NOT designed.
- Beta-first policy: operational intent expressed in audio_528; formal
  write-up does not yet exist as a canonical policy document.
- Brigadier strategies.md: live with 8+ DRR entries — the mechanism is
  working; it has not yet hit the cycle_10 maturation threshold.

**Potential split-trigger watch:**
- Brigadier §1d: split fires if intake >10/week for 3 consecutive weeks,
  2+ concurrent cycles, or accountability items >7. Currently at 6
  accountability items; 1 buffer remaining. km-materialization-mvp
  cycle is the second named cycle — approaching the 2+ concurrent
  threshold if a parallel cycle is opened before resolution.

---

## L9.6 Evolution path

### Phase 1 (solo, current — toward €50K)

Ruslan-HITL for every gate. Brigadier §1d enforced in full. All 9
AWAITING-APPROVAL triggers active. Compound step after every cycle
deposits DRR entries. The only governance mechanism that runs without
HITL is Compound-within-autonomous-scope.

Fork-and-merge is locked as a future primitive (D27) but not activated
— no forks exist yet. KB filtering (D28) begins to reshape `/ingest`
behavior as soon as the km-materialization-mvp extraction lands
(pending current gate ack).

### Phase 2 (€200K — first team hires)

Governance scales as the first 2-3 team members join (D26). The first
delegation question surfaces: which subset of AWAITING-APPROVAL
triggers can a team member ack on Ruslan's behalf, and which remain
Ruslan-only?

Provisional answer (not locked — requires Phase 2 gate):

- Triggers 4 (budget overrun), 5 (retry limit), 7 (method exhaustion)
  are candidates for delegation to a designated integration manager.
- Triggers 1 (foundation revision), 2 (Layer-9 activation), 6 (α-5
  Direction change), 8 (irreversible) remain Ruslan-only.
- Trigger 3 (contradiction with foundation) is judgment-dependent;
  likely Ruslan-only unless an explicit escalation rubric is written.

The brigadier split-trigger (§1d) may fire at Phase 2 if intake
exceeds 10/week sustained. Split produces [task-dispatcher,
integration-manager, gate-keeper] per brigadier §1d split-trigger row.

### Phase 3 (€1M+ — managed team)

Fork-and-merge governance formalized per D27. The methodology upstream
(canonical Jetix) gains a formal review process. The governance model
question (BDFL/committee/meritocracy — see §L9.7) must be answered
before fork-and-merge can safely accept external contributions.

The Compound protocol may begin harvesting cross-fork DRR entries —
best mutations from client/partner forks feed back into canonical
strategies.md via the merge-back mechanism.

At €1M, D26 team trajectory (50-100 persons) begins to materialize
(Phase 2b → Phase 3 growth path per D26 implications). Governance must
handle the agency shift from solo → delegated → managed — each
transition is a Stoic dichotomy-of-control re-bucketing (per §6.1
scalability rubric): many decisions that were in-our-control become
in-our-influence only.

### Phase 3+ ($100M — multi-team org)

Per STRATEGIC-INSIGHT (referenced in brigadier §1c): Mittelstand AI
Alliance methodology-parliament co-governs methodology-upstream. The
fork-and-merge architecture creates the substrate for this — canonical
Jetix is the upstream that alliance participants fork from, contribute
to, and are governed by.

L9 at this scale carries constitutional weight comparable to a legal
framework: the 28 Locks, or their successors, function as foundational
law. Amendments require a formal process (see §L9.7 on constitutional
amendment).

### Phase 3+ ($1T — constitutional revision)

At societal-scale (per §6.1 scalability output, $1T gate), the 28
Locks themselves may need amendment. D19 (Mировой рекорд скорости до
$1T) and D20 (USB-C positioning) are aspirational at current scale —
at actual $1T, the system is operating under conditions none of the
Lock authors anticipated.

The constitutional-amendment process does not yet exist. Per the
Stoic via-negativa (P5): the system will NOT amend a Lock via
swarm-autonomous action at any scale. The process must be designed
before it is needed.

---

## L9.7 Open questions

These are unresolved governance questions as of 2026-04-24. They are
preserved as open because they require Ruslan decision or future gate
ack — not because they were missed.

1. **Fork-and-merge governance model.** D27 §Downstream defers: BDFL /
   committee / meritocracy — which model governs who maintains
   canonical Jetix upstream? Who has merge-authority? What is the
   review protocol for merge-back contributions? This must be resolved
   before fork-and-merge opens to external participants (expected Phase
   3, post-€1M).
   - Falsifier: "fork-and-merge is operational externally without a
     governance model document" — this state must not occur.

2. **Gate-ack delegation for Phase 2.** When the first team member
   joins, which AWAITING-APPROVAL triggers can be delegated vs remain
   Ruslan-only? The provisional split in §L9.6 is not locked. A
   Phase 2 gate packet should formalize this before the first
   delegation event.

3. **Beta-first policy formal write-up.** audio_528 signals the
   principle; no canonical policy document exists. The write-up should
   specify: what counts as beta vs production, what gates the
   transition, what "не даунгрейдить" means operationally (which
   reversibility threshold is crossed at production-promotion).

4. **Constitutional amendment process.** If a Lock needs revision at
   Phase 3+ ($100M/$1T), what is the process? The current mechanism
   (foundation-revision gate → Ruslan ack) works at solo/small-team
   scale. At multi-org scale, unilateral Ruslan ack may not be
   appropriate. The process must be designed before the first
   amendment attempt.

5. **IP licensing for fork-and-merge.** D27 lists this as pending:
   MIT-like / proprietary with exception / dual-license. This interacts
   with D13 (Closed core / Open surface) — the license boundary between
   core and surface must be articulated before the first external fork.

---

## L9.8 Voice-memo provenance summary

The audio references in this section are sourced from
`reports/review_2026-04-24.md`, items 774-804.

- **audio_519** [22-04-2026 17:54]: modular system design with clear
  descriptions of inputs/outputs for each subsystem; fork-and-merge
  as methodology evolution (D27); sandbox-черновик working pattern;
  regular check-up loops for self-update.
- **audio_520** [22-04-2026 18:40]: boundary-setting before work begins
  (what enters and does not enter scope); working in a draft, not
  touching upper-level systems; confirm/reject changes only after
  completion — the sandbox-черновик principle operational description.
- **audio_521** [22-04-2026 20:23]: everything entering the system must
  be converted to information units; three core variables — people
  (managing + executing), agents (planning + executing), and their
  interaction.
- **audio_528** [24-04-2026 02:06]: develop everything with quality,
  responsibility, and depth; make instruments operate the same way;
  watch quality of team work from day one. Source of the beta-first /
  не переспрашивать / не даунгрейдить cluster.

---

## Integrator synthesis note

**Claim structure.** This section synthesizes constitutional,
operational, and mechanism strata. Per E-5 integrator protocol:

```yaml
primary_synthesis_claim:
  claim: "L9 governance operates on three distinct strata (constitutional /
          operational / mechanism) that must NOT be conflated when proposing
          changes; conflation is the primary governance failure mode"
  F: F6
  ClaimScope:
    holds_when: "Phase A swarm with brigadier as sole enforcement mechanism;
                solo-with-team-ready configuration (D2)"
    not_valid_when: "team of 50+ operating; fork-and-merge accepting external
                    contributions; governance-model has been formalized per D27"
  R:
    refuted_if: "a Lock amendment is made via swarm-autonomous action without
                HITL ack; OR a mechanism change (gate-packet format) triggers
                a foundation-revision gate unnecessarily"
    receipt: "swarm/gates/ directory; agents/brigadier/strategies.md DRR entries"
    accepted_if: "all 28 Locks remain in force; all 9 gate triggers route
                 correctly to their ack mechanism; no autonomous L9 state change"
  paradigm: "Popper + Lakatos (constitutional hard core / operational belt / mechanism tool)"
  vincenti_category: "design-instrumentalities"
  dichotomy_tag: "in-control"

secondary_claim:
  claim: "Compound protocol (strategies.md DRR accumulation) is the ONLY
          mechanism by which swarm governance evolves without an AWAITING-APPROVAL
          gate, and its scope is strictly limited to the autonomous column of §1d"
  F: F5
  ClaimScope:
    holds_when: "brigadier §1d autonomous column remains as specified"
    not_valid_when: "a DRR entry proposes a method change; that entry must
                    immediately trigger meta/agent-improvements escalation"
  R:
    refuted_if: "a strategies.md DRR entry causes a method change without
                a corresponding AWAITING-APPROVAL gate packet"
    receipt: "agents/brigadier/strategies.md + swarm/gates/ cross-check"
    accepted_if: "all 8+ current DRR entries are strictly within autonomous scope"
  paradigm: "Koen (sotam-as-method; compound-as-sotam-evolution)"
  vincenti_category: "practical-considerations"
  dichotomy_tag: "in-control"
```

**Dissents.** No substantive dissent between inputs on governance
structure. One paradigm-tension noted and preserved: audio_528's
emphasis on quality-and-depth-from-day-one implies a performance
standard that may conflict with beta-first incremental rollout. These
are NOT contradictory — beta-first governs capability-gate timing;
quality-from-day-one governs execution standard within any gate. They
operate at different strata (operational policy vs craft discipline).
No reconciliation needed; both preserved.

```yaml
dissents:
  - position: "beta-first policy implies tolerance for degraded initial quality"
    held_by: "naive reading of 'beta'"
    F: F2
    ClaimScope: "applies only if 'beta' is misread as 'low-quality permitted'"
    R:
      refuted_if: "audio_528 verbatim: quality + responsibility + depth from day one"
  - position: "quality-from-day-one implies no beta phase needed"
    held_by: "alternative reading of audio_528"
    F: F2
    ClaimScope: "applies only if 'quality' is misread as 'production-ready always'"
    R:
      refuted_if: "irreversibility threshold logic requires beta-gating before
                  production-commit; quality is about craft, not gate-timing"
  - reconciliation:
      method: "epistemic-coherence — different strata, not contradiction"
      verdict: "beta-first = WHEN to promote to production; quality-from-day-one =
               HOW to execute at any stage. Both operational; no constitutional
               conflict; no lock amendment required"
```

---

*Draft produced by philosophy-expert × integrator per shared-protocols §3.
Route to brigadier for §5.5.5 gate + promotion. Do not mutate canonical
decisions/ or wiki/ before gate pass.*
