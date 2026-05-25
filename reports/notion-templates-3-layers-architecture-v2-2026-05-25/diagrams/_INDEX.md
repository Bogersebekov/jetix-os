---
title: Diagrams INDEX — Notion 3-Layers Architecture v2 (ARCH-V2-1..9)
date: 2026-05-25
type: diagrams-catalog
parent_main: decisions/strategic/NOTION-TEMPLATES-3-LAYERS-ARCHITECTURE-V2-2026-05-25.md
suite_source: reports/notion-templates-3-layers-architecture-v2-2026-05-25/12-mermaid-suite.md
language: russian primary
---

# Diagrams INDEX — ARCH-V2-1..ARCH-V2-9

Все 9 схем v2 живут inline в `../12-mermaid-suite.md` и встроены в main `§9`. Это каталог-указатель
(append-only). Mermaid рендерится в Notion и GitHub; рисунки не экспортируются в PNG (R11 — спека, не реализация).

| ID | Тема | Тип | Где введён | Палитра |
|---|---|---|---|---|
| **ARCH-V2-1** | стек 3 слоёв (standalone-capable) | flowchart TB | Phase 1 (`02-overview`) | 🟢🔵🟠🟣 |
| **ARCH-V2-2** | fast-connect механика (3 сценария) | flowchart LR | Phase 1 (`02-overview`) | 🟢🔵🟠 |
| **ARCH-V2-3** | потоки данных (opt-in) | flowchart TB | Phase 6 (`07-cross-layer`) | 🟢🔵🟠🔴 |
| **ARCH-V2-4** | матрица прав (4 уровня, IP-1) | flowchart LR | Phase 6 (`07-cross-layer`) | 🟡🔵 |
| **ARCH-V2-5** | L2 Generic vs Jetix overlay split | flowchart TB | Phase 11 (`12-mermaid-suite`) | 🔵🟠🟣🟢 |
| **ARCH-V2-6** | implementation timeline Build/Run/Scale | flowchart LR | Phase 11 | 🟢🟡🟠 |
| **ARCH-V2-7** | AI Tools mega-page hub (4 кластера) | flowchart TB | Phase 11 | 🟣🔵 |
| **ARCH-V2-8** | R12 risk overlay (растёт со слоем) | flowchart LR | Phase 11 | 🟢🟡🔴🔵 |
| **ARCH-V2-9** | master synthesis (3 слоя + companion) | flowchart TB | Phase 11 | 🟢🔵🟠🟣 |

## Конвенции

- **Theme-init инвариант:** каждая схема открывается одним `%%{init...}%%` блоком с чёрным текстом
  (`primaryTextColor/textColor = #000000`) — читается в Notion light-theme и GitHub.
- **Палитра по слоям:** 🟢 зелёный = Layer 1 · 🔵 синий = Layer 2 · 🟠 оранжевый = Layer 3 ·
  🟣 фиолетовый = AI Tools companion · 🔴 красный = приватность / R12-high · 🟡 жёлтый = доступ/Run.
- **v1 → v2:** v1 имел 10 схем (ARCH-1..10) в `../../notion-templates-4-layers-architecture-2026-05-25/diagrams/`.
  v2 = 9 схем (ARCH-V2-*) — на одну меньше (4 слоя → 3 слоя; добавлены AI Tools hub + Generic/Jetix split).

*INDEX closure. 9 схем; единый theme-init; палитра по слоям. Источник — `../12-mermaid-suite.md`.*
