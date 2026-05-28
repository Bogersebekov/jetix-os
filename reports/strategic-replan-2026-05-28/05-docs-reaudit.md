---
title: Strategic Re-Plan — Phase 4 Docs Re-Audit (~28 verdicts)
date: 2026-05-28
type: strategic-replan-phase-report
phase: 4
verdicts: KEEP / REFINE / MERGE / DEFER / ARCHIVE
F: F3 (synthesis)
G: prompt-voice-batch-16-plus-strategic-replan-2026-05-28
prose_authored_by: brigadier-scribe — R1 surface; verdicts = recommendations, Ruslan decides
constitutional_posture: R1 surface + R2 STRICT (4 LOCKED = KEEP-LOCKED by definition, read-only) + R6 per-verdict + FPF role-fit lens (§3 substrate-read)
language: russian
parent_prompt: prompts/voice-batch-16-plus-strategic-replan-2026-05-28.md
---

# 🔍 Phase 4 — Docs Re-Audit (~28 verdicts)

> **FPF lens (per §3 substrate-read):** doc оценивается не «нравится/нет», а **выполняет ли свою роль в
> 4D-экстенте плана** (Simon satisficing): KEEP (роль активна, актуален) · REFINE (роль активна, нужна правка
> под V4/v16) · MERGE (роль дублирует соседа) · DEFER (роль валидна, не Wave 1) · ARCHIVE (роль закрыта —
> superseded). **R1:** все вердикты = recommendations; Ruslan picks. **R2 STRICT:** 4 LOCKED не трогаем
> (read-only); их вердикт = KEEP-LOCKED by constitutional definition. **Append-only:** ARCHIVE = рекомендация
> `git mv` в `archive/`, не удаление.

---

## §1 Verdicts summary (master table)

| # | Doc | Verdict | Reason (≤2 строки) | Action if not KEEP |
|---|---|---|---|---|
| **Metaplan-lineage** | | | | |
| 1 | JETIX-METAPLAN-V4-FINAL | **KEEP** | THE structure (16 dir canonical); no drift; status pool→fixate | — |
| 2 | JETIX-METAPLAN-V3-FINAL | **ARCHIVE** | Explicitly superseded V4 (80-85% overlap); «FINAL» ложно-окончательный | `git mv` archive/; phase-reports (65.5K) остаются substrate |
| 3 | JETIX-PUBLIC-DOCS-METAPLAN-V2 | **ARCHIVE** | Double-superseded (V3 явно + V4 транзитивно); pre-Foundation | `git mv` archive/ |
| 4 | JETIX-PUBLIC-DOCS-METAPLAN (v1) | **ARCHIVE** | Triple-superseded; уникум только variant-comparison (decision-trail) | `git mv` archive/ |
| **Foundation cluster** | | | | |
| 5 | WORKSHOP-MASTERY-NETWORK-CONCEPT | **KEEP** | THE Foundation metaphor; referenced V4 | — |
| 6 | WORKSHOP-CONCEPT-SUPPLEMENT | **KEEP** | Live companion; verbatim voice anchor; 7 R1 unacked | (ack R1 — Ruslan) |
| 7 | PREPARATION-STAGE-CONCEPT-SUPPLEMENT | **KEEP** | Live companion; extends §J 6→8; 7 R1 (D-P1..7) unacked | (ack R1 — Ruslan) |
| 8 | METHOD-MASTERY-PUBLIC-DESCRIPTION | **REFINE** | DRAFT — Ruslan prose pass; part of O-208 essence-set для Tseren/методолога | Ruslan prose pass + finalize |
| **Research outputs** | | | | |
| 9 | FOUNDER-ROLE-RESEARCH | **KEEP** | DONE substrate; 15 R1 pending (surface, not modify) | (ack R1 — Ruslan) |
| 10 | INFO-SECURITY-OWN-INFRA-RESEARCH | **KEEP** | DONE substrate; 11 R1; feeds #17 candidate | (ack R1 + #17 decision) |
| **Voice insights** | | | | |
| 11 | VOICE-BATCH-14-INSIGHTS | **KEEP** | Acked+materialized baseline | — |
| 12 | VOICE-BATCH-15-INSIGHTS | **KEEP** | Surface; ack alongside batch-16 | (ack — Ruslan) |
| 13 | VOICE-BATCH-16-INSIGHTS (this run) | **KEEP** | New; surface-for-ruslan | (ack — Ruslan) |
| **Ops/Build/Skeleton** | | | | |
| 14 | JETIX-FULL-MAP-AND-DOCS-SKELETON | **REFINE** | 94-doc skeleton + GAP heatmap live; 6-direction model superseded V4 16 | Normalize direction-layer to V4; keep skeleton |
| 15 | DOCS-CLASSIFICATION | **MERGE** | GAP-part ~60% absorbed Full-Map; 4-cat audience-matrix unique | Merge GAP→Full-Map; preserve 4-cat audience-matrix |
| 16 | PLATFORM-LIFECYCLE-STAGES-PLAN | **REFINE** | Build/Run/Scale concept live (→ V4 Кланы); 4-week plan dates elapsed | Re-fixate dates; keep concept |
| 17 | EXECUTION-PLAN-FIXATION | **MERGE** | 4-partner-types + 8-R12-Q primitives live (absorbed upward); sequencing superseded | Primitives→V4 #5/#8 canonical; then archive |
| 18 | CONSOLIDATED-HUMAN-LANGUAGE-PLAN | **KEEP** | Root education baseline; live, stable; feeds #7 | — |
| 19 | BUILD-ARTEFACTS-SPECS | **REFINE** | Deepest artefact blueprints live; timeline shares elapsed-staleness | Re-confirm timeline + V4 alignment; keep specs |
| **Outreach/Education substrate** | | | | |
| 20 | OUTREACH-CONTENT-OUTCOMES-CTAS | **KEEP** | FOUNDATIONAL ⭐⭐⭐; CTA/Bloom/archetype substrate live | (reconcile 3 priority-lists = §4 pool) |
| 21 | JETIX-NAVIGATION-GUIDE-DRAFT | **DEFER** | DRAFT; stalest prose; 5-stage conflicts Build/Run/Scale; June-date implausible; serves deferred Wave 1 | Full re-write vs V4 when Wave 1 activates |
| **Notion** | | | | |
| 22 | NOTION-TEMPLATES-3-LAYERS-V2 | **KEEP** | Canonical Notion architecture; built (Build Report) | — |
| 23 | NOTION-TEMPLATES-4-LAYERS | **ARCHIVE** | Superseded by 3-LAYERS-V2 (same day; V2 explicit supersede) | `git mv` archive/ |
| 24 | NOTION-BUILD-REPORT | **KEEP** | Build-record (35p/36DB LIVE); actionable tail | Status-check: token revoke + UX walkthrough done? |
| 25 | AI-TOOLS-LIFEHACKS-MEGA-PAGE | **KEEP** | Living reference; built in Notion | (periodic sync-check vs tools/) |
| 26 | PERSONAL-OS-NOTION-TEMPLATE-PLAN | **MERGE** | Evolved into Layer 1 of 3-LAYERS-V2 (~50% overlap) | Merge unique detail→3-LAYERS-V2 Layer 1; then archive |
| **Voice-pipeline / contact one-shots** | | | | |
| 27 | VOICE-PIPELINE-PUBLIC-V2 | **KEEP** | Send-ready reference; part of O-208 essence-set; supersedes V1 desc | Minor: sync Tseren-letter attachment-name |
| 28 | LETTER-TO-TSEREN-RESPONSE | **REFINE** | DRAFT not-sent; Ruslan prose pass + cost-figure drift vs V2 | Fix cost-fig + prose + send (status-check Tseren) |
| 29 | CALL-PLAN-DMITRIY-KAISER | **KEEP** | Re-usable for O-213 Kaiser mentor-ask (call may have passed 25.05) | Status-check call; update with mentor-referral ask |
| **4 LOCKED (R2 STRICT — read-only)** | | | | |
| L1 | METHOD-LIFE-DEVELOPMENT-V2 🔒 | **KEEP-LOCKED** | Methodological canon; substrate-only | — (R2 STRICT) |
| L2 | STRATEGIC-PLAN-NEAR-FUTURE 🔒 | **KEEP-LOCKED** | Operational skeleton; dates ~1wk stale (substrate, not edit) | — (re-plan supersedes operationally, doc preserved) |
| L3 | ECONOMIC-MODEL-TOKENOMICS V10 🔒 | **KEEP-LOCKED** | 75/16.67/8.33 + triple-role + V10 Hybrid | — (R2 STRICT) |
| L4 | AI-MARKET-ELECTRICITY-ANALOGY 🔒 | **KEEP-LOCKED** | Stage-1 PLAN; V11 candidate; Stage-2 deferred | — (R2 STRICT) |

**Verdict tally (29 re-auditable + 4 LOCKED):** KEEP 16 · REFINE 5 · MERGE 3 · DEFER 1 · ARCHIVE 4 · KEEP-LOCKED 4.

**Headline:** substrate в основном здоров — большинство KEEP. Чистка касается **metaplan-lineage** (3 archive — естественная супер-седация V1→V2→V3→V4) + **Notion-4L** (archive) + 3 MERGE (consolidate doc-organization layer) + 5 REFINE (normalize к V4 + re-fixate elapsed dates). Никаких сюрпризов «всё переделать» — это уборка предсказуемых супер-седаций + нормализация direction-count к 16.

---

## §2 Per-doc плотный абзац (REFINE / MERGE / DEFER / ARCHIVE)

### ARCHIVE

**#2 JETIX-METAPLAN-V3-FINAL.** V4 frontmatter явно `supersedes: V3` тем же паттерном, каким V3 supersede'ил V2. Overlap 80-85% (тот же Foundation, partner-extension, format-taxonomy, R12-структура); V4 = superset (+#15 Геймификация +#16 Хакатоны + Кланы lifecycle). Заголовок «FINAL» теперь вводит в заблуждение — есть более поздний FINAL. Рекомендация: `git mv` в `archive/` (append-only preserve), оставив 21 phase-report (65.5K слов портфелей) на месте как substrate — они drill-down детали, которые V4 компрессирует. **Уникальной потери нет** — всё содержание поглощено V4. Это самый бесспорный из metaplan-archive.

**#3 JETIX-PUBLIC-DOCS-METAPLAN-V2.** Double-superseded: V3 явно (`supersedes: V2`), V4 транзитивно. Создан 25.05 — на день до Foundation-сдвига (Workshop concept 26.05), поэтому концептуально не знает мега-мастерской (его главный пробел). Весь уникальный контент (11 directions, правила, ценности, Master Plan Tesla-style) поглощён V3→V4. `git mv` archive/.

**#4 JETIX-PUBLIC-DOCS-METAPLAN (v1).** Корень цепочки, triple-superseded. Единственный уникум — variant-comparison matrix (A/B/C/D, рекомендация D), но это уже зафиксированный decision-trail (D выбран в V2). Чисто исторический. `git mv` archive/ — самый ранний (25.05, до выбора D, до Foundation).

**#23 NOTION-TEMPLATES-4-LAYERS.** 3-LAYERS-V2 явно `supersedes` его (тот же день; рефактор 4→3 слоя, удалён «Personal Expanded», STANDALONE + SIMPLIFICATION). Build реализовал именно V2 (его `parent_spec`). 4-LAYERS = чистый предшественник. `git mv` archive/.

### MERGE

**#15 DOCS-CLASSIFICATION.** GAP-часть (19 артефактов) ~60% поглощена Full-Map (которая сама заявляет «их 19 = подмножество наших 33❌+25⚠️»). НО 4-категорийная линза (🟢/🛠️/📚/⚙️) + audience×category matrix + anti-patterns (не слать партнёру 📚/⚙️) — операционно полезны и НЕ переделаны нигде. Рекомендация MERGE: GAP-список → консолидировать в Full-Map; **сохранить 4-cat audience-matrix как отдельный reference** (это canonical answer на O-208 «что кому показывать»). Не чистый archive — есть live-уникум.

**#17 EXECUTION-PLAN-FIXATION.** Самый ранний (24.05) execution-layer. Его primitives — **4 типа партнёров (T1-T4)** + **8 R12-вопросов перед касанием** — это canonical reusable, цитируемые downstream (Platform-Lifecycle, Build-Artefacts, V4 §15). Эти primitives живы. НО его solo-work/video/sequencing контент re-expressed и расширен вверх (Platform-Lifecycle +Build/Run/Scale; Build-Artefacts +per-artefact specs). Рекомендация MERGE: primitives (4 типа + 8 Q) → зафиксировать в V4 #5 Партнёры / #8 R12 как canonical; сам sequencing-doc → archive после merge.

**#26 PERSONAL-OS-NOTION-TEMPLATE-PLAN.** Эволюционировал в Layer 1 (Personal Core) of 3-LAYERS-V2 (~50% overlap). 3-LAYERS-V2 — более новая интеграция. Рекомендация MERGE: уникальный Personal-OS detail (если есть, не вошедший в Layer 1) → в 3-LAYERS-V2 Layer 1; затем archive как предшественник.

### REFINE

**#8 METHOD-MASTERY-PUBLIC-DESCRIPTION.** DRAFT (`prose_authored_by: ai-draft → ruslan-ack pending`). Это public-facing артефакт для Tseren/любого методолога — **прямой компонент O-208 «документы донести суть партнёру»**. Honest-inheritance (4 точки вклада: Workshop metaphor / Mastery at transitions / Templates×Unique / Preparation Stage). REFINE: Ruslan prose pass → finalize. Категорийно — это output фазы наполнения, а не план; держим как первый материализованный essence-doc.

**#14 JETIX-FULL-MAP-AND-DOCS-SKELETON.** Integrator-doc: 12 entities + 94-docs skeleton (36✅/25⚠️/33❌) + GAP heatmap + 5 cross-cutting max-leverage. Это живая substrate-карта документов. НО его «6 directions» модель **предшествует** V4 16 directions. REFINE: нормализовать direction-layer к V4 16 (6→16); 94-doc skeleton + GAP heatmap + cross-cutting сохранить. После refine = canonical doc-inventory.

**#16 PLATFORM-LIFECYCLE-STAGES-PLAN.** Build/Run/Scale (по «кто крутит маховик») — концептуально живо, питает V4 Кланы lifecycle. НО §8 4-week Build plan привязан к окну 25.05-22.06 (частично elapsed; сегодня 28.05 — каскад mid-flight). REFINE: re-fixate даты (новая 2-недельная рамка voice-16 O-207: 28.05-01.06 fixate / 02-08.06 execute); концепт Build/Run/Scale + точки A/B/C/D сохранить.

**#19 BUILD-ARTEFACTS-SPECS.** Самый детальный artefact-spec layer (10 deep specs: видео A/B/C, Personal/Team OS, Charter, landing, discovery, legal, supporting + dependency graph BS-3 видео-A=blocker). Specs = живые blueprints (ближайшее к «готово исполнять»). НО timeline разделяет elapsed-staleness Platform-Lifecycle + предшествует V4 +16 directions/Workshop reframe. REFINE: re-confirm timeline + выровнять по V4 (видео A/B/C ↔ 8 dirs; Charter ↔ #8/#3; Team OS ↔ Кланы); specs сохранить.

**#28 LETTER-TO-TSEREN-RESPONSE.** DRAFT, НЕ отправлен (`status: DRAFT — Ruslan prose pass + send`). One-shot event-артефакт (ответ Tseren на cold rejection). Мелкая drift: cost-цифра «€2-5/день» (API-путь) расходится с V2 (CC-headless без API = default); attachment ссылается на старое имя `VOICE-PIPELINE-PUBLIC-DESCRIPTION` вместо V2. REFINE: fix cost-figure + attachment-name + Ruslan tone-pass → send. **Status-check:** прошло ~2 дня с 26.05 — Tseren мог двинуться дальше; проверить актуальность перед send.

### DEFER

**#21 JETIX-NAVIGATION-GUIDE-DRAFT.** Oldest dated (22.05), content-edited forward to 26.05, но всё ещё DRAFT (R1 prose pass не сделан). Несёт **stale strategic prose**: 5-stage plan (Ethereum L2 → influential people → cohort → universal people → healthy society) **конфликтует** с принятым Build/Run/Scale; mass-distribution «30 June 2026» date implausible; 38-day stats устарели. Doc-navigation catalog + repo-structure механически полезны. Поскольку служит Wave 1 mass-orientation (deferred per Founder-Role «не Wave 1 mass-отправку сейчас») — DEFER: полный re-write vs V4 (16 dir + Build/Run/Scale, drop June date) когда Wave 1 активируется. Не archive (роль валидна, отложена), не refine-сейчас (низкий приоритет).

---

## §3 Drift analysis cross-doc (где documents диверсили / conflict)

1. **Direction-count drift (главный):** 6 (Full-Map) → 11 (V2) → 14 (V3) → **16 (V4 canonical)**. Все pre-V4 planning docs несут устаревший direction-count. **Нормализация:** все REFINE-docs выравниваются к V4 16. Это #1 источник «каши» — re-plan фиксирует 16 как единый словарь направлений.
2. **Stage-model drift:** Navigation-Guide 5-stage (Ethereum-first) ⚔️ Platform-Lifecycle Build/Run/Scale ⚔️ V4 Кланы 7-фаз lifecycle. **Принятая модель:** Build/Run/Scale (маховик) + Кланы 7-фаз (per-clan). Navigation-Guide 5-stage = retired.
3. **Three priority-lists drift:** Full-Map (94-doc P0-P4) ⚔️ Docs-Classification (19-GAP P1-P3) ⚔️ Outreach-CTAS (18-artefact P0-P6). Три overlapping priority-системы. **Reconcile** = §4 pool item (Ruslan picks single master priority — рекоменд: V4 master matrix §10 P0-ядро как arbiter).
4. **Date-anchored staleness:** все execution/lifecycle docs + Strategic Plan привязаны к окну 22.05-22.06 (частично elapsed). voice-16 O-207 даёт новую рамку (эта неделя fixate / следующая execute). Re-fixate в REFINE-docs.
5. **Notion-version drift:** 4-LAYERS → 3-LAYERS-V2 (resolved: V2 canonical, 4L archive). Personal-OS plan → Layer 1 (resolved: merge).
6. **Voice-pipeline-version drift:** V1 DESCRIPTION (cited by Tseren letter) vs V2 (current). Resolve: V2 canonical; fix letter attachment-name; V1 archive-candidate (conditional on existence).

---

## §4 Recommended consolidations (pool — Ruslan picks; per `feedback_research_pool_pattern`)

> Surface only. NOT auto-execute. Per-item: name / scope / output / launch-when / dependency / priority-hint.

| Pool-ID | Consolidation | Scope | Output | Launch | Dependency | Priority hint |
|---|---|---|---|---|---|---|
| C-1 | Archive 3 metaplans + Notion-4L | `git mv` V1/V2/V3-metaplan + 4-LAYERS → archive/ | 4 docs archived, append-only | quick (server CC or Cloud Cowork) | Ruslan ack ARCHIVE verdicts | P2 (housekeeping) |
| C-2 | Normalize Full-Map to V4 16-dir | REFINE Full-Map §directions 6→16; keep skeleton+GAP | updated Full-Map | prompt | C-1 | P2 |
| C-3 | Merge Execution-Plan primitives into V4 #5/#8 | 4 partner-types + 8 R12-Q → canonical placement | V4 supplement / #5 #8 doc | prompt | V4 ack | P2 |
| C-4 | Reconcile 3 priority-lists → single master | Full-Map 94 + Docs-Class 19 + Outreach 18 → V4 master-matrix arbiter | 1 master priority list | prompt | V4 §10 | P1 (blocks Wave 1 sequencing) |
| C-5 | Re-fixate elapsed dates (Platform-Lifecycle + Build-Artefacts + Strategic-Plan-operationally) | new 2-week frame (voice-16 O-207) + Build/Run/Scale dates | dated execution timeline | THIS re-plan §8 roadmap partial | voice-16 | P1 |
| C-6 | Assemble O-208 «essence doc-set для партнёра» | collect existing (voice-pipeline-V2 + method-mastery-desc + presentation-spec + 1-pager) — NOT write new | curated doc-set for Kaiser/Tseren | quick (assembly) | #8 Method-Mastery REFINE | P1 (voice-16 explicit) |
| C-7 | Finalize Method-Mastery-public + Tseren letter | Ruslan prose pass both + send letter | sent letter + finalized public-desc | Ruslan (manual) | status-check Tseren | P1 |
| C-8 | Defer Navigation-Guide re-write | hold until Wave 1 activates; full re-write vs V4 | (deferred) | when Wave 1 | Wave 1 trigger | P3 |

---

## §5 Constitutional checkpoint (Phase 4)

- ✅ **R2 STRICT** — 4 LOCKED = KEEP-LOCKED, read-only; no edits. ARCHIVE = `git mv` recommendation (append-only), not delete; Ruslan executes.
- ✅ **R1 surface** — все вердикты = recommendations; Ruslan picks. No auto-archive/merge executed this run.
- ✅ **R6** — per-verdict reason + cross-doc provenance.
- ✅ **`feedback_no_unsolicited_alternatives`** — re-audit ИХ (выбранный substrate); никакого «лучше начать заново». ARCHIVE касается только явно superseded версий (естественная эволюция V1→V4).
- ✅ **FPF role-fit lens** — вердикт = «выполняет ли роль в 4D-экстенте плана».

---

*Phase 4 closure. 29 re-auditable + 4 LOCKED visited. KEEP 16 / REFINE 5 / MERGE 3 / DEFER 1 / ARCHIVE 4 /
KEEP-LOCKED 4. Headline: substrate здоров; чистка = предсказуемые супер-седации (3 metaplans + Notion-4L) +
direction-count нормализация к V4 16 + re-fixate elapsed dates. 8 consolidation pool-items (Ruslan picks). Next:
Phase 5 per-direction breakdown.*
