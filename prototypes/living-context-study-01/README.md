# Plantupia — Living Context / Interactive Design Study 01

**Status:** DESIGN PROOF / J1 + J2 FUNCTIONAL / NOT APPROVED OR CONNECTED TO PRODUCTION  
**Date:** 2026-10-12  
**Source:** [Product spec](../../docs/product/MASTER_PRODUCT_SPEC_V01_2026-10-12.md) → [Information architecture](../../docs/product/INFORMATION_ARCHITECTURE_V01_2026-10-12.md)  
**Entry:** [`index.html`](./index.html) — open as a static file in a desktop or Android browser; no build step.

## What this proves

An **interactive, original, Arabic-first mobile web prototype** of the proposed Android user experience. It is a *disposable interaction and visual study*, not a second production frontend and not a replacement for Compose or Flutter.

- **J1, complete demonstration:** blank onboarding → create private space → add plant with optional personal photo (small images only) → actual care act / observation → opt-in follow-up after 7 or 14 days → preview-time jump of seven days → user-authored outcome → living history. Real user inputs survive navigation and, in an ordinary supported browser, reloads via `localStorage`.
- **J2, bounded design simulation:** open contextual “Ask about this plant” → see optional plant scope → ask a question → receive **hardcoded example replies labeled DEMO** that ask about light, soil and drainage instead of pretending a biological diagnosis. General questions can opt out of the plant scope.
- **Privacy interaction sample:** private plant notes and a separate public question draft, followed by an exact preview. **Publishing is disabled**. The Circle does not show fictional users, experts or activity.
- **Navigation test:** proposed 4-intent N1 composition: Spaces / Care / Circle / Me, with contextual Assistant entry. N2 (Spaces / Assistant / Circle / Me) is still an unbuilt alternative requiring comparison.

There is **no real user account, Django write, AI model/API, expert, image recognition, weather, sensor, IoT device, Plantupia customer data or professional maintenance workflow** in the prototype. Plantupia currently **has no sensors in plants**; no telemetry is part of this experience.

## Design thesis — provisional

**LIFE, IN PLACE.** A plant should be legible as a living resident of a real space, with a personal name and temporal continuity. Editorial negative space, restrained natural hues, authentic user photo when provided, and a causal timeline replace generic wellness scores, smart gadgets and random eco decoration.

**Material hierarchy:** PLACE → LIVING IDENTITY → ACTUAL ACTION / OBSERVATION → REVISIT → OBSERVED CHANGE → SHARED LEARNING BY CHOICE.

**Assets:** all plant motifs are clearly labeled authored SVG *illustrations/placeholder*, not photos of real Plantupia installations. No downloaded reference imagery or Plantupia brand fonts/logos were copied. The textual “plantupia” mark is provisional.

**Visual status:** first authored study, NOT approved brand production or final art direction. Large/small screens and real approved photographic sources need another deliberate pass.

## How to test manually

1. Open `index.html` in a browser or a local static server. Start empty; create “بيتي”, then add “ليلى” (species optional) and a room/placement.
2. Open the plant → record actual watering, soil check etc. Add a personal observation and choose **7 days**. Leave, reopen, use the Care tab. Inspect the pending follow-up.
3. Use **“تقدم 7 أيام في النموذج”** to jump the *demo clock*, open the same plant's pending follow-up, record an observed outcome, inspect chronological history.
4. Open the plant assistant; ask about yellow leaves or watering. Inspect visible **DEMO** scope/simulation notice. Toggle context off. Verify it never claims a sensor reading or confirmed diagnosis.
5. From Circle, create a general question and inspect exact public payload. There is no Publish control.
6. Open My → reset demo data. Refresh the browser. If local storage is permitted, the app should return to the empty state.

For quick automated smoke tests, run `python qa_playwright.py` from this folder (requires Python Playwright and local Chromium).

## Known interaction/UX deltas (explicit, not hidden)

| Area | Status | Why it is not closed |
|---|---|---|
| J1 basic create → care → follow-up → outcome | Tested in Chromium | The in-memory/browser persistence is not Django API or real storage proof |
| J2 chatbot surface | Clickable scripted simulation | No authenticated AI call, provider, privacy retention, costs, RAG/source verification |
| Public Circle sharing preview | Clickable, safe non-publishing | No real Post API, moderation or media redaction proof |
| Brand photography and logo | SVG placeholder, text mark | Authorized Plantupia original materials not yet embedded |
| Visual comparison N1 vs N2 | Only N1 rendered | Compare contextual vs primary AI entry with task success and navigation cost |
| Care timeline timing | Simulated integer day | Calendar/dayzone/realtime notifications not present |
| Error states | Discussed in spec | Offline, expired auth, photo upload and permission failure need separate state mockups |
| Actual installation / staff workflows | NOT present | Need verified Plantupia company operation, role and entitlement |
| Production client | NONE | Android Compose branch remains separate and untouched |

## Decision this study helps answer

**Can a person with 1–7 household plants accomplish the entire care-and-learning loop without a feed-first experience, fabricated sensor data or a mandatory company purchase?** Then: is the Assistant more useful in plant context (N1) or as a main destination (N2)?

The next review should critique every surface against **actual Plantupia's life/spatial/company thesis**, not against the attractive appearance of this prototype. Reject, combine or redesign screens as needed **before** shipping anything to Android.

## Repo safety

This file lives on the active **Plantupia research branch**, not Nova `master` and not PR #240. It makes no deployment, Play release or private-company-data changes. All actual production integration requires its own agreed phase and tests.
