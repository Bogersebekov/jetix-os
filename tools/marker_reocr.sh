#!/usr/bin/env bash
# Marker — self-hosted PDF → Markdown (fallback if Mistral OCR unavailable).
#
# Usage:
#   bash tools/marker_reocr.sh <input_dir> <output_dir>
#
# Example:
#   bash tools/marker_reocr.sh inbox/failed-books/ raw/books-md/reocr/
#
# Requirements:
#   - Python 3.10+
#   - ~4GB RAM minimum, GPU highly recommended (CUDA)
#   - First run downloads ~2GB of models
#
# Install (one-time, auto-run if marker not present):
#   pip install marker-pdf
#
# Notes:
#   - Marker is slower than Mistral OCR but free and fully offline.
#   - Use when Mistral API is down / quota exceeded / offline work needed.
#   - GPU: set TORCH_DEVICE=cuda. CPU fallback works but ~10× slower.

set -euo pipefail

INPUT="${1:-}"
OUTPUT="${2:-}"

if [[ -z "$INPUT" || -z "$OUTPUT" ]]; then
  echo "usage: $0 <input_dir> <output_dir>" >&2
  exit 2
fi

if [[ ! -d "$INPUT" ]]; then
  echo "error: input dir not found: $INPUT" >&2
  exit 2
fi

mkdir -p "$OUTPUT"

if ! command -v marker >/dev/null 2>&1; then
  echo "[setup] marker not installed — installing marker-pdf…"
  pip install --quiet marker-pdf
fi

: "${TORCH_DEVICE:=cpu}"
export TORCH_DEVICE

echo "[info] TORCH_DEVICE=$TORCH_DEVICE"
echo "[info] input : $INPUT"
echo "[info] output: $OUTPUT"
echo ""

PDFS=$(find "$INPUT" -maxdepth 2 -type f -name "*.pdf" | sort)
COUNT=$(echo "$PDFS" | grep -c . || true)
echo "[info] found $COUNT PDF(s)"
echo ""

i=0
for pdf in $PDFS; do
  i=$((i+1))
  name=$(basename "$pdf" .pdf)
  out_md="$OUTPUT/$name.md"

  if [[ -s "$out_md" ]]; then
    echo "[$i/$COUNT] skip $name (already exists)"
    continue
  fi

  echo "[$i/$COUNT] marker: $name"
  marker_single "$pdf" "$OUTPUT" --output_format markdown || {
    echo "  [warn] marker failed for $name, continuing"
    continue
  }

  # marker creates subdir <name>/<name>.md — flatten
  if [[ -f "$OUTPUT/$name/$name.md" ]]; then
    mv "$OUTPUT/$name/$name.md" "$out_md"
    [[ -d "$OUTPUT/$name" ]] && mv "$OUTPUT/$name" "$OUTPUT/$name-assets"
  fi
  echo "  [ok ] $out_md"
done

echo ""
echo "done."
