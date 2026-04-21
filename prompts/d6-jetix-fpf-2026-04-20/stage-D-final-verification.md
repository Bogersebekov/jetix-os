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

## Specific Verification Targets для актуального D6 v2

D6 v2 готов (commit `639e3db`, 3758 строк, +1499 vs v1). Frontmatter заявляет:
- `structural-decision: Option C hybrid` (deep ontology + Jetix-application preserved;
  academic lineage Sections 10.1-10.5, 11.3-11.5, 11.7 compressed с companion pointers)
- `synthesized-from: 4 reviewer critiques` (commits a4cfac2, 8dd5420, 0e15f52, 582450b)
- `language-policy: RU-primary D6 + bilingual Левенчук quotes + DE-primary client artifacts`
- Stage C synthesizer commit message заявляет **все 12 P1 findings addressed** explicitly

**Твоя fresh-context задача — НЕ rubber-stamp эти claims, а independently verify.**

### 🎯 12 P1 Verification Checklist

Synthesizer заявил каждый из этих 12 P1 fixed/deferred. Проверь reality:

**От Reviewer 1 (Левенчук Purist):**

- **P1-R1-1 Line-numbers verification:** Section 14.2 — был claim "no `~approx` left,
  все exact". Grep `~` в Section 14.2 — сколько осталось? Sample 5-7 patterns: для
  каждого Grep FPF-Spec.md line + verify что pattern по claimed line number actually
  matches description в D6. Если 2+ wrong → P1 unresolved.
- **P1-R1-2 U-Types duplicates:** Section 8.1 — U.Holon (#3 vs #32) и U.Case (#15
  vs #33) split per Stratum discipline или suffixed? Verify table structure.
- **P1-R1-3 Past-participle violations:** Section 6.2 — synthesizer добавил Section
  5.5a exception (5 whitelisted in-X states). Verify (a) exception rationale документирован
  per Левенчук discipline; (b) Hook 4 spec updated; (c) НЕ создан loophole для всех
  будущих gerunds.

**От Reviewer 2 (DACH Compliance):**

- **P1-R2-1 BDSG §38 vs Art.28 DPA:** Section 2.3 matrix split — Art.28 (Phase 1
  readiness) vs §38 BDSG (Phase 2a/2b headcount 20+). Verify legal accuracy.
- **P1-R2-2 EU AI Act risk-tier matrix:** Section 4.5.1 — таблица 7 offerings × tier
  (Annex III/Limited/Minimal) × obligations × Aug 2026 deadline. Verify Annex III
  classifications correct per actual EU AI Act text. Sample 2-3 rows против official
  source.
- **P1-R2-3 CP-5 Art.22 expansion:** Section 4.5.1-4.5.10 — все 9 elements present
  (SLA window, audit trail format, escalation, off-hours fallback, contestation
  mechanism per Art.22(3), what counts as "client-affecting", logging, visibility,
  exceptions)? Word count ~1500?

**От Reviewer 3 (AI-Agent Designer):**

- **P1-R3-1 Per-agent loading tier:** Section 5.4a — 3-tier table (Tier 1 full /
  Tier 2 distilled ~2K / Tier 3 reference-only). Verify (a) tier assignment per
  agent rationale defensible; (b) cost projection ~60% reduction realistic given
  actual D6 v2 size (3758 строк).
- **P1-R3-2 J-level matrix:** Section 2.2 — delegated к D3+D7 с bridge sentence?
  Verify proper delegation (не abandonment).
- **P1-R3-3 Role-switching enforcement:** Section 5.9a — 3-layer (message-schema
  `acting_as:` field + manager monitoring + FPF-Steward audit). Verify (a) message-
  schema actually has this field; (b) enforcement points concrete не vague.
- **P1-R3-4 Agency-CHR schema:** Section 2.1a — "Option D hybrid" (`decisions/policy/
  agent-promotion-chr.yaml` defaults + `executors/<id>/executor-binding.yaml`
  overrides). Verify schema example concrete (не just bullet points).
- **P1-R3-5 Agent_onboarding YAML example:** Section 5.8.1 — full ~120-line
  `executor-binding.yaml` example для sales-lead с M1-M6 F.6 cycle. Verify
  completeness + alignment с FPF F.6 (L.50641).

**От Reviewer 4 (Enterprise Reader):**

- **P1-R4-1 Reader on-ramp:** §0-§0.9 (90 seconds + reader routes + glossary + TOC).
  Verify (a) §0 actually plain language (не FPF citations); (b) reader routes
  correctly target audiences (Geschäftsführer / investor / DACH hire / agent dev);
  (c) glossary covers top jargon.
- **P1-R4-2 RU/EN bilingual:** Левенчук quotes в Sections 5/9/11 — bilingual format
  (RU original + EN translation) или fallback? Sample 5-7 quotes.
- **P1-R4-3 Examples concentration:** 5-7 concrete examples added (Müller GmbH в
  §3.6/§4.3/§4.5; weekly close §7.1; sales-lead onboarding §5.8.1; executor-binding
  §2.1a). Verify each example actually concrete (named entity / actual values), не
  abstract.
- **P1-R4-4 TOC:** §0.9 — linked TOC (14 entries). Verify link anchors correct.
- **P1-R4-5 Cargo Sections 10+11:** Section 10.1-10.5 + Section 11.3-11.5+11.7 —
  compressed (per Option C) или full text remains? Verify compression actually
  done (sections shorter), не just renamed.

### 🔄 Cross-reviewer themes verification

Synthesizer заявил все 5 themes addressed. Verify:

- **T1 RU/EN tension** — language-policy frontmatter + bilingual quotes
- **T2 Operationalization gap** — Section 2.1a + 4.5 + 5.8.1 + 5.9a actually
  implementations (не principles+TBD)
- **T3 Reference-chain integrity** — claim "Section 14.2a Reference status audit
  table 44 rows" — verify exists с ETA dates
- **T4 Past-participle holistic** — exception consistent everywhere
- **T5 Cost realism** — Section 5.4a tier loading

### 🛡️ Regression check (CRITICAL)

v1 strengths должны быть preserved. Verify presence + intactness:

- **Mereology Section 10 Jetix-application** (10.6-10.11) — preserved ~40 lines?
- **A.14 typed edges** Section 3.5 + creation-graph
- **Compose-CAL** Section 10.10
- **8 true alphas** Section 6 — full state machines per alpha
- **FPF citations density** Section 14.2 — 60+ patterns
- **Müller GmbH walkthrough** Section 3.6 — preserved + expanded в §4.3/§4.5

Если **любой** strength сломан — flag as P1 regression в verification report.

### 🚨 New issues scan

После v2 expansion — possibly introduced:

- **Companion file dead links:** D6 v2 references множество `wiki/foundations/`
  файлов которые ещё не существуют. Verify (a) каждый reference имеет explicit
  ETA дату; (b) ETA дата realistic (не "soon" / "TBD"); (c) absence не блокирует
  immediate D6 use.
- **Internal contradictions:** v2 +1499 строк — возможные contradictions между
  старыми и новыми секциями. Sample check: новые 9 elements CP-5 align с старой
  CP-1 Section 4.1?
- **Frontmatter consistency:** version v2.0, all 4 reviewer credits, structural-
  decision rationale.

### 📊 Quality threshold per Ruslan "1000% depth"

D6 v2 = constitutional document. Verify:

- Full mereology applied (не lightweight)
- 16 trans-disciplines referenced (Section 11)
- Advanced patterns (Compose-CAL, Constructor theory) applied where relevant
- Max Левенчук fidelity preserved через Option C compression
- Defensible enterprise/investor/auditor review

**Score 0-100:** verify against this threshold с specific evidence.

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
