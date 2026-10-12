# Plantupia × Nova — Integrated Visual/Interaction Pass 02

**Status:** DESIGN STUDY / INTERACTIVE BROWSER PROTOTYPE / NOT APPROVED / NO PRODUCTION CHANGES  
**Date:** 2026-10-12  
**Prototype:** [open index.html](./index.html)  
**Parents:** [Master Product Specification](../../docs/product/MASTER_PRODUCT_SPEC_V01_2026-10-12.md) · [Screen Contracts](../../docs/product/INFORMATION_ARCHITECTURE_V01_2026-10-12.md) · [Nova Integration Contract](../../docs/product/NOVA_INTEGRATION_VISUAL_CONTRACT_V01_2026-10-12.md)

## Why this pass exists

The first Plantupia HTML study verified the **private plant care loop** but was too text-led, insufficiently visual, and didn't show how the existing Nova engine for **Stories, Inbox, Posts, Create, Circle, profiles and rich media** fits together. The user's feedback was explicit: Nova was chosen as an advanced fertile native product foundation, **not just a ready backend**. This pass corrects the missing product-system view.

**Target:** one visual grammar and navigable mock experience, not five unconnected wireframes. No code is modified in Nova; no Compose / Play / Oracle production deployment has occurred.

## Working UX proposition

**Life, in place.** Design signals should express: real place → personally identified plant → actual action/observation → retained timeline → optional public story/knowledge → person-to-person conversation; the contextual AI assistant is its own explicitly delimited knowledge lane.

The study keeps Nova PR #240's **four existing primary intents** as a visual test baseline:
1. **مساحتي** (Living Home) → Plant → Care → History / AI.
2. **الدائرة** (Circle) → plant knowledge, sample Stories, people, real Inbox entry.
3. **+ إنشاء** (Create) → *private care*, *public question*, *new plant*, *24-hour Story*, optional media.
4. **أنا** (Profile) → private-space shortcut, personal identity, Inbox, settings/notification destinations.

**Inbox** remains directly reachable from the top bar, Circle and Profile. **Stories** are public/temporary and separated from the private/permanent **Living History**. **AI** is a plant-contextual helper and not the Inbox. Direct `Story → PlantUnit` linking is **not implemented by Nova PR #240**.

## Interactive scenarios

| ID | Click-through | Actual prototype interaction | What is simulation |
|---|---|---|---|
| V-01 | Home → Plant | switch to a selected personal plant; view illustrated hero and identity | sample plants, photos are botanical **illustrations** (not real owner/company images) |
| V-02 | Plant → Record Care | choose icon action, write note, save to local event history | no Django API, no notification |
| V-03 | Create → New Plant | create a name/species/placement and view its profile | browser-local data only |
| V-04 | Circle → Story | view sample Stories and use next/previous; enter reply path | fictional examples only; no post/Story server |
| V-05 | Circle/Profile → Inbox → chat | open demo conversation, type/send locally | nothing goes to another person or Nova message service |
| V-06 | Plant → AI | ask and receive a **prewritten scripted** clarifying answer; toggle plant context | not a real AI model, not a diagnosis; no sensors |
| V-07 | Create → Public Question → Preview | write public data and inspect exactly what would be visible | posting is deliberately disabled |
| V-08 | Notifications | view sample due/DM/Circle notifications and open contextual destination | no actual push / unread / generated reminders |

The sample records and people are **demonstration data**. Users can reset state in the Profile demo. Their self-entered records are stored in browser localStorage where permitted and do not leave the device.

## Technical scope and safety

Single **standalone HTML** file with self-contained CSS, JavaScript, native browser SVG plant illustrations and Lucide-style inline vector symbols. No frameworks, external model calls, live photo feeds, SDK keys or network permissions needed; local browser interaction only.

Plantupia **has no plant sensors**. The interface never fabricates measurements or hardware screens. AI answers are labeled DEMO and avoid pretending to diagnose. Company visits, active support and real installations have not been invented. User-owned plant observation remains private; Story and public posts are explicit separate actions.

## Visual / UX audit (not a final signoff)

**Improvements over Study 01**
- richer plant imagery cards/illustrated hierarchy instead of paragraph walls;
- meaningful icon-based care and creation actions;
- four Nova-derived primary navigation intents;
- connected Circle → Stories → Inbox people flow;
- visual privacy difference between retained care and 24-hour Story;
- shared type/spacing/palette across phone screens;
- prototype-wide sample data label.

**Deliberate unresolved deltas**
- All botanical visuals are illustrations: **replace with authorized real plant/user/company photos where available, and improve art direction** before production.
- This is web DOM, **not** production Android Jetpack Compose and does not prove existing Nova components are wired to it.
- Production screenshots from Nova vs PR #240 still need direct side-by-side component audit; current reuse mapping comes from code.
- The eventual Circle Story placement, feed hierarchy and contextual Create/AI location must be user-approved after comparing actual Nova states and task success.
- The AI API, botanical sourcing, private-data consent and chat/session retention must be implemented and tested separately.
- End-to-end two-account privacy, actual uploads, notification deep links, Android navigation, offline and RTL/accessibility require genuine device proof.
- 100+ plants and company-authenticated service workflows need their own real-data/permissions test; don't call this a B2B product yet.
- The live backend/production Play package/Google Play listing must not be changed based on a browser study.

## QA evidence / precise limitation

A local Chromium Playwright smoke was run against the standalone HTML at desktop 1440px and mobile 390px. It covered Home → Circle → Inbox/Message → Create → public preview → Story → Plant → AI → Care; mobile Create → add plant → Care → Circle → Story → message. **PASS with no JavaScript page exceptions during tested routes.** This does **not** prove Android/Compose integration or data/backend correctness.

## Acceptance question

**Are the original Nova richness and human social surfaces now present in the right relationship to the plant's private care lifecycle?** If no, adjust the single integrated experience before writing the Compose implementation. Confirm hierarchy and missing functionality; then implement via native component-by-component reuse rather than bulk HTML porting.

**Source law:** keep the existing Nova engines where they help; do not let a media engine's mere existence decide the app's top-level product purpose.

**Only this research branch was changed. Nova PR #240 and master/production remain untouched by this study.**
