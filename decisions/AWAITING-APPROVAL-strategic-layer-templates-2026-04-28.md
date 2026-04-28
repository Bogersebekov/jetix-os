---
title: "AWAITING-APPROVAL — Strategic Layer Templates (Etap 2 of Генеральная чистка)"
date: 2026-04-28
type: awaiting-approval-packet
status: AWAITING-APPROVAL
priority: high — gates Strategic Layer content authoring (next sprint with 5-chat methodology)
estimated_walltime_used: ~2.5h server CC work (within brief's 2-4h target)
F: F2
G: "AWAITING-APPROVAL packet for Ruslan walkthrough; gates Strategic Layer content authoring next sprint"
R: R-medium
locked_decisions_referenced: [D-29, D-22, D-21, D-20, D-13, D-11, D-27, D-28, D-25]
related_locks: see §3 PROPOSE rationale references
related_strategic_docs:
  - decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md (Layer 1, LOCKED)
  - design/JETIX-FPF.md (Constitutional Spec, ongoing)
  - decisions/JETIX-PLAN.md (Phase Plan, current Phase 1)
  - 5 STRATEGIC-INSIGHT-* exemplars (corpus signal for Type 06)
  - decisions/VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md (proto-North-Star)
research_outputs:
  phase_1: decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md
  phase_2: decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md
  phase_3: decisions/strategic/_research/hierarchy-cadences-2026-04-28.md
  phase_4: decisions/strategic/_templates/ (7 templates) + decisions/strategic/_index.md
git_branch: claude/jolly-margulis-915d34
git_commits_in_this_cycle:
  - 87f7346 "[strategic] Phase 1 landscape research catalogue"
  - bc92820 "[strategic] Phase 2 jetix-fit filtering — 7 PROPOSE + 8 SKIP/DEFER"
  - ef55406 "[strategic] Phase 3 hierarchy + cadences + owner matrix"
  - 535f719 "[strategic] Phase 4 structural templates — 7 PROPOSE templates + manifest"
honest_limits:
  - >
    Memory files declared in brief at Windows-client paths (`C:\Users\49152\.claude\projects\C--Users-49152-Desktop-jetix-os\memory\`)
    are NOT on the Linux server. Substituted via inference from STRATEGIC-INSIGHT-* + FUNDAMENTAL +
    candidate-parts-merged content. Substitution is defensible (constraints encoded
    in those memories all surface in on-disk corpus) but Ruslan should verify in walkthrough.
  - >
    LJ post corpus (49 posts) sampled via 3 research compilations per Wave B levenchuk
    card §1 declaration; no direct LJ file-by-file reads at this scope.
  - >
    Edge-typing in §1 dependency graph uses informal labels (overlays / pulls /
    contains-shaped-bets / candidate-promotion / synthesizes-from) rather than strict
    FPF A.14 canonical edges (ComponentOf, ConstituentOf, etc.). FPF-canonical is too
    narrow for these strategic-doc relations; tighten in walkthrough if Ruslan requires.
  - >
    Honest-count: 7 PROPOSE + 8 SKIP/DEFER = 15 (matches Phase 1 catalogue). The +1 over
    brief's "5-7 SKIP/DEFER" target is defensible: 4 SKIP verdicts are driven by
    existing-coverage facts (Foundation Layer / canonical doc); compressing below 8
    misrepresents the corpus.
---

# AWAITING-APPROVAL — Strategic Layer Templates

## §1 Executive summary

**What was done.** 5-phase research + scoping cycle for the Strategic Layer (Etap 2
of Генеральная чистка), executed as **direct Cloud Code session in integrator mode**
(no ROY brigadier matrix dispatch — overkill for landscape research per brief §0).

**What was produced:**

| Phase | Output | Path | Words |
|---|---|---|---|
| 1 | Landscape catalogue (15 strategic doc types) | `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md` | ~4.5K |
| 2 | Jetix-fit filtering (7 PROPOSE + 8 SKIP/DEFER) | `decisions/strategic/_research/jetix-fit-filtering-2026-04-28.md` | ~2.3K |
| 3 | Hierarchy + cadences + owner matrix | `decisions/strategic/_research/hierarchy-cadences-2026-04-28.md` | ~2.5K |
| 4 | 7 structural templates + manifest | `decisions/strategic/_templates/*.md.template` (7 files) + `decisions/strategic/_index.md` | ~6.2K total |
| 5 | This packet | `decisions/AWAITING-APPROVAL-strategic-layer-templates-2026-04-28.md` | ~2.6K (target 2-3K) |

**Total walltime:** ~2.5h server work (within brief's 2-4h budget).

**Bottom line.** 7 PROPOSE types passed all 8 Jetix-fit criteria + corpus-evidence
+ framework-anchor checks — they are the candidate Strategic Layer types ready for
content authoring next sprint. 8 SKIP/DEFER types either already have canonical
artifacts (4 SKIP) or are premature for solo-founder Phase 1 €50K context (4 DEFER
with reactivation predicates declared).

**Key principle preserved across all 5 phases:**
> RESEARCH > CREATION. PROPOSE > DECIDE (Ruslan-only strategy). STRUCTURE > CONTENT.
> HONEST-FILTERING > LITERATURE-COMPLETENESS. RUSLAN-ACK > BRIGADIER-CONFIDENCE.
> *(Brief §7 mantra)*

---

## §2 Landscape catalogue summary (15 strategic doc types found)

Per Phase 1 — extracted from corpus (FUNDAMENTAL Vision + 14 consultant cards + books-md
+ 5 STRATEGIC-INSIGHT exemplars + Wave A/B Foundation artifacts).

| # | Type | Origin framework | Corpus exemplar |
|---|---|---|---|
| 01 | Foundation Vision (constitutional) | Levenchuk FPF + Anthropic CAI + Buffett genre | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` (LOCKED v1.0) |
| 02 | Constitutional Spec (FPF-class) | Levenchuk FPF | `design/JETIX-FPF.md` (3758 lines) |
| 03 | Locks Ledger Entry | FPF B.3 + CAI + Capital margin-of-safety | `decisions/LOCKS-D25-D28-ADDENDUM-*` + D1-D29 inline |
| 04 | Founder Overlay (RUSLAN-LAYER) | FUNDAMENTAL §0 two-layer pattern | (planned — Layer 2 referenced in cross-refs) |
| 05 | North Star / DoT | Cagan Ch.26 + Doerr O + Naval | (deferred — `VISION-NEXT-STRATEGIC-HORIZON-2026-04-24.md` proto) |
| 06 | Strategic Insight Memo | IP-7 + Marks memo + CAI engineering-blog | 5 corpus exemplars `STRATEGIC-INSIGHT-*` |
| 07 | Direction / Pillar Card | Cagan empowered + Buffett circle + Marks portfolio | M&A + Arbitrage Traffic exemplars |
| 08 | Phase Plan | Watkins + Grove + Ries strategic-zoom | `decisions/JETIX-PLAN.md` |
| 09 | Quarterly Plan / OKRs | Doerr Measure What Matters | (gap — PM card §6 OQ-5) |
| 10 | Bet Pitch / Shape-Up Pitch | Singer Shape Up + Munger inversion | (templates adjacent — `swarm/wiki/_templates/project-*/`) |
| 11 | Project Brief | Cagan + Torres + PMBOK 12 principles | `swarm/wiki/_templates/project-*/` (4 trees) |
| 12 | DRR / Compound Cycle | Compounding Engineering Klaassen | `agents/<expert>/strategies.md` operational |
| 13 | Capital / Investment Memo | Capital allocation card P1-P7 | (gap — referenced via investing books genre) |
| 14 | Mentor / Stakeholder Brief | Cagan + Naval specific knowledge + CAI triad | (deferred — brief §1 Антон) |
| 15 | Strategic Reflection / IP-7 Note | Levenchuk IP-7 primary | `daily-log/` adjacent |

**Observations:**
- Strategic Layer concentrates in FUNDAMENTAL Cat A (Strategic Management) — 7 of 15
  types serve A directly (Phase 1 §3.2)
- 5 corpus exemplars exist for Type 06 — strongest signal of fit
- 5 of 15 types have corpus gaps (09, 13, 14 fully missing; 04 + 05 planned/partial)
- 3 of 15 are existing canonical artifacts that don't need new templates (01, 02, 11, 12 — last is in Foundation Layer)

Full catalogue with 1-paragraph descriptions per type: `decisions/strategic/_research/landscape-strategic-docs-2026-04-28.md`

---

## §3 Filtering results (7 PROPOSE / 8 SKIP-or-DEFER)

8 criteria applied per type (Phase 2): Solo founder fit / AI agents augment fit /
Phase 1 €50K relevance / Phase B+ readiness / D29 Korp-Startup positioning fit /
FUNDAMENTAL §6 coherence / Hybrid framework fit / Memory feedback compliance.

### 3.1 PROPOSE (7) — receive structural templates

1. **Type 03 Locks Ledger Entry** — append-only, founder-only authority, F4-F5 default. Formalizes ad-hoc Lock format scattered across `LOCKS-D*-ADDENDUM-*.md` files.
2. **Type 04 Founder Overlay (RUSLAN-LAYER)** — explicit next deliverable per FUNDAMENTAL cross-refs. Two-layer pattern from §0 of Layer 1.
3. **Type 05 North Star / DoT** — explicit deferred 27.04 morning per brief §1; multi-chat methodology constraint encoded in template (per inferred memory `methodology_multi_chat_review_for_critical_docs`).
4. **Type 06 Strategic Insight Memo** — most-corpus-evidenced (5 exemplars over 10 days); template canonicalizes the existing format DNA.
5. **Type 07 Direction / Pillar Card** — Top Lists Partner Factory ACTIVE Phase 1+ + 5 deferred Directions need lifecycle tracking artifact. Resolves Phase 1 §3.3 corpus naming-conflation between Type 06 (one-shot) and Type 07 (standing).
6. **Type 10 Bet Pitch / Shape-Up Pitch** — Singer Shape Up appetite + circuit-breaker; sits *upstream* of Project Brief (Type 11, Foundation Layer) — fills the gap PM card §6 OQ-1 + OQ-2 flagged.
7. **Type 14 Mentor / Stakeholder Briefing Pack** — concrete gap (deferred 27.04 evening for Антон); sanitization checkpoint encodes §6.4 privacy boundary.

### 3.2 SKIP (4) — already-covered, no new template

| Type | Reason | Canonical |
|---|---|---|
| 01 Foundation Vision | LOCKED v1.0 already | `decisions/JETIX-VISION-FUNDAMENTAL-2026-04-27.md` |
| 02 Constitutional Spec FPF | Lives in design/ + ailev/FPF upstream | `design/JETIX-FPF.md` |
| 11 Project Brief | Foundation Layer covers | `swarm/wiki/_templates/project-{4 types}/` |
| 12 DRR / Compound Cycle | Foundation Layer covers | `agents/<expert>/strategies.md` |

For each SKIP type, the manifest §4 declares governance protocol (e.g., FPF-Steward
quarterly audit; vertical-axis revision per FUNDAMENTAL §8.6).

### 3.3 DEFER Phase B+ (4) — premature for solo Phase 1 €50K

| Type | Reactivation predicate |
|---|---|
| 08 Phase Plan | Phase 1 → Phase 2 transition (€50K Q2 2026 gate); JETIX-PLAN.md serves Phase 1 adequately |
| 09 Quarterly OKRs | Team grows past N=1; OKRs designed for team-coordination at Intel under Grove (Doerr lineage) |
| 13 Capital Memo | Phase 2+ when revenue/headcount/$ create meaningful $-allocation OR single allocation event >€20K |
| 15 Strategic Reflection | Pattern emerges where structured-reflection captures content free-form daily-log + Strategic Insight cannot; criterion 2 fails per IP-7 anti-pattern |

### 3.4 Verdicts that could flip on walkthrough

- Type 09 OKRs → PROPOSE if Ruslan articulates a quarterly-rhythm need that current docs do not satisfy.
- Type 13 Capital Memo → PROPOSE if Ruslan signals upcoming significant allocation events.
- Type 15 Strategic Reflection → PROPOSE if daily-log + Strategic Insight combination feels insufficient.
- Type 04 Founder Overlay → DEFER if Ruslan decides RUSLAN-LAYER content lives across Direction Cards + North Star + Phase Plan rather than its own document.

---

## §4 Hierarchy + cadences proposal

### 4.1 Dependency graph (informal edge labels)

```
Type 01 Foundation Vision (LOCKED, managed)
   ▼ overlays
Type 04 Founder Overlay (RUSLAN-LAYER)
   ├─ positions ▶ Type 05 North Star / DoT
   │                ▼ pulls
   │             Type 07 Direction / Pillar Card
   │                ▼ contains-shaped-bets
   │             Type 10 Bet Pitch / Shape-Up Pitch
   │                ▼ instantiates
   │             Type 11 Project Brief (Foundation Layer)
   │
   └─ informs ───▶ Type 03 Locks Ledger Entry
                       ▲ candidate-promotion
                       │
              Type 06 Strategic Insight Memo
                       │ candidate-promotion
                       └─▶ Type 07 Direction / Pillar Card

Type 14 Mentor Brief — synthesizes-from Types 03, 04, 05, 07, 10 (sanitization gate)
```

### 4.2 Cadence + owner matrix (compressed)

| Type | Cadence | Owner | Audience |
|---|---|---|---|
| 03 lock-entry | append-only; event-driven | T0 ack mandatory; T2 draft | T0/T1/T2 + T3 mentor at quarterly |
| 04 founder-overlay | annual baseline + event-driven Phase amendments | T0 + T2 structuring | T0/T1/T2 + T3 mentor |
| 05 north-star | annual major + quarterly soft | T0 only (multi-chat methodology) | T0/T1 + T3 mentor + T4 partners (sanitized) |
| 06 strategic-insight | event-driven (~1-2/week peak) | T0 + T2 drafting | T0/T1 + T3 mentor (selected) |
| 07 direction-card | quarterly review + event-driven status | T0 defines; T1/T2 mini-swarm | T0/T1/T2 + T3 mentor |
| 10 bet-pitch | per-cycle (6w + 2w cooldown default) | T0 shaping + T2 drafting; T0-only betting | T0/T1/T2 only |
| 14 mentor-brief | event-driven per call | T0 + T2 drafting + T2 sanitization-check | T3 mentor only |

Full per-type field declarations: `decisions/strategic/_research/hierarchy-cadences-2026-04-28.md` §4.

---

## §5 Structural templates summary

7 templates produced — STRUCTURAL only (frontmatter + section structure + 1-2-sentence
example fragments + anti-scope + provenance). NO content authoring.

| Template | Path | Sections | Word count |
|---|---|---|---|
| Lock Entry | `decisions/strategic/_templates/lock-entry.md.template` | §1-§7 + frontmatter | ~750 |
| Founder Overlay | `decisions/strategic/_templates/founder-overlay.md.template` | §0-§8 + frontmatter | ~1000 |
| North Star | `decisions/strategic/_templates/north-star.md.template` | §1-§8 + frontmatter (incl. multi-chat checklist §7) | ~1200 |
| Strategic Insight | `decisions/strategic/_templates/strategic-insight.md.template` | §0-§9 + frontmatter | ~1100 |
| Direction Card | `decisions/strategic/_templates/direction-card.md.template` | §0-§8 + frontmatter | ~1050 |
| Bet Pitch | `decisions/strategic/_templates/bet-pitch.md.template` | §1-§9 + frontmatter | ~1150 |
| Mentor Brief | `decisions/strategic/_templates/mentor-brief.md.template` | §0-§7 + frontmatter (incl. sanitization checkpoint §1) | ~1200 |
| **Manifest** | `decisions/strategic/_index.md` | §0-§8 (catalogue + governance refs + STOP) | ~1700 |

Per-template features per brief §2 Phase 4 quality bar:
- ✅ Frontmatter complete (type/cadence/owner/audience/F/G/R/last_updated/supersedes/references including foundation_parts + fpf_anchors + d_locks)
- ✅ 4-9 sections per template (not too sparse, not too verbose)
- ✅ Each section 1-2-sentence example fragment (illustrative, NOT content)
- ✅ Anti-scope explicit per template
- ✅ F-G-R defaults declared
- ✅ Cross-references to Foundation parts (Parts 1-10 from Wave A candidate-parts-merged.md)
- ✅ Citation format documented at template foot

---

## §6 Open questions for Ruslan ack

### Q1 — PROPOSE list approval (high-priority)

**Question.** Of the 7 PROPOSE types, do all 7 warrant Strategic Layer templates, or
are any redundant / premature for current Phase 1?

**Watch points:**
- Type 04 Founder Overlay vs Type 05 North Star — boundary fuzzy (Phase 1 §3.3 flagged); could merge if Ruslan prefers
- Type 06 Strategic Insight vs Type 07 Direction — corpus-naming-conflation resolved by Phase 2 split; verify the split feels right

### Q2 — DEFER list approval

**Question.** Are the 4 DEFER reactivation predicates correctly scoped?

**Watch points:**
- Type 09 OKRs DEFER assumes solo-founder Phase 1 has no need for separate quarterly OKR ritual — Phase Plan + Bet Pitches + North Star milestones cover. Verify.
- Type 15 Strategic Reflection DEFER on Criterion 2 fail (IP-7 anti-pattern) — verify daily-log + Strategic Insight Memo combination is sufficient.

### Q3 — Multi-chat methodology integration

**Question.** Does the North Star template §7 multi-chat methodology checklist match
Ruslan's intent for `methodology_multi_chat_review_for_critical_docs`?

The 5-chat suggestion (§1+§2 primary / §3+§4 second-zoom / §5 epistemic-discipline /
integrative critic / mentor walkthrough) is structural. Ruslan should override
specific session-naming if needed.

### Q4 — Memory file substitution acknowledgment

**Question.** Ruslan should acknowledge that Phase 1 + 2 + 3 work substituted memory
constraints from on-disk corpus inference (Windows-side memories not on Linux server).

**Affected memories:**
- `feedback_ai_does_not_strategize` → preserved via T0-only ack discipline across all owner matrix cells
- `feedback_no_solo_founder_downgrade` → preserved via DEFER (not SKIP) on Type 13 Capital Memo
- `methodology_multi_chat_review_for_critical_docs` → encoded in North Star template §7
- `project_jetix_hybrid_framework_vision` → encoded in Founder Overlay template §5
- `project_jetix_partner_factory_top_lists` → Top Lists Direction is example reference in Direction Card template
- `project_outreach_channels` → IndieHackers as example in Founder Overlay §2
- `project_jetix_private_library_knowledge_leverage` → not directly templated (Foundation Layer concern); flagged in landscape Phase 1 §2 Type 02

If Ruslan reads the templates and any inferred constraint reads wrong, flag in walkthrough.

### Q5 — Edge typing in dependency graph

**Question.** Phase 3 §1 + manifest §2 use informal edge labels (overlays / pulls /
contains-shaped-bets / candidate-promotion / synthesizes-from). Should these be
tightened to FPF A.14 canonical edges (ComponentOf, ConstituentOf, etc.) before
content authoring next sprint?

**Recommendation (low-confidence):** keep informal labels; FPF-canonical is too narrow
for these strategic-doc relations. Document the deviation as is. Ruslan override OK.

### Q6 — Type 14 Mentor Brief: is it standalone vs generated?

**Question.** Mentor Brief template assumes a standalone artifact (per call) with
sanitization checkpoint. Alternative: it could be a *generated* artifact (script that
pulls from active Direction Cards + Locks + Phase Plan + auto-sanitizes) at brief-
creation time, rather than an authored document.

**Watch point.** If generated, the "template" becomes a generation-script schema, not
an authoring scaffold. Different sprint scope.

### Q7 — Phase 5 next-sprint scope confirmation

**Question.** Brief §6 says: "STOP after AWAITING-APPROVAL packet. Ruslan ack required
before any Strategic Layer document content writing (next sprint)."

The next sprint scope (per manifest §8):
1. Apply 5-chat multi-session methodology to North Star authoring
2. Draft RUSLAN-LAYER (Founder Overlay) v1.0 baseline
3. Create cohort-1 Direction Cards (Top Lists Partner Factory + Quick-Money AI Consulting)
4. Author first round of Bet Pitches per active Direction
5. Draft Mentor Brief v1.0 for Антон call (deferred 27.04 evening)

**Question:** confirm scope + priority ordering. If priority is different (e.g.,
Mentor Brief first because Антон call is imminent), reorder.

### Q8 — Walkthrough format suggestion

**Suggestion:** before content authoring, walk through templates in this order
(complexity-ascending): Lock Entry → Strategic Insight → Bet Pitch → Mentor Brief →
Direction Card → Founder Overlay → North Star. Each ~5 min review = ~35 min total.
Reject/amend per template; final ack moves the cycle to next sprint.

---

## §7 Provenance + commits

**Branch:** `claude/jolly-margulis-915d34`

**Commits in this cycle:**
- `87f7346` `[strategic] Phase 1 landscape research catalogue`
- `bc92820` `[strategic] Phase 2 jetix-fit filtering — 7 PROPOSE + 8 SKIP/DEFER`
- `ef55406` `[strategic] Phase 3 hierarchy + cadences + owner matrix`
- `535f719` `[strategic] Phase 4 structural templates — 7 PROPOSE templates + manifest`
- (this packet) `[strategic] Phase 5 AWAITING-APPROVAL packet — Strategic Layer templates ready`

**Files created:** 12 new (4 research + 7 templates + 1 manifest = 12); this packet
makes 13.

**Pushes:** all phases pushed to `claude/jolly-margulis-915d34` after creation.

**Provenance honest declarations:**
- Research output frontmatter declares F2 (single-author scoping; not peer-validated)
- Memory file substitution flagged in §honest_limits of every Phase output
- LJ post corpus sampled via 3 research compilations per Wave B levenchuk card §1
- Edge-typing informal in dependency graph (§5 honest declaration repeated through Phases 3-4)

---

## §8 STOP — awaiting Ruslan ack

Per brief §6: **STOP after AWAITING-APPROVAL packet. Ruslan ack required before any
Strategic Layer document content writing (next sprint).**

**Walkthrough deliverables ready:**
- Phase 1 catalogue (15 types) + Phase 2 filtering (7 PROPOSE + 8 SKIP/DEFER) + Phase 3 hierarchy/cadences/owner-matrix
- 7 structural templates + manifest in `decisions/strategic/`
- This AWAITING-APPROVAL packet with 8 open questions for ack

**Decision points for Ruslan walkthrough:**
1. Approve / amend PROPOSE list (Q1)
2. Approve / amend DEFER reactivation predicates (Q2)
3. Approve / amend North Star multi-chat methodology checklist (Q3)
4. Acknowledge memory-file substitution + flag any inferred constraint that reads wrong (Q4)
5. Decide edge-typing tightening (Q5)
6. Decide Mentor Brief authored-vs-generated (Q6)
7. Confirm next-sprint scope + priority ordering (Q7)
8. Optional walkthrough order suggestion (Q8)

After Ruslan ack:
- Status of this packet moves `AWAITING-APPROVAL` → `ACK'D`
- `decisions/strategic/_index.md` manifest §8 unblocks
- Next sprint begins (5-chat methodology applied to North Star + RUSLAN-LAYER drafting + first Direction Cards + first Bet Pitches + Mentor Brief)

---

*End of AWAITING-APPROVAL packet. Strategic Layer research + scoping complete; content
authoring blocked pending Ruslan walkthrough.*
