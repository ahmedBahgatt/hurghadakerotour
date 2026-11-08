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

---

## Round 2 (2026-11-08) - performance + tracking + titles

### Changes (on top of commit `80fb47f`)

- `build.py`: inline all CSS; defer `config.js`; preload the homepage hero (LCP).
- `assets/js/app.js`: validated GCLID/gbraid/wbraid capture + conditional `Ref:` line.
- `data/i18n.py`: title suffix ` | KeRo Tours Hurghada` -> ` | KeRo Tours`.
- Docs `01..09` updated to final state.

### Gates (all green after rebuild)

check 38/0; test_seo 36/0 (2 title warnings, down from 8); test_whatsapp 39/0; test_analytics 37/0.

### Measurement (local dist, mobile throttled, render path)

| Page | Perf | A11y | LCP | FCP | SI | CLS |
|---|---|---|---|---|---|---|
| FR `/fr/` | 93 | 100 | 2.9 s | 1.4 s | 4.0 s | 0 |
| PL `/pl/` | 90 | 100 | 3.3 s | 1.8 s | 3.0 s | 0.013 |
| RO `/ro/` | 90 | 100 | 3.3 s | 1.8 s | 2.6 s | 0 |

Render-blocking resources: 0 (was fonts.css + styles.css + config.js). EU-edge curl TTFB
0.2-0.6 s (`x-cache: HIT`). No field (CrUX) data available; none invented.

### Deployment status (round 2) - DEPLOYED + LIVE-VERIFIED 2026-11-08

Integration: origin/main had advanced by one concurrent commit `b8db644` (another session's
hreflang x-default fix). This work was rebased on top of it (no force, no discard). One real
source conflict - both sides edited the same `head()` call in `build_home()` - resolved by
keeping BOTH (x-default=/fr/ from them, hero preload from this work); `dist/sitemap.xml` was
regenerated by a clean rebuild. Result: linear history, fast-forward ready (0 remote-only).

Push: `git push origin main` succeeded (`b8db644..3e09afc`, fast-forward). Rollback tag
`pre-deploy-2026-11-08` = `b8db644` pushed. GitHub Actions run `42505036362` = success
(Verify-and-build: secret-scan + build + check.py + all regression gates; Deploy-to-Pages).

Final commits on live `main`: `02a18ec` (a11y), `be1dcf5` (perf/GCLID), `d7d3ddc` (handoff),
`3e09afc` (sitemap rebuild), on top of `b8db644`.

### Live verification (done this session)

- FR/PL/RO + root = HTTP 200; `last-modified` = 2026-11-08; `x-cache: HIT`; TTFB 0.21-0.30 s.
- Live HTML confirmed: inline `<style>`, hero image preload, deferred `config.js`, NO external
  `styles.css` link, `x-default -> /fr/`, canonical self-ref, `index,follow`, WhatsApp
  `201288808645` (old `201278378685` absent), Ads tag `AW-18538088460`.
- `sitemap.xml` 200 with 36 URLs; GCLID capture present in live `app.js`.
- Live Lighthouse PL mobile: perf 91, a11y 100, best-practices 78, SEO 93, LCP 3.2 s,
  FCP 1.7 s, TBT 70 ms, CLS 0.013, TTFB 250 ms, 0 render-blocking resources.
- This confirms the earlier "12.9 s LCP / 53 perf" live run was a local-measurement artifact.

Remaining browser-only check (optional): load `/pl/?gclid=TEST123`, submit the booking form,
confirm the WhatsApp text ends with `Ref: TEST123` (and no `Ref:` without a gclid). The
capture code is verified present in the live `app.js`; this just exercises it in a browser.

### Post-deploy live verification (to run after the push)

- `curl -I` FR/PL/RO homepages (expect 200); confirm `x-cache` and gzip.
- Confirm the live HTML has the inline `<style>`, deferred `config.js`, hero image preload,
  no external `styles.css`/`fonts.css` link, and zero console errors (real Chrome).
- Re-run Lighthouse mobile on live `/pl/`, `/fr/`, `/ro/` + a Cairo/Dolphin tour page; record
  perf/LCP/CLS/TBT (expect numbers close to the local-dist render-path figures, better TTFB).
- GCLID: load `/pl/?gclid=TEST123`, open the booking form, submit, confirm the WhatsApp text
  ends with `Ref: TEST123`; load `/pl/` with no gclid and confirm NO `Ref:` line.
- Confirm WhatsApp opens `wa.me/201288808645`; language switcher; Ads tag still loads.
