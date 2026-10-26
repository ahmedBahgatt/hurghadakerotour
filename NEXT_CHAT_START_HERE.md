# Next chat - paste this prompt

Copy everything in the block below into a new Claude Code or ChatGPT chat to
continue this project with zero prior context. Full details are in `HANDOFF.md`.

---

I'm continuing an existing, live project - do not rebuild it, do not create a new
repo, and do not change the domain or hosting.

Project: **Hurghada KeRo Tours & Transfer**, a multilingual (French default,
Polish, Romanian) static website for Hurghada Red Sea excursions. Bookings go
through WhatsApp `201288808645`; no deposit, the customer pays at the start of the
excursion; "VIP" does not mean private (Cairo/Luxor are group minibus).

- Repo: `https://github.com/ahmedBahgatt/hurghadakerotour` (public, branch `main`).
- Domain: `https://hurghadakerotour.com` (Hostinger DNS -> GitHub Pages, HTTPS on).
- Hosting: GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`:
  secret-scan + `python3 build.py` + `python3 scripts/check.py` -> deploy).
- Stack: Python 3 stdlib static generator, `python3 build.py` -> `dist/`, vanilla
  CSS/JS. Content in `data/tours.py` + `data/i18n.py`; config in `site_config.py`.
  Clone the repo and read `HANDOFF.md` first.

Current verified state: root `/` shows the French homepage (canonical `/fr/`);
`/fr/ /pl/ /ro/` work; 4 categories (Sea & Islands, Desert & Safari, History &
Culture, Activities); 11 tours with fixed EUR prices; all 11 have real photo
galleries (57 images); official logo + full-logo favicon; JSON-LD (TravelAgency
geo + FAQPage + BreadcrumbList). V6 (2026-10-25) mobile-first overhaul is LIVE:
single AI panoramic hero (responsive WebP, slideshow removed), compact header +
slide-in right nav drawer, a WhatsApp booking-form dialog (bottom-sheet/modal,
localized FR/PL/RO, validation, preselected excursion), and a sticky mobile
booking bar on tour pages (speedboat priced per boat). Verified with Playwright
on Chromium/WebKit/Firefox (0px overflow at 320/390). See HANDOFF.md section E.
A full SEO/GEO/AEO/AIO pass (2026-10-26) added: accurate per-image localized ALT
(`data/seo.py`), per-tour meta descriptions, per-tour 1200x630 OG cards +
`og:image:alt`/`og:locale:alternate`/Twitter tags, an entity-linked JSON-LD graph
(TouristTrip+Offer+UnitPriceSpecification, TravelAgency, WebSite, WebPage,
BreadcrumbList - speedboat priced per boat), an image sitemap, and an SEO
regression gate (`scripts/test_seo.py`). Docs: SEO_AUDIT.md, SEO_KEYWORD_MAP.md,
SCHEMA_AUDIT.md, SEO_LAUNCH_CHECKLIST.md, reports/seo-page-inventory.csv.
Indexing is intentionally OFF: every page emits `noindex,follow` via
`ALLOW_INDEXING=False` - keep it off until the owner approves. Lion Cub is
published but ad-excluded (`LION_CUB_ADS_ELIGIBLE=False`) - keep it out of Google
Ads until its welfare/legal/ad-policy review is signed off.

Do NOT: start Sanity (postponed), enable Google indexing/Search Console
(postponed), delete the old repo `kero-tours-landing` or
`kero-tours-hurghada.pages.dev`, or modify the `egipskiewakacje.pl` repo. Never
invent prices, reviews, licences, addresses or contact details.

Open tasks: add missing gallery photos (esp. go-kart + lion cub), add real
business legal info when provided, then (only when the owner says so) Sanity and
Google indexing. Before claiming anything is done, verify both the source and the
live site, and ensure `scripts/check.py` passes.

Tell me what you'd like to work on, and I'll start from the current `main`.
