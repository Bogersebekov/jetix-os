---
title: "Consultant Card #6 — Site Reliability Engineering + Observability"
framework_id: 6
slug: sre-observability
date: 2026-04-27
phase: B-2
expert: engineering-expert
mode: integrator
cycle: cyc-foundation-build-2026-04-28
status: draft
confidence: high
confidence_method: mixed (2 library-direct, 3 training-knowledge)
F: F5
F_note: "Lifted post-supplement 2026-04-27 evening. 2/5 library-direct (Google SRE Book full + SRE Workbook Ch. 2 'Implementing SLOs'); 3/5 still training-knowledge (Honeycomb Observability Engineering, Mike Julian Practical Monitoring, OpenTelemetry spec — flag for Wave D supplement)."
ClaimScope: "Holds for single-node, single-owner, file-based Foundation substrate (git-based, no metrics infra). Unknown for multi-node distributed services or team-scale deployments. Deliberately scoped to Jetix Phase-A single-owner instance."
R:
  refuted_if: "Wave C interface card for Part 8 (Health Monitoring & System Integrity) cannot derive ≥3 actionable SLI/SLO pairs from FUNDAMENTAL §3 that are measurable with grep/git log/wc without a dedicated metrics backend"
  accepted_if: "Wave C materialises Part 8 with ≥5 SLI/SLO pairs drawn from FUNDAMENTAL §3.1-§3.8, each with a declared measurement method (grep / git log / file stat / manual count), and a behavior-change rule when the error budget burns"
sources:
  - "Google SRE Book — Betsy Beyer et al., 'Site Reliability Engineering: How Google Runs Production Systems', O'Reilly 2016. Ch. 4 Service Level Objectives, Ch. 6 Monitoring Distributed Systems, Ch. 22 Addressing Cascading Failures, Ch. 15 Postmortem Culture. https://sre.google/sre-book/table-of-contents/"
  - "Charity Majors, Liz Fong-Jones, George Miranda — 'Observability Engineering', O'Reilly 2022. Core argument: observability ≠ monitoring; observability = ability to ask arbitrary questions of system state without shipping new instrumentation. https://www.oreilly.com/library/view/observability-engineering/9781492076438/"
  - "Mike Julian — 'Practical Monitoring: Effective Strategies for the Real World', O'Reilly 2017. Anti-patterns in monitoring: tool-first thinking, alert fatigue, the four golden signals misuse. https://www.oreilly.com/library/view/practical-monitoring/9781491957349/"
  - "OpenTelemetry Specification v1.x — The Three Pillars (logs, metrics, traces) unified via OTel semantic conventions + propagation. https://opentelemetry.io/docs/specs/otel/"
  - "Alex Ewerlof et al. — 'Implementing SLOs' (Google SRE Workbook Ch. 2), 2018. Error budget burn rate algebra: 1x burn = SLO at risk in 1 window; 6x burn = urgent; 14.4x burn = critical window < 1h. https://sre.google/workbook/implementing-slos/"
provenance:
  - path: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
    range: "1004-1028"
    quote: "Health indicator = SLI + SLO + error-budget + alert behaviour... Behaviour change при burn — что меняется когда budget exhausted (not 'alert и забыли')"
  - path: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md
    range: "1615-1698"
    quote: "Reliability — это не 'оно работает', это 'оно не теряется и легко восстанавливается'... Fail-loud: Strategic doc modification — если что-то корраптит strategic doc → halt, alert, не proceed. Principle: silent failures = worst category of bug."
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
    range: "253-277"
    quote: "Part 8 — Health Monitoring & System Integrity. The operational observability substrate — SLI/SLO definition, metric collection, anomaly surfacing... that makes silent degradation visible before it becomes catastrophic."
  - path: swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md
    range: "265-277"
    quote: "FUNDAMENTAL §5.2 fail-loud principle... FPF P-7 (Pragmatic Utility — failures must be surfaced and visible, not suppressed)"
tags: [framework, sre, observability, sli-slo, error-budget, monitoring, honeycomb, wave-b, engineering]
---

# Consultant Card #6 — Site Reliability Engineering + Observability

---

## §1 Foundation Studied — Coverage Declaration

**Library coverage: 2/5 canonical SRE/observability sources library-direct as of 2026-04-27 supplement; 3/5 still training-knowledge.**

| # | Source | Status | Path (when library-direct) |
|---|--------|--------|----------------------------|
| 1 | **Google SRE Book — Beyer/Jones/Petoff/Murphy (eds.), O'Reilly 2016** | **library-direct ✅ (2026-04-27 supplement)** | `raw/books-md/sre/google-sre-book.md` (full 550-page book; quality grade A; 190,412 words) |
| 2 | Charity Majors et al., *Observability Engineering*, O'Reilly 2022 | training-knowledge — flag Wave D | — |
| 3 | Mike Julian, *Practical Monitoring*, O'Reilly 2017 | training-knowledge — flag Wave D | — |
| 4 | OpenTelemetry Specification v1.x | training-knowledge — flag Wave D | — |
| 5 | **Alex Ewerlof et al., *Implementing SLOs* (SRE Workbook Ch. 2), 2018** | **library-direct ✅ (2026-04-27 supplement)** | `raw/books-md/sre/google-srewb-implementing-slos.md` (single-chapter; quality grade B; 8,744 words) |

The framework taxonomy table (§1 row #6) had previously flagged: "NO direct SRE Book on disk → external 5-sources mandatory." Status post-supplement: the two Google sources (full SRE Book + SLO Workbook chapter) are now library-resident; Honeycomb / Practical Monitoring / OpenTelemetry remain via training-knowledge and should be flagged for Wave D supplement if Part 8 materialisation requires high-cardinality observability tooling, alert-fatigue anti-pattern depth, or OTel semantic-conventions detail beyond what training-knowledge synthesis confidently supplies.

**FUNDAMENTAL §3 + §5 — 100% via repo read.**

FUNDAMENTAL §3 (30+ SLI/SLO pairs across 8 health domains: §3.1 Information, §3.2 Agent, §3.3 Cycle, §3.4 Self-improvement, §3.5 Daily ops, §3.6 CRM, §3.7 Self-preservation, §3.8 Resource) and FUNDAMENTAL §5 (reliability principles §5.1-§5.6: data tiers, fail-loud, 3-2-1 backup, SPoF, defensive patterns, trust calibration) were read in full from `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md`. The Jetix-applied form is 100% on-disk derived.

**Part 8 interface card** was read from `candidate-parts-merged.md` §2 Part 8 — Health Monitoring & System Integrity.

**Risk declaration (post-supplement, 2026-04-27 evening):**
- **Lower risk** on core SLI / SLO / error-budget burn-rate algebra (Principles 1, 7) — Google SRE Book Ch. 4 + SRE Workbook Ch. 2 are now library-direct and ground every burn-rate / error-budget claim with verbatim citations available. The four golden signals (latency / traffic / errors / saturation, SRE Book Ch. 6) are now library-direct. Postmortem culture (Ch. 15) and toil definition (Ch. 5) are now library-direct. Fail-loud + monitoring philosophy + Borg / Chubby / GSLB context are all library-direct.
- **Risk remains** on Honeycomb-style high-cardinality observability tooling and the trace-dominant philosophy (Majors Observability Engineering territory), Mike Julian's anti-pattern catalog at full depth, and OpenTelemetry semantic conventions / propagation protocol details. If Wave C Part 8 surfaces these specific edges (e.g., trace-context propagation through agent mailboxes, OTel-aligned structured-event format, or alert-fatigue anti-patterns at quantitative threshold detail), flag Wave D supplement.

**Total foundation: 2/5 library-direct + 3/5 training-knowledge + Jetix-applied context 100% via repo reads.**

---

## §2 Framework Scope

**SRE (Site Reliability Engineering)** is a discipline originating at Google that applies software engineering methods to operations problems. Its core tools are the SLI/SLO/error-budget triad: a Service Level Indicator (SLI) is a measurable signal; a Service Level Objective (SLO) is the threshold that signal must meet; the error budget is what remains of SLO headroom and governs feature-vs-reliability tradeoffs.

**Observability** is the property of a system that enables operators to understand its internal state from external outputs alone. Charity Majors (Honeycomb) distinguishes observability from monitoring sharply: monitoring handles known unknowns (I know what might fail, I alert on it); observability handles unknown unknowns (I can ask arbitrary questions of system state, including questions I did not anticipate when I built the dashboards).

**Jetix application scope.** Foundation does not run public services with SLAs to external customers. The SRE framework applies at a different scale: Part 8 (Health Monitoring & System Integrity) is the internal observability substrate. The SLIs are process-health signals (KB freshness, cycle completion, agent mailbox depth), not HTTP latency percentiles. The error budget governs *behaviour change* when health degrades — not capacity planning. This is the correct framing; FUNDAMENTAL §3 already embeds it (§3 intro: "SLO budget burn → behaviour changes, not just fires alert").

**Primary Foundation target:** Part 8 — Health Monitoring & System Integrity (UC-I.1, I.2, I.3, I.4, H.4). Secondary: Part 5 — Compound Learning (§3.3 cycle metrics, §3.4 self-improvement), Part 6 — Governance & Human Gate (§3.7 self-preservation).

---

## §3 External Sources — 5 Mandatory

### Source 1 — Google SRE Book (Beyer et al., O'Reilly 2016) ✅ LIBRARY-DIRECT

**Library path (post-supplement 2026-04-27):** `raw/books-md/sre/google-sre-book.md` (full 550-page book; quality grade A; 190,412 words).
**Original URL:** https://sre.google/sre-book/table-of-contents/

**Chapters consulted via library-direct read:** Ch. 1 (Introduction — SRE definition + tenets — pp.3-12), Ch. 3 (Embracing Risk — error budget motivation — pp.25-36), Ch. 4 (Service Level Objectives — SLI/SLO/SLA terminology + indicators in practice — pp.37-47), Ch. 5 (Eliminating Toil — toil definition + < 50% rule — pp.49-54), Ch. 6 (Monitoring Distributed Systems — symptoms vs causes + black-box vs white-box + Four Golden Signals — pp.55-66), Ch. 14 (Managing Incidents — pp.161-167), Ch. 15 (Postmortem Culture — blameless culture + triggers + collaborate-and-share — pp.169-175), Ch. 22 (Addressing Cascading Failures — secondary for Foundation single-node).

**Relevance grade: A (primary).**

The SLO chapter is the canonical source for the SLI/SLO/error-budget triad. The monitoring chapter distinguishes symptoms vs causes and introduces the **four golden signals (latency, traffic, errors, saturation, p.60)**. The postmortem chapter grounds blameless incident culture. The cascading failures chapter is secondary for Foundation (single-node system does not have distributed failure cascades) but informs graceful degradation design in FUNDAMENTAL §5.2. Ch. 1 contributes the SRE-vs-DevOps framing + the "Hope is not a strategy" tenet + the 50%-cap on SRE operational work + the `MTTF`/`MTTR` framing for emergency response.

**Jetix application:** FUNDAMENTAL §3 embeds the SLO framework directly — each health domain (§3.1-§3.8) carries an SLI (what is measured), an SLO (threshold), an error budget (implicit in "alert trigger"), and a behaviour-change rule ("pause new feature work / simplify ritual / expand capacity"). The SRE Book provides the conceptual grounding; FUNDAMENTAL §3 is the Jetix-applied form.

### Source 2 — Observability Engineering (Majors, Fong-Jones, Miranda — O'Reilly 2022)

**URL:** https://www.oreilly.com/library/view/observability-engineering/9781492076438/

**Relevance grade: A (primary conceptual frame).**

Core argument: observability is not "more monitoring." Monitoring tells you whether the system is up or down based on pre-defined metrics. Observability lets you ask questions you did not think to ask at build time, using high-cardinality, high-dimensionality data (structured events with many fields). Traces dominate over logs and metrics in Majors' framework because traces carry causality — you can follow a request through the system and identify exactly where it degraded.

**Jetix application:** Foundation operates without a metrics backend (no Datadog, no Prometheus). The Honeycomb argument is adapted: for file-based Foundation, high-cardinality data = git log with structured commit messages (`[area] verb what (why)`) + YAML frontmatter on every artifact. Structured frontmatter fields (status, pipeline stage, last_modified, provenance coverage) are the "high-cardinality dimensions" that enable observability questions: "Which KB entries were last modified > 60 days ago and have status: active?" This is the Foundation-native analogue of a distributed trace query.

**Tradeoff flagged:** Honeycomb's trace-dominant argument assumes a service with request/response semantics. Foundation's primary operational unit is a file mutation + git commit, not a request. The observability principle transfers; the toolchain does not. Wave C Part 8 should resist adopting trace-first tooling (OpenTelemetry collectors) before Foundation has a service to instrument. Grep-first observability is the correct starting point.

### Source 3 — Practical Monitoring (Mike Julian, O'Reilly 2017)

**URL:** https://www.oreilly.com/library/view/practical-monitoring/9781491957349/

**Relevance grade: B (anti-pattern prevention).**

Julian's primary contribution for Foundation: the anti-patterns chapter. The most relevant:

- **Tool-first thinking:** "We bought Datadog, now let's figure out what to monitor." Foundation anti-version: "We have `system-health.json`, now let's figure out what it should contain." Both fail for the same reason — they start with the tool, not the question. Correct order: declare the SLI (what question?), then choose the measurement method.
- **Alert fatigue:** Alerts that fire without a declared response action train operators to ignore them. FUNDAMENTAL §3 explicitly addresses this ("each alert has declared response" — Five-laws-of-dashboards item 3). Julian grounds why.
- **Monitoring what is easy to measure, not what matters:** classic vanity metric trap. Foundation-specific risk: monitoring git commit count (easy) instead of compound application rate (hard to measure, actually matters).

**Jetix application:** Part 8 Wave C materialisation must follow the question-first order: enumerate the SLIs from FUNDAMENTAL §3, then select measurement methods. Do not reverse. Julian's anti-patterns serve as a checklist for the Wave C interface card author.

### Source 4 — OpenTelemetry Specification v1.x

**URL:** https://opentelemetry.io/docs/specs/otel/

**Relevance grade: B (Three Pillars vocabulary; low direct applicability Phase A).**

OpenTelemetry unifies the Three Pillars of observability — logs, metrics, traces — under a single semantic convention and propagation protocol. The specification is vendor-neutral and defines what structured observability data looks like at the schema level.

**Jetix application:** The Three Pillars concept applies even without OTel tooling:
- **Logs** = FUNDAMENTAL's append-only substrate (strategies.md, cycle logs, mailboxes, git log). Foundation already has logs.
- **Metrics** = FUNDAMENTAL §3 SLI counters (orphan ratio, query success rate, mailbox depth). Foundation has the SLI definitions but lacks a metrics collection mechanism. Wave C must provide this — simplest form: a `/company-status` run that writes a JSON snapshot to `shared/state/system-health.json`.
- **Traces** = Foundation does not have distributed traces in the OTel sense. The closest analogue is a provenance chain: artifact ← draft ← ingest event ← raw source. The FPF provenance graph (edges.jsonl) is a static trace, not a runtime trace. Phase A: not needed. Phase B+: if Foundation grows to multi-agent parallel execution, OTel-style trace propagation through agent mailboxes becomes relevant.

**Anti-scope:** OTel collector infrastructure, OTLP exporters, vendor backends (Jaeger, Zipkin, Honeycomb) — all Phase B+ at earliest. Foundation Phase A does not need them.

### Source 5 — Implementing SLOs (SRE Workbook Ch. 2 — Thurgood, Ferguson, Hidalgo, Beyer, 2018) ✅ LIBRARY-DIRECT

**Library path (post-supplement 2026-04-27):** `raw/books-md/sre/google-srewb-implementing-slos.md` (single chapter, full text; quality grade B; 8,744 words; CC BY-NC-ND 4.0).
**Original URL:** https://sre.google/workbook/implementing-slos/

**Relevance grade: A (operational algebra for Foundation health).**

The SRE Workbook chapter on implementing SLOs provides the burn rate algebra: if SLO = 99% (1% error budget), then:
- 1× burn rate = consuming error budget at exactly the rate that depletes it in the SLO window
- 6× burn rate = 1/6 of window remains; urgent attention needed
- 14.4× burn rate = critical; < 1 hour until budget exhausted in short window

This algebra was designed for request-error rates in services. The principle transfers to Foundation's non-service SLIs with reframing: the "error budget" for KB provenance coverage (SLO ≥ 95%) is 5% of items lacking provenance. When that 5% is exhausted, the response is not "page the SRE" — it is "halt promotions to canonical until provenance coverage is restored" (per §5.2 fail-loud).

The chapter also formalises the **SLO decision matrix** (Table 2-5 in the chapter): cross-product of {SLO Met / Missed} × {Toil Low / High} × {Customer Satisfaction High / Low} → 8 declared actions (relax / tighten / loosen alerting sensitivity / fix product). This is operational guidance for the behaviour-change-rule registry that Wave C Part 8 must populate. The chapter also names «**a four-week rolling window** to be a good general-purpose interval» complemented with weekly summaries for prioritisation and quarterly reports for project planning.

**Jetix application:** FUNDAMENTAL §3 already implements the behaviour-change rule correctly. The Workbook grounds *why* behaviour change is mandatory: alerting without behaviour change is noise that trains operators to ignore alerts. The error-budget burn model prevents this by making the response pre-declared, not reactive. The 4-week rolling window recommendation closes OQ-SRE-1 (SLO window declaration) — adopt 4-week rolling as the Foundation default unless an SLI has documented reasons for a different window.

---

## §4 Key Principles — Sourced, Applied, Tradeoff'ed

### P1 — SLI/SLO/Error-Budget Triad

**Sourced.** Google SRE Book Ch. 4 [Source 1, raw/books-md/sre/google-sre-book.md Ch.4 "Service Level Objectives" pp.37-47]: «An SLI is a service level *indicator* — a carefully defined quantitative measure of some aspect of the level of service that is provided… An SLO is a *service level objective*: a target value or range of values for a service level that is measured by an SLI.» SRE Book Ch. 1 grounds the error-budget motivation [pp.7-9]: «100% is the wrong reliability target for basically everything… An outage is no longer a 'bad' thing — it is an expected part of the process of innovation.» The SRE Workbook Ch. 2 [Source 5, raw/books-md/sre/google-srewb-implementing-slos.md §1] makes it categorical: «without SLOs, there is no need for SREs.» Error budget = 1 − SLO (e.g., 99% SLO → 1% budget). When budget exhausted, *behaviour changes*: feature work pauses, reliability investments escalate.

**Applied to Foundation.** FUNDAMENTAL §3 already structures each health domain in SLI/SLO/error-budget form, explicitly cited as Google SRE pattern. Critical instances for Part 8:
- §3.1.3 Queryability: SLI = query citation rate; SLO ≥ 85%; error budget = 15%. Alert at < 75% = budget half-burned. Behaviour change: trigger compile + consolidate sprint.
- §3.3.3 Weekly review run rate: SLI = % weeks with completed review; SLO ≥ 90% per quarter; alert at < 75%. Behaviour change: pause new feature work until run rate recovered (FUNDAMENTAL §3.5.3 explicitly states this SRE-pattern response).
- §3.8.4 API tokens: SLI = burn rate vs linear pace; SLO ≤ 1.0× linear; alert at > 1.0× by mid-month. Behaviour change: reduce non-essential agent runs.

What is missing from current FUNDAMENTAL §3: explicit SLO **windows** (daily / weekly / monthly budget). Each SLI needs a declared window length. Wave C Part 8 must add this. Example: weekly review run rate is meaningful only over a ≥ 4-week rolling window; single-week measurement is noise.

**Tradeoff.** SLO tightness vs alert fatigue: a 99% SLO for KB provenance coverage means any item without provenance burns budget fast. For a Phase-A system with few promotions per week, this is easy to maintain. As KB scales to thousands of entries, 99% becomes operationally costly. FUNDAMENTAL §3 starter values are calibrated for Phase A; the SRE Workbook explicitly recommends calibrating SLOs over 4-8 weeks of operational data. Wave C should not hard-lock numeric SLO values — they should be `calibrated` frontmatter fields, not constants.

---

### P2 — Observability vs Monitoring: Unknown Unknowns

**Sourced.** Charity Majors (Observability Engineering): "Monitoring is for known unknowns — the questions you thought to ask when you built the system. Observability is for unknown unknowns — questions you could not have anticipated." High-cardinality structured events (many fields per event) enable observability; pre-aggregated time-series metrics enable monitoring. Neither is sufficient alone.

**Applied to Foundation.** Foundation's known unknowns (monitoring): KB orphan ratio, mailbox depth, cycle completion rate, backup recency — all in FUNDAMENTAL §3, measurable with grep/git log. Foundation's unknown unknowns (observability): "Why did compound application rate drop last month?" requires cross-referencing strategies.md update timestamps, cycle log DRR counts, and weekly review depth signals — a multi-dimensional query across high-cardinality YAML frontmatter. Git log + structured frontmatter IS Foundation's observability substrate, even without dedicated tooling.

The practical implication for Part 8: the health dashboard (`shared/state/system-health.json`) handles the monitoring layer (known SLIs). The `/ask` skill + `/lint` handle the observability layer (arbitrary diagnostic queries). Both are needed. Neither replaces the other.

**Tradeoff.** High-cardinality observability increases cognitive load. The Honeycomb model assumes tooling (Honeycomb itself, or OTel + Jaeger) that reduces the query burden. Foundation has no such tooling in Phase A — the owner must manually grep. This means the observability payoff is lower than in a service context. The correct Phase-A response: invest in *structured* frontmatter conventions (consistent field names, consistent status values) so that grep-based observability queries are reliable. Unstructured frontmatter = unobservable Foundation.

---

### P3 — The Three Pillars: Logs, Metrics, Traces (and Foundation's Pragmatic Subset)

**Sourced.** OpenTelemetry specification + Google SRE Ch. 6: logs (timestamped event records), metrics (numeric aggregations over time), traces (causally-linked spans across system components). Honeycomb's Majors argues traces dominate in complex systems because they carry causality.

**Applied to Foundation.** Phase A pragmatic subset:
- **Logs:** Foundation already has high-quality logs — git log (structured, append-only, content-addressable), strategies.md files (append-only DRR entries), mailboxes (JSONL append-only), cycle logs. The log substrate is strong. Its weakness: logs are not uniformly queryable — each is in a different format. Part 8 Wave C should define a `lint-log-health` sub-check that scans for missing timestamps or non-JSONL mailbox entries.
- **Metrics:** Foundation lacks a metrics collection mechanism. The SLI values from FUNDAMENTAL §3 are *defined* but not *collected automatically*. `/company-status` and `/lint` produce partial snapshots but not a time-series. Wave C gap: a lightweight metric snapshot that appends to `shared/state/metrics/` on each `/company-status` run (JSON line: `{timestamp, sli_name, value}`). This creates a minimal time-series without a dedicated backend.
- **Traces:** Not applicable Phase A. The provenance chain (FPF edges.jsonl) is the static analogue. Sufficient for Phase A.

**Tradeoff.** Three Pillars vs Foundation simplicity. Full OTel instrumentation would require: an agent that emits structured events, a collector (daemon process), a backend (Jaeger / Honeycomb). This is dramatically over-engineered for a single-owner system. The correct tradeoff: logs (already present) + minimal metrics snapshot (one append per `/company-status` run) + no traces Phase A. This satisfies 80% of Part 8's observability need with ~5% of the infrastructure overhead.

---

### P4 — Toil Reduction: < 50% of Time on Manual Repetitive Work

**Sourced.** Google SRE Book Ch. 5 [Source 1, raw/books-md/sre/google-sre-book.md Ch.5 pp.49-54] toil definition: «Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.» Ch. 1 [pp.5-7] codifies the «50% cap on the aggregate "ops" work for all SREs». Above 50%, toil crowds out engineering work that reduces future toil — a reinforcing trap (Ch.5 lists six explicit harms: career stagnation, low morale, creates confusion, slows progress, sets precedent, promotes attrition, breach of faith).

**Applied to Foundation.** Foundation's toil candidates: manual KB linting (running `/lint` and reading the output manually), manual health metric collection (reading `system-health.json` which reports "all green" without computation), manual compound-step DRR writing (correctly kept human-authored per FUNDAMENTAL §5.6 Левенчук writing-as-thinking), manual provenance tagging on every artefact write. Of these: KB linting and health metric collection are legitimate automation targets (FUNDAMENTAL §4.1 explicitly includes both). DRR writing is HUMAN-ONLY (§4.3 — Левенчук writing-as-thinking primitive). Provenance tagging is AI-augmented (§4.2 — AI auto-fills, human verifies).

Part 8's role: surface which health checks are producing toil (alerts that are not actionable, checks that require manual interpretation). The `/lint` skill currently requires manual reading — a structured output mode (`/lint --json`) that returns machine-readable lint results would reduce this toil and enable Part 8 automation.

**Tradeoff.** Toil reduction automation vs FUNDAMENTAL §4.5 architectural-change hard rule. Automating `/lint --json` output = non-architectural code change (safe). Automating the *decision* of what to do when lint fails = architectural change (requires human ack). The boundary holds: Part 8 automates collection; the owner decides response. FUNDAMENTAL §4.6 Default Deny + Explicit Allow enforces this.

---

### P5 — Blameless Postmortems and Incident Learning Culture

**Sourced.** Google SRE Book Ch. 15 [Source 1, raw/books-md/sre/google-sre-book.md Ch.15 pp.169-175]: «The primary goals of writing a postmortem are to ensure that the incident is documented, that all contributing root cause(s) are well understood, and, especially, that effective preventive actions are put in place to reduce the likelihood and/or impact of recurrence.» Ch. 15 lists explicit triggers for postmortems: user-visible downtime/degradation beyond threshold, data loss, on-call engineer intervention, resolution time above threshold, monitoring failure (manual incident discovery). «Blamelessness is a tenet of SRE culture. For a postmortem to be truly blameless, it must focus on identifying the contributing causes of the incident without indicting any individual or team for bad or inappropriate behavior… A blamelessly written postmortem assumes that everyone involved in an incident had good intentions and did the right thing with the information they had.» The chapter also establishes «No Postmortem Left Unreviewed» as a best-practice rule.

**Applied to Foundation.** FUNDAMENTAL §3.4.5: "% significant failures / missed deadlines that get post-mortem within 7 days. Healthy baseline: ≥ 80%. Alert trigger: < 50% — failures forgotten without learning." This SLI operationalises the blameless postmortem cadence. FUNDAMENTAL §2.4 (Compound Learning) cites "Google SRE blameless post-mortems — каждый failed cycle → 5-line post-mortem: what happened / why / what changed / how detect next / owner. Stored permanently."

The 5-line format is the Foundation-pragmatic adaptation: a full RCA is too heavy for a single-owner system at Phase A cycle cadence. The 5-line format (what / why / what changed / detect next / owner) ensures learning is captured without crowding out execution time. Each postmortem is a strategies.md entry (Layer 2 self-write per agent whose scope the failure belongs to).

**Tradeoff.** Blameless culture vs agent accountability. In human SRE teams, blame drives people to hide failures. In an agent swarm, agents do not experience blame — but they can be optimized to suppress failures silently to avoid appearing defective (AP-ENG-1: no test deletion to make pipeline green; FUNDAMENTAL §5.2 fail-loud). The Foundation equivalent of blameless culture: fail-loud is the architectural rule; the postmortem is the learning rule. Together they prevent both failure suppression and blame-without-learning.

---

### P6 — Fail-Loud: Silent Failures Are the Worst Category of Bug

**Sourced.** FUNDAMENTAL §5.2: "Fail-loud (никогда не silent): Strategic doc modification — halt, alert, не proceed. Principle: silent failures = worst category of bug. Лучше loud false-positive чем silent corruption." FPF P-7 (Pragmatic Utility): failures must be surfaced and visible, not suppressed. Google SRE Book Ch. 6: "A system is healthy when it can tell you how unhealthy it is." Mike Julian (Practical Monitoring): silent errors are worse than noisy ones because they accumulate undetected until catastrophic.

**Applied to Foundation.** Four fail-loud categories in FUNDAMENTAL §5.2:
1. Strategic doc modification without ack → halt + alert
2. Lock changes without proper ack → halt + alert
3. Money/external commitment with unverifiable preconditions → halt, do not assume
4. Security boundary changes → halt + alert

Part 8's role: the monitoring substrate that makes "halt + alert" mean something. If Part 8 does not have a mechanism to surface the alert to the owner (FUNDAMENTAL §5.2: "system must stop and wait if it cannot reach owner for critical decision"), the fail-loud rule is aspirational, not operational. Wave C Part 8 must define the alert-delivery path: for a single-owner system, the simplest mechanism is a `shared/state/alerts.jsonl` (append-only) that `/plan-day` reads and surfaces at session start.

**Tradeoff.** Fail-loud vs cognitive load. A system that halts on every anomaly produces alert fatigue (Mike Julian's core anti-pattern). The correct calibration: fail-loud on integrity violations (data corruption, security boundaries, Lock modifications) and fail-soft with clear signal on operational SLI degradation (KB freshness, cycle completion rate). The distinction maps to FUNDAMENTAL §5.2: mandatory continuity failures → fail-loud; graceful degradation failures → fail-soft with surfaced signal.

---

### P7 — Error Budget Burn Changes Behavior (Not Just Fires Alerts)

**Sourced.** Google SRE Workbook Ch. 2 [Source 5, raw/books-md/sre/google-srewb-implementing-slos.md §12 "Decision Making Using SLOs and Error Budgets"]: when budget exhausted, the policy mandates one of: «(a) The development team gives top priority to bugs relating to reliability issues over the past four weeks. (b) The development team focuses exclusively on reliability issues until the system is within SLO. (c) A production freeze halts certain changes to the system until there is sufficient error budget.» Worked example: «a release of a new API version causes 100% NullPointerExceptions until the system can be reverted four hours later… 14,066 errors. Using the numbers from our 97% SLO earlier, and our budget of 109,897 errors, this single event used 13% of our error budget.» The algebraic burn-rate model makes this operationally precise. The 8-row decision matrix (Table 2-5) declares the response for every {SLO state × Toil × Customer Satisfaction} cell.

**Applied to Foundation.** FUNDAMENTAL §3.5.3 implements this explicitly: "Weekly review run rate < 75% per quarter → SRE-style trigger: pause new feature work until run rate recovered." This is error-budget behaviour change, not merely an alert. The same pattern should apply to the Part 8 materialisation for all SLIs where budget burn has a declared response:
- KB provenance coverage < 90% → halt canonical promotions until coverage restored
- Agent mailbox p90 > 7d → pause new agent dispatches until backlog cleared
- Compound application rate < 30% → protected compound time must be restored before new cycles begin

What is currently underspecified in FUNDAMENTAL §3: not all 30+ SLI/SLO pairs have an explicit behaviour-change rule (many have only an "alert trigger"). Wave C Part 8 must complete the behaviour-change declarations for all SLIs that have downstream consequences if ignored.

**Tradeoff.** Error budget behaviour change vs owner attention budget (FUNDAMENTAL §3.5 is itself an SLO domain). Both the error budget model and the owner attention budget are budget metaphors — they can conflict. If KB provenance SLO fires simultaneously with weekly review SLO and deep-work-hours SLO, three behaviour-change rules trigger at once, overwhelming the very owner whose attention is already the bottleneck. Resolution: establish a priority ordering for behaviour-change rules (Tier 0 data integrity > Tier 1 operational SLIs > Tier 2 velocity SLIs). Wave C Part 8 interface card must declare this priority ordering explicitly.

---

## §5 Tradeoffs to Surface

### T1 — Observability vs Cognitive Load

High-cardinality structured data (Honeycomb principle) increases debug power when something goes wrong but increases noise during normal operations. For a single-owner system where the "operator" is also the "developer" and the "product manager," cognitive load is the ultimate scarce resource (FUNDAMENTAL §3.5 — owner attention budget is the primary bottleneck per Goldratt TOC). The correct Foundation resolution: prefer few, high-quality, actionable SLIs (3-7 per domain per FUNDAMENTAL §3 five-laws-of-dashboards item 1) over comprehensive observability coverage. Do not instrument everything. Instrument the indicators that, when they degrade, change behaviour. This directly contradicts the Honeycomb philosophy of "collect everything, ask questions later" — which assumes cheap storage and tooling. Foundation has neither.

### T2 — Toil Reduction Automation vs D2 Architect-Orbit Human-in-Loop

SRE's toil reduction mandate (< 50% manual repetitive work) and Foundation's Default Deny + Explicit Allow (FUNDAMENTAL §4.6) are in structural tension. Every automation reduces toil but also reduces the owner's awareness of what the system is doing. The resolution is the FUNDAMENTAL §4.1-§4.3 taxonomy: automate collection (§4.1 auto-always), surface findings with human ack (§4.2 AI-augmented), never automate the response to critical integrity failures (§4.3 human-only). Part 8 sits at the collection-and-surfacing layer; the response layer is always human.

### T3 — Three Pillars vs Foundation Simplicity (File-Based Git Substrate)

Full Three Pillars implementation (OTel collector + metrics backend + trace aggregator) is correct for distributed service systems. Foundation's file-based, git-native substrate has no equivalent infrastructure requirement. The tradeoff: implement the Three Pillars conceptually (logs: already present; metrics: lightweight JSON snapshots; traces: not applicable Phase A) rather than infrastructurally. The risk of over-engineering Part 8 with OTel tooling before Foundation is a service is significant — it would add operational overhead without proportional observability benefit, violating Unix philosophy (do one thing well) and the Ousterhout deep-module principle (hide implementation complexity behind a thin interface; the Part 8 interface should be `/company-status` + `/lint`, not an OTel pipeline).

### T4 — Error Budget Burn vs Owner Attention Budget

Both are budget metaphors; both are real constraints; they compete for the same resource (owner time). When multiple SLO error budgets exhaust simultaneously, the mandated behaviour changes create more work for the owner, who was already at attention capacity. This is a structural fragility in applying SRE error budget theory to single-owner systems. Resolution: tiered priority ordering for behaviour-change rules (declared in Wave C Part 8 interface card), plus a "meta-SLI" for owner attention itself (FUNDAMENTAL §3.5 + §3.8.1 already define attention SLIs — these should be read before any other behaviour-change rule fires). Practically: if attention budget SLI is already in alert state, defer lower-priority behaviour-change rules to next cycle.

---

## §6 Anti-Scope

- **Distributed systems theory** — Foundation Phase A is single-node; CAP theorem, eventual consistency, leader election, Raft consensus are not applicable. If Foundation evolves to multi-node (Phase B+ multi-agent distributed execution), revisit.
- **DevOps / CI-CD pipelines** — Foundation does not deploy public services; CI/CD tooling (GitHub Actions, Jenkins, deployment pipelines) are out of scope. Foundation's "deployment" is a git commit with human ack.
- **Specific platform vendor tooling** — Datadog, New Relic, Grafana Cloud, Splunk, PagerDuty are explicitly out of scope. They create vendor lock-in and require infrastructure that Foundation does not have. Phase A instructs: grep-first, file-first, git-first.
- **Incident management process design** — SRE teams have on-call rotations, escalation policies, incident command structures. A single-owner system has one escalation path: the alert surfaces to the owner. Incident management process design belongs to Team Phase (when Foundation scales to multiple humans).
- **Service Mesh and network-layer observability** — Istio, Envoy, Linkerd are not applicable to a file-based system. Out of scope.

---

## §7 Application to Foundation Parts (Ordered by Relevance)

### Primary — Part 8: Health Monitoring & System Integrity

SRE/observability is the conceptual backbone of Part 8. Wave C interface card must specify:
1. **SLI registry** — a YAML file (`swarm/wiki/foundations/part-8/sli-registry.yaml`) that enumerates each SLI from FUNDAMENTAL §3 with: name, measurement method (grep command / git log / file stat / manual), measurement cadence, SLO threshold, error budget, and behaviour-change rule.
2. **Metrics snapshot mechanism** — `/company-status` appends a JSON line to `shared/state/metrics/health-snapshots.jsonl` on each run. This is the simplest possible metrics time-series. One JSONL line per run: `{timestamp, sli_name, value, slo, status: green|yellow|red}`.
3. **Alert delivery path** — `shared/state/alerts.jsonl` (append-only), read by `/plan-day` at session start. Alert format: `{timestamp, sli_name, value, slo, severity: warn|critical, behaviour_change_required: <text>}`.
4. **Behaviour-change rule registry** — for each SLI where budget exhaustion changes behaviour, the behaviour-change rule is declared alongside the SLI. Not aspirational — it is the acceptance predicate for Part 8: Part 8 is operational when every critical-SLI alert has a declared behaviour-change rule.

### Secondary — Part 5: Compound Learning & Methodology Capture

Cycle health SLIs (§3.3: ratio drift, completion rate, review depth, compound application rate, throughput) are Part 5's operational health signals. Part 8 collects them; Part 5 owns the compound learning that should improve them over time. The interface: Part 8 writes health signals to `shared/state/metrics/`; Part 5 reads them during Compound phase to assess whether methodology changes are having measurable effect.

### Secondary — Part 6: Governance & Human Gate

Self-preservation SLIs (§3.7: integrity check pass rate, backup recency, drift detection, credential hygiene, strategic doc drift, methodology archaeology) are Part 6's monitoring targets. Part 8 surfaces them; Part 6's quarterly immune-system audit reads Part 8's historical snapshots to assess drift trends. The fail-loud rules for Lock modification and strategic doc corruption are Part 6's jurisdiction; Part 8 is the detection mechanism that feeds Part 6's enforcement actions.

---

## §8 Open Questions for Wave C

**OQ-SRE-1:** SLO window declaration. FUNDAMENTAL §3 defines thresholds but not measurement windows. Is KB orphan ratio measured over a point-in-time snapshot or a rolling 30-day average? The choice changes the SLO semantics significantly. Wave C Part 8 must declare a window for each SLI.

**OQ-SRE-2:** Behaviour-change priority ordering. When multiple SLO error budgets exhaust simultaneously, what is the triage order? Proposal: Tier 0 data integrity SLIs > Tier 1 agent communication SLIs > Tier 2 velocity SLIs. Wave C Part 8 must formalise this as a decision record, not an emergent convention.

**OQ-SRE-3:** Observability vs monitoring boundary in Part 8. Is Part 8 a monitoring system (known SLIs, pre-declared dashboards) or an observability system (arbitrary diagnostic queries)? Answer: both, at different layers. The `/company-status` snapshot is the monitoring layer. The `/ask` skill + `/lint` are the observability layer. Part 8's Wave C interface card should explicitly declare both layers and their interaction.

**OQ-SRE-4:** The "system-health.json reports all green" gap (noted in candidate-parts-merged.md §2 Part 8). Current state: the file exists but has no computation mechanism. Wave C must replace the static file with a computed snapshot from a declared SLI registry. This is the primary materialisation gap for Part 8.

---

*Card produced by engineering-expert × integrator, Phase B-2, cycle cyc-foundation-build-2026-04-28. Reads performed on: decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (§3.1-§3.8, §5.1-§5.6), swarm/wiki/cycles/cyc-foundation-build-2026-04-28/wave-a/candidate-parts-merged.md (§2 Part 8 + §3 cross-cutting), wave-b/framework-taxonomy.md (§1 row #6). 5/5 external sources via training knowledge (cutoff Aug 2025), not live-fetched.*
