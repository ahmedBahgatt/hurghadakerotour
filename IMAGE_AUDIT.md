# Image audit - KeRo Tours

**Status: ALL tour photos are currently PLACEHOLDERS.** No external images have
been downloaded or published, because reuse rights are not confirmed.

Each card and tour page renders a branded gradient placeholder (category-themed,
clearly not a real photograph) with a small camera "slot" marker. To publish a
real photo, drop `assets/img/tours/<id>.webp` (or `.avif/.jpg/.png`) and rebuild;
the build swaps the placeholder automatically. Recommended: 1200x750, 16:10.

## Why nothing was downloaded

The brief allows reusing photos from the reference site
`https://egipskiewakacje.pl/` **only if the operator owns or is licensed to reuse
them**, and says to record images as "requires confirmation" rather than download
and publish when rights are unclear. Rights are not confirmed in this brief, so:

- no images were copied from that site,
- no external images are hotlinked,
- the site ships with honest branded placeholders instead of misleading stand-ins.

Do **not** copy that site's branding, logos, phone numbers, prices, testimonials
or text. Never label one excursion's photo as a different excursion.

## Per-tour status

| Tour (id) | Placeholder shown | Likely matching source photo exists? | Candidate source | Rights | Action |
|---|---|---|---|---|---|
| cairo-gem | sea? no - history art | Yes (Giza / GEM) | Egipskie Wakacje Hurghada listing - Cairo/Giza page | PENDING confirmation | Operator to supply owned/licensed Giza + GEM photo |
| luxor | history art | Yes (Karnak / Valley of the Kings) | Egipskie Wakacje - Luxor page | PENDING | Supply owned/licensed Luxor photo |
| vip-quad-safari | desert art | Yes (quad / desert safari) | Egipskie Wakacje - quad safari page | PENDING | Supply owned quad-safari photo |
| vip-super-safari | desert art | Yes (quad / jeep / spider car) | Egipskie Wakacje - super safari page | PENDING | Supply owned super-safari photo (distinct from quad) |
| three-islands | sea art | Yes (Orange Bay / Magawish / White Island) | Egipskie Wakacje - islands page | PENDING | Supply owned island/boat photo |
| orange-bay-hula-hula | sea art | Yes (Orange Bay / Hula Hula) | Egipskie Wakacje - islands page | PENDING | Supply owned island/boat photo |
| private-speedboat | sea art | Yes (speedboat / White Island) | Egipskie Wakacje - speedboat page | PENDING | Supply owned speedboat photo |
| dolphin-house | sea art | Yes (Dolphin House / dolphins) | Egipskie Wakacje - Dolphin House page | PENDING | Supply owned dolphin/boat photo |
| horse-riding-swimming | desert art | Maybe (horses on beach) | Egipskie Wakacje - horse riding page | PENDING | Supply owned horse-riding photo |
| el-gouna-go-kart | "other" art | **Unlikely** - do not assume a match | none assumed | N/A | Operator to supply own go-kart photo |
| lion-cub-photo (restricted) | "other" art | **Unlikely / do not source** | none | N/A | Hold until compliance + welfare review (see final report) |

## Rules enforced

- Images go into `assets/img/tours/`, never hotlinked.
- Optimize to WebP/AVIF, keep useful quality, descriptive filename = tour id.
- `alt` text is auto-set to the localized tour name (translated per language).
- `width`/`height` layout stability is handled by fixed-aspect-ratio containers,
  so swapping a real photo in will not cause layout shift.
- Social preview image (`assets/img/og-default.svg`) is a branded placeholder;
  replace with a real 1200x630 JPG/PNG before heavy social sharing.

## Verification log

- Reference site inspected for structure/semantic matching: not performed in-browser
  this session (rights unconfirmed, so no asset collection was warranted).
- When the operator confirms ownership/licence, record here per image:
  source page URL, original asset URL, chosen tour, rights evidence, verified Y/N.
