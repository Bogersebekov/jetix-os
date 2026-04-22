#!/usr/bin/env bash
# Acquire FREE direct-URL materials for ROY Information Diet
# Usage: bash tools/acquire/01-free-direct-urls.sh
# Run from repo root. Downloads ~30 PDFs/HTMLs directly to raw/books-external/ + raw/articles/
#
# Strategy:
# - curl/wget for direct-URL PDFs (Ashby, Shape Up, Naval, Buffett, etc.)
# - Skip interactive sites (Paul Graham, SEP, etc.) — handled by 02-chrome-playbook
# - Skip paid (Amazon, O'Reilly) — handled by 03-paid-sources-guide
#
# If a download fails (404 / dead link / paywall redirect) — script continues, logs error.

set -u  # fail on undefined vars
LOG="tools/acquire/download-log-$(date +%Y%m%d-%H%M%S).txt"
echo "Download log: $LOG"
echo "=== ROY Information Diet — FREE acquisition run $(date) ===" > "$LOG"

# Helper function
dl() {
    local url="$1"
    local dest="$2"
    local name
    name="$(basename "$dest")"
    if [ -f "$dest" ]; then
        echo "⏭️  SKIP (exists): $name" | tee -a "$LOG"
        return 0
    fi
    echo "⬇️  $name  <  $url" | tee -a "$LOG"
    if curl -fsSL -A "Mozilla/5.0" --max-time 60 -o "$dest" "$url"; then
        local size
        size=$(stat -c%s "$dest" 2>/dev/null || stat -f%z "$dest" 2>/dev/null || echo "?")
        echo "   ✅ OK ($size bytes)" | tee -a "$LOG"
    else
        echo "   ❌ FAIL ($?)" | tee -a "$LOG"
        rm -f "$dest"
    fi
}

# --- §3.3 UNIX PHILOSOPHY ---
# Art of Unix Programming (Eric Raymond) — HTML full book
dl "http://www.catb.org/~esr/writings/taoup/html/index.html" "raw/books-external/unix/art-of-unix-programming-raymond-TOC.html"

# --- §3.5 PROJECT MANAGEMENT ---
# Shape Up (Basecamp) — FULL BOOK PDF
dl "https://basecamp.com/assets/books/shape-up.pdf" "raw/books-external/pm/shape-up-basecamp-2019.pdf"
# Scrum Guide 2020
dl "https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf" "raw/books-external/pm/scrum-guide-2020.pdf"

# --- §3.9 CYBERNETICS ---
# Ashby Introduction to Cybernetics (1956) — FREE full PDF
dl "http://pcp.vub.ac.be/books/IntroCyb.pdf" "raw/books-external/cybernetics/ashby-introduction-to-cybernetics-1956.pdf"

# --- §3.11 INVESTING ---
# Warren Buffett shareholder letters 1977-2024 (index page, then sub-files manually via chrome)
dl "https://www.berkshirehathaway.com/letters/letters.html" "raw/books-external/investing/buffett-letters-INDEX.html"

# --- §3.14 PHILOSOPHICAL STRATEGIC ---
# Naval Almanack PDF
dl "https://www.navalmanack.com/almanack-of-naval-ravikant/the-almanack-of-naval-ravikant.pdf" "raw/books-external/philosophy/naval-almanack-2020.pdf"
# Meditations (MIT Classics — Casaubon translation)
dl "http://classics.mit.edu/Antoninus/meditations.html" "raw/books-external/philosophy/marcus-aurelius-meditations-MIT.html"
# Tao Te Ching (Legge translation, Project Gutenberg txt)
dl "https://www.gutenberg.org/files/216/216-0.txt" "raw/books-external/philosophy/tao-te-ching-legge.txt"
# Sun Tzu Art of War (Giles translation, Gutenberg)
dl "https://www.gutenberg.org/files/132/132-0.txt" "raw/books-external/philosophy/sun-tzu-art-of-war-giles.txt"
# Seneca Letters (Gutenberg)
dl "https://www.gutenberg.org/files/3794/3794-0.txt" "raw/books-external/philosophy/seneca-letters-from-a-stoic.txt"
# Epictetus Discourses + Enchiridion (Gutenberg combined)
dl "https://www.gutenberg.org/cache/epub/45109/pg45109.txt" "raw/books-external/philosophy/epictetus-discourses-and-enchiridion.txt"

# --- §3.16 ENGINEERING FOUNDATIONS ---
# Descartes Discourse on the Method (Gutenberg)
dl "https://www.gutenberg.org/files/59/59-0.txt" "raw/books-external/engineering-foundations/descartes-discourse-on-the-method.txt"

# --- §3.17 AGENT / AI primary sources (arXiv papers) ---
# Kim et al. — multi-agent scaling (2512.08296)
dl "https://arxiv.org/pdf/2512.08296" "raw/articles/arxiv-2512.08296-kim-multi-agent-scaling.pdf"
# Cemri et al. — MAST 14 failure modes (2503.13657)
dl "https://arxiv.org/pdf/2503.13657" "raw/articles/arxiv-2503.13657-cemri-mast-failure-modes.pdf"
# Qian et al. — scaling laws (2406.07155)
dl "https://arxiv.org/pdf/2406.07155" "raw/articles/arxiv-2406.07155-qian-scaling-laws.pdf"

# --- Anthropic engineering canonical posts ---
dl "https://www.anthropic.com/research/building-effective-agents" "raw/articles/anthropic-building-effective-agents-2024-12.html"
dl "https://www.anthropic.com/engineering/built-multi-agent-research-system" "raw/articles/anthropic-multi-agent-research-system-2025-06.html"
dl "https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic" "raw/articles/anthropic-ai-transforming-work-2025-12.html"

# --- Karpathy ---
# LLM Wiki Gist (raw file)
dl "https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw" "raw/articles/karpathy-llm-wiki-gist-2026-04.md"
# Year in Review 2025 (bearblog)
dl "https://karpathy.bearblog.dev/year-in-review-2025/" "raw/articles/karpathy-year-in-review-2025.html"

# --- Walden Yan (Cognition) ---
dl "https://cognition.ai/blog/dont-build-multi-agents" "raw/articles/cognition-walden-yan-dont-build-multi-agents.html"

# --- Aider blog (Paul Gauthier) - landing ---
dl "https://aider.chat/" "raw/articles/aider-chat-landing.html"

# --- Out of Control (Kevin Kelly) — full book online ---
dl "https://kk.org/outofcontrol/contents.php" "raw/books-external/cybernetics/kelly-out-of-control-TOC.html"

# --- Agile Manifesto ---
dl "https://agilemanifesto.org/" "raw/articles/agile-manifesto-2001.html"

echo ""
echo "=== DONE. See $LOG for full results. ==="
echo "Check: ls raw/books-external/ raw/articles/"
echo ""
echo "NEXT STEPS:"
echo "  1. Review download log for FAILs — some URLs may have changed"
echo "  2. Run tools/acquire/02-chrome-playbook.md via Claude for Chrome"
echo "  3. Use tools/acquire/03-paid-sources-guide.md for PAID books"
echo "  4. Commit: git add raw/ && git commit -m '[raw] acquisition Wave 1 FREE direct-URL'"
