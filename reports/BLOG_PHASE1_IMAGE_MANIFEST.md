# KeRo Polish Blog - Phase 1 handoff + image manifest

**Status:** content + code PREPARED, nothing published. `site_config.BLOG_PUBLISHED = False`.
**Prepared:** 2026-11-10. **Section:** `/pl/blog/` (Polish only).

## How to resume (Phase 2, when images are ready)
1. Drop the 12 `.webp` files into `assets/img/blog/` using the EXACT filenames below.
2. (Optional, recommended) generate responsive variants: `python3 scripts/gen_variants.py` picks up `-768/-1200/-1600` widths if configured; hero/inline `srcset` and LCP preload wire automatically when variants exist.
3. Set `BLOG_PUBLISHED = True` in `site_config.py`.
4. `python3 build.py` then `python3 scripts/check.py && python3 scripts/test_seo.py && python3 scripts/test_whatsapp.py && python3 scripts/test_analytics.py` (all must exit 0).
5. Commit + push to `main` (GitHub Actions rebuilds `dist/` and deploys to Pages).

If an image is missing at build time, the page renders a branded placeholder (never a broken `<img>`) and `build.py` prints a `WARN` - so a missing hero is never shipped silently.

## URLs produced (when published)
- Index: `https://hurghadakerotour.com/pl/blog/`
- `…/pl/blog/wycieczka-do-kairu-z-hurghady/`
- `…/pl/blog/wycieczka-do-luksoru-z-hurghady/`
- `…/pl/blog/wyspy-z-hurghady-orange-bay-magawish-white-island/`
- `…/pl/blog/safari-na-pustyni-hurghada-quad-czy-super-safari/`
- `…/pl/blog/snorkeling-w-hurghadzie-rafy-i-delfiny/`
- `…/pl/blog/jak-zaplanowac-wycieczki-z-hurghady/`

## Global image rules
- Format delivered: JPG/PNG/WebP master at **1600 x 900 px (16:9)**; the build serves WebP.
- Style: realistic, bright, editorial **travel photography** (unless marked "infographic"). No text baked into photos, no watermarks, no logos.
- Hero doubles as the social/OG image. The hero is the LCP image (loaded eagerly) - keep the main subject roughly centered so a social 1.91:1 crop still works.
- Do NOT depict real KeRo staff, real customers, specific branded vehicles, or anything implying documentary proof of a specific tour. Generic, representative scenes only.
- Filenames and ALT text are already wired in `data/blog.py`; keep filenames byte-for-byte.

---

## BLOG-01 - Wycieczka do Kairu z Hurghady

### BLOG-01-HERO  (hero, top of article; also OG image)
- **File:** `kair-z-hurghady-piramidy-gizy-hero.webp`  · **1600x900**
- **Purpose:** instantly signal "Cairo day trip = Giza pyramids + Sphinx".
- **Prompt:** "Photorealistic wide travel photograph of the Giza pyramids and the Great Sphinx on the desert plateau near Cairo at golden hour, warm low sunlight, clear sky, soft haze, a few distant tourists for scale, cinematic depth, high detail, no text, no watermark."
- **Composition:** Sphinx lower-left third, the three pyramids rising right/centre; generous sky for an OG-safe centre crop.
- **ALT (PL):** "Piramidy w Gizie i Wielki Sfinks na pustynnym płaskowyżu pod Kairem o złotej godzinie."
- **Caption (PL):** "Płaskowyż Giza - piramidy i Wielki Sfinks to główny cel jednodniowej wycieczki z Hurghady."
- **Constraints:** real Giza layout (3 pyramids + Sphinx); do not invent extra monuments or fantasy structures.

### BLOG-01-INLINE-01  (inline, in "Co zobaczysz" section)
- **File:** `kair-wielkie-muzeum-egipskie.webp`  · **1600x900**
- **Purpose:** show the new Grand Egyptian Museum (GEM).
- **Prompt:** "Photorealistic interior of a vast, modern museum of ancient Egyptian artifacts: soaring stone hall, monumental statues and a grand staircase, warm architectural lighting, a few visitors small for scale, clean contemporary design, high detail, no text, no watermark."
- **ALT (PL):** "Przestronne, nowoczesne wnętrze Wielkiego Muzeum Egipskiego z monumentalnymi kamiennymi eksponatami."
- **Caption (PL):** "Wielkie Muzeum Egipskie (GEM) otwarto w pełni 1 listopada 2025 roku."
- **Constraints:** generic grand-museum interior; do NOT copy a specific real gallery layout or claim a specific exhibit; no fabricated signage.

---

## BLOG-02 - Wycieczka do Luksoru z Hurghady

### BLOG-02-HERO
- **File:** `luksor-z-hurghady-karnak-hero.webp`  · **1600x900**
- **Prompt:** "Photorealistic travel photo of the great hypostyle hall at Karnak Temple, Luxor: forest of massive carved stone columns with hieroglyphs, warm morning light shafts between columns, a couple of tiny distant visitors for scale, high detail, no text, no watermark."
- **ALT (PL):** "Gigantyczne kolumny sali hypostylowej w świątyni Karnak w Luksorze, oświetlone porannym słońcem."
- **Caption (PL):** "Sala hypostylowa w Karnaku - las kamiennych kolumn to jeden z najmocniejszych punktów dnia w Luksorze."
- **Constraints:** Karnak-style columns; do not blend in pyramids or unrelated monuments.

### BLOG-02-INLINE-01  (inline, "Co zobaczysz jednego dnia")
- **File:** `luksor-dolina-krolow.webp`  · **1600x900**
- **Prompt:** "Photorealistic view of the Valley of the Kings on the west bank of Luxor: arid rocky desert hills under strong sun, footpaths and a few rock-cut tomb entrances, dry ochre tones, high detail, no text, no watermark."
- **ALT (PL):** "Skaliste, pustynne wzgórza Doliny Królów na zachodnim brzegu Nilu w Luksorze z wejściami do grobowców."
- **Caption (PL):** "Dolina Królów na zachodnim brzegu Nilu - wykute w skale grobowce faraonów Nowego Państwa."
- **Constraints:** no tomb interiors/paintings presented as a specific pharaoh's tomb; general valley scene only.

---

## BLOG-03 - Wyspy: Orange Bay, Magawish, White Island

### BLOG-03-HERO
- **File:** `wyspy-hurghada-orange-bay-hero.webp`  · **1600x900**
- **Prompt:** "Photorealistic aerial-ish travel photo of a Red Sea island lagoon near Hurghada: turquoise and emerald shallow water, white sand beach, a wooden jetty and a couple of excursion boats anchored, bright sunny sky, vivid natural colours, high detail, no text, no watermark."
- **ALT (PL):** "Turkusowa laguna u wybrzeża wyspy Orange Bay pod Hurghadą z zacumowanymi łodziami i białą plażą."
- **Caption (PL):** "Orange Bay - jedna z najpopularniejszych wysp na całodniowych rejsach z Hurghady."
- **Constraints:** no fake resort branding on boats/beach; natural Red Sea colours (do not oversaturate into unreal neon).

### BLOG-03-INLINE-01  (inline, "Czym różnią się te wyspy")
- **File:** `wyspy-hurghada-white-island-piaszczysta-lacha.webp`  · **1600x900**
- **Prompt:** "Photorealistic photo of a white sandbar island emerging from shallow turquoise Red Sea water, people walking on the thin strip of sand surrounded by sea, bright midday light, high detail, no text, no watermark."
- **ALT (PL):** "Biała piaszczysta łacha White Island wyłaniająca się z płytkiej turkusowej wody Morza Czerwonego."
- **Caption (PL):** "White Island to nie klasyczna wyspa, lecz piaszczysta łacha pośrodku morza - widoczna zależnie od pływów."
- **Constraints:** depict a sandbar (not a lush island); consistent with "visible depending on tides".

---

## BLOG-04 - Safari na pustyni: quad czy Super Safari

### BLOG-04-HERO
- **File:** `safari-pustynia-hurghada-quad-hero.webp`  · **1600x900**
- **Prompt:** "Photorealistic action travel photo of a line of quad bikes (ATVs) riding across a sandy desert track near Hurghada at late afternoon, low sun, dust trails, helmeted riders from behind, warm desert tones, mountains on the horizon, high detail, no text, no watermark."
- **ALT (PL):** "Rząd quadów na piaszczystym szlaku pustyni pod Hurghadą o zachodzie słońca, z tumanami kurzu."
- **Caption (PL):** "Przejażdżka quadem po pustyni pod Hurghadą to rdzeń każdego safari."
- **Constraints:** riders seen from behind/side (no identifiable faces); generic quads, no branded livery.

### BLOG-04-INLINE-01  (inline, "Quad Safari a Super Safari")
- **File:** `super-safari-jeep-spider-car.webp`  · **1600x900**
- **Prompt:** "Photorealistic desert photo showing a 4x4 off-road jeep and a low open-frame buggy / 'spider car' side by side on a sandy desert track near Hurghada, dust, warm daylight, mountains behind, high detail, no text, no watermark."
- **ALT (PL):** "Terenowy jeep 4x4 i niska, odkryta buggy-riksza typu spider car na pustynnym torze pod Hurghadą."
- **Caption (PL):** "Super Safari dokłada do quada jazdę jeepem 4x4 i spider carem - odkrytym pojazdem typu buggy."
- **Constraints:** show both a jeep AND a buggy-type vehicle (this is what distinguishes Super Safari). No branding.

---

## BLOG-05 - Snorkeling: rafy i delfiny

### BLOG-05-HERO
- **File:** `snorkeling-hurghada-rafa-hero.webp`  · **1600x900**
- **Prompt:** "Photorealistic underwater photo of a healthy Red Sea coral reef: colourful hard and soft corals, a shoal of small reef fish, a snorkeler in mask and fins near the surface above, sun rays through clear blue water, vivid natural colours, high detail, no text, no watermark."
- **ALT (PL):** "Osoba w masce i rurce płynąca nad kolorową rafą koralową Morza Czerwonego z ławicą ryb."
- **Caption (PL):** "Rafy Morza Czerwonego należą do najbogatszych i najłatwiej dostępnych na świecie."
- **Constraints:** healthy reef (not bleached); snorkeler NOT touching/standing on coral (reef-etiquette consistent with the article).

### BLOG-05-INLINE-01  (inline, "Dzikie delfiny - Dolphin House")
- **File:** `dolphin-house-dzikie-delfiny.webp`  · **1600x900**
- **Prompt:** "Photorealistic photo of a small pod of wild dolphins swimming just under the surface of clear turquoise Red Sea water near a reef, seen from a respectful distance, bright daylight, natural behaviour, high detail, no text, no watermark."
- **ALT (PL):** "Grupa dzikich delfinów płynących tuż pod powierzchnią turkusowej wody w pobliżu rafy Dolphin House."
- **Caption (PL):** "Dzikie delfiny w rejonie Dolphin House - obserwacja jest możliwa, ale nigdy gwarantowana."
- **Constraints:** WILD dolphins in open sea, from a distance - NOT captive dolphins, NOT a show, NOT people touching/riding dolphins.

---

## BLOG-06 - Jak zaplanować wycieczki z Hurghady (hub)

### BLOG-06-HERO
- **File:** `planowanie-wycieczek-hurghada-hero.webp`  · **1600x900**
- **Prompt:** "Photorealistic wide travel photo of Hurghada's seafront and marina on the Red Sea: excursion boats at a marina, turquoise sea, promenade, arid desert mountains in the background, bright sunny day, high detail, no text, no watermark."
- **ALT (PL):** "Panorama nadmorskiej Hurghady z mariną, łodziami wycieczkowymi i pustynnymi górami w tle."
- **Caption (PL):** "Hurghada to dobra baza wypadowa: morze, pustynia i zabytki Egiptu w zasięgu jednego dnia."
- **Constraints:** generic Hurghada marina scene; no specific hotel branding.

### BLOG-06-INLINE-01  (inline infographic, "Ile dni na co")
- **File:** `planowanie-wycieczek-hurghada-plan-tygodnia.webp`  · **1600x900**
- **Type:** clean **infographic** (not a photo) - optional but recommended.
- **Prompt:** "Clean, modern flat infographic of a 7-day holiday plan, horizontal timeline Day 1-7 with small simple icons (beach umbrella, boat, temple column, ATV/quad, airplane), teal and sand colour palette, lots of white space, minimal, friendly - LEAVE SPACE so Polish labels can be added later; do not bake in text."
- **ALT (PL):** "Prosta, czytelna infografika z przykładowym tygodniowym planem wycieczek z Hurghady dzień po dniu."
- **Caption (PL):** "Przykładowy rozkład tygodnia - morze, pustynia i kultura z dniami na odpoczynek."
- **Constraints:** if you add text, keep it Polish and consistent with the article's day-by-day table; teal (#0bb4c4 family) to match the site. If you prefer, skip this image - the article reads fine without it (placeholder shows until supplied).

---

## Verified facts the images must stay consistent with
- GEM (Grand Egyptian Museum) opened in full on **1 Nov 2025**; full Tutankhamun collection on public display.
- Hurghada->Cairo ~450-500 km (~5-7 h one way); Hurghada->Luxor ~290 km (~4 h one way).
- Dolphin House = **wild** dolphins, sightings not guaranteed; no feeding/touching.
- Super Safari = quad + 4x4 jeep + spider car (buggy-class); there is no standalone "buggy" tour.
- Cairo + Luxor require a 50% deposit; all other excursions: no prepayment, pay at the start.
