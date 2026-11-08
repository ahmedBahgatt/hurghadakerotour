# 07 - QA and Deployment Report

Date: 2026-11-08.

## Build / gate status (local, this session)

| Gate | Result |
|---|---|
| `python3 build.py` | OK - 38 pages, 11 tours, 57 gallery images, WhatsApp `201288808645`. Reproducible. |
| `scripts/check.py` | 38 HTML files, 0 problems. |
| `scripts/test_seo.py` | 36 content pages, 0 problems (8 pre-existing title > 70 warnings - report 04). |
| `scripts/test_whatsapp.py` | 39 files, 0 problems. New number present everywhere, old number nowhere. |
| `scripts/test_analytics.py` | 37 pages, 0 problems. Ads tag + Consent Mode + CSP host allowlist intact. |
| secret-scan | (runs in CI before build) - no secrets added this session. |

## Functional QA (verified against the live site this session)

| Check | FR | PL | RO |
|---|---|---|---|
| Homepage HTTP 200 | yes | yes | yes |
| `index,follow` robots | yes | yes | yes |
| Self canonical | yes | yes | yes |
| Reciprocal hreflang (fr/pl/ro/x-default) | yes | yes | yes |
| H1 present, parallel copy | yes | yes | yes |
| WhatsApp number `201288808645` | 33 refs | 33 refs | 33 refs |
| Old Meta number `201278378685` | 0 | 0 | 0 |
| Google Ads tag `AW-18538088460` | - | yes | - |

- All 36 canonical URLs (3 homepages + 33 tour pages) return HTTP 200 (full sitemap crawl).
- `404.html` = 200 (serves the branded 404), `robots.txt` = 200, `sitemap.xml` = 200, `/hu/` = 404 (expected).

## Accessibility / best-practices QA (Lighthouse 11.7.1, mobile)

- Live `/pl/` before: a11y 86, best-practices 74.
- Built `dist/` after the four fixes (local server, network-independent audits): **a11y 100**, best-practices 78, SEO 100. `color-contrast`, `heading-order`, `aria-required-children`, `errors-in-console` all pass.

## Deployment status

**BUILT, GATED, NOT YET PUSHED.** The changes exist in the working tree and in `dist/`
(39 files rebuilt) on branch `main`, local HEAD still equal to the previously deployed
commit. Nothing has been committed or pushed to `origin/main` this session.

Rationale: this is a live, ad-connected production site. Per standing instructions, the
production push (which triggers the GitHub Actions deploy and changes the live site) is
held for an explicit owner go/no-go. The change set is low-risk (two source files; a11y +
a dead CSP directive removal; no content/price/number/schema change) and all gates pass.

### To deploy (on go-ahead)

1. `cd` to the repo, confirm `git status` shows only `build.py`, `assets/css/styles.css`, and rebuilt `dist/**`.
2. Tag a rollback point: `git tag pre-a11y-csp-2026-11-08`.
3. Commit (message describing the four fixes) and `git push origin main`.
4. GitHub Actions runs secret-scan + build + `check.py` + deploy.
5. Post-deploy live verification:
   - `curl -I` the FR/PL/RO homepages (expect 200).
   - Confirm `frame-ancestors` is gone from the live HTML and there are zero CSP console errors (real Chrome).
   - Confirm the active language pill now uses the darker teal and footer titles are `<h3>`.
   - Re-run Lighthouse mobile on live `/pl/` to capture after-numbers for a11y/best-practices (and perf, noting TTFB variance).
   - Confirm WhatsApp links still open `wa.me/201288808645` and the Ads tag still loads.

### Rollback

- Before deploy: `git checkout -- build.py assets/css/styles.css && python3 build.py`.
- After deploy: `git revert <commit>` (or checkout the `pre-a11y-csp-2026-11-08` tag tree), rebuild, push. Do NOT `reset --hard`/force-push a public branch.

## Environment limits encountered

- The dev browser renders at desktop width; mobile layout was validated via Lighthouse mobile emulation + prior-session iframe true-width checks, not a physical device.
- PageSpeed Insights / CrUX field data unavailable (public API quota 429, no key). No field metrics are reported.
- No AVIF encoder on this machine (AVIF image path deferred).
- No Google Ads / Search Console account access (those items are recommendations, not changes).
