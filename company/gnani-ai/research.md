# Gnani.ai -- Research Notes

## Company Overview

- **Founded:** ~2016
- **Co-founders/CEO/CTO:** Ganesh Gopalan (CEO), Ananth Nagaraj (CTO) -- DO NOT contact (>50-person company rule)
- **HQ:** Bengaluru, India
- **Size:** 169+ employees (55% YoY growth as of Aug 2025)
- **Funding:** $17.7M total
  - Series A: ~$4M (multiple closes)
  - $10M Series B: March 2026, led by Aavishkaar Capital + Info Edge Ventures
  - Investors: Samsung Venture Investment, Commonwealth Inclusive Growth Services, Aavishkaar Capital, Info Edge Ventures
- **LinkedIn:** 114K followers, 51-200 employees bracket

## Products and Platform

- **Inya VoiceOS** (Feb 2026): India's first 5-billion-parameter voice-to-voice foundational model. Inaugurated by PM Modi at India AI Impact Summit 2026. Supports 15+ Indian languages, 24 kHz audio output, sub-second latency. Roadmap: 14B then 32B then 70B parameter model.
- **Vachana STT** (Dec 2025/Feb 2026): Indic speech-to-text model, trained on 1M+ hours of real-world voice data spanning 1,000+ domains under IndiaAI Mission
- **Vachana TTS** (Feb 2026): Text-to-speech with voice synthesis and voice cloning
- **Voice AI Agents:** Omnichannel, multilingual, industry-specific SLMs for enterprise automation
- 30M+ daily voice interactions, 200+ enterprise clients including Fortune 500
- Revenue target: Rs 160 crore FY26 (from Rs 56 crore FY25)
- Selected under IndiaAI Mission (12 orgs, govt-backed sovereign AI program)

## Target Industries

BFSI, Telecom, Healthcare, Automotive, Government, Retail, E-commerce

## Key Clients

Fortune 500 companies (undisclosed names)

---

## Full JD Signal

### Role 1: Applied ML Engineer - GenAI (Post Training)
**URL:** https://careers.gnani.ai/apply/App-Ben-2026-01-21-24
**Exp:** 3-5 years | Bengaluru, Onsite

**Key Responsibilities:**
- Lead post-training, alignment, and instruction fine-tuning of India's foundational LLMs (IndiaAI Mission)
- Build and optimize SFT (Supervised Fine-Tuning) pipelines for instruction-following and chat models
- Alignment: DPO, GRPO, RFT, reward modeling, multi-turn chat fine-tuning
- Drive fine-tuning for low-resource Indic languages (Bodo, Manipuri, Santali, Konkani, Dogri)
- Dataset versioning, automated validation, deduplication, toxicity filtering
- Fine-tuning libraries: HuggingFace TRL, OpenRLHF, DeepSpeed-Chat, NVIDIA NeMo Alignment, Axolotl, Colossal-AI
- LoRA/QLoRA/PEFT workflows at scale

**Must-haves:** Python, PyTorch, HuggingFace ecosystem, LLM post-training experience, Indic language alignment preferred

### Role 2: Applied ML Engineer - GenAI (RAG and AgenticAI Frameworks)
**URL:** https://careers.gnani.ai/apply/App-Sal-2026-01-21-27
**Exp:** 4-8+ years

**Key Responsibilities:**
- End-to-end RAG: ingestion -> chunking -> embeddings -> indexing -> retrieval -> reranking -> grounded generation
- Hybrid search, multi-hop retrieval, query rewriting, multilingual support for Indic languages
- Vector DBs: Qdrant, MongoDB Atlas Vector Search, FAISS, Pinecone, Weaviate, Milvus/Zilliz, Elastic/OpenSearch
- Multi-agent workflows: LangGraph, CrewAI, AutoGen, LangChain LCEL; ReAct, Reflexion, Tree-of-Thought
- LLM inference: vLLM, SGLang, TensorRT-LLM, TGI with quantization
- Document intelligence: OCR (Unstructured, DocTR, LayoutLMv3)
- Evaluation: Ragas, DeepEval, LangSmith

**Must-haves:** Open-source LLMs (LLaMA, Qwen, Mistral), Qdrant + MongoDB Vector Search expertise

---

## Last 60 Days -- Company Activity

1. **May 2026:** Hired 8 senior leaders after Series B -- Samuel Thomas (HR Director), Vasuta Agarwal (CRO), Rajesh Pantina (VP Marketing), and others across BFSI, product, AI delivery
2. **March 27, 2026:** $10M Series B close (Aavishkaar Capital + Info Edge Ventures)
3. **Feb 19, 2026:** Expanded Inya VoiceOS with two new speech models (Vachana STT + Vachana TTS)
4. **Feb 17, 2026:** PM Modi inaugurated Inya VoiceOS (5B param voice-to-voice model) at India AI Impact Summit 2026 -- major public milestone
5. **Feb 2026:** CTO Ananth Nagaraj stated "Specialised SLMs better suited for India needs than LLMs" (Business Standard interview)

**LinkedIn activity:** 114K followers; active posts on voice AI, enterprise automation, Inya VoiceOS launch; job listings for AI Engineering Manager, Principal Data Scientist Speech & LLMs

---

## Team -- Named Individuals

### TIER 1 -- Senior AI/ML

**Avinash Benki**
- Role: Lead NLP Engineer | Multimodal Speech & Audio LLMs | ASR, TTS, Conversational AI | Indic Language AI
- LinkedIn: https://in.linkedin.com/in/avinash-benki
- Background: At Gnani since 2019 (started as Senior NLP Engineer, promoted to Lead). 6+ years building NLP at scale. ML Nanodegree, Udacity.
- Email: avinash.benki@gnani.ai
- Research hook: Featured in gnani.ai's "People of gnani.ai" YouTube series as Lead NLP Engineer. His headline covers the exact stack: multimodal speech + audio LLMs, ASR, TTS, Indic language AI -- which spans both JDs. He has been there through the full Vachana STT/TTS and Inya VoiceOS build.

**Abhilash Sudhamshu**
- Role: Technical Leader | Driving Solutions and Delivery @ Gnani.ai | Conversational AI, GenAI, LLM
- LinkedIn: https://www.linkedin.com/in/abhilash-sudhamshu (search: "Abhilash Sudhamshu gnani")
- Background: Ex-Quantiphi (major AI/ML enterprise firm), Ex-Accenture
- Email: abhilash.sudhamshu@gnani.ai
- Research hook: Came from Quantiphi (known for large-scale ML deployment for Fortune 500) to lead technical delivery at Gnani across Conversational AI, GenAI, and LLM stacks. The Quantiphi-to-Gnani move maps exactly to Amit's current path: enterprise AI delivery to voice AI platform.

**N Nanda Kumar**
- Role: Senior NLP Engineer at Gnani.ai | NLP | GenAI | LLM Inferencing | LLM Training | RAG | SLM | LLM Finetuning
- LinkedIn: https://www.linkedin.com/in/n-nanda-kumar (search result)
- Background: Senior NLP Engineer at Gnani
- Email: n.nandakumar@gnani.ai (best guess -- name format uncertain; may be empty if bounces)
- Research hook: His headline explicitly lists both "LLM Training" and "LLM Finetuning" alongside RAG and SLM -- he is almost certainly working on the post-training and RAG pipelines for Vachana/Inya models. His profile also mentions "Vibe Coding" (newer term), signaling he keeps up with current tooling.

### TIER 3 -- Junior/Mid AI/ML

**Advait Joglekar**
- Role: Building 'Sovereign' AI @Gnani.ai | IIT-Madras
- LinkedIn: https://www.linkedin.com/in/advait-joglekar/
- Background: IIT-Madras (BS Data Science). Published researcher: Indic language translation (multilingual NLP), voice conversion using Diffusion-Transformer + conditional flow matching. Working on IndiaAI Mission sovereign AI stack at Gnani.
- Email: advait.joglekar@gnani.ai
- Research hook: His IIT-M research covers textless self-supervised voice conversion -- directly relevant to the Inya VoiceOS voice-to-voice model architecture. He openly uses the phrase "Sovereign AI" to describe his work, which connects to Gnani being one of 12 orgs funded by the government IndiaAI Mission.

**Ananya Angra**
- Role: Speech AI Engineer @ Gnani.ai | MTech (By Research) @ IIT Mandi
- LinkedIn: https://www.linkedin.com/in/ananya-angra
- Background: MTech research background from IIT Mandi (strong speech/NLP research program). Research-to-production engineer in Gnani's voice AI stack.
- Email: ananya.angra@gnani.ai
- Research hook: IIT Mandi's MTech By Research program is known for production-oriented speech research. Her move directly into Speech AI at Gnani bridges the research-to-deployment gap that both JDs emphasize.

**Anantharaman R**
- Role: Machine Learning Engineer | Speech ML
- LinkedIn: https://www.linkedin.com/in/anantharaman-r (from people page listing)
- Background: MLE focused specifically on Speech ML at Gnani
- Email: anantharaman.r@gnani.ai
- Research hook: Speech ML at Gnani during the Inya VoiceOS launch period -- working on core speech modeling alongside the team that built India's first voice-to-voice foundational model.

### TIER 4 -- HR/Recruiter

**Samuel Thomas**
- Role: Director -- Human Resources at gnani.ai
- LinkedIn: https://in.linkedin.com/in/samuel-thomas-742607b8
- Background: 16+ yrs global HR experience. Previous: Google, Geektrust, Jiva. Appointed May 2026 post Series B as one of 8 senior hires.
- Email: samuel.thomas@gnani.ai
- Research hook: Brand new hire (May 2026) as HR Director following the $10M Series B. He is actively building the team from scratch in his new role -- this makes him receptive to strong direct applications.

**Sabari Prasad**
- Role: Lead -- Talent Growth & Experience at gnani.ai
- LinkedIn: https://in.linkedin.com/in/sabari-prasad
- Background: Active on LinkedIn (8K followers). Posts job listings for Gnani including GTM operations and enterprise sales roles.
- Email: sabari.prasad@gnani.ai
- Research hook: "Talent Growth & Experience" title (not just "recruiter") signals focus on employer brand and hiring experience. Active on LinkedIn with Gnani content and job posts.

**Sanjana Swostika**
- Role: HRBP @ Gnani.ai | Talent Acquisition | HR Operations
- LinkedIn: https://www.linkedin.com/in/sanjana-swostika (from search)
- Background: HR Business Partner at Gnani covering both talent acquisition and HR operations. Based in Bengaluru.
- Email: sanjana.swostika@gnani.ai
- Research hook: Dual HRBP + TA role means she is both the business partner for hiring managers and the recruiter for open roles -- strong path to AI/ML openings.

---

## Email Pattern

- Primary (confirmed): firstname.lastname@gnani.ai
- Source: LeadIQ, multiple press release contacts, confirmed pattern

## Amit's Strongest Proof Points for This Role

**For Post Training JD:**
- HuggingFace ecosystem in production (models, tokenizers, inference pipelines)
- IIT Delhi research: 1,000+ model configurations tested on CNN-BiLSTM for audio classification -- empirical experimentation at scale
- Multi-model orchestration: GPT-4o, Qwen3-Coder, Gemini selected and evaluated per subtask empirically
- Samsung Solve for Tomorrow top 10: on-device TinyML with 2ms inference (low-resource model deployment)
- WeepScope project: 1D CNN+GRU on audio signals for cry classification

**For RAG/Agentic JD:**
- Production agentic RAG: LangChain + LangGraph, 50K+ queries/month, 95% MRR
- FAISS to Milvus migration: 45% to 95% MRR (vector DB expertise)
- BGE-M3 selected after benchmarking 6 embedding models on production data
- Permission-aware retrieval: 250+ granular permissions per query, PostgreSQL ground truth
- LangGraph stateful graph: permission filter + retrieval + tool-calling + answer generation
- Low-latency production: 8s under 500+ concurrent users (cut from 16s)
- OCR pipeline: 200+ PDFs processed in month one
- Azure AI Engineer Associate certified
