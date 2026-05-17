---
title: "engineering × critic — 01-fpf-on-human-language.md v1 → v2 tighten"
type: critic-review
mode: critic
expert: engineering-expert
task_id: task-fpf-iwe-phase-b-2026-05-17
artefact_path: reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md
cycle_id: cyc-fpf-iwe-phase-b-2026-05-17
date: 2026-05-17
F: F5
G: engineering-critic-output
R: refuted_if_spec_line_numbers_verified_correct_in_current_snapshot
prose_authored_by: claude (engineering-expert, scribe mode; per §1a constitutional posture)
---

# engineering × critic — FPF distillation tighten pass

> **Mode: critic.** Artefact under review: `reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md`
> (462 lines, Phase A v1 baseline). Brigadier integrates this return to write v2.
> This critic does NOT write v2.

---

## §3.1 Conformance Checklist (8 binary checks)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | **Navigability — extractable structure ≤5 min** | FAIL | No top-of-document quick-reference card. Sections §1..§7 have no summary table of (primitive → section → pattern-ID). A sophisticated reader opening cold must read all 462 lines to locate the API surface. No "start here" anchor. |
| 2 | **Deep-module locality — concepts isolated per section, no cross-section leak** | PARTIAL FAIL | §3.7 Стратегирование (line 186-219) and §3.8 Мышление письмом (line 222-238) are ШСМ primitives correctly, but §4.1–§4.7 mixes Левенчуковский IP patterns (IP-1, IP-2) with Jetix-internal RUSLAN-LAYER naming (which is NOT an FPF pattern). This leaks two distinct namespaces — Левенчуковский vs Jetix — into the same `##` section without a visible boundary marker. A L1 reader (Anatoly, Tseren) will be confused: "Is IP-1 from FPF or from Jetix?" |
| 3 | **Interface vs implementation — "API surface" (5 primitives + 7 mechanisms + 10 steps) legible without prose burial** | FAIL | The 5 primitives are scattered across §3.1–§3.9 without a consolidated interface table. §6.3 lists 7 mechanisms inline but does not surface them as a named list at top level. The 10-step workflow is in diagram `02-intelligence-amplification-workflow.md` but the doc body §6.3 lists only 7 and does not cross-reference the diagram explicitly by filename. The interface is buried in implementation prose. |
| 4 | **Provenance density — every non-trivial claim carries a [src:path:line]** | FAIL | Three specific provenance failures: (a) §1 cites `FPF-Spec.md L738` for "Purpose – an operating system for thought" — actual line in current spec (c86eabd) is L831; (b) §6.2 cites `FPF-Spec.md:700-708` for the Pareto frontier passage — actual line in current spec is L793; (c) §6.1 cites `Readme.md L165-171` for the "Because coordination…" list — actual line start is L167, section header is at L165. These are stale line numbers from the 2026-04-20 vendored snapshot, not the current c86eabd spec (+10K lines delta per CHANGELOG). Non-trivial claims in §3.2 (`FPF L444-451`), §3.5 (`A-fpf-spec-5-primitives.md`), and §5.2 carry single-file references with no line range — insufficient for F5-grade artefact. |
| 5 | **Code-likeness / structural integrity — tables consistent, mermaid referenced, no dangling links** | PARTIAL FAIL | Three findings: (a) diagram files (`diagrams/01-fpf-top-level-architecture.md`, `diagrams/02-intelligence-amplification-workflow.md`) are referenced in §00-SUMMARY but NOT explicitly linked from the body of `01-fpf-on-human-language.md` — §6.3 describes the 7-mechanism list without saying "see `diagrams/02-…`"; (b) §3.9 cross-references `02-u-episteme-and-iwe.md` inline ("DETAILS в `02-u-episteme-and-iwe.md`") — correct, but it's the only cross-ref to a companion file; the other 4 companion files go unreferenced from this doc; (c) §5.3 Eleven Pillars table is incomplete ("TO-COLLECT Phase B") — acceptable as a v1 gap but surfaces an interface gap that v2 must close or explicitly fence. |
| 6 | **v2 additions scoped correctly — (a) inline mermaid pointers, (b) quick-reference card, (c) inline glossary** | FAIL (v2 additions absent, as expected from v1) | v1 carries none of the three Phase B additions. This check documents the gap for v2 design. Absence in v1 = expected; absence in v2 = Conformance failure. |
| 7 | **Namespace contamination — Jetix-internal terms clearly fenced from Левенчуковский FPF terms** | FAIL | §4.1 "IP-1 Role≠Executor" is explicitly labeled "Не explicit pattern ID в Spec — это RUSLAN-LAYER IP-1 в Bundle 1 RUSLAN-ACK 2026-04-28 (см. CLAUDE.md §4.2)." §4.2–§4.3 are similarly labeled as "наш термин" / "наши". For L1 reader Anatoly Levenchuk this is confusing: the document is titled "FPF на человеческом языке" but §4 mixes his FPF patterns with Jetix-internal IPs without a clear structural separator (e.g. a dedicated subsection "§4.0 — Note: §4.1–§4.3 are Jetix mapping conventions, not canonical FPF patterns"). |
| 8 | **Version-snapshot declared — which FPF-Spec snapshot is the basis** | FAIL | Frontmatter `corpus:` field lists `raw/external/ailev-FPF/FPF-Spec.md` (pointing to current c86eabd), but the body line numbers throughout match the 2026-04-20 vendored snapshot (62K lines). The CHANGELOG documents +10 598 lines delta; line numbers shifted. The artefact does not declare that it was written against the OLD snapshot. v2 must either re-verify all line numbers against c86eabd or explicitly state "written against FPF-Spec-2026-04-20.md.bak; current spec line numbers in brackets." |

**Summary:** 4 outright FAIL, 2 PARTIAL FAIL, 2 N/A (check 6 = expected absent in v1; check 8 = stale corpus reference). No check passes cleanly. This is expected for a Phase A v1 distillation; the purpose of this critic pass is to produce the v2 design specification.

---

## §3.2 Acceptance Predicate (Hamel-binary)

`reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md` v2 PASSES iff:

1. A quick-reference card (≤50 lines) listing all 5 primitives, 7 mechanisms, and 10 amplification steps with their FPF pattern IDs exists at document top (or as a clearly marked §0 / §QR section).
2. All body line-number citations verified against the c86eabd spec snapshot (FPF-Spec.md 72 800 lines); OR a single prominent header note reads "Line numbers reference FPF-Spec-2026-04-20.md.bak (62 202 lines); c86eabd equivalents differ by +10K offset."
3. §4 Jetix-internal IPs (IP-1, IP-2, IP-3, IP-7) are structurally fenced with a subsection marker "§4.0 Mapping note: §4.1–§4.3 are Jetix RUSLAN-LAYER conventions, not canonical FPF patterns."
4. `diagrams/02-intelligence-amplification-workflow.md` is explicitly linked from §6.3 by filename.
5. Mermaid diagrams `01-fpf-top-level-architecture.md` and `02-intelligence-amplification-workflow.md` are embedded inline (as code blocks) OR explicitly linked at the sections they illustrate, not only in the SUMMARY companion.

---

## §3.3 Alternatives + status-quo + kill-conditions

### Alternative A — Line-number re-verification pass (minimal v2)

**Description.** Re-verify all FPF-Spec.md line-number citations against c86eabd; add the quick-reference card (§QR at top); add the §4.0 namespace mapping note; add the diagram link in §6.3. Minimal structural change — only the five Conformance failures addressed.

**Kill condition.** Fails if re-verification is done against the wrong snapshot (e.g. still using the .bak), OR if the quick-reference card omits the 10-step amplification list (which is in diagram 02, not in body §6.3), OR if the Jetix IP fence is added but not structurally visible (buried in prose, not a heading).

### Alternative B — Full restructure to API-surface-first (maximal v2)

**Description.** Invert the document structure: §0 = quick-reference card (primitives + mechanisms + 10 steps); §1 = FPF one-phrase; §2 = one-paragraph; §3 = deep-dive on each primitive with verified citations; §4 = mechanisms (Левенчуковский only; move Jetix IP mappings to a clearly named §4.X appendix); §5 = intelligence amplification step-by-step WITH inline mermaid diagram 02; §6 = principles and intellect base; §7 = gaps. Inline glossary (Левенчуковский terms with English parens) appended as §8 (or cross-link to `99-glossary-levenchuk-terms.md`).

**Kill condition.** Fails if restructure disrupts established companion-file references (`02-u-episteme-and-iwe.md` cross-refs) OR if it exceeds 1200 lines (target is 800-1200 per brief) OR if the IP-1/IP-2 Jetix mapping is lost entirely (it has value for Ruslan context; it must be preserved, just structurally fenced).

### Alternative C — Status-quo (ship v1 as-is, defer tightening)

**Description.** Do not produce v2; leave Phase A v1 as canonical distillation. Phase B work proceeds with the 462-line v1 as reference.

**Kill condition.** Fails if L1 audience (Левенчуков, Цэрэн) reads this document as an FPF reference, because: (a) stale line numbers will produce wrong citations; (b) namespace contamination will confuse what is canonical FPF vs Jetix derivative; (c) absent quick-reference card means 5-minute extractability fails for a 62K-line spec reader who has very high expectations.

**Recommended.** Alternative A is the minimum viable v2. Alternative B is the preferred v2 if the audience is L1 (it is). The delta between A and B is restructuring cost vs signal quality; given the Phase B Phase B framing (C4 benchmark, response draft to Левенчуков), B is worth it.

---

## §3.4 Anti-scope

This critique does NOT:

- **Not evaluating the substantive correctness of FPF claims.** Whether Левенчуков's 7 core ideas (§5.1) are correctly attributed is a philosophy/content question, not a structural engineering question. This pass evaluates structure, navigability, provenance format, and interface clarity.
- **Not rewriting v2.** The critic returns a specification; brigadier writes v2.
- **Not evaluating the companion files** (`02-u-episteme-and-iwe.md`, `03-intellect-stack.md`, etc.). Each companion deserves its own critic pass. This pass is scoped to `01-fpf-on-human-language.md` only.
- **Not capital-impact analysis.** Whether producing v2 is worth the effort given Phase B priorities is `mgmt × integrator` territory.
- **Not evaluating the Phase A corpus selection.** Whether the right sources were chosen is an epistemic question; this pass accepts the corpus as given.
- **Not evaluating mermaid diagram correctness.** Diagrams are artifacts in `diagrams/`; they would require their own critic pass.

---

## §3.5 v2 Design Deltas (concrete before/after snapshots)

### Delta 1 — Quick-Reference Card (INSERT at top, before §1)

**Before.** Document opens with frontmatter + constitutional posture blockquote + §1 "FPF в одной фразе."

**After.** Insert `## §QR Quick-Reference Card` immediately after the constitutional posture blockquote:

```markdown
## §QR Quick-Reference Card (5 primitives + 7 mechanisms + 10 amplification steps)

| # | Primitive | FPF pattern ID | Section |
|---|---|---|---|
| 1 | U.Holon — unit of composition | A.1 | §3.1 |
| 2 | U.BoundedContext — local CWA frame | A.1.1 | §3.2 |
| 3 | U.Role — method-signature not executor | A.2 / A.13 | §3.3 |
| 4 | U.Method + U.Work — transformer quartet | A.3 / A.15 | §3.4 |
| 5 | U.Alpha → state-graph | A.2.5 / A.15.1 | §3.5 |

| # | Mechanism | FPF pattern ID | Section |
|---|---|---|---|
| 1 | Bounded-context map | A.1.1 | §6.3 step 1 |
| 2 | Role + method-signatures | A.2 / A.3 | §6.3 step 2 |
| 3 | Alpha-state-graphs (past-participle) | A.2.5 | §6.3 step 3 |
| 4 | F-G-R per claim | B.3 | §6.3 step 4 |
| 5 | DRR decision record | E.9 | §6.3 step 5 |
| 6 | Abductive Loop + Open-Ended Search | B.5.2 / C.17-C.19 | §6.3 step 6 |
| 7 | Multi-View Publication | E.17 MVPK | §6.3 step 7 |

| # | Amplification step (10-step workflow) | FPF pattern | Diagram |
|---|---|---|---|
| 1 | Declare U.BoundedContext | A.1.1 | [02-intelligence-amplification-workflow.md](diagrams/02-intelligence-amplification-workflow.md) F1 |
| 2 | Map U.Roles + method-signatures | A.2/A.3 | diagram F2 |
| 3 | Define U.Alpha-state-graphs | A.2.5 | diagram F3 |
| 4 | Abductive Loop | B.5.2 | diagram F4 |
| 5 | Explore-Exploit governor | C.17-C.19 | diagram F5 |
| 6 | F-G-R per claim | B.3 | diagram F6 |
| 7 | F.17 UTS — vocabulary stabilization | F.17 | diagram F7 |
| 8 | E.9 DRR — decision rationale | E.9 | diagram F8 |
| 9 | E.17 MVPK — multi-view publication | E.17 | diagram F9 |
| 10 | F.9 Bridges — cross-context translation | F.9 | diagram F10 |

> Full diagrams: [`01-fpf-top-level-architecture.md`](diagrams/01-fpf-top-level-architecture.md)
> · [`02-intelligence-amplification-workflow.md`](diagrams/02-intelligence-amplification-workflow.md)
```

**Justification.** This satisfies Conformance checks 1 (navigability) and 3 (interface vs implementation). Ousterhout deep-module principle: the §QR is the thin interface; the §3–§6 body is the deep implementation. The reader can use the §QR as the public API and drill into the body only when needed. Estimated delta: +40 lines.

---

### Delta 2 — Corpus version declaration and line-number fence (INSERT in frontmatter / §1)

**Before.** Frontmatter `corpus: raw/external/ailev-FPF/FPF-Spec.md` (implying current snapshot). Body cites e.g. `FPF-Spec.md L738`, `FPF-Spec.md:700-708`, `FPF-Spec.md:499`, `FPF-Spec.md:513`.

**After.** Two changes:

1. Frontmatter — add:
```yaml
spec_snapshot: FPF-Spec-2026-04-20.md.bak  # line numbers in body reference this snapshot (62 202 lines)
spec_current: FPF-Spec.md  # c86eabd 2026-05-16; 72 800 lines; +10 598 lines delta per CHANGELOG
```

2. Add a note box immediately after the constitutional posture blockquote and before §QR:
```markdown
> **Snapshot note.** Body line citations (`FPF-Spec.md L###`) reference the
> 2026-04-20 vendored snapshot (62 202 lines, `FPF-Spec-2026-04-20.md.bak`).
> The current upstream snapshot is c86eabd (2026-05-16, 72 800 lines). Key
> line-number shifts: "Purpose – an operating system for thought" = L738 (old)
> → L831 (current); Pareto frontier passage = L700 (old) → L793 (current);
> "generative architecture for thought" = L499 (old) → L592 (current);
> U.Holon definition = L1055 (old) → L1149 (current). See
> `raw/external/ailev-FPF/CHANGELOG-2026-04-20-to-2026-05-16.md` for full delta.
```

**Justification.** Satisfies Conformance check 4 (provenance density) and check 8 (version-snapshot declared). For L1 readers (Левенчуков is the spec author), misquoted line numbers are a credibility signal. Estimated delta: +10 lines to frontmatter + body.

---

### Delta 3 — Jetix-internal IP namespace fence (INSERT as §4.0 in §4 block)

**Before.** §4 opens directly with `### §4.1 IP-1 Role≠Executor (FPF anti-conflation principle)`. The subsection body notes "Не explicit pattern ID в Spec — это RUSLAN-LAYER IP-1 в Bundle 1 RUSLAN-ACK 2026-04-28" — but this is buried in prose, not a structural marker.

**After.** Insert `### §4.0 Namespace note` before §4.1:

```markdown
### §4.0 Namespace note — §4.1–§4.3 vs §4.4–§4.7

**§4.1–§4.3 (IP-1, IP-2, IP-3)** = Jetix RUSLAN-LAYER mapping conventions
(see `CLAUDE.md §4.1–§4.2`). These are NOT canonical FPF patterns; they are
Jetix-internal identifiers that reference FPF mechanisms as their basis.
For L1 FPF readers: the underlying FPF mechanisms are A.2 + A.13 (IP-1),
E.9 + Rule-of-Constraints (IP-2), E.5.x Guard-Rails (IP-3).

**§4.4–§4.7 (A.6.B, A.14, B.3, IP-7)** = canonical FPF patterns + one
Jetix-layer escalation convention (IP-7 ≈ B.3.3 AssuranceLevels L0 escalation).
```

**Justification.** Satisfies Conformance check 7 (namespace contamination). For Левенчуков: he is the author of FPF; seeing "IP-1" referenced as if it were an FPF pattern when it is actually a Jetix internal convention is misleading. The fence makes the distinction structurally clear. Estimated delta: +12 lines.

---

### Delta 4 — Diagram explicit link in §6.3 (EDIT in §6.3 body)

**Before.** §6.3 "The actual mechanism — step-by-step (synthesized from Spec + Readme)" lists 7 mechanisms numbered 1–7. No link to diagram 02.

**After.** Add at the end of the §6.3 section header paragraph:

```markdown
> **Visual reference.** [`diagrams/02-intelligence-amplification-workflow.md`](diagrams/02-intelligence-amplification-workflow.md)
> shows this workflow as a mermaid LR diagram (vanilla AI loop vs FPF-loaded AI loop,
> F1–F10). Steps F1–F10 in the diagram correspond to §6.3 steps 1–7 below plus
> steps 8–10 (UTS, DRR, MVPK, Bridges — all in §QR table above). The diagram and
> `01-fpf-top-level-architecture.md` are the companion visuals for this document.
```

**Justification.** Satisfies Conformance check 5 (structural integrity, dangling links). The §6.3 inline list stops at 7 mechanisms; the diagram has 10 steps. Without the cross-link a reader thinks the body is exhaustive when it is not. Estimated delta: +6 lines.

---

### Delta 5 — Inline glossary pointer (ADD at end of document before the closing line)

**Before.** Document closes with: `*Distillation §1 complete. См. companion files §2-5 + glossary §99.*`

**After.** Replace with:

```markdown
---

## §8 Inline glossary — key Левенчуковский terms

For a full ~60-term alphabetical glossary see [`99-glossary-levenchuk-terms.md`](99-glossary-levenchuk-terms.md).
Critical terms used in this document with English glosses:

| RU term | EN gloss | First use | FPF pattern |
|---|---|---|---|
| Холон | Holon (whole-as-part) | §3.1 | A.1 |
| Граница контекста | Bounded Context | §3.2 | A.1.1 |
| Роль | Role (method-signature, not executor) | §3.3 | A.2 |
| Метод / Описание метода / Работа | Method / MethodDescription / Work | §3.4 | A.3 / A.15 |
| Альфа | Alpha (state-tracked element) | §3.5 | A.2.5 |
| Граф создания | Creation Graph | §3.6 | A.14 / B.2 |
| Стратегирование | Strategizing (method of choosing method) | §3.7 | B.4 / B.5 |
| Мышление письмом | Writing-as-Thinking | §3.8 | F.1/F.4/E.9 |
| Формальность / Область действия / Надёжность | Formality / Group-scope / Reliability | §4.6 | B.3 F-G-R |
| Запись обоснования решения | DRR (Design Rationale Record) | §4.6/§6.3 | E.9 |
| Мультивидовая публикация | Multi-View Publication Kit (MVPK) | §6.3 | E.17 |

*Distillation §1 complete (v2). FPF-Spec snapshot: 2026-04-20 (62 202 lines).
Companion files: §2-5 + glossary §99. Diagrams: `diagrams/01-*` + `diagrams/02-*`.*
```

**Justification.** Satisfies the Phase B brief requirement (c) inline glossary. Estimated delta: +22 lines inline table. Full glossary cross-reference prevents duplication. For L1 readers who already know the terms, the table is a scan-skip; for Ruslan/Tseren audience who uses both languages, it is a navigation aid.

---

## §3.5 Summary: v2 line-count projection

| Change | Delta lines |
|---|---|
| Delta 1 — §QR Quick-Reference Card | +42 |
| Delta 2 — Snapshot note in frontmatter + body | +12 |
| Delta 3 — §4.0 Namespace fence | +14 |
| Delta 4 — Diagram link in §6.3 | +6 |
| Delta 5 — §8 Inline glossary pointer | +24 |
| Base v1 | 462 |
| **Projected v2 total** | **~560 lines** |

Note: The Phase B target is 800-1200 lines ("tightened"). The 5 deltas above bring v1 to ~560 — tighter, but short of 800. Two paths to reach 800-1200:
- (Path A, preferred) Merge v1 body tightening (condense §3.9 "Additional primitives" from prose to table; tighten §4.2–§4.3 which are thin and redundant) + expand §6.4 "Why this is intelligence amplification" to include E.10.SEMIO reference from CHANGELOG (inscription discipline — directly relevant for Jetix append-only logs). Net: tighten 40 lines from body, add 60 lines of E.10.SEMIO + A.6.P content. Reaches ~580, still below target.
- (Path B) Add the full E.2 Eleven Pillars list extraction (§5.3 currently says "TO-COLLECT Phase B") — estimated +80 lines of P-1 through P-11 content from Spec L745 area in current snapshot. Reaches ~660, approaching lower bound.
- (Path C) Combine Path A + B + expand §6.3 from 7 mechanisms to full 10-step treatment matching diagram 02 (add UTS, DRR, Bridges as separate numbered items with provenance). Reaches ~750-800.

Recommendation for brigadier v2 authoring: implement Deltas 1-5 + Path C. This produces a structurally complete v2 of 750-800 lines that is denser and more navigable than the 462-line v1, without crossing 1200.

---

## §6 Specific Failures Found

| AP code | Location | Evidence |
|---|---|---|
| AP-ENG-10 (external-dep-without-failure-mode equivalent) | §1 L26, §6.2 L403-415, §6.1 L393, §6.4 L440-444 | Stale FPF-Spec.md line-number citations: L738 (should be L831), L700-708 (should be ~L793), L165-171 (should be L167), L499 (should be L592), L513 (should be L606). These are "external dependency call sites" in a provenance-dense artefact — incorrect line numbers in a doc authored for Левенчуков (the spec's author) are credibility failures. |
| AP-ENG-2 (shallow-module proliferation equivalent) | §4 (entire section) | §4.1–§4.7 mixes two namespaces (FPF canonical patterns + Jetix RUSLAN-LAYER IPs) without a structural boundary. This is a shallow-module failure: the section's "interface" (what it says it is: "Core mechanisms FPF") does not match its "implementation" (three of seven items are Jetix-only). |
| AP-ENG-12 (architecture-without-pattern-declaration) | §6.3, §6 overall | The 7 mechanisms in §6.3 are described without connecting back to the §QR (which does not exist in v1). A reader cannot verify "are there 7 mechanisms or 10?" The architecture pattern (10-step amplification workflow as shown in diagram 02) is not declared in the body. |
| AP-ENG-9 (premature-abstraction equivalent) | §3.9 "Additional FPF primitives (briefly — для polysemy)" | §3.9 introduces 7 additional primitives (U.Episteme, U.Capability, U.Characteristic, U.Scale, U.Level, U.Coordinate, U.View, U.UTS, U.DRR) with single-line descriptions. These are underdeveloped; each has fewer than 2 concrete use-illustrations in the document. Either give them full treatment (with provenance, cross-ref, use-case) or consolidate to a forward-reference table pointing to companion files. |

---

## §7 Recommended Changes

| Change | AP addressed | Estimated effort | Priority |
|---|---|---|---|
| Insert §QR Quick-Reference Card (Delta 1) | AP-ENG-12 (interface clarity) | small | P1 |
| Add snapshot declaration + line-shift note (Delta 2) | AP-ENG-10 (stale provenance) | small | P1 |
| Insert §4.0 namespace fence (Delta 3) | AP-ENG-2 (namespace contamination) | small | P1 |
| Add diagram cross-link in §6.3 (Delta 4) | AP-ENG-12 (dangling cross-ref) | small | P1 |
| Add §8 inline glossary pointer (Delta 5) | Phase B addition (c) | small | P2 |
| Expand §6.3 from 7 to 10 steps (matching diagram 02) + add UTS/DRR/Bridges as full items | AP-ENG-3 (MONO violation: list claims 7 but diagram shows 10) | medium | P2 |
| Convert §3.9 additional primitives to forward-reference table | AP-ENG-9 | small | P2 |
| Add E.10.SEMIO + A.6.P references per CHANGELOG | freshness (c86eabd delta) | medium | P3 |
| Expand §5.3 Eleven Pillars from partial to full P-1..P-11 list | Interface gap | medium | P3 |

---

## Escalations and Dissents

**No escalations.** All checks are within `engineering × critic` domain (structure, navigability, provenance format, interface clarity).

**No dissents.** No peer-expert inputs conflict with this pass.

**One integrative observation (per §1b integrative_obligation).** The stale line numbers (Delta 2 issue) are a direct consequence of the CHANGELOG documenting a +17% spec growth between Phase A (April snapshot) and Phase B (May current). If brigadier intends v2 to be durable across future FPF upstream updates, it should consider adding a "spec-version: <commit-hash>" field to the frontmatter and a CI-style note "these line numbers will drift as FPF evolves; use section headings as stable anchors where possible." This is a `systems × scalability` concern (how does the distillation stay fresh over a living spec?) — not resolved here, flagged for brigadier routing.

---

*Critic pass complete. Brigadier integrates this draft + parallel returns to author v2.*
