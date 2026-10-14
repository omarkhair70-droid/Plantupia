# PLANTUPIA × NOVA — Source Atlas Pass 04
## Award-winning cross-domain re-discovery **after** the working native product
**Date:** 2026-10-14  
**State:** NEW RESEARCH / product and design hypotheses, **NOT** approvals, production work, a guarantee of awards, or an instruction to port iOS screens.  
**Preceded by:** [Original Working Law](../WORKING_LAW.md), [7 Meanings](../synthesis/01-meaning-extraction.md), [Meaning → Product Translation](../synthesis/02-product-translation.md), [Master Spec](../product/MASTER_PRODUCT_SPEC_V01_2026-10-12.md), [Design Study 03](../design/FULL_PRODUCT_VISUAL_REVIEW_03_2026-10-12.md).  
**Native baseline:** stacked Nova [PR #240](https://github.com/omarkhair-labs/nova/pull/240) and Plantupia [PR #241](https://github.com/omarkhair-labs/nova/pull/241), and [2026-10-14 native roadmap audit](https://github.com/omarkhair-labs/nova/blob/feature/plantupia-native-experience-20261012/docs/PLANTUPIA_MASTER_ROADMAP_REFERENCE_AUDIT_2026-10-14.md).

> **The workflow repeats. The answer must not.** When a working prototype emerges, deliberately revisit even the premises that made it possible. "We have a mobile app" is not a reason to research only app UIs. Awards identify *interesting qualities worth dissecting*, not ready-made product answers.

## Research brief 04 / blank slate

**What actually exists:** a functioning-but-not-finalized Kotlin/Jetpack Compose Android app derived from months of original Nova work: authentication, visual/media components, messages, social posting, Stories/Reels, network/session/CI, plus newly built private spaces/plants/manual care/follow-ups/history, Circle opt-in public questions and a server-mediated AI assistant. This unusual foundation can make combinations feasible that a blank-slate plant startup would not build quickly. **Do not conflate engineering reuse with a design thesis or final app quality.** Server deployment, real hosted AI credentials, real mobile end-to-end data and official brand approval remain separate gates.

**New question:** What would Plantupia look and *behave* like if we studied exceptional digital products for memory, time, materiality, situated knowledge, social validation, service traceability, ecology and attention—in addition to plant care—and recomposed their underlying interaction laws into something original?

**Evidence tags:** `[A]` award organizer verifies win/finalist; `[O]` official product/developer says behavior exists; `[C]` community anecdote (not population evidence); `[H]` author's hypothesis; `[R]` existing repository code/docs. **A winner, finalist, SOTD, iF Student Talent project and a non-winning product reference are categorically different.** An award does not establish user retention, accessibility or technical robustness.

## 1 — Awards landscape: the reference is not the category

| Reference and award evidence | Mechanism worth reverse-engineering | Proposed Plantupia translation | Avoid |
| --- | --- | --- | --- |
| **[CapWords](https://developer.apple.com/articles/capwords)** — **[A] Apple Design Award 2025 winner**, Delight & Fun | Physical object photo → animated, affirmable sticker/knowledge object. Developer explains capture → background extraction → confirm → response stages and deliberate microfeedback during processing. | Photo of user's actual plant becomes a *living identity* that remains central across space, record, compare and optional question; joyful deliberate photo registration. | Auto-cropping away plant *context* (pot, light, surroundings) or attaching private photo to public post automatically. Also CapWords' Apple frameworks cannot simply be ported to Android. |
| **[Moonlitt](https://developer.apple.com/news/?id=v1nphz91)** — **[A] Apple Design Award 2026 winner**, Interaction | A complicated astronomical temporal model disappears behind meaningful sky/spatial scenes and direct manipulation. The team's interview explicitly describes quiet elegance and complexity made legible. | Let the actual place/plant photos and *recorded* calendar/history provide spatial and temporal continuity; keep complex backend hidden. | Copying iOS Liquid Glass, astronomical 3D, or faking a physical plant trajectory without observations. |
| **[Tide Guide](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/)** — **[A] Apple Design Award 2026 winner**, Visuals & Graphics | Specialized natural cycles become glanceable animated charts; palette changes with *actual* sky/daylight context. | Meaningful photographic before/after + factual event density, checked vs unchecked states, real elapsed time and dates. | Fake live humidity/soil graphs, fictional seasonal health curves or ornamental analytics. |
| **[Sago Mini Jinja's Garden](https://developer.apple.com/design/awards/)** — **[A] Apple Design Award 2026 winner**, **game** Interaction | A tiny number of comprehensible gesture-based interactions let children grow/harvest with minimal reading. | Care actions as legible custom pictograms, tactile confirmation, an entry flow a beginner can understand without botanical jargon. | Infantilizing the brand, cartoon avatars, gamifying irresponsible watering, replacing accessible buttons with undiscoverable gestures. |
| **[Art of Fauna](https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/)** — **[A] Apple Design Award 2025 winner**, **game** Inclusivity | Botanical/wildlife illustration as authored material world, multiple ways of understanding the same content, strong accessibility. | A distinctive editorial nature/architecture design vocabulary; reduced-text pathways and alternate descriptions for plant actions. | Using unlicensed wildlife illustration and equating poetic artwork with plant identification evidence. |
| **[Watch Duty](https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/)** — **[A] Apple Design Award 2025 winner**, Social Impact | Contextual, high-signal warnings with clear provenance in time-sensitive circumstances. | Attention architecture: overdue *user-selected* checks and explicitly observed concerns first; clear what is known and who observed it. | Alarmist red banners or emergency-style credibility for ordinary plant uncertainty. |
| **[Primary: News in Depth](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/)** — **[A] Apple Design Award 2026 winner**, Social Impact | Minimal UI steps out of the way of a spatially arranged, source-grounded narrative. | The *actual photographed living space* owns visual real estate; utility UI gets quieter. | Heavy VR/3D tooling without validated spatial data or need. |
| **[Structured](https://developer.apple.com/design/awards/)** — **[A] Apple Design Award 2026 finalist**, Inclusivity | Exceptionally scannable schedule including rest and downtime. | Check-ins as *user-selected reasons to look again*, not “must water now”; explicit snooze / skip / confirm later. | Productivity guilt, streak pressure, pretending to predict biology from a calendar. |
| **[Focus Friend](https://blog.google/products-and-platforms/platforms/google-play/best-apps-games-2025/)** — **[A] Google Play Best App 2025 winner** | Reduce phone engagement as a feature; charming focused ritual rather than infinite consumption. | A high-value 15-second “observe / record / leave” loop; app encourages actually visiting and touching plants rather than endless feed time. | Copying its reward mechanics or introducing an artificial pet needing attention. |
| **[100 Lost Species](https://www.awwwards.com/sites/100-lost-species)** — **[A] Awwwards Site of the Day, Oct 20 2025** | An *archival* ecological timeline is presented as an authored emotional journey of dates, imagery and loss. | Design an explicit Living Time mode: dated photos / observations / interventions / outcomes, with genuine gaps and absences. | Treating death or loss as a gimmick; transplanting an immersive showcase's scroll friction into daily care. |
| **[Kōzōwood — Made of Nature](https://www.awwwards.com/sites/kozowood-made-of-nature)** — **[A] Awwwards SOTD 2024** | Architectural material (wood) and built-place imagery guide typography, rhythm and interaction. | Nature × architecture editorial art direction for Plantupia's *commercial space* stories and public site. | Borrowing its visual identity, sound-on-default, cinematic entry time or dominant promotional motion inside utilitarian care routes. |
| **[Discover Nature Nearby](https://ifdesign.com/en/winner-ranking/project/discover-nature-nearby/535657)** — **[A] iF Talent Award project**, student category | Physical environmental discovery feeds a shared ecological database and encourages local learning. | An observation becomes a piece of structured knowledge; optional community outcomes enhance future questions. | Conflating student-concept jury recognition with a shipped production app or a commercial iF Design Award win. |
| **[Ranger Buddies Web Application](https://ifdesign.com/en/winner-ranking/project/ranger-buddies-web-application-rbwa/575183)** — **[A] iF award archive project** | Meaningful real-world exploration missions backed by conservation education. | Tiny optional grounded “go look for actual clues in your plant/space” prompts rather than passive AI answers. | Generic badges, XP or conservation claims unsupported by measured outcomes. |
| **[Periodic Table of Elements](https://ifdesign.com/en/winner-ranking/project/periodic-table-of-elements/259038)** — **[A] iF Gold archive reference**, 2018 launch | One complex knowledge source reconfigures into different views for novices and experts without split underlying truth. | Owner, shared carer, trained professional (if verified) see the *same plant*, with different actions/level of detail. | Professional UI access before company verifies staff/site entitlement. |
| **[Wetland Restoration Toolkit](https://ifdesign.com/en/winner-ranking/project/wetland-restoration-toolkit/775306)** — **[A] iF Talent/social-impact archive** | Combines a physical kit, knowledgeable humans, service processes and digital records. | Separate the physical act of checking soil/placement from the digital proof/next-question loop. | Claiming Plantupia supplies a kit, expert visits, or service guarantees. |

**Creative finding:** Apple's 2026 winner Moonlitt was produced by a three-person team according to its official case study. Scope and craft matter more than looking busy; a mature Nova engine means our opportunity is *cross-domain integration*, not endless modules.

## 2 — Non-award functional precedents: what each owns and cannot solve for us

| Cross-domain reference | Observed mechanism / evidence | Plantupia opportunity |
| --- | --- | --- |
| [Planta](https://getplanta.com/) and [Greg](https://greg.app/) | Consumer plant inventory, observation and care reminders/community; useful category baseline [O] | Keep useful reminder/recording affordances; **differentiate through placed-life continuity, photo evidence and AI → action → result**, not “we do reminders better” with no evidence. |
| [iNaturalist](https://help.inaturalist.org/en/support/solutions/articles/151000170368-which-taxa-are-included-in-the-computer-vision-suggestions-) | Computer-vision suggestions rest on prior observations; community-confirmed identifications matter; not every organism is classifiable [O] | Separate “suggested species” / “owner-confirmed species” / “expert-reviewed,” record correction history; never make AI certainty a fake score. |
| [Merlin Bird ID](https://support.ebird.org/en/support/solutions/articles/48001185783-sound-id) | “Suggestion, then human compare and confirm” with concrete recordings [O] | Assistant answers as **hypothesis → what to check → user confirms what happened**; genuine user feedback is more valuable than magical one-shot diagnosis. |
| [Day One](https://dayoneapp.com/features/) | Personal journal with photos, calendar view and lower-friction entries, available for Android [O] | Living History should have photographic/indexical ways to return, not just rows; personal continuity can be emotionally rewarding with zero gamification. |
| [Are.na](https://help.are.na/docs/guides/handling-blocks-with-care) | Image, text, PDF or link as knowledge “block”, grouped into channels [O] | Public “knowledge from a real plant question” is a distinguishable object, not just a social post; link real follow-up without leaking private plant metadata. |
| [ArcGIS Field Maps](https://www.esri.com/arcgis-blog/products/field-maps/field-mobility/whats-new-in-arcgis-field-maps-june-2026) | Professional place-linked asset forms and photo attachments, offline-capable route for field data [O] | Later B1 site/room/task proof for Plantupia installations *only after* confirmed process and access model. |
| [Google Arts & Culture sustainability](https://artsandculture.google.com/project/sustainability) | Narrative environmental views: species atlas, changing glaciers, ecological visuals [O] | Public site/editorial case studies could interpret *verified* impact and documented time; never use simulated carbon metrics as company achievement. |
| [iF Design's nature-system projects](https://ifdesign.com/en/winner-ranking/project/discover-nature-nearby/535657) | Education, citizen observations and human-expert information layers [O/A] | Community answers gain value only when a result returns; design trust around **author / evidence / status / later check-in**. |

**Not a claim:** No evidence says these apps necessarily have worse all-around features or that Plantupia already beats them. We *do* have unusual reusable infrastructure across social/media/care; differentiation remains a design and user-validation hypothesis.

## 3 — User evidence: plant owners do not want a machine to boss them around

Original community threads, directional only; self-selected forum posts are not a statistical sample:
- [“Plant app that learns my plants?” (Feb 2025)](https://www.reddit.com/r/houseplants/comments/1iwfxq6): person wants logged actual watering + context to affect future suggestions rather than a static prescription [C].
- [“Smart Schedule” same 16 days across different plants (Mar 2025)](https://www.reddit.com/r/houseplants/comments/1j2jr6a): skepticism of generic scheduling [C].
- [“170 plants in 13 rooms” (Sep 2025)](https://www.reddit.com/r/houseplants/comments/1nmmpex/is_anyone_using_a_plant_app_on_their_phone_and/): extreme collection makes room organization and reminders valuable [C].
- [Plant-collection maps vs twenty lists (Mar 2025)](https://www.reddit.com/r/houseplants/comments/1jfai0q): desire to navigate spatial groups not a flat inventory [C].
- [Debate: a fixed *checking* routine can work while identical watering rules cannot (May 2025)](https://www.reddit.com/r/houseplants/comments/1knru7d/removed/): important opposing practitioner perspectives [C].
- [Concern about plant AI/ID trust (2024)](https://www.reddit.com/r/houseplants/comments/1ho2pk7): anecdotal preference for human confirmation [C].

Research question reframe: **“What's worth checking, not what does the algorithm order me to do?”** A calendar is an invitation to observe, with the human action recorded separately. Context from human observation matters; a skipped recommendation is informative, not failure.

## 4 — Design-material deconstruction (not moodboarding for its own sake)

**Photos:** Use actual user- or company-authorized material, with explicit private/public boundary. Prefer:
- one real space/place crop with natural ambient light, allowed empty / no-photo state;
- a plant identity close crop paired with *its* place context, not an AI-crafted disconnected generic species glamour shot;
- true date and actor adjacent to media; before/after only when two actual dated photos are available;
- media viewer transitions preserve exact image identity between thumbnail and detail.

**Typography:** Working Plantupia 2026 brand guidance uses Playfair Display for headlines, Inter 400–600 for UI text, Deep Green `#123B2E`, Cream `#F3EEDE`, Sage `#9FB79A`, Muted Sage `#7E9C87`, Forest `#16302A`. These are verified against available design guidelines, but do not extract/redistribute font files from internal PDFs. Official wordmark/vector delivery and license are separate requirements. The app needs **editorial quiet + operational clarity**, not every paragraph in display serif.

**Material/form:** Natural imperfection, useful whitespace, quiet hairlines, restrained green/cream contrast. Refrain from over-rounded uniform cards in every module and from generic AI-generated plastic plant imagery. Care icon shapes must meaningfully show soil, water, trimming, placement etc, not copied emojis.

**Motion grammar:**
1. *Place → Plant*: actual thumbnail expands with a logical shared-element transition. **Android source:** [Compose Shared Elements](https://developer.android.com/develop/ui/compose/animation/shared-elements). Test interrupted/back gestures and image loading before admission.
2. *Picture → Record*: small confirmation frame / quiet tactile confirmation; no mandatory 3D visual.
3. *Care → Check-in*: pending becomes recorded fact; outcome links to historical event; do not pop confetti for maintenance.
4. *Private → Circle*: explicit full content preview and consent, no invisible or irreversible smart sharing.
5. *Circle → Return*: an answered question leads home to documenting the actual outcome.
6. *Video/Stories*: retain optimized Nova Media3 player lifecycle; don't cover playback with decorative effects.
7. Use native Compose interaction/accessibility, including >=48dp targets; do not copy iOS-only Liquid Glass. See [Android accessibility API defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults).

**Reward loop:** The real reward is *seeing actual change* and getting better at care, not a streak, plant mood score, rewards currency or compulsive daily login.

## 5 — Reconstruct the product from zero: five rival conceptual worlds [H]

These are **competing interactive briefs**, not five features to build.

### WORLD A — “The Living Atlas” / Place-first
**Thesis:** You visit a place, not a database. A real photographed Home / office has visible zones, planting units and human responsibilities. A contextual zoom/crop exposes relevant plants. **Task:** Can a user with 7 or 100 plants navigate rooms and find one unit faster than with a grid? **Build slice:** alternative Space navigation with real media; no auto-generated floor plan or fake map. **Failure:** too many taps for one household plant; amateur plan sketch implies professional surveyed accuracy.

### WORLD B — “Field Notes” / Evidence-first
**Thesis:** Taking a photo and noting what you *actually saw* should feel like preserving a small artifact. Dated images, care, questions, and outcomes accumulate into a legible living record. **Task:** On a 360dp phone, can user save a private care observation in 15–25 seconds and later find the outcome? **Build slice:** image + icon-led moment editor, re-photograph from similar frame, before/after backed by real originals. **Failure:** ornamental scrapbook blocks efficient routine.

### WORLD C — “Quiet Care” / Attention-first
**Thesis:** Open the app for 20 seconds, get the one thing worth checking, return to the plant physically. Notifications are chosen check-in prompts, never fictional moisture intelligence. **Task:** one glance explains “what do I need to look at, and why?” with genuine data. **Build slice:** precise Today decision stack, snooze/no-change and one-tap record with real confidence semantics. **Failure:** too much logic slips into unsupported biological predictions.

### WORLD D — “The Living Inquiry” / AI as field partner
**Thesis:** Human observation → ask → AI suggests *questions/tests* → human checks → own history records the result. Public community can help, with explicit redaction and consent, no private data auto-export. **Task:** user notices yellow leaves; does the assistant ask about wet/dry soil, light, airflow and timeline before prescribing? **Build slice:** multi-turn with bounded consented context; show evidence and cite sources when real; proposed action is **not** a database write. **Failure:** model hallucination, cost/performance, privacy and anthropomorphism. **No live-model claim without QA.**

### WORLD E — “Situated Knowledge Commons” / Place × society
**Thesis:** Nova's special asset is genuine people, posts, messaging and media. Most plant advice exists in unverified posts; Plantupia could connect a question and the later observed result, so answers get reality checks. **Task:** can users find a relatable solved question without seeing someone's private home/site/plant history? **Build slice:** Circle question → answer → optional private return → selected public learnings if approved. **Failure:** low engagement, spam, moderation, leaking house/workplace through images.

**Recommended exploration combination, NOT sign-off:** A (place and spatial identity) + B (dated evidence) forms the **core experience**; C (quiet attention) is the daily entry behavior; D (real AI) and E (Nova community) are *assistance when needed*, not mandatory home content. This is an architecture of meaning, not a proposal to add five more tabs.

## 6 — Specific *disconfirming* research tests before implementation

| Prototype challenge | Stimulus | What would disprove our favorite idea? | Evidence to collect |
| --- | --- | --- | --- |
| A/B/C main navigation | 1st launch; record care; Story; locate pending check; DM | Photo-heavy Home or Care tab delays the fastest common task | first tap, completion time, erroneous route, backtracking |
| Real empty/no photo | 0 spaces, 1 plant, 7 plants, 100+ office units | Composition only looks great with editorial stock photos | genuine no-image state, density and performance |
| Photo privacy | public question with user's actual private home photograph | consent text is not understood; disallowed location is visible | preview comprehension and server EXIF + object ACL audit |
| AI in uncertainty | yellowing plant with species unknown and conflicting observations | model invents assured pathogen/watering remedy or live sensor readings | structured prompt evaluation, uncertainty/source trace and decline cases |
| Temporal archive | 50 dated events, two authentic photographs 14 months apart | beautiful scrollytelling makes finding one event slower | photo indexing speed, scroll position, accessibility |
| Recurrence and agency | user skips a reminder but still records a soil check | UI pressures watering, shames skipped actions or lies about “overdue health” | calm notification copy and skip/review recovery |
| Shared owner/guest | user with view-only access sees a friend's space | camera/AI/public post can leak a private unit or edit it | two-account role tests, revoked permission, media URLs |
| Real brand | Playfair/Inter, actual logo/vector, real plant/photo | generic green app feel survives even with right colors | screenshot/voice/component critique on device |
| Android media reuse | Story, Reel, DM, keyboard, offline, suspend/resume | Nova original player/realtime has intermittent black-frame or keyboard issues | real Media3 playback, profile/traces, crash report |

## 7 — Execution backlog **from research**, not "features = tickets"

**P0: prove:** real isolated QA backend, true AI source/consent/error/limits, 2-account privacy, native journeys, image quality and robust media; no production mutation.
**P1: compare:** 3 non-portable *design treatments* using the same data and routes:
- `LIVING_ATLAS`: photo-led place navigation without fake floor plan;
- `FIELD_NOTES`: tactile photograph + dated moment + outcome;
- `QUIET_CARE`: sparse attention with a selected next review.
These are design experiments first, not code changes.
**P1: system polish:** bespoke 6 plant-care glyphs, consistent photographic ratio, restrained hero, native shared-element transition after performance test, clear LTR English while respecting authored mixed-language text, official typography/logo assets subject to rights.
**P2: later:** scene/room spatial structure, saved “then/now” alignment guidance, richer editorial Circle content retrieval, reviewed botanical knowledge corpus, optional contextual multimodal AI.
**B1 dependent on company confirmation:** verified installation/maintenance flow, staff roles, support status, project/public website with approved architectural photography.
**Explicit exclusion:** fictional plant IoT, sensor readings, automatic watering, invented carbon savings, copied animations/images, protected-client information.

## 8 — Next discovery passes that may overturn this one

- **Pass 05: Gallery-grade teardown**: inspect videos/screens of winning UI and draw per-screen behavioral maps, not a Pinterest moodboard. Score navigation/feedback/photographic density/copy/motion against the current real Plantupia APK.
- **Pass 06: Field ethnography & low-cost user testing**: household 1/7/30 plants and one *authorized* commercial caretaker (if available), real observed work; photo permissions.
- **Pass 07: High-fidelity challenge prototypes**: 3 incompatible worlds rendered with real or clearly labeled non-client imagery, interactive native semantics, same task paths; screen-to-screen comparison with old Nova components.
- **Pass 08: Source recheck after QA**: revise the principles; if “place-first” isn't faster or meaningful, remove it as primary nav. The research law allows rejecting a beloved thesis.

**Carryover:** Keep the primary app and original Nova engine stable while researching. No implicit decision to change bottom bar, save data publicly, acquire sensors or replace the app's Play package. Research must produce questions that could surprise us—not only evidence that congratulates what we've already made.
