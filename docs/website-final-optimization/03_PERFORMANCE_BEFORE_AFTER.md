# 03 - Performance: Before / After (updated round 2)

Date: 2026-11-08. This report was substantially revised after a deeper, multi-run
investigation (the user asked for evidence, not assumptions).

## Key correction: the "12.9 s LCP / 2.29 s TTFB" was a measurement artifact

The first live Lighthouse run (report 01) reported Performance 53, LCP 12.9 s, TTFB
2.29 s. Deeper measurement shows that run was distorted by this machine's network/headless
conditions, not by production:

- Lighthouse's own trace modelled an ~1,680 ms RTT and an 8.5 s fetch for the 15 KB
  gzipped HTML document. That is not physically consistent with the server.
- **Multi-run curl from an EU edge (Frankfurt/Fastly):**
  - Cold: DNS 0.25 s, TCP 0.07 s, TLS 0.41 s, TTFB 0.615 s, total 0.62 s.
  - Warm (connection reuse): TTFB 0.22-0.25 s.
  - Repeated hits show `x-cache: HIT`, `content-encoding: gzip`, HTML ~14.8 KB gzipped.
- **Clean render-path Lighthouse** (served from local dist, so network latency is removed
  and only render + CPU throttle remain): Performance 85, LCP 3.5 s, FCP 2.1 s, TBT 80 ms,
  CLS 0.013.

Conclusion: real users (especially the EU FR/PL/RO audience) already get sub-second TTFB.
The page's own render path is healthy. There was no 12.9 s production problem; there was a
bad measurement plus a few genuine render-path items, which were then fixed.

## Evidence-based Cloudflare decision: NOT needed for performance

The user asked to verify, not assume. Evidence:

- GitHub Pages already serves through **Fastly CDN** (`x-served-by: cache-...-MRS`,
  `x-cache: HIT`, `via: 1.1 varnish`), with edge POPs covering FR/PL/RO.
- Measured TTFB is 0.2-0.6 s with gzip and HTTP/2 already active.

Therefore **Cloudflare would not materially reduce TTFB** for this audience - the premise
that GitHub Pages is the latency bottleneck is wrong. Cloudflare's only real additions here
would be:

1. Brotli instead of gzip (a few KB; marginal).
2. HTTP/3 / QUIC (minor connection-setup win).
3. Response headers GitHub Pages cannot send: HSTS (site-wide), X-Frame-Options /
   `frame-ancestors`, X-Content-Type-Options, header-delivered CSP with nonces
   (would satisfy Lighthouse `csp-xss`).

Recommendation: Cloudflare is **optional and low priority, and its value is security
headers, not speed.** Do not expect a Core Web Vitals gain from it. If added, it is a
30-minute owner DNS task (steps retained in report 08). This corrects report 03's earlier
framing of Cloudflare as "the #1 performance lever."

## Repo-side optimizations actually implemented this round

All measured on the rebuilt `dist/` (Lighthouse 11.7.1, mobile, local server; network
removed so the deltas reflect the render path, which is what changed):

1. **Inlined all CSS** (`fonts.css` + `styles.css`, ~61 KB) into a single `<head>` `<style>`
   block, removing the two render-blocking stylesheet requests. CSP already allows
   `style-src 'unsafe-inline'`.
2. **Deferred `config.js`** (was a synchronous, render-blocking `<script>` in `<head>`; it
   only sets `window.KERO_WHATSAPP`, read later by the deferred `app.js`, so order is safe).
3. **Preloaded the homepage hero image** (responsive `imagesrcset`/`imagesizes` matching the
   hero `<img>`, `fetchpriority=high`). The homepage hero is the LCP element and previously
   had no preload (only tour pages did).

### Measured before -> after (local dist, mobile throttled)

| Metric | Before (round 1 render-path) | After (round 2) |
|---|---|---|
| Performance | 85 | **90** (FR 93, RO 90) |
| FCP | 2.1 s | **1.8 s** (FR 1.4 s) |
| Speed Index | 5.3 s | **3.0 s** (RO 2.6 s) |
| LCP | 3.5 s | **3.3 s** (FR 2.9 s) |
| TBT | 80 ms | 80-90 ms |
| CLS | 0.013 | 0.013 (RO/FR 0) |
| Render-blocking resources | fonts.css + styles.css + config.js | **none** |

All three languages measured (homepages): FR perf 93 / a11y 100, PL perf 90 / a11y 100,
RO perf 90 / a11y 100. Run-to-run variance accounts for the 90-93 spread.

### Page-weight tradeoff (honest)

- First paint before: ~15 KB gzip HTML + ~11.8 KB gzip `styles.css` + ~1.5 KB gzip
  `fonts.css` = ~28 KB across **3 render-blocking requests**.
- First paint after: **~27 KB gzip in one HTML request, 0 render-blocking CSS requests.**
- Tradeoff: on multi-page sessions the inlined CSS is re-sent per page (~12 KB gzip each)
  instead of using a shared cache entry. Acceptable for a landing-page-first site where paid
  visitors arrive cold on one page and convert via WhatsApp. The source `styles.css` /
  `fonts.css` are still emitted to `dist/assets/css` (tests read them; still cacheable if
  re-referenced later).

## What was already fast (prior sessions, retained)

Self-hosted WOFF2 fonts (zero cross-origin font requests, `font-display: swap`, latin-ext
subsets on demand for PL/RO), responsive WebP cards/galleries, CLS controlled with explicit
image dimensions, gtag async. Prior image-transfer cuts of 54-76%.

## Still not done (and why)

- AVIF images: no AVIF encoder on this machine (Pillow 9.4 no AVIF, no `avifenc`). WebP q82
  already in place. ~30% image-transfer win if an encoder is installed later.
- Delay-loading gtag (58 KiB "unused JS"): would raise the lab number but risks losing
  WhatsApp-click conversions. Not done - conversion fidelity outranks a score.
- Logo micro-optimization: Lighthouse "waste" is mostly a retina 1x-vs-2x artifact; low value.
- Live post-deploy re-measurement: pending the production push (report 07). The numbers above
  are local-dist (render path) + EU-edge curl (network); a live Lighthouse should be captured
  after deploy. No field (CrUX) data exists/was available; none is invented.

## Honest verdict

The site was never 12.9 s slow for real users. The render path is now cleaner (no
render-blocking CSS/JS, hero preloaded), measured at Performance ~90 and LCP ~3 s on
throttled mobile, CLS ~0. Cloudflare is not required for speed. The remaining sub-2.5 s LCP
gap under heavy throttling is image-decode/CPU bound and is already close to target on real
networks.
