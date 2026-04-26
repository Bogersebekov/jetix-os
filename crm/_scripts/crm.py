"""Main CRM CLI. All /crm-* skills delegate here.

Usage:
    python -m crm._scripts.crm <subcommand> [args]

Subcommands:
    add SLUG_OR_NAME [--role=R] [--niche=...] [--country=DE] [--channel=indiehackers]
                    [--first-contact=2026-04-26] [--context="..."]
    show SLUG
    list [field=val ...] [--sort=last_touch|icp|name] [--orgs|--no-orgs]
    search QUERY
    touch SLUG NOTE
    update SLUG [--field=val ...] [--note="..."]
    rebuild-index
    dash
    stuck
    weekly [--save]
    voice-route PATH       (read YAML list, route items)
    validate [PATH ...]    (validate one or all CRM files)
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

from . import frontmatter as fm_mod
from . import index_builder, dashboard, views, strategy_hooks, voice_router

CRM_ROOT = Path(__file__).resolve().parent.parent
PEOPLE_DIR = CRM_ROOT / "people"
ORGS_DIR = CRM_ROOT / "orgs"
LOG_PATH = CRM_ROOT / "log.md"
TEMPLATE_PERSON = CRM_ROOT / "_templates" / "person.md"


def _today() -> str:
    return _dt.date.today().isoformat()


def _now_ts() -> str:
    return _dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def _slugify(name: str) -> str:
    return voice_router._slugify(name)


def _append_log(line: str) -> None:
    LOG_PATH.touch(exist_ok=True)
    existing = LOG_PATH.read_text(encoding="utf-8")
    LOG_PATH.write_text(line + "\n" + existing, encoding="utf-8")


def _resolve_path(slug: str) -> Path | None:
    for d in (PEOPLE_DIR, ORGS_DIR):
        p = d / f"{slug}.md"
        if p.exists():
            return p
    return None


# ── add ───────────────────────────────────────────────────────────────────────


def cmd_add(args: argparse.Namespace) -> int:
    name = args.name
    slug = args.slug or _slugify(name)
    if (PEOPLE_DIR / f"{slug}.md").exists() or (ORGS_DIR / f"{slug}.md").exists():
        sys.stderr.write(f"error: slug {slug!r} already exists. Try {slug}-2.\n")
        return 1
    target_dir = ORGS_DIR if args.org else PEOPLE_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    template_path = (CRM_ROOT / "_templates" / ("org.md" if args.org else "person.md"))
    text = template_path.read_text(encoding="utf-8")
    today = _today()
    text = (text.replace("FULL_NAME" if not args.org else "ORG_NAME", name)
                .replace("SLUG", slug)
                .replace("TODAY", today))
    fm, body = fm_mod.parse_text(text)

    if args.role:
        fm["roles"] = [r.strip() for r in args.role.split(",") if r.strip()]
    if args.niche:
        fm["niche"] = args.niche
    if args.country:
        fm["location_country"] = args.country
    if args.channel:
        fm.setdefault("origin", {})["source_channel"] = args.channel
    if args.first_contact:
        fm.setdefault("origin", {})["first_contact_date"] = args.first_contact
    if args.context:
        fm.setdefault("origin", {})["context"] = args.context

    # auto-fix + validate
    fm, autofix_warnings = fm_mod.autofix(fm)
    errors = fm_mod.validate(fm, file_hint=f"{slug}.md")
    if errors:
        sys.stderr.write("Validation errors:\n")
        for e in errors:
            sys.stderr.write(f"  - {e}\n")
        return 1

    # strategy hooks prefill
    offers = strategy_hooks.suggest_offers(fm)
    asks = strategy_hooks.suggest_asks(fm)
    body = _replace_section(body, 7, strategy_hooks.render_section(offers))
    body = _replace_section(body, 8, strategy_hooks.render_section(asks))

    path = target_dir / f"{slug}.md"
    path.write_text(fm_mod.dump(fm, body), encoding="utf-8")

    _append_log(f"## {_now_ts()} — added {slug} ({name})\n  roles: {fm.get('roles')} / source: "
                f"{(fm.get('origin') or {}).get('source_channel') or 'unset'}\n")

    # silent index rebuild
    try:
        index_builder.rebuild(write=True)
    except Exception as e:  # pragma: no cover
        sys.stderr.write(f"warning: index rebuild failed: {e}\n")

    icp_status = "TBD (run /crm-update <slug> --icp.* later)"
    print(f"Added {path.relative_to(CRM_ROOT)}. Roles: {fm.get('roles')}. ICP scoring: {icp_status}.")
    print(f"Run /crm-show {slug} to view.")
    if autofix_warnings:
        for w in autofix_warnings:
            print(f"  (autofix) {w}")
    if offers:
        print(f"  §7 prefilled: {len(offers)} offer(s)")
    if asks:
        print(f"  §8 prefilled: {len(asks)} ask(s)")
    return 0


_SECTION_RE_TPL = r"(##\s*§{n}\.[^\n]*\n)(.*?)(?=\n##\s*§|\Z)"


def _replace_section(body: str, n: int, new_content: str) -> str:
    pattern = re.compile(_SECTION_RE_TPL.format(n=n), re.DOTALL)
    if not pattern.search(body):
        return body
    return pattern.sub(lambda m: m.group(1) + "\n" + new_content.rstrip() + "\n", body)


# ── show ──────────────────────────────────────────────────────────────────────


def cmd_show(args: argparse.Namespace) -> int:
    path = _resolve_path(args.slug)
    if not path:
        sys.stderr.write(f"error: {args.slug} not found\n")
        return 1
    fm, body = fm_mod.parse_file(path)
    print(f"=== {fm.get('name')} ({fm.get('slug')}) ===")
    print(f"Roles:    {', '.join(fm.get('roles') or [])}")
    pipe = fm.get("pipeline") or {}
    print(f"Status:   {pipe.get('status') or '?'} → next: {pipe.get('next_action') or '—'} "
          f"(by {pipe.get('next_action_date') or '—'})")
    icp = fm.get("icp") or {}
    if icp.get("total") is not None:
        print(f"ICP:      Startupper={icp.get('startupper')}, total={icp.get('total')}/20 "
              f"(azart={icp.get('azart')}, stable={icp.get('stable')}, "
              f"adequate={icp.get('adequate')}, upward={icp.get('upward')})")
    print(f"Location: {fm.get('location_city') or ''}, {fm.get('location_country') or ''}".rstrip(", "))
    if fm.get("income_bucket"):
        print(f"Income:   {fm.get('income_bucket')}")
    aud = fm.get("audience") or {}
    if aud.get("total_followers"):
        print(f"Audience: {aud['total_followers']:,}")
    print(f"Last touch: {pipe.get('last_touch_date') or '—'}")
    print()
    print(body.strip())
    return 0


# ── list ──────────────────────────────────────────────────────────────────────


def cmd_list(args: argparse.Namespace) -> int:
    try:
        recs = views.filter_records(args.filters, include_orgs=not args.no_orgs)
    except ValueError as e:
        sys.stderr.write(f"error: {e}\n")
        return 1
    if args.sort:
        recs = views.sort_records(recs, sort_by=args.sort, reverse=not args.asc)
    print(f"{'Slug':<24} | {'Name':<28} | {'Roles':<24} | {'Status':<14} | ICP | Last touch  | Next action")
    print("-" * 140)
    for path, fm, _body in recs:
        roles = ", ".join(fm.get("roles") or [])[:24]
        pipe = fm.get("pipeline") or {}
        icp = (fm.get("icp") or {}).get("total")
        icp_s = str(icp) if icp is not None else "—"
        print(f"{(fm.get('slug') or '')[:24]:<24} | {(fm.get('name') or '')[:28]:<28} | "
              f"{roles:<24} | {(pipe.get('status') or '—')[:14]:<14} | "
              f"{icp_s:<3} | {pipe.get('last_touch_date') or '—':<11} | "
              f"{(pipe.get('next_action') or '')[:50]}")
    print(f"\n{len(recs)} matches.")
    return 0


# ── search ────────────────────────────────────────────────────────────────────


def cmd_search(args: argparse.Namespace) -> int:
    hits = views.search_records(args.query)
    if not hits:
        print("(no matches)")
        return 0
    for path, fm, n in hits:
        kind = "[org]" if fm.get("type") == "org" else ""
        print(f"{(fm.get('slug') or ''):<28} {kind:<6} ({n} hit{'s' if n > 1 else ''})  — {fm.get('name')}")
    return 0


# ── touch ─────────────────────────────────────────────────────────────────────


def cmd_touch(args: argparse.Namespace) -> int:
    path = _resolve_path(args.slug)
    if not path:
        sys.stderr.write(f"error: {args.slug} not found\n")
        return 1
    fm, body = fm_mod.parse_file(path)
    today = _today()
    entry = f"\n### {today} — touch\n- {args.note}\n"
    new_body = re.sub(
        r"(##\s*§11\.[^\n]*\n)",
        lambda m: m.group(1) + entry,
        body,
        count=1,
    )
    if new_body == body:
        new_body = body + f"\n## §11. История взаимодействий (newest top, append-only)\n{entry}"
    fm.setdefault("pipeline", {})["last_touch_date"] = today
    fm["updated"] = today
    path.write_text(fm_mod.dump(fm, new_body), encoding="utf-8")
    _append_log(f"## {_now_ts()} — touch {args.slug}: {args.note[:80]}\n")
    print(f"Touched {args.slug} ({today}).")
    return 0


# ── update ────────────────────────────────────────────────────────────────────


def _set_path(d: dict, path: str, value):
    parts = path.split(".")
    cur = d
    for p in parts[:-1]:
        if p not in cur or not isinstance(cur.get(p), dict):
            cur[p] = {}
        cur = cur[p]
    cur[parts[-1]] = value


def _coerce(value: str):
    if value.lower() in ("true", "yes"):
        return value.lower() if value.lower() in ("yes", "no") else True
    if value.lower() in ("false", "no"):
        return value.lower() if value.lower() in ("yes", "no") else False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if re.fullmatch(r"-?\d+\.\d+", value):
        return float(value)
    return value


def cmd_update(args: argparse.Namespace) -> int:
    path = _resolve_path(args.slug)
    if not path:
        sys.stderr.write(f"error: {args.slug} not found\n")
        return 1
    fm, body = fm_mod.parse_file(path)
    changes: list[str] = []
    for assignment in (args.set or []):
        if "=" not in assignment:
            sys.stderr.write(f"warning: ignored {assignment!r} (use field=value)\n")
            continue
        k, v = assignment.split("=", 1)
        # convenience aliases
        alias_map = {
            "status": "pipeline.status",
            "next-action": "pipeline.next_action",
            "next_action": "pipeline.next_action",
            "next-action-date": "pipeline.next_action_date",
            "next_action_date": "pipeline.next_action_date",
            "owner": "pipeline.owner",
        }
        k = alias_map.get(k.strip(), k.strip())
        _set_path(fm, k, _coerce(v.strip()))
        changes.append(f"{k}={v.strip()}")
    today = _today()
    fm["updated"] = today
    if args.note:
        entry = f"\n### {today} — update\n- {args.note}\n"
        new_body = re.sub(
            r"(##\s*§11\.[^\n]*\n)",
            lambda m: m.group(1) + entry,
            body,
            count=1,
        )
        if new_body == body:
            new_body = body + f"\n## §11. История взаимодействий\n{entry}"
        body = new_body
        fm.setdefault("pipeline", {})["last_touch_date"] = today

    if args.resync_hooks:
        offers = strategy_hooks.suggest_offers(fm)
        asks = strategy_hooks.suggest_asks(fm)
        body = _replace_section(body, 7, strategy_hooks.render_section(offers))
        body = _replace_section(body, 8, strategy_hooks.render_section(asks))
        changes.append(f"resync-hooks: {len(offers)} offers, {len(asks)} asks")

    fm, autofix_warnings = fm_mod.autofix(fm)
    errors = fm_mod.validate(fm, file_hint=path.name)
    if errors:
        sys.stderr.write("Validation errors after update:\n")
        for e in errors:
            sys.stderr.write(f"  - {e}\n")
        return 1
    path.write_text(fm_mod.dump(fm, body), encoding="utf-8")
    _append_log(f"## {_now_ts()} — update {args.slug}: {', '.join(changes) or '(no changes)'}\n")
    print(f"Updated {args.slug}: {', '.join(changes) or '(no changes)'}")
    if autofix_warnings:
        for w in autofix_warnings:
            print(f"  (autofix) {w}")
    return 0


# ── rebuild-index ─────────────────────────────────────────────────────────────


def cmd_rebuild_index(_args) -> int:
    _, warnings, changed = index_builder.rebuild(write=True)
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")
    print(f"index.md {'rewritten' if changed else 'unchanged'}.")
    return 0


# ── dash ──────────────────────────────────────────────────────────────────────


def cmd_dash(_args) -> int:
    print(dashboard.render_dash())
    return 0


def cmd_stuck(_args) -> int:
    stuck = dashboard.find_stuck()
    if not stuck:
        print("(nothing stuck)")
        return 0
    for s in stuck:
        roles_short = ",".join(s["roles"][:2])
        print(f"  {s['slug']:<24} ({s['status']}, {s['days_since_touch']}d)  [{roles_short}]  "
              f"next: {s['next_action'] or '—'}")
    return 0


def cmd_weekly(args: argparse.Namespace) -> int:
    if args.save:
        p = dashboard.save_weekly()
        print(f"Saved {p.relative_to(CRM_ROOT)}.")
    else:
        print(dashboard.render_weekly())
    return 0


def cmd_voice_route(args: argparse.Namespace) -> int:
    summary = voice_router.route_file(Path(args.path))
    if "error" in summary:
        sys.stderr.write(f"error: {summary['error']}\n")
        return 1
    print(f"Voice route summary: {summary}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    paths: list[Path] = []
    if args.paths:
        paths = [Path(p) for p in args.paths]
    else:
        for d in (PEOPLE_DIR, ORGS_DIR):
            if d.is_dir():
                paths.extend(sorted(d.glob("*.md")))
    total_errors = 0
    for p in paths:
        try:
            fm, _ = fm_mod.parse_file(p)
        except Exception as e:
            print(f"{p.name}: PARSE ERROR — {e}")
            total_errors += 1
            continue
        errs = fm_mod.validate(fm, file_hint=p.name)
        if errs:
            total_errors += len(errs)
            for e in errs:
                print(e)
    if total_errors == 0:
        print(f"OK: {len(paths)} file(s) valid.")
        return 0
    print(f"FAIL: {total_errors} error(s) across {len(paths)} file(s).")
    return 1


# ── parser ────────────────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="crm")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Create a new person/org entry")
    a.add_argument("name")
    a.add_argument("--slug")
    a.add_argument("--role")
    a.add_argument("--niche")
    a.add_argument("--country")
    a.add_argument("--channel")
    a.add_argument("--first-contact", dest="first_contact")
    a.add_argument("--context")
    a.add_argument("--org", action="store_true", help="Create org instead of person")
    a.set_defaults(fn=cmd_add)

    s = sub.add_parser("show")
    s.add_argument("slug")
    s.set_defaults(fn=cmd_show)

    l = sub.add_parser("list")
    l.add_argument("filters", nargs="*", help="key=val or key>=N")
    l.add_argument("--sort", default="last_touch")
    l.add_argument("--asc", action="store_true")
    l.add_argument("--no-orgs", action="store_true")
    l.set_defaults(fn=cmd_list)

    sr = sub.add_parser("search")
    sr.add_argument("query")
    sr.set_defaults(fn=cmd_search)

    t = sub.add_parser("touch")
    t.add_argument("slug")
    t.add_argument("note")
    t.set_defaults(fn=cmd_touch)

    u = sub.add_parser("update")
    u.add_argument("slug")
    u.add_argument("--set", action="append", help="field=value (repeatable)")
    u.add_argument("--note")
    u.add_argument("--resync-hooks", action="store_true")
    u.set_defaults(fn=cmd_update)

    sub.add_parser("rebuild-index").set_defaults(fn=cmd_rebuild_index)
    sub.add_parser("dash").set_defaults(fn=cmd_dash)
    sub.add_parser("stuck").set_defaults(fn=cmd_stuck)

    w = sub.add_parser("weekly")
    w.add_argument("--save", action="store_true")
    w.set_defaults(fn=cmd_weekly)

    vr = sub.add_parser("voice-route")
    vr.add_argument("path")
    vr.set_defaults(fn=cmd_voice_route)

    v = sub.add_parser("validate")
    v.add_argument("paths", nargs="*")
    v.set_defaults(fn=cmd_validate)

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
