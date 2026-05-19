---
title: "SRE Error Budget — reliability bounded develop velocity"
type: concept
niche: tech
sources:
  - research/safety-develop-validation-2026-05-19/03-sre-error-budget.md (Phase 2 deep mining)
  - Google SRE Book 2016 (Beyer et al., O'Reilly; free at sre.google/books/) — primary
  - Google «Site Reliability Workbook» 2018
  - Google «Building Secure and Reliable Systems» 2020
related:
  - concepts/safety-develop-cross-disciplinary-corroboration.md (parent — strongest engineering parallel)
  - concepts/taleb-via-negativa.md (sibling — risk philosophy parallel)
tags: [#type/concept, #topic/reliability, #topic/engineering, #topic/sre, #topic/error-budget, #priority/p3]
topics: [sre, reliability, error-budget, slo, sli, sla, safety-develop]
created: 2026-05-19
updated: 2026-05-19
confidence: F2 (Google-internal verified; industry-wide adoption)
pipeline: ingested
constitutional_posture: R1 surface + R6 verbatim per claim + EP-5 F-grade
prose_authored_by: brigadier-scribe (K-5 Phase 2)
tier_status: Tier C (reference concept; complement к safety-develop-cross-disciplinary-corroboration.md)
batch_id: k-5-safety-develop-validation-2026-05-19
---

# SRE Error Budget — reliability bounded develop velocity

> **K-5 Tier C reference concept.** Strongest engineering parallel for Safety→Develop ordering. Mechanism: error budget = numeric Safety→Develop gate.

## Суть в одной строке

«Error budget» = explicit numeric allowance для unreliability spending; new releases halt when SLO violation depletes budget — operational embedding of Safety→Develop.

## Core mechanism

**Error budget = 1 - SLO target.**

Example: SLO = 99.9% availability → error budget = 0.1% per quarter ≈ 43m 49s downtime/quarter.

**Gate behaviour:**
- Budget remaining → feature velocity (push releases)
- Budget exhausted → halt releases; fix reliability

## SLI / SLO / SLA taxonomy (verbatim Google SRE Book 2016 ch. 4)

| Term | Definition |
|---|---|
| **SLI** (Service Level Indicator) | «a carefully defined quantitative measure of some aspect of the level of service that is provided» |
| **SLO** (Service Level Objective) | «a target value or range of values for a service level that is measured by an SLI» |
| **SLA** (Service Level Agreement) | «an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs they contain» |

## Counter-intuitive design principle

**Verbatim SRE Book 2016 ch. 3:**
> «100% is the wrong reliability target for basically everything… If your service is too reliable, you're spending too much on it — your engineering time should be going into features instead.»

**Implication:** Safety threshold is NOT «maximize»; it's «define right level + spend remaining budget on develop». Parallel к Maslow «prepotent but not always-dominant» (Phase 1 §3 best-practice synthesis).

## Adoption (industry-wide)

- **AWS** Well-Architected Framework Operational Excellence pillar
- **Microsoft Azure** SRE org (2018+)
- **Netflix** Chaos Engineering + SLO discipline
- **Atlassian / GitLab / GitHub** open SRE handbooks
- **DORA / Accelerate** (Forsgren+Humble+Kim 2018) — empirical validation

## Blameless postmortem (HRO bridge)

**Verbatim SRE Book 2016 ch. 15:**
> «A blameless postmortem assumes that everyone involved in an incident had good intentions and did the right thing with the information they had…»

→ Parallel к Toyota 5-Whys (Phase 3 §2.5) + NTSB accident investigation (Phase 6 §3.3) + HRO «preoccupation with failure» (Phase 6 §3.4).

## R12 alignment

**STRONG.** Error budget mechanism constrains product team's «extraction» of feature velocity from reliability budget. SRE org = institutional anti-extraction check. Users protected from reliability extraction.

## Cross-link к Safety→Develop

См. `concepts/safety-develop-cross-disciplinary-corroboration.md` — SRE = strongest engineering parallel (Phase 2 §4.2).

---

*Wiki Tier C reference concept. K-5 Phase 2 SRE deep mining substrate.*
