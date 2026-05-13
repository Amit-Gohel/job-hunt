---
description: Campaign dashboard. Counts research / drafted / approved / sent / replied across all 166 companies.
---

# /outreach-status

Read-only snapshot of the outreach campaign.

## Steps

1. Run `python3 build_index.py` to refresh `companies_index.json`.
2. Walk every `company/<slug>/tracker.json` and aggregate:
   - **Research:** count of companies where `research_status == "done"`
   - **Drafted:** count of companies where at least one contact has non-empty `subject` + `content`
   - **Approved:** count of companies where at least one contact has `status == "approved"`
   - **Sent:** count of companies where at least one contact has non-empty `date_sent`
   - **Replied:** count of companies where at least one contact has `status == "replied"`
   - **Bounced/Dead:** count of contacts (not companies) in those terminal states
3. Print a table summary, plus:
   - Top 10 highest-priority companies still at `research_status == "not_started"`
   - Companies with at least one contact awaiting follow-up (i.e. `date_sent` set, no `follow_up_1_sent_at` yet, and >= 3 days since `date_sent`)
   - Companies with at least one contact awaiting follow-up 2 (i.e. `follow_up_1_sent_at` set, no `follow_up_2_sent_at`, and >= 7 days since `follow_up_1_sent_at`)
4. Suggest one concrete next action based on what's most behind. Examples:
   - "5 companies have research done but no drafts. Run `/draft-outreach <slug>` on the highest priority next."
   - "12 contacts are overdue for follow-up #1. Approve and run `python3 send.py --live --type follow_up_1 --limit 5`."
   - "No companies researched yet. Start with `/next-company`."

## Output format

Keep it under 30 lines. Numbers + the suggested next action. No prose.

## Hard rules

- Do not modify any tracker file. Read-only.
- If `companies_index.json` is missing, build it first.
