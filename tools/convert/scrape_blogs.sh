#!/usr/bin/env bash
# Scrape all target blogs recursively using wget.
# Each blog gets saved to raw/books-external/<subcategory>/<blog-slug>/
# Later convert_all.py picks them up and converts HTML → Markdown.
#
# Usage: bash tools/convert/scrape_blogs.sh
#
# Skip already-scraped with --resume:
#   bash tools/convert/scrape_blogs.sh --resume
#
# Requirements: wget (comes with Git Bash on Windows).
#
# ETA: 1-3 hours wall-clock (depending on site sizes + network).

set -u
RESUME=${1:-""}

LOG="tools/convert/logs/scrape-$(date +%Y%m%d-%H%M%S).log"
echo "Scrape log: $LOG"
mkdir -p tools/convert/logs

UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'

scrape() {
    local name="$1"
    local dest="$2"
    local url="$3"
    local extra="${4:-}"

    mkdir -p "$dest"
    if [ "$RESUME" = "--resume" ] && [ -n "$(ls -A "$dest" 2>/dev/null)" ]; then
        echo "⏭️  SKIP (exists): $name" | tee -a "$LOG"
        return 0
    fi

    echo "" | tee -a "$LOG"
    echo "=== $name ===" | tee -a "$LOG"
    echo "URL: $url" | tee -a "$LOG"
    echo "Dest: $dest" | tee -a "$LOG"

    cd "$dest"
    # shellcheck disable=SC2086
    wget \
        --mirror \
        --convert-links \
        --adjust-extension \
        --page-requisites \
        --no-parent \
        --restrict-file-names=windows \
        --user-agent="$UA" \
        --wait=1 \
        --random-wait \
        --tries=3 \
        --timeout=30 \
        $extra \
        "$url" 2>&1 | tail -20 | tee -a "$LOG"
    cd - > /dev/null

    # Count files
    local count
    count=$(find "$dest" -name "*.html" -o -name "*.htm" 2>/dev/null | wc -l)
    echo "✅ $name: $count HTML files" | tee -a "$LOG"
}

REPO_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
cd "$REPO_ROOT"

# ========================================================================
# BLOGS
# ========================================================================

# Paul Graham essays (http://www.paulgraham.com/articles.html)
# Flat structure — все essays на paulgraham.com
scrape "Paul Graham essays" \
    "raw/books-external/philosophy/paul-graham-essays" \
    "http://www.paulgraham.com/articles.html" \
    "--level=2 --domains=paulgraham.com"

# Naval — nav.al (modern static site)
scrape "Naval blog (nav.al)" \
    "raw/books-external/philosophy/naval-blog" \
    "https://nav.al/" \
    "--level=3 --domains=nav.al --reject *.jpg,*.png,*.gif,*.svg,*.webp"

# Karpathy bearblog (https://karpathy.bearblog.dev/)
# Simple static blog
scrape "Karpathy bearblog" \
    "raw/books-external/meta/karpathy-bearblog" \
    "https://karpathy.bearblog.dev/" \
    "--level=2 --domains=karpathy.bearblog.dev"

# Karpathy main — https://karpathy.ai/
scrape "Karpathy main site" \
    "raw/books-external/meta/karpathy-ai" \
    "https://karpathy.ai/" \
    "--level=2 --domains=karpathy.ai"

# Anthropic engineering blog
# Note: Anthropic site может быть JS-heavy — если wget берёт мало, juggleм потом через Chrome
scrape "Anthropic engineering blog" \
    "raw/books-external/meta/anthropic-engineering" \
    "https://www.anthropic.com/engineering" \
    "--level=2 --domains=anthropic.com --include-directories=/engineering,/research"

# Aider blog (https://aider.chat/blog/)
scrape "Aider blog" \
    "raw/books-external/meta/aider-blog" \
    "https://aider.chat/blog/" \
    "--level=2 --domains=aider.chat"

# Cognition blog (Walden Yan + team)
scrape "Cognition blog" \
    "raw/books-external/meta/cognition-blog" \
    "https://cognition.ai/blog" \
    "--level=2 --domains=cognition.ai"

# Stanford Encyclopedia of Philosophy — specific entries only (site огромный)
for entry in popper thomas-kuhn lakatos feyerabend scientific-method \
             scientific-revolutions epistemology; do
    scrape "SEP: $entry" \
        "raw/books-external/philosophy-science/sep-$entry" \
        "https://plato.stanford.edu/entries/$entry/" \
        "--level=1 --domains=plato.stanford.edu"
done

# Farnam Street mental models (https://fs.blog/mental-models/)
scrape "Farnam Street mental models" \
    "raw/books-external/meta/farnam-street" \
    "https://fs.blog/mental-models/" \
    "--level=2 --domains=fs.blog --include-directories=/mental-models,/blog"

# Kevin Kelly — Out of Control (full book online)
scrape "Kevin Kelly Out of Control" \
    "raw/books-external/cybernetics/kelly-out-of-control" \
    "https://kk.org/outofcontrol/contents.php" \
    "--level=2 --domains=kk.org --include-directories=/outofcontrol"

# Art of Unix Programming (Eric Raymond) — full book online
scrape "Raymond Art of Unix Programming" \
    "raw/books-external/unix/art-of-unix-programming" \
    "http://www.catb.org/~esr/writings/taoup/html/" \
    "--level=2 --domains=catb.org --include-directories=/~esr/writings/taoup"

# 37signals writings + Getting Real
scrape "37signals podcast-and-excerpts" \
    "raw/books-external/mgmt/37signals-writings" \
    "https://37signals.com/podcast-and-excerpts" \
    "--level=2 --domains=37signals.com"
scrape "37signals Getting Real" \
    "raw/books-external/mgmt/37signals-getting-real" \
    "https://basecamp.com/gettingreal" \
    "--level=2 --domains=basecamp.com --include-directories=/gettingreal"

# Shape Up (уже скачали PDF, но полная web version может быть полезна)
scrape "Shape Up web version" \
    "raw/books-external/pm/shape-up-web" \
    "https://basecamp.com/shapeup" \
    "--level=2 --domains=basecamp.com --include-directories=/shapeup"

# Левенчук LiveJournal
scrape "Levenchuk LiveJournal recent" \
    "raw/books-external/systems/levenchuk-lj" \
    "https://ailev.livejournal.com/" \
    "--level=1 --domains=ailev.livejournal.com --wait=2"

# MCP spec
scrape "MCP specification" \
    "raw/books-external/meta/mcp-spec" \
    "https://modelcontextprotocol.io/" \
    "--level=2 --domains=modelcontextprotocol.io"

# agentskills.io
scrape "agentskills.io" \
    "raw/books-external/meta/agentskills-io" \
    "https://agentskills.io/" \
    "--level=2 --domains=agentskills.io"

# ========================================================================
# SUMMARY
# ========================================================================

echo "" | tee -a "$LOG"
echo "=== SCRAPE COMPLETE ===" | tee -a "$LOG"
echo "" | tee -a "$LOG"

total_html=$(find raw/books-external -name "*.html" -o -name "*.htm" 2>/dev/null | wc -l)
total_size=$(du -sh raw/books-external 2>/dev/null | cut -f1)

echo "Total HTML files: $total_html" | tee -a "$LOG"
echo "Total size: $total_size" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "Next: bash tools/convert/run_all.sh" | tee -a "$LOG"
echo "  (это конвертит все HTML в Markdown через pandoc)" | tee -a "$LOG"
