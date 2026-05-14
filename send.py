#!/usr/bin/env python3
"""
send.py — Send outreach emails from per-company tracker.json files.

Walks every company/<slug>/tracker.json and discovers all pending emails:
initial, follow_up_1, follow_up_2 — one send per contact per type.

Two modes:

  TEST MODE (default — no flag):
    - Every email is redirected to amitgohel2002@gmail.com so you can preview.
    - Subject prefixed with [TEST <type> -> <recipient>] for easy inbox triage.
    - No status filter (drafts are previewed too). Tracker is NOT modified.
    - Empty `to` is fine — preview-only.

  LIVE MODE (--live flag):
    - Email goes to the real `to` in each contact entry.
    - Status gating per email type:
        initial: contact.status == "approved"
        follow_up_1: contact.status in {"sent", "follow_up_1_sent"} AND date_sent set
        follow_up_2: contact.follow_up_1_sent_at set
    - Bounce/reply/dead states are always skipped.
    - On successful send, the tracker is updated in place:
        initial -> date_sent + status="sent"
        follow_up_1 -> follow_up_1_sent_at + status="follow_up_1_sent"
        follow_up_2 -> follow_up_2_sent_at
    - Refuses entries with blank `to` in live mode.

Resume:
  Each contact's email attaches company/<slug>/resume.pdf. If only resume.tex
  exists, pdflatex builds it once (twice for refs) before the first send.

Setup:
  1. Put your Gmail App Password in .env at project root:
         SMTP_PASS=xxxx xxxx xxxx xxxx
     (Generate at https://myaccount.google.com/apppasswords — needs 2FA.)
  2. Fill subject + content in company/<slug>/tracker.json contacts. Mark
     status="approved" to make a contact's initial email live-eligible.
  3. Run:
         python3 send.py                          # test mode (default)
         python3 send.py --live                   # actually send
         python3 send.py --company sarvam-ai      # only this slug
         python3 send.py --type initial           # only initial emails
         python3 send.py --type follow_up_1
         python3 send.py --type follow_up_2
         python3 send.py --limit 5                # cap to 5 sends
         python3 send.py --rate 60                # 60s between sends
         python3 send.py --dry-run                # plan only, no SMTP
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import smtplib
import ssl
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from email.utils import formataddr, make_msgid
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "amitgohel2002@gmail.com"
FROM_EMAIL = "amitgohel2002@gmail.com"
FROM_NAME = "Amit Gohel"
TEST_TARGET = "amitgohel2002@gmail.com"
RATE_LIMIT_SECONDS = 45

COMPANY_DIR = ROOT / "company"

EMAIL_TYPES = ("initial", "follow_up_1", "follow_up_2")
TERMINAL_STATUSES = {"replied", "bounced", "dead"}


@dataclass
class SendUnit:
    """One pending email to send."""
    company_slug: str
    company_name: str
    folder: Path
    tracker_path: Path
    contact_index: int
    contact: dict
    email_type: str           # initial | follow_up_1 | follow_up_2
    subject: str
    body: str
    to_addr: str              # actual recipient in live; ignored in test
    cc: list[str]


# ---------- PDF build ----------------------------------------------------

def build_pdf(tex_path: Path) -> Path:
    pdf_path = tex_path.with_suffix(".pdf")
    if pdf_path.exists() and pdf_path.stat().st_mtime >= tex_path.stat().st_mtime:
        return pdf_path
    if shutil.which("pdflatex") is None:
        sys.exit(
            "ERROR: pdflatex not installed.\n"
            "  sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended"
        )
    print(f"  building {pdf_path.name}")
    for _ in range(2):
        result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-output-directory", str(tex_path.parent),
                str(tex_path),
            ],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            tail = (result.stdout or "")[-1500:]
            sys.exit(f"ERROR: pdflatex failed for {tex_path}:\n{tail}")
    # cleanup aux files
    for suffix in (".aux", ".log", ".out"):
        aux = tex_path.with_suffix(suffix)
        if aux.exists():
            aux.unlink()
    return pdf_path


# ---------- Tracker discovery -------------------------------------------

def _email_payload(contact: dict, email_type: str) -> tuple[str, str]:
    if email_type == "initial":
        return contact.get("subject", "") or "", contact.get("content", "") or ""
    if email_type == "follow_up_1":
        return (
            contact.get("follow_up_1_subject", "") or "",
            contact.get("follow_up_1_content", "") or "",
        )
    if email_type == "follow_up_2":
        return (
            contact.get("follow_up_2_subject", "") or "",
            contact.get("follow_up_2_content", "") or "",
        )
    raise ValueError(email_type)


def _is_sent(contact: dict, email_type: str) -> bool:
    if email_type == "initial":
        return bool((contact.get("date_sent") or "").strip())
    if email_type == "follow_up_1":
        return bool((contact.get("follow_up_1_sent_at") or "").strip())
    if email_type == "follow_up_2":
        return bool((contact.get("follow_up_2_sent_at") or "").strip())
    raise ValueError(email_type)


def _live_eligible(contact: dict, email_type: str) -> tuple[bool, str]:
    status = (contact.get("status") or "").strip().lower()
    if status in TERMINAL_STATUSES:
        return False, f"status={status}"
    if email_type == "initial":
        if status != "approved":
            return False, f"status={status or 'empty'} (need approved)"
        return True, ""
    if email_type == "follow_up_1":
        if not (contact.get("date_sent") or "").strip():
            return False, "initial not sent yet"
        return True, ""
    if email_type == "follow_up_2":
        if not (contact.get("follow_up_1_sent_at") or "").strip():
            return False, "follow_up_1 not sent yet"
        return True, ""
    return False, "unknown type"


def discover_sends(
    live_mode: bool,
    company_filter: str | None,
    types_filter: set[str],
) -> tuple[list[SendUnit], list[str]]:
    """Walk every tracker.json. Return pending sends + reasons for skips."""
    units: list[SendUnit] = []
    skips: list[str] = []

    if not COMPANY_DIR.exists():
        sys.exit(f"ERROR: company directory missing: {COMPANY_DIR}")

    for folder in sorted(COMPANY_DIR.iterdir()):
        if not folder.is_dir():
            continue
        slug = folder.name
        if company_filter and slug != company_filter:
            continue
        tracker_path = folder / "tracker.json"
        if not tracker_path.exists():
            continue
        try:
            data = json.loads(tracker_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            skips.append(f"{slug}: tracker.json invalid ({exc})")
            continue
        company_name = data.get("company_name") or slug
        contacts = data.get("contacts") or []
        for idx, contact in enumerate(contacts):
            for email_type in EMAIL_TYPES:
                if email_type not in types_filter:
                    continue
                subject, body = _email_payload(contact, email_type)
                if not subject.strip() or not body.strip():
                    continue  # nothing drafted yet — silent skip
                if _is_sent(contact, email_type):
                    skips.append(
                        f"{slug}#{idx} {email_type}: already sent "
                        f"({contact.get('contact_name') or contact.get('to') or '?'})"
                    )
                    continue
                if live_mode:
                    ok, reason = _live_eligible(contact, email_type)
                    if not ok:
                        skips.append(
                            f"{slug}#{idx} {email_type}: {reason} "
                            f"({contact.get('contact_name') or contact.get('to') or '?'})"
                        )
                        continue
                    to_addr = (contact.get("to") or "").strip()
                    if not to_addr:
                        skips.append(f"{slug}#{idx} {email_type}: to empty (live)")
                        continue
                else:
                    to_addr = (contact.get("to") or "").strip()  # may be empty
                cc = [c.strip() for c in (contact.get("cc") or []) if isinstance(c, str) and c.strip()]

                # Build one SendUnit per address: primary + all permutations
                all_addresses = [to_addr] if to_addr else []
                for perm in (contact.get("to_permutations") or []):
                    perm = perm.strip()
                    if perm and perm not in all_addresses:
                        all_addresses.append(perm)
                if not all_addresses:
                    all_addresses = [""]  # keep one empty slot for test-mode preview

                for addr in all_addresses:
                    units.append(SendUnit(
                        company_slug=slug,
                        company_name=company_name,
                        folder=folder,
                        tracker_path=tracker_path,
                        contact_index=idx,
                        contact=contact,
                        email_type=email_type,
                        subject=subject.strip(),
                        body=body,
                        to_addr=addr,
                        cc=cc,
                    ))
    return units, skips


# ---------- Message build ------------------------------------------------

def build_message(unit: SendUnit, live_mode: bool, pdf_path: Path | None) -> tuple[EmailMessage, list[str]]:
    msg = EmailMessage()
    msg["From"] = formataddr((FROM_NAME, FROM_EMAIL))

    recipient_label = unit.contact.get("contact_name") or unit.to_addr or "unknown"
    if live_mode:
        to_addr = unit.to_addr
        subject = unit.subject
        cc = list(unit.cc)
    else:
        to_addr = TEST_TARGET
        type_tag = {"initial": "INIT", "follow_up_1": "FU1", "follow_up_2": "FU2"}[unit.email_type]
        addr_label = f" ({unit.to_addr})" if unit.to_addr else ""
        subject = f"[TEST {type_tag} -> {recipient_label}{addr_label}] {unit.subject}"
        cc = []

    msg["To"] = to_addr
    if cc:
        msg["Cc"] = ", ".join(cc)
    if live_mode:
        msg["Bcc"] = FROM_EMAIL  # silent copy to sender on every live send
    msg["Subject"] = subject
    msg["Reply-To"] = FROM_EMAIL
    msg["Message-ID"] = make_msgid(domain=FROM_EMAIL.split("@", 1)[1])

    msg.set_content(unit.body)

    # HTML alternative — paragraphs wrapped in <p>, URLs made clickable
    def _to_html(text: str) -> str:
        paragraphs = text.strip().split("\n\n")
        parts = []
        for p in paragraphs:
            # escape first, then convert newlines to <br> so tags aren't escaped
            escaped = html.escape(p).replace("\n", "<br>")
            escaped = re.sub(
                r'(https?://[^\s<&]+)',
                r'<a href="\1">\1</a>',
                escaped,
            )
            parts.append(f"<p>{escaped}</p>")
        body_html = "\n".join(parts)
        return (
            '<html><body style="font-family:Arial,sans-serif;font-size:14px;line-height:1.6;color:#1a1a1a">'
            f"{body_html}"
            "</body></html>"
        )

    msg.add_alternative(_to_html(unit.body), subtype="html")

    if pdf_path is not None and pdf_path.exists():
        filename = f"Amit_Gohel_Resume_{unit.company_slug}.pdf"
        msg.add_attachment(
            pdf_path.read_bytes(),
            maintype="application",
            subtype="pdf",
            filename=filename,
        )

    envelope_to = [to_addr, *cc]
    return msg, envelope_to


# ---------- Tracker write-back ------------------------------------------

def update_tracker_after_send(unit: SendUnit) -> None:
    """Re-read, mutate, write-back (avoids stomping concurrent edits in this file)."""
    data = json.loads(unit.tracker_path.read_text(encoding='utf-8'))
    contacts = data.get("contacts") or []
    if unit.contact_index >= len(contacts):
        return
    contact = contacts[unit.contact_index]
    today = datetime.now(timezone.utc).date().isoformat()
    if unit.email_type == "initial":
        contact["date_sent"] = today
        contact["status"] = "sent"
    elif unit.email_type == "follow_up_1":
        contact["follow_up_1_sent_at"] = today
        contact["status"] = "follow_up_1_sent"
    elif unit.email_type == "follow_up_2":
        contact["follow_up_2_sent_at"] = today
        # status stays where user manages it
    contacts[unit.contact_index] = contact
    data["contacts"] = contacts
    unit.tracker_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


# ---------- Main ---------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Send outreach emails (test mode by default).")
    parser.add_argument("--live", action="store_true",
                        help="LIVE mode: send to real recipients. Default = TEST mode (everything to your Gmail).")
    parser.add_argument("--company", help="Only process this slug (e.g. sarvam-ai).")
    parser.add_argument("--type", choices=("initial", "follow_up_1", "follow_up_2", "all"),
                        default="all", help="Restrict to one email type. Default: all.")
    parser.add_argument("--limit", type=int, help="Stop after this many sends.")
    parser.add_argument("--rate", type=float, default=RATE_LIMIT_SECONDS,
                        help=f"Seconds between sends (default {RATE_LIMIT_SECONDS}).")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the plan and quit. No SMTP connection, no sends.")
    parser.add_argument("--no-attachment", action="store_true",
                        help="Do not attach the resume PDF.")
    parser.add_argument("--show-skips", action="store_true",
                        help="Print full skip list (default: only count).")
    args = parser.parse_args()

    live_mode = args.live
    mode_label = "LIVE" if live_mode else "TEST"
    types_filter = set(EMAIL_TYPES) if args.type == "all" else {args.type}

    smtp_pass = os.environ.get("SMTP_PASS")
    if not smtp_pass and not args.dry_run:
        sys.exit(
            "ERROR: SMTP_PASS not set.\n"
            "  Put it in .env: SMTP_PASS=xxxx xxxx xxxx xxxx\n"
            "  Generate at https://myaccount.google.com/apppasswords (needs 2FA)."
        )

    units, skips = discover_sends(live_mode, args.company, types_filter)

    print(f"Mode: {mode_label}")
    if live_mode:
        print("  -> Emails go to the real `to` in each contact.")
        print("  -> Status gating: initial needs status='approved'; follow-ups need prior sends.")
        print("  -> Tracker is updated after each successful send.")
    else:
        print(f"  -> All emails redirected to {TEST_TARGET}")
        print("  -> Subject prefixed with [TEST <type> -> <recipient>]")
        print("  -> No status gating. Tracker is NOT modified.")
        print("  -> Pass --live to actually send to real recipients.")
    print(f"  -> Type filter: {sorted(types_filter)}")
    if args.company:
        print(f"  -> Company filter: {args.company}")
    print(f"\nPending sends: {len(units)}. Skipped: {len(skips)}.")
    if skips and args.show_skips:
        for s in skips:
            print(f"  SKIP {s}")
    elif skips:
        print(f"  (re-run with --show-skips to see all {len(skips)} skip reasons)")

    if not units:
        print("\nNothing to send.")
        return

    # Per-company breakdown
    print("\nBy company:")
    by_company: dict[str, dict[str, int]] = {}
    for u in units:
        by_company.setdefault(u.company_slug, {}).setdefault(u.email_type, 0)
        by_company[u.company_slug][u.email_type] += 1
    for slug in sorted(by_company):
        parts = ", ".join(f"{t}={n}" for t, n in sorted(by_company[slug].items()))
        print(f"  {slug}: {parts}")

    if args.dry_run:
        print("\n--dry-run: stopping before SMTP.")
        return

    if live_mode:
        print(f"\n!!! LIVE SEND of {len(units)} email(s). Ctrl-C in the next 5 seconds to cancel.")
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            print("Cancelled.")
            return

    # Pre-build PDFs once per company we'll touch
    pdfs: dict[str, Path | None] = {}
    if not args.no_attachment:
        for u in units:
            if u.company_slug in pdfs:
                continue
            tex = u.folder / "resume.tex"
            if not tex.exists():
                pdfs[u.company_slug] = None
                print(f"  WARN no resume.tex in {u.folder} — sending without attachment")
                continue
            pdfs[u.company_slug] = build_pdf(tex)

    print(f"\nConnecting to {SMTP_HOST}:{SMTP_PORT} as {SMTP_USER}")
    context = ssl.create_default_context()
    sent = 0
    failed = 0

    def _connect() -> smtplib.SMTP:
        s = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30)
        s.starttls(context=context)
        s.login(SMTP_USER, smtp_pass)
        return s

    smtp = _connect()
    try:
        for n, u in enumerate(units, 1):
            if args.limit and sent + failed >= args.limit:
                print(f"Hit --limit={args.limit}, stopping.")
                break
            pdf_path = None if args.no_attachment else pdfs.get(u.company_slug)
            msg, envelope_to = build_message(u, live_mode, pdf_path)
            actual_to = envelope_to[0] if envelope_to else "?"
            label = (
                f"[{n}/{len(units)}] {u.company_slug}#{u.contact_index} "
                f"{u.email_type} / {u.contact.get('contact_name') or u.to_addr or '?'}"
            )
            try:
                if sent + failed > 0:
                    time.sleep(args.rate)
                smtp.send_message(msg, from_addr=FROM_EMAIL, to_addrs=envelope_to)
                sent += 1
                print(f"SENT {label} -> {actual_to}")
                # Only update tracker status for the primary address (first in list)
                primary_to = (u.contact.get("to") or "").strip()
                if live_mode and u.to_addr == primary_to:
                    update_tracker_after_send(u)
            except (smtplib.SMTPServerDisconnected, smtplib.SMTPException, OSError, ssl.SSLError) as exc:
                print(f"FAIL {label}: {exc} — reconnecting...")
                try:
                    smtp.quit()
                except Exception:
                    pass
                try:
                    smtp = _connect()
                    smtp.send_message(msg, from_addr=FROM_EMAIL, to_addrs=envelope_to)
                    sent += 1
                    print(f"SENT {label} -> {actual_to} (after reconnect)")
                    primary_to = (u.contact.get("to") or "").strip()
                    if live_mode and u.to_addr == primary_to:
                        update_tracker_after_send(u)
                except Exception as exc2:
                    failed += 1
                    print(f"FAIL {label}: {exc2} (gave up)")
                    continue
    finally:
        try:
            smtp.quit()
        except Exception:
            pass

    print(f"\nDone. mode={mode_label} sent={sent} failed={failed}")


if __name__ == "__main__":
    main()
