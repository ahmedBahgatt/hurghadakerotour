# KeRo Tours Hurghada - multilingual VIP excursions site

Static, mobile-first landing site for **Hurghada KeRo Tours & Transfer**.
11 excursions, 3 languages (French / Polish / Romanian), WhatsApp booking.
No backend, no database, no paid hosting. Built for Google Search Ads.

- **Stack:** plain Python 3 static generator (standard library only) + vanilla CSS + ~3 KB of vanilla JS. No framework, no npm install.
- **Output:** fully pre-rendered, crawlable HTML in `dist/`.
- **Hosting:** Cloudflare Pages (free `*.pages.dev` subdomain).

---

## 1. Quick start / local development

Requires only Python 3 (3.8+).

```bash
python3 build.py            # generates ./dist
cd dist && python3 -m http.server 8787
# open http://127.0.0.1:8787/
```

The homepage is at `/fr/`, `/pl/`, `/ro/`. The root `/` is a language splash
that redirects by browser language.

There is **nothing to install** - no `node_modules`, no lockfile.

---

## 2. Project structure

```
build.py            # the generator - run it to rebuild dist/
site_config.py      # WhatsApp number, site URL, analytics IDs, business info, flags
data/
  tours.py          # the 11 excursions: prices, slugs, FR/PL/RO content  <- edit tours here
  i18n.py           # all UI strings (nav, hero, FAQ, buttons...) per language
assets/
  css/styles.css    # all styling
  js/app.js         # nav, filters, scroll reveal, WhatsApp wiring, analytics events
  js/config.js      # runtime WhatsApp number override (edit without rebuilding)
  img/tours/        # drop real tour photos here: <tour-id>.webp (see IMAGE_AUDIT.md)
  img/hero.*        # optional hero photo (hero.webp / .jpg / ...)
dist/               # GENERATED output (committed so Cloudflare can serve it directly)
IMAGE_AUDIT.md      # photo sourcing / reuse-rights tracking
```

After editing any source file, run `python3 build.py` again.

---

## 3. Common edits

### Change the WhatsApp number (LAUNCH BLOCKER - currently empty)
Two ways:

- **Permanent (recommended):** set `WHATSAPP_NUMBER` in `site_config.py`, then
  `python3 build.py`. Format: international, digits only, no `+`, no spaces.
  Example `+20 100 123 4567` -> `"201001234567"`.
- **Without rebuilding:** set `window.KERO_WHATSAPP` in `assets/js/config.js`
  (and `dist/assets/js/config.js` if dist is already deployed). This overrides
  the baked-in value at runtime.

Until a number is set, every booking button is shown in a disabled "pending"
state - it will never dial a wrong number.

### Edit a tour (price, text, inclusions)
Open `data/tours.py`, find the tour by `id`, edit the field, rebuild.
Prices are plain integers in EUR. Do not add currency symbols.

### Change a price
`data/tours.py` -> the tour's `"price"` value -> rebuild.

### Replace a photo
Put a file named `<tour-id>.webp` (or `.avif/.jpg/.png`) in `assets/img/tours/`.
The build auto-detects it and swaps out the placeholder. Recommended size:
1200x750, 16:10. See `IMAGE_AUDIT.md` for the exact id/filename per tour and
for the image-rights status. For the hero, add `assets/img/hero.webp`.

### Disable (hide) a tour
`data/tours.py` -> set the tour's `"active": False` -> rebuild. It stays in the
data but is removed from all pages, the sitemap and internal links.

### The lion cub experience
It is preserved in `data/tours.py` but **hidden by default** for compliance
review (see section 6). To publish it after review, set
`PROMOTE_LION_CUB = True` in `site_config.py`.

---

## 4. Deploy to Cloudflare Pages (free)

1. Push this repo to GitHub (see the owner note in the final report).
2. Cloudflare dashboard -> **Workers & Pages** -> **Create** -> **Pages** ->
   **Connect to Git** -> pick this repo.
3. Build settings:
   - **Framework preset:** None
   - **Build command:** `python3 build.py`
   - **Build output directory:** `dist`
   - (Python 3 is available in the Cloudflare Pages build image.)
4. Deploy. You get a free `https://<project>.pages.dev` URL.

**No-build alternative:** because `dist/` is committed, you can instead set the
build command to empty and output directory to `dist`, and Cloudflare serves the
committed files as-is.

After deploying, set the real domain in `site_config.py` -> `SITE_URL` (used by
canonical tags, hreflang and the sitemap) and rebuild so SEO URLs are correct.

---

## 5. Google Ads tracking (optional, add later)

Nothing is injected until you provide real IDs. In `site_config.py`:

- `GA4_MEASUREMENT_ID` - e.g. `G-XXXXXXXXXX`
- `GOOGLE_ADS_ID` - e.g. `AW-XXXXXXXXXX`
- `GOOGLE_ADS_CONVERSION_LABEL` - the label for the "WhatsApp click" conversion

Then rebuild. Behaviour:
- The gtag snippet loads only when at least one ID is set.
- **No conversion fires on page load.** A `whatsapp_click` event (with `tour_id`,
  `language`, `cta_position`) fires only on an actual WhatsApp button click, and
  the Ads conversion fires only if both the Ads ID and label are set.
- A WhatsApp click is an inquiry, **not** a confirmed booking - keep that in mind
  when optimizing campaigns.

---

## 6. Business inputs still required (do not fake these)

Set in `site_config.py` -> `BUSINESS` when the owner provides them: legal name,
address, tourism licence number, public email/phone. Empty fields are simply
hidden; none are invented. The WhatsApp number is the one hard launch blocker.

---

## 7. What this site deliberately does NOT do

No online payment, no deposit, no customer database, no accounts, no booking
engine. Bookings happen through a real WhatsApp conversation; customers pay at
the start of the excursion.
