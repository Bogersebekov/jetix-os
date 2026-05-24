---
title: D03 — Ack queue priority (47 acks / P1 first-hour + first-day + pre-Wave-1 sequence)
date: 2026-05-24
type: mermaid-diagram
parent: prompts/synthesis-execution-plans-2026-05-24.md
F: F2
---

# D03 — Ack Queue Priority

> 47 acks consolidated; P1 first-hour + first-day sequence + dependency graph. Per Phase 4 §10.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryTextColor':'#000','textColor':'#000','lineColor':'#333','primaryBorderColor':'#333','primaryColor':'#fafafa'}}}%%
graph TD
    subgraph H1[⏰ First Hour P1 Critical]
        X1[X-1 Plan choice<br/>A/B/C/D/combination]
        D13_1[D13-1 Naming-thread<br/>consolidation]
        PROP_3[PROP-3 W-frame<br/>commander's intent]
    end

    subgraph D1[📅 First Day P1 Unblocking]
        D13_3[D13-3 O-168 tier-structure]
        D13_4[D13-4 O-169 onboarding-artefact]
        D13_5[D13-5 O-170 hypothesis-cascade]
        D13_6[D13-6 O-171 point-A→B]
        D13_8[D13-8 O-173 embedded-development]
        PROP_1[PROP-1 Strategic path 1-5]
        PROP_2[PROP-2 Дмитрий+Сева first]
        LEV_1[LEV-1 Path A/B/C/D/E]
        LEV_2[LEV-2 Aisystant subscribe]
        SOTA_Q1[SOTA-Q1 Adopt 4 low-investment]
        SOTA_EXT4[SOTA-EXT-4 Partner-facing<br/>SOTA discipline doc]
    end

    subgraph PreWave[🚀 Pre-Wave-1 P1 Gate]
        LEV_3[LEV-3 Message variants per Path]
        LEV_6[LEV-6 12 offers selection]
        MTH_7[MTH-7 Левенчук direct collab]
        SOTA_Q3[SOTA-Q3 Wave 1 evidence]
        X2[X-2 R12 audit per plan]
    end

    subgraph P2[📋 P2 Day 2 desirable / 14 items]
        D13_2[D13-2 O-167 world-wide]
        D13_9[D13-9 O-174 persona]
        D13_10[D13-10 O-175 testing-posture]
        MTH_1[MTH-1 Lineage A/B/C/D]
        MTH_2[MTH-2 Strategic path 1-5]
        OtherP2[+9 more P2]
    end

    subgraph P3[🗄️ P3 DEFER / 16 items]
        D13_7[D13-7 O-172 R12 audit DEFER]
        OtherP3[+15 more P3 defer]
    end

    H1 --> D1
    D1 --> PreWave
    PreWave --> WaveSend([📨 Wave 1 send<br/>Plan A A8 / B B7 / D D5])

    D1 --> P2
    P2 --> P3

    style X1 fill:#ffd6d6
    style D13_1 fill:#ffd6d6
    style PROP_3 fill:#ffd6d6
    style D13_3 fill:#ffe0a0
    style D13_6 fill:#ffe0a0
    style LEV_1 fill:#ffe0a0
    style WaveSend fill:#d6e0f0
```

## Priority distribution

| Priority | Count | Description |
|---|---|---|
| P1 | 17 items | First-hour + first-day immediate; gates Production Day execution |
| P2 | 14 items | Day 2 desirable; next-day if no |
| P3 | 16 items | Defer / DEFER unless triggered |
| **Total** | **47 acks** | Cross-source consolidated |

## P1 sequence (per Phase 4 §10.1-10.3)

1. **X-1** Plan choice (60min)
2. **D13-1** Naming-thread (pre-Шаг 2 blocker)
3. **PROP-3** Welcome-frame commander's intent (Ruslan R1 only)
4-9. D13-3/4/5/6/8 batch-13 Tier A promote
10-12. PROP-1 + PROP-2 + LEV-1
13. LEV-2 Aisystant subscription
14-15. SOTA-Q1 + SOTA-EXT-4
16-18. LEV-3 + LEV-6 + MTH-7 (pre-Wave-1)
19. SOTA-Q3 evidence ack
20. X-2 R12 audit (auto-fire)
