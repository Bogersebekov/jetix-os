---
type: research-promt-package
target-tool: Perplexity Max Computer (DeepMode + parallel instances)
created: 2026-04-19
owner: ruslan
purpose: Wave 1 — 3 deep-research для Jetix working architecture implementation
quality: академический уровень, extensive citations, peer-reviewed where possible
parallelism: 3 промпта запускаются параллельно (3 Computer instances)
context-anchor: design/JETIX-ARCHITECTURE-WORKING.md v0.9 + Notion Шаг 2 + previous synthesis
---

# Wave 1 research-промпты — архитектурная реализация Jetix

## Что это

Три глубоких research-промпта для **Perplexity Max Computer** (subscription
$200/мес, агентский режим). Это **Wave 1** из плана
[🏗️ Создание рабочей архитектуры](https://www.notion.so/3472496333bf810bb7a2cbee07ae4b3c),
pокрывает research-волны R1, R2, R3.

Каждый промпт — **самодостаточный**: весь необходимый контекст Jetix встроен
внутрь, чтобы Perplexity Computer мог работать без доступа к нашим внутренним
документам.

## Как использовать

1. **Открой файл** для одного из R1/R2/R3
2. **Прокрути вниз до раздела `=== PROMPT START ===`**
3. **Скопируй весь текст** между `=== PROMPT START ===` и `=== PROMPT END ===`
4. **Открой новую Perplexity Computer instance** (новая вкладка / новый диалог)
5. **Вставь скопированный промпт** и запусти
6. **Повтори для R2 и R3 в параллельных вкладках** — они независимы друг от друга
7. **Жди результаты** (30-60 минут на каждый)
8. **Скачай отчёты** → перекинь на сервер в `raw/research/` с именами:
   - `career-levels-deep-research-2026-04-19.md` (R1)
   - `company-as-code-impl-deep-research-2026-04-19.md` (R2)
   - `levenchuk-for-ai-deep-research-2026-04-19.md` (R3)

## Общий контекст Jetix (встроен в каждый промпт)

Каждый промпт начинается с **Context Block** где описано:

- Кто Jetix и что строим
- Текущая концептуальная архитектура (7 слоёв + L0 + ритмы + 5 тезисов)
- Принцип Nested hierarchy (Life-OS root, Jetix = проект внутри)
- Mega-corporation scale-up-first design (не solo)
- Human+AI executors через единую role-abstraction
- Текущие технологии (GitHub + Hetzner + Claude Code)

Это означает **длинные промпты** (~2000-3000 слов контекст + 3000-5000 слов
конкретные вопросы). Perplexity Computer справляется.

## Критерии качества (применяется ко всем трём)

- **Академический уровень** — peer-reviewed articles где возможно, primary
  sources (книги в оригинале), industry reports, expert conferences
- **Extensive citations** — каждый ключевой факт с источником, предпочтительно
  с прямой ссылкой на материал
- **Non-generic** — не «есть senior и junior», а детальный breakdown
  obligations / decision-rights / time-in-role per level
- **Actionable для Jetix** — каждая секция заканчивается «что из этого
  применимо к Jetix и как конкретно»
- **Honest about uncertainty** — где данных нет, явно указать «мало данных»,
  не fabricate

## Ожидаемые deliverables

| R | Тема | Expected length | Output file |
|---|------|-----------------|-------------|
| R1 | Corporate career levels + делегирование | 5000-10000 слов | `raw/research/career-levels-deep-research-2026-04-19.md` |
| R2 | Company-as-code implementation | 5000-10000 слов | `raw/research/company-as-code-impl-deep-research-2026-04-19.md` |
| R3 | Левенчук / ШСМ для AI-агентов | 5000-10000 слов | `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` |

## После получения всех трёх

1. Ruslan ревьюет качество (30-45 мин каждое)
2. Если какое-то слабое — follow-up refinement промпт
3. Переход к Wave 2 (R4-R7 — knowledge architecture, CRM, folder structure, Life-OS separation)

## Параллелизация

Все три независимы. Запуск одновременно в 3 отдельных Perplexity Computer
instances. Тестирует собственный scale-out Ruslan'а — «насколько возможно
выжать Perplexity Max на 300%».

---

*README для пакета Wave 1. Файлы промптов:*
- *[R1-career-levels-prompt.md](R1-career-levels-prompt.md)*
- *[R2-company-as-code-impl-prompt.md](R2-company-as-code-impl-prompt.md)*
- *[R3-levenchuk-ai-prompt.md](R3-levenchuk-ai-prompt.md)*
