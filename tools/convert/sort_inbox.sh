#!/usr/bin/env bash
# Sort downloaded PDFs/EPUBs/TXTs from D:\Downloads\box1\ into inbox/<subcategory>/
# Based on filename matching — run once, drag-n-drop done automatically.
#
# Usage: bash tools/convert/sort_inbox.sh

set -u

REPO_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
cd "$REPO_ROOT"

SRC="D:/Downloads/box1"
INBOX="inbox"

if [ ! -d "$SRC" ]; then
    echo "❌ Source folder not found: $SRC"
    exit 1
fi

echo "=== Sorting files from $SRC into $INBOX/<subcategory>/ ==="
echo ""

# Helper: move file
mv_to() {
    local src_file="$1"
    local subcat="$2"
    local new_name="${3:-}"
    local src_path="$SRC/$src_file"

    if [ ! -f "$src_path" ]; then
        echo "⚠️  Not found: $src_file"
        return
    fi

    mkdir -p "$INBOX/$subcat"

    local dst_name
    if [ -n "$new_name" ]; then
        dst_name="$new_name"
    else
        dst_name="$src_file"
    fi

    local dst_path="$INBOX/$subcat/$dst_name"
    if [ -f "$dst_path" ]; then
        echo "⏭️  Exists: $INBOX/$subcat/$dst_name"
        return
    fi

    mv "$src_path" "$dst_path"
    echo "✅ $subcat/ ← $dst_name"
}

# ========================================================================
# §unix — Unix philosophy
# ========================================================================
mv_to "117249126-Unix-Programming-Environment-Brian-W-Kernighan-Rob-Pike.pdf" "unix" \
      "kernighan-pike-unix-programming-environment-1984.pdf"
mv_to "Art of Unix Programming — Eric Raymond.pdf" "unix" \
      "raymond-art-of-unix-programming-2003.pdf"

# ========================================================================
# §clean-code — Software engineering
# ========================================================================
mv_to "772053431-A-Philosophy-of-Software-Design-2nd-Edition-John-K-Ousterhout-Z-Library.pdf" "clean-code" \
      "ousterhout-philosophy-of-software-design-2ed-2021.pdf"
mv_to "402479056-the-pragmatic-programmer-pdf.pdf" "clean-code" \
      "hunt-thomas-pragmatic-programmer-2019.pdf"
mv_to "Clean Code ( PDFDrive.com ).pdf" "clean-code" \
      "martin-clean-code-2008.pdf"
mv_to "Martin Fowler - Refactoring - Improving the Design of Existing.pdf" "clean-code" \
      "fowler-refactoring-2ed-2018.pdf"
mv_to "mythical-man-month.pdf" "clean-code" \
      "brooks-mythical-man-month-1995.pdf"

# ========================================================================
# §pm — Project management
# ========================================================================
mv_to "shape-up.pdf" "pm" \
      "singer-shape-up-basecamp-2019.pdf"
mv_to "2020-Scrum-Guide-US.pdf" "pm" \
      "schwaber-sutherland-scrum-guide-2020.pdf"
mv_to "Project-Management-Institute-A-Guide-to-the-Project-Management-Body-of-Knowledge-PMBOK-R-Guide-PMBOK®️-Guide-Project-Management-Institute-2021.pdf" "pm" \
      "pmi-pmbok-7th-edition-2021.pdf"

# ========================================================================
# §pdm — Product management
# ========================================================================
mv_to "Inspired - Marty Cagan.pdf" "pdm" \
      "cagan-inspired-2ed-2017.pdf"
mv_to "transformed-moving-to-the-product-operating-model-silicon-valley-product-group-1nbsped-9781119697336-9781119697404-9781119697398.pdf" "pdm" \
      "cagan-transformed-2024.pdf"
mv_to "The Lean Startup - Erick Ries.pdf" "pdm" \
      "ries-lean-startup-2011.pdf"
mv_to "Measure-What-Matters-John-Doerr.pdf" "pdm" \
      "doerr-measure-what-matters-2018.pdf"
mv_to "dokumen.pub_continuous-discovery-habits-discover-products-that-create-customer-value-and-business-value-1736633309-9781736633304-t-8382149.epub" "pdm" \
      "torres-continuous-discovery-habits-2021.epub"

# ========================================================================
# §mgmt — Management philosophy
# ========================================================================
mv_to "2477the-hard-thing-about-hard-things.pdf" "mgmt" \
      "horowitz-hard-thing-about-hard-things-2014.pdf"
mv_to "458042966-Andrew-Grove-Only-the-Paranoid-Survive.pdf" "mgmt" \
      "grove-only-paranoid-survive-1996.pdf"
mv_to "Drucker-2006-The-Effective-Executive-The-Definitive-Guide-to-Getting-the-Right-Things-Done.pdf" "mgmt" \
      "drucker-effective-executive-2006.pdf"
mv_to "Reinventingorganization.pdf" "mgmt" \
      "laloux-reinventing-organizations-2014.pdf"
mv_to "The First 90 Days - Critical Success Strategies for New Leaders.pdf" "mgmt" \
      "watkins-first-90-days-2013.pdf"
mv_to "rework-jason-fried.pdf" "mgmt" \
      "fried-dhh-rework-2010.pdf"
mv_to "remote-office-not-required.pdf" "mgmt" \
      "fried-dhh-remote-2013.pdf"

# ========================================================================
# §systems — Systems thinking
# ========================================================================
mv_to "An Introduction to General Systems Thinking.pdf" "systems" \
      "weinberg-general-systems-thinking-1975.pdf"
mv_to "Meadows-2008.-Thinking-in-Systems.pdf" "systems" \
      "meadows-thinking-in-systems-2008.pdf"
mv_to "systems-thinking-for-curious-managers-with-40-new-management-f-laws-9781908009081.pdf" "systems" \
      "ackoff-systems-thinking-curious-managers-2010.pdf"

# ========================================================================
# §cybernetics — Cybernetics + VSM
# ========================================================================
mv_to "Ashby-Introduction-to-Cybernetics.pdf" "cybernetics" \
      "ashby-introduction-to-cybernetics-1956.pdf"
mv_to "The Brain of the Firm.pdf" "cybernetics" \
      "beer-brain-of-the-firm-1972.pdf"
mv_to "Wiener_Norbert_Cybernetics_or_the_Control_and_Communication_in_the_Animal_and_the_Machine_2nd_ed.pdf" "cybernetics" \
      "wiener-cybernetics-2ed-1961.pdf"
mv_to "ooc-mf.pdf" "cybernetics" \
      "kelly-out-of-control-1994.pdf"

# ========================================================================
# §complexity — Complexity science
# ========================================================================
mv_to "Complexity_-_A_Guided_Tour.pdf" "complexity" \
      "mitchell-complexity-a-guided-tour-2009.pdf"
mv_to "Origins of Wealth.pdf" "complexity" \
      "beinhocker-origin-of-wealth-2006.pdf"

# ========================================================================
# §investing
# ========================================================================
mv_to "Taleb_Antifragile__2012.pdf" "investing" \
      "taleb-antifragile-2012.pdf"
mv_to "skin-in-the-game-nassim-nicholas-taleb.pdf" "investing" \
      "taleb-skin-in-the-game-2018.pdf"
mv_to "The Intelligent Investor - BENJAMIN GRAHAM.pdf" "investing" \
      "graham-intelligent-investor.pdf"
mv_to "the-most-important-thing-illuminated-uncommon-sense-for-the-thoughtful-investor-9780231530798_compress.pdf" "investing" \
      "marks-most-important-thing-illuminated-2013.pdf"
mv_to "uorren_baffett-almanah_bednogo_charli_os-658da46057ce0.epub" "investing" \
      "munger-poor-charlies-almanack-ru.epub"
mv_to "the-complete-collection.pdf" "investing" \
      "buffett-shareholder-letters-collection.pdf"

# ========================================================================
# §biology — Biology / Evolution
# ========================================================================
mv_to "the-selfish-gene-4bhyg61ook.pdf" "biology" \
      "dawkins-selfish-gene.pdf"
mv_to "Richard Dawkins - The Blind Watchmaker.pdf" "biology" \
      "dawkins-blind-watchmaker-1986.pdf"
mv_to "Dennett-Darwin'sDangerousIdea.pdf" "biology" \
      "dennett-darwins-dangerous-idea-1995.pdf"
mv_to "Stuart Kauffman - At Home in the Universe The Search for the Laws of Self Organization and Complexity.pdf" "biology" \
      "kauffman-at-home-in-the-universe-1995.pdf"

# ========================================================================
# §philosophy — Naval + Stoic + Classical strategic
# ========================================================================
mv_to "Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf" "philosophy" \
      "jorgenson-naval-almanack-2020.pdf"
mv_to "The Daily Stoic.pdf" "philosophy" \
      "holiday-daily-stoic-2016.pdf"
mv_to "Finite-and-Infinite-Games-by-James-Carse.pdf" "philosophy" \
      "carse-finite-and-infinite-games-1986.pdf"
mv_to "The+48+Laws+Of+Power.pdf" "philosophy" \
      "greene-48-laws-of-power-1998.pdf"

# ========================================================================
# §philosophy-science — Popper / Kuhn / Lakatos
# ========================================================================
mv_to "popper-logic-scientific-discovery.pdf" "philosophy-science" \
      "popper-logic-of-scientific-discovery.pdf"
mv_to "CONJECTURES AND REFUTATIONS.pdf" "philosophy-science" \
      "popper-conjectures-and-refutations-1963.pdf"
mv_to "The Structure of Scientific Revolutions, 50th Anniversary Edition by Thomas S. Kuhn (z-lib.org).pdf" "philosophy-science" \
      "kuhn-structure-of-scientific-revolutions-50anniv-2012.pdf"

# ========================================================================
# §engineering-foundations
# ========================================================================
mv_to "526994063-Billy-Vaughn-Koen-Discussion-of-the-Method-Cond-BookFi-org.txt" "engineering-foundations" \
      "koen-discussion-of-the-method-2003.txt"
mv_to "what_engineers_know_and_how_they_know_it___analytical_studies_from_aeronautical_history_autoem.pdf" "engineering-foundations" \
      "vincenti-what-engineers-know-1990.pdf"
mv_to "engineering-of-creativity-0849322553-2820016200-9780849322556_compress.pdf" "engineering-foundations" \
      "altshuller-engineering-of-creativity-triz-1984.pdf"
mv_to "pg59.txt" "engineering-foundations" \
      "descartes-discourse-on-the-method-gutenberg.txt"

# ========================================================================
# UNKNOWN — these have UUID/number filenames, need manual check
# ========================================================================
echo ""
echo "⚠️  Unknown files (UUID/number names) — проверь ручками:"
for f in "0dd438d1-3d0f-4f50-b290-699e09f1bbf2.pdf" "1740653032786373292.pdf"; do
    if [ -f "$SRC/$f" ]; then
        size=$(stat -c%s "$SRC/$f" 2>/dev/null || stat -f%z "$SRC/$f" 2>/dev/null)
        echo "   $f ($size bytes)"
    fi
done
echo "   Открой каждый → посмотри на title → переместил в inbox/<subcategory>/ вручную"
echo ""

# ========================================================================
# SUMMARY
# ========================================================================
echo "=== SUMMARY ==="
echo ""
total=0
for sub in "$INBOX"/*/; do
    [ -d "$sub" ] || continue
    count=$(find "$sub" -maxdepth 1 -type f \( -name "*.pdf" -o -name "*.epub" -o -name "*.txt" \) 2>/dev/null | wc -l)
    if [ "$count" -gt 0 ]; then
        echo "  $(basename "$sub"): $count files"
        total=$((total + count))
    fi
done
echo ""
echo "Total moved: $total files"
echo ""

# Remaining in box1 (kept there — not recognized)
remaining=$(find "$SRC" -maxdepth 1 -type f 2>/dev/null | wc -l)
echo "Remaining in $SRC: $remaining"
if [ "$remaining" -gt 0 ]; then
    echo "Files left:"
    find "$SRC" -maxdepth 1 -type f 2>/dev/null | head -10
fi

echo ""
echo "NEXT: bash tools/convert/scrape_blogs.sh"
echo "  (это скачает blogs в inbox/ рядом с книгами)"
