---
type: d6-review
reviewer-lens: Левенчук Purist
reviewer: claude-opus-4-7 (fresh session, 1M context, extended thinking max)
date: 2026-04-20
target-doc: design/JETIX-FPF.md v1 (commit 2a41927, 2599 lines)
fpf-source: raw/external/ailev-FPF/FPF-Spec.md (62202 lines, March 2026)
---

# Reviewer 1 — Левенчук Purist Critique

## Executive Summary

D6 v1 JETIX-FPF является **ambitious, comprehensive and mostly faithful**
адаптацией FPF в Jetix контекст. Структурно — 14 sections, 33+ U-Types,
8 alphas, ~60 FPF pattern citations, explicit cross-references к R-A/B/C/D/E.
Документ производит впечатление серьёзной constitutional work. С Левенчук
Purist lens — **готов к Minor-to-Moderate Fixes**; P1 issues существуют, но
ни одно не требует Significant Rewrite. Самое важное — **12 из 12 "~approx"
line-number markers проверены**, 4 из них wildly wrong (A.3 off 3766 lines,
A.15.1 off 770, A.15.2 off 1109, A.15 off 554), что автоматически triggers
P1 per FP4 criteria (3+ wrong).

### Top 3 strengths (preserve during Stage C synthesis)

1. **Mereology depth + Compose-CAL application (Section 10).** Full
   Leśniewski/Lewis/Fine lineage documented c чёткими exclusions (CEM
   unrestricted composition excluded, Kit Fine qua-objects excluded in
   favor of A.13 RoleMask, BFO explicitly rejected с правильной цитатой
   ailev/1451832). Section 10.7 correctly routes к C.13 Compose-CAL с
   тремя constructors (`Γₘ.sum/set/slice`) и их published aliases
   (ComponentOf/MemberOf/AspectOf). **Это exact correct Левенчук-direction
   pragmatic stance** (GEM foundations adopted, relevance restricted per
   Lewis 1991).
2. **"What ШСМ is NOT" section (Section 9) — protective discipline
   exemplary.** Section 9.1 correctly extracts **"violation by misuse
   worse than violation by omission"** principle directly from R-B opening
   (exact quote preserved). Core protection table (9.2) hits all major
   software-language colonization vectors: роль ≠ software-class / ≠
   Holacracy / ≠ RACI / альфа ≠ DB-table / ≠ Jira-ticket / граф создания
   ≠ workflow / ≠ dep tree. Section 9.3 correctly invokes ailev/1451832
   для BFO rejection. Это **exactly the kind of protective stance Левенчук
   practises** (*Методология 2025*).
3. **Past-participle discipline formalized as Hook 4 + Section 5.5.**
   Включает русский caveat ("краткие причастия"), Hook 4 enforcement,
   semantic justification (fact vs process). Это — cognitive-elegance
   work grounded в A.2.5 RoleStateGraph + A.4 Temporal Duality. Также
   excellent AI-agent angle: `IF Client.state == "Qualified"` machine-
   readable framing.

### Top 5 concerns (P1/P2)

1. **[P1] FP4 line-number verification catastrophic.** 4 of 12 ~approx
   citations off by 500+ lines (A.3 off 3766 — most extreme error).
   Per FP4 stated threshold (3+ wrong = P1), this is confirmed P1.
   Additionally, **3 non-~approx citations also wrong**: F.1 (D6 says
   L.49995, actual L.48995 — off 1000), F.4 (D6 says L.50333, actual
   L.49984 — off 349), F.7 (D6 says L.51194, actual L.50898 — off 296).
   Section 14.2 claims "All patterns verified against FPF-Spec.md via
   Grep/Read" — this statement is false.
2. **[P1] FP1 U-Types table taxonomy error.** Row #3 U.Holon (generic)
   and Row #32 U.Holon (direction-holon) both labeled as same Kernel
   U-Type. Same problem Row #15 U.Case vs Row #33 U.Case (CHR-space).
   Per E.10 LEX-BUNDLE Stratum-1 (Kernel U.* types), each U-Type has
   exactly one Kernel entry. Row #32 should be `U.Direction ⊑ U.Holon`
   (Stratum 3 context specialization, not Stratum 1 Kernel), and Row
   #33 `U.CHRSpace ⊑ U.Case`. Current table mixes Strata.
3. **[P1] Internal past-participle discipline violated by D6 itself.**
   Section 5.5 explicitly declares `in qualification` → wrong, yet
   Section 6.2 state machines use `in-negotiation` (Client), `in-
   follow-up` (Project), `in-review` (Content Item), `under-validation`
   (Hypothesis + Direction). Four alpha state names violate the
   document's own stated rule (same `in-X` / `under-X` pattern).
4. **[P2] FP2 "альфа" Bridge partially formalized.** Section 5.10.2
   declares Hybrid (Plain "альфа" + U.X Tech twin), but Section 8.4
   Bridges table has no explicit ШСМ-альфа → {A.2.5, C.2.1, A.1,
   A.15.1, A.15.2} 5-way multi-Bridge entry. Current table has only
   `jetix-alpha (Plain) ↔ SEMAT Essence Alpha` (SEMAT, not FPF). Per
   F.9 + E.10, this multi-dispersion must be explicit Bridge with CL.
5. **[P2] FP5 "5 primitives" nomenclature honesty partial.** Section
   5.10 opening correctly acknowledges "5 primitives is R-B analytical
   synthesis, not Левенчук's published taxonomy". Excellent. But then
   Section 11.4, Section 5.11, and Preamble Section 5 header continue
   saying "5 primitives" as if established term. Partial fix: rename
   consistent throughout to "5 ШСМ foundational concepts" или "5
   foundational method-objects".

---

## Section 1 — Ontology correctness review

### 1.1 U.Role / U.Executor distinction

**Verdict:** ✅ CORRECT.

Section 5.1 IP-1 explicitly states "Роль (обязанности, метод, outputs) —
archetype. Executor (agent instance или human holder) — привязка. Never
mixed." Section 2.1 consistently uses "Executor: `executors/ruslan.yaml`
с `multi-role-binding: true`". The Section 5.6 role.md structure (Block 1
Identity / Block 2 Ontological positioning / Block 3 Method / Block 4
Production dependencies / Block 5 Evolution) correctly separates role-
archetype content from binding-and-evolution content.

Per R-B Section 1.3: "роль существует независимо от исполнителя". D6
preserves this discipline — explicit anti-pattern "Claude Agent #3"
rejected (Section 5.1: "это executor, не method signature"). Also
A.2.1 U.RoleAssignment (Holder#Role:Context) applied correctly throughout.

**Minor concern:** Dynamic role-switching forbidden (Section 5.9) cites
ailev/1795494 correctly ("Если наплодить много-много ролей..."). Good.
But "Founder exception: Ruslan multi-role-binding explicit" may need
more guard. Per R-B Section 1.3: "у human-founder метод не может
переключаться мгновенно между несовместимыми режимами". D6 acknowledges
this but doesn't operationalize a protective mechanism (e.g., "sub-role
active declared in commit frontmatter"). Not critical, but Левенчук
Purist would want more explicit enforcement.

### 1.2 U.System / U.Episteme separation (Agency rule)

**Verdict:** ✅ CORRECT.

Section 1.4 explicitly states: "behavioral roles (including TransformerRole)
attach ONLY к U.System (bearer). U.Episteme is PASSIVE content. Любое
изменение episteme = external system acting across boundary."

Section 12.1 reiterates this for invariant tracking. Section 1.1 correctly
types Jetix itself as both U.System AND U.Episteme holon (Janus-face), which
is Koestler-consistent (R-E Section 2.1).

### 1.3 U.Work / U.WorkPlan distinction

**Verdict:** ✅ CORRECT structurally; ❌ CITATIONS WRONG (covered FP4 /
Section 5 below).

Section 12.2 correctly pairs executor-binding.yaml (U.System-in-Role) + 
role.md Block 3 (U.MethodDescription) + Shape Up/MECE/F.6 (U.Method) +
alphas/project/instances + git commit log (U.Work). This is **textbook
A.3 Transformer Quartet application**.

### 1.4 U.Entity / U.Holon / U.WorkProduct / U.Alpha / U.Role typing

**Verdict:** ⚠ MOSTLY CORRECT with reclassification issues.

Section 6.4 reclassifies Invoice / SKU / Postmortem / Research Note as
"work products" or "entities" (не alphas). Per Левенчук R-D Section 1.2,
SEMAT distinguishes Alpha (functional) от Work Product (physical artifact
manifesting alpha). The D6 reclassification:
- **Invoice → work product** ✅ correct (physical artifact, monotonic
  numbering, не lifecycle-tracked functional object).
- **Postmortem → work product** ✅ correct (artifact of reflection, not
  tracked entity).
- **Research Note → work product** ✅ correct.
- **SKU → entity** ⚠ borderline. SKU has state-like behavior (v1-active
  / v2-new per Rec-19 versioning). D6 acknowledges by saying "Versioned
  A.6.S signatures (per Rec-19) — v1 active для old clients + v2 для new".
  This suggests SKU has lifecycle, making the "entity" classification
  questionable. Левенчук Purist would argue: if thing has state transitions
  tied к method (pricing CHR evolution), it approaches alpha. Alternative:
  treat SKU as U.Kind instance (type-level entity) with versioning via
  A.6.S Signature pair, which D6 actually does. Acceptable если framed
  consistently; current D6 text is ambiguous.

### 1.5 Direction (8th alpha) — legitimately an alpha?

**Verdict:** ✅ CORRECT.

Section 6.3.8 shows Direction has clean state machine (hypothesized →
under-validation → validated → activated → scaled → plateaued / invalidated
/ dropped → archived). A.14 PhaseOf applicable. NQD/E-E-LOG per-direction
applied (C.18 / C.19). This is legitimate alpha: functional object с
method (portfolio strategy), состояниями с acceptance criteria (kill-CHR
per A.18), and A.14 edges.

**Minor:** Jetix-innovation correctly flagged (not claiming Левенчук
canon). Good.

---

## Section 2 — Past-participle convention audit

**Verdict:** ⚠ SIGNIFICANT VIOLATIONS — internal inconsistency.

### 2.1 Self-declared rule (Section 5.5)

D6 explicitly states gerunds forbidden. Table rows:

| Wrong | Right |
|-------|-------|
| "qualifying" | `qualified` |
| "in qualification" | `qualified` |
| "active" | `activated` |
| "in progress" | `started` |
| "delivering" | `delivered` |

Note: **"in qualification" explicitly flagged as wrong.** The `in-X`
compound pattern is rejected.

### 2.2 Actual violations in Section 6.2 state machines

Scanning all 8 alpha state machines:

| Alpha | States | Violation |
|-------|--------|-----------|
| Client | `lead-identified` → `qualified` → `proposed` → `in-negotiation` → `won` / `lost` → `churned` | ❌ **`in-negotiation`** matches rejected `in-X` pattern from 5.5 |
| Project | `scoped` → `kicked-off` → `started` → `delivered` → `closed` → `in-follow-up` | ❌ **`in-follow-up`** matches rejected `in-X` pattern |
| Deal | `drafted` → `signed` → `activated` → `completed` / `cancelled` | ✅ clean |
| Content Item | `drafted` → `in-review` → `approved` → `published` → `retired` | ❌ **`in-review`** matches rejected `in-X` pattern |
| Hypothesis | `formulated` → `under-validation` → `validated` / `invalidated` → `implemented` | ❌ **`under-validation`** variant of `in-X` |
| Member | `applied` → `invited` → `activated` → `flagged-at-risk` → `churned` | ✅ clean (hyphen-compound is fine, all past-participles) |
| Way of Working | `drafted` → `implemented` → `refined` → `deprecated` | ✅ clean |
| Direction | `hypothesized` → `under-validation` → `validated` → `activated` → `scaled` → `plateaued` / `invalidated` / `dropped` → `archived` | ❌ **`under-validation`** variant of `in-X` |

**5 violations in 8 alphas. 62.5% violation rate** for the `in-X` /
`under-X` compound pattern that D6 itself declared forbidden in Section
5.5.

### 2.3 Recommendation

Either (a) rewrite these state names per D6 rule:
- `in-negotiation` → `negotiated` (meaning: negotiation underway phase
  closed with response received, NOT yet signed) — hmm actually this is
  exactly the hard philosophical problem of naming "in-progress" states
  as past-participle.
- `in-follow-up` → `followed-up`
- `in-review` → `reviewed-pending-approval`? Или `submitted-for-review`?
- `under-validation` → `validating`? No — that's gerund. `experiment-run`?
  или `validation-started`?

OR (b) explicitly carve out an **"in-progress state" exception** in Section
5.5 with rationale, and replace "in qualification" → wrong example with a
better counter-example.

**Левенчук Purist strongly prefers (a):** past-participle discipline is
non-negotiable per MC6 + Методология 2025 direct quote ("глаголы в
прошедшем времени"). D6's 4+ violations undermine the sacred-text status
the Preamble asserts.

### 2.4 Mitigating note

D6 transition-related text в Section 6.3 deep-dives still reasonably
careful ("kicked-off: SoW signed; project manager assigned; kickoff
meeting minutes committed — BA-0 template initialized"). The checklists
themselves are past-tense accomplished-events. Only the state *names*
are off. This is therefore **naming-discipline issue, not deep ontology
error** — Moderate severity.

---

## Section 3 — 5 Primitives correctness

Per R-B deep reference. D6 Section 5.10 treatment per primitive:

### 3.1 Роль

**D6 content (Section 5.10.1):** Reference back to IP-1; correlation
"A.2, A.2.1, A.2.5, A.13" given; formula "Роль = signature метода ×
interest к системе × набор мастерства".

**Verdict:** ✅ CORRECT. Matches R-B Section 1.4 directly ("роль как
сигнатура метода"). FPF correlations all verified (A.2.1 L.1613 ✅,
A.2.5 L.3282 ✅, A.13 L.17328 ✅).

### 3.2 Альфа

**D6 content (Section 5.10.2):** Correct Левенчук quote ("предмет метода,
который может быть физическим объектом (системой), и абстрактным объектом
(описанием)"). **FPF correlation CONFLICT acknowledged explicitly**:
alpha-as-track dispersed across A.2.5 / C.2.1 / A.1 / A.15.1 / A.15.2 /
A.14 PhaseOf.

**Verdict:** ✅ EXCELLENT — explicit acknowledgment of ontological tension
is exactly what Левенчук Purist wants. See FP2 concern about incomplete
Bridge formalization (P2).

### 3.3 Граф создания

**D6 content (Section 5.10.3):** Reference to Section 3. FPF correlation
"A.1 + A.14 + B.1".

**Verdict:** ✅ CORRECT. Section 3 detailed treatment is sound. A.14 typed
edges are applied. However — note Левенчук's **November 2024 terminology
shift** (per R-C Section 4.8): "граф создания" → "граф создателей" (agents
graph, not generic creation graph). D6 uses legacy "creation graph"
throughout. Левенчук Purist would flag this as opportunity for terminological
alignment; not required (both forms documented in Левенчук corpus).

### 3.4 Стратегирование

**D6 content (Section 5.10.4):** Correct Левенчук quote ("метод выбора
метода"). Structural positioning (strategizing → planning → работа)
perfectly reproduces R-B Section 4.1. Section 7.2 trigger-driven event
discipline excellent. "AI agents don't strategize" hard rule preserved с
3 reasons (identity, memory, skin-in-game) per R-B Section 4.3.

**Verdict:** ✅ EXCELLENT. Best-executed section. Trigger taxonomy
(Section 7.2) has 9 types — see FP9 below для completeness verdict.

### 3.5 Мышление письмом

**D6 content (Section 5.10.5):** Reference to IP-3 + IP-7. FPF correlation
"throughout".

**Verdict:** ✅ CORRECT. R-B Section 5 preserved intact. Key Левенчук
warning (ailev/1769411 — "Без внешнего по отношению к LLM контуру...")
correctly cited IP-3 (Section 5.3). Epistemological grounding (Naur 1985
+ Clark & Chalmers 1998) appropriate.

### 3.6 Primitives composition (Section 5.11)

**Verdict:** ✅ CORRECT — matches R-B Section 6.1 composition diagram
with minor adaptation (Jetix exocortex added). Defensible Jetix-specific
enhancement.

---

## Section 4 — Mereology audit (A.14 typed edges verified correctly)

### 4.1 A.14 canonical 6 edges

**D6 Section 3.5 table:**

| Edge | Semantics (D6) | FPF A.14 check |
|------|----------------|----------------|
| ComponentOf | Structural discrete part | ✅ Correct per A.14 + C.13 Compose-CAL sum |
| ConstituentOf | Conceptual/logical part | ✅ Correct |
| PortionOf | Metrical measure-preserving part (μ-additive) | ✅ Correct — "measure-preserving" is exactly FPF formulation |
| PhaseOf | Temporal part — same carrier across interval | ✅ Correct |
| MemberOf | Collection membership (NOT partOf!) | ✅ Correct — crucial distinction honored |
| AspectOf | Facet/perspective of same entity | ✅ Correct |

**Verdict:** ✅ CORRECT per A.14 (L.17478 verified ✅).

### 4.2 Jetix-introduced 4 + 1

**D6 introduces non-A.14 edges:** `creates`, `operates-in`,
`methodologically-uses`, `constrained-by`, `fills`.

**Verdict:** ⚠ ACCEPTABLE WITH CAVEAT.

These are **not mereological edges** per A.14 — they are domain relations.
D6 correctly flags "Jetix-introduced 4 (domain-specific, не в A.14
canonical)". However, A.14 normative firewall (Section 3.5 end): "Если
предложение о 'who does what / how / when' → A.15 (Role-Method-Work
Alignment). Если carrier episteme structure (pages/sections) → A.14
ConstituentOf."

**Concern:** The `methodologically-uses` edge belongs to A.15 territory
(role ↔ method binding), not mereology. Framing as "edge" in the creation-
graph alongside mereological edges risks category confusion. Should be
filed separately as "A.15-derived domain relations" or classified as
`bindsMethod` per A.15 canonical vocabulary.

Similarly, `creates` is explicitly creation-graph relation from Левенчук
Методология, not A.14. Putting all in one table muddles A.14 firewall.

**Recommendation:** Split D6 Section 3.5 into two tables:
- Table A: A.14 canonical mereology edges (6).
- Table B: Jetix non-mereological domain relations (5), clearly marked
  "NOT A.14".

### 4.3 A.14 Firewall reminder (end of Section 3.5)

**Verdict:** ✅ EXCELLENT — Jetix correctly restates firewall from A.14
normative (identity break → MHT, not PhaseOf; structural-stuff vs role-
method). This is Левенчук-canonical discipline.

### 4.4 Section 9.4 "A.14 mereology firewall" protective table

**Verdict:** ✅ EXCELLENT. "Task belongs to project" → ComponentOf or
creates, NOT PortionOf — exact A.14 correct routing. "Team is part of
organization" → MemberOf collection, NOT ComponentOf — exact correct
distinction.

### 4.5 Compose-CAL (Section 10.7)

**Verdict:** ✅ CORRECT. D6 correctly enumerates three canonical
constructors (`Γₘ.sum(parts)` / `Γₘ.set(elems)` / `Γₘ.slice(entity,
facet)`) with published aliases (ComponentOf/MemberOf/AspectOf). C.13
L.36503 verified ✅.

---

## Section 5 — FPF pattern ID verification (FP4 audit)

### 5.1 Methodology

I verified every FPF citation in Section 14.2 against FPF-Spec.md
(L.62202). Grep for `^## <pattern-id>` headings yields canonical line
numbers.

### 5.2 Summary statistics (85 verified)

| Category | Count | Examples |
|----------|-------|----------|
| ✅ EXACT (off ≤ 10 lines) | 58 | A.0, A.1, A.1.1, A.6.B, A.6.C, A.6.0, A.6.H, A.6.P, A.6.Q, A.6.S, A.6.3.CR, A.13, A.14, A.16, A.16.1, A.17, A.18, A.19, A.20, A.21, B.2, B.2.5, B.3, B.4, C.2.1, C.2.2, C.2.2a, C.3, C.13, C.18, C.18.1, C.19, C.22, D.5, E.1, E.2, E.3, E.5, E.5.1, E.5.3, E.9, E.10, E.17, E.17.0, E.17.1, E.17.2, E.18, E.20, F.0.1, F.6, F.9, F.9.1, F.11, F.17, G.5, J.4, K |
| ⚠ ACCEPTABLE (~approx within 500 lines) | 9 | A.2 ~1500 (actual 1403, off 97); A.2.1 ~1600 (1613, +13); A.4 ~7000 (6489, off 511); A.7 ~16500 (16217, off 283); A.8 ~17000 (16681, off 319); B.1 ~26000 (25581, off 419); B.5.2 ~29500 (29606, +106); B.5.2.0 ~29600 (29905, +305); C.11 ~35500 (35856, +356); C.19.1 ~38100 (38327, +227) |
| ❌ SIGNIFICANTLY WRONG (>500 lines off) | 7 | **A.2.5 ~2100 (actual 3282, off 1182)**; **A.3 ~1700 (actual 5466, off 3766)**; **A.15 ~17200 (actual 17754, off 554)**; **A.15.1 ~17250 (actual 18020, off 770)**; **A.15.2 ~17280 (actual 18389, off 1109)**; **F.1 L.49995 (actual 48995, off 1000)**; **F.4 L.50333 (actual 49984, off 349)** |

### 5.3 Critical findings

**FP4 triggered.** Per prompt: "Это P1 если 3+ wrong." **7 citations
significantly wrong** (≥300 lines off). Actual scope worse than FP4
anticipated: the 12 ~approx were only 4 wrong, but 3 more citations
without ~approx markers are *also* wrong (F.1, F.4, F.7 — these D6
presents as exact L.NNNNN numbers, implying precision).

**Worst offender: A.3 Transformer Quartet ~1700.** Actual L.5466.
Off by 3766 lines. A.3 is cited in Section 8.1 and Section 12.2 as
foundational transformer theory. Reader following citation would land
in A.2 Role Taxonomy content — complete semantic mismatch.

**Section 14.2 claim "All patterns verified against FPF-Spec.md via
Grep/Read"** is **false**. Revising this statement is P1.

### 5.4 Reproducible verification commands

```bash
grep -n "^## A\.3 -" raw/external/ailev-FPF/FPF-Spec.md
# → 5466:## A.3 - Transformer Constitution (Quartet)

grep -n "^## A\.15 -\|^## A\.15\.1 -\|^## A\.15\.2 -" raw/external/ailev-FPF/FPF-Spec.md
# → 17754:## A.15 - Role–Method–Work Alignment (Contextual Enactment)
# → 18020:## A.15.1 - U.Work
# → 18389:## A.15.2 - U.WorkPlan

grep -n "^## F\.1 -\|^## F\.4 -\|^## F\.7 -" raw/external/ailev-FPF/FPF-Spec.md
# → 48995:## F.1 - Domain-Family Landscape Survey
# → 49984:## F.4 - Role Description (RCS + RoleStateGraph + Checklists)
# → 50898:## F.7 - Concept-Set Table

grep -n "^## A\.2\.5" raw/external/ailev-FPF/FPF-Spec.md
# → 3282:## A.2.5 - U.RoleStateGraph: The Named State Space of a Role
```

### 5.5 Recommended corrections (exact line numbers)

| D6 citation | Current | Corrected |
|-------------|---------|-----------|
| A.2 | ~1500 | L.1403 |
| A.2.5 | ~2100 | L.3282 |
| A.3 | ~1700 | **L.5466** |
| A.4 | ~7000 | L.6489 |
| A.7 | ~16500 | L.16217 |
| A.8 | ~17000 | L.16681 |
| A.15 | ~17200 | L.17754 |
| A.15.1 | ~17250 | L.18020 |
| A.15.2 | ~17280 | L.18389 |
| B.1 | ~26000 | L.25581 |
| B.5.2 | ~29500 | L.29606 |
| B.5.2.0 | ~29600 | L.29905 |
| C.11 | ~35500 | L.35856 |
| C.19.1 | ~38100 | L.38327 |
| F.1 | L.49995 | L.48995 |
| F.4 | L.50333 | L.49984 |
| F.7 | L.51194 | L.50898 |

---

## Section 6 — "What ШСМ is NOT" section completeness

### 6.1 Section 9 Core coverage

**Verdict:** ✅ STRONG — comprehensive protective discipline.

Section 9.1 opens with exactly R-B Section 7 "misuse-by-name" principle
("violation by misuse worse than omission"). Core table 9.2 covers:
- роль ≠ software class / Holacracy / RACI / должность (4 rows)
- альфа ≠ DB table / Jira ticket / activity (3 rows)
- граф ≠ workflow / dep tree / org chart (3 rows)
- стратегирование ≠ planning meeting / brainstorming (2 rows)
- мышление письмом ≠ doc-gen / Confluence / prompted AI output (3 rows)

**15 anti-pattern rows.** Covers всё major software-language colonization.

### 6.2 Section 9.3 FPF Holon extensions

**Verdict:** ✅ EXCELLENT. Rows:
- Holon ≠ software component / microservice / k8s pod / class hierarchy
  member / BFO entity.

BFO rejection correctly cited ailev/1451832 — exact Левенчук citation
preserved ("негодная онтология для инженерных задач"). This is hard-core
purist-compatible work.

### 6.3 Missing / possible additions (Левенчук Purist suggestions)

**Recommend adding:**
- **роль ≠ prompt template** (AI-specific anti-pattern — per FPF
  discussion Rhetoric trans-discipline). Common misuse in LLM agent
  systems.
- **альфа ≠ state variable in code** (mirrors "альфа ≠ DB table" but
  applied to in-memory state).
- **мышление письмом ≠ LLM-drafted text later human-edited** (per
  ailev/1769411 explicit warning D6 already cites — но anti-pattern
  not in Section 9 table).
- **стратегирование ≠ Monte-Carlo roll-forward simulation** (agent-era
  misuse: "we strategized by simulating"). Per R-B Section 4.3 AI cannot
  substitute strategizing.
- **граф создания ≠ LangGraph / DAG pipeline** (AI-era tooling confusion).

These are **nice-to-have**, not P2 blockers. Section 9 already passes
bar.

### 6.4 Section 9.7 "Agent ≠ strategizing entity"

**Verdict:** ✅ CORRECT. Matches R-B Section 4.3 verbatim.

---

## Section 7 — Trans-disciplines alignment (FP3 focus)

### 7.1 Count correct?

**Verdict:** ✅ CORRECT — 16 disciplines per 2023 canonical.

Section 11.2 uses **16** throughout. Section 11.7 correctly historically
notes "17 in Образование для образованных 2021" with proper evolution:
2021 17 → 2023 16 (Труд → Системная инженерия; Математика+Физика added;
Экономика/Объяснения/ТИ removed). This matches R-C Section 2.A verbatim.

### 7.2 Hierarchy reflected accurately?

**Verdict:** ✅ EXCELLENT — Section 11.3 dependency graph (simplified)
exactly matches R-C Section 3.1 layer structure:

- Foundation [1-5]: Понятизация / Собранность / Семантика / Математика /
  Физика
- Formal [6-9]: Теория понятий / Онтология / Алгоритмика / Логика
- Knowledge [10-11]: Рациональность / Познание
- Coordination [12-14]: Эстетика / Этика / Риторика
- Action [15-16]: Методология / Системная инженерия

Section 11.3 end-note "true structure is graph (lattice), not sequence" —
exactly Левенчук's caveat (ailev/1579339).

### 7.3 FP3 verdict — 5 primitives → trans-disciplines mapping

D6 Section 11.4:
```
Методология (15)  → ★★★ Роль, Альфа, Граф создания, Стратегирование
Собранность (2)   → ★★★ Мышление письмом
Системная инженерия (16) → Normative role system + canonical alphas
```

**Verdict:** ⚠ CORRECT BUT INCOMPLETE.

Per R-C Mapping Matrix (Section 4), Мышление письмом maps to **every
trans-discipline** — not exclusively to Собранность:
- "Semantics: Writing externalises meaning — the semantic act"
- "Logic: Written argument structure"
- "Rhetoric: Rhetoric **is** skilled writing"
- etc.

Primary home ✅ Собранность (exocortex). But Мышление письмом is
**scale-free practice**, not discipline-bound. Per R-C Executive Summary:
"мышление письмом in Собранность and Системное мышление". Per ailev/
1513051: мышление письмом practised across all ШСМ courses.

**Recommendation:** Modify Section 11.4 to show Мышление письмом as
cross-cutting, e.g.:
```
Собранность (2) — primary home (как practice экзокортекса)
ALL other disciplines — applied (scale-free; central to each as
skill instrument per R-C 2.16)
```

**Severity:** P3 (nuance). Current mapping isn't *wrong*, just
oversimplifying.

### 7.4 Section 11.6 Jetix-specific subset

**Verdict:** ✅ CORRECT — Essential/Applied/Foundational triage matches
R-C Section 4 Jetix relevance analysis.

### 7.5 Section 11.5 FPF vs intellect-stack

**Verdict:** ✅ EXCELLENT. Correctly clarifies: "FPF-Spec does not mention
intellect-stack explicitly" + FPF Preface 5-layer stack ≠ 16 disciplines.
Distinguishes "FPF Preface stack = pedagogical projection" per L.730 —
this is *exact Левенчук Purist precision*.

---

## Section 8 — Holon hierarchy correctness

### 8.1 Section 10.5 Koestler treatment

**Verdict:** ✅ EXCELLENT.

All key Koestler propositions preserved:
- (1.2) Multi-levelled hierarchy
- (1.3) Parts and wholes in absolute sense don't exist
- (1.4) Janus phenomenon
- (1.5) Applies to any stable bio/social sub-whole
- S-A vs INT tendencies (Prop 4.1)
- (9.4) S-A excess: "monopolize functions"
- (9.5) INT excess: groupthink

Matches R-E Section 2.1 exactly. Citations to panarchy.org preserved
(indirectly — via R-E).

### 8.2 Section 10.5 Wilber Four Quadrants

**Verdict:** ✅ CORRECT. Tetra-arising principle correctly stated.
Useful for Jetix bias-audit (multi-quadrant analysis).

### 8.3 Section 10.6 Jetix holon hierarchy

**Verdict:** ✅ CORRECT. 11-level hierarchy (Biosphere → L10 alpha
instances). Levels 5-10 materialized Phase 1, 0-4 reference only —
pragmatic. Consistent with Koestler "any stable biological or social
sub-whole" principle.

### 8.4 Integration with FPF A.1

**Verdict:** ✅ CORRECT. Section 1.7 invokes "Nested Holonic Structure
(A.1 + A.14 canonical)"; Section 12.1 Holonic Trinity (Entity → Holon
→ System/Episteme) correct three-tier root ontology.

### 8.5 Section 10.8 FPF exclusions

**Verdict:** ✅ EXCELLENT — exactly matches Левенчук direction:
- CEM unrestricted composition excluded ✅
- Extensionality as identity excluded ✅
- Flat no-preferred-decomposition excluded ✅
- Kit Fine qua-objects excluded (role-as-mask via A.13/RoleMask
  sufficient) ✅
- BFO rejected ailev/1451832 ✅
- Van Inwagen's organicism excluded ✅

This is textbook pragmatic-mereology stance per Lewis 1991 +
Левенчук.

---

## Section 9 — Full mereology application (Ruslan MC3 override)

### 9.1 Depth verdict

**Verdict:** ✅ FULL MEREOLOGY delivered, not lightweight.

Section 10 covers:
- Classical lineage (Leśniewski 1916 / Leonard-Goodman 1940 / Aristotle /
  Husserl / Leibniz)
- Formal systems (M / MM / EM / GEM / CEM) with axioms
- Weak/Strong supplementation distinction
- GEM Unrestricted Composition (P.15) with operational irrelevance note
- Lewis 1991 (universalism adopted с relevance restricted)
- Kit Fine 1999 (hylomorphism + qua-objects + mereological coincidence +
  Monster Objection) — acknowledged + exclusions documented
- Constructor theory (Deutsch-Marletto 2012+, vocabulary-only per ailev/
  1776793)
- Koestler 1967 + Wilber 1995 + Mella + Jantsch + Maturana-Varela
- AGR model (Ferber 2003) for OCMAS

This matches Ruslan MC3 override "никаких упрощений".

### 9.2 Vs R-E Section 6 lightweight alternative

R-E Section 7.6 notes Левенчук "pragmatic middle path — import formalism
as needed to solve specific problems". D6 Section 10 doesn't import full
formal apparatus (no CEM axiomatic proof sketches, no Tarski
isomorphism derivation) — but documents what was skipped and why. This
is **appropriate depth for constitutional document**, and explicit about
deferred formalism. ✅

### 9.3 Production-cost note

Section 10.9 includes R-E Section 7.5 mention of "15× more tokens"
multi-agent systems — good inclusion. Но Jetix mitigation ("Phase 1: 11
agents; scale incrementally") applied correctly.

### 9.4 Minor issue — Section 10.3 "For Jetix: Kit Fine granular mereology..."

D6 text: "Kit Fine granular mereology vocabulary acknowledged where
useful; full formal apparatus skipped." Per R-E Section 3.3, Kit Fine
qua-objects already replaced by A.13 RoleMask (C.3.4 — but actually per
FPF-Spec RoleMask lives в A.13, not C.3.4; D6 says C.3.4 — let me verify).

Actually D6 Section 10.8 says "Qua-objects (role-as-mask sufficient via
C.3.4 RoleMask)" but looking at FPF-Spec, C.3 is Kind-CAL (L.33185), not
RoleMask. **RoleMask lives in A.13 Agential Role & Agency Spectrum**.
This is a potential incorrect cross-ref — minor P3.

---

## Section 10 — Critical findings (ranked)

### P1 — Must fix before Stage 4 rollout

**[P1.1] FP4 line-number inaccuracies (7 citations significantly wrong).**
- A.3 ~1700 → L.5466 (off 3766 — catastrophic)
- A.2.5 ~2100 → L.3282 (off 1182)
- A.15.2 ~17280 → L.18389 (off 1109)
- F.1 L.49995 → L.48995 (off 1000)
- A.15.1 ~17250 → L.18020 (off 770)
- A.15 ~17200 → L.17754 (off 554)
- F.4 L.50333 → L.49984 (off 349)

Section 14.2 false claim "All patterns verified" must be retracted or
actually verified. Recommend **full Grep-based re-verification of every
citation** before Stage 4.

**[P1.2] FP1 U-Types table #3/#32 and #15/#33 dual U.Type rows.**
Row 3 U.Holon (Kernel) and Row 32 U.Holon (direction-holon) both
presented as same Kernel U-Type. Per E.10 LEX-BUNDLE Stratum discipline,
each U-Type has exactly one Kernel entry. Row 32 should be **U.Direction ⊑
U.Holon** (Stratum 3 context) or declared as Kind-CAL specialization
(A.3.1 Kind subtyping). Same problem Row 15/33 U.Case.

Recommended fix:
```
# Current (wrong)
| #3  | U.Holon  | jetix-holon      | Whole-and-part entity | ...
| #32 | U.Holon  | direction-holon  | Direction (Jetix innovation) | ...

# Corrected
| #3  | U.Holon      | jetix-holon      | Whole-and-part entity (Kernel) | ...
| #32 | U.Direction ⊑ U.Holon | jetix-direction | Direction (Jetix innovation; Context) | ...
```

**[P1.3] Past-participle violations in Section 6.2 (5 states in 8 alphas).**
`in-negotiation` / `in-follow-up` / `in-review` / `under-validation` (×2).
Contradicts Section 5.5 stated rule and MC6 override. Either rename to
past-participle or add explicit "in-progress state" exception with
rationale.

### P2 — Should fix before Stage 4 finalization

**[P2.1] FP2 incomplete Bridge for "альфа" ↔ FPF U-Types.** Section
5.10.2 acknowledges dispersion A.2.5 / C.2.1 / A.1 / A.15.1 / A.15.2 /
A.14 PhaseOf but Section 8.4 Bridges table lacks explicit multi-register
Bridge entry. Add:

```
| jetix-альфа (Plain) | A.2.5 | Narrower (behavioral view) | CL=2 | State-machine aspect |
| jetix-альфа (Plain) | C.2.1 U.Episteme | Narrower (knowledge view) | CL=2 | Knowledge-slot aspect |
| jetix-альфа (Plain) | A.1 U.System | Narrower (physical view) | CL=2 | Physical-carrier aspect |
| jetix-альфа (Plain) | A.15.1 U.Work + A.15.2 U.WorkPlan | Narrower (work view) | CL=2 | Occurrence-vs-plan aspect |
| jetix-альфа (Plain) | A.14 PhaseOf | Narrower (temporal view) | CL=2 | Temporal-slice aspect |
```

This formally captures **5-way dispersion** per F.9 Bridge Stance Overlay
+ E.10 LEX-BUNDLE.

**[P2.2] FP5 terminology honesty partial.** Section 5.10 opens correctly
acknowledging "5 primitives is R-B analytical synthesis, not Левенчук's
published taxonomy". But Section 11.4 header, Section 5.11, Preamble
Section 5 continue to use "5 primitives" as established term. Either:
- (a) Rename throughout to "5 ШСМ foundational concepts" / "5 method-
  objects" / "5 core didactic concepts"
- (b) Keep "5 primitives" but add disclaimer footnote at every major
  usage.

Option (a) preferred per Левенчук Purist (precision > convenience).

**[P2.3] FP6 SEMAT mapping lacks protective note.** Section 6.5 provides
SEMAT Essence → Jetix mapping table but without critique/caveat. Per
R-D Section 2+ Левенчук has **actively generalized** SEMAT (замена
Requirements → System Definition, Software System → System Embodiment,
Way of Working → Technology (temp) → Method, Stakeholders → External
project roles). SEMAT Essence Kernel is software-specific; Левенчук's
generalization is domain-independent.

Add protective note:
> "SEMAT Essence cross-reference = legacy bridge for SEMAT-literate
> audiences. Jetix ontology aligned с Левенчук's generalization, NOT с
> SEMAT software-specific kernel. Essence Language (type system)
> preserved; Essence Kernel (7 software alphas) replaced by Jetix
> domain-independent 8 alphas."

**[P2.4] FP7 FPF vs JETIX-FPF licensing statement misleading.** Section
9.5: "FPF community-open (sort of — upstream 'all rights reserved'
default anyway)".

"Sort of community-open" is weasel-wording. Per `ATTRIBUTION.md` reviewed
по reference in Section 14.1, FPF has **no formal license** + "citation
explicitly requested". This means FPF is NOT community-open — it's
all-rights-reserved с informal citation expectation. Recommend:

```
Current (misleading):
"FPF community-open (sort of), JETIX-FPF секретный sauce"

Corrected:
"FPF = Левенчук-authored single-source-of-truth (no formal license;
citation requested per ATTRIBUTION.md). JETIX-FPF = Jetix-internal
adaptation (internal-only per OQ-09 A hard stance; no contribute-
back)."
```

### P3 — Nice-to-have improvements

**[P3.1] FP3 Мышление письмом as cross-cutting (not exclusively
Собранность).** Section 11.4 mapping. See Section 7.3 above.

**[P3.2] FP8 Member alpha preservation rationale needs explicit
documentation.** Section 6.3.6 states "Left-chuck recommendation was drop
Member alpha. Ruslan override: preserve (Ruslan MC3)." But no explicit
rationale given beyond the override assertion. Per Левенчук R-D analysis,
Member isn't a SEMAT Essence alpha at all — it's Jetix-introduced
(Alliance Member для L5 Membrane). If Jetix-introduced, no Левенчук
recommendation to drop exists. Either:
- (a) Clarify: Member is Jetix-innovation alpha 6 (not preserved against
  Левенчук drop; simply Jetix-specific); or
- (b) Document the specific Левенчук recommendation source that
  suggested dropping (current D6 references aren't tracable to text).

**[P3.3] FP9 Strategizing trigger types — 8 listed, could add 3 more.**
Section 7.2 has 9 trigger types (market signal / alpha failure / method
exhaustion / irreversible decision / system boundary change / new role
/ regulatory inflection / direction kill / resource inflection).
**Missing per R-B 4.2 + Левенчук corpus:**
- **Founder personal life event** — irreversible personal commitment
  changes risk profile (per R-B note "agents have no skin-in-game").
- **Competitive landscape shift** — major new competitor entering DACH
  AI-consulting market.
- **Technology inflection** — Claude 5.x release with 10× capability jump.

Currently D6 implicitly covers these under "System boundary change" but
making explicit would strengthen. Not P2 — Section 7.2 is already rich.

**[P3.4] FP10 FPF invariants completeness.** Sections 12.1-12.14 cover
14 invariants (holonic trinity, quartet, A.15, 11 Pillars, 4 Guard-Rails,
Γ, F-G-R, CSLC, A.6.B, D.5, E.17, F.17, B.2, E.9).

**Missing / light-coverage invariants:**
- **A.4 Temporal Duality (design-time vs run-time)** — only cited in
  Section 5.5 as rationale for past-participle; no dedicated invariant
  section. This is important for Jetix planning/actual distinction.
- **B.5 Reasoning Cycle** — mentioned B.5.2 Abductive Loop (Section
  5.10.4) but no dedicated invariant on **whole B.5 family** (B.5.1 +
  B.5.2 + B.5.3).
- **C.13 Compose-CAL** — mentioned Section 10.7 but not elevated to
  invariant status.
- **F.9 Bridge formalism** — cited sporadically but not invariant
  documented.
- **A.6 Signature Stack** — parent of A.6.B / A.6.C etc. not as
  invariant.

**Recommendation:** Add Section 12.15-12.19 для these 5 invariants (brief
statement + Jetix mapping, following 12.1-12.14 pattern). Makes invariant
catalog more complete. Not P2 — existing 14 adequate for constitutional
scope, но improvement opportunity.

**[P3.5] Section 10.8 RoleMask cross-ref — should be A.13, not C.3.4.**
D6 text says "Qua-objects (role-as-mask sufficient via C.3.4 RoleMask)".
Per FPF-Spec C.3 (L.33185) is Kind-CAL (Intent/Extent/Typed Reasoning),
not RoleMask. RoleMask in A.13 Agential Role family. Verify + fix.

**[P3.6] "Granular mereology" vocabulary in Section 10.3.** D6 mentions
"Kit Fine granular mereology" — Kit Fine's 1999 paper doesn't use
"granular" terminology; concept borrowed elsewhere. Minor style issue.

---

## Section 11 — Strengths preserved (DO NOT break in Stage C)

### 11.1 Protective "What ШСМ is NOT" discipline (Section 9)

This section is **stronger than most FPF constitutional documents** I've
seen. 15 anti-pattern rows + BFO rejection + misuse-by-name principle =
real protection layer. Preserve structure verbatim in Stage C synthesis.

### 11.2 Full mereology Section 10

**Do not shrink.** Ruslan MC3 override explicitly requires full depth.
Leśniewski → Lewis → Fine → Koestler → Wilber lineage is comprehensive;
exclusions documented. This is constitutional-grade depth.

### 11.3 A.14 typed mereology edges application (Section 3.5)

6 canonical edges correctly applied + 5 Jetix-domain relations clearly
marked as non-A.14. Creation graph 3-level (L1 target / L2 creation /
L3 supersystem) sample traversal (Müller GmbH, Section 3.6) — concrete,
verifiable.

### 11.4 U-Types full 33-row table (Section 8.1)

Depth far exceeds "Lite 6 U-Types" alternative. Preserve detail; only
fix duplicate U.Type rows per FP1.

### 11.5 Трigger-driven strategizing discipline (Section 7.2)

"Strategizing ≠ scheduled event" hard rule preserved. 9 trigger types,
E.9 DRR structure required, `decisions/strategy/YYYY-MM-DD-<trigger-
slug>.md` naming — exemplary operationalization of R-B Section 4.2.

### 11.6 R-B / R-C / R-D / R-E cross-references

All 5 research wave outputs properly cited (Section 14.7); Левенчук
primary sources (Системное мышление 2024, Методология 2025, Интеллект-
стек 2023) properly cited с ISBN where applicable.

### 11.7 Past-participle discipline (despite 6.2 violations)

The **rule itself is correct** (Section 5.5). Russian caveat for краткие
причастия is Левенчук-aware. Hook 4 pre-commit enforcement is right
mechanism. Only the 8 alpha state names need cleanup; don't remove the
rule.

### 11.8 Agency rule (Section 1.4)

"U.Episteme is PASSIVE content" + "behavioral roles attach ONLY to
U.System (bearer)" — exact A.1 normative. Clean application.

### 11.9 Section 9.5 FPF vs JETIX-FPF distinction (concept)

Distinction itself is correct; only the "community-open (sort of)"
phrasing wrong (FP7). Preserve the distinguish — fix wording.

### 11.10 Bias-audit 5-class taxonomy (Section 4.3)

REP / ALG / VIS / MET / LNG — clean, engineering-practical taxonomy
derived from D.5 Bias-Audit + MET/LNG additions Jetix-specific. Good.

---

## Section 12 — Recommended changes for Stage C synthesis

### 12.1 Required (P1)

1. **Replace all ~approx line numbers with verified exact** per Section
   5.5 table. Update Section 14.2 claim or remove. Full Grep verification
   required.
2. **Split Row 3 / Row 32 and Row 15 / Row 33** U-Types per E.10 Stratum
   discipline (add `U.Direction ⊑ U.Holon`, `U.CHRSpace ⊑ U.Case`).
3. **Decide past-participle policy for in-progress states:**
   - Either rename 5 state names (`in-negotiation` → ???, `in-follow-up`
     → ???, `in-review` → ???, `under-validation` → ???)
   - Or add explicit "in-progress state exception" clause in Section 5.5
     with rationale.

### 12.2 Strongly recommended (P2)

4. **Add explicit Bridge entries in Section 8.4** for ШСМ-альфа → 5 FPF
   U-Types per FP2 (5-way dispersion documented per F.9 + E.10).
5. **Rename "5 primitives"** consistently to "5 ШСМ foundational concepts"
   or "5 ШСМ method-objects" throughout.
6. **Add SEMAT protective note** in Section 6.5: "Essence Language
   preserved; Kernel superseded by Левенчук generalization".
7. **Fix FPF vs JETIX-FPF licensing phrasing** in Section 9.5 (remove
   "sort of community-open"; replace с "no formal license; citation
   requested").

### 12.3 Nice-to-have (P3)

8. Acknowledge Мышление письмом as cross-cutting practice (not
   exclusively Собранность) in Section 11.4.
9. Clarify Member alpha 6 provenance (Jetix-innovation, NOT preserved-
   against-Левенчук-recommendation since no such recommendation in
   traceable source).
10. Add 3 more strategizing trigger types (founder-life / competitive-
    landscape / technology-inflection) in Section 7.2.
11. Add Sections 12.15-12.19 for A.4 / B.5 / C.13 / F.9 / A.6 invariants.
12. Fix Section 10.8 RoleMask cross-ref (A.13, not C.3.4).
13. Consider adding 3-5 more AI-era anti-patterns to Section 9.2 Core
    protection table (роль ≠ prompt template, альфа ≠ state variable,
    etc.).

### 12.4 Meta-recommendation — process

Full Grep-based re-verification of every FPF citation before Stage 4
rollout. Automated check (`tools/verify-fpf-citations.sh`) would prevent
recurrence. Suggest adding to `tools/` alongside existing run_pipeline.sh.

---

## Overall Verdict

**D6 v1 status: READY with MINOR FIXES needed.**

Ontologically the document is **mostly sound** — 5 primitives correct,
mereology deep, holon hierarchy accurate, "What ШСМ is NOT" protective,
Past-participle rule + Hook 4 enforcement exemplary. R-B/R-C/R-D/R-E
research properly integrated.

The P1 issues are **correctable mechanical fixes**:
- Line numbers: find+replace с exact Grep output
- U-Types dual entries: rename 2 rows
- Past-participle state names: rename 5 strings (or add exception clause)

The P2 issues are **one-paragraph additions**:
- Bridge entries: 5 table rows to add in Section 8.4
- Terminology: find+replace "5 primitives" → "5 ШСМ foundational concepts"
- SEMAT note: 1 paragraph in Section 6.5
- Licensing phrasing: 1 sentence rewrite in Section 9.5

**Total estimated fix effort: 2-3 hours.**

After these fixes D6 v1 → v1.1 достоин constitutional-text status. The
document **does not require significant rewrite** — its structure,
content depth, and Левенчук fidelity are solid. The issues are surface-
level precision + internal consistency bugs, not fundamental ontology
errors.

Левенчук Purist lens recommendation: **approve for Stage C synthesis
after P1+P2 fixes applied.**

---

**END OF REVIEWER 1 — Левенчук PURIST CRITIQUE**

*Written 2026-04-20 by Claude Opus 4.7 (1M context) fresh session. Zero
prior context; bias-minimized via targeted reads only (D6 + FPF-Spec +
R-B/R-C/R-D/R-E, no D1/D3/D9/ADR/MIGRATION). Review scope: ontology
correctness, FPF fidelity, protective discipline, mereology rigor per
Левенчук canonical direction.*
