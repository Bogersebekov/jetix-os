---
title: "Interface Card — Part 8: Health Monitoring & System Integrity"
part: 8
slug: health-monitoring-system-integrity
phase: A-2
cycle: cyc-foundation-build-2026-04-28
expert: engineering-expert
mode: integrator
date: 2026-04-27
originating_expert: systems-expert (convergence: mgmt-expert + investor-expert also proposed)
critic_flags_applied:
  - "CLEAN (A-1-critic-gate.md §2 Part 8) — no required edits"
  - "F-G-R dual-ownership note: Part 6 = real-time gate enforcement; Part 8 = periodic audit (drift detection) — must be explicit in both Wave C interface cards"
  - "OQ-MERGED-5 applied: Wave C scope = specify and stub (not specify and implement)"
  - "TRADEOFF-01 surfaced: VSM S3 authority split between Part 6 and Part 8 — flagged as Open Q"
F: F4
ClaimScope: "Holds for Foundation observability design at Phase A scale (<=10 agents); SLI/SLO starter values are calibration parameters, NOT Foundation constants; Wave C scope = specify and stub"
R: "Refuted if Wave C produces hardcoded SLI thresholds in Foundation artefacts without labeling them as calibration parameters; accepted if SLI/SLO schema exists with explicit starter-value + calibration-cadence fields"
sources:
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/A-1-critic-gate.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-b/consultants/systems-thinking-cybernetics.md
  - swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/expert-pre-reads/mgmt-expert.md
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
  - design/JETIX-FPF.md
---

# Interface Card — Part 8: Health Monitoring & System Integrity

**Scope sentence.** The operational observability substrate — SLI/SLO definition,
metric collection, anomaly surfacing, backup verification, agent-drift detection,
methodology-freshness tracking, and periodic immune-system integrity checks — that
makes silent degradation visible before it becomes catastrophic.

**U.System.** Monitoring pipeline owner: collects signals, evaluates thresholds,
surfaces alerts, triggers behaviour-change rules when error budgets burn.

---

## A. Inputs

- Health signals from ALL other parts (derived from their committed artefacts) :: periodic-collection event
  - Part 1: git log metrics (commit frequency, commit format compliance)
  - Part 2: pipeline run records (transcription backlog, triage queue depth)
  - Part 3: KB freshness (wiki entity count, stale-claim rate, lint output)
  - Part 4: mailbox metrics (cycle time, queue depth, escalation rate)
  - Part 5: DRR write rate per cycle, compound-application rate
  - Part 6: gate-open count per cycle, approval-lag SLI
  - Part 7: project state distribution (cycle completion rate, appetite overrun rate)
  - Part 9: daily log creation rate, attention-budget utilisation
  - Part 10: CRM touch rate, stuck-contact count
- `shared/state/system-health.json` :: baseline snapshot (current state)
- `shared/state/metrics/agent-performance.json` :: agent-level signal source
- FUNDAMENTAL §3 SLI/SLO starter values :: calibration parameters (NOT Foundation constants — calibrate first 2-3 months per FUNDAMENTAL §3 note)

## B. Outputs

- `shared/state/system-health.json` :: updated health snapshot (weekly at minimum)
- Health dashboard artefact (committed `decisions/weekly/<YYYY-WNN>-health.md`) :: weekly structured report
- `decisions/quarterly/<YYYY-QN>-immune-audit.md` :: quarterly immune-system audit (F-G-R compliance, alpha classification drift)
- Alert records (HITL packets to Part 6 escalation taxonomy) :: anomaly events above threshold
- Recommendation list ("look here") → consumed by Part 9 (Owner Interaction Scaffold) for weekly review :: recommendation-ready event
- Behaviour-change signals when error budget burns → consumed by Part 6 and Part 9 :: budget-burn event

## C. Side-effects

- Append to `swarm/wiki/log.md` on each weekly health snapshot commit (append-only)
- Write to `shared/state/system-health.json` (idempotent re-computation; prior value preserved in git history)
- Open AWAITING-APPROVAL packet via Part 6 when structural integrity failure detected (FUNDAMENTAL §6.7: halt + log + alert)
- Quarterly audit writes to `decisions/quarterly/` — git commit `[health] quarterly immune audit: <YYYY-QN>` per D25

## D. Dependencies (typed per FPF A.14)

- `operates-in` **all other parts** — monitoring consumes health signals derived from artefacts of every other part; Part 8 is the observability context for the entire Foundation [candidate-parts-merged.md §2 Part 8; systems-thinking-cybernetics.md §4 Principle 3 VSM S3]
- `methodologically-uses` **Part 1** — health records committed as git artefacts; durable storage via Part 1
- `methodologically-uses` **Part 6** — anomaly alerts routed through Part 6's escalation taxonomy; Part 6 is the enforcement arm for structural failures Part 8 detects [A-1-critic-gate.md §2 Part 8 B.3 F-G-R check]

**VSM S3 note (systems-thinking-cybernetics.md §4 Principle 3):** Part 8 serves Beer VSM System 3 (Audit/Optimisation) function — the periodic audit function. Part 6 serves VSM S3 as the real-time enforcement gate. TRADEOFF-01 (VSM S3 authority split) is preserved as an Open Q below — Beer's VSM shows that splitting S3 across two controllers creates oscillation risk; Wave C must designate a clear S3 lead Part.

## E. Boundary (FPF A.6.B L/A/D/E)

**Laws (invariants that MUST hold):**
- Health monitoring is observability ONLY — it surfaces alerts; it does NOT auto-change system configuration or auto-promote/demote artefacts (FUNDAMENTAL §6.1; anomaly detection is J-Auto; behaviour-change on budget burn is J-Approve; structural integrity failure is J-Strategic per A.13 Agency-CHR)
- Fail-loud principle: anomaly detected → committed alert record + HITL packet opened via Part 6 within one monitoring cycle (FUNDAMENTAL §5.2 fail-loud)
- SLI/SLO values declared in Foundation artefact MUST be labeled as starter/calibration values with explicit calibration-cadence field; hardcoded thresholds without calibration label are a Foundation violation [FUNDAMENTAL §3 note; OQ-MERGED-5]
- Quarterly immune-system audit MUST cover: F-G-R compliance drift across artefact types; alpha classification drift (IP-5); role-manifest freshness (IP-6); strategies.md staleness [FPF IP-4; A-1-critic-gate.md §2 Part 8]

**Admissibility (acceptance criteria for health signals):**
- Health signals accepted only if they are derived from committed git artefacts — no ephemeral in-memory metrics (D25 Company-as-Code; FPF IP-3)
- SLI definition must name: what is measured, how measured, measurement cadence; SLOs without these three fields are rejected

**Deontics (obligations toward consumers):**
- MUST produce weekly health dashboard for Part 9 (Owner Interaction Scaffold) for the weekly review ritual [FUNDAMENTAL §2.5 health checkup cadence]
- MUST open a HITL gate packet via Part 6 within 24h of detecting a structural integrity failure (L1 SLA per FUNDAMENTAL §4.2)
- MUST NOT execute behaviour-change without human ack — surfacing is automatic; response decision is founder-owned (FUNDAMENTAL §6.1)

**Effects (measurable outcomes):**
- Weekly: `decisions/weekly/<YYYY-WNN>-health.md` committed
- Quarterly: `decisions/quarterly/<YYYY-QN>-immune-audit.md` committed
- Anomaly → HITL packet opened via Part 6 (lag: within 1 monitoring cycle)

## F. Anti-scope

- Part 8 does NOT make strategic decisions (FUNDAMENTAL §6.1) — it makes system health VISIBLE; the owner decides what to do
- Part 8 does NOT enforce stage gates — that is Part 6 (Governance). Part 8 DETECTS compliance drift; Part 6 ENFORCES compliance at promotion time [A-1-critic-gate.md §2 Part 8 B.3 F-G-R dual-ownership note]
- Part 8 does NOT implement SLI/SLO numerical tooling in Wave C — Wave C scope is "specify and stub" (schema + cadence declaration); numerical calibration and tool implementation are Phase-B materialisation [OQ-MERGED-5; Kauffman Ch. 1 adjacent-possible — numerical calibration requires ≥5 cycles of real data before the numbers are stable]
- Part 8 does NOT name specific role holders for immune-system function — the immune-system function (IP-4 audit cadence) is generic; the specific role assigned (e.g. "ontological-integrity-steward") is a RUSLAN-LAYER executor-binding [FPF §5.1 IP-1; A-1-critic-gate.md §6 item 3; candidate-parts-merged.md §2 Part 8 FPF anchor]
- Part 8 does NOT produce recommendations that substitute for founder judgment — output is a "look here" list; the owner acts or defers (FUNDAMENTAL §1 UC-I.3)
- Part 8 does NOT cover capital-impact analysis on health signals — that routes to investor-expert domain

## G. F-G-R Tagging

| Artefact emitted | F | G (ClaimScope) | R |
|---|---|---|---|
| Weekly health snapshot | F4 | Current system state only; calibration parameters may shift | medium — automated computation, owner-reviewed |
| Quarterly immune audit | F5 | Foundation-wide artefact types across the quarter | high — structured audit protocol, human-reviewed |
| Alert record (anomaly) | F4 | Specific anomaly event, single cycle | medium — threshold-based detection, may have false positives |
| Recommendation list | F3 | Current week's signals only | low — surfacing heuristics, owner validation required |
| SLI/SLO schema (Wave C output) | F5 | Foundation-wide, calibration-cadence declared | high once schema acked; starter values are F3 until calibrated |

## H. Originating Expert + Critic Flags

**Originating expert.** Systems-expert (Part 4: Health Monitoring & Self-Correction Layer). Convergence: mgmt-expert (Part 5: Operational Health Monitoring Layer) and investor-expert (Part 4: Health + Integrity Monitor) independently proposed. Engineering-expert was outlier (cross-cutting-only position — resolved in favor of standalone part per Munger inversion + Popper falsifier). [candidate-parts-merged.md §2 Part 8]

**Critic flags:** CLEAN — no required edits from A-1 critic gate. [A-1-critic-gate.md §2 Part 8]

**F-G-R dual-ownership note (for Wave C):** Part 6 = gate enforcement (real-time, per-artefact; compliance checked at promotion time). Part 8 = audit compliance (periodic, system-wide drift detection; quarterly immune-system check). This distinction MUST be explicit in both Parts 6 and 8 Wave C interface cards. [A-1-critic-gate.md §2 Part 8 B.3]

**Ashby requisite variety (systems-thinking-cybernetics.md §4 Principle 2):** Part 8's monitoring channels must match the variety of Foundation failure modes. FUNDAMENTAL §3 names 30+ SLI/SLO pairs across 8 health domains. Wave C design check: enumerate all failure modes → find minimal sensor set with variety ≥ failure-mode count. Do not over-reduce variety (blindspot risk) or over-specify (dashboard-overload anti-pattern per FUNDAMENTAL §1 UC-H.4).

**TRADEOFF-01 — Open Q (VSM S3 split):** Beer VSM predicts that splitting S3 (Audit/Optimisation) across Part 6 (gate enforcement) and Part 8 (audit) creates oscillation risk — neither Part has full S3 authority. Wave C must designate a clear S3 lead Part (likely Part 8 for audit authority, Part 6 as enforcement arm). This is a Wave C scoping decision requiring Ruslan ack. [systems-thinking-cybernetics.md §7 TRADEOFF-01; Beer Ch. 9 VSM S3]

**Wave C bullets (preview).**
- Define Foundation SLI/SLO schema (field spec: what / how / cadence / starter-value / calibration-trigger) — M effort; systems-expert integrator + engineering-expert critic
- Specify weekly health dashboard artefact template — S effort; mgmt-expert integrator
- Specify quarterly immune-system audit protocol and artefact template — M effort; philosophy-expert integrator (F-G-R compliance audit requires philosophy-expert lens)
- Stub alert-routing interface to Part 6 escalation taxonomy — S effort; engineering-expert integrator
