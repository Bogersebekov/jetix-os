---
title: "Task intake — KM Materialization MVP (Cycle-3 implementation)"
type: task-intake
id: T-km-materialization-mvp-2026-04-24
cycle_id: cyc-km-materialization-mvp-2026-04-24
task_class: M                                # Method-development (structural)
operating_mode: Stage-Gated
niche: meta                                  # cross-niche substrate (CLAUDE.md 6-niche lock)
pmbok_state: Planned
intaked_at: 2026-04-24
intaked_by: brigadier
layer: root
created: 2026-04-24
last_modified: 2026-04-24
pipeline: drafted
state: intaked
confidence: high
confidence_method: ruslan-attested            # Gate-2 ack 2026-04-24T21:00:00Z + deep-prompt spec
tier: core
produced_by: brigadier
sources:
  - {path: "prompts/swarm-launch-brigadier-km-materialization-2026-04-24.md"}
  - {path: "prompts/km-materialization-mvp-execution-2026-04-24.md", range: "§§1-13"}
  - {path: "prompts/meta-brief-km-materialization-mvp-2026-04-24.md"}
  - {path: "decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md", range: "§§11-13 recommendation + 4-response ack"}
  - {path: ".claude/agents/brigadier.md", range: "§1d + §2 + §3"}
  - {path: "swarm/lib/shared-protocols.md", range: "§§1-9"}
related:
  - "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md"
  - "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md"
  - "swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md"
  - "agents/brigadier/strategies.md"
binding_scope: task-T-km-materialization-mvp-2026-04-24
granularity: jetix-internal
---

# Task Intake — KM Materialization MVP

## §1 Arrival

Ruslan's swarm-launch prompt at `prompts/swarm-launch-brigadier-km-materialization-2026-04-24.md`
directs brigadier to execute the deep execution prompt at
`prompts/km-materialization-mvp-execution-2026-04-24.md` (2304 lines) end-to-end
as a ROY swarm cycle.

Upstream anchor: Ruslan Gate-2 decision acked 2026-04-24T21:00:00Z —
**A1 full ADOPT + B2 full ADOPT + B3 MERGE INTO B2 + Company-as-Code cross-cutting**.
No A2. No A3. No B1. No M3 this cycle.

## §2 Classification (§2.2 four axes)

| Axis | Value | Rationale |
|---|---|---|
| **PMBOK alpha-state** | `Planned` | acceptance-predicate + decomposition outline arrive with the launch prompt (§§2-3 of deep prompt) |
| **Operating-mode** | `Stage-Gated` | mandatory AWAITING-APPROVAL pause between Part F (verification) and Part G (report). Full-Auto NOT authorized (launch §4). |
| **Task-class** | `M` (Method) | 2nd M-slot of cycle. Per Ruslan explicit HD-02 override 2026-04-24: `N=3` for this cycle (one-cycle override; restores to N=2 next cycle). Class rationale: changes how the swarm operates — new skills, config-driven project types, stage-gate DSL, mini-swarm spawn protocol, company-as-code discipline. |
| **Niche** | `meta` | cross-niche substrate that rewrites KM + PM foundations for all 6 niches. Quick-money bootstrap in Part E is business-niche data; research project in Part E is meta-niche; the substrate itself is meta. |

**HD-02 override audit.** Counter `m_class_dispatched_this_cycle` at
`swarm/wiki/meta/health.md` will read `2/3` when this task intakes
(prior M-task `T-km-architecture-research-2026-04-24` already closed in
cycle-2-compound; this is cycle-3). The `/3` ceiling applies for this
cycle only, per Ruslan verbatim directive: *"рой на 500%, пиздуем"*.
Default N=2 restores next cycle unless Ruslan re-asserts.

## §3 Acceptance predicate (AP-25 prevention)

> The task is `done` when:
> (a) Parts A–E deliverables from `prompts/km-materialization-mvp-execution-2026-04-24.md`
>     §§2.A–2.E land in the repo (≥30 new files spanning
>     `.claude/skills/`, `.claude/config/`, `.claude/agents/`,
>     `swarm/wiki/_templates/`, `swarm/wiki/operations/`, `swarm/tests/`,
>     `tools/`, plus edited `CLAUDE.md`);
> (b) `swarm/tests/km-mvp-verify.sh` exits 0 covering 4 per-Part smoke
>     suites + 10 use-case probes (UC-INGEST-1, UC-ASK-1, UC-ASK-OFFLINE,
>     UC-DIGEST, UC-PROJECT-CONSULTING, UC-PROJECT-ADAPTIVE, UC-REVERSE,
>     UC-REVIEW, UC-ISOLATION-DEMO, UC-COMPANY-STATUS);
> (c) `/grep -rEn 'ANTHROPIC_API_KEY|OPENAI_API_KEY|GROQ_API_KEY|COHERE_API_KEY'`
>     over `.claude/ swarm/ tools/` returns zero hits in body/script
>     (may appear only in `unset`-style guards);
> (d) quick-money P1 project bootstrapped with real ICP from JETIX-VISION D22
>     + mini-swarm scaffold present + one end-to-end ingest+ask demo logged
>     to `quick-money/history.md`;
> (e) levenchuk-deep-dive P3 research project bootstrapped adaptively (3-file
>     baseline) with stage-gate declarations live;
> (f) `swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-<XX>.md`
>     written with full verification matrix + HALT honored until Ruslan ack;
> (g) Post-ack only: `decisions/KM-MATERIALIZATION-MVP-REPORT-2026-04-<XX>.md`
>     ≥3000 words with all §9.3 sections + §9.7 attestation paragraph;
> (h) 4 × 4-part DRR entries appended to `agents/brigadier/strategies.md`
>     + 5 × per-expert learning entries to
>     `swarm/wiki/meta/agent-improvements/<expert>-2026-04-<XX>.md`;
> (i) cycle-archive entry + `meta/health.md` counter increments;
> (j) final `git status` clean on `claude/jolly-margulis-915d34`; no
>     unpushed commits.

Binary Hamel-falsifier: if any of (a)–(j) fails after Ruslan ack, the
task is NOT done — brigadier re-enters Part F verification or Part G
compound per §§8.4–8.5 of deep prompt.

## §4 Pull manifest (Q4 priority-ranked context budget)

Files brigadier + cells will read across the cycle. Hard cap
`total_tokens_estimated: ≤20,000` per any single cell dispatch (§2.5
of brigadier). Manifest below is cycle-wide; cell-specific subsets
carve from this.

### Tier 0 — Runtime contract (every cell reads)

- `swarm/lib/shared-protocols.md` (274 lines)
- `.claude/agents/brigadier.md` (1090 lines) — cells read own expert file + import stubs; brigadier re-reads both
- `prompts/km-materialization-mvp-execution-2026-04-24.md` (2304 lines) — section-scoped per cell

### Tier 1 — Gate-2 anchor + variant specs

- `decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md` (508 lines; §§11-12 verbatim)
- `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-A1-karpathy-plus-plus.md` (296 lines)
- `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B2-rich-mini-swarm.md` (356 lines)
- `swarm/wiki/drafts/T-km-architecture-research-2026-04-24-variant-B3-adaptive-scaffold.md` (328 lines)
- `prompts/meta-brief-km-materialization-mvp-2026-04-24.md` (243 lines)

### Tier 2 — Strategic + vision context (Part E bootstrap inputs)

- `decisions/JETIX-VISION.md` (498 lines; §§7.1-7.2 ICP)
- `decisions/JETIX-PLAN.md` (923 lines; §§3.1-3.9 Phase-1 targets)
- `decisions/JETIX-ARCHITECTURE-BRIEF.md` (842 lines; §§2 + 4)
- `decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` (212 lines)
- `decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md` (211 lines)

### Tier 3 — Expert lenses (cell-local; brigadier skims)

- `.claude/agents/engineering-expert.md` (995 lines) — Part A/D primary owner
- `.claude/agents/mgmt-expert.md` (1553 lines) — Part B/E primary owner
- `.claude/agents/systems-expert.md` (1568 lines) — Part C primary owner
- `.claude/agents/philosophy-expert.md` (1482 lines) — Part C SG validation
- `.claude/agents/investor-expert.md` (1529 lines) — Part E ICP realism check

### Tier 4 — Existing substrate (read-only reference)

- `.claude/config/wiki-roots.yaml` (45 lines) — Part A.1 extends
- `.claude/skills/{ingest,ask,lint,consolidate,build-graph}.md` — Part A extends
- `design/ROY-WIKI-V3-ARCHITECTURE-SPEC-2026-04-23.md` — §§D1 D2 D3 D7 D8 referenced
- `CLAUDE.md`, `.claude/rules/global.md`, `agents/brigadier/strategies.md`

## §5 Dispatch plan (see decomposition.md for full WBS)

Matrix 5×4 activation: **integrator-heavy** with targeted **critic** and
**scalability** modes. Optimizer mode reserved for Part D before/after
snapshots. Weak-Supplementation floor honored (≥2 cells per Part).

- **Wave 1 (parallel dispatch)** — Parts A+B+C:
  - `engineering × integrator` (A.1–A.9 substrate skill bundle)
  - `mgmt × integrator` (B.1–B.8 mini-swarm bundle)
  - `systems × integrator` (C.1–C.6 stage-gate merged mechanic)
  - `philosophy × critic` on Part C SG predicate DSL (Hamel-binary discipline — deep §2.C.6)

- **Wave 2 (serial after Wave 1 drafts land)** — Part D cross-cutting:
  - `engineering × integrator` (D.4 /company-status + D.5 /knowledge-diff)
  - Per-Wave-1-expert pass-through: each expert validates its Part artefacts respect company-as-code principle (cell returns via writing-support extraction, not separate dispatch — brigadier composes gate evidence inline)

- **Wave 3 (serial after Wave 2)** — Part E real application:
  - `mgmt × integrator` (E.1–E.3 quick-money + levenchuk bootstrap)
  - `investor × critic` on quick-money ICP + KPI realism
  - `engineering × optimizer` on end-to-end ingest+ask demo (measurable deliverable)

- **Pre-gate sweep** — Part F verification + gate packet.

## §6 Risk register (OPP-04 non-trivial predicates required per cell)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Token-budget exhaustion before Part E | medium | high | Parts A/B/C in parallel (one dispatch wave); write-scope-guard on drafts; shared Tier-0/1 manifest referenced by path not inlined |
| Expert-draft rejected at §5.5.5 gate (2× retry-limit fires) | medium | medium | §2 pre-dispatch checklist hardened (`cell_acceptance_predicate` ≥ 20 chars, non-trivial, references `swarm/evals/` or `health.md`); OPP-04 compliance auditable in `decomposition.md` |
| B3↔B2 merge clash (meta-brief §12 flagged) | medium | medium | Default per deep §11.3.4: `--adaptive` wins → baseline + stage-gates declared → auto-spawn on SG fire. Ambiguity packet path available. |
| Part E ingest URL unreachable | low | low | Local-transcript fixture under `swarm/tests/fixtures/km-mvp/` (deep §UC-INGEST-1 probe already defines hermetic fallback) |
| tcpdump requires sudo for UC-ASK-OFFLINE | medium | low | substitute `ss -t state established '( dport = :443 )'` before/during/after — same intent (deep §UC-ASK-OFFLINE note) |
| Part G premature writing before Ruslan ack | low | high | Stage-Gated hard pause. Brigadier refuses Part G dispatch until `swarm/gates/...-ack.md` exists OR frontmatter `state: acked`. Shadow-write forbidden (deep §8.2). |
| HD-02 N=3 misread as permanent | low | low | Intake frontmatter explicitly tags one-cycle override; post-cycle compound restores N=2 (brigadier §3.3.1 counter reset at cycle-open). |

## §7 Escalation triggers active

Per shared-protocols §4 + brigadier §1d, auto-escalate on:
1. Foundation revision (no foundation is created in this cycle; if surfaced → HITL).
2. Contradiction with accepted foundation without obvious resolution (deep §11 ambiguity path).
3. Budget overrun (per-cell `ap_budget` in decomposition; 2× aggregate → HITL).
4. Retry-limit (2 consecutive rejections at §5.5.5 gate).
5. Irreversible decision (architecture commit beyond drafts — all Part A–E promoted writes ARE irreversible in spirit, but licensed by Gate-2 ack; any DELTA from spec → ambiguity packet first).
6. `split_trigger` fires — not expected this cycle.
7. Method exhaustion (same AP >5× across cycles) — watchlist: AP-5 mode-confusion, AP-25 missing acceptance-predicate, AP-15 handoff failure.

## §8 Side-effects performed at intake

1. `mkdir -p swarm/wiki/tasks/T-km-materialization-mvp-2026-04-24/{context,artefacts,decisions}` — done.
2. `mkdir -p swarm/logs/cyc-km-materialization-mvp-2026-04-24` — done.
3. Cycle-events log will be appended at dispatch-time to
   `swarm/logs/cyc-km-materialization-mvp-2026-04-24/events.md`.
4. `swarm/wiki/log.md` will receive one-line entry on dispatch.
5. `swarm/wiki/index.md` will receive entry under niche `meta` at close.

## §9 Language + tone

Russian primary for Ruslan-facing gate packets; English for all
frontmatter, code, skill manifests, test probes, commit messages, and
inter-cell communication (CLAUDE.md §7 rule). Gate ack messages
interpreted in Russian or English equally.

## §10 Summary

Intake complete. α-1 transitions `submitted → intaked → decomposed`
once `decomposition.md` commits alongside this file. Dispatch begins
immediately after in Wave 1.
