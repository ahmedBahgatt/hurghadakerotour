# 02 - Implemented Fixes

Date: 2026-11-08. All changes are in `build.py` and `assets/css/styles.css` (source),
rebuilt into `dist/` (39 files). All four CI gates pass. Not yet pushed to production
(see report 07 for deployment status).

Scope discipline: this session extends the existing, already-optimized project. No
rebuild, no content/price/number/schema changes, no redesign. Each fix below is tied to
a specific measured Lighthouse failure from the baseline (report 01).

## Fix 1 - Remove ineffective `frame-ancestors` from the meta CSP

- File: `build.py` (CSP string).
- Before: `... frame-src ...; frame-ancestors 'none'; base-uri 'self'; form-action 'self'`
- After: `... frame-src ...; base-uri 'self'; form-action 'self'` (+ explanatory comment).
- Why: `frame-ancestors` is **ignored by browsers when delivered via `<meta>`** (per CSP spec). It did nothing except emit a console error (`"The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element."`) that Lighthouse "best-practices" penalised via `errors-in-console`.
- Effect: `errors-in-console` now passes (0 nodes). No security regression - it never provided clickjacking protection on GitHub Pages (that needs an HTTP response header, which Pages cannot send). `base-uri` and `form-action` are retained (those DO work in meta).
- Clickjacking note: to actually set `frame-ancestors` / `X-Frame-Options`, front the site with a CDN that can send response headers (report 08).

## Fix 2 - `social__row` ARIA role (`list` -> `group`)

- File: `build.py` (`social_links()`).
- Before: `<div class="social__row" role="list" aria-label="...">` with `<a>` children.
- After: `<div class="social__row" role="group" aria-label="...">`.
- Why: `role="list"` requires children with `role="listitem"`; the children are links, so Lighthouse `aria-required-children` failed. `role="group"` with an `aria-label` is a valid labelled grouping with no required-children constraint, and preserves the "Follow us" semantics without stripping link semantics from the icons.
- Effect: `aria-required-children` no longer applies (clean). Applied to all 37 content pages (footer, drawer, contact card).

## Fix 3 - Footer heading level (`<h4>` -> `<h3>`)

- Files: `build.py` (footer template), `assets/css/styles.css` (`.footer h4` -> `.footer h3`, `.footer__col h4` -> `.footer__col h3`).
- Why: the footer column titles were `<h4>`, following section `<h2>`s with no intervening `<h3>` - Lighthouse `heading-order` flagged the skipped level. Visual styling is unchanged (the CSS selectors were moved with the tag).
- Effect: `heading-order` passes. Document outline is now h1 -> h2 -> h3 with no skips.

## Fix 4 - Active language pill contrast (AA)

- File: `assets/css/styles.css`.
- Before: `.langswitch a[aria-current="true"] { background: var(--sea); color: #fff; }` - white on `#0bb4c4` = **2.5:1** (fails WCAG AA; small bold text needs 4.5:1).
- After: `background: var(--sea-deep)` - white on `#077a8a` = **5.06:1** (passes AA).
- Why: the current-language pill is the only element Lighthouse `color-contrast` flagged. `--sea-deep` is the existing brand dark-teal, so the change is on-brand and affects only the active pill state.
- Effect: `color-contrast` passes.

## Verified result on the built `dist/` (Lighthouse 11.7.1, mobile, local server)

| Category | Baseline (live) | After (built dist) |
|---|---|---|
| Accessibility | 86 | **100** |
| Best practices | 74 | 78 (residual = third-party cookies from Clarity/Ads + meta-CSP; structural, see report 08) |
| SEO | 100 | 100 |
| `color-contrast` | fail | pass |
| `heading-order` | fail | pass |
| `aria-required-children` | fail | pass (n/a) |
| `errors-in-console` | fail | pass |

Performance score is intentionally not compared on the local server (localhost has no realistic TTFB). The performance lever is TTFB/CDN (report 03), which these source edits do not change and do not claim to.

## CI gates (all green after rebuild)

- `scripts/check.py`: 38 HTML files, 0 problems.
- `scripts/test_seo.py`: 36 content pages, 0 problems (8 pre-existing title > 70 char warnings, unrelated to this change - report 04).
- `scripts/test_whatsapp.py`: 39 files, 0 problems (number `201288808645` everywhere, old number nowhere).
- `scripts/test_analytics.py`: 37 pages, 0 problems (Ads tag + Consent Mode + CSP host allowlist intact).

## Unchanged (verified)

Content, 11 EUR prices, FR/PL/RO text and diacritics, WhatsApp number `201288808645`, Google Ads `AW-18538088460` + label `HOYlCNeOq6odEIyQ04dF`, Microsoft Clarity, canonical/hreflang/robots, deposit policy (Cairo/Luxor 50%), JSON-LD, layout, `LION_CUB_ADS_ELIGIBLE=False`.

## Rollback

Source changes are two files; `git checkout -- build.py assets/css/styles.css && python3 build.py` restores the prior build. A tag can be created at the pre-change commit before deploy (report 07).
