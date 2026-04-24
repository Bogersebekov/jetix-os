#!/usr/bin/env bash
# swarm/lib/hooks/parse-frontmatter-field.sh
# Extract a single-line scalar field from a markdown file's YAML frontmatter.
# Usage: parse-frontmatter-field.sh <file> <field-name>
# Emits the value to stdout (empty string if field absent or multi-line).
# Reference: OPP-02 §3.2 lines 232-238 (Fowler Extract Function). Pure Bash.
set -euo pipefail
if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <file> <field-name>" >&2
  exit 2
fi
file="$1"
field="$2"
[[ -f "$file" ]] || { echo "" ; exit 0; }
# Walk only the region between the first two `---` markers; match `^<field>:`
awk -v fld="$field" '
  /^---$/ { n++; if (n >= 2) exit; next }
  n == 1 {
    # match "<field>:" (single-line scalar only); capture value after first colon
    if (match($0, "^" fld ":[ \t]*")) {
      v = substr($0, RSTART + RLENGTH)
      # strip trailing inline comment (after whitespace + #)
      sub(/[ \t]+#.*$/, "", v)
      # strip trailing whitespace
      sub(/[ \t]+$/, "", v)
      # strip a surrounding double-quote pair (single-line YAML scalar)
      sub(/^"/, "", v)
      sub(/"$/, "", v)
      print v
      exit
    }
  }
' "$file"
exit 0
