# Paid Sources Guide — где искать и legal/grey варианты

**Что это:** книги которые стоят денег (Amazon / O'Reilly / publisher).
Варианты получения в порядке preference.

## Strategy

### Option 1 — Buy legit (preferred для long-term reference)
- **Amazon Kindle** — $10-30 per book, download as .azw3 → convert to PDF
- **O'Reilly Safari subscription** — $39/mo unlimited technical books
- **Audible** — audiobook + text-to-text conversion (Whisper transcribe)

### Option 2 — Library loans (legit, free)
- **Archive.org / Internet Archive** — controlled lending — https://archive.org/details/inlibrary
- **Local library via Libby / Overdrive** — German libraries often have English PDFs
- **Open Library** — openlibrary.org

### Option 3 — Grey zone (most effective for acquisition speed)
- **Anna's Archive** — https://annas-archive.org — META search (LibGen + Z-Library + Sci-Hub + IA)
- **Library Genesis** — https://libgen.is/ OR https://libgen.rs/ — прямой search
- **Z-Library** — https://z-library.sk/ (нестабильный, постоянно меняет домен)
- **1lib.sk** — Z-Library mirror

**ВАЖНО:** эти источники работают в серой правовой зоне. Используй для
**personal study**, не distribute. Для production Jetix deliverables — купи
legit versions критичных книг.

## Полный список — Wave 2 PRIORITY (20-25 книг)

### §3.8 Systems Thinking (P0)
1. **Thinking in Systems: A Primer** — Donella Meadows, 2008, ISBN: 978-1603580557
2. **The Fifth Discipline** — Peter Senge, 1990 rev 2006, ISBN: 978-0385517256
3. **Systems Thinking for Curious Managers** — Russell Ackoff, 2010, ISBN: 978-0956263155

### §3.7 Management Philosophy (P1)
4. **High Output Management** — Andy Grove, 1995, ISBN: 978-0679762881
5. **Only the Paranoid Survive** — Andy Grove, 1996, ISBN: 978-0385483827
6. **Reinventing Organizations** — Frederic Laloux, 2014, ISBN: 978-2960133509
7. **The Effective Executive** — Peter Drucker, 2006, ISBN: 978-0060833459
8. **No Rules Rules** — Reed Hastings, 2020, ISBN: 978-1984877864
9. **The Hard Thing About Hard Things** — Ben Horowitz, 2014, ISBN: 978-0062273208

### §3.6 Product Management (P1)
10. **Inspired, 2nd ed** — Marty Cagan, 2017, ISBN: 978-1119387503
11. **Empowered** — Cagan & Jones, 2020, ISBN: 978-1119691297
12. **Continuous Discovery Habits** — Teresa Torres, 2021, ISBN: 978-1736633301
13. **The Lean Startup** — Eric Ries, 2011, ISBN: 978-0307887894
14. **Measure What Matters** — John Doerr, 2018, ISBN: 978-0525536222

### §3.4 Clean Code / Engineering (P1)
15. **A Philosophy of Software Design, 2nd ed** — John Ousterhout, 2021, ISBN: 978-1732102217
16. **The Pragmatic Programmer, 20th anniv** — Hunt & Thomas, 2019, ISBN: 978-0135957059
17. **Refactoring, 2nd ed** — Martin Fowler, 2018, ISBN: 978-0134757599

### §3.9 Cybernetics (P1)
18. **Brain of the Firm** — Stafford Beer, 1972, ISBN: 978-0471948391
19. **Cybernetics: Or Control and Communication** — Norbert Wiener, 1961, ISBN: 978-0262730099

### §3.13 Biology/Evolution (P1)
20. **The Selfish Gene, 40th anniv** — Dawkins, 2016, ISBN: 978-0198788607
21. **The Blind Watchmaker** — Dawkins, 1986, ISBN: 978-0393315707
22. **The Major Transitions in Evolution** — Maynard Smith & Szathmáry, 1995, ISBN: 978-0198502944
23. **At Home in the Universe** — Stuart Kauffman, 1995, ISBN: 978-0195111309

### §3.15 Philosophy of Science (P1)
24. **The Logic of Scientific Discovery** — Popper, 2002 ed, ISBN: 978-0415278447
25. **The Structure of Scientific Revolutions, 50th anniv** — Kuhn, 2012, ISBN: 978-0226458120

### §3.16 Engineering Foundations (P1)
26. **Discussion of the Method** — Billy Vaughn Koen, 2003, ISBN: 978-0195155990

### §3.11 Investing (P2)
27. **Poor Charlie's Almanack** — Charlie Munger / Peter Kaufman, ISBN: 978-1578645015
28. **Antifragile** — Nassim Taleb, 2012, ISBN: 978-0812979688
29. **The Intelligent Investor, rev ed** — Graham/Zweig, 2006, ISBN: 978-0060555665

## Wave 3 — Wider expansion (P2)
- Complexity: Mitchell / Beinhocker / West / Johnson / Barabási
- Meta: Kahneman / Ahrens / Deutsch / Hofstadter
- Management: Watkins First 90 Days + Horowitz What You Do + Grove extras
- PM: Play Bigger / Crossing the Chasm / Hooked / JTBD
- Philosophy: Holiday full stoic / Carse Finite & Infinite / Dixit Art of Strategy

Full list see: [Список документов и сырых материалов](https://www.notion.so/34a2496333bf816ab907e2dfe77ede0b)

---

## Semi-automated acquisition via Claude for Chrome

**Prompt для Chrome-агента:**
```
For each ISBN/title from tools/acquire/03-paid-sources-guide.md Wave 2 list:
1. Navigate to https://annas-archive.org/
2. Search by ISBN (most reliable) or title+author
3. Select top-rated English edition (latest PDF preferred)
4. Download to: raw/books-external/<subcategory>/<slug>.pdf
5. Rename according to ROY-INFORMATION-DIET.md naming convention
6. Log result (success/fail/alternative-needed) в tools/acquire/paid-acquisition-log.md

Subcategory mapping:
- Systems thinking (§3.8) → raw/books-external/systems/
- Management (§3.7) → raw/books-external/mgmt/
- Product mgmt (§3.6) → raw/books-external/pdm/
- Clean code (§3.4) → raw/books-external/clean-code/
- Cybernetics (§3.9) → raw/books-external/cybernetics/
- Biology (§3.13) → raw/books-external/biology/
- Philosophy of science (§3.15) → raw/books-external/philosophy-science/
- Engineering foundations (§3.16) → raw/books-external/engineering-foundations/
- Investing (§3.11) → raw/books-external/investing/

ETA: 5-10 minutes per book × 25 books = 2-4 hours автономно.
```

---

## Verification script (после acquisition)

```bash
# Count downloaded books per subcategory
for dir in raw/books-external/*/; do
    count=$(find "$dir" -name "*.pdf" -o -name "*.epub" -o -name "*.txt" | wc -l)
    echo "$(basename "$dir"): $count files"
done

# Sanity: total sizes
du -sh raw/books-external/*/
```

---

## Эскалация если Anna's Archive не работает

1. Try LibGen direct: https://libgen.is/ (search by ISBN)
2. Try Z-Library through Tor
3. Try Internet Archive borrow: https://archive.org/details/inlibrary (14-day loan, convert via Calibre)
4. Last resort: buy Kindle copy, use Calibre DeDRM plugin for personal PDF backup
