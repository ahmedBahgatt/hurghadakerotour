# HANDOFF - Hurghada KeRo Tours & Transfer

Self-contained project handoff. A new assistant (Claude Code or ChatGPT) can
continue from this file alone. "Verified" = checked this session; "Assumption"
is labelled where used.

> **2026-10-28 - Microsoft Clarity installed site-wide (owner-authorized).**
> **Objective:** add Microsoft Clarity (heatmaps + session recordings) to the
> live site without disrupting SEO, Google Ads or the WhatsApp booking flow.
> **Done:** project id `z4klch73ka` added as `site_config.CLARITY_PROJECT_ID`
> (empty -> no injection). New `build.clarity_head()` emits the official async
> snippet verbatim, injected in the shared `head()` AFTER `analytics_head()` on
> all **37** content pages (36 canonical + root `/`); the 404 stays tag-free and
> `noindex`, mirroring the Google tag. Exactly one install per page, no dup.
> **Consent:** no new consent UI and no `consentv2` call. Clarity's NATIVE Google
> Consent Mode integration auto-reads the existing gtag `analytics_storage`
> signal (Microsoft doc: "If your website already uses GCM, no additional changes
> are required"). gtag defaults render first, so EEA/UK/CH stay denied ->
> cookieless (Clarity also enforces EEA/UK/CH consent by default since
> 2025-10-31); Egypt/rest granted. No fabricated consent; gtag Consent Mode v2
> untouched. **Privacy:** booking form marked `data-clarity-mask="True"`; input
> values + dropdowns are masked by Clarity in ALL modes regardless; no
> name/phone collected on-page (WhatsApp handoff is off-site); no PII in events.
> **CSP:** added enumerated Clarity hosts (no wildcard, gate-locked) -
> `www.clarity.ms` + `a..z.clarity.ms` + `c.bing.com` on `script-src`,
> `connect-src`, `img-src`. No `unsafe-eval`; every Google Ads directive
> unchanged. **Google Ads:** tag, conversion label `HOYlCNeOq6odEIyQ04dF`,
> firing logic (`app.js` untouched) all unchanged; no live test conversion fired
> (would pollute the account). **Tests:** `test_analytics.py` extended to lock
> the Clarity contract (one async install, id, ordering after consent default,
> CSP hosts, 404 clean). All gates green: check 38, analytics 37, whatsapp 39,
> seo 36 (8 pre-existing title warns). HTML + JSON-LD parse clean. Commit
> **bbf0163**, Actions run **40622564845** success, deployed. Live-verified: FR/
> PL/RO/root each serve 1 Clarity install + CSP hosts + masked form; 404 = 0.
> Tag endpoint `https://www.clarity.ms/tag/z4klch73ka` = HTTP 200 x6 via curl.
> **Blocker/caveat:** in the dev Chrome the tag returns **503** (uBlock Origin
> blocks clarity.ms; Caido is down, so not a proxy; NOT a CSP block - request
> reaches the server, no "Refused" console error). Could not observe an in-browser
> `/collect` beacon or cookie here because of the blocker. **Next step:** owner
> confirms first sessions in the Clarity dashboard from a normal browser/phone
> (no ad-blocker), and enable Clarity "Cookie consent"/Consent Mode is already
> default-on for EEA; verify GCM shows the signal under Settings.

> **2026-10-26 - CSP aligned with Google's spec (Tag Assistant warning fixed).**
> Tag Assistant reported the meta CSP blocking Google scripts + unreliable tag
> detection. Live network capture (uBlock off) confirmed the core conversion
> already reached Google (`www.googleadservices.com/pagead/conversion` -> 200) but
> the policy was incomplete vs Google's official CSP doc, and the Ads first-party
> pings go to the visitor's LOCAL Google ccTLD (seen hitting `www.google.com.eg`),
> which was not listed. Minimum doc-aligned fix in `build.py` (no `unsafe-eval`,
> no wildcards, gtag/Consent Mode unchanged): `script-src` +`www.google.com`;
> `frame-src`/`connect-src`/`img-src` +`www.googletagmanager.com`; `connect-src`
> +`ad.doubleclick.net`; `img-src` +`pagead2.googlesyndication.com`;
> `img-src`+`connect-src` + the Google supported ccTLDs (`GOOGLE_AD_DOMAINS`:
> Egypt + FR/PL/RO + main EEA/UK/CH). `test_analytics.py` now asserts these hosts
> per-directive + no wildcard/unsafe-eval. Re-verified live after deploy: **zero**
> CSP console violations on FR home + PL excursion, conversion still fires exactly
> once with the correct label, googleadservices conversion ping = 200, WhatsApp
> still opens in a separate tab (page does not navigate). The residual `503` on
> the `1p-conversion`/`ccm/collect` enhanced-conversions pings is Google's
> server-side response (enhanced conversions OFF), not a CSP block. Gates green
> (check 38/38, whatsapp 39/0, seo 36/0, analytics 37/0). Commit **a0aee5e**,
> Actions **40338699593** success. Conversion ID, indexing, design, content,
> prices unchanged. Still NOT confirmed in the Google Ads UI diagnostics.
>
> **2026-10-26 - INDEXING ENABLED + live Google Ads WhatsApp conversion tracking.**
> Owner authorized both. No redesign, no content/price/schema/WhatsApp changes.
> **Indexing:** `site_config.ALLOW_INDEXING=True`. All **36** localized canonical
> content pages (3 homepages + 33 excursion pages) now emit
> `index,follow,max-image-preview:large`; root `/` still canonicalizes to `/fr/`
> (no duplicate indexable page); the 404 stays hard-coded `noindex`. robots.txt,
> the 36-URL image sitemap and canonicals/hreflang were already correct;
> `test_seo.py` reads the flag and now asserts the index directive.
> **Google Ads:** `GOOGLE_ADS_ID=AW-18538088460`, conversion label
> `HOYlCNeOq6odEIyQ04dF` (the one action **KeRo | WhatsApp Contact**). One async
> `gtag.js` per content page (no GA4, no GTM). `analytics_head()` sets Google
> **Consent Mode v2** region defaults (EEA/UK/CH denied -> cookieless modelling,
> no banner; granted elsewhere - the Egypt tourist audience) + `url_passthrough`
> + `ads_data_redaction` before `config`. The meta **CSP was widened** to allow
> googletagmanager / googleadservices / (googleads|td).doubleclick.net so the
> beacon is not CSP-blocked.
> **Firing (already centralized in app.js, unchanged):** exactly ONE conversion
> per deliberate WhatsApp handoff - direct `[data-wa]` click OR a validated
> booking-form submit. Form-opens (`[data-book-open]`) are skipped (no double
> count); invalid submits fire nothing; **no personal data** (hotel/room/notes/
> date/message/URL) is sent to Google; WhatsApp still opens in a new tab
> (`target=_blank rel=noopener`), no same-tab `window.location` redirect, no
> `event_callback` gating the handoff (non-blocking, ad-blocker-resilient).
> **New gate** `scripts/test_analytics.py` wired into `deploy.yml`.
> **Live-verified (Chrome, this session):** `gtag.js` loads 200 (CSP OK); one
> float click = 1 conversion w/ correct label, page stays, new-tab anchor intact;
> booking form invalid submit = 0 conversions, valid submit = 1 with NO
> hotel/notes/room in the payload; FR + RO checked; ad-blocker dropped the beacon
> yet WhatsApp still worked. All gates green: check.py 38/38, test_whatsapp 39/0,
> test_seo 36/0 (8 title warnings), test_analytics 37/0. Commit **b732336**,
> Actions run **40325044701** success. `LION_CUB_ADS_ELIGIBLE=False` unchanged
> (organic indexing only, never an ad landing page); Sanity untouched; no ad
> campaign launched. Privacy details + limitations: `ANALYTICS_PRIVACY.md`.
> Remaining owner-only steps: Search Console DNS-TXT verify + sitemap submit
> (`SEO_LAUNCH_CHECKLIST.md` step 6); confirm the tag/conversion in the Google Ads
> UI (not yet observed there).
>
> **2026-10-26 - Schema accuracy fixes + desktop floating WhatsApp (indexing still OFF).**
> Targeted follow-up to the SEO pass (no redesign, no new SEO overhaul).
> **Schema accuracy** (`build.py`): (1) removed `Offer.availability`
> (`schema.org/InStock`) from every excursion - bookings are WhatsApp-confirmed,
> there is no live inventory, so no availability status is claimed (not replaced
> with PreOrder/LimitedAvailability). (2) removed `TravelAgency.geo`
> (GeoCoordinates) and `TravelAgency.address` (PostalAddress) - no verified office
> premises/coordinates provided; kept the accurate `areaServed: Hurghada`, brand
> name, telephone, `sameAs`, logo. TouristTrip/Offer architecture, EUR prices,
> per-person basis and speedboat per-boat all preserved.
> **Desktop floating WhatsApp** (`styles.css` only; HTML/JS unchanged): the
> existing `.wa-float` (homepage) and `.wa-bubble` (tour pages) were hidden at
> >=1000px; that gap is fixed. Both now render as a compact ~56px circular,
> icon-only green button fixed bottom-right (24px inset on desktop), on homepage
> AND every excursion page, on desktop AND mobile - exactly one per page. It opens
> a DIRECT wa.me chat in a new tab (target=_blank rel=noopener, never the booking
> form; the iPhone/Android handoff fix is untouched), with the correct per-page /
> per-language message + URL via the existing centralized builders
> (`wa_float`/`wa_tour_float`). The float is hidden via `:has()` while the booking
> dialog or nav drawer is open (no overlap). Mobile layout (sticky book bar +
> bubble above it) unchanged - verified at true 390px width (iframe technique; the
> session window won't shrink below desktop).
> **Tests**: `scripts/test_seo.py` now fails on any `availability`/`InStock` or
> `GeoCoordinates`; `scripts/test_whatsapp.py` asserts exactly one floating control
> per page (homepage `.wa-float`, tour `.wa-bubble`), direct-chat (no
> `data-book-open`), `target=_blank`/`rel=noopener`, new number, and that the CSS
> does not hide the float on desktop. All gates green: check.py 38/38,
> test_whatsapp 39/0, test_seo 36/0 (8 title warnings). Deployed + live-verified;
> desktop button screenshots captured (homepage + Cairo tour). `SCHEMA_AUDIT.md`
> updated (no InStock / no geo). `ALLOW_INDEXING=False` + `LION_CUB_ADS_ELIGIBLE=False`
> unchanged.
>
> **2026-10-26 - Full SEO / GEO / AEO / AIO pass (indexing still OFF).** A
> production-grade multilingual search-optimization overhaul was implemented in
> the generator + data layer (not a rebuild). `ALLOW_INDEXING=False` is
> **unchanged** - every page still emits `noindex,follow`. What changed:
> (1) **Image SEO** - the old generic `"<tour name> - N"` ALT was replaced with
> accurate, localized, per-image ALT for all 57 gallery images x FR/PL/RO (new
> `data/seo.py` `GALLERY_ALT`), written after visually verifying each image vs
> `IMAGE_AUDIT.md`; no cross-tour mislabeling; hero stays decorative (AI composite).
> `app.js` now swaps ALT on gallery/lightbox navigation.
> (2) **Open Graph** - tour pages now use a per-tour 1200x630 card
> (`assets/img/og/<id>.jpg`, generated from the covers); added `og:image:alt`,
> `og:locale:alternate`, and Twitter title/description/image. Homepage keeps the
> branded `og-logo.png`.
> (3) **Structured data** rebuilt into one entity graph: `TouristTrip` (+`Offer`
> +`UnitPriceSpecification`) replacing the loose `Product`; `TravelAgency`
> (`#business`), `WebSite` (`#website`), `WebPage`, `BreadcrumbList`, all linked by
> stable `@id`. **Speedboat is modeled per private boat (base 2-5), never per
> person.** Prices come from `data/tours.py` (no separate price list). `Product`
> intentionally NOT used (service, not a buyable product); FAQ markup kept but
> noted as deprecated by Google (no rich result expected). See `SCHEMA_AUDIT.md`.
> (4) **Meta descriptions** - purpose-written per tour x language (`data/seo.py`
> `META_DESC`), replacing the truncated-intro "...".
> (5) **Image sitemap** added to `sitemap.xml` (Google Images).
> (6) **SEO regression suite** `scripts/test_seo.py` (titles, canonicals, robots
> vs `ALLOW_INDEXING`, hreflang reciprocity, one H1, OG completeness, JSON-LD
> validity + required entities, structured==visible==source price, speedboat
> per-boat, image-ALT coverage, sitemap coverage, no stale domain / old number /
> fabricated identity) - wired into `deploy.yml`.
> Deliverables committed: `SEO_AUDIT.md`, `SEO_KEYWORD_MAP.md`, `SCHEMA_AUDIT.md`,
> `SEO_LAUNCH_CHECKLIST.md`, `reports/seo-page-inventory.csv`.
> Local gates all green: `check.py` 38/38, `test_whatsapp.py` 39 files 0,
> `test_seo.py` 36 pages 0 problems (8 title-length warnings only). Business legal
> info still empty (never fabricated). Lion Cub still `LION_CUB_ADS_ELIGIBLE=False`.
> To enable indexing later follow `SEO_LAUNCH_CHECKLIST.md` (flip one flag).
>
> **2026-10-26 - Official contact number changed site-wide.** The WhatsApp /
> phone number is now **`201288808645`** (display `+20 128 880 8645`,
> `https://wa.me/201288808645`). The previous number `201278378685` is retired
> and must have **zero** references in source or `dist/`. Single source of truth:
> `site_config.py` -> `WHATSAPP_NUMBER` (+ `BUSINESS["phone_display"]`); every
> link/JSON-LD/booking script derives from it at build time. The localized
> WhatsApp messages (FR/PL/RO) were rewritten to read naturally and now carry the
> exact localized tour URL (tour context) or homepage URL (generic). Regression
> gate: `scripts/test_whatsapp.py` (run after `build.py`; also wired into the CI
> workflow) asserts the new number everywhere, the old number nowhere, and the
> three language builders. To change the number again, edit `site_config.py` and
> update `NEW_NUMBER`/`OLD_VARIANTS` in `scripts/test_whatsapp.py`.
>
> **2026-10-26 - Desktop navbar hamburger hidden.** The hamburger (`.nav__toggle`)
> was leaking onto desktop because a late unconditional `display:inline-flex` rule
> overrode the earlier `@media (min-width:1000px){display:none}`. Fixed with a
> final `@media (min-width:1000px){.nav__toggle{display:none !important}}` (last in
> `styles.css`, wins the cascade). 1000px is the single shared desktop breakpoint
> (nav links/Book/langs/drawer). `app.js` now closes the drawer on resize up to
> desktop (releases the scroll lock, resets aria/focus). Mobile/tablet (<1000px)
> hamburger + drawer unchanged.
>
> **2026-10-26 - Booking date field + WhatsApp app-return fix.**
> (1) The booking form now has a required **preferred excursion date**
> (`<input type="date">`, full-width, after people/before notes). JS sets
> `min` = today in **Africa/Cairo** (`Intl` en-CA) on open, and the submit
> re-validates: empty -> `err_date`, past -> `err_date_past` (ISO-string compare,
> no timezone off-by-one). The date is formatted localized long-form
> (`Intl.DateTimeFormat`, weekday+day+month+year, parsed as a LOCAL date to avoid
> UTC roll-back) and added to the WhatsApp message as `m_date`. It is a REQUESTED
> date - the outro still asks the business to confirm availability. New BOOKING
> keys per lang: `f_date`, `err_date`, `err_date_past`, `m_date`. No name field,
> no tour dropdown on tour pages (unchanged).
> (2) **WhatsApp handoff** no longer strands the visitor on `api.whatsapp.com`.
> Root cause: the form submit did `window.open(url,"_blank","noopener")` then
> `if(!w) location.href=url` - but `noopener` makes `window.open` return `null`
> by spec, so the same-tab fallback ran every time. Replaced with `openWhatsApp()`
> which clicks a synthesized `<a target="_blank" rel="noopener">` (a reliable
> user-gesture new-tab trigger), matching Egipskie Wakacje's approach and the
> site's existing anchor CTAs. The KeRo page stays in its own tab; returning from
> WhatsApp lands back on KeRo. Direct `[data-wa]` CTAs were already `target=_blank`
> (unchanged). `scripts/test_whatsapp.py` extended to cover the date field + the
> no-strand handoff. Verified in Chromium at FR/PL/RO, tour + homepage, direct +
> form. Note: the Android `api.whatsapp.com` "Continue to Chat" interstitial is
> WhatsApp-server behaviour of `wa.me` and cannot be removed site-side; opening in
> a new tab keeps it off the KeRo page. Native app-switch return is OS-controlled
> and needs a real-device check (see below).
>
> **2026-10-26 - Date field moved to FIRST + past dates hard-blocked.**
> Form order is now: **preferred date (first)**, hotel, room, people, notes (the
> excursion selector still precedes everything on the homepage generic flow). Past
> dates are blocked at three layers: (1) the native `<input type="date" min>` is
> set to today-in-Cairo on init AND on every open (`refreshDateMin()`), so the
> native picker greys past days and flags `rangeUnderflow`; (2) a `change`/`input`
> guard clears any past value that slips through manual typing / paste / JS and
> shows the localized `err_date_past` inline, which clears on a valid pick; (3) the
> submit re-validates. `min` is recomputed from `Africa/Cairo` each open so a page
> left open past Egyptian midnight still refuses yesterday. Verified in Chromium
> FR/PL/RO (first-field = date, native rangeUnderflow, immediate clear+error on a
> past value, valid date in the message, submit blocked without a date). iOS Safari
> wheel respects `min`; the JS guard + submit check are the backstop - confirm on a
> real iPhone per the procedure below.

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
- **SEO/indexing state:** indexing is **ON** (`ALLOW_INDEXING=True`, owner
  authorized 2026-10-26). All 36 canonical content pages emit
  `index,follow,max-image-preview:large`; root `/` canonicalizes to `/fr/`; 404 is
  `noindex`. `robots.txt` allows crawl + lists the sitemap; the 36-URL image
  sitemap is live. **Not yet submitted to Search Console** (owner-only DNS-TXT
  step - see `SEO_LAUNCH_CHECKLIST.md` step 6).
- **Analytics/Ads:** live Google Ads tag `AW-18538088460` + one conversion
  `KeRo | WhatsApp Contact` (`.../HOYlCNeOq6odEIyQ04dF`) installed site-wide; no
  GA4, no GTM. Consent Mode v2 (EEA/UK/CH denied, else granted), no cookie banner.
  See `ANALYTICS_PRIVACY.md`. No ad campaign launched.
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
- **WhatsApp:** every CTA opens `https://wa.me/201288808645` with a localized,
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
- **Photo galleries: 57 images.** Per tour: cairo 5, luxor 6, quad 5, super 5,
  three-islands 5, orange-bay+hula 5, speedboat 6, horse 5, dolphin 5,
  lion cub 5 (+cover), **go-kart 5 (+cover)**. All 11 excursions now have photos.
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
- **Hero (V6, 2026-10-25):** the slideshow was REPLACED by a single owner-supplied
  AI panoramic (Cairo + Luxor + lion cub + desert safari + Red Sea) at
  `assets/img/hero/hero-{480,768,1200,1672}.webp` (responsive `srcset`,
  fetchpriority high, explicit 1672x941 dims for CLS). Slideshow JS + slide*.webp
  removed; dark gradient overlay kept for headline legibility.
- **MOBILE UX OVERHAUL (V6, 2026-10-25):** full mobile-first pass, verified with
  Playwright on Chromium + WebKit (iOS engine) + Firefox (0px horizontal overflow
  at 320/390; iPhone-13 emulation). Added: compact ~62px header (logo left,
  hamburger right; language pill moved into the drawer); a **slide-in right nav
  drawer** (`[data-drawer]`, app.js) with expandable category sections listing
  tour links, Booking/Why/FAQ/Contact, FR/PL/RO + socials, scrim/Esc/outside-tap
  close, focus trap, iOS-safe scroll lock; a **WhatsApp booking form** dialog
  (`[data-bookdlg]`, bottom-sheet on mobile / modal >=640px) with excursion
  select (preselected from the tour/card/bar), name/date/hotel/adults/children/
  child-ages/notes, localized validation, and a localized WA message to
  `201288808645` (per-boat price + >5-pax quote line for the speedboat; no false
  confirmation); a **sticky mobile bottom booking bar** on tour pages (price +
  Book, safe-area inset, body padding clearance, hidden >=1000px). The floating
  WhatsApp bubble is removed on tour pages (sticky bar is primary) and kept on the
  homepage. Sticky-header overlap fixed via `--header-h` + `scroll-margin-top`.
  Main CTAs open the form but keep their `wa.me` href as the no-JS fallback.
  Files: `build.py` (header/drawer/dialog/bar/hero), `assets/js/app.js` (rewritten),
  `assets/css/styles.css` (V5 block), `data/i18n.py` (`BOOKING`).
- **V5.1 MOBILE NAVBAR / BOOKING / FORM FIXES (2026-10-25):** targeted pass on top
  of V6, verified with real 320/375/390/414px rendering (page embedded in a
  fixed-width same-origin iframe so media queries fire at the true width; the
  session's browser window would not shrink below ~1728px). Changes:
  (1) **Navbar** - root cause of the "logo+hamburger both on the left" bug was
  `.nav__links + .nav__right { margin-left: 24px }` overriding the intended
  `margin-left:auto`; restored auto under `<=999.98px`. Logo now far-left,
  compact IG/FB/TikTok social icons (`header__social`, mobile-only) + hamburger
  far-right. Socials drop the 3rd icon `<=360px` and hide entirely `<340px`
  (the drawer still carries the full set). 0px horizontal overflow at all four
  widths.
  (2) **Booking vs WhatsApp split** - the sticky bottom bar's CTA is now a
  KeRo-teal `btn--book` (calendar icon, opens the form, never WhatsApp, no green).
  A separate circular green `wa-bubble` sits just above the bar's right side on
  tour pages: it opens a DIRECT WhatsApp chat prefilled with the tour name +
  canonical URL (no form), and is hidden via `:has()` while the drawer or form is
  open. Homepage keeps its `wa-float` pill (direct WA); no bubble on the homepage.
  (3) **Simplified form** - removed the excursion dropdown and the customer-name
  field, and the date field (date is confirmed on WhatsApp). On a tour page /
  clicked card / sticky bar the form shows a READ-ONLY tour context (title +
  price) derived from the clicked element's `data-tour`, falling back to the
  page's own tour (`BK.tour`) - never a global default. Homepage general CTAs
  (hero, contact, drawer) show a tour selector. Fields: hotel (required), room
  (optional), number of people (required, positive int), notes (optional). Entry
  is preserved in-memory across close/reopen within the page (NOT localStorage).
  Message builder sends tour name, canonical URL, EUR price+unit, hotel, room (if
  given), people, notes (if given), a >5-pax quote line for the speedboat, and an
  availability/date/pickup confirmation request, URL-encoded to
  `wa.me/201288808645`. Speedboat stays €150 total / private boat.
  Verified FR/PL/RO messages for speedboat (per-boat) + per-person tours, all
  entry points, validation, and no console errors.
  Files: `build.py`, `assets/js/app.js`, `assets/css/styles.css`, `data/i18n.py`.
- **V5.2 MOBILE UI POLISH (2026-10-26):** owner review follow-ups, verified at
  320/375/390/414px (iframe true-width). Changes:
  (1) **Navbar strategy** - mobile header is now logo LEFT / language switcher
  CENTER / hamburger RIGHT. The centered langs are a 2nd `langswitch--mobile`
  instance absolutely centered (`left:50%;translate(-50%,-50%)`), measured dead-
  center (lang center == viewport center) at all four widths, no overlap with
  logo/hamburger, 0px overflow. Social icons were REMOVED from the header and now
  live only in the drawer foot (cleaner header per owner preference). The
  `header_social_links()` builder + `header__social` CSS were deleted.
  (2) **Hamburger** - refined 44x44 rounded button: 3 rounded 18x2px lines,
  gap 4px, perfectly centered (measured 13/13 side pad, 15/15 top/bottom),
  subtle shadow + hover border.
  (3) **Floating WhatsApp** - homepage `wa-float` is now a 56px circle on mobile
  (icon-only, `place-items:center`), WA glyph centered to 0px offset; the
  tour-page `wa-bubble` keeps its centered circle (`line-height:0` safety).
  (4) **Booking form symmetry** - room number + number of people share one grid
  row, equal 48px height, equal width, inputs bottom-aligned via
  `.bookform__grid{align-items:end}` (stays aligned even if a label wraps at
  320px); labels also top-align at 375/390/414 after shortening the room label to
  `Numéro de chambre` / `Numer pokoju` / `Număr cameră`. Form order unchanged
  (Hotel full-width -> Room+People row -> Notes); no name field, no dropdown on
  detail pages. Files: `build.py`, `assets/css/styles.css`, `data/i18n.py`.
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

- **WhatsApp:** 201288808645 (+20 128 880 8645).
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
  - WhatsApp links -> `wa.me/201288808645` intact.
- **QA gate:** 38/38 HTML valid, canonical present, 0 stale domains, valid JSON-LD.
- **Known issues / limitations:** mobile screenshots could not be captured at a
  true sub-1000px viewport in this environment (the browser rendered at desktop
  width); responsive behavior was instead verified by measuring the live DOM.
  Chrome may auto-translate the PL/RO pages in-browser - the HTML source is
  correct localized text.

## H. Pending tasks / next priorities

- Photos: galleries at 57 images (2026-10-25). **All 11 excursions now have real
  photos** - Baby Lion (5) and El Gouna Go-Kart (5) installed from owner-supplied
  Desktop folders; go-kart placeholder gap CLOSED. Lion images are LOW-RES/portrait
  (335-415px, cropped to 16:11); go-kart mixed (best 1400px). RIGHTS: both new
  folders have web/stock-style filenames (not original camera files) - owner-
  asserted, confirm before paid use. `LION_CUB_ADS_ELIGIBLE=False` kept.
  Egipskie page tiles for Luxor/speedboat/horse remain modest res (668-900px);
  swap for larger masters if the owner provides them. If the owner later supplies
  higher-res ORIGINAL lion/go-kart photos (esp. landscape), swap them in.
- Business legal info (address, licence, email) - owner to provide; never fake.
- **Sanity integration: postponed** until explicit authorization. (Pipeline already
  has `CONTENT_SOURCE` var + `sanity-publish` dispatch; content is in `data/*.py`.)
- **Indexing: DONE** (`ALLOW_INDEXING=True`). Remaining owner-only step: verify
  the property in Google Search Console (DNS-TXT recommended) and submit
  `https://hurghadakerotour.com/sitemap.xml` - exact instructions in
  `SEO_LAUNCH_CHECKLIST.md` step 6.
- **Google Ads conversion tracking: DONE** (tag + one WhatsApp conversion live).
  Remaining owner-only step: confirm in the Google Ads UI (Tools -> Conversions)
  that the tag is recognized and a conversion was received; then decide on
  campaigns/budget (not launched). Details: `ANALYTICS_PRIVACY.md`.
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
> through WhatsApp `201288808645`; no deposit, the customer pays at the start of
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
