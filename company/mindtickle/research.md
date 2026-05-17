# Mindtickle -- Research Notes

**Role:** SDE-III AI/ML (GenAI/LLM) -- CoE-ML (Center of Excellence for Machine Learning)
**Location:** Pune, India
**Salary:** 25-38 LPA
**Company size:** 501-1K employees
**Hiring status:** Actively hiring

---

## Company Overview

Mindtickle is the leading AI-powered revenue enablement platform. Product helps sales teams onboard faster, coach reps in real time, and close more deals. The CoE-ML team embeds AI across the entire product: Copilots, AI-powered role plays, automated content curation, intelligent coaching, deal intelligence, and digital sales rooms.

Email pattern: **first.last@mindtickle.com** (93% confirmed via LeadIQ)

---

## Full JD Signal

**Tech stack (explicit from JDs):**
- Python (primary), Java, Go
- LangGraph, CrewAI for agentic workflows
- LiteLLM, Portkey, TrueFoundry for AI gateway / LLM governance
- LangFuse, Maxim, Weights & Biases for eval frameworks
- Pinecone, Weaviate, pgvector for vector DBs
- AWS, Docker, Kubernetes
- Datadog, Prometheus, Grafana for observability
- Amazon Bedrock for LLM fine-tuning (from AWS case study)

**SDE-III specific signals:**
- Lead end-to-end design, prototyping, implementation of AI systems
- Architect GenAI/LLM integrations: prompt engineering, context management, agentic workflows
- Production-grade code with CI/CD on AWS/K8s
- Post-deployment monitoring, performance testing, SLA alerting
- Mentor SDE-1/SDE-2; lead design reviews and brown-bag talks
- Cross-functional work with product, QA, data engineering, DevOps

**Must-haves:**
- 5+ years total; 2+ years production AI/ML
- RAG pipelines, LLM-powered features, model inference services
- Agentic frameworks (LangGraph, CrewAI, LangChain)
- AI gateway experience for LLM cost governance
- Evaluation discipline: precision/recall, BLEU, ROUGE, LLM-as-judge

**Strong fit notes for Amit:**
- RAG chatbot at 95% MRR / 50K+ queries/month maps directly to their production scale requirements
- BGE-M3 embedding benchmarking (6 models tested) maps to their model selection requirement
- Agentic workflows (AI Course Builder, Form Builder) map to their LangGraph/CrewAI focus
- Milvus + PostgreSQL RBAC 2-stage retrieval = their vector DB + permission-aware retrieval combo
- Production monitoring / observability = their Datadog/Prometheus/Grafana requirement

---

## Last 60 Days -- Company

- **April 21, 2026**: Launched **ElevateOS** -- "the first agentic operating system for revenue enablement." Built on MCP (Model Context Protocol) and A2A standards. Houses AI Tutor, AI Roleplay, AI Manager Coach, AI Content Creation, Deal Guide, AI Simulator, and Copilot. Powered by a "Behavior Intelligence Context Engine" (proprietary). Designed to interoperate with external AI agents and BYO model infrastructure. CEOs Krishna Depura and COO Deepak Diwakar quoted in launch.
- **April/May 2026**: Yogita Malviya (Sr. TA Partner) posted about hiring Senior TPM for "high-impact, AI-first engineering programs" at Mindtickle Bengaluru.
- **May 13, 2026**: Hitesh Nankani attended the first Claude Code meetup in India and posted about production LLMOps being the gap most engineers miss.
- **AWS case study (recent)**: Mindtickle uses Amazon Bedrock for LLM fine-tuning; Amazon Q for internal development efficiency. The Mindtickle Copilot is the flagship GenAI product.

---

## Person: Ajay Dubey

**Role:** Senior Engineering Manager -- Driving GenAI & Agentic AI Infrastructure | LLMOps, Prompt Engineering & AI Observability
**Tier:** 1
**LinkedIn:** https://www.linkedin.com/in/ajay0221/
**Email:** ajay.dubey@mindtickle.com
**Background:** Ex-AppLift, Ex-Groupon | IIIT-H | 10+ years engineering experience

**Recent activity:**
- Posted about hiring SDE-III COE-ML at Mindtickle (referral post, March/April 2026). Described the team as "reshaping sales enablement with AI" using LLMs, NLP, and speech AI. Post got 54 reactions.
- Leads the GenAI & Agentic AI infra team -- LLMOps practices and building trustworthy, scalable AI systems.
- His LinkedIn headline specifically calls out LLMOps, Prompt Engineering, AI Observability -- the exact problem set Amit worked on.

**Research hook:** He directly manages the CoE-ML hiring pipeline and posted the SDE-III opening. His focus on production LLMOps infrastructure maps to Amit's multi-tenant RAG with custom evaluation and embedding benchmarking.

---

## Person: Hitesh Nankani

**Role:** SDE-III (AI & Engineering) -- leading AI initiatives and driving org-wide AI adoption
**Tier:** 1
**LinkedIn:** https://www.linkedin.com/in/hitesh-nankani-04408115a/
**Email:** hitesh.nankani@mindtickle.com
**Background:** 8 years AI/ML software engineering | Ex-Myntra | NSIT Delhi

**Recent activity:**
- **May 13, 2026 (4 days ago):** Attended the first Claude Code meetup in India. Post excerpt: "Most of the community is still treating a prompt as the entire solution. In reality, it's just one component in a much larger machine. I'm seeing very little focus on the 'Day 2' problems: E2E LLMOps, automated evaluation frameworks, and the complex orchestration required to make a model reliable in a production environment. This is exactly what I've been focused on at Mindtickle." Hashtagged: #LLMOps #GenAI #SystemDesign #Reliability
- **Late April 2026 (3 weeks ago):** Published "One Loop, Three Patterns: A Practical Guide to Multi-Agent Orchestration" in Towards AI. Argues most implementations conflate three distinct orchestration patterns, which is where the complexity comes from.
- **January 2026 (4 months ago):** Led Mindtickle's first internal workshop on meta-prompting. Built in-house tools supporting 7+ projects in 60 days. "Stop chatting with AI and start architecting it."

**Research hook:** He attended the first Claude Code meetup in India and wrote about "Day 2 LLMOps" being the real challenge. Amit's production RAG (custom eval pipeline, BGE-M3 benchmarked vs 5 others, 50K/month) is exactly this problem. Best hook in the batch.

---

## Person: Aayush Desai

**Role:** SDE-II @MindTickle | Go | Java | Agentic AI | AWS | Kafka | Docker | MySQL
**Tier:** 3
**LinkedIn:** https://www.linkedin.com/in/aayush-desai-40a3741b5/
**Email:** aayush.desai@mindtickle.com
**Background:** DA-IICT (Dhirubhai Ambani Institute) | Pune

**Recent activity:**
- No original posts in last 6 months; mostly comments.
- LinkedIn headline explicitly includes "Agentic AI" -- actively working on Mindtickle's agentic seller platform.
- Built Seller Copilot using RAG at Mindtickle (agentic platform helping sellers close deals faster); reduced unit testing time 50% using GenAI tools.

**Research hook:** He built Mindtickle's agentic Seller Copilot with RAG. Amit's multi-tenant RAG (Milvus + RBAC) and AI Course Builder (multi-model orchestration) are directly adjacent to his work. Email asks "you should talk to Amit" framing (Tier 3 IC ask).

---

## Person: Yogita Malviya

**Role:** Senior Talent Acquisition Partner @MindTickle
**Tier:** 4
**LinkedIn:** https://in.linkedin.com/in/yogita-malviya-b19b14b2
**Email:** yogita.malviya@mindtickle.com
**Location:** Noida, Uttar Pradesh (remote TA)
**Followers:** 48,013

**Recent activity:**
- April/May 2026 (3 weeks ago): Posted about hiring Senior TPM for "high-impact, AI-first engineering programs" at Mindtickle Bengaluru.
- Regularly posts about open Mindtickle roles; most visible TA voice for the company on LinkedIn.

**Research hook:** She actively posts about AI-first engineering programs at Mindtickle. Email frames Amit as a clean match for the SDE-III CoE-ML opening.

---

## Person: Shilpa Malhotra

**Role:** Talent Acquisition Head at Mindtickle
**Tier:** 4
**LinkedIn:** https://in.linkedin.com/in/malhotrashilpa
**Email:** shilpa.malhotra@mindtickle.com

**Background:** Previously Senior Manager TA at AgroStar (scaled TA function); Cvent before that.

**Research hook:** Heads all TA at Mindtickle. With ElevateOS launching and CoE-ML open reqs, she owns getting AI/ML engineers hired. Short direct intro from Amit with the SDE-III COE-ML opening as hook.

---

## Person: Sondarya Nagarkar

**Role:** Talent Acquisition Partner at Mindtickle
**Tier:** 4
**LinkedIn:** https://www.linkedin.com/in/sondarya-nagarkar-384086220/
**Email:** sondarya.nagarkar@mindtickle.com
**Location:** Pune Division, Maharashtra (same city as the role)

**Research hook:** TA Partner in Pune -- directly involved in local engineering hiring for the SDE-III AI/ML role in Pune.

---

## Email Pattern

**Confirmed:** first.last@mindtickle.com (93% of employees per LeadIQ)

Permutations to include:
- firstname.lastname@mindtickle.com (primary)
- f.lastname@mindtickle.com
- firstnamelastname@mindtickle.com
