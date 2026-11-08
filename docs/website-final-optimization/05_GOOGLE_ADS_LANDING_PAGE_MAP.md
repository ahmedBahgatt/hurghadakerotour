# 05 - Google Ads Landing Page Map (Polish priority) + account-side recommendations

Date: 2026-11-08.

IMPORTANT boundaries respected: no Google Ads campaign, budget, bid, keyword or ad was
created or changed. No read-only account access was available this session, so the
"current final URL" column is the recommended landing per the keyword, to be confirmed
against the live account. Sekrety Egiptu and all Meta campaigns were not touched.

## How website vs account responsibilities split

- **Landing Page Experience** (website): relevance of page to query, originality/usefulness, transparency/trust, ease of navigation, and load speed. Website-controllable. The dominant current weakness is **load speed (TTFB)** - see report 03; the content relevance below is already good.
- **Ad Relevance** (account): how closely the keyword matches the ad text (headlines/descriptions). Website edits cannot fix this; it is fixed in the Responsive Search Ad. Recommendations below.
- **Expected CTR** (account): historical/competitive click propensity. Account-side.
- Quality Score is a blend of the three. **Website code changes cannot guarantee a Quality Score increase**, and QS diagnostics update on a lag as Google re-collects data (especially relevant because pages were `noindex` until 2026-10-26).

## Keyword -> landing page map (Polish, the problem campaign)

| Keyword (PL) | Intent | Recommended final URL | Page satisfies intent? | Landing-page action |
|---|---|---|---|---|
| `hurghada wycieczki` | broad: list of Hurghada excursions | `https://hurghadakerotour.com/pl/` | Yes - catalog of 11 tours, 4 categories, prices, WhatsApp booking | Speed (CDN). Optionally ensure above-the-fold shows the excursion grid fast. |
| `wycieczki z hurghady` | broad: excursions from Hurghada | `https://hurghadakerotour.com/pl/` | Yes - H1 + meta use "z Hurghady" / "w Hurghadzie" | Speed (CDN). |
| `wycieczki fakultatywne hurghada` | optional/excursion-package intent | `https://hurghadakerotour.com/pl/` | Yes | Speed (CDN). |
| `kair hurghada wycieczka` | Cairo day trip from Hurghada | `https://hurghadakerotour.com/pl/wycieczki/cairo-giza-pyramids-grand-egyptian-museum/` | Yes - GEM + Giza, EUR 85, 50% deposit stated | Shorten title (76 chars). |
| `luksor z hurghady` | Luxor day trip from Hurghada | `https://hurghadakerotour.com/pl/wycieczki/luxor-ancient-egypt-highlights/` | Yes - Karnak/Valley of Kings, EUR 70, 50% deposit | - |
| `plywanie z delfinami hurghada` | swim-with-dolphins | `https://hurghadakerotour.com/pl/wycieczki/dolphin-house/` | Yes - Dolphin House, wild dolphins (conditions), snorkel, EUR 30 | Ensure the RSA for this keyword points here, not the homepage. |
| `safari quad hurghada` | quad safari | `https://hurghadakerotour.com/pl/wycieczki/vip-quad-safari/` | Yes | - |
| `super safari hurghada` | jeep+quad+spider | `https://hurghadakerotour.com/pl/wycieczki/vip-super-safari/` | Yes | - |

The equivalent FR (`/fr/...`) and RO (`/ro/...`) URLs exist for every row (same slugs) and are equally ad-ready; map French/Romanian ad groups to them 1:1. Confirm the real FR/RO search terms with Keyword Planner / search-terms report before finalizing (no invented volumes).

## Diagnosis of the three worst PL keywords

From the brief: `hurghada wycieczki` (QS 3, LPE below avg, Ad Relevance below avg, lost IS rank ~90%); `wycieczki z hurghady` (QS 5, LPE + relevance below avg); `plywanie z delfinami hurghada` (QS 5, below avg).

Most-likely root causes, in order:
1. **noindex history**: the final URLs were `noindex` until 2026-10-26. Low LPE can persist from that period; it should recover as Google re-crawls the now-indexable pages. Re-check diagnostics ~2-4 weeks after indexing + CDN.
2. **Load speed**: TTFB-driven LCP (report 03) is a real LPE drag on mobile. Fix = CDN (owner).
3. **Ad Relevance (account-side)**: "below average" here is the ad text not containing the keyword theme, independent of the page. Fix in the RSA (below).
4. **Broad match + thin negatives**: lost IS (rank) ~90% plus "Maximize clicks with a low max-CPC" means ads rarely win the auction; low QS raises required CPC. This is structural to the bid strategy, not the page.

## Account-side recommendations (for the owner to apply; NOT applied here)

| Area | Recommendation |
|---|---|
| Ad groups | Tightly theme ad groups so each contains one intent (one "Hurghada excursions / wycieczki" group, one "Dolphin / delfiny" group, one "Cairo / Kair" group, one "Luxor / Luksor" group, one "Safari / quad" group). Single-theme ad groups raise Ad Relevance. |
| RSA headlines | Put the exact keyword theme in at least 2-3 pinned-eligible headlines per group, e.g. for the dolphin group: "Plywanie z delfinami - Hurghada", "Dolphin House z Hurghady", "Rezerwacja przez WhatsApp". For the broad group: "Wycieczki z Hurghady", "Wycieczki fakultatywne Hurghada", "Bez przedplaty - platnosc na miejscu". |
| RSA descriptions | State the differentiators the page backs up: no deposit (except Cairo/Luxor 50%), pay at start, WhatsApp booking, hotel pickup, EUR prices. Do not promise anything the page does not. |
| Final URL alignment | Point the dolphin keyword's ad at the dolphin page, the Cairo keyword at the Cairo page, etc. - not the homepage. Broad "wycieczki" keywords -> `/pl/`. |
| Match types / negatives | Add exact/phrase variants of the money keywords; build a negative list (jobs, free, "sekrety egiptu" brand, unrelated cities) to stop wasted broad-match spend. |
| Bidding | The brief rules out simply raising CPC. Keep Maximize Clicks only until QS/LPE recover; once the conversion action has enough WhatsApp conversions, move to a conversion-based strategy. Do not chase impression share by bid alone while QS is low - fix QS inputs first. |
| Tracking | The site already fires one Ads conversion on a genuine WhatsApp handoff (report 06). Confirm it is received in the Ads UI before switching to conversion bidding. |

## Lion Cub exclusion (unchanged)

`LION_CUB_ADS_ELIGIBLE=False`. The Lion Cub Photo Experience URL must NOT be used as a Google Ads final URL until its legal/animal-welfare/facility/ad-policy review is signed off. It remains organically indexable only.
