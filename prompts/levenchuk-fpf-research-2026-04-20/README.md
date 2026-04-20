---
type: research-prompt-package
target-tool: Perplexity Max Computer (DeepMode + parallel instances)
created: 2026-04-20
owner: ruslan
purpose: Knowledge base compilation для D6 JETIX-FPF.md (full Левенчук + FPF max depth)
quality: академический уровень, extensive citations, primary sources where possible
parallelism: 5 промптов запускаются параллельно (5 Computer instances если можно)
expected-output-size: 50-100 pages compiled knowledge base
---

# Левенчук + FPF Knowledge Base — 5 deep-research waves

## Что это

5 глубоких research-промптов для **Perplexity Max Computer** (subscription
$200/мес, агентский режим). Цель — собрать **comprehensive knowledge
base** про методологию Анатолия Левенчука (ШСМ + связанные дисциплины) +
FPF principles + applied frameworks для AI-native business.

Output этих researches → input для writing **D6 JETIX-FPF.md** (30-50
страниц constitutional document, full Левенчук max depth, no compromises).

## Как использовать

1. **Открой файл** для одного из R-A до R-E
2. **Прокрути вниз до `=== PROMPT START ===`**
3. **Скопируй весь текст** между `=== PROMPT START ===` и `=== PROMPT END ===`
4. **Открой новую Perplexity Computer instance** (вкладка / новый диалог)
5. **Вставь скопированный промпт** и запусти
6. **Повтори для R-B до R-E в параллельных вкладках** (независимы друг от друга)
7. **Жди результаты** (~45-90 мин каждый)
8. **Скачай отчёты** → push на сервер в `raw/research/levenchuk-fpf-research-2026-04-20/`:
   - `R-A-levenchuk-full-body-of-work.md`
   - `R-B-shsm-5-primitives-deep.md`
   - `R-C-17-trans-disciplines-mapping.md`
   - `R-D-essence-kernel-shsm-relation.md`
   - `R-E-mereology-holon-hierarchy.md`

## После всех 5 researches

Я compile эти 5 reports в single **`raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md`** —
unified reference для D6 writing.

Затем — Phase 2 plan: writing prompt для D6 → Claude Code на сервере →
verification pass.

## Общий контекст Jetix (встроен в каждый промпт)

Каждый prompt — **самодостаточный**: весь Jetix-context встроен внутрь,
чтобы Perplexity Computer мог работать без доступа к internal документам.
Если разные waves кажутся overlapping — это **по дизайну**: pereсечение
обеспечивает triangulation качества + охват разных angles.

## Quality criteria для каждого research

- **Primary sources first** (книги Левенчука, его курсы, official ШСМ материалы)
- **Citations to source material** (везде где возможно)
- **Academic-grade rigor** — peer-reviewed papers, authoritative books
- **Anti-hallucination** — если concept не verified в source — flag explicitly как "unverified"
- **Russian primary, English secondary** — Левенчук primarily Russian-language; English when sources allow
- **Structured output** — sections clear, tables где применимо, bullet lists для enumerations

## Файлы

- `R-A-levenchuk-full-body-of-work.md` — Левенчук как person + полный corpus работ
- `R-B-shsm-5-primitives-deep.md` — 5 примитивов ШСМ deep dive
- `R-C-17-trans-disciplines-mapping.md` — 17 trans-disciplines structure
- `R-D-essence-kernel-shsm-relation.md` — Essence Kernel + SEMAT адаптация ШСМ
- `R-E-mereology-holon-hierarchy.md` — мereology + холоны + applied к организациям
