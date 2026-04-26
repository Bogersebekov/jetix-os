#!/usr/bin/env python3
"""Extract structured items from transcripts using Anthropic Claude API.

Also emits a consolidated YAML at inbox/processed/extract-items-latest.yaml
with CRM routing items (target/intent/person_name/role_hint/source_channel/
context/raw_quote) consumed by crm/_scripts/voice_router.py. The CRM YAML is
built by `build_crm_items_yaml()` from the union of:
  (a) explicit `crm_items` arrays the model emits per the updated system prompt
  (b) fallback heuristic: any item with category=="Контакты" → derived CRM item

This file can be invoked in two modes:
  • Default (no args): full pipeline — call API for new transcripts, then
    rebuild extract-items-latest.yaml.
  • `--rebuild-yaml-only`: skip API entirely, only re-aggregate existing JSON
    extractions into the YAML. Safe to run without ANTHROPIC_API_KEY (zero cost).
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime

try:
    import yaml as _yaml
except ImportError:
    _yaml = None

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None  # only required for full pipeline mode

HOME = Path.home()
TRANSCRIPTS = HOME / "jetix-os" / "raw" / "transcripts"
OUT = HOME / "jetix-os" / "inbox" / "processed" / "extractions"
CONTEXT_FILE = HOME / "jetix-os" / "config" / "context.md"
CRM_ITEMS_YAML = HOME / "jetix-os" / "inbox" / "processed" / "extract-items-latest.yaml"

MODEL = "claude-sonnet-4-20250514"


def load_context() -> str:
    try:
        return CONTEXT_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""

SYSTEM_PROMPT = """Ты — аналитик персональной базы знаний. Получаешь транскрипт голосовой заметки на русском и извлекаешь структурированные единицы по 12 категориям:

ВАЖНО: помимо `items[]`, ОПЦИОНАЛЬНО верни поле `crm_items[]` — список структурированных
CRM-routing объектов для каждого упомянутого человека/организации (целевая запись для
crm/_scripts/voice_router.py). Каждый crm_item:
{
  "target": "crm",
  "intent": "add" | "touch" | "update",
  "person_name": "<полное имя как в транскрипте>",
  "slug": "<kebab-case-slug или null если новый>",
  "role_hint": "<advisor|mentor|partner_prospect|client_lead|interesting|friend|...>" или null,
  "source_channel": "voice_memo",
  "context": "<1-2 предложения контекста — что про них сказано>",
  "raw_quote": "<точная цитата из транскрипта>"
}

Правила crm_items:
- intent="add" — новое знакомство / первое упоминание
- intent="touch" — после взаимодействия (звонок, встреча, переписка)
- intent="update" — узнал новые факты о существующем контакте
- НЕ дублируй person из обычной категории "Контакты" в crm_items — только если есть
  явный сигнал что это контакт для CRM (имя + минимальный контекст для записи).



1. Видение — долгосрочные образы желаемого будущего
2. Решения — принятые решения
3. Инсайты — озарения, новое понимание
4. Стратегические гипотезы — предположения, требующие проверки
5. Задачи — конкретные TODO (в т.ч. делегирование)
6. Идеи для проектов — замыслы инициатив/продуктов
7. Идеи — темы, направления без привязки к проекту
8. Открытые вопросы — что требует ответа/исследования
9. Контакты — упомянутые люди и контекст
10. Ресурсы — ссылки, книги, инструменты
11. Личные наблюдения — про себя, состояние, паттерны
12. Принципы — правила, которым следовать

Для каждой единицы верни объект:
{
  "category": "<одна из 12 категорий точно как выше>",
  "content": "<суть одним-двумя предложениями на русском>",
  "priority": "high" | "medium" | "low",
  "project": "<название проекта или null>",
  "actionable": true | false,
  "horizon": "now" | "backlog",
  "delegate": "<кому делегировать или null>",
  "date": "<YYYY-MM-DD дата обработки>"
}

Правила:
- Отвечай СТРОГО валидным JSON-объектом вида {"items": [...]} без markdown и комментариев.
- Если категории нет в заметке — не придумывай, просто пропусти.
- Метаданные заголовка транскрипта (# Источник, # Обработано и т.д.) игнорируй как контент.
- priority: high — важное/срочное; medium — обычное; low — фоновое.
- actionable=true только если есть конкретное действие.
- horizon=now — в ближайшие дни; backlog — отложенное.
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


def process_file(client: Anthropic, txt_path: Path, today: str, system_prompt: str) -> dict:
    content = txt_path.read_text(encoding="utf-8")
    user_msg = (
        f"Дата обработки: {today}\n"
        f"Источник: {txt_path.name}\n\n"
        f"Транскрипт:\n---\n{content}\n---\n\n"
        f"Извлеки единицы и верни JSON-объект {{\"items\": [...]}}."
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=8000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = "".join(b.text for b in resp.content if getattr(b, "type", None) == "text")
    data = extract_json(raw)
    if not isinstance(data, dict) or "items" not in data:
        raise ValueError("Ответ модели не содержит поле items")
    out = {
        "source": txt_path.name,
        "processed_at": datetime.now().isoformat(timespec="seconds"),
        "model": MODEL,
        "items": data["items"],
    }
    # Optional crm_items list (may be empty / absent on older outputs)
    if "crm_items" in data and isinstance(data["crm_items"], list):
        out["crm_items"] = data["crm_items"]
    return out


# ─── CRM YAML aggregator ─────────────────────────────────────────────────────


_NAME_RE = re.compile(
    r"^([A-ZА-ЯЁ][A-Za-zА-Яа-яёЁ-]+(?:\s+[A-ZА-ЯЁ][A-Za-zА-Яа-яёЁ-]+){0,2})"
    r"\s*[—\-:,.]"
)


def _person_from_kontakty_content(content: str) -> str | None:
    """Best-effort extract a person name from a Контакты item's content.

    Heuristic: leading capitalized 1-3 word phrase before em-dash / hyphen /
    colon / comma. Returns None if no clear name.
    """
    if not content:
        return None
    m = _NAME_RE.match(content.strip())
    if not m:
        return None
    name = m.group(1).strip()
    if len(name) < 3 or len(name.split()) > 3:
        return None
    return name


def _kontakty_to_crm_item(item: dict) -> dict | None:
    """Fallback heuristic: convert a category=Контакты item into a CRM item."""
    name = _person_from_kontakty_content(item.get("content") or "")
    if not name:
        return None
    return {
        "target": "crm",
        "intent": "add",
        "person_name": name,
        "slug": None,
        "role_hint": "interesting",
        "source_channel": "voice_memo",
        "context": item.get("content") or "",
        "raw_quote": item.get("content") or "",
        "_provenance": "fallback_kontakty",
    }


def build_crm_items_yaml(extractions_dir: Path = OUT, out_path: Path = CRM_ITEMS_YAML) -> dict:
    """Aggregate CRM items from all .json extractions into a single YAML list.

    Returns a summary dict: {total_files, with_crm_items, fallback_items, total_items}.
    """
    if _yaml is None:
        raise RuntimeError("PyYAML required for build_crm_items_yaml")
    if not extractions_dir.is_dir():
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("[]\n", encoding="utf-8")
        return {"total_files": 0, "with_crm_items": 0, "fallback_items": 0, "total_items": 0}

    all_items: list[dict] = []
    total_files = 0
    with_crm_items = 0
    fallback_count = 0

    for jf in sorted(extractions_dir.glob("*.json")):
        total_files += 1
        try:
            d = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        # explicit crm_items take priority
        explicit = d.get("crm_items") if isinstance(d, dict) else None
        if isinstance(explicit, list) and explicit:
            with_crm_items += 1
            for ci in explicit:
                ci2 = dict(ci)
                ci2.setdefault("_source_extraction", jf.name)
                all_items.append(ci2)
            continue
        # fallback: scan items[] for category=Контакты
        for item in (d.get("items") or []):
            if (item.get("category") or "") == "Контакты":
                fb = _kontakty_to_crm_item(item)
                if fb:
                    fb["_source_extraction"] = jf.name
                    all_items.append(fb)
                    fallback_count += 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        _yaml.safe_dump(all_items, allow_unicode=True, sort_keys=False, default_flow_style=False),
        encoding="utf-8",
    )
    return {
        "total_files": total_files,
        "with_crm_items": with_crm_items,
        "fallback_items": fallback_count,
        "total_items": len(all_items),
    }


def main():
    # Handle --rebuild-yaml-only mode (zero API cost — re-aggregate existing JSONs)
    if "--rebuild-yaml-only" in sys.argv[1:]:
        summary = build_crm_items_yaml()
        print(f"[rebuild-yaml-only] {CRM_ITEMS_YAML.relative_to(HOME)}")
        print(f"  total_files={summary['total_files']}, "
              f"with_crm_items={summary['with_crm_items']}, "
              f"fallback_items={summary['fallback_items']}, "
              f"total_items={summary['total_items']}")
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: переменная окружения ANTHROPIC_API_KEY не задана.", file=sys.stderr)
        sys.exit(1)
    if Anthropic is None:
        print("ERROR: anthropic SDK не установлен. Установи: pip install anthropic", file=sys.stderr)
        sys.exit(1)

    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in TRANSCRIPTS.iterdir() if p.is_file() and p.suffix.lower() == ".txt"])
    if not files:
        print(f"Нет транскриптов в {TRANSCRIPTS}")
        return

    client = Anthropic(api_key=api_key)
    today = datetime.now().strftime("%Y-%m-%d")
    context_md = load_context()
    if context_md:
        system_prompt = (
            "Контекст проекта ниже. Используй ТОЛЬКО названия проектов из контекста. "
            "Маппинг по ключевым словам — в секции 'Keyword-маппинг проектов'. "
            "Если заметка не относится ни к одному проекту — ставь project=null, "
            "не придумывай новые названия.\n\n"
            "===== КОНТЕКСТ =====\n"
            f"{context_md}\n"
            "===== /КОНТЕКСТ =====\n\n"
            + SYSTEM_PROMPT
        )
    else:
        system_prompt = SYSTEM_PROMPT

    processed, skipped, failed = [], [], []

    for txt in files:
        out_path = OUT / (txt.stem + ".json")
        if out_path.exists():
            print(f"[SKIP] {txt.name} — извлечение уже существует")
            skipped.append(txt.name)
            continue

        print(f"[...]  {txt.name} — извлекаю...")
        try:
            result = process_file(client, txt, today, system_prompt)
            out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"[OK]   {txt.name} -> {out_path.name} ({len(result['items'])} единиц)")
            processed.append((txt.name, out_path.name, len(result["items"])))
        except Exception as e:
            print(f"[FAIL] {txt.name}: {e}", file=sys.stderr)
            failed.append((txt.name, str(e)))

    print("\n===== ОТЧЁТ =====")
    print(f"Обработано: {len(processed)}")
    for src, out, n in processed:
        print(f"  • {src} -> {out} ({n} единиц)")
    if skipped:
        print(f"Пропущено: {len(skipped)}")
        for n in skipped:
            print(f"  • {n}")
    if failed:
        print(f"Ошибок: {len(failed)}")
        for n, err in failed:
            print(f"  • {n}: {err}")

    # Always rebuild the consolidated CRM YAML at the end (idempotent, safe).
    try:
        summary = build_crm_items_yaml()
        print(f"\n[crm-yaml] {CRM_ITEMS_YAML.relative_to(HOME)}: "
              f"{summary['total_items']} CRM item(s) "
              f"({summary['with_crm_items']} files с explicit crm_items, "
              f"{summary['fallback_items']} fallback)")
    except Exception as e:
        print(f"[crm-yaml] WARNING: failed to rebuild yaml: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
