# 09 - Final Executive Report

Date: 2026-11-08. Site: https://hurghadakerotour.com (FR / PL / RO). Production source:
`github.com/ahmedBahgatt/hurghadakerotour` (static, GitHub Pages).

## Context correction

The brief anticipated a possible WordPress/Webflow/Next.js production site. It is not:
it is a **Python static-site generator on GitHub Pages**, and it was already heavily
optimized by prior work (self-hosted fonts, responsive WebP, LCP preload, live Google Ads
conversion tracking, Consent Mode v2, valid multilingual SEO + schema). This session was
therefore a targeted finish-and-verify pass, not a rebuild, correctly operating on the
real production repo (not the retired landing-page repos or `egipskiewakacje.pl`).

## 1. What exactly was wrong

- **Load speed (the real driver of "Landing Page Experience: Below Average")**: GitHub Pages TTFB on a cold cache MISS was 2.29 s, pushing throttled-mobile LCP to 12.9 s (target <= 2.5 s). This is the single biggest controllable weakness and it is owner-side (needs a CDN).
- **Accessibility (86/100)**: active language pill failed WCAG AA contrast (2.5:1); a footer heading skipped a level; the social-icons row used `role="list"` without list-item children.
- **Best practices (74/100)**: the meta CSP carried `frame-ancestors`, which browsers ignore in `<meta>` and which logged a console error; plus third-party cookies from the owner's analytics/ads tools.
- **8 page titles** exceed ~70 characters (SERP truncation risk; cosmetic).
- Ad-account-side (not website): Ad Relevance "below average" (RSA copy) and lost impression share to Ad Rank; plus the fact that pages were `noindex` until 2026-10-26, which can depress historical Quality Score readings.

No broken pages, wrong prices, wrong WhatsApp number, or mis-indexing were found. The
website WhatsApp number `201288808645` is correct everywhere; the Meta-campaign number
`201278378685` correctly does not appear.

## 2. What was actually fixed (deployed status: built + gated, push held for go-ahead)

Four surgical source edits (`build.py`, `assets/css/styles.css`), rebuilt into `dist/`:
1. Removed the ineffective `frame-ancestors` from the meta CSP -> console error cleared.
2. Social row `role="list"` -> `role="group"` -> ARIA children audit cleared.
3. Footer `<h4>` -> `<h3>` (+ CSS) -> heading-order cleared.
4. Active language pill `--sea` -> `--sea-deep` -> contrast now 5.06:1 (AA pass).

Measured result on the built site (Lighthouse mobile): **Accessibility 86 -> 100**,
best-practices 74 -> 78, SEO 100 -> 100. All four CI gates pass. No content, price,
number, schema, or layout change.

## 3. How much faster the site became - with real numbers

Honest answer: this session's edits do **not** change raw speed, and none is claimed.
Speed is TTFB-bound, and TTFB is a GitHub Pages trait fixable only by fronting the site
with a CDN (owner action). Measured baseline (mobile lab, live `/pl/`): Performance 53,
LCP 12.9 s, FCP 7.5 s, TBT 160 ms, CLS 0.013, TTFB 2.29 s. Prior-session image work had
already cut image transfer 54-76% (e.g. PL home 1204 -> 550 KB). The expected large speed
gain (LCP toward/under 2.5 s) comes from the Cloudflare step in report 03, to be verified
by measurement after it is applied. No field (CrUX) numbers exist/were available, so none
are reported.

## 4. Are FR, PL, RO technically ready for SEO and Google Ads?

**Yes, technically.** All three are indexable (`index,follow`), self-canonical,
reciprocally hreflang-linked (fr/pl/ro/x-default), individually titled/described,
schema-valid (score 100), and internally linked, with correct landing pages for the
priority keywords. Caveats: eligibility is not a guarantee of indexing or ranking; the
8 long titles are a minor cosmetic cleanup; and real paid-search success still depends on
the speed (CDN) and account-side (RSA/keyword/bid) items, plus Search Console submission.

## 5. Do the booking and WhatsApp flows work?

Yes. All 36 pages load (HTTP 200); every WhatsApp CTA targets `wa.me/201288808645` with a
localized, tour-specific prefilled message; the booking-form dialog validates and hands
off in a new tab without stranding the user; the single Ads conversion fires once per
genuine handoff with no personal data and is not conflated with a booking.

## 6. What remains unresolved

Owner-side: CDN/Cloudflare (speed + headers), Search Console verification + sitemap
submit, Google Ads account restructuring (ad groups/RSAs/negatives/final-URL alignment/
bidding), business legal info, offline conversion import (GCLID + lead/booking logging),
and confirming the conversion in the Ads UI. Repo-side deferred: 8 long titles, AVIF
images (no encoder available), gtag delay-load (declined to protect conversions). Full
list with reasons in report 08. Structural: best-practices is capped ~78 by the owner's
own tracking cookies; GitHub Pages cannot send header-level security policies.

## 7. Is it safe to resume/optimize the Polish Google Ads campaign?

Qualified yes, in this order:
1. **Deploy** this session's fixes (push on go-ahead) and verify live.
2. **Front with Cloudflare** - this is the highest-leverage move for Landing Page
   Experience and should precede any budget increase. Do not "fix" low quality by raising
   CPC.
3. **Restructure the PL ad groups + RSAs** (report 05) so Ad Relevance rises and each
   keyword points at the right page.
4. **Submit to Search Console** and let Google re-crawl the now-indexable pages.
5. Give it ~2-4 weeks and re-read the Quality Score / Landing Page Experience diagnostics
   (they lag, and the noindex history will keep clearing). Then scale budget on the
   keywords whose QS has recovered.

Quality Score improvements cannot be guaranteed or claimed as immediate; the website side
is now clean, and the remaining levers are the CDN and the ad account.
