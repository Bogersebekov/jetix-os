#!/usr/bin/env bash
# Scrape blogs into inbox/<subcategory>/<blog-slug>/
# Later sync_to_server.sh pushes inbox to server, where Claude Code converts.
#
# Usage: bash tools/convert/scrape_blogs.sh
# Resume: bash tools/convert/scrape_blogs.sh --resume
#
# ETA: 1-3 hours wall-clock.

set -u
RESUME=${1:-""}

REPO_ROOT=$(cd "$(dirname "$0")/../.." && pwd)
cd "$REPO_ROOT"

INBOX="inbox"
mkdir -p tools/convert/logs
LOG="tools/convert/logs/scrape-$(date +%Y%m%d-%H%M%S).log"
echo "Scrape log: $LOG"

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

    (cd "$dest" && \
        wget \
            --mirror \
            --convert-links \
            --adjust-extension \
            --no-parent \
            --restrict-file-names=windows \
            --user-agent="$UA" \
            --wait=1 --random-wait --tries=3 --timeout=30 \
            $extra \
            "$url" 2>&1 | tail -20 | tee -a "$LOG")

    local count
    count=$(find "$dest" \( -name "*.html" -o -name "*.htm" -o -name "*.txt" \) 2>/dev/null | wc -l)
    echo "✅ $name: $count files" | tee -a "$LOG"
}

# ========================================================================
# BLOGS — scrape to inbox/<subcategory>/<blog-slug>/
# ========================================================================

# §philosophy
scrape "Paul Graham essays" "$INBOX/philosophy/paul-graham-essays" \
    "http://www.paulgraham.com/articles.html" \
    "--level=2 --domains=paulgraham.com"

scrape "Naval blog (nav.al)" "$INBOX/philosophy/naval-blog" \
    "https://nav.al/" \
    "--level=3 --domains=nav.al --reject=*.jpg,*.png,*.gif,*.svg,*.webp,*.woff,*.woff2"

# §philosophy-science
for entry in popper thomas-kuhn lakatos feyerabend scientific-method \
             scientific-revolutions epistemology; do
    scrape "SEP: $entry" "$INBOX/philosophy-science/sep-$entry" \
        "https://plato.stanford.edu/entries/$entry/" \
        "--level=1 --domains=plato.stanford.edu"
done

# §meta
scrape "Karpathy bearblog" "$INBOX/meta/karpathy-bearblog" \
    "https://karpathy.bearblog.dev/" \
    "--level=2 --domains=karpathy.bearblog.dev"

scrape "Karpathy main" "$INBOX/meta/karpathy-ai" \
    "https://karpathy.ai/" \
    "--level=2 --domains=karpathy.ai"

scrape "Anthropic engineering blog" "$INBOX/meta/anthropic-engineering" \
    "https://www.anthropic.com/engineering" \
    "--level=2 --domains=anthropic.com --include-directories=/engineering,/research"

scrape "Aider blog" "$INBOX/meta/aider-blog" \
    "https://aider.chat/blog/" \
    "--level=2 --domains=aider.chat"

scrape "Cognition blog" "$INBOX/meta/cognition-blog" \
    "https://cognition.ai/blog" \
    "--level=2 --domains=cognition.ai"

scrape "Farnam Street mental models" "$INBOX/meta/farnam-street" \
    "https://fs.blog/mental-models/" \
    "--level=2 --domains=fs.blog --include-directories=/mental-models,/blog"

scrape "MCP specification" "$INBOX/meta/mcp-spec" \
    "https://modelcontextprotocol.io/" \
    "--level=2 --domains=modelcontextprotocol.io"

scrape "agentskills.io" "$INBOX/meta/agentskills-io" \
    "https://agentskills.io/" \
    "--level=2 --domains=agentskills.io"

# §cybernetics
scrape "Kevin Kelly Out of Control" "$INBOX/cybernetics/kelly-out-of-control" \
    "https://kk.org/outofcontrol/contents.php" \
    "--level=2 --domains=kk.org --include-directories=/outofcontrol"

# §unix
scrape "Raymond Art of Unix Programming" "$INBOX/unix/art-of-unix-programming" \
    "http://www.catb.org/~esr/writings/taoup/html/" \
    "--level=2 --domains=catb.org --include-directories=/~esr/writings/taoup"

# §mgmt
scrape "37signals writings" "$INBOX/mgmt/37signals-writings" \
    "https://37signals.com/podcast-and-excerpts" \
    "--level=2 --domains=37signals.com"

scrape "37signals Getting Real" "$INBOX/mgmt/37signals-getting-real" \
    "https://basecamp.com/gettingreal" \
    "--level=2 --domains=basecamp.com --include-directories=/gettingreal"

# §pm
scrape "Shape Up web version" "$INBOX/pm/shape-up-web" \
    "https://basecamp.com/shapeup" \
    "--level=2 --domains=basecamp.com --include-directories=/shapeup"

# §systems
scrape "Levenchuk LiveJournal recent" "$INBOX/systems/levenchuk-lj" \
    "https://ailev.livejournal.com/" \
    "--level=1 --domains=ailev.livejournal.com --wait=2"

# ========================================================================
# SUMMARY
# ========================================================================

echo "" | tee -a "$LOG"
echo "=== SCRAPE COMPLETE ===" | tee -a "$LOG"

total_files=$(find "$INBOX" -type f -not -name "README.md" 2>/dev/null | wc -l)
total_size=$(du -sh "$INBOX" 2>/dev/null | cut -f1)

echo "Inbox: $INBOX" | tee -a "$LOG"
echo "Total files: $total_files" | tee -a "$LOG"
echo "Total size: $total_size" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "NEXT: положи PDFs в inbox/<subcategory>/ (вручную или см. inbox/README.md)" | tee -a "$LOG"
echo "      потом: bash tools/convert/sync_to_server.sh" | tee -a "$LOG"
