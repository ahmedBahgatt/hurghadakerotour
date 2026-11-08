# 04 - Multilingual SEO Audit (FR / PL / RO)

Date: 2026-11-08. Verified against the live site and the generator source. All three
languages are treated as equal production targets.

## Indexability

- Every one of the 36 canonical content pages emits `index,follow,max-image-preview:large` (verified live on FR/PL/RO homepages and sampled tour pages).
- `robots.txt`: `User-agent: * / Allow: /` + `Sitemap: https://hurghadakerotour.com/sitemap.xml`. Correct.
- `404.html` is `noindex` (hard-coded), not in the sitemap. Correct.
- Root `/` serves the FR homepage and canonicalises to `/fr/` (no duplicate indexable root).
- `/hu/` returns 404 (Hungarian intentionally not present; out of scope per brief).

Note on history: indexing was `noindex,follow` until 2026-10-26. Any Google Ads Quality
Score / Landing Page Experience reading captured before that date reflects a page Google
was told not to index. Current state is correct; diagnostics should be re-read now that
pages are indexable (see report 05).

## Canonical tags

- Each localized page is self-canonical (e.g. `/pl/wycieczki/dolphin-house/` canonicals to itself).
- No cross-language canonical collapse (translations are not pointed at one language).
- Verified: `/pl/`, `/pl/wycieczki/dolphin-house/`, FR/RO homepages.

## hreflang

- Reciprocal cluster on every page: `fr`, `pl`, `ro`, and `x-default` -> FR.
- Absolute URLs, correct per-tour slug mapping (e.g. dolphin-house: `/fr/excursions/dolphin-house/`, `/pl/wycieczki/dolphin-house/`, `/ro/excursii/dolphin-house/`).
- Language-only targeting (no `fr-FR`/`ro-RO` region codes) - intentional: French/Polish/Romanian speakers are not country-bound (Belgium, Switzerland, Moldova, etc.). Documented in `SEO_AUDIT.md`.
- No alternates point to non-existent or redirected pages (all 36 URLs are 200).

## XML sitemap

- `sitemap.xml` is valid, lists the 36 canonical URLs + an image sitemap block, `lastmod` present.
- No noindex pages, no 404s, no redirected or non-canonical entries (crawl: all 36 = 200).
- `robots.txt` references the sitemap correctly.

## Metadata

- Unique per-page, per-language titles and meta descriptions (verified FR/PL/RO homepages + dolphin page). Descriptions are purpose-written per tour in `data/seo.py`, not truncated intros.
- One H1 per page; parallel across languages (e.g. "Excursions VIP a Hurghada, sans acompte" / "Wycieczki VIP w Hurghadzie, bez przedplaty" / "Excursii VIP in Hurghada, fara avans").
- Open Graph + Twitter cards: per-tour 1200x630 images with `og:image:alt`, `og:locale` + `og:locale:alternate`; homepage uses the branded logo card.
- Image ALT text: accurate, localized, per-image for all gallery images (`data/seo.py`), verified in prior SEO pass.

### Minor finding: 8 titles exceed ~70 characters

These are warnings (not errors) from `test_seo.py`; they risk SERP truncation but do not harm indexing or relevance:

- fr: homepage; Cairo/GEM (84); Luxor (74); Three Islands (77).
- pl: Cairo/GEM (76); Three Islands (76).
- ro: Cairo/GEM (79); Three Islands (77).

Recommendation (P2, not done this session to avoid untested copy changes on a live ad site): shorten the Cairo and Three Islands titles in `data/seo.py` for all three languages (e.g. drop the trailing brand suffix on the longest ones). Must be re-validated with `test_seo.py` and visually in all three languages.

## Structured data

- Single JSON-LD `@graph` per page linking `WebSite` (#website), `TravelAgency` (#business), `WebPage`, `BreadcrumbList`, and per tour `TouristTrip` + `Offer` + `UnitPriceSpecification`.
- Prices come from `data/tours.py` (structured == visible == source), EUR, per person; the private speedboat is modelled per boat (base 2-5), never per person.
- No `Offer.availability`/`InStock` (bookings are WhatsApp-confirmed, no live inventory). No `GeoCoordinates`/`PostalAddress` (no verified premises). No fake ratings/reviews/opening hours. `areaServed: Hurghada`, brand, telephone, `sameAs` socials retained.
- FAQ markup is present but Google no longer shows FAQ rich results for most sites - kept as valid markup, not expected to produce a rich snippet.
- Lighthouse SEO category = 100/100 on sampled pages.

## Internal linking

- Homepages link to all 11 tours (4 category sections) and to booking/why/FAQ/contact.
- Tour pages link to 3 related tours (same category), breadcrumb back to category/home.
- Language-specific links stay within-language (PL links to PL pages, etc.).
- No orphan canonical pages: every sitemap URL is reachable from navigation (header dropdown/drawer + homepage sections + related-tour blocks).

## Verdict by language

FR, PL and RO are **technically ready for organic SEO**: indexable, canonical-correct, reciprocally hreflang-linked, individually titled/described, schema-valid, and internally linked. The remaining organic-ranking variables (content depth vs competitors, backlinks, and Google's own crawl/indexing decisions) are outside code control; making pages eligible does not guarantee indexing or ranking.

Owner-only next step: verify the property in Google Search Console (DNS-TXT) and submit the sitemap (`SEO_LAUNCH_CHECKLIST.md` step 6). Not done here (requires DNS access).
