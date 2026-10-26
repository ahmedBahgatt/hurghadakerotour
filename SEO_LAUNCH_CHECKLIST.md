# SEO Launch Checklist - Hurghada KeRo Tours & Transfer

Date prepared: 2026-10-26.

> **STATUS 2026-10-26 - INDEXING ENABLED (owner authorized).**
> `ALLOW_INDEXING=True` is live. All **36** localized canonical content pages
> (3 homepages + 33 excursion pages) now emit
> `index,follow,max-image-preview:large`; root `/` canonicalizes to `/fr/`; the
> 404 stays `noindex`. Built, all gates green, pushed to `main`, GitHub Actions
> deploy succeeded, and the live directives/robots.txt/sitemap were verified.
> **Steps 1-5 below are DONE.** The remaining manual, owner-only actions are
> **Google Search Console verification + sitemap submission (step 6)** and
> **step 7-8 monitoring** - these require the owner's Google account and the
> Hostinger DNS panel, so they are not automatable from the repo.

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

## 6. Google Search Console (and optionally Bing) - OWNER ACTION

Two ways to verify. **Domain property (DNS TXT)** is recommended because it
covers http/https + www + apex in one shot. Do NOT fabricate a token - Google
generates the real one in the console and it must be pasted exactly.

### Option A - Domain property via Hostinger DNS TXT (recommended)
1. In [Search Console](https://search.google.com/search-console) -> *Add
   property* -> **Domain** -> enter `hurghadakerotour.com` (no https, no path).
2. Google shows a line like `google-site-verification=XXXXXXXXXXXXXXXXXXXXXXXX`.
   Copy the **exact** value Google gives you (this repo does not and must not
   invent it).
3. In **Hostinger -> Domains -> hurghadakerotour.com -> DNS / Nameservers**, add a
   record:
   - **Type:** `TXT`
   - **Name / Host:** `@`  (the apex; Hostinger may show it as blank/`@`)
   - **Value / TXT content:** the full `google-site-verification=...` string
   - **TTL:** default (e.g. 3600)
   Keep the existing 4 apex `A` records and the `www` CNAME untouched - just add
   this TXT alongside them.
4. Wait for DNS propagation (minutes to a few hours), then click **Verify**.
   Check from CLI: `dig +short TXT hurghadakerotour.com` should list the string.

### Option B - URL-prefix via HTML meta tag (alternative)
1. Add property -> **URL prefix** -> `https://hurghadakerotour.com`.
2. Choose the *HTML tag* method; copy the `content="..."` token.
3. Put it in `site_config.py` -> `GOOGLE_SITE_VERIFICATION = "<token>"`, rebuild
   (`python3 build.py`), commit, push (the generator already emits the
   `<meta name="google-site-verification">` tag on every page when set), wait for
   deploy, then click **Verify**. (Bing: same pattern via `BING_SITE_VERIFICATION`.)

### Submit the sitemap (after verification)
- [ ] Search Console -> *Sitemaps* -> submit `sitemap.xml` (full URL
      `https://hurghadakerotour.com/sitemap.xml`). It lists all 36 canonical URLs
      + image entries + FR/PL/RO hreflang alternates.

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

## Status of adjacent items

- **Google Ads conversion tracking - DONE (2026-10-26).** The live tag
  `AW-18538088460` and the single conversion `KeRo | WhatsApp Contact`
  (`.../HOYlCNeOq6odEIyQ04dF`) are installed and live-verified. See
  `ANALYTICS_PRIVACY.md`. **No ad campaign is launched and no budget is set** -
  that remains a separate owner decision. GA4 is intentionally **not** installed
  (`GA4_MEASUREMENT_ID` empty); no GTM container.
- Confirm in Google Ads (Tools -> Conversions) that the tag is recognized and a
  test conversion was received before relying on it. Lion Cub stays
  `LION_CUB_ADS_ELIGIBLE=False` - never an ad landing page until its review.

## Explicitly NOT part of this launch (separate owner decisions)

- Launching Google Ads campaigns / setting budgets.
- Sanity CMS integration (postponed).
- Lion Cub as a paid landing page (blocked until its compliance review).
- Deleting the old repo `kero-tours-landing` / `kero-tours-hurghada.pages.dev`
  (only with permission).

## Rollback

Set `ALLOW_INDEXING = False`, rebuild, redeploy - every page returns to
`noindex,follow`. Fully reversible.
