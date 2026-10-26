# Image audit - KeRo Tours

Primary source of photos: the operator's own repository
`https://github.com/ahmedBahgatt/egipskiewakacje.pl` (public), cloned read-only
at `/Users/ahmedbahgat/Desktop/projects/egipskiewakacje` and never modified.
Owner directed reuse of these assets and operates both sites, so reuse rights are
**owner-asserted**. The brand logo is the owner-supplied `Kero_Logo.png`.

Cover images: `assets/img/tours/<id>.webp` (homepage cards, 16:10).
Galleries: `assets/img/gallery/<id>/NN.webp` (detail-page gallery + lightbox).
Hero: `assets/img/hero/hero-*.webp` (single responsive panoramic). All referenced
locally, never hotlinked. OG social cards: `assets/img/og/<id>.jpg` (1200x630,
per tour).

**ALT text (updated 2026-10-26 - SEO pass):** each gallery image now has an
accurate, localized, per-image `alt` describing the ACTUAL visible subject, in
FR/PL/RO, stored in `data/seo.py` (`GALLERY_ALT`). The earlier generic "tour name
+ index" scheme was replaced. ALTs were written after visually verifying every
image against this audit's subject table; no cross-tour mislabeling (Orange Bay
is not labelled Magawish, wild dolphins are not labelled captive, the generic
indoor karting frame is not tied to the El Gouna outdoor venue). The hero is an AI
panoramic composite and stays decorative (`alt=""` + `aria-hidden`) so it is not
presented as a real tour photo.

## 2026-10-25 gallery photo refresh

The nine excursion galleries below were rebuilt to remove soft / low-resolution
TikTok video frames and replace them with sharp, high-resolution photographs from
the Egipskie Wakacje collection. Each selected image was **inspected visually**
(contact sheets), not chosen by filename. Egipskie JPEG sources (mostly 1600x1000,
some up to 2000px) were re-encoded to WebP with `cwebp -q 82 -m 6`, capped at
1600px width (no upscaling), preserving aspect ratio and natural colors.

Encoding tool: `cwebp 1.x`. Gallery container renders 16:11 (object-fit: cover);
the lightbox shows each image at its native ratio, so no source was hard-cropped.

**Baby Lion Photo Experience and El Gouna Go-Kart were NOT touched** in this
refresh (see bottom). Lion-cub compliance state is unchanged.

## 2026-10-25 gallery expansion (speedboat / Luxor / horse)

Second pass on the three thin galleries, sourced from the **exact Egipskie Wakacje
tour-page image sets** (Sanity project `ej04dib0`, pulled from the live pages the
owner referenced) re-encoded to WebP (`cwebp -q 82`, <=1600px). This closes the
earlier shortfalls. Covers updated for speedboat + horse; Luxor cover kept
(highest-res sunset colonnade). Operator video frames removed from speedboat and
horse. **Baby Lion and El Gouna Go-Kart still untouched.**

- **Private Speedboat 4 -> 6** (egipskiewakacje.pl/wycieczki-z-hurghady/prywatny-speedboat/):
  aerial private boat (new cover), guests driving, wild-dolphin freedive, dolphin
  selfie, lagoon fruit on board, snorkel gear on stern.
- **Luxor 3 -> 6** (…/luksor-dolina-krolow/): sunset colonnade (cover, repo
  `h-luksor-dolina-krolow`) + Hatshepsut, Valley of the Kings painted tomb, Karnak
  Osiride court, Karnak hypostyle, Luxor Temple colossi — the requested balanced mix.
- **Horse Riding 4 -> 5** (…/jazda-konno-kapiel-w-morzu/): surf bathing, beach
  canter, white-horse beach walk, shallow-water sunset, brown horse in turquoise
  sea (cover, repo `s-jazda-na-wielbladzie`). Horse/beach/swimming only — **NO quad**.

## Gallery coverage — 57 images (9 Egipskie tours = 47; lion-cub 5; go-kart 5)

All 11 excursions now have real-photo galleries (go-kart's placeholder gap closed).

| Tour (id) | Imgs | Source (egipskiewakacje.pl `public/media/…`) | Cover replaced | Notes |
|---|---|---|---|---|
| cairo-gem | 5 | `kair-piramidy/piramida-cheopsa-giza-zachod-slonca` (2000px, cover), `categories/kair` (Sphinx+Khafre), `tours/h-kair-wielkie-muzeum-gem` (GEM hall), `kair-piramidy/piramidy-giza-wielblad-turysci`, `kair-piramidy/turysci-wielblady-piramida-giza` | yes | Museum = **GEM** (matches itinerary). Old Tahrir-museum shots deliberately dropped (different building). cairo 04/05 are 669px (max available). |
| luxor | 6 | `tours/h-luksor-dolina-krolow` (sunset colonnade, cover) + Egipskie page set: Hatshepsut temple, Valley of the Kings painted tomb, Karnak Osiride court, Karnak hypostyle, Luxor Temple colossi | yes (kept sunset colonnade) | Balanced Karnak / VoK / Hatshepsut / temple-statue mix from the Egipskie Luxor page (Sanity ej04dib0). Earlier shortfall resolved. Page images are 668-900px originals; sunset colonnade is 1600px. |
| vip-quad-safari | 5 | `tours/s-quad-safari-3h` (action, cover), `categories/safari` (quad dust), `tours/h-quad-safari-3h`, `tours/h-quad-safari-5h`, `tours/h-jazda-na-wielbladzie` (camel) | yes | Desert quad activity is location-agnostic; `s-` (Sharm-tagged) quad shot used because the activity depicted is identical Eastern-Desert quad safari. |
| vip-super-safari | 5 | `tours/h-buggy-safari` (spider cars, cover), `tours/ma-jeep-safari` (4x4), `tours/h-super-safari-sahara-park` (Bedouin camels), `tours/s-buggy-safari` (spider car), `tours/ma-quad-safari-5h` (quad+camel) | yes | Combines quad + jeep + spider car + Bedouin per brief. Fully distinct file set from vip-quad-safari (no shared images). `s-`/`ma-` = same desert activity. |
| three-islands | 5 | `tours/orange-bay/orange-bay-molo-giftun` (Giftun jetty, cover), `tours/h-wyspa-magawish` (Magawish sign), `tours/orange-bay/orange-bay-plaza-parasole`, `tours/orange-bay/orange-bay-plaza-pomosty` (island boat), `tours/orange-bay/snorkeling-rafa-orange-bay` | yes | Represents Orange Bay + Magawish + snorkeling. **No authentic Hurghada "White Island" photo exists** in the repo, so White Island is not depicted (not faked). Distinct file set from orange-bay-hula-hula. plaza-pomosty 800px, snorkeling-rafa 720px (max available). |
| orange-bay-hula-hula | 5 | `tours/orange-bay/orange-bay-hustawka-morze` (swing-in-sea 1920px, cover), `tours/h-wyspa-hula-hula` (Hula Hula hammock), `tours/h-orange-bay` (Orange Bay beach), `tours/h-plaza-orange-ozirea`, `tours/orange-bay/orange-bay-lodz-rejs` | yes | Genuine Orange Bay + Hula Hula imagery. Distinct file set from three-islands. |
| private-speedboat | 6 | Egipskie speedboat page set (Sanity ej04dib0): aerial private boat (new cover), guests driving, wild-dolphin freedive, dolphin selfie, lagoon fruit on board, snorkel gear on stern | yes (aerial) | Rebuilt from the Egipskie `prywatny-speedboat` page gallery. Operator video frames removed. aerial 1280x720, lagoon 1200x900, rest 669x446. |
| horse-riding-swimming | 5 | Egipskie horse page set (Sanity ej04dib0): rider bathing with horse in surf, beach canter, white-horse beach walk, shallow-water sunset + repo `tours/s-jazda-na-wielbladzie` (brown horse in turquoise sea, cover) | yes (s-jazda) | Rebuilt from the Egipskie `jazda-konno-kapiel-w-morzu` page. Horse/beach/swimming ONLY — the 2 quad shots from that page's set were deliberately excluded (per request: this is the horse tour, not the horse+quad variant). Operator frames removed. Page images 669-830px; cover 1600px. |
| dolphin-house | 5 | `categories/snorkeling-delfiny` (snorkeler+pod, cover), `tours/h-dom-delfinow-snorkeling`, `tours/h-dom-delfinow-nurkowanie`, `tours/h-abu-dabbab-snorkeling` (reef), `tours/s-white-island-ras-mohamed` (reef+eagle ray) | yes | **WILD dolphins + reef snorkeling only.** `h-delfinarium-dolphin-show` / `s-dolphin-show` (captive shows) deliberately EXCLUDED per brief. |

## 2026-10-25 Baby Lion + Go-Kart photo install (last two excursions)

Owner supplied photo folders for the two remaining excursions. Images were
inspected visually, the strongest selected, cropped to the gallery aspect
(16:11) and cover aspect (16:10) keeping the key subject, and encoded to WebP
(PIL q85, no upscaling). Source folders left untouched (worked on copies).

**Compliance unchanged: `LION_CUB_ADS_ELIGIBLE=False` — Baby Lion stays OUT of
Google Ads. Adding photos is NOT an animal-welfare/legal/ad-policy approval.**

| Tour (id) | Imgs | Source folder | Selected | Cover | Notes |
|---|---|---|---|---|---|
| lion-cub-photo | 5 | `~/Desktop/Photo session with a lion cub` | `images (4)` (cub facing camera + child), `images (3)` (cheek-to-cheek), `images (1)` + `images (2)` (adult holding cub), `images.jpeg` (family group) | `images (4)` (cub facing camera) | Replaced the prior video frames. **LOW RES / PORTRAIT source** (335-415px wide, vertical) → cropped to 16:11 keeping the cub; adult faces are partly cropped on 2 tiles. Genuine cub-photo-session shots. **RIGHTS: filenames (`images (N).jpeg`) look web-sourced, not original camera files — owner-asserted; confirm before any paid use.** |
| el-gouna-go-kart | 5 | `~/Desktop/GO KART À EL GOUNA` | `elgouna-karting-night` (kid in kart), `2000x2000-…` (kart pack), `900x600-…` (karts on bend), `images (1)` (rental-kart driver #20), `karting-636x426` (indoor fist-bump) | `elgouna-karting-night` (1400x1050, kid in kart) | First real media for this tour (was a placeholder). `images.jpeg` was a **duplicate** of `images (1)` → excluded. Tile 05 is **indoor/generic** karting (not the El Gouna outdoor track) — flagged. **RIGHTS: stock-style filenames (hash/size names) suggest web-sourced, not owner originals — owner-asserted; confirm before paid use.** |

### Earlier status (now superseded)
Before this pass: lion-cub = 5 operator video frames; el-gouna-go-kart = 0 (branded placeholder, the last gallery gap). Both are now real-photo galleries.

## Matching rules enforced

- Every photo accurately depicts its excursion or activity. Ambiguous ones were
  checked visually: dolphin = WILD dolphins snorkeling (never a captive show);
  super-safari = quad + jeep + spider car + Bedouin camp; the "camel"-named horse
  shot is actually a horse; the Cairo museum = GEM (not the old Tahrir museum).
- The two island galleries are kept **distinct** (no shared files) and each island
  is represented honestly: Orange Bay, Magawish and Hula Hula by their own photos;
  White Island is not depicted because no authentic Hurghada White Island photo
  exists (never substituted with another island).
- Desert safari images tagged `s-`/`ma-` in the source are used only where the
  depicted activity (quad / jeep / spider car) is identical to Hurghada's; no
  Sharm/Marsa Alam *place* (e.g. a specific island or reef name) is passed off as
  a Hurghada destination.
- No stock, no AI images, no fabricated imagery. No captive dolphin-show footage.
- Soft/low-res TikTok frames were removed from all nine refreshed tours **except**
  where the Egipskie collection could not supply enough genuine photos (speedboat,
  horse-riding) — there a minimal number of the operator's OWN authentic frames
  were retained and the shortfall is reported above.

## Brand assets (from Kero_Logo.png) — unchanged

- `logo.png` (500x500) — header, footer, splash, 404.
- `favicon.ico` + `favicon-16/32/512.png` — full logo in the browser tab.
- `apple-touch-icon.png` (180), `og-logo.png` (1200x630) — social / Open Graph.

## Rights caveat

"Owner-asserted": owner directed reuse from their own repo; no explicit licence
file exists there. The retained speedboat/horse frames are the operator's own
video content. If any Egipskie photo was itself third-party licensed, confirm the
licence covers this domain before running paid ads.
