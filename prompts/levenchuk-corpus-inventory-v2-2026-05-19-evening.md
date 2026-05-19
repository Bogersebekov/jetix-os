---
title: Levenchuk Corpus Inventory v2 — refresh + extend + cross-link к Jetix substrate
date: 2026-05-19 evening
type: deep-prompt-autonomous
phase_count: 8
parent_explain: prompts/explanations/_EXPLAIN-levenchuk-corpus-inventory-v2-2026-05-19-evening.md
output_namespace: research/levenchuk-corpus-inventory-v2-2026-05-19-evening/
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: levenchuk-corpus-inventory-v2
R: refuted_if_freshness_missed_OR_cross-link_omitted_OR_paid_layer_unmarked
constitutional_posture: R1 surface + R6 + R11 + R12 N/A + EP-5 F2 + IP-1 STRICT + FPF lens Phase 0 + breadth-NOT-selection + append-only
estimated_runtime: 90-110 min autonomous
estimated_cost: <€2 (built-in tools only)
---

# Levenchuk Corpus Inventory v2 — Deep Prompt

> **Autonomous server CC run.** 8 phases. Per-phase commit + push. NOT plan mode — execute immediately when launched. Read EXPLAIN file first для context.

---

## §0 Pre-flight — обязательное чтение

ПЕРЕД Phase 0 прочитать:

1. **EXPLAIN file:** `prompts/explanations/_EXPLAIN-levenchuk-corpus-inventory-v2-2026-05-19-evening.md`
2. **Memory rules** (load в context):
   - `feedback_fpf_lens_first.md` — FPF lens Phase 0 mandatory
   - `feedback_iwe_chat_rejected.md` — IWE chat REJECTED, materials only
   - `feedback_breadth_not_selection.md` — inventory mode, NO selection
   - `feedback_prompt_explanation_required.md` — already satisfied (EXPLAIN exists)
3. **Existing 2026-05-17 substrate:**
   - `raw/external/levenchuk-corpus-2026-05-17/00-INVENTORY.md` (10-category map)
   - `raw/external/levenchuk-corpus-2026-05-17/MANIFEST.md`
   - `raw/external/levenchuk-corpus-2026-05-17/blockers.md`
4. **Jetix substrate для cross-link Phase 4:**
   - 5 concept docs: `decisions/strategic/JETIX-*-2026-05-18.md`
   - Platform v2: `reports/jetix-platform-v2-2026-05-19/99-SUMMARY-FOR-RUSLAN.md`
   - 6 K-research summaries: `research/{agi-reception-market,method-systems-thinking,info-substrate-philosophy,society-as-code-stress-test,intellect-12-component-audit,safety-develop-validation}-deep-2026-05-19/99-SUMMARY-FOR-RUSLAN.md`
   - 3 Tier A K-6 wikis: `wiki/concepts/{method-systems-thinking,jetix-as-exokortex,sense-of-measure-scientific-approach}.md`

---

## §1 Phase 0 — FPF Lens Scope (5 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/phase-0-fpf-lens-scope.md`

Declare explicitly per `feedback_fpf_lens_first.md`:

- **Object:** Levenchuk-corpus = (a) body of work (books / courses / articles / videos / repos); (b) person (bio / role / history); (c) ecosystem (МИМ / ШСМ / Aisystant / IWE / Цэрэн / partners / community)
- **FPF layer:** Part B.3 F-grade surfacing (F2 inventory / cataloguing — NOT F4+ analytical)
- **Diff predicate:** N/A — this is **inventory phase, no comparison.** Pure cataloguing. Cross-link к Jetix substrate в Phase 4 = mapping/overlap-identification, NOT comparison.
- **F-G-R per claim:** F2 surface / G=levenchuk-corpus-map / R=medium (web-discoverable + repo-vendored)
- **Acceptance predicate:** «inventory v2 complete-enough» когда (a) FPF freshness verified vs 2026-04-20, (b) Tier 1+2 collection gaps filled, (c) cross-link к 8 Jetix substrate sources done, (d) paid layer explicit для Ruslan, (e) blockers updated, (f) Summary ≤500w + 5 mermaid

Commit: `[levenchuk-inventory-v2] Phase 0 FPF lens scope`

---

## §2 Phase 1 — Verify Existing Inventory + Freshness Deltas (10 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/02-freshness-deltas.md`

### Steps

1. **FPF upstream freshness check:**
   - `gh api repos/ailev/FPF/commits/main --jq '.[0:20]'` → top-20 commits с 2026-04-20
   - Compare vs `raw/external/ailev-FPF/FPF-Spec.md` (vendored 2026-04-20)
   - Note: line-count delta / new sections / removed sections / version tag changes
   - **DO NOT auto-pull updated FPF-Spec.md** — flag для Ruslan handling (R11 Default-Deny — Foundation-adjacent vendored content)

2. **LJ ailev.livejournal.com freshness:**
   - WebFetch `https://ailev.livejournal.com` latest 30 posts list (titles + dates)
   - Identify any new posts since 2026-05-17 (по date filter)
   - Note: title / date / brief topic / URL

3. **ШСМ events freshness:**
   - WebFetch `https://events.system-school.ru` → check для новых events post-17.05
   - Note any new conferences / residency cohorts announced

4. **Blocker status update:**
   - B2 IWE direct interaction → **RESOLVED rejected** per `feedback_iwe_chat_rejected.md` 2026-05-17 evening
   - B5 «Системный фитнес» → **RESOLVED practice-not-book** per existing analysis
   - B4 «Инженерия интеллекта» → still pending Ruslan clarification (flag)
   - B6 YouTube transcripts → still infrastructure-blocked (metadata-only preserved)
   - B7 @ailev_blog handle → re-verify (WebFetch search)

5. **New sources surfaced since 17.05** (если discovered through WebSearch / WebFetch на этом phase):
   - Surface in `02-freshness-deltas.md` per-source со full URL + access path

Commit: `[levenchuk-inventory-v2] Phase 1 verify + freshness deltas`

---

## §3 Phase 2 — Tier 1 Fast-Wins Collection (15-20 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/03-collected-new-content.md` (Tier 1 section)

### Sources (WebFetch each → captured content с provenance trail)

**T1.1 — LJ Левенчуковский key posts (RE-VERIFY + новые с 17.05):**
- 02.10 set: post IDs 1051048, 1067999, 1082662, 1188876, 1318973, 1331004, 1575106, 1718836, 1725757
- 02.11 set: 1777145 (Autumn 2025 residency), 1798285 (10th MIM conf 2026), 1788706 (FPF dev plans 2026-02)
- Любые новые post IDs identified в Phase 1 LJ freshness check

WebFetch каждый: extract title / date / verbatim первые 1500 слов / topic tags / mentioned books-courses-events.

**T1.2 — МИМ public site core pages:**
- 03.01 https://system-school.ru (homepage)
- 03.05 https://system-school.ru/stack (intellect-stack)
- 03.06 https://events.system-school.ru
- 03.11 https://events.system-school.ru/conf-2026 (10th conference)
- 03.04 Цэрэн profile if accessible

WebFetch каждый: extract structure / curriculum mentions / event list / pricing if public.

**T1.3 — arXiv PDFs metadata:**
- 07.01 https://arxiv.org/abs/1502.00121 (Towards a Systems Engineering Essence 2015)
- 07.02 https://arxiv.org/abs/2310.11524 (Third Generation Systems Thinking 2023)

WebFetch abstract pages: extract abstract / authors / citation count / DOI / publication date.

**T1.4 — Psybertron English review:**
- 09.03 https://www.psybertron.org/archives/15807

WebFetch: extract review summary / cited claims / external interpretation framing.

**T1.5 — systemsworld.club Tseren profile:**
- 08.11 https://systemsworld.club/t/czeren-czerenov-strateg-sistemnogo-myshleniya-i-sozdatel-uspeshnyh-sistem/22932

WebFetch: extract profile / community framing.

**T1.6 — Левенчуковский 2024 alpha/Essence posts (R-D cited):**
- WebFetch verify availability + extract если new или need re-capture

### Per-source provenance в `03-collected-new-content.md`:
```markdown
### T1.X — <Source name>
- URL: <full URL>
- Retrieved: 2026-05-19 evening
- Tool: WebFetch
- Volume: <N words extracted>
- Status: ✅ captured / 🟡 partial / 🔴 failed (<reason>)

[Extracted content here]

[src: <URL> | retrieved 2026-05-19 | F2 verbatim]
```

Commit: `[levenchuk-inventory-v2] Phase 2 Tier 1 collection (T1.1-T1.6)`

---

## §4 Phase 3 — Tier 2 Medium-Effort Collection (15-20 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/03-collected-new-content.md` (Tier 2 section, append)

### Sources

**T2.1 — LJ tag-filtered samples (top 20 posts per tag, titles + dates only):**
- 02.02 https://ailev.livejournal.com/tag/интеллект-стек
- 02.03 https://ailev.livejournal.com/tag/мышление
- 02.04 https://ailev.livejournal.com/tag/методология
- 02.05 https://ailev.livejournal.com/tag/FPF

WebFetch каждый tag page; extract latest 20 post titles + dates + URLs (DO NOT fetch each post в этом phase — это metadata только для inventory).

**T2.2 — Habr / vc.ru third-party:**
- 09.01 https://habr.com/ru/search/?q=Левенчук
- 09.02 https://vc.ru/search?query=ШСМ

WebFetch каждый: extract latest 10 articles each (title + author + date + URL).

**T2.3 — GitHub ailev other repos listing:**
- 01.03 https://github.com/ailev?tab=repositories

`gh api users/ailev/repos --jq '.[] | {name, description, updated_at, stargazers_count}'` → list all public repos с metadata.

**T2.4 — TechInvestLab 2015 PDF:**
- 07.05 https://techinvestlab.ru/files/systems_engineering_thinking/systems_engineering_thinking_2015.pdf

Try curl PDF metadata only (HEAD request); если accessible — note size + page count.

**T2.5 — inexsu.wordpress.com 2020 ШСМ alpha post:**
- 09.06 https://inexsu.wordpress.com/2020/05/23/левенчук-системноинжене/

WebFetch: extract third-party interpretation framing.

**T2.6 — in.wiki bio:**
- 09.08 https://in.wiki/Левенчук,_Анатолий_Игоревич

WebFetch: extract encyclopedia bio / cited works / external references.

**T2.7 — Tseren Medium English:**
- 08.04 https://medium.com/@tserentserenov

WebFetch: extract latest 10 article titles + dates.

**T2.8 — Левенчуковский Ridero author page:**
- 05.14 https://ridero.ru/author/levenchuk_anatolii_iv2h/

WebFetch: extract full title catalog с publish dates / ISBNs / page counts.

**T2.9 — Ozon catalog:**
- 05.15 https://www.ozon.ru/category/levenchuk/

WebFetch: extract titles + prices + ratings (paid layer cost reference).

**T2.10 — LitRes:**
- 05.16 https://www.litres.ru/author/anatoliy-levenchuk/about/

WebFetch: extract catalog + sample availability.

Commit: `[levenchuk-inventory-v2] Phase 3 Tier 2 collection (T2.1-T2.10)`

---

## §5 Phase 4 — Cross-Link к Jetix Substrate ⭐ (15-20 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/04-cross-link-к-jetix-substrate.md`

### Steps

1. **Read** 6 K-research 99-SUMMARY-FOR-RUSLAN.md + Platform v2 99-SUMMARY + 5 concept docs F2 (top-of-doc only, ~10 min reading)

2. **Build matrix** Levenchuk-topics × Jetix-substrate-sources:

| Levenchuk topic | 5 concept docs | Platform v2 | K-1 InfoSub | K-2 AGI | K-3 SocietyCode | K-4 Intellect-12 | K-5 Safety-Develop | K-6 Method ⭐⭐ | 3 Tier A wikis |
|---|---|---|---|---|---|---|---|---|---|
| Системное мышление | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Методология | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Системная инженерия | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Системный менеджмент | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Инженерия личности | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Интеллект-стек | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Рациональная работа / Собранность | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| FPF spec | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| IWE (как concept) | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Essence Kernel | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| 17 transdisciplines | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Mereology / Holon | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| R0/R1/R2 residency model | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Master-Apprentice 4-role | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| U.Episteme | ? | ? | ? | ? | ? | ? | ? | ? | ? |

Per cell: ✅ explicit overlap with [src] / 🟡 partial / 🔴 none / ⭐ gap-to-fill

3. **Narrative findings (3-5 paragraphs):**
   - Where Levenchuk methodology уже **deeply latent** в нашем substrate (e.g., K-6 Method × Системное мышление = direct lineage)
   - Where Levenchuk methodology **superficially mentioned** но not deeply integrated
   - Where Levenchuk methodology **absent** despite topical relevance (gap candidates для deep FPF phase)
   - Specific K-6 deep overlap analysis (Sense of Measure ≈ scientific approach; Recursive lifecycle 8-step; 31 components × Levenchuk's stack)

4. **Top-5 cross-link findings** ⭐ — distilled paragraph для Summary

Commit: `[levenchuk-inventory-v2] Phase 4 cross-link к Jetix substrate (matrix + 5 findings)`

---

## §6 Phase 5 — Paid Layer Mark + Ruslan Handles (10 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/05-paid-layer-ruslan-handles.md`

### Structure

**§A Aisystant courses (8):**
| # | Course | Format | Page est | Cost ref | Priority for Jetix |
|---|---|---|---|---|---|
| 1 | Системное мышление | online guide + exercises | ~900 pp (vol 1+2 digitized) | subscription | ⭐⭐⭐ K-6 anchor |
| 2 | Методология | online guide | ~872 pp | subscription | ⭐⭐⭐ K-6 anchor |
| 3 | Системная инженерия | online guide | ~one book | subscription | ⭐⭐ Platform v2 anchor |
| 4 | Системный менеджмент | online guide | ~one book | subscription | ⭐⭐ Platform v2 |
| 5 | Инженерия личности | online guide | ~one book | subscription | ⭐⭐ Education Layer concept doc |
| 6 | Интеллект-стек | online guide | ~one book | subscription | ⭐⭐⭐ K-4 anchor |
| 7 | Рациональная работа / Собранность (R0) | online + cohort | ~one course | subscription | ⭐⭐ Safety→Develop K-5 anchor |
| 8 | English Systems Thinking 2020 (translation) | online | ~one book | subscription | ⭐ optional cross-lang |

**§B Ridero books (9 — verify против Phase 3 T2.8 fresh catalog):**
| # | Book | ISBN | Pages | Price est | Format options |
|---|---|---|---|---|---|
| 1 | Системное мышление 2024 том 1 | 978-5-0064-2853-9 | 412 | ~€10-15 | PDF / EPUB / print |
| 2 | Системное мышление 2024 том 2 | 978-5-0064-2855-3 | 488 | ~€10-15 | PDF / EPUB / print |
| 3 | Методология 2025 | - | ~872 | ~€15-20 | PDF / EPUB / print |
| 4 | Системная инженерия 2022 | - | - | ~€10-15 | - |
| 5 | Системный менеджмент 2023 | - | - | ~€10-15 | - |
| 6 | Инженерия личности 2023 | - | - | ~€10-15 | - |
| 7 | Интеллект-стек 2023 | 978-5-0060-4990-1 | - | ~€10-15 | - |
| 8 | Визуальное мышление 2018 | - | short | ~€5-10 | - |
| 9 | (TBD по T2.8 fresh catalog) | - | - | - | - |

**§C Residency R0/R1/R2:**
- Apply path / cohort dates / cost / format details (per LJ 2025 Autumn post + 10th conf info)
- Status: per inventory blocker B3 — Ruslan acked apply but pending cohort schedule

**§D Recommended priority order для Ruslan acquisition (per cross-link findings Phase 4):**
1. (Top-tier) — какие сначала купить given Jetix substrate maximum overlap
2. (Mid-tier) — secondary
3. (Optional) — defer

**§E Total cost estimate:**
- Aisystant subscription: ~€X/month for N months
- 9 Ridero books: ~€80-130 total
- Residency R0: TBD per cohort price

Commit: `[levenchuk-inventory-v2] Phase 5 paid layer Ruslan-handles`

---

## §7 Phase 6 — 5 Mermaid Diagrams (10-15 min)

**Output:** `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/diagrams/`

ВСЕ диаграммы — black text theme init (per `wiki/operations/mermaid-style-guide-2026-05-07.md` + recent mermaid fix 213 blocks 2026-05-19):

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
```

### Diagram 1 — `01-corpus-map-landscape.md`
Graph TB. 10 categories × source types × status flags (✅ collected / 🟡 free-pending / 🟢 paid-Ruslan / 🔴 blocked). Subgraphs per category.

### Diagram 2 — `02-publication-timeline-2000-2026.md`
Gantt. Major Левенчуковский publication years 2000-2026 (books published per year + key LJ era / FPF dev / IWE launch / 10 conferences MIM).

### Diagram 3 — `03-topic-taxonomy.md`
Mindmap. Левенчуковский topic taxonomy (Системное мышление → Методология → Инженерия → Менеджмент → Личность → Интеллект-стек → FPF → IWE → Residency → 17 transdisciplines).

### Diagram 4 — `04-paid-vs-free-vs-blocked.md`
Pie + summary table. Volume estimates: free (LJ + МИМ + arXiv + Habr + GitHub) vs paid (aisystant + Ridero + residency) vs blocked (YT transcripts).

### Diagram 5 — `05-cross-link-к-jetix-substrate.md` ⭐
Graph LR. Levenchuk topics → 8 Jetix substrate sources (5 concept docs + Platform v2 + 6 K-research + 3 Tier A wikis) — strength of overlap encoded в edge colour.

Commit: `[levenchuk-inventory-v2] Phase 6 5 mermaid diagrams`

---

## §8 Phase 7 — Synthesis + Summary + Daily Log + Push (10 min)

**Output:**
- `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/00-SUMMARY-FOR-RUSLAN.md` (≤500w)
- `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/01-inventory-v2-master.md` (full UPDATED 10-category map с status flags)
- `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/06-blockers-v2.md` (updated)
- `research/levenchuk-corpus-inventory-v2-2026-05-19-evening/07-next-phase-deep-fpf-prompt-substrate.md` (substrate readiness checklist для next prompt)
- `daily-logs/_DAILY-LOG-2026-05-19.md` §APPEND — new §10 «§APPEND-levenchuk-inventory-v2-2026-05-19-evening»

### `00-SUMMARY-FOR-RUSLAN.md` structure (≤500w)

```markdown
---
title: "Summary for Ruslan — Levenchuk Corpus Inventory v2 (19.05 evening)"
date: 2026-05-19 evening
F: F2
G: levenchuk-corpus-inventory-v2-summary
target_audience: Ruslan (≤3-min read)
word_target: ≤500
---

# Summary for Ruslan — Levenchuk Corpus Inventory v2

## §0 TL;DR (≤150w)
- Inventory v2 done. {N} sources verified / {M} новых surfaced с 17.05 / {K} Tier 1+2 captures fresh / cross-link matrix к 8 Jetix substrate sources built / paid layer marked для tebya / blockers updated (B2+B5 resolved).
- **Top finding cross-link:** К-6 Method-Systems-Thinking + Sense-of-Measure + Recursive-lifecycle = direct Levenchuk-methodology lineage; deep FPF phase должен start с этого overlap.
- **Paid layer:** Aisystant 8 courses + 9 Ridero books + R0 residency — recommended priority order в `05-paid-layer-ruslan-handles.md`.
- **Ready signal:** substrate готов для next FPF deep research run.

## §1 What's new vs 2026-05-17 (≤100w)
- FPF upstream delta: {summary}
- LJ new posts с 17.05: {N posts; titles}
- ШСМ events delta: {summary}
- New sources surfaced: {list}

## §2 Cross-link к Jetix substrate — top 5 findings ⭐ (≤150w)
[5 bullets — где Levenchuk уже latent / где gap / где new direction]

## §3 Paid layer (≤50w)
[Recommended acquisition order — 3-5 items]

## §4 Blockers status (≤50w)
- B2 IWE chat: RESOLVED rejected ✅
- B5 Системный фитнес: RESOLVED practice ✅
- B4 Инженерия интеллекта: still pending Ruslan clarification 🟡
- B6 YT transcripts: still infrastructure-blocked 🔴

## §5 Next phase pointer
Substrate готов. Ruslan reviews → ack → next prompt (deep FPF research 8-12 phases) launches.
```

### `01-inventory-v2-master.md` — full 10-category map с UPDATED status

Mirror 2026-05-17 inventory structure но с UPDATED status flags + новые sources + cross-link к Jetix anchors per row.

### Final commit + push

```bash
git add research/levenchuk-corpus-inventory-v2-2026-05-19-evening/ daily-logs/_DAILY-LOG-2026-05-19.md
git commit -m "[levenchuk-inventory-v2] Phase 7 Summary + Daily Log §APPEND + final push"
git push origin main
```

Final echo:
```
DONE Phase 7 — N commits / M files / 5 mermaid / Levenchuk corpus inventory v2 ready substrate для next FPF deep phase
```

---

## §9 Operational rules

- **Per-phase commit + push** (mandatory; не batch all-or-nothing)
- **No paid content download** (per `feedback_iwe_chat_rejected.md` + R12 cost discipline)
- **No selection language** («top-N» / «recommended» / «best» / «pick») — pure inventory (per `feedback_breadth_not_selection.md`)
- **No Foundation writes** (R2 preserved)
- **Append-only к Daily Log** (никакая modification existing sections)
- **R6 provenance per source** (URL + retrieved date + tool + F-G-R triple)
- **Cost cap €10/день baseline** (built-in tools only)
- **WebFetch timeouts:** если single fetch fails — continue, mark 🔴 в inventory, не halt entire run
- **Mermaid black text init** — все 5 diagrams
- **Russian primary** в всех output docs

---

## §10 If blocked / unclear

- **Не halt entire run** at single source failure — mark + continue
- **Не invent content** — если WebFetch returns empty / 404 / paywall → log + skip
- **Не promote anything** к wiki/concepts/ или decisions/ автономно (R2 + R1)
- **Не decide «top priority» books** в paid layer — just surface с factual data; Ruslan decides

---

*Prompt closure 2026-05-19 evening Berlin. Server CC autonomous launch ready. Per memory `feedback_prompt_explanation_required.md` — EXPLAIN file written first; Ruslan ack → launch.*
