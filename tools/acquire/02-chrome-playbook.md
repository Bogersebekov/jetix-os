# Chrome Playbook — Claude for Chrome acquisition

**Инструмент:** Claude for Chrome extension (Anthropic)
**Что делает:** автономно ходит по сайтам, собирает контент
**Когда использовать:** interactive sites / JS-rendered / blog archives / multi-page

Для каждого источника — step-by-step prompt для Chrome-агента.
Запускать один блок за раз, проверять download, move в правильную папку.

---

## Setup (1 раз)

1. Установи Claude for Chrome extension
2. Открой папку repo в проводнике: `C:\Users\49152\Desktop\jetix-os\`
3. Default download folder: `raw/books-external/<subcategory>/` или `raw/articles/`

---

## §3.7 Management Philosophy

### 37signals full manifesto archive

**Prompt для Claude for Chrome:**
```
Navigate to https://37signals.com/writing/ and scroll to find all canonical
manifesto-style posts (Rails doctrine, Getting Real excerpts, Remote Work
principles, Shape Up announcement, ItDoesn'tHaveToBe manifesto). Save each as
markdown with title + date + author + body + URL. Save all into a single file:
raw/articles/37signals-manifesto-archive.md
```

### Netflix Culture Deck (Reed Hastings / Patty McCord 2009)

**Prompt:**
```
Navigate to https://www.slideshare.net/reed2001/culture-1798664 and download
the full deck as PDF. Save to: raw/books-external/mgmt/netflix-culture-deck-2009.pdf
If SlideShare requires login, extract slides as images and combine, or use
reed2001.com/culture-1798664 alternative.
```

### Paul Graham essays

**Prompt:**
```
Navigate to http://www.paulgraham.com/articles.html. For each essay in the
list, open it, extract title + date + full HTML body, save as markdown in
raw/articles/pg-<slug>-<year>.md. Focus на эти первыми:
- "Do Things That Don't Scale" (2013)
- "Makers Schedule, Managers Schedule" (2009)
- "How to Do Great Work" (2023)
- "Founder Mode" (2024)
- "How to Think for Yourself" (2020)
- "The Hacker Philosophy" (2004)
- "Startup = Growth" (2012)
После них — остальные по порядку.
```

---

## §3.8 Systems Thinking — Левенчук

### Левенчук LiveJournal archive

**Prompt:**
```
Navigate to https://ailev.livejournal.com/ and extract recent + top-rated posts
(2024-2026) о системном мышлении, методологии, интеллект-стеке. Save each как
markdown с metadata (title, date, URL) into:
raw/books-external/systems/levenchuk-livejournal-<year>.md
```

### ШСМ school resources

**Prompt:**
```
Navigate to https://system-school.ru/ and download any public free materials
(course outlines, sample chapters, essays). Save into
raw/books-external/systems/ with proper naming.
```

---

## §3.12 Mental Models

### Farnam Street archive

**Prompt:**
```
Navigate to https://fs.blog/mental-models/ and extract the complete Mental
Models primer + linked sub-pages. For each mental model page, save as markdown
into raw/books-external/meta/farnam-street-mental-models.md (consolidated) or
split by category. Also grab https://fs.blog/blog/ top-30 essays.
```

### LessWrong Rationality A-Z

**Prompt:**
```
Navigate to https://www.lesswrong.com/rationality and locate Sequences archive.
Download available ebook/PDF versions. Save to:
raw/books-external/meta/lesswrong-rationality-az.pdf
```

---

## §3.14 Philosophical Strategic — Naval

### Naval Ravikant — podcasts/tweetstorms

**Prompt:**
```
Naval content acquisition:
1. Navigate https://nav.al/rich — save tweetstorm + podcast transcript as:
   raw/transcripts/naval-how-to-get-rich-2019.md
2. Navigate https://nav.al/happy (Becoming Happy series) — save all transcripts:
   raw/transcripts/naval-becoming-happy-series.md
3. Navigate https://nav.al/think (How to Think Clearly) — save:
   raw/transcripts/naval-how-to-think-clearly.md
4. Twitter archive: go to https://twitter.com/naval — scroll pinned + top
   threads last 2 years, extract text+date, save:
   raw/transcripts/naval-twitter-threads.md
```

---

## §3.15 Philosophy of Science — SEP entries

### Stanford Encyclopedia of Philosophy

**Prompt:**
```
Navigate to https://plato.stanford.edu/ and download these entries as markdown:
1. "Karl Popper" — plato.stanford.edu/entries/popper/
2. "Thomas Kuhn" — plato.stanford.edu/entries/thomas-kuhn/
3. "Imre Lakatos" — plato.stanford.edu/entries/lakatos/
4. "Paul Feyerabend" — plato.stanford.edu/entries/feyerabend/
5. "Scientific Method" — plato.stanford.edu/entries/scientific-method/
6. "Scientific Revolutions" — plato.stanford.edu/entries/scientific-revolutions/

Save each as: raw/books-external/philosophy-science/sep-<slug>.md
```

---

## §3.17 Agent / AI Primary Sources

### Anthropic engineering blog — full archive

**Prompt:**
```
Navigate to https://www.anthropic.com/engineering and extract ALL posts
2024-2026. For each post: title + date + author + full body. Save as
markdown individually:
raw/articles/anthropic-engineering-<slug>-<date>.md
```

### Karpathy full archive

**Prompt:**
```
Karpathy content:
1. https://karpathy.ai/ — main page + linked essays
2. https://karpathy.bearblog.dev/ — all bearblog posts
3. https://github.com/karpathy (public gists especially) — key gists:
   - 442a6bf555914893e9891c11519de94f (LLM Wiki)
   - Any other gists with stars
4. YouTube channel https://www.youtube.com/@AndrejKarpathy — download
   transcripts for "Intro to LLMs", "Software is Changing (Again)", "Let's
   build GPT from scratch", etc. Use youtube transcript tool.

Save into: raw/articles/karpathy-<slug>-<date>.md
Save transcripts into: raw/transcripts/karpathy-<video>-<date>.md
```

### Boris Cherny talks

**Prompt:**
```
YouTube searches:
- "Boris Cherny Claude Code"
- "Boris Cherny Builder.io"
- "Boris Cherny Anthropic"
Download transcripts for top 5-10 videos. Save:
raw/transcripts/boris-cherny-<video>-<date>.md
```

### Aider blog (Paul Gauthier)

**Prompt:**
```
Navigate to https://aider.chat/blog/ and extract ALL posts. Save each:
raw/articles/aider-<slug>-<date>.md
```

---

## Priority order — Wave 1 Chrome

Run in this sequence:
1. Anthropic engineering blog (full archive) — 1-2h
2. Karpathy full archive — 1-2h
3. 37signals manifesto archive — 30min
4. Paul Graham essays (top 20) — 45min
5. SEP entries (6 entries) — 30min
6. Naval content (all podcasts transcripts) — 1h
7. Farnam Street archive — 1h
8. Aider blog — 30min
9. Boris Cherny YouTube transcripts — 45min
10. Karpathy YouTube transcripts — 1h

Total ETA: ~8-10 hours автономного Chrome-агента.

## После завершения

```bash
git add raw/
git commit -m "[raw] acquisition Wave 1 Chrome — interactive sites"
git push
```
