---
title: Diagram 1 — Levenchuk Corpus Map Landscape
phase: 6
parent: research/levenchuk-corpus-inventory-v2-2026-05-19-evening/
---

# Diagram 1 — Corpus Map Landscape (10 categories × source types × status)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    LC[Levenchuk Corpus<br/>2026-05-19 evening v2]

    subgraph "01 GitHub"
        G1[ailev/FPF ⭐368<br/>✅ active 2026-05-19]
        G2[ailev/anird<br/>✅ inactive 5y]
        G3[ailev.github.io<br/>✅ inactive 5y]
    end

    subgraph "02 LiveJournal"
        L1[ailev.livejournal.com<br/>✅ 1 new post 2026-05-18]
        L2[Key posts 2012-2026<br/>✅ re-verified]
        L3[Tag pages<br/>🔴 404 all 4 tested]
    end

    subgraph "03 МИМ Public"
        M1[system-school.ru<br/>✅ refreshed]
        M2[/stack 16 transdisc<br/>✅ refreshed delta vs 17]
        M3[/programs/orgdev<br/>✅ R1-R10 refreshed]
        M4[events.system-school.ru<br/>🟡 no public events]
        M5[10th conf 2026<br/>✅ already happened 18-19.04]
    end

    subgraph "04 Aisystant Paid"
        A1[8 courses<br/>🟢 Ruslan-handles]
        A2[IWE chat<br/>🔴 REJECTED]
    end

    subgraph "05 Books Paid"
        B1[Ridero 9 books refreshed<br/>🟢 4080 pages total]
        B2[LitRes 12 books<br/>🟢 Ruslan-handles]
        B3[Ozon catalog<br/>🔴 too many redirects]
    end

    subgraph "06 Telegram"
        T1[@ailev_blog 2258 subs<br/>✅ confirmed]
        T2[@system_school cohort<br/>🟢 bot-mediated]
    end

    subgraph "07 arXiv + PDFs"
        AR1[arXiv 1502.00121 2015<br/>✅ captured]
        AR2[arXiv 2310.11524 2023<br/>✅ captured]
        AR3[TechInvestLab 2015 PDF 8MB<br/>🟢 free download]
    end

    subgraph "08 Tseren"
        TS1[systemsworld.club profile<br/>✅ captured]
        TS2[Medium English 2 articles<br/>🟡 dormant]
        TS3[TG raw 618 posts<br/>✅ in repo]
        TS4[YT raw 127+452+37 vids<br/>✅ in repo]
    end

    subgraph "09 Third-party"
        TP1[Psybertron review 15807<br/>✅ captured]
        TP2[Habr 10 articles via WebSearch<br/>✅ captured]
        TP3[vc.ru 10 articles via WebSearch<br/>✅ captured]
        TP4[in.wiki bio<br/>✅ captured]
        TP5[inexsu.wordpress 2020<br/>✅ captured]
    end

    subgraph "10 YouTube"
        YT1[ailev* channel<br/>🔴 transcripts blocked]
        YT2[Metadata only<br/>🟡 preserved]
    end

    LC --> G1 & G2 & G3
    LC --> L1 & L2 & L3
    LC --> M1 & M2 & M3 & M4 & M5
    LC --> A1 & A2
    LC --> B1 & B2 & B3
    LC --> T1 & T2
    LC --> AR1 & AR2 & AR3
    LC --> TS1 & TS2 & TS3 & TS4
    LC --> TP1 & TP2 & TP3 & TP4 & TP5
    LC --> YT1 & YT2

    style LC fill:#fff4e6,color:#000
    style G1 fill:#d6f0d6,color:#000
    style L1 fill:#d6f0d6,color:#000
    style M3 fill:#d6f0d6,color:#000
    style M2 fill:#d6f0d6,color:#000
    style M5 fill:#d6f0d6,color:#000
    style A2 fill:#ffd6d6,color:#000
    style L3 fill:#ffd6d6,color:#000
    style B3 fill:#ffd6d6,color:#000
    style YT1 fill:#ffd6d6,color:#000
    style A1 fill:#fff8d5,color:#000
    style B1 fill:#fff8d5,color:#000
    style B2 fill:#fff8d5,color:#000
```

**Legend:**
- ✅ (green) — collected / verified
- 🟢 (yellow) — paid / Ruslan-handles
- 🟡 (light) — partial / dormant
- 🔴 (red) — blocked / 404 / rejected

**Status summary:** ~25 sources verified; 3 new sources (T1.0 R1-R10 / T1.1.1 post 1801412 / T1.2.2 16 transdisc refresh) surfaced since 2026-05-17.
