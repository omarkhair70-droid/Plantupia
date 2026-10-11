# PLANTUPIA — Master Product Specification v0.1

**Prepared:** 2026-10-12 · **Decision state:** WORKING PRODUCT DEFINITION / REVIEW REQUIRED  
**Owner approval:** NOT RECORDED · **Company operational validation:** INCOMPLETE  
**Scope:** Whole prospective product, organized by truth/priority; NOT an instruction to implement everything.  
**Source of truth:** [Working Law](../WORKING_LAW.md), [Product Translation](../synthesis/02-product-translation.md), [Cross-World Critique](../exploration/05-cross-world-critique.md), [Lifecycle Map](../exploration/06-project-lifecycle-map-v0.md), [Master Capability Atlas](./MASTER_CAPABILITY_ATLAS_V0_2026-10-12.md), [Screen Atlas](./SCREEN_FLOW_ATLAS_V0_2026-10-12.md); [Nova conversion PR #240](https://github.com/omarkhair-labs/nova/pull/240).

**Change from preceding atlas (user-confirmed):** Plantupia **does not currently have sensors installed in plants**. Hardware measurements, sensor pairing and telemetry are **OUT OF CURRENT PRODUCT SCOPE** and are not dependencies, planned V1 features, or claims about Plantupia's operations. Physical-object ideas remain historical research only, pending separate future proposal.

## 1. The problem we are actually solving

Plant apps often give a person disconnected species instructions, timers and feeds. An individual living plant, however, belongs to a real place, experiences real interventions, and changes on biological time. Plantupia's research points to a different opportunity: continuity between **living plant × place × responsible person × action × visible consequence**.

**Working product promise (not approved public marketing copy):**

> Know the plants that live with you, understand their context, care with more confidence, and remember what actually changed.

For *Plantupia-installed spaces*, continuity may extend backward to design/installation and forward to professional aftercare, **only if company reality validates those workflows**. No professional service entitlement may be inferred from the fact a user has an account.

### Experience laws

1. **Place before generic advice.** Species is not sufficient; position, light, drainage, seasonal change and human observation are meaningful.
2. **Evidence before confidence.** A user note is an observation, not a certified diagnosis; photos and time should be accurately attributed.
3. **Life is a trajectory.** Organize around history, interventions and delayed results — not invented health-score percentages.
4. **Care stays human.** Remove memory/documentation burden without turning a living thing into a passive gadget.
5. **Private by default.** Physical space and plant history are sensitive user context; a public Circle post is a separately authorized act.
6. **No synthetic business reality.** No fabricated installations, maintenance visits, expert availability, warranties or company rules.
7. **One complete experience before breadth.** A running APK or a green CI does not close the product.
8. **Independent identity.** Research and brand determine Plantupia UX, not the current Nova UI and navigation.

## 2. Whom this product serves

| Actor | Real job | Design consequence | Validation |
|---|---|---|---|
| **Household plant owner** | Start using the app with any existing plants; notice, act, learn, return | Zero-purchase onboarding; create a space/plant; photos and observed care; contextual help | **Primary working launch persona**; usability needs testing |
| **Plantupia customer / office or hospitality contact** | Understand permitted installed plants, report concerns, know who is responsible for aftercare | Site/zone organization, roles and support status when real | **COMPANY GATE**: customer/service operations not confirmed |
| **Shared carer / household helper** | Know which care is needed and document what was really done | Scoped membership, visible actor/timestamp, deliberate permissions | Candidate; current backend roles need end-to-end audit |
| **Plantupia employee / service technician** | Efficiently care for actual installations, leave trustworthy service evidence | Assignment and field views only after company process discovery | **COMPANY GATE**, not first consumer-release prerequisite |
| **Architect / interior designer** | Understand real Plantupia projects and initiate a fitting project | Public website, verifiable images/services/inquiry, optional specifier resources later | Separate website, real source material needed |
| **Community participant** | Seek/share experience about plants voluntarily | Contextual questions, clear disclosure, moderation, outcome learning | Candidate; existing Nova public/social machinery reused selectively |

One human can have several roles. **Do not force different people into one undifferentiated dashboard.** Keep consumer simple and client/business surfaces permission-aware.

## 3. Product boundaries: four related but distinct surfaces

**A. Consumer mobile app (current design priority).** Real personal spaces, plant records, observation/care, check-ins, contextual AI guidance, selective Circle knowledge, identity/privacy.

**B. Plantupia customer extension (conditional).** Approved installations and site hierarchy, service/handover evidence, concerns, role-aware shared view. No promises until real company process is documented.

**C. Plantupia public creative website (separate deliverable).** Architectural green integration explained through real projects, authorship, capabilities, credible inquiry, case-study evidence. It is NOT a generic app marketing template and not part of Android PR #240.

**D. Internal operations layer (conditional).** Django Admin is enough for first restricted management; staff visits/assignments, site service histories or operations software require actual workflow research. Avoid rebuilding an ERP/FSM based on category assumptions.

**Explicit exclusion:** sensor onboarding, automatic soil readings, IoT graphs, invented measurements and hardware control; no current Plantupia sensors exist. **Speculative AR/3D/specifier CAD** remains R&D outside release commitments.

## 4. Core domain and information model

These are product concepts, not claims that current Django schema implements them all:

| Concept | Meaning | Invariants |
|---|---|---|
| Account / identity | Person who signs in | Auth and session handled securely; account-specific privacy |
| Space | Real environment (e.g., home, office, lobby) | Exists without a purchased installation; has owner and explicit access rules |
| Zone/placement | Where a plant lives inside a space | Can be a simple placement note for home; structured zones only when needed |
| PlantUnit | Living individual or intentionally tracked group | Permanent internal ID; may be named without species certainty or QR |
| Alias | Personal name assigned by a person | Separate from species label and business installation label |
| Species claim | Human-verified or suggested botanical identity | Unknown is valid; candidates are not facts without confirmation |
| Observation | What a person actually noticed | Actor/time/evidence; no AI diagnosis masquerading as observation |
| Care action | What a person actually did | Dated, human authored; not evidence that plant improved |
| Follow-up | A user-chosen time to check again | Not a predicted watering interval; closes with actual observed outcome |
| Concern | An unresolved visible change needing attention | Can evolve through observations and interventions; no invented status |
| AI response | Generated explanation with scope and uncertainties | Advice ≠ evidence or expert visit; no database mutation without confirmation |
| Public discussion | Explicitly shared question/answer/outcome | Detached from private location/history unless separately consented |
| Installation / service event | Real company installation or visit | **Gated**: only represent company-confirmed records |

### Core timeline

`plant + place → observation → care/intervention → human-chosen check-back → observed outcome → retained evidence`

The same physical plant can move between positions without losing its history. A replacement plant should not inherit the biological history of its predecessor, even if a planter or installation remains.

## 5. Functional product domains: complete inventory and release policy

| Domain | **C0: coherent on-device demonstration** | **C1: credible fuller consumer product** | **B1 / conditional company layer** |
|---|---|---|---|
| Identity | Login, signup/session, recovery pathway review, profile/privacy | preferences, account control/export, accessibility hardening | scoped company/client/staff roles |
| Spaces | private create, list/switch, image if real, plant listing, empty state | edit/archive, zones, light/HVAC/soil context as HUMAN inputs, shared access | validated client sites, installation handover |
| Plants | add, photo, optional species label, alias, detail, search | correction/identification suggestions, edit/move, guide profiles, retirement | large site inventories, unit/group relations |
| Care | real action + observation/concern, media, history and dated compare | personalized manual tasks, reminders, history filters, delegation | verified staff visit, intervention, plant swap |
| Follow-up | choose date (current 7/14 option), due list, close with observed result | flexible interval, postpone, confirmation safeguards | client/technician responsibility if contracted |
| Knowledge | concise safe guidance inside AI with sources | plant library, placement help, curated guides, supported species metadata | company-approved service instructions |
| **AI Companion** | general text chat + *authorized* optional plant context; uncertainty and source labels; read-only advice | photo-assisted observations (careful), history settings, feedback and specialist API | company FAQ/support only from approved facts |
| Circle | explicit plant question, consent preview, public replies, opt-in private outcome | feed/search, moderation QA, trusted knowledge patterns | company support handoff only after service validation |
| Social/media | only justified parts of existing Nova engines | user-approved meaningful sharing | NOT a default requirement for B2B |
| Operations | **none required for self-service C0** | none required unless people/service demand | assignments, visits, notes and reporting validated by company |

**No shipping promise**: C0/C1/B1 are candidate slices, not approved dates. Some CURRENT CODE features are partial; code presence ≠ acceptance and backend on preview ≠ QA on device.

### What is already coded, based on Nova PR #240 (2026-10-12)

- Django `backend/plants/`: `Space`, `SpaceMember`, `PlantUnit`, `PlantNickname`, `PlantEvent`, `PlantDiscussion`; APIs for spaces, plants, events, nickname, questions and Circle. Account-scoped server queries.
- Android Compose: space self-creation and plant registration; private living overview and plant history; human care-action choices; observations/photos; dated follow-ups and outcomes; contextual questions and Circle panels; existing Nova authentication/social engine.
- Android QA artifacts built; branch exists in **draft PR #240**, head at audit `bf26a052c4dfe197e87bcb23a7cb1166fa659d69`. These are **engineering inputs**, not signed-off design or full end-to-end product proof.
- No working AI chat endpoint or accepted botanical knowledge corpus is present in the audited `backend/plants/urls.py` and UI sources.
- Production Play migration, brand approval, customer reality, and physical-device acceptance remain open gates. Preserve original Nova production.

## 6. AI assistant: a specific product, not a generic chat tab

**Core user job:** “I noticed this change in *my actual plant*. Help me understand what to inspect, what may be happening, and what to observe next.” A model should not simply deliver a fixed recipe.

**Entry:** from a plant profile (“Ask about this plant”), plus optional global general ask with no private context. For private context, UI shows which plant facts it may pass and requires permission. Django checks authorization server-side. No model credentials ship in Android.

**Response contract:** helpful text; explicit source class (general botanical knowledge / actual user observation / company-verified knowledge); uncertainty; follow-up questions; cautious suggestions with source links. No pretending to read moisture, sensors or exact botanical pathology. Advice can propose a user-confirmed observation/check-in, but cannot silently write a care action.

**Operational gate:** rate limiting, per-user budget caps, server-side logs with privacy/retention policy, abuse/error UX, source licensing, Arabic UX, two-account authorization test, factual/botanical evaluation with representative prompts. Text-first inexpensive hosted models; provider decision remains subject to cost/quality testing. Dedicated training and vector DB are **not** prerequisites.

**Company knowledge is different:** installation-specific instructions, services, SLA or warranties require explicit authorized company source documents. If unavailable, the assistant says so.

Reference: [AI feasibility study](../technical/AI_CARE_ASSISTANT_FEASIBILITY_2026-10-12.md).

## 7. Complete journeys required before calling C0 closed

**J1 — New household owner.** No Plantupia purchase, no serial, no sensor → signup → make `Home` → add one plant/photo → observe/record care → optionally check back → exit/reopen → real history preserved.

**J2 — Concern + assistant.** User opens a named plant → asks about a change → assistant receives only permitted context, explains uncertainties and checks → user may explicitly record an observation or plan a check-in → assistant creates nothing on its own.

**J3 — Privacy-safe sharing.** Private plant issue → preview EXACT public text/media → explicit publish to Circle → public discussion → recorded outcome stays private unless explicitly shared again.

**J4 — Multiple spaces/scale.** User switches spaces, finds a plant by name/species/placement; list remains usable for 1, 7, and 100 units without an overwhelming UI.

**J5 — Authorized shared care.** Two accounts with different scopes; viewer can't record if view-only; stranger with a plant UUID sees no data. Share roles require UX and QA closure before release.

**J6 — Company-installed site.** Separate **B1** acceptance journey, not C0 blocker: actual site → approved plant roster → real handover/service evidence → concern → responsible human intervention → outcome. Do not simulate what Plantupia's team has not confirmed.

See [Information Architecture](./INFORMATION_ARCHITECTURE_V01_2026-10-12.md) for screen structure and states.

## 8. Nonfunctional product requirements

- **Security:** strict space/plant membership; private images and events remain private; published media explicitly sanitized/authorized; tests for foreign UUID and wrong role.
- **Usability:** Arabic first-class with natural RTL/bidi; English expansion is target, not proof of existing localization. Clear labels and familiar Android patterns.
- **State coverage:** empty/loading/error/offline/retry, auth expiration, upload failure, duplicate submit and restored navigation; no fake success confirmation.
- **Performance:** read/search/scroll for 1/7/100 plants; appropriately paginated timelines; image compression/caching as needed and assessed on real devices.
- **Reliability:** real preview DB migration/storage checks, backup/restore awareness, network interruption and retry; no production mutation without explicit authorization.
- **Accessibility:** readable dynamic text, touch targets, screen reader labels, visible focus/contrast, reduced motion.
- **Biological humility:** no magic universal watering interval, unverified diagnoses, purported toxicity/medical advice without sources.
- **Editorial/brand:** original Plantupia art direction and approved real imagery; not a green reskin of Nova or a competitor.

## 9. Company facts that must be resolved (not silently designed around)

| ID | Decision/question | Why blocking | Current treatment |
|---|---|---|---|
| C-01 | Are customers given an app and what can they actually see? | Determines B1 experience and visibility | UNKNOWN / require founder confirmation |
| C-02 | Who maintains installed plants and how are issues routed? | Determines care ownership and requests | UNKNOWN |
| C-03 | Are existing sites inventoried, and do source photos have rights? | Enables truthful Plantupia client data | UNKNOWN |
| C-04 | What services are actually sold, with which boundaries? | Prevents invented company claims/support | UNKNOWN |
| C-05 | Who may publish sites/photos and what must be private? | Client privacy / permissions | UNKNOWN |
| C-06 | Does the company expect distinct iOS and Android deliverables? | Architecture/distribution strategy | Clarify and record; current PR is Android only |
| C-07 | Should Plantupia have an independent app package/store identity? | Critical release/Play continuity decision | NOT DECIDED; existing Nova package must not change by surprise |
| C-08 | Which official logo/type/photo assets are approved? | Art direction and public distribution | Requires approvals |
| C-09 | Does Plantupia have any sensor-installed plants? | Would change the product architecture | **USER ANSWER: NO. Sensors removed from current scope.** |

## 10. The next design gate (and why code waits)

1. Review **Product Spec + IA** as a coherent whole; select consumer vs customer priority and whether Circle belongs in main navigation.
2. Run three realistic scenarios and identify screen/state gaps, without faking a company installation.
3. Sketch low-fi all primary views and critical error/empty states. Compare competitor **behaviors**, not brand skin.
4. Develop Plantupia-specific visual/interaction grammar from living context and time; render for Arabic Android screen sizes.
5. Compare existing Nova PR with accepted experience. Reuse backend/auth/media where appropriate; replace UI if legacy navigation conflicts. Then decide Kotlin Compose vs new client framework with evidence, not sunk cost.
6. Implement/verify end-to-end slices and capture device proof, then hold a formal acceptance review.

**Freeze status today:** **NOT FROZEN**. These documents create a single reviewable baseline; they do not authorize a Play release, a production migration, changing Nova's package ID, or implementing speculative company operations.

---

**Working maxim:** *The workflow repeats. The answer must not.*  
Source follows reality; concept selects technology; a build is not the product.
