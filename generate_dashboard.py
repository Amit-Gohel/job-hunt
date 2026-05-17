#!/usr/bin/env python3
"""Generate a self-contained HTML dashboard from all company tracker.json files."""

import json
import os
import glob
from pathlib import Path

BASE = Path(__file__).parent

def load_all_trackers():
    trackers = []
    for path in sorted(glob.glob(str(BASE / "company" / "*" / "tracker.json"))):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            data["_path"] = path
            trackers.append(data)
        except Exception as e:
            print(f"Skip {path}: {e}")
    return trackers

def status_color(status):
    colors = {
        "sent": "#22c55e",
        "replied": "#3b82f6",
        "approved": "#f59e0b",
        "queued": "#8b5cf6",
        "bounced": "#ef4444",
        "dead": "#6b7280",
        "no_response": "#f97316",
        "": "#94a3b8",
    }
    return colors.get(status or "", "#94a3b8")

def tier_label(tier):
    labels = {"1": "EM/Lead", "2": "Founder", "3": "IC", "4": "Recruiter"}
    return labels.get(str(tier), str(tier))

def tier_color(tier):
    colors = {"1": "#ef4444", "2": "#f59e0b", "3": "#22c55e", "4": "#3b82f6"}
    return colors.get(str(tier), "#94a3b8")

def research_badge(status):
    colors = {"done": "#22c55e", "in_progress": "#f59e0b", "not_started": "#6b7280"}
    return colors.get(status, "#6b7280")

def escape_js(s):
    if not s:
        return ""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

def make_company_card(t):
    slug = t.get("slug", "")
    name = t.get("company_name", slug)
    meta = t.get("metadata", {})
    contacts = t.get("contacts", [])
    rs = t.get("research_status", "not_started")
    emails_sent = sum(1 for c in contacts if c.get("date_sent"))
    total_contacts = len(contacts)
    statuses = {}
    for c in contacts:
        s = c.get("status", "")
        statuses[s] = statuses.get(s, 0) + 1

    dots = ""
    for s, count in statuses.items():
        dots += f'<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{status_color(s)};margin:0 2px;title="{s}"></span>'

    return f"""<div class="company-card" data-slug="{slug}" data-rs="{rs}" onclick="showCompany('{slug}')">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px">
    <div>
      <div class="company-name">{name}</div>
      <div class="company-meta">{meta.get('location','')}{' · ' + meta.get('role_title','') if meta.get('role_title') else ''}</div>
    </div>
    <span class="badge" style="background:{research_badge(rs)};white-space:nowrap">{rs.replace('_',' ')}</span>
  </div>
  <div style="margin-top:8px;display:flex;justify-content:space-between;align-items:center">
    <div>{dots}</div>
    <div style="font-size:11px;color:#94a3b8">{emails_sent}/{total_contacts} sent · P{meta.get('priority_score','?')}</div>
  </div>
</div>"""

def make_contact_block(c, idx):
    name = c.get("contact_name", "")
    role = c.get("contact_role", "")
    tier = str(c.get("tier", ""))
    status = c.get("status", "")
    email = c.get("to", "")
    linkedin = c.get("linkedin", "")
    hook = c.get("research_hook", "")
    subject = c.get("subject", "")
    content = c.get("content", "")
    date_sent = c.get("date_sent", "")
    fu1_sub = c.get("follow_up_1_subject", "")
    fu1_content = c.get("follow_up_1_content", "")
    fu1_date = c.get("follow_up_1_date", "")
    fu1_sent = c.get("follow_up_1_sent_at", "")
    fu2_sub = c.get("follow_up_2_subject", "")
    fu2_content = c.get("follow_up_2_content", "")
    fu2_date = c.get("follow_up_2_date", "")
    fu2_sent = c.get("follow_up_2_sent_at", "")
    response = c.get("response_notes", "")

    def email_card(label, sub, body, sched, sent_at):
        if not sub and not body:
            return ""
        sent_indicator = f'<span style="color:#22c55e;font-size:11px">sent {sent_at}</span>' if sent_at else (f'<span style="color:#f59e0b;font-size:11px">sched {sched}</span>' if sched else '')
        return f"""<div class="email-card">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
    <span style="font-size:11px;font-weight:600;color:#94a3b8;text-transform:uppercase;letter-spacing:.05em">{label}</span>
    {sent_indicator}
  </div>
  <div style="font-size:12px;color:#e2e8f0;margin-bottom:4px"><strong>Subject:</strong> {sub}</div>
  <div class="email-body">{body.replace(chr(10), '<br>')}</div>
</div>"""

    linkedin_link = f'<a href="{linkedin}" target="_blank" style="color:#60a5fa;font-size:11px">LinkedIn</a>' if linkedin else ""

    return f"""<div class="contact-block">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:6px">
    <div>
      <span style="font-weight:600;color:#f1f5f9">{name}</span>
      <span style="font-size:12px;color:#94a3b8;margin-left:8px">{role}</span>
    </div>
    <div style="display:flex;gap:6px;align-items:center;flex-wrap:wrap">
      <span class="tier-badge" style="background:{tier_color(tier)}">{tier_label(tier)}</span>
      <span class="badge" style="background:{status_color(status)}">{status or 'no status'}</span>
      {linkedin_link}
    </div>
  </div>
  {'<div style="margin-top:6px;font-size:11px;color:#64748b"><strong>Email:</strong> ' + email + '</div>' if email else '<div style="margin-top:6px;font-size:11px;color:#ef4444">No email found</div>'}
  {'<div style="margin-top:4px;font-size:11px;color:#64748b;border-left:2px solid #334155;padding-left:8px;margin-top:6px"><em>' + hook + '</em></div>' if hook else ''}
  {email_card("Initial Email", subject, content, "", date_sent)}
  {email_card("Follow-up 1", fu1_sub, fu1_content, fu1_date, fu1_sent)}
  {email_card("Follow-up 2", fu2_sub, fu2_content, fu2_date, fu2_sent)}
  {'<div style="margin-top:8px;padding:8px;background:#1e293b;border-radius:6px;font-size:12px;color:#fbbf24"><strong>Response:</strong> ' + response + '</div>' if response else ''}
</div>"""

def make_detail_panel(t):
    slug = t.get("slug", "")
    name = t.get("company_name", slug)
    meta = t.get("metadata", {})
    contacts = t.get("contacts", [])
    rs = t.get("research_status", "not_started")
    summary = t.get("research_summary", "")
    jd = t.get("jd_full_text", "")
    tailoring = t.get("tailoring_notes", "")
    resume_path = t.get("resume_latex_path", "")
    resume_pdf = t.get("resume_pdf_path", "")

    meta_items = [
        ("Location", meta.get("location", "")),
        ("Role", meta.get("role_title", "")),
        ("Salary", meta.get("salary_range_lpa", "")),
        ("Funding", meta.get("funding_stage", "")),
        ("Hiring", meta.get("hiring_status", "")),
        ("Priority", str(meta.get("priority_score", ""))),
        ("Source CSV", meta.get("_source_csv", "")),
    ]
    meta_html = "".join(
        f'<div class="meta-item"><span class="meta-label">{k}</span><span class="meta-value">{v}</span></div>'
        for k, v in meta_items if v
    )

    match_reason = meta.get("match_reason", "")
    angle = meta.get("cold_outreach_angle", "")
    notes = meta.get("notes", "")
    careers = meta.get("careers_page", "")
    job_url = meta.get("job_url", "")
    linkedin_co = meta.get("linkedin_company_page", "")

    links_html = ""
    if careers:
        links_html += f'<a href="{careers}" target="_blank" class="ext-link">Careers page</a>'
    if job_url:
        links_html += f'<a href="{job_url}" target="_blank" class="ext-link">Job URL</a>'
    if linkedin_co:
        links_html += f'<a href="{linkedin_co}" target="_blank" class="ext-link">LinkedIn</a>'

    contacts_html = "".join(make_contact_block(c, i) for i, c in enumerate(contacts))

    total = len(contacts)
    sent_count = sum(1 for c in contacts if c.get("date_sent"))
    replied_count = sum(1 for c in contacts if c.get("status") == "replied")
    approved_count = sum(1 for c in contacts if c.get("status") == "approved")
    queued_count = sum(1 for c in contacts if c.get("status") == "queued")

    return f"""<div id="detail-{slug}" class="detail-panel" style="display:none">
  <div class="detail-header">
    <div>
      <h2 style="margin:0;color:#f1f5f9">{name}</h2>
      <div style="font-size:13px;color:#94a3b8;margin-top:2px">{meta.get('location','')} · {meta.get('role_title','')}</div>
    </div>
    <span class="badge" style="background:{research_badge(rs)};font-size:13px;padding:4px 10px">{rs.replace('_',' ')}</span>
  </div>

  <div class="section">
    <div class="meta-grid">{meta_html}</div>
    {('<div style="margin-top:8px">' + links_html + '</div>') if links_html else ''}
  </div>

  {'<div class="section"><div class="section-title">Match Reason</div><p class="prose">' + match_reason + '</p></div>' if match_reason else ''}
  {'<div class="section"><div class="section-title">Outreach Angle</div><p class="prose">' + angle + '</p></div>' if angle else ''}
  {'<div class="section"><div class="section-title">Notes</div><p class="prose">' + notes + '</p></div>' if notes else ''}
  {'<div class="section"><div class="section-title">Research Summary</div><p class="prose">' + summary + '</p></div>' if summary else ''}
  {'<div class="section"><div class="section-title">Tailoring Notes</div><p class="prose">' + tailoring + '</p></div>' if tailoring else ''}

  <div class="section">
    <div class="section-title">Contacts &amp; Emails
      <span style="margin-left:12px;font-size:12px;font-weight:400;color:#94a3b8">
        {total} contacts · {sent_count} sent · {replied_count} replied · {approved_count} approved · {queued_count} queued
      </span>
    </div>
    {contacts_html if contacts_html else '<p style="color:#64748b;font-style:italic">No contacts yet.</p>'}
  </div>

  {'<div class="section"><div class="section-title">Job Description</div><pre class="jd-text">' + jd + '</pre></div>' if jd else ''}
</div>"""

def generate():
    trackers = load_all_trackers()
    print(f"Loaded {len(trackers)} trackers")

    # Build sidebar cards
    sidebar_cards = "\n".join(make_company_card(t) for t in trackers)

    # Build detail panels
    detail_panels = "\n".join(make_detail_panel(t) for t in trackers)

    # Stats
    total_companies = len(trackers)
    research_done = sum(1 for t in trackers if t.get("research_status") == "done")
    all_contacts = [c for t in trackers for c in t.get("contacts", [])]
    total_contacts = len(all_contacts)
    sent = sum(1 for c in all_contacts if c.get("date_sent"))
    replied = sum(1 for c in all_contacts if c.get("status") == "replied")
    approved = sum(1 for c in all_contacts if c.get("status") == "approved")
    queued = sum(1 for c in all_contacts if c.get("status") == "queued")

    # Build slug list for JS search
    slug_names = json.dumps({t.get("slug", ""): t.get("company_name", "") for t in trackers})

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Job Hunt Dashboard</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; height: 100vh; overflow: hidden; display: flex; flex-direction: column; }}
  a {{ color: inherit; text-decoration: none; }}

  /* Top bar */
  .topbar {{ background: #1e293b; border-bottom: 1px solid #334155; padding: 12px 20px; display: flex; align-items: center; gap: 16px; flex-shrink: 0; }}
  .topbar h1 {{ font-size: 16px; font-weight: 700; color: #f1f5f9; white-space: nowrap; }}
  .stat-chip {{ background: #0f172a; border: 1px solid #334155; border-radius: 20px; padding: 4px 12px; font-size: 12px; color: #94a3b8; white-space: nowrap; }}
  .stat-chip strong {{ color: #f1f5f9; }}

  /* Layout */
  .layout {{ display: flex; flex: 1; overflow: hidden; }}

  /* Sidebar */
  .sidebar {{ width: 300px; flex-shrink: 0; background: #0f172a; border-right: 1px solid #1e293b; display: flex; flex-direction: column; overflow: hidden; }}
  .sidebar-controls {{ padding: 10px; border-bottom: 1px solid #1e293b; display: flex; flex-direction: column; gap: 6px; flex-shrink: 0; }}
  #search {{ background: #1e293b; border: 1px solid #334155; border-radius: 6px; padding: 7px 10px; color: #f1f5f9; font-size: 13px; width: 100%; outline: none; }}
  #search:focus {{ border-color: #60a5fa; }}
  .filter-row {{ display: flex; gap: 4px; flex-wrap: wrap; }}
  .filter-btn {{ background: #1e293b; border: 1px solid #334155; border-radius: 4px; padding: 3px 8px; font-size: 11px; cursor: pointer; color: #94a3b8; transition: all .15s; }}
  .filter-btn:hover, .filter-btn.active {{ background: #334155; color: #f1f5f9; border-color: #475569; }}
  .sidebar-list {{ overflow-y: auto; flex: 1; padding: 6px; }}

  /* Company card */
  .company-card {{ background: #1e293b; border: 1px solid #1e293b; border-radius: 8px; padding: 10px 12px; margin-bottom: 4px; cursor: pointer; transition: all .15s; }}
  .company-card:hover {{ border-color: #334155; background: #243347; }}
  .company-card.active {{ border-color: #60a5fa; background: #1e3a5f; }}
  .company-name {{ font-size: 13px; font-weight: 600; color: #f1f5f9; }}
  .company-meta {{ font-size: 11px; color: #64748b; margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

  /* Badges */
  .badge {{ display: inline-block; border-radius: 4px; padding: 2px 7px; font-size: 11px; font-weight: 600; color: #fff; }}
  .tier-badge {{ display: inline-block; border-radius: 4px; padding: 2px 7px; font-size: 10px; font-weight: 700; color: #fff; }}

  /* Main content */
  .main {{ flex: 1; overflow-y: auto; padding: 0; background: #0f172a; }}
  .empty-state {{ display: flex; align-items: center; justify-content: center; height: 100%; color: #334155; font-size: 18px; }}

  /* Detail panel */
  .detail-panel {{ padding: 24px 28px; max-width: 900px; }}
  .detail-header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; gap: 16px; }}
  .section {{ background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 16px 18px; margin-bottom: 14px; }}
  .section-title {{ font-size: 13px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: .06em; margin-bottom: 10px; }}
  .meta-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 8px; }}
  .meta-item {{ background: #0f172a; border-radius: 6px; padding: 6px 10px; }}
  .meta-label {{ font-size: 10px; color: #64748b; text-transform: uppercase; letter-spacing: .05em; display: block; }}
  .meta-value {{ font-size: 13px; color: #e2e8f0; display: block; margin-top: 1px; }}
  .ext-link {{ display: inline-block; background: #0f172a; border: 1px solid #334155; border-radius: 4px; padding: 3px 8px; font-size: 11px; color: #60a5fa; margin-right: 6px; margin-top: 4px; }}
  .ext-link:hover {{ border-color: #60a5fa; }}
  .prose {{ font-size: 13px; color: #cbd5e1; line-height: 1.6; }}

  /* Contact block */
  .contact-block {{ background: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 14px; margin-bottom: 10px; }}
  .email-card {{ background: #1e293b; border-left: 3px solid #334155; border-radius: 0 6px 6px 0; padding: 10px 12px; margin-top: 10px; }}
  .email-body {{ font-size: 12px; color: #94a3b8; line-height: 1.7; margin-top: 6px; white-space: pre-wrap; font-family: inherit; }}

  /* JD */
  .jd-text {{ font-size: 12px; color: #64748b; line-height: 1.7; white-space: pre-wrap; font-family: inherit; overflow-x: auto; }}

  /* Scrollbar */
  ::-webkit-scrollbar {{ width: 6px; }}
  ::-webkit-scrollbar-track {{ background: transparent; }}
  ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 3px; }}
</style>
</head>
<body>

<div class="topbar">
  <h1>Job Hunt Dashboard</h1>
  <div class="stat-chip"><strong>{total_companies}</strong> companies</div>
  <div class="stat-chip"><strong>{research_done}</strong> researched</div>
  <div class="stat-chip"><strong>{total_contacts}</strong> contacts</div>
  <div class="stat-chip" style="border-color:#22c55e"><strong style="color:#22c55e">{sent}</strong> sent</div>
  <div class="stat-chip" style="border-color:#3b82f6"><strong style="color:#3b82f6">{replied}</strong> replied</div>
  <div class="stat-chip" style="border-color:#f59e0b"><strong style="color:#f59e0b">{approved}</strong> approved</div>
  <div class="stat-chip" style="border-color:#8b5cf6"><strong style="color:#8b5cf6">{queued}</strong> queued</div>
</div>

<div class="layout">
  <div class="sidebar">
    <div class="sidebar-controls">
      <input id="search" placeholder="Search companies..." oninput="filterCards()" />
      <div class="filter-row">
        <button class="filter-btn active" onclick="setFilter('all', this)">All</button>
        <button class="filter-btn" onclick="setFilter('done', this)">Researched</button>
        <button class="filter-btn" onclick="setFilter('not_started', this)">Not started</button>
        <button class="filter-btn" onclick="setFilter('has_emails', this)">Has emails</button>
        <button class="filter-btn" onclick="setFilter('replied', this)">Replied</button>
      </div>
    </div>
    <div class="sidebar-list" id="sidebar-list">
      {sidebar_cards}
    </div>
  </div>

  <div class="main" id="main">
    <div class="empty-state">Select a company to view details</div>
    {detail_panels}
  </div>
</div>

<script>
const slugNames = {slug_names};
let activeFilter = 'all';
let activeSlug = null;

function showCompany(slug) {{
  // Hide all
  document.querySelectorAll('.detail-panel').forEach(el => el.style.display = 'none');
  document.querySelector('.empty-state').style.display = 'none';
  // Show target
  const panel = document.getElementById('detail-' + slug);
  if (panel) panel.style.display = 'block';
  // Update active card
  document.querySelectorAll('.company-card').forEach(el => el.classList.remove('active'));
  const card = document.querySelector(`.company-card[data-slug="${{slug}}"]`);
  if (card) card.classList.add('active');
  activeSlug = slug;
  window.location.hash = slug;
}}

function filterCards() {{
  const q = document.getElementById('search').value.toLowerCase();
  document.querySelectorAll('.company-card').forEach(card => {{
    const slug = card.dataset.slug;
    const name = (slugNames[slug] || slug).toLowerCase();
    const rs = card.dataset.rs || '';
    let show = true;
    if (q && !name.includes(q) && !slug.includes(q)) show = false;
    if (activeFilter === 'done' && rs !== 'done') show = false;
    if (activeFilter === 'not_started' && rs !== 'not_started') show = false;
    if (activeFilter === 'has_emails') {{
      // show only cards that have at least one email sent (green dot visible)
      const dots = card.querySelectorAll('span[style*="22c55e"]');
      if (dots.length === 0) show = false;
    }}
    if (activeFilter === 'replied') {{
      const dots = card.querySelectorAll('span[style*="3b82f6"]');
      if (dots.length === 0) show = false;
    }}
    card.style.display = show ? '' : 'none';
  }});
}}

function setFilter(f, btn) {{
  activeFilter = f;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  filterCards();
}}

// Restore from hash
if (window.location.hash) {{
  const slug = window.location.hash.slice(1);
  if (document.getElementById('detail-' + slug)) {{
    showCompany(slug);
  }}
}}
</script>
</body>
</html>"""

    out = BASE / "dashboard.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Written: {out}")
    return out

if __name__ == "__main__":
    generate()
