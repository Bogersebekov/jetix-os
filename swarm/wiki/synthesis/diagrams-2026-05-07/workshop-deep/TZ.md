---
title: TZ — Workshop / Information Flow Deep Version
date: 2026-05-08
type: tz-spec
purpose: deep version Workshop diagram — full information flow + people + tools + network + output cycle
parent_baseline: ../01-workshop-7-elements.md
audience: Цэрэн / Левенчук / Mittelstand partners
chosen_palette: Variant B (Pastel Warm Set2 — qualitative)
status: TZ approved (Ruslan voice transcript 2026-05-08)
---

# 🎯 TZ — Workshop / Information Flow Deep Diagram

## Главный message

Мастерская = живая система которая **превращает хаос внешней информации в осмысленные действия**, и эти действия влияют на внешний мир, который затем кормит мастерскую новой информацией. **Замкнутый цикл.**

---

## Layout

- **Left-to-right** (`flowchart LR`) — не сверху-вниз
- INPUT слева → WORKSHOP центр → OUTPUT справа → EXTERNAL WORLD дальше справа
- PHONE / OTHER WORKSHOPS — сбоку (top или bottom dock)
- **Feedback loop** — снизу через всю диаграмму обратно в INPUT (CIRCLE)

---

## Nodes detail

### 1. INPUT cluster (слева, что входит в мастерскую)

| Node | Role |
|---|---|
| Информация о мире | umbrella container |
| ↳ Статьи | sub-source |
| ↳ Видео | sub-source |
| ↳ Разговоры | sub-source (звонки / встречи) |
| ↳ Гипотезы / опыт | sub-source |

### 2. GUARD (entry filter, red accent)

| Node | Role |
|---|---|
| 🛡️ Охрана / фильтр входа | rejects spam / low-quality / distractions |

### 3. WORKSHOP внутренний слой

#### 3a. Substrate
| Node | Role |
|---|---|
| 🏗 Фундамент | substrate (git / naming / Foundation v1.0) |
| 📦 Склад | knowledge base (drafts / sources / artifacts) |

#### 3b. People cluster
| Node | Role |
|---|---|
| 👤 МАСТЕР | центр work, multi-роль (архитектор / исполнитель / арбитр / судья / дегустатор) |
| 🤖 AI-агенты | отдельная node — 12 ролей (Manager / Personal Assistant / Strategist / etc.) |
| 👥 Коллабораторы | отдельная node — human partners / mentors / ad-hoc helpers |

Master может **dial** к agents и collaborators.

#### 3c. Tools cluster (adaptable станки)
| Node | Role |
|---|---|
| 🔧 Mermaid | diagrams |
| 🔧 MCP | integrations |
| 🔧 Voice | pipeline transcribe/extract |
| 🔧 Plan Mode | strategic thinking |
| 🔧 ... | другие, добавляются за день |

#### 3d. Automation
| Node | Role |
|---|---|
| 🤖 Auto pipelines | cron / sync / scheduled — updates STORAGE автоматически |

### 4. NETWORK (network sidecar)

| Node | Role |
|---|---|
| 📞 Телефон | network interface |
| 🏭 Other workshops (×3-5) | другие мастерские (партнёры / коллеги-founders) |

**Связь:** PHONE ↔ OTHER WORKSHOPS bidirectional. Info from other workshops → comes back **через GUARD** → попадает в FOUNDATION (любая внешняя info фильтруется).

### 5. OUTPUT cluster (справа)

| Node | Role |
|---|---|
| 📤 OUTPUT umbrella | what мастерская produces |
| ↳ Решения | decisions logged |
| ↳ Артефакты | statтьи / видео / посты / документы |
| ↳ Действия | physical actions (transfers / outreach / hires) |

### 6. EXTERNAL WORLD (right far)

| Node | Role |
|---|---|
| 🌍 Внешний мир / жизнь | business / health / отношения / network / financial state |

### 7. Feedback loop (CIRCLE)

EXTERNAL WORLD → новая информация / feedback → обратно в INPUT (через нижнюю curve через всю диаграмму).

---

## Edges (связи)

| From | To | Type |
|---|---|---|
| INFO_SOURCES (multi) | GUARD | thick → |
| GUARD | FOUNDATION | → |
| FOUNDATION | STORAGE | → |
| STORAGE | MASTER | → |
| MASTER ↔ AGENTS | bidirectional | dashed if access |
| MASTER ↔ COLLABORATORS | bidirectional | |
| MASTER → TOOLS (multi) | uses | |
| TOOLS → AUTO | triggers | |
| AUTO -.-> STORAGE | updates | dashed |
| MASTER ↔ PHONE | reaches out | |
| PHONE ↔ OTHER_WORKSHOPS (multi) | network | |
| OTHER_WORKSHOPS info → GUARD | external info filtered | dashed back |
| MASTER → OUTPUT (multi) | produces | thick → |
| OUTPUT → EXTERNAL_WORLD | influences | thick → |
| EXTERNAL_WORLD -.-> INPUT_SOURCES | feedback / new info | dashed circle bottom |

---

## Palette (Variant B — Pastel Warm Set2 — APPROVED)

| Class | Fill | Stroke | Used for |
|---|---|---|---|
| `cloud` | `#f5f5f5` | `#999` | INPUT umbrella, sub-sources, OUTPUT items, EXTERNAL_WORLD |
| `guard` | `#e41a1c` | `#a00` | GUARD red accent |
| `foundation` | `#66c2a5` | `#2c7a5e` | FOUNDATION + STORAGE (substrate cluster green) |
| `master` | `#fc8d62` | `#a35332` | MASTER (high contrast orange, stroke-width: 4) |
| `agent` | `#fc8d62` | `#a35332` | AGENTS + COLLABORATORS (stroke-width: 2) |
| `tools` | `#fc8d62` | `#a35332` | TOOLS multi-stations (stroke-width: 2) |
| `auto` | `#e78ac3` | `#a64a87` | AUTO pipelines pink |
| `phone` | `#8da0cb` | `#4d5a8a` | PHONE (high contrast, width 3) |
| `other_workshop` | `#8da0cb` | `#4d5a8a` | OTHER WORKSHOPS (lighter, width 2) |

---

## 3 версии для сравнения (deliverables)

| File | Подход |
|---|---|
| `v1-detailed.md` | LR, все nodes explicit, max detail (всё видно, может быть busy) |
| `v2-clustered.md` | LR с subgraph clusters (грouping nodes в визуальные boxes — cleaner) |
| `v3-circular.md` | LR + explicit feedback loop emphasized (закольцовка bold внизу) |

Все три — **same logic / nodes / edges**, но разные visual takes. Ruslan выбирает один → fix → используется как baseline для остальных 3 диаграмм (TRM / L0-L5 / Collaboration).
