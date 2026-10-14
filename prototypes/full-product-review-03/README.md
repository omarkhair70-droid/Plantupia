# Plantupia — Full-Product Design Review 03

**Status:** INTERACTIVE DESIGN COMPARISON · **NOT** final design sign-off or implemented Android changes  
**View:** [Standalone study HTML](./index.html)  
**Review ledger:** [Full screen-by-screen Nova integration and design assessment](../../docs/design/FULL_PRODUCT_VISUAL_REVIEW_03_2026-10-12.md)  
**Source basis:** [Integrated Visual Pass 02](../nova-integrated-visual-pass-02/README.md) · [Master Product Spec](../../docs/product/MASTER_PRODUCT_SPEC_V01_2026-10-12.md) · [Nova Draft PR #240](https://github.com/omarkhair-labs/nova/pull/240)

## What changed in design (not the app)

The earlier HTML V02 had a good integrated visual starting point but over-emphasized text in parts, and implementation was prematurely going to change only the bottom navigation. This is a **full product visual review**: V02's living-space, plant, care, history, Create, Circle, moments/media, Story, Inbox, conversation, AI, public preview, profile and notifications remain accessible.

### One-click A/B comparison

**A — current Nova-like navigation:** `مساحتي / الدائرة / [+ إنشاء] / أنا`, care contextual within plant and Home. **B — user's proposed contender:** `مساحتي / ♡ الرعاية / الدائرة / أنا`, with an exposed, tappable and swipe-up **Create drawer** containing record care, add plant, public question, Story, AI assistant and video/media plus a link to the complete Create page.

The top **A/B and «ملاحظات»** bar is a **design-review affordance only**, not app chrome. Each screen's notes identify what is working and what must change before native implementation. Neither A nor B is approved. Create is never a hidden gesture with no visible control.

**No production modifications:** no Kotlin changes, merge, app store or database deployment. A temporary experiment branch was opened earlier from PR #240, but remains without design implementation.

## Testing

On local Chromium (desktop 1440×900, mobile 390×844 and 360×760) the tested route sequences ran without JavaScript exceptions:
- switch A ↔ B, inspect bottom navigation, open Care overview;
- reveal Create drawer and open add plant;
- move to Circle and Inbox;
- return to A / restore B;
- show/hide per-screen critique notes;
- navigate Home.

This browser test **does not prove** accessibility, real native gestures, backend persistence, content source accuracy, or Compose Android integration.

## Existing explicit demo boundaries

- User records use browser state; no private production data or Django writes.
- Inbox/Stories/AI/notifications are scripted/local examples, not Nova live engines and not real AI.
- Botanical artwork is **illustrated placeholder**, not Plantupia client or user photographs.
- Private care history and public publishing are separated.
- Plantupia **has no plant sensors**; no simulated IoT telemetry.
- B's Care screen aggregates demo local events; Nova PR #240 **does not contain** that new root screen.

## Next design pass before code

Critique each screen against **real current Nova APK** on a device, reject generic/text-led areas, test two navigation tasks with real users, then develop an approved Plantupia material/photographic/iconographic/interaction system. Only after reviewing the **whole connected experience** should a native Compose implementation plan be frozen.
