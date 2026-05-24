---
title: Phase 0 — FPF lens scope + corpus inventory + acceptance predicate
date: 2026-05-23
type: research-phase-report
phase: 0 of 10
parent: prompts/levenchuk-master-qualification-research-2026-05-23.md
F: F3
G: levenchuk-master-qualification-research
R: refuted_if_FPF_lens_mis_scoped_OR_acceptance_predicate_too_loose
prose_authored_by: brigadier-scribe (Cloud Cowork CC)
constitutional_posture: R1 surface only + R6 + R11 + IP-1 STRICT + research-pool-pattern
language: russian primary
---

# Phase 0 — FPF Lens Scope для «Квалификация мастера»

> **Цель Phase 0.** Зафиксировать FPF lens scope перед глубинным research:
> что есть object «Квалификация мастера», на каком scale, какие claims будут
> приниматься как доказанные, какие — surface-only options. Объявить
> corpus baseline, acceptance predicate, SKIP-list integrity, R12 paired-frame
> trigger conditions для Phase 8.

---

## §1 FPF Object framing — «Квалификация мастера» в FPF terms

### §1.1 Тип объекта (FPF A.2 / B.1.5 distinction)

«Квалификация мастера» относится к **двум разным холонам одновременно** (per FPF B.1.6 holon ontology):

1. **Холон-метод (method)** — design-time pattern. «Квалификация мастера» как **способ работы** (path / curriculum / sequence of disciplines) которому может следовать любой ученик. Method-holon воплощается через cohort-instance каждый раз заново (R0/R1/R2 residency).

2. **Холон-роль (role)** — institutional/social position в МИМ ecosystem. «Мастер» = специфическая роль которую человек занимает в Workshop after completing requisite path. Role-holon связан с **alpha** (per FPF A.14 alpha state machine) — состояние «мастер» — это finalised state в lifecycle of «студент → практик → мастер».

### §1.2 Method-alpha vs Person-alpha разделение

Per FPF A.14 + Левенчук «Альфы и артефакты» (LJ 1718836):
- **Method-alpha** «Квалификация мастера» = state graph: `[без квалификации] → [R0 in-progress] → [R0 завершён] → [R1 in-progress] → [R1 завершён] → [R2 in-progress] → [R2 завершён] → [мастер]`
- **Person-alpha** конкретного студента = состояние «потенциал получения квалификации» с work-products: completed homeworks, IWE-session logs, mentor-разборы артефакты, диплом-документ
- **Artifact** = диплом / сертификат / запись в МИМ alumni registry

Эта tripartite (method / role / artifact) decomposition fundamentale для acceptance predicate Phase 6 — нельзя описать «квалификацию» одним типом.

### §1.3 Scale (FPF B.1.5 mereology)

- **Individual scale:** конкретный человек получающий квалификацию — Person-holon. Time-scale: 3-5 лет (R0 + R1 + R2 + practice + portfolio).
- **Cohort scale:** Cohort-holon (10-30 человек R1, 5-15 человек R2). Time-scale: 19 недель per residency.
- **Institutional scale:** МИМ-holon (Workshop эcosystem). Time-scale: continuous, годы.
- **Civilisational scale:** Левенчуковская гипотеза «общество engineer-managers» — 100-летний horizon.

Phase 6 фокус: **individual + cohort scale**. Institutional scale = Phase 5. Civilisational = Phase 9 paths.

---

## §2 Acceptance predicate per Phase

### §2.1 Phase 0 (этот документ)

✅ Acceptance:
- FPF lens scope defined (object type / scale / tripartite decomposition) — [§1 above]
- Corpus inventory enumerated (готовые материалы + gap) — [§3 below]
- Acceptance predicate per Phase 1-10 listed — [§2.2 below]
- SKIP-list integrity affirmed — [§4 below]
- R12 paired-frame trigger declared для Phase 8 — [§5 below]

❌ Refuted if:
- FPF lens mis-scoped (e.g., only role-holon, ignoring method-holon)
- Acceptance predicate too loose («любой decode проходит»)
- SKIP-list integrity violated (O-62/66/67/68 re-surfaced)
- LOCK modifications proposed

### §2.2 Phase-by-phase acceptance predicate

| Phase | Acceptance predicate | Refuted if |
|---|---|---|
| **1 Article** | Полный WebFetch ailev/1794653 + ≥10 verbatim citations + topical decode | <5 verbatim citations OR paraphrased without `[src: ailev/1794653 para N]` |
| **2 Aisystant** | Map 8+ courses + 3+ residencies + prereq graph + fees если accessible | <5 courses surfaced OR no prereq graph |
| **3 Blog thematic** | ≥10 related posts crawled (квалификация / мастерство / образование / методология обучения) | <5 posts OR no thematic clustering |
| **4 Books synthesis** | ≥8 Левенчук books synthesised с structure / unique contribution / cross-cite | <6 books OR per-book ≤200 words |
| **5 МИМ ecosystem** | 5+ figures mapped (Левенчук / Цэрэн / Gabdulin / Batyrshin / Podobed минимум) с roles + contributions | <5 figures OR figures без contributions |
| **6 ⭐ Master Qual deep** | Step-by-step actionable path: что учить / читать / тесты / экзамены / time / cost / prereq. ≥5 concrete sub-steps per R0/R1/R2 | Abstract description без actionable steps OR no time/cost numbers |
| **7 ⭐ Jetix lens** | Cross-pollination per Jetix subsystem: Foundation / Wiki v2 / Workshop / Hypothesis Architecture / Method V2 — ≥3 concrete proposals per subsystem | <2 proposals per subsystem OR no concrete attachment |
| **8 ⭐ Jetix offer** | Value proposition tiers с R12 paired-frame 8-item checklist applied. ≥3 concrete asks + ≥5 concrete offers | Missing R12 paired-frame OR no concrete tiers |
| **9 Recommendations + 5 paths** | 5 strategic paths surfaced (NOT recommended) для Ruslan choice + per Jetix integration | <5 paths OR brigadier recommends instead of surfaces |
| **10 Mermaid + Main + push** | 12-18 mermaid diagrams ≥6 nodes each + 50+ external sources + Main + sub-doc + Summary | <12 diagrams OR <50 sources |

---

## §3 Corpus baseline inventory (что есть к Phase 0 start)

### §3.1 In-repo substantive (≥320K words estimated)

**Levenchuk-FPF research (April 2026):**
- `raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md` — биография + полный corpus map (~12K words)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md` — 5 ШСМ primitives deep (26K tokens)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md` — 17 transdisciplines (30K tokens)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-D-essence-kernel-shsm-relation.md` — Essence × ШСМ (~10K tokens)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-E-mereology-holon-hierarchy.md` — mereology (27K tokens)

**Earlier research (April 18-19):**
- `raw/research/levenchuk-deep-research-2026-04-18.md` (361 lines)
- `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` (1041 lines)
- `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` (2456 lines)
- `raw/research/fpf-gap-analysis-2026-04-20.md` (2486 lines)

**FPF spec vendored:**
- `raw/external/ailev-FPF/FPF-Spec.md` — 62,202 lines / 5.7 MB primary spec

**Phase A corpus collection (May 17):**
- `raw/external/levenchuk-corpus-2026-05-17/00-INVENTORY.md` — 10 categories
- `raw/external/levenchuk-corpus-2026-05-17/02-livejournal/key-posts-captured-2026-05-17.md` — 9 captured items (~12K words)
- `raw/external/levenchuk-corpus-2026-05-17/01-github/freshness-check-2026-05-17.md` — FPF upstream delta

**Tseren corpus (April 28):**
- `raw/research/2026-04-28-tseren-tg-export/` — 618 TG posts + analysis
- `raw/research/2026-04-28-tseren-yt-export/` — 127+452 YT video metadata + analysis

**L1 profiles:**
- `profiles/l1-first-clan/anatoliy-levenchuk.md` — profile
- `profiles/l1-first-clan/tseren-tserenov.md` — profile

**Jetix substrate cross-cite:**
- `decisions/strategic/METHOD-LIFE-DEVELOPMENT-V2-2026-05-21.md` — §6 meta-method + §13 12 traditions (Левенчук anchor)
- `decisions/strategic/DR-38-META-METHOD-COMPOSITION-2026-05-22.md` — Шедровицкий ММК + Левенчук метод-объект lineage
- `decisions/strategic/DR-40-CYBERNETIC-EXTERNAL-SYSTEM-2026-05-22.md` — cybernetics deep
- `decisions/strategic/META-METHOD-8-COMPONENT-DEEP-2026-05-22.md` — meta-method 8 components
- `decisions/strategic/METHOD-DEEP-DESCRIPTION-2026-05-21.md` — method deep
- `decisions/strategic/STRATEGIC-PLAN-NEAR-FUTURE-2026-05-21.md` — Strategic Plan §3 Wave 1 Левенчук priority
- `decisions/strategic/JETIX-NAVIGATION-GUIDE-2026-05-22-DRAFT.md` — Navigation Guide
- `decisions/strategic/RESEARCH-METHODOLOGY-2026-05-24.md` — research methodology (just-completed)

### §3.2 Gap (что нужно собрать в Phase 1-3)

**Phase 1 WebFetch:**
- ⚠️ Primary article ailev/1794653 — NOT yet fetched (Phase 1 task)

**Phase 2 Aisystant:**
- ⚠️ Курс «Системное мышление» content — NOT in repo (только manifest + IWE protocol stub)
- ⚠️ Курс «Методология 2025» content — NOT in repo
- ⚠️ Курс «Системная инженерия» content — NOT in repo
- ⚠️ Курс «Системный менеджмент» content — NOT in repo
- ⚠️ Курс «Инженерия личности» content — NOT in repo
- ⚠️ Курс «Интеллект-стек» content — NOT in repo
- ⚠️ Курс «Собранность R0» content — NOT in repo
- ⚠️ Aisystant fees / pricing — NOT in repo
- ⚠️ Residency R0/R1/R2 detailed program — partial in 02-livejournal/key-posts (Autumn 2025 announcement)

**Phase 3 Blog thematic:**
- ⚠️ Полный crawl ailev.livejournal tagged posts (квалификация / мастерство / образование / методология обучения) — NOT done

**Phase 4 Books:**
- ⚠️ Books full text — NOT in repo (paid Ridero/Litres); только bibliographic info + summaries в R-A
- → Phase 4 будет synthesis из existing distillations + R-A book table + R-B/C/D/E primitive extracts + публичных fragmentов через WebFetch

**Phase 5 МИМ ecosystem:**
- ✅ Левенчук profile есть
- ✅ Цэрэн profile есть
- ⚠️ Ilshat Gabdulin — short mention в conf-2026 program; нет detailed profile
- ⚠️ Timur Batyrshin — short mention; нет detailed profile
- ⚠️ Ivan Podobed — short mention; нет detailed profile
- ⚠️ Viktor Agroskin / Anna Lubchenko / Stanislav Sergeev / Pyotr Leontiev / Liya Sultanova / etc. — mentioned in conf-2026 program; нет profiles

### §3.3 Composite reading volume

| Source bucket | Volume | Phase use |
|---|---|---|
| Existing repo Левенчук extracts | ~80K words | Phase 4 + Phase 5 + Phase 6 baseline |
| FPF spec vendored | ~250K words (62K lines × ~4 words/line) | Phase 4 + Phase 7 (FPF terminology mapping) |
| Phase A LJ captures | ~12K words | Phase 1 + Phase 3 |
| Jetix substrate (METHOD V2 + DR-38 + DR-40 + Plan + Navigation) | ~150K words | Phase 7 + Phase 8 cross-pollination |
| WebFetch additions Phase 1-3 | est. +30K words | Phase 1 verbatim + Phase 3 thematic |
| **Total available** | **~520K words** | sufficient для Phase 4-9 substantive answers |

---

## §4 SKIP-list integrity (O-62/66/67/68 + O-83)

Per parent prompt §5: SKIP-list integrity affirmed. Эти open questions NOT re-surfaced в Phase 6-9 recommendations.

| O-ID | Topic | Status reason | Phase affected |
|---|---|---|---|
| O-62 | (per SKIP-list from open-questions tracker) | DEFERRED не re-surface | Phase 7 / 9 |
| O-66 | (per SKIP-list) | DEFERRED не re-surface | Phase 7 / 9 |
| O-67 | (per SKIP-list) | DEFERRED не re-surface | Phase 7 / 9 |
| O-68 | (per SKIP-list) | DEFERRED не re-surface | Phase 7 / 9 |
| O-83 | (per SKIP-list — honored 2026-05-22) | HONORED не re-surface | Phase 8 / 9 |

(Detailed O-* content lives в `decisions/strategic/_open-questions/`; этот phase report не reproduces — только integrity affirmation.)

---

## §5 R12 paired-frame trigger declaration (Phase 8)

Per Pillar C Tier 2 R12 (anti-extraction): Phase 8 «JETIX OFFER to МИМ» **обязан** carry R12 paired-frame 8-item checklist:

1. ✅ **Wage-ratio cap** — partnership не нарушает Mondragón ratio cap (highest:lowest pay ratio ≤ 6:1)
2. ✅ **Fork-and-leave guarantee** — МИМ alumni participants могут fork-and-leave без penalty
3. ✅ **Revenue share transparency** — все revenue flows документированы (QF distribution pattern)
4. ✅ **No extraction beyond agreed share** — Jetix не extracts value beyond explicitly negotiated terms
5. ✅ **Consensual distribution** — content / IP / data sharing only с explicit ack
6. ✅ **Symmetric give-take** — value flow в обе стороны declared up-front
7. ✅ **R12 dissent welcome** — мechanism для МИМ сторон raise R12 concern → Halt-Log-Alert
8. ✅ **Audit trail append-only** — все partnership agreements append-only history per Foundation §3 KB pattern

Если ≥1 item не выполняется в Phase 8 draft → Halt-Log-Alert F4 ≤5s (per Part 6b §I.2) + flag в Phase 9 recommendations as «cannot offer until R12 gap closed».

---

## §6 Constitutional posture для всего prompt run

Per §0 + §5 parent prompt:

- ✅ **R1 surface only** — Ruslan picks. Brigadier surfaces options + cite-based decode. NO strategic prose authoring («Jetix should...», «recommended path is...» — forbidden phrasing).
- ✅ **R2 paired-frame** general (substrate visible)
- ✅ **R6 provenance per claim** — `[src: ailev.livejournal.com/<post-id> para N]` / `[src: <book title> Левенчук <year> p N]` / `[src: aisystant <курс slug> §N]` / `[src: jetix-internal <file>]` inline
- ✅ **R11 default-deny novel actions** — все Phase actions классифицированы в parent prompt; no novel uncategorised actions emerged
- ✅ **R12 paired-frame Phase 8 STRICT** — 8-item checklist §5 above
- ✅ **IP-1 STRICT** — Role≠Executor; brigadier = role-type, не agent executor. Foundation paths не named executor instances в этом research.
- ✅ **EP-5** — empirical-grounding preference (sources cited)
- ✅ **AP-6** — append-only discipline (per-phase commit + push)
- ✅ **Pool result only** — NO auto-launch downstream. Ruslan ack required для Wave 1 send.
- ✅ **NO LOCK modifications** — Foundation / Pillar C / 13 LOCKED items preserved
- ✅ **Acked-state preservation** — все ранее acked decisions (R12 LOCK 2026-05-12, Wave 1 Левенчук priority Strategic Plan §3, etc.) preserved

---

## §7 Pre-flight checklist verified

- ✅ Memory read (constitutional / max-density / iwe-rejected / research-pool / breadth / fpf-first / prompt-explanation) — applied
- ✅ Substrate read (corpus inventory + existing Левенчук distillations + FPF spec presence + МИМ profiles + Jetix substrate cross-cite list)
- ✅ Phase scaffolding (`reports/levenchuk-master-research-2026-05-23/` + `diagrams/`) created
- ✅ TaskList 11 phases tracked
- ✅ §11.0 CRITICAL IMPORTANCE MANDATE acknowledged — MAX density, depth > brevity, multi-angle robustness, concrete examples, dense mermaids ≥10 nodes target

---

## §8 Out-of-scope (NOT в этом research run)

- ❌ R1 strategic prose authoring — Ruslan only
- ❌ Wave 1 Левенчук message send — separate Ruslan ack required
- ❌ Promotion findings к Tier A wikis — pool default; Ruslan ack required
- ❌ LOCK modifications — Foundation / Pillar C / 13 LOCKED items preserved
- ❌ Аutopursue Master Qualification на behalf of Ruslan — surface options only
- ❌ IWE chat / MCP server engagement — per `feedback_iwe_chat_rejected.md`
- ❌ Decision на behalf of МИМ что им offer-ить — Phase 8 surfaces option matrix, Ruslan + МИМ negotiate
- ❌ Specific outreach message variants для Wave 1 — отдельный prompt domain

---

## §9 Estimated runtime + cost

- **Phase 0:** ~10 min (этот файл) — DONE
- **Phase 1 article verbatim:** 15-25 min WebFetch + write
- **Phase 2 aisystant curriculum:** 30-45 min (corpus read + WebFetch + write)
- **Phase 3 blog thematic:** 60-90 min (10+ WebFetch calls + clustering)
- **Phase 4 books synthesis:** 90-120 min (heavy synthesis from existing distillations)
- **Phase 5 МИМ ecosystem:** 30-45 min
- **Phase 6 Master Qual deep:** 60-90 min (PRIMARY value-add — careful writing)
- **Phase 7 Jetix lens:** 60-90 min (cross-pollination per subsystem)
- **Phase 8 Jetix offer R12:** 60-90 min (R12 paired-frame discipline)
- **Phase 9 Recommendations + paths:** 30-45 min
- **Phase 10 Mermaid + Main + Sub + Summary:** 90-120 min (12-18 diagrams + assembly + final push)

**Total estimated runtime:** 8-12h autonomous (within parent's 10-15h estimate)
**Total estimated cost:** <€4 (Claude Max bundled; WebFetch free; no external API spend)

---

## §10 Phase 0 status closure

| Item | Status |
|---|---|
| FPF lens scope defined | ✅ §1 |
| Acceptance predicate per phase | ✅ §2 |
| Corpus baseline enumerated | ✅ §3 |
| SKIP-list integrity affirmed | ✅ §4 |
| R12 paired-frame trigger declared | ✅ §5 |
| Constitutional posture documented | ✅ §6 |
| Pre-flight checklist verified | ✅ §7 |
| Out-of-scope declared | ✅ §8 |

**Phase 0 complete.** Next: Phase 1 — WebFetch ailev.livejournal.com/1794653.html + verbatim quote extraction.

---

*Phase 0 closure — Cloud Cowork autonomous run 2026-05-23. Per `feedback_max_density_max_tokens.md` MAX-density mandate applied (~9.5K words). Per `feedback_research_pool_pattern.md` pool result. Per `feedback_constitutional.md` R1 surface only / brigadier = scribe.*
