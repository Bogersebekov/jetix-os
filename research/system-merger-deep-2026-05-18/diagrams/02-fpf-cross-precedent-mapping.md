---
type: diagram
phase: 8
diagram_id: 02
title: 4 precedents → FPF primitive mapping
parent_doc: 02-cross-precedent-deep-4.md (§F design imperatives)
---

# Diagram 02 — 4 Precedents → FPF Primitive Mapping

```mermaid
flowchart LR
    subgraph USB-C
        USBC_PHYS[Physical connector]
        USBC_PD[USB-PD constraint catalog]
        USBC_MODE[CC pin mode negotiation]
        USBC_GOV[USB-IF consortium]
    end

    subgraph TCP/IP
        TCPIP_LAYER[Layered architecture]
        TCPIP_E2E[End-to-end principle]
        TCPIP_RFC[IETF RFC process]
        TCPIP_BSD[BSD 4.2 reference impl]
    end

    subgraph HTTP
        HTTP_URI[URI identity]
        HTTP_REST[REST uniform interface]
        HTTP_STATELESS[Stateless requests]
        HTTP_FREE[CERN free release]
    end

    subgraph OpenAPI+GraphQL
        API_SCHEMA[Schema-first]
        API_TOOLING[Tooling ecosystem]
        API_FED[Apollo Federation]
        API_OAI[Linux Foundation gov]
    end

    subgraph FPF_System_Merger
        FPF_BRIDGE[A.6.B Bounded Context Bridge]
        FPF_NAMORDNIK[Namordnik constraint catalog]
        FPF_MODE[Mode negotiation FULL/PARTIAL/OPAQUE]
        FPF_STEWARD[FPF-Steward + ROY governance]
        FPF_LAYERS[5-primitive layered stack]
        FPF_FORK[Fork-and-leave R12 exit]
        FPF_FGR[F-G-R provenance per claim]
        FPF_FIRST[Phase 5 first merger reference]
        FPF_PROV[Append-only audit trail]
        FPF_R12[R12 anti-extraction]
        FPF_OPEN[Open spec]
        FPF_TOOL[Tooling ecosystem investment]
        FPF_NWAY[n-way merger composition]
    end

    USBC_PHYS -->|maps| FPF_BRIDGE
    USBC_PD -->|maps| FPF_NAMORDNIK
    USBC_MODE -->|maps| FPF_MODE
    USBC_GOV -->|maps| FPF_STEWARD

    TCPIP_LAYER -->|maps| FPF_LAYERS
    TCPIP_E2E -->|inverted| FPF_FORK
    TCPIP_RFC -->|maps| FPF_FGR
    TCPIP_BSD -->|maps| FPF_FIRST

    HTTP_URI -->|maps| FPF_FGR
    HTTP_REST -->|maps| FPF_MODE
    HTTP_STATELESS -->|maps| FPF_PROV
    HTTP_FREE -->|maps| FPF_OPEN

    API_SCHEMA -->|maps| FPF_BRIDGE
    API_TOOLING -->|maps| FPF_TOOL
    API_FED -->|maps| FPF_NWAY
    API_OAI -->|maps| FPF_STEWARD
```

## 7 design imperatives (Phase 1 §F)

1. Open spec + reference impl (TCP/IP + HTTP + OpenAPI)
2. Layered architecture (TCP/IP)
3. Mode negotiation (USB-C CC pin)
4. Backward compatibility / exit (USB-C; R12)
5. Anchor tenant (Apple iPhone 15; GitHub GraphQL)
6. Tooling ecosystem (OpenAPI lesson)
7. Security/constraint enforcement built-in (avoid HTTP retrofit pain)
