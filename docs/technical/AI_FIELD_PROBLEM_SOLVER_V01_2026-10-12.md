# Plantupia AI — Field Problem Solver / Product + Technical Brief v0.1

**Date:** 2026-10-12
**Status:** **RESEARCH / PROPOSED. NOT SHIPPED. NO NEW CODE CHANGED BY THIS BRIEF.**
**Core user example:** Plantupia founder says a real customer had a problem he could not resolve at first, so he took it to Claude and received practical help. This is the *intent*, not an invented transcript of the incident. No exact client/plant, diagnosis or final outcome is provided yet.

## The real job

**NOT:** "A watering-reminder chatbot" or "a green ChatGPT reskin."

**YES:** a **multimodal, grounded and conversational problem-solving partner** available both to (1) everyday owners with one of their actual plants and (2) authorized staff handling a real Plantupia installed client site. The assistant helps investigate, asks good diagnostic questions, consults sources, explains plausible causes and low-risk next checks, proposes an intervention for human review, and remembers the actual outcome in a private plant/issue timeline after a user confirms it.

"Like Claude/ChatGPT" refers to **interaction/capabilities**, not cloning the proprietary app, model or interface. Either an OpenAI API or Anthropic Claude API can be an implementation engine; keep a provider adapter, evaluate actual case quality, do not train an LLM or build a general foundation model from scratch.

**Company reality:** Plantupia has **no sensors in its plants**. AI cannot claim soil moisture readings, live temperature telemetry, sensor calibrations or measurements from unseen hardware.

## Current code reality — audited on Nova experiment branch 1844651

Native Kotlin/Compose:
- `PlantupiaAssistantScreen.kt`: a real chat surface. The user can opt into sharing the *selected plant* context; messages and responses appear on screen in a local, ephemeral list.
- `PlantupiaRepository.kt`: `askAssistant()` POST to `plantupia/assistant/ask/`.
- The screen **does not** include image upload, documents, source/link UI, follow-up report, saved conversation, staff role or company-site management.
- **Critical:** the API request includes only the newest question, plant ID and consent flag. Prior turns are drawn in UI but are **NOT** transmitted to the model, so this is *not a context-aware multi-turn conversation*, even though it visually resembles one.

Django:
- `backend/plants/assistant.py`: authenticated model gateway at `/api/v1/plantupia/assistant/ask/`, OpenAI Responses API `gpt-5.4-mini` default, optional name/species/placement + latest five human notes, short output, explicit privacy permissions, no autonomous DB write, `store:false`, two per-user throttles.
- No public-web search tool, retrieval/source corpus, explicit source citations, vision, model followup state, configurable company instructions or integration with external service tickets.
- No confirmed active production or QA `PLANTUPIA_AI_API_KEY`. Without configured server secret endpoint returns 503. GitHub CI on isolated branch passed Django tests (mock provider) + Android build; **no real provider or client-site E2E evidence**.

**User-visible status label:** *AI infrastructure built, live field problem solver NOT YET implemented/activated.*

## The key scenario — client incident

**Input, not fictional diagnosis:** "A client reports leaves have begun yellowing in a planted office space. They send photos. Staff cannot tell the reason." This is merely a **testing hypothetical**, not the founder's exact event.

Desired conversation:
1. User opens **Ask AI** from the plant or permitted company site / from general assistant.
2. Uploads **whole plant photo + close symptom photo + optional pot/root/room context photo**, asks in natural Egyptian Arabic/English, optionally voice dictated through OS.
3. Assistant retrieves **only authorized** species confidence, actual location/conditions *as human written*, event history, previous interventions/observed outcomes, and (once provided) verified site care guidelines and maintenance responsibility.
4. AI asks targeted questions **before a strong claim**: When did it start? New/old leaves? Extent? Soil feels wet or dry? Does pot drain? Recent watering/change in light/AC/heat? Other plants nearby affected? Any pests/spots?
5. If uncertain, ask for **additional specific photos or observations**; do not infer root condition from a leaf image.
6. Assistant retrieves reviewed public horticultural references and approved Plantupia care documents. Prefer sources relevant to plant and place; attach a live source URL/title to each important recommendation. Source absence must be acknowledged.
7. Response structured:
   - **What's observed** (from image or actual user report; attribute source)
   - **Possible explanations** (not false exact diagnosis)
   - **What to check next** and why
   - **Low-risk immediate step(s)**, reversibility, avoid speculative pesticide or damaging intervention
   - **When to ask real staff/expert/diagnostic lab** and why
   - **Sources** (proper article link, not imagined citations)
   - **What to document** and user-proposed revisit/check-in.
8. Human reviews and **explicitly chooses** save a concern, intervention, photo or follow-up to the private actual plant history; AI doesn't silently mutate or notify a client.
9. On revisit the assistant compares **user-provided before/after photos and observed outcome**, may revise its previous hypothesis, and stores resolution only after consent.

**No promise of professional plant disease diagnosis** from one photo. Consult actual plant clinic/extension/expert for situations requiring testing.

## AI capability architecture

```
Jetpack Compose Assistant
├─ Text / multimodal composer (+ real photo-picker with visible permissions)
├─ Real conversation UI with follow-up state
├─ Plant/site context consent and editable context summary
├─ Source drawer: verified URLs/docs, uncertainty labels
├─ Action chips: ask follow-up, attach evidence, save report, request human help
└─ Native error/offline/cancel/too-large-image / sensitive-data states
        |
authenticated Django /api/v1/plantupia/assistant/
        |
┌───────┴───────────────────┐
| Authorization & user scope | (must NEVER trust arbitrary plant IDs)
| Rate budgets, limits, logs   | (private, short retention, delete policy)
| Conversation state/history  | (resend/managed, opt-in persisted where allowed)
| Evidence/media service      | (actual uploaded files; strip EXIF, presigned/safe access)
| Plant / zone / site context  | (human-entered, timestamps, proven identities)
| Knowledge retrieval         | (reviewed, licensed/up-to-date horticultural + approved company)
| Provider adapter            | (OpenAI Responses or Claude Messages; multimodal/tool support)
| Tools: read-only fetch plant | (use server authorization per request)
| Tools: web search            | (source URLs + dates; vet reputation)
| Confirmed save actions       | (ONLY separate user-authorized mutations)
└─────────────────────────────┘
```

### Distinct knowledge classes

1. **Model general knowledge** = useful hypotheses, not authoritative current site/plant diagnosis.
2. **Reviewed horticultural reference** = real RHS, university extension/plant clinic/UC IPM guides; store URL, title, retrieved date, source snippet and content license. The presence of a public web page **doesn't automatically authorize copying its full text into a paid corpus**.
3. **Owner's living history** = only authorized human-uploaded facts, photos, work done and outcomes.
4. **Company operating instructions** = approved installations, actual maintenance procedure, client entitlements, staff contacts and support workflow. **UNAVAILABLE until company sends or confirms docs.** Keep private and role scoped. An AI cannot invent who installed, which visits occurred or what warranty applies.

### Practical tool set

- `get_plant_context(plant_id)`: authorized, minimum necessary context, record source/time.
- `get_recent_care(plant_id)`: signed human care and observations, scoped.
- `search_verified_plant_guides(query, species, symptoms)`: retrieval with source citations and notes.
- `web_search_trusted_sources(query)`: only when fresh reference is necessary; show links + date.
- `get_client_site_protocol(site_id)`: GATED on approved documents and staff/site roles.
- `draft_plant_issue_report()`: structured draft only; returned to Compose, not auto-persisted.
- `save_confirmed_issue_report()`: explicit reviewed user confirmation and server authorization, later phase.
- `ask_human_support()`: ONLY after the company validates a real staffed channel or reporting workflow.

**Important**: The tool loop always runs on the backend; the AI only asks and server validates. Uploaded photos/care notes are untrusted content, never permission or system instructions.

## Phased implementation, no premature promises

### FIELD-0 — First genuinely working assistant
- One provider behind the existing Django endpoint; secure API key in an **isolated** environment; server-side usage cap and useful error messages.
- Fix multi-turn: carry previous user/assistant turns with bounded size/structured state and protect retention. User can ask "طب لو التربة ناشفة؟" and model knows which question it follows.
- Native gallery/camera selection, image moderation/limits, safe upload and **real vision processing** (not just attach image icon).
- General vs plant-context mode, consented actual plant details and staff/private client scope.
- Produce concise differential answer/checklist with follow-up questions.
- **Do not claim source grounding until retrieval/citations exist.** This is a functional vision/chat milestone, not complete field solver.

### FIELD-1 — Grounded client troubleshooting
- Curated source catalogue: RHS, PSU Extension, UC IPM/diagnostic guides and species/region sources as applicable. Validate usage rights before persisting materials.
- Tool/search retrieval with real citations. Include source names and direct links, no invented URLs.
- Human-checked issue record/observations/measurements (no nonexistent sensors), review after care.
- Field staff/client roles, actual site/unit context from confirmed company data, privacy controls.
- Multi-photo chronological comparisons where images are reliable enough; explain limits.
- UX shows likely causes, next evidence, proposed intervention and staff escalation.
- Separate company/staff capabilities from consumer-accessible Chat. Avoid exposing other client sites.

### FIELD-2 — Mature assistant
- Read-only "ask from site" summary across legitimate installation history, real service reports, reviewed maintenance protocols.
- Approved notes/photographs as case-based retrieval with strict tenant boundaries, de-identification for shared examples.
- Human confirmation for write actions; outcome-based feedback and evidence quality scoring.
- Provider routing by complexity (fast low-cost chat, stronger diagnostic/evidence cases); budget alerts.
- Optional voice dictation and domain-specific training of **evaluations**. Fine-tuning is not a requirement.

## Distinguish chat / content / access

- **AI Assistant** = model conversation + image input + retrieval/context.
- **Nova Inbox** = real person-to-person DM, NOT the AI and NOT automatically a company support ticket.
- **Circle / Story** = explicitly public or audience-limited expression, NEVER an implicit export of private customer photos/history.
- **Plant history** = persistent owner-verified record, unlike 24h Story or temporary AI chat.
- **Company support** = only activated when Plantupia confirms real staff, processes and authorized information.

## Source/reference pass (checked 2026-10-12)

### Platform implementation (official)
- OpenAI GPT-5.4 Mini: https://developers.openai.com/api/docs/models/gpt-5.4-mini — existing code default; image input and native tool/function calling are supported by model, but currently unused in Plantupia.
- OpenAI vision: https://developers.openai.com/api/docs/guides/images-vision — input photos, vision limitations.
- OpenAI Responses tools: https://developers.openai.com/api/docs/guides/tools — function calling, web/file search.
- OpenAI web search: https://developers.openai.com/api/docs/guides/tools-web-search
- OpenAI file search: https://developers.openai.com/api/docs/guides/tools-file-search — hosted vector store option, not required initially.
- Anthropic vision: https://platform.claude.com/docs/en/build-with-claude/vision
- Anthropic tool-use contract: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works — provider-neutral architecture.
- Anthropic web search: https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- Anthropic files: https://platform.claude.com/docs/en/build-with-claude/files

### Botanical reference and diagnostic procedure (professionally useful)
- RHS diagnosing houseplant conditions: https://www.rhs.org.uk/plants/types/houseplants/how-to-help-a-poorly-houseplant
- RHS leaf damage can have multiple causes: https://www.rhs.org.uk/prevention-protection/leaf-damage-on-houseplants
- Penn State Extension plant diagnosis 101: https://extension.psu.edu/diagnosing-a-plant-problem-101
- UC IPM: symptom/site/care/environment diagnostic questions: https://ucanr.edu/node/137278/printable/print

**Not sufficient source:** an unreviewed app listing claiming "AI doctor" or an AI-generated diagnosis with no date, provenance or input evidence.

## Pilot evaluation: must test before founder demo signoff

Ask founder for **one anonymized real client incident** (what happened, any images, species and place, intervention actually tried, outcome). Use this case as the first ground truth but don't infer the real facts from the anecdote.

Build 15–20 varied cases:
- yellowing caused by dry vs very wet soil, both ambiguous photos;
- nearby AC draft; direct light scorch; low light with weak growth;
- pests visible on close-up; incomplete blurry images; unknown plant species;
- multiple plants in one office affected after environmental change;
- wrong-account client data attempt; staff unauthorized site; user opts out of context;
- unsupported pesticides/dangerous intervention requests; two-round clarification;
- assistant asked to cite something when no sources found; broken resource links;
- official warranty/company question with no approved instructions;
- API key absent, quota exceeded, provider outage; no false "success".
Score: right *next diagnostic question*, source quality, risky overconfidence rate, task completion, latency/cost, data access leaks, usefulness to actual field technician/founder. A convincing answer on one demo plant is not enough.

## Open questions for company, not invented decisions

- The founder's **actual** incident: what symptom, installation, photos/notes, time, what Claude suggested, what human did and what worked?
- Should first AI be mainly a professional staff tool, household owner helper, or both with clear permissions?
- Which handover documents, service manuals, supplier plant lists and maintenance reports can be used legally/privately?
- Which Plantupia employee reviews advice, and what is the escalation contact/workflow for unresolved cases?
- Which production billing/key and maximum budget are approved? Keep API secrets in backend, not GitHub/Android.

## Acceptance line

**Founder's intended result:** "أدخل مشكلة حقيقية عند عميل، أصورها وأشرحها، المساعد يفهم سياقها ويسألني اللي ناقص ويبحث في مصادر حقيقية، وبعدها أطلع بخطوات عملية مع حدود واضحـة وأقدر أراجع النتيجة بعد التنفيذ."

**Current branch:** has only **text AI plumbing, simple opt-in record retrieval, and ephemeral UI**. This brief does not change that fact.

**No deployment/production DB/Play changes were made by authoring this brief.**
