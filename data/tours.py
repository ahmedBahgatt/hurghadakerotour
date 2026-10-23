# -*- coding: utf-8 -*-
"""
Authoritative tour catalog for Hurghada KeRo Tours & Transfer.

This file is the single source of truth for the 11 excursions.
Prices are in EUR. The content here overrides any external reference site.

To edit a price, text or inclusion: change it here and rebuild (python3 build.py).
To disable a tour from the public site: set "active": False.
"""

# category ids -> used for filters. Labels are translated in data/i18n.py
# history | sea_islands | desert_adventure | other

TOURS = [

    # -----------------------------------------------------------------
    # TOUR 01 - Lion Cub Photo Experience  (RESTRICTED - review before promo)
    # -----------------------------------------------------------------
    {
        "id": "lion-cub-photo",
        "slug": "lion-cub-photo",
        "category": "other",
        "price": 30,
        "price_type": "per_person",
        "featured": False,
        "active": True,        # visibility also gated by PROMOTE_LION_CUB flag
        "ads_safe": False,
        "restricted": True,
        "image": "lion-cub-photo",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Séance photo avec un lionceau",
                "tagline": "Rencontre encadrée et photo souvenir",
                "intro": "Une rencontre encadrée avec un lionceau le temps d'une séance photo souvenir à Hurghada. Transfert privé depuis et vers votre hôtel inclus.",
                "highlights": [
                    "Rencontre encadrée avec un lionceau",
                    "Séance photo souvenir",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Séance photo encadrée",
                ],
                "conditions": [
                    "Soumis à la disponibilité, au règlement de l'établissement et aux exigences de sécurité et de bien-être animal.",
                    "Expérience en cours de revue réglementaire et de bien-être animal avant toute promotion.",
                ],
            },
            "pl": {
                "name": "Sesja zdjęciowa z lwiątkiem",
                "tagline": "Spotkanie pod opieką i zdjęcie na pamiątkę",
                "intro": "Spotkanie z lwiątkiem pod opieką opiekuna podczas pamiątkowej sesji zdjęciowej w Hurghadzie. W cenie prywatny transfer z hotelu i z powrotem.",
                "highlights": [
                    "Spotkanie z lwiątkiem pod opieką opiekuna",
                    "Pamiątkowa sesja zdjęciowa",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Sesja zdjęciowa pod opieką",
                ],
                "conditions": [
                    "W zależności od dostępności, regulaminu obiektu oraz wymogów bezpieczeństwa i dobrostanu zwierząt.",
                    "Oferta w trakcie przeglądu prawnego i pod kątem dobrostanu zwierząt przed promocją.",
                ],
            },
            "ro": {
                "name": "Ședință foto cu un pui de leu",
                "tagline": "Întâlnire supravegheată și fotografie de amintire",
                "intro": "O întâlnire supravegheată cu un pui de leu în timpul unei ședințe foto de amintire la Hurghada. Transfer privat dus-întors de la hotel inclus.",
                "highlights": [
                    "Întâlnire supravegheată cu un pui de leu",
                    "Ședință foto de amintire",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Ședință foto supravegheată",
                ],
                "conditions": [
                    "În funcție de disponibilitate, de regulamentul locației și de cerințele de siguranță și de bunăstare a animalelor.",
                    "Experiență aflată în curs de verificare legală și de bunăstare a animalelor înainte de promovare.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 02 - Cairo, Giza Pyramids & Grand Egyptian Museum
    # -----------------------------------------------------------------
    {
        "id": "cairo-gem",
        "slug": "cairo-giza-pyramids-grand-egyptian-museum",
        "category": "history",
        "price": 85,
        "price_type": "per_person",
        "featured": True,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "cairo-gem",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Le Caire : Pyramides de Gizeh & Grand Musée égyptien",
                "tagline": "Les Pyramides et le GEM depuis Hurghada",
                "intro": "Une journée complète au départ de Hurghada vers Le Caire pour découvrir les Pyramides de Gizeh et le nouveau Grand Musée égyptien. Transport en minibus climatisé, aller-retour, avec guide professionnel et déjeuner inclus.",
                "highlights": [
                    "Pyramides de Gizeh",
                    "Grand Sphinx",
                    "Grand Musée égyptien (GEM)",
                    "Fabrique de parfums traditionnelle",
                    "Institut du papyrus",
                ],
                "included": [
                    "Transport en minibus climatisé (aller-retour)",
                    "Déjeuner",
                    "Guide touristique professionnel",
                ],
                "conditions": [
                    "Transport en groupe en minibus climatisé : il ne s'agit pas d'un transport privé.",
                    "Détails des billets d'entrée aux sites à confirmer via WhatsApp.",
                ],
            },
            "pl": {
                "name": "Kair: piramidy w Gizie i Wielkie Muzeum Egipskie",
                "tagline": "Piramidy i GEM z Hurghady",
                "intro": "Całodniowa wycieczka z Hurghady do Kairu, aby zobaczyć piramidy w Gizie i nowe Wielkie Muzeum Egipskie. Przejazd klimatyzowanym minibusem w obie strony, z profesjonalnym przewodnikiem i obiadem.",
                "highlights": [
                    "Piramidy w Gizie",
                    "Wielki Sfinks",
                    "Wielkie Muzeum Egipskie (GEM)",
                    "Tradycyjna wytwórnia perfum",
                    "Instytut papirusu",
                ],
                "included": [
                    "Przejazd klimatyzowanym minibusem (w obie strony)",
                    "Obiad",
                    "Profesjonalny przewodnik",
                ],
                "conditions": [
                    "Przejazd grupowy klimatyzowanym minibusem - to nie jest transport prywatny.",
                    "Szczegóły biletów wstępu do obiektów do potwierdzenia przez WhatsApp.",
                ],
            },
            "ro": {
                "name": "Cairo: Piramidele din Giza și Marele Muzeu Egiptean",
                "tagline": "Piramidele și GEM din Hurghada",
                "intro": "O zi întreagă plecând din Hurghada spre Cairo pentru a descoperi Piramidele din Giza și noul Mare Muzeu Egiptean. Transport cu minibuz climatizat, dus-întors, cu ghid profesionist și prânz incluse.",
                "highlights": [
                    "Piramidele din Giza",
                    "Marele Sfinx",
                    "Marele Muzeu Egiptean (GEM)",
                    "Fabrică tradițională de parfumuri",
                    "Institutul de papirus",
                ],
                "included": [
                    "Transport cu minibuz climatizat (dus-întors)",
                    "Prânz",
                    "Ghid turistic profesionist",
                ],
                "conditions": [
                    "Transport în grup cu minibuz climatizat: nu este transport privat.",
                    "Detaliile biletelor de intrare la obiective se confirmă prin WhatsApp.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 03 - Luxor: Ancient Egypt Highlights
    # -----------------------------------------------------------------
    {
        "id": "luxor",
        "slug": "luxor-ancient-egypt-highlights",
        "category": "history",
        "price": 70,
        "price_type": "per_person",
        "featured": True,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "luxor",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Louxor : les trésors de l'Égypte ancienne",
                "tagline": "Karnak, la Vallée des Rois et plus encore",
                "intro": "Partez à la journée depuis Hurghada à la découverte de Louxor, véritable musée à ciel ouvert de l'Égypte antique. Transport en minibus climatisé, aller-retour, avec guide professionnel et déjeuner inclus.",
                "highlights": [
                    "Temple de Karnak",
                    "Vallée des Rois",
                    "Temple de la reine Hatchepsout",
                    "Colosses de Memnon",
                ],
                "included": [
                    "Transport en minibus climatisé (aller-retour)",
                    "Déjeuner",
                    "Guide touristique professionnel",
                ],
                "conditions": [
                    "Transport en groupe en minibus climatisé : il ne s'agit pas d'une excursion privée.",
                    "Détails des billets d'entrée aux sites à confirmer via WhatsApp.",
                ],
            },
            "pl": {
                "name": "Luksor: skarby starożytnego Egiptu",
                "tagline": "Karnak, Dolina Królów i więcej",
                "intro": "Całodniowa wyprawa z Hurghady do Luksoru - prawdziwego muzeum starożytnego Egiptu pod otwartym niebem. Przejazd klimatyzowanym minibusem w obie strony, z profesjonalnym przewodnikiem i obiadem.",
                "highlights": [
                    "Świątynia w Karnaku",
                    "Dolina Królów",
                    "Świątynia królowej Hatszepsut",
                    "Kolosy Memnona",
                ],
                "included": [
                    "Przejazd klimatyzowanym minibusem (w obie strony)",
                    "Obiad",
                    "Profesjonalny przewodnik",
                ],
                "conditions": [
                    "Przejazd grupowy klimatyzowanym minibusem - to nie jest wycieczka prywatna.",
                    "Szczegóły biletów wstępu do obiektów do potwierdzenia przez WhatsApp.",
                ],
            },
            "ro": {
                "name": "Luxor: comorile Egiptului antic",
                "tagline": "Karnak, Valea Regilor și nu numai",
                "intro": "O excursie de o zi din Hurghada pentru a descoperi Luxorul, un adevărat muzeu în aer liber al Egiptului antic. Transport cu minibuz climatizat, dus-întors, cu ghid profesionist și prânz incluse.",
                "highlights": [
                    "Templul Karnak",
                    "Valea Regilor",
                    "Templul reginei Hatșepsut",
                    "Coloșii lui Memnon",
                ],
                "included": [
                    "Transport cu minibuz climatizat (dus-întors)",
                    "Prânz",
                    "Ghid turistic profesionist",
                ],
                "conditions": [
                    "Transport în grup cu minibuz climatizat: nu este o excursie privată.",
                    "Detaliile biletelor de intrare la obiective se confirmă prin WhatsApp.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 04 - VIP Quad Safari
    # -----------------------------------------------------------------
    {
        "id": "vip-quad-safari",
        "slug": "vip-quad-safari",
        "category": "desert_adventure",
        "price": 35,
        "price_type": "per_person",
        "featured": False,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "vip-quad-safari",
        "schedule": None,
        "addons": [
            {
                "id": "lion-cub-addon",
                "price": 25,
                "price_type": "per_person",
                "restricted": True,
                "name": {
                    "fr": "Option séance photo avec un lionceau",
                    "pl": "Opcja: sesja zdjęciowa z lwiątkiem",
                    "ro": "Opțional: ședință foto cu un pui de leu",
                },
            },
        ],
        "content": {
            "fr": {
                "name": "VIP Quad Safari",
                "tagline": "Quad, village bédouin et soirée orientale",
                "intro": "Une échappée dans le désert d'Hurghada en quad, suivie d'une immersion dans un village bédouin traditionnel et d'une soirée orientale. Transferts privés aller-retour depuis votre hôtel inclus.",
                "highlights": [
                    "Randonnée en quad dans le désert",
                    "Visite d'un village bédouin traditionnel",
                    "Balade à dos de chameau",
                    "Thé bédouin et pain traditionnel",
                    "Dîner",
                    "Soirée et spectacle orientaux",
                ],
                "included": [
                    "Transferts privés aller-retour depuis l'hôtel",
                    "Quad, balade à chameau et activités du programme",
                    "Thé bédouin, pain traditionnel et dîner",
                    "Spectacle oriental",
                ],
                "conditions": [
                    "Expérience VIP - les transferts sont privés ; les activités se déroulent sur un site partagé avec d'autres visiteurs.",
                ],
            },
            "pl": {
                "name": "VIP Quad Safari",
                "tagline": "Quady, wioska beduińska i orientalny wieczór",
                "intro": "Wypad na pustynię pod Hurghadą quadem, a potem wizyta w tradycyjnej wiosce beduińskiej i orientalny wieczór. W cenie prywatne transfery z hotelu i z powrotem.",
                "highlights": [
                    "Przejażdżka quadem po pustyni",
                    "Wizyta w tradycyjnej wiosce beduińskiej",
                    "Przejażdżka na wielbłądzie",
                    "Herbata beduińska i tradycyjny chleb",
                    "Kolacja",
                    "Orientalny wieczór z pokazem",
                ],
                "included": [
                    "Prywatne transfery z hotelu i z powrotem",
                    "Quad, przejażdżka na wielbłądzie i aktywności z programu",
                    "Herbata beduińska, tradycyjny chleb i kolacja",
                    "Pokaz orientalny",
                ],
                "conditions": [
                    "Oferta VIP - transfery są prywatne; aktywności odbywają się w miejscu wspólnym z innymi gośćmi.",
                ],
            },
            "ro": {
                "name": "VIP Quad Safari",
                "tagline": "ATV, sat beduin și seară orientală",
                "intro": "O evadare în deșertul din Hurghada cu ATV-ul, urmată de o vizită într-un sat beduin tradițional și o seară orientală. Transferuri private dus-întors de la hotel incluse.",
                "highlights": [
                    "Tură cu ATV-ul în deșert",
                    "Vizită într-un sat beduin tradițional",
                    "Plimbare cu cămila",
                    "Ceai beduin și pâine tradițională",
                    "Cină",
                    "Seară și spectacol oriental",
                ],
                "included": [
                    "Transferuri private dus-întors de la hotel",
                    "ATV, plimbare cu cămila și activitățile din program",
                    "Ceai beduin, pâine tradițională și cină",
                    "Spectacol oriental",
                ],
                "conditions": [
                    "Experiență VIP - transferurile sunt private; activitățile au loc într-o locație comună cu alți vizitatori.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 05 - VIP Super Safari
    # -----------------------------------------------------------------
    {
        "id": "vip-super-safari",
        "slug": "vip-super-safari",
        "category": "desert_adventure",
        "price": 35,
        "price_type": "per_person",
        "featured": True,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "vip-super-safari",
        "schedule": None,
        "addons": [
            {
                "id": "lion-cub-addon",
                "price": 25,
                "price_type": "per_person",
                "restricted": True,
                "name": {
                    "fr": "Option séance photo avec un lionceau",
                    "pl": "Opcja: sesja zdjęciowa z lwiątkiem",
                    "ro": "Opțional: ședință foto cu un pui de leu",
                },
            },
        ],
        "content": {
            "fr": {
                "name": "VIP Super Safari",
                "tagline": "Quad, jeep ET spider car - le grand programme",
                "intro": "La version la plus complète de notre safari : au quad s'ajoutent une virée en jeep 4x4 et un spider car, avant le village bédouin et la soirée orientale. Transferts privés aller-retour inclus.",
                "highlights": [
                    "Randonnée en quad",
                    "Safari en jeep 4x4 dans le désert",
                    "Tour en spider car",
                    "Visite d'un village bédouin traditionnel",
                    "Balade à dos de chameau",
                    "Thé bédouin et pain traditionnel",
                    "Dîner",
                    "Soirée et spectacle orientaux",
                ],
                "included": [
                    "Transferts privés aller-retour depuis l'hôtel",
                    "Quad, jeep 4x4 et spider car",
                    "Balade à chameau et activités du programme",
                    "Thé bédouin, pain traditionnel et dîner",
                    "Spectacle oriental",
                ],
                "conditions": [
                    "Plus complet que le Quad Safari : il ajoute le safari en jeep 4x4 et le spider car.",
                    "Expérience VIP - les transferts sont privés ; les activités se déroulent sur un site partagé.",
                ],
            },
            "pl": {
                "name": "VIP Super Safari",
                "tagline": "Quad, jeep ORAZ spider car - pełny program",
                "intro": "Najbardziej rozbudowana wersja naszego safari: oprócz quada czekają na Ciebie przejazd jeepem 4x4 i spider car, a potem wioska beduińska i orientalny wieczór. Prywatne transfery w obie strony w cenie.",
                "highlights": [
                    "Przejażdżka quadem",
                    "Safari jeepem 4x4 po pustyni",
                    "Przejazd spider carem",
                    "Wizyta w tradycyjnej wiosce beduińskiej",
                    "Przejażdżka na wielbłądzie",
                    "Herbata beduińska i tradycyjny chleb",
                    "Kolacja",
                    "Orientalny wieczór z pokazem",
                ],
                "included": [
                    "Prywatne transfery z hotelu i z powrotem",
                    "Quad, jeep 4x4 i spider car",
                    "Przejażdżka na wielbłądzie i aktywności z programu",
                    "Herbata beduińska, tradycyjny chleb i kolacja",
                    "Pokaz orientalny",
                ],
                "conditions": [
                    "Bogatszy niż Quad Safari: dochodzą safari jeepem 4x4 oraz spider car.",
                    "Oferta VIP - transfery są prywatne; aktywności odbywają się w miejscu wspólnym.",
                ],
            },
            "ro": {
                "name": "VIP Super Safari",
                "tagline": "ATV, jeep ȘI spider car - programul complet",
                "intro": "Cea mai completă versiune a safari-ului nostru: pe lângă ATV, ai parte de o tură cu jeep-ul 4x4 și cu spider car, apoi satul beduin și seara orientală. Transferuri private dus-întors incluse.",
                "highlights": [
                    "Tură cu ATV-ul",
                    "Safari cu jeep 4x4 în deșert",
                    "Tură cu spider car",
                    "Vizită într-un sat beduin tradițional",
                    "Plimbare cu cămila",
                    "Ceai beduin și pâine tradițională",
                    "Cină",
                    "Seară și spectacol oriental",
                ],
                "included": [
                    "Transferuri private dus-întors de la hotel",
                    "ATV, jeep 4x4 și spider car",
                    "Plimbare cu cămila și activitățile din program",
                    "Ceai beduin, pâine tradițională și cină",
                    "Spectacol oriental",
                ],
                "conditions": [
                    "Mai complet decât Quad Safari: adaugă safari-ul cu jeep 4x4 și spider car-ul.",
                    "Experiență VIP - transferurile sunt private; activitățile au loc într-o locație comună.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 06 - Three Islands
    # -----------------------------------------------------------------
    {
        "id": "three-islands",
        "slug": "three-islands-orange-bay-magawish-white-island",
        "category": "sea_islands",
        "price": 50,
        "price_type": "per_person",
        "featured": True,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "three-islands",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Trois îles : Orange Bay + Magawish + White Island",
                "tagline": "Trois destinations de la mer Rouge en une journée",
                "intro": "Une journée en bateau sur la mer Rouge pour enchaîner trois lieux emblématiques : Orange Bay, l'île de Magawish et White Island. Baignade, arrêts snorkeling et déjeuner à bord, transfert privé inclus.",
                "highlights": [
                    "Orange Bay",
                    "Île de Magawish",
                    "White Island",
                    "Arrêts snorkeling",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Excursion en bateau sur la mer Rouge",
                    "Déjeuner à bord",
                    "Boissons sans alcool à bord",
                    "Équipement de snorkeling",
                ],
                "conditions": [
                    "Trois destinations en une seule journée.",
                ],
            },
            "pl": {
                "name": "Trzy wyspy: Orange Bay + Magawish + White Island",
                "tagline": "Trzy miejsca na Morzu Czerwonym w jeden dzień",
                "intro": "Całodniowy rejs po Morzu Czerwonym z trzema kultowymi przystankami: Orange Bay, wyspa Magawish i White Island. Kąpiel, przystanki na snorkeling i obiad na pokładzie, prywatny transfer w cenie.",
                "highlights": [
                    "Orange Bay",
                    "Wyspa Magawish",
                    "White Island",
                    "Przystanki na snorkeling",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Rejs po Morzu Czerwonym",
                    "Obiad na pokładzie",
                    "Napoje bezalkoholowe na pokładzie",
                    "Sprzęt do snorkelingu",
                ],
                "conditions": [
                    "Trzy miejsca w ciągu jednego dnia.",
                ],
            },
            "ro": {
                "name": "Trei insule: Orange Bay + Magawish + White Island",
                "tagline": "Trei destinații din Marea Roșie într-o singură zi",
                "intro": "O zi cu barca pe Marea Roșie pentru a lega trei locuri emblematice: Orange Bay, insula Magawish și White Island. Scăldat, opriri pentru snorkeling și prânz la bord, transfer privat inclus.",
                "highlights": [
                    "Orange Bay",
                    "Insula Magawish",
                    "White Island",
                    "Opriri pentru snorkeling",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Excursie cu barca pe Marea Roșie",
                    "Prânz la bord",
                    "Băuturi răcoritoare la bord",
                    "Echipament de snorkeling",
                ],
                "conditions": [
                    "Trei destinații într-o singură zi.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 07 - Orange Bay + Hula Hula
    # -----------------------------------------------------------------
    {
        "id": "orange-bay-hula-hula",
        "slug": "orange-bay-hula-hula-two-islands",
        "category": "sea_islands",
        "price": 40,
        "price_type": "per_person",
        "featured": False,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "orange-bay-hula-hula",
        "schedule": "08:30 - 17:00",
        "addons": [],
        "content": {
            "fr": {
                "name": "Orange Bay + Hula Hula : deux îles",
                "tagline": "Deux îles de la mer Rouge en une journée",
                "intro": "Une belle journée en mer pour découvrir deux îles phares de la région : Orange Bay et Hula Hula. Arrêts snorkeling, déjeuner à bord et transfert privé inclus. Horaire approximatif : 08h30 - 17h00.",
                "highlights": [
                    "Orange Bay",
                    "Île de Hula Hula",
                    "Arrêts snorkeling",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Excursion en bateau sur la mer Rouge",
                    "Déjeuner à bord",
                    "Boissons sans alcool à bord",
                    "Équipement de snorkeling",
                ],
                "conditions": [
                    "Deux îles en une journée.",
                    "Horaire 08h30 - 17h00 indicatif : ce n'est pas une heure de prise en charge garantie.",
                ],
            },
            "pl": {
                "name": "Orange Bay + Hula Hula: dwie wyspy",
                "tagline": "Dwie wyspy Morza Czerwonego w jeden dzień",
                "intro": "Udany dzień na morzu z dwiema popularnymi wyspami regionu: Orange Bay i Hula Hula. Przystanki na snorkeling, obiad na pokładzie i prywatny transfer w cenie. Przybliżone godziny: 08:30 - 17:00.",
                "highlights": [
                    "Orange Bay",
                    "Wyspa Hula Hula",
                    "Przystanki na snorkeling",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Rejs po Morzu Czerwonym",
                    "Obiad na pokładzie",
                    "Napoje bezalkoholowe na pokładzie",
                    "Sprzęt do snorkelingu",
                ],
                "conditions": [
                    "Dwie wyspy w ciągu jednego dnia.",
                    "Godziny 08:30 - 17:00 są orientacyjne - to nie jest gwarantowana godzina odbioru.",
                ],
            },
            "ro": {
                "name": "Orange Bay + Hula Hula: două insule",
                "tagline": "Două insule din Marea Roșie într-o singură zi",
                "intro": "O zi frumoasă pe mare pentru a descoperi două insule de referință din regiune: Orange Bay și Hula Hula. Opriri pentru snorkeling, prânz la bord și transfer privat incluse. Orar aproximativ: 08:30 - 17:00.",
                "highlights": [
                    "Orange Bay",
                    "Insula Hula Hula",
                    "Opriri pentru snorkeling",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Excursie cu barca pe Marea Roșie",
                    "Prânz la bord",
                    "Băuturi răcoritoare la bord",
                    "Echipament de snorkeling",
                ],
                "conditions": [
                    "Două insule într-o singură zi.",
                    "Orarul 08:30 - 17:00 este orientativ - nu este o oră de preluare garantată.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 08 - Private Speed Boat
    # -----------------------------------------------------------------
    {
        "id": "private-speedboat",
        "slug": "private-speed-boat",
        "category": "sea_islands",
        "price": 150,
        "price_type": "per_boat",
        "group_base": "2-5",
        "featured": True,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "private-speedboat",
        "schedule": None,
        "addons": [
            {"id": "orange-bay", "price": 15, "price_type": "per_person", "restricted": False,
             "name": {"fr": "Orange Bay", "pl": "Orange Bay", "ro": "Orange Bay"}},
            {"id": "hula-hula", "price": 15, "price_type": "per_person", "restricted": False,
             "name": {"fr": "Hula Hula", "pl": "Hula Hula", "ro": "Hula Hula"}},
            {"id": "ozirea", "price": 25, "price_type": "per_person", "restricted": False,
             "name": {"fr": "Île d'Ozirea", "pl": "Wyspa Ozirea", "ro": "Insula Ozirea"}},
        ],
        "content": {
            "fr": {
                "name": "Bateau rapide privé",
                "tagline": "Votre propre bateau rapide - 150 € au total",
                "intro": "Un bateau rapide rien que pour votre groupe, à la découverte de White Island et des eaux turquoise de la mer Rouge. Le prix de 150 € s'entend pour le bateau complet (forfait de base 2 à 5 personnes), et non par personne.",
                "highlights": [
                    "Bateau rapide privé pour votre groupe",
                    "White Island",
                    "Observation possible de dauphins dans leur milieu naturel (non garantie)",
                    "Arrêts snorkeling",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Bateau rapide privé pour le groupe",
                    "Équipement de snorkeling",
                    "Fruits frais, en-cas et boissons sans alcool",
                ],
                "conditions": [
                    "Prix de 150 € pour le bateau complet (forfait de base 2 à 5 personnes), pas par personne.",
                    "Groupes de 5 à 10 personnes : devis personnalisé selon la taille du groupe et le bateau adapté - contactez-nous via WhatsApp.",
                    "Un bateau prévu pour cinq personnes ne peut pas accueillir légalement dix personnes.",
                    "L'observation de dauphins dépend des conditions naturelles et n'est pas garantie.",
                ],
            },
            "pl": {
                "name": "Prywatna łódź motorowa",
                "tagline": "Łódź tylko dla Was - 150 € za całość",
                "intro": "Szybka łódź wyłącznie dla Twojej grupy, z wizytą na White Island i wśród turkusowych wód Morza Czerwonego. Cena 150 € dotyczy całej łodzi (pakiet podstawowy 2 do 5 osób), a nie jednej osoby.",
                "highlights": [
                    "Prywatna łódź motorowa dla Twojej grupy",
                    "White Island",
                    "Możliwość obserwacji delfinów w ich naturalnym środowisku (bez gwarancji)",
                    "Przystanki na snorkeling",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Prywatna łódź motorowa dla grupy",
                    "Sprzęt do snorkelingu",
                    "Świeże owoce, przekąski i napoje bezalkoholowe",
                ],
                "conditions": [
                    "Cena 150 € za całą łódź (pakiet podstawowy 2 do 5 osób), nie za osobę.",
                    "Grupy od 5 do 10 osób: wycena indywidualna w zależności od liczby osób i odpowiedniej łodzi - napisz do nas przez WhatsApp.",
                    "Łódź przewidziana dla pięciu osób nie może legalnie pomieścić dziesięciu osób.",
                    "Obserwacja delfinów zależy od warunków naturalnych i nie jest gwarantowana.",
                ],
            },
            "ro": {
                "name": "Barcă rapidă privată",
                "tagline": "Barca voastră privată - 150 € în total",
                "intro": "O barcă rapidă numai pentru grupul tău, pentru a descoperi White Island și apele turcoaz ale Mării Roșii. Prețul de 150 € este pentru barca întreagă (pachet de bază 2 până la 5 persoane), nu de persoană.",
                "highlights": [
                    "Barcă rapidă privată pentru grupul tău",
                    "White Island",
                    "Posibilitatea de a observa delfini în mediul lor natural (fără garanție)",
                    "Opriri pentru snorkeling",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Barcă rapidă privată pentru grup",
                    "Echipament de snorkeling",
                    "Fructe proaspete, gustări și băuturi răcoritoare",
                ],
                "conditions": [
                    "Preț de 150 € pentru barca întreagă (pachet de bază 2 până la 5 persoane), nu de persoană.",
                    "Grupuri de 5 până la 10 persoane: ofertă personalizată în funcție de numărul de persoane și de barca potrivită - scrie-ne pe WhatsApp.",
                    "O barcă pentru cinci persoane nu poate transporta legal zece persoane.",
                    "Observarea delfinilor depinde de condițiile naturale și nu este garantată.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 09 - El Gouna Go Kart
    # -----------------------------------------------------------------
    {
        "id": "el-gouna-go-kart",
        "slug": "el-gouna-go-kart",
        "category": "other",
        "price": 35,
        "price_type": "per_person",
        "featured": False,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "el-gouna-go-kart",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Karting à El Gouna",
                "tagline": "Sensations sur piste à El Gouna",
                "intro": "Direction El Gouna pour une séance de karting sur piste, pleine de sensations. Transfert privé aller-retour depuis votre hôtel inclus.",
                "highlights": [
                    "Séance de karting à El Gouna",
                    "Expérience de pilotage sur piste",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Séance de karting sur piste",
                ],
                "conditions": [
                    "La durée de 10 à 15 minutes correspond à la séance de pilotage, pas à l'ensemble de l'excursion.",
                ],
            },
            "pl": {
                "name": "Gokarty w El Gouna",
                "tagline": "Emocje na torze w El Gouna",
                "intro": "Wyprawa do El Gouna na emocjonującą sesję jazdy gokartami po torze. W cenie prywatny transfer z hotelu i z powrotem.",
                "highlights": [
                    "Sesja jazdy gokartem w El Gouna",
                    "Jazda po torze",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Sesja jazdy gokartem po torze",
                ],
                "conditions": [
                    "Czas 10-15 minut dotyczy samej jazdy, a nie całej wycieczki.",
                ],
            },
            "ro": {
                "name": "Karting la El Gouna",
                "tagline": "Senzații pe pistă la El Gouna",
                "intro": "Mergem la El Gouna pentru o sesiune de karting pe pistă, plină de senzații. Transfer privat dus-întors de la hotel inclus.",
                "highlights": [
                    "Sesiune de karting la El Gouna",
                    "Experiență de pilotaj pe pistă",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Sesiune de karting pe pistă",
                ],
                "conditions": [
                    "Durata de 10-15 minute se referă la sesiunea de pilotaj, nu la întreaga excursie.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 10 - Horse Riding: Desert, Beach & Swimming
    # -----------------------------------------------------------------
    {
        "id": "horse-riding-swimming",
        "slug": "horse-riding-desert-beach-swimming",
        "category": "desert_adventure",
        "price": 35,
        "price_type": "per_person",
        "featured": False,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "horse-riding-swimming",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Équitation : désert, plage et baignade",
                "tagline": "À cheval entre désert et mer",
                "intro": "Une balade à cheval qui relie le désert et le bord de mer, avec la possibilité de nager avec les chevaux dans la mer. Guide accompagnateur et transfert privé aller-retour inclus.",
                "highlights": [
                    "Balade à cheval dans le désert",
                    "Chevauchée au bord de la plage et de l'eau",
                    "Baignade avec les chevaux dans la mer",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Balade à cheval accompagnée",
                    "Guide accompagnateur professionnel",
                ],
                "conditions": [
                    "L'ambiance au coucher du soleil dépend des conditions du jour et n'est pas garantie.",
                ],
            },
            "pl": {
                "name": "Jazda konna: pustynia, plaża i kąpiel",
                "tagline": "Konno między pustynią a morzem",
                "intro": "Przejażdżka konna łącząca pustynię i brzeg morza, z możliwością kąpieli z końmi w morzu. W cenie przewodnik i prywatny transfer w obie strony.",
                "highlights": [
                    "Jazda konna po pustyni",
                    "Jazda wzdłuż plaży i wody",
                    "Kąpiel z końmi w morzu",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Jazda konna z opiekunem",
                    "Profesjonalny przewodnik towarzyszący",
                ],
                "conditions": [
                    "Klimat zachodu słońca zależy od warunków danego dnia i nie jest gwarantowany.",
                ],
            },
            "ro": {
                "name": "Călărie: deșert, plajă și scăldat",
                "tagline": "Călare între deșert și mare",
                "intro": "O plimbare călare care leagă deșertul de malul mării, cu posibilitatea de a înota cu caii în mare. Ghid însoțitor și transfer privat dus-întors incluse.",
                "highlights": [
                    "Plimbare călare în deșert",
                    "Călărie pe lângă plajă și apă",
                    "Scăldat cu caii în mare",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Plimbare călare însoțită",
                    "Ghid însoțitor profesionist",
                ],
                "conditions": [
                    "Atmosfera de apus depinde de condițiile din ziua respectivă și nu este garantată.",
                ],
            },
        },
    },

    # -----------------------------------------------------------------
    # TOUR 11 - Dolphin House
    # -----------------------------------------------------------------
    {
        "id": "dolphin-house",
        "slug": "dolphin-house",
        "category": "sea_islands",
        "price": 30,
        "price_type": "per_person",
        "featured": True,
        "active": True,
        "ads_safe": True,
        "restricted": False,
        "image": "dolphin-house",
        "schedule": None,
        "addons": [],
        "content": {
            "fr": {
                "name": "Dolphin House",
                "tagline": "À la rencontre des dauphins sauvages",
                "intro": "Une sortie en bateau vers Dolphin House, un site réputé de la mer Rouge où l'on peut parfois observer des dauphins sauvages. Snorkeling au-dessus des récifs coralliens, déjeuner à bord et transfert privé inclus.",
                "highlights": [
                    "Sortie en bateau vers Dolphin House",
                    "Observation possible de dauphins sauvages",
                    "Snorkeling au-dessus des récifs coralliens",
                ],
                "included": [
                    "Transfert privé aller-retour depuis l'hôtel",
                    "Excursion en bateau vers Dolphin House",
                    "Équipement de snorkeling",
                    "Déjeuner à bord",
                    "Boissons sans alcool à bord",
                ],
                "conditions": [
                    "L'observation des dauphins et la possibilité de nager à proximité ne sont pas garanties : elles dépendent des conditions naturelles et des bonnes pratiques de sécurité et de respect de la faune.",
                    "Les dauphins sont sauvages : il n'est pas question de les nourrir, de les toucher, de les poursuivre ni de les capturer.",
                ],
            },
            "pl": {
                "name": "Dolphin House",
                "tagline": "Spotkanie z dzikimi delfinami",
                "intro": "Rejs łodzią do Dolphin House - znanego miejsca na Morzu Czerwonym, gdzie czasem można obserwować dzikie delfiny. Snorkeling nad rafami koralowymi, obiad na pokładzie i prywatny transfer w cenie.",
                "highlights": [
                    "Rejs łodzią do Dolphin House",
                    "Możliwość obserwacji dzikich delfinów",
                    "Snorkeling nad rafami koralowymi",
                ],
                "included": [
                    "Prywatny transfer z hotelu i z powrotem",
                    "Rejs łodzią do Dolphin House",
                    "Sprzęt do snorkelingu",
                    "Obiad na pokładzie",
                    "Napoje bezalkoholowe na pokładzie",
                ],
                "conditions": [
                    "Obserwacja delfinów i możliwość pływania w ich pobliżu nie są gwarantowane: zależą od warunków naturalnych oraz zasad bezpieczeństwa i poszanowania dzikiej przyrody.",
                    "Delfiny są dzikie: nie wolno ich karmić, dotykać, ścigać ani łapać.",
                ],
            },
            "ro": {
                "name": "Dolphin House",
                "tagline": "În întâmpinarea delfinilor sălbatici",
                "intro": "O ieșire cu barca spre Dolphin House, un loc renumit din Marea Roșie unde uneori pot fi observați delfini sălbatici. Snorkeling deasupra recifelor de corali, prânz la bord și transfer privat incluse.",
                "highlights": [
                    "Ieșire cu barca spre Dolphin House",
                    "Posibilitatea de a observa delfini sălbatici",
                    "Snorkeling deasupra recifelor de corali",
                ],
                "included": [
                    "Transfer privat dus-întors de la hotel",
                    "Excursie cu barca spre Dolphin House",
                    "Echipament de snorkeling",
                    "Prânz la bord",
                    "Băuturi răcoritoare la bord",
                ],
                "conditions": [
                    "Observarea delfinilor și posibilitatea de a înota în apropierea lor nu sunt garantate: depind de condițiile naturale și de bunele practici de siguranță și de respect față de faună.",
                    "Delfinii sunt sălbatici: nu se pune problema de a-i hrăni, atinge, urmări sau captura.",
                ],
            },
        },
    },

]
