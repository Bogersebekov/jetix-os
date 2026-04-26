#!/usr/bin/env python3
"""Filter & meta-analyze extracted items via Claude.

Backend: CC headless by default (Max sub, no API key). Set JETIX_LLM_BACKEND=api
to use anthropic SDK directly. See tools/lib/cc_helper.py.

Fault-tolerance (added cycle 11):
  • Each successful batch is written immediately to a partial file
    `OUT_DIR/.partials/batch_<date>_partial_NN.json` BEFORE moving to the next.
  • If the run is interrupted (kill, crash, hit rate-limit, hard cap), reruns
    SKIP batches whose partial file already exists, picking up where they left off.
  • At end-of-run, all partials for `today` are merged into the final
    `OUT_DIR/batch_<today>.json` and the .partials/ folder for that day cleaned.
  • `--resume` (default behavior) is implicit; pass `--restart` to ignore
    existing partials and recompute from scratch.
"""

import os
import sys
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

# Add tools/ to sys.path so `from lib.cc_helper import …` works regardless of cwd.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.cc_helper import claude_call, backend_info  # noqa: E402

HOME = Path.home()
EXTRACTIONS = HOME / "jetix-os" / "inbox" / "processed" / "extractions"
OUT_DIR = HOME / "jetix-os" / "inbox" / "processed" / "filtered"
PARTIALS_DIR = OUT_DIR / ".partials"
CONTEXT_FILE = HOME / "jetix-os" / "config" / "context.md"
MODEL = "claude-opus-4-7"

BATCH_SIZE = 50
THRESHOLD = 100


def load_context() -> str:
    try:
        return CONTEXT_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""


SYSTEM_PROMPT = """Ты — мета-аналитик персональной базы знаний Jetix OS.
Тебе дан массив извлечённых единиц (items) из множества голосовых заметок.
Твоя задача — провести второй проход над всем массивом:

а) Удали дубли и объедини очень похожие единицы (сохрани источники в поле sources).
б) Найди связи и противоречия между единицами.
в) Уточни horizon (now/backlog) в контексте ВСЕХ заметок — если что-то упоминается многократно или имеет дедлайн, поднимай приоритет.
г) Сгруппируй единицы по проектам (поле project).
д) Добавь секцию meta_analysis: ключевые темы, противоречия, паттерны.

Верни СТРОГО валидный JSON без markdown:
{
  "items": [
    {
      "category": "<одна из 12 категорий>",
      "content": "<суть>",
      "priority": "high|medium|low",
      "project": "<проект или null>",
      "actionable": true|false,
      "horizon": "now|backlog",
      "delegate": "<кому или null>",
      "date": "YYYY-MM-DD",
      "sources": ["<имена исходных файлов>"],
      "duplicate_flag": true|false
    }
  ],
  "groups_by_project": {
    "<project_name>": [<индексы items>]
  },
  "meta_analysis": {
    "key_themes": ["..."],
    "contradictions": ["..."],
    "patterns": ["..."],
    "key_findings": ["..."]
  }
}

Правила:
- Пиши на русском.
- Не выдумывай содержание — работай только с данным входом.
- **Сохраняй ВСЕ уникальные мысли.** Сливай ТОЛЬКО если две единицы говорят БУКВАЛЬНО одно и то же.
- Если есть сомнения — сохраняй обе. Лучше оставить дубликат, чем потерять уникальную мысль.
- На выходе обычно почти столько же единиц, сколько на входе (снижение только за счёт явных дублей).
- Категории те же 12: Видение, Решения, Инсайты, Стратегические гипотезы, Задачи,
  Идеи для проектов, Идеи, Открытые вопросы, Контакты, Ресурсы, Личные наблюдения, Принципы.
- Используй ТОЛЬКО названия проектов из раздела 'Активные/Замороженные проекты' контекста.
- Поле duplicate_flag=true если единица дублирует принятое решение из контекста
  или информацию из 'Что уже обработано ранее'. Иначе false.
- При мета-анализе учитывай текущие приоритеты из контекста
  (Быстрые деньги = P1, AI-инструменты = P2 и т.д.) и уже принятые решения.
"""


def extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
        raise


# ─── Partial-save helpers ────────────────────────────────────────────────────


def _partial_path(today: str, batch_idx: int) -> Path:
    """Path for the Nth batch's partial file. Stable + deterministic.

    Includes BATCH_SIZE in the filename so changes to BATCH_SIZE don't cause
    silent partial reuse against a different chunking scheme.
    """
    return PARTIALS_DIR / f"batch_{today}_bsz{BATCH_SIZE}_partial_{batch_idx:03d}.json"


def _load_partial(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _save_partial(p: Path, payload: dict):
    PARTIALS_DIR.mkdir(parents=True, exist_ok=True)
    # write to .tmp then rename → atomic on POSIX
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, p)


def _cleanup_partials_for(today: str) -> int:
    if not PARTIALS_DIR.exists():
        return 0
    n = 0
    for p in PARTIALS_DIR.glob(f"batch_{today}_*_partial_*.json"):
        try:
            p.unlink()
            n += 1
        except OSError:
            pass
    # remove dir if now empty
    try:
        if not any(PARTIALS_DIR.iterdir()):
            PARTIALS_DIR.rmdir()
    except OSError:
        pass
    return n


def main():
    print(f"[filter] {backend_info()}")

    restart = "--restart" in sys.argv[1:]
    if restart:
        n = _cleanup_partials_for(datetime.now().strftime("%Y-%m-%d"))
        if n:
            print(f"[filter] --restart: removed {n} existing partial(s) for today")

    if not EXTRACTIONS.exists():
        print(f"ERROR: нет папки {EXTRACTIONS}", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(EXTRACTIONS.glob("*.json"))
    if not files:
        print(f"Нет extraction-файлов в {EXTRACTIONS}")
        return

    all_items = []
    per_file = []
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[WARN] не читается {f.name}: {e}", file=sys.stderr)
            continue
        source = data.get("source", f.name)
        items = data.get("items", []) or []
        for it in items:
            it = dict(it)
            it.setdefault("sources", [source])
            all_items.append(it)
        per_file.append((f.name, len(items)))

    if not all_items:
        print("Нет единиц для фильтрации.")
        return

    print(f"Входные файлы: {len(per_file)}, единиц всего: {len(all_items)}")

    context_md = load_context()
    system_prompt = SYSTEM_PROMPT
    if context_md:
        system_prompt = (
            "===== КОНТЕКСТ ПРОЕКТА =====\n"
            f"{context_md}\n"
            "===== /КОНТЕКСТ =====\n\n"
            + SYSTEM_PROMPT
        )

    today = datetime.now().strftime("%Y-%m-%d")

    def call_model(batch):
        user_msg = (
            f"Массив единиц ({len(batch)} шт.):\n\n"
            f"{json.dumps(batch, ensure_ascii=False, indent=2)}\n\n"
            f"Проведи мета-анализ и верни JSON по схеме."
        )
        try:
            raw = claude_call(system=system_prompt, user=user_msg, model=MODEL, expect_json=True)
        except Exception as e:
            fname = f"raw_error_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.txt"
            (OUT_DIR / fname).write_text(f"call failed: {e}", encoding="utf-8")
            return None, f"{e} (note -> {fname})"
        try:
            return extract_json(raw), None
        except Exception as e:
            fname = f"raw_error_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.txt"
            (OUT_DIR / fname).write_text(raw, encoding="utf-8")
            return None, f"{e} (raw -> {fname})"

    # ─── Batched path with partial-save ──────────────────────────────────────

    def run_batched():
        merged_items = []
        meta_accum = {"key_themes": [], "contradictions": [], "patterns": [], "key_findings": []}
        groups_accum = {}

        total_batches = (len(all_items) + BATCH_SIZE - 1) // BATCH_SIZE
        resumed = 0
        computed = 0
        failed = 0

        for bi in range(total_batches):
            batch_idx = bi + 1
            i = bi * BATCH_SIZE
            batch = all_items[i:i + BATCH_SIZE]
            ppath = _partial_path(today, batch_idx)

            existing = _load_partial(ppath)
            if existing is not None:
                print(f"  batch {batch_idx}/{total_batches}: RESUME (partial exists, "
                      f"{len(existing.get('items', []))} items)")
                resumed += 1
                merged_items.extend(existing.get("items") or [])
                for k in meta_accum:
                    meta_accum[k].extend((existing.get("meta_analysis") or {}).get(k, []) or [])
                for pname, idxs in (existing.get("groups_by_project") or {}).items():
                    groups_accum.setdefault(pname, []).append({"batch": batch_idx, "indices": idxs})
                continue

            print(f"  batch {batch_idx}/{total_batches}: {len(batch)} items → calling model...")
            data_b, err = call_model(batch)
            if err:
                print(f"  ERROR в батче {batch_idx}: {err}", file=sys.stderr)
                failed += 1
                continue

            payload = {
                "batch_idx": batch_idx,
                "batch_size_target": BATCH_SIZE,
                "input_count": len(batch),
                "model": MODEL,
                "generated_at": datetime.now().isoformat(timespec="seconds"),
                "items": data_b.get("items", []) or [],
                "meta_analysis": data_b.get("meta_analysis") or {},
                "groups_by_project": data_b.get("groups_by_project") or {},
            }
            try:
                _save_partial(ppath, payload)
                print(f"    [partial-save] {ppath.name} ({len(payload['items'])} items)")
            except Exception as e:
                print(f"    [partial-save] WARNING: failed to write {ppath.name}: {e}",
                      file=sys.stderr)

            computed += 1
            merged_items.extend(payload["items"])
            for k in meta_accum:
                meta_accum[k].extend((payload.get("meta_analysis") or {}).get(k, []) or [])
            for pname, idxs in (payload.get("groups_by_project") or {}).items():
                groups_accum.setdefault(pname, []).append({"batch": batch_idx, "indices": idxs})

        print(f"\n[partial-save summary] resumed={resumed}, computed={computed}, "
              f"failed={failed}, total_batches={total_batches}")

        if not merged_items:
            print("ERROR: ни один батч не дал результата.", file=sys.stderr)
            sys.exit(3)

        return {
            "items": merged_items,
            "groups_by_project": groups_accum,
            "meta_analysis": meta_accum,
        }

    if len(all_items) > THRESHOLD:
        print(f"Единиц > {THRESHOLD} — обрабатываю батчами по {BATCH_SIZE} с partial-save.")
        data = run_batched()
    else:
        # small-corpus path: single call, no partials needed
        data, err = call_model(all_items)
        if err:
            print(f"ERROR: {err}", file=sys.stderr)
            sys.exit(3)

    out_path = OUT_DIR / f"batch_{today}.json"
    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "input_files": [n for n, _ in per_file],
        "input_items_count": len(all_items),
        "output_items_count": len(data.get("items", [])),
        **data,
    }
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    # Successful merge → clean up today's partials.
    n_clean = _cleanup_partials_for(today)
    if n_clean:
        print(f"[partial-save] cleaned {n_clean} partial(s) after successful merge")

    print("\n===== ОТЧЁТ =====")
    print(f"На входе единиц: {len(all_items)}")
    print(f"На выходе единиц: {len(data.get('items', []))}")
    print(f"Сохранено: {out_path}")
    meta = data.get("meta_analysis", {}) or {}
    if meta.get("key_themes"):
        print("Ключевые темы:")
        for t in meta["key_themes"]:
            print(f"  • {t}")
    if meta.get("contradictions"):
        print("Противоречия:")
        for c in meta["contradictions"]:
            print(f"  • {c}")
    if meta.get("patterns"):
        print("Паттерны:")
        for p in meta["patterns"]:
            print(f"  • {p}")
    if meta.get("key_findings"):
        print("Ключевые находки:")
        for k in meta["key_findings"]:
            print(f"  • {k}")


if __name__ == "__main__":
    main()
