---
title: "Diagram 03 — Critical Path 7-14d Gantt (BL-1 cascade)"
date: 2026-05-19
type: mermaid-diagram
parent_doc: 02-action-plan-proposal.md
diagram_id: 03
---

# Diagram 03 — Critical Path 7-14 day Gantt

```mermaid
gantt
    title BL-1 Cascade — 7-step Critical Path Steps 0-6
    dateFormat YYYY-MM-DD
    axisFormat %d.%m

    section Step 0 — 6th resource ack
    Surface 6 candidates (DONE этим run) :done, s0prep, 2026-05-19, 0d
    Ruslan ack 6th category              :crit, s0, 2026-05-20, 1d

    section Step 1 — Monetization
    Author monetization model C.7        :crit, s1, after s0, 5d

    section Step 2 — Pitch
    Pitch one-pager C.1                  :crit, s2a, after s0, 4d
    Pitch deck v1 C.2                    :crit, s2b, after s1, 5d

    section Step 3 — Grundstück
    Broker engagement (parallel)         :s3, 2026-05-20, 14d
    Workshop spec C.8                    :s3b, after s2a, 3d

    section Step 4 — Outreach queue
    Outreach queue v1 C.9 + CRM tag      :s4, after s0, 4d

    section Step 5 — Daily cadence
    Templated pitch sequences            :s5a, after s2a, 3d
    Hire помощник                        :s5b, after s2a, 5d
    Daily 10-20/day cadence (ongoing)    :active, s5c, after s4, 60d

    section Step 6 — Engineer cohort
    Identify 5-15 candidates             :crit, s6a, after s5a, 7d
    Outreach с pitch v1                  :crit, s6b, after s2b, 7d
    Q3 hackathon engineer secured        :milestone, m1, 2026-07-01, 0d

    section Milestones
    P1-10 ack                            :milestone, p10, 2026-05-21, 0d
    Pitch v1 ready                       :milestone, p3, 2026-06-02, 0d
    Outreach cadence sustained 2-week    :milestone, p6, 2026-06-15, 0d
    BL-1 unblocked                       :milestone, bl1, 2026-06-20, 0d
    Q3 2026 first hackathon              :milestone, q3, 2026-09-01, 0d
```

---

## Critical path commentary

- **Step 0 (1-day blocker)** unblocks Steps 1, 5: 6-resource clarity → monetization category + outreach queue tagging
- **Steps 1+2 sequential** — monetization → pitch (pitch needs unit econ)
- **Steps 3+4 parallel** — Grundstück broker + outreach queue (independent)
- **Step 5 ongoing** — daily cadence starts after pitch artifact ready
- **Step 6 = STOPPER UNBLOCK** — engineer cohort identification + outreach с pitch v1; 7d sprint after Step 2 done
- **Q3 2026 milestone** — first hackathon event (Berlin or adjacent; €23K budget; 30 participants 5-7 teams)

## F-grade per step

| Step | F | Aspirational vs operational |
|---|---|---|
| 0 | F2 (gap question) | Operational ack |
| 1 | F2 (aspirational $1B target) + F4 (unit econ math) | Mixed |
| 2 | F3 (pitch quality) | Operational |
| 3 | F4 (2-month timeline anchor) | Operational |
| 4 | F4 (150-300 contacts cascade math) | Operational |
| 5 | F3 (sustained cadence; depends on помощник + execution) | Operational |
| 6 | **F5 STOPPER** (Ruslan-explicit; primary blocker) | Critical |
| Q3 milestone | F2 aspirational | Aspirational |

---

*Mermaid diagram 03 for Doc 2 §1 sprint-synthesis-2026-05-19.*
