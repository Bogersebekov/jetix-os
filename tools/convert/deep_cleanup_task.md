# Deep Cleanup Task — prompt для Claude Code на сервере

**Цель:** Глубокая content-based чистка `raw/books-md/meta/` и `raw/books-md/philosophy/`
через multi-agent review. Не по size filter — по SUBSTANCE.

## Как запустить

```
ssh ruslan@100.99.156.28
tmux new -s deep-cleanup
cd ~/jetix-os
git pull origin claude/jolly-margulis-915d34
claude --dangerously-skip-permissions
```

Когда Claude запустится — paste промпт ниже целиком.

---

## PROMPT (copy-paste целиком)

```
Задача: глубокая content-based очистка raw/books-md/meta/ (184 файла) и
raw/books-md/philosophy/ (69 файлов) через multi-agent review.

Не критично на perfection — best-effort cleanup. Цель — убрать файлы которые
НЕ принесут ценности Jetix swarm при чтении (navigation / promotional /
content-thin / duplicate-of-book).

## Контекст задачи

Raw/books-md — это Jetix Private Library (см. decisions/ROY-INFORMATION-DIET.md
§1.6). Каждый файл должен нести substantive value для recursive swarm который
будет читать всё это через Domain-Experts. Naval tiny teasers / Anthropic
contact pages / duplicates of canonical books — шум для agents.

## Multi-Agent Workflow

Используй CE Cora pattern — brigadier + parallel reviewers.

### Роли

**Brigadier (ты)** — orchestrator
1. Load all file metadata (paths + titles + word_counts + first 500 chars)
2. Split по batches of ~20-30 files
3. Launch parallel Task subagents (Claude Code Task tool) — по batchu per
   subagent
4. Aggregate verdicts
5. Execute deletions
6. Regenerate INDEX + log

**Content Reviewer subagent** (одинаковый тип, запускается параллельно на
каждом batch)
- Читает каждый file (при необходимости — open + sample content)
- Outputs verdict: KEEP / DELETE / UNCERTAIN
- Brief reason per verdict (1 sentence)

## Critères для решений

### DELETE если:
- Navigation page ("subscribe", "contact", "careers", "newsletter", "404")
- Content-thin (<1500 слов AND не содержит dense insights — просто blog-teaser)
- Duplicate of canonical book в той же subcategory (напр. Naval Almanack
  chapter preview vs full Naval Almanack book)
- Promotional / marketing fluff без substance
- Meta / "about this site" / TOS / privacy / GDPR pages
- Mostly links list без original content
- Podcast episode transcripts где 90% = автор смех / ads / intro — без
  real information density

### KEEP если:
- Standalone substantive essay (Paul Graham essay / Naval podcast transcript
  если contains full philosophical content)
- Technical deep-dive (Anthropic engineering post / Karpathy insight)
- Book chapter или section с unique content not covered в книге
- Management lesson с real substance (37signals / Basecamp manifesto with
  actual principles)
- Any canonical work (даже короткая)

### UNCERTAIN если:
- Borderline 1500-3000 слов где substance unclear
- Контент overlap с книгой но имеет уникальный angle
- Keep by default, flag в log

## Конкретные patterns для meta/

**DELETE candidates (проверь что это junk before delete):**
- Anthropic legal / trust pages (privacy / security / data-processing /
  DPA / cookie-policy)
- Anthropic careers / contact / about-us / brand-page
- Cognition navigation (cognition-london / cognition-contact)
- MCP documentation DUPLICATES (если same content в multiple files)
- Windsurf-data-use и подобное
- Short teaser posts <2000 слов без density

**KEEP (high-value):**
- Karpathy's actual blog posts (LLM Wiki / SPL / Year in Review)
- Boris Cherny talks transcripts с substance
- Anthropic engineering deep-dives (built-multi-agent-research / etc.)
- Cognition blog posts с architectural lessons
- Aider blog posts с technical insights
- Farnam Street mental models posts
- MCP spec main documents

## Конкретные patterns для philosophy/

**DELETE candidates:**
- Naval "subscribe", "venture-hacks" teasers
- "New blog and feed address" / "stories" / admin notes
- Short "on humility" / "on meditation" без substance (если <300 слов — это
  tweet-teaser Naval, delete)
- Interview announcements ("interview on entrepreneurship up at gigaom tv")
- Venture-hacks co-founder / shortform posts

**KEEP:**
- Naval full podcasts: "How to Get Rich" (44K слов — keep), "How to Think
  Clearly", "Becoming Happy"
- Naval Almanack — canonical, keep
- Paul Graham essays — все legitimate (даже короткие 1500-2500 слов — это
  canonical)
- Greene 48 Laws (canonical)
- Holiday Daily Stoic (canonical)
- Carse Finite and Infinite Games (canonical)

## Workflow Steps

1. **Gather metadata** — для каждого MD file в meta/ и philosophy/:
   - path, title, word_count, first 500 chars content preview
   - Collect в один JSON массив
   - Не читай full content — только frontmatter + preview

2. **Batch split** — разбей на batches по 25 files per batch. Ожидаемо:
   - meta/ (184) → 8 batches
   - philosophy/ (69) → 3 batches
   - Total: 11 parallel subagent calls

3. **Launch subagents** — используй Task tool. Prompt каждому:
   ```
   You are a content reviewer для Jetix Private Library.
   
   Read this batch of {N} blog posts metadata. For each file, verdict:
   - KEEP (substantive content — keep in library)
   - DELETE (junk: navigation / promo / duplicate / content-thin)
   - UNCERTAIN (keep by default, flag reason)
   
   Critères provided: [insert critères above]
   
   For BORDERLINE cases — read the content (up to 1000 words) to verify.
   
   Return a JSON array with entries:
   [
     {"path": "...", "verdict": "KEEP|DELETE|UNCERTAIN", "reason": "1 sentence"},
     ...
   ]
   ```
   Pass batch metadata + critères.

4. **Aggregate verdicts** — collect all subagent outputs.

5. **Execute deletions** — для each DELETE:
   - rm file
   - Log in raw/books-md/_DELETED-LOG-DEEP.md (path + reason)

6. **Regenerate INDEX** — `python tools/convert/convert_all.py --step index`

7. **Git commit + push**:
   ```
   git add raw/books-md/ tools/convert/logs/
   git commit -m "[raw] deep cleanup meta/ + philosophy/ via multi-agent review (kept N, deleted M)"
   git push origin claude/jolly-margulis-915d34
   ```

## Safety

- НЕ удаляй files вне meta/ и philosophy/ subcategories
- НЕ удаляй files с title matching canonical book names (Naval Almanack /
  PG essay / Horowitz book / etc.) — эти всегда keep
- UNCERTAIN → KEEP by default
- Сохрани _DELETED-LOG-DEEP.md with ВСЕ deletions: path / size / reason /
  which subagent made decision

## Expected результат

- meta/ 184 → ~100-140 files (cleaned но sizeable base)
- philosophy/ 69 → ~40-60 files (Naval core + PG essays + Stoic)
- _DELETED-LOG-DEEP.md с detailed deletions
- INDEX.md regenerated
- Git pushed

## Рассчитываемое время

- Subagent batches в parallel: 5-10 минут
- Aggregation + execution: 5 минут
- Total: ~15-20 минут

Используй extended thinking max для balancing aggression vs preservation.
Приоритет — сохранять substance, удалять только явно low-value.

Поехали.
```

---

## После завершения

На локале:
```
cd C:\Users\49152\Desktop\jetix-os
git pull origin claude/jolly-margulis-915d34
cat raw/books-md/_DELETED-LOG-DEEP.md | head -30
find raw/books-md -name "*.md" ! -name "INDEX.md" ! -name "_*" | wc -l
```

Увидишь deletions with reasons. Total files будет ~350-380 (сейчас 438).

Потом — re-OCR 8 failed books (отдельная задача).
