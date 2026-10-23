# HANDOFF - KeRo Tours landing site (V2)

## 1. Current objective
Production multilingual (FR/PL/RO) VIP excursions site for Hurghada KeRo Tours.
V2 redesign done: 4-category homepage, Excursions dropdown, per-tour photo
galleries + lightbox, expanded tour content, official logo/favicon, lion cub
published (ads-excluded), production domain SEO.

## 2. State
- Generator: `build.py` (Python stdlib only). `python3 build.py` -> `dist/`.
- SITE_URL = https://kero-tours-hurghada.pages.dev (production).
- 38 pages: root + 3 homepages + 33 tour pages (11 tours x 3 langs) + 404.
- Homepage = 4 category sections (Sea & Islands / Desert & Safari / History &
  Culture / Activities), each tour exactly once. No featured/all duplication.
- Galleries: 28 real photos across 9 tours (cover + up to 5). go-kart + lion cub
  are branded placeholders. Lightbox + thumbnails + swipe.
- Lion cub: published in Activities with factual "A savoir" disclaimer;
  ads_safe=False, LION_CUB_ADS_ELIGIBLE=False (keep OUT of Google Ads).
- WhatsApp 201278378685: all booking links live, localized per tour.
- Favicon/apple-touch/OG = the FULL supplied logo (owner request).
- QA: 38/38 HTML valid; canonical/hreflang/sitemap on production domain; 0 stale
  kero-tours-landing refs; dropdown + gallery + lightbox verified in browser.

## 3. Recently modified
- site_config.py (SITE_URL, LION_CUB_PUBLISHED, SHOW_LION_ADDON, LION_CUB_ADS_ELIGIBLE)
- data/tours.py (4 categories, program stages, practical info, lion published)
- data/i18n.py (category labels + intros, dropdown/gallery/program/practical labels)
- build.py (category homepage, dropdown nav, gallery+lightbox, logo, favicon/og)
- assets/css/styles.css (dropdown, catbar, gallery, lightbox, program, logo)
- assets/js/app.js (dropdown, gallery, lightbox)
- assets/img/ (logo.png, favicon*, apple-touch, og-logo, tours/*, gallery/*, hero)
- IMAGE_AUDIT.md, README.md, this file

## 4. Next steps / blockers
- [ ] Push triggers Cloudflare auto-deploy; verify build on the existing project.
- [ ] Galleries: 28/55. Add remaining photos into assets/img/gallery/<id>/ later.
- [ ] el-gouna-go-kart photo + lion cub photo still missing (placeholders).
- [ ] Lion cub: do NOT use as a Google Ads final URL until legal + welfare +
      facility + ad-policy review is signed off.
- [ ] Business legal info (address, licence, email) still owner-supplied = empty.
- [ ] NOT Google-Ads-ready until go-kart photo + business info verified.
