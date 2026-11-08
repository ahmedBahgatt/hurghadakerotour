# 03 - Performance: Before / After

Date: 2026-11-08. Honest measurement with the lab-vs-field distinction the brief requires.

## Method and caveats

- Lab: Lighthouse 11.7.1, mobile form factor, simulated throttling.
- Field (CrUX): PageSpeed Insights / CrUX API were **not usable this session** (public PSI quota returned HTTP 429 with no API key). The site also has low traffic, so a site-level CrUX record may not exist yet. **No field INP/LCP percentiles are reported** - none were observed, and none are invented.
- GitHub Pages TTFB varies by cache state (cold MISS vs warm edge), so single-run LCP/Performance swing widely. Treat perf score and LCP as ranges, not fixed numbers (consistent with prior-session findings: PL home score observed 73-82 and LCP 4.5-5.7 s across runs on other dates).

## Before (live `/pl/`, mobile lab, this session)

| Metric | Value |
|---|---|
| Performance | 53 |
| LCP | 12.9 s (cold MISS run; TTFB 2.29 s) |
| FCP | 7.5 s |
| Speed Index | 19.0 s |
| TBT | 160 ms |
| CLS | 0.013 |
| TTFB (server-response) | 2,290 ms |
| Total bytes | 941 KiB |
| Accessibility | 86 |
| Best practices | 74 |
| SEO | 100 |

Warm-edge sanity check (curl, EU/Frankfurt edge): `time_starttransfer` ~0.61 s, gzipped HTML ~15 KB. So real EU users on a warm edge see far better TTFB than the 2.29 s cold-MISS lab figure - but throttled mobile still exceeds the 2.5 s LCP target because of origin variability + render-blocking CSS.

## After (this session's changes)

The source changes in report 02 target **accessibility and best-practices**, not raw speed. Measured on the rebuilt `dist/` (mobile lab, local server; localhost removes TTFB so perf is not comparable, but a11y/bp audits are network-independent and valid):

| Category | Before (live) | After (dist) | Delta |
|---|---|---|---|
| Accessibility | 86 | 100 | +14 |
| Best practices | 74 | 78 | +4 (console error cleared; residual = tracking cookies) |
| SEO | 100 | 100 | 0 |
| CLS | 0.013 | ~0 (layout untouched) | - |

Performance score / LCP after deploy are **expected to be unchanged** because they are TTFB-bound and this session made no change to origin latency. This is stated plainly rather than claimed as an improvement. A post-deploy live re-run should be taken to confirm (report 07 / 08).

## What already made the site fast (prior sessions, retained)

- Self-hosted WOFF2 fonts (Manrope + Fraunces), zero cross-origin font requests, `font-display: swap`, latin-ext subsets load on demand for PL/RO diacritics.
- Responsive WebP variants (`srcset`/`sizes`) for cards and galleries; LCP hero/gallery image preloaded with `fetchpriority=high` and matching `imagesrcset`. Prior measured image-transfer cuts: PL home 1204 -> 550 KB, others -54% to -76%.
- CLS controlled (explicit image dimensions); TBT already under 200 ms.
- gtag loaded `async`; the only sizeable unused JS is the Ads tag itself (needed for conversions).

## The remaining performance lever (owner-side): CDN in front of GitHub Pages

This is the single highest-impact action for Core Web Vitals and for Google Ads Landing Page Experience, and it cannot be done in the repo.

Recommended: **Cloudflare (free plan)** in front of the existing GitHub Pages origin.

Benefits, all directly tied to measured weaknesses:
1. **TTFB**: Cloudflare edge caches the static HTML/assets globally (incl. Poland/Romania/France POPs), removing the GitHub Pages cold-MISS origin fetch that produced the 2.29 s TTFB and the 12.9 s LCP. This is the dominant LCP driver.
2. **Brotli + HTTP/3 (QUIC)**: smaller transfer and faster connection setup than the current gzip/HTTP-2.
3. **Response headers** (impossible on bare Pages): real `Content-Security-Policy` (header-delivered, enabling `frame-ancestors`/nonces to satisfy Lighthouse `csp-xss`), `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, long-lived immutable `Cache-Control` for `/assets/`.

Setup (owner, ~30 min, reversible):
1. Add the domain to Cloudflare; it imports existing DNS.
2. Switch the domain's nameservers at Hostinger to the two Cloudflare nameservers.
3. Keep the GitHub Pages custom-domain setup; set the apex/`www` records to "Proxied" (orange cloud).
4. SSL/TLS mode "Full (strict)". Enable Brotli, HTTP/3, "Always Use HTTPS".
5. Add a Transform/Response-header rule (or Cloudflare Workers) for the security headers above.
6. Re-run Lighthouse + PageSpeed on `/pl/`, `/fr/`, `/ro/` to capture the real after-numbers.

Expected outcome: TTFB from seconds to tens of milliseconds at the edge; LCP should move toward or under 2.5 s on throttled mobile, and the `csp-xss` / header-based best-practices items become addressable. This is an expectation, not a guarantee, and should be verified by measurement after the change.

## Not done (and why)

- AVIF `<picture>`: no AVIF encoder is available on this machine (Pillow 9.4 has no AVIF; no `avifenc`). WebP q82 <= 1600 px is already in place. Deferred; it is a ~30% image-transfer win if an encoder is installed later.
- Delay-loading gtag until interaction: would cut the 58 KiB unused-JS figure but risks losing WhatsApp-click conversions (the whole point of the tag). Not done - conversion fidelity outranks a lab number.
- Logo micro-optimization: Lighthouse flags `logo.png` ~42 KiB "waste", but that is largely a 1x-vs-retina artifact (300 px served for a 150 px slot on 2x screens). Deferred as low-value/low-priority.
