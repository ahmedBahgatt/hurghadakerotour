# 06 - Conversion Tracking Audit

Date: 2026-11-08. Verified in source (`build.py`, `assets/js/app.js`, `site_config.py`)
and against the live pages; no test conversion was fired into the live account (that
would pollute real data).

## What is installed

| Component | State |
|---|---|
| Google Ads tag | `AW-18538088460`, one async `gtag.js` per content page. |
| Conversion action | One: "KeRo \| WhatsApp Contact" (`HOYlCNeOq6odEIyQ04dF`). Count: One, value 0, 30-day click window, enhanced conversions OFF. |
| GA4 | None (intentionally no `GA4_MEASUREMENT_ID`). |
| GTM | None (no container; direct gtag). |
| Microsoft Clarity | `z4klch73ka` (heatmaps + session recordings), input masked, CSP-allowed. |
| Consent Mode | v2. EEA/UK/CH `ad_storage`/`analytics_storage`/`ad_user_data`/`ad_personalization` denied by default (cookieless modelling); granted elsewhere (the Egypt-based tourist audience). `url_passthrough` + `ads_data_redaction` on. No cookie banner. |

## Firing logic (verified in `app.js`)

Exactly one conversion is counted per deliberate WhatsApp handoff:
- A direct `[data-wa]` WhatsApp click, OR a validated booking-form submit.
- Form-open clicks (`[data-book-open]`) fire nothing (no double count).
- Invalid form submits fire nothing.
- No personal data (hotel, room, people, notes, date, message, URL) is sent to Google.
- WhatsApp opens in a new tab (`target=_blank rel=noopener`) via a synthesized anchor; the handoff is not gated on the gtag beacon, so an ad-blocker that drops the beacon still lets the user reach WhatsApp.

This correctly respects the brief's event hierarchy:
`WhatsApp button click` != `actual WhatsApp message` != `qualified lead` != `confirmed booking`.
The site can only observe the **click/handoff** (step 1). It does not and must not fire a
Purchase-type conversion on a WhatsApp open. The single action is explicitly a "Contact",
not a sale.

## Gaps and the offline-conversion reality

The website cannot see what happens after the user lands in WhatsApp. Steps 2-4 happen
off-site in the operator's WhatsApp Business app. To measure real leads and bookings:

1. **Qualified lead** = a WhatsApp conversation where the tourist gives hotel + date + pax. Record manually (or via WhatsApp Business labels) with the date and, ideally, the GCLID.
2. **Confirmed booking** = the customer shows up / pays at the start of the excursion.

### Offline Conversion Import (OCI) workflow - website side now IMPLEMENTED (round 2)

Website-side GCLID capture is now live in the code (see report 02, Fix 8):

- `assets/js/app.js` `captureClickId()` reads `gclid` / `gbraid` / `wbraid` from the landing
  URL, validates it against `^[A-Za-z0-9_.-]{1,120}$` (URL params are untrusted input, so the
  value is sanitised before it can ever enter a WhatsApp message), and persists it in
  `localStorage` for ~90 days (the Ads click window), surviving in-site navigation.
- The booking-form message appends a single `Ref: <id>` line **only when an id is present**.
  Organic / direct visitors have no id and get a clean, unchanged message - honouring "avoid
  exposing long tracking identifiers unnecessarily."
- The id is appended at the END of the message, after the human-readable booking details, so
  the operator can copy it into their log. gtag's own `_gcl_aw` cookie continues to attribute
  the on-click "Contact" conversion independently (no reliance on the message for that).

Why the message-line approach: the site is static with no backend, so there is no server to
map a short code back to a GCLID. The only no-backend way to carry the click id to the
operator with the inquiry is inside the WhatsApp message. A cleaner short-code scheme would
require a backend / CRM (documented below as the remaining integration).

To close the loop (owner side):
1. (done, website) GCLID travels with the booking inquiry as `Ref: <id>`.
2. In Google Ads, create two import conversion actions: "Qualified WhatsApp lead" and
   "Confirmed booking".
3. The operator keeps a simple sheet: `Ref` (GCLID), timestamp, stage (lead / booking), value.
4. Import via the Ads UI (CSV) or the API on a schedule.
5. Once "Confirmed booking" has volume, switch bidding toward it (report 05).

Optional future (needs a backend/CRM): capture the inquiry server-side so the message can
carry a short code instead of the raw GCLID, and so lead/booking stages can be imported
automatically rather than from a manual sheet.

This is the only honest way to optimize toward real revenue; until then the "WhatsApp
Contact" action is the proxy, and it must not be interpreted as a booking.

## Consent / privacy

- EEA/UK/CH cookieless-by-default via Consent Mode v2 (no banner shown; no storage until/unless granted). Egypt + rest granted. Details in `ANALYTICS_PRIVACY.md`.
- Clarity reads the same gtag consent signal (native GCM integration) and masks all input values.
- Residual best-practices "third-party cookies" (report 08) come from these tools when consent is granted; they are the cost of measurement, not a defect. If stricter EU posture is wanted later, add an explicit consent UI - this is a legal decision for the owner, not a code default.

## Duplicate-event check

- One Ads tag install per page (asserted by `test_analytics.py`). No GA4/GTM to double up.
- Conversion fires once per handoff (asserted logic). No page-load conversion.

## Verdict

Tracking is correctly scoped and privacy-aware. The measurable event is the WhatsApp
handoff, and it is not conflated with a booking. Round 2 added the website side of offline
attribution: validated GCLID capture + a conditional `Ref:` line on the booking message. The
remaining pieces are owner-side and process-level: create the two import conversion actions
in Google Ads and keep a lead/booking log keyed by `Ref`. A fully automated loop (short codes,
auto-import) would need a backend/CRM.
