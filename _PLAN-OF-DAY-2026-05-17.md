---
title: План дня 17.05.2026 — что мы делаем, какие prompts запускаем, что получим
date: 2026-05-17
type: plan-of-day
status: ACTIVE
deadline: 2026-05-18T08:00:00+02:00
purpose: |
  Antigravity-friendly plan-of-day. Объясняет ЧТО мы делаем сегодня, КАКИЕ
  prompts будем запускать на server CC, ЧТО получим в конце. Cross-link на
  explanation files per prompt. Ruslan читает ЭТО первым → решает launch'ать
  ли каждый prompt → ack-ает → запускаем.
language: russian
---

# 📋 План дня — 17.05.2026 (Вс)

## 🎯 Главная цель дня

**Изучить досконально FPF и IWE, сравнить с моей системой, упаковать Jetix как working file, составить план сотрудничества по FPF — и к 8:00 18.05 финальные ответы Левенчуку + Цэрэну готовы к отправке.**

> Тон: «ебало поотваливались» — максимальная плотность качественной проработанной информации. Без дуэма.

---

## 📦 Что у нас есть СЕЙЧАС (state на 17.05 утро)

| Артефакт | Где | Что это |
|---|---|---|
| ✅ Phase A SUMMARY | [`reports/.../00-SUMMARY-FOR-RUSLAN.md`](reports/fpf-iwe-distillation-2026-05-17/00-SUMMARY-FOR-RUSLAN.md) | 2048 слов, top-line что есть FPF + честный self-audit Jetix vs Левенчуковский bar |
| ✅ FPF understanding base | [`reports/.../01-fpf-on-human-language.md`](reports/fpf-iwe-distillation-2026-05-17/01-fpf-on-human-language.md) | 462 строки, FPF на человеческом языке (5 primitives + 7 mechanisms + 10-step intelligence amplification) |
| ✅ IWE understanding base | [`reports/.../02-u-episteme-and-iwe.md`](reports/fpf-iwe-distillation-2026-05-17/02-u-episteme-and-iwe.md) | Conceptual mapping IWE как FPF-applied |
| ✅ Honest self-audit Jetix vs FPF | [`reports/.../06-honest-self-audit.md`](reports/fpf-iwe-distillation-2026-05-17/06-honest-self-audit.md) | ~27 memory/automation vs ~12 intelligence/FPF-derivative компонентов |
| ✅ 12 mermaid diagrams | [`reports/.../diagrams/`](reports/fpf-iwe-distillation-2026-05-17/diagrams/) | FPF architecture / IWE / intellect-stack / etc. |
| ✅ Левенчуковское TG message | [`inbox/levenchuk-tg-2026-05-17.md`](inbox/levenchuk-tg-2026-05-17.md) | Verbatim + C1-C7 surface'нутые claims |
| ✅ Канонический FPF source | [`raw/external/ailev-FPF/FPF-Spec.md`](raw/external/ailev-FPF/FPF-Spec.md) | 62K строк, vendored 20.04 |
| 🆕 **Tseren GitHub** | `github.com/TserenTserenov/FMT-exocortex-template` | **IWE template — Tseren's public artifact** (нашли только что, ещё не обработано) |

---

## 🎯 Что получим к 8:00 18.05 (целевое состояние)

| Артефакт | Где будет | Назначение |
|---|---|---|
| FPF tighten v2 | `reports/.../01-fpf-on-human-language-v2.md` | Refined FPF understanding на «человеческом языке», ready для L1 |
| IWE deep collection | `reports/iwe-deep-collection-2026-05-17.md` | Все материалы IWE (Tseren github + TG + YT + LJ + aisystant) выжаты |
| Jetix vs IWE audit | `reports/jetix-vs-iwe-audit-2026-05-17.md` | Mirror self-audit Phase A, но vs IWE |
| **Jetix как working file** | `JETIX-WORKING-FILE-v0-2026-05-17.md` (root) | Single navigable artifact в стиле `github.com/ailev/FPF` или Tseren IWE template |
| FPF cooperation plan | `outreach/JETIX-FPF-COOPERATION-PLAN-2026-05-17.md` | 3-tier ladder сотрудничества (light/medium/deep) |
| Letter base Левенчуку | `outreach/levenchuk-response-base-2026-05-17.md` | Content blocks для финального ответа (Ruslan-authored) |
| Letter base Цэрэну | `outreach/tseren-response-base-2026-05-17.md` | Content blocks для финального ответа (Ruslan-authored) |
| **Pack for L1** | `outreach/pack-for-l1-2026-05-17/` | Готовая папка артефактов которые Ruslan скидывает |

---

## 🛠️ Какие prompts сегодня запускаем

### Сегодня — **ОДИН** prompt: **Phase B**

- **Prompt file:** [`prompts/fpf-iwe-phase-b-2026-05-17.md`](prompts/fpf-iwe-phase-b-2026-05-17.md)
- **Explanation file (ОБЯЗАТЕЛЬНО ЧИТАТЬ ПЕРВЫМ):** [`_EXPLAIN-PHASE-B-PROMPT-2026-05-17.md`](_EXPLAIN-PHASE-B-PROMPT-2026-05-17.md)
- **Time estimate:** 8-12 часов autonomous server CC
- **Inside:** 6 sequential шагов (FPF tighten → IWE collect → vs IWE audit → pack Jetix → cooperation plan → letter bases)

**Почему ОДИН prompt а не 6 разных:** шаги имеют чёткие зависимости (§2 → §3 → §4 → §5 → §6), splitting на 6 promptov добавит overhead context loading × 6 без выгоды. Один autonomous run = эффективнее. Если в середине Ruslan хочет course correct — interrupt + relaunch с new prompt.

### Завтра утром (после Phase B finish):
- **Letter finalization** — Ruslan-authored, не отдельный server CC prompt (это его работа)
- **Pack отправка** — Ruslan-authored

---

## 🗺️ Flow дня (mermaid)

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Inter','fontSize':'12px'}}}%%
flowchart TB
    START["17.05 утро<br/>Phase A complete"]:::start
    PLAN["План дня + Explanation files"]:::plan
    ACK{"Ruslan ack<br/>explanation?"}:::ack
    LAUNCH["Launch Phase B<br/>tmux + claude dangerous"]:::launch

    subgraph PHASEB["Phase B server CC autonomous (8-12h)"]
        S1["§1 FPF tighten v2<br/>+ freshness sync upstream"]:::step
        S2["§2 IWE collect<br/>Tseren github FMT-exocortex<br/>+ TG + YT + aisystant"]:::step
        S3["§3 Jetix vs IWE audit"]:::step
        S4["§4 Pack Jetix as working file<br/>JETIX-WORKING-FILE-v0.md"]:::step
        S5["§5 FPF cooperation plan<br/>3-tier ladder"]:::step
        S6["§6 Letter bases<br/>+ pack-for-l1/"]:::step
        S1 --> S3
        S2 --> S3
        S3 --> S4
        S4 --> S5
        S5 --> S6
    end

    FINISH["Phase B SUMMARY<br/>+ pack-for-l1 готов"]:::finish
    MORNING["18.05 утро<br/>Ruslan finalize letters<br/>отправка к 8:00"]:::morning

    START --> PLAN --> ACK
    ACK -->|"go"| LAUNCH --> S1 & S2
    ACK -->|"course correct"| PLAN
    S6 --> FINISH --> MORNING

    classDef start fill:#e8eaf6,stroke:#283593,stroke-width:2px
    classDef plan fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    classDef ack fill:#fff8e1,stroke:#f57c00,stroke-width:3px
    classDef launch fill:#fce4ec,stroke:#ad1457,stroke-width:2px
    classDef step fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    classDef finish fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef morning fill:#f1f8e9,stroke:#33691e,stroke-width:2px
```

---

## 📂 Файлы дня в repo (Antigravity-friendly)

- 📋 **[`_PLAN-OF-DAY-2026-05-17.md`](_PLAN-OF-DAY-2026-05-17.md)** ← этот файл, общий план
- 📖 **[`_EXPLAIN-PHASE-B-PROMPT-2026-05-17.md`](_EXPLAIN-PHASE-B-PROMPT-2026-05-17.md)** — explanation Phase B prompt'a (ОБЯЗАТЕЛЬНО)
- 📅 **[`_DAILY-LOG-2026-05-17.md`](_DAILY-LOG-2026-05-17.md)** — Antigravity-friendly copy of Notion daily log
- 🛠️ **[`prompts/fpf-iwe-phase-b-2026-05-17.md`](prompts/fpf-iwe-phase-b-2026-05-17.md)** — сам prompt

Notion mirror: [🎯 17.05.2026 — Вс](https://www.notion.so/3632496333bf81328397dc98e0451f3c) (sandbox view; primary working layer — здесь в repo)

---

## ⚠️ Что НЕ делаем сегодня

- НЕ запускаем prompt пока Ruslan не прочитал `_EXPLAIN-PHASE-B-PROMPT-2026-05-17.md` и не дал go
- НЕ trogат Foundation paths (R2)
- НЕ отвечаем Левенчуку / Цэрэну ДО finishing §1-§5
- НЕ начинаем новые направления вне §1-§6 Phase B
- НЕ перфекционим — beta-первый
