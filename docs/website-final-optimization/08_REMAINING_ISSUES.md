# 08 - Remaining Issues

Date: 2026-11-08. Everything that is not fully resolved, with the exact reason and the
required action/owner.

## Owner-side (cannot be done in the repo)

| # | Item | Why it matters | Required action | Blocker |
|---|---|---|---|---|
| 1 | Cloudflare in front of GitHub Pages - OPTIONAL, security-headers only | CORRECTED (round 2): this is NOT a performance necessity. Evidence (report 03): GitHub Pages already uses Fastly CDN; measured TTFB is 0.2-0.6 s with `x-cache: HIT` + gzip + HTTP/2. Cloudflare would not materially cut TTFB. Its only real benefit here is response headers GitHub Pages cannot send (HSTS site-wide, X-Frame-Options / header-CSP + nonces, X-Content-Type-Options) plus Brotli/HTTP3 (marginal). | If wanted for security headers: add domain to Cloudflare, switch Hostinger nameservers to Cloudflare, proxy the apex/`www` records (orange cloud), SSL/TLS = Full (strict), enable Always-Use-HTTPS, add a response-header rule (HSTS, X-Frame-Options DENY, X-Content-Type-Options nosniff, Referrer-Policy, header CSP), keep the GitHub Pages custom-domain config. Verify no redirect loop and that the Pages cert still validates. | Owner: Hostinger DNS + Cloudflare account. Do NOT expect a speed gain. |
| 2 | Google Search Console verification + sitemap submit | Lets Google discover/monitor the now-indexable pages and surfaces indexing problems. | DNS-TXT verify the property, submit `sitemap.xml`. `SEO_LAUNCH_CHECKLIST.md` step 6. | Needs DNS access + GSC login. |
| 3 | Google Ads account changes (ad groups, RSAs, negatives, final URLs, bidding) | Fixes "Ad Relevance: Below Average" and lost-IS-rank, which website edits cannot touch. | Apply report 05 recommendations in the account. | No account access this session; brief forbids changing campaigns here anyway. |
| 4 | Business legal info (legal name, address, tourism licence number, public email) | Trust signal; some are legal/VAT requirements for EU-facing commerce. Empty in `site_config.BUSINESS`. | Owner supplies real values; then populate and rebuild. Never fabricated. | Owner input. |
| 5 | Offline conversion loop - website side DONE; owner steps remain | Website now captures GCLID and appends `Ref: <id>` to the booking message (report 02/06). To measure real leads/bookings: create the two import conversion actions in Google Ads and keep a log keyed by `Ref`. | Owner: create import conversions + maintain a lead/booking sheet (or add a backend/CRM for auto-import). | Owner process. |
| 6 | Confirm the live Ads conversion in the Ads UI | Verify "KeRo \| WhatsApp Contact" is received before conversion bidding. | Ads UI: Tools -> Conversions. | Owner. |

## Repo-side, deferred (reason stated)

| # | Item | Why deferred |
|---|---|---|
| 7 | 2 residual titles > 70 chars (was 8; FR Cairo 75, FR home 76) | Mostly resolved round 2 by shortening the shared title suffix ` | KeRo Tours Hurghada` -> ` | KeRo Tours` (all 3 langs). The 2 residual are FR only, keyword-first ("Le Caire ..." / brand-led home title), display-safe (~68 shown; the raw count is inflated by the `&amp;`/`&#x27;` entities). Acceptable; optionally trim the FR home `&` -> `et` later. |
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
