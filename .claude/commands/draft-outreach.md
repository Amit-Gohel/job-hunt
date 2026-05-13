---
description: Write the initial email + 2 follow-ups for every contact in a company tracker. Run anti-AI vocab pass before saving.
---

# /draft-outreach $ARGUMENTS

Generate cold-email content for every contact in `company/<slug>/tracker.json`. `$ARGUMENTS` is the slug.

## Pre-flight

1. Refuse if `$ARGUMENTS` is empty. Tell the user: "Pass a slug, e.g. `/draft-outreach sarvam-ai`."
2. Read `templates and ai avoidance.md` end-to-end. The anti-AI vocabulary list is the spec.
3. Read `cold email strategy.md` for the subject-line rules and follow-up cadence.
4. Read `company/<slug>/tracker.json`. Confirm:
   - `jd_full_text` is populated
   - `tailoring_notes` is populated (run `/tailor-resume` first if not)
   - `contacts[]` has at least one entry with `contact_name`, `tier`, and `research_hook` filled by `/research-company`
5. Read `chunks.json` and the per-company `resume.tex` for the specific proof points to weave in.

## Per-contact workflow

For every contact in `contacts[]` with `contact_name` filled and `status != "approved"` (don't overwrite already-approved drafts):

### Template choice by tier

- **Tier 1** (engineering manager / tech lead) → Template 3 in `templates and ai avoidance.md`
- **Tier 2** (founder / CEO / CTO at sub-50-person startup) → Template 1
- **Tier 3** (IC / senior engineer) → Template 3 (slightly shorter, ask is "you should talk to X")
- **Tier 4** (recruiter) → Template 2

### Fill these fields per contact

- `subject` — under 8 words, lowercase or sentence case, specific. Pull from the `research_hook` and the JD's tech stack. No two contacts in this campaign share the same subject. No "Quick question", no "Application for", no emojis.
- `content` — three short paragraphs max:
  1. Opener that references the contact's specific recent activity (from `research_hook`)
  2. One bridge sentence from that to Amit's relevant production work (use specific numbers — "95% MRR on 50K+ queries/month", "BGE-M3 after benchmarking 6 embedding models", etc.)
  3. Low-friction ask ("Open to a 15-min call next Tuesday or Thursday?" — not "let me know if interested!")
- `follow_up_1_subject` — `re: <original subject>`
- `follow_up_1_content` — short. Adds one new thing (a benchmark Amit shipped that week, a thought on their latest post, a public link). Never just "bumping this."
- `follow_up_1_date` — initial send date + 3 or 4 days (planned; send.py will write actual `follow_up_1_sent_at`).
- `follow_up_2_subject` — `re: <original subject>`
- `follow_up_2_content` — even shorter. Close the loop, no new ask: "Last note. If now's not the right time, would still appreciate being on your radar."
- `follow_up_2_date` — initial send date + 10 days.

### Vary across the campaign

For every batch of contacts across the company:
- No two openers start with the same phrase. Mix: "Saw your...", "Came across...", "Quick one —", "Going through... this week and...", "[Mutual connection] mentioned...", "Was reading... and remembered..."
- Vary sentence length aggressively. Short sentences. Then one longer sentence that twists a bit. Then a fragment.
- Mention 2-3 concrete proof points per email (numbers, library names, products). Generic phrasing is the AI tell.

### Anti-AI pre-save check (BLOCKING)

Before writing the email back to `tracker.json`, run a vocabulary scan. **Reject and rewrite** any draft that contains:

`delve`, `intricate`, `pivotal`, `leverage` (verb), `robust`, `comprehensive`, `seamlessly`, `harness`, `navigate the landscape`, `journey`, `tapestry`, `testament`, `vibrant`, `underscore`, `showcasing`, `in today's fast-paced world`, `in the realm of`, `it's worth noting that`, `that being said`, `I hope this email finds you well`, `I am writing to express`, `excited to share`, `looking forward to hearing from you`.

Also reject:
- More than one em-dash in a single email
- Any bullet list inside an email body
- Three-part parallel triplets ("built, deployed, and scaled")
- The pattern "It's not X, it's Y"
- Any leftover `[brackets]`, `{braces}`, "Company Name", "First name" — cardinal sin
- Curly quotes / smart quotes

Re-draft until clean. Don't save junk and "fix later."

### Set status

After all three emails are clean for a contact, do NOT auto-set `status = "approved"`. Leave it at `queued`. The user manually flips to `approved` after reviewing — this is the gate before `send.py --live` will deliver.

## After

- Save `tracker.json`.
- Run `python3 build_index.py` to refresh the master index.
- Print a summary table: contact name | tier | subject | "anti-AI scan: PASS".
- Tell the user: "Drafts written for `<slug>` (N contacts). Review in `company/<slug>/tracker.json`. When ready, set `status='approved'` per contact and run `python3 send.py` (test) or `python3 send.py --live --company <slug>`."

## Hard rules

- Three paragraphs max per email. Subject under 8 words.
- One em-dash per email max. Zero is better.
- No bullets in email bodies.
- No leftover placeholders. Search for `[`, `{`, "Company Name", "First name" before saving.
- Anti-AI vocab list is BLOCKING, not advisory. Rewrite until clean.
- Never set `status = "approved"` automatically. That's the user's manual gate.
