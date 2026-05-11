---
title: Gamification Deep Wiki Mining — Source Quality & Manual Downloads Addendum (Шаг B.1)
date: 2026-05-11
type: mining-plan-addendum
status: ACK'D 2026-05-11 — §6 Q1-Q7 resolved + §1/§3 ack'd by Ruslan; awaits CORE 3 manual downloads in raw/ → Шаг C trigger
ack_log:
  - 2026-05-11 Ruslan ack §6 Q1-Q7 (Q1 MD preferred / Q2 FULL 9 target CORE 3 minimum / Q3 skip paid GDC / Q4 skip Audible / Q5 thresholds default / Q6 Tier 2 wikis mechanics-only / Q7 Twitter Tier 3 named-author OR REJECT)
  - 2026-05-11 Ruslan ack §1 tier policy unchanged
  - 2026-05-11 Ruslan ack §3 self-audit hooks unchanged (all thresholds mandatory)
authored_by: claude-opus-4-7 (acting_as gamification-curator-role) + Ruslan (vision + spec)
prose_authored_by: hybrid-with-ack-trail
parent_plan_doc: reports/gamification-deep-wiki-mining-plan-2026-05-11.md
parent_notion: 35d2496333bf814b978ad6159600447f (Gamification Deep Wiki — Mining Plan, Шаг A)
strategic_anchor: decisions/STRATEGIC-INSIGHT-JETIX-AS-GAMIFIED-PLATFORM-2026-05-11.md
F: F2
G: gamification-mining
R: refuted_if_tier_classification_unused_in_Step_C_OR_no_manual_downloads_before_trigger
blast_radius: F2
constitutional_posture: derived-from-parent §5/§11; append-only к reports/; no Foundation writes; no principles/ touches; no .claude/config/ touches
hooks_into:
  - parent §3 Methodology (via Addendum §1 Source Quality Policy)
  - parent §4.3 Checkpoint cadence (via Addendum §3 Self-Audit Hooks)
  - parent §5 Quality Filters (via Addendum §1 + §3 — extends §5.1 REJECT + §5.3 cite-or-skip)
  - parent §11 Execution Sequence Step 0 (via Addendum §5 Pre-Execution Checklist)
gates_step_c: true
related_canonical:
  - reports/gamification-deep-wiki-mining-plan-2026-05-11.md
  - swarm/wiki/foundations/part-3-knowledge-base-methodology-library/architecture.md
  - swarm/wiki/foundations/part-6a-provenance-officer/architecture.md
---

# 🎯 Gamification Deep Wiki Mining — Source Quality & Manual Downloads Addendum (Шаг B.1)

> **Шаг A** = Notion subpage (Ruslan high-level structure 2026-05-11).
> **Шаг B** = `reports/gamification-deep-wiki-mining-plan-2026-05-11.md` (1003 строки plan-doc).
> **Шаг B.1 (этот документ)** = source-quality + manual-downloads + self-audit layer для Шаг B.
> **Шаг C** = autonomous brigadier execution per Шаг B + B.1 — **БЛОКИРОВАН до Ruslan ack §6 + manual downloads checklist**.

---

## §0 TL;DR (10 строк)

```
 1. Шаг B.1 закрывает 3 gap-а в parent plan-doc: source-quality 3-tier policy / manual downloads checklist / per-source+per-entry self-audit hooks.
 2. 3-tier source policy: Tier 1 (R-high, anchor-eligible) / Tier 2 (R-medium, supportive) / Tier 3 (R-low DRAFT only) + REJECT list (content-farm / streamer / Wikipedia-cite / AI-gen / single-source).
 3. Manual downloads CORE 5: Castronova Synthetic Worlds / Hooked / Theory of Fun / Flow / Virtual Economies.
 4. Manual downloads EXTENDED 4: Technofeudalism / Influence / Evolution of Cooperation / Strategy of Conflict.
 5. Free papers/talks: Nash 1950 / Deci-Ryan 2000 / Castronova GNP papers / GDC Vault free talks.
 6. Storage paths trio: raw/books-md/gamification/ (existing root) + raw/papers-pdf/gamification/ (NEW dir) + raw/talks-transcripts/gamification/ (NEW dir).
 7. Self-audit per-source frontmatter: source_classifier { tier / type / verifiable_author / year / cross_validated / primary_source_url_or_path }.
 8. Self-audit per-entry frontmatter: audit { confidence / primary_source_cited / hallucination_risk / fallback_to_bm25 } + post-domain summary template.
 9. Real-time halt thresholds: >20% low-confidence per domain → PAUSE; >10% high hallucination → PAUSE; cite-failure rate >15% → PAUSE; primary_source_cited:false → REJECT entry.
10. STATUS ACK'D 2026-05-11: §6 Q1-Q7 resolved (FULL 9 target / MD preferred / halt thresholds default) + §1+§3 ack'd. Шаг C trigger waits ONLY на CORE 3 manual downloads physical placement в raw/books-md/gamification/ или raw/papers-pdf/gamification/.
```

---

## §1 Source Quality Policy — 3-Tier + REJECT

> **Why this section exists.** Parent §5.1 (Garbage filter REJECT) + §5.3 (Cite-or-skip) описывают what to throw out, но не дают positive classification источников. Без 3-tier policy mining run-time decisions становятся ad-hoc → high variance в quality между domains.

### §1.1 Tier 1 — R-high — anchor-eligible

**Что попадает:**
- Primary academic peer-reviewed publications (Castronova, Lehdonvirta, Hamari, Ryan-Deci, Hamari-Koivisto-Sarsa)
- Authoritative books with citations (Castronova *Synthetic Worlds* 2005, Schelling *Strategy of Conflict* 1960, Axelrod *Evolution of Cooperation* 1984, Csikszentmihalyi *Flow* 1990)
- Dev firsthand postmortems (GDC Vault talks by lead designers, official dev blogs by named authors, Schreiber/Sirlin/Cook talks)
- Foundational original papers (Nash 1950, Smith ESS 1973, Deci-Ryan SDT 2000)

**Rationale:** primary academic peer-review · dev firsthand experience · authoritative books with traceable citations · verifiable named-human authorship · methodology stated explicitly.

**When-to-use:**
- Concept anchor definitions (`concepts/*.md` canonical attribute lists)
- Claim primary citations (`claims/*.md` `sources:` first entry)
- Entity canonical attributes (`entities/*.md` design-decision references)
- Cross-validation source для Tier 2/3 entries

### §1.2 Tier 2 — R-medium — supportive, not anchor

**Что попадает:**
- Industry experts с published track record (Sebastian Deterding writings, Yu-kai Chou *Actionable Gamification* + Octalysis framework, Nicole Lazzaro 4 Keys to Fun talks)
- Official game wikis (Old School RuneScape Wiki, EVE Online Uniwiki, WoW Wiki) — ОНЛИ для game-mechanics anchor description, NOT для theory claims
- Textbooks (Salen-Zimmerman *Rules of Play* 2003, Schell *The Art of Game Design* 2008)
- Curated industry references (Gamasutra/GameDeveloper.com articles by named industry veterans with date >2015)

**Rationale:** deep practitioner experience OR curated reference, но not peer-reviewed; verifiable human identity; bounded epistemic scope.

**When-to-use:**
- Secondary citation в claims (`sources:` second+ entry)
- Mechanics description в entities (especially game-specific economies, gameplay loops)
- Cross-check against Tier 1 (`cross_validated: true` enabler)
- Practitioner pattern naming (Octalysis 8 core drives, Bartle taxonomy)

### §1.3 Tier 3 — R-low — DRAFT only

**Что попадает:**
- Industry articles (Gamasutra/GameDeveloper.com posts with named author + dates, но не industry-veteran tier)
- Podcast transcripts (Lex Fridman / Acquired / EconTalk interviews с primary authors как guests)
- Curated postmortem aggregators (GDC proceedings summaries, indie postmortem collections)
- Substack newsletters by named experts (recent, <3 years)

**Rationale:** useful pointer/hypothesis material but not verifiable as primary; risk of paraphrase drift.

**When-to-use:**
- `state: draft` + `confidence: low` mandatory
- Must cross-validate with Tier 1 or Tier 2 source BEFORE promote to `pipeline: ingested`
- Acceptable as `ideas/*.md` (hypothesis material) — NEVER as primary citation in `claims/*.md`
- Flagged via `audit.fallback_to_bm25: true` если discovered via web-search

### §1.4 REJECT list (hard filter — extends parent §5.1)

❌ **Content-farms** — TopTal blogs, listicles ("Top 10 Gamification Tips" без cited methodology), MEDIUM aggregator articles без named author research basis
❌ **Marketing collateral** — vendor whitepapers без methodology section; SaaS marketing pages; pitch decks
❌ **AI-generated text** — Medium AI-flagged posts; ChatGPT-essay aggregators; "GPT-generated summary" sites
❌ **Streamer commentary** — Twitch VOD clips; YouTube reaction videos; gameplay-only streams без analytical commentary by published designer
❌ **Reddit-primary** — Reddit thread AS primary source for theory/mechanics claims (OK as observation pointer with `audit.primary_source_cited: false`; NEVER as Tier 1)
❌ **Wikipedia-cited claims** — Wikipedia OK as orientation/disambiguation only; **NEVER cite from it**; trace to Wikipedia's primary source instead and cite that
❌ **Outdated material** — >15 years для industry data; >25 years для theory unless foundational (Nash/Schelling/Smith/Csikszentmihalyi/Deci-Ryan are foundational exceptions)
❌ **Single-source unverified claims** — any claim resting on exactly one source without `cross_validated: true` flag, при `tier: T2` or `T3`

---

## §2 Manual Downloads — Ruslan Checklist

> **Why this section exists.** Domain experts in Шаг C полагаются на full-text source access для accurate citation. Без manual-downloads — fallback на web-search → BM25 snippets → высокий hallucination risk + low source verifiability. CORE 3 минимум gate Шаг C trigger.

### §2.1 CORE 5 (priority — Шаг C requires minimum 3 of these)

| # | Author — Title (Year) | Domain | Why critical |
|---|------------------------|--------|--------------|
| 1 | Castronova — *Synthetic Worlds* (2005) | EXPERTS, GAMES | Virtual economy foundational text; primary anchor для §2.2 in parent |
| 2 | Eyal — *Hooked* (2014) | PSYCHOLOGY | Trigger / Action / Variable Reward / Investment loop framework |
| 3 | Koster — *Theory of Fun for Game Design* (2004) | GAMES, PSYCHOLOGY | Pattern-recognition theory of fun; cognitive frame for mechanic design |
| 4 | Csikszentmihalyi — *Flow* (1990) | PSYCHOLOGY | Challenge/skill balance; foundational psychology anchor |
| 5 | Lehdonvirta-Castronova — *Virtual Economies: Design and Analysis* (2014) | EXPERTS | Design treatise on synthetic economies; extends Synthetic Worlds |

**Gate:** Шаг C cannot trigger без minimum **CORE 3** (#1 + #2 + #3) физически downloaded. CORE 5 recommended для full coverage.

### §2.2 EXTENDED 4 (load if available; not gating)

| # | Author — Title (Year) | Domain | Why useful |
|---|------------------------|--------|------------|
| 6 | Varoufakis — *Technofeudalism* (2023) | EXPERTS | Platform attention extraction critique; modern frame |
| 7 | Cialdini — *Influence* (1984/2021) | PSYCHOLOGY | 7 persuasion principles; cross-cuts with Hooked |
| 8 | Axelrod — *Evolution of Cooperation* (1984) | THEORY | Iterated prisoner dilemma dynamics; tit-for-tat |
| 9 | Schelling — *Strategy of Conflict* (1960) | THEORY | Coordination + focal points; foundational game theory |

### §2.3 Papers/Talks (free — Ruslan or Шаг C web-fetch later, NOT manual gate)

- Nash 1950 — equilibrium paper (PDF — public domain status varies; mirror available via arxiv mirrors or academic archives)
- Deci-Ryan 2000 — SDT review article (PsyINFO available; multiple PDF mirrors)
- Castronova — EverQuest GNP papers (CESifo Working Paper, free PDFs available)
- GDC Vault free tier talks (Schreiber game balance, Cook MDA framework, Sirlin yomi)

### §2.4 Storage paths (Ruslan creates dirs at download time)

```
raw/books-md/gamification/       # for Markdown-converted books (Calibre ebook-convert output)
                                  # NOTE: raw/books-md/ root EXISTS (21 subdirs); gamification/ to be added
raw/papers-pdf/gamification/     # for PDFs (NEW ROOT DIR — Ruslan mkdir at first download)
raw/talks-transcripts/gamification/  # for GDC/podcast transcripts (NEW ROOT DIR)
```

**Создание dirs:**
```bash
mkdir -p raw/books-md/gamification raw/papers-pdf/gamification raw/talks-transcripts/gamification
```
(Run by Ruslan one-time; Шаг C не создаёт.)

### §2.5 Conversion guidance (informational, not mandatory)

- **Books в Markdown (preferred for Tier 1):** Calibre `ebook-convert input.epub output.md` → place в `raw/books-md/gamification/`
- **Books в PDF (acceptable):** drop PDF в `raw/papers-pdf/gamification/`
- **Audible-only:** skip для Шаг C (see §6.Q4); транскрипция отложена в Шаг C+1
- **GDC talks:** скачивай transcript (если доступен) или audio → Whisper транскрипция → `raw/talks-transcripts/gamification/<talk-slug>.md`

---

## §3 Self-Audit Hooks

> **Why this section exists.** Parent §4.3 (Checkpoint cadence) + §7.3 (Abort conditions) описывают macro-level halt triggers; этот section добавляет per-source + per-entry frontmatter audit fields + real-time threshold halts.

### §3.1 Per-source frontmatter (mandatory in every ingested source file)

```yaml
source_classifier:
  tier: T1 | T2 | T3                      # mandatory; matches §1 policy
  type: book | paper | postmortem | wiki | article | podcast | talk
  verifiable_author: true | false         # named human, traceable identity
  year: YYYY                              # publication
  cross_validated: true | false           # at least 1 OTHER Tier 1/2 source corroborates the key claim
  primary_source_url_or_path: <relative-path-or-URL>
```

**Enforcement:** any source file без `source_classifier:` block → lint failure → REJECT для citation pool.

### §3.2 Per-entry frontmatter (mandatory in every wiki entry created by Шаг C)

```yaml
audit:
  confidence: low | medium | high          # self-assessed by domain expert
  primary_source_cited: true | false       # at least 1 Tier 1/2 source in `sources:` field
  hallucination_risk: low | medium | high  # self-assessed; reflects degree of inference vs direct citation
  fallback_to_bm25: true | false           # true if entry relied on web-search snippet vs full-text source
```

**Enforcement:** any entry где `primary_source_cited: false` AND `pipeline: ingested` → **REJECT** (kept as draft until source attached).

### §3.3 Real-time halt conditions (extends parent §7.3 abort list)

Per-domain checkpoint thresholds:

| Trigger | Threshold | Action |
|---------|-----------|--------|
| `confidence: low` count | > 20% of domain entries | **PAUSE** — Ruslan ack to continue OR roll back domain |
| `hallucination_risk: high` count | > 10% of domain entries | **PAUSE** — Ruslan review domain output |
| `primary_source_cited: false` AND `pipeline: ingested` | per-entry | **REJECT** — auto-demote to `state: draft, pipeline: raw` |
| Cite-failure rate (extends parent §5.3) | > 15% per domain | **PAUSE** — review citation pool quality |
| `fallback_to_bm25: true` count | > 40% per domain | **WARN** (not halt) — flag in post-domain audit |

**Grade timeouts (inherited from CLAUDE.md §I.2):** F8 ≤1s, F4 ≤5s, F2 ≤60s. This Addendum is F2 (mining ops) — halts apply на ≤60s window before brigadier escalates.

### §3.4 Post-domain audit summary template

Emitted at each checkpoint (parent §4.3 cadence) into brigadier scratchpad:

```yaml
domain: GAMES | EXPERTS | THEORY | PSYCHOLOGY
entries_created: N
tier_distribution: { T1: a, T2: b, T3: c }
confidence_distribution: { low: x, medium: y, high: z }
hallucination_risk_distribution: { low: x, medium: y, high: z }
fallback_to_bm25_count: N
primary_source_cited_false_count: N
cite_failure_rate: N%
halt_triggered: true | false
halt_reason: <if halt_triggered=true; one of: low_confidence_threshold | hallucination_risk_threshold | cite_failure_rate>
recommended_next_action: continue | pause_for_ruslan_review | rollback_domain
```

**Audit transparency:** all 4 post-domain summaries appended to final hand-back report (parent §12).

---

## §4 Integration — Hooks into Parent Plan-Doc

Specifies WHERE Addendum hooks into parent. Parent gets **4 one-line cross-references** (surgical, append-only) — no content rewrite.

| Parent section (line ref) | Hook target в Addendum | Cross-reference inserted в parent |
|----------------------------|------------------------|-----------------------------------|
| §3 Methodology preamble (after L238) | §1 Source Quality Policy | One-line blockquote ref to Addendum §1 |
| §4.3 Checkpoint cadence (after L367-369) | §3 Self-Audit Hooks | One-line blockquote ref to Addendum §3 |
| §5 Quality Filters preamble (after L386) | §1 + §3 | One-line blockquote ref extending §5.1/§5.3 |
| §11 Execution Sequence Step 0 (before L881 Step 1) | §5 Pre-Execution Checklist | One-line blockquote gate-condition for Step 0 |

All 4 cross-references формата `> **Addendum reference / gate:** ... — see [Source Quality Addendum §N](gamification-source-quality-addendum-2026-05-11.md#N-anchor).`

**Append-only guarantee:** none of 4 edits modifies existing parent content. Each adds one line под header.

---

## §5 Pre-Execution Checklist (gates Шаг C trigger)

Status snapshot 2026-05-11 (post Ruslan §6 ack):

- [ ] Ruslan скачал минимум **CORE 3** (Castronova *Synthetic Worlds* + Eyal *Hooked* + Koster *Theory of Fun*) — **IN PROGRESS** (Ruslan downloading parallel; target FULL 9 per Q2 ack)
- [ ] `mkdir -p raw/books-md/gamification raw/papers-pdf/gamification raw/talks-transcripts/gamification` — **PENDING** (Ruslan within minutes)
- [ ] Books placed в `raw/books-md/gamification/` (Calibre MD conversion preferred per Q1 ack) **OR** PDF в `raw/papers-pdf/gamification/` — **PENDING** download
- [ ] CC verify через `Read` tool на 1-2 sample files — paths resolve, content parseable — **PENDING** file placement
- [✓] Pipeline registry знает paths — convention-based, no config required (per §5 note; confirmed)
- [✓] Ruslan answered §6 Open Questions — **Q1-Q7 all resolved 2026-05-11** (see §6 inline ACK'D)
- [✓] §1 (Tier policy) + §3 (Audit hooks) reviewed + ack'd by Ruslan — **2026-05-11** (unchanged, all thresholds mandatory as written)

**Шаг C trigger condition:** all 7 boxes checked. Brigadier dispatch НЕ initiated иначе.

**Remaining blockers (4):** download CORE 3 minimum → mkdir dirs → place files → CC sample-read verify. Ruslan signals separately when git push с книгами done.

---

## §6 Open Questions — RESOLVED 2026-05-11 (Ruslan ack)

**Q1 (gating).** Книги — конвертировать в Markdown (Calibre `ebook-convert`) или достаточно PDF в `raw/papers-pdf/gamification/`?
**✓ ACK'D 2026-05-11:** MD preferred для всех books — convert via Calibre `ebook-convert` → `raw/books-md/gamification/`. PDF-only книги → `raw/papers-pdf/gamification/`, далее separate conversion to MD для consistency.

**Q2 (gating).** Приоритет manual downloads — CORE 3 / CORE 5 / FULL 9?
**✓ ACK'D 2026-05-11:** Target = **FULL 9** (CORE 5 + EXTENDED 4). Минимум для Шаг C trigger = **CORE 3** (Castronova *Synthetic Worlds* + Eyal *Hooked* + Koster *Theory of Fun*). Остальные подгрузим в ближайшие часы — не блокируют trigger, но maximize до FULL 9 if feasible.

**Q3.** GDC Vault paid talks подключаем или skip?
**✓ ACK'D 2026-05-11:** Skip paid GDC — free public talks достаточно для Шаг C.

**Q4.** Audible workflow — нужна Whisper transcription?
**✓ ACK'D 2026-05-11:** Skip Audible-only для Шаг C — только manually-downloadable books (MD/PDF). Audible transcription отложен в Шаг C+1.

**Q5 (gating).** Halt thresholds (>20% low-confidence / >10% high hallucination / >15% cite-failure)?
**✓ ACK'D 2026-05-11:** Accept as is. Tunable после первого checkpoint если data покажет drift.

**Q6.** Tier 2 game wikis (OSRS / EVE Uniwiki / WoW Wiki) — anchor только для mechanics description, NOT для theory claims?
**✓ ACK'D 2026-05-11:** Confirmed. Game wikis Tier 2 mechanics-only, NOT для theory.

**Q7.** REJECT list — Twitter/X threads policy?
**✓ ACK'D 2026-05-11:** Twitter/X threads → **Tier 3** с mandatory `verifiable_author: true` (named human handle) + thread-archive-URL (e.g. Nitter snapshot / Archive.org) в `primary_source_url_or_path`. Иначе → **REJECT**.

---

## §7 Commit + Integration

**Commit message:**
```
[gamification] Source Quality + Manual Downloads Addendum Шаг B.1
```

**Staged files (one commit, both):**
1. NEW: `reports/gamification-source-quality-addendum-2026-05-11.md` (этот файл)
2. MODIFIED (4 surgical one-line inserts): `reports/gamification-deep-wiki-mining-plan-2026-05-11.md` — at §3 / §4.3 / §5 / §11 Step 0 preambles

**API-key scan pre-commit:** `grep -rEn 'ANTHROPIC_API_KEY|GROQ_API_KEY|OPENAI_API_KEY' reports/gamification-source-quality-addendum-2026-05-11.md reports/gamification-deep-wiki-mining-plan-2026-05-11.md` → must return 0 hits.

**Push:** `git push origin main` after commit success.

**Gate (post-ack 2026-05-11):** Шаг C trigger **NOT** initiated. Remaining blocker:
1. ~~Ruslan ack on §6~~ **DONE 2026-05-11** (Q1-Q7 all resolved; §6 inline)
2. Manual download checklist §5 minimum **CORE 3** physical placement в raw/ — IN PROGRESS
3. ~~Optional tweaks to §1/§3~~ **DONE** — accepted as written (no tweaks requested)

Brigadier dispatch WAITS на Ruslan explicit signal `«Шаг C: starts brigadier dispatch — gamification deep wiki mining»` AFTER он confirms CORE 3 physical presence + git push с книгами done.

---

## Hand-back

Этот Addendum — последний preparatory artifact перед Шаг C trigger. После Ruslan ack §6 + manual downloads checklist completion (§5) → trigger phrase: `«Шаг C: starts brigadier dispatch — gamification deep wiki mining»` → brigadier инициирует execution per parent §11 sequence, enriched этим Addendum's tier policy + audit hooks.

Без ack — brigadier dispatch **NOT** initiated. F2 blast-radius preserved; constitutional posture intact.
