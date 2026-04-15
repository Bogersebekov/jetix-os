#!/bin/bash
cd ~/jetix-os
echo "=== Шаг 0: Синхронизация контекста ==="
python3 tools/sync_context.py
echo "=== Шаг 1: Транскрипция ==="
python3 tools/transcribe.py
echo "=== Шаг 2: Извлечение ==="
python3 tools/extract.py
echo "=== Шаг 3: Сводка по темам ==="
python3 tools/summarize.py
echo "=== ГОТОВО (до фильтрации) ==="
echo "Сводка: ~/summary-latest.md"
echo "Скачай: scp ruslan@100.99.156.28:~/summary-latest.md C:\\Users\\49152\\Desktop\\summary-latest.md"
echo ""
echo "После ревью запусти:  bash ~/jetix-os/tools/run_filter.sh"
