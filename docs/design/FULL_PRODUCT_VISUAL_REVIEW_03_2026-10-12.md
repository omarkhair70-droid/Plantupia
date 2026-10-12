# Plantupia — Full-Product Visual Review / Design Study 03

**Date:** 2026-10-12 · **State:** REVIEWABLE DRAFT · **User approval:** NOT GIVEN · **No Nova runtime/production writes**
**Actual visual test:** [clickable HTML Study 03](../../prototypes/full-product-review-03/index.html) · [earlier Integrated Study 02](../../prototypes/nova-integrated-visual-pass-02/index.html)
**Code audit reference:** [Nova Draft PR #240](https://github.com/omarkhair-labs/nova/pull/240), at commit `bf26a052c4dfe197e87bcb23a7cb1166fa659d69`.

## 0. Scope / what feedback meant

The user asked to review and finish the **whole Plantupia experience as a cohesive design system** before native Kotlin/Compose changes. A previous attempt to immediately implement Care/Create navigation on a new Nova experiment branch was premature: a positive reaction to parts of an HTML prototype was **not** a product-wide design sign-off. The newly opened `experiment/plantupia-care-create-native-20261012` branch has no code changes as a result of this review.

Feedback to preserve:
- Nova was selected as fertile product foundation for **native Android components, real social flows, motion, media, Inbox, Stories, and infrastructure**, not only reusable servers.
- Integrated HTML Study 02 has some good visual direction but is **not** final polished Android UI; several screens remain more text-led than desired.
- The **Care heart/icon** identity felt useful. The **Create grouping itself** was also praised. They must not be treated as mutually exclusive.
- The user offered a **small exposed, swipe-up Create drawer**, but explicitly said they were uncertain and did not want to rush a permanent decision.
- Plantupia **has no sensors in its plants**. No IoT controls, telemetry or invented moisture figures.

### Two materially different navigation hypotheses (both testable now)

**A — Existing Nova pattern (control):** `مساحتي / الدائرة / [ + إنشاء ] / أنا`. Care is an important **contextual** destination within plant and home. Create opens its full well-grouped experience.

**B — Dedicated Care:** `مساحتي / ♡ الرعاية / الدائرة / أنا` plus an **exposed compact “إنشاء +” peeking drawer**, opened by tap or upward swipe; drawer contains the same action families and link to the original full Create page.

**No winner selected.** Compare first tap success for new plant, record care, return to due check-in, make Story, send DM, ask AI. A hidden gesture alone is unacceptable; B's exposed handle must remain legible and accessible.

The HTML is a **decision experiment**; a Bottom Sheet in production would be a genuine native Compose sheet preserving back gestures, scroll, focus/IME and accessibility, not a WebView or a hardcoded CSS drawer.

## 1. Whole-product screen / source-to-visual review ledger

Legend: **KEEP** technical engine/behavior where suitable; **REFINE** visible hierarchy/UX; **NEW** domain or integration; **GATED** needs approved real company/technical facts. These are review dispositions, **not** approved production tasks.

| Surface | Study 02/03 visual behavior | Verified existing Nova PR #240 source | Recommended disposition | Gap before native implementation |
|---|---|---|---|---|
| Welcome/auth/session | Study starts with sample owner; **not** full onboarding | `feature/welcome/WelcomeScreen.kt`, `feature/auth/AuthScreens.kt`, `NovaApp.kt` | **KEEP** auth/session foundation; **REFINE** first-use identity | Real return/resume, no forced hardware/purchase; dedicated Arabic empty state; proper auth errors |
| **Living Home** | Botanical illustrated image hero, compact actions, recent change, plant strip | `feature/home/HomeScreen.kt` + `feature/plants/PlantupiaClientSection.kt`; existing Nova home shell | **KEEP** auth, media, pull-to-refresh, notifications; **REFINE** authored visual hierarchy | Use real authorized/user photos; 0/1/7/100 plants, role-aware fields; no fake “healthy” metrics |
| Spaces / zones | Study's `بيتي` hero and plant list | `backend/plants/models.py` Space/PlantUnit + `PlantupiaRepository.kt` | **KEEP** existing models; **REFINE** navigation and spatial grouping | Zone model not currently shipped; office workflows require company evidence |
| Plant profile | Full-screen image, identity, placement, entry points to Care/AI/history | `PlantupiaClientSection.kt` currently renders plant detail **inside Home**, `PlantupiaRepository.kt` | **REFINE** screen composition; potential **NEW** dedicated native route if justified | Preserve deep return, search context, media loading and full-size photos |
| Care record | Icon-based human actions and real note (in prototype stored locally) | `PlantupiaCareActions.kt`, `PlantupiaClientSection.kt`, `backend/plants/views.py` | **KEEP** manual-care facts; **REFINE** illustrated/icon editor | Photo upload, actor/date, errors, duplicate tap, truthful follow-up vs watering recommendation |
| **Care overview ♡** | **Study 03 B** adds a Care destination for attention/history and icon actions | Plant list exposes next follow-up and events; **no separate Care root** in Nova yet | **NEW UX, using existing records**; compare A vs B | Cross-plant due aggregation; whether permanent tab adds value; avoid generic “water today” |
| Living history | Chronology explicitly separate from ephemeral Story | `PlantupiaClientSection.kt`, `PlantupiaRepository.kt` events | **KEEP** truth model; **REFINE** visual time, photos and change | Actual photo comparison and pagination on devices; source actor and date |
| **Create (+)** | One visual location for private care/add plant + public question/Story/media | `feature/create/CreateHubScreen.kt`: current full Create with these action families | **KEEP** behavior and full destination; **REFINE** visual cards and contextual intent | A full page vs B peeking sheet; correct private/public audience preview; native media capability |
| Circle/plant questions | Question cards, temporary stories and people/media split | `feature/orbit/OrbitScreen.kt` + `PlantupiaCommunityPanels.kt` + Nova Post | **KEEP** Post/circle engine; **REFINE** discovery | moderation/reporting; public context preview; content density with real posts |
| Stories | 24h media viewer, next/back, compose and reply demo | `feature/stories/StoriesRail.kt`, Nova Stories repo, publishing flows | **KEEP** 24h engine, audience settings, video; **REFINE** entry placement | Story→Plant **not implemented**; no auto-publication of private care |
| Reels/Pulse/Rooms/Memories | Study groups under social media/secondary actions rather than four primary tabs | `ReelsScreen.kt`, `PulseRail`, `RoomsRail`, `MemoriesRail` | **KEEP engines conditionally; REFINE** placement | User value of each format must be evidenced; don't let inherited availability dictate nav |
| Inbox | People-to-people conversation list + sample search | `feature/messages/MessagesScreen.kt`, messaging repositories and MainActivity Inbox overlay | **KEEP** messaging engine; **REFINE** contextual placement | Real search, unread, new message, media/calls, blocked/user perms, error/offline |
| Conversation | A local example message thread, separate from AI | Existing Nova chat messaging/navigation | **KEEP** native conversation semantics | Demonstrate actual thread through Nova staging; no claim prototype sends anything |
| **AI Companion** | Question tied to selected plant, opt-out context, prewritten explanatory answer | **No** `backend/plants/urls.py` assistant endpoint in audited branch | **NEW**, read-only text-first after approval | Provider, API key server-side, authorized retrieval, source labels, limits, factual evaluation, Arabic |
| Profile | Cover, avatar, private space shortcut, public/social identity | `feature/profile/ProfileScreen.kt`, `PlantupiaProfileSpaces.kt` and Nova follow graph | **KEEP** social identity, editing, follow metrics; **REFINE** hierarchy | Do not show private plants, locations or photos to visitors |
| Notifications | Sample care review/DM/reply states and contextual links | `NovaNotificationRepository.kt`, Home header, push routing; **not** plant follow-up push | **KEEP** genuine messaging/reply notifications; **NEW** any plant-specific notice | Opt-in notification, delivery, deep link and privacy; distinguish timer/check-in from guessed need |
| Company customer surfaces | Missing from Study 02/03 deliberately | Research `Cross-World Critique`; existing Space memberships, no proven actual lifecycle | **GATED** | Real site/visit/handover process, consented imagery and maintenance contracts |
| Public website | **Separate product** from this Android prototype | Plantupia research and site briefs; not in Nova PR #240 | **SEPARATE** design program | Real photographic case studies, approved services/brand and project inquiry |

## 2. Product-wide design language — what survives / what changes

### Preserve from Study 02 where effective
- Plant and space identity occupy the **visual center**, not a generic home timeline or KPI dashboard.
- Soft material tones, restrained typography and negative space can support real botanical images.
- Short contextual actions, icon-driven care choices, and clear private/public distinctions.
- Circle, Stories, Inbox, Profile and Create are **one app**, not invented as independent experiments.

### Correct before brand/production sign-off
- Move from **drawn generic leaf illustration as primary evidence** toward real user-supplied plant photography and authorized actual Plantupia case photos, with meaningful placeholders for empty states. Don't fabricate company assets.
- Use native **icon family and microinteraction system** throughout: water, soil, observation, pruning, photo, light/placement; do not substitute text blocks for meaningful controls.
- The home should show actual **attention** (user-selected check-in, unanswered issue), plants as recognizable photographic portraits, and real dated change over time. Never a fake health percent, sensor chart or default “water now” command.
- Create must have **clearly separated private** care and **public** Story/Post/Circle content. The transition to public must show audience and exact payload.
- Inbox and Stories must retain **their own media and social personalities**, not get simplified to text-only forms.
- AI text may be readable, but surfaced from plant context with evidence, uncertainty and conversation affordances, not portrayed as a verified plant doctor.
- Respect RTL/mixed English brand and botanical names, contrast and accessibility rather than imitating screenshot typography.
- Retain Nova motion/gestures where useful, but art-direct where transitions help causality (plant > care > change) instead of loading animation for decoration.

## 3. Which interactions need review together

**Trip T1 — private living loop:** Home → choose plant/photo → log real care → choose check-in → revisit due → record observed result → private history. Compare A vs B on number of taps and discoverability.

**Trip T2 — social expression:** Create → temporary Story/video → view & reply → Inbox with correct identity. Public content never takes private plant events without consent.

**Trip T3 — community learning:** plant concern → user authors selected public payload → preview audience/media → Circle question → replies → optional *private* outcome. Posting remains disabled in browser prototypes.

**Trip T4 — help from AI:** plant → contextual read-only AI → clarify soil/light/drainage → suggest a user-controlled observation/check-in; no real model in this design study.

**Trip T5 — personal vs public:** My profile → private space shortcut and user-authored public posts → other person's public profile → DM → return without revealing private plant history.

## 4. Study 03 A/B protocol (lightweight, not a research theater)

Use the **same** plants and tasks under both modes. On a phone, time 3 short tasks: (1) log a care action, (2) create Story, (3) find overdue follow-up. Note **hesitation and wrong taps** before liking the appearance. Prefer a variant that reduces discoverability burden without hiding Creation.

- **A keeps Nova behavior:** big plus on bottom; Care reachable in Home/plant.
- **B tests user's idea:** Care ♡ on bottom; a *visible* Create handle appears just above tab bar, can be tapped or swiped upward, with all action groups from current Create and a link to the complete Create page.
- Screen 'Care Hub' is a **new demo illustration** computed from local sample notes; currently Nova does not have this aggregate root. This is a hypothesis, not a release promise.
- The **Review Mode bar** and **Notes button** are editor affordances only and **must not be shipped in the Android UI**.
- No selection or screenshot can substitute for private/user journey acceptance.

## 5. Design progress, QA and remaining gates

**Delivered**: two switching navigation variants in a **single functional HTML prototype**; all Study 02 Home/Plant/Care/History/Create/Circle/Moments/Story/Inbox/Conversation/AI/Community Compose/Preview/Add Plant/Profile/Notifications are still accessible; new Care overview and Create drawer; screen-specific design review notes.

**Verified locally**: Chromium Desktop 1440×900 and mobile 390×844, 360×760; navigation A↔B, open Care, Create drawer, choose new plant, Circle, Inbox, notes; no JS page errors in those tested routes. This is **web interaction QA only**, not Compose, Android, backend, or accessibility certification.

**Open — no signoff yet**:
- Revisit actual Nova screen captures in the QA APK side by side before retiring/replacing native components.
- Produce high-fidelity art direction studies with approved real/photo sources and native interaction illustrations.
- Study 03 only varies navigation + Create format while retaining Study 02's general visual language. It does **not** solve all visual issues or implement missing mobile functionality.
- Company client and employee workflows require real operational facts. Sensors are categorically out of this product's scope.
- Once direction is approved: implement screen-by-screen Compose with reuse of live engines and real staging API E2E checks; independently test Nova production untouched.

## 6. Decisions ledger

| Decision | Current decision state |
|---|---|
| Keep Nova as code/infrastructure/media/motion base | Working agreed direction, subject to component review |
| Plantupia dedicated identity vs Nova green reskin | **Plantupia-specific experience** |
| Care as permanent bottom tab | **OPEN: A vs B experiment** |
| Create as full page or peeking Bottom Sheet | **OPEN: experiment** |
| Temporary Stories vs permanent plant history | **Separate by principle; retain original Story engine** |
| Public sharing of private care | **Explicit user consent required** |
| AI assistant | **Proposed, not implemented** |
| IoT/sensors | **EXCLUDED: company currently has none** |
| Final typography/photos/motion, screen layout and art direction | **OPEN: not approved** |
| Merge into Nova master or deploy to Oracle/Play | **NOT AUTHORIZED** |

**Next review:** look through the clickable study together and capture concrete feedback screen-by-screen, not “looks good, so implement now.” `The workflow repeats. The answer must not.`
