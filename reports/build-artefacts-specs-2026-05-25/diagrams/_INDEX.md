---
title: Mermaid INDEX — Build Artefacts Specs (BS-1..BS-7)
date: 2026-05-25
type: diagrams-index
parent_main: decisions/strategic/BUILD-ARTEFACTS-SPECS-2026-05-25.md
prose_authored_by: brigadier-scribe (Cloud Cowork Opus 4.7 [1M ctx])
language: russian primary
mermaid_count: 7
---

# 🎨 Mermaid INDEX — BS-1..BS-7

Каталог всех 7 схем Build Artefacts Specs (тема base / light bg для GitHub-читаемости).

| # | Схема | О чём | Где inline |
|---|---|---|---|
| **BS-1** | Кросс-карта артефактов | 10-12 артефактов × умные партнёры × Build→Run→Scale | Main §2 + `02-overview-cross-map.md` |
| **BS-2** | Граф зависимостей | что от чего зависит; видео A = блокер | Main §13 + `13-dependencies-risks.md` |
| **BS-3** | Критический путь | минимальная цепь к Build exit | Main §13 + `13-dependencies-risks.md` |
| **BS-4** | R12-риск overlay | где высшая R12-поверхность + AUTO-FIRE | Main §14 |
| **BS-5** | Build → Run handoff | что каждый артефакт сдаёт в Run | Main §15 |
| **BS-6** | Приоритет аудитории | умные партнёры primary, масса secondary | Main §15 |
| **BS-7** | Порядок 4 недель | sequencing Week 1-4 → Build exit | Main §18 |

---

## BS-1 — Кросс-карта артефактов (умные партнёры × Build → Run → Scale)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteTextColor':'#000','noteBkgColor':'#fff8d5'}}}%%
graph TB
    subgraph AUD[👥 PRIMARY — умные партнёры Build]
        A1[🟣 T1 Методолог<br/>проверяет substance]
        A2[🟣 T1 R12-мост<br/>проверяет анти-секту]
        A3[🔵 smart T3 тестер<br/>пробует сам]
    end
    subgraph ART[🏗️ 10-12 BUILD-АРТЕФАКТОВ]
        V1[🎬 Видео A]
        V2[🎬 Видео B]
        V3[🎬 Видео C]
        N1[📋 Personal OS]
        N2[📋 Team OS]
        CH[📜 Charter]
        LD[🌐 Лендинг+FAQ]
        DC[🗣️ Discovery]
        LF[⚖️💰 Юр+счёт]
        SP[📚📊 Supporting]
    end
    A1 ==>|substance| V1
    A1 ==>|место| V3
    A1 ==>|co-design| N2
    A2 ==>|R12 ревью| CH
    A2 ==>|анти-секта| V3
    A3 ==>|про меня?| V2
    A3 ==>|форк+юз| N1
    A1 -.first touch.-> LD
    A3 -.first touch.-> LD
    A1 -.разговор.-> DC
    A3 -.разговор.-> DC
    LF -.базис.-> ART
    SP -.trust.-> A1
    ART ==>|Build exit ≥80%| RUN[▶️ RUN когорта + partner-led]
    RUN ==>|кланы + 1K| SCALE[📡 SCALE community-варианты]
    NOTE1[⚖️ R12-риск растёт Build→Scale:<br/>Charter + Видео C + Team OS = высшая]
    CH -.- NOTE1
    style AUD fill:#cce6ff,color:#000
    style ART fill:#d6f0d6,color:#000
    style RUN fill:#fff4cc,color:#000
    style SCALE fill:#ffe0a0,color:#000
    style CH fill:#ffd6d6,color:#000
    style V3 fill:#ffe8e0,color:#000
    style N2 fill:#ffe8e0,color:#000
    style NOTE1 fill:#fff8d5,color:#000
```

---

## BS-2 — Граф зависимостей артефактов

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteTextColor':'#000','noteBkgColor':'#fff8d5'}}}%%
graph TD
    VA[🎬 Видео A · БЛОКЕР]
    VB[🎬 Видео B]
    VC[🎬 Видео C]
    NP[📋 Personal OS 5 баз]
    NT[📋 Team OS demo]
    CH[📜 Charter v1]
    CHR[📜 R12-ревью → v1.1]
    LD[🌐 Лендинг+FAQ]
    DC[🗣️ Discovery]
    LF[⚖️💰 Юр+счёт]
    CONV[💬 первые 3-5 разговоров]
    W1[📨 Wave 1]
    EXIT{🚦 Build exit ≥80%}
    VA ==> VB
    VA ==> VC
    VB ==> VC
    VA ==> LD
    VB ==> LD
    VA ==> DC
    VB ==> NP
    NP ==> NT
    CH ==> NT
    CH --> CHR
    VC -.цифры.-> CH
    CONV ==> LD
    VC ==> DC
    CHR ==> DC
    LF -.контракт ← Charter.-> CH
    VA ==> W1
    VC ==> W1
    LD ==> W1
    DC ==> EXIT
    CHR ==> EXIT
    NP ==> EXIT
    LF -.юр начато.-> EXIT
    style VA fill:#ffd6d6,color:#000
    style CH fill:#ffe8e0,color:#000
    style CHR fill:#ffe8e0,color:#000
    style NT fill:#ffe8e0,color:#000
    style EXIT fill:#fff8d5,color:#000
    style W1 fill:#cce6ff,color:#000
```

---

## BS-3 — Критический путь к Build exit

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteTextColor':'#000','noteBkgColor':'#fff8d5'}}}%%
graph LR
    START([Build 25.05]) --> VA[🎬 Видео A БЛОКЕР]
    VA --> P{параллельно}
    P --> NP[📋 Personal OS]
    P --> CHT[📜 Charter текст]
    NP --> TR[🧪 trial Дмитрий → feedback]
    CHT --> CHR[📜 R12-ревью]
    CHR --> CH11[📜 Charter v1.1]
    TR --> DC[🗣️ Discovery ≥5 репетиций]
    CH11 --> DC
    DC --> CONF[✅ ≥1 T1 + ≥3 T3]
    LF[⚖️ юр начато] -.-> CONF
    CONF --> EXIT{🚦 Build exit ≥80%}
    EXIT -->|да| RUN[▶️ Run]
    EXIT -->|анти-триггер| HOLD[⏸ пауза]
    NOTE[💡 Видео B/C · Team OS · лендинг · supporting<br/>= желательны, не строго блокируют]
    EXIT -.- NOTE
    style VA fill:#ffd6d6,color:#000
    style CHR fill:#ffe8e0,color:#000
    style EXIT fill:#fff8d5,color:#000
    style RUN fill:#cce6ff,color:#000
    style HOLD fill:#ffcccc,color:#000
    style NOTE fill:#eeeeee,color:#000
```

---

## BS-4 — R12-риск по артефактам (overlay)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteTextColor':'#000','noteBkgColor':'#fff8d5'}}}%%
graph TD
    subgraph HIGHEST[🔴 ВЫСШАЯ/ВЫСОКАЯ — AUTO-FIRE]
        CH[📜 Charter<br/>infl-ethics + recruitment]
        VC[🎬 Видео C<br/>infl-ethics + recruitment + propaganda]
        NT[📋 Team OS<br/>infl-ethics + gamification]
    end
    subgraph MED[🟡 СРЕДНЯЯ]
        LD[🌐 Лендинг<br/>nlp + infl-ethics]
        DC[🗣️ Discovery<br/>infl-ethics + nlp]
        LF[⚖️ Контракт<br/>infl-ethics]
        SP[📚 Supporting<br/>nlp]
    end
    subgraph LOW[🟢 НИЗКАЯ-СРЕДНЯЯ]
        VA[🎬 Видео A]
        VB[🎬 Видео B]
        NP[📋 Personal OS]
        FIN[💰 Счёт]
    end
    GUARD[🛡️ 4 RUSLAN-LAYER action classes<br/>extraction_beyond_share · wage_ratio_violation<br/>non_consensual_distribution · fork_prevention_attempt<br/>Halt-Log-Alert F4 ≤5с]
    HIGHEST ==> GUARD
    MED ==> GUARD
    LAW[⚖️ защита растёт быстрее системы]
    GUARD -.-> LAW
    style HIGHEST fill:#ffd6d6,color:#000
    style MED fill:#fff4cc,color:#000
    style LOW fill:#d6f0d6,color:#000
    style GUARD fill:#d6e0f0,color:#000
    style LAW fill:#fff8d5,color:#000
```

---

## BS-5 — Build → Run handoff

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteTextColor':'#000','noteBkgColor':'#fff8d5'}}}%%
graph LR
    subgraph BUILD[🏗️ BUILD — мы пишем сами]
        b1[🎬 Видео A/B/C]
        b2[📋 Notion 5 баз + demo]
        b3[📜 Charter v1.1]
        b4[🗣️ Discovery + 🌐 лендинг]
        b5[⚖️💰 Юр + счёт]
    end
    subgraph RUN[▶️ RUN — пишет партнёр]
        r1[📚 Курс end-to-end T1]
        r2[🚀 Онбординг когорты]
        r3[📜 Charter подписан 3→50]
        r4[📊 Кейсы 10-20]
    end
    b1 ==>|адаптация| r1
    b2 ==>|кастомизация| r2
    b3 ==>|подпись| r3
    b4 ==>|partner-led| r4
    b5 -.базис.-> RUN
    GATE{🚦 ≥1 T1 + ≥3 T3<br/>+ Charter R12 PASS<br/>+ Notion multi-user<br/>+ звонок ≥5<br/>+ юр начато}
    BUILD ==> GATE ==> RUN
    style BUILD fill:#d6f0d6,color:#000
    style RUN fill:#cce6ff,color:#000
    style GATE fill:#fff8d5,color:#000
    style b1 fill:#ffd6d6,color:#000
```

---

## BS-6 — Приоритет аудитории в Build

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa','noteTextColor':'#000','noteBkgColor':'#fff8d5'}}}%%
graph TD
    PRIMARY[⭐ PRIMARY Build<br/>умные партнёры]
    PRIMARY --> P1[🟣 T1 методолог<br/>Видео A · Видео C · Team OS]
    PRIMARY --> P2[🟣 T1 R12-мост<br/>Charter · Видео C]
    PRIMARY --> P3[🔵 smart T3 тестер<br/>Видео B · Personal OS · лендинг]
    SECONDARY[➖ SECONDARY · mention only<br/>масса 5+1 архетипов]
    SECONDARY -.зовём ПОСЛЕ.-> P1
    NOTE[💡 умные партнёры проходят первыми<br/>→ T1 становится co-creator<br/>→ T3 становится адвокатом<br/>→ только потом масса]
    PRIMARY -.- NOTE
    style PRIMARY fill:#cce6ff,color:#000
    style SECONDARY fill:#eeeeee,color:#000
    style NOTE fill:#fff8d5,color:#000
```

---

## BS-7 — Порядок 4 недель (sequencing)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TB
    W1[Week 1 · 25-31.05<br/>🎬 Видео A БЛОКЕР · Дмитрий trial<br/>CRM 5+1 · Steuerberater email] --> W2[Week 2 · 1-7.06<br/>🎬 Видео B+C · 📋 Personal OS 5 баз<br/>📜 Charter v1 · Wave 1 · счёт]
    W2 --> W3[Week 3 · 8-14.06<br/>Wave 1 вторая · 📋 Team OS demo<br/>🗣️ discovery-звонки · 🌐 лендинг+FAQ]
    W3 --> W4[Week 4 · 15-22.06<br/>1-2 T1 confirmed · 3-5 T3<br/>лендинг published · ✅ Build exit check]
    W4 --> GATE{🚦 Build→Run ≥80%?}
    GATE -->|да| RUN[▶️ Run transition]
    GATE -->|анти-триггер| HOLD[⏸ пауза]
    style W1 fill:#ffd6d6,color:#000
    style W2 fill:#d6f0d6,color:#000
    style W3 fill:#c0e0c0,color:#000
    style W4 fill:#b3dab3,color:#000
    style GATE fill:#fff8d5,color:#000
    style RUN fill:#cce6ff,color:#000
    style HOLD fill:#ffcccc,color:#000
```

---

*Mermaid INDEX closure 2026-05-25. 7 схем BS-1..BS-7, тема base / light bg. Все inline в Main +
phase reports. Per prompt §13 mermaid INDEX 5-7 schemes.*
