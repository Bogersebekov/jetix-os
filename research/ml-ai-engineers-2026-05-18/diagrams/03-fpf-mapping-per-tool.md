---
type: diagram
title: 21 tools × FPF primitives matrix
date: 2026-05-18
---

# Diagram 03 — Tool × FPF primitive matrix

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa','noteTextColor':'#000000','noteBkgColor':'#fff8d5','edgeLabelBackground':'#ffffff'}}}%%
graph LR
    subgraph "Layer 1 tools → FPF primitives"
        PY[Python] --> CU[U.Capability: implement]
        MA[Math] --> UC[U.Capability + U.MethodDescription]
        NP[NumPy] --> US1[U.System: array compute]
        PD[pandas] --> US2[U.System: tabular]
        MP[matplotlib] --> BS[B.5.1 Explore: present]
        PL[Polars] --> US3[U.System: tabular at scale]
    end

    subgraph "Layer 2 tools → FPF primitives"
        JU[Jupyter] --> BS2[B.5.1 Explore + B.5.2 Abductive]
        SK[sklearn] --> UM1[U.MethodDescription: classical ML]
        PT[PyTorch] --> UC2[U.Capability: differentiable]
        HF[HuggingFace] --> US4[U.System: shared substrate]
        CB[CatBoost] --> UM2[U.Method: boosted tree]
        XG[XGBoost] --> UM3[U.Method: boosted tree canonical]
        LG[LightGBM] --> UM4[U.Method: leaf-wise boost]
        OP[Optuna] --> UM5[U.Method: HPO sampler]
    end

    subgraph "Layer 3 tools → FPF primitives"
        DK[Docker] --> UC3[U.Capability: env isolation]
        AF[Airflow] --> UM6[U.MethodDescription orchestration]
        PS[PySpark] --> UC4[U.Capability: distributed compute]
        WB[W&B] --> P6A[Part 6a Provenance analog]
        ML[MLflow] --> P5[Part 5 Compound Learning analog]
        GR[Grafana] --> P8[Part 8 Health Monitoring analog]
        FA[FastAPI] --> P10[Part 10 External Touchpoints]
        GT[Git] --> SUB[Cross-cutting substrate]
        GH[GitHub] --> P10b[Part 10 + Community]
        GL[GitLab] --> P10c[Part 10 + Sovereign option]
        K8[Kubernetes] --> P7[Part 7 Lifecycle Substrate]
    end

    style PY fill:#fff4e6
    style JU fill:#d6f0d6
    style DK fill:#ffd6f0
```

**Key cross-cutting insight:** Foundation Parts (5/6a/7/8/10) have direct production-ML tooling analogs. **Workshop curriculum can use these tools to teach Foundation patterns concretely.**

**Cross-link:** docs 03 / 04 / 05 (per-tool deep dive); doc 07 §6 (universal pattern lifts).
