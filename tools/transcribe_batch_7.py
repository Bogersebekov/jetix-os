#!/usr/bin/env python3
"""One-off transcription for voice batch-7 (9 audio files in-place).

Reads from raw/voice-memos-2026-05-19-batch/ + raw/voice-memos-2026-05-20-batch/
Writes to raw/voice-transcripts/<stem>.txt with batch-7 header.
Does NOT move/archive originals (in-place processing).

Per Phase 1 spec voice-batch-7-deep-analysis-2026-05-20.md.
Ruslan acked GROQ_API_KEY use for this canonical voice pipeline batch (cost <€0.20).
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from groq import Groq

ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS = ROOT / "raw" / "voice-transcripts"
MODEL = "whisper-large-v3"
LANGUAGE = "ru"
BATCH = "voice-batch-7-2026-05-20"

AUDIO_FILES = [
    ROOT / "raw/voice-memos-2026-05-19-batch/audio_680@18-05-2026_02-42-57.ogg",
    ROOT / "raw/voice-memos-2026-05-19-batch/audio_681@18-05-2026_06-04-03.ogg",
    ROOT / "raw/voice-memos-2026-05-19-batch/audio_688@19-05-2026_01-43-13.ogg",
    ROOT / "raw/voice-memos-2026-05-19-batch/audio_692@19-05-2026_04-49-13.ogg",
    ROOT / "raw/voice-memos-2026-05-19-batch/audio_693@19-05-2026_05-35-29.ogg",
    ROOT / "raw/voice-memos-2026-05-20-batch/audio_697@20-05-2026_11-18-43.ogg",
    ROOT / "raw/voice-memos-2026-05-20-batch/audio_698@20-05-2026_11-34-20.ogg",
    ROOT / "raw/voice-memos-2026-05-20-batch/audio_699@20-05-2026_12-25-19.ogg",
    ROOT / "raw/voice-memos-2026-05-20-batch/audio_700@20-05-2026_12-41-50.ogg",
]


def get_duration(path: Path):
    try:
        from mutagen import File as MutagenFile
        f = MutagenFile(str(path))
        if f is not None and f.info is not None:
            return float(f.info.length)
    except Exception:
        pass
    return None


def format_duration(seconds):
    if seconds is None:
        return "неизвестно"
    m, s = divmod(int(seconds), 60)
    return f"{m}:{s:02d}"


def transcribe_file(client: Groq, audio_path: Path) -> str:
    with audio_path.open("rb") as f:
        result = client.audio.transcriptions.create(
            file=(audio_path.name, f.read()),
            model=MODEL,
            language=LANGUAGE,
            response_format="text",
        )
    return result if isinstance(result, str) else getattr(result, "text", str(result))


def main():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("ERROR: GROQ_API_KEY не задан", file=sys.stderr)
        sys.exit(1)

    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    client = Groq(api_key=api_key)
    processed, skipped, failed = [], [], []

    for audio in AUDIO_FILES:
        if not audio.exists():
            print(f"[MISS] {audio.name} — нет файла", file=sys.stderr)
            failed.append((audio.name, "missing"))
            continue
        txt_path = TRANSCRIPTS / (audio.stem + ".txt")
        if txt_path.exists():
            print(f"[SKIP] {audio.name} — транскрипт уже существует")
            skipped.append(audio.name)
            continue
        print(f"[...]  {audio.name}")
        try:
            text = transcribe_file(client, audio)
            duration = get_duration(audio)
            header = (
                f"# Источник: {audio.name}\n"
                f"# Обработано: {datetime.now().isoformat(timespec='seconds')}\n"
                f"# Длительность: {format_duration(duration)}\n"
                f"# Модель: {MODEL} (lang={LANGUAGE})\n"
                f"# Batch: {BATCH}\n"
                f"\n"
            )
            txt_path.write_text(header + text.strip() + "\n", encoding="utf-8")
            print(f"[OK]   {audio.name} -> {txt_path.name} ({len(text)} chars)")
            processed.append((audio.name, txt_path.name, len(text)))
        except Exception as e:
            print(f"[FAIL] {audio.name}: {e}", file=sys.stderr)
            failed.append((audio.name, str(e)))

    print("\n===== ОТЧЁТ batch-7 =====")
    print(f"Обработано: {len(processed)}")
    for n, t, chars in processed:
        print(f"  • {n} -> {t} ({chars} chars)")
    if skipped:
        print(f"Пропущено: {len(skipped)}")
    if failed:
        print(f"Ошибок: {len(failed)}")
        for n, err in failed:
            print(f"  • {n}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
