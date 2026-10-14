# PLANTUPIA / PASS 07 — INTEGRATED EXPERIENCE CHALLENGE
**Date:** 2026-10-14  |  **Status:** DESIGN RESEARCH — TESTABLE HYPOTHESIS, NOT USER APPROVAL OR PRODUCTION IMPLEMENTATION.

Companions: [Pass 04 Source Atlas](../research/06-award-winning-cross-domain-discovery-pass-04-2026-10-14.md), [Pass 05 teardown](./07-award-winners-behavioral-teardown-pass-05-2026-10-14.md), [Pass 06 reality-check protocol](../research/08-field-realities-validation-protocol-pass-06-2026-10-14.md), [Visual Study 03](../../prototypes/full-product-review-03/index.html), [Native audit](https://github.com/omarkhair-labs/nova/blob/feature/plantupia-native-experience-20261012/docs/PLANTUPIA_MASTER_ROADMAP_REFERENCE_AUDIT_2026-10-14.md).

## 1. What was actually built this pass
New local HTML `Plantupia_Pass07_Integrated_Studio.html` builds on the corrected Pass 05 three-world lab and adds a **fourth integrated candidate**. This standalone download is currently a generated conversation artifact, **not a committed website nor part of Android**. It retains all original worlds, same five comparison tasks, private composer, a human-readable local observation, dated history, one-image no-fake-pair state, and consent-gated simulated Circle preview. It adds scenario fixtures **0 / 1 / 7 / 100** for the integrated composition. All labels and imagery must remain explicitly marked illustrative; 100-unit fixtures are NOT actual persisted plants, and stock photographs are NOT Plantupia client installations. Non-modelled fixture entries aren't false clickable real plant records.

**Browser smoke executed using Chromium/Playwright `page.set_content`:** four tabs visible; Integrated view loads; 0/1/7/100 state buttons work; open plant → compose → local save → history displays actual just-written text; photograph screen honestly has only one; original worlds switch; desktop 1480px and mobile 390px viewport present without document horizontal overflow; no reported page errors. **Important limitations:** file-URL navigation was blocked by the test browser's administrator policy, so smoke used page.set_content; external stock photo fetches were unavailable in that browser environment; Android pixel/media/jank QA and user research are NOT covered by this test. The prior Pass 05 blank phone from JS global `top` shadowing was already corrected and did not recur.

## 2. Product synthesis is not a collage of four apps
The research hypothesis is **PLACE as context → QUIET CARE as current attention → FIELD NOTES as durable proof → NOVA-powered HUMAN HELP as optional route**. This does not create additional root tabs. Working owner navigation stays **My Space / Circle / Create / Me** pending the Study 03 A/B comparison. Private care/photo histories are distinct from public stories/questions. The physical plant continues to exist independently of the app.

### Screen-by-screen design contract: eight candidate improvements
| Native surface | Research source / interaction law | Current native evidence | Integrated challenge | Exact success criterion |
| --- | --- | --- | --- | --- |
| **Home / My Space** | Moonlitt: show real content instead of calculation chrome; Living Atlas spatial identity | `HomeScreen.kt`, `PlantupiaClientSection.kt`, `PlantupiaTodayPanel.kt` | Real user-uploaded space/photo is hero **only if authorized and present**, then one clear check-in; separate journal evidence; minimal repeated prose | 1st actionable check-in within one visible viewport; zero-photo empty state honest, not stock replacement |
| **Space** | Relational Life, site/place over generic plant list | `PlantupiaSpaceSwitcher.kt` and private Django `Space` | Space thumbnail + concise place metadata, plant search/filter when large; no fabricated surveyed layout | 1/7/100 fixture search/switch, correct access permissions |
| **Plant** | CapWords capture confirmation; field notes; ecological evidence | `PlantupiaVisualComponents.kt`, `PlantupiaClientSection.kt`, role-scoped context edits | Plant identity image + clear context + care action near thumb; personal nickname separate from shared label | Open from Home, reach action without giant paragraph, save actual selected action to Django |
| **Care Composer** | Quiet Care: get back to physical plant, standard Android confirmation | `PlantupiaCareActions.kt`, local date reminder WorkManager | First select actual action; optional note/photo/date; concise explanation. Saving is visibly pending/succeeded/failed | Nothing marked watered unless user selected it; denied photo/network handled; no duplicate write |
| **History** | Day One + Tide Guide truthful time and evidence | linked `PlantEvent` outcomes and history filters | One dated photographic story, care/outcome relationship, Notes/Care/Photos filters; no fictional comparison | 0/1/200+ events, missing/older photo states, reload/pagination preserve exact reality |
| **AI** | Merlin: observation→hypothesis→human test; source provenance | `PlantupiaAssistantSheet.kt`, backend model adapter | Ask bounded, optional context; show uncertainty; never infer sensors or write care autonomously | Real QA provider replies with no fabricated sensor measurement; failure state actually shown |
| **Circle / Create / public** | Are.na linked knowledge blocks; account-specific privacy | `PlantupiaCommunityPanels.kt`, existing Nova posts/comments | Separate public preview, independently chosen image, explicit consent, documented result stays private unless separately shared | Two-account public payload and EXIF/security test |
| **Profile / Inbox / Stories/Reels** | Nova's existing social engine is an asset, not an aesthetic endpoint | original Compose/media/messaging routes | Retain native player and DM, align English and shared design tokens; do not graft plant records onto feeds | Actual Story→DM→back with media/keyboard working on device |

**Surface ownership:** Core Home/Plants/Space/Care/History visual UI can become distinct Plantupia design; settings/security should use standard familiar components. The same **real information architecture** underlies all experimental worlds, and data must be truthful.

## 3. Four-world comparison protocol: without imaginary “winning scores”

| Candidate | First use case | Likely superiority | Dangerous failure | Status |
| --- | --- | --- | --- | --- |
| Living Atlas | authentic photographed location + few plants | spatial sense and familiarity | non-photo zero-state, slow 100-unit collection | Prototype interaction demonstrated, not measured |
| Field Notes | someone preserving images and observations | meaning, story and traceability | scrapbook tax on daily care | Prototype interaction demonstrated, not measured |
| Quiet Care | one human-chosen item needing observation | speed, agency and low distraction | hides context or multiple plants | Prototype interaction demonstrated, not measured |
| Integrated Candidate | actual photo + check-in + short dated memory | may connect strengths into cohesive Home | risk of becoming four cards stacked, editorial noise and non-matching imagery | Prototype interaction demonstrated, not measured |

**Metrics awaiting participants/device:** measured time/taps for finding Monstera, recording soil observation without watering, recovering history, finding genuine photo, and understanding public preview; 0/1/7/100 data shapes; error actions and screen reader; read-only account; offline. **No scores are filled in** and no winner approved.

## 4. Design choices and the right to reject them
- **Photographic hierarchy:** one authorized real image tied to a real plant/space, provenance/date near photo. No invented second image, no client photo with doubtful rights.
- **Editorial not templated:** Playfair/Inter from original brand guidance, restrained deep green/cream/sage, natural texture only when useful. Avoid over-rounded every-card UI and paragraph-first hero sections.
- **Real gestures:** custom artwork for plant care icons and selected photographic transitions; native system patterns for dates/settings/accessibility. Minimum Android target ~48dp.
- **Care is not diagnosis:** “Check soil” = real action; “Watered” = human report; date = user-selected check-in; alarm is NOT a watering order.
- **Agency/privacy:** read-only role cannot change shared plant; private records remain private; public explicit preview.
- **Motion is semantic:** photo expand confirms identity, saved action shows server ACK, check-in outcome links to source. Avoid animation that masks errors.
- **Native-first:** Kotlin/Compose/Coil/Media3/messaging remain. Don't implement experimental HTML as a WebView.
- **Brand review:** confirm official logo/vector and approved client assets with company before final. Preserve English chrome and authored RTL/multilingual notes.

## 5. Implementation readiness vs exploration
**Ready to design/specify now:** tighten Home copy/actions, visual tokens, an image-first plant header without false records, clear save-loading feedback, genuine history filters, first-run empty states; compare with final Android screenshots before committing redesign.

**Needs engineering acceptance and QA:** isolated Django QA deploy, real-account plant/photo/public flows, actual AI provider (secret in QA only), Android reminders/persisted permissions, Nova inherited video/DM regressions. Green unit CI is not a demo of live infrastructure.

**Needs product/company decision:** official wordmark and typeface licensing, actual company install/service model B1, responsibility rights, app package/Play/distribution, professional SOPs. No carbon or IoT telemetry unless real hardware/source exists.

**Deferred research:** derived health charts, forced adaptive watering, immersive indoor 3D model, automatically shared private photo, plant gamification, notification streaks, speculative annual carbon metrics.

## 6. Technical trace to Native PR
PR: [omarkhair-labs/nova#241](https://github.com/omarkhair-labs/nova/pull/241) remains Draft. At research start HEAD `5f190068` had two successful Android/Backend CI runs. **Pass 07 does not change this native head**. Continue engineering independently only for accepted product semantics and audited security; do not block on user screen review. Review complete integrated APK once at the end, as the owner requested.

## 7. Decisions before converting concept → native
- **D07-01** (tentative): Integrated candidate is a **fourth hypothesis**, not a merged final design.
- **D07-02** (accepted product constraint): C0 care/history true and private; no fabricated sensors, before/after, or diagnosis.
- **D07-03** (tentative): Default app navigation stays as-current while testing Care-focused alternative.
- **D07-04** (accepted product constraint): UI English-first; user-authored text Unicode stays as authored.
- **D07-05** (unresolved): Does Home show a space hero, a due item, or last actual image first depending on state? Test per context rather than one global answer.
- **D07-06** (unresolved): For 100-unit company scenario, photo atlas may be secondary to searchable plant inventory and explicit caretaker assignments (company role approval required).

**Next pass:** actual 390dp and 360dp QA screenshot comparison against prototype, true 0/1/7/100 data fixtures if safe on isolated QA, identify component-level diffs, then implement only validated improvements in Compose. The experimental file is standalone and not evidence of native completion.

## Addendum: local anonymous comparison trace
The standalone prototype now exports a JSON trace of task completions and on-phone button taps per world. It deliberately omits typed care notes, images, accounts, and personal data. These numbers document scripted prototype actions, not user-validated success. Chromium smoke tests pass after this addition, including desktop and 390px mobile layout.
