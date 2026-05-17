---
title: "Pre-flight critic — JETIX-WORKING-FILE-v0-2026-05-17.md design audit"
type: critic-pre-flight
mode: critic
expert: philosophy-expert
task_id: task-fpf-iwe-phase-b-2026-05-17
caller: brigadier Phase B Шаг 4
date: 2026-05-17
F: F4
G: philosophy-critic-internal
R: refuted_if_brigadier_integrated_v0_shows_none_of_predicted_hotspots_flagged_by_L1_reader
prose_authored_by: philosophy-expert (critic scribe; R1 posture — surface epistemic risks; no positioning for Levenchuk)
artefact_under_consideration: planned JETIX-WORKING-FILE-v0-2026-05-17.md (not yet written; critic is pre-flight design audit)
sources:
  - path: reports/jetix-vs-iwe-audit-2026-05-17.md
    range: "§0-§12 full"
  - path: reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md
    range: "§1-§14 full"
  - path: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language-v2.md
    range: "§0-§QR frontmatter + §0 freshness"
  - path: inbox/levenchuk-tg-2026-05-17.md
    range: "C1-C7 full"
  - path: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-fpf-tighten.md
    range: "§1-§13 full"
  - path: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-iwe-verify.md
    range: "§1-§9 full"
  - path: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-jetix-vs-iwe.md
    range: "§1-§11 full"
  - path: CLAUDE.md
    range: "§4.1 Tier 2 Constitutional + Foundation Architecture v1.0"
  - path: decisions/JETIX-CORPORATION-2026-05-05.md
    range: "frontmatter + §1 overview"
---

# Pre-flight Critic — JETIX-WORKING-FILE-v0 Design Audit

> **Constitutional posture.** R1 scribe + epistemic risk surface. This critic does NOT
> author positioning for Levenchuk. It audits the DESIGN of a document not yet written —
> identifying traps, F-G-R gaps, and hot spots BEFORE the document is drafted.
> Brigadier uses this to instruct the Шаг 4 writing cells.
> Per §1d decision-rights ritual: all writes to `swarm/wiki/drafts/` only.

> **Pre-flight context.** Phase B Шаг 4 goal: pack Jetix as a single navigable artefact
> for L1 reading (Tseren Tserenov). Brigadier integrates 3 cells: eng × scalability,
> mgmt × integrator, philosophy × critic (this cell). Canonical write belongs to brigadier.

---

## §1 Conformance Checklist — design-level checks against C1-C7 traps

≥8 binary checks (extended from standard ≥5 to cover all 7 trap categories):

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| CC-1 | **C1 overreach trap.** Working file design includes explicit «NOT FPF — Jetix specific» framing for every section that uses FPF-derived mechanisms. Predicate: design brief names a §4a/§4b structural split (canonical FPF vs RUSLAN-LAYER) visible at section-heading level, not only in sub-section inline text. | **REQUIRES ACTION** | Step 1 critic (`fpf-tighten.md §7`) found posture creep in three locations: §4 title confusion, §6.3 synthesis without boundary, §3.5 alpha-word interpretation. The working file design must INCORPORATE the §4a/§4b split from `01-fpf-on-human-language-v2.md` frontmatter as a structural discipline rule for every analogous section. The risk: any «Jetix has FPF-like mechanism X» sentence without explicit «RUSLAN-LAYER» or «Jetix-unique» tag triggers C1 reaction from Levenchuk. |
| CC-2 | **C2-C5 attribution discipline.** Every surface mechanism in the planned working file carries one of four explicit attribution tags: `[FPF-derivative]` / `[RUSLAN-LAYER]` / `[Jetix-unique]` / `[unknown-TBD]`. Predicate: design brief specifies that attribution tags are MANDATORY per mechanism row, not optional. | **REQUIRES ACTION** | `06-honest-self-audit.md §11` produces a 5-column attribution table (~39 components). The working file design must incorporate this table OR explicitly require per-mechanism tagging. Without tags, the working file will repeat the JETIX-FPF.md error (3762-line derivative claiming FPF authority). `[src: 06-honest-self-audit.md:233-239]` |
| CC-3 | **C5b symmetry check.** The working file design explicitly states that C5b-Jetix (F2 positioning until C4 Arm D runs) is NEVER stated as fact without C4 evidence. Predicate: design brief contains an explicit prohibition: «do not claim 'Jetix умнее' without C4 benchmark». | **REQUIRES ACTION** | `jetix-vs-iwe-audit.md §9 C5b-Jetix` establishes F2 grade for the comparative intelligence claim. The working file is for L1 reading (Tseren, who will share with Levenchuk). Any comparative intelligence claim without C4 evidence will trigger the same objection Levenchuk already raised in C3. `[src: reports/jetix-vs-iwe-audit-2026-05-17.md:223-229]` |
| CC-4 | **C6 Drucker trap (achievements ≠ hours/files).** The working file does NOT lead with volume metrics (5 months / 110 LOCKED docs / 166 H bank entries / 6 strategic insights). Predicate: design brief explicitly bans volume-leading as a proof-of-value pattern. Working file must lead with FUNCTIONAL demonstrations, not artefact counts. | **REQUIRES ACTION** | Levenchuk C6 verbatim: «затраченные часы не означают, что есть какие-то достижения, кроме сгенерированных AI файлов — даже если эти файлы проверены.» `[src: inbox/levenchuk-tg-2026-05-17.md:32]` Any section that leads with «we have 110 LOCKED docs» is a direct C6 trigger. Functional demonstration means: «what does Jetix DO that vanilla Claude does NOT, observable in 5 minutes» (Levenchuk's own test from C4). |
| CC-5 | **R12 surfacing protocol.** The working file design includes an explicit R12 surfacing protocol that (a) attributes R12 verbatim to its 4 sources, (b) does NOT present R12 as «Jetix's claim to superiority», and (c) frames it as a constitutional design choice, not a marketing differentiator. Predicate: design brief has a named R12 surfacing section with attribution list. | **REQUIRES ACTION** | `jetix-vs-iwe-audit.md §3 J-U2` confirms R12 is genuinely Jetix-unique (not in FPF, not in IWE). `CLAUDE.md §4.1 rule 12` gives verbatim sources: H7 People-NS LOCKED 2026-05-12 + Clan Charter + Game Theory M-C mechanism §11 + Q2 ack `reports/strategic-decisions-2026-05-12.md §2`. Without this attribution trail, R12 surfacing sounds self-aggrandizing. With it, R12 is traceable and credible. |
| CC-6 | **F-G-R discipline per section.** The working file design specifies that every non-trivial claim in the working file carries F + G + R triple footer or inline tag. Predicate: design brief names this requirement explicitly, and identifies which sections are likely to produce F2 claims that must be labeled F2 (not presented as F5+). | **REQUIRES ACTION** | Step 1 critic found 5 fail / 2 partial pass on F-G-R for doc 01. `fpf-tighten.md §6 F-G-R Audit Table`. The same failures will replicate in the working file unless the design brief proactively specifies F-G-R per section. Highest-risk sections (likely F2): any comparative intelligence claim, any «Jetix is smarter» framing, any market-claim about differentiation. |
| CC-7 | **Hot-spot prediction completeness.** Design brief requires a hot-spot register (≥5 predicted Levenchuk or Tseren objections) that must be addressed in the working file structure. Predicate: at least 5 hot spots with explicit falsifier per hot spot are defined before writing begins. | **REQUIRES ACTION** | Steps 1-3 produced a total of 5+5+6=16 hot spots across the three prior critic drafts. The working file design must absorb these or explain why they are not applicable. §5 below provides the consolidated hot-spot register for the working file specifically. |
| CC-8 | **Boundary discipline (§4a/§4b mirror for working file).** Every section of the working file that uses RUSLAN-LAYER constructs (IP-1, IP-2, IP-3, IP-7, Halt-Log-Alert, AWAITING-APPROVAL) explicitly disclaims these as Jetix-internal, not Levenchuk-attributed. Predicate: design brief identifies RUSLAN-LAYER sections vs canonical-FPF sections at the table-of-contents level. | **REQUIRES ACTION** | `fpf-tighten.md §7 Epistemic Posture Check` identified 3 posture-creep locations in doc 01. The working file will have analogous locations because it draws from the same Foundation v1.0 LOCKED material. The §4a/§4b structural discipline must be built into the working file TOC, not applied post-hoc. |

**Aggregate result:** 8/8 checks require action. The working file design, as inferred from available inputs, does not yet address these traps structurally. This is the expected state for a pre-flight critic — the purpose is to identify these before the document is written. Brigadier should convert each CC row into a design requirement for the Шаг 4 writing cells.

---

## §2 Acceptance Predicate (Hamel-binary)

```
acceptance_predicate:
  "JETIX-WORKING-FILE-v0 is ACCEPTED for L1 (Tseren) reading if:
   (1) every mechanism claim carries one of {FPF-derivative / RUSLAN-LAYER / Jetix-unique
       / unknown-TBD} attribution tag visible at section-heading or table-row level
       (not only in sub-section inline text), AND
   (2) no claim of the form 'Jetix is smarter than X' appears without explicit
       F2 grade label AND C4-benchmark-required disclaimer, AND
   (3) R12 surfacing cites all 4 verbatim sources: H7 People-NS + Clan Charter +
       Game Theory M-C §11 + Q2 ack reports/strategic-decisions-2026-05-12.md §2, AND
   (4) the document does NOT lead with volume metrics (hours / doc counts / H-bank count)
       as proof-of-value — functional demonstration leads, AND
   (5) ≥5 predicted hot spots from §5 below are structurally addressed
       (i.e. the section structure prevents each hot spot from firing, or explicitly
       acknowledges the limitation with falsifier)."
```

Currently NOT satisfied (document not yet written). This predicate is the gate condition
brigadier should apply before publishing the working file for L1 reading.

---

## §3 Alternatives (≥2 + status quo, each with kill-condition)

### Alternative A — «FPF mirror» style (heavy FPF grounding, Jetix as applied case)

Design: working file explicitly positions Jetix as «FPF-applied to a specific domain
(consulting business OS)». Each section mirrors FPF's §-numbering and mechanism vocabulary.
FPF-derivative sections use FPF identifiers (A.2, B.3, E.5 etc.). RUSLAN-LAYER sections
are in a clearly-separated appendix.

Kill-condition: This style fails if it looks like another attempt at JETIX-FPF.md
(3762-line derivative archived per `06-honest-self-audit.md §8`). The 72K-line FPF-Spec
makes this approach extremely difficult — any FPF-mirror will be incomplete and Levenchuk
will notice immediately. C1 reaction: «это не FPF, у меня один документ».

Verdict: NOT recommended for L1 reading. Appropriate only for internal FPF-integration
phase (Phase B technical work), not for the working file aimed at Tseren cooperation.

### Alternative B — «IWE mirror» style (Jetix framed as analogue to IWE for different scope)

Design: working file uses IWE vocabulary as the comparison anchor. Each Jetix mechanism
is compared directly to the IWE equivalent (or gap). Structure follows the Jetix-vs-IWE
audit format from `reports/jetix-vs-iwe-audit-2026-05-17.md`.

Kill-condition: This style fails because Tseren is IWE's author — he will immediately
detect any mischaracterisation of IWE. More critically, IWE and Jetix serve different
scopes (individual vs organisational) per `jetix-vs-iwe-audit.md §0`. Framing Jetix
as «IWE for organisations» is a category claim that requires IWE agreement.
D-PHIL-2 dissent: complementary vs gap-filling is unresolved.
`[src: reports/jetix-vs-iwe-audit-2026-05-17.md:44]`

Verdict: Viable as a SECTION (the Jetix-vs-IWE overlap table) but not as the working
file's primary framing.

### Alternative C — «Jetix-own» style (Jetix presented on its own terms + transparent gaps) — RECOMMENDED

Design: working file presents Jetix's own structure (Foundation v1.0 + Strategic Layer +
unique mechanisms) with explicit attribution tags (§4a/§4b split), honest capability
table (§8 of the audit template), and named gaps against Levenchuk bar. No claim of
FPF-equivalence or IWE-equivalence. Jetix-unique mechanisms (R12, Heptagon, 5-layer
memory, B2 mini-swarm, F-G-R Halt-Log-Alert) are named with verbatim sources.

Kill-condition: This style fails if the result reads as «we have some infrastructure
with nothing to show functionally» — the C6 trap. The functional anchor must be
demonstrated by citing what Jetix does that vanilla Claude does not (per Levenchuk's
own C4 test design: «grузите FPF AI-агенту — разница видна за пять минут»).

Verdict: RECOMMENDED. Honest scribe posture, transparent gap registry, Jetix-unique
surfaced with attribution, no false FPF or IWE authority claimed.

### Status quo (no pre-flight audit; write the working file directly)

Kill-condition: Status quo fails because without pre-flight audit, the working file will
repeat JETIX-FPF.md's overreach pattern (C1), lead with volume metrics (C6), and make
comparative intelligence claims without evidence (C5b). Three prior critic drafts
(Steps 1-3) collectively identified 16 hot spots that status quo leaves unaddressed.

---

## §4 Anti-scope

- This pre-flight critic is NOT producing the working file text — that is brigadier +
  writing cells (Шаг 4).
- This pre-flight critic is NOT deciding what Jetix IS strategically — that is Ruslan
  (HITL sole-strategist rule, CLAUDE.md §4.1 rule 1).
- This pre-flight critic is NOT arbitrating whether Jetix should adopt IWE or FPF
  deeper — that is instrumental Рациональность (investor-expert + Ruslan; FPF L1003-1006).
- This pre-flight critic is NOT authoring a response to Levenchuk — that is HITL prose.
- This pre-flight critic is NOT running an engineering review of the Foundation Parts —
  that is engineering-expert territory.
- This pre-flight critic is NOT evaluating the paid IWE platform (B2 blocker active).
- This pre-flight critic does NOT address capital allocation, subscription decisions,
  or ШСМ residency — investor-expert territory.

---

## §5 Hot-Spot Register — ≥5 predicted Levenchuk/Tseren objections for working file

Each hot spot carries: location-in-design / predicted reaction / falsifier for hot spot.

### HS-1 — «Jetix-корпорация с 110 документами» as lead claim

**Predicted location.** Any working file introduction that leads with «Foundation
Architecture v1.0 LOCKED 2026-04-28 — 10 Foundation Parts + 11 locked docs + 110 LOCKED
canonical documents».

**Predicted reaction (Levenchuk).** Direct C6 trigger: «затраченные часы не означают
достижений, кроме сгенерированных AI файлов». Doc count = C6 trap.

**Predicted reaction (Tseren).** A sophisticated IWE user who has read Levenchuk's
critiques of org-complexity will view 110 docs as overhead evidence, not achievement
evidence.

**Falsifier for hot spot.** Hot spot fires if brigadier's integrated working file
opens with «we have N documents / months of work» as the primary value claim.
Not fires if the opening demonstrates a functional capability
(e.g. «run this prompt with/without Jetix and see the difference in 5 minutes» —
Levenchuk's own C4 test).

**Design requirement.** Functional demonstration MUST precede volume metrics.
If volume metrics appear, they must be in an appendix or footnote, not the lead.

`F: F4 | G: risk-prediction | R: refuted_if_Tseren_does_not_flag_doc-count_lead`

---

### HS-2 — Attribution creep: RUSLAN-LAYER presented as FPF-canonical

**Predicted location.** Any section describing IP-1 Role≠Executor, AWAITING-APPROVAL
packets, Halt-Log-Alert, or Default-Deny without a «RUSLAN-LAYER» or «Jetix-internal»
header tag.

**Predicted reaction (Levenchuk).** «IP-1 — откуда? У меня нет такого термина в FPF.
Вы приписываете мне терминологию которой не существует.»

**Predicted reaction (Tseren).** A practitioner who knows FPF will recognize that
«IP-1», «AWAITING-APPROVAL», and «Halt-Log-Alert» are Jetix-specific constructs,
not FPF terms. If the working file presents them as if they were FPF-standard, trust
is damaged.

**Falsifier for hot spot.** Hot spot fires if «IP-1» or any Jetix-internal construct
appears in a section titled «FPF-based mechanisms» or equivalent without explicit
RUSLAN-LAYER disclaimer visible at the section heading.

**Design requirement.** §4a/§4b structural split from `01-fpf-on-human-language-v2.md`
must be replicated in the working file. Exact mirror: §4a = canonical FPF mechanisms
(A.6.B, A.14, B.3 only); §4b = Jetix-layer abstractions inspired by FPF (IP-1, IP-2,
IP-3, IP-7, Halt-Log-Alert, AWAITING-APPROVAL) with bold: «RUSLAN-LAYER only.
Эти термины не существуют в FPF-Spec».

`F: F4 | G: risk-prediction | R: refuted_if_both_Levenchuk_and_Tseren_read_the_file_without_flagging_IP-1`

---

### HS-3 — C5b-Jetix implicit: «Jetix умнее конкурентов» without C4 evidence

**Predicted location.** Any section describing Jetix's intelligence-amplification
mechanisms (Strategic Insights Hexagon, F-G-R per claim, 5-layer agent memory) that
concludes with a comparative superiority claim or implies Jetix is smarter than vanilla
Claude / IWE / competitor systems.

**Predicted reaction (Levenchuk).** «У вас непонятно — за счёт чего ваш Jetix умнее.
Вы ещё не показали разницу с vanilla AI-агентом.» — verbatim C3 restated.
`[src: inbox/levenchuk-tg-2026-05-17.md:26]`

**Predicted reaction (Tseren).** Tseren lives in the FPF ecosystem. He knows that
structural FPF-dependency (which Jetix has partially) does not automatically produce
intelligence amplification — it requires operational enforcement of FPF primitives
(which Jetix has partially, per `06-honest-self-audit.md §12`).

**Falsifier for hot spot.** Hot spot fires if working file contains any sentence of
the form «Jetix produces better results than vanilla AI / than competitor systems»
without an explicit F2 grade label AND «C4 benchmark pending» qualifier.

**Design requirement.** Every comparative-intelligence claim in the working file
must carry: `F: F2 | positioning | R: refuted_if_C4_Arm_D_scores_at_or_below_Arm_A`.
The working file should proactively include the C4 benchmark design (Arm A / B / C / D)
as an open question — demonstrating we know how to test, even if we have not tested yet.
`[src: inbox/levenchuk-tg-2026-05-17.md:53-58 C4 design]`

`F: F4 | G: risk-prediction | R: refuted_if_Levenchuk_accepts_F2_labeled_comparative_claim_without_objection`

---

### HS-4 — R12 surfacing sounds self-aggrandizing without attribution chain

**Predicted location.** Any section presenting R12 anti-extraction as a Jetix strength
without the verbatim 4-source attribution trail.

**Predicted reaction (Levenchuk).** If R12 is presented as «a principle we invented»
without grounding, Levenchuk will ask: «откуда? Это в FPF есть? В IWE есть?
Вы сами придумали — это не аргумент.»

**Predicted reaction (Tseren).** Tseren's IWE has fork-friendly data portability by
design (update.sh preserves extensions/), but no explicit constitutional norm.
He may interpret R12 as a claim that Jetix is constitutionally superior to IWE —
which is a comparative claim, not a description.

**Falsifier for hot spot.** Hot spot fires if R12 appears in the working file without
ALL FOUR of: H7 People-NS LOCKED 2026-05-12 + Clan Charter + Game Theory M-C §11 +
Q2 ack `reports/strategic-decisions-2026-05-12.md §2` in the same section.

**Design requirement.** R12 surfacing section must: (1) name all 4 sources; (2) state
the mechanism: «AI/substrate cannot extract value beyond agreed share; members can
fork-and-leave without penalty»; (3) explicitly note this is NOT in FPF nor in IWE
public template (per `jetix-vs-iwe-audit.md §3 J-U2`); (4) carry `F: F5 | G: comparison
| R: refuted_if_SPF_or_FPF_contains_equivalent_norm`.

`F: F4 | G: risk-prediction | R: refuted_if_R12_surfacing_with_4-source_attribution_not_flagged`

---

### HS-5 — «Honest gaps» section absent: Jetix presented only through its strengths

**Predicted location.** If the working file has no «where Jetix does NOT work /
where IWE works better» section, or if the «shared gaps vs Levenchuk bar» table from
the audit is absent.

**Predicted reaction (Levenchuk).** «Вы мне показываете только сильные стороны.
Это не доказательство. Покажите где вы хуже — тогда поверю честности.»
C3 critique is partly addressed by honest self-audit. Without surfacing the gaps,
the working file looks like marketing.

**Predicted reaction (Tseren).** A practitioner who has built IWE knows its own gaps
well. He will immediately see Jetix gaps that are not mentioned. Omitting them reads
as dishonest or uninformed.

**Falsifier for hot spot.** Hot spot fires if working file has no section equivalent
to `reports/jetix-vs-iwe-audit-2026-05-17.md §8.1 «Where IWE WORKS but Jetix doesn't»`
with ≥6 honest gap entries.

**Design requirement.** Working file MUST include an honest-gaps section with entries
covering at minimum: (a) no session-level OWC discipline (IWE I-U2 advantage);
(b) no memory TTL demotion (IWE I-U4 advantage); (c) no ArchGate 7-factor profile
(IWE I-U3 advantage); (d) C5b-Jetix unverified (no C4 benchmark yet); (e) JETIX-FPF.md
archived as overreach — «we tried full FPF derivative; it was wrong; current state is
lighter tactical adoption».
`[src: 06-honest-self-audit.md:192-198 §8.1; 06-honest-self-audit.md:183-198]`

`F: F4 | G: risk-prediction | R: refuted_if_Tseren_does_not_raise_absent_gaps`

---

### HS-6 — Working file does not navigate L1 reading path (not navigable as single artefact)

**Predicted location.** If the working file lacks explicit reading-path markers
(5-min / 15-min / 30-min paths or equivalent entry points) analogous to
`01-fpf-on-human-language-v2.md §QR-NAV`.

**Predicted reaction (Tseren).** L1 reader time is constrained. If the working file
requires a full linear read to extract value, it will not be read. Tseren will ask for
a summary — which is not what the working file is intended to produce.

**Predicted reaction (Levenchuk).** «Я не буду читать 200 строк чтобы найти суть.»

**Falsifier for hot spot.** Hot spot fires if the working file has no explicit
reading-path table (≤5 min entry point named; section-by-section map of what each
section unlocks for the reader).

**Design requirement.** Working file must have a navigation section (§QR-NAV equivalent)
at the top with ≥2 reading paths: «5-min: read §1 + §2 + §5-min-summary» and
«full: sequential with functional demo anchor».

`F: F3 | G: risk-prediction | R: refuted_if_working_file_is_short_enough_to_read_linearly_in_5min`

---

### HS-7 — C4 benchmark design absent: no falsifiable test offered

**Predicted location.** If the working file claims any form of intelligence
amplification without citing the C4 benchmark test design from `inbox/levenchuk-tg-2026-05-17.md`.

**Predicted reaction (Levenchuk).** «Вот FPF проверяется очень просто: грузите FPF
AI-агенту и спрашиваете про ваш проект... Разница видна за пять минут.»
`[src: inbox/levenchuk-tg-2026-05-17.md:26]`
Levenchuk has already provided a falsifiable test. A working file that does not
acknowledge this test looks like we are avoiding it.

**Falsifier for hot spot.** Hot spot fires if working file makes any
intelligence-amplification claim without citing the C4 Arm A/B/C/D benchmark design.

**Design requirement.** Working file must include: «Levenchuk's proposed test (verbatim):
[C4 quote]. Our C4 Arm design: Arm A = vanilla Claude; Arm B = FPF-loaded Claude;
Arm C = IWE-template-loaded Claude; Arm D = Jetix stack. Status: Phase B queue.
C5b-Jetix remains F2 / positioning until Arm D results available.»

`F: F4 | G: risk-prediction | R: refuted_if_Levenchuk_does_not_raise_missing_benchmark`

---

## §6 F-G-R Discipline Rubric — per planned working file section

Design specification: every section of the planned working file must carry the F-G-R
grade appropriate to its claim type. This rubric names the likely grade per section type
and identifies the highest-risk over-grading patterns.

| Planned working file section type | Appropriate F grade | Common over-grade risk | Design requirement |
|---|---|---|---|
| Verbatim Levenchuk quote citations (FPF mechanisms A.x, B.x) | F5-F8 (verbatim + line ref) | Over-graded if context is added without attribution | Cite FPF-Spec.md line + commit `c86eabd` for all FPF verbatim |
| Foundation v1.0 architecture description (Parts 1-11, LOCKED) | F5 (RUSLAN-ACK + LOCKED + git tag) | Over-graded if presented as «FPF-standard» | Tag each Part with RUSLAN-ACK bundle + date; note «Jetix-internal» |
| Comparison claim (Jetix has X / IWE has Y / gap) | F4 (design-declaration level) | Over-graded if presented as empirical outcome | Tag `F: F4 | G: comparison | R: refuted_if_...` |
| R12 anti-extraction (constitutional candidate) | F5 (4-source attribution) | Under-cited if one source is missing | All 4 sources required in same section |
| Intelligence-amplification claim for Jetix | F2 (positioning) | CRITICAL over-grade risk — frequently implied F5+ | MUST carry F2 label + C4-benchmark-required |
| Honest-gaps entries (where Jetix does not work) | F4 (self-audit level per `06-honest-self-audit.md` frontmatter) | No over-grade risk; these are honest | Cite `06-honest-self-audit.md` section for each gap entry |
| C4 benchmark design (Arm A/B/C/D) | F3 (design proposal, not executed) | Over-graded if presented as plan rather than proposal | Label «proposed benchmark; pending Phase B execution» |
| Jetix-unique mechanisms (R12, Heptagon, 5-layer memory, B2 mini-swarm, F-G-R Halt-Log-Alert) | F4-F5 (structural, RUSLAN-ACK) | Over-graded if comparative superiority is implied | Each unique must cite source + carry `R: refuted_if_...` |
| Shared gaps against Levenchuk bar (both Jetix + IWE fail) | F4 (parallel audit, brigadier-integrated) | No over-grade risk | Cite `jetix-vs-iwe-audit.md §8.4` for each shared gap |

**Critical over-grade pattern.** The most dangerous section is any comparative
intelligence claim. Per `06-honest-self-audit.md §12`, the honest read is:
«Jetix = memory + automation + ~25% structural-intelligence + ~10% FPF-derivative
— but missing full intelligence amplification layer.» If the working file presents
the ~25% structural-intelligence as if it were full intelligence amplification,
Levenchuk's C3 critique applies directly.

---

## §7 R12 Surfacing Protocol

R12 is confirmed Jetix-unique: not in FPF, not in IWE public template.
`[src: reports/jetix-vs-iwe-audit-2026-05-17.md:79 §3 J-U2]`
`[src: swarm/wiki/drafts/task-fpf-iwe-phase-b-2026-05-17-philosophy-critic-jetix-vs-iwe.md:321-334 §U-J2]`

To surface without self-aggrandizing, the working file MUST use this protocol:

**Step 1: Attribution-first framing.** R12 section opens with the attribution trail
before making any claim:
```
Sources: H7 People-NS LOCKED 2026-05-12 (commit 93b796d) +
         decisions/JETIX-FIRST-CLAN-CHARTER-2026-05-12.md +
         Game Theory M-C mechanism §11 +
         Q2 ack reports/strategic-decisions-2026-05-12.md §2
```

**Step 2: Mechanism before name.** Present the mechanism in plain language before
naming it R12:
«Substrate cannot extract value from members beyond agreed share. Members can
fork-and-leave without penalty. No lock-in. This is formalized as a constitutional
candidate rule (CLAUDE.md §4.1 rule 12).»

**Step 3: Meadows leverage level.** Name the level: «L2 system goals (Meadows).»
This is the appropriate vocabulary for an FPF-literate audience.
`[src: reports/jetix-vs-iwe-audit-2026-05-17.md:166-170 §7]`

**Step 4: IWE comparison honest.** «IWE has fork-friendly data portability by design
(update.sh preserves extensions/), but no explicit constitutional norm at Pillar C
equivalent level. R12 is Jetix-specific.»

**Step 5: F-G-R tag.** `F: F5 | G: comparison | R: refuted_if_SPF_or_FPF_contains_equivalent_norm`

**Why this protocol prevents self-aggrandizing.** It presents R12 as a mechanism
with traceable sources, not as «we are better». The distinction is: «here is what we
designed and why, with the sources that motivated it» vs «we have something superior».
The former invites peer discussion; the latter triggers defensive reaction.

---

## §8 BA-Cycle-lite (§3.5)

**BA-0 Ethical surface?** Partial. The working file is being prepared for L1 reading
(Tseren) with the goal of surfacing Jetix to the Levenchuk/IWE/ШСМ community.
This involves Ruslan's professional positioning. Not a capital memo; not a public claim
artefact yet. BA-0 = borderline.

**BA-1 Stakeholders.** (1) Ruslan — author/owner, professional reputation affected.
(2) Tseren — will read the document; his assessment of Jetix's FPF relationship affects
his willingness to collaborate. (3) Levenchuk — if Tseren shares the file.

**BA-2 Reversibility.** Once the working file is shared with Tseren, it cannot be
unshared. However it is a working file, not a public publication — the sharing is
controlled. Moderately reversible (can be revised; cannot be unread). NOT irreversible
in the strongest sense.

**BA-3 Via-negativa.** What we will NOT do in the working file:
- NOT claim FPF authority we do not have
- NOT lead with volume metrics as proof
- NOT make comparative intelligence claims without F2 label
- NOT present R12 as superiority rather than mechanism
- NOT omit the honest-gaps section

**BA-Cycle verdict.** BA-2 = NOT fully irreversible → no mandatory HITL escalation.
However, given the professional stakes (Ruslan's relationship with Levenchuk/Tseren
community), brigadier should flag the working file for Ruslan review before L1 sharing.
This is a «requires-approval» action per §1d decision rights, not an autonomous publish.

---

## §9 Specific AP codes predicted for the working file (if CC actions not taken)

| AP code | Predicted trigger location | Condition for triggering |
|---|---|---|
| AP-PHIL-1 (claim-without-falsifiability) | Any comparative intelligence claim without C4 benchmark reference | If working file states «Jetix produces better results» without falsifier |
| AP-PHIL-2 (paradigm-inconsistency-unflagged) | If FPF-derivative and RUSLAN-LAYER sections are merged without §4a/§4b split | If «Part 4 Role Taxonomy = FPF A.2» is stated without «also RUSLAN-LAYER IP-1 overlay» |
| AP-PHIL-3 (instrumental-vs-epistemic-collision) | Any section on «why Jetix, not IWE» that mixes epistemic classification with action recommendation | If working file says «Jetix has X therefore Ruslan should use Jetix» — instrumental invasion |
| AP-PHIL-5 (first-principles-without-method-declaration) | Jetix-unique mechanism sections that do not name Koen sotam | If R12 is stated as a principle without naming its derivation method (Game Theory M-C) |
| AP-PHIL-11 (meta-without-object-level) | «Jetix has structural-intelligence mechanisms» without a concrete functional demo | If §06 audit conclusion (~25% structural-intelligence) is cited without a specific object-level instance of intelligence amplification in action |
| AP-PHIL-6 (BA-Cycle-skipped) | If the working file is shared with Tseren without Ruslan review | BA-2 is borderline; sharing without owner review is a soft BA-6 trigger |

---

## §10 Residual open questions for brigadier integration

1. **Working file audience.** Is the working file for Tseren only, or also for potential
   future Levenchuk review? This affects how aggressively the §4a/§4b split must be
   enforced. Tseren is more forgiving of RUSLAN-LAYER terminology confusion than
   Levenchuk would be. Brigadier should specify audience in the working file frontmatter.

2. **C4 benchmark status.** Before the working file is shared, does Phase B include
   running C4 Arm A/B? Even running Arm A (vanilla Claude) vs Arm B (FPF-loaded Claude)
   — without Arm D (Jetix) — would demonstrate that we understand the benchmark design
   and have begun execution. This is more credible than «benchmark pending» alone.

3. **Working file scope boundary.** Does the working file include the strategic layer
   (Hexagon H1-H7, Clan Charter, €50K → €1T trajectory from `decisions/JETIX-CORPORATION-2026-05-05.md`)?
   If yes, these sections require explicit RUSLAN-LAYER labeling (Ruslan-authored strategic
   prose; AI is scribe, not author per CLAUDE.md §4.1 rule 1). If included, the
   `prose_authored_by:` field in each section must distinguish Ruslan-authored vs
   brigadier-scribed content.

4. **D-PHIL-1 resolution.** The template-vs-paid-platform IWE distinction (Dissent D-1,
   carried across all Steps) is unresolved. Before showing the working file to Tseren,
   Ruslan should confirm: do references to «IWE» in the working file mean the public
   template (GitHub ver 0.31.0) or the paid AI guide? Conflating them risks the same
   false-attribution problem as C1.

---

*Pre-flight critic draft complete.*
*Brigadier converts CC rows (§1) into design requirements for Шаг 4 writing cells.*
*Philosophy-expert does NOT write the working file.*
*All 8 CC checks require action — this is the expected state for a pre-flight audit.*
*10 dissents from Steps 1-3 carry forward per AP-6 (see §10 open question 4 re D-PHIL-1).*
