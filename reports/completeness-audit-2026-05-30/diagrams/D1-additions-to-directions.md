---
title: "D1 — Карта additions (S1-S8 + LOCKED-gaps) → 16 directions / пакет"
date: 2026-05-30
type: diagram
theme: light (white bg)
parent: reports/completeness-audit-2026-05-30/03-base-audit-gaps.md
---

# D1 — Additions → directions / пакет (приоритет + R12)

> Светлая тема. P0 = красный (срочно/несущее) · P1 = оранжевый · P2 = синий · gated = жёлтый.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph LR
    PKG([📦 Партнёрский пакет<br/>P-1..P-8])

    subgraph P0[🔴 P0 — несущее]
      S1[S1 WHY «с тренером»<br/>coach-thesis → P-1 opener]
      S5[S5 числа ⭐ A1 блокер<br/>Economic V10 → P-6/P-7]
      S8[S8 recursive chain<br/>→ P-1 close]
    end

    subgraph P1[🟠 P1 — усиление]
      S2[S2 two-sided → P-2]
      S4[S4 full-stack 20 → P-5]
      MOAT[Концепт3 cooperation-moat → P-1]
      INT[Концепт4 intelligence → P-2]
      AIM[AI-Market timing → P-1]
    end

    subgraph P2[🔵 P2 — пробелы базы]
      D3[#3 Бизнес/кооператив]
      D7[#7 Образование/прогрессия]
      D14[#14 Кланы lifecycle]
      FUND[Концепт1 фонд → P-6]
      COIN[Концепт2 коины → P-4]
    end

    subgraph GATED[🟡 R12-GATED]
      S6[S6 лига/spectator<br/>GATE #15 Anti-Dark-Patterns]
    end

    S1 --> PKG
    S5 --> PKG
    S8 --> PKG
    P1 --> PKG
    P2 --> PKG
    GATED -.audit first.-> PKG

    style P0 fill:#ffd6d6,color:#000
    style P1 fill:#ffe0a0,color:#000
    style P2 fill:#cce6ff,color:#000
    style GATED fill:#fff8d5,color:#000
    style PKG fill:#d6f0d6,color:#000
```

**Чтение.** 3 P0-additions (WHY-opener · числа · recursive close) = несущие пробелы пакета.
P1 = усиление (two-sided / когорта / 2 moat-аргумента / timing). P2 = 6 недопредставленных
направлений + 2 механизм-концепта (фонд/коины). GATED = лига (#15 audit обязателен до вставки).
