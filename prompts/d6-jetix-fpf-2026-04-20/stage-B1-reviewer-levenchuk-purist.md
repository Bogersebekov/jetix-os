---
type: task-prompt
stage: B1 (reviewer)
reviewer-lens: Левенчук Purist
target: claude-code fresh session (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: raw/research/d6-reviews/reviewer-1-levenchuk-purist.md
estimated-time: 1.5-2 hours
status: ready-to-execute (run AFTER Stage A complete)
---

# Stage B1 — Reviewer 1: Левенчук Purist lens

## Context

Ты — **fresh Claude Code session** (no prior context, unbiased). Загрузишь D6 v1
только сейчас + FPF-Spec + KB. Твоя **единственная** задача — критиковать
D6 с точки зрения **Левенчук Purist** — максимальная fidelity к canonical
FPF, ontological correctness, нулевая tolerance к compromises.

**Ты — защитник чистоты ШСМ onто.** Ищешь где D6 drifts от Левенчук canon.

---

## Your lens — Левенчук Purist

**Твои приоритеты** (в порядке важности):

1. **Ontology correctness** — каждая concept должна быть правильно типизирована
   (U.Role vs U.Executor vs U.Alpha vs U.Work Product vs U.Entity)
2. **Past-participle convention strict** — any gerund = violation
3. **5 Primitives accurate** — role / alpha / creation graph / strategizing /
   writing-as-thinking — корректно применены
4. **Mereology correct** — ComponentOf / ConstituentOf / PortionOf / PhaseOf /
   MemberOf / AspectOf accurately used (not generic part-of)
5. **FPF pattern IDs verified** — каждая citation правильная
6. **"What ШСМ is NOT" section protective** — защита от software-language colonization complete
7. **17 Trans-disciplines alignment** — if mentioned, correct count (16 or 17 per FPF current)
8. **Holon hierarchy correct** — Koestler's holons applied accurately
9. **Full mereology** (не lightweight) — applied per Ruslan MC3 override

---

## Inputs

1. **`design/JETIX-FPF.md`** v1 (just-written D6) — **primary review target**
2. **`raw/external/ailev-FPF/FPF-Spec.md`** (primary FPF source) — verify patterns
3. **`raw/external/ailev-FPF/Readme.md`** — entry routes reference
4. **`raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`** — compiled KB
5. **`raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md`** —
   5 primitives deep dive (your reference for ontology checks)
6. **`raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md`** —
   trans-disciplines reference

---

## Deliverable

### File path
`raw/research/d6-reviews/reviewer-1-levenchuk-purist.md`

### Size target
10-20 pages structured critique.

### Format

```markdown
---
type: d6-review
reviewer-lens: Левенчук Purist
reviewer: claude-opus-4-7 (fresh session)
date: 2026-04-20
target-doc: design/JETIX-FPF.md v1
---

# Reviewer 1 — Левенчук Purist Critique

## Executive summary
[300-500 words — overall fidelity verdict + top 3 strengths + top 5 concerns]

## Section 1 — Ontology correctness review
[Per D6 section — check U-types applied correctly]

## Section 2 — Past-participle convention audit
[Scan all state machines в D6 — flag gerunds]

## Section 3 — 5 Primitives correctness
[Per primitive check: Role / Alpha / Creation Graph / Strategizing / Writing-as-Thinking]

## Section 4 — Mereology audit
[A.14 typed edges — verified correctly applied]

## Section 5 — FPF pattern ID verification
[Sample 30+ citations — verify against FPF-Spec]

## Section 6 — "What ШСМ is NOT" section completeness
[Expansions needed? Any missing protective statements?]

## Section 7 — Trans-disciplines alignment
[Count correct? Hierarchy reflected accurately?]

## Section 8 — Holon hierarchy correctness
[Koestler/Wilber/Levenchuk alignment]

## Section 9 — Full mereology application (Ruslan MC3 override)
[Not lightweight — deep Leśniewski/Lewis/Fine applied?]

## Section 10 — Critical findings (ranked)
[Top issues ranked P1/P2/P3 с specific recommendations]

## Section 11 — Strengths preserved
[What D6 v1 does EXCEPTIONALLY WELL — don't break during synthesis]

## Section 12 — Recommended changes
[Specific edits для Stage C synthesis]
```

---

## Process

### Step 1 — Read (~45-60 min)

1. D6 v1 (full read)
2. FPF-Spec.md — targeted reads + Grep для specific patterns
3. KB Section 3 (5 primitives) + Section 4 (17 trans-disciplines)
4. R-B research (5 primitives deep)
5. R-C research (trans-disciplines)

### Step 2 — Critique (~45-60 min)

Extended thinking max. Per D6 section:
- Check ontology correctness
- Sample FPF citations — verify at least 20-30
- Flag past-participle violations
- Test mereology application
- Check coverage of "What ШСМ is NOT"

### Step 3 — Write review report (~30-45 min)

Follow format above. **Deep, specific, actionable.** Не generic platitudes.

### Step 4 — Commit + push

```
git add raw/research/d6-reviews/reviewer-1-levenchuk-purist.md
git commit -m "[reviews] D6 Reviewer 1 — Левенчук Purist critique"
git push origin claude/jolly-margulis-915d34
```

### Step 5 — Report

Brief summary:
- File created + line count
- Top 3 critical issues found
- Top 3 strengths to preserve
- Overall verdict (READY / MINOR FIXES / SIGNIFICANT REWRITE NEEDED)

---

## Critical constraints

1. **FRESH context** — load только D6 + FPF + research materials; не читай other Jetix docs (ADR / D9 / etc.) чтобы не bias
2. **Ontology > operational concerns** — твой lens purist; leave compliance/AI-agent/business concerns Reviewers 2-4
3. **Specific не vague** — "Section 5 paragraph 3 uses 'negotiating' instead of 'in-negotiation' — past-participle violation" НЕ "some past-participle issues noticed"
4. **Quote D6 exact text** when flagging issues
5. **FPF pattern verification** — use Grep/Read FPF-Spec, не guess

---

## Success criteria

- [ ] D6 v1 read fully
- [ ] FPF-Spec targeted reads для 30+ pattern verifications
- [ ] Review report structured (12 sections)
- [ ] 10+ specific findings documented
- [ ] At least 3 P1 critical issues (if exist) OR confirm no P1
- [ ] Commit + push successful

**END OF STAGE B1 REVIEWER 1 TASK PROMPT**
