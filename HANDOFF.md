# HANDOFF - Hurghada KeRo Tours & Transfer

Self-contained project handoff. A new assistant (Claude Code or ChatGPT) can
continue from this file alone. "Verified" = checked this session; "Assumption"
is labelled where used.

---

## A. Project background and objectives

- **Business:** Hurghada KeRo Tours & Transfer - a Hurghada (Red Sea, Egypt)
  operator of VIP excursions, Red Sea boat trips, desert safaris, sightseeing
  and private transfers.
- **Goal:** generate booking inquiries via **WhatsApp**, mainly from
  **French, Polish and Romanian** speaking tourists.
- **Model:** no online payment. **No deposit / no advance payment**; the customer
  **pays at the start of the excursion**. Availability and exact pickup are
  confirmed over WhatsApp.
- **"VIP" != private.** Only tours whose data says so include private transport /
  private boat. Cairo and Luxor are **group minibus** trips.
- **Eventual use:** Google Ads (FR -> /fr/, PL -> /pl/, RO -> /ro/). Not running yet.

## B. Development history (chronological)

1. Initial multilingual (FR/PL/RO) static site concept; first repo
   `ahmedBahgatt/kero-tours-landing`; first deploy on Cloudflare Pages
   (`kero-tours-hurghada.pages.dev`).
2. **V2 redesign:** 4 excursion categories, per-tour photo galleries + lightbox,
   expanded tour descriptions, official logo + favicon.
3. **Domain move:** owner bought **hurghadakerotour.com** at Hostinger. New repo
   `ahmedBahgatt/hurghadakerotour`, moved to **GitHub Pages + GitHub Actions**.
4. **DNS + HTTPS:** owner set Hostinger DNS (4 apex A records + `www` CNAME).
   GitHub Pages "DNS check successful", **Enforce HTTPS enabled** (owner
   confirmed; HTTPS verified live this session).
5. **This session (UI refinement):** removed the language splash (root now shows
   the French homepage), compact card buttons, concise footer, polish pass, and a
   reversible `noindex` while indexing is postponed.

## C. Current infrastructure (Verified)

- **Repo:** <https://github.com/ahmedBahgatt/hurghadakerotour> - owner
  `ahmedBahgatt`, branch **main**, **public**.
- **Hosting:** GitHub Pages (build_type: workflow / GitHub Actions).
- **Generator:** Python 3 standard library only (no deps). `python3 build.py` -> `dist/`.
- **CI/CD:** `.github/workflows/deploy.yml` on push to main, `workflow_dispatch`,
  and `repository_dispatch[sanity-publish]`. Steps: checkout, setup-python 3.12,
  `scripts/secret-scan.sh`, `python3 build.py`, `python3 scripts/check.py`
  (QA gate), upload-pages-artifact (`dist`), deploy-pages.
- **Domain / DNS:** hurghadakerotour.com. Apex A -> 185.199.108-111.153;
  `www` CNAME -> ahmedbahgatt.github.io. Custom domain set in Pages (no CNAME file).
- **HTTPS:** active and enforced (Let's Encrypt via GitHub Pages).
- **Security:** per-page CSP + Referrer-Policy meta; `.nojekyll`; CI secret scan +
  QA gate. **Limitation (verified):** GitHub Pages cannot send custom HTTP
  response headers, so response-level CSP/HSTS/X-Frame-Options are not possible
  without fronting the site with Cloudflare. HSTS on the apex is applied by Pages.
- **SEO/indexing state:** pages currently emit **`noindex,follow`**
  (`ALLOW_INDEXING=False`) by owner request; `robots.txt` still allows crawling so
  the directive is readable; `sitemap.xml` present. **Not** submitted to Search Console.
- **Costs (verified where known):** GitHub (public repo + Pages) = free;
  domain = paid at Hostinger (renewal, amount not confirmed here). No other paid
  services active.

### Key files / folders
```
build.py              # static generator -> dist/
site_config.py        # domain, WhatsApp, flags (indexing, lion cub, analytics)
data/tours.py         # 11 excursions: category, price, slug, FR/PL/RO content, gallery link
data/i18n.py          # all UI strings + category labels/intros per language
assets/css/styles.css # all styles (vanilla)
assets/js/app.js      # nav dropdown, gallery, lightbox, WhatsApp wiring, reveal
assets/js/config.js   # runtime WhatsApp override
assets/img/           # logo, favicons, og, tours/<id>.webp (covers), gallery/<id>/NN.webp, hero
scripts/secret-scan.sh, scripts/check.py   # CI gates
.github/workflows/deploy.yml
dist/                 # built output (committed)
DEPLOYMENT.md, README.md, IMAGE_AUDIT.md, HANDOFF.md, NEXT_CHAT_START_HERE.md
```

## D. Website architecture (Verified)

- **Languages:** French (default), Polish, Romanian. No English in public pages
  (English seen in a browser screenshot = Chrome auto-translate, not the source).
- **Root `/`:** serves the full **French homepage** (no splash, no JS redirect);
  `canonical -> /fr/`, `hreflang x-default -> /`. `/pl/` and `/ro/` are the
  Polish/Romanian entry points (used for Google Ads).
- **Routes:** `/fr/`, `/pl/`, `/ro/`; tours at `/fr/excursions/<slug>/`,
  `/pl/wycieczki/<slug>/`, `/ro/excursii/<slug>/`. 38 pages total
  (root + 3 homepages + 33 tour pages + 404).
- **Homepage:** hero -> trust strip -> category shortcut chips -> **4 category
  sections** (each tour once) -> how-to-book -> why-us -> FAQ -> contact -> footer.
- **4 categories (order):** Sea & Islands, Desert & Safari, History & Culture,
  Activities & Experiences.
- **11 excursions (EUR, verified):**
  | Tour | Category | Price |
  |---|---|---|
  | Three Islands (Orange Bay + Magawish + White Island) | Sea & Islands | EUR 50 / person |
  | Orange Bay + Hula Hula (two islands) | Sea & Islands | EUR 40 / person |
  | Private Speedboat | Sea & Islands | **EUR 150 / private boat, base 2-5 people** |
  | Dolphin House | Sea & Islands | EUR 30 / person |
  | VIP Quad Safari | Desert & Safari | EUR 35 / person |
  | VIP Super Safari (adds jeep 4x4 + spider car) | Desert & Safari | EUR 35 / person |
  | Cairo - Pyramids, Sphinx & GEM | History & Culture | EUR 85 / person |
  | Luxor - Karnak, Valley of the Kings, Hatshepsut, Colossi | History & Culture | EUR 70 / person |
  | Horse Riding - Desert, Beach & Swimming | Activities | EUR 35 / person |
  | El Gouna Go-Kart | Activities | EUR 35 / person |
  | Lion Cub Photo Experience | Activities | EUR 30 / person |
- **Tour page:** breadcrumb, gallery (main + thumbnails + lightbox), title + price,
  intro, Experience/Highlights, narrated Program timeline, Included, Practical info,
  conditions/disclaimers, WhatsApp CTA, sticky booking panel, 3 related tours.
- **Navigation:** sticky header with logo, **Excursions dropdown** (4 categories +
  "all"), Reservation/Why/FAQ/Contact, language switcher (FR/PL/RO), WhatsApp CTA;
  mobile accordion menu; floating WhatsApp button on mobile.
- **Footer:** brand + pay-at-departure chip / 4 categories / contact (WhatsApp +
  phone) / compact bottom bar with language pills. (No 11-tour list.)
- **WhatsApp:** every CTA opens `https://wa.me/201278378685` with a localized,
  tour-specific prefilled message. Short card labels (Details/Reserver etc.) with
  full `aria-label`s.
- **Branding:** official KeRo logo in header/footer/splash-404; favicon + apple
  touch + OG image are the **full logo** (owner request).
- **SEO/AEO/GEO:** per-page title/description, canonical, FR/PL/RO + x-default
  hreflang, sitemap.xml, robots.txt, and JSON-LD (TravelAgency with Hurghada geo,
  FAQPage, BreadcrumbList, WebSite).

## E. Content and image status (Verified)

- **Tour content:** complete in FR/PL/RO for all 11 tours (name, intro,
  highlights, program, included, practical, conditions).
- **Photo galleries: 52 images.** Per tour: cairo 5, luxor 6, quad 5, super 5,
  three-islands 5, orange-bay+hula 5, speedboat 6, horse 5, dolphin 5,
  lion cub 5 (+cover), **go-kart 0 (branded placeholder - still the only gap)**.
- **2026-10-25 GALLERY EXPANSION (speedboat/Luxor/horse):** the three thin
  galleries were rebuilt from the exact Egipskie Wakacje tour-page image sets
  (Sanity ej04dib0 assets pulled from the live pages): speedboat 4->6 (aerial boat
  cover + dolphins/lagoon/snorkel), Luxor 3->6 (added Hatshepsut + Valley of the
  Kings + Karnak Osiride/hypostyle + Luxor colossi; kept sunset-colonnade cover),
  horse 4->5 (surf bathing + beach canter/walk + sunset + brown horse in sea;
  NO quad). Operator frames removed from speedboat/horse. Earlier shortfalls
  closed. Baby Lion + Go-Kart untouched.
- **2026-10-25 PHOTO-QUALITY REFRESH (this session):** the nine excursion
  galleries were rebuilt to drop soft / low-res TikTok video frames and replace
  them with sharp, high-resolution photographs from the Egipskie Wakacje repo
  (`egipskiewakacje.pl`, cloned read-only at
  `/Users/ahmedbahgat/Desktop/projects/egipskiewakacje`). Images were inspected
  visually (contact sheets), re-encoded to WebP (`cwebp -q 82`, <=1600px), covers
  updated. Count dropped from 55 to 46 **by design — quality over count**: Luxor
  (3), private-speedboat (4) and horse-riding (4) are reported SHORTFALLS because
  the repo lacks enough genuine itinerary-matching photos (balloon/Dendera/old
  Tahrir museum/day-yacht excluded as misleading; captive dolphin-show excluded).
  Speedboat keeps 3 and horse keeps 2 of the operator's OWN authentic frames to
  stay usable. Cairo museum now correctly shows the GEM. **Baby Lion and El Gouna
  Go-Kart were NOT modified.** Full map in `IMAGE_AUDIT.md`.
- **2026-10-25 media refresh:** galleries enriched from the operator's OWN
  content: (a) the six creative tour videos in `/Users/ahmedbahgat/Desktop/Final`
  (local, HQ 1080x1920) and (b) their TikTok posts `@hurghadakerotours`
  (public, pulled with yt-dlp). Frames were extracted, cropped 16:11 to remove
  the ads' promo captions/price badges, and saved as webp. Lion cub now uses
  real family+cub frames (video `KeRo_Tours_Creative_01`). Dolphin-house uses
  only WILD-dolphin-at-sea frames (the captive dolphin-show footage was
  deliberately NOT used - would misrepresent the wild Dolphin House trip).
- **Hero:** homepage hero is now a Ken-Burns crossfade **slideshow** of 5
  verified text-free stills (Orange Bay, Giza pyramids, Luxor, GEM, quad safari)
  in `assets/img/hero/slide1..5.webp` (~356KB total, lazy-loaded). A silent
  VIDEO montage was built and rejected: the source ad clips have baked-in promo
  captions that can't be cleanly removed for a silent hero, so the polished
  slideshow (the owner's accepted fallback) was shipped instead. Degrades
  without JS and freezes under prefers-reduced-motion.
- **Social media:** official Instagram / Facebook / TikTok icon links added to
  the footer (all pages) + homepage contact card (open in new tab), and to the
  TravelAgency JSON-LD `sameAs`. URLs live in `site_config.py` (`SOCIAL`).
- **Image source/rights:** earlier photos reused from the owner's own repo
  `ahmedBahgatt/egipskiewakacje.pl` (read-only); new media is the operator's own
  video + TikTok content. All **owner-asserted** rights. No stock, no AI images
  in galleries, no mislabeled/unrelated images. Full log in `IMAGE_AUDIT.md`.
- **Known missing business info:** legal name, street address, tourism licence
  number, public email (see F).

## F. Business and compliance (Verified / do-not-fabricate)

- **WhatsApp:** 201278378685 (+20 127 837 8685).
- **Booking:** choose tour -> WhatsApp inquiry -> confirmation + pickup details ->
  pay at the start of the excursion.
- **Payment:** no deposit / no advance payment; pay at departure.
- **VIP vs private:** VIP = curated experience; private transport/boat only where
  the tour says so. Cairo/Luxor = group minibus (never call them private).
- **Speedboat:** EUR 150 is for the whole boat (base 2-5 people), not per person;
  5-10 people = personalized quote; a 5-seat boat cannot legally carry 10.
- **Dolphin House:** sightings/swimming not guaranteed; no feeding/touching/
  pursuing/capturing wild dolphins.
- **Lion Cub:** published in Activities **with a factual disclaimer**, but
  **NOT approved for Google Ads**: `ads_safe=False`, `LION_CUB_ADS_ELIGIBLE=False`.
  Do not use its URL as an ad landing page or change its compliance state until a
  legal + animal-welfare + facility + ad-policy review is signed off.
- **Missing legal/contact info:** address, licence number, legal name, email are
  empty in `site_config.py` (`BUSINESS`) - never invent them.
- **Google Ads readiness blockers:** missing go-kart photo + more gallery images;
  missing business legal info; indexing intentionally off; lion cub ad-excluded.
- **Hosting limitation (not a failure):** GitHub Pages can't set custom response
  headers (see C).

## G. Completed work and verification (this session)

- **Implemented:** root -> French homepage (no splash/JS redirect, canonical /fr/,
  x-default /); compact uniform card buttons (short labels + aria-labels, 44px,
  two-on-one-row down to 320px - verified via live DOM measurement); concise
  4-column-less footer (brand / 4 categories / contact / bottom bar); polish pass;
  reversible `noindex` (`ALLOW_INDEXING=False`).
- **Deployed:** yes. Latest code commit before this handoff: **da151e2**.
  GitHub Actions run: **success**.
- **Verified in production (live, this session):**
  - `https://hurghadakerotour.com/` returns the French homepage (not the splash).
  - canonical = `https://hurghadakerotour.com/fr/`; robots = `noindex,follow`.
  - `/fr/`, `/pl/`, `/ro/` all HTTP 200; HTTPS valid.
  - footer shows the 4 categories (not 11 tours); card labels shortened.
  - WhatsApp links -> `wa.me/201278378685` intact.
- **QA gate:** 38/38 HTML valid, canonical present, 0 stale domains, valid JSON-LD.
- **Known issues / limitations:** mobile screenshots could not be captured at a
  true sub-1000px viewport in this environment (the browser rendered at desktop
  width); responsive behavior was instead verified by measuring the live DOM.
  Chrome may auto-translate the PL/RO pages in-browser - the HTML source is
  correct localized text.

## H. Pending tasks / next priorities

- Photos: galleries at 52 HQ images (2026-10-25). Luxor/speedboat/horse shortfalls
  now CLOSED via the Egipskie tour-page sets (>=5 each). Note the Egipskie page
  images are modest resolution (668-900px for several Luxor/speedboat/horse tiles);
  swap for larger masters if the owner provides them. **Only `el-gouna-go-kart`**
  has no media at all - the operator has NO go-kart photo/video on TikTok
  or Instagram (whole IG grid scanned 2026-10-25) and none online under their
  name; it keeps its branded placeholder. Get a real go-kart clip/photo from
  the owner to finish it. Do NOT substitute stock/third-party karting imagery.
- Business legal info (address, licence, email) - owner to provide; never fake.
- **Sanity integration: postponed** until explicit authorization. (Pipeline already
  has `CONTENT_SOURCE` var + `sanity-publish` dispatch; content is in `data/*.py`.)
- **Google Search Console / indexing: postponed.** When approved: set
  `GOOGLE_SITE_VERIFICATION` in site_config.py, set `ALLOW_INDEXING=True`, rebuild,
  verify in Search Console, submit `https://hurghadakerotour.com/sitemap.xml`.
- Analytics / Google Ads conversion tracking: future phase (config placeholders exist).
- Old resources to retire **only with permission**: `ahmedBahgatt/kero-tours-landing`
  and `kero-tours-hurghada.pages.dev` (superseded; not deleted).

## I. Critical instructions for the next assistant

- Do NOT rebuild from scratch; extend this project.
- Do NOT create another repository, or change domain/hosting, without permission.
- Do NOT touch the `egipskiewakacje.pl` repo (read-only source of photos).
- Do NOT delete old GitHub/Cloudflare resources without permission.
- Do NOT start Sanity integration yet.
- Do NOT enable indexing / Search Console yet (keep `ALLOW_INDEXING=False` until told).
- Preserve all 11 products + EUR prices, 4 categories, itineraries, galleries,
  logo/favicon, FR/PL/RO content, WhatsApp number, and the no-deposit policy.
- Keep Lion Cub ad-excluded until its compliance review is confirmed.
- Verify both the source and the deployed site before claiming anything is done.
- Edit content in `data/tours.py` / `data/i18n.py`; rebuild with `python3 build.py`;
  the QA gate (`scripts/check.py`) must pass; push to main triggers deploy.

---

## COPY THIS INTO A NEW CHAT

> I'm continuing an existing, live project - do not rebuild it, do not create a new
> repo, and do not change the domain or hosting.
>
> Project: **Hurghada KeRo Tours & Transfer**, a multilingual (French default,
> Polish, Romanian) static website for Hurghada Red Sea excursions. Bookings go
> through WhatsApp `201278378685`; no deposit, the customer pays at the start of
> the excursion; "VIP" does not mean private (Cairo/Luxor are group minibus).
>
> - Repo: `https://github.com/ahmedBahgatt/hurghadakerotour` (public, branch `main`).
> - Domain: `https://hurghadakerotour.com` (Hostinger DNS -> GitHub Pages, HTTPS on).
> - Hosting: GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`:
>   secret-scan + `python3 build.py` + `python3 scripts/check.py` -> deploy).
> - Stack: Python 3 stdlib static generator, `python3 build.py` -> `dist/`,
>   vanilla CSS/JS. Content in `data/tours.py` + `data/i18n.py`; config in
>   `site_config.py`. Clone the repo and read `HANDOFF.md` first.
>
> Current verified state: root `/` shows the French homepage (canonical `/fr/`);
> `/fr/ /pl/ /ro/` work; 4 categories (Sea & Islands, Desert & Safari, History &
> Culture, Activities); 11 tours with fixed EUR prices; 28/55 gallery photos
> (go-kart + lion cub are placeholders); official logo + full-logo favicon;
> compact card buttons; concise footer; JSON-LD (TravelAgency geo + FAQPage +
> BreadcrumbList). Indexing is intentionally OFF: every page emits
> `noindex,follow` via `ALLOW_INDEXING=False` - keep it off until the owner
> approves. Lion Cub is published but ad-excluded (`LION_CUB_ADS_ELIGIBLE=False`) -
> keep it out of Google Ads until its welfare/legal/ad-policy review is signed off.
>
> Do NOT: start Sanity (postponed), enable Google indexing/Search Console
> (postponed), delete the old repo `kero-tours-landing` or
> `kero-tours-hurghada.pages.dev`, or modify the `egipskiewakacje.pl` repo.
> Never invent prices, reviews, licences, addresses or contact details.
>
> Open tasks: add missing gallery photos (esp. go-kart + lion cub), add real
> business legal info when provided, then (only when the owner says so) Sanity and
> Google indexing. Before claiming anything is done, verify both the source and
> the live site, and ensure `scripts/check.py` passes.
>
> Tell me what you'd like to work on, and I'll start from the current `main`.
