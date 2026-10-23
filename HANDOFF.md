# HANDOFF - KeRo Tours landing site

## 1. Current objective
Production-ready static multilingual (FR/PL/RO) VIP excursions site for Hurghada
KeRo Tours, WhatsApp booking, Google-Ads-ready, deployable free on Cloudflare
Pages. Build is complete and QA-passed locally.

## 2. State
- Generator: `build.py` (Python stdlib only). `python3 build.py` -> `dist/`.
- 35 pages built: root splash + 3 homepages + 30 tour pages (10 public tours x 3
  langs) + 404. All 11 tours in `data/tours.py`.
- Prices verified against brief (all EUR). Speedboat = EUR150 total (base 2-5).
- WhatsApp buttons all render "pending/disabled" (number not set).
- HTML validated (35/35 well-formed, 1x h1, canonical/lang/title each).
- Visual QC in Chrome: FR/PL/RO render, diacritics correct, placeholders per
  category, mobile layout + floating WhatsApp OK. (English text seen in a
  screenshot was Chrome auto-translate, not a build issue - raw HTML is correct.)

## 3. Recently modified / created files
- `build.py`, `site_config.py`
- `data/tours.py`, `data/i18n.py`, `data/__init__.py`
- `assets/css/styles.css`, `assets/js/app.js`, `assets/js/config.js`
- `README.md`, `IMAGE_AUDIT.md`, `.gitignore`, this file
- generated: `dist/**`

## 3b. Git / remote
- Private repo created and pushed: https://github.com/ahmedBahgatt/kero-tours-landing
  (owner ahmedBahgatt, confirmed by user). Branch `main`.

## 4. Next steps / blockers
- [x] WhatsApp number set: 201278378685 (+20 127 837 8685). 672 live links, 0 pending.
      Also added to footer business contact.
- [ ] Deploy on Cloudflare Pages (README section 4). No live URL yet.
- [ ] After deploy: set `SITE_URL` to the pages.dev URL, rebuild, push (updates
      canonical/hreflang/sitemap).
- [ ] NOT Google-Ads-ready until real licensed photos + business legal info verified.
- [x] Real photos: 9/11 excursions + hero now use owner-held photos from
      ahmedBahgatt/egipskiewakacje.pl (owner-asserted rights). Pending: go-kart
      (no match) + lion cub (restricted). See IMAGE_AUDIT.md.
- [ ] Lion cub tour: hidden by default (PROMOTE_LION_CUB=False) pending legal +
      animal-welfare + ad-policy review.
- [ ] Business legal info (address, licence, email/phone) to be supplied by owner.
- [ ] After deploy: set `SITE_URL` to the real pages.dev URL and rebuild.
- [ ] Optional: GA4 / Google Ads IDs when available.
