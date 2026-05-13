---
description: Tailor the per-company resume.tex against the captured JD and compile to PDF.
---

# /tailor-resume $ARGUMENTS

Edit `company/<slug>/resume.tex` so the resume mirrors the JD captured during research. `$ARGUMENTS` is the slug.

## Pre-flight

1. Refuse to run if `$ARGUMENTS` is empty. Tell the user: "Pass a slug, e.g. `/tailor-resume sarvam-ai`."
2. Read `company/<slug>/tracker.json`. If `jd_full_text` is empty or `research_status != "done"`, stop and tell the user to run `/research-company <slug>` first.
3. Read `chunks.json` to refresh on Amit's full track record (RAG metrics, projects, hardware wins, certifications) — this is the canonical source for what can go on the resume.

## What to change

Edit `company/<slug>/resume.tex` (NOT the project-root resume.tex — that's the master template).

Decisions to make per company:

1. **Professional Summary**: rewrite one sentence to mirror the JD's tech stack and seniority signal. Keep it under 75 words. No hyperbole, no AI tells, no "passionate about".
2. **Technical Skills section**: reorder so the categories the JD emphasizes come first. Example: a Milvus/Qdrant-heavy JD → "Vector Databases and Retrieval" goes to the top of the list. A LangGraph/agentic JD → "AI/ML Frameworks" with LangChain/LangGraph emphasized first.
3. **Work Experience bullets**: do not change facts. Reorder bullets so the most JD-relevant ones come first. Drop bullets that don't help (e.g., hardware/IoT bullets for a pure LLM-infra role). Keep at most 4 bullets per role.
4. **Projects**: if the JD is not hardware-leaning, drop the Voicer + WeepScope project section (or keep only the most relevant one).
5. **Certifications and Achievements**: keep the Microsoft Azure cert always. Drop Smart India Hackathon if the role is pure software/cloud and the bullet count needs to come down for one-page fit.

## Capture the diff

After editing `resume.tex`, write a 4-8 line summary in `tracker.json` field `tailoring_notes` describing exactly what changed and why. Reference the specific JD phrases that drove each change. This is what future-you reads when reviewing the email batch.

## Compile

Build the PDF:

```bash
cd company/<slug>
pdflatex -interaction=nonstopmode -halt-on-error resume.tex
pdflatex -interaction=nonstopmode -halt-on-error resume.tex   # second pass for refs
rm -f resume.aux resume.log resume.out
```

If `pdflatex` fails, paste the last 30 lines of the error to the user and stop. Do not silently leave a broken `resume.pdf` behind.

## After

- Confirm `resume.pdf` exists and is non-empty.
- Tell the user: "Resume tailored for `<slug>`. Tailoring summary in `tracker.json`. Next: `/draft-outreach <slug>`."

## Hard rules

- Do not edit the project-root `resume.tex`. Per-company changes belong in `company/<slug>/resume.tex`.
- Do not invent achievements. Everything stays grounded in `chunks.json` + `resume.tex` master template.
- Keep the resume to one page. If it spills to two, cut bullets — don't shrink the font.
- Use straight quotes (`'`), not curly quotes — anti-AI hygiene also applies to documents.
