# SEO / GEO / AEO / AIO Audit - Hurghada KeRo Tours & Transfer

Date: 2026-10-26. Scope: the entire generated static site (FR / PL / RO + root).
Method: whitebox review of the generator (`build.py`, `data/*.py`, `site_config.py`)
cross-checked against the actual built HTML in `dist/`, plus automated gates
(`scripts/check.py`, `scripts/test_whatsapp.py`, `scripts/test_seo.py`).

> Indexing is intentionally OFF. Every page emits `<meta name="robots"
> content="noindex,follow">` via `ALLOW_INDEXING=False`. This audit prepares the
> site for indexing; it does NOT authorize it. Do not flip the flag without the
> owner's explicit approval (see `SEO_LAUNCH_CHECKLIST.md`).

---

## A. Executive summary

- **SEO readiness:** technically ready for indexing once the owner approves. All
  on-page signals, structured data, hreflang, Open Graph, image SEO and a
  regression test suite are in place.
- **Pages audited:** 38 generated files = root `/` (French homepage, canonical
  `/fr/`) + 3 localized homepages + 33 excursion pages (11 tours x FR/PL/RO) +
  `404.html`. Indexable content pages = **36** (3 homepages + 33 tours).
- **Pages updated this pass:** all 36 content pages (metadata, schema, OG, image
  ALT) + sitemap + the generator + data layer.
- **Languages:** French (default), Polish, Romanian. No English in public text.
- **Critical issues fixed:**
  1. **Per-image ALT text** was generic (`"<tour name> - 1/2/3"`). Replaced with
     accurate, localized, per-image descriptions of the real subject in all three
     languages (57 images x 3 = 171 ALT strings), verified against the images and
     `IMAGE_AUDIT.md`. No cross-tour mislabeling (Orange Bay != Magawish; wild vs
     captive dolphins; the generic indoor karting frame is not tied to El Gouna).
  2. **Open Graph image was the logo on every page**, including tours. Tour pages
     now use a per-tour 1200x630 social card (`/assets/img/og/<id>.jpg`); added
     `og:image:alt`, `og:locale:alternate`, and Twitter `title/description/image`.
  3. **Structured data rebuilt** from a loose `Product` into a coherent, honest
     entity graph: `TouristTrip` (correct type for a guided day trip) + `Offer`
     with a localized `UnitPriceSpecification`, linked to the operator
     (`TravelAgency`) by a stable `@id`, plus `WebPage` and `BreadcrumbList`
     nodes. The private speedboat is modeled **per boat** (never per person).
  4. **Per-tour meta descriptions** now purpose-written (was a truncated intro
     with a mid-word "...").
  5. **Image sitemap** added (Google Images discovery) alongside the existing
     hreflang sitemap.
  6. **SEO regression suite** (`scripts/test_seo.py`) added and wired into CI so
     future content edits cannot silently break these signals.
- **Issues remaining (owner input / future):** business legal identity
  (legal name, street address, tourism licence, public email) still empty - not
  fabricated; some gallery images are modest resolution; the go-kart tile 05 and
  speedboat/lion-cub image rights are owner-asserted (confirm before paid ads).
  Indexing, Search Console, analytics and Sanity remain intentionally off.

---

## B. Per-URL audit (20 checkpoints)

Status key: OK = correct; FIXED = corrected this pass; N/A = not applicable;
HOST = limited by GitHub Pages; OWNER = needs owner-supplied data.

| # | Checkpoint | Homepages (FR/PL/RO) | Excursion pages (33) | Notes |
|---|---|---|---|---|
| 1 | HTTP status / canonical | OK | OK | Self-referencing canonical; root `/` canonicalizes to `/fr/`. |
| 2 | Robots directives | OK | OK | `noindex,follow` (intended lock). `robots.txt` allows crawl so the directive is readable. |
| 3 | Title tag quality | FIXED | FIXED | Unique per language; brand suffix; price in tour titles. 8 titles > 70 chars (proper-noun names) - acceptable; Google may truncate. |
| 4 | Meta description | FIXED | FIXED | Purpose-written, localized, 147-165 chars. Unique within each language. |
| 5 | H1 / heading hierarchy | OK | OK | Exactly one H1 per page (enforced by `check.py` + `test_seo.py`); H2/H3 structured sections. |
| 6 | Search intent | OK | OK | Homepage = Hurghada excursion catalog; each tour = one distinct intent. See `SEO_KEYWORD_MAP.md`. |
| 7 | Keyword targeting | OK | OK | One primary keyword per page/language; cannibalization avoided (quad vs super safari, three-islands vs orange-bay+hula, dolphin vs speedboat, Cairo vs Luxor). |
| 8 | Semantic completeness | OK | OK | Tour pages answer what/where/included/price/booking/pickup/deposit; only confirmed facts. |
| 9 | Internal linking | OK | OK | Header dropdown, category sections, footer, breadcrumb, 3 related tours per page. Crawlable `<a href>`. |
| 10 | Image ALT | FIXED | FIXED | Accurate localized per-image ALT (was generic). Hero is decorative (AI composite) - empty ALT by design, see note below. |
| 11 | Image URLs / discoverability | FIXED | FIXED | Local WebP, crawlable paths, image sitemap added, high-res URLs in structured data. |
| 12 | Open Graph | FIXED | FIXED | Full OG incl. per-page image + `og:image:alt` + `og:locale:alternate`. |
| 13 | Twitter/X cards | FIXED | FIXED | `summary_large_image` + title/description/image/image:alt. |
| 14 | Structured data | FIXED | FIXED | See `SCHEMA_AUDIT.md`. Entity-linked graph; valid JSON-LD. |
| 15 | Hreflang / language | OK | OK | Reciprocal fr/pl/ro + x-default; `<html lang>` correct; each tour maps to the same tour in other languages. |
| 16 | Duplicate / near-duplicate | OK | OK | Root aliases `/fr/` via canonical (no duplicate signal). Cross-language pages differentiated by hreflang. |
| 17 | Page performance | OK | OK | Single CSS, deferred JS, responsive WebP, lazy-loading, LCP hero eager + `fetchpriority=high`, explicit dims (no CLS). See section E. |
| 18 | Mobile SEO | OK | OK | Responsive, mobile-first (verified previously at 320-414px); 44px tap targets. |
| 19 | Breadcrumbs | OK | OK | Visible breadcrumb + `BreadcrumbList` JSON-LD on every tour page. |
| 20 | Broken links / assets | OK | OK | `check.py` validates HTML + JSON-LD; `test_seo.py` checks referenced OG images exist + sitemap coverage. |

The machine-readable per-page detail is in `reports/seo-page-inventory.csv`
(36 content rows: url, lang, type, canonical, robots, primary keyword, title,
description, H1, schema types, OG image, hreflang, image counts, QA status).

---

## C. What was changed (implementation)

**Data layer**
- `data/seo.py` (new): `META_DESC` (purpose-written descriptions per tour x
  language) and `GALLERY_ALT` (per-image ALT per tour x language). Kept separate
  from the authoritative catalog in `data/tours.py` so prices/itineraries are
  untouched.

**Generator (`build.py`)**
- `head()` gains `og_image`, `og_image_alt`, `og_type`; emits `og:image:alt`,
  `og:locale:alternate` (the other two languages) and Twitter card fields.
- Structured data: new `sd_trip()` (TouristTrip + Offer + UnitPriceSpecification),
  `sd_webpage()` (WebPage node), stable `@id`s (`#business`, `#website`,
  `#trip`, `#breadcrumb`, `#webpage`); `TravelAgency` now emitted on tour pages
  too so `provider`/`seller` references resolve on-page. Removed the generic
  `Product` type.
- Gallery main image + thumbnails use the real localized ALT; `data-alts` passed
  to `assets/js/app.js` so the gallery swap and the lightbox announce the correct
  ALT (accessibility).
- Tour meta description taken from `META_DESC` (word-boundary fallback, no
  mid-word ellipsis).
- `build_sitemap()` adds the Google image-sitemap namespace and per-URL images.

**Assets**
- `assets/img/og/<id>.jpg`: 11 per-tour 1200x630 social cards (center-cropped
  from the existing covers via `sips`). Homepage keeps the branded `og-logo.png`.

**QA**
- `scripts/test_seo.py` (new) + wired into `.github/workflows/deploy.yml`.

---

## D. Notes on deliberate choices

- **Hero image is decorative.** The homepage hero is an owner-supplied AI
  panoramic composite, not a photograph of a specific real tour. To avoid
  misrepresenting generated art as a real tour photo (and because it sits behind
  the headline), it keeps `alt=""` + `aria-hidden="true"`. This is the honest and
  accessible choice; it is not a missing-ALT defect.
- **FAQPage markup kept, but no FAQ rich result is expected.** Google has
  **deprecated** FAQ rich results (the feature stopped appearing in Search on
  2026-05-07 and the documentation was removed 2026-06-15). The markup is still
  valid Schema.org, the Q&A is genuinely visible on the page, and it helps AI /
  answer engines understand the content, so it is retained for AEO value only.
  See `SCHEMA_AUDIT.md`.
- **TouristTrip, not Product.** A WhatsApp booking inquiry is not a purchasable
  product with checkout, so `Product`/merchant-listing markup is not appropriate
  and the site is not expected to be eligible for Google price snippets. See the
  pricing-eligibility discussion in `SCHEMA_AUDIT.md`.

---

## E. Performance (lab reasoning; no fabricated field data)

GitHub Pages serves static files over HTTPS/HTTP2 with a CDN. The templates are
already performance-conscious: one stylesheet, `app.js` deferred, Google Fonts
with `preconnect` + `display=swap`, responsive WebP with `srcset/sizes`, offscreen
images `loading="lazy"`, the LCP hero `fetchpriority="high"` + eager with explicit
`1672x941` dimensions (prevents CLS). No analytics/third-party scripts are loaded
(IDs empty). No render-blocking JS.

Not measured here: real Lighthouse scores and field Core Web Vitals (LCP/CLS/INP).
Do not quote a lab score as field data. Run Lighthouse on the production URL and,
after indexing is enabled, read the Search Console Core Web Vitals (field) report.
See `SEO_LAUNCH_CHECKLIST.md`.

**Host limitation (not a defect):** GitHub Pages cannot set custom HTTP response
headers, so response-level CSP/HSTS/X-Frame-Options are not available. The site
uses per-page `<meta>` CSP + Referrer-Policy as the best available substitute.
Fronting the site with Cloudflare would enable real response headers later.

---

## F. Verification status (this pass, local build)

- `python3 build.py` -> 38 pages, 57 gallery images.
- `python3 scripts/check.py` -> 38/38 HTML valid, canonical present, 0 stale
  domains, valid JSON-LD.
- `python3 scripts/test_whatsapp.py` -> 39 files, 0 problems.
- `python3 scripts/test_seo.py` -> 36 content pages, 0 problems (8 title-length
  warnings, informational).
- `ALLOW_INDEXING=False` confirmed: every content page emits `noindex,follow`.

Production verification (live HTML/meta/schema on hurghadakerotour.com) is done
after the change is pushed and GitHub Actions deploys - see the final report in
`HANDOFF.md`.
