"""
One-shot setup script.

Reads company_data_1.csv + company_data_2.csv, creates a folder per company under
./company/<slug>/, drops in:
  - resume.tex   (base copy, to be tailored when the JD is researched)
  - tracker.json (per-company tracker, pre-filled with CSV metadata)
  - research.md  (scaffold for the per-company research step)

Idempotent: re-running will not clobber tracker.json contacts or research.md
content; it will refresh resume.tex from the project root and refresh the
metadata block in tracker.json.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
COMPANY_DIR = ROOT / "company"
BASE_RESUME = ROOT / "resume.tex"
CSV_FILES = [ROOT / "company_data_1.csv", ROOT / "company_data_2.csv"]


def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def read_companies() -> list[dict]:
    out: list[dict] = []
    seen: set[str] = set()
    for csv_path in CSV_FILES:
        with csv_path.open() as f:
            for row in csv.DictReader(f):
                name = (row.get("company_name") or "").strip()
                if not name:
                    continue
                slug = slugify(name)
                if slug in seen:
                    continue
                seen.add(slug)
                row["_slug"] = slug
                row["_source_csv"] = csv_path.name
                out.append(row)
    return out


def build_metadata(row: dict) -> dict:
    keys = [
        "location",
        "role_title",
        "salary_range_lpa",
        "funding_stage",
        "recent_signal",
        "match_reason",
        "company_url",
        "careers_page",
        "linkedin_company_page",
        "contact_page",
        "job_url",
        "hiring_status",
        "priority_score",
        "cold_outreach_angle",
        "notes",
    ]
    meta = {}
    for k in keys:
        v = row.get(k)
        if v is None:
            meta[k] = ""
            continue
        v = v.strip()
        if k == "priority_score":
            try:
                meta[k] = int(v)
            except (TypeError, ValueError):
                meta[k] = v
        else:
            meta[k] = v
    meta["_source_csv"] = row.get("_source_csv", "")
    return meta


def empty_contact() -> dict:
    return {
        "contact_name": "",
        "contact_role": "",
        "tier": "",
        "to": "",
        "cc": [],
        "linkedin": "",
        "research_hook": "",
        "subject": "",
        "content": "",
        "date_sent": "",
        "follow_up_1_subject": "",
        "follow_up_1_content": "",
        "follow_up_1_date": "",
        "follow_up_1_sent_at": "",
        "follow_up_2_subject": "",
        "follow_up_2_content": "",
        "follow_up_2_date": "",
        "follow_up_2_sent_at": "",
        "status": "queued",
        "response_notes": "",
    }


def initial_tracker(row: dict) -> dict:
    return {
        "company_name": row["company_name"].strip(),
        "slug": row["_slug"],
        "metadata": build_metadata(row),
        "research_status": "not_started",
        "research_summary": "",
        "jd_full_text": "",
        "resume_latex_path": "./resume.tex",
        "resume_pdf_path": "./resume.pdf",
        "tailoring_notes": "",
        "contacts": [empty_contact()],
    }


def write_research_md(folder: Path, row: dict) -> None:
    path = folder / "research.md"
    if path.exists():
        return  # don't clobber human-written research
    name = row["company_name"].strip()
    body = f"""# {name} — Research

> Scaffold for per-company research. Fill in once you (or a future Claude session) actually go deep on this target.

## CSV signal (starting hints)

- **Location:** {row.get('location','').strip()}
- **Role title (CSV):** {row.get('role_title','').strip()}
- **Salary band (LPA):** {row.get('salary_range_lpa','').strip()}
- **Funding stage:** {row.get('funding_stage','').strip()}
- **Hiring status:** {row.get('hiring_status','').strip()}
- **Priority score:** {row.get('priority_score','').strip()}
- **Recent signal:** {row.get('recent_signal','').strip()}
- **Match reason:** {row.get('match_reason','').strip()}
- **Cold outreach angle:** {row.get('cold_outreach_angle','').strip()}
- **Notes:** {row.get('notes','').strip()}

## Links

- Company: {row.get('company_url','').strip()}
- Careers: {row.get('careers_page','').strip()}
- LinkedIn: {row.get('linkedin_company_page','').strip()}
- Contact: {row.get('contact_page','').strip()}
- Job URL: {row.get('job_url','').strip()}

## To research (fill in later)

- [ ] Full JD text (copy verbatim)
- [ ] Tech stack confirmed from JD
- [ ] 10-20 named individuals with role, LinkedIn, verified email (Tier 1 EMs/leads first, then founders, then ICs, then recruiters)
- [ ] Last 60 days: shipped products, blog posts, podcasts, X/LinkedIn threads, funding moves
- [ ] Specific technical bet to reference in cold email
- [ ] Mutual connections (alumni, ex-colleagues, shared investors)

## Resume tailoring brief (fill in once JD is read)

- [ ] Which of Amit's projects to lead with
- [ ] Which bullets to drop or de-emphasize
- [ ] Skill section reordering
- [ ] Summary line rewrite

## Outreach plan

- [ ] First-send batch (Tue/Wed/Thu, recipient local time)
- [ ] Subject lines per contact (no two identical)
- [ ] Follow-up #1 hook (something new — not just "bumping")
- [ ] Follow-up #2 hook (close-the-loop line)
"""
    path.write_text(body)


def write_tracker(folder: Path, row: dict) -> None:
    path = folder / "tracker.json"
    if path.exists():
        # Merge: refresh metadata, preserve everything else
        existing = json.loads(path.read_text())
        existing["company_name"] = row["company_name"].strip()
        existing["slug"] = row["_slug"]
        existing["metadata"] = build_metadata(row)
        # Don't touch research_summary, jd_full_text, tailoring_notes, contacts
        path.write_text(json.dumps(existing, indent=2, ensure_ascii=False))
        return
    path.write_text(json.dumps(initial_tracker(row), indent=2, ensure_ascii=False))


def write_resume(folder: Path) -> None:
    target = folder / "resume.tex"
    shutil.copyfile(BASE_RESUME, target)


def main() -> None:
    if not BASE_RESUME.exists():
        raise SystemExit(f"Base resume not found at {BASE_RESUME}")
    COMPANY_DIR.mkdir(parents=True, exist_ok=True)

    companies = read_companies()
    print(f"Found {len(companies)} unique companies across CSVs.")

    created = 0
    refreshed = 0
    for row in companies:
        folder = COMPANY_DIR / row["_slug"]
        existed = folder.exists()
        folder.mkdir(parents=True, exist_ok=True)
        write_resume(folder)
        write_tracker(folder, row)
        write_research_md(folder, row)
        if existed:
            refreshed += 1
        else:
            created += 1

    print(f"Created: {created} new folders.")
    print(f"Refreshed: {refreshed} existing folders.")
    print(f"All folders live under: {COMPANY_DIR}")


if __name__ == "__main__":
    main()
