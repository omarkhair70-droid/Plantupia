# ADR-001 — Plantupia Native Implementation, Nova Reuse & Motion/Visual Quality

**Date:** 2026-10-12  
**Decision:** **RECOMMEND NATIVE ANDROID KOTLIN/JETPACK COMPOSE ON THE CURRENT NOVA PR #240 BASE**, rather than a greenfield Flutter rewrite.  
**Decision status:** RECOMMENDED IMPLEMENTATION STRATEGY / NOT A SIGNED PLAY RELEASE OR PRODUCT OWNERSHIP DECISION.  
**Design acceptance:** User approved [Integrated Visual Pass 02](../../prototypes/nova-integrated-visual-pass-02/README.md) as *direction*, with expectation of a richer native app, not a literal HTML conversion.  
**Implementation:** **NO native code changed by this ADR.**  
**Scope:** Android application. iOS has **not** been explicitly committed for the current release.

## 1 — The decision in one paragraph

Build Plantupia as a **fully native Kotlin + Jetpack Compose experience**, starting from Nova PR #240's branch and reusing its existing social and platform engines (auth, conversations, Stories, media, posts, notifications, profile, backend client, Media3, Coil, Navigation 3). Replace/reshape Plantupia's application-level experience *component by component*, not by embedding the browser prototype inside a WebView. Keep project operations on isolated branches and a QA deployment; protect original Nova `master`, production, existing Play signing and user data.

**Repository independence is a separate decision from choosing Flutter.** A new repo can host a copied/extracted **Kotlin Compose** project after engineering/license/ownership review, if Plantupia requires its own corporate ownership or delivery pipeline. It does not require rewriting the app in Dart. Do not create a new Flutter repo merely to make the product visually distinctive.

## 2 — What was inspected in actual code

Source: https://github.com/omarkhair-labs/nova/pull/240, head as checked earlier **`bf26a052c4dfe197e87bcb23a7cb1166fa659d69`**.

- `app/build.gradle.kts`: `namespace="com.nova.app"`, original Play `applicationId="com.omarkhair70.nova"`, `qa` applicationIdSuffix `.qa`, Kotlin/Compose, Material3, Coil 3, Firebase Messaging, OkHttp, Media3, Navigation3, WorkManager, WebRTC, telecom, and Android test frameworks.
- `gradle/libs.versions.toml`: Compose BOM, Kotlin, Coil and Gradle catalogue. **Pin only after project compile/compatibility test; new published library version ≠ immediate upgrade requirement.**
- `NovaApp.kt`: existing `NavDisplay` and stateful NovaRoute back stack; 916-line integrated host.
- `app/app/NovaAppHost.kt`: existing native root plus guarded Inbox/Reels overlays.
- `ui/components/NovaBottomBar.kt`: four intents **مساحتي / الدائرة / + / أنا**, with Inbox contextual.
- `ui/icons/NovaIcons.kt`: app-owned bundled Material Symbols Rounded vector drawables. The legacy Material Icons library isn't the primary app icon system.
- `feature/stories/StoriesRail.kt`: 24h Story composer/viewer, photo/text/video and audience.
- `feature/messages/MessagesScreen.kt`: inbox, search/filter, loaded conversations.
- `feature/create/CreateHubScreen.kt`: private plant care vs public question/post; old Story, Pulse, video & Rooms engines secondary.
- `feature/home/HomeScreen.kt` and `feature/plants/PlantupiaClientSection.kt`: existing living-module placed into native Home; the Plantupia component is large and combines multiple screen states, a refactor opportunity.
- `feature/profile/ProfileScreen.kt`, `feature/orbit/OrbitScreen.kt`: user identity, existing messages access, social/plant question separation.
- `backend/plants/*`: account-scoped spaces/plants/events/questions and a human-choice follow-up loop. No built AI assistant endpoint or real company sensor data.

**Important:** Repository/source proves code exists, **not** successful live real-device integration, complete visual quality, privacy security audit or future source/license ownership.

## 3 — Kotlin Compose vs Flutter comparison, for *this* codebase

| Criterion | Keep native Compose | New Flutter/Dart repo | Result |
|---|---|---|---|
| Android visual authorship | Custom `Canvas`, vector XML, Compose drawing, custom design tokens, native state and gesture APIs | CustomPaint, Widgets, animations, `Hero`, Impeller rendering | BOTH capable; no inherent win for Flutter on our design |
| Screen transition continuity | `SharedTransitionLayout`, `sharedElement`, `AnimatedContent`, Navigation 3, predictive back | `Hero`, Navigator, implicit/explicit animations | BOTH capable; native preserves existing navigation |
| Existing Nova Stories/Reels/Inbox | Existing Compose code and Media3 implementation reusable with targeted refactors | Native UI has to be rewritten in Flutter or bound via costly platform bridges/add-to-app | Native major advantage |
| Existing Firebase, Play, Android permissions | Preserve established code with QA/regression | Reconfigure and retest wrappers/plugins and release behavior | Native advantage |
| Django backend | Existing Plantupia endpoints reusable | Same Django API reusable | TIE |
| Android speed to integrated product | Focus on Plantupia UX, models and QA | Rebuild equivalent messaging/media first or cut scope | Native advantage in this project |
| Potential iOS first-class app | Kotlin Compose Android UI doesn't automatically ship iOS | Flutter can share much UI across Android+iOS | Flutter advantage **if** iOS becomes a near-term signed requirement |
| Repository/ownership independence | New separate Kotlin repo possible later | New Flutter repo possible | Repo choice is framework-neutral |

**Rejected shortcuts:** shipping the HTML prototype as WebView; promising that `add-to-app` automatically ports Kotlin screens to Flutter (it doesn't); starting a second Dart codebase while keeping native social subfeatures unmanaged.

**When to re-evaluate Flutter:** A separately confirmed commercial need for simultaneous iOS+Android and greenfield UI where UI reuse outweighs rewriting or interfacing with native social modules; a short proof-of-capability spike should validate all auth/media/push/inbox/story flows before framework switch.

## 4 — Actual Native visual architecture (not an HTML skin)

### Design system package

Suggested initial packages inside the existing `:app` project, **no premature Gradle-module explosion**:

```
ui/plantupia/
  foundation/   Colors, Type, Spacing, Shape, Elevation, semantic state
  icons/        Semantic icons, Android vector drawables, custom botanical glyphs
  media/        PlantPhoto, PhotoStrip, CompareView, Avatar & Story media adapter
  motion/       motion tokens + route/shared-element/gesture contracts
  components/   CareAction, PlantPortrait, SectionHeader, EventTimeline,
                EmptyState, ConfirmSheet, SafePublicPreview
  navigation/   plant destination keys + result/restore/deep-link contracts
feature/plants/
  home/         LivingHome (real space / recent actions / plants)
  detail/       PlantDetail (identity / historical event)
  care/         Observation, actual Care action, human follow-up & outcome
  explore/      Plant index/search
  ask/          Assistant read-only scoped to plant or generic, *new backend*
feature/circle/  Plant Q&A + existing Nova people, posts and Story engines
feature/create/  One native Create hub: private record vs public media/story
feature/messages/ existing Nova engine, visually integrated not rewritten
feature/profile/  private/public-safe account identity
```

Begin by refactoring the largest multi-state Plantupia view into independent UI/domain owners **without changing endpoints or data**. Keep story/chat dependencies behind stable application navigation callbacks/adapters, rather than copying 1078-line Story components into a new app.

If modular builds become a proven maintainability issue, extract `:core:designsystem`, `:feature:plantupia` etc later with tests. The current Gradle project only includes `:app`.

### Integration boundary

```
Native Compose UI (new visual system)
  ↕ ViewModel / UI state / event intents
Current repositories: PlantupiaRepository + Nova authenticated, media, social, notifications
  ↕
Django API (real selected plant, private action, Circle linkage)
```

**PRIVATE history**, **PUBLIC Story/question** and **PERSON-TO-PERSON chat** are separate domains. AI chat is a fourth domain and must never be silently identified as Nova Inbox. Direct Story↔Plant cross-link isn't currently implemented: needs a deliberate consent/source and backend relation contract.

### What the approved HTML is

The interactive HTML Pass 02 is a **design reference** for layout density, relative hierarchy, iconography, navigation, motion feel and full product story. It is **not a component kit to transplant 1:1**. Translate intent, assets and interactions into Compose; improve screen density and native affordances based on device experience.

## 5 — Visual finish, icons, illustration and images

**No paragraphs-as-app.** State-first visual hierarchy:
- Real photographed plant/space as the hero when authorized, never fabricated installation photo.
- Icon-based quick-care action row; descriptive accessible labels, concise assistance text only where necessary.
- Plant grid/portrait and image strips, not repeated identical text cards.
- Dated timeline with actual authorship/photo; visual `before → after` where evidence exists.
- Concrete status emphasis: **normal states quiet / authentic change noticeable / unresolved concern clear**, not invented health percentages.

**Three levels of imagery**
1. General controls/navigation: **reuse audited Nova Material Symbols vector catalog**, perhaps update sizes/optical weight, don't redraw standard “back/search/inbox”.
2. Plant-specific care action icons: author **8–12 semantic vector glyphs** with a coherent stroke/shape/optical grid; e.g. soil inspection vs watering vs pruning vs repot, actual source vector XML/ImageVector or Compose `Canvas`. Design them if general sets are ambiguous.
3. Large authored illustrations and transient animation: selectively bespoke editable SVG source (vector drawable where compatible), or authored motion assets. Use actual photos for primary user-generated content. No visual inference from an asset unless sourced/approved.

Material Symbols are currently recommended by Android documentation; Compose legacy `material-icons-extended` is not the correct automatic default. For **tiny stateful animation**, native Compose is preferred. For authored short illustration sequences, **Lottie Compose** is an *option* after size/performance/licensing evaluation; no need to add Rive or a second runtime by default.

**Illustration and photography must remain distinguishable.** The current browser botanical drawings are placeholder/demo art, not proof of an approved photographic art direction.

## 6 — Motion grammar: “smooth as Nova” is a tested system, not magic

| Interaction | Native mechanism | Motion brief |
|---|---|---|
| Home plant card → plant detail | `SharedTransitionLayout + sharedElement/sharedBounds` with Nav3 state | image/label continuity rather than abrupt cut |
| Tab switch | preserved tab destination/back stack; short content transition | keep tab states, scroll position and media; no reload flashes |
| Tap care action | interaction state + subtle scale/color + optional haptic | instant feedback; never imply success until server confirms |
| Create (+) | `ModalBottomSheet` / custom Compose sheet | spring natural entry; preserve text draft on dismiss |
| Save care event | pending UI → confirmed API response → timeline insert/transition | clear success only with real backend persistence |
| History | `LazyColumn` stable keys/content types + image caching | fast scroll even on 100+ plants; avoid per-frame layout |
| Photo viewer → return | shared media bounds or viewer presentation | contextual return, not lost route |
| Story viewer | existing Media3 pipeline / existing gestures, 24h semantics | responsive progress/pause/tap, native system/keyboard handling |
| Inbox → conversation | existing Nova destination flow plus state restoration | no wrong-person deep-link or accidentally shared plant data |
| Assistant → suggested action | normal native conversation, then explicit confirmation sheet | no model-driven writes, no false sensor readings |
| Android back swipe | Navigation 3 + predictive back where supported | no broken pop or ignored system gestures |

**Suggested engineering trial ranges, not fixed brand constants:** micro feedback ~100–180ms; moderate transitions ~220–360ms; larger shared imagery ~300–500ms when gesture/state justifies it. Springs should be interrupted by user input. Motion may differ across devices and reduced-motion settings.

**Performance gates:**
- Profile **release/profile equivalent** builds on at least one realistic midrange Android phone (not only debug/Chrome).
- Gather `FrameTimingMetric`, cold/warm startup and real-device video of J1/J2, Stories and Inbox; no invented pass/fps percentages.
- Aim to fit the frame budget at device refresh (60Hz ~16.7ms; 90Hz ~11.1ms); diagnose actual jank.
- Baseline Profiles + Macrobenchmark for selected high-frequency flows, when measured.
- Correct lazy-list stable keys, Coil downsampling/caching and thumbnail sizes, no network fetch or decode inside animation-critical composition.
- Android back gesture, dynamic text, RTL/bidi, low RAM, low network, offline/error and privacy handling.
- Build states: EMPTY, LOADING, DATA, EDITING, SAVING, SUCCESS, ERROR, OFFLINE; buttons never cosmetic.

## 7 — Native implementation slices (ordered)

**Gate 0 — freeze current source/QA safety:** verify PR head; note branch, APK QA; verify Coolify PR preview's DB+storage separation before app writes (Django Docker CMD runs `migrate` automatically); no original Nova master/Play updates. Confirm which app identity/distribution path is authorized.

**Slice 1 — Design foundation & Native Living Home:** implement real color/type/icon/action primitives in Compose; render Home zero/1/7 plants with real backend or privacy-safe fixtures; make screenshot/gallery and matched shared-transition details; Android screenshot/unit/UI proof.

**Slice 2 — Plant & Care complete:** profile/photo/placement, care composer, human choice check-in, real dated timeline, persist after app restart; private media permissions; 2-account isolation tests; no fake hardcoded results.

**Slice 3 — Create + Circle + Stories + Inbox:** unify shell and public/private choice; connect existing Nova social engines and verify Story/Message/E2E entry/return paths. Do not create a new social system.

**Slice 4 — AI Companion & botanical knowledge:** Django-authenticated plant context read-only AI + sources, cost/rate/privacy gates; one actual Android flow, no company warranty/policy hallucinations.

**Slice 5 — Hardening and full-app convergence:** design/brand asset review, UI state gates, responsive screens, real-device performance and accessibility, full UX/functional review, cut unnecessary Nova residual presentation without deleting reusable backends, QA release artifacts and approved Play strategy.

Each slice is a **complete end-to-end experience and demonstration artifact**, not a list of unrelated merged Compose screens.

## 8 — Repo / Play / company ownership decisions

Current `app/build.gradle.kts` uses Google Play `com.omarkhair70.nova` and an isolated `.qa` package variant. The original branch contract contemplated **updating the existing Nova Play listing** rather than shipping a new listing, but this is a consequential decision, not a mere package label.

- **Option A: update existing Nova listing:** preserve `applicationId`, signing, version line, privacy/update migration after explicit acceptance and ownership rights.
- **Option B: standalone Plantupia app:** new package ID/Play listing and usually separate delivery identity; assess backend ownership, license rights, migration, push, signing, terms, Google services, asset permissions. A new repo can be Kotlin/Compose with reusable code extracted under permission.
- **Do not choose both implicitly** or use QA suffix as a permanent public product identity.
- Avoid automatically changing server's Django auth schema or uploading private Plantupia facts into a public repository.
- Production PR merge/Play promotion needs an explicit release gate after real testing, not this ADR.

## 9 — Documentation and research sources

**Existing project:** https://github.com/omarkhair-labs/nova/pull/240

**Official external technical references, retrieved 2026-10-12:**
- Compose custom design system: https://developer.android.com/develop/ui/compose/designsystems/custom
- Compose graphics/Canvas: https://developer.android.com/develop/ui/compose/graphics/draw/overview
- Shared element transitions: https://developer.android.com/develop/ui/compose/animation/shared-elements
- Navigation 3: https://developer.android.com/guide/navigation/navigation-3
- Predictive back: https://developer.android.com/develop/ui/compose/system/predictive-back-setup
- Material Symbols icon guidance: https://developer.android.com/develop/ui/compose/graphics/images/material
- Native animation spring: https://developer.android.com/develop/ui/compose/animation/quick-guide
- Compose performance: https://developer.android.com/develop/ui/compose/performance
- Baseline Profile: https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile
- Coil/image performance: https://developer.android.com/develop/ui/compose/graphics/images/optimization
- Lottie Compose: https://github.com/airbnb/lottie/blob/master/android-compose.md
- Flutter explicit/hero animations: https://docs.flutter.dev/ui/animations
- Flutter Impeller/perf: https://docs.flutter.dev/perf/rendering-performance
- Flutter add-to-app: https://docs.flutter.dev/add-to-app/android/project-setup

**Execution criteria:** native code, real user flows, smooth measured motions, rich icon/visual hierarchy, no sensors, social engine preserved, isolated QA; genuine acceptance before any production release.
