---
description: Deep research on one company using the connected Chrome browser. Fills research.md, jd_full_text, and the contacts list in tracker.json.
---

# /research-company $ARGUMENTS

Deep-research one target company using the real Chrome browser (`claude --chrome` / `/chrome`).

`$ARGUMENTS` is the company slug (e.g. `sarvam-ai`). If empty, fall back to `/next-company` to pick the top priority untouched record.

## Pre-flight

1. Confirm Chrome is connected. If the Chrome tools are not available in this session, stop and tell the user: "Run `/chrome` first, or restart with `claude --chrome`."
2. Read `company/<slug>/tracker.json` and `company/<slug>/research.md`. If either is missing, run `python3 setup_companies.py` and re-read.
3. Re-read `cold email strategy.md` (priority hierarchy + per-company contact cap) and `templates and ai avoidance.md` (anti-AI rules). These govern who to find and how to phrase later.

## Research workflow

Do these in order. Save findings to the files as you go — don't batch.

### A. Pull the full JD

1. Open `metadata.job_url` in Chrome.
2. If the page redirected or rotted, fall back to `metadata.careers_page` and find the role matching `metadata.role_title`.
3. Copy the JD verbatim into `tracker.json` field `jd_full_text`. Save.
4. Note the explicit tech stack, seniority band, location, and any "must-have" language in `research.md` under a new "## Full JD signal" section.

### B. Map the team and find named individuals

Contact targets depend on company size (check LinkedIn employee count or `metadata`):

**Companies >50 employees — minimum 6-8 contacts:**
- **4-5 employees** from the AI/ML team: `engineering manager`, `ml engineer`, `ai engineer`, `tech lead`, `principal engineer`, `staff engineer`, `senior software engineer`, `ml researcher`, `applied scientist` (Tier 1 and Tier 3)
- **2-3 HR/recruiters**: `recruiter`, `talent acquisition`, `hr business partner`, `hr manager` (Tier 4)
- **Hard skip**: Do NOT add any founder, CEO, CTO, or C-suite contact — they do not screen candidates at this scale and emailing them reads as naive
- Search employees first, then HR. Hit both minimums before stopping.

**Companies <=50 employees — aim for 6-10 contacts, mix all three groups:**
- **2-3 employees** from the team: `engineering manager`, `ml engineer`, `ai engineer`, `tech lead` (Tier 1)
- **1-2 founders/exec**: `founder`, `ceo`, `cto`, `vp engineering` (Tier 2 — they often interview directly at this size)
- **1-2 HR/recruiters**: `recruiter`, `talent acquisition` (Tier 4)
- **Additional ICs** if needed to hit the minimum: `senior software engineer`, `applied scientist` (Tier 3)

1. Open `metadata.linkedin_company_page` in Chrome.
2. Use the "People" search and filter using the keywords above in the right order for the company size.
3. For each named individual, capture in `research.md`:
   - Name
   - Role title (exact wording from LinkedIn)
   - LinkedIn URL
   - Tier (1/2/3/4)
   - At least 5 recent posts or activity items from the last 60 days (check their activity page — this is the hook material for the cold email). Note what topics they post about, what they care about, any product announcements, opinions.
4. Do not stop at one or two. Aim for 10-20 with the tier mix above.

### C. Verify email addresses

For each named individual found in B:

1. Try the company's standard pattern (often visible from a Hunter.io public-profile lookup, careers-page contact email, or a press release email). Capture pattern in `research.md`.
2. Build a single best-guess email per person. Examples for `first.last@company.com` pattern: `aman.mishra@unsiloed.ai`. Avoid sending multiple permutations — bounce risk is real.
3. If a single verified email is not findable, leave `to` empty for that contact (the user will skip live-send for them).
4. **Never** use `careers@`, `jobs@`, `hello@`, `info@`. Hard rule.

### D. Recent activity scan

1. Open the company X/Twitter handle (search company name on x.com). Note last 5 posts in the last 60 days.
2. Open the founder's X handle. Same.
3. Search company name on news.ycombinator.com and the company's blog. Note funding rounds, launches, podcasts, conference talks from the last 60 days.
4. Capture all of this under "## Last 60 days" in `research.md`. This becomes the cold-email opener material.

### E. Wire it into tracker.json

1. For each named individual from B, append a contact entry to `tracker.json` `contacts[]`. Fields to populate:
   - `contact_name`, `contact_role`, `tier`, `to`, `linkedin`, `research_hook` (one of the specific items from D that connects to this person — be specific)
   - Leave `subject`, `content`, follow-up fields, `status="queued"` for now (those get filled by `/draft-outreach`)
2. Set `research_status = "done"` and write a 3-5 line `research_summary` in `tracker.json`.
3. Save the tracker.

## After research

- Run `python3 build_index.py` to refresh the master index.
- Tell the user: "Research done for `<slug>`. <N> contacts captured. Next: `/tailor-resume <slug>`."

## Hard rules

- Real names + verified emails only. Skip Tier 4 generic inboxes.
- One contact per person, not per permutation. Pick the best-guess pattern; don't shotgun.
- Don't write any email content here. That's `/draft-outreach`.
- Don't modify the source CSVs. They are read-only feeders.
- If Chrome is not connected (no chrome tools available), stop and tell the user — do not fall back to WebFetch for LinkedIn pages (login-gated content will return nothing useful).
