# Plantupia — Screen & Flow Atlas / V0

**Date:** 2026-10-12  
**Status:** PROPOSED IA + SCREEN INVENTORY, **not** a locked UI or a promise to ship.  
**Read alongside:** `MASTER_CAPABILITY_ATLAS_V0_2026-10-12.md`, `docs/WORKING_LAW.md`, Nova PR #240 / `docs/PLANTUPIA_PRODUCT_CONVERSION.md`.

## 0. Experience principles

- **Context first:** plant, place, conditions, care owner, and evidence always determine what is relevant.
- **Trajectory, not a green health number:** meaningful change and observed result over speculative health-score widgets.
- **Memory, not generic reminders:** observation → intervention → waiting → observed consequence.
- **Privacy by default:** a private care note is not a post; sharing includes an explicit preview.
- **Intelligence must disclose source and uncertainty:** human report ≠ measurement ≠ machine inference.
- **One plant is not one space:** support a person's 2–7 plants, and a commercial installation with 100+ units and zone/group organization.
- **Use familiar native controls where appropriate; invest visual authorship in spatial identity, living time and before/after continuity.**
- **No fake site photos, sensor data, clients, conversations, success messages or live appointments.**

## 1. Actors / interfaces

**Consumer:** self-service space + plant + contextual care + optional Circle. No requirement to be a Plantupia customer.  
**Plantupia client / facility contact:** own authorized installed spaces; shared view, care boundaries and service visibility *only once confirmed*.  
**Carer/family member:** limited role in a space; record care when authorized, private by default.  
**Plantupia technician/manager:** separate role-aware service UI (likely mobile-first for field); **gated on actual company operations**.  
**Public visitor/architect/specifier:** the separate creative website and case studies; no login needed to browse.  
**System admin/editor/moderator:** limited Django Admin initially, domain-specific console only if necessary.

## 2. Navigation hypotheses (do not implement until visual/experience pass)

Consumer Android IA candidate:
```
YOUR SPACE (home and actual plants)
  ├─ space switcher, zones (when useful), living timeline
  ├─ plant identity + profile + physical context
  ├─ record observation / care / issue (contextual create)
  └─ check-ins, comparisons and history
CARE / ATTENTION (consolidated, test whether primary)
  ├─ due human check-ins
  ├─ optional care tasks (later)
  └─ issues that need review
ASK (contextual entry on plant, and general entry)
  ├─ plant-specific AI care companion
  └─ escalate to human / public Circle with consent
CIRCLE (separate public environment)
  ├─ contextual questions, answers, useful outcomes
  └─ secondary people/media experiences if product-approved
ME (account and private settings)
```
This might become **four bottom intents** (Spaces, Care, Circle, Me) plus *Ask* as a strong contextual action; alternatively a five-tab model may test better. No automatic green-themed Nova navigation transplant. *Create* should be available in relevant contexts, not necessarily an always-prominent social composer.

## 3. Detailed Android screen inventory

Phase: **C0** demonstrable complete core / **C1** fuller consumer product / **B1** verified business customer/operations / **OPTION** only after research.

| ID | Surface / screen or state | Core user job & required behavior | Phase |
|---|---|---|---|
| E01 | Splash/session gate | restore actual auth or explain expired session | C0 |
| E02 | Welcome/intro | state real promise; do not require company installation | C0 |
| E03 | Login | sign in and handle wrong credentials, loading, retry | C0 |
| E04 | Signup | new user and verification requirements as actually supported | C0 |
| E05 | Password recovery | complete existing recovery flow; don't fake sent emails | C0 |
| E06 | First choice / initial context | “my plants” vs “my Plantupia space” if business-approved | B1 |
| E07 | Consent/perms sheet | camera/notifications only at actual point of use | C0/C1 |
| E08 | First-empty-home | a clear non-judgmental path to add first space/plant | C0 |
| S01 | Living Home | relevant private spaces, recent real change, next check-in | C0 |
| S02 | Space switcher/list | select real space across home/work | C0 |
| S03 | Create space | name and optional location/context, no serial | C0 |
| S04 | Space detail | living identity, image if real, summary, plants/groups | C0 |
| S05 | Plants in space | readable inventory; pagination/search/filters | C0 |
| S06 | Space settings | name, privacy, editing/archiving and member roles | C1 |
| S07 | Zones in a space | named physical regions; support many plants | C1/B1 |
| S08 | Space context | directional light, HVAC, drainage/access observations | C1 |
| S09 | Shared access | invite/withdraw helper with explicit rights | C1 |
| P01 | Add plant | native photo capture/import, own label, optional species | C0 |
| P02 | Plant profile | photo, personal name, species certainty, place, recent activity | C0 |
| P03 | Rename plant | private nickname vs physical installation label | C0 |
| P04 | Species identification | ranked suggestions and explicit human confirmation | C1 |
| P05 | Plant care profile | licensed/source-linked species guide with environmental caveats | C1 |
| P06 | Edit plant/placement | move plant; preserve event and identity history | C1 |
| P07 | Retire/replace | distinguish old living plant from persistent site/planter | B1 |
| C01 | Quick care composer | select actual watering/soil/pruning/feeding/moving, with notes | C0 |
| C02 | Observation composer | describe/photo only the thing seen; no automatic diagnosis | C0 |
| C03 | Concern/issue composer | symptom, real photo, situation, possible human escalation | C0 |
| C04 | Photo capture/review | actual file, upload state, crop/compress/privacy | C0 |
| C05 | Check-in choice | optional review 7/14 days; **not** assumed watering need | C0 |
| C06 | Care/attention summary | real pending follow-ups across plants | C0 |
| C07 | Follow-up detail | original note + date + plant and actual context | C0 |
| C08 | Follow-up outcome | user confirms observed result; close only once | C0 |
| C09 | Living history | chronological notes/actions/issues/outcomes, fetch older events | C0 |
| C10 | Photo comparison | two real dated images, no inferred growth claims | C0 |
| C11 | Care plan | user-managed tasks; due/postpone/skipped/completed | C1 |
| C12 | Reminder controls | opt-in native/local/push delivery backed by real settings | C1 |
| C13 | How-to guide | short, source-reviewed lesson linked to context | C1 |
| C14 | History filters | browse care vs observations vs issues | C1 |
| C15 | Vacation/delegation | assign responsibility and track what someone actually did | C1 |
| AI01 | Assistant entry | know whether ask is general or tied to plant ID | C0 |
| AI02 | Plant contextual chat | user question + only authorized plant facts, never invent sensor values | C0 |
| AI03 | Source/uncertainty details | clear general advice vs retrieved evidence vs observed data | C0 |
| AI04 | Questions to clarify | soil, lighting, drainage, prior intervention; avoid immediate diagnosis | C0 |
| AI05 | Suggested follow-up | user-directed observation checklist; no write without confirmation | C0 |
| AI06 | Assistant session/history | storage/expiry/delete/feedback; consented logs | C1 |
| AI07 | Photo-assisted questions | secure image submission, alternative hypotheses and limits | C1 |
| AI08 | Specialized species results | candidate ranking and user confirmation | C1 |
| AI09 | Escalate to person / Circle | selective export with privacy preview | C1/B1 |
| M01 | Circle index | public opt-in plant questions, not all private care | C0 |
| M02 | Question compose | separate public copy + topic + optional safe photo | C0 |
| M03 | Publish privacy preview | show exact public data before submission | C0 |
| M04 | Discussion detail | comments, moderation, attribution, useful replies | C0/C1 |
| M05 | Follow-up on answer | document what happened after advice privately | C0 |
| M06 | Report/block | functioning moderation and abuse controls | C1 |
| M07 | Circle search/discovery | topics and relevance beyond empty endless feed | C1 |
| M08 | People/inbox | inherit only where useful/approved; protect private space links | OPTION |
| U01 | My profile | own public identity separate from private spaces | C0 |
| U02 | Privacy overview | who can see every relevant surface | C0 |
| U03 | Preferences | language, notifications, sensory/motion settings | C1 |
| U04 | Manage shared space | member invite, roles, revoke, activity | C1 |
| U05 | Help/feedback | support, report inaccurate advice, contact paths | C0 |
| U06 | Data/account control | data export/delete, consent history, legal | C1 |
| B01 | My Plantupia installations | authorized client sites and installation states | B1 |
| B02 | Site handover record | what installed, date, approved original photos and roles | B1 |
| B03 | Client request for help | issue linked to real site/unit, no promised SLA unless agreed | B1 |
| B04 | Service progress/history | only company-supported visits/notes/statuses | B1 |
| B05 | Field worker sites | assigned sites and authorization | B1 |
| B06 | Maintenance visit | task/route/context, field photo, minimum useful record | B1 |
| B07 | Issue/replace workflow | approve, intervene, document outcome; replacement identity | B1 |
| B08 | Visit report preview | human-reviewed accurate summary and client visibility | B1 |
| B09 | Staff offline state | draft/sync/conflict handling where field conditions require | B1 |
| B10 | Manager overview | exception-driven sites, not invented plant health dashboards | B1 |
| H01 | Connect hardware | only actual compatible sensor device; no mandatory QR | OPTION |
| H02 | Sensor plant data | measured + timestamped + offline state, not inferred | OPTION |
| H03 | Device reliability | battery, pairing, calibration, failed sync | OPTION |

**A screen is not complete merely because it renders.** Normal/empty/loading/error/offline/no-permission states, RTL, keyboard/large-text, privacy, restoration, and tested real device behavior belong to its completion contract. Adjacent actions can be sheets/dialogs instead of distinct navigation destinations: screen count is an **IA inventory**, not a mandate to create 70 routes.

## 4. Separate public website and internal surfaces

| ID | Web surface | Job and proof |
|---|---|---|
| WEB01 | Home / thesis | Plantupia spaces as lived experience, no stock-eco clichés |
| WEB02 | Work / projects index | real approved installations, by spatial intent/use |
| WEB03 | Project case detail | brief → site → authored intervention → installed evidence → change if available |
| WEB04 | Approach/solutions | biophilic design, installation and care **as verified company offerings** |
| WEB05 | About/people | factual team capabilities, genuine sources |
| WEB06 | Inquiry/RFQ | request a space intervention, constraints, consent, real confirmation |
| WEB07 | Knowledge/editorial | sourced articles and applied plant/space thinking |
| WEB08 | Support/account bridge | actual customers move from site to app where relevant |
| WEB09 | Architect/specifier resources | only if actual spec data and assets are approved |
| ADM01 | Internal site/plant roster | safe Django Admin bridge, role-scoped |
| ADM02 | Company-approved knowledge articles | version, author, references, effective period |
| ADM03 | Service operations | only after workflow validation |
| ADM04 | Assistant review | flagged replies, sample quality checks, user privacy |

## 5. Five journeys to render/prototype before production coding

### J1 — New person with 3 household plants
first open → add home → add photo/species optional → plant profile → record care → choose check-in → return → outcome. Countercheck: no purchases, QR, sensor or social feed forced.

### J2 — Someone sees yellow leaves
plant detail → “Ask about this plant” → assistant asks contextual questions before suggesting cautious checks → sources/uncertainty visible → optionally save observation/check-in (explicit authorization). Countercheck: no definitive disease or pesticide recommendation from one image.

### J3 — Office with Plantupia-installed plants
invite/activate permitted installed site → space/zone grouping → authorized client reads actual maintenance history → customer concern → professional takes responsibility → intervention/outcome. **Needs company reality interview before this can be promised.**

### J4 — Vacation/care handoff
owner delegates one space with time/role limits → carer logs a real care act → owner sees authored evidence; neither can access other private spaces. Countercheck: no inferred care just because a reminder was due.

### J5 — Public knowledge feedback
user opts into a plant question → exact publish preview → useful response → user documents observed outcome in private history → public post does not expose private space address/history.

## 6. Design proof gate

Before accepting IA/visual direction:
1. Source and evidence pass for content, imagery and product reality.
2. Paper/low-fi IA with J1–J5, representative plant counts 1/7/100, and empty/error states.
3. Three *authored* design theses / UI behavior studies (not screenshots from Planta).
4. Side-by-side competitor task comparison (actual flow, friction, visual hierarchy, trust).
5. High fidelity native prototype captures in RTL + representative English.
6. Interaction validation with device, upload, back navigation, re-entry, privacy.
7. Delta pass and explicit freeze decision: accepted / hypothesis / blocked.
8. Implementation as coherent end-to-end vertical slices; green CI + field/device proof per slice.

## 7. Company questions required before B1 sign-off

Who installs and cares after handover? Which customer sites/asset lists already exist? Does Plantupia have repeat maintenance contracts? Which staff roles and client approvals? How are replacements approved? How is confidential site/location information handled? What is the company-approved brand/imagery and assistance policy? Should an app be branded Plantupia as separate Play package or update the Nova listing?

If unknown, **record UNKNOWN**. Don't invent a business rule, warranty, subscription, work order, customer roster or service assurance.

## 8. Evidence and next decisions

Public research evidence and precedent: `MASTER_CAPABILITY_ATLAS_V0_2026-10-12.md`. AI design and price assumptions: `../technical/AI_CARE_ASSISTANT_FEASIBILITY_2026-10-12.md`.

**This document is intended to be criticized.** The next phase is a product/experience audit against actual Nova PR #240 and company-confirmed reality, not an instruction to build everything in these tables.
