---
title: Tasks Pack — Consolidated Kanban view all active work
date: 2026-05-21
type: tasks-pack-substrate
parent_prompt: prompts/expanded-docs-substrate-2026-05-21.md
parent_phase_1: decisions/strategic/EXPERTS-PACK-2026-05-21.md
parent_phase_2: decisions/strategic/QUESTIONS-PACK-2026-05-21.md
parent_plan: daily-logs/_EXPANDED-DOCS-PLAN-2026-05-21.md
prose_authored_by: brigadier-scribe (Server CC autonomous — substrate only)
F: F3
G: tasks-pack-2026-05-21
R: refuted_if_dedup_missing_OR_pool_refs_absent_OR_SKIP_list_breach_OR_LOCK_modified
constitutional_posture: R1 surface + R6 provenance + IP-1 STRICT + EP-5 + AP-6 + SKIP-list-integrity + research-pool-pattern + Manager-attention-budget-cap-20
word_count_target: ~3000-4000w
status: ACTIVE
---

# Tasks Pack — Consolidated Kanban view all active work

> **Purpose:** Все active tasks (что ещё надо сделать) в одном Kanban view с dedup. Substrate consolidated from 48 KAs (16 batch-7 + 14 batch-8 + 18 batch-9) + 11 A-actions Updated Plan 21.05 (7 FINAL v2 + 4 NEW + restructure) + 22 Tier B (O-97..O-119) + 25 DR (DR-9..DR-32) + 5 GAPS Левенчук + BL backlog. **Dedup applied; consolidated view; cross-batch references preserved.**

---

## §0 Intro — Kanban methodology / dedup approach

**Kanban columns:**
- **NOW** (this week 21-26.05) — execute this week
- **NEXT** (this month 27.05-30.06) — Month 1
- **LATER** (this quarter Q3 2026 Jul-Sep) — beyond Month 1
- **POOL** (defer / cherry-pick) — 22 Tier B + 25 DR + 5 GAPS + BL
- **DROPPED** (SKIP-list with reason) — O-62 / O-66 / O-67 / O-68

**Dedup methodology:**
- 48 KAs raw inventory → cross-batch reference + status-update vs new
- 7 A-actions FINAL v2 + 11 A-actions Updated Plan 21.05 = 18 raw → 11 unique (A-1 / A-1b / A-NEW-1..10 / A-4..A-7)
- KAs already operationalised в A-actions = deduplicated (A-1 ← KA-many; A-4 ← KA-02; A-5 ← KA-01; A-6 ← KA-07; A-NEW-7 ← DR-26)
- Pool items NOT promoted; referenced via pool docs

**Manager attention budget enforcement:** Pillar C §4.2 max 20 active tasks [src: CLAUDE.md §4.2]. **NOW column = 11 items ≤ 20 cap ✅.**

**Per-task format:**
- Task title
- Source (batch-N KA-N / A-N / pool / GAP)
- Owner (Ruslan / brigadier autonomous / both)
- Time estimate
- Priority (P1 / P2 / P3)
- Dependency
- Status (active / blocked / deferred / done)
- Acceptance criteria

---

## §1 NOW — this week (21-26.05)

### N-1 ⭐⭐ A-1 + A-1b — One-pager C.1 L2 (substrate + Ruslan prose)
- **Source:** A-1 + A-1b from FINAL v2 / Updated Plan 21.05 §2
- **Owner:** brigadier (2h substrate) + Ruslan R1 (2-4h strategic prose)
- **Time:** 4-6h total
- **Priority:** P1 ⭐⭐
- **Dependency:** Phase 5 one-pager substrate (this prompt deliverable) feeds A-1
- **Status:** active (Phase 5 of this prompt is the substrate prep)
- **Acceptance:** ≥3 Левенчук cross-cites + O-75/O-86 frames + 3-tier funnel + R12 paired + ≤600w final + 20-25% provisional language (pre-DR-26)

### N-2 ⭐⭐ A-NEW-1 — C.2 Pitch deck compile (3 audience variants)
- **Source:** A-NEW-1 Updated Plan 21.05 §2
- **Owner:** brigadier (2h substrate) + Ruslan R1 (2-4h prose)
- **Time:** 4-6h
- **Priority:** P1 ⭐⭐
- **Dependency:** A-1+A-1b done
- **Status:** active
- **Acceptance:** 12-slide structure × 3 audience emphasis (L1/L2/L3) + Master Packaging Step 6 / O-107 / O-115 / O-119 / Substrate-sandwich O-113

### N-3 A-NEW-2 — C.3 Tech brief compile (L1 engineering audience)
- **Source:** A-NEW-2 Updated Plan 21.05 §2
- **Owner:** brigadier (2h substrate, heavy) + Ruslan (1-2h prose)
- **Time:** 3-4h
- **Priority:** P1
- **Dependency:** A-1 done + Hypothesis arch overnight
- **Status:** active
- **Acceptance:** Engineering-depth content для L1 audience (Karpathy lineage / OSS maintainers / ML researchers) + Foundation v1.0 + ROY swarm + Hypothesis arch + Wiki v2 + K-6 31-component method

### N-4 A-NEW-3 — C.4 Vision narrative L3 (humanitarian)
- **Source:** A-NEW-3 Updated Plan 21.05 §2
- **Owner:** brigadier (2h substrate) + Ruslan R1 (1-2h prose)
- **Time:** 3-4h
- **Priority:** P1
- **Dependency:** A-1 + O-86 frame + HR-4 hubris paraphrase
- **Status:** active
- **Acceptance:** L3 institutional vision — O-86 / O-106 / O-107 / O-111 + R-batch-9-N3 timing-argument paraphrase applied

### N-5 A-NEW-4 — C.5 Onboarding doc (cohort intake)
- **Source:** A-NEW-4 Updated Plan 21.05 §2
- **Owner:** brigadier (1.5h substrate) + Ruslan (1h prose)
- **Time:** 2-3h
- **Priority:** P1
- **Dependency:** A-NEW-1..3 done
- **Status:** active
- **Acceptance:** Partnership-baseline / O-109 / O-116 / O-117 + Hypothesis arch hands-on + day 1-30 actions / mastery milestones / mentor pairing

### N-6 ⭐ A-NEW-5 — Promote H-batch-9-06 + H-08 via `/hypothesis-add`
- **Source:** A-NEW-5 Updated Plan 21.05 §2 + D9-6 ack queue
- **Owner:** Ruslan + brigadier
- **Time:** 30-60 min
- **Priority:** P1 ⭐
- **Dependency:** Hypothesis arch overnight ✓ ready
- **Status:** ready (D9-6 acked per REFLECTION-INBOX §APPEND-2026-05-21)
- **Acceptance:** 2 active hypotheses в `hypotheses/active/` + `/hypothesis-dash` shows promoted

### N-7 A-NEW-6 — Hypothesis arch hands-on first session
- **Source:** A-NEW-6 Updated Plan 21.05 §2
- **Owner:** Ruslan
- **Time:** 30-60 min
- **Priority:** P1
- **Dependency:** A-NEW-5 done
- **Status:** active
- **Acceptance:** 9 skills used at least once (per arch overview §5 short-term plan); Friday ritual scaffold validated

### N-8 ⭐⭐ A-NEW-7 — DR-26 unit-econ deep-dive launch
- **Source:** A-NEW-7 Updated Plan 21.05 §2; gates Q-1.1 + R-batch-9-N1
- **Owner:** Brigadier autonomous (~8-12h) после 5 min Ruslan ack
- **Time:** 5 min Ruslan ack + 8-12h server CC autonomous
- **Priority:** P1 ⭐⭐
- **Dependency:** None (parallel autonomous)
- **Status:** awaiting ack
- **Acceptance:** `research/unit-econ-deep-dive-2026-05-21/` с memo + scenarios + Mondragón / QF / cooperative DAOs comparable baselines + recommendation

### N-9 A-NEW-8 — Tier-1 ack queue review 14 names (KA-03 CRM)
- **Source:** A-NEW-8 Updated Plan 21.05 §2; D9-* batch
- **Owner:** Ruslan
- **Time:** 30 min × 14 = 7h batched (e.g. weekend dedicated session)
- **Priority:** P1
- **Dependency:** A-1 done (canonical descriptors)
- **Status:** ready
- **Acceptance:** All 14 contacts statuses updated + 6 batch-9 outreach opener-hooks applied where relevant

### N-10 A-4 — KA-02 Дмитрий pitch drafting + send Week 1
- **Source:** A-4 FINAL v2 + Updated Plan 21.05 §2 unchanged
- **Owner:** Ruslan
- **Time:** 2-3h drafting + send
- **Priority:** P1
- **Dependency:** A-1 done (canonical descriptors)
- **Status:** active (end-of-week 1)
- **Acceptance:** Pitch sent; CRM status updated `contacted`; tracking response

### N-11 A-NEW-9 — §APPEND 6 wikis mechanical execution
- **Source:** A-NEW-9 Updated Plan 21.05 §3.5; D9-* set
- **Owner:** brigadier (mechanical execution post-ack)
- **Time:** 1-2h mechanical
- **Priority:** P2 (low blocker; deferable but easy win)
- **Dependency:** Ruslan §APPEND set ack
- **Status:** ready
- **Acceptance:** 6 wiki concepts §APPEND'd (partnership-baseline / project-of-humanity-positioning / method-systems-thinking / jetix-as-exokortex / mastery-formula / sense-of-measure)

### Optional N-12 (overflow) A-NEW-10 — C.6 use cases substrate dictation
- **Source:** A-NEW-10 Updated Plan 21.05 §2
- **Owner:** Ruslan dictation (1-2h) + brigadier compile (2h)
- **Time:** 3-4h
- **Priority:** P2 (partial; substrate sparse)
- **Dependency:** A-NEW-8 may surface case-study candidates
- **Status:** overflow / partial
- **Acceptance:** Distribution Plan §1 C.6 use-case-tier scaffolded; concrete cases TBD post-traction

**NOW summary:** 11 items P1 + 1 P2 + 1 overflow = 13 total ≤ 20 cap ✓. Critical path: N-1+N-2 → N-3+N-4+N-5 → N-10 send.

---

## §2 NEXT — this month (27.05-30.06)

### M-1 A-5 — KA-01 Левенчук pitch drafting + send Week 2 (27.05-2.06)
- **Source:** A-5 FINAL v2 + Updated Plan substrate-sandwich integration
- **Owner:** Ruslan
- **Time:** 4-6h drafting + send
- **Priority:** P1 (Week 2 start)
- **Dependency:** A-4 outcome informs (Дмитрий response shapes Левенчук framing)
- **Status:** queued
- **Acceptance:** Pitch sent с 5 hooks Левенчук distillation §4 + cross-link matrix + DE-RU glossary 40 entries + substrate-sandwich O-113

### M-2 Phase 2 cascade activation (Tier-1 cluster outreach)
- **Source:** Distribution Plan §1.2 Week 4
- **Owner:** Ruslan (heavy) + brigadier substrate
- **Time:** ongoing Month 1 Week 3-4
- **Priority:** P1-P2
- **Dependency:** C.1 + C.2 ready + A-4/A-5 feedback
- **Status:** queued
- **Acceptance:** Karpathy / Buterin / Anthropic cluster initial touches sent

### M-3 C.2-C.5 iteration based on A-4 / A-5 feedback
- **Source:** Distribution Plan §1.2
- **Owner:** Ruslan R1 + brigadier substrate
- **Time:** ongoing
- **Priority:** P1
- **Dependency:** A-4 / A-5 responses arrive
- **Status:** queued
- **Acceptance:** Docs updated based on real conversation feedback

### M-4 First hypothesis closures + compound learning
- **Source:** Hypothesis arch §5 short-term plan
- **Owner:** Ruslan (Friday ritual A-7)
- **Time:** 30 min × 4 weeks = 2h
- **Priority:** P1
- **Dependency:** A-NEW-5 + A-NEW-6 first hypothesis active
- **Status:** queued
- **Acceptance:** ≥1 hypothesis closed (refuted / supported / pivoted) + compound learning written to `agents/<expert>/strategies.md`

### M-5 First cohort intake mechanism design
- **Source:** Q-2.1..Q-2.6 batch
- **Owner:** Ruslan R1
- **Time:** 4-8h strategic
- **Priority:** P1
- **Dependency:** DR-26 result + A-4/A-5 feedback + Tier-1 ack queue review
- **Status:** queued
- **Acceptance:** Quantity / criteria / onboarding / equity / closed-vs-open all locked

### M-6 DR-28 humanity-self-awareness threshold philosophy
- **Source:** §3.2 batch-9 DR P2
- **Owner:** brigadier autonomous (~6-8h)
- **Time:** 5 min Ruslan ack + autonomous
- **Priority:** P2 (enhances C.4 narrative)
- **Dependency:** A-NEW-3 C.4 baseline drafted
- **Status:** queued
- **Acceptance:** `research/humanity-self-awareness-threshold-2026-XX-XX/` substrate

### M-7 Monetization test (first revenue attempt)
- **Source:** Distribution Plan §0.2 short-term $100K summer 2026
- **Owner:** Ruslan R1 + brigadier substrate
- **Time:** ongoing
- **Priority:** P1
- **Dependency:** Founding cohort 1-3 contracts
- **Status:** queued
- **Acceptance:** $1+ revenue actual (first paid contract)

### M-8 Operational discipline iteration (cadence / budget / burnout)
- **Source:** Q-6.1..Q-6.7 batch
- **Owner:** Ruslan + system-admin (deprecated, on-demand)
- **Time:** ongoing
- **Priority:** P1
- **Dependency:** Empirical Week 1-4 measurement
- **Status:** queued
- **Acceptance:** Manager attention budget enforced (cap 20); cadence 55-85 touches/week sustained; burnout signals tracked

**NEXT summary:** 8 items; mix of execution + iteration + strategic decisions.

---

## §3 LATER — this quarter Q3 2026 (Jul-Sep)

### Q-1 6 ⭐⭐⭐ Левенчук chapters deep FPF phase
- **Source:** Q-7.6 + Q-8.3; Левенчук distillation §3 findings
- **Owner:** brigadier autonomous (50-100h budget) + Ruslan R1 oversight
- **Time:** 50-100h deep research
- **Priority:** P3 (Q3 2026 candidate)
- **Dependency:** Левенчук response + first cohort traction
- **Status:** deferred
- **Acceptance:** OMG Essence + 5 регионов + 16 транс-дисциплин + LXP + Метод 1-го класса + графы создания full integration

### Q-2 $100K revenue milestone trajectory
- **Source:** Distribution Plan §0.2 short-term + audio_681
- **Owner:** Ruslan + brigadier substrate
- **Time:** ongoing
- **Priority:** P1 (Q3 2026 milestone)
- **Dependency:** Founding cohort + monetization mechanic locked
- **Status:** deferred (Q3 2026 target)
- **Acceptance:** $100K cumulative revenue achieved (might extend to Q4 if needed)

### Q-3 First 1000 users
- **Source:** Distribution Plan §0.2 mid-term
- **Owner:** Ruslan + cohort
- **Time:** ongoing
- **Priority:** P1 (Q3 2026 milestone)
- **Dependency:** Cohort intake mechanism + cascade activation
- **Status:** deferred
- **Acceptance:** 1000 active users counted (definition: monthly active engagement)

### Q-4 Foundation Strategic Layer Phase 2 onset
- **Source:** CLAUDE.md `### Strategic Layer Foundation extension` Bundle 5
- **Owner:** Ruslan R1 + brigadier
- **Time:** ongoing
- **Priority:** P2
- **Dependency:** Phase 1 cohort traction + decisions DB maturity
- **Status:** deferred (Q3-Q4 2026)
- **Acceptance:** Phase 2 strategic-doc types operational (Direction Card / Phase Plan / Strategic Reflection)

### Q-5 R12 programmable Ethereum substrate concrete deploy
- **Source:** Q-1.7 + Q-5.3; CLAUDE.md §4.2 Phase 2+ Ethereum acked
- **Owner:** Ruslan R1 + external technical
- **Time:** TBD
- **Priority:** P3 (Phase 2+ deferred)
- **Dependency:** Cohort traction + legal entity formed
- **Status:** deferred
- **Acceptance:** First on-chain fork-and-leave token operational

---

## §4 POOL — defer / cherry-pick

### §4.1 Tier B candidates pool (22 → 37 with batch-9 extensions)

**Reference:** `reports/voice-pipeline-2026-05-20-batch-7/_TIER-B-CANDIDATES-POOL-2026-05-20.md` (22 baseline) + Updated Plan 21.05 §3.1 (15 batch-9 extensions O-105..O-119).

**Cherry-pick principle (research-pool pattern):** NOT auto-promoted. Surface per Ruslan ack only.

Key batch-9 high-signal entries:
- **O-106** ⭐ Desire-to-live = primary info-valve — Tier A standalone candidate
- **O-107** Canonical one-liner «метод по объединению методов» — ready ack (D9-11)
- **O-108** ⭐⭐ 20-25% take rate — DR-26 gates (Q-1.1 + R-batch-9-N1)
- **O-114** ⭐⭐⭐ «Метод обработки информации» descriptor + 8-doc inventory — PRE-ACKED voice
- **O-115** Public self-label «методологист философ изобретатель» — bio material
- **O-119** Self-validation by outcome — origin-story substrate

Remaining 31 Tier B items cherry-pick на per-cycle basis.

### §4.2 Research pool (17 → 25 with batch-9 extensions DR-25..DR-32)

**Reference:** `reports/voice-pipeline-2026-05-20-batch-7/_RESEARCH-CANDIDATES-POOL-2026-05-20.md` (17 baseline) + Updated Plan 21.05 §3.2 (8 batch-9 extensions).

**Cherry-pick principle:** NOT auto-launched.

Key DR candidates:
- **DR-26** ⭐⭐ Unit-economics deep-dive — **P1 URGENT** ([N-8 above])
- **DR-28** Humanity-self-awareness threshold philosophy — **P2** ([M-6 above])
- **DR-31** Governance R12 boundary audit — **P3** (deferred long-term)
- **DR-32** Origin-story / bootstrap-credibility pitch A/B — P3

Remaining 21 DR cherry-pick.

### §4.3 5 GAPS Левенчук distillation

**Reference:** `research/levenchuk-books-distillation-2026-05-20/00-SUMMARY-FOR-RUSLAN.md` §4.

1. **OMG Essence 2.0 alpha-machinery** — GAP-1 CLOSED overnight 20.05 evening (Hypothesis arch Layer 6)
2. **Праксиология (Mises)** — instrumental Рациональность layer; defer to investor-expert × integrator review
3. **5 регионов стратегирования** — Pillar A extension proposal; defer to Strategic Layer Phase 2 (Q-4 above)
4. **Системные ритмы / 4D системность** — Foundation Part 5 extension candidate
5. **16 транс-дисциплин стека** — K-4 12-Component Audit expansion candidate

**Status:** Deep FPF phase Q3 2026 candidate (Q-1 above).

### §4.4 BL backlog (retained)

- **BL-1** Engineer Workshop Berlin component (retained)
- **BL-N** additional backlog items per FINAL v2 §10+

---

## §5 DROPPED — SKIP-list (with reason)

> **SKIP-list integrity preserved per FINAL v2 §5.** NOT surfaced in NOW / NEXT / LATER / POOL.

| Item | Reason for skip | Source ack |
|---|---|---|
| **O-62** Fund-of-Humanity | Ruslan ack permanent skip — concept misaligned with R12 paired-frame voluntary | FINAL v2 §5 ack |
| **O-66** | Deferred pending additional gates | FINAL v2 §5 |
| **O-67** | Deferred pending additional gates | FINAL v2 §5 |
| **O-68** | Deferred pending additional gates | FINAL v2 §5 |

**Integrity check:** None of O-62 / O-66 / O-67 / O-68 surfaced в Tasks Pack §1-§4 ✓.

---

## §6 Dedup logic + audit

### §6.1 Source-to-Kanban map (48 KAs / 11 A-actions → N-1..N-12 + M-1..M-8 + Q-1..Q-5 + POOL refs)

**16 KAs batch-7:** Mostly subsumed into A-1 (one-pager substrate via 6 promotion docs C.1-C.6) or A-4/A-5 (pitch substrates). Specific KA-01 Левенчук → A-5 (M-1); KA-02 Дмитрий → A-4 (N-10); KA-03 CRM → done overnight 20.05; KA-07 R12 → A-6 → weekend KA-07 scheduled (not separately listed; ongoing).

**14 KAs batch-8:** Subsumed into A-NEW-1..4 detailed documents (pitch deck / tech brief / vision narrative / onboarding) + §APPEND wiki recommendations (A-NEW-9).

**18 KAs batch-9:** Subsumed into A-NEW-5..10 + Tier B pool (15 entries §4.1) + DR pool (8 entries §4.2) + 6 outreach opener-hooks (subsumed into A-NEW-8 Tier-1 ack queue review).

**Dedup ratio:** 48 KAs raw → 11 unique A-actions + pool refs = ~77% dedup via A-action subsumption + pool referencing.

### §6.2 11 A-actions Updated Plan 21.05 → Kanban map

| A-action | Kanban slot |
|---|---|
| A-1 / A-1b | N-1 ⭐⭐ |
| A-NEW-1 | N-2 ⭐⭐ |
| A-NEW-2 | N-3 |
| A-NEW-3 | N-4 |
| A-NEW-4 | N-5 |
| A-NEW-5 | N-6 ⭐ |
| A-NEW-6 | N-7 |
| A-NEW-7 | N-8 ⭐⭐ |
| A-NEW-8 | N-9 |
| A-4 | N-10 |
| A-NEW-9 | N-11 |
| A-NEW-10 | N-12 overflow |
| A-5 | M-1 |
| A-6 | weekend continuous (not listed; ongoing P1) |
| A-7 | M-4 weekly Friday ritual (and N-7 first execution) |

✓ 11 + 4 = 15 A-actions mapped (some merge / some continuous).

### §6.3 Pool reference integrity

✓ Tier B pool 22 → 37 referenced §4.1 (NOT promoted; ack-only)
✓ DR pool 17 → 25 referenced §4.2 (NOT auto-launched; ack-only; DR-26 + DR-28 surfaced in NOW/NEXT)
✓ 5 GAPS Левенчук referenced §4.3 (GAP-1 closed; 4 remain)
✓ BL backlog referenced §4.4

### §6.4 Tier B → active hypothesis migration map

Per Updated Plan §3.3:
- **Promotable immediately (2):** H-batch-9-06 + H-08 → N-6 (A-NEW-5)
- **Pool-tagged in Tier B (7):** H-batch-9-01/02/03/07/09 + samples promotion review → pool §4.1
- **Deferred frame-level / DR scope (2):** H-batch-9-04 (frame-level) + H-batch-9-05 (DR-29 scope) → pool §4.2 (DR-29)

---

## §7 Per-task format consistency check

All N-1..N-12, M-1..M-8, Q-1..Q-5 items carry: title + source + owner + time + priority + dependency + status + acceptance — ✓ checked.

---

## §8 Acceptance + closure

- ✅ Kanban NOW / NEXT / LATER / POOL / DROPPED structure
- ✅ 48 KAs + 11 A-actions consolidated dedup'd (~77% dedup ratio via A-action subsumption)
- ✅ Pool references (Tier B 22→37; DR 17→25; 5 GAPS; BL) preserved
- ✅ SKIP-list integrity (O-62/O-66/O-67/O-68 NOT surfaced)
- ✅ Manager attention budget cap 20 enforced (NOW = 13 items ≤ 20 cap)
- ✅ Constitutional posture preserved (R1 + R6 + IP-1 STRICT + EP-5 + AP-6 + research-pool-pattern)
- ✅ Cross-cite to Experts Pack + Questions Pack + Updated Plan + Distribution Plan
- ✅ DR-26 surfaced N-8 (P1 ⭐⭐) gates 20-25% take rate public lock

**Next actions:**
- Ruslan reads + re-prioritize if needed (R1 strategic)
- Critical path NOW (N-1 → N-2 → N-10) executed Week 1
- Cap enforcement: if new task surfaces, drop NEXT or POOL not NOW (respect 20-cap)

---

*Tasks Pack closure 2026-05-21. Phase 3 deliverable. ~3000w. Per memory feedback_research_pool_pattern.md + feedback_constitutional.md. Next: Phase 4 Development Plan.*
