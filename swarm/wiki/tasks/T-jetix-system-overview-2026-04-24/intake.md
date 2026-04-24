---
task_id: T-jetix-system-overview-2026-04-24
cycle_id: cyc-jetix-system-overview-2026-04-24
acceptance_predicate: >-
  decisions/JETIX-SYSTEM-OVERVIEW.md exists AND body has §0 TL;DR + §1-§6 top-level
  + §L0..§L9 + §L-R/§L-C/§L-B/§L-P (14 layer sections) + §L+1..§L+4 (post-layer) AND
  every layer section has Mission + What-lives-here (agents/docs/tools/data) + Boundaries +
  Interfaces + Current-status + Evolution-path + Voice-memo-refs + Open-questions AND each
  layer section body ≥800 words AND every audio_NNN claim resolves to reports/review_2026-04-24.md
  OR raw/voice-transcripts/*.md OR decisions/LOCKS-D25-D28-ADDENDUM OR JETIX-VISION/PHILOSOPHY/PLAN
  AND D1-D28 summary table has 28 rows one-liner each AND USB-C/McKinsey resolution §6
  written AND Mermaid/ASCII system-level diagram in §4 AND swarm/gates/AWAITING-APPROVAL-jetix-system-overview-2026-04-24.md
  written + HALT honored before compound/archive.
classifier:
  pmbok_state: Initiated
  operating_mode: Stage-Gated
  task_class: M
  niche: meta
intaked_at: 2026-04-24
intaked_by: brigadier
operating_posture:
  max_subscription: asserted
  hd_02_override: N=3 this cycle (parallel to KM Mat MVP awaiting Ruslan ack + 1 reserve)
  m_slot: 3 of 3
  self_improvement_mandate: non-optional per §8 of launch prompt
  stage_gate_mandatory_pause: before Part G compound/archive
  full_auto_authorized: false
---

# T-jetix-system-overview-2026-04-24 — Phase-1 Intake

## §1 Scope

Write `decisions/JETIX-SYSTEM-OVERVIEW.md` — the single coherent 15-25K-word layered description of the
Jetix system as of 2026-04-24 + evolution path through €50K → €200K → €1M → $100M → $100B → $1T gates,
with agents as first-class citizens in every relevant layer.

This is the 4th orchestrated brigadier cycle (after swarm-self-improve-v1 / km-architecture-research
/ km-materialization-mvp). Task class is **description** — not implementation, not research, not
strategy-directive. Foundation document for Phase 2 per-layer deep-dives (separate M-tasks each)
and Phase 3 strategic docs.

## §2 The 14 layers (mandatory, verbatim from launch §3)

### Core system stack (L0-L9)

- **L0 Foundation — Company-as-Code** (D25); ref audio_510, 519, 520
- **L1 Knowledge — Query-driven KB + Private Library** (D28); ref audio_517, 520, 522
- **L2 Ingest & Signal** — voice-transcribe, auto-loggers, reverse-engineering crawlers; ref 514, 518, 522, 527
- **L3 Synthesis & Compounding Engineering** — strategist + knowledge-synth, daily/weekly loops, sandbox-draft; ref 519, 520, 521
- **L4 Agent Layer — Holding-style** — 6 ROY + 14 legacy; D26 holding-with-agents; ref 510, 514, 521, 529
- **L5 Product & Services — Smart AI directions** — Smart AI flagship + 7 offerings; ref 508, 510, 511, 514, 524, 527, 528, 529
- **L6 Business & Trajectory** — ICP + outreach + pricing + partnerships + gates €50K → $1T; ref 506, 510, 511, 515, 523, 528, 529
- **L7 Research & Reverse-Engineering** — D24 open-source research + reverse-eng, Левенчук ШСМ; ref 510, 515, 524, 527
- **L8 People & Alliance — Swarm + Digital Portraits** — core team 50-100 (D26), Alliance + 5h/week, Secure Network, fork-community (D27); ref 506, 507, 510, 512, 513, 519, 524, 525, 527
- **L9 Governance & Evolution** (cross-cutting) — 28 Locks, AWAITING-APPROVAL, sandbox-черновик, fork-and-merge (D27); ref 519, 520, 521, 528

### Cross-cutting layers (L-R / L-C / L-B / L-P)

- **L-R Resource Management** — time/attention/finances/energy/credits; ref 449, 510, 413, 428
- **L-C Compute & Infrastructure** — own servers/GPUs for distilled LLMs; ref 526 + STRATEGIC-INSIGHT local-first
- **L-B Brand & Narrative** — USB-C / прошивка Windows / Smart AI internal / 3-audience landing / document-compass; ref 507, 527, 528
- **L-P Life OS** — Ruslan wellness/productivity/finance/Bank of Ideas/life-coach + PA agents; ref 517, 518, 525

## §3 Context manifest (priority-ranked, ≤20K tokens estimated)

```yaml
tier_1_constitutional:
  - {path: decisions/LOCKS-D25-D28-ADDENDUM-2026-04-24.md, tokens_est: 2400, role: locks-non-negotiable}
  - {path: decisions/JETIX-VISION.md, tokens_est: 10000, role: D1-identity}
  - {path: decisions/JETIX-PHILOSOPHY.md, tokens_est: 20000, role: D2-principles}
  - {path: decisions/JETIX-PLAN.md, tokens_est: 18000, role: D3-step-plan}
  - {path: decisions/JETIX-ARCHITECTURE-BRIEF.md, tokens_est: 17000, role: D4-tech-arch}
  - {path: design/JETIX-FPF.md, tokens_est: 75000, role: FPF-constitutional}

tier_2_master_plan:
  - {path: decisions/MASTER-PLAN-FOUNDATION-TO-EXECUTION-2026-04-24.md, tokens_est: 5000, role: week-plan}
  - {path: decisions/STRATEGIC-INSIGHT-JETIX-AI-BIOS-MOMENT-2026-04-24.md, tokens_est: 5000, role: positioning}
  - {path: decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md, tokens_est: 4500, role: 6-pillar}

tier_3_voice_evidence:
  - {path: reports/review_2026-04-24.md, tokens_est: 38000, role: audio_NNN-citations-source-of-truth}
  - {path: reports/summary_2026-04-24.md, tokens_est: 12000, role: voice-summary}
  - {path: raw/voice-transcripts/2026-04-24-ruslan-chat-voice-usb-c-positioning.md, tokens_est: 2400, role: USB-C-verbatim-pitch}

tier_4_operational:
  - {path: swarm/gates/AWAITING-APPROVAL-km-materialization-mvp-2026-04-24.md, tokens_est: 5700, role: L1/L2-what-just-materialized}
  - {path: decisions/KM-ARCHITECTURE-VARIANTS-2026-04-24.md, tokens_est: 10000, role: L1-KM-options}
  - {path: swarm/lib/shared-protocols.md, tokens_est: 5500, role: L3-L4-operational-contract}
  - {path: .claude/agents/brigadier.md, tokens_est: 26000, role: L4-brigadier-reference}
  - {path: .claude/agents/engineering-expert.md, tokens_est: 20000, role: L4-expert}
  - {path: .claude/agents/mgmt-expert.md, tokens_est: 20000, role: L4-expert}
  - {path: .claude/agents/systems-expert.md, tokens_est: 20000, role: L4-expert}
  - {path: .claude/agents/philosophy-expert.md, tokens_est: 20000, role: L4-expert}
  - {path: .claude/agents/investor-expert.md, tokens_est: 20000, role: L4-expert}
  - {path: .claude/agents/strategist.md, tokens_est: 6000, role: L4-legacy-L3-synth}
  - {path: .claude/agents/knowledge-synth.md, tokens_est: 6000, role: L4-legacy-L3-synth}
  - {path: .claude/agents/life-coach.md, tokens_est: 4000, role: L4-legacy-L-P}
  - {path: .claude/agents/personal-assistant.md, tokens_est: 4000, role: L4-legacy-L-P}
  - {path: .claude/agents/inbox-processor.md, tokens_est: 4000, role: L4-legacy-L2}
  - {path: .claude/agents/sales-lead.md, tokens_est: 4000, role: L4-legacy-L6}
  - {path: .claude/agents/sales-researcher.md, tokens_est: 4000, role: L4-legacy-L6}
  - {path: .claude/agents/sales-outreach.md, tokens_est: 4000, role: L4-legacy-L6}
  - {path: .claude/agents/meta-agent.md, tokens_est: 4000, role: L4-legacy-L9}
  - {path: .claude/agents/crazy-agent.md, tokens_est: 4000, role: L4-legacy-L3/L7}
  - {path: .claude/agents/manager.md, tokens_est: 4000, role: L4-legacy-L4}
  - {path: .claude/agents/system-admin.md, tokens_est: 3000, role: L4-legacy-L0/L-C}
  - {path: .claude/agents/staging-writer.md, tokens_est: 2000, role: L4-legacy-task-class}
  - {path: .claude/agents/sweep-worker.md, tokens_est: 2000, role: L4-legacy-task-class}
  - {path: .claude/agents/strategist.md, tokens_est: 6000, role: L4-legacy-L3-synth}
  - {path: CLAUDE.md, tokens_est: 2200, role: project-conventions}
  - {path: swarm/wiki/index.md, tokens_est: 1500, role: wiki-state-ref}
  - {path: swarm/wiki/log.md, tokens_est: 1500, role: wiki-changes-ref}

total_tokens_estimated: ~400k (cells subsample per assignment; not all read by all)
```

## §4 Anti-scope (verbatim launch §10)

- NO re-opening 28 Locks (D1-D28). Voice-evidence conflict → flag in open questions, do NOT override.
- NO per-layer deep-dives (Phase 2 of master plan).
- NO strategic per-direction recommendations (consulting-DACH / producer / Secure Network) — Phase 3.
- NO implementation code. Description only.
- NO Notion writes (D17 filesystem-SoT).
- NO API-key references.
- NO hardcoded Jetix-specific paths in examples; config-driven per D25.

## §5 Classifier justification

- **M (Method-class)** — description of system structure that downstream M-tasks depend on. Changes
  how the swarm operates: downstream layer deep-dives reference this. Counts against HD-02 N=3
  override budget (this cycle only).
- **Stage-Gated** — mandatory AWAITING-APPROVAL pause before compound/archive per launch §9.
- **niche: meta** — describes the system itself, cross-cutting across personal / business /
  sales / life / tech niches.

## §6 M-slot accounting

- Slot 1: KM Materialization MVP (awaiting Ruslan ack on gate packet)
- **Slot 2: this task (T-jetix-system-overview-2026-04-24) — ACTIVE**
- Slot 3: reserve (unused this cycle)

Post-cycle: restore to N=2 unless Ruslan re-asserts.

## §7 Escalation triggers (task-specific)

- `contradiction-with-foundation` — voice evidence conflicts with a D1-D28 lock. Flag in §L+1
  Open Questions; do NOT attempt to revise locks in this doc.
- `peer-input-needed` — cell B requires cell A's layer draft before synthesizing cross-cutting
  section (expected for L9 Governance + L-R Resources + top-level §3 28-Locks table).
- `budget-overrun` — cell exceeds `ap_budget`; brigadier escalates, does NOT silently extend.
- Retry-limit hit (2 consecutive §5.5.5 fails on same draft) — escalate before 3rd retry.

## §8 Definition of done (per acceptance predicate + launch §§4-6)

1. `decisions/JETIX-SYSTEM-OVERVIEW.md` exists with 14 layer sections (L0-L9 + L-R/L-C/L-B/L-P)
   + top-level §0-§6 + post-layer §L+1..§L+4.
2. Each layer section ≥800 words.
3. Every claim has audio_NNN / document citation.
4. 28-lock summary table has 28 rows one-liner each with cross-reference to primary layer.
5. USB-C / McKinsey-platform resolution §6 written (brigadier proposes; Ruslan acks/rejects in review).
6. Mermaid/ASCII system-level diagram §4.
7. `swarm/gates/AWAITING-APPROVAL-jetix-system-overview-2026-04-24.md` written.
8. Gate-learning entries per major section landing in `agents/brigadier/strategies.md`.
9. 17-22 commits total per §11; push per commit on `claude/jolly-margulis-915d34`; no amend/force/no-verify.
10. HALT before compound/archive; Ruslan reviews → acks → Phase 7 compound + Phase 8 archive.
