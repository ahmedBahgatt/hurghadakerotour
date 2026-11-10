# -*- coding: utf-8 -*-
"""
Polish travel blog ("Poradnik turystyczny") for Hurghada KeRo Tours & Transfer.

PURPOSE
  Genuinely useful, independent travel-planning content for Polish-speaking
  tourists researching excursions in Hurghada. NOT an SEO link farm. Every
  article stands on its own value; cross-site links to Egipskie Wakacje appear
  only where a reader genuinely benefits (see ARTICLE 6) and are qualified
  rel="nofollow" via the inline `ext:` scheme in build.py.

SCOPE / GATING
  The whole section is gated by site_config.BLOG_PUBLISHED (master switch) and
  each article's own `published` flag. While BLOG_PUBLISHED is False, build.py
  emits NO blog output, NO footer link and NO sitemap entries, so production is
  unaffected. Flip BLOG_PUBLISHED to True (after the hero/inline images are in
  assets/img/blog/) and rebuild to go live. Images are referenced by filename;
  if a file is missing the builder renders a branded placeholder, never a broken
  <img>.

CONTENT RULES (enforced by hand, mirror the project brief)
  - Polish only (this is the Polish-audience section). No auto FR/RO translation.
  - Verified facts only. Prices/itineraries mirror data/tours.py (pulled live in
    build.py where shown, never hard-coded in prose). No invented entrance fees,
    pickup times, schedules, meals, wildlife guarantees or reviews.
  - KeRo's own excursion pages are the priority internal links. A booking CTA is
    contextual, not stapled to every paragraph.
  - Deposit policy (Cairo + Luxor: 50% to confirm, 50% at start; everything else:
    no prepayment, pay at the start) stated only where relevant.

BODY FORMAT
  article["body"] is a list of blocks rendered by build.render_block():
    {"t":"h2","text":..}             section heading (gets an in-page anchor id)
    {"t":"h3","text":..}             sub-heading
    {"t":"p","text":..}              paragraph; inline markup allowed
    {"t":"ul"/"ol","items":[..]}     list; each item allows inline markup
    {"t":"table","head":[..],"rows":[[..],..]}   comparison table (cells: inline)
    {"t":"note","title":..,"text":..}            highlighted aside / tip
    {"t":"image","id":"BLOG-0X-INLINE-0Y"}       inline image (looked up in
                                                 article["images"])
    {"t":"cta","tour":"<tour-id>","text":..}     booking CTA -> KeRo tour page

  Inline markup inside "text"/"items"/table cells:
    **bold**
    [label](tour:<tour-id>)      -> KeRo excursion detail page (localized PL URL)
    [label](article:<slug>)      -> another blog article
    [label](url:/pl/...)         -> any internal path
    [label](ext:https://...)     -> external link (rel="nofollow noopener", _blank)
"""

# ---------------------------------------------------------------------------
# Blog macro-categories (Polish labels). Keyed by a stable id used on cards.
# ---------------------------------------------------------------------------
BLOG_CATEGORIES = {
    "zwiedzanie":  "Zwiedzanie i kultura",
    "morze":       "Morze i wyspy",
    "pustynia":    "Pustynia i safari",
    "planowanie":  "Planowanie wyjazdu",
}

# ---------------------------------------------------------------------------
# UI strings for the blog (Polish). Kept here, out of data/i18n.py, because the
# blog is a Polish-only section and i18n.py holds the shared FR/PL/RO UI.
# ---------------------------------------------------------------------------
BLOG_UI = {
    "base_path":        "blog",
    "footer_link":      "Poradnik turystyczny",
    "nav_blog":         "Poradnik",
    "index_h1":         "Poradnik turystyczny po Hurghadzie",
    "index_title":      "Poradnik turystyczny - wycieczki z Hurghady | KeRo Tours",
    "index_desc":       "Praktyczny poradnik po wycieczkach z Hurghady: Kair i piramidy, Luksor, wyspy Morza Czerwonego, safari na pustyni i snorkeling. Rady, porównania i planowanie.",
    "index_intro":      "Praktyczne poradniki dla polskich turystów w Hurghadzie - jak wybrać wycieczkę, czego się spodziewać i jak dobrze zaplanować czas nad Morzem Czerwonym. Bez naciągania: konkretne porównania i rzeczowe informacje.",
    "index_lead_card":  "Zacznij tutaj",
    "read_min":         "min czytania",
    "updated_label":    "Aktualizacja",
    "toc_title":        "W skrócie",
    "related_articles": "Czytaj dalej",
    "related_tours":    "Pasujące wycieczki KeRo",
    "cta_see":          "Zobacz wycieczkę i sprawdź termin",
    "faq_title":        "Najczęściej zadawane pytania",
    "all_articles":     "Wszystkie poradniki",
    "back_to_blog":     "Poradnik turystyczny",
    "home":             "Start",
    "from_price":       "od",
    "category_label":   BLOG_CATEGORIES,
}

# Dates: the day the section is prepared. These become the real datePublished /
# dateModified when BLOG_PUBLISHED is flipped on and the site is deployed.
_PREP_DATE = "2026-11-10"

# ---------------------------------------------------------------------------
# ARTICLES
# ---------------------------------------------------------------------------
ARTICLES = [

    # =====================================================================
    # 1) CAIRO FROM HURGHADA
    # =====================================================================
    {
        "slug": "wycieczka-do-kairu-z-hurghady",
        "category": "zwiedzanie",
        "published": True,
        "date": _PREP_DATE,
        "updated": _PREP_DATE,
        "read_min": 9,
        "title": "Wycieczka do Kairu z Hurghady: piramidy, Sfinks i Wielkie Muzeum Egipskie",
        "card_title": "Wycieczka do Kairu z Hurghady: piramidy i GEM",
        "seo_title": "Wycieczka do Kairu z Hurghady - piramidy i GEM | KeRo",
        "meta_desc": "Wycieczka do Kairu z Hurghady: ile trwa dojazd, piramidy w Gizie, Sfinks i nowe Wielkie Muzeum Egipskie (GEM). Autokar czy samolot, dla kogo i jak się przygotować.",
        "excerpt": "Ile trwa dojazd z Hurghady do Kairu, co zobaczysz na płaskowyżu Giza i czym nowe Wielkie Muzeum Egipskie różni się od starego Muzeum Egipskiego - plus jak przygotować się na długi dzień.",
        "primary_kw": "wycieczka do Kairu z Hurghady",
        "intent": "informacyjny / porównawczy (planowanie jednodniowego wyjazdu do Kairu)",
        "secondary_kw": ["piramidy z Hurghady", "Wielkie Muzeum Egipskie", "GEM Kair", "Kair autokarem czy samolotem", "muzeum egipskie a GEM"],
        "related_tours": ["cairo-gem", "luxor"],
        "related_articles": ["wycieczka-do-luksoru-z-hurghady", "jak-zaplanowac-wycieczki-z-hurghady"],
        "hero": {
            "id": "BLOG-01-HERO",
            "file": "kair-z-hurghady-piramidy-gizy-hero.webp",
            "alt": "Piramidy w Gizie i Wielki Sfinks na pustynnym płaskowyżu pod Kairem o złotej godzinie.",
            "caption": "Płaskowyż Giza - piramidy i Wielki Sfinks to główny cel jednodniowej wycieczki z Hurghady.",
        },
        "images": {
            "BLOG-01-INLINE-01": {
                "id": "BLOG-01-INLINE-01",
                "file": "kair-wielkie-muzeum-egipskie.webp",
                "alt": "Ilustracja: monumentalne, nowoczesne wnętrze muzeum ze starożytnymi egipskimi posągami, w stylu Wielkiego Muzeum Egipskiego.",
                "caption": "Ilustracja poglądowa w stylu Wielkiego Muzeum Egipskiego (GEM), które otwarto w pełni 1 listopada 2025 roku.",
            },
        },
        "toc": [
            "Ile trwa dojazd z Hurghady do Kairu",
            "Autokar czy samolot - jak dotrzeć do Kairu",
            "Co zobaczysz: Giza, Sfinks i Wielkie Muzeum Egipskie",
            "Stare Muzeum Egipskie a nowe GEM",
            "Dla kogo jest wersja jednodniowa",
            "Jak się przygotować i ile to kosztuje",
        ],
        "body": [
            {"t": "p", "text": "Kair z piramidami w Gizie to dla wielu osób najważniejszy punkt wakacji w Egipcie - i da się go zrealizować nawet wtedy, gdy nocujesz nad Morzem Czerwonym. Z Hurghady jedzie się na jeden dzień, więc warto wiedzieć, ile zajmuje dojazd, co realnie zobaczysz i jak przygotować się na wcześnie rozpoczynający się, długi dzień. Poniżej konkrety, bez upiększania."},

            {"t": "h2", "text": "Ile trwa dojazd z Hurghady do Kairu"},
            {"t": "p", "text": "Hurghada i Kair dzieli mniej więcej **450-500 km** drogą lądową. W zależności od trasy, postojów i kontroli przejazd w jedną stronę zajmuje najczęściej od około **5 do 7 godzin**. To oznacza, że wersja jednodniowa jest wykonalna, ale wymaga bardzo wczesnej pobudki i powrotu późnym wieczorem. Dokładną godzinę odbioru spod hotelu potwierdzamy indywidualnie na WhatsAppie - podawane wcześniej orientacyjne godziny nie są gwarantowane."},
            {"t": "note", "title": "W skrócie", "text": "Jednodniowy Kair z Hurghady = długi dzień w drodze i intensywne zwiedzanie. Jeśli zależy Ci na spokojniejszym tempie, rozważ nocleg w Kairze we własnym zakresie i dłuższy pobyt."},

            {"t": "h2", "text": "Autokar czy samolot - jak dotrzeć do Kairu"},
            {"t": "p", "text": "W praktyce masz dwie drogi do Kairu: lądową i lotniczą. [Wycieczka KeRo do Kairu](tour:cairo-gem) odbywa się **klimatyzowanym minibusem** w obie strony, z przewodnikiem i obiadem - to rozwiązanie bez organizowania czegokolwiek samodzielnie. Przelot z Hurghady do Kairu trwa około godziny i skraca sam transport, ale wiąże się z wyższym kosztem oraz koniecznością samodzielnego ogarnięcia lotniska, transferów i biletu, a i tak dochodzi dojazd na/z lotniska. Poniżej uczciwe porównanie."},
            {"t": "table",
             "head": ["", "Minibus / autokar", "Samolot (samodzielnie)"],
             "rows": [
                 ["Czas w jedną stronę", "ok. 5-7 godz. drogą", "ok. 1 godz. lotu + dojazdy i lotnisko"],
                 ["Organizacja", "wszystko po stronie KeRo (transfer, przewodnik, obiad)", "bilety i transfery organizujesz sam"],
                 ["Koszt", "niższy", "wyższy"],
                 ["Dla kogo", "budżetowo, jeden dzień, bez kombinowania", "gdy chcesz oszczędzić czas w drodze i masz większy budżet"],
             ]},
            {"t": "p", "text": "Jeśli Twoim celem jest zobaczyć piramidy i muzeum w jeden dzień bez logistycznej układanki, wersja autokarowa jest najprostsza. Jeśli masz większy budżet i źle znosisz wielogodzinne przejazdy, przelot bywa wygodniejszy - ale to już organizacja na własną rękę."},

            {"t": "h2", "text": "Co zobaczysz: Giza, Sfinks i Wielkie Muzeum Egipskie"},
            {"t": "p", "text": "Klasyczny jednodniowy program obejmuje dwa filary. Pierwszy to **płaskowyż Giza**: trzy wielkie piramidy (z piramidą Cheopsa na czele) oraz **Wielki Sfinks**. Drugi to **Wielkie Muzeum Egipskie (GEM)** u progu płaskowyżu. W trasie KeRo pojawia się też krótki postój w tradycyjnej wytwórni perfum i instytucie papirusu. To dużo wrażeń jak na jeden dzień, dlatego tempo bywa intensywne."},
            {"t": "image", "id": "BLOG-01-INLINE-01"},
            {"t": "p", "text": "GEM to dziś najważniejsza nowość w regionie. Muzeum otwarto w pełni **1 listopada 2025 roku**, a kompletną kolekcję grobową **Tutanchamona** udostępniono publiczności - po raz pierwszy w całości od odkrycia grobowca w 1922 roku. To największe muzeum na świecie poświęcone jednej cywilizacji, z dziesiątkami tysięcy eksponatów."},

            {"t": "h2", "text": "Stare Muzeum Egipskie a nowe GEM"},
            {"t": "p", "text": "Łatwo pomylić dwie różne instytucje. **Muzeum Egipskie na placu Tahrir** w centrum Kairu działa od ponad stu lat i wciąż prezentuje ogromną część zbiorów starożytności. **Wielkie Muzeum Egipskie (GEM)** przy płaskowyżu Giza to nowy, znacznie większy obiekt, do którego przeniesiono m.in. kolekcję Tutanchamona. Wycieczka KeRo prowadzi do **GEM** - to logiczne, bo stoi tuż obok piramid, dzięki czemu jeden dzień łączy obie największe atrakcje bez przejazdu przez zakorkowane centrum."},
            {"t": "table",
             "head": ["", "Muzeum Egipskie (Tahrir)", "Wielkie Muzeum Egipskie (GEM)"],
             "rows": [
                 ["Lokalizacja", "centrum Kairu, plac Tahrir", "przy płaskowyżu Giza, obok piramid"],
                 ["Charakter", "zabytkowe, historyczne wnętrza", "nowoczesny, bardzo duży obiekt"],
                 ["Kolekcja Tutanchamona", "przeniesiona do GEM", "prezentowana w całości"],
                 ["W programie KeRo", "nie", "tak"],
             ]},

            {"t": "h2", "text": "Dla kogo jest wersja jednodniowa"},
            {"t": "ul", "items": [
                "Dla osób, które mają w Hurghadzie ograniczoną liczbę dni i chcą zobaczyć piramidy oraz GEM bez przedłużania pobytu.",
                "Dla tych, którzy dobrze znoszą długie przejazdy i wczesną pobudkę.",
                "Dla rodzin i par, które wolą gotowy pakiet z przewodnikiem zamiast samodzielnej logistyki w wielkim mieście.",
            ]},
            {"t": "p", "text": "Jeśli marzysz o spokojnym, dwu- lub trzydniowym zwiedzaniu Kairu z wejściem do wnętrza piramidy i dłuższym czasem w muzeum, lepszym pomysłem będzie osobny, dłuższy wyjazd zorganizowany we własnym zakresie. Jednodniówka to świadomy kompromis: dużo zobaczysz, ale w szybkim tempie."},

            {"t": "h2", "text": "Jak się przygotować i ile to kosztuje"},
            {"t": "ul", "items": [
                "**Wygodne buty i ochrona przeciwsłoneczna** - na płaskowyżu jest słonecznie i przestronnie, dużo chodzenia.",
                "**Woda i mała przekąska** na drogę; obiad jest w cenie wycieczki KeRo.",
                "**Dokument tożsamości** i trochę gotówki na drobne wydatki (np. pamiątki, napoje).",
                "Nastaw się na **bardzo wczesny wyjazd** - dokładną godzinę odbioru potwierdzamy przez WhatsApp.",
            ]},
            {"t": "p", "text": "W cenie wycieczki KeRo do Kairu jest **transport klimatyzowanym minibusem w obie strony, obiad i profesjonalny przewodnik**. Bilety wstępu na poszczególne obiekty nie są wliczone w cenę - ich szczegóły potwierdzamy indywidualnie na WhatsAppie, bo stawki bywają aktualizowane. Aktualną cenę wyjazdu znajdziesz zawsze na [stronie wycieczki](tour:cairo-gem)."},
            {"t": "note", "title": "Rezerwacja i płatność", "text": "Kair i Luksor to jedyne wycieczki KeRo, które wymagają zaliczki: 50% ceny potwierdza rezerwację, a pozostałe 50% płacisz na początku wyjazdu. Pozostałe wycieczki nie wymagają przedpłaty - płacisz na starcie."},
            {"t": "cta", "tour": "cairo-gem", "text": "Gotowy na piramidy i GEM? Sprawdź aktualny termin i cenę jednodniowej wycieczki do Kairu z Hurghady."},
        ],
        "faq": [
            ["Czy wycieczkę do Kairu da się zrobić w jeden dzień z Hurghady?", "Tak. Dojazd w jedną stronę to zwykle 5-7 godzin, więc jest to długi dzień z wczesną pobudką i powrotem wieczorem. Program jednodniowy obejmuje piramidy w Gizie, Sfinksa i Wielkie Muzeum Egipskie."],
            ["Czy wycieczka obejmuje stare Muzeum Egipskie na placu Tahrir, czy nowe GEM?", "Program KeRo prowadzi do nowego Wielkiego Muzeum Egipskiego (GEM) przy płaskowyżu Giza, obok piramid. To właśnie tam przeniesiono m.in. pełną kolekcję Tutanchamona."],
            ["Czy bilety wstępu są w cenie?", "W cenie jest transport klimatyzowanym minibusem w obie strony, obiad i przewodnik. Bilety wstępu na obiekty nie są wliczone; ich szczegóły potwierdzamy przez WhatsApp, bo stawki bywają aktualizowane."],
            ["Czy trzeba wpłacać zaliczkę?", "Tak, przy Kairze i Luksorze. 50% ceny potwierdza rezerwację, a pozostałe 50% płacisz na początku wycieczki. Inne wycieczki nie wymagają przedpłaty."],
        ],
    },

    # =====================================================================
    # 2) LUXOR FROM HURGHADA
    # =====================================================================
    {
        "slug": "wycieczka-do-luksoru-z-hurghady",
        "category": "zwiedzanie",
        "published": True,
        "date": _PREP_DATE,
        "updated": _PREP_DATE,
        "read_min": 9,
        "title": "Wycieczka do Luksoru z Hurghady: Karnak, Dolina Królów i co warto wiedzieć",
        "card_title": "Wycieczka do Luksoru z Hurghady: Karnak i Dolina Królów",
        "seo_title": "Wycieczka do Luksoru z Hurghady - Karnak i Dolina Królów | KeRo",
        "meta_desc": "Wycieczka do Luksoru z Hurghady: ile trwa dojazd, Karnak, Dolina Królów, świątynia Hatszepsut i Kolosy Memnona. Wersja jednodniowa czy dłuższa i jak się przygotować.",
        "excerpt": "Luksor to muzeum starożytnego Egiptu pod gołym niebem. Sprawdź, ile trwa dojazd z Hurghady, co zobaczysz jednego dnia i czym Luksor różni się od wyjazdu do Kairu.",
        "primary_kw": "wycieczka do Luksoru z Hurghady",
        "intent": "informacyjny / planowanie (jednodniowy Luksor, porównanie z Kairem)",
        "secondary_kw": ["Luksor z Hurghady", "Dolina Królów", "świątynia Karnak", "Luksor czy Kair", "Luksor jednodniowa wycieczka"],
        "related_tours": ["luxor", "cairo-gem"],
        "related_articles": ["wycieczka-do-kairu-z-hurghady", "jak-zaplanowac-wycieczki-z-hurghady"],
        "hero": {
            "id": "BLOG-02-HERO",
            "file": "luksor-z-hurghady-karnak-hero.webp",
            "alt": "Gigantyczne kolumny sali hypostylowej w świątyni Karnak w Luksorze, oświetlone porannym słońcem.",
            "caption": "Sala hypostylowa w Karnaku - las kamiennych kolumn to jeden z najmocniejszych punktów dnia w Luksorze.",
        },
        "images": {
            "BLOG-02-INLINE-01": {
                "id": "BLOG-02-INLINE-01",
                "file": "luksor-dolina-krolow.webp",
                "alt": "Skaliste, pustynne wzgórza Doliny Królów na zachodnim brzegu Nilu w Luksorze z wejściami do grobowców.",
                "caption": "Dolina Królów na zachodnim brzegu Nilu - wykute w skale grobowce faraonów Nowego Państwa.",
            },
        },
        "toc": [
            "Ile trwa dojazd z Hurghady do Luksoru",
            "Co zobaczysz jednego dnia",
            "Jednodniowa wycieczka czy dłuższy pobyt",
            "Luksor czy Kair - który wyjazd wybrać",
            "Jak się przygotować",
        ],
        "body": [
            {"t": "p", "text": "Luksor bywa nazywany największym muzeum pod gołym niebem na świecie - i trudno się dziwić. Na obu brzegach Nilu skupia się tu wyjątkowa liczba świątyń i grobowców z czasów faraonów. Z Hurghady jest bliżej niż do Kairu, więc jednodniowy wyjazd jest spokojniejszy logistycznie. Oto, czego się spodziewać."},

            {"t": "h2", "text": "Ile trwa dojazd z Hurghady do Luksoru"},
            {"t": "p", "text": "Hurghadę i Luksor dzieli około **290 km**, a przejazd w jedną stronę to najczęściej **około 4 godzin**. To wyraźnie mniej niż do Kairu, dlatego jednodniowy Luksor jest mniej męczący i zostaje więcej czasu na samo zwiedzanie. Nadal jednak jest to pełny dzień z wczesnym startem - dokładną godzinę odbioru potwierdzamy na WhatsAppie."},

            {"t": "h2", "text": "Co zobaczysz jednego dnia"},
            {"t": "p", "text": "Program [jednodniowej wycieczki KeRo do Luksoru](tour:luxor) prowadzi przez najważniejsze punkty obu brzegów Nilu:"},
            {"t": "ul", "items": [
                "**Świątynia Karnak** - ogromny kompleks świątynny ze słynną salą hypostylową pełną gigantycznych kolumn.",
                "**Dolina Królów** - wykute w skale grobowce faraonów Nowego Państwa na zachodnim brzegu.",
                "**Świątynia Hatszepsut** - imponująca, tarasowa budowla wtulona w skalny klif.",
                "**Kolosy Memnona** - dwa monumentalne posągi strzegące miejsca po nieistniejącej już świątyni.",
            ]},
            {"t": "image", "id": "BLOG-02-INLINE-01"},
            {"t": "p", "text": "To mocno wypełniony dzień. W cenie jest **klimatyzowany minibus w obie strony, obiad i profesjonalny przewodnik**, który poukłada historię tych miejsc w całość - bez niego kamienie mówią znacznie mniej."},

            {"t": "h2", "text": "Jednodniowa wycieczka czy dłuższy pobyt"},
            {"t": "p", "text": "Jeden dzień wystarcza, by zobaczyć ikony Luksoru i wrócić na nocleg do Hurghady. Jeśli jednak jesteś pasjonatem starożytnego Egiptu, rozważ samodzielny, dłuższy pobyt w samym Luksorze: wtedy zmieścisz dodatkowo m.in. świątynię Luksor w centrum, Medinet Habu czy poranny lot balonem nad doliną. Dla większości turystów z Morza Czerwonego jednodniowy wypad to jednak najlepszy stosunek wrażeń do czasu."},
            {"t": "note", "title": "Dobrze wiedzieć", "text": "Latem w Luksorze bywa znacznie goręcej niż nad morzem - to wnętrze lądu, bez morskiej bryzy. Kapelusz, woda i ochrona przeciwsłoneczna to nie dodatek, tylko konieczność."},

            {"t": "h2", "text": "Luksor czy Kair - który wyjazd wybrać"},
            {"t": "p", "text": "To najczęstszy dylemat. Oba wyjazdy są jednodniowe, ale różnią się dystansem i charakterem. Kair to piramidy, Sfinks i wielkie muzeum (GEM); Luksor to świątynie i grobowce faraonów. Jeśli masz czas tylko na jeden, podpowiedź jest prosta: krótsza droga i spokojniejsze tempo - Luksor; piramidy jako cel życia - Kair."},
            {"t": "table",
             "head": ["", "Luksor", "Kair"],
             "rows": [
                 ["Dystans z Hurghady", "ok. 290 km (ok. 4 godz.)", "ok. 450-500 km (ok. 5-7 godz.)"],
                 ["Co zobaczysz", "Karnak, Dolina Królów, Hatszepsut, Kolosy Memnona", "piramidy w Gizie, Sfinks, Wielkie Muzeum Egipskie"],
                 ["Tempo dnia", "intensywne, ale krótsza droga", "bardzo długi dzień w trasie"],
                 ["Najlepsze dla", "miłośników świątyń i historii", "osób, dla których piramidy to priorytet numer jeden"],
             ]},
            {"t": "p", "text": "Jeśli chcesz zobaczyć i jedno, i drugie, zaplanuj je w osobne dni z przerwą na odpoczynek - oba to pełne, męczące wyjazdy. Więcej o układaniu takiego tygodnia znajdziesz w poradniku [jak zaplanować wycieczki z Hurghady](article:jak-zaplanowac-wycieczki-z-hurghady)."},

            {"t": "h2", "text": "Jak się przygotować"},
            {"t": "ul", "items": [
                "**Ochrona przed słońcem i upałem** - kapelusz, okulary, krem, dużo wody.",
                "**Wygodne buty** - w Karnaku i Dolinie Królów sporo się chodzi po nierównym terenie.",
                "**Dokument tożsamości** i gotówka na drobne wydatki oraz ewentualne bilety dodatkowe.",
                "Nastaw się na **wczesny wyjazd** - godzinę odbioru potwierdzamy przez WhatsApp.",
            ]},
            {"t": "note", "title": "Rezerwacja i płatność", "text": "Luksor, podobnie jak Kair, wymaga zaliczki: 50% ceny potwierdza rezerwację, a pozostałe 50% płacisz na początku wyjazdu. Bilety wstępu na obiekty nie są wliczone w cenę - potwierdzamy je przez WhatsApp."},
            {"t": "cta", "tour": "luxor", "text": "Chcesz zobaczyć Karnak i Dolinę Królów? Sprawdź aktualny termin i cenę jednodniowej wycieczki do Luksoru z Hurghady."},
        ],
        "faq": [
            ["Ile trwa dojazd z Hurghady do Luksoru?", "Około 4 godzin w jedną stronę (ok. 290 km). To krótsza droga niż do Kairu, dlatego jednodniowy Luksor jest mniej męczący."],
            ["Co obejmuje jednodniowa wycieczka do Luksoru?", "Najważniejsze punkty obu brzegów Nilu: świątynię Karnak, Dolinę Królów, świątynię Hatszepsut i Kolosy Memnona. W cenie jest klimatyzowany minibus w obie strony, obiad i przewodnik."],
            ["Luksor czy Kair, jeśli mam czas tylko na jeden wyjazd?", "Jeśli zależy Ci na krótszej drodze i spokojniejszym tempie, wybierz Luksor. Jeśli piramidy w Gizie są dla Ciebie priorytetem, wybierz Kair. Oba to pełne, męczące dni, więc nie planuj ich dzień po dniu."],
            ["Czy wycieczka do Luksoru wymaga zaliczki?", "Tak. Przy Luksorze i Kairze 50% ceny potwierdza rezerwację, a pozostałe 50% płacisz na początku wyjazdu."],
        ],
    },

    # =====================================================================
    # 3) ISLANDS: ORANGE BAY / MAGAWISH / WHITE ISLAND
    # =====================================================================
    {
        "slug": "wyspy-z-hurghady-orange-bay-magawish-white-island",
        "category": "morze",
        "published": True,
        "date": _PREP_DATE,
        "updated": _PREP_DATE,
        "read_min": 8,
        "title": "Orange Bay, Magawish i White Island - jak wybrać rejs na wyspy z Hurghady",
        "card_title": "Wyspy z Hurghady: Orange Bay, Magawish i White Island",
        "seo_title": "Wyspy z Hurghady: Orange Bay, Magawish, White Island | KeRo",
        "meta_desc": "Rejsy na wyspy z Hurghady: czym różnią się Orange Bay, Magawish i White Island, dwie czy trzy wyspy, prywatna łódź - i jak wybrać wycieczkę dopasowaną do siebie.",
        "excerpt": "Turkusowe laguny i białe łachy piasku wyglądają podobnie na zdjęciach, ale rejsy różnią się programem i tempem. Zobacz, czym różnią się popularne wyspy i która wycieczka pasuje do Ciebie.",
        "primary_kw": "wyspy z Hurghady",
        "intent": "porównawczy (wybór rejsu na wyspy Morza Czerwonego)",
        "secondary_kw": ["Orange Bay Hurghada", "White Island", "wyspa Magawish", "rejs z Hurghady", "prywatna łódź Hurghada"],
        "related_tours": ["three-islands", "orange-bay-hula-hula", "private-speedboat"],
        "related_articles": ["snorkeling-w-hurghadzie-rafy-i-delfiny", "jak-zaplanowac-wycieczki-z-hurghady"],
        "hero": {
            "id": "BLOG-03-HERO",
            "file": "wyspy-hurghada-orange-bay-hero.webp",
            "alt": "Turkusowa laguna z drewnianym pomostem i zacumowanymi łodziami wycieczkowymi u wybrzeża wyspy na Morzu Czerwonym pod Hurghadą.",
            "caption": "Orange Bay - jedna z najpopularniejszych wysp na całodniowych rejsach z Hurghady.",
        },
        "images": {
            "BLOG-03-INLINE-01": {
                "id": "BLOG-03-INLINE-01",
                "file": "wyspy-hurghada-white-island-piaszczysta-lacha.webp",
                "alt": "Biała piaszczysta łacha wyłaniająca się z płytkiej, turkusowej wody Morza Czerwonego.",
                "caption": "White Island to nie klasyczna wyspa, lecz piaszczysta łacha pośrodku morza - widoczna zależnie od pływów.",
            },
        },
        "toc": [
            "Czym różnią się te wyspy",
            "Dwie wyspy, trzy wyspy czy prywatna łódź",
            "Czego się spodziewać na pokładzie",
            "Co zabrać na rejs",
            "Którą wycieczkę wybrać",
        ],
        "body": [
            {"t": "p", "text": "Rejs na wyspy to jedna z tych wycieczek, którą z Hurghady robi niemal każdy - i słusznie. Turkusowa woda, biały piasek i przystanki na snorkeling to kwintesencja Morza Czerwonego. Na zdjęciach wszystko wygląda podobnie, ale program, liczba przystanków i tempo potrafią się różnić. Oto jak się w tym połapać."},

            {"t": "h2", "text": "Czym różnią się te wyspy"},
            {"t": "ul", "items": [
                "**Orange Bay** - najbardziej rozpoznawalna, z szeroką białą plażą i turkusową laguną; klasyk, który pojawia się w większości rejsów.",
                "**Magawish** - spokojniejszy przystanek na kąpiel i relaks w pocztówkowej scenerii, mniej zatłoczony.",
                "**White Island** - to nie klasyczna wyspa, lecz **piaszczysta łacha pośrodku morza**, która wynurza się zależnie od poziomu wody; idealna na zdjęcia i krótki postój.",
                "**Hula Hula** - druga popularna łacha/wysepka, często łączona z Orange Bay w wersji dwuwyspowej.",
            ]},
            {"t": "image", "id": "BLOG-03-INLINE-01"},

            {"t": "h2", "text": "Dwie wyspy, trzy wyspy czy prywatna łódź"},
            {"t": "p", "text": "KeRo ma trzy różne formuły rejsu i to głównie one decydują o wyborze:"},
            {"t": "table",
             "head": ["Wycieczka", "Co obejmuje", "Dla kogo"],
             "rows": [
                 ["[Trzy wyspy](tour:three-islands)", "Orange Bay + Magawish + White Island, snorkeling, obiad na pokładzie, prywatny transfer", "gdy chcesz zobaczyć jak najwięcej w jeden dzień"],
                 ["[Orange Bay + Hula Hula](tour:orange-bay-hula-hula)", "dwie wyspy, snorkeling, obiad, prywatny transfer", "spokojniejsze tempo, dwa mocne przystanki"],
                 ["[Prywatna łódź motorowa](tour:private-speedboat)", "łódź tylko dla Twojej grupy, White Island i własny program", "pary, rodziny i grupy ceniące prywatność"],
             ]},
            {"t": "p", "text": "Wersja trzywyspowa daje najwięcej różnorodności, dwuwyspowa - spokojniejszy rytm, a **prywatna łódź** to pełna swoboda: płyniecie we własnym gronie, bez tłumu i sztywnego planu. Pamiętaj, że cena prywatnej łodzi dotyczy **całej łodzi** (pakiet podstawowy 2-5 osób), a nie jednej osoby."},
            {"t": "note", "title": "Uczciwie o cenie prywatnej łodzi", "text": "150 euro to koszt całej łodzi w pakiecie 2-5 osób, nie od osoby. Grupy 5-10 osób wyceniamy indywidualnie w zależności od liczby osób i odpowiedniej łodzi - łódź przewidziana dla pięciu osób nie może legalnie zabrać dziesięciu. Szczegóły ustalamy na WhatsAppie."},

            {"t": "h2", "text": "Czego się spodziewać na pokładzie"},
            {"t": "p", "text": "W rejsach grupowych w cenie jest zwykle **prywatny transfer z hotelu i z powrotem, obiad na pokładzie, napoje bezalkoholowe i sprzęt do snorkelingu**. Dzień to naprzemienne pływanie łodzią, przystanki na wyspach i wejścia do wody z maską i rurką nad rafami. Tempo jest wakacyjne, ale to pełny dzień na słońcu i wodzie."},

            {"t": "h2", "text": "Co zabrać na rejs"},
            {"t": "ul", "items": [
                "Strój kąpielowy (najlepiej założony pod ubranie), ręcznik i rzeczy na zmianę.",
                "Krem z filtrem - ważne, by był **przyjazny rafom** - oraz kapelusz i okulary.",
                "Obuwie do wody, jeśli masz wrażliwe stopy, i lekką bluzę na powrót, gdy zrywa się wiatr.",
                "Woreczek wodoszczelny na telefon i trochę gotówki na drobne wydatki.",
            ]},

            {"t": "h2", "text": "Którą wycieczkę wybrać"},
            {"t": "p", "text": "Chcesz maksimum widoków i przystanków - wybierz [trzy wyspy](tour:three-islands). Wolisz spokojniejszy dzień - [dwie wyspy](tour:orange-bay-hula-hula). Zależy Ci na prywatności i własnym tempie - [prywatna łódź](tour:private-speedboat). Jeśli pod wodą interesują Cię głównie rafy i delfiny, zajrzyj też do poradnika o [snorkelingu w Hurghadzie](article:snorkeling-w-hurghadzie-rafy-i-delfiny)."},
            {"t": "note", "title": "Płatność", "text": "Rejsy na wyspy nie wymagają przedpłaty - płacisz na początku wycieczki, gotówką. Dostępność i szczegóły odbioru potwierdzamy przez WhatsApp."},
            {"t": "cta", "tour": "three-islands", "text": "Marzysz o turkusowej lagunie i snorkelingu? Sprawdź termin całodniowego rejsu na trzy wyspy z Hurghady."},
        ],
        "faq": [
            ["Czym różni się White Island od zwykłej wyspy?", "White Island to piaszczysta łacha pośrodku morza, która wynurza się zależnie od poziomu wody, a nie klasyczna wyspa z plażą. Świetnie wygląda na zdjęciach i służy jako krótki, efektowny przystanek."],
            ["Ile osób obejmuje cena prywatnej łodzi?", "Cena 150 euro dotyczy całej łodzi w pakiecie podstawowym 2-5 osób, a nie jednej osoby. Grupy 5-10 osób wyceniamy indywidualnie - łódź dla pięciu osób nie może legalnie zabrać dziesięciu."],
            ["Czy w cenie rejsu jest obiad i snorkeling?", "W rejsach grupowych w cenie jest zwykle prywatny transfer, obiad na pokładzie, napoje bezalkoholowe i sprzęt do snorkelingu. Szczegóły danej wycieczki znajdziesz na jej stronie."],
            ["Czy trzeba płacić zaliczkę za rejs na wyspy?", "Nie. Rejsy na wyspy nie wymagają przedpłaty - płacisz na początku wycieczki. Zaliczki dotyczą tylko Kairu i Luksoru."],
        ],
    },

    # =====================================================================
    # 4) DESERT SAFARI: QUAD vs SUPER SAFARI
    # =====================================================================
    {
        "slug": "safari-na-pustyni-hurghada-quad-czy-super-safari",
        "category": "pustynia",
        "published": True,
        "date": _PREP_DATE,
        "updated": _PREP_DATE,
        "read_min": 8,
        "title": "Quad Safari czy Super Safari w Hurghadzie - które safari na pustyni wybrać",
        "card_title": "Safari na pustyni: quad czy Super Safari?",
        "seo_title": "Safari na pustyni w Hurghadzie: quad czy Super Safari | KeRo",
        "meta_desc": "Safari na pustyni w Hurghadzie: czym różni się Quad Safari od Super Safari (quad, jeep 4x4 i spider car), co zabrać, bezpieczeństwo i dla kogo jest każda wersja.",
        "excerpt": "Quad, jeep 4x4, spider car, wioska beduińska i orientalny wieczór. Sprawdź, czym różni się zwykłe Quad Safari od pełnego Super Safari i jak przygotować się na pustynię.",
        "primary_kw": "safari quad Hurghada",
        "intent": "porównawczy (wybór rodzaju safari na pustyni)",
        "secondary_kw": ["super safari Hurghada", "quad Hurghada", "safari jeep Hurghada", "spider car Hurghada", "wioska beduińska"],
        "related_tours": ["vip-quad-safari", "vip-super-safari"],
        "related_articles": ["jak-zaplanowac-wycieczki-z-hurghady", "wyspy-z-hurghady-orange-bay-magawish-white-island"],
        "hero": {
            "id": "BLOG-04-HERO",
            "file": "safari-pustynia-hurghada-quad-hero.webp",
            "alt": "Rząd quadów na piaszczystym szlaku pustyni pod Hurghadą o zachodzie słońca, z tumanami kurzu.",
            "caption": "Przejażdżka quadem po pustyni pod Hurghadą to rdzeń każdego safari.",
        },
        "images": {
            "BLOG-04-INLINE-01": {
                "id": "BLOG-04-INLINE-01",
                "file": "super-safari-jeep-spider-car.webp",
                "alt": "Terenowy jeep 4x4 i niska, odkryta buggy-riksza typu spider car na pustynnym torze pod Hurghadą.",
                "caption": "Super Safari dokłada do quada jazdę jeepem 4x4 i spider carem - odkrytym pojazdem typu buggy.",
            },
        },
        "toc": [
            "Co łączy obie wersje safari",
            "Quad Safari a Super Safari - różnice",
            "Czym jest spider car",
            "Bezpieczeństwo i co zabrać",
            "Dla kogo która wersja",
        ],
        "body": [
            {"t": "p", "text": "Safari na pustyni to najpopularniejszy sposób, by oderwać się od plaży i poczuć trochę adrenaliny. Pod Hurghadą wybór sprowadza się zwykle do dwóch wariantów KeRo: klasycznego **Quad Safari** i rozbudowanego **Super Safari**. Różnią się głównie liczbą pojazdów i długością programu. Rozłóżmy to na części."},

            {"t": "h2", "text": "Co łączy obie wersje safari"},
            {"t": "p", "text": "Oba warianty mają wspólny szkielet: **prywatny transfer z hotelu i z powrotem**, przejażdżkę quadem po pustynnych szlakach, wizytę w **wiosce beduińskiej** (herbata, pieczony na miejscu chleb), krótką **jazdę na wielbłądzie** oraz **kolację i orientalny pokaz** wieczorem. To dlatego safari często wybiera się na popołudnie i wieczór - zachód słońca na pustyni robi wrażenie."},

            {"t": "h2", "text": "Quad Safari a Super Safari - różnice"},
            {"t": "p", "text": "Najprościej: [Quad Safari](tour:vip-quad-safari) stawia na quada i wieczór beduiński, a [Super Safari](tour:vip-super-safari) to **najbogatszy program** - do quada dokłada przejazd **jeepem 4x4** i **spider carem**. Jeśli chcesz spróbować różnych pojazdów w jeden wieczór, Super Safari jest naturalnym wyborem."},
            {"t": "image", "id": "BLOG-04-INLINE-01"},
            {"t": "table",
             "head": ["", "Quad Safari", "Super Safari"],
             "rows": [
                 ["Pojazdy", "quad", "quad + jeep 4x4 + spider car"],
                 ["Wioska beduińska i wielbłąd", "tak", "tak"],
                 ["Kolacja i pokaz orientalny", "tak", "tak"],
                 ["Program", "krótszy, skupiony na quadzie", "najbardziej rozbudowany"],
                 ["Dla kogo", "pierwszy raz na pustyni, prościej", "chcesz maksimum atrakcji i pojazdów"],
             ]},

            {"t": "h2", "text": "Czym jest spider car"},
            {"t": "p", "text": "To pytanie wraca najczęściej. **Spider car** to niski, odkryty pojazd terenowy typu buggy - coś pomiędzy gokartem a małym autem terenowym - prowadzony na piaszczystym torze. Jeśli szukasz w ofercie \"buggy\", to właśnie ten pojazd; u KeRo pojawia się jako element **Super Safari**, a nie osobnej wycieczki. Dzięki temu w jeden wieczór przesiadasz się między quadem, jeepem i spider carem."},

            {"t": "h2", "text": "Bezpieczeństwo i co zabrać"},
            {"t": "ul", "items": [
                "**Chusta lub komin na twarz** - pustynny piasek potrafi dać się we znaki, zwłaszcza w kolumnie quadów.",
                "**Okulary** (najlepiej przylegające) i ochrona przeciwsłoneczna.",
                "**Zakryte, wygodne ubranie i buty** - wieczorem na pustyni szybko robi się chłodno.",
                "Jedź **rozważnie**, trzymaj dystans do pojazdu z przodu i słuchaj instruktora - to nie wyścig.",
            ]},
            {"t": "note", "title": "Dobrze wiedzieć", "text": "To oferta VIP w zakresie transferów (prywatny dojazd i powrót), ale same aktywności odbywają się w miejscu wspólnym z innymi gośćmi. Nastawienie \"prywatna pustynia tylko dla nas\" byłoby nieuczciwe - a dobra zabawa i tak jest gwarantowana."},

            {"t": "h2", "text": "Dla kogo która wersja"},
            {"t": "p", "text": "Pierwsze safari, prostszy program i skupienie na quadzie - wybierz [Quad Safari](tour:vip-quad-safari). Chcesz spróbować wszystkiego: quada, jeepa i spider cara w jeden wieczór - wybierz [Super Safari](tour:vip-super-safari). Obie wersje kończą się tak samo dobrze: kolacją i pokazem pod rozgwieżdżonym niebem."},
            {"t": "note", "title": "Płatność", "text": "Safari nie wymaga przedpłaty - płacisz na początku wycieczki, gotówką. Dostępność i godzinę odbioru potwierdzamy przez WhatsApp."},
            {"t": "cta", "tour": "vip-super-safari", "text": "Chcesz quada, jeepa i spider cara w jeden wieczór? Sprawdź termin Super Safari z Hurghady."},
        ],
        "faq": [
            ["Czym różni się Quad Safari od Super Safari?", "Quad Safari skupia się na przejażdżce quadem, wiosce beduińskiej oraz kolacji z pokazem. Super Safari to najbogatszy program - dokłada jazdę jeepem 4x4 i spider carem."],
            ["Czy u KeRo jest osobna wycieczka buggy?", "Pojazd typu buggy, czyli spider car, jest elementem Super Safari, a nie osobnej wycieczki. W jeden wieczór przesiadasz się między quadem, jeepem 4x4 i spider carem."],
            ["Co zabrać na safari na pustyni?", "Chustę lub komin na twarz chroniący przed piaskiem, przylegające okulary, ochronę przeciwsłoneczną oraz zakryte, wygodne ubranie i buty - wieczorem na pustyni bywa chłodno."],
            ["Czy safari jest prywatne?", "Prywatny jest transfer z hotelu i z powrotem. Same aktywności odbywają się w miejscu wspólnym z innymi gośćmi."],
        ],
    },

    # =====================================================================
    # 5) SNORKELING & MARINE LIFE
    # =====================================================================
    {
        "slug": "snorkeling-w-hurghadzie-rafy-i-delfiny",
        "category": "morze",
        "published": True,
        "date": _PREP_DATE,
        "updated": _PREP_DATE,
        "read_min": 8,
        "title": "Snorkeling w Hurghadzie - rafy koralowe, dzikie delfiny i jak wybrać wycieczkę",
        "card_title": "Snorkeling w Hurghadzie: rafy i dzikie delfiny",
        "seo_title": "Snorkeling w Hurghadzie: rafy, delfiny, jak wybrać rejs | KeRo",
        "meta_desc": "Snorkeling w Hurghadzie: co zobaczysz pod wodą, gdzie szukać dzikich delfinów (Dolphin House), co zabrać, zasady bezpieczeństwa i jak wybrać rejs snorkelingowy.",
        "excerpt": "Morze Czerwone to jedno z najlepszych miejsc do snorkelingu na świecie. Zobacz, co realnie zobaczysz pod wodą, jak to jest z dzikimi delfinami i jak wybrać dobry rejs.",
        "primary_kw": "snorkeling Hurghada",
        "intent": "informacyjny (snorkeling, życie morskie, wybór rejsu)",
        "secondary_kw": ["Dolphin House Hurghada", "dzikie delfiny Hurghada", "rafy Morze Czerwone", "co zabrać na snorkeling"],
        "related_tours": ["dolphin-house", "three-islands", "private-speedboat"],
        "related_articles": ["wyspy-z-hurghady-orange-bay-magawish-white-island", "jak-zaplanowac-wycieczki-z-hurghady"],
        "hero": {
            "id": "BLOG-05-HERO",
            "file": "snorkeling-hurghada-rafa-hero.webp",
            "alt": "Osoba w masce i rurce płynąca nad kolorową rafą koralową Morza Czerwonego z ławicą ryb.",
            "caption": "Rafy Morza Czerwonego należą do najbogatszych i najłatwiej dostępnych na świecie.",
        },
        "images": {
            "BLOG-05-INLINE-01": {
                "id": "BLOG-05-INLINE-01",
                "file": "dolphin-house-dzikie-delfiny.webp",
                "alt": "Grupa dzikich delfinów płynących przy powierzchni błękitnego morza w rejonie Dolphin House, z pustynnym wybrzeżem w tle.",
                "caption": "Dzikie delfiny w rejonie Dolphin House - obserwacja jest możliwa, ale nigdy gwarantowana.",
            },
        },
        "toc": [
            "Co zobaczysz pod wodą",
            "Dzikie delfiny - Dolphin House bez ściemy",
            "Jak wybrać rejs snorkelingowy",
            "Co zabrać i bezpieczeństwo",
            "Szacunek dla raf i zwierząt",
        ],
        "body": [
            {"t": "p", "text": "Morze Czerwone to jeden z powodów, dla których w ogóle przylatuje się do Hurghady. Ciepła, przejrzysta woda i rafy pełne życia sprawiają, że snorkeling jest tu dostępny praktycznie dla każdego - nie trzeba umieć nurkować. Oto, czego naprawdę się spodziewać i jak wybrać dobrą wycieczkę."},

            {"t": "h2", "text": "Co zobaczysz pod wodą"},
            {"t": "p", "text": "Rafy Morza Czerwonego słyną z bogactwa: kolorowe koralowce, ławice ryb, czasem żółwie czy rozgwiazdy. Już na niewielkiej głębokości, tuż przy powierzchni, dzieje się bardzo dużo. Większość rejsów KeRo zawiera przystanki na snorkeling nad rafami - zarówno te na [wyspy](article:wyspy-z-hurghady-orange-bay-magawish-white-island), jak i rejs do [Dolphin House](tour:dolphin-house)."},
            {"t": "note", "title": "Nie musisz być pływakiem olimpijskim", "text": "Kamizelka wypornościowa lub pianka pomagają utrzymać się na wodzie, a maska i rurka wystarczą, by oglądać rafę z powierzchni. Jeśli słabo pływasz, trzymaj się blisko łodzi i poproś o kamizelkę."},

            {"t": "h2", "text": "Dzikie delfiny - Dolphin House bez ściemy"},
            {"t": "p", "text": "**Dolphin House** (Sha'ab El Erg) to rafa znana z tego, że bywają tam **dzikie delfiny**. Słowo klucz: dzikie. To znaczy, że ich obecność i ewentualna możliwość popływania w pobliżu **nie są gwarantowane** - zależą od warunków naturalnych oraz zasad bezpieczeństwa i poszanowania zwierząt. Żadna uczciwa firma nie obieca Ci delfinów \"na pewno\"."},
            {"t": "image", "id": "BLOG-05-INLINE-01"},
            {"t": "p", "text": "To ważne rozróżnienie: Dolphin House to **dzikie delfiny w naturze**, a nie pokaz czy pływalnia z delfinami w niewoli. Jeśli dopisze szczęście, zobaczysz je z łodzi lub z wody z pewnego dystansu - i to jest znacznie cenniejsze przeżycie niż jakikolwiek pokaz."},

            {"t": "h2", "text": "Jak wybrać rejs snorkelingowy"},
            {"t": "ul", "items": [
                "**Cel pod wodą**: głównie rafy i wyspy - wybierz rejs na [trzy wyspy](tour:three-islands); szansa na dzikie delfiny - [Dolphin House](tour:dolphin-house).",
                "**Prywatność**: jeśli wolisz mały skład i własne tempo, rozważ [prywatną łódź](tour:private-speedboat).",
                "**Co w cenie**: sprawdź, czy są prywatny transfer, obiad i sprzęt do snorkelingu - w rejsach KeRo zwykle są.",
                "**Tempo dnia**: więcej przystanków = mniej czasu na każdym; mniej przystanków = spokojniej.",
            ]},

            {"t": "h2", "text": "Co zabrać i bezpieczeństwo"},
            {"t": "ul", "items": [
                "Własna **maska i rurka**, jeśli masz - lepiej dopasowane niż sprzęt z wypożyczenia; pianka, jeśli łatwo marzniesz.",
                "**Krem z filtrem przyjazny rafom** (reef-safe), kapelusz i koszulka z filtrem UV - łatwo o poparzenie pleców podczas pływania twarzą w dół.",
                "**Woda do picia** - słońce i sól mocno odwadniają.",
                "Słuchaj załogi w sprawie **prądów i miejsc wejścia do wody**; nie oddalaj się samotnie od łodzi.",
            ]},

            {"t": "h2", "text": "Szacunek dla raf i zwierząt"},
            {"t": "p", "text": "Rafa to żywy organizm. Kilka prostych zasad sprawia, że przetrwa dla kolejnych turystów:"},
            {"t": "ul", "items": [
                "**Nie dotykaj koralowców i nie stawaj na nich** - jeden krok potrafi zniszczyć lata wzrostu.",
                "**Nie karm ryb** ani innych zwierząt - zaburza to ich naturalne zachowania.",
                "Przy delfinach: **nie dotykaj, nie karm, nie ścigaj i nie otaczaj ich** - obserwuj z dystansem, który narzuca załoga.",
                "Nie zabieraj \"pamiątek\" z morza (muszli, korali) i nie zostawiaj śmieci.",
            ]},
            {"t": "note", "title": "Płatność", "text": "Rejsy snorkelingowe nie wymagają przedpłaty - płacisz na początku wycieczki. Dostępność i szczegóły odbioru potwierdzamy przez WhatsApp."},
            {"t": "cta", "tour": "dolphin-house", "text": "Chcesz spróbować szczęścia z dzikimi delfinami i popływać nad rafami? Sprawdź termin rejsu do Dolphin House."},
        ],
        "faq": [
            ["Czy na Dolphin House na pewno zobaczę delfiny?", "Nie. Delfiny w rejonie Dolphin House są dzikie, więc ich obecność i możliwość popływania w pobliżu nie są gwarantowane - zależą od warunków naturalnych oraz zasad bezpieczeństwa i poszanowania zwierząt."],
            ["Czy muszę umieć dobrze pływać, żeby snorkelować?", "Nie musisz być zaawansowanym pływakiem. Kamizelka wypornościowa lub pianka pomagają utrzymać się na wodzie, a rafę ogląda się z powierzchni. Jeśli słabo pływasz, trzymaj się blisko łodzi i poproś o kamizelkę."],
            ["Co zabrać na snorkeling?", "Własną maskę i rurkę, jeśli masz, krem z filtrem przyjazny rafom, koszulkę z filtrem UV, kapelusz i wodę do picia. Sprzęt do snorkelingu jest zwykle w cenie rejsu KeRo."],
            ["Czy Dolphin House to delfiny w niewoli?", "Nie. To dzikie delfiny w ich naturalnym środowisku, a nie pokaz ani pływalnia z delfinami w niewoli."],
        ],
    },

    # =====================================================================
    # 6) PLANNING HUB
    # =====================================================================
    {
        "slug": "jak-zaplanowac-wycieczki-z-hurghady",
        "category": "planowanie",
        "published": True,
        "date": _PREP_DATE,
        "updated": _PREP_DATE,
        "read_min": 10,
        "title": "Jak zaplanować wycieczki podczas wakacji w Hurghadzie",
        "card_title": "Jak zaplanować wycieczki z Hurghady",
        "seo_title": "Jak zaplanować wycieczki z Hurghady - poradnik | KeRo",
        "meta_desc": "Jak zaplanować wycieczki w Hurghadzie: rodzaje wypraw, ile dni na co, transfery z hotelu (Makadi, Sahl Hasheesh, Safaga), rezerwacja przez WhatsApp i płatności.",
        "excerpt": "Morze, pustynia, kultura i atrakcje - w Hurghadzie jest w czym wybierać. Zobacz, jak mądrze rozłożyć wycieczki w ciągu tygodnia i jak działa rezerwacja oraz płatność.",
        "primary_kw": "wycieczki z Hurghady",
        "intent": "informacyjny / cornerstone (planowanie całego tygodnia wycieczek)",
        "secondary_kw": ["co robić w Hurghadzie", "wycieczki fakultatywne Hurghada", "transfer z hotelu Hurghada", "Makadi Bay wycieczki", "Sahl Hasheesh"],
        "related_tours": ["three-islands", "cairo-gem", "luxor", "vip-super-safari", "dolphin-house"],
        "related_articles": ["wycieczka-do-kairu-z-hurghady", "wycieczka-do-luksoru-z-hurghady", "wyspy-z-hurghady-orange-bay-magawish-white-island", "safari-na-pustyni-hurghada-quad-czy-super-safari", "snorkeling-w-hurghadzie-rafy-i-delfiny"],
        "hero": {
            "id": "BLOG-06-HERO",
            "file": "planowanie-wycieczek-hurghada-hero.webp",
            "alt": "Marina z zacumowanymi jachtami, kolorowymi budynkami i palmami w nadmorskim kurorcie nad Morzem Czerwonym.",
            "caption": "Hurghada to dobra baza wypadowa: morze, pustynia i zabytki Egiptu w zasięgu jednego dnia.",
        },
        # BLOG-06-INLINE-01 (7-day infographic) intentionally omitted: the supplied
        # graphic placed Luxor + Cairo on back-to-back days, contradicting this
        # article's core advice to separate the two long trips with a rest day.
        "images": {},
        "toc": [
            "Cztery rodzaje wycieczek",
            "Ile dni na co - przykładowy tydzień",
            "Transfery z hotelu i okolice Hurghady",
            "Jak rezerwować i płacić",
            "Nie mieszkasz w Hurghadzie?",
        ],
        "body": [
            {"t": "p", "text": "Hurghada to jedna z najwygodniejszych baz wypadowych w Egipcie: w zasięgu jednego dnia masz rafy Morza Czerwonego, pustynię i największe zabytki starożytności. Sztuka polega na tym, by nie przeładować programu i zostawić sobie czas na plażę. Oto jak poukładać wycieczki w sensowny tydzień."},

            {"t": "h2", "text": "Cztery rodzaje wycieczek"},
            {"t": "p", "text": "Ofertę najłatwiej podzielić na cztery grupy - i dobrze mieć po jednym punkcie z każdej:"},
            {"t": "ul", "items": [
                "**Morze i wyspy** - rejsy na [wyspy](article:wyspy-z-hurghady-orange-bay-magawish-white-island) (Orange Bay, Magawish, White Island) i [snorkeling](article:snorkeling-w-hurghadzie-rafy-i-delfiny), w tym [Dolphin House](tour:dolphin-house).",
                "**Pustynia i safari** - [Quad Safari lub Super Safari](article:safari-na-pustyni-hurghada-quad-czy-super-safari) z wioską beduińską i wieczorem orientalnym.",
                "**Historia i kultura** - całodniowe wyjazdy do [Kairu](article:wycieczka-do-kairu-z-hurghady) i [Luksoru](article:wycieczka-do-luksoru-z-hurghady).",
                "**Atrakcje i wyjątkowe przeżycia** - np. [jazda konna z kąpielą koni w morzu](tour:horse-riding-swimming) czy [gokarty w El Gouna](tour:el-gouna-go-kart).",
            ]},

            {"t": "h2", "text": "Ile dni na co - przykładowy tydzień"},
            {"t": "p", "text": "Najczęstszy błąd to wrzucenie dwóch długich wyjazdów (Kair i Luksor) dzień po dniu. Oba to męczące, kilkunastogodzinne dni - rozdziel je odpoczynkiem. Oto bezpieczny szkielet tygodnia:"},
            {"t": "table",
             "head": ["Dzień", "Plan", "Dlaczego tak"],
             "rows": [
                 ["1", "Odpoczynek, plaża, aklimatyzacja", "po locie warto złapać rytm i nie planować pobudki o świcie"],
                 ["2", "Rejs na wyspy / snorkeling", "lekki, przyjemny start wycieczek"],
                 ["3", "Luksor (całodniowy)", "krótsza droga niż Kair, mocny punkt kulturalny"],
                 ["4", "Plaża / basen", "dzień regeneracji po długim wyjeździe"],
                 ["5", "Safari na pustyni (popołudnie i wieczór)", "zachód słońca i kolacja beduińska"],
                 ["6", "Kair (całodniowy) albo spokojny dzień", "najdłuższy wyjazd - tylko gdy masz na niego siłę"],
                 ["7", "Lekko: zakupy, plaża, pakowanie", "unikaj dalekich wyjazdów tuż przed wylotem"],
             ]},
            {"t": "note", "title": "Zasada dnia przylotu i wylotu", "text": "Nie planuj dalekiej, całodniowej wycieczki w dniu przylotu ani tuż przed wylotem. Transfery lotniskowe i niepewne godziny potrafią pokrzyżować plany, a wczesna pobudka po nocnym locie to kiepski pomysł."},

            {"t": "h2", "text": "Transfery z hotelu i okolice Hurghady"},
            {"t": "p", "text": "KeRo obsługuje nie tylko samą Hurghadę, ale też pobliskie kurorty, m.in. **Makadi Bay, Sahl Hasheesh i Safagę**. Przy większości wycieczek transfer z hotelu i z powrotem jest wliczony w cenę (gdy opis wycieczki tak wskazuje). Im dalej Twój hotel od punktu zbiórki, tym wcześniejszy bywa odbiór - dlatego dokładną godzinę zawsze potwierdzamy indywidualnie na WhatsAppie. Podawane orientacyjnie godziny nie są gwarantowane."},

            {"t": "h2", "text": "Jak rezerwować i płacić"},
            {"t": "p", "text": "Rezerwacja jest prosta i odbywa się przez **WhatsApp**: wybierasz wycieczkę, podajesz hotel, liczbę osób i preferowaną datę, a my potwierdzamy dostępność i szczegóły odbioru. Zasady płatności:"},
            {"t": "ul", "items": [
                "**Większość wycieczek** (morze, pustynia, atrakcje) - **bez przedpłaty**; płacisz na początku wycieczki, gotówką.",
                "**Kair i Luksor** - **zaliczka 50%** potwierdza rezerwację, a pozostałe 50% płacisz na początku wyjazdu.",
            ]},
            {"t": "note", "title": "Dlaczego WhatsApp", "text": "Bezpośrednia rozmowa pozwala potwierdzić realną dostępność na Twój termin, dopasować odbiór do hotelu i odpowiedzieć po polsku na pytania - bez sztywnego, automatycznego koszyka, który nie zna lokalnych warunków."},

            {"t": "h2", "text": "Nie mieszkasz w Hurghadzie?"},
            {"t": "p", "text": "KeRo organizuje wycieczki z Hurghady i okolic. Jeśli Twój hotel jest w innym kurorcie nad Morzem Czerwonym, pomocny może być polski serwis **Egipskie Wakacje**, który opisuje wyprawy m.in. [z Marsa Alam](ext:https://egipskiewakacje.pl/wycieczki-z-marsa-alam/) i [z Sharm el-Sheikh](ext:https://egipskiewakacje.pl/wycieczki-z-sharm-el-sheikh/). To wygodny punkt startu, gdy planujesz [wycieczki spoza rejonu Hurghady](ext:https://egipskiewakacje.pl/)."},
            {"t": "p", "text": "Jeśli jednak nocujesz w Hurghadzie, Makadi Bay, Sahl Hasheesh lub Safadze - jesteś we właściwym miejscu. Zacznij od poradników powyżej, a potem po prostu [napisz do nas](url:/pl/#contact) z wybraną wycieczką i terminem."},
            {"t": "cta", "tour": "three-islands", "text": "Nie wiesz, od czego zacząć? Lekki, przyjemny rejs na wyspy to dobry pierwszy wybór - sprawdź termin."},
        ],
        "faq": [
            ["Ile wycieczek zmieścić w tygodniowe wakacje?", "Rozsądnie jest zaplanować 3-4 wycieczki i zostawić dni na plażę oraz odpoczynek. Unikaj łączenia dwóch długich wyjazdów (Kair i Luksor) dzień po dniu - oba są męczące."],
            ["Czy KeRo odbiera z hoteli poza Hurghadą?", "Tak, m.in. z Makadi Bay, Sahl Hasheesh i Safagi. Przy większości wycieczek transfer z hotelu i z powrotem jest w cenie, gdy opis tak wskazuje. Dokładną godzinę odbioru potwierdzamy przez WhatsApp."],
            ["Jak wygląda płatność?", "Większość wycieczek nie wymaga przedpłaty - płacisz na początku, gotówką. Kair i Luksor wymagają zaliczki 50% na potwierdzenie rezerwacji, a pozostałe 50% płacisz na starcie."],
            ["Mieszkam w Marsa Alam lub Sharm el-Sheikh - co wtedy?", "KeRo działa z Hurghady i okolic. Dla innych kurortów nad Morzem Czerwonym pomocny będzie polski serwis Egipskie Wakacje, który opisuje wyprawy m.in. z Marsa Alam i z Sharm el-Sheikh."],
        ],
    },

]

# Order shown on the index (lead/cornerstone first makes a strong entry card).
INDEX_ORDER = [
    "jak-zaplanowac-wycieczki-z-hurghady",
    "wycieczka-do-kairu-z-hurghady",
    "wycieczka-do-luksoru-z-hurghady",
    "wyspy-z-hurghady-orange-bay-magawish-white-island",
    "safari-na-pustyni-hurghada-quad-czy-super-safari",
    "snorkeling-w-hurghadzie-rafy-i-delfiny",
]
