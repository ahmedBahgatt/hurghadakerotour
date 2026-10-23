# Image audit - KeRo Tours

Source of matched photos: **the operator's own repository**
`https://github.com/ahmedBahgatt/egipskiewakacje.pl` (public), cloned read-only.
The owner (ahmedBahgatt) directed us to reuse images from this repo and is the
same party operating KeRo Tours, so reuse rights are **owner-asserted** for the
images below. No external/third-party images were used. That repo was not
modified or pushed to.

Images are referenced from `assets/img/tours/<id>.webp` (and `assets/img/hero.webp`),
copied into this project (not hotlinked). `alt` text = localized tour name.

## Matched & published (9 excursions + hero)

| KeRo tour (id) | Image used (`<id>.webp`) | Source file in egipskiewakacje.pl | Visually verified | Rights |
|---|---|---|---|---|
| cairo-gem | cairo-gem.webp | public/media/tours/h-kair-piramidy-muzeum-egipskie.webp | yes - Giza pyramids | owner-asserted |
| luxor | luxor.webp | public/media/tours/h-luksor-dolina-krolow.webp | by filename (Valley of the Kings) | owner-asserted |
| vip-quad-safari | vip-quad-safari.webp | public/media/tours/h-quad-safari-5h.webp | by filename (quads) | owner-asserted |
| vip-super-safari | vip-super-safari.webp | public/media/tours/h-super-safari-sahara-park.webp | yes - desert camp + camels | owner-asserted |
| three-islands | three-islands.webp | public/media/tours/h-wyspa-magawish.webp | by filename (Magawish island) | owner-asserted |
| orange-bay-hula-hula | orange-bay-hula-hula.webp | public/media/tours/h-wyspa-hula-hula.webp | by filename (Hula Hula island) | owner-asserted |
| private-speedboat | private-speedboat.webp | public/media/tours/h-prywatny-speedboat.webp | yes - group on private speedboat | owner-asserted |
| horse-riding-swimming | horse-riding-swimming.webp | public/media/tours/h-jazda-konno-kapiel-w-morzu.webp | by filename (horse riding + sea) | owner-asserted |
| dolphin-house | dolphin-house.webp | public/media/tours/h-dom-delfinow-snorkeling.webp | yes - WILD dolphins + snorkeler | owner-asserted |
| HERO (site) | hero.webp | public/media/tours/h-orange-bay.webp | yes - Hurghada Red Sea beach | owner-asserted |

Notes:
- `three-islands` deliberately uses the **Magawish** island photo and
  `orange-bay-hula-hula` uses the **Hula Hula** photo, so the two sea trips do
  not share an image and neither is mislabeled.
- For Dolphin House we chose the **wild-dolphins snorkeling** photo and explicitly
  avoided `h-delfinarium-dolphin-show` (captive dolphin show), which would
  contradict KeRo's "wild dolphins, no feeding/touching/capture" positioning.

## Still missing / not matched (placeholders remain)

| KeRo tour (id) | Status | Reason |
|---|---|---|
| el-gouna-go-kart | PLACEHOLDER | No go-kart photo in the source repo. `h-el-gouna` shows the El Gouna town/marina, not karting - using it would mislabel the activity. Needs a real go-kart photo. |
| lion-cub-photo | PLACEHOLDER (and hidden) | Restricted pending legal + animal-welfare + ad-policy review. Do not source a photo yet. |

## To replace a placeholder later
Drop `assets/img/tours/el-gouna-go-kart.webp` (real karting photo) and rebuild.

## Not used from the source repo
- Marsa Alam (`ma-*`) and Sharm (`s-*`) prefixed images - different resorts, not
  Hurghada; excluded to avoid wrong-destination photos.
- Tours KeRo does not offer (aquapark, parasailing, balloon, Jordan/Petra, etc.).
- The `hero-poster.jpg` (Giza pyramids) was not used as the site hero because the
  hero should depict Hurghada/Red Sea, not Cairo.

## Rights caveat
"Owner-asserted" means the operator stated they own/may reuse these assets by
directing us to their repository. There is no explicit licence file in that repo.
If any of these photos were themselves licensed from a third party, confirm that
licence covers reuse on this new domain before running paid ads.
