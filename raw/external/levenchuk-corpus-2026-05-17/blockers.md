---
title: Blockers — what needs Ruslan for Levenchuk corpus Phase A
date: 2026-05-17
type: blockers-explicit
F: F8
G: external-corpus
R: refuted_if_addressed_silently
prose_authored_by: claude (scribe)
purpose: |
  Explicit list of blockers from §1 Inventory + actually-encountered blocks
  during §2 Collection. For Ruslan decision-making at end of Phase A.
language: russian
---

# Blockers — Phase A Левенчук corpus collection

## Tier 1 — Critical (Phase B blocked without)

### B1. Aisystant subscription credential handoff
- **Inventory ref:** 04.01-04.11
- **Status:** RUSLAN-ACK 2026-05-17 (Ruslan платит, server CC может тащить)
- **Block:** server-side CC не имеет credentials. Без них только public landing pages WebFetch.
- **Resolution path:**
  - Option A (preferred): Ruslan logs into aisystant in browser, exports HTML/PDF of courses (curse outline + sample chapters) to a local dir, рассказывает CC где взять
  - Option B: Ruslan provides session cookies / token if API supports
  - Option C: defer paid content to Phase B; Phase A работает только с public layer + R-A/R-B/R-C/R-D/R-E уже-extracted material
- **Phase A decision:** Option C — proceed with Phase A using existing extracted material + public sources. Paid content waits for Ruslan handoff (Phase B input).

### B2. IWE direct interaction
- **Inventory ref:** 04.09, 08.10
- **Status:** Critical for answering Левенчуковский C5 («IWE опирается на FPF — и понятно за счёт чего его IWE умнее конкурентов»)
- **Block:** IWE = embedded AI in aisystant; needs subscription + interactive session
- **Resolution path:**
  - Ruslan самостоятельно делает 5-10 sessions с IWE на типичные вопросы из Jetix domain (Project management, monetization, etc.)
  - Records the sessions (full transcripts) → puts in `raw/external/levenchuk-corpus-2026-05-17/04-books-outlines/iwe-interaction-log-YYYY-MM-DD.md`
- **Phase A decision:** distillation §3.2 records what IWE IS conceptually (per Левенчук + R-A + conference talk references). Empirical IWE behavior waits for Ruslan sessions.

### B3. Residency R0/R1/R2 application + cohort start
- **Inventory ref:** 04.10
- **Status:** RUSLAN-ACK 2026-05-17 («apply на ближайший cohort»)
- **Block:** Apply form requires identity + payment; cohort start dates discrete (per LJ 2025-09 post: R0 next likely starts Oct 2026 unless mid-year offering exists)
- **Resolution path:** Ruslan applies; cohort schedule TBD; format details come from inside experience
- **Phase A decision:** Residency format documented from LJ Autumn 2025 post + conference references (mentor-led «разборы», 10-15h/week, 19 sessions for R1). Insider experience waits.

## Tier 2 — Clarification needed

### B4. «Инженерия интеллекта» (Engineering of Intelligence)
- **Inventory ref:** 05.11
- **Block:** упомянут в prompt §1.2.5, но не найден в R-A bibliography 2026-04-18 nor in LJ Apr 2024 / Feb 2026 posts
- **Possible interpretations:**
  - (a) Future title not yet published (FPF-aligned book?)
  - (b) Misnamed «Инженерия личности» (existing 2023 book)
  - (c) IWE-platform artifact (not a book — but a product)
  - (d) Sequence of blog posts under some tag
  - (e) Левенчуковский future curriculum module
- **Resolution:** Ruslan, какое из (a)-(e) правильно? Если (b) — proceed with «Инженерия личности 2023». Если (c) — IWE itself. Если (a)/(d)/(e) — uniquely deferred.

### B5. «Системный фитнес»
- **Inventory ref:** 05.10
- **Block:** упомянут в prompt §1.2.5, но в R-A bibliography НЕ как book — а как PRACTICE (per 10th MIM conf 2026: Pyotr Leontiev's talk «System fitness work in 2025-2026»)
- **Possible interpretations:**
  - (a) Practice, not a book — physical/cognitive routine under Tier «Personal Development»
  - (b) Book in development (Leontiev possibly authoring)
- **Resolution:** Per LJ post 3 evidence, «System fitness» = PRACTICE (sub-program of Personal Development track), not a standalone Левенчуковский book. **Treating as resolved: not a book — practice/curriculum component.**

## Tier 3 — Infrastructural (blocked at server level)

### B6. YouTube transcripts (ШСМ + Tseren channels)
- **Inventory ref:** 03.08a, 08.01
- **Status:** BLOCKED at network / IP level (per 2026-04-28 analysis: yt-dlp + youtube-transcript-api + Invidious — все возвращают bot challenge / IP-block / empty caption body)
- **Volume blocked:** 452 ШСМ videos + 127 Tseren videos = **579 videos** total; 13/15 top videos have Russian auto-captions per metadata but extraction blocked.
- **Resolution path:**
  - Option A: Ruslan manually downloads transcripts via browser for top 20-30 highest-priority videos (Левенчуковский FPF talks, Tseren IWE talks, intellect-stack lectures); puts in `raw/external/levenchuk-corpus-2026-05-17/03-youtube/transcripts/`
  - Option B: Use audio download (smaller, may bypass transcript-API block) + whisper.cpp local transcription (free)
  - Option C: Accept metadata-only fidelity for Phase A; revisit Phase B
- **Phase A decision:** Option C. Metadata + titles + descriptions sufficient для surface'инга что в этих видео обсуждается. Empirical transcript content deferred.

### B7. @ailev_blog Telegram handle existence
- **Inventory ref:** 06.01
- **Status:** Not confirmed in any source seen. R-A lists `@system_school` (ШСМ channel) + бот, but no personal `@ailev_blog`.
- **Possible:** Levenchuk не имеет personal TG channel — только LJ blog + ШСМ channel for announcements
- **Resolution:** mark as «handle not found»; if Ruslan knows different — surface

## Tier 4 — Optional gaps (low priority)

### B8. arXiv PDFs (07.01, 07.02)
- **Block:** none; curl works
- **Why deferred in Phase A:** content already extensively absorbed in R-A §1.2 + §4.2 + Bibliography
- **If Phase B needs:** simple curl + add to corpus

### B9. Habr / vc.ru deep scrapes (09.01-02)
- **Block:** none; WebFetch works
- **Why deferred:** these are third-party interpretations (часто distorted); Левенчуковский primary preferred for distillation
- **If Phase B needs:** simple WebFetch batch

### B10. Tseren Medium blog (08.04)
- **Block:** none; WebFetch works
- **Why deferred:** English content of Tseren; primary RU corpus already captured (TG + YT metadata + community profile)

---

## Cost cap snapshot (§0.0 of prompt)

- **Daily €10 baseline:** NOT exceeded — all collection через free WebFetch / curl / built-in tools
- **€50 halt:** N/A
- **External services used:** WebFetch (Claude Code built-in), curl (free), GitHub API (free, no auth needed for public repos)
- **NOT used:** ANTHROPIC_API_KEY direct calls, GROQ paid API, web scraper services, paywall bypass

---

## Phase A → Phase B handoff items

**For Ruslan when reading SUMMARY:**
1. Decide on B4 («Инженерия интеллекта» interpretation)
2. Activate B1 aisystant subscription handoff method (Option A/B/C)
3. Run 5-10 IWE sessions (B2) для empirical comparison
4. Apply for R0 cohort (B3) — note next cohort date
5. Decide on B6 YouTube transcripts approach
6. **THEN** Phase B (C4 benchmark + integration plan + Левенчук response draft) можно запустить with full corpus

---

*Blockers complete — surface'нуто Ruslan видимо.*
