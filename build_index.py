"""
Build a master index of every per-company tracker.

Reads every company/<slug>/tracker.json and writes companies_index.json at the
project root: a single sorted list (descending priority_score) with the fields
a future session needs to pick which company to work on next.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
COMPANY_DIR = ROOT / "company"
OUT = ROOT / "companies_index.json"


def load_one(folder: Path) -> dict | None:
    tracker = folder / "tracker.json"
    if not tracker.exists():
        return None
    data = json.loads(tracker.read_text())
    meta = data.get("metadata", {})
    contacts = data.get("contacts", [])
    named = [c for c in contacts if (c.get("contact_name") or "").strip()]
    sent = [c for c in contacts if (c.get("date_sent") or "").strip()]
    return {
        "company_name": data.get("company_name", ""),
        "slug": data.get("slug", folder.name),
        "folder": f"./company/{folder.name}",
        "priority_score": meta.get("priority_score", 0),
        "hiring_status": meta.get("hiring_status", ""),
        "role_title": meta.get("role_title", ""),
        "location": meta.get("location", ""),
        "salary_range_lpa": meta.get("salary_range_lpa", ""),
        "research_status": data.get("research_status", ""),
        "named_contacts": len(named),
        "emails_sent": len(sent),
        "source_csv": meta.get("_source_csv", ""),
    }


def priority_key(rec: dict) -> int:
    p = rec.get("priority_score", 0)
    try:
        return -int(p)
    except (TypeError, ValueError):
        return 0


def main() -> None:
    rows: list[dict] = []
    for folder in sorted(COMPANY_DIR.iterdir()):
        if not folder.is_dir():
            continue
        rec = load_one(folder)
        if rec is not None:
            rows.append(rec)
    rows.sort(key=priority_key)
    OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT} with {len(rows)} companies.")
    top = [r for r in rows if r["priority_score"] != ""][:10]
    print("Top 10 by priority:")
    for r in top:
        print(f"  {r['priority_score']:>3}  {r['company_name']}  -- {r['role_title']}")


if __name__ == "__main__":
    main()
