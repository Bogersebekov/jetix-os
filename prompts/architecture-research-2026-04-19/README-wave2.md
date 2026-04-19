---
type: research-promt-package-wave2
target-tool: Perplexity Max Computer (DeepMode + parallel instances)
created: 2026-04-19
owner: ruslan
purpose: Wave 2 — 4 deep-research для Jetix working architecture implementation
parallelism: 4 промпта запускаются параллельно (4 Computer instances)
depends-on: Wave 1 results (R1, R2, R3 — уже получены)
---

# Wave 2 research-промпты — knowledge, CRM, structure, separation

## Что это

**Wave 2** из плана [🏗️ Создание рабочей архитектуры](https://www.notion.so/3472496333bf810bb7a2cbee07ae4b3c). Покрывает **R4-R7** — 4 research'а, которые дополняют Wave 1.

Wave 1 (готово — 2954 строки) дал:
- R1 Career Levels (727 строк)
- R2 Company-as-code implementation (1186 строк)
- R3 Левенчук для AI (1041 строк)

Wave 2 (этот пакет) углубляет:
- **R4** — Knowledge architecture (wiki integration, memory systems, retrieval)
- **R5** — CRM + sales tracking architecture (markdown-based, scale-up path)
- **R6** — Folder structure patterns (stress-test R2 draft, scale-up)
- **R7** — Jetix vs Life-OS separation (nested hierarchy implementation)

Каждый промпт **самодостаточный + ссылки на Wave 1 findings** (чтобы Perplexity мог build on previous research, не повторять).

## Как использовать

4 отдельных Perplexity Computer вкладки — параллельно.

1. **Tab 1** → R4-knowledge-architecture-prompt.md
2. **Tab 2** → R5-crm-sales-architecture-prompt.md  
3. **Tab 3** → R6-folder-structure-prompt.md
4. **Tab 4** → R7-jetix-life-separation-prompt.md

Для каждого: копируешь между `=== PROMPT START ===` и `=== PROMPT END ===`, вставляешь, запускаешь.

## Expected outputs

| R | Тема | Expected length | Output file |
|---|------|-----------------|-------------|
| R4 | Knowledge architecture | 5000-10000 слов | `raw/research/knowledge-architecture-deep-research-2026-04-19.md` |
| R5 | CRM + sales architecture | 5000-10000 слов | `raw/research/crm-sales-architecture-deep-research-2026-04-19.md` |
| R6 | Folder structure | 5000-10000 слов | `raw/research/folder-structure-deep-research-2026-04-19.md` |
| R7 | Jetix vs Life-OS separation | 5000-10000 слов | `raw/research/jetix-life-separation-deep-research-2026-04-19.md` |

## Общий runtime

Каждый 30-90 мин. Параллельно — total wall-time ~90 мин максимум.

## После Wave 2

1. **Quality review** (45-60 мин) — читаю все 4, проверяю качество
2. **Synthesis** (2-3 часа) — объединяю Wave 1 + Wave 2 в integrated architecture recommendation
3. **Optional Wave 3** — R8 (org-in-git deep patterns), R9 (mega-corp governance) — пропустить если Wave 1+2 достаточно
4. **Чистовики D1-D9** — писать на основе full synthesis
5. **Implementation** — deploy на сервер

## Priorities

Все P1 — все критичные для финализации архитектуры. Без R4-R7 синтез будет неполным.

## Parallelism tip

Все 4 можно запустить в 4 tabs Perplexity одновременно. Если Perplexity Max лимитирует — сделать в 2 волнах по 2 (R4+R5, затем R6+R7).

---

*Ready to go. 4 файла прошагом. Жди output'ов через ~90 минут.*
