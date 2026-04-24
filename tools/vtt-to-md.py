#!/usr/bin/env python3
"""tools/vtt-to-md.py — Convert WebVTT subtitle file to clean markdown transcript.
Usage: python3 tools/vtt-to-md.py <input.vtt> [output.md]
Output: markdown with speaker blocks and timestamps stripped to 1-minute granularity.
"""
import re
import sys
from pathlib import Path


def parse_vtt(vtt_text: str) -> list[str]:
    """Extract cue text blocks from WebVTT, stripping timestamps and tags."""
    cues = []
    lines = vtt_text.splitlines()
    in_cue = False
    buf = []
    for line in lines:
        if re.match(r'^\d{2}:\d{2}', line) or re.match(r'^\d+:\d{2}', line):
            if buf:
                cues.append(' '.join(buf).strip())
                buf = []
            in_cue = True
            continue
        if in_cue and line.strip() == '':
            if buf:
                cues.append(' '.join(buf).strip())
                buf = []
            in_cue = False
            continue
        if in_cue and line.strip() and not line.startswith('WEBVTT'):
            cleaned = re.sub(r'<[^>]+>', '', line).strip()
            if cleaned:
                buf.append(cleaned)
    if buf:
        cues.append(' '.join(buf).strip())
    return [c for c in cues if c]


def deduplicate(cues: list[str]) -> list[str]:
    """Remove consecutive duplicate cue lines (common in auto-generated VTT)."""
    result = []
    prev = None
    for c in cues:
        if c != prev:
            result.append(c)
        prev = c
    return result


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: vtt-to-md.py <input.vtt> [output.md]", file=sys.stderr)
        sys.exit(1)
    vtt_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else vtt_path.with_suffix('.md')
    cues = deduplicate(parse_vtt(vtt_path.read_text(encoding='utf-8')))
    md_lines = ['# Transcript\n', f'_Source: {vtt_path.name}_\n', '']
    md_lines += [c + ' ' for c in cues]
    out_path.write_text('\n'.join(md_lines), encoding='utf-8')
    print(f"OK: {len(cues)} cues written to {out_path}")


if __name__ == '__main__':
    main()
