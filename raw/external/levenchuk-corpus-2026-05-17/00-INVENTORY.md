---
title: Levenchuk Corpus Inventory — Phase A
date: 2026-05-17
type: corpus-inventory
trigger: inbox/levenchuk-tg-2026-05-17.md
parent_prompt: prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md
status: exhaustive-baseline
F: F6
G: levenchuk-corpus-map
R: refuted_if_significant_channel_missed
prose_authored_by: claude (scribe-mode, surface-only)
purpose: |
  Inventory всех известных Левенчуковских источников до collection. Без selection
  «что важно / что нет». Платное + бесплатное + закрытое + открытое. Фиксирует
  ГДЕ каждый источник и КАК к нему достучаться. Базис для §2 Collection,
  §3 Distillation, §4 Mermaid, §5 Self-audit, §6 Summary.
language: russian + english (sources)
---

# Levenchuk Corpus Inventory — 2026-05-17

> **Scope.** Полный inventory материалов Левенчука + IWE Цэрэна + ШСМ/МИМ.
> 9 категорий источников. Per-source: ID / URL / тип / формат / volume estimate /
> access method / status. Surface-инг — без выбора «важно/неважно».

---

## §1 Source list (exhaustive, numbered)

### Category 01 — GitHub canonical (FPF + ailev other repos)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 01.01 | `ailev/FPF` repo — FPF-Spec.md | https://github.com/ailev/FPF/blob/main/FPF-Spec.md | open | markdown (one monolith) | 62,202 lines / 5.7 MB / ~ "300+ patterns by April 2026" | git clone / curl raw | ✅ EXISTING-IN-REPO at `raw/external/ailev-FPF/FPF-Spec.md` (vendored 2026-04-20); freshness vs upstream NOT verified 2026-05-17 |
| 01.02 | `ailev/FPF` repo — Readme.md | https://github.com/ailev/FPF/blob/main/Readme.md | open | markdown | 384 lines | git clone | ✅ EXISTING-IN-REPO at `raw/external/ailev-FPF/Readme.md` |
| 01.03 | `ailev/*` other repos | https://github.com/ailev?tab=repositories | open | mixed | unknown (likely ≤10 repos based on author profile) | gh api / web inspect | 🟡 TO-VERIFY — listing not pulled 2026-05-17 |
| 01.04 | FPF git log (commit history) | https://github.com/ailev/FPF/commits/main | open | git metadata | months of activity (active dev 2024-2026) | git log --oneline | 🟡 TO-COLLECT — useful for tracking evolution of patterns |

### Category 02 — LiveJournal blog (ailev.livejournal.com)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 02.01 | Main blog `ailev.livejournal.com` | https://ailev.livejournal.com | open | LiveJournal HTML | ~5000+ posts (active since early 2000s; ~25 yr archive) | web scrape (curl + html2md) or RSS | 🟡 TO-COLLECT (large; bulk download not started 2026-05-17) |
| 02.02 | Tag: `intellect-stack` | https://ailev.livejournal.com/tag/интеллект-стек | open | filtered post list | ≤200 posts est. | tag-filtered scrape | 🟡 TO-COLLECT |
| 02.03 | Tag: `мышление` | https://ailev.livejournal.com/tag/мышление | open | filtered | unknown | tag-filtered scrape | 🟡 TO-COLLECT |
| 02.04 | Tag: `методология` | https://ailev.livejournal.com/tag/методология | open | filtered | unknown | tag-filtered scrape | 🟡 TO-COLLECT |
| 02.05 | Tag: `FPF` | https://ailev.livejournal.com/tag/FPF | open | filtered | unknown | tag-filtered scrape | 🟡 TO-COLLECT |
| 02.06 | Tag: `IWE` (if exists) | https://ailev.livejournal.com/tag/IWE | open | filtered | unknown | tag-filtered scrape | 🟡 TO-VERIFY (tag may not exist) |
| 02.07 | Tag: `U.Episteme` | https://ailev.livejournal.com/tag/U.Episteme | open | filtered | unknown | tag-filtered scrape | 🟡 TO-VERIFY |
| 02.08 | Tag: `OntoLern` | https://ailev.livejournal.com/tag/OntoLern | open | filtered | unknown | tag-filtered scrape | 🟡 TO-VERIFY |
| 02.09 | Tag: `ПравТех` | https://ailev.livejournal.com/tag/правтех | open | filtered | unknown | tag-filtered scrape | 🟡 TO-VERIFY |
| 02.10 | Key posts identified (2012-2024) — Essence / Alpha topic | LJ ids 1051048, 1067999, 1082662, 1188876, 1318973, 1331004, 1575106, 1718836, 1725757 | open | individual posts (~10) | ~30K words combined | WebFetch | 🟡 TO-COLLECT (subset captured in R-D extraction) |
| 02.11 | Key posts 2025-2026 — FPF дев / residencies / 10th conf | LJ ids 1777145 (Autumn 2025 residency), 1798285 (10th MIM conf 2026), 1788706 (FPF dev plans 2026-02) | open | posts | ~10K words combined | WebFetch | 🟡 TO-COLLECT |

### Category 03 — ШСМ / МИМ public materials (system-school.ru + YouTube)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 03.01 | МИМ main site | https://system-school.ru | open | HTML | ~50-100 public pages | WebFetch | 🟡 TO-COLLECT (homepage + team + curriculum + residencies pages) |
| 03.02 | МИМ team page | https://system-school.ru/team | open | HTML | one page | WebFetch | 🟡 TO-COLLECT |
| 03.03 | МИМ team / Левенчук bio | https://system-school.ru/team/levenchuk (or similar) | open | HTML | one page | WebFetch | 🟡 TO-VERIFY URL |
| 03.04 | МИМ team / Цэрэнов bio | https://system-school.ru/team/tserenov | open | HTML | one page | WebFetch | ✅ PARTIAL — bio cited in profiles/l1-first-clan/tseren-tserenov.md §1 |
| 03.05 | МИМ intellect-stack public page | https://system-school.ru/stack | open | HTML | one page | WebFetch | 🟡 TO-COLLECT — lists transdisciplines |
| 03.06 | МИМ events page | https://events.system-school.ru | open | HTML | event listing | WebFetch | 🟡 TO-COLLECT |
| 03.07 | МИМ Telegram channel | https://t.me/system_school | open | TG | active channel; posts go back years | tdlib/export or web view | 🟡 TO-COLLECT |
| 03.08 | YouTube `@system_school` channel | https://www.youtube.com/@system_school | open | YT videos | **452 videos** [per analysis 2026-04-28] | yt-dlp (blocked on server IP — see 03.08a) | ✅ PARTIAL EXISTING-IN-REPO — metadata + analysis at `raw/research/2026-04-28-tseren-yt-export/system_school/` |
| 03.08a | YouTube transcripts blocked | — | open-but-blocked | — | — | yt-dlp + youtube-transcript-api + Invidious — все возвращают bot-challenge / empty / IP-blocked per 2026-04-28 analysis | 🔴 BLOCKED at infrastructure level; ADD TO blockers.md |
| 03.09 | YouTube ШСМ channel (alternative URL) | https://www.youtube.com/c/Школасистемногоменеджмента | open | YT videos | same as 03.08 likely | same | 🟡 likely DUPLICATE of 03.08 |
| 03.10 | Community forum systemsworld.club | https://systemsworld.club | open | Discourse forum | thousands of posts | web scrape | 🟡 TO-COLLECT (selective — search for "FPF", "IWE", "intellect-stack") |
| 03.11 | MIM annual conference 10th edition (April 2026) | https://events.system-school.ru/conf-2026 (est.) | open | event page + video archive | ~20 talks | WebFetch + YT | 🟡 TO-COLLECT |
| 03.12 | Past conf recordings 9th (April 2025) | https://www.youtube.com/watch?v=4s4d2MxdSdU + companions | open | YT video | ~2 hours each | yt-dlp blocked → use metadata only | 🟡 PARTIAL — metadata in 03.08 dataset |
| 03.13 | МИМ "Что такое FPF" seminar excerpt (Oct 2025) | https://www.youtube.com/watch?v=YiSR9v5PstU | open | YT | 9:20 | yt-dlp blocked | 🟡 METADATA-ONLY |

### Category 04 — Aisystant (paid courses + AI guide IWE)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 04.01 | Aisystant platform | https://aisystant.system-school.ru | paid | LMS | registration free; homework paid; full guides ~tens of MB | Ruslan subscription per §0.0 ack | 🟢 RUSLAN-ACK 2026-05-17 — берём всё что можно с подписки |
| 04.02 | Курс «Системное мышление» (R1 residency content) | aisystant LMS | paid | online guide + exercises | one full book (Sys Thinking 2024 vol 1+2) digitized | subscription | 🟢 RUSLAN-ACK |
| 04.03 | Курс «Методология» | aisystant LMS | paid | online guide | Методология 2025 book ~872 pp digitized | subscription | 🟢 RUSLAN-ACK |
| 04.04 | Курс «Системная инженерия» | aisystant LMS | paid | online guide | ~one book | subscription | 🟢 RUSLAN-ACK |
| 04.05 | Курс «Системный менеджмент» | aisystant LMS | paid | online guide | ~one book | subscription | 🟢 RUSLAN-ACK |
| 04.06 | Курс «Инженерия личности» | aisystant LMS | paid | online guide | ~one book | subscription | 🟢 RUSLAN-ACK |
| 04.07 | Курс «Интеллект-стек» | aisystant LMS | paid | online guide | ~one book | subscription | 🟢 RUSLAN-ACK |
| 04.08 | Курс «Рациональная работа / Собранность» (R0) | aisystant LMS | paid | online guide | one course (~10 weeks) | subscription | 🟢 RUSLAN-ACK |
| 04.09 | **IWE** — Intelligent Workflow Engine | aisystant LMS (embedded AI guide) | paid | AI chat interface | session-based; product of ШСМ | subscription | 🟢 RUSLAN-ACK — Левенчук's TG message C5: «IWE опирается на тот же FPF — и понятно, за счёт чего его IWE умнее конкурентов» — критический для Phase A |
| 04.10 | **Резидентура R0 / R1 / R2 рабочего развития** | aisystant + cohort | paid | weekly mentor + guide + AI | 10-19 wk per residency | apply per §0.0 ack (Ruslan applying for nearest cohort) | 🟢 RUSLAN-ACK — Левенчук's TG C7 invite |
| 04.11 | Bilingual sample courses (English Sys Thinking 2020 trans) | aisystant LMS | paid | online | ~one book translated by Ivan Metelkin | subscription | 🟡 TO-VERIFY availability post-subscription |

### Category 05 — Books (Ridero / Litres / Ozon / Yandex Books / Amazon)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 05.01 | Системное мышление 2024 том 1 | https://ridero.ru/books/sistemnoe_myshlenie_2024_tom_1/ | paid | book (Ridero) | 412 pp, ISBN 978-5-0064-2853-9 | purchase Ridero / Ozon / aisystant digitized | 🟢 RUSLAN-ACK — берём всё что есть |
| 05.02 | Системное мышление 2024 том 2 | https://ridero.ru/books/sistemnoe_myshlenie_2024_tom_2/ | paid | book | 488 pp, ISBN 978-5-0064-2855-3 | same | 🟢 RUSLAN-ACK |
| 05.03 | Методология 2025 | https://books.yandex.ru/books/ftXba12F + Ridero | paid | book | ~872 pp | purchase + aisystant | 🟢 RUSLAN-ACK |
| 05.04 | Системная инженерия 2022 | Ridero | paid | book | ~unknown pp | purchase + aisystant | 🟢 RUSLAN-ACK |
| 05.05 | Системный менеджмент 2023 | Ridero | paid | book | ~unknown pp | purchase + aisystant | 🟢 RUSLAN-ACK |
| 05.06 | Инженерия личности 2023 | Ridero | paid | book | ~unknown pp | purchase + aisystant | 🟢 RUSLAN-ACK |
| 05.07 | Интеллект-стек 2023 | https://ridero.ru/books/intellekt-stek_2023/ | paid | book | ISBN 978-5-0060-4990-1 | purchase + aisystant | 🟢 RUSLAN-ACK |
| 05.08 | Образование для образованных 2021 (superseded by 05.07) | Ridero | paid | book | historical | optional purchase | 🟡 LOW PRIORITY (superseded) |
| 05.09 | Визуальное мышление 2018 | Ridero | paid | book | short | purchase | 🟢 RUSLAN-ACK — береги companion к «мышление письмом» |
| 05.10 | Системный фитнес | Ridero (if extant) | paid | book | unknown | purchase | 🟡 TO-VERIFY existence (mentioned in prompt §1.2 but not seen in R-A bibliography) |
| 05.11 | «Инженерия интеллекта» (упомянуто prompt §1.2.5) | unknown publisher | paid | unknown | unknown | TO-VERIFY | 🔴 NOT FOUND in R-A bibliography 2026-04-18 — may be (a) future title, (b) misnamed «Инженерия личности», (c) IWE-related artifact. ADD TO blockers.md for Ruslan clarification |
| 05.12 | Практическое системное мышление 2023 (superseded by 05.01-02) | Ridero | paid | book | historical 8th rewrite | optional | 🟡 SUPERSEDED |
| 05.13 | Системное мышление 2020 (English translation by Ivan Metelkin) | aisystant + LitRes? | paid | book | ~one book | per 04.11 access | 🟡 EN VERSION VALUABLE for cross-checking RU terminology |
| 05.14 | Ridero author page (full catalog) | https://ridero.ru/author/levenchuk_anatolii_iv2h/ | open | listing | metadata only | WebFetch | 🟡 TO-COLLECT — verify all current titles |
| 05.15 | Ozon author catalog | https://www.ozon.ru/category/levenchuk/ | open | listing + reviews | metadata + reviews | WebFetch | 🟡 TO-COLLECT |
| 05.16 | LitRes author page | https://www.litres.ru/author/anatoliy-levenchuk/about/ | open | listing | metadata + samples | WebFetch | 🟡 TO-COLLECT |

### Category 06 — Telegram channels (ailev + system_school + ШСМ ecosystem)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 06.01 | @ailev_blog (if exists) | https://t.me/ailev_blog | open if exists | TG | unknown | tdlib export | 🔴 TO-VERIFY — handle not confirmed; per R-A there's `@system_school` not personal channel |
| 06.02 | @system_school (МИМ official) | https://t.me/system_school | open | TG | active; multi-year archive | tdlib export or web | 🟡 TO-COLLECT |
| 06.03 | @SystemsSchool_bot | https://t.me/SystemsSchool_bot | open | TG bot | registration bot only | n/a | n/a — bot only |
| 06.04 | @ssm_tg (referenced in YT) | https://t.me/ssm_tg | open | TG | unknown | tdlib | 🟡 TO-VERIFY existence |
| 06.05 | Цэрэн @systemsthinkinglife | https://t.me/systemsthinkinglife | open | TG | **618 posts 2021-03-16 → 2026-04-28** | full JSON export 5.8 MB | ✅ EXISTING-IN-REPO at `raw/research/2026-04-28-tseren-tg-export/` |
| 06.06 | Цэрэн @TserenTserenov (personal handle) | https://t.me/TserenTserenov | direct DM | n/a | n/a | Ruslan already messaged 2026-05-04 | n/a |

### Category 07 — Academic / formal publications (arXiv / INCOSE / OMG)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 07.01 | arXiv 2015 «Towards a Systems Engineering Essence» | https://arxiv.org/abs/1502.00121 | open | PDF (English) | one paper | curl PDF | 🟡 TO-COLLECT |
| 07.02 | arXiv 2023 «Toward an Ontology for Third Generation Systems Thinking» | https://arxiv.org/abs/2310.11524 | open | PDF (English) | one paper | curl PDF | 🟡 TO-COLLECT |
| 07.03 | INCOSE Russia chapter materials (2010-2013) | INCOSE site (archived?) | open if archived | unknown | minor | search | 🟡 LOW PRIORITY |
| 07.04 | OMG Essence specifications (referenced by Левенчук) | https://www.omg.org/spec/Essence/1.2 + 2.0 alpha | open | PDF | OMG specs | curl | 🟡 LOW PRIORITY (not Левенчук authored; but his framework reference) |
| 07.05 | TechInvestLab «Системноинженерное мышление 2015» PDF | https://techinvestlab.ru/files/systems_engineering_thinking/systems_engineering_thinking_2015.pdf | open | PDF | ~one textbook | curl | 🟡 TO-COLLECT |
| 07.06 | Emergent Mind index of arXiv 2310.11524 | https://www.emergentmind.com/papers/2310.11524 | open | analysis | meta only | WebFetch | 🟡 OPTIONAL |

### Category 08 — Цэрэн IWE materials (primary FPF-applied artefact per Левенчук C5)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 08.01 | YouTube `@tserentserenov77` (личный) | https://www.youtube.com/@tserentserenov77 | open | YT | **127 videos / 114.3 hours / 2024-01 → 2026-04** | yt-dlp blocked → metadata only | ✅ EXISTING-IN-REPO metadata + analysis at `raw/research/2026-04-28-tseren-yt-export/tserentserenov77/` |
| 08.02 | YouTube `@system_school` Tseren-mentioned videos | 03.08 dataset filtered | open | YT subset | 37 videos | metadata only | ✅ EXISTING-IN-REPO |
| 08.03 | Цэрэн Telegram @systemsthinkinglife corpus | https://t.me/systemsthinkinglife | open | TG | 618 posts | full export | ✅ EXISTING-IN-REPO at `raw/research/2026-04-28-tseren-tg-export/` |
| 08.04 | Medium @tserentserenov (English) | https://medium.com/@tserentserenov | open | blog | semi-active | WebFetch | 🟡 TO-COLLECT |
| 08.05 | Tenchat | mentioned but URL not confirmed | open | RU professional network | unknown | TO-VERIFY URL | 🟡 LOW PRIORITY |
| 08.06 | Instagram @tseren.tserenov | https://www.instagram.com/tseren.tserenov/ | open | photos | unknown | LOW priority for FPF/IWE study | 🟡 SKIP — non-technical |
| 08.07 | Facebook tseren.tserenov | https://www.facebook.com/tseren.tserenov | open | mixed | unknown | SKIP for FPF/IWE | 🟡 SKIP |
| 08.08 | LiveLib author profile | https://www.livelib.ru/author/1879306-tseren-tserenov | open | book metadata | minor | WebFetch | 🟡 LOW PRIORITY |
| 08.09 | «Мысли системно» book (co-authored, Bombora) | publisher Bombora — Eksmo group | paid | book | popular-science systems thinking | purchase | 🟡 LOW-MEDIUM PRIORITY (popular-science layer; FPF rigor lower) |
| 08.10 | **IWE itself** — interaction with the AI guide | aisystant platform | paid | AI chat | session-based | per 04.09 RUSLAN-ACK | 🟢 RUSLAN-ACK — Phase A target |
| 08.11 | systemsworld.club Tseren profile | https://systemsworld.club/t/czeren-czerenov-strateg-sistemnogo-myshleniya-i-sozdatel-uspeshnyh-sistem/22932 | open | community profile | one page | WebFetch | 🟡 TO-COLLECT |

### Category 09 — Third-party discussions (Habr / vc.ru / Reddit / HN / academic reviews)

| ID | Source | URL | Type | Format | Volume estimate | Access | Status |
|----|--------|-----|------|--------|-----------------|--------|--------|
| 09.01 | Habr articles tagged ailev | https://habr.com/ru/search/?q=Левенчук | open | tech articles | unknown count | WebFetch | 🟡 TO-COLLECT |
| 09.02 | vc.ru articles on ШСМ / Левенчук | https://vc.ru/search?query=ШСМ | open | business articles | unknown | WebFetch | 🟡 TO-COLLECT |
| 09.03 | Psybertron English review (Ian Glendinning) | https://www.psybertron.org/archives/15807 | open | blog review | one article | WebFetch | 🟡 TO-COLLECT — one of few English-language reviews |
| 09.04 | LeanZone.ru debate thread | https://www.leanzone.ru/index.php?option=com_kunena&view=topic&catid=9&id=13813 | open | forum | one thread | WebFetch | 🟡 LOW PRIORITY |
| 09.05 | mtsepkov.org notes (Tsepkov blog) | https://mtsepkov.org/ | open | blog | multi-year | WebFetch | 🟡 LOW PRIORITY |
| 09.06 | inexsu.wordpress.com 2020 ШСМ alpha post | https://inexsu.wordpress.com/2020/05/23/левенчук-системноинжене/ | open | blog | one post | WebFetch | 🟡 TO-COLLECT |
| 09.07 | baguzin.ru book review | https://baguzin.ru/wp/anatolij-levenchuk-sistemnoe-myshlenie/ | open | book review | one article | WebFetch | 🟡 LOW PRIORITY |
| 09.08 | in.wiki article (Russian bio wiki) | https://in.wiki/Левенчук,_Анатолий_Игоревич | open | encyclopedia entry | one page | WebFetch | 🟡 TO-COLLECT (already partially in R-A) |
| 09.09 | Letopis.org chronicle entry | https://letopis.org/hero/386 | open | bio entry | one page | WebFetch | 🟡 LOW PRIORITY |

### Category 10 — What we already have in repo (Existing-in-Repo inventory)

| ID | Source | Path | Status |
|----|--------|------|--------|
| 10.01 | FPF spec vendored copy | `raw/external/ailev-FPF/FPF-Spec.md` (62,202 lines) | ✅ EXISTING |
| 10.02 | FPF readme vendored | `raw/external/ailev-FPF/Readme.md` (384 lines) | ✅ EXISTING |
| 10.03 | FPF attribution | `raw/external/ailev-FPF/ATTRIBUTION.md` | ✅ EXISTING |
| 10.04 | Levenchuk deep biographical research | `raw/research/levenchuk-deep-research-2026-04-18.md` (361 lines) | ✅ EXISTING |
| 10.05 | Levenchuk for AI deep research | `raw/research/levenchuk-for-ai-deep-research-2026-04-19.md` (1041 lines) | ✅ EXISTING |
| 10.06 | Levenchuk FPF knowledge base | `raw/research/levenchuk-fpf-knowledge-base-2026-04-20.md` (2456 lines) | ✅ EXISTING |
| 10.07 | FPF gap analysis | `raw/research/fpf-gap-analysis-2026-04-20.md` (2486 lines) | ✅ EXISTING |
| 10.08 | R-A Levenchuk body of work | `raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md` | ✅ EXISTING |
| 10.09 | R-B ШСМ 5 primitives | `raw/research/levenchuk-fpf-research-2026-04-20/R-B-shsm-5-primitives-deep.md` (26,597 tokens) | ✅ EXISTING |
| 10.10 | R-C 17 transdisciplines mapping | `raw/research/levenchuk-fpf-research-2026-04-20/R-C-17-trans-disciplines-mapping.md` (30,904 tokens) | ✅ EXISTING |
| 10.11 | R-D Essence Kernel × ШСМ | `raw/research/levenchuk-fpf-research-2026-04-20/R-D-essence-kernel-shsm-relation.md` | ✅ EXISTING |
| 10.12 | R-E Mereology / holon hierarchy | `raw/research/levenchuk-fpf-research-2026-04-20/R-E-mereology-holon-hierarchy.md` (27,992 tokens) | ✅ EXISTING |
| 10.13 | Sub-agent A — FPF-Spec 5 primitives extraction | `raw/research/step-2-2-2-extractions/A-fpf-spec-5-primitives.md` | ✅ EXISTING |
| 10.14 | Sub-agent B — 8 blocks / 10 alphas / rituals | `raw/research/step-2-2-2-extractions/B-8blocks-10alphas-rituals.md` | ✅ EXISTING |
| 10.15 | Sub-agent C — 17 transdisciplines essence holon | `raw/research/step-2-2-2-extractions/C-17transdiscs-essence-holon.md` | ✅ EXISTING |
| 10.16 | Sub-agent D — baseline master synthesis | `raw/research/step-2-2-2-extractions/D-baseline-master-synthesis.md` | ✅ EXISTING |
| 10.17 | Sub-agent E — gap analysis prior art | `raw/research/step-2-2-2-extractions/E-gap-analysis-priorart.md` | ✅ EXISTING |
| 10.18 | Anatoly Levenchuk L1 profile | `profiles/l1-first-clan/anatoliy-levenchuk.md` | ✅ EXISTING |
| 10.19 | Tseren Tserenov L1 profile | `profiles/l1-first-clan/tseren-tserenov.md` | ✅ EXISTING |
| 10.20 | L1 profiles synthesis | `_archive/calls/_L1-PROFILES-TSEREN-LEVENCHUK-2026-05-16.md` | ✅ EXISTING |
| 10.21 | Tseren YT export + analysis | `raw/research/2026-04-28-tseren-yt-export/` (127+452+37 videos metadata + report) | ✅ EXISTING |
| 10.22 | Tseren TG export + analysis | `raw/research/2026-04-28-tseren-tg-export/` (618 posts + report) | ✅ EXISTING |
| 10.23 | JETIX-FPF derivative doc (archived) | `archive/design/JETIX-FPF.md` (3762 lines) | ✅ EXISTING (archived 2026-05-06) |
| 10.24 | Inbox: Левенчук TG message 2026-05-17 | `inbox/levenchuk-tg-2026-05-17.md` | ✅ EXISTING — trigger |
| 10.25 | 292 files mentioning Левенчук/FPF/ШСМ across repo | various | grep-count 2026-05-17 — large derivative web |

---

## §2 Access plan

### §2.1 Tooling

- **`git clone` / `gh api`** — Category 01 (GitHub FPF); free, fast
- **`curl` + `pandoc` / `html2text`** — Categories 02 (LJ), 03 (МИМ site), 07 (arXiv PDFs), 08.04 (Medium), 09 (third-party)
- **`WebFetch` (built-in Claude Code tool)** — single-page extraction with prompt-based summarization; не сохраняет full HTML, но extracts key claims
- **`WebSearch`** — discovery layer (find URLs we don't have yet)
- **yt-dlp** — Category 03.08, 08.01 YouTube; **BLOCKED on server IP** per 2026-04-28 analysis (bot challenge); workaround = metadata only via Invidious API (limited)
- **`tdlib` / TG export** — Category 06 Telegram; 06.05 already done; 06.02 would need new export
- **Manual purchase / aisystant subscription** — Categories 04, 05 paid materials; Ruslan handles per §0.0 ack
- **Residency application** — 04.10 paid + cohort-gated; Ruslan applies per §0.0 ack

### §2.2 Priority order (for Phase A within autonomy budget)

**Tier 1 — fast wins, no blockers (do first in §2 Collection):**

- **T1.1** — FPF freshness check: compare local `raw/external/ailev-FPF/FPF-Spec.md` (vendored 2026-04-20) vs upstream HEAD via `gh api repos/ailev/FPF/commits/main` — note any deltas
- **T1.2** — Левенчук LJ key posts (02.10 + 02.11) via WebFetch — ~10 posts
- **T1.3** — МИМ public site core pages (03.01, 03.05, 03.06, 03.11) via WebFetch
- **T1.4** — arXiv PDFs (07.01, 07.02) via curl
- **T1.5** — Psybertron English review (09.03) via WebFetch
- **T1.6** — systemsworld.club Tseren profile (08.11) via WebFetch

**Tier 2 — medium effort:**

- **T2.1** — LJ tag-filtered scrapes (02.02-02.09) — pick top 50 posts each tag
- **T2.2** — Habr / vc.ru third-party (09.01, 09.02) via WebFetch
- **T2.3** — `ailev/*` other repos listing (01.03) via gh api
- **T2.4** — TechInvestLab 2015 PDF (07.05) via curl

**Tier 3 — paid (RUSLAN handles separately per §0.0):**

- aisystant subscription activation + curse content download
- Book purchases (Ridero)
- Residency application R0 → R1

**Tier 4 — blocked (add to blockers.md):**

- YouTube full transcripts (03.08a) — infrastructure-level block; **degrade gracefully** к metadata + titles + descriptions
- 06.01 `@ailev_blog` if doesn't exist — surface as "not found"

### §2.3 Output structure (raw/external/levenchuk-corpus-2026-05-17/)

```
01-github/        — FPF freshness diff + ailev/* repos listing
02-livejournal/   — key posts + tag-filtered samples (markdown)
03-youtube/       — metadata-only (transcripts blocked); analysis reports
04-books-outlines/— TOC + sample chapter excerpts (PUBLIC parts only; per §0.0 paid sources Ruslan handles separately)
05-aisystant-public/ — public landing page + course description (NOT paid content unless Ruslan supplies)
06-tseren-iwe/    — Цэрэн TG + YT analysis enrichments + Medium posts
07-third-party-discussions/ — Habr / vc.ru / Psybertron / others
blockers.md       — explicit list для Ruslan
MANIFEST.md       — final inventory с volumes (filled in §2 Collection complete)
```

---

## §3 Blockers (what needs Ruslan)

1. **05.11 «Инженерия интеллекта»** — title упомянут в `prompts/fpf-iwe-levenchuk-deep-study-2026-05-17.md §1.2.5` но не найден в R-A bibliography 2026-04-18. Возможные интерпретации: (a) future title not yet published; (b) misnamed «Инженерия личности»; (c) IWE-platform artifact (not a book); (d) sequence of blog posts. **NEEDS RUSLAN CLARIFICATION.**
2. **05.10 «Системный фитнес»** — упомянут в prompt §1.2.5 но не в R-A bibliography. **NEEDS RUSLAN CLARIFICATION.**
3. **04.01-04.11 Aisystant subscription** — Ruslan acked в §0.0 но subscription activation + credentials handoff к server CC = manual step. Без credentials серверный CC может только public landing page WebFetch. **NEEDS RUSLAN handoff** OR explicit «работай только с public + Ruslan позже подгрузит paid content».
4. **04.10 Residency R0 application** — Ruslan acked но apply form likely requires identity/payment manually. **RUSLAN ACTION**.
5. **05.01-09 Books** — Ruslan acked «берём всё что есть». Самый pragmatic путь: aisystant digitized versions (если subscription active per blocker 3). Иначе Ridero purchases handled by Ruslan. **WAIT-FOR**.
6. **03.08a YouTube transcripts** — server-side blocked. Workarounds: (a) Ruslan manually downloads transcripts via browser; (b) accept metadata-only fidelity; (c) попробовать через client-side тулз позже. **DEGRADE GRACEFULLY** to metadata-only for Phase A.
7. **06.01 @ailev_blog** — handle existence not confirmed. **VERIFY via WebFetch / Telegram search** в §2 Collection.

---

## §4 Volume + cost estimate

### §4.1 Free / accessible volume (target for §2 Collection autonomy)

| Category | Estimated text volume | Notes |
|----------|----------------------|-------|
| 01 GitHub | ~5.8 MB (already vendored) + small delta | FPF-Spec already в repo |
| 02 LJ key posts | ~50K words (~150-200 pages) | Tier 1 + Tier 2 subset |
| 03 МИМ public | ~5-10K words | landing pages + curriculum |
| 03 YT metadata | already collected ~452+127 entries | analysis report exists |
| 07 arXiv | ~30-40 pages × 2 papers | ~80 pages total |
| 09 Third-party | ~5-20K words | selective |
| **TOTAL FREE** | **~5.9 MB FPF + ~250K words new** | manageable in Phase A |

### §4.2 Paid materials volume (Ruslan handles separately per §0.0)

| Category | Estimated text volume | Cost |
|----------|----------------------|------|
| 04 Aisystant courses (8+ courses) | ~3000+ pages digitized | €/month subscription |
| 05 Books (~10 titles ≥1 not-yet-known) | ~3000+ pages | ~€100-200 if Ridero direct |
| 04.10 Residency R0 | mentor time + cohort | TBD cohort price |
| **TOTAL PAID** | **~6000+ pages** | within Ruslan baseline ack |

### §4.3 Cost cap snapshot (§0.0)

- €10/день baseline ack snimat для external services (cf. WebSearch / additional tools)
- €50 hard halt → log + ask
- WebFetch + WebSearch (built-in Claude Code) = no incremental cost
- yt-dlp = local-only (free)
- arXiv curl = free
- **Phase A within budget assuming server-side tools only.**

---

## §5 Stop condition for §1 Inventory

Inventory considered **complete-enough** для proceeding to §2 Collection when:

- [x] 10 categories enumerated (matched prompt §1.2)
- [x] EXISTING-IN-REPO inventory (category 10) explicit — avoid duplicate effort
- [x] Blockers explicit (§3) — Ruslan visibility
- [x] Volume/cost frame (§4) — no surprise overshoot
- [x] Access tooling specified (§2.1)
- [x] Tier priority order (§2.2) — preserves autonomous progress если paid blockers delay

**NOT a stop condition for inventory**: 100% completeness of every channel discovered. Per prompt §9: "продолжать с остальными" if any single source blocked. Inventory is alive document — extend if new channels discovered.

---

## §6 Provenance per row

Каждая строка sources таблицы выше имеет inline URL OR file path. Major source attestations:

- **R-A** (`raw/research/levenchuk-fpf-research-2026-04-20/R-A-levenchuk-full-body-of-work.md`) — primary biographical + corpus map source; cited for almost all Category 03, 05, 07 metadata
- **R-D** (`R-D-essence-kernel-shsm-relation.md`) — Essence / ШСМ adaptation history; cited for 02.10 LJ post IDs
- **R-B** + R-C + R-E — additional cross-refs for primitives
- **Tseren TG / YT analysis reports** (2026-04-28) — cited for 06.05, 08.01-03
- **profiles/l1-first-clan/{anatoliy-levenchuk,tseren-tserenov}.md** — cited for 03.04, 06.05-06, 08.04-08
- **inbox/levenchuk-tg-2026-05-17.md** — trigger document; cited for category 04.09 IWE significance, 04.10 residency invite

---

*Inventory complete. Proceeding to §2 Collection per Tier order.*
