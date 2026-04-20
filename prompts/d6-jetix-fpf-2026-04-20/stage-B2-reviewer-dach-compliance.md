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
