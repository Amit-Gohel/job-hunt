# CLAUDE.md — Project context for the job-hunt outreach system

This file is the single source of truth for any Claude session opened in this directory. Read it end-to-end before doing anything.

---

## Who the user is

Amit Gohel. AI/ML engineer (~2 years production). Currently at Vivansh Infotech, Ahmedabad. Targeting AI/ML roles primarily at India-based AI companies (Bengaluru, Hyderabad, Delhi/Gurgaon, Pune, Mumbai). Personal site: https://amitgohel.dev. See `chunks.json` for the full first-person knowledge base scraped from amitgohel.dev — that is the canonical source for resume content and cold-email proof points.

Date today: see system context.

---

## What this project does

Run a personalized cold-email outreach campaign to ~166 target companies. End-to-end: research → resume tailoring → contact discovery → cold email → follow-ups → status tracking.

Strategy doc: `cold email strategy.md` (when, how often, who to contact, follow-up cadence, anti-spray rules).
Templates + anti-AI-detection: `templates and ai avoidance.md` (3 templates, follow-ups, vocabulary to strip, human-writing techniques).

**Both docs are load-bearing. Do not write a single outreach email without re-reading them.** Especially the anti-AI vocabulary list.

---

## File layout

```
job_hunt/
├── CLAUDE.md                       # this file
├── cold email strategy.md          # outreach strategy (volume, timing, follow-ups)
├── templates and ai avoidance.md   # templates + anti-AI-detection rules
├── chunks.json                     # Amit's profile knowledge base (resume + email source-of-truth)
├── resume.tex                      # master LaTeX resume — base for all per-company copies
├── company_data_1.csv              # 103 target companies (general India AI scan)
├── company_data_2.csv              # 63 target companies (second scan)
├── companies_index.json            # generated — every company sorted by priority_score
├── Cold email tracker.json         # legacy/example tracker format (the schema reference)
├── setup_companies.py              # builds company/<slug>/ folders from CSVs (idempotent)
├── build_index.py                  # rebuilds companies_index.json from all trackers
├── send.py                         # SMTP sender — walks all per-company tracker.json files
├── .env                            # SMTP_PASS for send.py (do not commit)
└── company/
    └── <company-slug>/             # one folder per company, slug is kebab-case
        ├── resume.tex              # starts as a copy of root resume.tex; tailor per JD here
        ├── tracker.json            # per-company tracker (metadata + contacts + email content)
        └── research.md             # research scaffold; fill in once you go deep on this target
```

Slug rule: lowercase, non-alphanumerics → hyphen, collapse repeats, strip ends.
Example: `5C Network` → `5c-network`, `Hasura (PromptQL)` → `hasura-promptql`.

---

## Per-company tracker schema (`company/<slug>/tracker.json`)

```jsonc
{
  "company_name": "Unsiloed AI",
  "slug": "unsiloed-ai",
  "metadata": {                     // copied from the CSV, refreshable by setup_companies.py
    "location": "...",
    "role_title": "...",
    "salary_range_lpa": "...",
    "funding_stage": "...",
    "recent_signal": "...",
    "match_reason": "...",
    "company_url": "...",
    "careers_page": "...",
    "linkedin_company_page": "...",
    "contact_page": "...",
    "job_url": "...",
    "hiring_status": "...",
    "priority_score": 95,
    "cold_outreach_angle": "...",
    "notes": "...",
    "_source_csv": "company_data_2.csv"
  },
  "research_status": "not_started", // not_started | in_progress | done
  "research_summary": "",            // 3-5 line distillation of research.md once done
  "jd_full_text": "",                // verbatim JD copy
  "resume_latex_path": "./resume.tex",
  "resume_pdf_path": "./resume.pdf",
  "tailoring_notes": "",             // what was changed vs base resume, and why
  "contacts": [                      // one entry PER NAMED PERSON. Goal: 10-20 per company.
    {
      "contact_name": "",
      "contact_role": "",
      "tier": "",                    // 1 = hiring manager/EM/lead, 2 = founder/exec, 3 = IC, 4 = recruiter
      "to": "",                      // single verified email (Hunter.io / Apollo). NEVER careers@.
      "cc": [],
      "linkedin": "",
      "research_hook": "",           // the specific recent thing this email opens on
      "subject": "",
      "content": "",                 // the email body
      "date_sent": "",
      "follow_up_1_subject": "",
      "follow_up_1_content": "",
      "follow_up_1_date": "",
      "follow_up_2_subject": "",
      "follow_up_2_content": "",
      "follow_up_2_date": "",
      "status": "queued",            // queued | sent | replied | bounced | dead | no_response
      "response_notes": ""
    }
  ]
}
```

---

## Workflow (one company at a time)

For each company the user wants to work on:

1. **Open `company/<slug>/tracker.json` and `company/<slug>/research.md`.** Slug derived from `companies_index.json` (sorted by priority).
2. **Research.** Fill `research.md`:
   - Pull the full JD verbatim from `job_url` and save to `jd_full_text` in tracker.json.
   - Identify 10-20 named individuals: mix of senior AI/ML employees (Tier 1), junior/mid AI/ML employees (Tier 3), founders/co-founders for small companies (Tier 2), and HR/recruiters who actively hire (Tier 4). Capture name, role, LinkedIn, verified email (Hunter.io / Apollo). **Never use generic `careers@` / `jobs@` / `hello@`.**
   - For each contact: read their top 4-5 LinkedIn posts (what they argue, what they built, opinions) and Google their name + company in news (interviews, talks, mentions). This per-person research is the source of the cold-email opener.
   - Note the last 60 days of company-level public activity: blog posts, X threads, podcast appearances, product launches, funding moves.
   - Capture 1+ technical detail of theirs that maps to Amit's work (RAG/Milvus/multi-model orchestration/OCR/TinyML — see `chunks.json` for the canonical list of proof points).
3. **Tailor the resume.** Edit `company/<slug>/resume.tex` based on the JD:
   - Rewrite the Professional Summary line to mirror their tech stack.
   - Reorder Technical Skills so the categories they care about come first.
   - Bring up bullets that match; downplay or drop ones that don't (e.g., hardware/IoT bullets for a pure LLM-infra role).
   - Record what was changed and why in `tailoring_notes`.
   - Compile to PDF: `pdflatex resume.tex` (writes `resume.pdf` next to it).
4. **Write contacts and emails.** One contact entry per named person:
   - Pick the right template from `templates and ai avoidance.md` based on tier (1/2/3 = engineering-manager template, 2 = founder template, 4 = recruiter template).
   - Personalize: research_hook → subject → opening line → bridge to Amit's specific work → low-friction ask.
   - **Run every email through the anti-AI vocabulary checklist** in `templates and ai avoidance.md`. Strip every flagged word. Zero em-dashes, zero non-ASCII characters (plain ASCII 32-126 only — em-dashes cause `â€"` encoding corruption in send.py on Windows). No bullets. Vary opening lines across the campaign.
   - Plan follow-up #1 (day 3-4, must add new value, not just "bumping") and #2 (day 10, close-the-loop only).
5. **Space the sends.** Tue-Thu, 8-11 AM or 2-4 PM in the recipient's local time zone. 3-5 days between contacts at the same company. Stop after follow-up #2.
6. **Run `python3 build_index.py`** after meaningful tracker edits to refresh `companies_index.json` (named_contacts and emails_sent counts).

---

## Hard rules (do not violate)

These come from the user's standing feedback and the strategy doc:

- **Per-person, not per-company.** 10-20 named contacts per target. Never `careers@`, `jobs@`, or any generic inbox — same black hole as the ATS.
- **No AI tells.** Every email is screened against the anti-AI vocabulary list in `templates and ai avoidance.md`. The list is the spec, not a suggestion. Read it before writing any email.
- **No placeholder leftovers.** Search for `[`, `{`, "Company Name", "First name" before any send. Cardinal sin.
- **Contact targets are company-size-dependent with hard minimums.**
  - **Companies >50 employees:** Find 2-3 senior AI/ML employees (EMs, tech leads, principal/staff engineers, ML researchers) AND 2-3 junior/mid AI/ML employees (SWEs, ML engineers, data scientists — they reply more and are closer to daily work) AND 2-3 HR/recruiters who actively hire (technical recruiter, talent acquisition, HR business partner). Hard minimum: 6 contacts across all three groups. Never add a founder, CEO, CTO, or any C-suite — they don't screen candidates at this scale.
  - **Companies <=50 employees:** Find 1-2 senior team employees (Tier 1), 1-2 junior/mid team employees (Tier 3), 1-2 founders/co-founders/CTO (Tier 2 — they often interview directly at this size), and 1-2 recruiters/HR (Tier 4). Aim for 6-10 contacts mixing all four groups.
  - For every contact, read their top 4-5 LinkedIn posts and search them in news. The research_hook must come from something specific they wrote or said — not generic company facts.
  - Never cold-email a CEO or founder at a >50-person company.
- **15-25 emails per week, max.** Mass sends collapse reply rates to spam baseline. Hand-tailoring is the whole point.
- **No new docs, plans, or summary files unless the user asks.** Work happens in the existing tracker.json + research.md per company.
- **Skill scope:** only job-hunting tasks are relevant here. Do not invoke dev/code/design gstack skills (`/design-review`, `/qa`, `/ship`, etc.) in this project. They do not apply.

---

## Anti-AI vocabulary — the cut list (load-bearing, do not forget)

Cut every instance in any email or content you generate for Amit:

`delve`, `intricate`, `intricacies`, `pivotal`, `leverage` (as a verb), `robust`, `comprehensive`, `seamlessly`, `harness`, `navigate the landscape`, `journey`, `tapestry`, `testament`, `vibrant`, `underscore`, `showcasing`, `in today's fast-paced world`, `in the realm of`, `it's worth noting that`, `that being said`, `I hope this email finds you well`, `I am writing to express`, `excited to share`, `looking forward to hearing from you`.

Plus: zero em-dashes (not "one max" — zero; em-dashes corrupt to `â€"` in SMTP on Windows), zero non-ASCII characters anywhere in email body or subject (plain ASCII 32-126 only), no bullet lists in cold emails, no three-part parallel triplets, no "it's not X, it's Y" parallelisms, no curly/smart quotes, vary sentence length aggressively.

Full guidance + the 5-step pre-send checklist lives in `templates and ai avoidance.md`. Re-read it before every batch.

---

## Project slash commands (live in `.claude/commands/`, committed to git)

These wrap the per-company workflow so you can drive everything from chat. They are project-local, portable across machines, and travel with the repo.

| Command | What it does |
|---------|--------------|
| `/next-company` | Read `companies_index.json`, print the highest-priority untouched target. |
| `/research-company <slug>` | Chrome-driven deep research. Pulls JD verbatim, maps the team, finds 10-20 named contacts with tier + LinkedIn + best-guess email, captures last-60-days activity. Writes to `tracker.json` + `research.md`. |
| `/tailor-resume <slug>` | Edits `company/<slug>/resume.tex` to mirror the captured JD. Records the diff in `tailoring_notes`. Compiles to `resume.pdf`. |
| `/draft-outreach <slug>` | Writes initial + 2 follow-ups per contact. Runs the anti-AI vocabulary scan as a blocking pre-save check. Leaves status at `queued` for user approval. |
| `/work-company [slug]` | Full pipeline: research → tailor → draft, runs end-to-end without stopping. Only live sending remains for the user. Auto-picks the next target if no slug given. |
| `/outreach-status` | Read-only dashboard. Counts research / drafted / approved / sent / replied across all 166 companies and suggests the next concrete action. |

The canonical workflow on a fresh machine: `claude --chrome`, then `/work-company`. That command does the rest.

---

## Running this on a second machine

The repo is portable — clone it, install the two host requirements, and you're up.

```bash
# 1. Clone
git clone <repo-url> && cd job_hunt

# 2. Install gstack (the .claude/hooks/check-gstack.sh hook requires it)
git clone --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack && ./setup --team && cd -

# 3. Python deps for send.py
pip install python-dotenv

# 4. LaTeX for resume PDF builds
sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# 5. Put your Gmail App Password in .env (NOT committed)
echo "SMTP_PASS=xxxx xxxx xxxx xxxx" > .env

# 6. Open Claude Code with the official Chrome integration
claude --chrome
# (or once running: type /chrome to attach. First run installs Chrome's native messaging host.)
```

After that, the entire pipeline is `/work-company`, then `python3 send.py` to preview, then `python3 send.py --live` once you've flipped approved contacts.

Everything stateful lives in the repo: per-company trackers, research notes, tailored resumes, the index. Push and pull as usual. The only non-repo file is `.env` (intentionally gitignored).

---

## Helper commands

```bash
# Refresh per-company folders from CSVs (idempotent — preserves contacts/research)
python3 setup_companies.py

# Rebuild the priority-sorted master index
python3 build_index.py

# Pick the next company to work on (highest priority not yet contacted):
python3 -c "import json; d=[r for r in json.load(open('companies_index.json')) if r['emails_sent']==0]; print(d[0])"

# Build the PDF for a tailored resume:
cd company/<slug> && pdflatex -interaction=nonstopmode resume.tex && rm -f resume.aux resume.log resume.out

# Send outreach — TEST MODE (all preview emails go to Amit's own Gmail):
python3 send.py                          # all pending emails, all companies, all types
python3 send.py --company sarvam-ai      # scope to one slug
python3 send.py --type initial           # only initial emails
python3 send.py --dry-run                # see the plan without connecting SMTP

# LIVE — actually deliver to real recipients (only contacts with status="approved"):
python3 send.py --live --limit 5         # cap blast radius
python3 send.py --live --rate 60         # 60s between sends
python3 send.py --live --company sarvam-ai
```

---

## How send.py works

Walks every `company/<slug>/tracker.json`. For each contact in `contacts[]`, looks for up to three pending emails (initial, follow_up_1, follow_up_2). An email is "pending" when its subject + content are non-empty and its corresponding sent marker is empty.

**Test mode (default, no flag):** every email is redirected to `amitgohel2002@gmail.com` with subject prefixed `[TEST INIT/FU1/FU2 -> <recipient>]`. No status filter — drafts get previewed too. The tracker is NOT modified. Empty `to` fields are fine. This is the preview path.

**Live mode (`--live`):** real recipients. Status gating per type:
- `initial` requires `contact.status == "approved"`
- `follow_up_1` requires `date_sent` set on the contact
- `follow_up_2` requires `follow_up_1_sent_at` set

On a successful live send, the tracker is updated in place:
- initial → writes `date_sent` and flips `status` to `"sent"`
- follow_up_1 → writes `follow_up_1_sent_at` and flips `status` to `"follow_up_1_sent"`
- follow_up_2 → writes `follow_up_2_sent_at` (status stays where the user manages it)

Each email auto-attaches `company/<slug>/resume.pdf`. If only `resume.tex` is present, it builds the PDF once via `pdflatex` before the first send. Pass `--no-attachment` to skip the attachment entirely.

The contact `status` workflow: `queued` → `approved` (user marks ready) → `sent` (after initial) → `follow_up_1_sent` → user manually flips to `replied` / `no_response` / `dead` / `bounced` as outcomes land. Terminal statuses (`replied`, `bounced`, `dead`) skip all further sends.

---

## Notes

- The `company/openai/` and `company/deepseek/` folders are user-created placeholders that pre-date this setup; they have no tracker.json and are not in either CSV. Leave them unless the user says to delete.
- The `Cold email tracker.json` at the project root is the **schema example** (OpenAI / Anthropic / Perplexity). Treat it as documentation, not data — the real per-company trackers live under `company/<slug>/tracker.json`.
