# 09 - Final Executive Report (round 2)

Date: 2026-11-08. Site: https://hurghadakerotour.com (FR / PL / RO). Production source:
`github.com/ahmedBahgatt/hurghadakerotour` (static Python generator, GitHub Pages + Fastly).

## Context

The production site is a Python static-site generator on GitHub Pages (not WordPress/
Webflow/Next.js), already heavily optimized by prior work. Two rounds of work this cycle:
round 1 = accessibility + a dead-CSP console fix (commit `80fb47f`); round 2 = a deeper
performance investigation + real render-path fixes + offline-attribution tracking + title
cleanup. Correct production repo used throughout (not the retired landing-page repos or
`egipskiewakacje.pl`).

## 1. All issues discovered

- The headline "12.9 s LCP / 2.29 s TTFB" from the first live Lighthouse run was a
  **local-measurement artifact**. Real EU-edge TTFB is 0.2-0.6 s (`x-cache: HIT`, gzip,
  HTTP/2); the clean render-path score is Performance 85 / LCP 3.5 s.
- Render path had removable waste: 2 render-blocking stylesheets + 1 render-blocking script;
  the homepage hero (LCP element) was not preloaded.
- Accessibility 86: active language pill contrast (2.5:1), a skipped footer heading level,
  and a `role="list"` without list items.
- Best practices 74: an ineffective `frame-ancestors` in the meta CSP (console error) +
  third-party cookies from the owner's own analytics/ads.
- 8 SEO titles over ~70 chars (SERP truncation risk).
- No website-side GCLID capture for offline (lead/booking) conversion attribution.
- Account-side (not website): PL Ad Relevance "below average" (RSA copy) and lost IS to Ad
  Rank; pages were `noindex` until 2026-10-26, which depresses older Quality Score reads.
- No broken pages, wrong prices, wrong WhatsApp number, or mis-indexing (all 36 URLs 200;
  `201288808645` everywhere; Meta number `201278378685` absent).

## 2. All fixes actually implemented (committed locally; gates green)

Round 1 (`80fb47f`): lang-pill contrast -> AA (5.06:1); footer `<h4>`->`<h3>`; social
`role="list"`->`role="group"`; removed `frame-ancestors` from meta CSP.

Round 2: inlined all CSS (0 render-blocking stylesheets); deferred `config.js`; preloaded the
homepage hero; validated GCLID/gbraid/wbraid capture + conditional `Ref:` line on the booking
message; shortened the title suffix (8 title warnings -> 2).

No content, price, booking-term, WhatsApp-number, or schema change.

## 3. Actual performance results, before -> after

Measured with Lighthouse 11.7.1 (mobile, throttled) on the render path (local dist, which
isolates render from the bad network measurement), plus EU-edge curl for network:

| | Before (round 1 render path) | After (round 2) |
|---|---|---|
| Performance | 85 | 90 (FR 93, RO 90) |
| FCP | 2.1 s | 1.8 s (FR 1.4 s) |
| Speed Index | 5.3 s | 3.0 s (RO 2.6 s) |
| LCP | 3.5 s | 3.3 s (FR 2.9 s) |
| CLS | 0.013 | 0.013 (FR/RO 0) |
| Render-blocking resources | 3 | 0 |
| Accessibility | 86 | 100 |
| Best practices | 74 | ~78 (capped by tracking cookies) |

Network (curl, EU edge): TTFB 0.2-0.6 s, `x-cache: HIT`. No field (CrUX) data exists/was
available; none invented. A live post-deploy Lighthouse should confirm these (report 07).

## 4. Was Cloudflare configured, or does it still require you?

Neither configured nor needed for speed. Evidence-based conclusion (you asked to verify):
GitHub Pages already fronts with Fastly CDN and delivers 0.2-0.6 s TTFB, so **Cloudflare
would not materially improve performance.** Its only real benefit here is response headers
(HSTS, X-Frame-Options, header-CSP) GitHub Pages cannot send - a security nicety, optional,
owner-only (DNS). Steps in report 08. Do not expect a Core Web Vitals gain from it.

## 5. Are GCLID and booking attribution ready?

Website side: yes. GCLID/gbraid/wbraid are captured (validated, 90-day `localStorage`) and a
`Ref: <id>` line is appended to the booking-form WhatsApp message only when present (clean
message otherwise; long id not exposed for organic visitors). gtag's `_gcl_aw` still
attributes the on-click "Contact" conversion. Remaining (owner/process): create two import
conversion actions in Google Ads ("Qualified lead", "Confirmed booking") and keep a log keyed
by `Ref`; a backend/CRM would allow short codes + auto-import. The click/lead/booking stages
are kept distinct - a WhatsApp open is never reported as a booking.

## 6. Are all three languages ready for advertising?

Yes, technically. FR/PL/RO are indexable, self-canonical, reciprocally hreflang-linked,
individually titled/described, schema-valid (SEO 100), internally linked, with correct
landing pages for the priority keywords and the 4 PL ad groups (report 05, existing URLs; no
new pages needed now). Measured a11y 100 and perf ~90 across all three homepages. Caveats:
eligibility is not a guarantee of indexing/ranking; 2 FR titles remain slightly long
(display-safe); real paid success still needs the account-side RSA/keyword/bid work and
Search Console submission.

## 7. Exact GitHub deployment status

- Repo confirmed: `ahmedBahgatt/hurghadakerotour`, branch `main` (the repo serving the
  production domain; not a different KeRo project).
- Round 1 committed: `80fb47f`. Round 2 committed locally on top of it. Rollback tag
  `pre-a11y-csp-2026-11-08` at the last-deployed commit.
- `git push` is **blocked by the harness permission classifier** and was not bypassed.
  `origin/main` and the live site are unchanged. All four CI gates pass locally.
- Deploy = you run `git push origin main` (+ the tag) locally; GitHub Actions builds and
  deploys. Exact commands in report 07.

## 8. Remaining actions you personally need to perform

1. Run the `git push` (deploy) - commands in report 07. Then I/we do live verification.
2. Optional: Cloudflare for security headers only (not speed) - report 08.
3. Google Search Console: verify the property + submit the sitemap.
4. Google Ads account (your other session): restructure the 4 PL ad groups + RSAs + final
   URLs + negatives per report 05; create the two offline-import conversion actions; confirm
   the "Contact" conversion is received. Do not fix quality by raising CPC.
5. Supply real business legal info (legal name, address, licence, email) when available.
6. Maintain the `Ref`-keyed lead/booking log for offline import.

Not claimed as "100% optimized": performance is strong and measured (perf ~90, LCP ~3 s
throttled, CLS ~0, a11y 100) but LCP is not under 2.5 s on heavy throttling, best practices
is capped by your tracking cookies, 2 FR titles remain long, and live post-deploy numbers are
pending the push. Everything stated is backed by measurement or marked as owner-side.
