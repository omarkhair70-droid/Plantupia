# PLANTUPIA / PASS 05 — THE ANATOMY OF EXCEPTIONAL INTERACTION
**2026-10-14 · Working teardown · Public evidence + new experiments, not product approval**

Pass 04 rebuilt a cross-domain reference atlas. Pass 05 asks a harder question: **which *mechanism*, precisely, made an award-winning interaction successful—and would that mechanism survive Plantupia's actual user tasks, Android stack, human-generated content and privacy boundaries?** This is not a gallery of attractive screenshots.

**Primary context:** [Pass 04](../research/06-award-winning-cross-domain-discovery-pass-04-2026-10-14.md), [the 7 original principles](../synthesis/01-meaning-extraction.md), [interactive Visual Study 03](../../prototypes/full-product-review-03/index.html), and [Native implementation audit](https://github.com/omarkhair-labs/nova/blob/feature/plantupia-native-experience-20261012/docs/PLANTUPIA_MASTER_ROADMAP_REFERENCE_AUDIT_2026-10-14.md).

## Method: follow the gesture, not the style

Decompose a reference into seven stages: **trigger → first screen → single strongest action → feedback → true data mutation → return path → failure/alternative**. The last three stages are especially important because promotional award videos rarely establish robust error states. Terms below: **[VERIFIED]** directly stated by organizer/developer; **[INFERRED]** interpretation from public demos/screens; **[PROPOSED]** our own test design. Do not imply screen recording, private access to apps or user testing if none occurred.

### T1 — CapWords / Apple Design Award 2025 winner, Delight & Fun
**Original:** [Apple 2025 ADA winners](https://developer.apple.com/design/awards/2025/); [developer interview with screenshots](https://developer.apple.com/articles/capwords).
- **Trigger [VERIFIED]:** the user sees a real-world object and photographs it. **Visible action:** capture the object. **Feedback:** a tiny animated, labeled collectible sticker; voice/sound couples sensory signal to meaning.
- **Process [VERIFIED]:** capture → foreground segmentation → confirm → display. Team describes using confirmation and micro-animation during API processing.
- **Actual insight:** confirmation can simultaneously **protect user intent** and **shape perceived latency**; an image's relevance is not identical to aesthetic polish.
- **Translate [PROPOSED]:** create Plant → capture existing photo → verify **which actual plant and which space** → private record saved → new photo remains the identity across Home/Plant/History. During *real* upload wait, show local preview and a restrained processing state. No simulated successful write.
- **Do NOT transfer:** automatic background removal erases physical placement and leaf/environment context; gamified sticker rewards for routine care; copying proprietary illustration or audio.
- **Failure test:** deny photo permission, upload times out, user changes space mid-upload, user taps back. Must display **unsaved / saved / retry** correctly; no invented successful record.
- **Prototype implication:** **Field Notes** interaction emphasizes photo, annotation and a deliberate confirmation with persistence status.

### T2 — Moonlitt / Apple Design Award 2026 winner, Interaction
**Original:** [official awards announcement](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/); [full team Q&A/screens](https://developer.apple.com/news/?id=v1nphz91); [WWDC26 UI brand talk](https://developer.apple.com/videos/play/wwdc2026/251/).
- **Trigger [VERIFIED]:** a time/location question about the moon. **Foreground:** grounded celestial visual / calendar or map / real sky; conventional platform navigation remains legible. **What is hidden:** complex astronomical calculations and coordinate transformations.
- **Insight:** the experience is ***simple* because the hard parts are real and accurately modeled**, not because it masks uncertainty with pretty graphics. WWDC explicitly encourages customizing the content layer where it matters and retaining familiar system patterns.
- **Translate [PROPOSED]:** space and plant photography is the center. A small but *correct* timestamp and next human-chosen check-in are readable at a glance. Use standard Android date pickers, scroll, semantics, navigation back.
- **Do NOT transfer:** sky simulation, liquid glass visuals, three-dimensional viewpoint without reliable planting geometry and lighting. No fictitious “plant health orbit.”
- **Failure test:** plant has zero photos, user changes timezone, plant never recorded care. UI remains intelligible rather than losing its premise.
- **Prototype implication:** **Living Atlas** gives real place context more weight than ornamental text.

### T3 — Tide Guide / Apple Design Award 2026 winner, Visuals & Graphics
**Original:** [Apple 2026 award announcement](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/).
- **Trigger [VERIFIED]:** user needs real tides/conditions. **Information architecture:** full-screen charts, hourly forecasts, widgets, time-sensitive palette. Strong imagery corresponds to a real physical variable.
- **Insight:** data is worth visualizing if it changes a decision at the right resolution.
- **Translate [PROPOSED]:** build only charts of **recorded events** (observations, photos, planned reviews, recorded outcomes). A blank graph for missing data is preferable to a fictional green “health” curve.
- **Do NOT transfer:** automatic irrigation rhythms, bogus temperature/CO2/soil telemetry or unlicensed chart visual design.
- **Failure test:** user has one data point in 4 months. Design must say “not enough observations to compare,” not interpolate pretend growth.
- **Prototype implication:** **Field Notes** should reveal actual photo-pairs *when present*, otherwise show a single dated record.

### T4 — Focus Friend / Google Play Best App of 2025
**Original:** [Google Play 2025 official winners](https://blog.google/products-and-platforms/platforms/google-play/best-apps-games-2025/).
- **Trigger [VERIFIED]:** need to focus on an activity away from the phone. **Key idea:** joyful, small ritual and minimal attention demands. The literal gamification belongs to Focus Friend, not the Plantupia problem.
- **Translate [PROPOSED]:** a 20-second home loop: **one real item to check → log what happened → leave the app**. No streak pressure; “checked soil” is not synonymous with “watered.”
- **Failure test:** can a person dismiss an irrelevant check-in without seeing a red danger banner or losing history?
- **Prototype implication:** **Quiet Care** starts with exactly one due item and clear skip/defer.

### T5 — Are.na / non-award knowledge structuring reference
**Original:** [Channels](https://help.are.na/docs/getting-started/channels); [Handling blocks with care](https://help.are.na/docs/guides/handling-blocks-with-care).
- **Mechanism [VERIFIED]:** images/text/links become reusable blocks; the context of their connections provides meaning. Channels have distinct access types, including private.
- **Translate [PROPOSED]:** a question is a **knowledge object** with a source plant, public-safe image, community responses, and **a separate observed outcome**. Data ownership remains private unless user explicitly publishes a chosen extract.
- **Failure test:** user logs private placement “behind bedroom window”; other users must never see that through a social preview, notifications, guessed ID or AI context.
- **Prototype implication:** private/public is **visibly separate in all three worlds**.

### T6 — Day One / personal journal mechanics (not claimed an award winner)
**Original:** [Day One features](https://dayoneapp.com/features/).
- **Mechanism [VERIFIED as product feature]:** dated entries with media, calendar/chronological retrieval and “return to an earlier self.” A photo/date can be more meaningful than a health score.
- **Translate [PROPOSED]:** a plant and its environment change through human observations. Time appears with *photographic evidence*; records are not decorative cards.
- **Failure test:** 200 notes and only 2 photos. User can find both photos immediately and retrieve a named care event without traversing 200 cards.
- **Prototype implication:** **Field Notes** gets a photo-index and All/Photos/Care filters without inventing missing photos.

## Visual reference deconstruction — what to look at in primary captures

| Reference | Actual original screenshot/story to inspect | Composition law | Critical interaction | Android transfer decision |
| --- | --- | --- | --- | --- |
| CapWords | [Original iPhone photo/sticker screenshots](https://developer.apple.com/articles/capwords) | One hero artifact at a time, feedback attached to it | Capture → confirm → durable item | **Use** review and persistence status; don't copy sticker artwork |
| Moonlitt | [Moon / city / map screenshots](https://developer.apple.com/news/?id=v1nphz91) | Main content can breathe when chrome steps back | Spatial/time switch with little explanation | **Use** contextual states and standard native platform controls |
| Tide Guide | [Award screenshots](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/) | Visual chart is the explanation, not decoration | Scrub/chart context anchored to actual data | **Use if** actual plant records justify a chart |
| Focus Friend | [Play winner story](https://blog.google/products-and-platforms/platforms/google-play/best-apps-games-2025/) | One focused task with reward | Enter activity / return to life | **Use** attention reduction, **reject** engagement tricks |
| Are.na | [Channel screenshot and access modes](https://help.are.na/docs/getting-started/channels) | Sparse material index, context from relationship | Organize/return to source | **Use** Circle's knowledge accountability |
| Day One | [Product feature captures](https://dayoneapp.com/features/) | Photography + specific time remains central | Revisit earlier entries | **Use** evidence-backed temporal navigation |

This is a source-audited teardown, **not** a claim of having watched real device interaction frame-by-frame; a full motion-frame capture will be a separate **Pass 05B**, prioritized over more inspirational lists. Record the evidence source and the sequence we can actually verify, then note what still needs viewing.

## Three competing worlds — **one dataset, comparable route depth**

These three concepts use the **same synthetic, clearly labeled test data** for fair comparison. An image shown in the demonstrator is independently sourced, licensed sample stock **never presented as a real Plantupia client installation or a real user's photo**. Sample events never claim API persistence. UI language English-first; test users may enter multilingual text.

**Scenario:** A user has one living-room space with three plants and one **person-selected check-in** due; they want to (1) find plant, (2) record that they inspected its soil, (3) see the previous dated record, (4) locate its actual photographs, (5) open an optional community question without exposing private details. Same scenarios in each world.

1. **Living Atlas — PLACE.** Entry = space photograph and plant “spots”; geometry is illustrative, not a floor plan; tap an actual plant → private history → quick record → optional community. Success = find plant within 2 direct taps and know where it lives. Failure = no actual photo / 100+ plants becomes unreadable.
2. **Field Notes — EVIDENCE.** Entry = selected plant photo/dated observation, a native note composer and change over time. A check-in outcome is shown under the actual source event. Success = record a private observation with media and recover it without searching generic feed. Failure = too many poetic transitions to log one action.
3. **Quiet Care — ATTENTION.** Entry = one due review and explicit **Inspect / Not today / Open history** choices. Hero is editorial but does not obscure next action. Success = one observation in ≤20 seconds without declaring an automatic watering instruction. Failure = “quick” design deletes essential context or discourages larger collections.

## Scoring instrument — hypotheses, not fake usability results

Every concept is judged with identical evidence:
- **Task completion** 0–5: five tasks above, observed, not presumed.
- **First useful action**: taps/time from launch to safe private care record.
- **Data truth**: every displayed number/photo/time has provenance or is clearly labeled synthetic sample.
- **Privacy**: cannot accidentally carry private placement/photos into public preview.
- **Identity**: photograph, architecture and living time feel native to Plantupia, not a skin over generic social feed.
- **Accessibility**: readable English, large text, high contrast, meaningful focus/label; Android's interactive target should be ≥48dp. [Android accessibility](https://developer.android.com/develop/ui/compose/accessibility/api-defaults).
- **Implementation risk**: preservation of Nova native back, navigation, Media3, original data and users.
- **Qualitative aftertaste**: “I want to go check the actual plant” vs “I want to stay scrolling this app.”

The scores stay **unfilled** until actual testing. No winner declared from screenshots alone.

## Rules for motion / actual implementation

- **No 3D plant health illusion.** Time mapping from actual `observed_at`/event date; if no photo pair, no animated growth forecast.
- **Private/public are structurally different flows**; third-party stock placeholders are never silently published.
- **One image identity across navigation**; implement optional shared element only after checking Coil placeholder/cache, back-stack, cancellation, TalkBack. Official [Compose shared element](https://developer.android.com/develop/ui/compose/animation/shared-elements) and [async image cache guidance](https://developer.android.com/develop/ui/compose/animation/shared-elements/common-use-cases).
- **Use system behavior where familiar.** Custom visual work should be concentrated where photos and real care matter, not every toolbar or Settings list. Apple WWDC26 makes the same general argument, but follow **Android** native conventions, not iOS cosmetics. [WWDC26 brand talk](https://developer.apple.com/videos/play/wwdc2026/251/).
- **The user approves the fully integrated APK at the end.** Research prototypes are **not** production commits or secret access.

## Source recheck that could overturn this pass

Could the most meaningful activity happen *outside* the app (physical care)? Could stronger image-driven stories harm quick care? Could a serious caretaker prefer a plain searchable list? Could “community wisdom” spread wrong advice? These are genuine disconfirmation criteria, not reasons to abandon experiments.

**Next Pass 05B deliverable:** clickable, one-file desktop/mobile comparison studio of the three directions, with 5 shared task buttons, simulated photo/media, and no backend writes, accompanied by a shot-by-shot audit against *current* installed QA captures at final review. Native PR remains unchanged for this experimental design research.
