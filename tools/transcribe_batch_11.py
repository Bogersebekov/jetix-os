#!/usr/bin/env python3
"""One-shot transcribe для voice batch-11 (7 audio в raw/voice-memos-2026-05-22-batch-2/).
Output → raw/voice-transcripts/ matching past batches pattern.
Audio files PRESERVED in place (no archive move)."""

import os
import sys
from pathlib import Path
from datetime import datetime

from groq import Groq

ROOT = Path("/home/ruslan/jetix-os")
SRC = ROOT / "raw" / "voice-memos-2026-05-22-batch-2"
DST = ROOT / "raw" / "voice-transcripts"
MODEL = "whisper-large-v3"
LANG = "ru"

FILES = [
    "audio_722@22-05-2026_16-50-02.ogg",
    "audio_723@22-05-2026_16-52-33.ogg",
    "audio_724@22-05-2026_16-55-38.ogg",
    "audio_725@22-05-2026_17-04-41.ogg",
    "audio_726@22-05-2026_17-23-31.ogg",
    "audio_727@22-05-2026_17-32-29.ogg",
    "audio_728@22-05-2026_17-40-59.ogg",
]


def get_duration(path):
    try:
        from mutagen import File as MF
        f = MF(str(path))
        if f and f.info:
            return float(f.info.length)
    except Exception:
        pass
    return None


def fmt(s):
    if s is None:
        return "неизвестно"
    m, sec = divmod(int(s), 60)
    return f"{m}:{sec:02d}"


def main():
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        print("ERROR: GROQ_API_KEY не задан", file=sys.stderr)
        sys.exit(1)
    DST.mkdir(parents=True, exist_ok=True)
    client = Groq(api_key=key)
    done, skipped, failed = [], [], []
    for name in FILES:
        src = SRC / name
        if not src.exists():
            print(f"[MISS] {name}", file=sys.stderr)
            failed.append((name, "file-missing"))
            continue
        txt_path = DST / (src.stem + ".txt")
        if txt_path.exists():
            print(f"[SKIP] {name}")
            skipped.append(name)
            continue
        print(f"[...]  {name} — транскрибирую...")
        try:
            with src.open("rb") as f:
                result = client.audio.transcriptions.create(
                    file=(src.name, f.read()),
                    model=MODEL,
                    language=LANG,
                    response_format="text",
                )
            text = result if isinstance(result, str) else getattr(result, "text", str(result))
            dur = get_duration(src)
            header = (
                f"# Источник: {src.name}\n"
                f"# Обработано: {datetime.now().isoformat(timespec='seconds')}\n"
                f"# Длительность: {fmt(dur)}\n"
                f"# Модель: {MODEL} (lang={LANG})\n"
                f"\n"
            )
            txt_path.write_text(header + text.strip() + "\n", encoding="utf-8")
            print(f"[OK]   {name} -> {txt_path.name} ({fmt(dur)})")
            done.append(name)
        except Exception as e:
            print(f"[FAIL] {name}: {e}", file=sys.stderr)
            failed.append((name, str(e)))
    print("\n===== ОТЧЁТ =====")
    print(f"Обработано: {len(done)} / Пропущено: {len(skipped)} / Ошибок: {len(failed)}")
    if failed:
        for n, e in failed:
            print(f"  FAIL {n}: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
