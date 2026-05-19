---
title: Phase 1 — Freshness Deltas (Levenchuk Corpus Inventory v2)
date: 2026-05-19 evening
phase: 1
parent_prompt: prompts/levenchuk-corpus-inventory-v2-2026-05-19-evening.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: levenchuk-corpus-inventory-v2
R: medium (verified via WebFetch + GitHub REST API + repo file inspection 2026-05-19 evening Berlin)
constitutional_posture: R6 provenance per source / R11 Default-Deny (no auto-pull of FPF-Spec) / breadth-NOT-selection
---

# Phase 1 — Freshness Deltas

> Comparison: 2026-05-17 substrate (existing inventory) vs current state 2026-05-19 evening. Documents what's new / changed / still-blocked. **NO auto-pull of FPF-Spec** (R11 Default-Deny — Foundation-adjacent vendored content).

---

## §1 FPF upstream freshness — `github.com/ailev/FPF`

### §1.1 Repo summary
- URL: `https://github.com/ailev/FPF`
- Stars: **368** (as of 2026-05-19)
- `updated_at`: 2026-05-19
- Tool: `curl https://api.github.com/users/ailev/repos?per_page=100&sort=updated` + `python3 -c json.load`
- Retrieved: 2026-05-19 evening
- F-G-R: F2 / corpus-map / R-high (direct API)

### §1.2 Top-20 commits HEAD (newest first)

| SHA | Date (UTC) | Message |
|---|---|---|
| 46d5d58 | 2026-05-17 21:19 | first principles in C.29 and pillars |
| 5e0232a | 2026-05-17 14:56 | C.29 - mathematical lens adequacy |
| c86eabd | 2026-05-16 08:49 | corrections for E.10.SEMIO campaign |
| 34bad8f | 2026-05-16 07:02 | E.10.SEMIO plain text preservation |
| 37a1906 | 2026-05-15 23:29 | E.10.SEMIO cleanup for all FPF |
| 7f8a04c | 2026-05-15 08:50 | E.10.SEMIO and episteme semiotic ontology |
| ee40821 | 2026-05-12 16:57 | formatting for GitHub |
| 2b3e0f4 | 2026-05-12 16:45 | admissible action in problematic situations |
| f73766d | 2026-05-12 13:41 | functional descriptions and new A.15.4 |
| 136be3b | 2026-05-10 06:26 | A.6.P terminology cleanup |
| 1f7c9e5 | 2026-05-08 17:00 | authority-looking reliance tuning |
| 1f21daa | 2026-05-04 21:36 | terminology cleaning (counterfactuality) |
| 9cb163b | 2026-05-04 19:48 | Causality and Realizability |
| 34b4d63 | 2026-04-30 15:03 | temporal claim adequacy |
| b18acde | 2026-04-27 19:17 | terminology cleanup in E.8, E.9, E.19 |
| 53d1f69 | 2026-04-26 22:05 | quantum-like cluster |
| ef3566e | 2026-04-24 20:51 | controlled semantic coarsening |
| a2c5d62 | 2026-04-23 13:55 | E.9 (DRR for FPF) major update |
| dba54a2 | 2026-04-21 17:40 | less disclaimers |
| 975d8d4 | 2026-04-21 17:30 | recognizability |

### §1.3 Major new patterns added since 2026-04-20 vendored baseline

Per top-20 commit titles + upstream README cross-check (`raw.githubusercontent.com/ailev/FPF/main/Readme.md` retrieved 2026-05-19):

| New / updated pattern | First commit visible | Topic |
|---|---|---|
| **C.29** — Mathematical lens adequacy | 5e0232a 2026-05-17 (+ 46d5d58 2026-05-17 first principles + pillars) | Adequacy of mathematical apparatus for engineering work |
| **C.28** — Causality & Realizability | 9cb163b 2026-05-04 (+ 1f21daa 2026-05-04 counterfactuality cleanup) | Causal-use / counterfactual-support repair patterns |
| **E.10.SEMIO** — Semiotic ontology campaign | 7f8a04c 2026-05-15 + 37a1906 2026-05-15 + 34bad8f 2026-05-16 + c86eabd 2026-05-16 | Semio patterns for publication / use boundaries; episteme semiotic ontology |
| **A.6.P** — Boundary precision restoration (RPR) | 136be3b 2026-05-10 | Boundary precision restoration discipline; terminology cleanup |
| **A.15.4** — Functional descriptions | f73766d 2026-05-12 | New section on functional descriptions; admissible action in problematic situations |
| **Authority-looking reliance tuning** | 1f7c9e5 2026-05-08 | (terminology / pattern tuning) |
| **Temporal claim adequacy** | 34b4d63 2026-04-30 | Temporal adequacy refinements |
| **E.8 / E.9 / E.19** terminology | b18acde 2026-04-27 + a2c5d62 2026-04-23 (E.9 DRR major) | Decision-Record-Record (DRR) major update; Episteme terminology |
| **Quantum-like cluster** | 53d1f69 2026-04-26 | Quantum-like pattern cluster |
| **Controlled semantic coarsening** | ef3566e 2026-04-24 | Semantic coarsening as managed degradation |

### §1.4 Vendored vs upstream — line-count delta

- Vendored `raw/external/ailev-FPF/FPF-Spec.md` line count: **72,800** (header says "May 2026"; vendored 2026-04-20 per `MANIFEST.md`)
- Vendored `raw/external/ailev-FPF/Readme.md` line count: 384
- Upstream HEAD line count of `FPF-Spec.md`: not fetched (R11 Default-Deny — would require auto-pull); flag для Ruslan если нужен exact delta
- **Discrepancy note:** Prompt §2 reported baseline as "62,202 lines / 5.7 MB". Actual vendored file = 72,800 lines. Two possibilities: (a) vendored file already received partial update post-04-20 not reflected in MANIFEST.md; (b) prompt baseline figure was stale. **Flag for Ruslan** — investigation требует direct file diff which is out-of-scope для inventory phase.

### §1.5 R11 Default-Deny posture
- **NO auto-pull of FPF-Spec.md** executed
- Rationale: Foundation-adjacent vendored content; updates require AWAITING-APPROVAL packet (Part 6b §I.2)
- Surfacing only: «10+ new patterns добавлены upstream since 2026-04-20 vendored baseline; Ruslan decides pull or skip»

---

## §2 LJ ailev.livejournal.com freshness

### §2.1 Latest posts (top-5 visible на homepage 2026-05-19 evening)

| # | Date | URL | Title | Topic |
|---|---|---|---|---|
| 1 | **2026-05-18** ⭐ NEW since 17.05 | https://ailev.livejournal.com/1801412.html | «Адекватное использование математики — уже в FPF» | New FPF pattern C.29 on mathematical apparatus adequacy for engineering work |
| 2 | 2026-05-16 | https://ailev.livejournal.com/1801179.html | «lytdybr» (lifestream entry) | Reflections on revising system thinking guidelines and МИМ organizational structure |
| 3 | 2026-05-11 | https://ailev.livejournal.com/1800779.html | «lytdybr» (lifestream entry) | Semiotic architecture refinement work and Second Principles Framework experiments |
| 4 | 2026-05-10 | https://ailev.livejournal.com/1800477.html | «Доработки формулировок допусков к работе — уже в FPF» | MCP server launch for FPF and work authorization semantic patterns |
| 5 | 2026-05-05 | https://ailev.livejournal.com/1800060.html | «Что было бы, если бы: причинность и реализуемость» | New FPF pattern C.28 on causality and counterfactual realizability in engineering |

### §2.2 Delta vs 2026-05-17 substrate

- **1 new post** identified since 2026-05-17 evening: **2026-05-18 post 1801412** «Адекватное использование математики — уже в FPF»
- Topic = FPF C.29 commentary (mirrors 2026-05-17 upstream commit `5e0232a` + `46d5d58`)
- All earlier 4 posts (2026-05-05 → 2026-05-16) были already в 2026-05-17 inventory scope; re-verified existence + URLs стабильны

### §2.3 Provenance
- URL: `https://ailev.livejournal.com`
- Retrieved: 2026-05-19 evening
- Tool: WebFetch
- F-G-R: F2 / corpus-map / R-high (direct fetch homepage)

---

## §3 ШСМ events freshness

### §3.1 events.system-school.ru
- WebFetch returned: no specific dated events on landing page
- Site indicates: «Регулярно: Мы проводим два типа семинаров» (free intro + paid workshops)
- Cohort dates: только через Telegram bot @system_school (not autonomously fetchable)
- Tool: WebFetch
- Retrieved: 2026-05-19 evening
- F-G-R: F2 / corpus-map / R-medium

### §3.2 10th МИМ conference 2026 page
- URL: `https://events.system-school.ru/conf-2026`
- Status: **HTTP 404 Not Found**
- Interpretation: либо URL slug изменился, либо страница не публиковалась под этим путём, либо конференция не объявлена под slug `conf-2026`
- Cross-ref: LJ post 1798285 (2026-02) per existing 2026-05-17 inventory mentioned "10th MIM conf 2026"; possibly anonymously hosted либо not indexable at root events.system-school.ru
- **Flag** для Ruslan: confirm canonical URL для 10th conf 2026 (либо через Tg/email subscription, либо direct ask к МИМ admin)
- F-G-R: F2 / corpus-map / R-medium

### §3.3 system-school.ru main offerings (refreshed)

| Section | Content |
|---|---|
| Main programs | Personal Development («Личное развитие») / Work Development («Рабочее развитие») / Self-Study Subscription / Top Management Team / Corporate Talent Pipeline |
| Core framework | Intelligence Stack underpins all programs |
| Residency designation | «резидентуры и практикумы с наставником» mentioned; **NO explicit R0/R1/R2 nomenclature** на main page |
| Cohort schedule | Telegram bot provides «дату ближайшего потока» |
| Navigation | About / Programs / Research / Community / Team / Contacts |

- F-G-R: F2 / corpus-map / R-high (direct fetch)
- Note re R0/R1/R2: inventory v1 (2026-05-17) used designations R0/R1/R2 per LJ post 1777145 Autumn 2025 residency announcement; live site main page does not surface those slugs publicly. R0/R1/R2 — internal cohort taxonomy not advertised на landing.

---

## §4 Blocker status update

| # | Blocker (2026-05-17) | Status 2026-05-19 | Notes |
|---|---|---|---|
| B1 | Aisystant subscription handoff | **ACTIVE** (Ruslan ack «handle separately» — Option C) | Per existing 2026-05-17 inventory; awaiting Ruslan acquisition decision per Phase 5 doc |
| B2 | IWE direct interaction | ✅ **RESOLVED — REJECTED** | Per memory `feedback_iwe_chat_rejected.md` 2026-05-17 evening: «Aisystant chat = помойка»; use materials only, no chat-mediated interaction |
| B3 | Residency R0/R1/R2 apply path | **ACTIVE** | Ruslan acked apply but cohort schedule pending; Phase 1 §3.2 confirmed schedule fetchable only via Tg bot |
| B4 | «Инженерия интеллекта» book existence | 🟡 **STILL PENDING Ruslan clarification** | Per existing inventory; cannot verify autonomously |
| B5 | «Системный фитнес» book existence | ✅ **RESOLVED — practice not book** | Per existing 2026-05-17 analysis: «Системный фитнес» = practice / discipline reference, не отдельная книга в Ridero catalog |
| B6 | YouTube transcripts | 🔴 **STILL INFRASTRUCTURE-BLOCKED** | yt-dlp not used per cost cap + R11; metadata-only degrade preserved |
| B7 | @ailev_blog handle verification | ✅ **RESOLVED — CONFIRMED EXISTS** | `t.me/ailev_blog` = «Лабораторный журнал»; 2,258 subscribers; mirror of LJ blog. Retrieved 2026-05-19 evening via WebFetch |

---

## §5 GitHub `ailev/*` other repos listing

Per `curl https://api.github.com/users/ailev/repos?per_page=100&sort=updated` (retrieved 2026-05-19):

| Repo | Updated | Stars | Description |
|---|---|---|---|
| **FPF** | 2026-05-19 | 368 | First Principles Framework (FPF): Pattern language and core specification for adequate engineering thinking |
| anird | 2020-12-15 | 7 | Reference Data for Anime and Manga — Ontology Summit 2014 Hachathon |
| ailev.github.io | 2020-12-14 | 0 | (empty / no description) |

**Finding:** Only **3 public repos** total. FPF — единственный активный; остальные 2 inactive >5 years (Dec 2020). Confirms FPF = single active substrate под `github.com/ailev/`.

- F-G-R: F2 / corpus-map / R-high (direct API)

---

## §6 New sources surfaced на этом phase

Cross-references discovered during Phase 1 fetches:

| # | Source | URL | Status |
|---|---|---|---|
| N.1 | FPF MCP server | (mentioned в LJ post 2026-05-10 «MCP server launch for FPF»; concrete URL not surfaced на homepage) | 🟡 surfaced — needs Tier 2 explicit fetch |
| N.2 | «Second Principles Framework» experiments | (mentioned в LJ post 2026-05-11 «lytdybr») | 🟡 mention only; no separate corpus URL identified |
| N.3 | Telegram bot @system_school (cohort schedule) | `t.me/system_school` (suggested by system-school.ru main page) | 🟡 surfaced — not autonomously fetched (bot interaction out-of-scope) |

---

## §7 Phase 1 acceptance check

Per Phase 0 §5 acceptance predicate item 1 («FPF freshness verified vs 2026-04-20»):

- ✅ FPF upstream commits с 2026-04-21 → 2026-05-17 enumerated (20 commits)
- ✅ Major new patterns since vendored baseline catalogued (C.28 / C.29 / A.6.P / A.15.4 / E.10.SEMIO + E.9 DRR major + quantum-like + semantic coarsening)
- ✅ LJ delta identified (1 new post since 17.05: 2026-05-18 post 1801412)
- ✅ ШСМ events delta surfaced (no new public-page announcements; 10th conf URL 404)
- ✅ Blockers updated (B2 + B5 + B7 resolved; B4 + B6 still flagged; B1 + B3 active)
- 🟡 Vendored line-count discrepancy flagged для Ruslan (72,800 actual vs prompt-stated 62,202 baseline)

**Phase 1 complete — substrate готов для Phase 2 Tier 1 collection.**

---

*Phase 1 closure 2026-05-19 evening Berlin. Cost: ~3 WebFetch + 2 curl API calls + 1 Read = <€0.20.*
