---
description: Pick the highest-priority untouched target company and brief on what to do next.
---

# /next-company

Quickly identify which company to work on next based on `companies_index.json`.

## Steps

1. Read `companies_index.json` at the project root. (If missing or stale, regenerate first: `python3 build_index.py`.)
2. Pick the first record where `emails_sent == 0` and `research_status` is `not_started` or empty. That is the next target.
3. Print a 6-line brief:
   - **Company:** `<company_name>` (slug: `<slug>`)
   - **Role:** `<role_title>`
   - **Priority:** `<priority_score>` — `<hiring_status>`
   - **Location / Salary:** `<location>` / `<salary_range_lpa>` LPA
   - **Folder:** `company/<slug>/`
   - **Next:** run `/research-company <slug>` to start research with the connected Chrome browser
4. Do not modify any files. This command is read-only — it tells the user where to point next.

## Notes

- If `companies_index.json` does not exist, run `python3 build_index.py` first, then re-run this command.
- Skip records where `research_status == "done"` even if `emails_sent == 0` (user may have deferred outreach intentionally).
- If there are no untouched targets, print "All 166 companies have research_status set. Review `companies_index.json` for what to follow up on." and stop.
