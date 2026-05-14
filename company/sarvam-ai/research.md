# Sarvam AI — Research

## CSV signal (starting hints)

- **Location:** Bengaluru
- **Role title (CSV):** Forward Deployed Software Engineer | 2-5 years
- **Salary band (LPA):** 25-45 LPA (estimated)
- **Funding stage:** Series A — $53M (Lightspeed, Peak XV, Khosla Ventures)
- **Company size:** 51-200 employees (per LinkedIn)
- **Hiring status:** Actively hiring — 38 open roles as of May 2026
- **Priority score:** 98
- **Match reason:** JD explicitly lists LangChain, LlamaIndex, CrewAI, LangGraph, RAG, tool calling, multi-agent systems — near-perfect overlap with Amit's production AI stack
- **Notes:** Govt-selected for India sovereign LLM; partners include Tata Capital, SBI Life, CRED, IDFC, LIC

## Links

- Company: https://www.sarvam.ai
- Careers: https://www.sarvam.ai/careers
- JD (live): https://www.sarvam.ai/careers/jobs/ac2b835e-375c-48d8-a174-8c2935f408b2
- LinkedIn: https://www.linkedin.com/company/sarvamai/
- Blog: https://www.sarvam.ai/blogs

---

## Full JD signal

**Role:** Forward Deployed Software Engineer | 2-5 years  
**Team fit:** ARYA is the primary fit (MCP servers, LangGraph, multi-agent orchestration, Kafka). Samvaad is secondary (conversational AI agents, voice + WhatsApp).

**Must-haves from JD:**
- 2-5 years production engineering with shipped systems
- Strong Python
- LLMs and agents: RAG, tool calling, embeddings, context windows, failure modes
- Multi-agent architecture design: memory management, orchestration
- Eval pipelines for agentic AI
- High agency — ship without hand-holding

**Bonus points:**
- LangChain, LlamaIndex, CrewAI, LangGraph — ability to author agents from scratch without depending on them
- Voice/speech models (TTS, STT, ASR)
- Familiarity with Sarvam's own models/APIs
- Customer-facing or product-embedded engineering experience
- ARYA-specific: MCP servers, Kafka/SQS/RabbitMQ, SQL/NoSQL at scale, Google ADK

---

## Team map — named individuals

### Tier 1 — Engineering Leads / Heads

| Name | Role | LinkedIn | Email | Hook |
|------|------|----------|-------|------|
| Aalekh Sharan | Head, Agentic AI & Head, Public Sector | https://www.linkedin.com/in/aalekh-sharan-b1050330/ | aalekh@sarvam.ai | Tech-à-Tête podcast Episode 2 (~April 2026): discussed building AI that is safe, sovereign, scalable — multilingual models + compute constraints |
| Tushar Goswamy | Head of Edge AI & GTM Leadership | https://www.linkedin.com/in/tgoswamy/ | tushar@sarvam.ai | Sarvam Edge launch (Feb 14, 2026); on-device AI deployment at scale |
| Krishna Prasad Srinivasan | Vision Models Team Lead | https://www.linkedin.com/in/krishna-prasad-srinivasan/ | krishna@sarvam.ai | ex-Harvard Research Fellow + ex-Engineering Manager; Sarvam Vision launch Feb 5, 2026 |

### Tier 2 — Founders / Execs

| Name | Role | LinkedIn | Email | Hook |
|------|------|----------|-------|------|
| Vivek Raghavan | Co-Founder | https://www.linkedin.com/in/vivek-raghavan-16005424/ | vivek@sarvam.ai | Open-Sourced Sarvam 30B + 105B (March 6, 2026) — largest Indian open-source LLM release |
| Pratyush Kumar | Co-Founder | https://www.linkedin.com/in/pratyush-kumar-8844a8a3/ | pratyush@sarvam.ai | ARYA blog post (Feb 10, 2026) — authored the technical piece on immutable state ledger + declarative agent authoring via HCL |
| Saurabh Karn | Founding Member | https://www.linkedin.com/in/saurabh-karn-466a9535/ | saurabh@sarvam.ai | Sovereign AI Partnerships with Indian States announcement (Feb 8, 2026) |

### Tier 3 — ICs / Senior Engineers (FDSEs)

| Name | Role | LinkedIn | Email | Hook |
|------|------|----------|-------|------|
| Prajna Vegesna | Forward Deployed AI Engineer | https://www.linkedin.com/in/prajna-vegesna-64778250/ | prajna@sarvam.ai | Fellow FDSE on the exact team; prev Fractal AI — peer referral path |
| Dnyaneshwar More | Forward Deployed AI Engineer (Conversational AI) | https://www.linkedin.com/in/dpmore/ | dnyaneshwar@sarvam.ai | Shipping Conversational AI to production — directly mirrors Amit's agentic chatbot work |
| Arpit Dwivedi | Machine Learning Engineer | https://www.linkedin.com/in/arpitdwi/ | arpit@sarvam.ai | Building LLMs at Sarvam; ex-Microsoft Data/Applied Scientist — IIT KGP background |

---

## Email pattern

**Confirmed:** `firstname@sarvam.ai`  
Source: Karman Sethi (GTM & Strategy, Sarvam) publicly listed `karman@sarvam.ai` on LinkedIn profile.

---

## Last 60 days (cold email opener material)

| Date | Event | Hook |
|------|-------|------|
| April 2, 2026 | Blog: "Evaluating Indian Language ASR" — practical guide to layered Indic ASR evaluation: LLM-WER, LLM-CER, Intent/Entity scores, COMET | Technical depth signal; Amit can connect to eval pipeline experience |
| ~April 2026 | Aalekh Sharan on Tech-à-Tête podcast (Episode 2) — discussed AI sovereignty, safe + scalable multilingual AI, compute constraints for Indic models | Direct hook for email to Aalekh |
| March 6, 2026 | Blog: "Open-Sourcing Sarvam 30B and 105B" — India's largest open-source LLM models released | Hook for Vivek/Pratyush emails |
| Feb 20, 2026 | Blog: "Introducing Indus" — new product launch | |
| Feb 10, 2026 | Blog: "Introducing Sarvam Arya" — full technical post on ARYA agent orchestration stack: 8 composable primitives (LLM, Agent, MCP, Node, Ledger, Task Graph, Code Interpreter, Artefact), immutable state ledger, declarative HCL authoring, controlled dynamism (the "slider"), Acta Diurna distributed tracing | Primary hook for ARYA team emails — immutable ledger + MCP servers + LangGraph equivalent |
| Feb 8, 2026 | Sarvam Announces Sovereign AI Partnerships with Indian States | Hook for Saurabh email |
| Feb 5, 2026 | Sarvam Vision launch | Hook for Krishna Prasad email |

**Key ARYA technical details** (from blog — use in emails):
- 8 flat composable primitives — deliberately avoids hierarchy/accretion
- Immutable state ledger: append-only, atomic commits, crash recovery via clean snapshots
- "Constraints liberate, liberties constrain" — their design philosophy
- Declarative HCL config (like Terraform for agents) — spec separate from execution
- "Acta Diurna" debugging service — distributed tracing via single correlation ID
- Built because "nothing available survived contact with production"
- GPT-4.1 mini used for structured extraction workloads

---

## Technical mapping (Amit → Sarvam ARYA)

| Amit's work | Sarvam ARYA equivalent |
|-------------|----------------------|
| LangGraph multi-agent upgrade of EHS RAG chatbot (8s response, 50K queries/month) | ARYA task graph orchestration for production agents |
| Permission-aware RAG with 250+ granular permissions, multi-tenant | ARYA's ledger scoping + schema enforcement at boundaries |
| Multi-model orchestration: GPT-4o + Gemini + Qwen3-Coder | ARYA's LLM primitive — swap LLM with one-line `llm_uid` change |
| FastAPI (4 workers) + LangChain agents + tool calling over 10+ APIs | ARYA's MCP servers + agentic backend infrastructure |
| Production eval: MRR 80%, query relevance scoring | ARYA's per-node feedback loops + evolutionary prompt optimization |
| Milvus migration from FAISS (MRR 45% → 95%) | Retrieval stack decisions — matches ARYA's structured data pipeline work |

---

## Resume tailoring brief

- **Lead with:** Multi-tenant permission-aware RAG chatbot (LangGraph upgrade, 50K queries/month, 250+ permissions, 8s latency)
- **Rewrite summary to:** "AI Engineer with 2 years shipping production RAG and agentic systems at scale — LangGraph multi-agent orchestration, FastAPI, Milvus, multi-model routing (GPT-4o/Gemini/Qwen3). Built permission-aware, multi-tenant AI infrastructure handling 50K+ queries/month."
- **Lead skills section with:** LangGraph, LangChain, LlamaIndex, FastAPI, Milvus/Qdrant/FAISS, multi-agent orchestration, RAG
- **Bring up:** MCP tool calling, agentic eval pipelines, multi-model routing
- **De-emphasize:** Hardware/IoT bullets (Voicer, WeepScope TinyML) — mention briefly if space, don't lead with them
- **Keep:** SAP Analytics Bot (Text-to-SQL), AI Course Builder (FastAPI + LLM orchestration)

---

## Outreach plan

- **Primary send window:** Tuesday–Thursday, 8–11 AM IST (both target and sender in IST)
- **Send order:** Aalekh Sharan first (Tier 1, directly hires for ARYA) → Vivek Raghavan (Tier 2) → Pratyush Kumar (Tier 2) — space 3-4 days between each
- **Follow-up #1 hook:** Share link to amitgohel.dev + one specific ARYA observation (e.g., "the immutable state ledger design maps exactly to why our multi-tenant RAG needed a permission index separate from content chunks")
- **Follow-up #2 hook:** Reference the ASR evaluation blog post (April 2) — "still following Sarvam's evals work"
