---
title: Phase 0 — Pre-flight + FPF lens scope + substrate inventory
date: 2026-05-24
type: execution-plan-fixation-phase-output
phase: 0
parent_prompt: prompts/execution-plan-fixation-2026-05-24.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
F: F2
G: execution-plan-fixation
R: refuted_if_substrate_unverified
constitutional_posture: R1 surface only + R2 STRICT + R6 + R11 + R12 paired-frame + IP-1 STRICT + append-only
language: russian primary
---

# Phase 0 — Pre-flight + substrate inventory

> Проверка перед запуском: что прочитано, в каком режиме работаем, какие границы держим.
> Это технический файл — не для чтения Русланом. Содержательное начинается с Phase 1.

---

## §0.1 Режим работы (mode)

**EXECUTION-PLAN SYNTHESIS** — собираем существующий substrate в один execution-oriented
документ. НЕ новый ресёрч. НЕ авторим стратегическую прозу за Руслана. Surface + sequencing.

Mode shift зафиксирован: research/exploration → production/execution (per O-160 dev→promotion).

---

## §0.2 Memory read

Прочитаны фактически присутствующие memory-файлы:

- `MEMORY.md` (index)
- `feedback_plan_mode_minimal_friction.md` — это autonomous-execution prompt (не Plan Mode),
  поэтому: per-phase commit+push без granular approval dialog. Прямое исполнение.
- `feedback_no_api_keys.md` — built-in tools only; никаких ANTHROPIC_API_KEY / GROQ_API_KEY вызовов.
- `project_balaji_outreach_target.md` — Balaji Phase 2+ deferred (не в scope этого цикла).

**Note (provenance honesty):** prompt §0 ссылается на 6 memory-файлов
(`feedback_constitutional`, `feedback_max_density_max_tokens`,
`feedback_research_pool_pattern`, `feedback_prompt_explanation_required`,
`feedback_fpf_lens_first`, `feedback_no_unsolicited_alternatives`), которых физически
нет в `memory/`. Их принципы применяются из самого prompt'а (он явно их разворачивает в
§0.1 + §13 + §14): R1 surface only / MAX-density через concreteness / pool-result /
FPF-lens-first / facts-not-recommendations. Поведенчески это покрыто.

---

## §0.3 FPF lens scope verification (обязательно per prompt §0)

Какие FPF / constitutional границы активны в этом цикле и как они переводятся на человеческий:

| Lens | На внутреннем | На человеческом (что это значит для документа) |
|---|---|---|
| **R1** | AI не стратегирует | Руслан выбирает финальную рамку видео, финальный список партнёров, формулировки. Документ surface'ит варианты, не решает за него. |
| **R2 STRICT** | No Foundation modifications | Не трогаем `swarm/wiki/foundations/`, `principles/`, `shared/schemas/`, LOCKED canonical. |
| **R6** | Provenance per claim | Cross-refs к substrate — но в footnotes / отдельной секции, не inline mid-prose (чтобы текст остался человеческим). |
| **R11** | Default-Deny novel actions | Никаких auto-launch: видео не записываются, outreach не отправляется, templates не создаются. Всё = план. |
| **R12 paired-frame** | Anti-extraction + influence-ethics receiver | Phase 3 + Phase 4 (партнёрский outreach) — каждый тип партнёров проходит 8-item R12 audit. На человеческом: «не доим, не запираем, не манипулируем». |
| **IP-1 STRICT** | Role ≠ Executor | Имена (Maxim / Oleg / Дмитрий / Левенчук / Цэрэн / Прапион) = **примеры** ролей-типов, НЕ executor-bindings в Foundation-путях. В этом документе они живут как кандидаты-примеры, не как назначенные исполнители. |
| **EP-5** | F2 substrate + F3 derivative | Документ = F2-F3 (синтез из существующего acked substrate). |
| **AP-6** | Dissent preservation | Type 4 deferred path + contingent branches сохраняются как валидные ветки, не вычёркиваются. |
| **Append-only** | — | Новое сверху в логах; ничего не переписываем. |

---

## §0.4 Substrate inventory (что прочитано / verified exists)

Все parent_substrate документы verified присутствуют на диске:

| Документ | Размер | Роль в этом цикле |
|---|---|---|
| `CONSOLIDATED-HUMAN-LANGUAGE-PLAN-2026-05-24.md` | 32K | **Baseline** — план обучения, который фиксируем «идём воплощать» |
| `reports/consolidated-human-language-plan-2026-05-24/01-05*.md` | — | Детальные части baseline (кого берём / чему учим / порядок / прошивка / mermaid) |
| `OUTREACH-CONTENT-OUTCOMES-CTAS-2026-05-24.md` | 31K | **CTA-каталог** (13 + CTA-NULL) + Bloom 7-stage + 5-category anti-CTAs + per-archetype |
| `PLAN-MODE-DOCS-VIDEO-NOTION-2026-05-24.md` | 23K | Plan A Video / Plan B Docs / Plan C Notion — источник для Ruslan-solo scope |
| `RESEARCH-EDUCATION-2026-05-24.md` | 26K | Образовательная парадигма детально |
| `SYNTHESIS-EXECUTION-PLANS-2026-05-24.md` | 26K | Синтез execution-планов (3-week Option 3 Mixed) |
| `RUSLAN-NOTES-EDUCATION-PARADIGM-2026-05-24.md` | 16K | Голос Руслана verbatim + O-176..O-185 (adequate intellect / anti-cheat) |
| `POINT-B-FOCUSED-WEEK-1-2026-05-23.md` | 22K | **Sequencing источник** — 8 шагов Week-1 (видео → сайт → Notion → Дмитрий → Сева) |
| `POINT-B-NEAR-TARGET-2026-05-23.md` | 32K | Описание ближней цели (Point B) |
| `POINT-A-CURRENT-STATE-2026-05-23.md` | 30K | Текущее состояние (Point A) |
| `TASK-A-EXISTING-DOCS-INVENTORY-2026-05-24.md` | 18K | Инвентарь существующих документов |
| `LEVENCHUK-MASTER-QUALIFICATION-RESEARCH-2026-05-23.md` | 21K | **Phase 8 fast-access network** — МИМ 12 figures + 5 Wave-1 candidates + 7 program variants |
| `PARTNER-OFFERING-HUMAN-LANG-2026-05-22.md` | — | **Style anchor** + деньги/тиры L1-L7 на человеческом |
| 4 LOCKED canonical | — | Method V2 / Strategic Plan / Economic V10 / AI Market PLAN — только ссылки, R2 STRICT |
| `crm/` 180 contacts | — | Кандидаты-примеры для 4-partner-type (R1 — Руслан picks) |

---

## §0.5 Извлечённые опорные точки (для Phases 2-5)

**CTA-каталог (из OUTREACH-CONTENT §, для Phase 4 per-type CTA):**

| CTA | Что | Stages | R12 |
|---|---|---|---|
| CTA-01 | Free explore (репо / вики) | 1-7 | PASS |
| CTA-02 | Subscribe | 1-7 | PASS |
| CTA-04 | Comment / question | 2-7 | PASS |
| CTA-05 | Discovery call 30-60 мин | 3-5 | PASS |
| CTA-06 | Donate | 3-7 | PASS |
| CTA-07 | Buy course / workshop | 4-7 | PASS conditional |
| CTA-08 | Trial cohort member (L6) | 5-6 | MEDIUM (Charter req) |
| CTA-09 | L5 partner | 6 | HIGH (R12 STRICT) |
| CTA-10 | L4 Founding partner | 6 | HIGH (3-stage consent) |
| CTA-11 | Co-create content | 6-7 | PASS |
| CTA-12 | Mass advocate / refer | 7 | MEDIUM (anti-MLM STRICT) |
| CTA-NULL | NO CTA (educational only) | 1-7 | PASS gold-standard |

**Имена-кандидаты (IP-1 — examples, не bindings):**

- **Maxim** — джедайские практики (T1 methodology образец)
- **Oleg** — trouble-shooters (T1 methodology образец)
- **Anatoly Левенчук** — canonical FPF + МИМ Managing Partner (T1/T2 mixed; substrate-sandwich pre-staged)
- **Цэрэн (Tseren)** — МИМ Managing Partner / e-government (T1/T2; 11-летнее партнёрство с Левенчуком)
- **Прапион Медведева** — Reformer + co-founder Кочерга (T1/T2; R12 bridge CRITICAL)
- **Ilshat Gabdulin** — AI-agents practice (T1; ROY synergy direct)
- **Ivan Podobed** — method engineering (T1; DR-38 anchor)
- **Дмитрий** — humanitarian-focused community (T3 audience tester, engaged 22.05)
- **Сева (Seva)** — crypto domain (T3 2nd Notion-trial candidate)
- **МИМ как institution** — (T2 resource — через Левенчук/Цэрэн)
- **Кочерга** — applied rationality community (T2 resource — через Прапион bridge)

**7 ступеней Bloom (из baseline, для всех phases):**
Узнаёшь (5-15м) → Понимаешь (1-3ч) → Применяешь (~неделя) → Анализируешь (звонок) →
Оцениваешь (1-4нед) → Создаёшь (3-12мес) → Передаёшь (постоянно).

---

## §0.6 Acceptance check для всего цикла

- [ ] 7 phases (0-6) per-phase commit+push (`[exec-plan] Phase N`)
- [ ] Plain language throughout — jargon только с переводом
- [ ] 5-6 mermaid (readable без extension, 8-20 nodes)
- [ ] Main doc ~8-12K слов в стиле PARTNER-OFFERING-HUMAN-LANG
- [ ] R1 surface only — 7 R1 decisions для Руслана
- [ ] R12 8-item audit per partner type
- [ ] NO LOCK modifications / NO auto-launch
- [ ] IP-1 STRICT — имена = примеры
- [ ] Append-only

**Phase 0 готов. Переход к Phase 1 — Anchor + fixation момент.**
