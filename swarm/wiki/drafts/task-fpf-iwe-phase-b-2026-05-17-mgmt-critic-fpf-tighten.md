---
title: "Critic Review — FPF на человеческом языке v1 (tighten for L1 audience)"
type: critic-review
produced_by: mgmt-expert
mode: critic
expert: mgmt-expert
cycle_id: cyc-fpf-iwe-phase-b-2026-05-17
task_id: task-fpf-iwe-phase-b-2026-05-17
artefact_reviewed: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md
audience_target: L1 (Левенчук, Цэрэн) + intelligent reader without FPF background
acceptance_criterion: "Любой intelligent человек читает v2 за 30 минут → понимает что есть FPF и как усиливает интеллект. Левенчук читает → не указывает на bullshit."
sources:
  - reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md
  - reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md
  - _L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md
  - inbox/levenchuk-tg-2026-05-17.md
provenance_inline: true
date: 2026-05-17
F: F5
G: mgmt-critic-draft
R: refuted_if_conformance_checks_incorrect_OR_alternatives_not_actionable
prose_authored_by: mgmt-expert (scribe; critique only; no primary FPF prose)
acceptance_test: fail
---

# Critic Review — FPF на человеческом языке v1

> **Mode gate confirmed.** mode: critic. Artefact-type: distillation.md (maps to «research item
> tied to revenue path» per §3.1 check 5 — this distillation is Phase B of the Левенчук
> engagement, which is Critical Path A1.2 in the Action Plan per
> `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §8`).
>
> **Anti-scope pre-declaration.** This critique does NOT evaluate FPF theory correctness
> (philosophy-expert scope). Does NOT compute cost/ROI of FPF adoption (investor-expert scope).
> Does NOT assess code artefacts (engineering-expert scope). It evaluates the v1 document
> on: time-to-utility for L1 audience, stakeholder fit, AP compliance, risk register, and
> v2 design proposals.

---

## §3.1 Conformance Checklist (≥5 binary checks)

Each check is a binary PASS / FAIL. Source citations are `[file:line-range]`.

---

### Check 1 — Time-to-utility at min 5 (skim): FAIL

**Predicate:** Within the first 5 minutes of skimming (= reading §1, §2, and scanning headers),
a reader unfamiliar with FPF can extract ONE concrete mental model — a single sentence that
explains what FPF is and what value it delivers.

**Verdict: FAIL.**

§1 opens directly with a verbatim English quote:
> «[FPF is an] operating system for thought…» `[01-fpf-on-human-language.md:24]`

That is a useful anchor. But the skim-path immediately falls apart:

- There is NO table of contents. A reader skimming a 462-line document has no navigation map.
  The first structural signal after §1 is §2 (one paragraph), then §3 which expands into 9
  sub-sections across ~190 lines. The reader skimming at min 5 has no idea whether §4, §5, §6
  are also required for the mental model or optional depth.
- The **elevator paragraph (§2)** — the single highest-leverage element for a skim reader — is
  buried 20 lines in and not labeled as such. It reads as a dense technical paragraph, not a
  "this is the 30-second version" marker.
- Левенчуковский C4 benchmark claim («разница видна за пять минут сравнений»
  `[inbox/levenchuk-tg-2026-05-17.md:53]`) is completely absent from v1. A reader who arrived
  here **because** of Левенчук's TG message gets no acknowledgment of that framing at min 5.

**Required delta for v2:** Add TOC (≤10 lines) at top. Label §2 explicitly as
«30-секундная версия». Add a single-line teaser before the TOC: «За 5 минут — §1+§2.
За 15 минут — §3+§6. За 30 минут — весь документ + ссылки.» Reading-time signposting
is the highest-leverage edit for the skim path.

---

### Check 2 — Time-to-utility at min 15 (dive): PARTIAL PASS (counts as FAIL for L1)

**Predicate:** At minute 15, the reader who dives into the intelligence amplification section
(§6) can articulate the 7-step mechanism in their own words and understand WHY this is
different from "vanilla AI".

**Verdict: FAIL for L1 specifically.**

§6.3 «The actual mechanism» is the strongest section in v1. The 7-step enumeration with
before/after framing («Без этого / С этим») is concrete and well-grounded
`[01-fpf-on-human-language.md:419-433]`. For a general intelligent reader this is sufficient.

For **Левенчук specifically**, it fails on one critical point: the section is titled
«synthesized from Spec + Readme» — meaning it is a synthesis, not verbatim. Левенчук's C3
critique says Jetix can't demonstrate intelligence amplification beyond vanilla AI
`[inbox/levenchuk-tg-2026-05-17.md:48]`. A synthesis that is not clearly anchored to Spec
line numbers risks triggering «это ваша интерпретация, не FPF» — the exact C1 sensitivity
`[inbox/levenchuk-tg-2026-05-17.md:41]`.

**Additional failure:** §6.4 contains the most important verbatim quotes from Spec (L499,
L513, L674) but they are placed AFTER the 7-step mechanism. For a reader building trust
in scribe-mode fidelity, the verbatim anchors should lead, not follow. A 15-minute diver
who stops at §6.3 misses the best verbatim grounding.

**Required delta for v2:** Move §6.4 verbatim quotes to open §6 (before the mechanism steps).
Every mechanism step in §6.3 should have its Spec line number in the same line, not just the
section header.

---

### Check 3 — Anti-AP-1: no summary-compression that erases nuance: FAIL

**Predicate:** No section collapses a multi-dimensional FPF concept into a single claim that
loses load-bearing nuance for L1 readers.

**Verdict: FAIL on §4 IP-mapping.**

§4 covers IP-1 / IP-2 / IP-3 / IP-7 / A.6.B / A.14 / B.3. But the treatment of IP-2, IP-3,
and IP-7 (§4.2, §4.3, §4.7) explicitly acknowledges: «Не Левенчуковский pattern; наш Bundle
1 IP-2» `[01-fpf-on-human-language.md:272]` — and then maps them to approximate FPF equivalents.

For a general intelligent reader, this is confusing. For Левенчук, this is a bullshit signal:
the document announces it will cover «IP-1 / IP-2 / IP-3 / IP-7 / A.6.B / A.14 / B.3» in
the prompt-driven §4 header but then reveals partway through that IP-2, IP-3, IP-7 are
**Jetix-internal terms** mapped onto FPF equivalents — not FPF mechanisms at all. This
compression erases the nuance that the reader is reading a partial mapping of Jetix
conventions onto FPF vocabulary, not a description of FPF mechanisms.

**Specific offending passage:** `[01-fpf-on-human-language.md:271-283]`
> «§4.1 IP-1 Role≠Executor… Source. Не explicit pattern ID в Spec — это RUSLAN-LAYER IP-1…»
> «§4.2 IP-2 (наш термин для Foundation gate)… Не Левенчуковский pattern; наш Bundle 1 IP-2»
> «§4.3 IP-3 / IP-7 (наши)»

These three subsections collapse into «here is how we map our concepts to FPF» — which
is legitimate Phase B analysis, but misleadingly framed under «Core mechanisms FPF» header.
Левенчук explicitly knows C1: «ваш JETIX-FPF.md — это наша интерпретация, не FPF»
`[inbox/levenchuk-tg-2026-05-17.md:42]`. If he reads §4 and sees IP-2/IP-3/IP-7 labeled
as FPF mechanisms, this is a guaranteed bullshit trigger.

**Required delta for v2:** Split §4 into two clearly labeled sub-sections:
(a) «FPF canonical mechanisms» (IP-1 re-labeled as A.2/A.13; A.6.B; A.14; B.3 only);
(b) «Как наши паттерны (Jetix IP-2/IP-3/IP-7) соответствуют FPF эквивалентам» — clearly
marked as mapping, not FPF description. OR: drop IP-2/IP-3/IP-7 from v2 entirely and
surface only canonical FPF mechanisms.

---

### Check 4 — Anti-AP-25: every section has a clear "что reader unlock'нул" promise: FAIL

**Predicate:** Each major section (§1–§7) opens with or closes with an explicit one-line
statement of what the reader can DO with the content: a mental model, a decision, an action.
Sections that end without a "what now" signal are AP-25 candidates.

**Verdict: FAIL on §3, §4, §5.**

- **§3** (9 sub-sections, ~190 lines) closes with §3.9 «Additional FPF primitives (briefly)»
  — a bullet list of terms with no synthesis statement. A reader finishing §3 has absorbed
  9 definitions without a «you now have X» payoff signal `[01-fpf-on-human-language.md:241-249]`.

- **§4** closes with §4.7 «IP-7 (наш — escalation)» — one short paragraph with «не explicit
  Левенчуковский» `[01-fpf-on-human-language.md:316-318]`. No unlock statement.

- **§5** closes with the methodology lineage table and a pointer to §04-methodology-lineage.md
  `[01-fpf-on-human-language.md:382]`. No synthesis of «what the 7 core ideas collectively
  enable», just a list with a "see companion file" pointer.

The document does NOT carry an explicit «30-second elevator» card at the top, nor a
«quick-reference card» at the end, which means a reader who wants to test comprehension
has no structured exit artifact. This directly blocks the acceptance criterion
«за 30 минут понимает что есть FPF и как усиливает интеллект» — understanding requires
an exit artifact, not just reading.

**Required delta for v2:** Each section (§1–§6) closes with one line in bold:
«Читатель после этого раздела может: [concrete mental model / action / question].»
End of document: add a «Quick-Reference Card» (≤20 lines) with: 1 elevator sentence,
7 intelligence-amplification mechanisms in one word each, 3 verbatim Левенчуковских
quotes that anchor the reader.

---

### Check 5 — Lock-14 / revenue-path tie (research item tied to revenue path): PASS

**Predicate:** The research distillation ties to a Jetix revenue path or critical-path
action per CLAUDE.md project priorities.

**Verdict: PASS.**

Phase B Phase A distillation is explicitly connected to Critical Path A1.2 (Левенчук as
Tyson-mentor candidate) and to the C4 benchmark which anchors the «quick-money consulting»
positioning (`_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §8`). The `00-SUMMARY-FOR-RUSLAN.md`
explicitly connects this to Phase B actions including «Integration plan FPF → Jetix» and
«Draft Ruslan-authored response to Левенчук» `[00-SUMMARY-FOR-RUSLAN.md:149-153]`.
Revenue-path tie is adequate for a Phase B research document.

---

### Check 6 — Risk: wrong tone (defensive vs neutral scribe): PARTIAL PASS (borderline)

**Predicate:** The document reads as neutral scribe, not as Jetix defending itself against
Левенчуковский C3 critique. No passages could be read as motivated reasoning.

**Verdict: PARTIAL PASS with one flagged passage.**

The document maintains scribe posture well through §1–§5. The constitutional note at top
`[01-fpf-on-human-language.md:16-18]` is clean. The §7 «Что мы НЕ вытащили» section is
honest and well-structured.

**Flagged passage:** §6.4, last paragraph `[01-fpf-on-human-language.md:446]`:
> «Левенчуковский C3 («ваш scope = «память+автоматизация» = vanilla AI») целится в то что
> наша Foundation v1.0 + Wiki v2 + skills focus на storage + retrieval + delegation…»

This paragraph shifts from FPF description to Jetix self-analysis. In a document whose
stated purpose is to explain FPF to an external reader, this passage introduces Jetix
internal framing mid-explanation. For Левенчук reading v2, this is a tone risk: it looks
like the document is trying to rehabilitate Jetix's position while describing FPF. The
passage belongs in a separate Jetix-self-audit document (which `06-honest-self-audit.md`
already is), not in the FPF explanation document.

**Required delta for v2:** Remove the «Левенчуковский C3 целится» paragraph from §6.4.
If the document is «FPF на человеческом языке», it must stay on FPF. The
self-audit framing goes to `06-honest-self-audit.md` only.

---

### Check 7 — Freshness acknowledgment (E.10.SEMIO / A.6.P active upstream): FAIL

**Predicate:** The document acknowledges that FPF is actively evolving (latest upstream commit
2026-05-16 per `00-SUMMARY-FOR-RUSLAN.md`), that E.10.SEMIO campaign is active, and that the
distillation is a Phase A snapshot with known gaps.

**Verdict: FAIL.**

§7 «Что мы НЕ вытащили Phase A» `[01-fpf-on-human-language.md:450-458]` is honest about
gaps but uses internal research-task language («TO-COLLECT Phase B»). For a reader who is
not familiar with Jetix's Phase A/B terminology, this reads as opaque project management
jargon, not as a legitimate epistemic acknowledgment.

More critically: the document has **no freshness note at the top**. The FPF upstream HEAD
was `c86eabd 2026-05-16` per `00-SUMMARY-FOR-RUSLAN.md` — one day before this distillation.
E.10.SEMIO is named in §7 but not explained. A.6.P (active development cluster per LJ post
1788706) appears only in §4.4 buried in a technical paragraph.

Левенчук is the author of FPF. If he reads a document about his framework and it doesn't
acknowledge that the document is based on a specific commit and may not reflect the latest
upstream changes, this is a credibility gap. Given Левенчуковский C1 sensitivity about
canonic vs interpretive sources, a freshness note is non-optional.

**Required delta for v2:** Add at the top, after constitutional posture note:
«Snapshot: FPF upstream HEAD `c86eabd` 2026-05-16. Активные dev-ветки: E.10.SEMIO campaign
(2026-05-16), A.6.P Compression-Decompression. Этот документ = Phase A distillation;
упомянутые пробелы в §7 будут addressed в Phase B.»

---

## §3.2 Acceptance Predicate (Hamel-binary, single line)

The v2 artefact passes this predicate when ALL of the following hold simultaneously:

**«v2 содержит: (1) TOC + reading-time map ("за 5 мин / 15 мин / 30 мин") в первых 20
строках тела; (2) §2 явно помечен как «30-секундная версия»; (3) §4 разделяет FPF-canonical
mechanisms от Jetix-internal IP-2/IP-3/IP-7 mapping с явными метками; (4) §6.3 каждый шаг
механизма имеет Spec line-number в той же строке; (5) §6.4 не содержит Jetix-self-analysis
абзацев; (6) freshness note с FPF commit hash и датой стоит ДО §1; (7) каждая основная
секция §1–§6 закрывается одной bold-строкой "Читатель после этого раздела может: [X]";
(8) Quick-Reference Card ≤20 строк стоит в конце документа.»**

This predicate is currently **NOT satisfied** by v1. Failing items: (1), (2), (3), (4),
(5), (6), (7), (8). Only check (3) is partially handled but not cleanly separated.

---

## §3.3 Alternatives + kill-conditions (≥2 + status quo)

### Alt A: Surgical patch of v1 (minimal edit, preserve structure)

**Description:** Apply only the 8 deltas from §3.2 predicate items without restructuring.
TOC added, §4 split labeled, §6.4 cleaned, freshness note added, Quick-Ref Card appended,
section-exit lines added. Estimated edit volume: 40–60 lines delta.

**Kill-condition:** If post-edit, a test reader (Ruslan reading as Левенчук proxy) still
can't articulate the 7-step mechanism in 15 minutes → v1 structure is fundamentally wrong
and Alt C needed.

**Confidence:** High for addressing identified failures. Moderate for L1 acceptance (Левенчук
may surface deeper theoretical issues once navigation is fixed — the document may pass
AP-25 but still fail Левенчуковский «bullshit» test on IP-2/IP-3/IP-7 framing).

### Alt B: Restructure around the reader's clock (30 / 15 / 5 minute layers)

**Description:** Rebuild v2 as three concentric layers:
- Layer 1 (5 min): §1 + §2 + Quick-Ref Card — everything the reader needs for party
  conversation about FPF.
- Layer 2 (15 min): §6 (intelligence amplification mechanism) — everything needed to
  evaluate FPF vs vanilla AI.
- Layer 3 (30 min): §3 + §4 + §5 — full primitive/mechanism detail for practitioners.

§7 (gaps) moves to a separate footnote file to keep the body under 350 lines.

**Kill-condition:** If target audience for v2 includes Левенчук as primary reader (not just
one of several), and Левенчук reads Layer 2 before Layer 3, he may not see the primitive
definitions and ask «где определения холона?» → restructuring fails for L1 depth use.

**Confidence:** High for general intelligent reader. Medium for Левенчук (he reads deep,
not skims; the layered structure may read as «popular science» to him which is its own risk).

### Alt C: Split into two documents (popular + technical)

**Description:** v2a = «FPF за 5 минут» (≤30 lines: elevator + 7 mechanisms + Quick-Ref).
v2b = «FPF: подробный разбор» (current v1 with patches from Alt A). Links between them.

**Kill-condition:** If Левенчук receives v2a without v2b link and reads it as the complete
distillation → risks triggering C3 («поверхностно»). If the two documents diverge in content
under separate editing → provenance drift.

**Confidence:** High for separation of concerns. Requires brigadier coordination to ensure
both documents are promoted together.

### Status quo: v1 as-is

**Kill-condition:** Immediate — acceptance test fails (7 of 8 predicate items unmet). Status
quo is not viable for the Phase B acceptance criterion.

---

## §3.4 Anti-scope

This critique is NOT:
- Evaluating FPF theory correctness or theoretical fidelity of the distillation → philosophy-expert × critic scope.
- Computing unit-economics of FPF adoption for Jetix → investor-expert × critic scope.
- Critiquing the mermaid diagram files in `diagrams/` (separate artefacts, not under review) → this task's scope is 01-fpf-on-human-language.md only.
- Assessing code artefacts or system architecture in the FPF spec → engineering-expert × critic scope.
- Strategizing how Ruslan should respond to Левенчук → HITL scope (Tier 2 R1).
- Producing v2 prose — brigadier integrates and writes based on this critique.

---

## §3.5 Stakeholder map (reader-as-stakeholder)

Three distinct reader profiles with distinct needs and failure modes:

### Stakeholder A — Левенчук (primary L1 risk)

**Profile (from `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §2.7`):**
- 67-68 лет; chemical faculty background re-trained into systems engineering.
- Daily LiveJournal writer since early 2000s. High content density, low tolerance for vague.
- «Не любит: pitchy / vague messages без методологического хука; startup-flavored инициативы
  без проверенной методологии; общие слова без артефактов.»
- He wrote FPF. He knows every primitive by heart. He will detect any mischaracterization
  of a mechanism immediately.

**What he needs from v2:**
- Scribe fidelity: every claim traceable to Spec/Readme line.
- No Jetix self-promotion mixed into FPF description.
- Explicit acknowledgment that this is a snapshot, not exhaustive.
- Recognition of active development clusters (E.10.SEMIO, A.6.P).

**Primary failure mode in v1:** IP-2/IP-3/IP-7 labeled under FPF mechanisms (Check 3).
He will read §4.2 «Не Левенчуковский pattern; наш Bundle 1» and the credibility of the
entire document collapses. The «bullshit» trigger fires at this exact point.

**Accountability (single-named):** Ruslan (author of v2; per Tier 2 R1 «AI does NOT make
strategic decisions»; the document is strategic communication to a critical-path mentor).

### Stakeholder B — Цэрэн (secondary L1; production applicability)

**Profile (from `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md §1.4`):**
- 54; мехмат МГУ; active Claude Code / n8n / MCP builder 2026.
- «#1 значимое слово 2026: claude.» Sees AI as augmentation / exocortex substrate.
- Requires: methodological rigor AND production applicability.

**What he needs from v2:**
- The 7-step intelligence amplification mechanism maps to something he can instantiate
  in Claude Code agents (he already builds Claude agents; «за счёт чего его IWE умнее
  конкурентов» `[inbox/levenchuk-tg-2026-05-17.md:28]`).
- A connection between FPF primitives and operational agent design (bounded context,
  role≠executor, alpha-state-graph).

**Primary failure mode in v1:** §6.3 mechanism steps are clear but do NOT connect to
agent implementation patterns. For Цэрэн the question is «как это делается в коде /
агентной конфигурации», and v1 has no answer to that. This is a Phase B gap, acceptable
in Phase A distillation — but v2 should acknowledge it.

### Stakeholder C — «Любой intelligent человек без FPF background»

**Profile:** Per Phase B acceptance criterion.
- No exposure to ШСМ/МИМ/FPF vocabulary.
- 30-minute budget.
- Goal: walk away with ONE usable mental model.

**What they need from v2:**
- Navigation map (TOC + reading-time signal).
- §2 clearly marked as the «enough for now» version.
- §6 clearly marked as the «real payoff section».
- Quick-Ref card at end to consolidate retention.

**Primary failure mode in v1:** Zero navigation infrastructure. No TOC, no reading-time
signals, no section-exit unlock statements. Reader finishing §3.1 (U.Holon definition) has
no idea whether this is 10% or 40% of the document.

---

## §3.6 Risk register

| Risk | Probability | Impact | Trigger | Mitigation in v2 |
|---|---|---|---|---|
| **R1 — Bullshit trigger on IP-2/IP-3/IP-7** | HIGH | HIGH | Левенчук reads §4.2-§4.3; sees «наши термины» under «FPF mechanisms» header | Separate §4 into canonical-FPF vs Jetix-mapping clearly labeled; or remove IP-2/IP-3/IP-7 from v2 entirely [src: Check 3; C1 sensitivity `inbox/levenchuk-tg-2026-05-17.md:41`] |
| **R2 — «Слишком длинно» — skipped** | MEDIUM | HIGH | v2 is still 400+ lines; Левенчук reads first 20 lines and stops | TOC + reading-time map at top; «5-minute path: §1+§2+Quick-Ref only» explicit signal [src: Check 1; `_L1-PROFILES §2.7`] |
| **R3 — Tone drift: reads as Jetix self-defense** | MEDIUM | HIGH | §6.4 last paragraph (`L446`) surfaces Jetix internal framing mid-FPF description | Remove §6.4 Jetix-analysis paragraph; restrict §1-§6 to FPF-only description [src: Check 6] |
| **R4 — Freshness gap triggers «не актуально»** | LOW | MEDIUM | Левенчук knows E.10.SEMIO is active (he's authoring it); distillation doesn't acknowledge it | Add freshness note with commit hash + active dev cluster names before §1 [src: Check 7] |
| **R5 — §3 definitions without payoff → reader lost** | MEDIUM | MEDIUM | General reader hits §3's 9 sub-sections (~190 lines) and loses thread | Section-exit «unlock» lines per §3.4 requirement; or re-order §3 after §6 (reader gets mechanism first, then primitives) |
| **R6 — §6.3 mechanism not anchored to Spec lines** | LOW | HIGH for Левенчук | Левенчук challenges «откуда именно в Spec?» for each step; synthesis without line anchors = «ваша интерпретация» | Add Spec line number per mechanism step in §6.3 [src: Check 2] |

---

## §3.7 v2 Design proposals (concrete deltas)

These are concrete structural deltas for brigadier to implement. Not prose — structural changes.

**Delta D1 — Freshness note + commit hash (before §1).**
Insert before constitutional posture note:
`Snapshot: FPF HEAD c86eabd 2026-05-16. Active dev clusters: E.10.SEMIO (semiotic campaign),
A.6.P (compression-decompression). Phase A distillation; gaps enumerated in §7.`

**Delta D2 — TOC + reading-time map (after frontmatter, before §1).**
≤12 lines. Sections §1–§7 + Quick-Ref. Column: estimated reading time per section.
Format: «§1 (1 мин) / §2 (2 мин) / §3 (10 мин, optional deep) / §4 (5 мин) / §5 (4 мин)
/ §6 (8 мин, KEY) / §7 (2 мин) / Quick-Ref (1 мин читать; keep permanently)»

**Delta D3 — Label §2 as 30-second version.**
Change §2 header to:
`## §2 FPF в одном абзаце (30-секундная версия — достаточно для старта)`

**Delta D4 — Split §4 into canonical / mapping.**
Rename §4 header:
`## §4 Core mechanisms FPF — canonical`
Add new sub-section before §4.1:
`### §4.0 Что входит / что нет`
One-paragraph note: «§4.1 (A.2/A.13), §4.4 (A.6.B), §4.5 (A.14), §4.6 (B.3) = canonical
FPF patterns. §4.2–§4.3 и §4.7 = наши внутренние IP-2/IP-3/IP-7 и их приближённые
FPF-эквиваленты — это Jetix-internal mapping, not FPF description. Перемещены в
06-honest-self-audit.md §X для чистоты.»
Then remove §4.2, §4.3, §4.7 body from v2 and move content to `06-honest-self-audit.md`.

**Delta D5 — Spec line numbers per §6.3 mechanism step.**
Each of the 7 steps in §6.3 currently ends with a pattern code. Add the primary Spec line
reference: e.g. step 1 «Bounded-context map (A.1.1) `[FPF L444-451]`» — the line range is
already in §3.2 `[01-fpf-on-human-language.md:73]` and can be cited here directly.

**Delta D6 — Remove §6.4 Jetix-analysis paragraph.**
The paragraph beginning «Не "память" и не "автоматизация"…»
`[01-fpf-on-human-language.md:446]` is moved to `06-honest-self-audit.md`.
§6.4 ends after the three verbatim Spec quotes (L499, L513, L674).

**Delta D7 — Move §6.4 verbatim quotes to open §6.**
The three verbatim quotes from Spec (L499, L513, L674) in §6.4 become the opening of §6,
before §6.1. Rationale: establish verbatim grounding before the synthesized mechanism;
reader trust is higher when verbatim comes first.

**Delta D8 — Section-exit unlock lines.**
After each of §1–§6, add one line in bold:
Example for §2: «**Читатель после §2 может:** объяснить коллеге что такое FPF в одном
абзаце и почему это не очередной Agile/Scrum.»
Example for §6: «**Читатель после §6 может:** описать разницу между vanilla AI и
FPF-loaded AI на конкретном примере — и предложить C4-тест за 5 минут (per Левенчуковский
benchmark `[inbox/levenchuk-tg-2026-05-17.md:53]`).»

**Delta D9 — Quick-Reference Card at document end (≤20 lines).**
Structure:
```
## Quick-Reference: FPF в 20 строках

**В одной фразе:** [§1 quote]
**В одном абзаце:** [§2 opening sentence]

**7 механизмов intelligence amplification:**
1. Bounded-context map → нет context drift
2. Role-method signature → accountability traceable
3. Alpha-state graph → machine-checkable status
4. F-G-R per claim → audit trail of trust
5. DRR → rationale preserved after team rotation
6. Abductive loop → portfolio of alternatives
7. MVPK → one reality, multiple aligned outputs

**3 Левенчуковских ключевых цитаты:**
— «FPF turns raw intelligence into work that is easier to align, review, evolve, and delegate.» [Readme L132]
— «A generative architecture for thought… making entire classes of errors difficult or impossible to commit in the first place.» [Spec L499]
— «Coordination, not raw generation, becomes the bottleneck.» [Readme L165]

**Canonical source:** https://github.com/ailev/FPF (FPF-Spec.md + Readme.md)
**Snapshot:** c86eabd 2026-05-16
```

---

## Summary of required v2 deltas (9 deltas, ranked by leverage for L1 acceptance)

| # | Delta | Rank (leverage) | Blocks which predicate item |
|---|---|---|---|
| D4 | Split §4 canonical/mapping | 1 (CRITICAL — bullshit trigger R1) | Predicate item (3) |
| D1 | Freshness note + commit hash | 2 (credibility with author) | Predicate item (6) |
| D6 | Remove §6.4 Jetix-analysis para | 3 (tone risk R3) | Predicate item (5) |
| D2 | TOC + reading-time map | 4 (skim failure R2) | Predicate item (1) |
| D3 | Label §2 as 30-sec version | 5 (skim utility) | Predicate item (2) |
| D7 | Move §6.4 verbatim quotes to open §6 | 6 (scribe fidelity for Левенчук) | Predicate item (4) |
| D5 | Spec line numbers in §6.3 | 7 (scribe fidelity; R6) | Predicate item (4) |
| D8 | Section-exit unlock lines | 8 (general reader utility) | Predicate item (7) |
| D9 | Quick-Reference Card at end | 9 (retention + skim recovery) | Predicate item (8) |

D4 + D1 + D6 are the minimum viable v2 for Левенчуковского bullshit-avoidance.
All 9 are required for full acceptance predicate satisfaction.

---

*Critique complete. Brigadier integrates this draft with parallel expert returns before dispatching v2 composition.*
