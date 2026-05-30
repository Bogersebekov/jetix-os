---
title: "D2 — 4 концепта как один R12-контур + где встраиваются + R12-метки"
date: 2026-05-30
type: diagram
theme: light (white bg)
parent: reports/completeness-audit-2026-05-30/02-four-concepts.md
---

# D2 — 4 концепта: один контур + R12-guards

> Светлая тема. Красный = R12 CRITICAL/HIGHEST surface · жёлтый = guard/gate · зелёный = healthy.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteBkgColor':'#fff8d5'}}}%%
graph TB
    GT[⚖️ Концепт3 GAME THEORY<br/>почему кооперация = равновесие<br/>→ #8/#1 · cooperation-moat]
    INT[🧠 Концепт4 INTELLIGENCE<br/>δ→1 горизонт + ответственность<br/>= кто удерживает равновесие → #1/#13]
    COIN[🪙 Концепт2 CRYPTO/COINS<br/>enforced in code: QF/cap/exit/SBT<br/>→ #8 · Phase 2+ opt-in]
    FUND[💰 Концепт1 INVEST-FUND<br/>treasury → система + проекты<br/>Caja-Laboral pattern → #4]

    GT <-->|изоморфизм| INT
    GT -->|mechanism design| COIN
    INT -->|human capital| GT
    COIN -->|enforced| FUND
    FUND -->|реинвест-петля| GT

    GUARD{⚖️ R12 — 4 guards<br/>extraction_beyond_share<br/>wage_ratio_violation 5:1<br/>fork_prevention_attempt<br/>non_consensual_distribution}

    FUND --> GUARD
    COIN --> GUARD
    GT --> GUARD
    INT --> GUARD
    GUARD -->|pass| OK[✅ healthy R12-движок<br/>«нагнуть теорию игр» этично]
    GUARD -->|fail| BAD[🚫 фонд=доение · коин=спекуляция<br/>mechanism=манипуляция · отбор=каста]

    style GT fill:#cce6ff,color:#000
    style INT fill:#d6f0d6,color:#000
    style COIN fill:#ffe0a0,color:#000
    style FUND fill:#ffe0a0,color:#000
    style GUARD fill:#fff8d5,color:#000
    style OK fill:#d6f0d6,color:#000
    style BAD fill:#ff9999,color:#000
```

**Чтение.** 4 концепта = **один контур**, не 4 темы: §3 (почему) ↔ §4 (кто) — изоморфизм
(δ→1 + ответственность = условие folk-theorem); §2 enforced'ит §3 в коде; §1 финансирует петлю.
**R12 (4 guards) = то, что держит весь контур на здоровой стороне.** Без guards каждый концепт
коллапсирует в extraction. Ни один концепт НЕ требует нового направления (суб-грани #4/#8/#14/#1).
