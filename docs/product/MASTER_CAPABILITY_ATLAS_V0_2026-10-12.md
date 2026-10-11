# Plantupia — Master Capability Atlas / V0

**Date:** 2026-10-12  
**Status:** PROPOSED FEATURE UNIVERSE — NOT SIGNED OFF; not a promise to ship everything.  
**Reality correction (2026-10-12):** Plantupia has **no sensors in its plants** (user confirmed). All sensor, telemetry, pairing and smart-device controls are excluded from the current product, V1 and active roadmap. Past Living Object/IoT research is historical exploration only, not a company capability.

**Basis:** the active Plantupia research branch (Working Law, Source Atlases, Meaning Extraction, Product Translation, Cross-World Critique, Lifecycle Map); the post-research Nova conversion branch PR #240; public competitor documentation reviewed on 2026-10-12.

> Purpose: make the *whole product* legible before coding more features. Preserve the difference between known company reality, verified competitor behavior, implemented code, product hypotheses and future exploration.

## 0 — Scope law

**Working thesis, not final company-approved copy:** Plantupia connects people, plants and places through a persistent living identity and meaningful continuity: context → observation → care → change → consequence. An installed living system should retain its design/installation context across its life rather than becoming a photo album or a generic reminders app.

Two near-term outputs must not be confused:
- **Android client app:** personal plant owners AND eligible clients of Plantupia installations, with a shared living-context and care model; consumer use must not require serials.
- **Public creative website:** real architectural work, built projects, capabilities, inquiry and company credibility; separate surface and acceptance gates.
- **Professional/operations surface:** a role-specific layer only when actual company workflow and service responsibility have been verified. Django Admin can be a limited V1 bridge, not a claim of a finished operations platform.
- **Physical product / sensors / architect tools:** researched candidate worlds, **not** commitments or Android V1 dependencies.

Project constraints: research is revisable; source/truth classes are kept explicit; reference patterns can be reused but not proprietary code/assets or a competitor's identity; no fake customer/site/biological data; do not expose private company records in public Git.

## 1 — Status / priority vocabulary

- **CODE**: source present in Nova PR #240; **not** equal to E2E proven or design approved.
- **DISCOVERY**: researched hypothesis or industry precedent; company-specific implementation not approved.
- **NEW**: proposed scope requiring product/design/engineering validation.
- **GATED**: cannot promise or activate before company facts, licensed source material, or a real integration exist.
- **C0**: coherent demonstrable consumer foundation + safety, with selected AI read-only assistant.
- **C1**: fuller care product and retention loop before public consumer release.
- **B1**: basic *confirmed* Plantupia client installation/service lifecycle.
- **R&D**: optional future business/technical experiments, not part of first delivery.

## 2 — Complete capability universe

| ID | Domain | Candidate features (feature-level, not implementation sign-off) | Status | Target |
|---|---|---|---|---|
| A01–A05 | Identity | register/login; recover session; personal profile; language/RTL; account deletion/data export | CODE partial for existing Nova identity; else audit | C0–C1 |
| A06–A08 | Privacy | public/private separation; per-space roles; consented media sharing | CODE partial; must test | C0 |
| A09–A11 | Settings | notification preferences; personalization; accessibility/reduced motion | NEW / Nova reuse review | C1 |
| S01–S05 | Living spaces | create/edit/archive a private space; home/office context; multiple spaces; space hero photo; per-space summary | CODE partial; NEW edit/archive | C0–C1 |
| S06–S10 | Spatial organization | zones/rooms; placement within zones; light/HVAC exposure; purpose/design intent; site media | DISCOVERY | C1 / B1 |
| S11–S13 | Collaboration | invite a helper; shared carer/viewer roles; responsibility/handover | CODE roles backend partial; NEW UX | C1 / B1 |
| P01–P06 | Plant identity | create plant without scanner; photo; common name; species as verified/unknown; personal nickname; grouped installation | CODE partial | C0 |
| P07–P11 | Plant identity | photo species suggestion; confidence + user correction; edit/move; retirement/replacement; biological individual vs persistent planter | NEW; identification API candidate | C1 / B1 |
| P12–P15 | Plant context | container/size; substrate/drainage; window/light; human-observed temperature/humidity | NEW, no fake sensor values | C1 |
| C01–C06 | Care actions | watered; inspected soil; pruned; repotted; fertilized; moved | CODE as self-reported note choices | C0 |
| C07–C12 | Care evidence | note; dated photo; observation/concern; timestamp and actor; history; real before/after | CODE partial | C0 |
| C13–C16 | Check-in loop | opt-in 7/14-day follow-up; due list; outcome; persistence | CODE partial on PR #240 | C0 |
| C17–C20 | Care planning | individual tasks; user-controlled recurring reminders; postpone/skip; absence/vacation delegation | NEW; do not conflate fixed timer and actual plant need | C1 |
| C21–C25 | Understanding | beginner how-to; plant care profile; species context; light placement help; symptom triage | NEW, reputable sourced content | C1 |
| C26–C29 | Plant history | filter by events; visible changes/trajectory; photo compare; human confirmed recovery/replacement outcomes | CODE photo history partial; more NEW | C0–C1 |
| AI01–AI04 | AI assistant | text chat; launch within plant context; Arabic/Egyptian Arabic + English; read-only question/answer with uncertainty | NEW technically feasible | C0 |
| AI05–AI09 | AI assistant | opt-in plant history retrieval; approved botanical sources; structured suggested checks; cited grounds; feedback/report | NEW | C0–C1 |
| AI10–AI14 | AI assistant | optional photo analysis; species candidates via specialized API; conversation history/erase; moderated escalation; explicit confirmation before any database write | NEW / GATED | C1 |
| AI15–AI17 | Company AI | specific Plantupia FAQ; installation/service answers; access-controlled commercial details | GATED on approved verified materials and service rules | B1 |
| D01–D04 | Discovery | species browse/search; common questions; care guides; bookmarking | NEW | C1 |
| D05–D07 | Discovery | pet/child toxicity flags from licensed sources; plant/room suitability; beginner-friendly collections | NEW and source-required | C1 |
| O01–O05 | Issues & support | open concern; document visible symptoms; link relevant interventions; record outcome; optional peer help | CODE partial | C0–C1 |
| O06–O09 | Issues & support | expert handoff; paid service request; escalation status; staff resolution evidence | GATED on business operation | B1 |
| M01–M05 | Circle/community | consented public question; preview/redaction; discussion; comments; resolve to private outcome | CODE partial through Nova | C0–C1 |
| M06–M10 | Circle/community | topic search; useful-answer curation; user reports/blocking; moderation; people/profile context | Some Nova inherited; product UX NEW | C1 |
| M11–M14 | Social media | public plant story; short video; messaging; user follow graph | Nova engine retained ≠ approved Plantupia main-tab features | OPTIONAL |
| B01–B05 | Client installations | site record; actual installed zones; delivered inventory; handover; permitted client view | GATED: confirm real Plantupia process/assets | B1 |
| B06–B11 | Professional care | staff roles; assigned sites; visit checklist; brief field observations; offline notes/sync; report signoff | GATED, One Big Green proves category not Plantupia need | B1 |
| B12–B16 | Operations | client-visible maintenance history; issues/escalation; plant swap; service evidence; care responsibilities | GATED | B1 |
| B17–B21 | Commercial | services/plans; warranty rules; billing/payment; SLA; renewal/subscription | GATED, no invented entitlements | LATER |
| W01–W06 | Public website | authored Home; projects/case studies with real photos; service/solution pages; company story; enquiry/RFQ; contact/legal | SEPARATE web output, not built by Nova PR | WEB |
| W07–W10 | Website R&D | space-photo visualizer; product/plant-selection guidance; specifier kit; BIM/CAD support | R&D; asset and company gate | LATER |
| EXCLUDED | IoT / Smart hardware | Plantupia has no plant sensors; no pairing, telemetry, automatic soil readings or device management in this app or active roadmap | User-confirmed exclusion | OUT OF SCOPE |
| X01–X06 | Platform | authenticated API; scoped media; role-based access; rate limiting; observability; backup/restore | Nova infrastructure exists, verify Plantupia-specific correctness | C0–B1 |
| X07–X12 | Platform | offline/retry/queued photo; image optimization; RTL/accessibility; delete cascade; data retention; release/legal | PARTIAL / audit required | C1 |
| X13–X16 | Business analytics | aggregate engagement, issue outcomes, real service activity, feedback trends | GATED; never invent health score | LATER |

**Catalog rule:** this is an opportunity map. C0 ≠ all of the rows. C0 release is a *small but complete and tested user journey*; every new item must pass relevance, data/source truth, technical cost, privacy, state and UX review before promotion.

## 3 — Proposed C0 complete journey

1. Register/login → create private space without QR or purchase requirement.
2. Add actual plant with name, placement, real photo; species may stay unknown.
3. Open plant, understand recorded history and what is *not* known.
4. Document a real care action/observation/issue; optionally select a later check-in.
5. Return after restart; see persisted data; record observed result.
6. Ask a contextual, read-only assistant or ask Circle with explicit privacy preview.
7. Access private profile/history; account-scoped permissions and error/offline states behave truthfully.
8. Device/E2E proof with two accounts + photo uploads + preview DB/media; UI captures for Arabic and English where implemented.

This is the **minimum credible review slice**, not proof of a complete consumer plant-care competitor to Planta, Greg, PictureThis or FYTA.

## 4 — Product design decisions still open

- Does first launch optimize for *consumer personal collection*, *existing Plantupia client installation*, or a dual entrance sharing the same living identity?
- Is human care performed by customers, Plantupia staff, or both — and with what business entitlements?
- Should Care become a primary destination or remain plant-contextual? Do not redesign navigation on inference alone.
- Is Circle a first-class product promise or an optional targeted help route?
- Is the assistant an always-present companion, a plant-specific action, or both?
- Should Plantupia be a separate app/Play identity, and if so what compatibility/migration path is intended versus Nova's existing package?
- What company source imagery/logo/fonts/service language is explicitly approved?
- How do we separate plant/species guides and confident statements from uncertain image analysis?
- What precise acceptance evidence is required before committing release scope?

## 5 — Competitor evidence used (public feature evidence only)

- Planta listing: https://play.google.com/store/apps/details?id=com.stromming.planta
- Greg listing: https://play.google.com/store/apps/details?id=greg.io.care_app_android
- PictureThis FAQ: https://www.picturethisai.com/faq
- PlantIn: https://myplantin.com/app
- FYTA app: https://fyta.de/en/pages/app-download
- One Big Green inventory: https://www.onebiggreen.com/plant-asset-and-site-inventory-management
- Naava smart green walls: https://www.naava.io/en/green-walls
- RHS growing guide: https://www.rhs.org.uk/plants/types/houseplants/growing-guide

## 6 — Source-of-truth boundaries

- Research: `docs/WORKING_LAW.md`, `docs/synthesis/02-product-translation.md`, `docs/exploration/05-cross-world-critique.md`, `docs/exploration/06-project-lifecycle-map-v0.md`.
- Current code: https://github.com/omarkhair-labs/nova/pull/240 and `docs/PLANTUPIA_PRODUCT_CONVERSION.md` on its feature branch.
- Public competitor descriptions are *marketing/product claims*, not verified screenshots of every UI or evidence of the same features in Plantupia.
- User conversation and external private company knowledge are **not** captured wholesale into this public repository.
- Do not treat this atlas as company signoff, deployment permission, app naming permission or a contract with customers.
