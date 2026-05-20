---
title: Hypothesis Lifecycle — state transitions
type: diagram
date: 2026-05-20
---

# Hypothesis Lifecycle (state machine)

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','textColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
stateDiagram-v2
    [*] --> active: /hypothesis-add
    
    active --> testing: test method initiated
    active --> paused: deprioritized pre-test
    
    testing --> confirmed: success criteria met
    testing --> refuted: refutation criteria met
    testing --> paused: blocked / resource constraint
    
    paused --> active: trigger condition met; resume
    
    confirmed --> [*]: archived с learning_extracted
    refuted --> [*]: archived с learning_extracted
    
    note right of confirmed
        Promotion candidate
        if fpf_F=F5+ AND fpf_R=high:
        consider /ingest к wiki/concepts/
        OR Foundation update packet
    end note
```

## State definitions (per `hypotheses/_schema/status.yaml`)

| Status | Description |
|---|---|
| **active** | Гипотеза surfaced; test не initiated |
| **testing** | Test in progress; результаты emerging |
| **confirmed** | Test confirmed гипотезу within scope |
| **refuted** | Test refuted гипотезу within scope |
| **paused** | Testing paused; revisit trigger documented |

## Transitions + file move discipline

| Transition | Action | Skill |
|---|---|---|
| `[*] → active` | Scaffold new file в `hypotheses/active/H-NNN-<slug>.md` | `/hypothesis-add` |
| `active → testing` | `git mv` к `testing/` | `/hypothesis-update --status testing` |
| `testing → confirmed` | `git mv` к `confirmed/`; outcome + learning required | `/hypothesis-close --outcome confirmed` |
| `testing → refuted` | `git mv` к `refuted/`; outcome + learning required | `/hypothesis-close --outcome refuted` |
| `testing → paused` | `git mv` к `paused/`; outcome required | `/hypothesis-close --outcome paused` |
| `paused → active` | `git mv` back к `active/` | `/hypothesis-update --status active` |

Каждая transition → entry в `hypotheses/_log.md` (timestamp + H-NNN + transition + reason).

## F-G-R progression overlay

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph LR
    F2["F2 / R:low<br/>newly surfaced"]
    F3["F3 / R:low<br/>conceptual + method"]
    F3T["F3 / R:med<br/>mid-test"]
    F4["F4 / R:med<br/>single-context confirmed"]
    F5["F5 / R:high<br/>replicated cross-context"]
    F8["F8 / R:high<br/>constitutional<br/>(rare)"]

    F2 --> F3
    F3 --> F3T
    F3T --> F4
    F4 --> F5
    F5 -.AWAITING-APPROVAL packet.-> F8

    style F5 fill:#d6f0d6,color:#000
    style F8 fill:#ffd6d6,color:#000
```

Per `hypotheses/docs/fpf-integration.md` §2 lifecycle stage → F-G-R progression.

## Alpha state overlay

Каждая hypothesis может tracks 1-3 OMG Essence alphas independently:

```mermaid
%%{init: {'theme':'base', 'themeVariables': {'primaryTextColor':'#000000','lineColor':'#333333','primaryBorderColor':'#333333','primaryColor':'#fafafa'}}}%%
graph LR
    subgraph WORK["alpha: work"]
        W1[initiated] --> W2[prepared] --> W3[started] --> W4[under_control] --> W5[concluded] --> W6[closed]
    end
    
    subgraph WOW["alpha: way-of-working"]
        Y1[principles_established] --> Y2[foundation_established] --> Y3[in_use] --> Y4[in_place] --> Y5[working_well] --> Y6[retired]
    end
```

Per `/hypothesis-alpha-state` skill + `hypotheses/_schema/alphas.yaml`.

## Cross-refs

- Schema: `hypotheses/_schema/status.yaml` (transitions)
- Schema: `hypotheses/_schema/fgr-triple.yaml` (F-G-R progression rules)
- Schema: `hypotheses/_schema/alphas.yaml` (7 alpha state-graphs)
- Docs: `hypotheses/docs/fpf-integration.md` (Layer 5)
- Docs: `hypotheses/docs/alpha-machinery-guide.md` (Layer 6)
