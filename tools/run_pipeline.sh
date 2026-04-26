#!/bin/bash
cd ~/jetix-os
echo "=== Шаг 0: Синхронизация контекста ==="
python3 tools/sync_context.py
echo "=== Шаг 1: Транскрипция ==="
python3 tools/transcribe.py
echo "=== Шаг 2: Извлечение ==="
python3 tools/extract.py
echo "=== Шаг 2b: CRM voice routing (DRAFT-only) ==="
# Idempotent + graceful: only routes if extract.py emits a items file
# at expected path. Each item with target:crm becomes -DRAFT.md (never
# auto-overwrites prod CRM records). Safe to re-run.
if [ -f inbox/processed/extract-items-latest.yaml ]; then
    python3 -m crm._scripts.crm voice-route inbox/processed/extract-items-latest.yaml || \
        echo "  (warning: voice-route returned non-zero — check output, drafts may still have been created)"
else
    echo "  (skip: no inbox/processed/extract-items-latest.yaml — extract.py did not emit CRM items)"
fi
echo "=== Шаг 3: Сводка по темам ==="
python3 tools/summarize.py
echo "=== ГОТОВО (до фильтрации) ==="
echo "Сводка: ~/summary-latest.md"
echo "Скачай: scp ruslan@100.99.156.28:~/summary-latest.md C:\\Users\\49152\\Desktop\\summary-latest.md"
echo ""
echo "После ревью запусти:  bash ~/jetix-os/tools/run_filter.sh"
