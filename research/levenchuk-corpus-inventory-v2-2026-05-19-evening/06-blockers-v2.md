---
title: Phase 7 — Blockers v2 (updated from 2026-05-17)
date: 2026-05-19 evening
phase: 7
parent: research/levenchuk-corpus-inventory-v2-2026-05-19-evening/
predecessor: raw/external/levenchuk-corpus-2026-05-17/blockers.md
prose_authored_by: brigadier-scribe (Cloud Cowork)
F: F2
G: levenchuk-corpus-inventory-v2-blockers
R: high (status verified each blocker)
constitutional_posture: R1 + R6 + R11 + breadth-NOT-selection
---

# Blockers v2 — updated 2026-05-19 evening

> Status updated from 2026-05-17 baseline. Per Phase 1 §4 verification + memory cross-check.

---

## §A Resolved blockers (3) ✅

### B2 — IWE direct interaction
- **2026-05-17 status:** Pending
- **2026-05-19 status:** ✅ **RESOLVED — REJECTED**
- **Resolution:** Per memory `feedback_iwe_chat_rejected.md` 2026-05-17 evening — «Aisystant chat = помойка»; используем только text materials, не chat-mediated interaction. Reject preserved.
- **Implication для next phase:** IWE = concept only (exokortex precursor cross-cite); no chat-mediated session attempted.

### B5 — «Системный фитнес» book existence
- **2026-05-17 status:** Pending verification
- **2026-05-19 status:** ✅ **RESOLVED — practice not book**
- **Resolution:** Per existing analysis — «Системный фитнес» = practice / discipline reference, не отдельная книга в Ridero catalog. Confirmed: refreshed Ridero T2.8 (9 books) НЕ includes title «Системный фитнес». It's an Aisystant cohort practice + LJ post discussions.
- **Implication для cross-link Phase 4:** «системный фитнес» = direct operationalisation of sense-of-measure в Russian engineering tradition (per §3.1 finding 2). Cross-cite в `sense-of-measure-scientific-approach.md` wiki = gap-to-fill.

### B7 — @ailev_blog Telegram handle verification
- **2026-05-17 status:** Pending verification
- **2026-05-19 status:** ✅ **RESOLVED — CONFIRMED EXISTS**
- **Resolution:** `t.me/ailev_blog` = «Лабораторный журнал»; 2,258 subscribers; description: «трансляция блога А.И.ЛЕВенчука из ЖЖ» — mirror of LJ blog. Retrieved 2026-05-19 evening via WebFetch.
- **Implication:** Tg channel = passive mirror; no original content; LJ ailev = primary source.

---

## §B Still active / still-pending blockers (4) 🟡 + 🔴

### B1 — Aisystant subscription handoff
- **Status:** 🟡 ACTIVE (Ruslan ack «handle separately» — Option C)
- **Notes:** Per inventory v1 — Ruslan acked acquisition decision is his per `feedback_iwe_chat_rejected.md` + R11 cost discipline. No autonomous purchase.
- **Next action (Ruslan):** Subscribe / pick subset of 8 courses per Phase 5 §A overlap-ordered list.

### B3 — Residency apply path (R1-R10 refreshed)
- **2026-05-17 status:** R0/R1/R2 schedule pending
- **2026-05-19 status:** 🟡 ACTIVE (structure refreshed to R1-R10; cohort schedule via Tg bot)
- **Resolution path:** Phase 2 T1.0 refreshed structure (R1 Распожаризация → R10 Системный менеджмент); 60K ₽/each с mentor. R1 cohort 2026-04-11 already started (probably missed для current cycle); next R1 cohort ~2026-10.
- **Next action (Ruslan):** Confirm next R1 cohort date via @system_school bot; decide test cohort acquisition.

### B4 — «Инженерия интеллекта» book existence
- **Status:** 🟡 STILL PENDING Ruslan clarification
- **Notes:** Refreshed Ridero T2.8 (9 books) does NOT include title «Инженерия интеллекта». LitRes T2.10 mentions «Интеллект-стек Ч.I Deep Learning» — possibly the source of confusion. Cannot verify autonomously.
- **Next action (Ruslan):** Clarify — это сlip-of-tongue / cross-reference к Интеллект-стек 2023 / отдельная WIP book?

### B6 — YouTube transcripts
- **Status:** 🔴 STILL INFRASTRUCTURE-BLOCKED
- **Notes:** yt-dlp not used per cost cap + R11; no Whisper API calls (per memory `feedback_no_api_keys.md` — direct API costs real money). Metadata-only degrade preserved (existing in `raw/research/2026-04-28-tseren-yt-export/`).
- **Next action (separate workstream):** Re-evaluate если yt-dlp + local Whisper setup becomes available. Currently NOT in inventory scope.

---

## §C NEW blockers surfaced inventory v2 (2)

### B8 — Vendored FPF-Spec.md line-count discrepancy
- **Status:** 🟡 FLAG для Ruslan
- **Detail:** Prompt §2 stated baseline «62,202 lines / 5.7 MB» for vendored 2026-04-20 FPF-Spec.md. Actual file = **72,800 lines** (header dated «May 2026»). Two possibilities: (a) vendored file already received partial update post-04-20 not reflected в MANIFEST.md; (b) prompt baseline figure stale.
- **Investigation deferred per R11** — Foundation-adjacent vendored content; auto-pull blocked.
- **Next action (Ruslan):** Investigate via direct file diff if needed; OR acknowledge that 5+ NEW upstream patterns (C.28 / C.29 / A.6.P / A.15.4 / E.10.SEMIO) are NOT in current vendored copy and should trigger AWAITING-APPROVAL packet для updated pull.

### B9 — 10th МИМ conf 2026 canonical URL
- **Status:** 🟡 FLAG для Ruslan
- **Detail:** `events.system-school.ru/conf-2026` = 404 (Phase 1 §3.2). Conference happened 2026-04-18/19 (recovered via LJ post 1798285 with full agenda). Canonical archive URL not surfaced.
- **Workaround:** Recordings/proceedings access likely via @system_school Telegram channel or direct МИМ contact.
- **Next action (Ruslan):** If conference recordings desired, request via МИМ admin OR @system_school bot.

---

## §D Removed blockers vs inventory v1

Inventory v1 (2026-05-17) referenced blockers B8-B10 in some places — those were placeholder slots; not re-stated here. All active blockers consolidated above.

---

## §E Summary state

| Status | Count | Blockers |
|---|---|---|
| ✅ RESOLVED | 3 | B2 IWE chat / B5 «Системный фитнес» / B7 @ailev_blog handle |
| 🟡 ACTIVE / PENDING | 4 | B1 Aisystant / B3 R1-R10 cohort / B4 «Инженерия интеллекта» / B8 FPF vendored discrepancy + B9 10th conf URL |
| 🔴 INFRA-BLOCKED | 1 | B6 YT transcripts |
| TOTAL | 8 | (B8 + B9 are new vs inventory v1) |

---

*Blockers v2 closure 2026-05-19 evening Berlin.*
