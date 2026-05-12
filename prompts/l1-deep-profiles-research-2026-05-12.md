# L1 First Clan Deep Profiles Research — Trigger Prompt

> **Создано:** 2026-05-12 evening.
> **Назначение:** CC autonomous deep research per 9 L1 First Clan members; output = 9 profile files в `profiles/l1-first-clan/`.
> **Wall-clock target:** 1.5-2.5h.
> **Per profile target:** 800-1500 words, 11 sections.

---

## Команды запуска

```bash
# В Claude Code:
# (paste prompt ниже)
```

---

===PROMPT===

Задача: deep research per 9 L1 First Clan members → 9 profile files в `profiles/l1-first-clan/`. Web search public + social media OK. Goal: quick-share elevator pitch + new contact methods discovery + outreach strategy per person.

## L1 First Clan — 9 members (research targets)

| # | Имя | CRM stub | Profile output slug |
|---|---|---|---|
| 1 | Андрей Федорев | `crm/people/andrey-fedorev.md` | `andrey-fedorev` |
| 2 | Оскар Хартман | `crm/people/oskar-khartmann.md` | `oskar-khartmann` |
| 3 | Олег Брагинский | `crm/people/oleg-braginsky.md` | `oleg-braginsky` |
| 4 | Цэрэн Цэрэнов | `crm/people/tseren-tserenov-l1.md` | `tseren-tserenov` |
| 5 | Анатолий Левенчук | `crm/people/anatoliy-levenchuk-l1.md` | `anatoliy-levenchuk` |
| 6 | Дмитрий (Гуманитарщина) | `crm/people/dmitriy-humanitarschina.md` | `dmitriy-humanitarschina` |
| 7 | Павел Дуров | `crm/people/pavel-durov.md` | `pavel-durov` |
| 8 | Егор Гиренко | `crm/people/egor-girenko.md` | `egor-girenko` |
| 9 | Владимир Тарасов | `crm/people/vladimir-tarasov.md` | `vladimir-tarasov` |

Existing CRM stubs (read first) содержат initial contact links + 1-line context — use as starting point.

## Output structure

**Folder:** `profiles/l1-first-clan/` (NEW dir — mkdir at first write)

**Files (9 total):** `profiles/l1-first-clan/{slug}.md` per person matching slugs above

**Per file: 11 sections** per following template:

```markdown
---
title: Profile — <Имя Фамилия>
date: 2026-05-12
type: l1-deep-profile
person_slug: <slug>
crm_entry: crm/people/<crm-filename>.md
cohort: l1-first-clan-2026-05-12
research_depth: web-search + public sources + social media
confidence: <high|medium|low>  # per-section если varies
information_cutoff: 2026-05-12
F: F2
G: l1-profile-applied-now
R: refuted_if_contact_method_invalid_OR_biographical_facts_demonstrably_wrong
---

# <Имя Фамилия> — L1 First Clan Profile

## §1 Basic Profile
- **Полное имя:** <verbatim official>
- **Aliases / транслитерации:** <list>
- **Год рождения / возраст:** <if public>
- **Гражданство / current location:** <country / city if public>
- **Языки:** <ru/en/de/etc>
- **Education:** <university / degree if public>
- **Family / status:** <only if public AND relevant к L1 context — skip if private>

## §2 Professional Summary
- **Current role / org:** <position + company>
- **Notable past roles:** <2-3 prior key positions>
- **Career arc (5-7 lines):** <compressed timeline>
- **Key achievements:** <3-5 verifiable>
- **Net worth / income bucket:** <high/medium/unknown — only bucket, not specific>

## §3 Expertise / Methodology
- **Core expertise areas:** <3-5 domains>
- **Methodological school / lineage:** <which tradition>
- **Signature ideas / concepts:** <3-5 ideas they're known for>
- **Key works (books / papers / talks):** <list с years>
- **Influences / mentors:** <who shaped them>

## §4 Public Presence (channels — table)
| Channel | URL | Followers (est) | Activity | Notes |
|---|---|---|---|---|
| YouTube | ... | ... | active/dormant | ... |
| Telegram (personal/channel) | ... | ... | ... | ... |
| Twitter / X | ... | ... | ... | ... |
| LinkedIn | ... | ... | ... | ... |
| Personal blog / website | ... | ... | ... | ... |
| Podcast | ... | ... | ... | ... |
| Other | ... | ... | ... | ... |

**NEW contacts discovered (вне initial CRM stub):** <highlight всё что новое >

## §5 Contact Methods
- **Direct contact options:** <TG handle / email / DM channels>
- **Indirect paths:** <mutual connections / managers / agents / community paths>
- **Estimated response probability per channel:**
  - Channel X: high/medium/low — reasoning
- **Best approach recommended:** <which channel first touch + why>

## §6 Connection Points с Jetix
- **Why critical для L1 (3 specific reasons):** <list>
- **What overlaps с Jetix vision:** <Hexagon insights resonance — H1-H7 references>
- **What they could contribute:** <expertise / network / mentorship / endorsement / capital>
- **What Jetix could offer them:** <value proposition specific to this person>
- **Existing references к их work в Jetix docs:** <if any в decisions/ / wiki/ / reports/>

## §7 Outreach Strategy
- **First touchpoint:** <where + when + format>
- **Tone:** <intellectual / casual / formal / philosophical>
- **Initial ask (low-barrier):** <«прочитать» / «обратная связь» / «короткий разговор»>
- **Long-term ask:** <Charter signature / mentorship / partnership / Council membership>
- **Potential blockers:** <busy / brand mismatch / political stance / etc>
- **What to prepare BEFORE contact:** <materials / specific question / mutual intro>

## §8 1-Line Elevator Pitch (для quick share между L1)
> «<X> — <role>, <key signature idea>, <why relevant к L1>»

Example format: «Левенчук — научный руководитель ШСМ, methodology as moat для info-work, 11-летний партнёр Цэрэна (МИМ).»

## §9 Risks / Cautions
- **Sensitive topics:** <areas where opinionated / divisive>
- **Reputation flags:** <controversy / lawsuits / public friction>
- **Compatibility concerns:** <anti-extraction stance? cooperation orientation? scale ambitions?>
- **Geopolitical sensitivities:** <RU/UA/IL/etc context if relevant>

## §10 Sources / Provenance
- **Web search queries used:** <list with date>
- **Primary sources cited:** <wikipedia / interviews / books / website / verified social>
- **Information cutoff:** <date of last verified info>
- **Confidence level overall:** <high/medium/low + per-section variance>
- **Outdated info flags:** <what might be stale + what was unverifiable>

## §11 Recommended Next Actions
- **Specific first contact action:** <verbatim what Ruslan should do>
- **Preparation needed:** <materials / video / letter / specific question>
- **Timeline suggestion:** <when reasonable to reach out>
- **Tracking:** <success metric для first response>

---

*Source: web search + public materials (cutoff 2026-05-12). NOT exhaustive — initial profile draft. Deeper relationship research follows after initial contact.*
```

## Workflow per person (~10-15 min each × 9)

1. Read CRM stub `crm/people/<slug>.md` для starting point (links / context)
2. Web search:
   - `<Имя> Wikipedia` (biographical baseline)
   - `<Имя> interview podcast 2024 2025` (recent voice)
   - `<Имя> книга OR статья OR talk` (key works)
   - `<Имя> Twitter OR Telegram` (social presence)
   - `<Имя> LinkedIn OR website` (professional)
   - `<Имя> + Jetix-relevant keyword` (для connection points — e.g., «Levenchuk + systems thinking», «Hartmann + investor», etc.)
3. Synthesize per template (11 sections)
4. Write file `profiles/l1-first-clan/<slug>.md`
5. Mark confidence level per section honestly (skip if unverifiable)
6. Move to next person

**Order:** твой call (efficient batching по language / domain similarity OK). All 9 must be done.

## Web search policy

- ✅ Public sources (Wikipedia / official websites / published interviews / books)
- ✅ Social media public posts (Twitter/X / TG channels / YouTube descriptions / LinkedIn public)
- ❌ Private / paywalled investigations (lawsuits / financial disclosures beyond bucket-level)
- ❌ Speculation / unverified rumors / gossip
- ❌ Family details unless person made public themselves

**Provenance:** every claim in profile must cite source URL OR mark `confidence: low / unverified` explicitly.

## Hard constraints

- **Constitutional posture:** F2 blast-radius (append-only к `profiles/l1-first-clan/`), NO writes к Foundation / principles / .claude/config / shared/schemas / CLAUDE.md / decisions/ / wiki/ / crm/
- **AI = scribe (Tier 2 R1):** profiles = factual extraction + outreach strategy hypothesis; NOT strategic prose authored
- **Tier 2 R6 provenance:** every claim cites source OR marked unverified
- **Tier 2 R7:** profiles не contradict existing Hexagon (Heptagon) insights
- **Tier 2 R10:** NO impersonation — profiles describe person from public sources only, не false-quoting
- **Append-only:** new files, NO overwrites
- **Halt-log-alert** при violations

## Special handling per person

- **Дуров (Павел)** — high-public-profile, much info available, но direct contact unlikely. Focus on indirect paths.
- **Цэрэн / Левенчук** — already partially covered в existing Jetix docs (МИМ / ШСМ references). Cross-link к existing canonical.
- **Тарасов (Владимир)** — Tallinn school + Russian-speaking management strategy. Может быть more bio info available чем initial guess.
- **Дмитрий (Гуманитарщина)** — может быть hard to find full name (handle-only). Document accurately what's findable.
- **Гиренко (Егор)** — Strategy Club community profile, less mainstream visibility. Focus on community context.
- **Хартман (Оскар)** — well-known German-Russian investor, much info available.
- **Брагинский (Олег)** — already в Jetix memory как future research target. Cross-link к memory note.
- **Федорев (Андрей)** — least info в existing Jetix docs. Need broader search.

## Wall-clock target

- Per profile: 10-15 min average
- Total: 1.5-2.5h for all 9
- Hard cap: 3h

## Commit + push (incremental OK)

После each batch of 3 profiles (или all 9 at end):
```
git add profiles/l1-first-clan/
git commit -m "[l1-profiles] Deep profile batch — <count> profiles done (<slugs>), web+social sources, outreach strategy per person"
git push origin main
```

OR all 9 at once в финальный commit:
```
git add profiles/l1-first-clan/
git commit -m "[l1-profiles] 9 L1 First Clan deep profiles complete — Heptagon-grounded outreach strategy per person, new contacts discovered, elevator pitches ready для L1 cross-sharing"
git push origin main
```

## Final report

Surface к Ruslan:
- 9 profile paths (GitHub URLs)
- SHA final commit
- **NEW contacts discovered** (channels не в initial CRM stubs)
- 3-5 surprising findings (что non-obvious surfaced about anyone)
- **Top 3 priority order для outreach** (Ruslan recommendation based on response probability + readiness)
- Recommended next: «Ruslan reads profiles → strategizes Charter outreach order → Charter v0 writing с specific cite per person»

Constitutional preserved. AI = scribe + analyst. Ruslan = sole strategist + outreach decision-maker.

GO. Жгу до конца or 3h hard cap.

===END PROMPT===
