# Image audit - KeRo Tours (V2)

Source of photos: the operator's own repository
`https://github.com/ahmedBahgatt/egipskiewakacje.pl` (public), cloned read-only
and never modified. Owner directed reuse of these assets and operates both sites,
so reuse rights are **owner-asserted**. Only Hurghada (`public/media/tours/h-*`
and `.../orange-bay/`, `.../kair-piramidy/`) and matching category images were
used. No third-party/stock images. The brand logo is the owner-supplied
`Kero_Logo.png`.

Cover images: `assets/img/tours/<id>.webp` (homepage cards).
Galleries: `assets/img/gallery/<id>/NN.webp` (detail-page gallery, up to 5).
Hero: `assets/img/hero.webp`. All referenced locally, never hotlinked.
`alt` text = localized tour name + index.

## Gallery coverage — 28 / 55 target images

| Tour (id) | Gallery photos | Source stems (egipskiewakacje.pl) | Verified |
|---|---|---|---|
| cairo-gem | 5 | kair-piramidy: piramida-cheopsa sunset, piramidy-giza-wielblad, turysci-wielblady, muzeum-gmach, muzeum-wnetrze | yes |
| luxor | 2 | h-luksor-dolina-krolow, categories/luksor (Karnak) | yes |
| vip-quad-safari | 4 | h-quad-safari-5h, h-quad-safari-3h, h-jazda-na-wielbladzie, categories/safari | yes |
| vip-super-safari | 4 | h-super-safari-sahara-park, h-quad-safari-3h, h-jazda-na-wielbladzie, categories/safari | yes |
| three-islands | 4 | h-wyspa-magawish, orange-bay: plaza-parasole, lodz-rejs, snorkeling-rafa | yes |
| orange-bay-hula-hula | 4 | h-wyspa-hula-hula, orange-bay: hustawka-morze, plaza-pomosty, molo-giftun | yes |
| private-speedboat | 1 | h-prywatny-speedboat | yes |
| dolphin-house | 3 | h-dom-delfinow-snorkeling, h-dom-delfinow-nurkowanie, categories/snorkeling-delfiny | yes |
| horse-riding-swimming | 1 | h-jazda-konno-kapiel-w-morzu | yes |
| el-gouna-go-kart | 0 (placeholder) | no go-kart photo in repo; `h-el-gouna` is the town, NOT karting | n/a |
| lion-cub-photo | 0 (placeholder) | restricted; no photo sourced pending compliance review | n/a |

Missing image slots to fill later (drop files into `assets/img/gallery/<id>/`):
- luxor: +3, private-speedboat: +4, dolphin-house: +2, horse-riding: +4,
  el-gouna-go-kart: 5 (incl. cover), lion-cub-photo: 5 (after review).

## Matching rules enforced

- Every photo accurately depicts its excursion. Checked visually for the
  ambiguous ones (dolphin = WILD dolphins snorkeling, not a captive show;
  super-safari = desert camp; speedboat = private boat; Orange Bay / Magawish /
  Hula Hula kept distinct).
- `three-islands` uses the Magawish cover; `orange-bay-hula-hula` uses the Hula
  Hula cover; their Orange Bay gallery photos are different files (no overlap).
- No Sharm (`s-*`) or Marsa Alam (`ma-*`) images. No stock. No image reused five
  times. Go-kart and lion cub are honest branded placeholders, not substitutes.
- `h-delfinarium-dolphin-show` (captive show) deliberately NOT used.

## Brand assets (from Kero_Logo.png)

- `logo.png` (500x500) — header, footer, splash, 404.
- `favicon.ico` (16/32/48) + `favicon-16/32/512.png` — the **full logo** in the
  browser tab (per owner request), not a cropped mark.
- `apple-touch-icon.png` (180, full logo on white).
- `og-logo.png` (1200x630, full logo on white) — Open Graph / social.

## Rights caveat
"Owner-asserted": owner directed reuse from their own repo; no explicit licence
file exists there. If any photo was itself third-party licensed, confirm the
licence covers this domain before running paid ads.
