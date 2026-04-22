#!/usr/bin/env bash
# One-time setup: install Python dependencies for conversion pipeline.
# Run: bash tools/convert/install.sh

set -e

echo "=== Installing conversion tools ==="

# Check Python
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "❌ Python not found. Install Python 3.10+ first: https://www.python.org/downloads/"
    exit 1
fi

PY=$(command -v python3 || command -v python)
echo "Using Python: $PY"

# Install tools
echo ""
echo "Installing docling (IBM enterprise-grade PDF → MD)..."
$PY -m pip install --upgrade docling

echo ""
echo "Installing pymupdf4llm (fast PDF → MD fallback)..."
$PY -m pip install --upgrade pymupdf4llm

echo ""
echo "Installing ocrmypdf (OCR for scanned PDFs)..."
$PY -m pip install --upgrade ocrmypdf

echo ""
echo "Installing python-frontmatter (YAML metadata)..."
$PY -m pip install --upgrade python-frontmatter

echo ""
echo "Installing tqdm (progress bars)..."
$PY -m pip install --upgrade tqdm

# Check pandoc
echo ""
if command -v pandoc &> /dev/null; then
    echo "✅ pandoc already installed"
else
    echo "⚠️  pandoc not installed. EPUB conversion will be skipped."
    echo "   Install manually: https://pandoc.org/installing.html"
    echo "   (Windows: download .msi installer, run it)"
fi

# Check tesseract (OCR backend for ocrmypdf)
echo ""
if command -v tesseract &> /dev/null; then
    echo "✅ tesseract already installed"
else
    echo "⚠️  tesseract not installed. OCR will fail on scanned PDFs."
    echo "   Install: https://github.com/UB-Mannheim/tesseract/wiki"
    echo "   (Windows: run installer, add to PATH)"
fi

echo ""
echo "=== Install done ==="
echo ""
echo "Verify:"
echo "  python -c 'import docling; print(docling.__version__)'"
echo "  ocrmypdf --version"
echo "  pandoc --version  (optional, for EPUB)"
echo ""
echo "Next: bash tools/convert/run_all.sh"
