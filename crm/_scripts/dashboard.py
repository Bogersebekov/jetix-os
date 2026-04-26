"""/crm-dash + /crm-stuck + /crm-weekly output."""
from __future__ import annotations

import datetime as _dt
from collections import Counter, defaultdict
from pathlib import Path

from .frontmatter import parse_file
from .index_builder import _load_all

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

CRM_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = CRM_ROOT / "_schema"
VIEWS_DIR = CRM_ROOT / "views"


def _today() -> _dt.date:
    return _dt.date.today()


def _date_or_none(v) -> _dt.date | None:
    if isinstance(v, _dt.date):
        return v
    if isinstance(v, str) and len(v) == 10:
        try:
            return _dt.date.fromisoformat(v)
        except ValueError:
            return None
    return None


def _stuck_config() -> tuple[set[str], int]:
    p = SCHEMA_DIR / "statuses.yaml"
    if not p.exists():
        return ({"warm", "contacted", "discovery_call", "proposal", "negotiation"}, 14)
    cfg = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    s = cfg.get("stuck") or {}
    return set(s.get("active_statuses") or []), int(s.get("threshold_days") or 14)


def find_stuck() -> list[dict]:
    active, days = _stuck_config()
    today = _today()
    out: list[dict] = []
    records, _ = _load_all()
    for r in records:
        fm = r["fm"]
        pipe = fm.get("pipeline") or {}
        status = pipe.get("status")
        if status not in active:
            continue
        last = _date_or_none(pipe.get("last_touch_date"))
        if last is None:
            continue
        delta = (today - last).days
        if delta > days:
            out.append({
                "slug": fm.get("slug"),
                "name": fm.get("name"),
                "roles": fm.get("roles") or [],
                "status": status,
                "days_since_touch": delta,
                "next_action": pipe.get("next_action"),
            })
    out.sort(key=lambda x: -x["days_since_touch"])
    return out


def render_dash() -> str:
    records, warnings = _load_all()
    today = _today()
    week_ago = today - _dt.timedelta(days=7)
    people = [r for r in records if r["kind"] == "person"]
    orgs = [r for r in records if r["kind"] == "org"]

    # by role
    role_counter: Counter = Counter()
    for r in records:
        for role in r["fm"].get("roles") or []:
            role_counter[role] += 1

    # status breakdown per role
    role_status: dict[str, Counter] = defaultdict(Counter)
    for r in records:
        st = (r["fm"].get("pipeline") or {}).get("status")
        for role in r["fm"].get("roles") or []:
            if st:
                role_status[role][st] += 1

    # client pipeline
    client_pipe: Counter = Counter()
    for r in records:
        roles = r["fm"].get("roles") or []
        if any(role.startswith("client_") for role in roles):
            st = (r["fm"].get("pipeline") or {}).get("status")
            if st:
                client_pipe[st] += 1

    # this week
    new_this_week = sum(
        1 for r in records
        if _date_or_none(r["fm"].get("created")) and _date_or_none(r["fm"].get("created")) >= week_ago
    )
    updated_this_week = sum(
        1 for r in records
        if _date_or_none(r["fm"].get("updated")) and _date_or_none(r["fm"].get("updated")) >= week_ago
    )

    # ICP distribution (clients only)
    icp_buckets = Counter()
    for r in records:
        if not any(role.startswith("client_") for role in r["fm"].get("roles") or []):
            continue
        total = (r["fm"].get("icp") or {}).get("total")
        if total is None:
            icp_buckets["unscored"] += 1
        elif total >= 18:
            icp_buckets["18+"] += 1
        elif total >= 15:
            icp_buckets["15-17"] += 1
        elif total >= 10:
            icp_buckets["10-14"] += 1
        else:
            icp_buckets["<10"] += 1

    # channel performance (clients only)
    channel_counts: Counter = Counter()
    channel_won: Counter = Counter()
    for r in records:
        if not any(role.startswith("client_") for role in r["fm"].get("roles") or []):
            continue
        ch = (r["fm"].get("origin") or {}).get("source_channel")
        if ch:
            channel_counts[ch] += 1
            if (r["fm"].get("pipeline") or {}).get("status") == "closed_won":
                channel_won[ch] += 1

    # audience leverage (advisors+partners)
    leveraged_roles = {"advisor", "mentor", "facilitator", "consultant",
                       "partner_prospect", "partner_active", "friend"}
    total_followers = 0
    overlap_sum = 0
    overlap_n = 0
    for r in records:
        if not (set(r["fm"].get("roles") or []) & leveraged_roles):
            continue
        aud = r["fm"].get("audience") or {}
        tf = aud.get("total_followers") or 0
        total_followers += tf
        if aud.get("icp_overlap_pct") is not None:
            overlap_sum += aud["icp_overlap_pct"]
            overlap_n += 1

    stuck = find_stuck()

    out: list[str] = []
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    out.append(f"=== CRM DASHBOARD ({now}) ===")
    out.append("")
    out.append(f"Total: {len(records)} contacts ({len(people)} people + {len(orgs)} orgs)")
    out.append(f"Updated last 7d: {updated_this_week}")
    out.append("")

    if role_counter:
        out.append("By role:")
        for role, n in role_counter.most_common():
            sub = role_status.get(role, Counter())
            sub_str = ""
            if sub:
                sub_str = "  (" + ", ".join(f"{k}: {v}" for k, v in sub.most_common(4)) + ")"
            out.append(f"  {role:22s} {n:3d}{sub_str}")
        out.append("")

    if client_pipe:
        out.append("Sales pipeline (clients only):")
        for st in ("cold", "warm", "contacted", "discovery_call", "proposal", "negotiation",
                   "closed_won", "closed_lost", "paused"):
            if client_pipe.get(st):
                marker = "  ⚠️" if st == "closed_won" and client_pipe[st] == 0 else ""
                out.append(f"  {st:18s} {client_pipe[st]}{marker}")
        if not client_pipe.get("closed_won"):
            out.append("  closed_won         0  ⚠️  (no wins yet)")
        out.append("")

    out.append(f"This week (since {week_ago}):")
    out.append(f"  + {new_this_week} new contacts")
    out.append("")

    if stuck:
        out.append(f"Stuck (>{ _stuck_config()[1] }d, no touch):")
        for s in stuck[:10]:
            roles_short = ",".join(s["roles"][:2])
            out.append(f"  - {s['slug']:24s} ({s['status']}, {s['days_since_touch']} days)  [{roles_short}]")
        if len(stuck) > 10:
            out.append(f"  … +{len(stuck) - 10} more")
        out.append("")

    if icp_buckets:
        out.append("ICP fit distribution (clients only):")
        bucket_str = "  ".join(f"{k}: {v}" for k, v in sorted(icp_buckets.items()))
        out.append(f"  {bucket_str}")
        out.append("")

    if channel_counts:
        out.append("Channel performance (clients only):")
        for ch, n in channel_counts.most_common():
            won = channel_won.get(ch, 0)
            out.append(f"  {ch:18s} {n} contacts → {won} won")
        out.append("")

    if total_followers > 0:
        out.append("Audience leverage (advisors + partners + friends):")
        out.append(f"  Total reach available: {total_followers:,} followers")
        if overlap_n:
            avg = overlap_sum // overlap_n
            out.append(f"  AI-native audience overlap (avg): ~{avg}%")
        out.append("")

    if warnings:
        out.append(f"⚠ Warnings: {len(warnings)} (run /crm-rebuild-index to surface details)")
    return "\n".join(out)


def render_weekly(today: _dt.date | None = None) -> str:
    today = today or _today()
    week_ago = today - _dt.timedelta(days=7)
    records, _ = _load_all()
    new_records = []
    updated_records = []
    for r in records:
        cdate = _date_or_none(r["fm"].get("created"))
        udate = _date_or_none(r["fm"].get("updated"))
        if cdate and cdate >= week_ago:
            new_records.append(r)
        elif udate and udate >= week_ago:
            updated_records.append(r)

    out: list[str] = []
    out.append(f"# CRM Weekly Report — {today}")
    out.append("")
    out.append(render_dash())
    out.append("")
    out.append("## New contacts this week")
    out.append("")
    if not new_records:
        out.append("(none)")
    else:
        for r in new_records:
            fm = r["fm"]
            out.append(f"- **{fm.get('name')}** ({fm.get('slug')}) — "
                       f"roles: {', '.join(fm.get('roles') or [])}, "
                       f"channel: {(fm.get('origin') or {}).get('source_channel') or '?'}")
    out.append("")
    out.append("## Status changes this week")
    out.append("")
    if not updated_records:
        out.append("(none with frontmatter-update flag)")
    else:
        for r in updated_records:
            fm = r["fm"]
            pipe = fm.get("pipeline") or {}
            out.append(f"- **{fm.get('name')}** — status: {pipe.get('status') or '?'}, "
                       f"next: {pipe.get('next_action') or '—'}")
    out.append("")
    stuck = find_stuck()
    out.append("## Stuck — requires action")
    out.append("")
    if not stuck:
        out.append("(none stuck)")
    else:
        for s in stuck:
            out.append(f"- **{s['name']}** ({s['slug']}) — {s['status']}, "
                       f"{s['days_since_touch']}d. Next: {s['next_action'] or '—'}")
    out.append("")
    return "\n".join(out)


def save_weekly() -> Path:
    today = _today()
    VIEWS_DIR.mkdir(exist_ok=True)
    p = VIEWS_DIR / f"weekly-{today.isoformat()}.md"
    p.write_text(render_weekly(today), encoding="utf-8")
    return p
