# HANDOFF - KeRo Tours (hurghadakerotour.com)

## 1. Current objective
Production multilingual (FR/PL/RO) VIP excursions site for Hurghada KeRo Tours,
on the new domain hurghadakerotour.com, deployed via GitHub Pages, with
security + SEO/AEO/GEO and a path to Sanity.

## 2. State
- Repo: https://github.com/ahmedBahgatt/hurghadakerotour (public, main).
- Hosting: GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`).
  Last deploy: SUCCESS. Custom domain set (cname=hurghadakerotour.com, build_type=workflow).
- SITE_URL = https://hurghadakerotour.com. Canonical/hreflang/sitemap/robots on
  new domain; 0 stale pages.dev / kero-tours-landing refs.
- Generator: `python3 build.py` -> `dist/` (stdlib only). 38 pages.
- 4-category homepage, dropdown nav, per-tour galleries (28 photos) + lightbox,
  expanded content, official logo, favicon/OG = full logo. WhatsApp 201278378685 live.
- Lion cub published in Activities w/ disclaimer; LION_CUB_ADS_ELIGIBLE=False.
- Security: CSP + Referrer-Policy + robots meta; .nojekyll; CI secret-scan + QA gate.
- SEO/AEO/GEO JSON-LD: TravelAgency(geo) + FAQPage + BreadcrumbList + WebSite.

## 3. Blockers / next steps
- [ ] DNS at Hostinger (A/AAAA for @, CNAME www -> ahmedbahgatt.github.io). See DEPLOYMENT.md.
      Until set, hurghadakerotour.com does not resolve and the cert can't issue.
- [ ] After cert issues: enable Enforce HTTPS (Settings -> Pages) or
      `gh api -X PUT repos/ahmedBahgatt/hurghadakerotour/pages -F https_enforced=true`.
- [ ] Verify domain in GitHub Settings -> Pages -> Verified domains (anti-takeover).
- [ ] DELETE old repo (user approved): needs delete scope the token lacks. Run:
      `gh auth refresh -h github.com -s delete_repo` then
      `gh repo delete ahmedBahgatt/kero-tours-landing --yes`  (or delete in the UI).
- [ ] Google indexing: add GOOGLE_SITE_VERIFICATION in site_config.py, rebuild,
      verify in Search Console, submit https://hurghadakerotour.com/sitemap.xml.
- [ ] Photos: galleries 28/55; go-kart + lion cub still placeholders.
- [ ] Business legal info (address/licence/email) still empty - never fabricate.
- [ ] Sanity: content is in data/*.py; pipeline has CONTENT_SOURCE var +
      sanity-publish dispatch. Wiring schemas + fetch is a follow-up.

## 4. Old assets to retire
- ahmedBahgatt/kero-tours-landing (old repo) + kero-tours-hurghada.pages.dev (old
  Cloudflare deploy) are superseded. Delete the repo per above.
