# SEO Launch Checklist - Hurghada KeRo Tours & Transfer

Date prepared: 2026-10-26. **Do NOT execute these steps now.** Indexing is
intentionally off (`ALLOW_INDEXING=False`). This is the documented sequence to run
**only when the owner explicitly authorizes indexing.**

---

## 0. Pre-conditions (owner sign-off) - BEFORE flipping anything

- [ ] Owner approves the published content and prices across FR/PL/RO.
- [ ] Owner supplies real business identity (then add to `site_config.py`
      `BUSINESS`; never fabricate): **legal name, street address, tourism licence
      number, public email.** These unlock richer `TravelAgency` schema and footer
      trust info; they are optional for indexing but recommended for trust.
- [ ] Compliance review where needed:
      - **Lion Cub** experience: legal + animal-welfare + facility + ad-policy
        review signed off before it is ever used as a Google Ads landing page.
        Keep `LION_CUB_ADS_ELIGIBLE=False` until then (indexing the page organically
        is already allowed by the owner's decision to publish it).
- [ ] Image rights confirmed for paid use (owner-asserted today): go-kart tile 05
      (generic indoor), lion-cub + speedboat frames, and any Egipskie-sourced
      photos whose licence must cover this domain.

## 1. Flip indexing (single central switch)

- [ ] In `site_config.py` set `ALLOW_INDEXING = True`.
      Effect: every page emits `index,follow,max-image-preview:large` instead of
      `noindex,follow`. Nothing else needs editing - it is the one switch.
- [ ] (Optional) set `GOOGLE_SITE_VERIFICATION` (and/or `BING_SITE_VERIFICATION`)
      in `site_config.py` once you have the token (see step 6).

## 2. Rebuild & verify locally

- [ ] `python3 build.py`
- [ ] `python3 scripts/check.py` (HTML/JSON-LD/canonical/stale-domain gate)
- [ ] `python3 scripts/test_whatsapp.py` (contact-number gate)
- [ ] `python3 scripts/test_seo.py` - **after the flip this now asserts
      `index,follow,max-image-preview:large`** on every content page (the test
      reads `ALLOW_INDEXING` and checks the matching directive). 0 problems expected.

## 3. Deploy

- [ ] Commit and push to `main`. GitHub Actions
      (`.github/workflows/deploy.yml`) runs secret-scan + build + all three QA
      gates, then deploys to GitHub Pages.
- [ ] Confirm the Actions run is green.

## 4. Verify published directives & canonicals (live)

- [ ] `curl -s https://hurghadakerotour.com/fr/ | grep -i robots` -> should show
      `index,follow,max-image-preview:large`.
- [ ] Spot-check canonicals on `/fr/`, `/pl/`, `/ro/` and one tour per language.
- [ ] Confirm `https://hurghadakerotour.com/robots.txt` allows crawl and lists the
      sitemap; `https://hurghadakerotour.com/sitemap.xml` loads (URLs + images +
      hreflang alternates).
- [ ] Confirm HTTPS is enforced.

## 5. Structured-data validation (now that pages are fetchable without noindex)

- [ ] Run representative URLs through the
      [Rich Results Test](https://search.google.com/test/rich-results) - expect
      **Breadcrumbs** eligible on tour pages. FAQ is no longer reported (deprecated).
- [ ] Run through the [Schema.org Validator](https://validator.schema.org/) -
      expect 0 errors.

## 6. Google Search Console (and optionally Bing)

- [ ] Add the property for `https://hurghadakerotour.com` (domain property via DNS
      TXT is cleanest; or URL-prefix via the HTML-tag token -> paste into
      `GOOGLE_SITE_VERIFICATION`, rebuild, deploy, verify).
- [ ] Submit `https://hurghadakerotour.com/sitemap.xml`.

## 7. Inspect & request indexing (representative URLs)

- [ ] URL Inspection on `/fr/`, `/pl/`, `/ro/` + one tour per language. Confirm
      "URL is on Google: eligible / indexing allowed".
- [ ] Request indexing for the key landing pages.

## 8. Monitor

- [ ] Coverage/Pages report: indexed vs excluded, any `noindex`/canonical issues.
- [ ] Enhancements: Breadcrumbs; Merchant/Product report **not expected** for this
      service site (do not treat its absence as a bug - see `SCHEMA_AUDIT.md`).
- [ ] Core Web Vitals (field) report once data accrues - LCP/CLS/INP.
- [ ] Performance report: branded ("KeRo Tours") vs non-branded queries, per
      language/market; impressions/clicks for the primary keywords in
      `SEO_KEYWORD_MAP.md`.

---

## Explicitly NOT part of this launch (separate owner decisions)

- Google Ads activation / conversion tracking (`GOOGLE_ADS_ID`,
  `GOOGLE_ADS_CONVERSION_LABEL`) and GA4 (`GA4_MEASUREMENT_ID`) - config
  placeholders exist and inject nothing while empty.
- Sanity CMS integration (postponed).
- Lion Cub as a paid landing page (blocked until its compliance review).
- Deleting the old repo `kero-tours-landing` / `kero-tours-hurghada.pages.dev`
  (only with permission).

## Rollback

Set `ALLOW_INDEXING = False`, rebuild, redeploy - every page returns to
`noindex,follow`. Fully reversible.
