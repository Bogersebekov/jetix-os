---
title: Diagram 12 — Jetix = Exokortex stack
date: 2026-05-19
type: mermaid-diagram
phase: 8
parent: ../07-jetix-exokortex-ontological-deep.md
source: Phase 5.5 + text_014 §2.29-30
---

# Jetix Workshop = Экзокортекс stack (Phase 5.5)

```mermaid
flowchart TB
    subgraph BIO[Bio-internal cognition]
        BRAIN[Biological brain<br/>Ruslan + participants]
    end

    subgraph EMBODIED[Body-internal cognition]
        VOICE[Voice pipeline<br/>(speech I/O channel)]
    end

    subgraph ENV[Environment-coupled cognition]
        LANG[Language: FPF<br/>(same-language layer)]
        TOOL[Tools: ROY swarm +<br/>Claude Code + MCP]
        REPO[Repository: wiki +<br/>5 K-research + Foundation]
        PROTO[Protocols: Part 4 + 6a + 6b]
        METHOD["Methodology: K-6 itself<br/>+ Recursive Engine<br/>+ Hackathon discipline"]
    end

    subgraph SOCIAL[Socially-distributed cognition]
        WORKSHOP[Workshop cohort]
        EDUC[Education Layer Tier 1-4]
        PARTNERS[Partnerships + CRM]
    end

    BRAIN <-->|speech| VOICE
    VOICE <-->|FPF| LANG
    LANG <-->|same-language| TOOL
    TOOL <-->|access| REPO
    TOOL <-->|coordinate| PROTO
    PROTO <-->|deploy| METHOD
    REPO <-->|memory| METHOD

    METHOD <-->|train| EDUC
    EDUC <-->|graduate| WORKSHOP
    WORKSHOP <-->|engage| PARTNERS
    PARTNERS <-->|extend| BRAIN

    classDef bio fill:#fee2e2,stroke:#ef4444
    classDef embod fill:#fef3c7,stroke:#f59e0b
    classDef env fill:#dbeafe,stroke:#3b82f6
    classDef social fill:#dcfce7,stroke:#22c55e
    class BRAIN bio
    class VOICE embod
    class LANG,TOOL,REPO,PROTO,METHOD env
    class WORKSHOP,EDUC,PARTNERS social
```

**Reading:** Clark 2008 4 levels of cognitive extension. Bio + body + environment + social. Workshop = full-stack exokortex = all 4 levels engaged. **IP-1 STRICT: humans = decision actors; exokortex = substrate (NOT autonomous mind).**
