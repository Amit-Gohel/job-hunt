# Part 2: Cold Email Templates + The Anti-AI-Detection Playbook

*Templates personalized for Amit Gohel (AI/ML Engineer) + a guide to making every email read as human-written.*

---

## The 3 Templates

### Template 1 — Startup Founder / CEO (seed to Series B)

**Subject:** ran your platform through a RAG benchmark — thoughts

---

Hi [First name],

Saw [Company]'s Series A announcement last month and went down a rabbit hole on the [specific product feature, e.g., "agent memory layer"] you demoed at [conference / on Twitter / on their blog].

Quick context: I spent the last year rebuilding RAG infrastructure at Vivansh — multi-tenant, permission-aware, 50K+ queries/month, MRR from 45% to 95% after migrating off FAISS. The bit I think you'd find interesting: the 2-stage retrieval with a dedicated permission index. Wrote up a short teardown of how I'd approach the same problem if it came up at [Company] — happy to send it over.

Not pitching anything. Just curious whether you're hiring on the ML side this quarter, and if so, whether a 20-min call makes sense.

Amit
amitgohel.dev

---

### Template 2 — Recruiter / HR

**Subject:** AI/ML engineer — 2 yrs production RAG, MS Azure AI cert

---

Hi [First name],

Reaching out directly because I think my background is a clean match for what [Company] tends to hire for on the AI side.

Short version: 2+ years shipping production AI — RAG chatbots at 95% MRR / 50K queries per month, on-prem OCR pipelines for sensitive docs, multi-model orchestration with GPT-4o, Qwen, Gemini. Azure AI Engineer Associate certified. Most recent work was at Vivansh Infotech in Ahmedabad; before that, a research stint at IIT Delhi.

Resume and live projects: amitgohel.dev

If there's an open AI/ML role I should be looking at, I'd appreciate a pointer. If not, no worries — would still be happy to be on your radar for future openings.

Thanks,
Amit

---

### Template 3 — Engineering Manager / Tech Lead

**Subject:** question about [Company]'s retrieval stack

---

Hi [First name],

Read your [blog post / talk / Twitter thread] on [specific topic — e.g., "scaling Milvus past 100M vectors"] a couple of weeks ago. The bit about [specific detail] matched something I ran into rebuilding our chatbot infra at Vivansh — we ended up with BGE-M3 + a reranker after testing 6 embedding models on production data, but the latency tradeoff was painful until we layered intent classification on top.

Reason I'm writing: I'm 2 years into AI/ML (RAG at 50K queries/month, on-prem document pipelines, video gen orchestration) and I've been quietly tracking what [Company] is shipping. If your team is hiring or planning to hire on the ML side, I'd love 15 minutes to hear how you think about [their specific technical bet].

If not the right time, totally understood.

Amit
github.com/amit-gohel | amitgohel.dev

---

## Follow-up Templates

### Follow-up #1 (Day 3-4)

**Subject:** re: [original subject]

Hi [First name],

Bumping this up in case it got buried. Since I sent the last email, I [specific new thing — e.g., "shipped a benchmark comparing our 6 tested embedding models on a public dataset" / "read your latest post on X"].

If now's not the right time, no worries — happy to circle back next quarter.

Amit

---

### Follow-up #2 (Day 10)

**Subject:** re: [original subject]

Hi [First name],

Last note from me on this. If [Company] isn't actively hiring on ML right now, totally understood — would still appreciate being on your radar for when it does come up.

Either way, good luck with [specific recent thing they're working on].

Amit

---

## How to make these *not* read as AI-written

LLMs leave fingerprints. Recruiters and hiring managers now recognize them by feel, even when they can't articulate why. Here are the patterns to strip out.

### The AI vocabulary that gives it away instantly

Words and phrases LLMs over-use. **Cut every one of these:**

| Avoid | Why |
|-------|-----|
| delve, delve into | The most-flagged AI tell |
| intricate, intricacies | Almost never appears in real email |
| pivotal | Business jargon overuse |
| leverage (as a verb) | Use "use" instead |
| robust | Generic positive filler |
| comprehensive | Generic positive filler |
| seamlessly | Pure AI signal |
| harness | "Use" works fine |
| navigate (the landscape) | LLM staple |
| journey | Hallmark Channel energy |
| tapestry | Instant AI flag |
| testament | Overused in praise |
| vibrant | Overused descriptor |
| underscore | Academic-AI tic |
| showcasing | Resume-AI tic |
| in today's fast-paced world | Death sentence |
| in the realm of | Death sentence |
| it's worth noting that | Filler |
| that being said | Filler |
| I hope this email finds you well | The #1 cliché |
| I am writing to express | Stiff and AI-default |
| excited to share | Hyperbolic |
| looking forward to hearing from you | Default sign-off |

### The em-dash plague

LLMs sprinkle em-dashes everywhere — like this — and humans rarely do in casual email. Use parentheses, commas, or just two sentences.

**Rule:** One em-dash per email is the max. Zero is better.

### Three-part lists everywhere

"Concise, specific, and value-driven." "Built, deployed, and scaled." AI loves balanced triplets. Real humans write asymmetrically.

Mix: one-item callouts, two-item pairs, and occasional lists.

### The "it's not X, it's Y" tic

A common LLM pattern is parallelisms like "It's not X, it's Y" or "no X, no Y, just Z." Strip these.

### Curly quotes and curly apostrophes

ChatGPT outputs "smart quotes" and curly apostrophes by default. Most email clients also do this, so it's not a fatal tell — but if you're pasting from an LLM and your other emails use straight quotes, the inconsistency is the giveaway.

### Suspicious symmetry

Every paragraph the same length. Every email starts with greeting → context → ask → close. **Vary it.** Sometimes lead with the question. Sometimes skip the pleasantry.

### Over-polish

No contractions, no fragments, no minor weirdness. Real emails have "I'm" and "don't" and sentences. Like this one. AI rounds off all the edges.

### Bullet-list reflex

LLMs default to bullets for anything with 3+ items. Real emails almost never use them. If your email has bullets, you've probably AI'd it.

### Hyperbolic positivity

"I'd love to," "I'm super excited about," "absolutely thrilled," "this is exactly the kind of work I'm passionate about." Tone it down.

### Generic openings

"I hope this email finds you well." "I trust this finds you well." Anyone who reads cold email knows these are AI defaults. Skip the pleasantry entirely or replace with something concrete: "Saw [specific thing] this morning..."

### Placeholder leftovers — the cardinal sin

When users copy-paste an AI-generated email in a rush, they leave behind unedited placeholders like `{company name}`. Always proofread for `[brackets]`, `{braces}`, "[Company Name]", and "[insert here]".

---

## Techniques to actually sound human at scale

### Write one email from scratch first, then adapt
Don't ask an LLM to generate 20 emails. Write your best version manually for the most important target, then use the LLM only to help you adapt the structure for the next 10 — and always rewrite at least 40% of the body each time.

### Use your real speech patterns
Read your draft out loud. If you wouldn't say it in person, don't put it in the email. You probably don't say "leverage" or "robust" out loud. Use "use" and "solid" instead.

### Break grammar lightly, on purpose
Start a sentence with "And" or "But." Use a sentence fragment for emphasis. Drop a "honestly," in the middle. These cost nothing and instantly sound human.

### Use specific numbers and proper nouns
"Migrated from FAISS to Milvus" is impossible to fake without context. "Improved retrieval performance significantly" is exactly what an AI would write. Force yourself to include 2-3 concrete details (numbers, library names, specific products) in every email — they double as proof of work *and* anti-AI signal.

### Vary openings across your campaign
If you send 20 emails, none should start the same way. Mix:

- "Saw your [thing] on [platform]..."
- "Quick one — [direct question]..."
- "[Mutual connection] mentioned I should reach out..."
- "Came across [Company]'s work on [thing] while [context]..."
- "[Specific observation about their product]..."
- "Going through [Company]'s [thing] this week and..."
- "Was reading about [topic] and remembered [Company] shipped..."

### Vary sentence length aggressively
AI defaults to 15-25 word sentences, consistently. Mix in 3-word sentences. And 35-word run-ons that twist a bit before ending. The variance is what reads as human.

### Keep imperfection
A lowercase "i" in a signature, a contraction in a formal context, one extra space somewhere — minor noise reads as human. Don't manufacture typos, but don't sand them all off either.

### Skip the closing flourish
"Looking forward to your response!" / "Would love to hear your thoughts!" — both AI defaults. End with just your name, or a single dry line: "No rush" or "If not a fit, totally fine."

---

## The 5-step pre-send checklist

Before every email, scan for:

1. **AI-vocabulary scan** — any word from the list above. Cut or replace.
2. **Em-dash count** — limit to one, ideally zero.
3. **Bullet points** — remove unless absolutely necessary.
4. **Generic openings** — replace with something specific to that recipient.
5. **Bracket sweep** — search for `[`, `{`, and "Company Name." Fix any survivors.

If the email still reads slightly imperfect after that — slightly informal, slightly uneven, slightly *yours* — you're doing it right.

---

## Personalization variables to fill in per email

For each target, gather:

- First name (verify spelling)
- Company name (and how they style it — "OpenAI" not "Open AI")
- One specific thing they shipped/wrote in the last 60 days
- The specific team or product line you'd join
- One technical detail of yours that maps to their work
- Mutual connection (if any) — name and how you know them

Time investment: 10-15 minutes of research per email. Anything less and the personalization isn't real.

---

## Tools worth using

- **Hunter.io** — find verified email addresses
- **Apollo.io** — contact database with org charts
- **Clearbit** — company enrichment
- **Mailtracker / Streak** — light tracking (but watch out: tracking pixels reduce reply rates by 10-15%, so use sparingly or skip)
- **Custom domain email** — set up `you@yourdomain.dev` with SPF/DKIM. ~3x reply rate vs `@gmail.com`.

---

## Mistakes that look human but aren't

A few things to *not* do, even though they might seem like "humanizing":

- Adding deliberate typos — readers notice
- Using slang you don't actually use ("hey what's good")
- Over-casual when contacting executives ("yo, quick question")
- Manufactured vulnerability ("I'm just a kid from Ahmedabad trying to break in")

The goal is *natural*, not *folksy*. Write like the smartest, calmest version of yourself.