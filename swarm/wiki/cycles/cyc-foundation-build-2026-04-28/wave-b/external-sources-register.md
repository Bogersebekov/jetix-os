---
title: External Sources Register — Wave B-2 web URLs aggregated across 14 consultant cards
date: 2026-04-27
phase: B-2-aggregation
expert: brigadier
mode: routing
cycle: cyc-foundation-build-2026-04-28
total_sources: ~50-55 declared (5 mandatory × 5 frameworks + 0-2 optional × 9 frameworks)
quality_grades: A-predominant; some B-context; 0 C
F4_NOT_LIVE_FETCHED_flag: 4 cards (anthropic-constitutional-ai / event-sourcing-cqrs / sre-observability / mereology-typed-edges)
---

# External Sources Register

> Per spec §11 deliverable checklist: "all 70-85 web URLs, 5/framework × 14-17, with quality grades". Actual count this cycle: ~50-55 (5 frameworks didn't need 5 web sources because library coverage was strong).

> **Index-only aggregation.** Detailed source notes + relevance grades + 1-paragraph reasoning live in each consultant card §3. This document indexes which framework points to which web URLs.

---

## §1 Per-framework external source pointers (14 frameworks)

For each framework, see consultant card §3 for full source URLs + relevance grades + 1-paragraph notes:

| # | Framework slug | Card path §3 | External source count | F4 flag? |
|---|----------------|---------------|------------------------|----------|
| 1 | levenchuk-shsm-fpf | `wave-b/consultants/levenchuk-shsm-fpf.md §3` | 5 (suggested LJ posts not in disk corpus + FPF-Spec changelog + ШСМ public lectures + Левенчук Twitter highlights + ШСМ courses) | NO — overlaps with library |
| 2 | systems-thinking-cybernetics | `wave-b/consultants/systems-thinking-cybernetics.md §3` | 5 (Donella Meadows Institute / Beer archive / contemporary VSM applications) | NO — library STRONG |
| 3 | multi-agent-architecture | `wave-b/consultants/multi-agent-architecture.md §3` | 5 (Latest Anthropic skills 2025-2026 / LangGraph / CrewAI / recent MAST / AutoGen-SmolAgents) | NO |
| 4 | knowledge-management-karpathy-luhmann-matuschak | `wave-b/consultants/knowledge-management-karpathy-luhmann-matuschak.md §3` | 5 (Matuschak evergreens / Schmidt Luhmann Sociologica / Forte PARA / Karpathy bearblog / Matuschak+Nielsen ttft) | NO — verified web URLs at grade A |
| 5 | event-sourcing-cqrs | `wave-b/consultants/event-sourcing-cqrs.md §3` | 5 (Kleppmann DDIA Ch. 10-11 / Greg Young CQRS Documents / Fowler EventSourcing+CQRS bliki / Vernon IDDD Ch. 8 / Dahan Clarified CQRS) | **YES — F4-NOT-LIVE-FETCHED** |
| 6 | sre-observability | `wave-b/consultants/sre-observability.md §3` | 5 (Google SRE Book / Observability Engineering / Practical Monitoring / OpenTelemetry / Implementing SLOs) | **YES — F4-NOT-LIVE-FETCHED** |
| 7 | compounding-engineering | `wave-b/consultants/compounding-engineering.md §3` | 0-2 optional | NO — library STRONG |
| 8 | product-management-cagan-shape-up | `wave-b/consultants/product-management-cagan-shape-up.md §3` | 0-2 optional | NO — library STRONG |
| 9 | stoic-epistemic | `wave-b/consultants/stoic-epistemic.md §3` | 0-2 optional | NO — library STRONG |
| 10 | capital-allocation-antifragility | `wave-b/consultants/capital-allocation-antifragility.md §3` | 0-2 optional | NO — library STRONG |
| 11 | unix-philosophy | `wave-b/consultants/unix-philosophy.md §3` | 1-2 (supplement Kernighan-Pike unusable on disk) | NO |
| 12 | clean-code | `wave-b/consultants/clean-code.md §3` | 1-2 (Brooks "No Silver Bullet" 1987 IEEE essay supplement) | NO |
| 13 | anthropic-constitutional-ai | `wave-b/consultants/anthropic-constitutional-ai.md §3` | 5 (Bai 2022 / Askell 2021 HHH / Anthropic RSP / Anthropic Model Spec / 1 currency) | **YES — F4-NOT-LIVE-FETCHED** |
| 14 | mereology-typed-edges | `wave-b/consultants/mereology-typed-edges.md §3` | 5 (SEP Mereology / Leśniewski / Lewis 1991 Parts of Classes / Fine 1999 Things and Their Parts / Varzi survey) | **YES — F4-NOT-LIVE-FETCHED** |

**Aggregate**:
- Frameworks with 5 mandatory web sources (no/partial library coverage): 5, 6 (#5, #6) + #4 (KM) + #13 + #14 = 5 frameworks × 5 = 25 URLs
- Frameworks with 5 currency-only web sources (library STRONG, 5 for 2025-2026 currency): #1, #2, #3 = 3 × 5 = 15 URLs
- Frameworks with 0-2 optional web sources: #7, #8, #9, #10, #11, #12 = 6 × 0-2 ≈ 0-12 URLs
- **Total**: 40-52 web URLs declared across 14 cards

---

## §2 Quality grade distribution (across all cards' §3)

- **Grade A** (peer-reviewed paper / official docs / Anthropic-Cognition-Karpathy-tier blog / canonical book / standards body): ~40+ URLs (predominant)
- **Grade B** (background context, indirectly applicable): ~10 URLs
- **Grade C** (context-only, cite if challenged): 0 URLs (none accepted; quality bar held)

Per spec §5 Phase B-2 "External 5-sources rule" + Ruslan ack: source quality bar held; reject Medium-tier rehashes / listicles / AI-generated SEO.

---

## §3 F4 quality flag — 4 cards with NOT-LIVE-FETCHED web sources

Per spec §15 R5 (Provenance mandatory + audit-trail) + Ruslan emphasis #1 (100% framework foundation studied marking, transparently flagged where coverage <100%):

| Card | F4 sources | Reason | Brigadier action recommended |
|------|------------|--------|------------------------------|
| anthropic-constitutional-ai #13 | S1-S4 | philosophy-expert agent lacks WebFetch tool per frontmatter | WebFetch validation in Wave D OR declare in AWAITING-APPROVAL §5 as F4-trained-knowledge basis |
| event-sourcing-cqrs #5 | S1-S5 | engineering-expert agent in this dispatch lacks WebFetch tool | same |
| sre-observability #6 | S1-S5 | engineering-expert agent in this dispatch lacks WebFetch tool | same |
| mereology-typed-edges #14 | S1-S5 | philosophy-expert agent lacks WebFetch tool | same |

**Mitigation**: brigadier (canonical, has WebFetch) can run validation post-AWAITING-APPROVAL ack if Ruslan requires 100% live-verified before promotion to canonical Foundation. AWAITING-APPROVAL packet §5 declares this honestly per spec §15 R5.

---

## §4 Provenance

This register itself is an aggregation — every detail lives in the cited consultant cards' §3 Sources sections. No new claims introduced here.

| Claim | Source |
|-------|--------|
| 14 consultant cards with §3 web sources | `wave-b/consultants/*.md` (14 files) |
| F4 flag for 4 cards | `wave-b/consultants/{anthropic-constitutional-ai,event-sourcing-cqrs,sre-observability,mereology-typed-edges}.md §1` |
| Quality grade discipline | spec §5 Phase B-2 "Quality bar: peer-reviewed paper / official docs / etc" |
| Total source count vs spec target 70-85 | spec §11 deliverable checklist |
