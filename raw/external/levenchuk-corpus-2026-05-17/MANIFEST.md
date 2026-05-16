---
title: Levenchuk corpus collection MANIFEST — Phase A
date: 2026-05-17
type: corpus-manifest
F: F6
G: external-corpus-manifest
R: refuted_if_paths_wrong_OR_volumes_off
prose_authored_by: claude (scribe)
---

# Phase A Collection MANIFEST — 2026-05-17

## §1 What was collected (raw/external/levenchuk-corpus-2026-05-17/)

| Subdir | Files | Description | Volume |
|--------|-------|-------------|--------|
| `01-github/` | freshness-check-2026-05-17.md | FPF upstream HEAD vs local vendored copy delta | 1 small file |
| `02-livejournal/` | key-posts-captured-2026-05-17.md | 9 captured items (5 LJ posts + Psybertron + Цэрэн profile + МИМ team + intellect-stack page) | ~12K words |
| `03-youtube/` | (empty — transcripts blocked, see blockers.md B6) | YouTube blocked per infrastructure | metadata-only via 2026-04-28 analysis |
| `04-books-outlines/` | (empty — paid; waiting Ruslan handoff per blockers.md B1) | Books not captured Phase A | 0 |
| `05-aisystant-public/` | (empty — would need full subscription per blockers.md B1) | aisystant paid; awaiting | 0 |
| `06-tseren-iwe/` | (Tseren TG + YT analysis already in raw/research/2026-04-28-tseren-{tg,yt}-export/) | Existing-in-repo, see inventory category 10 | 618 TG posts + 127+452+37 YT metadata |
| `07-third-party-discussions/` | (Psybertron review captured in 02-livejournal/key-posts file — only English review of substance found) | Habr/vc.ru deferred per blockers.md B9 | minimal |
| `blockers.md` | explicit blockers list | what Ruslan needs to unblock | this file |
| `00-INVENTORY.md` | full inventory pre-collection | 10 categories | this file |
| `MANIFEST.md` | this file | post-collection summary | self |

## §2 What was NOT collected (and why)

### §2.1 Paid (Ruslan handoff awaited — blockers.md B1-B3)
- Aisystant 8+ courses (Системное мышление / Методология / Системная инженерия / Системный менеджмент / Инженерия личности / Интеллект-стек / Собранность / R0-R1-R2 residencies)
- 9+ Ridero books (Системное мышление 2024 vol 1+2, Методология 2025, Системная инженерия 2022, Системный менеджмент 2023, Инженерия личности 2023, Интеллект-стек 2023, Визуальное мышление 2018, English Systems Thinking 2020)
- IWE empirical sessions
- Residency cohort experience

**Rationale:** Per §0.0 ack Ruslan handles paid layer; server-side CC scope = public + existing repo extracts.

### §2.2 Infrastructure-blocked (blockers.md B6)
- 579 YouTube videos full transcripts (metadata available, captions blocked at IP level)

### §2.3 Tier 4 deferred (blockers.md B8-B10)
- arXiv PDFs (content already absorbed in R-A)
- Habr / vc.ru third-party (interpretations preferred over primary)
- Tseren Medium English blog

## §3 Cumulative corpus available для §3 Distillation

### §3.1 Already-in-repo (Category 10 of inventory — heavy material)

- `raw/external/ailev-FPF/FPF-Spec.md` — **62,202 lines** primary FPF spec
- `raw/external/ailev-FPF/Readme.md` — 384 lines orientation
- `raw/research/levenchuk-deep-research-2026-04-18.md` — 361 lines bio
- `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` — 1041 lines AI angle
- `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` — 2456 lines KB
- `raw/research/fpf-gap-analysis-2026-04-20.md` — 2486 lines gap analysis
- `raw/research/levenchuk-fpf-research-2026-04-20/R-A` — biographical/corpus map (~12K words)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-B` — 5 ШСМ primitives deep (26K tokens)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-C` — 17 transdisciplines mapping (30K tokens)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-D` — Essence × ШСМ (~10K tokens — read)
- `raw/research/levenchuk-fpf-research-2026-04-20/R-E` — mereology + holon hierarchy (27K tokens)
- `raw/research/step-2-2-2-extractions/{A,B,C,D,E}*.md` — 5 sub-agent extractions
- `raw/research/2026-04-28-tseren-tg-export/` — 618 Tseren posts + analysis report
- `raw/research/2026-04-28-tseren-yt-export/` — 127 + 452 YT video metadata + analysis
- `profiles/l1-first-clan/{anatoliy-levenchuk,tseren-tserenov}.md` — L1 profiles
- `_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md` — synthesis

### §3.2 New (Phase A collected)

- 02-livejournal/key-posts: FPF dev plans Feb 2026 + alpha post 2024 + 10th MIM conf 2026 + residency announcement + methodology in intellect-stack post + Psybertron review + Tseren systemsworld profile + МИМ team page + intellect-stack 16-disc list
- 01-github: FPF freshness vs upstream

### §3.3 Composite estimated reading volume

- Primary FPF spec: 62K lines (~250K words)
- Existing research extractions: ~50K words
- New Phase A captures: ~12K words
- Tseren TG corpus analysis: ~10K words (analysis report only)
- **Total ~320K words distillation source**

Enough material для thoroughly answering §3.1 (1-12) prompt questions. Paid books would add depth (e.g., specific R0/R1 curriculum details) but not change top-line answers.

## §4 Provenance trail

Все captured content carries:
- Source URL or file path
- Retrieved date
- Retrieval tool (WebFetch / Read / Bash curl)
- Verbatim quotes preserved где captured

Per Tier 2 R6 (provenance per item): no claim в distillation reports без source attribution.

## §5 Cost snapshot end-of-collection

- €0 external spend Phase A collection
- WebFetch calls used: ~9 (within Claude Code built-in tool allowance)
- curl calls: 1 (GitHub API)
- Read calls: ~12 (existing repo material)
- **Within €10/день baseline cap by wide margin.**

---

*Collection complete. Proceeding to §3 Distillation with composite corpus.*
