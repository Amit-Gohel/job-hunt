# Atlan -- Research

## Company Overview

Atlan (atlan.com) is the "Context Layer for AI" -- the infrastructure that makes enterprise data usable for AI agents. They pull context from across the enterprise, make it machine-readable, and deliver it to every AI agent and human who needs it. Think of them as the connective tissue between a company's data stack and its AI systems.

- **Size**: 201-500 employees (LinkedIn), 400+ enterprise customers
- **Funding**: $105M Series C (May 2024), led by GIC (Singapore sovereign wealth fund) + Meritech Capital + Insight Partners + Salesforce Ventures
- **Customers**: General Motors, Nasdaq, Workday, Elastic, Fox Corporation, Autodesk, Dropbox
- **Location**: San Francisco HQ, strong India engineering team (remote-first)
- **Product**: Context store built on vector + graph + structured data; MCP servers; AI metadata agents; App Framework; Data Quality Studio

## Full JD Signal

**Note**: No "AI Engineer" role is currently listed. The closest active India-remote role is "Engineering Manager, Data Platform" (Ashby: aea0a9e5). The CSV signal ("AI Engineer / AI Platform Engineer") likely reflected a previous or upcoming opening. The EM JD captures exactly what Atlan builds technically and culturally.

### Engineering Manager, Data Platform (India, Remote)

Two high-leverage problem spaces:

**1. Data Quality & Context Intelligence**
- Proactive detection/resolution of data issues (schema drift, freshness, anomalies) at scale
- Using AI to auto-generate metadata context (descriptions, classifications, lineage) for thousands of undocumented enterprise data assets

**2. App Platform**
- Shared runtime, SDK, lifecycle, and distribution infrastructure that powers every app, agent, and workflow built on Atlan's platform

**Core technical deliverables:**
- High-scale ingestion and validation frameworks
- Contract-driven routing, storage, and serving layers
- Multi-tenant isolation and noisy-neighbor resilience
- Search APIs with sub-second P95 response times
- Systems operating at 99.99% availability

**Must-have signals from JD:**
- Data ingestion frameworks or lakehouse foundations
- Metadata, governance, or catalog platforms
- Multi-tenant SaaS infrastructure and tenant isolation mechanisms
- Search, storage, or distributed serving layers
- Data quality, validation, or contract enforcement systems
- "AI-native curiosity": actively explores AI-assisted dev workflows

**Amit match**: Permission-aware 2-stage Milvus RAG at 500+ concurrent users, BGE-M3 after benchmarking 6 embedding models on production data, multi-tenant architecture enforcing 250+ permissions per query, Milvus over FAISS/Qdrant on production benchmarks. This maps directly to Atlan's context store problem.

## Last 60 Days -- Company Activity

**Activate 2025 (Aug 2025 conference -- Atlan's annual event):**
- Launched App Framework publicly (infrastructure for developers/partners to build apps on Atlan)
- Announced AI Context Ecosystem: 40+ partners sharing one understanding of enterprise data
- Demoed Context Agents: "From 8% to 100% metadata coverage" using AI agents
- Atlan + Immuta: Security Context Layer for AI agents
- Cursor + Atlan MCP: bootstrap agent context from IDE
- "Same Model, Different Context" demo showing how context changes AI accuracy

**"WTF is the Context Layer" live series (May 2026):**
- Episode 2 coming May 27, hosted by Austin Kronz and Prukalpa Sankar
- Guest: Sanjeev Mohan (analyst) on what's real vs hype in enterprise AI context

**Gartner recognition (2025):**
- Named Leader in both Gartner MQ for Data & Analytics Governance AND Metadata Management
- "#1 Rated leader in every eligible analyst report, 2025"

**Technical bet to reference in cold email:**
Atlan's core thesis: "The gap in enterprise AI isn't the model. It's context." They argue 95% of GenAI pilots fail to reach production because AI agents don't have the business context (definitions, policies, lineage) to reason correctly. Their MCP server delivers this context to any AI tool at inference time.

## Email Pattern

Confirmed via Prospeo: `firstname.lastname@atlan.com`

## Named Contacts

### Tier 1 -- Senior Engineering Manager

**1. Viswesh Subramanian**
- Role: Senior Engineering Manager | AI-native context engineering @ Atlan
- LinkedIn: https://www.linkedin.com/in/viswesh-subramanian/
- Email: viswesh.subramanian@atlan.com
- Background: Ex-Adobe, Ex-Juniper; 3K followers; based in India
- Recent posts:
  - 3 weeks ago: Ran a free workshop "From Agent Demo to Agent System: A Production Architecture Workshop" -- framed agent failures as infrastructure problems (not model problems): "it invents policies that don't exist, forgets customers between sessions, burns money looping on impossible requests." Covered all nine components of a production agent harness: context engineering, memory, looping prevention. Directly maps to Amit's permission-aware RAG + LangGraph agentic architecture.
  - 1 month ago: "You can validate engineering hypotheses in minutes without touching staging"
- Research hook: His workshop on agent infrastructure is almost a blueprint for what Amit built at Vivansh -- the permission-aware context layer that enforces 250+ policies per query is exactly the "infrastructure around the LLM" he was teaching.

**2. Birendra Kumar Sahu**
- Role: Distinguished Engineer - AI Expert @ Atlan
- LinkedIn: https://www.linkedin.com/in/birendrasahu/
- Email: birendra.sahu@atlan.com
- Background: Ex-CTO, Ex-Chargebee, Ex-Razorpay, Ex-Teradata; authoring "Agentic AI Systems" book; building third-gen data/AI platform; based in Bengaluru
- Recent posts:
  - 2 weeks ago: "Most AI models are built to be capable. The best ones are built to be purposeful." -- Discussing Anthropic's approach with Claude: "They didn't just train for benchmark scores. They built a system where values and reliability are baked in from day one." 
  - 3 weeks ago: Post about AI platform architecture
- Research hook: His post on "purposeful vs capable AI" maps to Amit's production-first mindset -- every system Amit ships is designed for production reliability, not benchmark optimization. His book on agentic AI systems is directly in Amit's work territory.

### Tier 3 -- IC / Senior Engineer

**3. Mustafa Hasan Khan**
- Role: Senior Software Engineer @ Atlan | Building AI Observability & LLM-native systems
- LinkedIn: https://www.linkedin.com/in/mustafahasankhan/
- Email: mustafa.khan@atlan.com
- Background: IIT Madras; 3x Google Summer of Code mentor; from Uttar Pradesh
- Recent activity: Engaged with DuckDB-skills launch on LinkedIn (commented); posted AI Engineering intern job at Atlan; building LLM observability pipelines
- Research hook: He's building LLM observability at Atlan -- Amit's multi-model orchestration work (GPT-4o + Qwen3-Coder + Gemini on one flow, each validated by Pydantic) is exactly the kind of system that needs observability. The GSoC mentoring shows he engages with the broader community.

**4. Shekh Aliul**
- Role: Senior Software Engineer II @ Atlan
- LinkedIn: https://www.linkedin.com/in/shekh-aliul/
- Email: shekh.aliul@atlan.com
- Background: Based in Ghaziabad, UP; 4K followers; promoted twice in short time at Atlan
- Recent posts: Promotion announcements -- says "at Atlan, it still feels like Day 1, there's always something new to build, learn, and improve." Offers mentorship/guidance to people reaching out.
- Research hook: His back-to-back promotions (SWE-III to SSE-II) and description of Atlan's culture as "Day 1 always" signal a fast-moving, high-ownership environment. Amit has shipped 3 production AI systems in under a year, which is that same pace.

### Tier 4 -- Recruiter / HR

**5. Manu Barki**
- Role: Lead Talent Partner / Tech Recruiter @ Atlan | Building elite data & AI teams across India & North America | 13 years experience
- LinkedIn: https://www.linkedin.com/in/manubarki/
- Email: manu.barki@atlan.com
- Background: Bengaluru-based; 30K followers; 13 years scaling technical talent
- Recent posts:
  - 2 weeks ago: Posted about Atlan's AI Context Ecosystem launch (40+ partners) from Activate -- framing it as Atlan moving from data catalog to broader AI infrastructure
  - 3 weeks ago: Skeptical post about AI-automated LinkedIn outreach ("LinkedIn outreach is dead" narrative is overblown; mechanical AI personalization has low real value). Values genuine human connection.
- Research hook: He posted about the AI Context Ecosystem launch -- leads directly into why Atlan is hiring for AI engineering. His skepticism of AI-automated outreach means a genuine, specific email will stand out.

**6. Nikita Parate**
- Role: Senior Recruitment Coordinator @ Atlan
- LinkedIn: https://www.linkedin.com/in/nikita-parate-477b51150/
- Email: nikita.parate@atlan.com
- Background: Pune-based; talent acquisition specialist; connecting "top talent with opportunity"
- Research hook: India-based recruiter actively supporting Atlan's engineering hiring across India.

## Resume Tailoring Brief

- **Lead with**: Permission-aware multi-tenant RAG (250+ permissions, Milvus 2-index architecture) -- closest to Atlan's context store problem
- **Summary line**: Mirror "context layer for AI" language -- Amit builds the retrieval and context delivery layer
- **Skills to emphasize first**: Milvus, vector databases, RAG, LangChain/LangGraph, multi-tenant architecture, production AI systems
- **Drop or de-emphasize**: TinyML/hardware bullets (not relevant to Atlan's platform work)
- **Proof points to front-load**: 50K queries/month, 95% MRR, BGE-M3 after benchmarking 6 models, 250+ permissions enforced per query
- **Projects to keep**: Both RAG chatbots (Silver Touch + Vivansh), Form Builder (multi-model orchestration), Course Builder (RAG + AWS Lambda)

## Outreach Plan

- Initial sends: Tue-Thu, 8-11 AM IST (India team) or 2-4 PM IST
- Contacts: 6 (2x Tier 1, 2x Tier 3, 2x Tier 4)
- Space sends: 1-2 days apart, not all at once
- Follow-up #1 (day 3-4): Add new value -- mention Atlan blog/MCP or a specific technical observation
- Follow-up #2 (day 10): Close the loop
