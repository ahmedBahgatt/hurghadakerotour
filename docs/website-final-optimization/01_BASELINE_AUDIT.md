# 01 - Baseline Audit

Date: 2026-11-08. Scope: live production site https://hurghadakerotour.com (FR/PL/RO).
All values below were measured this session unless labelled "prior session".

## 1. Stack and infrastructure (verified)

| Item | Finding |
|---|---|
| Platform | Static site on GitHub Pages. `server: GitHub.com`, Fastly edge (`x-served-by: cache-...`, `x-github-edge-region: fra`). NOT WordPress / Webflow / Next.js. |
| Source of truth | `github.com/ahmedBahgatt/hurghadakerotour`, branch `main`. Local checkout: `France_websit/kero-tours-landing` (origin confirmed; `old-origin` = the retired `kero-tours-landing` repo). |
| Generator | Python 3 standard-library static generator. `python3 build.py` -> `dist/` (committed). Content in `data/tours.py`, `data/i18n.py`, `data/seo.py`; config in `site_config.py`. |
| Deploy | Push to `main` -> GitHub Actions (`.github/workflows/deploy.yml`): secret-scan + `build.py` + `check.py` -> `deploy-pages`. |
| CDN / caching | Fastly in front of Pages (gzip on, 10 min `cache-control`). No custom CDN. No custom response headers possible on Pages. |
| TLS | HTTPS enforced (Let's Encrypt via Pages). |
| Repo cleanliness | `main` == `origin/main`, working tree clean before this session. Build is reproducible (only `sitemap.xml` lastmod churns). |

Separate properties deliberately NOT touched: `egipskiewakacje.pl` (photo source), the retired `kero-tours-landing` repo, `kero-tours-hurghada.pages.dev`, and the Meta ad campaigns.

## 2. URL inventory and crawl (verified)

- Sitemap `https://hurghadakerotour.com/sitemap.xml` lists **36 canonical page URLs** (3 homepages + 33 excursion pages) plus an image sitemap.
- **All 36 returned HTTP 200.** Root `/` = 200 (French homepage). `404.html` = 200. `robots.txt` = 200. `sitemap.xml` = 200.
- `/hu/` = 404 (expected: Hungarian is explicitly out of scope).
- No 4xx/5xx among indexable pages. No broken-page (P0) issues found.

Route pattern: `/fr/`, `/pl/`, `/ro/`; tours at `/fr/excursions/<slug>/`, `/pl/wycieczki/<slug>/`, `/ro/excursii/<slug>/`.

## 3. On-page SEO signals (verified live, all three languages)

| Page | Title | H1 | robots | canonical |
|---|---|---|---|---|
| `/fr/` | KeRo Tours Hurghada - Excursions VIP & transferts \| Reservation WhatsApp | Excursions VIP a Hurghada, sans acompte | index,follow,max-image-preview:large | self |
| `/pl/` | KeRo Tours Hurghada - Wycieczki VIP i transfery \| Rezerwacja WhatsApp | Wycieczki VIP w Hurghadzie, bez przedplaty | index,follow,... | self |
| `/ro/` | KeRo Tours Hurghada - Excursii VIP si transferuri \| Rezervare WhatsApp | Excursii VIP in Hurghada, fara avans | index,follow,... | self |

- Indexing is **ON** (`ALLOW_INDEXING=True`). (It was `noindex,follow` until 2026-10-26; any Quality Score read taken before that date reflects a page Google could crawl but was told not to index - see report 05.)
- hreflang present and reciprocal on every page: `fr`, `pl`, `ro`, `x-default` -> FR. Verified on `/pl/` and `/pl/wycieczki/dolphin-house/` (each lists all four alternates with absolute URLs).
- Canonicals are self-referential per localized page (no cross-language collapse).
- JSON-LD graph present (WebSite, TravelAgency, WebPage, BreadcrumbList, TouristTrip+Offer). SEO category score 100/100 in Lighthouse.

## 4. Performance baseline - Lighthouse mobile, live `/pl/` (lab, throttled)

Tool: Lighthouse 11.7.1, mobile form factor, simulated throttling. Single run (GitHub Pages TTFB swings run-to-run on cache MISS).

| Metric | Value | Google "good" target |
|---|---|---|
| Performance score | **53** | 90+ |
| LCP (lab) | **12.9 s** | <= 2.5 s |
| FCP (lab) | 7.5 s | <= 1.8 s |
| Speed Index | 19.0 s | - |
| TBT (lab) | 160 ms | < 200 ms |
| CLS | 0.013 | <= 0.1 |
| Server response (TTFB) | **2,290 ms** | < 600 ms |
| Total transferred | 941 KiB | - |

Top Lighthouse opportunities: reduce server response time (2.29 s), reduce unused JavaScript (58 KiB, = the Google Ads `gtag.js`), properly size images (168 KiB).

Diagnosis: **LCP and FCP are dominated by TTFB** (origin fetch on Fastly cache MISS). TBT and CLS are already good. Real-world edge TTFB measured separately with curl was ~0.6 s (warm EU edge), so the 2.29 s is a cold-MISS lab figure - but even the warm case plus render-blocking CSS keeps LCP above target on throttled mobile. The single biggest controllable lever is **fronting Pages with a CDN** (see report 03 and 08); it is an owner-side DNS action.

## 5. Accessibility / best-practices baseline (Lighthouse mobile, live `/pl/`)

| Category | Score | Notes |
|---|---|---|
| Accessibility | 86 | Failures: color-contrast (active language pill), heading-order (`<h4>` skip), aria-required-children (`social__row role="list"`). |
| Best practices | 74 | Failures: errors-in-console (meta CSP `frame-ancestors` ignored), third-party cookies (Clarity/Ads), inspector-issues. |
| SEO | 100 | - |

All three accessibility failures and the console error are **repo-fixable** and were fixed this session (report 02). The third-party-cookie best-practices items are structural (owner's analytics/ads) and are documented in report 08.

## 6. Tracking baseline (verified in source + live)

- Google Ads tag `AW-18538088460` present on all content pages (async). One conversion action "KeRo \| WhatsApp Contact" (`HOYlCNeOq6odEIyQ04dF`). No GA4, no GTM.
- Google Consent Mode v2: EEA/UK/CH denied by default (cookieless), granted elsewhere. No cookie banner.
- Microsoft Clarity `z4klch73ka` (heatmaps/recordings), CSP-allowed, input masked.
- WhatsApp number integrity: `201288808645` present on all pages (33 refs/homepage); the Meta-campaign number `201278378685` appears **zero** times. Correct separation maintained.

## 7. Summary of baseline problems

| # | Problem | Severity | Fixable where |
|---|---|---|---|
| 1 | TTFB / LCP on throttled mobile (GitHub Pages origin) | High (drives Landing Page Experience) | Owner (CDN) |
| 2 | Meta CSP `frame-ancestors` console error (best-practices) | Medium | Repo - FIXED |
| 3 | Accessibility: contrast, heading-order, aria children | Medium | Repo - FIXED |
| 4 | Unused JS 58 KiB (= Ads gtag) | Low (needed for conversions) | Keep - documented |
| 5 | 8 excursion/homepage titles > 70 chars | Low (cosmetic SERP truncation) | Repo - documented |
| 6 | No custom security response headers (HSTS beyond apex, X-Frame-Options) | Low | Owner (CDN) |
| 7 | Business legal info (licence, address, email) empty | Medium (trust) | Owner to supply |

No Priority-0 (broken functionality / wrong number / wrong price / mis-indexing) issues were found on the live site.
