#!/usr/bin/env python3
"""Transcribe voice memos from inbox/voice/ using Groq Whisper API."""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime

try:
    from groq import Groq
except ImportError:
    print("ERROR: Groq SDK не установлен. Установи: pip install groq", file=sys.stderr)
    sys.exit(1)

HOME = Path.home()
INBOX = HOME / "jetix-os" / "inbox" / "voice"
TRANSCRIPTS = HOME / "jetix-os" / "raw" / "transcripts"
ARCHIVE = HOME / "jetix-os" / "raw" / "voice-memos"

AUDIO_EXTS = {".ogg", ".mp3", ".m4a", ".wav", ".webm"}
MODEL = "whisper-large-v3"
LANGUAGE = "ru"


def get_duration(path: Path):
    """Try to get audio duration in seconds using mutagen (optional)."""
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
        print("ERROR: переменная окружения GROQ_API_KEY не задана.", file=sys.stderr)
        sys.exit(1)

    INBOX.mkdir(parents=True, exist_ok=True)
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    ARCHIVE.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in INBOX.iterdir() if p.is_file() and p.suffix.lower() in AUDIO_EXTS])
    if not files:
        print(f"Нет аудиофайлов в {INBOX}")
        return

    client = Groq(api_key=api_key)

    processed, skipped, failed = [], [], []

    for audio in files:
        txt_path = TRANSCRIPTS / (audio.stem + ".txt")
        if txt_path.exists():
            print(f"[SKIP] {audio.name} — транскрипт уже существует")
            skipped.append(audio.name)
            continue

        print(f"[...]  {audio.name} — транскрибирую...")
        try:
            text = transcribe_file(client, audio)
            duration = get_duration(audio)
            header = (
                f"# Источник: {audio.name}\n"
                f"# Обработано: {datetime.now().isoformat(timespec='seconds')}\n"
                f"# Длительность: {format_duration(duration)}\n"
                f"# Модель: {MODEL} (lang={LANGUAGE})\n"
                f"\n"
            )
            txt_path.write_text(header + text.strip() + "\n", encoding="utf-8")

            dest = ARCHIVE / audio.name
            if dest.exists():
                dest = ARCHIVE / f"{audio.stem}_{int(datetime.now().timestamp())}{audio.suffix}"
            shutil.move(str(audio), str(dest))

            print(f"[OK]   {audio.name} -> {txt_path.name}")
            processed.append((audio.name, txt_path.name, dest.name))
        except Exception as e:
            print(f"[FAIL] {audio.name}: {e}", file=sys.stderr)
            failed.append((audio.name, str(e)))

    print("\n===== ОТЧЁТ =====")
    print(f"Обработано: {len(processed)}")
    for src, txt, arch in processed:
        print(f"  • {src}")
        print(f"      транскрипт: {TRANSCRIPTS / txt}")
        print(f"      архив:      {ARCHIVE / arch}")
    if skipped:
        print(f"Пропущено (уже есть): {len(skipped)}")
        for n in skipped:
            print(f"  • {n}")
    if failed:
        print(f"Ошибок: {len(failed)}")
        for n, err in failed:
            print(f"  • {n}: {err}")


if __name__ == "__main__":
    main()
