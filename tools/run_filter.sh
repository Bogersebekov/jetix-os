#!/bin/bash
cd ~/jetix-os
echo "=== Фильтрация ==="
python3 tools/filter.py
echo "=== Генерация отчёта ==="
python3 tools/review_report.py
TODAY=$(date +%F)
if [ -f ~/jetix-os/reports/review_${TODAY}.md ]; then
  cp ~/jetix-os/reports/review_${TODAY}.md ~/review-latest.md
fi
echo "=== ГОТОВО ==="
echo "Отчёт: ~/review-latest.md"
echo "Скачай: scp ruslan@100.99.156.28:~/review-latest.md C:\\Users\\49152\\Desktop\\review-latest.md"
