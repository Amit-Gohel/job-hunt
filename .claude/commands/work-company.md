---
description: Full pipeline for one company — research, tailor resume, draft outreach. Pauses for user review at each stage.
---

# /work-company $ARGUMENTS

Run the entire per-company pipeline end-to-end with user-review pauses. `$ARGUMENTS` is the slug; if empty, auto-pick the top untouched record from `companies_index.json`.

## Pre-flight

1. Confirm Chrome is connected (the user ran `claude --chrome` or `/chrome`). If chrome tools are not available, stop and tell the user to connect first.
2. If `$ARGUMENTS` is empty, run the logic from `/next-company` to pick a slug. Print which slug was chosen and proceed.
3. If the chosen slug already has `research_status == "done"` AND `tailoring_notes` populated AND every contact has `subject` and `content` filled, ask the user: "Pipeline already complete for `<slug>`. Re-run anyway? (y/N)". Default to N.

## Stage 1 — Research (BLOCKING review)

1. Run the steps in `.claude/commands/research-company.md` for `<slug>`.
2. When done, print:
   - Number of contacts captured per tier
   - The `research_summary` field
   - The list of contact names with their `research_hook`
3. Ask the user: "Research saved to `company/<slug>/tracker.json` and `research.md`. Approve to proceed to resume tailoring? (y/N)"
4. Do NOT proceed until the user says yes. If the user wants edits, stop and let them edit, then they re-run `/work-company <slug>`.

## Stage 2 — Tailor resume (BLOCKING review)

1. Run the steps in `.claude/commands/tailor-resume.md` for `<slug>`.
2. When done, print:
   - The `tailoring_notes` summary
   - Path to the built PDF
3. Ask the user: "Resume tailored. Open `company/<slug>/resume.pdf` to review, then approve to proceed to drafting? (y/N)"
4. Do NOT proceed until the user says yes.

## Stage 3 — Draft outreach (BLOCKING review)

1. Run the steps in `.claude/commands/draft-outreach.md` for `<slug>`.
2. When done, print a table:
   - Contact name | tier | subject | "anti-AI scan: PASS"
3. Tell the user: "Drafts saved with `status='queued'`. Review each contact in `company/<slug>/tracker.json`. When you're happy:
   - Set `status='approved'` per contact you want to live-send.
   - Run `python3 send.py --company <slug>` (test mode — previews to your inbox).
   - Then `python3 send.py --live --company <slug>` to send for real.
   "
4. Stop. The pipeline does NOT auto-approve or auto-send. Sending is always a separate, user-driven step.

## Hard rules

- Three blocking review gates. Never skip them.
- Never set `status = "approved"` automatically.
- Never call `send.py --live` from inside this command.
- If a stage's command file (`/research-company`, etc.) fails or stops early, surface the error and let the user decide whether to retry.
- This command must be re-runnable. Re-running on an already-researched company should not stomp existing data — each sub-command has its own idempotence rules.
