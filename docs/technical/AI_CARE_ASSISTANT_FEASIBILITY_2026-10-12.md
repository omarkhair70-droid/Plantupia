# Plantupia — AI Care Assistant Feasibility (2026-10-12)

**Status:** RESEARCH / PROPOSED technical contract; **NOT IMPLEMENTED IN NOVA PR #240**; no API account or operating budget has been approved.  
**Confirmed operational boundary (2026-10-12):** Plantupia has **no sensors in its plants**. The assistant may interpret user-supplied observations but must never imply live readings or sensor-integrated functionality. Sensor/IoT integration is outside the active product scope.

**Product anchor:** context before advice; observed history before AI; uncertainty and evidence before certainty; automate burden, not the human relationship.  
**Linked docs:** `../product/MASTER_CAPABILITY_ATLAS_V0_2026-10-12.md` and `../product/SCREEN_FLOW_ATLAS_V0_2026-10-12.md`.

## 1. Decision: YES, a useful chatbot is feasible today

No custom training, GPU, local LLM model or company-written encyclopedia is needed to launch a **general, read-only, opt-in plant-care assistant**. Build a native Compose conversation UI and **Django backend endpoint** that calls one supported hosted multimodal/text model. The existing Nova-derived authentication, image upload/storage, and authenticated Plantupia domain can be *reused* only after security/contract checks.

The assistant must have **three separate knowledge scopes**:

1. **General botanical guidance:** sourced educational material from RHS/university extension/approved plant-care guide datasets; clearly attributed and with caveats, not indiscriminate scraped copyrighted text.
2. **User's plant context:** with authenticated authorization and user consent, retrieve that plant's name/species certainty, placement, notes, photo evidence and **recent events** from Plantupia's own database. The assistant is more valuable when it can compare a user's observed change over time; it should distinguish actual reported facts from tentative interpretations.
3. **Plantupia company-specific answers:** **locked until authorized input** such as approved service catalogue, installation instructions, warranty/contact policy, operating regions, SLA, actual visit history. If absent, explicitly say the assistant does not have company-confirmed details; route to actual company support.

Do not pretend 1 or 2 proves 3. Do not index internal offer letters, private chats, customer addresses or non-public corporate documents in public repositories or third-party stores without approval.

## 2. MVP interaction in the Android app

```
Plant profile (real plant ID)
    ↓ tap “Ask about this plant”
Assistant opens with plant name + visible context summary (user can exclude it)
    ↓
User: “ورقها اصفر، أعمل إيه؟”
    ↓
Django checks access / rate limit / user consent
    ↓
Retrieve a short, **authorized** plant context and approved guidance excerpts
    ↓
Model asks targeted questions (e.g. soil moisture, light, timing, drainage)
    ↓
Answer: likely possibilities, checks that do not cause harm, limitations, sources
    ↓
Optional: “Record observation” or “Check back in 7 days”
    ↓
***user taps explicit confirmation*** before saving anything
```

Separate general entry: “Ask about plants” with no personal-data retrieval or selected plant. Chat history may be ephemeral in the first demo, provided the UI doesn't pretend it persists. A public Circle question is never a side effect of private AI chat.

## 3. Provider options and independently published pricing

Pricing checked against official provider docs on 2026-10-12; prices, limits and region/availability can change. The free tier is for evaluation, **not** a promise of free production use.

| Candidate | Representative paid text price, per 1M input / output tokens (USD) | Usage idea | Tradeoffs |
|---|---|---|---|
| Google Gemini 2.5 Flash-Lite | $0.10 / $0.40 | cheap first experiments and high-volume everyday dialogue | evaluate Arabic, care advice, source adherence |
| Google Gemini 2.5 Flash | $0.30 / $2.50 | better response tier if tested | more expensive responses |
| OpenAI GPT-5.4 Mini | $0.75 / $4.50 | quality-oriented alternative, image input / tool workflows | higher token cost; source and safety eval still required |
| OpenAI GPT-5.4 nano | $0.20 / $1.25 | price reference **only**: docs presently flag it deprecated | **do not choose deprecated model as default for new integration** |

**Illustrative token-only spend** for 10,000 single turns with ~2,000 input + ~500 output tokens each (20M input and 5M output tokens), using standard rates, no caching: Gemini Flash-Lite ~**$4**, Gemini Flash ~**$18.50**, GPT-5.4 Mini ~**$37.50**. This is **not total operating cost**: excludes image tokens, larger follow-up context, thinking overhead where billed, retrieval/tool calls, storage, cloud, observability, image-ID providers, currency/tax, and support/moderation.

**Official pricing:**
- https://ai.google.dev/gemini-api/docs/pricing
- https://developers.openai.com/api/docs/models/gpt-5.4-mini
- https://developers.openai.com/api/docs/models/gpt-5.4-nano
- https://developers.openai.com/api/docs/guides/tools-file-search
- https://ai.google.dev/gemini-api/docs/file-search

## 4. Smallest secure architecture

```
Compose native Chat surface
  ↓ authenticated POST /api/v1/plantupia/assistant/ask/
Django API (source of truth)
  ├─ authenticate, permissions, user rate and budget caps
  ├─ optional selected plant context from approved user/space only
  ├─ optional retrieved botanical guide excerpts with IDs/version
  ├─ provider adapter (Gemini/OpenAI behind one service boundary)
  ├─ safe-response contract / scope labels / refusal or uncertainty
  └─ response text + suggested user-reviewed follow-up + citations
      ↓
Compose renders source labels, uncertainty, questions, optional next step
```

**NEVER ship provider credentials inside Android APK or JS client.** Put secrets only in appropriate server-side secret management. Avoid cross-account leakage by querying Plantupia's accessible plants using the current auth principal, not an arbitrary client-provided UUID. Build short context windows to control cost; avoid dumping long unfiltered histories. Default to limited storage/retention and make deletion possible.

Recommend a minimal stable server contract:
- request: `message`, optional `plant_id`, optional `image_reference`, optional conversation cursor (after a session policy exists), explicit `include_my_plant_context`;
- response: `answer`, `scope` (`general` / `plant_context` / `company_verified`), `source_links`, `uncertainty`, `follow_up_questions`, optional `suggested_actions` requiring user confirmation;
- error: provider unavailable/rate-limit/data inaccessible/unsafe source; recoverable UI without fictitious saved results.

Start with a single provider; an adapter permits switching after quality and budget eval. **Avoid adding a vector DB or agent framework before any verified document volume requires one.** For a small reviewed guide set, server-side excerpt lookup is enough; for larger approved knowledge, hosted file search/RAG can index guides and return source links. Hosted retrieval still requires permission controls, licensing checks and evaluation.

## 5. Botanical knowledge and photo ID are different problems

- **Care advice:** use reviewed licensed/publicly usable source entries; RHS and university-extension are good fact-check references. Rights to store/index full text are not implied by public availability. https://www.rhs.org.uk/plants/types/houseplants/growing-guide
- **Plant identification:** optional later Pl@ntNet API suggests ranked species with confidence; user chooses. It is not a definitive label or a disease diagnosis. Free tier up to 500 requests/day subject to API terms; commercial terms/attribution must be verified. https://my.plantnet.org/doc/api/identify and https://my.plantnet.org/terms_of_use
- **Species/care metadata:** Perenual exposes species/care endpoints; public free tier has limits and their listed commercial plan is separate. Check accuracy/licensing before using guide content or images. https://www.perenual.com/docs/api and https://www.perenual.com/subscription-api-pricing
- **Photo-based symptom discussion:** model vision can see visible patterns but is not a verified disease laboratory. Prefer cautious differential possibilities plus environmental questions, not an exact pathogen diagnosis. https://developers.openai.com/api/docs/guides/images-vision
- **Smart data:** do not output soil sensor measurements unless a real sensor event was received and timestamped; human observation must never be labeled as measurement.

## 6. Product constraints and safe recommendations

- State “unknown” when species/placement/history or company policy is missing.
- Distinguish user reports vs measurements vs AI guesses in UI and API.
- Ask if pot drains, soil is wet/dry, light has changed, recent watering and HVAC drafts before confident causal claims.
- Do not use a fixed-date watering reminder as biological truth.
- Avoid risky pesticide, ingestion/toxicity, pet/child exposure, or medical claims without verified sources and appropriate safety guidance.
- Give escalation path for severe plant damage and company service questions.
- A chatbot should *teach the user to observe* and record outcomes, not pretend the plant has spoken.
- Protect private location notes, office/client names and images from public Circle prompts and unrelated users.
- Device QA must test Arabic dialect spelling, mixed English species names, no internet, rate limits, empty plant, wrong user UUID, malformed image, consent revocation, hallucinated company policies and long conversations.
- Record costs and quality, not just CI green.

## 7. Staged delivery and gates

**AI-0 — text-only read-only demo:** Compose chat screen, Django authenticated endpoint, one provider, clear limitations, general cited guidance, hard request/cost limit. Can be prototyped quickly if a funded/available API account and backend access exist; *not* a guarantee of a finished production assistant in a day.

**AI-1 — plant-specific:** authorized user's selected plant record + note/history context + verified scope provenance; regression tests for cross-account leaks, and plant-less fallback.

**AI-2 — specialized content/vision:** approved guide corpus/retrieval, photo observation assistance, confidence labels, appropriate licensed plant identification provider, real mobile QA.

**AI-3 — verified Plantupia help and actions:** company-reviewed FAQ/policies/services, support routing, optional create-a-care-note *only after user confirmation*. Requires explicit company review/permissions and real service flow.

Do not wait for AI-3 to run AI-0, but do not publicly promise company-specific AI support with only AI-0.

## 8. Why this is NOT a simple copy of competitor features

Planta, Greg, PictureThis and PlantIn already cover broad advice/reminders/image-ID; FYTA has *actual device telemetry*. Competing with a generic “AI Plant Doctor” by visual imitation or hallucinated diagnosis has weak differentiation. Plantupia's more defensible candidate is:

> The same living plant in its actual space, seen across time — and an assistant that knows *what was really observed and done*, asks better questions, then returns knowledge to the real human care loop.

This aligns with the Plantupia source research but remains a hypothesis awaiting user and company validation.

## 9. Public evidence

- Existing thesis: `docs/synthesis/02-product-translation.md` and `docs/exploration/05-cross-world-critique.md`
- RHS houseplants: https://www.rhs.org.uk/plants/types/houseplants/growing-guide
- RHS poorly houseplant: https://www.rhs.org.uk/plants/types/houseplants/how-to-help-a-poorly-houseplant
- OpenAI Responses: https://developers.openai.com/api/reference/responses/overview
- Google Gemini Structured Outputs: https://ai.google.dev/gemini-api/docs/structured-output
- Google Gemini tools: https://ai.google.dev/gemini-api/docs/tools
- Google Gemini API key security: https://ai.google.dev/gemini-api/docs/api-key

**NO custom company dataset, training pipeline, payment, integration, third-party API account or Android chatbot has been created by writing this feasibility study.**
