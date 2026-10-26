# Analytics & Privacy - Google Ads WhatsApp Conversion

Date: 2026-10-26. Describes exactly what the Google Ads tag does on
hurghadakerotour.com, what it sends, what it deliberately does not send, and the
consent handling. **This is an engineering description, not a legal compliance
certification.** Full legal compliance must be verified by the owner / counsel
for the markets actually reached.

## What is installed

- **One** Google tag (`gtag.js`), loaded **async** (non-blocking), once per
  content page, through the shared generator (`build.py` -> `analytics_head()`).
  Tag id: **AW-18538088460** (Google Ads). Source of truth: `site_config.py`
  (`GOOGLE_ADS_ID`, `GOOGLE_ADS_CONVERSION_LABEL`).
- **No GA4.** **No Google Tag Manager container.** No other trackers.
- The 404 page carries no tag and stays `noindex`.

## The single conversion action

- Name in Google Ads: **KeRo | WhatsApp Contact**
- `send_to`: **AW-18538088460/HOYlCNeOq6odEIyQ04dF**
- Category: Contact. Count: **One**. Value: **0 EGP** (no value is ever sent -
  the price is never submitted as revenue). Click window: 30 days.
  Attribution: data-driven. Enhanced conversions: **off**.

It represents a **WhatsApp contact attempt**, not a confirmed message, a
qualified lead, a purchase or a booking.

## When the conversion fires (and when it does not)

Central handling in `assets/js/app.js` - no duplicated inline `onclick`.

Fires **exactly once** on a deliberate WhatsApp handoff:
- any direct `wa.me` CTA click (`[data-wa]`): homepage floating button, tour-page
  floating button, header/footer WhatsApp links, excursion-card and
  contact-section WhatsApp links - on desktop and mobile;
- a booking-form submission **after** client-side validation passes.

Does **not** fire on:
- page views / page load / tag initialization / background scripts;
- opening the booking form (`[data-book-open]` is explicitly skipped);
- invalid form submits (missing hotel, bad people count, missing/past date);
- merely selecting a date.

**No double counting.** A CTA that opens the booking form carries both
`data-wa` and `data-book-open`; the click handler returns early for
`data-book-open`, so the conversion is counted only once, on the eventual
validated submit - never once on the click and again on the submit. There is one
delegated click listener and one form-submit listener (no overlapping handlers).

## What is sent to Google - and what is NOT

The conversion payload is only `{ 'send_to': 'AW-18538088460/HOYlCNeOq6odEIyQ04dF' }`.

**Never transmitted to Google:** hotel name, room number, number of people,
preferred date, customer notes, the WhatsApp message text, or the complete
prefilled `wa.me` URL that contains those fields. (Verified live: filling the
form with test hotel/notes/room values produced a conversion payload containing
none of them.)

## Consent handling (region-scoped Consent Mode v2, no cookie banner)

The intended advertising audience is tourists **physically in Egypt**, so no
intrusive global cookie banner is injected merely because the UI offers FR/PL/RO.
But ad location targeting does not prove every visitor is in Egypt, so:

- Google **Consent Mode v2** defaults are set **before** the tag configures.
- In the **EEA (EU-27 + IS/LI/NO), the UK and Switzerland**, `ad_storage`,
  `ad_user_data`, `ad_personalization` and `analytics_storage` default to
  **denied** - no advertising cookies/identifiers are stored for those visitors
  without consent; Google can still model conversions cookielessly.
- Everywhere else they default to **granted**.
- `url_passthrough` keeps the GCLID flowing across navigations without cookies;
  `ads_data_redaction` redacts ad identifiers **only** where consent is denied,
  so normal auto-tagging/attribution outside the EEA is untouched (the GCLID is
  not stripped unnecessarily).

This prevents consent-requiring (cookie-based) tag firing where consent is
legally required, **without** a banner. It is **not** a claim of full legal
compliance. If the owner intends to actively target EEA/UK/CH traffic, a proper
consent-management solution (banner + a mechanism to *grant*) is required; this
setup only sets safe defaults and never grants on their behalf.

## Reliability / non-blocking

- `gtag.js` loads `async`; nothing blocks rendering.
- The conversion is fired and the WhatsApp tab is opened immediately; the code
  does **not** wait on a Google `event_callback`.
- If `gtag` is unavailable, an ad blocker drops the beacon, or the request fails,
  the user still reaches WhatsApp. Verified live: with the test browser's privacy
  extension dropping the Google beacon, the WhatsApp handoff still worked and the
  original page did not navigate away.
- The Content-Security-Policy `<meta>` is aligned with Google's official CSP
  guidance for the Google tag + Google Ads conversion/remarketing/Conversion
  Linker + Tag Assistant
  (developers.google.com/tag-platform/security/guides/csp): `script-src` allows
  `googletagmanager.com`, `googleadservices.com`, `googleads.g.doubleclick.net`
  and `www.google.com`; `img-src`/`connect-src`/`frame-src` include
  `www.googletagmanager.com` (Tag Assistant debug channel); `connect-src` adds
  `ad.doubleclick.net` and `img-src` adds `pagead2.googlesyndication.com`; and
  `img-src`+`connect-src` list the visitor's local Google ccTLDs
  (`GOOGLE_AD_DOMAINS`: Egypt + FR/PL/RO + main EEA/UK/CH) because the Ads
  first-party pings (`1p-user-list`, `1p-conversion`) go to the local Google
  domain. No `unsafe-eval`, no wildcards. (GitHub Pages cannot send real response
  headers, so CSP is a meta tag.)
- Verified live (uBlock off): zero CSP `Refused` console violations; the core
  conversion `www.googleadservices.com/pagead/conversion/18538088460/` returns
  200. The secondary enhanced-conversions/remarketing pings
  (`1p-conversion`, `ccm/collect`) may return server-side `503` because enhanced
  conversions is disabled - that is Google's response, not a CSP block, and does
  not affect the counted conversion.

## WhatsApp navigation (unchanged by this work)

`wa.me` still opens in a **separate tab** (`target="_blank" rel="noopener"`); the
KeRo page stays open. The Google sample's `window.location = url` same-tab
redirect is **not** used. Number: `201288808645`. Messages stay localized and
carry the correct per-page URL.

## Limitations / not verified here

- Google Ads showing the tag as "active" and recording a conversion is confirmed
  **only** once observed in the Google Ads UI (Tools -> Conversions /
  diagnostics). A tag can take time to be recognized. Do not assume a verified
  conversion until it appears there.
- Legal compliance (ePrivacy/GDPR/consent, local Egyptian and destination-market
  rules) is **not** certified by this document.
