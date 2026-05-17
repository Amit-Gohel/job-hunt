---
description: Full pipeline for one company — research, tailor resume, draft outreach — runs end-to-end without stopping. Only live sending remains for the user.
---

# /work-company $ARGUMENTS

Run the entire per-company pipeline autonomously from research through drafted outreach. `$ARGUMENTS` is the slug; if empty, auto-pick the top untouched record from `companies_index.json`. Do NOT stop or ask for approval between stages — run all three stages back-to-back and only stop when drafts are saved and ready to send.

## Pre-flight

1. Confirm Chrome is connected (the user ran `claude --chrome` or `/chrome`). If chrome tools are not available, stop and tell the user to connect first.
2. If `$ARGUMENTS` is empty, run the logic from `/next-company` to pick a slug. Print which slug was chosen and proceed immediately — do not wait for user confirmation.
3. If the chosen slug already has `research_status == "done"` AND `tailoring_notes` populated AND every contact has `subject` and `content` filled, tell the user "Pipeline already complete for `<slug>`. Only live sending is pending." and stop.

## Stage 1 — Research (no pause)

1. Run the steps in `.claude/commands/research-company.md` for `<slug>`.
2. Print a one-line progress note when done: "Research done — N contacts captured across tiers X/Y/Z."
3. Proceed immediately to Stage 2. Do NOT ask for approval.

## Stage 2 — Tailor resume (no pause)

1. Run the steps in `.claude/commands/tailor-resume.md` for `<slug>`.
2. Print a one-line progress note when done: "Resume tailored and PDF compiled at company/<slug>/resume.pdf."
3. Proceed immediately to Stage 3. Do NOT ask for approval.

## Stage 3 — Draft outreach (final stop)

1. Run the steps in `.claude/commands/draft-outreach.md` for `<slug>`.
2. When done, print a summary table:
   - Contact name | tier | subject | "anti-AI scan: PASS"
3. Tell the user:

   "Pipeline complete for `<slug>`. All drafts saved with `status='queued'`. Only sending is left:
   - Review contacts in `company/<slug>/tracker.json` if you want.
   - Set `status='approved'` on each contact you want to send.
   - Run `python3 send.py --company <slug>` to preview (test mode — sends to your inbox).
   - Run `python3 send.py --live --company <slug>` to deliver for real."

4. Stop here. Never auto-approve or auto-send.

## Hard rules

- No blocking review gates between Stage 1, 2, or 3. Run all three without pausing.
- Never set `status = "approved"` automatically.
- Never call `send.py --live` from inside this command.
- If any stage fails or errors, surface the error clearly and stop — do not skip to the next stage silently.
- This command is re-runnable. Re-running on an already-researched company must not stomp existing data — each sub-command has its own idempotence rules.
