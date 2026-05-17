---
title: "Critic review — 01-fpf-on-human-language.md v1 epistemic audit"
type: critic-review
mode: critic
expert: philosophy-expert
task_id: task-fpf-iwe-phase-b-2026-05-17
target_artefact: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md
date: 2026-05-17
F: F4
G: philosophy-critic-internal
R: refuted_if_any_hot-spot-prediction_shown_wrong_by_Levenchuk_reaction
prose_authored_by: philosophy-expert (critic scribe; not Levenchuk)
sources:
  - path: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md
    range: "full"
  - path: inbox/levenchuk-tg-2026-05-17.md
    range: "C1..C7"
  - path: reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
    range: "full"
  - path: reports/fpf-iwe-distillation-2026-05-17/99-glossary-levenchuk-terms.md
    range: "full"
  - path: raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md
    range: "full"
---

# Critic review — `01-fpf-on-human-language.md` epistemic tightening

> **Critic posture.** philosophy-expert in `mode: critic`. Audience: Levenchuk + Tseren
> (L1 epistemic guardians). Goal: surface every point where the doc could trigger
> "bredoten'" / "вы перевернули смысл" / "поверхностно" from Levenchuk.
> Brigadier writes v2 from this. I do NOT write v2.

---

## §1 Conformance Checklist (≥5 binary checks per §3.1)

| # | Check | Result | Evidence (line ref in artefact) |
|---|-------|--------|---------------------------------|
| CC-1 | **Falsifier-named (Popper).** Every non-trivial claim carries an explicit falsifier or refutation receipt. | **PARTIAL FAIL** | Frontmatter has `R: refuted_if_levenchuk_verbatim_misquoted_OR_mechanism_mischaracterized` — one global R for 462 lines. Section-level claims (§4 mechanism descriptions, §6.3 seven-mechanism list) carry NO per-claim R. Violates F-G-R granularity requirement — a single blanket falsifier is not per-claim. |
| CC-2 | **Paradigm-named on shift (Kuhn).** When the doc transitions from Levenchuk-verbatim to our synthesis, the shift is declared. | **FAIL** | §6.3 ("The actual mechanism — step-by-step (synthesized from Spec + Readme)") and §6.4 ("Why this is intelligence amplification") blend verbatim Levenchuk quotes with our synthesis framing without declaring the boundary. The header `synthesized from Spec + Readme` is insufficient — it does not name the paradigm of the synthesis (our interpretive frame vs Levenchuk's own) nor the anomaly/transition. |
| CC-3 | **Mental-model + applicable-conditions cited.** Every model invocation names the model + conditions. | **FAIL** | §4.1 frames IP-1 Role≠Executor as a Levenchuk mechanism but IP-1 is explicitly a RUSLAN-LAYER term (per the artefact itself, line 258: "Не explicit pattern ID в Spec — это RUSLAN-LAYER IP-1 в Bundle 1 RUSLAN-ACK 2026-04-28"). The same §4.2, §4.3, §4.7 do the same: they present Jetix-internal constructs in a section titled "Core mechanisms FPF". No `conditions:` or `applicable_in_our_context_only:` tag distinguishes FPF-canonical from RUSLAN-LAYER. |
| CC-4 | **Method declares what it is NOT (via-negativa).** The doc names what it is NOT trying to do. | **PARTIAL PASS** | §7 "Что мы НЕ вытащили Phase A" exists and is honest. Constitutional posture note at top of document establishes scribe framing. However, no via-negativa block names that §4 is NOT a presentation of canonical FPF patterns — it mixes FPF and RUSLAN-LAYER without an `anti_scope:` block that would protect against this misread. |
| CC-5 | **Dichotomy-of-control identified for meta-decisions.** Where the doc makes a meta-claim about what FPF "does" for intelligence amplification, in-control/not-in-control is identified. | **FAIL** | §6.4 "Why this is intelligence amplification" presents Levenchuk's claim as universal ("FPF provides the architectural discipline to navigate the entire frontier"). No ClaimScope qualifies this: "holds when: team size >= N; complexity dimension >= M" — absent. The claim as written looks absolute. Per Levenchuk's C2/C3 feedback, he would flag: "you are stating FPF's value claim without bounding it." |
| CC-6 | **Fallacy-named-when-named.** When the doc implicitly reasons "FPF = intelligence amplification, therefore Jetix with FPF = intelligence amplification", the inference is made explicit and testable. | **FAIL** | §6.4 last paragraph (lines 446-447) makes the inference leap: "Не 'память' и не 'автоматизация' — а архитектура коллективного интеллекта. Левенчуковский C3 целится в то что наша Foundation v1.0 + Wiki v2 + skills focus на storage + retrieval + delegation — это substrate для intelligence amplification, но без FPF механизмов... не сама intelligence amplification." This is a valid claim BUT it has not been made falsifiable — no acceptance predicate states what would refute the claim that "our substrate + FPF mechanisms = intelligence amplification." |
| CC-7 | **Meta-claim grounded in object-level.** Every meta-level claim about FPF mechanisms references a concrete object-level instance. | **PARTIAL PASS** | §6.3 seven-mechanism list does ground each mechanism in a pattern reference (A.1.1, A.2+A.3, etc.). However §5.2 "Big storylines unique to FPF" is almost entirely meta without concrete_instance fields — it lists narrative labels ("Trans-disciplinarity as meta-theory of thinking") without an example of the pattern in action. |

**Aggregate CC result:** 2 partial pass, 4 fail, 1 partial pass. Artefact does NOT pass conformance gate as-is.

---

## §2 Acceptance Predicate (Hamel-binary, §3.2)

```
acceptance_predicate:
  "Every non-trivial claim in §3..§6 carries either (a) a verbatim Levenchuk
  quote with FPF-Spec line ref + explicit falsifier, OR (b) a clearly marked
  RUSLAN-LAYER / OUR-SYNTHESIS disclaimer with ClaimScope declaring
  'holds_in_our_context_only' AND an explicit falsifier; zero claims in §4
  present RUSLAN-LAYER IP-* patterns as canonical FPF patterns without
  disambiguation."
```

This predicate is currently NOT satisfied. The primary blocking failures are:
- §4 (IP-1, IP-2, IP-3, IP-7) — RUSLAN-LAYER terms presented in an FPF-mechanisms section without clear RUSLAN-LAYER labels visible to a cold reader (Levenchuk).
- §6.3-6.4 — synthesized claims without per-claim F-G-R.

---

## §3 Alternatives (≥2 + status-quo, each with kill-condition, per §3.3)

### Alternative A — "Radical scribe" (verbatim-only)

Strip §4 entirely of IP-1/IP-2/IP-3/IP-7 content. Replace with a clearly-titled section "RUSLAN-LAYER abstractions we derived from FPF" that explicitly does not claim Levenchuk authorship. Retain §4.4 (A.6.B), §4.5 (A.14), §4.6 (B.3 F-G-R) as these ARE FPF-canonical.

Kill-condition: This kills the document's utility for explaining to Tseren how our Foundation maps to FPF — the mapping is useful context for the residency conversation. But for Levenchuk-facing material, this is the safest path.

### Alternative B — "Disambiguated dual-column" (our reading vs their text)

Retain IP-* sections but restructure §4 as two explicit sub-sections: `§4a FPF-canonical mechanisms` (A.6.B, A.14, B.3, with verbatim Spec quotes + line refs) and `§4b RUSLAN-LAYER abstractions inspired by FPF` (IP-1, IP-2, IP-3, IP-7 — explicitly labeled as Jetix-internal). Each claim in §4b carries `ClaimScope: holds_in_Jetix_context_only; not_attributed_to_Levenchuk`.

Kill-condition: This works ONLY if every reader sees the structural split clearly. If Levenchuk reads linearly and hits §4b before noticing the section heading, confusion remains. Requires prominent section-level disclaimer.

### Status quo (no change)

Keep v1 as-is. Current §4 header "Core mechanisms FPF" with IP-* patterns inside. Glossary §99 and self-audit §06 clarify IP-* are RUSLAN-LAYER, but a cold reader of doc 01 alone would not see this.

Kill-condition: Levenchuk reads §4.1 ("IP-1 Role≠Executor") and flags "это не мой термин — откуда IP-1?" The "Не explicit pattern ID в Spec" clarifier on line 258 is insufficient — it appears AFTER the header "IP-1 Role≠Executor" which implies FPF canonicity. Status quo fails the L1-audience bullshit-proofness test.

**Recommendation for brigadier:** Alternative B is the correct v2 path. The IP-* mapping value must be preserved for Tseren cooperation framing, but with explicit RUSLAN-LAYER labeling.

---

## §4 Anti-scope (§3.4)

- This critic is NOT producing a replacement for §4 prose — that is brigadier + writer responsibility.
- This critic is NOT evaluating whether Levenchuk's intelligence amplification claim is correct epistemically — that is outside our domain (his work, his claim; we are scribes).
- This critic is NOT assessing capital/product strategy implications of FPF adoption — that is investor-expert domain.
- This critic is NOT running domain code review on FPF pattern names or their technical correctness — that is engineering-expert domain.
- This critic is NOT recommending whether to respond to Levenchuk's TG message — that is Ruslan's (HITL) strategic decision.
- This critic is NOT evaluating the other 5 distillation files (02-05) — scope is doc 01 only.

---

## §5 Hot-Spot Register — ≥3 predicted Levenchuk objection points

### HS-1 — §4 title "Core mechanisms FPF" containing RUSLAN-LAYER IP-* terms

**Artefact location:** Lines 254-319. Section header: "§4 Core mechanisms FPF — verbatim treatment". Sub-sections include §4.1 "IP-1 Role≠Executor", §4.2 "IP-2 (наш термин для Foundation gate)", §4.3 "IP-3 / IP-7 (наши)".

**Predicted Levenchuk reaction:** "IP-1, IP-2, IP-3, IP-7 — откуда? Это не FPF. Вы мне приписываете термины которых у меня нет." Even though the artefact says "Не explicit pattern ID в Spec — это RUSLAN-LAYER" within the sub-sections, a cold reader scanning section headers sees "§4 Core mechanisms FPF" and then "IP-1 Role≠Executor" and reads it as an FPF pattern. This is the highest-risk hot spot for the "вы перевернули смысл" reaction.

**Source evidence:** `inbox/levenchuk-tg-2026-05-17.md` C1 — Levenchuk explicitly states he has ONE document (FPF-Spec + README). Any terminology not in that document that appears under a "Core mechanisms FPF" header is a false attribution risk. [src: inbox/levenchuk-tg-2026-05-17.md:41-42]

**v2 design proposals:**

(a) **Tighter quote path.** Rename §4 header to "§4 Selected FPF mechanisms + Jetix-layer abstractions". Add bold disclaimer at top of §4: `> FPF-canonical = §4.4, §4.5, §4.6 below. IP-1/IP-2/IP-3/IP-7 (§4.1-§4.3, §4.7) = RUSLAN-LAYER abstractions inspired by FPF — NOT Levenchuk's patterns. Левенчуковского термина «IP-*» не существует.`

(b) **Explicit disclaimer path.** In each IP-* sub-section, add at the very first line (before the Source note): `> **RUSLAN-LAYER only.** Этот термин не существует в FPF-Spec. Не атрибутировать Левенчуку.`

(c) **Structural split path.** Move §4.1-§4.3, §4.7 into a completely separate §4b section titled "Jetix-specific abstractions (RUSLAN-LAYER; inspired by FPF, not identical to FPF)". Keep §4 title as purely FPF-canonical: §4 = A.6.B + A.14 + B.3 only.

**Recommended:** (c) structural split is cleanest for L1 audience.

---

### HS-2 — §6.3 "synthesized from Spec + Readme" — our synthesis posing as FPF claim

**Artefact location:** Lines 417-433. Header "§6.3 The actual mechanism — step-by-step (synthesized from Spec + Readme)". The 7-point list is our own synthesis mapping FPF patterns to an "intelligence amplification" narrative.

**Predicted Levenchuk reaction:** "Я нигде не говорю '7 механизмов intelligence amplification'. Это ваша интерпретация. Вы написали 'verbatim treatment' в заголовке §4 и 'synthesized' в §6.3 — где граница?"

The risk is:
1. The framing "FPF превращает 'raw intelligence' в 'amplified collective work' через 7 механизмов" is our synthesis — we invented this 7-point structure. Levenchuk may object to both the number and the framing as oversimplification.
2. The "без этого / с этим" format in each of the 7 points is our comparative narrative device — not from Spec.

**v2 design proposals:**

(a) **Tighter quote.** Replace "The actual mechanism — step-by-step (synthesized from Spec + Readme)" with "§6.3 По нашему пониманию Spec + Readme: 7 patterns intelligence amplification". Add: `> **Наш разбор, не Левенчуковская формулировка.** Структура «7 механизмов» — наш синтез из FPF Spec L165-171, L700-708, L499, L513. Levenchuk не использует этот enumeration.`

(b) **Explicit ClaimScope.** Add frontmatter-style block before §6.3: `ClaimScope: наш синтез; not attributed to Levenchuk; holds_for_our_explication_purposes_only`.

(c) **Replace with structural map vs interpretation.** Instead of "7 mechanisms", present a Levenchuk verbatim table: column 1 = exact Spec quote, column 2 = pattern reference, column 3 = what we understand this to mean for intelligence amplification (clearly labeled "наше понимание").

**Recommended:** (a) + (c) combined — keep our synthesis value but mark it unambiguously as our explication, not his claim.

---

### HS-3 — §5.3 "Eleven Pillars" — partial list presented as if complete

**Artefact location:** Lines 355-366. "§5.3 Eleven Pillars (E.2) — Constitution". Lists P-1, P-2, P-7, P-8, P-10 then "(Full P-1 through P-11 list in E.2; not fully extracted Phase A — TO-COLLECT в Phase B if Ruslan needs.)"

**Predicted Levenchuk reaction:** "Почему вы перечисляете только 5 из 11? И почему TO-COLLECT? Вы же загрузили FPF-Spec.md — там всё есть. Это выглядит как поверхностно." The TO-COLLECT note signals to Levenchuk that we did not actually read/extract the spec — we skimmed it. This is the "поверхностно" trigger.

**v2 design proposals:**

(a) **Tighter quote.** Extract all 11 Pillars from FPF-Spec.md E.2 before publishing v2. This is a Phase B task but the gap should be closed before showing to L1 audience.

(b) **Honest scribe path.** Replace "not fully extracted Phase A — TO-COLLECT в Phase B" with: `> **Phase A scope limit.** FPF-Spec.md (72K lines) содержит полный список E.2. Мы сознательно ограничились §5 pillars наиболее релевантными к intelligence amplification discussion (P-1, P-2, P-7, P-8, P-10). Full E.2 читается напрямую в [FPF-Spec.md §E.2].`

(c) **Replace with full list.** Search FPF-Spec.md for E.2 and extract all 11. This is the correct action for an L1-facing document.

**Recommended:** (c) for v2. The partial list with TO-COLLECT is a credibility risk with Levenchuk.

---

### HS-4 — §3.5 "FPF encoding (word 'alpha' ABSENT in Spec)" — high-risk interpretation

**Artefact location:** Lines 143-151. "Why FPF dropped the word." Claims FPF generalizes to non-SEMAT context; that FPF "uniformly" encodes alpha mechanism via A.2.5 + A.15.1.

**Predicted Levenchuk reaction:** "Почему вы объясняете зачем я 'dropped' слово alpha? Вы знаете лучше меня зачем?" The "Why FPF dropped the word" header is us assigning motivation/rationale to Levenchuk's design decision. This is posture creep — from scribe to interpreter of his intent.

**v2 design proposals:**

(a) **Tighter quote.** Find verbatim Levenchuk statement about why the alpha word is absent in FPF (from LJ posts or Spec Preface). If none exists, do not claim to know why.

(b) **Explicit disclaimer.** Replace "Why FPF dropped the word" with "Наше понимание (не Левенчуковское объяснение): word 'alpha' absent in FPF-Spec; mechanism encoded via A.2.5 + A.15.1. Если есть прямая цитата — заменить."

(c) **Remove interpretive claim.** Simply state the observable fact: "Слово 'alpha' в FPF-Spec.md не используется. FPF encoding этого механизма — через A.2.5 U.RoleStateGraph и A.15.1 U.Work [per A-fpf-spec-5-primitives.md §3.3]." Remove all "Why FPF dropped" interpretive framing.

**Recommended:** (c) removes the interpretation risk cleanly.

---

### HS-5 — §2 (last sentence) — attributing Levenchuk's TG message as source for "один документ"

**Artefact location:** Lines 42-43. "FPF — не один документ + код, а одна большая spec (62K строк) + Readme; других «FPF-related» документов нет — Левенчуков explicit в TG 2026-05-17: «всего один — github.com/ailev/FPF (ладно, два: ещё README.md)» [inbox/levenchuk-tg-2026-05-17.md:26]."

**Epistemic status.** This is actually correct and well-cited. The risk is different: the TG message is a private message (F8 as per inbox frontmatter); however in v2 shown to Levenchuk this becomes a public document. Levenchuk would see us quoting his private TG message. This is not a falsifiability issue but a **consent / attribution** issue. If the doc is shared with Levenchuk as a research artefact, citing his private message without noting it was private TG may cause friction.

**v2 design proposal.** Add context note: `[inbox/levenchuk-tg-2026-05-17.md:26 — частное TG-сообщение Левенчука Руслану, 2026-05-17]`. This makes the source nature explicit.

---

## §6 F-G-R Audit Table (per §3.6)

Non-trivial claims in the artefact audited against F-G-R discipline.

| Claim | Location | F declared? | G declared? | R declared? | Gap |
|-------|----------|-------------|-------------|-------------|-----|
| "FPF is an operating system for thought" | §1, line 24-26 | F (verbatim Spec) — acceptable | G: general | R: refuted_if_misquoted — OK | **Pass** — verbatim quote with line ref |
| "FPF — это pattern language (300+ patterns)" | §2, line 42 | Implicit F4-F5 | G: general | R: none | **Fail** — 300+ count needs source ref (Spec line) + explicit F + R-refuted_if_count_wrong |
| "IP-1 Role≠Executor — why critical: personnel changes = role changes" | §4.1, lines 262-267 | Not declared | G: not declared | R: not declared | **Fail** — entire IP-1 sub-section has no F-G-R; it is F3 (Jetix internal doc, not externally verified) |
| "7 mechanisms intelligence amplification" | §6.3, lines 419-433 | F: not declared (our synthesis) | G: not declared | R: not declared | **Fail** — synthesized claim list needs F: F3 (our interpretation) + G: Jetix-internal analysis + R: refuted_if_Levenchuk_says_list_wrong |
| "Pareto frontier of complexity" verbatim quote | §6.2, lines 403-413 | F: verbatim Spec | G: not declared | R: refuted_if_misquoted — implied | **Partial** — good quote + line ref but no G or explicit R |
| "Это substrate FOR intelligence amplification, не сама intelligence amplification" | §06 self-audit §2.1, cross-referenced in §6.4 | F: F4 (per 06-honest-self-audit.md frontmatter) | G: distillation-self-audit | R: refuted_if_classification_overstates | **Pass in §06** — but this conclusion is stated in §6.4 of doc 01 WITHOUT its F-G-R anchor |
| "AI agents do NOT strategize" | §3.7, line 208 | Implicit F6 (R-B cite) | G: not declared | R: not declared | **Partial** — cite is R-B §4.3, acceptable; G and R missing |
| "Writing-as-Thinking: если сам текст пишет LLM — исчезает мышление письмом как когнитивный процесс" | §3.8, lines 236-238 | Verbatim R-B §5.5 | G: not declared | R: refuted_if_Levenchuk_retracts | **Partial** — verbatim + cite acceptable; G missing |

**Summary.** 1 Pass, 2 Partial, 5 Fail/Partial. The most critical failures are the 7-mechanism synthesis (§6.3) and the IP-* sections (§4.1-4.3) — these have zero F-G-R and are the highest-risk content for L1 audience.

---

## §7 Epistemic Posture Check (C1 + C5 surface)

**Question:** Is the doc framed as "наш разбор FPF" (honest scribe) or does it creep toward "наш аналог FPF"?

**Finding.** v1 has POSTURE CREEP in three locations:

1. **§4 section title** "Core mechanisms FPF" with IP-* content — implies Jetix's IP-* labels ARE FPF. (Creep type: false attribution of our constructs to Levenchuk's framework.)

2. **§6.3 synthesis** "The actual mechanism — step-by-step" without "наш разбор" qualifier — implies the 7-step enumeration is FPF's own claim. (Creep type: our synthesis presented as FPF content without explicit boundary declaration.)

3. **§3.5 "Why FPF dropped the word 'alpha'"** — interprets Levenchuk's design motivation without a source quote. (Creep type: we author an explanation for his decision, attributing it to him implicitly.)

The Constitutional posture note at the top of the document ("Scribe-mode. Verbatim Левенчуковский где возможно") does NOT propagate into the sections where the creep occurs. A cold reader (Levenchuk or Tseren reading §4 without the preamble fresh in mind) would encounter IP-* framing inside an FPF-mechanisms section.

**What C1 demands** (`inbox/levenchuk-tg-2026-05-17.md` C1): our docs that reference FPF must clearly mark what is Levenchuk's and what is ours. v1 does this partially but incompletely. v2 must make the boundary **structurally visible** (section headings + per-section disclaimers), not only visible in sub-section inline text.

---

## §8 Freshness Check (CHANGELOG-2026-04-20-to-2026-05-16.md)

v1 was based on the 2026-04-20 vendored snapshot of FPF-Spec.md. The upstream HEAD is now `c86eabd (2026-05-16)` with +10,598 lines (+17%).

**Freshness implications for v2:**

1. **E.10.SEMIO campaign** — new conformance items (CC-E10.*) on inscription/normative vs informative distinction. Directly relevant to our "мышление письмом" claim in §3.8 and to our append-only log discipline. v2 should add: `[Note: E.10.SEMIO per upstream c86eabd 2026-05-16 adds inscription-discipline anchor — relevant to §3.8.]`

2. **A.6.P publication discipline** sub-clause — links SEMIO boundary statements to role-output artefacts. Relevant to Part 4 Role Taxonomy reference in §4.1. v2 should note A.6.P as additional reference in §4.1 context (or in the RUSLAN-LAYER section if restructured per Alternative B/C).

3. **Canonical snapshot.** v2 must update the corpus reference from `2026-04-20` to `c86eabd 2026-05-16` to show we are reading the current upstream.

---

## §9 Specific Failures (AP code register)

| AP code | Where triggered | Count |
|---------|----------------|-------|
| AP-PHIL-1 (claim-without-falsifiability) | §6.3 seven-mechanism list; §4.1-4.3 IP-* sections; §2 "300+ patterns" count | 3 instances |
| AP-PHIL-2 (paradigm-inconsistency-unflagged) | §6.3 synthesis vs scribe posture — paradigm transition not declared | 1 instance |
| AP-PHIL-3 (instrumental-vs-epistemic-collision) | §6.4 final para — mixes "это substrate" (epistemic) with "без FPF механизмов не сама intelligence amplification" (implies "we should add FPF" = instrumental) | 1 instance |
| AP-PHIL-11 (meta-without-object-level) | §5.2 "Big storylines" — meta-labels without concrete object-level instances | 1 instance |
| AP-mental-model-out-of-context | §4.4 A.6.B presented without stating when it applies (conditions absent) | 1 instance |

---

## §10 BA-Cycle-lite (§3.5)

- **BA-0 Ethical surface?** No — this is a technical distillation doc, not a capital memo or public-facing claim doc. BA-0 = no.
- BA-Cycle-lite not required. Proceeding without BA-1..BA-3.

---

## §11 Recommended changes for brigadier (v2 construction)

Priority order (P1 = blocking for L1 audience):

**P1 — Structural split §4.**
Rename §4 to "§4a FPF-canonical mechanisms" (A.6.B / A.14 / B.3 only) + add "§4b Jetix-layer abstractions inspired by FPF (RUSLAN-LAYER; NOT Levenchuk's patterns)". IP-1/IP-2/IP-3/IP-7 move to §4b with bold per-section disclaimer.

**P1 — §6.3 synthesis declaration.**
Replace "synthesized from Spec + Readme" with: "По нашему пониманию Spec + Readme — наш разбор, не Левенчуковская формулировка." Add ClaimScope block: `holds_for_our_explication_purposes_only; structure not from Levenchuk`.

**P1 — Remove "Why FPF dropped the word 'alpha'".**
Replace with observable fact: "Слово 'alpha' в FPF-Spec.md не используется." Remove all interpretive motivation framing.

**P2 — Complete Eleven Pillars list (§5.3).**
Extract all 11 Pillars from FPF-Spec.md E.2 before publishing. Remove TO-COLLECT note.

**P2 — Per-claim F-G-R for §6.3 seven mechanisms.**
Add per-claim F-G-R: F: F3 (our synthesis) + G: Jetix-internal analysis + R: refuted_if_Levenchuk_provides_different_enumeration.

**P2 — Corpus snapshot update.**
Update corpus ref from `2026-04-20` to `c86eabd 2026-05-16`. Add E.10.SEMIO reference in §3.8.

**P3 — §2 "300+ patterns" count.**
Add FPF-Spec line ref for the count. If line ref unavailable, flag as "per Readme L9 approximate; exact count TO-VERIFY".

**P3 — Private TG citation note (§2).**
Add `[частное TG-сообщение, 2026-05-17]` to the inbox citation so source nature is clear.

---

## §12 Escalations

```yaml
escalations: []
```

No escalation required. All findings are within philosophy-expert critic domain. v2 is a brigadier write task — no HITL gate triggered (no ethical-surface-irreversible, no foundation revision, no out-of-domain).

---

## §13 Dissents

```yaml
dissents: []
```

No dissent within this single-expert critic invocation. All conformance check results are grounded in observable artefact content vs Popper/Kuhn/F-G-R rubric.

---

*Draft complete. Brigadier constructs v2 from §11 Recommended changes. Philosophy-expert does not write v2.*
