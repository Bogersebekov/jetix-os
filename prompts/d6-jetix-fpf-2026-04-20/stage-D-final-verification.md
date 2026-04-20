---
type: task-prompt
stage: D (final verification)
target: claude-code FRESH session — NO prior context (Opus 4.7, 1M)
mode: extended-thinking-max
deliverable: raw/research/d6-reviews/stage-d-final-verification.md
estimated-time: 1-2 hours
status: ready-to-execute (run AFTER Stage C)
---

# Stage D — Final Verification (Fresh Independent Session)

## Context

Ты — **BRAND NEW Claude Code session**. Нет prior context про Jetix.
Ты загружаешь ТОЛЬКО:
- D6 v2 (just-synthesized final)
- FPF-Spec.md (primary source)
- Gap Analysis (ground-truth accepted decisions)
- KB (reference для completeness check)

**Твоя задача — definitive verdict READY / NEEDS-FIXES** based on:
- Ontological correctness
- FPF pattern ID accuracy
- Past-participle convention strict
- Completeness vs Gap Analysis adoptions
- Hallucination absence
- Quality threshold (Ruslan "1000% depth")

Ты — **последняя линия защиты** до D1-D5 + D7-D8 writing starts. Если
D6 имеет issues, **лучше flag сейчас** чем discover Phase 1 rollout.

---

## Inputs (load fresh)

1. **`design/JETIX-FPF.md`** v2 — primary verification target
2. **`raw/external/ailev-FPF/FPF-Spec.md`** — primary FPF source
3. **`raw/research/fpf-gap-analysis-2026-04-20.md`** — Gap Analysis (completeness reference)
4. **`raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`** — KB digest

**NE загружай:** ADR / D9 / reviews / tracking files. **Fresh lens** —
only D6 + FPF + KB + Gap Analysis.

---

## Deliverable

### File path
`raw/research/d6-reviews/stage-d-final-verification.md`

### Size target
5-10 pages structured verification report.

### Format

```markdown
---
type: d6-final-verification
reviewer: claude-opus-4-7 (fresh session, no prior Jetix context)
date: 2026-04-20
target-doc: design/JETIX-FPF.md v2
verdict: [VERIFIED READY | MINOR ISSUES | MAJOR ISSUES]
---

# D6 JETIX-FPF Final Verification Report

## Executive verdict
[Single-paragraph conclusion + overall quality score 0-100]

## 1 — FPF pattern ID verification sample (Grep-based)
[Sample 50+ citations из D6 — verify each в FPF-Spec]

## 2 — Ontological correctness audit
[5 primitives applied correctly? Alpha vs Work Product vs Entity? 
Role vs Executor? Holon typing?]

## 3 — Past-participle convention check
[Scan state machine mentions — any gerunds? qualifying/negotiating/
active/in-progress violations?]

## 4 — Completeness vs Gap Analysis
[Each 22 Recs + 5 Gaps + 9 Innovations — reflected в D6? Check list.]

## 5 — Hallucination detection
[Any mentioned concepts/patterns NOT found в FPF-Spec? Any invented
terminology? Any unrealistic line numbers?]

## 6 — Quality threshold assessment
[Does D6 meet "1000% depth" Ruslan commitment?
- Full mereology (not lightweight)?
- 17 trans-disciplines referenced?
- Advanced patterns (constructor/category) applied где relevant?
- Max Левенчук fidelity?]

## 7 — Internal consistency
[Terminology consistent across sections? No contradictions? 
Cross-references correct?]

## 8 — Critical issues found (ranked)
[P1 / P2 / P3 priorities с specific page/section references]

## 9 — Verification verdict + reasoning

### Option 1: VERIFIED READY
Если критических issues нет. D6 proceed к Stage E companion OR D1-D5
writing.

### Option 2: MINOR ISSUES
< 5 issues, each fixable in <30 min. List with fix suggestions.
Recommend Stage C quick-iteration (1h session).

### Option 3: MAJOR ISSUES
≥5 critical issues OR structural problems. Require Stage C full iteration
OR back к Stage A для significant rewrite.

## 10 — Recommended next action
[Concrete next step: proceed / minor fix / major iterate]
```

---

## Process

### Step 1 — Read all inputs (~45-60 min)

**Don't rush.** Extended thinking aggressively.

Read D6 v2 fully. Read FPF-Spec selectively via Grep (search для pattern IDs
mentioned в D6). Read Gap Analysis accepted decisions список. Read KB для
terminology reference.

### Step 2 — Verify (~30-45 min)

Execute all 7 checks (FPF patterns / ontology / past-participle / completeness /
hallucinations / quality / consistency).

### Step 3 — Write report (~20-30 min)

Follow format. Be **specific + actionable** для all issues.

### Step 4 — Verdict

Choose: VERIFIED READY / MINOR ISSUES / MAJOR ISSUES.

**Err towards MINOR если anyway unsure** — better find + fix than proceed
с hidden issues.

### Step 5 — Commit + push

```
git add raw/research/d6-reviews/stage-d-final-verification.md
git commit -m "[reviews] D6 Stage D final verification — verdict [VERDICT]"
git push origin claude/jolly-margulis-915d34
```

### Step 6 — Report

- Verdict + quality score
- Top 3 findings (если any)
- Recommended next action
- Commit SHA

---

## Critical constraints

1. **FRESH context** — load ТОЛЬКО 4 specified inputs
2. **Independent judgment** — not rubber-stamp; real verification
3. **Specific citations** — quote D6 + FPF-Spec line numbers для all findings
4. **Sample 50+ FPF pattern IDs** via Grep — statistically significant
5. **Don't bias toward "ready"** — if issues, flag accurately
6. **Extended thinking max** — slow, careful reasoning

---

## Success criteria

- [ ] D6 v2 read fully
- [ ] 50+ FPF pattern IDs verified via Grep/Read
- [ ] All 7 check sections completed
- [ ] Verdict chosen + justified
- [ ] Commit + push successful
- [ ] Report generated

**END OF STAGE D TASK PROMPT**
