# -*- coding: utf-8 -*-
"""
SEO content layer for Hurghada KeRo Tours & Transfer.

Kept separate from the authoritative catalog (data/tours.py) so that the search
metadata can evolve without touching prices / itineraries / inclusions.

Two maps, keyed by tour id then language (fr / pl / ro):

  META_DESC[tour_id][lang]      -> purpose-written meta description (~150 chars).
                                   Falls back to the tour intro in build.py if a
                                   tour id is missing here.
  GALLERY_ALT[tour_id][lang]    -> list of localized ALT strings, ONE per gallery
                                   image in sorted order (01.webp, 02.webp, ...).
                                   Each ALT describes the ACTUAL visible subject
                                   (verified against the gallery images and
                                   IMAGE_AUDIT.md). No "photo 1 / image 2"
                                   placeholders; no cross-tour mislabeling.

Rules enforced here (see IMAGE_AUDIT.md + the project brief):
  - Describe what is actually in the frame, in natural localized language.
  - Never label one attraction as a different one (Orange Bay != Magawish, etc.).
  - Wild dolphins are described as wild; captive-show imagery is not used at all.
  - Go-kart tile 05 is a generic indoor karting shot, so it is NOT tied to the
    El Gouna outdoor venue.
  - No keyword stuffing: the destination appears only where it is genuinely the
    subject, not on every single image.
"""

# ---------------------------------------------------------------------------
# Meta descriptions (per tour, per language). Prices mirror data/tours.py.
# ---------------------------------------------------------------------------
META_DESC = {
    "three-islands": {
        "fr": "Journée en bateau depuis Hurghada : Orange Bay, Magawish et White Island. Snorkeling, déjeuner à bord et transfert privé. 50 €/pers., sans acompte.",
        "pl": "Całodniowy rejs z Hurghady: Orange Bay, Magawish i White Island. Snorkeling, obiad na pokładzie i prywatny transfer. 50 €/os., bez przedpłaty.",
        "ro": "Zi cu barca din Hurghada: Orange Bay, Magawish și White Island. Snorkeling, prânz la bord și transfer privat. 50 €/pers., fără avans.",
    },
    "orange-bay-hula-hula": {
        "fr": "Sortie bateau depuis Hurghada vers Orange Bay et Hula Hula : lagons turquoise, snorkeling, déjeuner à bord, transfert privé. 40 €/pers., paiement au départ.",
        "pl": "Rejs z Hurghady na Orange Bay i Hula Hula: turkusowe laguny, snorkeling, obiad na pokładzie, prywatny transfer. 40 €/os., płatność na starcie.",
        "ro": "Ieșire cu barca din Hurghada spre Orange Bay și Hula Hula: lagune turcoaz, snorkeling, prânz la bord, transfer privat. 40 €/pers., plata la început.",
    },
    "private-speedboat": {
        "fr": "Bateau rapide privé au départ de Hurghada : White Island, snorkeling, dauphins selon conditions. 150 € le bateau (forfait 2-5 pers.), sans acompte.",
        "pl": "Prywatna łódź motorowa z Hurghady: White Island, snorkeling, delfiny zależnie od warunków. 150 € za łódź (2-5 os.), bez przedpłaty.",
        "ro": "Barcă rapidă privată din Hurghada: White Island, snorkeling, delfini în funcție de condiții. 150 € barca (2-5 pers.), fără avans.",
    },
    "dolphin-house": {
        "fr": "Sortie bateau vers Dolphin House depuis Hurghada : dauphins sauvages selon conditions, snorkeling sur les récifs, déjeuner à bord. 30 €/pers., sans acompte.",
        "pl": "Rejs do Dolphin House z Hurghady: dzikie delfiny zależnie od warunków, snorkeling na rafach, obiad na pokładzie. 30 €/os., bez przedpłaty.",
        "ro": "Ieșire cu barca spre Dolphin House din Hurghada: delfini sălbatici în funcție de condiții, snorkeling pe recife, prânz la bord. 30 €/pers., fără avans.",
    },
    "vip-quad-safari": {
        "fr": "Safari quad dans le désert de Hurghada : village bédouin, balade à chameau, dîner et spectacle. Transferts privés inclus. 35 €/pers., paiement au départ.",
        "pl": "Safari quadem na pustyni pod Hurghadą: wioska beduińska, jazda na wielbłądzie, kolacja i pokaz. Prywatne transfery. 35 €/os., płatność na starcie.",
        "ro": "Safari cu ATV în deșertul din Hurghada: sat beduin, plimbare cu cămila, cină și spectacol. Transferuri private. 35 €/pers., plata la plecare.",
    },
    "vip-super-safari": {
        "fr": "Super Safari à Hurghada : quad, jeep 4x4 et spider car, village bédouin, dîner et spectacle oriental. Transferts privés. 35 €/pers., sans acompte.",
        "pl": "Super Safari w Hurghadzie: quad, jeep 4x4 i spider car, wioska beduińska, kolacja i pokaz. Prywatne transfery. 35 €/os., bez przedpłaty.",
        "ro": "Super Safari la Hurghada: ATV, jeep 4x4 și spider car, sat beduin, cină și spectacol oriental. Transferuri private. 35 €/pers., fără avans.",
    },
    "cairo-gem": {
        "fr": "Excursion d'une journée au Caire depuis Hurghada : pyramides de Gizeh, Sphinx et Grand Musée égyptien. Minibus climatisé, guide et déjeuner. 85 €/pers.",
        "pl": "Całodniowa wycieczka do Kairu z Hurghady: piramidy w Gizie, Sfinks i Wielkie Muzeum Egipskie. Klimatyzowany minibus, przewodnik, obiad. 85 €/os.",
        "ro": "Excursie de o zi la Cairo din Hurghada: piramidele din Giza, Sfinxul și Marele Muzeu Egiptean. Minibuz climatizat, ghid, prânz. 85 €/pers.",
    },
    "luxor": {
        "fr": "Excursion à Louxor depuis Hurghada : Karnak, Vallée des Rois et temple d'Hatchepsout. Minibus climatisé, guide et déjeuner inclus. 70 €/pers., acompte 50 % requis.",
        "pl": "Wycieczka do Luksoru z Hurghady: Karnak, Dolina Królów i świątynia Hatszepsut. Klimatyzowany minibus, przewodnik i obiad. 70 €/os., wymagana zaliczka 50%.",
        "ro": "Excursie la Luxor din Hurghada: Karnak, Valea Regilor și templul lui Hatșepsut. Minibuz climatizat, ghid și prânz incluse. 70 €/pers., avans 50% necesar.",
    },
    "horse-riding-swimming": {
        "fr": "Équitation à Hurghada entre désert et mer, avec baignade à cheval. Guide accompagnateur et transfert privé inclus. 35 €/pers., paiement au départ.",
        "pl": "Jazda konna w Hurghadzie między pustynią a morzem, z kąpielą na koniu. Przewodnik i prywatny transfer. 35 €/os., płatność na starcie.",
        "ro": "Călărie la Hurghada între deșert și mare, cu scăldat călare. Ghid însoțitor și transfer privat incluse. 35 €/pers., plata la început.",
    },
    "el-gouna-go-kart": {
        "fr": "Karting à El Gouna au départ de Hurghada : session de pilotage sur piste, transfert privé aller-retour inclus. 35 €/pers., sans acompte.",
        "pl": "Gokarty w El Gouna z Hurghady: sesja jazdy po torze, prywatny transfer w obie strony. 35 €/os., bez przedpłaty.",
        "ro": "Karting la El Gouna din Hurghada: sesiune de pilotaj pe pistă, transfer privat dus-întors. 35 €/pers., fără avans.",
    },
    "lion-cub-photo": {
        "fr": "Séance photo encadrée avec un lionceau à Hurghada, transfert privé inclus. 30 €/pers., sans acompte, paiement au départ. Soumis à disponibilité.",
        "pl": "Pamiątkowa sesja zdjęciowa z lwiątkiem w Hurghadzie, prywatny transfer. 30 €/os., bez przedpłaty, płatność na starcie. W zależności od dostępności.",
        "ro": "Ședință foto supravegheată cu un pui de leu la Hurghada, transfer privat. 30 €/pers., fără avans, plata la început. În funcție de disponibilitate.",
    },
}

# ---------------------------------------------------------------------------
# Per-image ALT text. Order matches sorted gallery files (01, 02, ...).
# Length MUST equal the number of gallery images for that tour (checked by
# scripts/test_seo.py).
# ---------------------------------------------------------------------------
GALLERY_ALT = {
    "cairo-gem": {
        "fr": [
            "Grande Pyramide de Gizeh au coucher du soleil avec un chameau au repos",
            "Le Grand Sphinx et la pyramide de Khéphren au coucher du soleil",
            "Grand Musée égyptien : hall intérieur avec une statue royale colossale",
            "Touristes et chameau devant les trois pyramides de Gizeh",
            "Couple à dos de chameau devant les pyramides de Gizeh",
        ],
        "pl": [
            "Wielka Piramida w Gizie o zachodzie słońca z odpoczywającym wielbłądem",
            "Wielki Sfinks i piramida Chefrena o zachodzie słońca",
            "Wielkie Muzeum Egipskie: hol z kolosalnym posągiem królewskim",
            "Turyści i wielbłąd przed trzema piramidami w Gizie",
            "Para na wielbłądach przed piramidami w Gizie",
        ],
        "ro": [
            "Marea Piramidă din Giza la apus, cu o cămilă în repaus",
            "Marele Sfinx și piramida lui Khafre la apus",
            "Marele Muzeu Egiptean: hol interior cu o statuie regală colosală",
            "Turiști și o cămilă în fața celor trei piramide din Giza",
            "Cuplu pe cămile în fața piramidelor din Giza",
        ],
    },
    "luxor": {
        "fr": [
            "Colonnade du temple de Louxor au coucher du soleil",
            "Temple d'Hatchepsout adossé à la falaise de Deir el-Bahari",
            "Couloir de tombeau peint dans la Vallée des Rois",
            "Statues osiriaques dans une cour du temple de Karnak",
            "Colonnes de la grande salle hypostyle de Karnak",
            "Statues colossales à l'entrée du temple de Louxor",
        ],
        "pl": [
            "Kolumnada świątyni w Luksorze o zachodzie słońca",
            "Świątynia Hatszepsut wtulona w klif Deir el-Bahari",
            "Malowany korytarz grobowca w Dolinie Królów",
            "Posągi ozyriackie na dziedzińcu świątyni w Karnaku",
            "Kolumny wielkiej sali hypostylowej w Karnaku",
            "Kolosalne posągi przy wejściu do świątyni w Luksorze",
        ],
        "ro": [
            "Colonada templului din Luxor la apus",
            "Templul lui Hatșepsut lipit de faleza de la Deir el-Bahari",
            "Coridor pictat de mormânt în Valea Regilor",
            "Statui osiriace într-o curte a templului Karnak",
            "Coloanele marii săli hipostile din Karnak",
            "Statui colosale la intrarea templului din Luxor",
        ],
    },
    "vip-quad-safari": {
        "fr": [
            "Randonnée en quad dans les dunes du désert de Hurghada",
            "Quads soulevant la poussière sur une piste du désert",
            "Pilotage de quad dans le désert",
            "Groupe en quad dans le désert ouvert",
            "Balade à dos de chameau dans le désert",
        ],
        "pl": [
            "Przejażdżka quadem po wydmach pustyni pod Hurghadą",
            "Quady wzbijające kurz na pustynnym szlaku",
            "Jazda quadem po pustyni",
            "Grupa na quadach na otwartej pustyni",
            "Przejażdżka na wielbłądzie po pustyni",
        ],
        "ro": [
            "Tură cu ATV-ul printre dunele deșertului din Hurghada",
            "ATV-uri ridicând praful pe o pistă din deșert",
            "Pilotaj de ATV în deșert",
            "Grup cu ATV-uri în deșertul deschis",
            "Plimbare cu cămila în deșert",
        ],
    },
    "vip-super-safari": {
        "fr": [
            "Spider cars alignés dans le désert",
            "Jeep 4x4 en safari dans le désert",
            "Chameaux dans un camp bédouin du désert",
            "Au volant d'un spider car sur le sable",
            "Quad et chameau dans le désert",
        ],
        "pl": [
            "Spider cary ustawione na pustyni",
            "Jeep 4x4 na pustynnym safari",
            "Wielbłądy w beduińskim obozie na pustyni",
            "Jazda spider carem po piasku",
            "Quad i wielbłąd na pustyni",
        ],
        "ro": [
            "Spider car-uri aliniate în deșert",
            "Jeep 4x4 în safari prin deșert",
            "Cămile într-o tabără beduină din deșert",
            "La volanul unui spider car pe nisip",
            "ATV și cămilă în deșert",
        ],
    },
    "three-islands": {
        "fr": [
            "Ponton en bois de l'île de Giftun au-dessus de l'eau turquoise (Orange Bay)",
            "Enseigne colorée Magawish sur la plage de l'île",
            "Plage avec parasols en paille et poufs au bord de la mer",
            "Bateau d'excursion amarré au ponton d'une île de la mer Rouge",
            "Plongeur en snorkeling devant un banc de poissons sur le récif",
        ],
        "pl": [
            "Drewniane molo na wyspie Giftun nad turkusową wodą (Orange Bay)",
            "Kolorowy napis Magawish na plaży wyspy",
            "Plaża z parasolami ze słomy i pufami nad morzem",
            "Łódź wycieczkowa przy molo na wyspie Morza Czerwonego",
            "Snorkeling przy ławicy ryb nad rafą",
        ],
        "ro": [
            "Pontonul de lemn al insulei Giftun deasupra apei turcoaz (Orange Bay)",
            "Firmă colorată Magawish pe plaja insulei",
            "Plajă cu umbrele de paie și puf-uri la malul mării",
            "Barcă de excursie ancorată la pontonul unei insule din Marea Roșie",
            "Snorkeling lângă un banc de pești deasupra recifului",
        ],
    },
    "orange-bay-hula-hula": {
        "fr": [
            "Balançoire dans la mer turquoise peu profonde à Orange Bay",
            "Hamac sur le sable blanc au bord de la mer",
            "Poufs et parasols sur la plage avec un ponton",
            "Lits de plage sous des parasols en feuilles de palmier",
            "Tables dans le lagon et bâtiment du complexe d'Orange Bay",
        ],
        "pl": [
            "Huśtawka w płytkim turkusowym morzu w Orange Bay",
            "Hamak na białym piasku nad morzem",
            "Pufy i parasole na plaży z molem",
            "Leżanki pod parasolami z liści palmowych na piasku",
            "Stoliki w lagunie i budynek ośrodka Orange Bay",
        ],
        "ro": [
            "Leagăn în marea turcoaz puțin adâncă la Orange Bay",
            "Hamac pe nisipul alb la malul mării",
            "Puf-uri și umbrele pe plajă, cu un ponton",
            "Paturi de plajă sub umbrele din frunze de palmier",
            "Mese în lagună și clădirea complexului Orange Bay",
        ],
    },
    "private-speedboat": {
        "fr": [
            "Vue aérienne d'un bateau rapide privé sur l'eau turquoise",
            "Passagers aux commandes du bateau rapide privé",
            "Plongeur en apnée près de dauphins sauvages",
            "Nageur aux côtés d'un dauphin sauvage",
            "Fruits frais à bord dans un lagon calme",
            "Équipement de snorkeling prêt à l'arrière du bateau",
        ],
        "pl": [
            "Widok z lotu ptaka na prywatną łódź motorową na turkusowej wodzie",
            "Goście za sterem prywatnej łodzi motorowej",
            "Freediver obok dzikich delfinów",
            "Pływak obok dzikiego delfina",
            "Świeże owoce na pokładzie w spokojnej lagunie",
            "Sprzęt do snorkelingu gotowy na rufie łodzi",
        ],
        "ro": [
            "Vedere aeriană a unei bărci rapide private pe apa turcoaz",
            "Oaspeți la cârma bărcii rapide private",
            "Scufundător în apnee lângă delfini sălbatici",
            "Înotător alături de un delfin sălbatic",
            "Fructe proaspete la bord într-o lagună liniștită",
            "Echipament de snorkeling pregătit la pupa bărcii",
        ],
    },
    "dolphin-house": {
        "fr": [
            "Plongeur en snorkeling près d'un groupe de dauphins sauvages",
            "Plongeur s'approchant d'un groupe de dauphins sauvages",
            "Enfant en snorkeling à côté d'un dauphin sauvage",
            "Plongeurs en snorkeling au-dessus d'un récif corallien coloré",
            "Récif corallien avec poissons tropicaux et une raie mouchetée",
        ],
        "pl": [
            "Snorkeling obok stada dzikich delfinów",
            "Snorkelujący zbliża się do stada dzikich delfinów",
            "Dziecko snorkelujące obok dzikiego delfina",
            "Snorkeling nad kolorową rafą koralową",
            "Rafa koralowa z tropikalnymi rybami i nakrapianą płaszczką",
        ],
        "ro": [
            "Snorkeling lângă un grup de delfini sălbatici",
            "Un snorkeler se apropie de un grup de delfini sălbatici",
            "Copil făcând snorkeling lângă un delfin sălbatic",
            "Snorkeling deasupra unui recif de corali colorat",
            "Recif de corali cu pești tropicali și o pisică-de-mare pătată",
        ],
    },
    "horse-riding-swimming": {
        "fr": [
            "Cheval dans la mer turquoise au bord de la plage",
            "Cavalier se baignant avec un cheval dans les vagues",
            "Galop à cheval le long de la plage",
            "Promenade d'un cheval blanc sur la plage",
            "Cheval dans l'eau peu profonde au coucher du soleil",
        ],
        "pl": [
            "Koń w turkusowym morzu przy plaży",
            "Jeździec kąpiący się z koniem w falach",
            "Galop konno wzdłuż plaży",
            "Spacer z białym koniem po plaży",
            "Koń w płytkiej wodzie o zachodzie słońca",
        ],
        "ro": [
            "Cal în marea turcoaz la malul plajei",
            "Călăreț scăldându-se cu un cal în valuri",
            "Galop călare de-a lungul plajei",
            "Plimbare cu un cal alb pe plajă",
            "Cal în apa puțin adâncă la apus",
        ],
    },
    "el-gouna-go-kart": {
        "fr": [
            "Jeune pilote casqué au volant d'un kart sur la piste",
            "Karts rassemblés sur la piste",
            "Karts dans un virage de la piste",
            "Pilote dans un kart de location sur la piste",
            "Deux pilotes de kart se saluent du poing",
        ],
        "pl": [
            "Młody kierowca w kasku za kierownicą gokarta na torze",
            "Gokarty zgromadzone na torze",
            "Gokarty na zakręcie toru",
            "Kierowca w wypożyczonym gokarcie na torze",
            "Dwóch kierowców gokartów przybija piątkę pięścią",
        ],
        "ro": [
            "Tânăr pilot cu cască la volanul unui kart pe pistă",
            "Karturi adunate pe pistă",
            "Karturi într-un viraj al pistei",
            "Pilot într-un kart de închiriat pe pistă",
            "Doi piloți de kart se salută cu pumnul",
        ],
    },
    "lion-cub-photo": {
        "fr": [
            "Lionceau tenu à côté d'un jeune enfant souriant",
            "Femme joue contre joue avec un lionceau",
            "Lionceau porté dans les bras pendant la séance photo",
            "Pose avec un lionceau en intérieur",
            "Lionceau allongé sur le sable devant une famille",
        ],
        "pl": [
            "Lwiątko trzymane obok uśmiechniętego małego dziecka",
            "Kobieta policzek przy policzku z lwiątkiem",
            "Lwiątko na rękach podczas sesji zdjęciowej",
            "Pozowanie z lwiątkiem we wnętrzu",
            "Lwiątko leżące na piasku przed rodziną",
        ],
        "ro": [
            "Pui de leu ținut lângă un copil mic zâmbitor",
            "Femeie obraz lângă obraz cu un pui de leu",
            "Pui de leu purtat în brațe în timpul ședinței foto",
            "Pozând cu un pui de leu în interior",
            "Pui de leu întins pe nisip în fața unei familii",
        ],
    },
}


def meta_desc(tour_id, lang):
    """Return the purpose-written meta description, or None to fall back."""
    return META_DESC.get(tour_id, {}).get(lang)


def gallery_alt(tour_id, lang, index, fallback):
    """Return the ALT for gallery image `index` (0-based), else `fallback`."""
    alts = GALLERY_ALT.get(tour_id, {}).get(lang)
    if alts and 0 <= index < len(alts):
        return alts[index]
    return fallback
