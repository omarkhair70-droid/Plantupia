# ADR-0001 — Native execution strategy for Plantupia (2026-10-12)

**Status:** RECOMMENDED, not frozen; user needs to affirm distribution ownership/package strategy before Play decisions.  
**Decision:** Use **Kotlin + Jetpack Compose** for the Plantupia Android product, **reuse/refactor the existing Nova engineering stack** rather than rewrite it in Flutter. Maintain an isolated working branch / PR while product ownership, store listing, and CI/release boundaries are decided. A *new repository* may later be created as a clean ownership and distribution boundary **without changing framework**; an empty Flutter rewrite is not the recommended starting point.

**No production change authorized by this record.** Existing PR [#240](https://github.com/omarkhair-labs/nova/pull/240) is draft, current head at research time `bf26a052c4dfe197e87bcb23a7cb1166fa659d69`, and remains separated from `master`. The existing production Nova Play identity `com.omarkhair70.nova`, release keys, Oracle production and database are protected.

## 1. User-approved experience, not approved execution equivalence

The user approved the **Plantupia × Nova Integrated Visual Pass 02** as a creative direction, and requested a **real app** matching or exceeding its expressive qualities: distinctive illustrated action controls, high-quality icons, efficient screens with comfortable density, flowing route transitions, animated media, complete Stories/Inbox/Profile/Circle/plant care, and a real AI assistant. A clickable HTML mock proves conceptual interaction only; it is **not** production code, doesn't establish Android visual behavior, and never provides tested access to Nova API and social engines.

Sources:
- [Integrated visual study](../../prototypes/nova-integrated-visual-pass-02/README.md)
- [Screen IA](../product/INFORMATION_ARCHITECTURE_V01_2026-10-12.md)
- [Nova integration/visual contract](../product/NOVA_INTEGRATION_VISUAL_CONTRACT_V01_2026-10-12.md)
- [Master product spec](../product/MASTER_PRODUCT_SPEC_V01_2026-10-12.md)

## 2. Verified existing Nova baseline (repository inspection on 2026-10-12)

Original Nova `master` is a substantial Android-native social product with:
- `app/build.gradle.kts`: Kotlin 2.2.10, AGP 9.2.1, Compose BOM 2026.02.01, Material3, Navigation3, Coil3, Media3 ExoPlayer/Transformer/effects, Firebase push, WorkManager, OkHttp, WebRTC/calls.
- `NovaBottomBar.kt`: original **five** nav destinations (Home / Orbit / Create / Inbox / Profile) with icon/vector ownership, animated Create selection and unread count.
- `ui/theme/Motion.kt`: semantic motion tokens `fast=120ms`, `standard=220ms`, `emphasized=320ms`; brand motion `NovaBrandMotion.kt` uses focused `Animatable` and presence animations; don't copy visual identity automatically.
- `ui/icons/NovaIcons.kt`: owned, bundled Material Symbols Rounded **vector drawables** through a semantic icon registry; good abstraction to retain but artwork is not automatically the final Plantupia icon grammar.
- `StoriesRail.kt`: text/image/video Stories, 24h semantics, progress/viewer, posting/audience states.
- `ReelsScreen.kt`: Compose `VerticalPager`, `ExoPlayer`, reused player surface and playback pool, reactions/sharing.
- `MessagesScreen.kt` + `ConversationScreen.kt` + features: active Inbox, chat, group interactions, audio/video call affordances, realtime.
- `NOVA_DESIGN_SYSTEM.md` and `NOVA_PRODUCT_POLISH_BRIEF.md`: semantic visual owners, multi-mood feature rules, genuine tactile polish; explicit note that implementation coverage is not perceived quality, and real device QA is essential.

The repository does **not** ship authoritative screen recordings/screenshots of the full original UI; code/design docs can verify the approach, not certify relative visual quality or smoothness. Capture side-by-side builds on the same Android device before claiming the new app equals/exceeds Nova.

Current PR #240 retains these engines, introduces `backend/plants/` and Compose space/plant/care/Circle features, and changes primary navigation to **مساحتي / الدائرة / إنشاء / أنا**, with Inbox reachable contextually. However the PR is NOT signed-off for visual or real device acceptance, and the new HTML prototype is not wired to it.

## 3. Alternatives

| Path | Benefit | Cost/risk | Verdict |
|---|---|---|---|
| A. Continue Compose on isolated Nova conversion branch, reuse code | No rewrite of social/media/network; fastest path to real on-device behavior | Must separate Nova visual identity and avoid production/Play changes; inherited monolith complexity | **RECOMMENDED immediate implementation** |
| B. Separate Plantupia **Kotlin/Compose** repository seeded from reviewed reusable Nova source | Stronger code/ownership/pipeline separation; proper branded app independent of Nova listing | Repo extraction/import, secrets, CI, Firebase/Play, backend service and release ownership must be coordinated | **Recommended when separate app/ownership is confirmed; no need to redo UI** |
| C. New empty Flutter repository with same backend | Cross-platform UI from outset; good Impeller renderer/tooling | Reimplement social calls, Stories, Reels, native interaction, messaging, notification/session plumbing and QA | **Not recommended now** unless validated simultaneous iOS delivery outweighs reuse |
| D. Raw HTML/WebView wrapping prototype | Fastest UI demo | Wrong platform boundary for complex native social/media UX, gestures, notifications and Android polish | **Rejected for production** |

Framework vs repo vs store identity are three **independent** decisions. Creating a repo does **not** require Flutter. Reusing code does **not** require merging the current PR to `master` or overwriting the existing Play listing.

## 4. Proposed native architecture (logical code boundaries)

```
plantupia-app/
  app/                             # Plantupia app shell: own launcher, nav, visual identity
  core/designsystem/               # PlantupiaTheme, PlantupiaType, color, shape, spacing, icon, motion
  core/identity-auth/              # audited and reused Nova auth
  core/network/                    # reused OkHttp/client transport / state
  core/media/                      # reused Nova media picker/uploads, Coil, Media3 player/coordinators
  core/messaging/                  # reused Nova Inbox/DM/groups and deep links
  core/social/                     # posts, profiles, relationships, story/reel services
  feature/spaces/                  # Living Home, Space index, placement/zone
  feature/plants/                  # Plant identity, details, photos and history
  feature/care/                    # record actions, check-ins/outcomes
  feature/circle/                  # plant Q&A + optional people/stories
  feature/create/                  # private/public media/action selector
  feature/inbox/                   # real people-to-people conversations
  feature/profile/                 # public identity + private space account context
  feature/assistant/               # separate, authorized AI conversation and sourced guidance
  benchmark/                       # macrobenchmarks and baseline profile when warranted
  docs/                             # architecture/quality contracts and review evidence
backend/Django plants + Nova reusable domain APIs (separate isolated environment for QA)
```

This is **target ownership, not a demand to immediately create 15 Gradle modules**. First maintain the existing working app module, establish package boundaries and contract tests, then extract shared modules only if justified. Android's official modularization guidance warns against excessive module overhead.

**Identity/ownership gate:** Decide whether Plantupia has an independent package/store listing/company-owned repo or deliberately replaces the owner's Nova listing. If separate, new package ID, signing, Firebase credentials, push links, legal/data terms, backend origin and Play provisioning are distinct. Don't publish an app under Nova's identity just because this conversion started in Nova's repository. Reuse rights/company IP transfer need explicit agreement before transferring a personal Nova codebase to a company-owned repository.

**Device/platform gate:** Kotlin Compose is the most cost-effective Android route *given existing assets*. If first release must ship iOS concurrently and budget/team can support it, reopen A vs C with quantified build work; don't imply Android code automatically ships to iOS.

## 5. Visual production contracts: build a genuine app, not text walls

- **Design for content and action:** readable plant photo portrait, actual room/place context, tactile action rail (Water, Inspect, Prune, Repot, Note, Ask), compact copy, chronological photographic continuity, accessible state badges.
- **Illustration ownership:** use an existing well-drawn **SVG/vector icon** when it communicates the action well and has appropriate license. Only custom draw meaning-bearing Plantupia primitives (e.g., soil check, real-care difference, botanical placement, plant timeline) when the baseline set fails. Don't hand-draw 100 generic settings/back/close icons. Convert SVG → Android vector drawable / Compose `ImageVector`, not a rasterized emoji-as-icon.
- **Brand assets:** Plantupia-approved real imagery and approved logo/type assets; user plant uploads are real content. Editorial/botanical placeholder illustrations must be clearly placeholders, not evidence of a real installed site.
- **Animation grammar:**
  - direct tactile response to press/check/record; localized physics-based `spring` where interruption matters.
  - photo-card → detailed plant image via `SharedTransitionLayout` / `sharedElement` or `sharedBounds` if compatible, avoiding expensive full-layout shifts.
  - status transitions `AnimatedContent`/`AnimatedVisibility` and medium/small emphasis roles for progress, due and saved events.
  - route navigation via current Navigation3 when integration is suitable; **don't replace the root routing engine because a new library is fashionable**.
  - `Media3/ExoPlayer` for actual Stories/Reels, preserve lifecycle/gesture/pool; never animate full-page video plus unrelated canvases without measuring frame budget.
  - Compose Canvas/DrawScope for custom branded line/shape drawing; **Lottie Compose or Rive** only for authored animations needing their specific timeline/state machines and after evaluating asset/runtime licensing and measured impact.
  - Android back/insets/keyboard, accessibility and reduced motion are part of visual quality; background data updates never freeze primary thread.
- **Motion cadence:** Start by auditing Nova's current fast/standard/emphasized semantics (120/220/320 ms), then author `PlantupiaMotion` by interaction purpose. Do not universally copy Nova timing nor turn every transition into a spring.

## 6. Proposed tech selection: reuse before add

| Job | Starting point | Admission test |
|---|---|---|
| Native UI | Kotlin + Jetpack Compose + Material3 | Existing, match user-approved behavior |
| Navigation | existing Navigation3 + app-owned route/state policies | back stack, deep-link, restore, no lost drafts |
| Images | existing Coil3 + Android photo selection/upload | loading/cache/sizing, private media, memory |
| Stories/Reels/video | existing Media3/ExoPlayer + current codecs/player components | player lifecycle, fast enter/exit, smooth next media |
| API/auth/DM | current Nova Kotlin repositories and Django endpoints | server-side authorization and privacy, reconnect |
| Icons | existing bundled Material Symbols Rounded vector set + bespoke Plantupia SVGs only where needed | semantic shape/weight coherence, 24dp readability |
| Custom motion | built-in Compose animation + SharedTransition APIs | measured frames, reduced motion |
| Authored vector motion | optional Lottie Compose | proof of specific motion asset and maintenance need |
| Complex interactive art | optional Rive Android runtime | tested need, authoring/usage rights and frame-time budget |
| AI | new Django-authenticated assistant proxy using hosted model + vetted references | consent, scopes, costs, botanical factual eval, no API key in client |
| Task scheduling | existing WorkManager (where appropriate) + server truth | actual reminder semantics, no invented watering predictions |
| Performance | Macrobenchmark + app-specific Baseline Profiles | real-device startup and jank improvement proof |

**No new dependency solely to follow a reference.**

## 7. Quality gates and evidence (NON-NEGOTIABLE)

**Screen contract:** natural Arabic RTL, responsive densities for 360/390/430 dp, dynamic text, touch area, accessibility labels, error/loading/empty/offline/permission, no fake success, quick visible feedback, back/gesture/keyboard, restore after process death where appropriate.

**Real device:** physical target Android, including older/minimum supported Android where possible. Performance analyzed on release/profile (not only debug). At 60 Hz a frame is about 16.7 ms; 120 Hz about 8.3 ms, but real display and OS conditions vary. Test cold/warm open, plant grid/long history, photo transitions, 24h story, video swipe, chat keyboard/input, create-with-media, uploads/retry, push/deep-link and active audio/call states. Record frame-time/jank, dropped media frames, launch delay, app ANR/crashes, network effects and battery/regression.

**Security:** two-account scoped spaces, user vs viewer roles, no public exposure of private plant notes/photo, AI only has authorized context; public Story vs private care are separate storage and consent lanes.

**Build proof:** unit + Android UI/instrumented checks, screenshot diffs, lint, backend tests, isolated preview DB/media verification, on-device walkthrough. No release/merge before signoff.

**Visual QA:** compare new app **side-by-side with a captured original Nova Android build**; screenshots/recordings of original required for claims about “as smooth as before.” Repo's `NOVA_FINAL_VISUAL_QA_2026-09-16.md`, `NOVA_DESIGN_SYSTEM.md`, `NOVA_PRODUCT_POLISH_BRIEF.md` explain intended design but are not a recorded user session.

## 8. Implementation sequence (real end-to-end vertical slices)

**P0 Baseline & decision (1 review pass):**
- protect Nova master/production and PR #240; preserve exact revisions and storage/QA configuration;
- secure original Nova app and PR #240 builds for direct on-device A/B;
- confirm separate app/store/ownership and first release device platforms;
- inspect currently working backend API and media privacy in truly isolated QA.
- produce visual native component contract for user-approved web study (semantic translation, not porting HTML).

**P1 Native design system + Living Home (first real APK):**
- implement `PlantupiaTheme/Type/Spacing/Shapes/Motion/Icons`; evaluate baseline vectors and author missing botanical action SVG/vector primitives;
- build real visual Home/Space/Plant profile and navigation with actual authenticated Plantupia data, solid empty/error/loading states;
- smooth photo-card→plant transition and a real media view, QA captures 360/390/430dp;
- deliver installable QA APK and measurable on-device review.

**P2 Care and Create:**
- user-owned care/observation/issue actions, photo evidence, check-in/outcome/history; visual icon quick-action sheet and privacy preview;
- retain existing Nova post/story/video publishing engine and make private/public destinations unmistakable.

**P3 Community/media/messaging integration:**
- Circle Q&A/people sections, real Stories viewer/composer, real Inbox/Conversation/Profile/Notifications/People, original Nova service state; preserve deep links and privacy.
- actual Story linked to a plant **only if explicitly approved** and separate from plant permanent history.

**P4 AI native companion:**
- real Django authenticated endpoint + model behind server-side secret, contextual plant data by permission/consent, sourced botanical knowledge, bounded cost/rate, text-first, possible photo later.
- AI chat is not the person-to-person Inbox or a Plantupia employee support guarantee.

**P5 Whole-product polish + release QA:**
- whole app visual/motion continuity, device metrics/macrobenchmark/baseline profile, realistic large and small collections, offline/recovery, RTL, two-account privacy.
- independent Play listing/signing/migration only after approved business package/ownership choice.

Sequence can be reorganized to unlock real device evidence earlier; no pointless “wait until all screens complete to test.” Every slice must be designed → implemented → tested → reviewed → closed.

## 9. External technical references reviewed (official)

- Android modularization: https://developer.android.com/topic/modularization
- Compose animation springs: https://developer.android.com/develop/ui/compose/animation/customize
- Compose shared transitions: https://developer.android.com/develop/ui/compose/animation/shared-elements
- Compose drawing: https://developer.android.com/develop/ui/compose/graphics/draw/overview
- Compose performance: https://developer.android.com/develop/ui/compose/performance/bestpractices
- Android Macrobenchmark / Baseline profile: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile
- Android Media3 Compose player: https://developer.android.com/media/media3/ui/compose
- Android icons and vectors: https://developer.android.com/develop/ui/compose/graphics/images/material
- Google Material Symbols Apache 2.0: https://developers.google.com/fonts/docs/material_symbols
- Lottie Compose: https://github.com/airbnb/lottie/blob/master/android-compose.md
- Rive Android runtime: https://github.com/rive-app/rive-android
- Flutter Impeller: https://docs.flutter.dev/perf/impeller
- Flutter profiling: https://docs.flutter.dev/tools/devtools/performance

## 10. Open decision to prevent accidental wrong app release

**The one critical product-distribution question:** Is Plantupia meant to be a **separate company app and Google Play listing** with its own package ID, while personal Nova stays independently available, or is it deliberately a **renamed/replaced Nova existing Play app**? A new Git repository is compatible with **either**, but the package/update/signing/distribution strategy is not interchangeable.

**Recommended default unless explicitly decided otherwise:** protect Nova Play product and produce an independent Plantupia app identity once approved, while sharing reviewed Kotlin/Compose and Django code under a clear owner-controlled boundary.
