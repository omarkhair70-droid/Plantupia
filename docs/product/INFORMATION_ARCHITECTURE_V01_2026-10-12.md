# PLANTUPIA — Information Architecture & Screen Contracts v0.1

**Date:** 2026-10-12 · **Status:** DESIGN HYPOTHESIS / NOT APPROVED / NO CLIENT CODE MODIFIED  
**Parent contract:** [Master Product Specification v0.1](./MASTER_PRODUCT_SPEC_V01_2026-10-12.md)  
**Source inventory (broader, uncommitted):** [Capability Atlas](./MASTER_CAPABILITY_ATLAS_V0_2026-10-12.md) and [Screen Atlas](./SCREEN_FLOW_ATLAS_V0_2026-10-12.md).

This file defines **logical screens and workflows**, not pixel-accurate designs. A logical screen may become a full view, native sheet, inline mode, or dialog after interaction testing. Do **not** translate each row into a mandatory route.

## 1. IA thesis

> **Start with the living thing in its actual space; make the next useful human action obvious; preserve the result; surface knowledge only when helpful.**

A user must be able to finish an everyday task — “what needs attention / what changed / what did I do?” — without first navigating a feed, paying for hardware, or understanding expert plant terminology.

### Main spatial hierarchy

```
Account
└─ My spaces
   └─ Space (e.g. Home / Office)
      ├─ Room / Zone (optional, advanced or commercial)
      └─ Plant / tracked group
         ├─ Identity / species confidence / placement
         ├─ Observations and human care records
         ├─ Follow-ups and outcomes
         ├─ Real dated photos and comparisons
         ├─ Ask about this plant (authorized AI context)
         └─ Share a chosen question publicly (explicit opt-in)
```

Company installations are an **additional scoped relationship to the same space/plant identity**, not a required code/scanner path. Sensors are **not part of the actual Plantupia product** and no place in navigation is reserved for them.

## 2. Navigation candidates

### Candidate N1 — recommended *for prototype comparison*, not yet frozen

Four primary destinations:
- **Spaces:** the tangible places/plants and recent living changes; the default arrival.
- **Care:** due follow-ups, unresolved concerns and the next useful documented action. Not a fake “water now” alarm.
- **Circle:** voluntary public questions/experience; no private history auto-publication.
- **Me:** account, personal identity, privacy, support and settings.

A prominent **Ask** action appears inside each plant and as a reachable general assistant entry on Spaces/Care. For the general entry no plant data is included. Creating a plant, note, care act or question occurs contextually.

### Candidate N2 — challenger in low-fi tests

Four destinations: **Spaces / Assistant / Circle / Me**, with Care as a strong section on Spaces and the plant view.

**Choose N1 vs N2 by observed tasks**, not preference for “more tabs.” If people primarily open for help, N2 may reduce friction; if they open for scheduled check-ins, N1 may be better. Do not preserve Nova's tab bar merely because navigation implementation already exists.

**Inbox, Stories, Reels, social People activity** are not mandatory primary destinations. Inherited Nova capabilities require explicit Plantupia product approval and privacy/UX evaluation before promotion.

## 3. Entry/onboarding screen contracts

| ID | Logical screen/state | Goal | Necessary UI elements | Important failures/alternates | Phase |
|---|---|---|---|---|---|
| A-00 | Session launch | Resolve real saved session and route | brand/auth state, loading, retry | expired token, offline, never fake authenticated | C0 |
| A-01 | First welcome | Explain what the app is *without* implying a company installation is mandatory | concise promise, “Start with my plants”, sign in | skip decorative tutorial; no sensor promotion | C0 |
| A-02 | Login | Existing account enters safely | login + error + recovery | server unavailable, invalid credentials | C0 |
| A-03 | Signup | Allow a new account | identity fields and required policy | duplicate account, incomplete verification, recovery | C0 |
| A-04 | First plant handoff | Lead from goal to creation without form fatigue | add first plant → create/select space inline | account with no spaces; optional species unknown | C0 |
| A-05 | Context/permission moment | Ask for camera/photo access only when needed | system permissions and explanation | denial, image chooser alternatives | C0 |
| A-06 | Returning user resume | Resume at the correct meaningful context | last space/plant or attention state | missing/deleted/unauthorized plant fallback | C0 |
| A-07 | Company space linking | Attach existing Plantupia client to correct authorized site | safe invitation or approved account mapping | no public QR/serial requirement; **COMPANY GATE** | B1 |

## 4. Spaces and plant identity contracts

| ID | Logical screen/state | Goal | Core content/actions | Exit/next action | Phase |
|---|---|---|---|---|---|
| S-01 | Living Home | Feel an actually inhabited, owned space; see meaningful next thing | active space, real photo only if available, plant count, latest observation, due check-in; add/switch | open space/plant, record care, Ask | C0 |
| S-02 | Space switcher | Move between real locations | owned + permitted spaces, member role | choose space | C0 |
| S-03 | Create space | Add home/office/terrace | name required, optional description/location note; private default | new empty space with add-plant CTA | C0 |
| S-04 | Space overview | Understand what lives there | actual units, recent events, contextual placements | inspect plant or add one | C0 |
| S-05 | Plants index | Find one among 1, 7 or 100+ | search nickname/species/placement, sort, lazy load, empty filtered state | plant detail | C0 |
| S-06 | Space edit/archive | Rename/change without losing history | consented edit, archiving consequence, member effects | updated space | C1 |
| S-07 | Zones | Group by room/area for larger sites | zones, plant counts, placement | location and plant list | C1/B1 |
| S-08 | Environmental notes | Record human-observed site conditions | window/orientation/light notes, airflow, drainage, access | return to plant/space | C1 |
| S-09 | Members/permissions | Give helper safe role | invite, viewer/carer, revoke, “who can see this?” | limited shared surface | C1/B1 |
| P-01 | Add plant | Start a truthful living record | photo optional, personal name or label, species optional, placement | plant profile | C0 |
| P-02 | Plant profile | See *this* plant's actual life | image, alias, species certainty, place, recent change, clear record / Ask / history actions | care/Ask/history | C0 |
| P-03 | Rename | Personal nickname without changing biology | edit alias, label/source clearly distinguished | updated profile | C0 |
| P-04 | Edit/Move | Update placement or species identification | change context with human confirmation; retain history | updated profile with event/context | C1 |
| P-05 | Identification candidate | Suggest species without automatic certainty | candidate list, evidence/source, select “not sure” | confirmed or unknown species | C1 |
| P-06 | Plant guide | Make care guidance understandable | sourced light, water/drainage basics and context caveats | back to plant, Ask | C1 |
| P-07 | Retire/replace | End biological identity respectfully | archived timeline, replacement relation where real | new individual with new history | C1/B1 |

### S-01 home hierarchy (provisional layout order)

1. **Actual space identity** — real title/image/location note if entered; not fictional “Your plants are thriving.”
2. **Attention only when real** — due follow-up from user, open concern from user; no health score.
3. **Plants** — recognizable photo/alias and location, easy selection/search.
4. **Recent living change** — user-recorded events and image pair where available.
5. **Ask / Add** — helpful contextual next steps.
6. **Circle discovery** — opt-in and secondary, never mixed into private events.

If the user has **zero plants**, use a deliberately designed empty state: one explanation, one action, and no fake “community for you” statistics.

## 5. Care, history and help contracts

| ID | Screen/state | Main task | Key behavior | Phase |
|---|---|---|---|---|
| C-01 | Care Overview | Decide what deserves attention | user-chosen check-ins, user-recorded concerns, activity; clear “no pending” | C0 |
| C-02 | Record Action | Capture what was *done* | six current manual options (water, check soil, prune, move, feed, repot) + optional note/photo; no auto-health claim | C0 |
| C-03 | Record Observation | Capture what was *seen* | free text + real photo/time/actor; separate from action | C0 |
| C-04 | Report Concern | Identify an observed change | describe issue/photo and optional ask/help | C0 |
| C-05 | Photo Picker/Review | Retain genuine evidence safely | picker/camera, crop if required, upload progress/retry/remove/consent | C0 |
| C-06 | Choose Check-in | Revisit result when *user* decides | currently 7 / 14 days or none; not a prescribed irrigation interval | C0 |
| C-07 | Pending Check-in | Recall original event/context | plant, original event, chosen date, actual history | C0 |
| C-08 | Record Outcome | Observe what actually happened | new observation required; prevent double completion | C0 |
| C-09 | Living History | Understand chronology | event types, actor, time, photo, load older events | C0 |
| C-10 | Compare Photos | Notice visual change | only real photos with dates and user control; no fabricated progression | C0 |
| C-11 | Task/Reminder Rules | Control personal care reminders | manual preferences, pause/skip/reschedule, truthful notification delivery | C1 |
| C-12 | Shared Care Event | Understand delegated actions | real actor, timestamp, role permissions | C1 |
| C-13 | Guided Learning | Learn a plant-relevant skill | concise sourced instruction with uncertainty and safe escalation | C1 |

### No conflation

- “**I watered**” is a **past human action**.
- “**I plan to check**” is a **personal future date**.
- “**This plant needs watering**” is an **inference requiring relevant evidence**, not an existing feature.
- “**The soil is 20% moist**” is **unavailable data**: Plantupia has no plant sensors.

## 6. AI Companion experience (text-first C0 candidate)

| ID | Screen/state | Main task | Rule |
|---|---|---|---|
| AI-01 | General Ask | Ask without private plant context | no plant records automatically accessed |
| AI-02 | Ask about plant | Open contextual help from P-02 or C-04 | visible plant scope and optional consent/exclusion |
| AI-03 | Conversational answer | Explain alternatives + next observation | caveats, relevant trusted links, no strong diagnosis unsupported by evidence |
| AI-04 | Clarification mode | Ask what soil, light, pot drainage and last care *were like* | clearly distinguishes human answers from measurements |
| AI-05 | Suggested Next Step | Offer user to add observation/check-in | requires explicit confirmation; no database writes from generated text |
| AI-06 | Error/cost limit | Recover transparently when unavailable | no “assistant is thinking forever”; safe retry or manual guide |
| AI-07 | Conversation privacy | Control retention, remove history and feedback | no unapproved long-term log retention | 
| AI-08 | Photo questions | Discuss visible changes with uncertainty | **C1 only after visual quality/privacy tests**, no guaranteed pathogen ID |

Backend proposal: authenticated `/api/v1/plantupia/assistant/ask/` via Django, authorized plant retrieval, single hosted model provider, modest budget/rate caps, source labels, no key in APK. This endpoint is **NOT implemented currently**. Company service questions must say “not verified” unless approved knowledge is available.

## 7. Circle, profile and privacy contracts

| ID | Screen/state | Main task | Core constraint | Phase |
|---|---|---|---|---|
| M-01 | Circle discovery | Browse contextually useful public questions | not a copy of generic Nova feed | C0/C1 |
| M-02 | Ask community | Turn an actual concern into a public question | author selects title/body/media; no auto-pull of private site information | C0 |
| M-03 | Share Preview | Know precisely what's leaving private context | review exact public payload, confirm explicit consent | C0 |
| M-04 | Discussion | Read/react/comment safely | permissions, reporting/moderation, correct published scope | C0/C1 |
| M-05 | Answer Outcome | Return real world outcome to private life | save observed result; public repost separately authorized | C0 |
| M-06 | Moderation/report | Block/report inappropriate content | actual behavior + support pathways | C1 / safety gate |
| M-07 | Public People / inbox | Relationships/messages if valuable | strictly separate from private space identity | OPTIONAL |
| U-01 | Profile | Identity and own public output | private spaces visible only to owner/authorized parties | C0 |
| U-02 | Privacy overview | Explain data boundaries | explicit who can see plant history, photos and posts | C0 |
| U-03 | Settings | Preferences, language, notifications, accessibility | don't imply unavailable notification channels | C1 |
| U-04 | Help / feedback | Report app issue or assistant error | real destination/contact | C0 |
| U-05 | Account & data | Review/export/delete when implemented | policy, confirmation and lifecycle | C1 / release requirements |

## 8. Company/B2B extension — provisional and gated

Do not draw these as an already-enabled customer product until staff and one **real, permission-cleared** company project lifecycle have been documented.

| ID | Surface | Job | Required company fact |
|---|---|---|---|
| B-01 | My managed installations | See sites Plantupia actually manages | actual customer mapping and entitlement |
| B-02 | Site/zone/unit roster | Navigate living inventory and responsibilities | real handover labels and correct permissions |
| B-03 | Care responsibility | Distinguish client vs company work | actual maintenance/service agreement |
| B-04 | Request help | Send a real concern and know response path | approved contact/workflow and response promise |
| B-05 | Visit/service history | Read authenticated visits and observations | verified service records and photo permissions |
| B-06 | Technician worklist | See work assigned by real operation | real staff roles and process |
| B-07 | Field documentation | Capture efficient care and interventions | actual work/visit model, offline needs |
| B-08 | Plant replacement | Link failed plant to new individual | operational approvals and inventory rules |
| B-09 | Manager exceptions | Resolve real care issues by priority | real operational statuses and people |
| B-10 | Service reports | Authorize what a customer can see | actual report owner/sign-off |

## 9. Separate public website IA

**Creative rationale:** Show what Plantupia *does to physical space over time* through real spatial work; never a generic eco-tech dashboard with fabricated charts.

```
Home (spatial thesis)
├─ Projects / Work
│  └─ Project case: real site → intent → living intervention → evidence
├─ Approach / Services (confirmed offerings)
├─ Studio / Company (true people/process/values)
├─ Knowledge / Journal (careful sourced articles, optional)
├─ Start a Project / Enquiry (real response flow and privacy)
├─ Contact / Legal
└─ Existing client access to app (only if offered)
```

Recommended logical pages: **WEB-01 Home, WEB-02 Projects Index, WEB-03 Case Study, WEB-04 Approach/Services, WEB-05 About/Company, WEB-06 Enquiry/RFQ, WEB-07 Contact, WEB-08 Legal, WEB-09 Client Bridge, WEB-10 Knowledge editorial (optional).**

Production art direction requires approved brand assets, real installation photos and relevant permissions. A hypothetical photo visualizer or architect specifier tool is **not** a committed section or a substitute for showing built reality.

## 10. Journeys rendered as decision paths

### J1 — New owner with seven plants

```
Welcome → Sign up → “Add my first plant”
→ create/select Home inline → plant details (species unknown OK)
→ plant profile → Care: actual action + photo
→ choose 7/14-day check-in → close app
→ return: Care due / plant history → actual outcome saved
```

**Failure variants:** denied photo permission, interrupted upload, no internet, failed save, no species known, user with 0 plant data. Do not depend on a Plantupia purchase.

### J2 — Yellow leaves / trusted AI

```
Plant detail → Ask about this plant
→ consented context summary (plant, place, past *human* notes)
→ user question → clarifying questions → cautious suggestions + sources
→ user elects record observation/check-in → confirm save → history
```

**Failure variants:** provider outage, quota exceeded, wrong plant ownership, unknown species, no history, user excludes context, image ambiguous. No "water today" certainty from unmeasured soil.

### J3 — Private concern → public help

```
Plant profile → private concern → Ask people
→ user-authored public payload → exact preview → Publish
→ discussion → return to private plant → record observed result
```

**Failure variants:** user cancels before publishing; hidden workplace/location details; moderation and no permission; photo upload failure.

### J4 — Office installation (**B1 company gate**)

```
Verified company invitation → authorized office → zone and plant roster
→ client sees approved site/maintenance history
→ complaint linked to unit → human staff acknowledges/acts → confirmed outcome
```

**Do not fake** access invitations, assigned staff, upcoming visits, telemetry or customer names just to render this.

### J5 — Cross-account boundary

```
Owner sees Space A / viewer sees only authorized A
→ viewer may inspect but cannot mutate restricted records
→ Account B submits a known UUID not in its accessible scope
→ consistent 403/404 and NO plant image, note or event leaks
```

## 11. Core screen states to design, not just happy-path frames

| Component | Required states |
|---|---|
| Home and inventory | first-empty, loading, loaded, empty filtered results, error/retry, offline/cached when supported |
| Plant image | no photo, uploading, uploaded, failed upload, inaccessible media, removal |
| Add/edit | unsaved draft, validation, submitting, saved, duplicate tap, conflict |
| Care history | no history, one event, many events/pagination, wrong role, stale/removed plant |
| Follow-up | none, upcoming, due, outcome required, completed, already completed by another session |
| AI | general context, plant-specific consent, response, ambiguous answer, unavailable, rate-limited, no authorized plant, privacy opt-out |
| Circle | no posts, composing, exact preview, published, flagged/blocked, removed content |
| Auth/account | logged out, session resumed, expired/revoked session, offline, data deletion confirmation |
| Client installation | **not rendered as "real product" before service model is verified** |

Common UX QA across all: Arabic RTL/bidi for mixed species/IDs, 360/390/430dp Android widths as representative sizes, dynamic type, accessible targets, focus order, no motion-critical-only information, hardware keyboard/back behavior, warm/cold reopen.

## 12. Navigation and visual freeze test

Before implementing a new nav tree or screen system, deliver:
1. **Paper IA:** N1 vs N2 with J1/J2/J3, and observed step/cognitive counts.
2. **Wireflow:** full J1 and J2, including empty/loading/errors; J3 privacy gate.
3. **Three authored visual thesis explorations:** derived from Plantupia's spatial/living reality, not green Nova or copied competitor layouts.
4. **Rendered native prototype proof:** major views and states on Android in RTL, compare with real Planta/Greg/PictureThis tasks and the approved Plantupia brand.
5. **Critical review/delta:** where the visual system is generic, where real attention is hidden, whether a person trusts the data.
6. **Architecture choice:** only after product UX review decide what to reuse from Nova backend/Compose and whether an independent Flutter client would reduce *overall* cost/complexity.
7. **Frozen decision register** signed by user and (where company-specific) authorized Plantupia owner. No phantom “approved” stamps.

### Recommended first render set

`A-01, A-04, S-01(empty), S-01(populated), S-04, S-05(7 items), P-01, P-02, C-01, C-02, C-06, C-08, C-09, AI-02, AI-03, AI-06, M-02, M-03, U-02`. This is a *visual proof selection*, not a request for 19 unrelated production pages.

## 13. Current decision state

- **Confirmed by user:** Plantupia currently has **no sensors in plants**. No current-app IoT/screens/metrics.
- **Existing tested code candidate:** Nova PR #240 (not merged); Android + Django functionality documented in [Master Product Spec](./MASTER_PRODUCT_SPEC_V01_2026-10-12.md).
- **Working IA recommendation:** prototype **N1** against **N2**, do not freeze a fixed tab bar by intuition.
- **Unknown:** production-facing buyer persona priority, company maintenance rules, B2B client promise, approved imagery/service data, iOS delivery/independent package requirements.
- **Immediate next gate:** low-fi wireflows and rendered design proof, not an unsolicited code sprint.

**Status: PROPOSED / AWAITING REVIEW.**
