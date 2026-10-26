# Structured Data (Schema.org / JSON-LD) Audit - Hurghada KeRo Tours & Transfer

Date: 2026-10-26. Applies to the built `dist/` output. All structured data is
JSON-LD, generated in `build.py` from the single source of truth in
`data/tours.py` + `data/seo.py` (no separate hardcoded price list).

> **Four different things, kept distinct throughout this document:**
> 1. **JSON-LD syntax valid** - parses as JSON. (Enforced by `scripts/check.py`.)
> 2. **Schema.org semantically valid** - correct types/properties.
> 3. **Google feature technically eligible** - meets a rich-result's requirements.
> 4. **Rich result actually shown** - Google's discretion; **never guaranteed.**
>
> We optimize for (1)-(2), note (3) honestly, and **never claim (4).**

---

## 1. Entity graph (how the nodes connect)

Stable `@id`s are used so the entities form one graph instead of disconnected
objects:

- `https://hurghadakerotour.com/#business` - `TravelAgency` (the operator)
- `https://hurghadakerotour.com/#website` - `WebSite`
- `<page-url>#webpage` - `WebPage`
- `<tour-url>#trip` - `TouristTrip`
- `<tour-url>#breadcrumb` - `BreadcrumbList`

References: `WebSite.publisher` -> `#business`; `WebPage.isPartOf` -> `#website`;
`WebPage.about` -> `#business` (home) or `#trip` (tour); `WebPage.breadcrumb` ->
`#breadcrumb`; `TouristTrip.provider` and `Offer.seller` -> `#business`.
The `TravelAgency` node is emitted on **every** page so these references always
resolve on-page (not only cross-page).

---

## 2. Business entity - `TravelAgency`

`TravelAgency` (a subtype of `LocalBusiness`/`Organization`) is the honest type:
KeRo Tours sells and operates excursions. Fields emitted:

- `name`, `url`, `logo`, `image`, `priceRange` (`€€`)
- `telephone` (+201288808645, the official WhatsApp/booking line)
- `areaServed` (City: Hurghada) - the public service area
- `sameAs` - the verified official Instagram / Facebook / TikTok profiles

**Deliberately NOT emitted (not provided / would be fabrication or unverified):**
`geo` (GeoCoordinates) and `address` (PostalAddress) are **removed** - no verified
public business premises or office coordinates have been provided, and a generic
city-centre point would misrepresent an exact location; `areaServed: Hurghada`
remains as the accurate service-area signal. Also not emitted: street address,
tourism licence number, company registration, founding date, opening hours,
reviews, aggregate rating, awards, certifications. `email`/`legalName` are emitted
**only if** set in `site_config.py` (`BUSINESS`), which is currently empty. If the
owner later supplies a verified address/coordinates, re-add them in `sd_org()`.

> No `Review`/`AggregateRating` is present anywhere. Do not add star ratings or
> review counts until there are genuine, policy-compliant reviews. Fake review
> markup is a Google spam violation.

---

## 3. Homepage - `WebSite` + `TravelAgency` + `WebPage` + `FAQPage`

- `WebSite` (with `publisher` -> business) and `WebPage` give Google the site/page
  context and `primaryImageOfPage`.
- `TravelAgency.makesOffer` lists all public excursions as `Offer`s (name, EUR
  price, canonical URL) - a truthful catalog, derived from the same tour data
  shown on the page.
- `FAQPage` - see section 6.

(No `SearchAction`/sitelinks-searchbox: the site has no on-site search, so that
markup would be false.)

---

## 4. Excursion pages - `TouristTrip` + `Offer` (the key decision)

### Why TouristTrip, not Product

`TouristTrip` (subtype of `Trip`) is the Schema.org type for "a created itinerary
of visits to one or more places of interest" - exactly a guided day excursion.
It is the semantically correct choice.

We deliberately **do not** use `Product`. A KeRo booking is a **WhatsApp inquiry
for a service**, not a purchasable product with an online checkout. Dressing a
service up as `Product` to chase a price snippet is the kind of type-manipulation
the brief (and Google's guidelines) warn against. The brief's instruction is
explicit: *prioritize truthful, policy-compliant structured data over a green
validation indicator.*

### Offer + price basis (truthful, matches the visible page)

Every `TouristTrip` carries one `Offer`:
- `price`, `priceCurrency: "EUR"`, `url` (canonical), `seller` -> `#business`.
- **No `availability`.** Excursions are booked by WhatsApp and a given date is
  confirmed manually by the operator - there is no live booking inventory, so any
  availability status (`InStock`, `PreOrder`, `LimitedAvailability`, ...) would be
  unverified. It is deliberately omitted. (`scripts/test_seo.py` fails the build if
  any availability status reappears.)
- `priceSpecification` = `UnitPriceSpecification` stating the **price basis**:
  - per-person tours: `unitText` = "par personne" / "za osobę" / "de persoană".
  - **private speedboat**: `unitText` = "par bateau privé" / "za prywatną łódź" /
    "de barcă privată" **plus** a `description` that the €150 is for the **whole
    private boat (base 2-5 people), not per person.** €150 is never encoded as a
    per-person price. Larger groups (5-10) get a personalized quote - stated on
    the page, not invented in markup.

All prices come from `data/tours.py` at build time and are asserted equal to the
visible on-page price by `scripts/test_seo.py` (structured == visible == source).

### Also on each tour page
- `BreadcrumbList` (Home > Category > Tour) - matches the visible breadcrumb and
  the page language.
- `WebPage` with `primaryImageOfPage` (first real gallery photo), `about` -> the
  trip, `breadcrumb` -> the breadcrumb.
- `TouristTrip.image` = the full list of real, crawlable gallery image URLs.

---

## 5. Pricing & Google rich-result eligibility (per excursion)

| Excursion | Price | Unit (schema `unitText` / description) | Google price/merchant rich result? |
|---|---|---|---|
| Cairo + GEM | EUR 85 | per person | Not expected (service, not a merchant product) |
| Luxor | EUR 70 | per person | Not expected |
| VIP Quad Safari | EUR 35 | per person | Not expected |
| VIP Super Safari | EUR 35 | per person | Not expected |
| Three Islands | EUR 50 | per person | Not expected |
| Orange Bay + Hula Hula | EUR 40 | per person | Not expected |
| **Private Speedboat** | **EUR 150** | **per private boat (base 2-5 people), NOT per person** | Not expected |
| El Gouna Go-Kart | EUR 35 | per person | Not expected |
| Horse Riding | EUR 35 | per person | Not expected |
| Dolphin House | EUR 30 | per person | Not expected |
| Lion Cub Photo | EUR 30 | per person | Not expected (also ad-excluded) |

### Why "not expected" for price snippets

The owner wants prices to appear in Google. Here is the honest position:

- Google's **price-in-search** experiences (merchant listings / product
  snippets) are built on **`Product`** structured data and are intended for pages
  where a shopper can **buy the item** (merchant listings) or review/aggregator
  product pages (product snippets). ([Google Search Central - Merchant listings /
  Product structured data](https://developers.google.com/search/blog/2022/09/merchant-listings))
- A **WhatsApp-only excursion inquiry** is a service booking, not a buyable
  product with checkout, so it is **generally not eligible** for merchant/product
  price rich results, regardless of markup validity.
- `TouristTrip` is **not** a Google rich-result type - there is no Google-rendered
  itinerary or price feature for it. (It is still the correct Schema.org type and
  helps Google and AI systems *understand* the offering; the price is present and
  truthful should any future feature use it.)

**Therefore:** the EUR price is marked up truthfully and is also plainly visible
on the page (and in meta/OG), but we **do not promise a price snippet in Google**.
The one rich result tour pages are genuinely eligible for is **Breadcrumbs**.

---

## 6. FAQPage - kept for AEO, no rich result expected

The homepage `FAQPage` markup is valid Schema.org and the Q&A is genuinely visible
and truthful. However, **Google has deprecated FAQ rich results**: the feature
stopped appearing in Search on **2026-05-07**, and the FAQ documentation was
removed on **2026-06-15**. ([Google Search Central - FAQ structured data,
deprecation notice](https://developers.google.com/search/docs/appearance/structured-data/faqpage))

- We **keep** the markup: it is honest, the content is visible, it causes no harm
  (Google states unused structured data does not hurt Search), and it helps AI /
  answer engines parse the Q&A for AEO.
- We make **no claim** of a FAQ rich result. If you prefer to remove it entirely,
  that is also defensible - it is now purely a semantic/AEO aid, not a rich-result
  driver.

---

## 7. Validation status

- **JSON-LD syntax:** valid on all 38 pages (`scripts/check.py` parses every
  `application/ld+json` block; 0 errors).
- **Schema.org semantics:** types/properties conform (TouristTrip/Offer/
  UnitPriceSpecification/TravelAgency/WebSite/WebPage/BreadcrumbList/FAQPage).
  Recommended external cross-check before go-live: paste representative URLs into
  the [Schema.org Validator](https://validator.schema.org/) and Google's
  [Rich Results Test](https://search.google.com/test/rich-results) (the Rich
  Results Test will report **Breadcrumbs** as the eligible enhancement on tour
  pages; it no longer reports FAQ).
- **Price == visible == source:** enforced by `scripts/test_seo.py`
  (offer price equals `data/tours.py`; the exact `&euro;N` appears on the page;
  speedboat flagged per-boat).
- **No unverified fields:** `scripts/test_seo.py` fails the build if any Offer
  `availability` / `schema.org/InStock`, or any `GeoCoordinates`, reappears.
- **Entity links:** `provider`/`seller`/`publisher`/`isPartOf`/`about`/
  `breadcrumb` all reference on-page `@id`s.

> Note: a live Rich Results Test needs a publicly fetchable URL **without**
> `noindex`. While `ALLOW_INDEXING=False`, use the "Code" (paste-HTML) mode of the
> testing tools, or run the external validation during the launch step after
> indexing is enabled. Do not enable indexing just to validate schema.

---

## 8. Summary per page type

| Page type | Entities emitted | Eligible Google rich result | Not claimed |
|---|---|---|---|
| Homepage (FR/PL/RO) | WebSite, TravelAgency(+makesOffer), WebPage, FAQPage | Breadcrumbs: N/A (no breadcrumb on home); FAQ: **deprecated** | FAQ rich result; price snippet |
| Excursion (33) | TouristTrip(+Offer+UnitPriceSpecification), TravelAgency, BreadcrumbList, WebPage | **Breadcrumbs** | Product/merchant price snippet; TouristTrip "rich result" |
| 404 | none | none | - |

Sources: Google Search Central structured-data documentation (FAQ deprecation;
Merchant listings / Product); Schema.org (`TouristTrip`/`Trip`). Links inline
above.
