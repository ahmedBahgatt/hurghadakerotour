# 08 - Remaining Issues

Date: 2026-11-08. Everything that is not fully resolved, with the exact reason and the
required action/owner.

## Owner-side (cannot be done in the repo)

| # | Item | Why it matters | Required action | Blocker |
|---|---|---|---|---|
| 1 | CDN in front of GitHub Pages (Cloudflare free) | The dominant Core Web Vitals / Landing Page Experience lever: removes the GitHub Pages TTFB (2.29 s cold MISS -> 12.9 s LCP on throttled mobile). Also enables Brotli, HTTP/3, and real security response headers. | Add domain to Cloudflare, switch Hostinger nameservers, proxy DNS, Full (strict) TLS, header rules. Steps in report 03. | Needs Hostinger DNS + Cloudflare account. |
| 2 | Google Search Console verification + sitemap submit | Lets Google discover/monitor the now-indexable pages and surfaces indexing problems. | DNS-TXT verify the property, submit `sitemap.xml`. `SEO_LAUNCH_CHECKLIST.md` step 6. | Needs DNS access + GSC login. |
| 3 | Google Ads account changes (ad groups, RSAs, negatives, final URLs, bidding) | Fixes "Ad Relevance: Below Average" and lost-IS-rank, which website edits cannot touch. | Apply report 05 recommendations in the account. | No account access this session; brief forbids changing campaigns here anyway. |
| 4 | Business legal info (legal name, address, tourism licence number, public email) | Trust signal; some are legal/VAT requirements for EU-facing commerce. Empty in `site_config.BUSINESS`. | Owner supplies real values; then populate and rebuild. Never fabricated. | Owner input. |
| 5 | Offline conversion loop (GCLID capture + lead/booking import) | So real WhatsApp leads/bookings are measured, not just clicks (report 06). | Approve GCLID-in-message + create import conversion actions + maintain a log. | Owner go-ahead + manual logging. |
| 6 | Confirm the live Ads conversion in the Ads UI | Verify "KeRo \| WhatsApp Contact" is received before conversion bidding. | Ads UI: Tools -> Conversions. | Owner. |

## Repo-side, deferred (reason stated)

| # | Item | Why deferred |
|---|---|---|
| 7 | 8 titles > 70 chars (Cairo/GEM + Three Islands in FR/PL/RO, FR/Luxor homepage) | Cosmetic SERP-truncation only; shortening is a copy change in 3 languages that should be reviewed and re-validated, not rushed onto a live ad site. Edit `data/seo.py`, re-run `test_seo.py`. |
| 8 | AVIF images via `<picture>` | No AVIF encoder available on this machine (Pillow 9.4 no AVIF, no `avifenc`). ~30% image-transfer win if an encoder is installed later. WebP q82 already in place. |
| 9 | Delay-loading `gtag.js` (58 KiB unused JS) | Would improve the lab number but risks losing WhatsApp-click conversions. Conversion fidelity outranks the score. Not recommended. |
| 10 | Logo micro-optimization | Lighthouse "waste" is largely a retina 1x-vs-2x artifact; low value. |

## Structural limits (not defects)

| Item | Explanation |
|---|---|
| Best-practices capped ~78 | Third-party cookies from Microsoft Clarity + Google Ads (and the meta-delivered CSP with `unsafe-inline`). These are the owner's chosen analytics/ads tools; removing them removes measurement. A header-delivered CSP with nonces (via CDN, item 1) would clear the `csp-xss` part. |
| No custom HTTP response headers | GitHub Pages cannot send them, so header-level CSP/HSTS/X-Frame-Options are impossible without the CDN (item 1). |
| No field (CrUX) metrics | Public PSI/CrUX quota blocked this session and site traffic may be too low for a CrUX record. Re-check after indexing + ads ramp; never invent field numbers. |
| Quality Score not guaranteed | Website changes improve inputs (relevance, speed, trust) but cannot guarantee a QS or ranking increase; diagnostics update on a lag (and pages were noindex until 2026-10-26). |

## Compliance holds (unchanged)

- Lion Cub Photo Experience stays ad-excluded (`LION_CUB_ADS_ELIGIBLE=False`) until its legal/welfare/facility/ad-policy review is signed off. Organic-only.
- Cairo/Luxor 50% deposit; all other tours pay-at-start, no deposit. Prices unchanged.
- Hungarian (`/hu/`) intentionally absent - separate future project, out of scope.
