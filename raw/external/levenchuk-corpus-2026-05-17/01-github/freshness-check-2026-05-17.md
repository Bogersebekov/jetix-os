---
title: FPF upstream freshness check vs vendored copy
date: 2026-05-17
type: provenance-check
source_local: raw/external/ailev-FPF/FPF-Spec.md (vendored 2026-04-20)
source_upstream: github.com/ailev/FPF main branch HEAD as of 2026-05-17
F: F4
G: external-corpus
R: refuted_if_commit_sha_wrong
prose_authored_by: claude (scribe)
---

# FPF upstream freshness check — 2026-05-17

## §1 Upstream HEAD (via api.github.com/repos/ailev/FPF/commits/main)

```
sha:  c86eabdd0dd6060863f2abf1f65ab91e6ca9af47
date: 2026-05-16T08:49:40Z
msg:  corrections for E.10.SEMIO campaign
```

## §2 Local vendored copy

- **Path:** `raw/external/ailev-FPF/FPF-Spec.md`
- **Vendored date:** 2026-04-20
- **Per ATTRIBUTION.md:** "commit-source: main branch HEAD at 2026-04-20"
- **Volume:** 62,202 lines / 5.7 MB

## §3 Delta

- **Calendar gap:** ~26 days (2026-04-20 → 2026-05-16)
- **Latest visible commit topic:** "E.10.SEMIO campaign" — Левенчуковский semio-architecture workstream (10-campaign plan per R-A §3.4, "semio-architecture workstream: Currently in development (10 campaign plan as of April 2026), formalizing semiotic concepts for engineering projects").
- **Per LJ 2026-02 post (FPF dev plans):** Levenchuk is actively iterating language-precision cluster (A.6.P), TGA, problem-solving factory, holonic conflict ontology, Q-bundle architecture characteristics, SoTA-packs (Part G).

## §4 Decision for Phase A

- **Vendored copy is sufficient** для distillation work § 3-4-5. Кernel architecture stable (Parts A-K — established before 2026-04-20).
- Active dev = E.10.SEMIO (semiotics) + A.6.P (compression-decompression) — нюансы вне ядра.
- **No re-vendor for Phase A.** Update vendored copy can be done in Phase B if needed (after Ruslan ack).
- **Provenance note** added к all FPF-Spec citations in distillation: «cited as of 2026-04-20 vendored copy; upstream HEAD c86eabd as of 2026-05-16».

## §5 Other ailev/* repos (Category 01.03 in inventory)

Per inventory §1 Category 01, listing `ailev/*` repositories was deferred. WebFetch / curl на `api.github.com/users/ailev/repos` would resolve. **Status: TODO if Phase B needs it.** Per prompt §1.2.1, FPF + Readme — main artifacts; other repos likely peripheral.
