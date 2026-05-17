# Zomato (Eternal) — Research

## CSV signal (starting hints)

- **Location:** Gurgaon
- **Role title (CSV):** Machine Learning Engineer / Sr AI Engineer
- **Salary band (LPA):** 20-34 LPA
- **Funding stage:** Public (NSE: ETERNAL)
- **Hiring status:** actively hiring
- **Priority score:** 94
- **Match reason:** Zomato + Blinkit jointly hiring AI/ML Engineers to optimize LLMs; Zia AI assistant for restaurants; ML for spam review detection, search ranking, dish tagging.
- **Notes:** Eternal group: Zomato, Blinkit, Hyperpure, District, Nugget. NLP heavy. Python primary. 5000+ employees.

## Links

- Company: https://www.zomato.com
- Careers: https://www.zomato.com/careers
- LinkedIn: https://www.linkedin.com/company/zomato
- Contact: https://www.zomato.com/contact
- Job URL: https://www.instahyre.com/job-365916-sr-ai-engineer-at-zomato-bangalore/

## Full JD signal

**Role:** Sr. AI Engineer / Machine Learning Engineer
**Location:** Gurgaon / Bangalore
**Experience:** 3-7 years
**Salary:** 20-34 LPA

**Core responsibilities:**
- Maintain and optimize large-scale ML infrastructure powering search ranking, recommendations
- Build and improve restaurant + dish recommendation engines
- End-to-end ownership: data pipelines -> training -> real-time prediction serving
- NLP applications: review spam detection, dish tagging, review summaries, sentiment analysis
- LLM optimization: fine-tuning, RLHF, reducing latency and cost at scale
- ML Runtime: Feature Compute Engine, Feature Store, Model Store, Model Serving API Gateway
- Work with Kafka, Airflow, Spark, Pulsar for data streaming

**Tech stack required:**
- Python (primary) or Go
- ML fundamentals, data structures, algorithms
- GenAI / LLM experience (fine-tuning, RLHF)
- Vector databases, embeddings
- Real-time prediction systems at scale
- NLP pipelines

**Zomato ML applications in production:**
- Search ranking (restaurant + dish search, NLP-powered)
- Personalized recommendations (homepage, listing sort, user personalization)
- Spam and review quality detection
- Photo classification (dish/restaurant photos)
- Nugget: AI customer support (15M+ conversations/month, 85% resolution rate)
- ZIA: AI chatbot for restaurant partners
- Weather Union: hyperlocal weather data service

## Last 60 days -- Company

- **Feb 2026:** Eternal signed expanded partnership with OpenAI to deploy AI across Zomato, Blinkit, Hyperpure, District. Deploying contextual AI assistants for restaurant/delivery partners, next-gen search interfaces, and OpenAI coding models into Stitch (internal automation platform).
- **Jan 2026:** Nugget (Zomato's AI CX platform) now handles 15M+ conversations/month at 85% resolution. Launched as enterprise product to external companies. Reduced Zomato support costs from $20M to $9M/year (55% reduction). Built on MongoDB Atlas, Together AI (Llama 70B + 8B).
- **Mar 2025:** Published blog "Elements of Scalable Machine Learning" - documented their 4-component ML Runtime: Feature Compute Engine, Feature Store, Model Store, Model Serving API Gateway.
- **2025:** GenAI team grew from 3 to 20+ engineers. Team hiring across interns and seniors for LLM optimization roles.
- **2025:** Stitch - internal AI orchestration platform for automation across engineering and non-engineering functions.

## Contacts found

### Tier 1 -- Senior ML/AI

**1. Naresh Mehta**
- Role: AVP, Data Science & Analytics at Zomato (current)
- LinkedIn: https://www.linkedin.com/in/naresh-mehta-68a52811/
- IIT Madras grad, 10K+ followers, "Building Zomato"
- Leads: recommendation engines, search algorithms, listing sort, homepage personalization, user personalization, A/B experiments, clickstream analytics, adtech analytics
- Recent: posted hiring for adtech analytics at Zomato (2024). Wrote 2025 ML blog about Feature Store + Model Store infra.
- Research hook: His team's March 2025 ML Runtime blog (Feature Store / Model Store architecture) maps directly to Amit's production Milvus + VLLM infra work at Silver Touch (separate model serving, vector DB at production scale, 50K queries/month).
- Email: naresh.mehta@zomato.com

**2. Vivek Gupta**
- Role: Senior Developer, Nugget at Zomato (current) - building Nugget AI CX platform
- LinkedIn: https://www.linkedin.com/in/vivek-gupta-545a06197
- Key quote from MongoDB case study: "Nugget was built to reflect the reality of enterprise customer support, where conversations are fragmented, context is constantly evolving, and automation must coexist with human judgment."
- Nugget uses Llama 70B (intent detection) + Llama 8B (chat completion) via Together AI; multi-class classification, policy guardrails, JSON-to-text pipeline, MongoDB Atlas
- Research hook: Amit built a very similar multi-model + permission-aware conversational system at Vivansh (LangGraph state machine, GPT-4o + permission filtering, 500+ concurrent users). The architecture parallels Nugget's policy-layer + intent classification pattern.
- Email: vivek.gupta@zomato.com

### Tier 3 -- Junior/Mid ML

**3. Anshuman Mishra**
- Role: ML @ Zomato (current), Bengaluru
- LinkedIn: https://www.linkedin.com/in/anshuizme OR https://www.linkedin.com/in/athletickoder
- 29K+ followers; active poster on ML topics
- Recent posts: LoRA fine-tuning mechanics (attention-only LoRA vs MLP-only LoRA, parameter efficiency), ML engineering interview questions
- Ex-Google AI Consultant before Zomato
- Research hook: His LoRA fine-tuning posts connect to Zomato's LLM optimization work; Amit's empirical multi-model testing (Qwen3-Coder winning over GPT-4o in blueprint generation after benchmarking) is the same data-driven mindset.
- Email: anshuman.mishra@zomato.com

**4. Anish Majumder**
- Role: Data Scientist @ Zomato (current), IIT Delhi
- LinkedIn: https://www.linkedin.com/in/anish-majumder-15b734121/
- weatherunion.com listed as company - works on/with Zomato's WeatherUnion hyperlocal weather service
- IIT Delhi connection: Amit did research internship at IIT Delhi (Dr. Lalan Kumar) -- mutual ground
- Research hook: IIT Delhi shared ground + Amit's production embedding/retrieval work overlaps with Zomato's recommendation and NLP systems.
- Email: anish.majumder@zomato.com

**5. Anukul Kashyap**
- Role: Data Science @ District (Zomato subsidiary), Gurugram (current)
- LinkedIn: https://www.linkedin.com/in/anukulsingh125
- NIT Agartala grad
- District is Zomato's premium dining and experiences platform (part of Eternal)
- Research hook: District's recommendation + personalization work is the applied DS angle; Amit's 2-stage retrieval and personalization (per-user permission + course filtering at Vivansh) demonstrates the same multi-constraint recommendation thinking.
- Email: anukul.kashyap@zomato.com

### Tier 4 -- HR / Recruiters

**6. Shreya Mishra**
- Role: Talent Acquisition Specialist at Zomato (current), Gurugram
- LinkedIn: https://www.linkedin.com/in/shreya-mishra-2b3baa2ba/
- MDI Gurgaon; 61 connections (newer to TA role)
- Email: shreya.mishra@zomato.com

**7. Ananya Jain**
- Role: Talent Acquisition Strategist, Zomato (current), Bengaluru
- LinkedIn: https://www.linkedin.com/in/ananyajain31
- "Building Zomato"; NextLeap Top PM Fellow
- Email: ananya.jain@zomato.com

**8. Namira A.**
- Role: People and Culture, Zomato (current), Delhi
- LinkedIn: https://www.linkedin.com/in/namira-a-a46b4818b/
- 22K+ followers; prominent in Zomato's people brand
- Email: namira.a@zomato.com (best guess)

## Email pattern confirmed

Primary: firstname.lastname@zomato.com (90%+ of employees)
Secondary: firstname.lastinitial@zomato.com

## Resume tailoring brief

- Lead with RAG/retrieval production work -- maps to search ranking and recommendation infrastructure
- Rewrite summary to mention NLP, search ranking, LLM optimization at scale
- Bring up Milvus benchmarking (FAISS -> Milvus, 45% -> 95% MRR) -- mirrors their Feature Store / Model Store architecture work
- Multi-model orchestration (GPT-4o + Qwen3-Coder empirical selection) maps to their LLM optimization mandate
- LangChain + LangGraph agentic architecture maps to Nugget's multi-agent CX pipeline
- Drop hardware/TinyML bullets entirely -- pure software/LLM role
- Keep BGE-M3 embedding benchmarking, vLLM serving, on-prem deployment details

## Outreach plan

- Tiers 1 and 3: Engineering-focused template (Template 3)
- Tier 4: Recruiter template (Template 2)
- Send window: Tue-Thu, 8-11 AM IST (Gurgaon / Delhi / Bengaluru recipients all in IST)
- Space contacts 3-5 days apart within company
