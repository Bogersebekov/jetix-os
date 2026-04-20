---
type: task-prompt
stage: B2 (reviewer)
reviewer-lens: DACH Compliance Expert
target: claude-code fresh session (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: raw/research/d6-reviews/reviewer-2-dach-compliance.md
estimated-time: 1.5-2 hours
status: ready-to-execute (run AFTER Stage A)
---

# Stage B2 — Reviewer 2: DACH Compliance Expert lens

## Context

Ты — **fresh Claude Code** (unbiased). Загрузишь D6 v1 + compliance materials.
Твоя задача — критиковать D6 с точки зрения **DACH Compliance** — EU AI Act,
GDPR, BDSG, Mittelstand regulatory patterns.

---

## Your lens — DACH Compliance Expert

**Приоритеты:**

1. **EU AI Act compliance** (Aug 2026 — high-risk AI systems obligations)
2. **GDPR Article 22** (automated individual decisions protection)
3. **BDSG §38** (DPO threshold, 20+ data processors)
4. **DACH Mittelstand audit readiness** (IHK, VDMA, auditors)
5. **Boundary discipline (A.6.B L/A/D/E routing) operational**
6. **Trust tagging (F-G-R) auditable**
7. **Bias-Audit Cycle (D.5) practical implementation**
8. **Client DPA template audit-defensibility**
9. **Konsenskultur alignment** (DACH business culture)
10. **Art. 33 GDPR breach notification readiness**

---

## Specific Focus Points для актуального D6 v1

D6 v1 написан (commit `2a41927`, 2599 строк). При чтении ОБЯЗАТЕЛЬНО focus
на следующие compliance gaps — каждый с verdict + цитатой D6:

**FP1 — EU AI Act risk-tier classification missing:** D6 Section 4.5 (CP-5)
+ Section 12.10 ссылаются на EU AI Act, но **НЕТ explicit таблицы Jetix
offerings × EU AI Act risk tier**. Какой tier у Audit SKU (likely Annex III
high-risk если automated decision-impacting)? У внутренней agent automation
(general-purpose AI без direct decision authority — limited risk?)? Aug 2026
high-risk obligations конкретно как mapped к Jetix processes? Verdict:
P1 critical gap или адекватно для constitutional doc (delegated к D8/policy)?

**FP2 — Section 4.5 CP-5 "Human approval gate" operational depth:** Stated
briefly ("Human gate = sales-closer / acceptance-authority / Ruslan, no
purely autonomous client-affecting AI decisions, EU AI Act risk-proportional
Scenario C per OT3"). Missing: approval SLA window, audit trail format
(хто, когда, почему approved), escalation если gate-keeper unavailable >X
hours, fallback rules для off-hours decisions. Verdict: достаточно для
GDPR Art. 22 defense + EU AI Act human-oversight requirements?

**FP3 — Section 12.10 Bias-Audit Cycle Phase 1 simplification:** BA-0 + BA-1
+ BA-3 (no BA-2 Panel — solo Ruslan Phase 1; BA-2 activation Phase 2a).
Verdict: достаточна ли эта 3-stage cycle для:
  (a) GDPR Art. 22 individual decision defense
  (b) EU AI Act Article 14 human oversight requirements
  (c) ISO/IEC 24029-2 robustness testing expectations
Какой compliance risk если первый Mittelstand client требует formal Panel?

**FP4 — Section 4.4 Multi-View "Regulatory" view depth:** Listed как 3-5
pages "pre-mapped EU AI Act / GDPR / DORA". Но **template, schema, process
для regulatory pre-mapping** в D6 НЕ описаны deep — только promised "First
pilot: Müller GmbH audit". Verdict: must-add framework к D6, или OK relegated
к `decisions/templates/views/regulatory.yaml`?

**FP5 — F-G-R audit trail mapping table missing:** Section 4.2 + 12.7 описывают
F0-F9 + G + R abstract. Но **НЕТ explicit таблицы "Jetix artifact type ×
required F-G-R level"**: ADRs F2 minimum? Client deliverables F3 obligatory?
Strategy notes F1 acceptable? DPA contracts F3 + R-certified? Verdict:
audit-defensibility gap или delegated к `decisions/policy/trust-tagging.md`
(yet-to-be-written)?

**FP6 — Art. 33 GDPR 72h breach notification framework absent:** D6 Section
2.1 mentions `ops/gdpr-art-33.md` reference, но **НЕТ описания breach response
flow** в constitutional doc. Verdict: для regulatory audit signal — must-have
high-level framework в D6 (даже brief 1-page), или OK relegate к ops doc?

**FP7 — DPO §38 BDSG threshold criteria mismatch:** Section 2.3 mentions DPO
stub Phase 1 + activation Phase 2a "when ≥1 client requests GDPR DPA". Но
**§38 BDSG actual trigger = 20+ data processors handling personal data
regularly**, не client request. DPA request = Art. 28 GDPR processor obligation,
не §38 BDSG DPO obligation. Verdict: trigger criteria conflated — должно
быть 2 separate triggers (Art. 28 DPA = Phase 1 readiness; §38 BDSG DPO =
Phase 2a/2b headcount trigger)?

**FP8 — Konsenskultur (Section 4.1 CP-1) operational signals:** Stated, но
**operational signals для DACH cultural alignment** генеризированы (Russian/
English content). Missing: German-language proposal templates, Austrian
formality patterns (Sehr geehrte… vs Hallo), Swiss precision conventions
(Punkt-und-Komma in numbers), Mittelstand contract structure expectations
(Vertragsgestaltung, AGBs reference). Verdict: достаточно для Mittelstand
audit signal или red flag для Geschäftsführer review?

**FP9 — Section 14.4 policy docs list — 9 placeholders only:** D6 references
9 policy docs которые **ещё не написаны** (Phase 1 post-D6): boundary-
discipline.md, trust-tagging.md, sku-pricing-chr.yaml, agent-promotion-chr.yaml,
characteristic-space-conventions.md, mereology-edge-types.md, phase-transitions-
mht.md, bias-audit-cycle.md, mechanism-introduction.md, multi-method-dispatcher.md.
Verdict: для compliance audit это red flag (existing references to non-
existing docs) или OK для internal constitutional doc Phase 1 если roadmap
explicit?

**FP10 — ISO/IEC/IEEE 42010 alignment absence:** Architecture description
standard 42010 (stakeholders, concerns, viewpoints, views, models). Mittelstand
auditor + investor due diligence likely expect alignment. D6 Section 4.4
Multi-View Publication Kit — this is FPF E.17 framework, but **explicit
mapping к 42010 vocabulary** missing. Verdict: gap или OK delegate к D1
(Architecture Final)?

**FP11 — DORA (Digital Operational Resilience Act) absence:** EU DORA
applicable если Jetix handles financial-sector clients (BaFin scope). D6
mentions DORA only once в Section 4.4 viewpoint. Verdict: insufficient для
financial-sector ICP expansion, или OK Phase 1 since ai-consulting-dach
direction primary?

---

## Inputs

1. **`design/JETIX-FPF.md`** v1 — primary review target
2. **`raw/external/ailev-FPF/FPF-Spec.md`** — FPF patterns (A.6 Boundary, B.3 F-G-R, D.5 Bias-Audit)
3. **`decisions/2026-04-19-architecture-v2-approval.md`** — ADR Chunks 1-8 (compliance decisions)
4. **`decisions/gap-analysis-review-decisions-2026-04-20.md`** — Gap 1 (A.6.*), Gap 2 (B.3), OQ-03 EU AI Act, Rec-03 Bias-Audit
5. **`raw/research/architecture-research-2026-04-19/R4-knowledge-architecture-deep-research-2026-04-19.md`** и
   **R5 DACH CRM research** — если existing references relevant

---

## Deliverable

### File path
`raw/research/d6-reviews/reviewer-2-dach-compliance.md`

### Size target
10-15 pages critique.

### Format

```markdown
---
type: d6-review
reviewer-lens: DACH Compliance Expert
reviewer: claude-opus-4-7 (fresh session)
date: 2026-04-20
target-doc: design/JETIX-FPF.md v1
---

# Reviewer 2 — DACH Compliance Critique

## Executive summary
[Overall compliance-readiness verdict + top 3 strengths + top 5 concerns]

## Section 1 — EU AI Act readiness
- Risk-tier classification (OT3 Scenario C) — materialized в D6?
- High-risk obligations (Aug 2026) — coverage?
- Art. 22 GDPR защита через human-gate — applied?

## Section 2 — GDPR readiness
- Art. 13 information disclosure
- Art. 22 automated decisions
- Art. 33 breach notification (72h)
- Art. 28 processor obligations (DPA)

## Section 3 — BDSG §38 DPO compliance
- DPO role defined (external-mode)?
- 20+ data processors trigger recognized?

## Section 4 — Boundary discipline operational
- A.6.B L/A/D/E routing applied в contract/DPA templates (D6 reference)?
- Audit filter capability (show me L clauses)?

## Section 5 — Trust tagging auditability
- F-G-R convention applied в D6 sections?
- Audit trail quality?

## Section 6 — Bias-Audit Cycle (D.5) practical
- BA-0/1/2/3 cycle documented?
- Quarterly aggregation structure?
- Art. 22 defense integrated?

## Section 7 — Mittelstand audit signal
- Professional signal для DACH enterprise audits?
- Clarity для Aufsichtsrat review?
- Reference к ISO/IEC/IEEE 42010?

## Section 8 — Konsenskultur alignment
- Consensus-building patterns recognized?
- DACH business culture honored?

## Section 9 — Breach + incident response
- Art. 33 playbook referenced?
- ops/regulatory-incidents/gdpr-art-33-playbook.md integration?

## Section 10 — Critical findings ranked
[P1/P2/P3 с specific recommendations]

## Section 11 — Strengths to preserve

## Section 12 — Recommended changes для Stage C
```

---

## Process (~1.5-2h)

Similar к B1 process но с compliance lens.

Extended thinking max.

### Commit + push

```
git add raw/research/d6-reviews/reviewer-2-dach-compliance.md
git commit -m "[reviews] D6 Reviewer 2 — DACH Compliance critique"
git push origin claude/jolly-margulis-915d34
```

---

## Critical constraints

1. **FRESH context** — не bias от other reviews
2. **Compliance > ontology/AI/business** — your exclusive lens
3. **Specific regulatory citations** (GDPR Art. 22, BDSG §38, EU AI Act specific sections)
4. **Quote D6 exact text when flagging**

**END OF STAGE B2 TASK PROMPT**
