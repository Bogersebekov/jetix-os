---
title: Diagrams INDEX — ARCH-1..ARCH-10 (Notion 4-Layers Architecture)
date: 2026-05-25
type: diagrams-index
parent_main: decisions/strategic/NOTION-TEMPLATES-4-LAYERS-ARCHITECTURE-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
language: russian primary
mermaid_count: 10
---

# 📐 Diagrams INDEX — ARCH-1..ARCH-10

> Каталог 10 схем архитектуры. Тела встроены inline в main doc + фазовые отчёты + Phase 13
> (`14-mermaid-suite.md`). Все light bg theme, ≥10-15 nodes.

| # | Схема | Тип | О чём | Тело (main §) | Тело (report) |
|---|---|---|---|---|---|
| **ARCH-1** | 4 layers stack | graph TB | стек 4 слоёв, overlay опционален | §1 | 02-overview-cross-layers + 14-mermaid-suite |
| **ARCH-2** | dependencies + inheritance | graph LR | зависимости L1→L2→L3, L4 standalone, overlay≠слой | §1 | 02-overview-cross-layers |
| **ARCH-3** | cross-layer data flows | graph TB | ⬆️opt-in/rollup ⬇️сигнал/контроль 🚫privacy | §6.1 | 07-cross-layer-data-flows |
| **ARCH-4** | permissions heat matrix | graph TB | концентрация прав L1→L4, Steward сквозной, R12 guard | §6.2 | 08-cross-layer-permissions |
| **ARCH-5** | sync mechanics | sequenceDiagram | родной Notion + 5 helper'ов, файлы=правда | §6.3 | 09-cross-layer-sync |
| **ARCH-6** | implementation timeline | gantt | Build→Run→Scale, L1+L4min→L2+L3→L4 full | §7 | 12-implementation-roadmap |
| **ARCH-7** | Layer 4 executive dashboard | graph TB | Command Center: 6 групп + брифинг 5 секций | §5.13 | 14-mermaid-suite |
| **ARCH-8** | R12 risk heat per layer | graph LR | риск растёт L1🟢→L4🔴, защита быстрее | §8 | 14-mermaid-suite + 13-r12-paired-frame-sweep |
| **ARCH-9** | fork-and-leave preservation | graph TD | 5-шаговый выход, gualtee архитектурна | §8 | 14-mermaid-suite |
| **ARCH-10** | master synthesis | graph TB | вся архитектура одной схемой | §9 | 14-mermaid-suite |

## Mermaid theme (для всех 10)

```
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000',
'lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa',
'edgeLabelBackground':'#ffffff'}}}%%
```

Light bg, чёрный текст — читаемо в Notion light mode + при экспорте в PDF/PNG.

## Покрытие (что показано)

- **Стек + зависимости:** ARCH-1, ARCH-2 (4 слоя, лестница, overlay).
- **Cross-layer механика:** ARCH-3 (потоки), ARCH-4 (права), ARCH-5 (синк).
- **Реализация:** ARCH-6 (таймлайн Build/Run/Scale).
- **Layer 4 deep:** ARCH-7 (executive dashboard).
- **R12 / этика:** ARCH-8 (risk heat), ARCH-9 (fork-and-leave).
- **Синтез:** ARCH-10 (вся архитектура).

---

*10 схем ARCH-1..ARCH-10. Phase 13 closure. Каждая встроена inline в main + соответствующий фазовый
отчёт. Тела всех 4 новых (ARCH-7..ARCH-10) + полный каталог — в `14-mermaid-suite.md`.*
