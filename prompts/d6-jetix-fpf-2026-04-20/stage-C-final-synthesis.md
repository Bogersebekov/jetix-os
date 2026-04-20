---
type: task-prompt
stage: C (final synthesis)
target: claude-code main session (Opus 4.7, 1M context)
mode: extended-thinking-max
deliverable: design/JETIX-FPF.md v2 (final polished)
estimated-time: 1-3 hours
status: ready-to-execute (run AFTER Stage B — all 4 reviews complete)
---

# Stage C — Final Synthesis: D6 v2

## Context

Ты — main Claude Code session. Stage A написал D6 v1. Stage B provided
**4 independent perspective critiques** from fresh sessions:

1. Reviewer 1 — Левенчук Purist (ontology fidelity)
2. Reviewer 2 — DACH Compliance (regulatory)
3. Reviewer 3 — AI-Agent Designer (operational для агентов)
4. Reviewer 4 — Enterprise Reader (clarity + trust)

**Твоя задача:** synthesize D6 v1 + 4 reviews → **D6 v2 final polished.**

Не naive merge. Intelligent integration:
- P1 critical findings from any reviewer → **apply**
- Conflicting critiques between reviewers → **resolve через ranking** (ontology > compliance > AI-agent > reader clarity для этого document)
- Strengths preserved (all reviewers agreed NOT to break)
- Recommended changes integrated coherent

---

## Inputs

1. **`design/JETIX-FPF.md`** v1 (base — modify в place → v2)
2. **`raw/research/d6-reviews/reviewer-1-levenchuk-purist.md`** — ontology critique
3. **`raw/research/d6-reviews/reviewer-2-dach-compliance.md`** — compliance critique
4. **`raw/research/d6-reviews/reviewer-3-ai-agent-designer.md`** — AI-agent critique
5. **`raw/research/d6-reviews/reviewer-4-enterprise-reader.md`** — readability critique
6. **`raw/external/ailev-FPF/FPF-Spec.md`** — selective reference для fixes (via Grep/Read ranges)
7. **`decisions/gap-analysis-review-decisions-2026-04-20.md`** — ground-truth accepted decisions
8. **`decisions/2026-04-19-architecture-v2-approval.md`** — ADR reference

---

## Deliverable

### File path
`design/JETIX-FPF.md` (update in place, v1 → v2)

### Frontmatter update

```yaml
version: v2.0
previous-version: v1.0
synthesized-from:
  - v1 (Stage A commit SHA [fill in])
  - Reviewer 1 Левенчук Purist critique
  - Reviewer 2 DACH Compliance critique
  - Reviewer 3 AI-Agent Designer critique
  - Reviewer 4 Enterprise Reader critique
state: draft-synthesized (awaiting Stage D verification)
```

### Size target
Similar к v1 (~30-50 pages) — может slight increase если review findings add sections.

---

## Process

### Step 1 — Read all inputs (~30-45 min)

Load D6 v1 + all 4 reviews + selective FPF-Spec + Gap Analysis context.

Extended thinking aggressively.

### Step 2 — Synthesis analysis (~20-30 min)

Build mental map:

- **P1 findings across reviewers** (critical — must fix):
  - List all P1 issues from each reviewer
  - Deduplicate (same issue flagged by multiple)
  - Rank by impact

- **P2 findings** (valuable — should fix):
  - Similar process

- **P3 findings** (nice — if time):
  - Similar

- **Conflicts between reviewers:**
  - Реже, но possible (e.g., Reviewer 1 wants more ontology depth, Reviewer 4 wants more accessibility)
  - **Resolution rule:** this document's primary purpose is **constitutional ontology** (per Ruslan directive "max Левенчук depth"). **Ontology fidelity > clarity > compliance > AI-agent** в resolution ranking. Reviewer 1 wins при direct conflict.
  - НО: can often satisfy both (add clear example next to deep concept)

- **Strengths all agreed** (preserve — don't break):
  - Extract list
  - Guard them during edits

### Step 3 — Apply changes (~60-90 min)

**Priority order:**

1. **P1 critical from Reviewer 1 (Левенчук Purist)** — ontology corrections first
2. **P1 from Reviewer 2 (DACH Compliance)** — regulatory gaps
3. **P1 from Reviewer 3 (AI-Agent)** — operational clarity для agents
4. **P1 from Reviewer 4 (Enterprise Reader)** — readability blocks
5. **P2 findings** from all — batch apply where coherent
6. **P3 findings** — apply если не disrupting

**Methods:**
- Use Edit tool для in-place changes
- Preserve good v1 passages (reviewers agreed)
- Expand sections где reviewers flagged gaps
- Add examples где Reviewer 4 flagged abstractness
- Add compliance citations где Reviewer 2 flagged
- Add agent-operational specs где Reviewer 3 flagged
- Tighten ontology где Reviewer 1 flagged

### Step 4 — Consistency check (~15-30 min)

After all changes:
- Re-read full D6 v2 для coherence
- Verify no contradictions introduced
- Past-participle discipline maintained
- Russian primary + English citations consistent
- Section flow natural

### Step 5 — Commit + push

```
git add design/JETIX-FPF.md
git commit -m "[design] D6 JETIX-FPF v2 synthesized — Stage C complete

Integrated 4 independent perspective reviews:
- Reviewer 1 Левенчук Purist (ontology)
- Reviewer 2 DACH Compliance (regulatory)
- Reviewer 3 AI-Agent Designer (operational)
- Reviewer 4 Enterprise Reader (readability)

Applied:
- [N] P1 critical findings fixed
- [M] P2 valuable findings integrated
- [K] strengths preserved from v1

D6 v2 ready для Stage D independent final verification.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

git push origin claude/jolly-margulis-915d34
```

### Step 6 — Report

Brief summary:
- v1 → v2 delta (sections modified, added, expanded)
- P1 findings addressed (count + brief list)
- P2 findings addressed (count)
- Strengths preserved (confirmation)
- Outstanding issues deferred (if any — flag для Stage D)
- Commit SHA

---

## Critical constraints

1. **Ontology fidelity primary** — при conflicts, Reviewer 1 wins
2. **Preserve v1 strengths** — don't accidentally break what reviewers praised
3. **Single document edit** — D6 v2 = enhanced v1, не rewrite
4. **Extended thinking** для every significant edit decision
5. **FPF pattern verification** via Grep if adding new citations
6. **No new decisions** — only apply review findings within existing approved scope

---

## Success criteria

- [ ] All 4 review reports read fully
- [ ] D6 v1 analyzed для baseline
- [ ] P1 findings from each reviewer addressed
- [ ] P2 batch applied
- [ ] Strengths preserved
- [ ] Consistency verified
- [ ] Commit + push successful
- [ ] Report generated

**END OF STAGE C TASK PROMPT**
