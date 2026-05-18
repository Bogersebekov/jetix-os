---
type: diagram
title: ML stack 3 layers (image 1 reproduced)
date: 2026-05-18
source: Ruslan-shared infographic «Стек в ML»
---

# Diagram 01 — ML stack 3 layers (21 tools)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph TB
    subgraph "Layer 3 — ПРОДУКТОВАЯ РАЗРАБОТКА (deploy + monitor + scale)"
        DK[Docker]
        AF[Airflow]
        PS[PySpark]
        WB[W&B]
        ML[MLflow]
        GR[Grafana]
        FA[FastAPI]
        GT[Git]
        GH[GitHub]
        GL[GitLab]
        K8[Kubernetes]
    end

    subgraph "Layer 2 — РАЗРАБОТКА (ML dev)"
        JU[Jupyter]
        SK[scikit-learn]
        PT[PyTorch]
        HF[HuggingFace]
        CB[CatBoost]
        XG[XGBoost]
        LG[LightGBM]
        OP[Optuna]
    end

    subgraph "Layer 1 — БАЗА (foundation)"
        PY[Python]
        MA[Math]
        NP[NumPy]
        PD[pandas]
        MP[matplotlib]
        PL[Polars]
    end

    PY --> NP
    PY --> PD
    PY --> MP
    PY --> PL
    MA --> PY

    NP --> SK
    NP --> PT
    PD --> SK
    PD --> JU

    JU --> SK
    JU --> PT
    JU --> HF
    SK --> CB
    SK --> XG
    SK --> LG
    SK --> OP
    PT --> HF

    SK --> DK
    PT --> DK
    HF --> FA
    DK --> K8
    DK --> AF
    DK --> WB
    DK --> ML
    GT --> GH
    GT --> GL
    K8 --> GR

    style PY fill:#fff4e6
    style MA fill:#fff4e6
    style NP fill:#fff4e6
    style PD fill:#fff4e6
    style MP fill:#fff4e6
    style PL fill:#fff4e6

    style JU fill:#d6f0d6
    style SK fill:#d6f0d6
    style PT fill:#d6f0d6
    style HF fill:#d6f0d6
    style CB fill:#d6f0d6
    style XG fill:#d6f0d6
    style LG fill:#d6f0d6
    style OP fill:#d6f0d6

    style DK fill:#ffd6f0
    style AF fill:#ffd6f0
    style PS fill:#ffd6f0
    style WB fill:#ffd6f0
    style ML fill:#ffd6f0
    style GR fill:#ffd6f0
    style FA fill:#ffd6f0
    style GT fill:#ffd6f0
    style GH fill:#ffd6f0
    style GL fill:#ffd6f0
    style K8 fill:#ffd6f0
```

**Цветовая легенда:**
- 🟡 Жёлтый: Layer 1 — Foundation (Python / Math / NumPy / pandas / matplotlib / Polars)
- 🟢 Зелёный: Layer 2 — ML Development (Jupyter / sklearn / PyTorch / HF / CatBoost / XGB / LGB / Optuna)
- 🟣 Розовый: Layer 3 — Production (Docker / Airflow / PySpark / W&B / MLflow / Grafana / FastAPI / Git / GitHub / GitLab / Kubernetes)

**Cross-link:** docs 03 (Layer 1), 04 (Layer 2), 05 (Layer 3).
