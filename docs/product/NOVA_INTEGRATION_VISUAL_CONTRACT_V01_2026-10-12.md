# Plantupia — Nova Integration & Visual Experience Contract v0.1

**Date:** 2026-10-12  
**Status:** CORRECTION / UX-ENGINEERING AUDIT — *NOT* a frozen redesign or permission to modify production.  
**Code inspected:** `omarkhair-labs/nova`, PR [#240](https://github.com/omarkhair-labs/nova/pull/240) / `feature/plantupia-product-conversion-20261010`, current HEAD verified earlier `bf26a052c4dfe197e87bcb23a7cb1166fa659d69`.  
**Parents:** [Master Product Specification](./MASTER_PRODUCT_SPEC_V01_2026-10-12.md), [Information Architecture](./INFORMATION_ARCHITECTURE_V01_2026-10-12.md), [Design Study 01](../../prototypes/living-context-study-01/README.md).

## Critical correction

The HTML prototype is **only a disposable early interactive wireflow and visual experiment**. It is **not** the Plantupia design, is not Compose, does not reuse Nova's UI library, does not cover the full feature set, and never connects to Nova chat, Story, Reels or Django. It must not become a screen-by-screen implementation specification.

The user explicitly chose Nova for more than backend/servers: existing **native Android Compose component work, iconography, photos/video handling, motion, navigation, social infrastructure, sessions, messages, Stories, feed, real-time and CI**. This investment must be evaluated for direct reuse while Plantupia's authored product language stays independent.

**No sensors:** Plantupia has no sensors in plants. No IoT UI/telemetry/automatic soil measurement belongs to the current app.

## Audit of actual current Nova PR surfaces

| Technical source/surface | Inspected evidence | Candidate Plantupia role | Must NOT claim |
|---|---|---|---|
| `NovaBottomBar.kt` | Current four primary destinations: **مساحتي / الدائرة / + Create / أنا**; Inbox outside main bar | **Baseline to test**, preserve familiar access; compare alternatives with tasks | That prototype `Spaces/Care/Circle/Me` is an agreed nav replacement |
| `HomeScreen.kt` + `PlantupiaClientSection.kt` | Living-space module first, optional community feed afterwards | Redesign as visual living home using real plant media and attention, preserving authored Compose motion/icons | That stacked text sections are final UI or that full-page plant navigation is well resolved |
| `CreateHubScreen.kt` | Distinguishes private observation from public question/post; optional video, Story, Pulse, Gathering, Memory tools | Human-action-focused **Create composer**: record private care/photo, ask about plant, post a public moment, optional Story/video formats | That every inherited format must become a top-level tab |
| `StoriesRail.kt` | Story groups, photo/video/text creation, audience and viewer, 24-hour semantics | Existing Story engine; potentially show in a meaningful Circle people/media subspace | That Story automatically references `PlantUnit` or appears in a private plant timeline |
| `MessagesScreen.kt` + messaging repositories | Native Inbox/search/filter; existing conversations | User-to-user messaging with existing identity and moderation; access via Circle + Profile or richer discoverable path if tested | That this is company support chat or the AI Companion |
| `OrbitScreen.kt` | Two sections **النباتات والأسئلة / الناس واللحظات**; Inbox icon+unread badge, discovery | Plant Q&A connected to real plant/public consent, plus people feed and optional media | That all Nova social formats are necessary Plantupia landing content |
| `ProfileScreen.kt` | Existing Nova identity/posts/follow stats; private `PlantupiaProfileSpaces` self-only; Inbox shortcut | Keep personal/public community identity separate from private spaces; review which stats matter | That client-space photos/records are public profile posts |
| `ReelsScreen.kt`, `PulseRail`, `RoomsRail`, `MemoriesRail` | Existing engines/features retained under old Nova | **Retain code until deliberate product review**, selectively surface if actual purpose exists | That inherited engine availability determines core IA |
| `backend/plants/` | Spaces, plants, event history, nicknames, linked questions; authenticated views | Actual living-domain source of truth for the mobile experience | That a complete company operations, species AI or Chatbot backend already exists |
| `PlantupiaCreateIntent.kt` | Routes private observation/public plant question from existing destinations | Reusable navigation bridge for contextual actions | That UX is complete just because it routes |

## Connected experience: three independent data/publicity lanes

```
A. PRIVATE, PERSISTENT LIVING RECORD
My Space → Plant (actual identity) → Record care / observation / concern
  → private dated history → human follow-up → actual outcome

B. PUBLIC SOCIAL EXPRESSION (explicit and revocable choices)
Plant issue → user decides “Ask Circle”
  → public-payload preview → Publish question / linked Post
  → public replies → OPTIONAL private observed outcome
OR
Create → Public photo/post OR Story (24h) OR video, where relevant.
Private plant history NEVER silently becomes a Story.
Story ↔ Plant direct linking = NEW scoped contract + privacy migration, NOT implemented.

C. PRIVATE COMMUNICATION / AI
Circle or Profile → Inbox → existing person-to-person conversation.
Plant → “Ask AI about this plant” → NEW server-authenticated assistant
  → consented plant context + general botanical knowledge, read-only answer
  → user explicitly saves only chosen observation/check-in.
These are different conversations, permissions, retention and trust models.
```

**Additional flows to design beyond the early HTML prototype:**
- Circle → public plant question → answer/comments → deliberate action/privately recorded follow-up.
- User story row → 24h viewer → reply/reaction → existing inbox; assess actual Nova behavior before specifying deep links.
- Relevant notifications: reply, message, mention, follow-up. Existing Nova push can be *reused*, but **new care event types and routes have not been tested end-to-end**.
- Profile / person → follow / message → return to Circle without losing personal/private context.
- Publishing public photo vs saving private care photo: visible destination, audience and media retention at time of action.

## Visual/interaction design correction

The feedback on HTML study 01 is **accepted as a real delta**: too text-led, insufficient visual hierarchy, custom icons, meaningful native interactions and connection to existing rich Nova composables.

The next **high-fidelity native visual study** must:
- Treat **real plant/space photographs** as visual evidence, with a well-designed illustration/placeholder only when no approved photo exists.
- Use **legible illustrated/icon actions** for watering, observing soil, pruning, repotting, recording change, questioning; icons describe actual actions, not generic green decorations.
- Let photo hero, plant gallery, care state and dated image sequence carry hierarchy; descriptions stay compact and progressive.
- Make **“record”** a contextual action sheet with clearly separated PRIVATE vs PUBLIC actions.
- Preserve Nova's performant native media viewer, image picker/upload, gestures and animation systems when suitable; adapt components/tokens rather than wholesale WebView replacement.
- Design a visible and trustworthy **Inbox/Story/People** navigation position with social richness, not remove it behind a text-only plant prototype.
- Keep useful controls familiar and true to Android; image and transitions should represent causal state, not decoration.
- Use audited company branding and actual source materials; avoid generic template AI imagery or invented office client photos.
- Audit RTL, text scale, loading/offline/error, unsaved draft and small screen behaviors, and compare to original Nova and relevant competitor task experiences.

### Recommended initial composition to TEST (not freeze)

```
LIVING HOME — real private space identity / hero / planting arrangement
    due check-in(s) and observed change (actual records)
    visual grid/strip of plant portraits + quick actions
    record [private] / ask [plant-specific] / explore other spaces

CIRCLE — question knowledge section | people & moments section
    relevant public posts and Story rail if testing shows it adds value
    Inbox (unread badge); person profile and messaging

CREATE (+) — private care / observation / concern
          — public question / post
          — Story / video as deliberate expressive choices

ME — public profile and follows, personal space shortcut,
     inbox, settings and account/private-data boundaries
```

The **Assistant** should be accessible in a plant and optionally globally; it does not have to consume a tab. **Care** may be a Home/plant destination rather than replacing the central `+`; compare with N2 and real task tests.

## Integration/build sequencing

1. **Surface inventory:** screenshot/capture each existing Nova production branch UX (home, Story, chats, Create, Circle, Profile, notifications) plus PR #240 QA; note what is mechanically reusable vs visually entangled.
2. **Architect a full-component screen map:** Navigation, auth, Space/Plant, private Care, Circle/Post/Stories, Inbox, Profile, Notification and AI. Separate public/private data and context passing.
3. **Rendered high-fidelity proof** of ONE interconnected trip: Space → plant → care/photo → optional Circle question → reply/inbox → return to plant. Include actual Compose-native iconography and interaction state; 360/390/430dp screenshots + Arabic.
4. **Storyboard user-generated Story separately:** creation, visibility, 24h, viewer, reply and how it differs from persistent plant history.
5. **Only then choose code boundary:** reuse existing Compose components, refactor/replace each obsolete presentation, retain backend; no blanket rewrite from HTML, no automatic Flutter migration.
6. **Review/freeze with evidence**, then implement on isolated branch/PR and test against a genuinely isolated preview DB/media; do not alter Nova master, production environment, signing or Play automatically.

## Current conclusion

This design study should **sit beside** Nova as a conceptual experiment, **not replace** the existing screens. Plantupia's eventual native design is a complete integrated experience; how much existing Nova presentation to keep is evaluated *component-by-component*. **Message and Story engines remain**, their product placement and Plant-specific linkage need explicit UX design and technical contracts. No main navigation decision is yet final.
