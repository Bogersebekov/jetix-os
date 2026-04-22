#!/usr/bin/env bash
# Orchestrator — runs full conversion pipeline.
# Usage: bash tools/convert/run_all.sh

set -e

cd "$(dirname "$0")/../.."  # go to repo root

PY=$(command -v python3 || command -v python)
if [ -z "$PY" ]; then
    echo "❌ Python not found"
    exit 1
fi

echo "=== Jetix Knowledge Conversion Pipeline ==="
echo "Python: $PY"
echo "Repo: $(pwd)"
echo ""

# Check dependencies
echo "Checking dependencies..."
$PY -c "import docling" 2>/dev/null && echo "  ✅ docling" || { echo "  ❌ docling missing. Run: bash tools/convert/install.sh"; exit 1; }
$PY -c "import pymupdf4llm" 2>/dev/null && echo "  ✅ pymupdf4llm" || echo "  ⚠️  pymupdf4llm missing (optional fallback)"
$PY -c "import frontmatter" 2>/dev/null && echo "  ✅ python-frontmatter" || { echo "  ❌ frontmatter missing"; exit 1; }
command -v ocrmypdf &>/dev/null && echo "  ✅ ocrmypdf" || echo "  ⚠️  ocrmypdf missing (OCR scanned PDFs skipped)"
command -v pandoc &>/dev/null && echo "  ✅ pandoc" || echo "  ⚠️  pandoc missing (EPUB/HTML skipped)"
echo ""

# Run pipeline
$PY tools/convert/convert_all.py --resume

echo ""
echo "=== Done ==="
echo ""
echo "Review: raw/books-md/INDEX.md"
echo ""
echo "Next:"
echo "  git add raw/books-md/ tools/convert/"
echo "  git commit -m '[raw] books converted to Markdown — Waves 1-2'"
echo "  git push origin claude/jolly-margulis-915d34"
