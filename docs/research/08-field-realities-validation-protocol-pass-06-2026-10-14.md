# PLANTUPIA / PASS 06 — Real-world Friction, Not Another Moodboard
**2026-10-14 | Usability / field-activity research protocol, not a completed field study.**

Companion sources: [Pass 04 source atlas](./06-award-winning-cross-domain-discovery-pass-04-2026-10-14.md), [Pass 05 award interaction teardown](../design/07-award-winners-behavioral-teardown-pass-05-2026-10-14.md), [Original S3 three-context test](../synthesis/03-core-stress-test.md), [Current Native Roadmap Audit](https://github.com/omarkhair-labs/nova/blob/feature/plantupia-native-experience-20261012/docs/PLANTUPIA_MASTER_ROADMAP_REFERENCE_AUDIT_2026-10-14.md).

## What this phase is, and is not
Pass 05 created research criteria and a downloadable local-interaction prototype showing three concept worlds with identical *simulated* data. Pass 06 replaces aesthetic preference with **observable work done by actual people in real places**. No participants have been recruited/interviewed, and no measured time, task score, preference, demand or company SOP is claimed in this document. Research permissions, nonpublic client media and company terms remain out of the public source repository.

## Strongest hypotheses to try to disprove
1. A photo-first **Living Atlas** helps people recover spatial context, but may slow care if no real space photograph exists.
2. **Field Notes** makes recording/returning meaningful, but may impose too much visual friction on someone documenting many plants daily.
3. **Quiet Care** best supports short household check-ins, but may hide site-wide situational awareness in an office.
4. **Plant × place × dated evidence × observed outcome** might differentiate Plantupia from a generic plant inventory; novelty alone does not prove real value.
5. Someone who only wants a basic reminder may prefer a simpler direct-to-task experience, independent of Plantupia's unique social/media stack.
6. A helper can perform care efficiently only if their permissions, role and today's plant assignment are self-evident.

## Sampling plan (recruit only with consent)
| Context | Suggested participants | Avoid | Primary truth to observe |
| --- | --- | --- | --- |
| H1: first household plant | 2–3 beginners with 1–3 actual plants | product-owning friends only | onboarding and first real photo/record |
| H2: routine household care | 2–3 users with ~7 actual plants | rehearsed steps or designer coaching | get to one room/plant, document what happened, see next review |
| H3: large mixed plant collection | 1–2 users with 30+ (or simulated fixture only for performance) | taking photos of private home without permission | inventory/search, organization, overdue/no-data states |
| B1: verified commercial Plantupia site | 1 confirmed authorized caretaker/contact **only if company approves** | fabricate employee/service protocol | sites, zones, care responsibility and record ownership |
| T1: future living physical object | paper/physical concept walkthrough, optional | implying Plantupia sells sensor products | whether physical material interaction outweighs dashboard |

Six household sessions are a proposed **small qualitative sample**, not statistically representative. If no company approval, B1 remains a hypothesis; no unauthorized on-site photography or device/network access.

## Same five tasks, three interface worlds; counterbalance order
Run the same task script with **Atlas → Field → Quiet**, **Field → Quiet → Atlas**, **Quiet → Atlas → Field**, rotating assignment to reduce order bias. Use the same synthetic names and photos in the clickable lab, not a participant's private media. Keep sessions brief and participant-controlled.

| ID | Task spoken neutrally, without naming a button | Record observable facts | Failure |
| --- | --- | --- | --- |
| T1 | “Find the Monstera that lives near the window.” | seconds, touches, false entries, first correct destination | wrong plant/room or needed intervention |
| T2 | “You touched the soil and found it damp. Record what you actually noticed.” | touches, typing, hidden vs visible save, submission comprehension | logged watering when none happened, ambiguous success |
| T3 | “Go back and find what you recorded earlier.” | retrieval time and date/source comprehension | invented inferred outcome or lost event |
| T4 | “Find the older photograph and compare only what can really be compared.” | photo index discovery and no-photo comprehension | invented second photo or automatic health score |
| T5 | “You want to ask others about yellow leaves without sharing your home details.” | preview disclosure comprehension, consent/revise/abort behavior | user thinks a private note is a public post or leaks contextual metadata |
| T6 (separate) | “A reminder came, but you haven't checked the plant.” | skip/defer action and calm system feedback | plant automatically marked watered, forced streak |
| T7 (separate) | “You have view-only rights to your friend's plant.” | actual affordance and wrong-action prevention | edit/add/public context available despite read-only role |

Do not time participants without informing them. Record *observed completion time*, not a guess based on visual mockups.

## Operational observation — focus on acts outside the phone
Ask *before* they use an interface: “Show me what you actually do before deciding a plant needs water.” Observe soil check, location, light, pot condition, routines (only with their permission). Record whether they think the app should act **before** or **after** the physical gesture. A user may validly say they want **no AI, no reminders, no social features**.

After each concept, ask: “Where did you expect that action to be?”, “What did you think would become public?”, “What would make this take less effort?”, “What seemed trustworthy versus assumed?” Avoid “Don't you like this beautiful design?”

## Logging template (fill *only* from actual consented sessions)
- Study code (pseudonym), date/context, number of plants *as voluntarily described*, authorization level.
- World order; each T1–T7 success (independent / aided / incomplete / user refuses), time if actually measured, tap/back count.
- Exact misunderstood UI phrase, unwanted disclosure, missed photo/record, silent failure.
- Participant quote *with consent* and no personal location/client/phone/photo identifiers.
- **Disconfirming observations first:** what surprised us or disproved the preferred design.
- A/B/C winner only if evidence is good enough for the target segment; preference without task completion is insufficient.

## Scenario stress: three original contexts, one domain model
1. **Cairo office** (if authorized): 100 units, floors/zones, helper role, occasional maintenance. Office contacts may need **exceptions and clear accountability** rather than a hero photo. Many units stress photo-led Atlas; no fictional installations.
2. **US household / seven plants**: the owner wants a plant's location and care history without becoming a professional grower. Quiet Care may help but must show plant inventory and preserve prior notes. Multiple time zones and owner-selected reminders require true device behavior.
3. **Future physical living object**: the object's changing material and the plant's actual response may be a more important interface than the phone. No sensors currently exist; build a sketch/concept only, not IoT UI.
4. **A first-time user with zero spaces**: no stock plants are silently assigned; create space/plant manually. Any concept whose visual promise collapses without photography must show an excellent honest empty state.

## Prioritization / kill, merge, or refine
A concept earns *more* testing only when it has plausible relevance to at least one real task and does not violate privacy/data truth. Potential outcomes:
- **Keep Atlas** for spaces and richer photo identity, but let a compact searchable list win for 100 plants.
- **Keep Field Notes** for longitudinal records, but make the quick composer one action.
- **Keep Quiet Care** for daily glanceable checking, without burying inventory or messaging.
- **Kill** animated health states, automatic diagnoses, forced progression and content-heavy editorial home if they cost task completion.
- **Delay** public knowledge features without moderation, user consent, genuine replies or outcome evidence.
- **Delay** B1 if company site/roles/service obligations remain undefined.

## Android QA and company constraints
- Implement design winners only in Kotlin/Compose after review; retain native Nova media/messaging capabilities but test inherited video/keyboard flows.
- Android Compose controls need accessible semantics and minimum 48dp touch targets (official [API defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)).
- Validate font scaling, 360/390/430dp layouts, English-first chrome with genuine RTL/Unicode user notes, bad network, unknown species and zero-photo states.
- Separate local HTML simulated actions from a **real** installed APK connected to an isolated backend.
- Need company's authorized product/package/brand media/service facts before any Production or Google Play distribution.
- Keep the previously agreed **single final owner-facing review** of the integrated QA APK; internal tests and research may occur continuously.

## Research next-step checklist (not completion marks)
- [x] Pass 04 awarded reference atlas, meanings and counterexamples.
- [x] Pass 05 case-study decomposition (official awards/interviews and design laws).
- [x] Pass 05B standalone local three-world interactive HTML and programmatic UI route smoke.
- [ ] Recruit consented households/authorized business participant.
- [ ] Observe real care at plant; collect neutral T1–T7 evidence.
- [ ] Measure real Android versus prototypes on equal fixture (not screenshots alone).
- [ ] Recheck thesis and update navigation A/B decision from test evidence.
- [ ] Get approved company/site and brand media for official art direction.
- [ ] Implement only supported refinements in native PR; run isolated Android/backend privacy QA.
