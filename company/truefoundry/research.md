# TrueFoundry -- Research

## Company Overview

TrueFoundry builds Enterprise-Ready Agentic AI infrastructure. Core products: AI Gateway (control plane for governing agentic workloads), AI Deploy (deploy model inference, fine-tuning, MCP servers, and agents as Kubernetes apps), MCP Gateway, and Skills Registry. Processes 10B+ requests/month. Clients include ResMed, Siemens Healthineers, NVIDIA, Zscaler.

Funded: $19M Series A (Sequoia/Peak XV + Intel Capital). 40+ employees, offices in Bengaluru and San Jose. Team tripled in 2025.

Recognition: Named Representative Vendor in Gartner Market Guide for AI Gateways (Feb 2026). DevTools & Infrastructure Startup of the Year at AIBoomi Awards 2026.

Co-founders: Nikunj Bajaj (CEO, ex-Meta Lead ML Engineer), Abhishek Choudhary (CTO, ex-Meta Senior Staff Engineer infrastructure), Anuraag Gutgutia (COO, ex-WorldQuant VP).

## Full JD Signal

**Role:** Senior AI/ML Engineer: LLM & Agent Stack (also a Staff ML Platform Engineer listing found)
**Source:** Wellfound, Bebee
**Location:** Bengaluru
**Seniority:** 4-10 years software engineering

**Core Responsibilities:**
- Architect and implement scalable agent orchestration patterns: graph-based executors, state management, multi-agent coordination
- Own critical integrations: model adapters, LLM gateway hooks, vector DBs, tools, external APIs, LLMops flows
- Build tracing, benchmarking, observability for LLMs and agents; token/cost accounting, latency p95, throughput, correctness checks
- Design guardrails: moderation hooks, human-in-the-loop checkpoints, audit trails
- Mentor junior engineers, conduct design reviews
- Work directly with strategic customers prototyping agentic solutions

**Must-Have:**
- Deep practical experience deploying LLMs in production: RAG, retrieval, embeddings
- Hands-on experience with agent orchestration frameworks (LangGraph/LangChain or custom)
- Distributed systems, infra, or ML platform experience
- Proven track record with observability, cost controls, policy enforcement

**Preferred:**
- Open-source contributions to LLM orchestration tools
- Enterprise deployment: on-prem/cloud hybrid, data residency, compliance
- Security, privacy, model governance
- Cross-functional project leadership

**Tech stack from JD + company blog:** LangGraph, LangChain, LLM Gateway, MCP, vector stores (Milvus/Qdrant), OpenTelemetry, Kubernetes, FastAPI, Python, vLLM

## Last 60 Days -- Company Activity

- Feb 2026: Recognized as Representative Vendor in Gartner Market Guide for AI Gateways (formal establishment of AI Gateways as major enterprise requirement)
- Jan 2026: MCP Gateway blog post by Boyu Wang -- 10ms latency, 350+ RPS on 1 vCPU, OAuth 2.0 identity injection, hybrid on-prem architecture; framing shift from "passive context" to "active tool use"
- 2026: DevTools & Infrastructure Startup of the Year at AIBoomi Awards
- 2026: Cerebras strategic partnership (run advanced models at speed on TrueFoundry infra)
- 2025 year-end: "truefailover" launched (resilience layer sitting on AI Gateway, routes around failures across models/regions/providers in real time); AutoDeploy and AutoPilot features shipped
- 2025: Series A $19M; team tripled

## Person: Chirag Jain

**Role:** Senior Machine Learning Engineer
**LinkedIn:** https://www.linkedin.com/in/chiragjn/
**GitHub:** https://github.com/chiragjn
**Email:** chirag@truefoundry.com
**Tier:** 1
**Background:** 5 years NLU, Engineering, and MLOps at Haptik before TrueFoundry. Builds MLOps tooling at intersection of distributed systems, ML, and software engineering.
**Recent activity:**
- Posted about ICLR 2025 LLM paper analysis
- Posts about truefailover (resilience layer), AutoDeploy (automatic infra config for model deployment), AutoPilot (monitors AI workloads for resource efficiency)
- Posts on Gartner AI gateway cost optimization coverage
**Research hook:** His ICLR 2025 LLM paper roundup maps well to Amit's production embedding/retrieval work. His focus on MLOps tooling (AutoDeploy, truefailover) directly overlaps with the LangGraph + Milvus orchestration work Amit has shipped.

## Person: Anant Agarwal

**Role:** Principal Applied Scientist, GenAI
**LinkedIn:** https://www.linkedin.com/in/agarwalanant/
**Email:** anant@truefoundry.com
**Tier:** 1
**Background:** IIT Kharagpur + ISB Hyderabad (Dean's and Merit List awards). In 2025, co-launched The Gen Academy with Arvind Narayanamurthy -- trained ~2,000 professionals in workshops on RAG architectures, agentic systems, MCP, context engineering, LangChain/LangGraph, white-coding with AI tools. Published IEEE 2025 paper on automated prompt optimization using LLM-powered Genetic Algorithm.
**Research hook:** His Gen Academy workshops on RAG and agentic systems parallel exactly what Amit has built in production -- 2-stage retrieval with permission filtering, LangGraph orchestration at Vivansh. The genetic algorithm prompt optimization paper is a specific technical angle.

## Person: Aditi Gupta

**Role:** Senior Machine Learning Engineer
**LinkedIn:** https://www.linkedin.com/in/aditi-gupta-777764149/
**Email:** aditi@truefoundry.com
**Tier:** 1
**Background:** Joined TrueFoundry Sept 2024. Builds and deploys AI chat agents; integrates LLM evaluation frameworks into the platform. Former Lead Data Scientist at Delhivery (logistics; truck utilization and damage prediction modeling). Earlier roles at Apna.
**Research hook:** Her work integrating LLM eval frameworks into TrueFoundry's platform overlaps with Amit's production RAG work where MRR measurement and retrieval benchmarking were core to decision-making (switching from FAISS to Milvus based on production-data evaluation).

## Person: Mitanshu Dodia

**Role:** Machine Learning Platform Engineer
**LinkedIn:** https://in.linkedin.com/in/mitanshu-dodia-34b287208
**Email:** mitanshu@truefoundry.com
**Tier:** 3
**Background:** ML and Backend Engineer at TrueFoundry. Previous ML/NLP at Soteria Mental Health AI (Nov 2022 - Aug 2023); SecOps Solution (Feb 2023 - Jun 2023). "Loves turning tricky problems into simple solutions, passionate about AI, coding, and making tech fun."
**Research hook:** His background in ML + backend (same combo as Amit) and focus on platform engineering -- turning hard ML problems into clean platform abstractions -- aligns with Amit's form builder (Pydantic-validated intermediate JSON as the abstraction layer).

## Person: Kunwar Raj Singh

**Role:** Machine Learning Engineer
**LinkedIn:** https://www.linkedin.com/in/kunwar-raj-singh-a18745151/
**Email:** kunwar@truefoundry.com
**Tier:** 3
**Background:** ML Engineer at TrueFoundry, Bengaluru. Won accelData Hackathon top spot with team-not-found for AWS resource management project. Passionate about AI, learning new things; plays classical piano; into DIY projects and homelabs.
**Research hook:** His hackathon win for AWS resource management overlaps with Amit's serverless work on AWS Lambda for video rendering pipeline.

## Person: Kashish Kumar

**Role:** Senior Machine Learning Engineer / Senior Data Scientist
**LinkedIn:** https://www.linkedin.com/in/kashishkumar/
**GitHub:** https://github.com/kashishkumar
**Personal site:** https://www.kashishkumar.com
**Email:** kashish@truefoundry.com
**Tier:** 3
**Background:** Former ExxonMobil. At TrueFoundry as Senior ML Engineer / Senior Data Scientist. Has personal blog on Medium and personal website. "Creates impactful AI products and systems." Active on X as @Kashish__Kumar_.
**Research hook:** His move from ExxonMobil (enterprise/energy sector) to a pure AI infra company mirrors the trajectory Amit is targeting. His personal site/blog signals he cares about sharing technical work publicly.

## Person: Parth Kathuria

**Role:** Talent Lead, People and Culture (Founding Team)
**LinkedIn:** https://www.linkedin.com/in/parth-kathuria-057862171/
**Email:** parth@truefoundry.com (confirmed)
**Tier:** 4
**Background:** People and Culture founding team at TrueFoundry. Prior: Senior Technical Recruiter at HonorVet Technologies; Technical Recruiter at TALENT Software Services and Varite Inc. CS degree from Kurukshetra University. Posted about TrueFoundry funding rounds and actively hiring. Bio: "Building in MLOps (Actively Hiring)".
**Research hook:** His post after TrueFoundry's Series A announcement explicitly called out engineering hiring. He's the primary recruiting contact and has a technical CS background -- so a credentialed email will resonate more than a generic one.

## Email Pattern

Confirmed: firstname@truefoundry.com (from parth@truefoundry.com public source, ZoomInfo shows c***@truefoundry.com for Chirag)

Permutations per contact:
- Primary: firstname@truefoundry.com
- Alt 1: f.lastname@truefoundry.com
- Alt 2: flastname@truefoundry.com

## Resume Tailoring Brief

- Lead with LangChain/LangGraph agentic architecture work (directly matches JD requirement)
- Front-load Milvus + vector DB evaluation bullet (their core infra is vector search + LLM gateway)
- Reorder Technical Skills: "LLMs and Techniques" + "Vector DBs and Retrieval" first; "Languages and Frameworks" (with LangGraph prominent) second; push Hardware/IoT to bottom
- Summary line: rewrite to call out agentic AI platforms, production LLM deployment, LangGraph orchestration
- Drop or minimize hardware TinyML details in experience bullets; keep in Projects section brief
- IIT Delhi bullet: keep the 1,000+ model configs benchmark angle (signals rigorous evaluation methodology -- matching their observability/benchmarking focus)
- Voicer/WeepScope: keep as compact single bullets; they show breadth and national recognition

## Outreach Plan

**Send window:** Tue-Thu 8-11 AM IST (TrueFoundry team is India-based)
**Spacing:** 3-4 days between contacts at same company
**Priority send order:** Chirag Jain (Tier 1), Anant Agarwal (Tier 1), Parth Kathuria (Tier 4), then Mitanshu Dodia, Kunwar Raj Singh, Kashish Kumar, Aditi Gupta
