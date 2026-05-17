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
3. **Work Experience bullets**: do not change facts. Reorder bullets so the most JD-relevant ones come first. Drop bullets that don't help (e.g., hardware/IoT bullets for a pure LLM-infra role). Keep at most 4 bullets per role. Always keep all 3 work experience entries (Vivansh, Silver Touch, IIT Delhi) — never drop a job.
4. **Projects**: ALWAYS keep exactly 2 projects — never fewer. Pick the best 2 from the full project pool below based on the JD. Use the selection guide beneath the pool.
5. **Certifications and Achievements**: keep the Microsoft Azure cert always. Drop Smart India Hackathon if the role is pure software/cloud and the bullet count needs to come down for one-page fit.

---

## Project pool — all 8 available projects

Read `chunks.json` for full detail on each. Use the LaTeX blocks below verbatim (edit only the bullet text if a specific angle needs emphasis).

**P1 — Multi-Tenant RAG Chatbot** *(production scale, RBAC, Milvus, GPT-4o)*
```latex
        \begin{twocolentry}{
            2024--2025
        }
            \textbf{Multi-Tenant RAG Chatbot -- Permission-Aware Enterprise AI}
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Production RAG chatbot serving \textbf{50,000+ queries/month} across 10+ tenants; enforced \textbf{250+ permissions per query} via 2-stage Milvus + PostgreSQL RBAC; improved MRR from \textbf{45\% to 95\%} through benchmarking 6 embedding models and custom BGE-M3 + reranker pipeline
            \end{highlights}
        \end{onecolentry}
```

**P2 — AI Course Builder** *(end-to-end pipeline, Cohere, Gemini 2.5, ElevenLabs, AWS Lambda)*
```latex
        \begin{twocolentry}{
            2025
        }
            \textbf{AI Video Course Generation Pipeline -- 99\% Faster EHS Training Production}
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Reduced course production from \textasciitilde1 week to \textasciitilde10 minutes (\textbf{99\% reduction}) via RAG-based video selection (Milvus + Cohere), Gemini 2.5 Pro for visual-audio alignment, ElevenLabs narration, and serverless FFmpeg rendering on AWS Lambda
            \end{highlights}
        \end{onecolentry}
```

**P3 — AI Form Builder** *(multi-model orchestration, Pydantic, GPT-4o + Qwen3-Coder)*
```latex
        \begin{twocolentry}{
            2025
        }
            \textbf{AI Form Builder -- PDF-to-Digital Form Converter}
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Converted PDF forms to structured digital replicas in \textasciitilde20 seconds (\textbf{200+ forms in month 1}) using multi-model pipeline (GPT-4o, Qwen3-Coder-480B, GPT-4o-mini) with Pydantic-validated intermediate JSON; bulk-processed 100+ PDFs in 5--10 minutes; replaced 1+ hour of manual work per form
            \end{highlights}
        \end{onecolentry}
```

**P4 — SAP Analytics Bot** *(Text-to-SQL, NLP, auto-dashboard, Silver Touch)*
```latex
        \begin{twocolentry}{
            2024
        }
            \textbf{SAP Analytics Bot -- Natural Language to SQL + Auto-Dashboard}
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Production Text-to-SQL system letting business users query live SAP-connected databases in plain English; auto-generates dashboard charts from results; handles multi-step clarification, large result preprocessing, and statistical summaries -- no SQL knowledge required
            \end{highlights}
        \end{onecolentry}
```

**P5 — On-Premise OCR Pipeline** *(document processing, DocTR, Llama-3.1, zero cloud)*
```latex
        \begin{twocolentry}{
            2024
        }
            \textbf{On-Premise OCR + Document Entity Extraction Pipeline}
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Hybrid OCR pipeline for sensitive government documents (200+ page PDFs, zero cloud APIs): ran DocTR + DocLink per page, used on-premise Llama-3.1-Nemotron-70b to merge outputs; achieved \textasciitilde\textbf{90\% entity extraction accuracy} on Aadhaar, PAN, and GST numbers; fully self-hosted on client's 250GB server
            \end{highlights}
        \end{onecolentry}
```

**P6 — Air Writing Recognition** *(IMU, CNN-BiLSTM, IIT Delhi research, 1000+ model configs)*
```latex
        \begin{twocolentry}{
            2024
        }
            \textbf{Air Writing Recognition System -- IIT Delhi Research}
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Wearable IMU wristband (ESP32 + MPU6050) classifying 62 air-written characters via CNN-BiLSTM; evaluated \textbf{1,000+ model configurations} across 5 architecture families using TensorFlow/Keras with leave-one-subject-out cross-validation; collected 12,400 labeled samples from 20 participants
            \end{highlights}
        \end{onecolentry}
```

**P7 — Voicer** *(TinyML, Samsung Top 10 / 70,000+ participants, CNN News18)*
```latex
        \begin{twocolentry}{
            2023
        }
            \textbf{Voicer -- Sign Language to Speech Device} (\hrefWithoutArrow{https://github.com/amit-gohel/voicer}{GitHub})
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Wearable device translating Indian Sign Language to speech using 10 IMU sensors + NodeMCU with on-device TinyML inference in \textbf{2ms}, \textbf{94.1\% accuracy} across 12 gesture classes; \textbf{Samsung Solve for Tomorrow Top 10 among 70,000+ participants}, featured on CNN News18
            \end{highlights}
        \end{onecolentry}
```

**P8 — WeepScope** *(1D CNN+GRU on audio, 86% accuracy, co-authored research paper)*
```latex
        \begin{twocolentry}{
            2023
        }
            \textbf{WeepScope -- Infant Cry Classifier} (\hrefWithoutArrow{https://github.com/amit-gohel/Weep-Scope}{GitHub})
        \end{twocolentry}

        \vspace{0.02 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Standalone device classifying infant cries into 5 categories using hybrid 1D CNN + GRU on Arduino Nano 33 BLE Sense (1MB flash); \textbf{86\% test accuracy} with 5-cycle majority voting; co-authored research paper with Dr.\ Kirankumar Trivedi
            \end{highlights}
        \end{onecolentry}
```

---

## Project selection guide

Read the JD, identify its primary domain, pick the best 2. Hard rule: **always exactly 2, never fewer.**

| JD primary signal | Pick these 2 |
|---|---|
| RAG / vector DB / retrieval / embeddings | P1 (RAG Chatbot) + P7 (Voicer for social proof) |
| Agentic AI / LLM orchestration / multi-model | P1 (RAG Chatbot) + P2 (Course Builder) |
| MLOps / data pipelines / feature engineering | P5 (OCR Pipeline) + P4 (SAP Analytics Bot) |
| Voice / ASR / TTS / audio / speech | P7 (Voicer) + P8 (WeepScope — audio CNN+GRU) |
| Hardware / edge ML / TinyML / IoT / embedded | P7 (Voicer) + P8 (WeepScope) |
| NLP / text analytics / information extraction | P4 (SAP Analytics Bot) + P5 (OCR Pipeline) |
| Document processing / OCR / PDF / vision | P5 (OCR Pipeline) + P3 (Form Builder) |
| Product AI / full-stack / end-to-end systems | P3 (Form Builder) + P2 (Course Builder) |
| Computer vision / multimodal | P5 (OCR Pipeline) + P2 (Course Builder) |
| ML research / model architecture / deep learning | P6 (Air Writing / IIT Delhi) + P7 (Voicer) |
| General ML engineering (no strong signal) | P1 (RAG Chatbot) + P7 (Voicer) |

**Tie-breaking rules:**
- P7 (Voicer) has the strongest social proof signal (Samsung Top 10, 70,000+ participants, CNN News18). Prefer it when in doubt between two otherwise equal options.
- P1 (RAG Chatbot) maps to the widest range of AI engineering JDs. Default to it unless the role is clearly hardware/audio/vision.
- Do NOT put P1, P2, P3 in Projects if they already appear as prominent bullets in Work Experience for the same role. In that case, step down to the next best option in the table so the Projects section adds new signal rather than repeating the same work.
- P6 (Air Writing) is the IIT Delhi research project. It overlaps with the IIT Delhi Work Experience bullets. Only use it in Projects if you trim the IIT Delhi bullets to 1, so the same work does not appear twice at the same depth.

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
- Target two pages. Do not shrink the font to force content in — two pages is correct for a 2+ year candidate with multiple production systems. Include all meaningful work experience, all projects, and full skills. Only cut bullets if the resume spills beyond two pages.
- Use straight quotes (`'`), not curly quotes — anti-AI hygiene also applies to documents.
