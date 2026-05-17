# Nurix AI — Research Notes

## Company Overview

- **Founded:** 2024
- **Co-founders:** Mukesh Bansal (CEO, ex-Myntra co-founder, ex-Curefit) and Abhishek Asawa (co-founder — DO NOT contact, >50-person company rule)
- **HQ:** HSR Layout, Bengaluru (India ops) + Mountain View, CA (US entity)
- **Size:** 84+ employees (51-200 on LinkedIn, Aug 2025 count)
- **Funding:** $42.2M total
  - $27.5M Series A — Accel + General Catalyst (Sep 2024)
  - $14.7M Series A extension — Prosus (March 7, 2026)
  - Incubated through Meraki Labs (Mukesh Bansal's venture studio)

## Products and Platform

- **NuPlay** (launched June 2025): Enterprise voice AI platform — low-latency, human-like voice agents
  - 250,000+ customer conversations/month
  - 99% accuracy with resolution activity; 80% of inquiries automated
  - 50%+ workflow efficiency gains; 65%+ support cost reduction
  - Integrates with 300+ enterprise systems (CRM, ERP, CCaaS)
  - SOC 2, GDPR, HIPAA, ISO compliant
- **NuRep:** AI sales representatives
- **NuPulse:** AI Monitoring and Insights Hub
- **NuPilot:** Workflow automation for enterprises
- Multi-agent orchestration across workflows

## Target Industries

Retail, Insurance, Financial Services, Collections and Mortgage, Home Services, Health and Fitness, Education, Real Estate

## Key Clients

AllFly, First Mid Insurance, Super.Money

---

## Full JD Signal

**Role: ML Engineer / AI Engineer (2-4 yrs, Bengaluru, Onsite)**

Responsibilities:
- Design, train, optimize custom ASR/TTS models (stated goal: overcome limitations of Sarvam ASR)
- Develop agents that handle interruptions, natural pauses, real-world voice variability
- Contribute to Voice-to-Voice (V2V) systems using state space models (Mamba, Hamba)
- Develop Agentic RAG pipelines and LLM orchestration for context-aware voice agents
- Build self-learning agents for continuous improvement
- Bring models into real-time, low-latency production environments

Tech stack:
- Python, PyTorch, TensorFlow, JAX
- ASR, TTS, NLP, LLM fine-tuning, dialogue systems
- Low-latency real-time ML applications; ML lifecycle and deployment
- Open-source contributions or research publications preferred
- Multilingual / Indian-context ASR/TTS preferred

Other open roles as of May 2026: Prompt Engineer, QA Engineer (Conversational AI), Product Lead, Sr. DevOps, Enterprise Architect, Product Manager.

---

## Last 60 Days — Company Activity

**LinkedIn:**
1. **May 16, 2026 (1 day ago):** Mortgage lenders use case — Nurix voice AI handling payment reminders, delinquency follow-ups, 2 AM status checks. "The question for lenders is not 'if', it is 'how fast before competitors close the gap.'"
2. **May 12, 2026 (5 days ago):** Co-hosting event with Deepgram on May 22 in SF. Theme: "latency, language mirroring, interruption handling, the gap between pilot and scale." Over 1 million calls handled. Speakers: Anuj Jain (Head of Product, Nurix) and Adam Proschek (Deepgram). 30 seats only.
3. **Jan 2026 (4 months ago):** Multi-agent orchestration explainer for NuPlay — multiple specialized agents coordinating context and decisions.
4. **Nurix hackathon 2025 ("AI Agents to Create an Autopilot Enterprise"):** Internal team hackathon where engineers built multi-agent systems in 24 hours.

**News:**
- March 7, 2026: $14.7M additional from Prosus — confirms continued investor confidence post-Series A
- June 17, 2025: NuPlay launch — 5x QoQ growth, 250K+ monthly calls, enterprise deployments live
- Sep 2024: $27.5M Series A close (Accel + General Catalyst)

---

## Team — Named Individuals

### TIER 1 — Senior AI/ML

**Pushkar Patel**
- Role: ML Engineer at Nurix
- Specialty: inference engineering, kernels, agentic workflows, post-training
- LinkedIn: https://www.linkedin.com/in/thepushkarp/
- Background: Samsung Research | GSoC 2022 | IIIT Vadodara
- Followers: ~2K (active poster)
- Email: pushkar.patel@nurix.ai
- Research hook: Nurix featured Pushkar in their NEX video series on voice AI evaluation. He made the specific argument that evaluating voice AI is fundamentally different from text LLMs — "latency, turn-taking, context retention, tone, recovery from failure, and behavior across multi-step workflows matter just as much as the final answer." He also reposted a paper on low-rank circuit conditioning (extracting and reusing neural network capabilities) — shows genuine interest in model internals and post-training research.

**Syed Amjad Ali**
- Role: Building Voice AI at Nurix
- LinkedIn: https://www.linkedin.com/in/amjad4/
- Background: Razorpay (distributed systems at scale) + Akamai (CDN/edge infrastructure, sub-50ms delivery) | PES University
- Email: amjad.ali@nurix.ai
- Research hook: His Akamai background in low-latency CDN delivery maps directly to the real-time constraints of voice AI (NuPlay targets sub-200ms response). At Razorpay he operated high-throughput fault-tolerant payment infrastructure. That infrastructure thinking applied to voice AI latency problems is the specific angle.

### TIER 3 — Junior/Mid AI/ML

**Tanmay Srivastava**
- Role: MLE at Nurix AI
- Education: CSE, BITS Pilani
- LinkedIn: https://www.linkedin.com/in/tanmay-srivastava-a0338623a
- Email: tanmay.srivastava@nurix.ai
- Research hook: Won Nurix internal hackathon. His post: "In just 24 hours, we moved far beyond a simple 'call-the-LLM-and-print-response' setup and built a fully functional multi-agent AI system from the ground up with smart coordination in handling audio-video streaming packets and decent latency." Also reposts Nurix content on multi-agent orchestration and the full voice AI pipeline (ASR to NLU to process layer to NLG to TTS).

**Meghana Krishna**
- Role: AI Engineer at Nurix
- LinkedIn: https://www.linkedin.com/in/meghana-krishna-5771ab204
- Email: meghana.krishna@nurix.ai
- Research hook: Working on Nurix's sentinel layer for AI agent data privacy — addressing how agent logs become "PII black holes" with SSNs, API secrets, and PHI cascading through chains. Nurix's approach uses NER + regex techniques plus SHA-256 obfuscation. Security-conscious, privacy-first angle on production AI agents.

**Damodar Hegde**
- Role: AI Engineer at Nurix.ai
- Background: ex-Zigment.ai (AI-powered customer engagement/sales automation)
- LinkedIn: https://www.linkedin.com/in/damodar-hegde
- Email: damodar.hegde@nurix.ai
- Research hook: ex-Zigment.ai — hands-on building AI for automated sales and customer engagement workflows, the exact domain Nurix serves with NuRep and NuPlay.

### TIER 4 — Recruiter/HR

**Khushi Rathi**
- Role: Talent Partner at Nurix
- Education: Jain (Deemed-to-be University)
- LinkedIn: https://www.linkedin.com/in/khushi-rathi-5351a81b5
- Followers: 7,943 (highly active)
- Email: khushi.rathi@nurix.ai
- Research hook: Posted about Nurix Offsite 2025 "Agents of Change" — 264 reactions, 20 reposts. Her caption: "one of those rare days where you get to pause the sprint, zoom out, and genuinely feel how far we've come." Actively posts AI engineer and ML engineer job listings at Nurix.

---

## Email Pattern

- Primary (59.3%): firstname.lastname@nurix.ai
- Secondary: firstname@nurix.ai
- Tertiary: flastname@nurix.ai (first initial + last name)

## Amit's Strongest Proof Points for This Role

- Agentic RAG pipeline: LangChain + LangGraph, 2-stage retrieval, 50K+ queries/month at 95% MRR (Silver Touch) and 80% MRR (Vivansh)
- Multi-model LLM orchestration in production: GPT-4o + Qwen3-Coder + Gemini — each chosen empirically per subtask
- Low-latency production AI: 8s response time under 500+ concurrent users; cut from 16s to 8s by migrating vector infra
- Permission-aware retrieval with 250+ granular permissions per query — dynamic, no caching
- LangGraph stateful graph orchestrating permission filter + retrieval + tool-calling + answer generation
- BGE-M3 selected after benchmarking 6 embedding models on production data
- FAISS to Milvus migration: 45% to 95% MRR
- Samsung Solve for Tomorrow top 10 (70,000+ participants) — on-device TinyML with 2ms inference
- IIT Delhi research internship: 1,000+ model configurations tested, CNN-BiLSTM hybrid selected empirically
- Azure AI Engineer Associate certified
