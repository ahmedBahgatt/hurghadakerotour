# -*- coding: utf-8 -*-
"""
UI strings and localization for FR / PL / RO.

All public-facing text (except the tour catalog in tours.py) lives here.
No English is shown to visitors.
"""

LANG_ORDER = ["fr", "pl", "ro"]

# Native language names for the switcher
LANG_NATIVE = {"fr": "Français", "pl": "Polski", "ro": "Română"}

# URL path segment for tour detail pages, per language
PATH_TOURS = {"fr": "excursions", "pl": "wycieczki", "ro": "excursii"}

# <html lang> and og:locale
HTML_LANG = {"fr": "fr", "pl": "pl", "ro": "ro"}
OG_LOCALE = {"fr": "fr_FR", "pl": "pl_PL", "ro": "ro_RO"}

# Macro-category labels (ids come from tours.py)
CATEGORIES = {
    "fr": {"sea_islands": "Mer & Îles", "desert_safari": "Safari & Désert",
           "history_culture": "Histoire & Culture", "activities": "Activités & Expériences"},
    "pl": {"sea_islands": "Morze i Wyspy", "desert_safari": "Safari i Pustynia",
           "history_culture": "Historia i Kultura", "activities": "Atrakcje i Wyjątkowe Przeżycia"},
    "ro": {"sea_islands": "Mare și Insule", "desert_safari": "Safari și Deșert",
           "history_culture": "Istorie și Cultură", "activities": "Activități și Experiențe Speciale"},
}

# Homepage category order
CATEGORY_ORDER = ["sea_islands", "desert_safari", "history_culture", "activities"]

# Short, persuasive localized intro per category (homepage section lead-in)
CATEGORY_INTRO = {
    "fr": {
        "sea_islands": "Îles paradisiaques, lagons turquoise et snorkeling sur les récifs de la mer Rouge.",
        "desert_safari": "Adrénaline dans le désert : quad, jeep, village bédouin et soirée orientale.",
        "history_culture": "Les grands trésors de l'Égypte ancienne, au départ de Hurghada.",
        "activities": "Des expériences uniques pour pimenter vos vacances à Hurghada.",
    },
    "pl": {
        "sea_islands": "Rajskie wyspy, turkusowe laguny i snorkeling na rafach Morza Czerwonego.",
        "desert_safari": "Adrenalina na pustyni: quady, jeep, wioska beduińska i orientalny wieczór.",
        "history_culture": "Największe skarby starożytnego Egiptu - z wyjazdem z Hurghady.",
        "activities": "Wyjątkowe doświadczenia, które urozmaicą wakacje w Hurghadzie.",
    },
    "ro": {
        "sea_islands": "Insule paradisiace, lagune turcoaz și snorkeling pe recifele Mării Roșii.",
        "desert_safari": "Adrenalină în deșert: ATV, jeep, sat beduin și seară orientală.",
        "history_culture": "Marile comori ale Egiptului antic, cu plecare din Hurghada.",
        "activities": "Experiențe unice care îți condimentează vacanța la Hurghada.",
    },
}

T = {
    # =====================================================================
    "fr": {
        "meta_home_title": "KeRo Tours Hurghada - Excursions VIP & transferts | Réservation WhatsApp",
        "meta_home_desc": "Excursions VIP à Hurghada : Pyramides de Gizeh, Louxor, îles de la mer Rouge, safari quad, Dolphin House. Sans acompte, paiement au départ. Réservation sur WhatsApp.",
        "meta_title_suffix": " | KeRo Tours Hurghada",

        "skip_to_content": "Aller au contenu",
        "nav_home": "Accueil",
        "nav_excursions": "Excursions",
        "nav_process": "Réservation",
        "nav_why": "Pourquoi nous",
        "nav_faq": "FAQ",
        "nav_contact": "Contact",
        "nav_book": "Réserver",
        "select_language": "Choisir la langue",
        "open_menu": "Ouvrir le menu",
        "close_menu": "Fermer le menu",

        "hero_kicker": "Hurghada - Mer Rouge",
        "hero_h1": "Excursions VIP à Hurghada, sans acompte",
        "hero_sub": "Pyramides, Louxor, îles de la mer Rouge, safari dans le désert et bien plus. Vous choisissez, vous réservez sur WhatsApp, vous payez au début de l'excursion.",
        "hero_cta_primary": "Réserver sur WhatsApp",
        "hero_cta_secondary": "Voir les excursions",

        "payment_line": "Excursions VIP • Aucun acompte • Paiement au départ de l'excursion",
        "trust": ["Excursions VIP", "Aucun acompte", "Paiement au départ", "Réservation WhatsApp"],

        "featured_title": "Nos excursions phares",
        "featured_sub": "Une sélection de nos sorties les plus demandées.",
        "all_title": "Toutes les excursions",
        "all_sub": "Filtrez par catégorie pour trouver votre prochaine aventure.",
        "filter_all": "Toutes",

        "process_title": "Comment réserver",
        "process_sub": "Simple, direct, sans paiement à l'avance.",
        "process_steps": [
            ["Choisissez votre excursion", "Parcourez nos excursions VIP et retenez celle qui vous fait envie."],
            ["Écrivez-nous sur WhatsApp", "Envoyez votre demande : nombre de personnes, hôtel et date souhaitée."],
            ["Recevez la confirmation", "Nous confirmons la disponibilité et les détails de prise en charge."],
            ["Payez au début de l'excursion", "Aucun acompte, aucun paiement à l'avance : vous réglez au départ."],
        ],

        "why_title": "Pourquoi choisir KeRo Tours",
        "why_items": [
            ["Sans acompte", "Vous payez au début de l'excursion. Aucun paiement à l'avance n'est demandé."],
            ["Réservation par WhatsApp", "Un échange simple et direct pour confirmer votre place, dans votre langue."],
            ["Transferts hôtel", "Transfert depuis et vers l'hôtel inclus lorsque la fiche de l'excursion le précise."],
            ["Basés à Hurghada", "Une équipe locale qui connaît la région et ses plus belles sorties."],
        ],

        "faq_title": "Questions fréquentes",
        "faq": [
            ["Faut-il payer à l'avance ?", "Non. Aucun acompte n'est demandé. Vous payez au début de l'excursion, au moment du départ ou de la prise en charge."],
            ["Comment réserver une excursion ?", "Choisissez votre excursion et envoyez-nous votre demande sur WhatsApp. Nous confirmons ensuite la disponibilité et les détails de prise en charge."],
            ["Le transfert depuis l'hôtel est-il inclus ?", "Oui lorsque la fiche de l'excursion l'indique. Les détails de prise en charge sont confirmés via WhatsApp."],
            ["Les horaires de prise en charge sont-ils garantis ?", "Les horaires indiqués sont approximatifs. L'heure exacte de prise en charge est confirmée via WhatsApp."],
            ["« VIP » veut-il dire privé ?", "VIP désigne une expérience soignée. Le transport privé n'est garanti que lorsque la fiche le précise (transfert privé ou bateau privé). Certaines excursions, comme Le Caire ou Louxor, se font en minibus de groupe."],
            ["En quelle langue puis-je écrire ?", "Vous pouvez nous écrire en français, en polonais ou en roumain."],
        ],

        "contact_title": "Contact & réservation",
        "contact_sub": "Écrivez-nous sur WhatsApp : nous confirmons votre excursion et les détails de prise en charge.",
        "contact_whatsapp": "Nous écrire sur WhatsApp",

        "price_per_person": "/ personne",
        "price_per_boat": "/ bateau privé",
        "price_total": "au total",
        "price_from": "À partir de",
        "group_base_label": "Forfait de base",
        "persons": "pers.",

        "label_experience": "Points forts",
        "label_program": "Programme de l'excursion",
        "label_practical": "Infos pratiques",
        "label_included": "Ce qui est inclus",
        "label_conditions": "À savoir",
        "nav_excursions_all": "Toutes les excursions",
        "gallery_prev": "Image précédente",
        "gallery_next": "Image suivante",
        "gallery_close": "Fermer",
        "gallery_open": "Agrandir la photo",
        "label_addons": "Options",
        "label_addon_price": "en supplément",
        "label_related": "Autres excursions",
        "label_schedule": "Horaire approximatif",
        "view_details": "Voir les détails",
        "card_details": "Détails",
        "card_book": "Réserver",
        "book_whatsapp": "Réserver sur WhatsApp",
        "back_to_all": "Toutes les excursions",
        "restricted_note": "Expérience en cours de revue réglementaire et de bien-être animal avant toute promotion.",

        "floating_wa_label": "Réserver sur WhatsApp",

        "footer_about": "Excursions VIP et transferts privés à Hurghada, sur la mer Rouge.",
        "footer_excursions_title": "Excursions",
        "footer_contact_title": "Contact",
        "social_follow": "Suivez-nous",
        "social_aria": "{brand} sur {network} (nouvel onglet)",
        "footer_disclaimer": "La disponibilité et les modalités exactes de prise en charge sont confirmées via WhatsApp.",
        "footer_rights": "Tous droits réservés.",
        "footer_lang_title": "Langues",

        "wa_message_tour": "Bonjour ! Je souhaite réserver l'excursion {tour}. Nous sommes [NOMBRE] personnes. Notre hôtel : [HÔTEL]. Date souhaitée : [DATE]. Pouvez-vous confirmer la disponibilité ?",
        "wa_message_generic": "Bonjour ! Je souhaite des informations sur vos excursions VIP à Hurghada. Pouvez-vous m'aider ?",

        "notfound_title": "Page introuvable",
        "notfound_text": "La page demandée n'existe pas. Retournez à l'accueil.",
        "notfound_home": "Retour à l'accueil",
    },

    # =====================================================================
    "pl": {
        "meta_home_title": "KeRo Tours Hurghada - Wycieczki VIP i transfery | Rezerwacja WhatsApp",
        "meta_home_desc": "Wycieczki VIP z Hurghady: piramidy w Gizie, Luksor, wyspy Morza Czerwonego, safari quadem, Dolphin House. Bez przedpłaty, płatność przy starcie. Rezerwacja przez WhatsApp.",
        "meta_title_suffix": " | KeRo Tours Hurghada",

        "skip_to_content": "Przejdź do treści",
        "nav_home": "Start",
        "nav_excursions": "Wycieczki",
        "nav_process": "Rezerwacja",
        "nav_why": "Dlaczego my",
        "nav_faq": "FAQ",
        "nav_contact": "Kontakt",
        "nav_book": "Rezerwuj",
        "select_language": "Wybierz język",
        "open_menu": "Otwórz menu",
        "close_menu": "Zamknij menu",

        "hero_kicker": "Hurghada - Morze Czerwone",
        "hero_h1": "Wycieczki VIP w Hurghadzie, bez przedpłaty",
        "hero_sub": "Piramidy, Luksor, wyspy Morza Czerwonego, safari na pustyni i wiele więcej. Wybierasz, rezerwujesz przez WhatsApp i płacisz na początku wycieczki.",
        "hero_cta_primary": "Rezerwuj przez WhatsApp",
        "hero_cta_secondary": "Zobacz wycieczki",

        "payment_line": "Wycieczki VIP • Bez przedpłaty • Płatność przy rozpoczęciu wycieczki",
        "trust": ["Wycieczki VIP", "Bez przedpłaty", "Płatność przy starcie", "Rezerwacja WhatsApp"],

        "featured_title": "Nasze najpopularniejsze wycieczki",
        "featured_sub": "Wybór naszych najczęściej wybieranych wypraw.",
        "all_title": "Wszystkie wycieczki",
        "all_sub": "Filtruj według kategorii i znajdź swoją kolejną przygodę.",
        "filter_all": "Wszystkie",

        "process_title": "Jak zarezerwować",
        "process_sub": "Prosto, bezpośrednio, bez przedpłaty.",
        "process_steps": [
            ["Wybierz wycieczkę", "Przejrzyj nasze wycieczki VIP i wybierz tę, która Cię kusi."],
            ["Napisz do nas na WhatsApp", "Wyślij zgłoszenie: liczba osób, hotel i preferowana data."],
            ["Otrzymaj potwierdzenie", "Potwierdzamy dostępność oraz szczegóły odbioru."],
            ["Zapłać na początku wycieczki", "Bez przedpłaty i bez płatności z góry - płacisz na starcie."],
        ],

        "why_title": "Dlaczego KeRo Tours",
        "why_items": [
            ["Bez przedpłaty", "Płacisz na początku wycieczki. Nie pobieramy żadnej zaliczki z góry."],
            ["Rezerwacja przez WhatsApp", "Prosta, bezpośrednia rozmowa, aby potwierdzić miejsce - w Twoim języku."],
            ["Transfery z hotelu", "Transfer z hotelu i z powrotem w cenie, gdy opis wycieczki tak wskazuje."],
            ["Baza w Hurghadzie", "Lokalny zespół, który zna region i jego najlepsze wyprawy."],
        ],

        "faq_title": "Najczęstsze pytania",
        "faq": [
            ["Czy trzeba płacić z góry?", "Nie. Nie pobieramy zaliczki. Płacisz na początku wycieczki, w chwili wyjazdu lub odbioru."],
            ["Jak zarezerwować wycieczkę?", "Wybierz wycieczkę i wyślij zgłoszenie przez WhatsApp. Następnie potwierdzamy dostępność i szczegóły odbioru."],
            ["Czy transfer z hotelu jest w cenie?", "Tak, gdy opis wycieczki to wskazuje. Szczegóły odbioru potwierdzamy przez WhatsApp."],
            ["Czy godziny odbioru są gwarantowane?", "Podane godziny są orientacyjne. Dokładną godzinę odbioru potwierdzamy przez WhatsApp."],
            ["Czy „VIP” oznacza prywatną wycieczkę?", "VIP oznacza dopracowane doświadczenie. Transport prywatny jest gwarantowany tylko wtedy, gdy opis tak wskazuje (prywatny transfer lub prywatna łódź). Niektóre wycieczki, jak Kair czy Luksor, odbywają się minibusem grupowym."],
            ["W jakim języku mogę pisać?", "Możesz pisać do nas po francusku, polsku lub rumuńsku."],
        ],

        "contact_title": "Kontakt i rezerwacja",
        "contact_sub": "Napisz do nas na WhatsApp: potwierdzimy wycieczkę i szczegóły odbioru.",
        "contact_whatsapp": "Napisz do nas na WhatsApp",

        "price_per_person": "/ osoba",
        "price_per_boat": "/ łódź prywatna",
        "price_total": "za całość",
        "price_from": "Od",
        "group_base_label": "Pakiet podstawowy",
        "persons": "os.",

        "label_experience": "Najważniejsze",
        "label_program": "Program wycieczki",
        "label_practical": "Informacje praktyczne",
        "label_included": "Co obejmuje",
        "label_conditions": "Dobrze wiedzieć",
        "nav_excursions_all": "Wszystkie wycieczki",
        "gallery_prev": "Poprzednie zdjęcie",
        "gallery_next": "Następne zdjęcie",
        "gallery_close": "Zamknij",
        "gallery_open": "Powiększ zdjęcie",
        "label_addons": "Opcje dodatkowe",
        "label_addon_price": "dopłata",
        "label_related": "Inne wycieczki",
        "label_schedule": "Przybliżone godziny",
        "view_details": "Zobacz szczegóły",
        "card_details": "Szczegóły",
        "card_book": "WhatsApp",
        "book_whatsapp": "Rezerwuj przez WhatsApp",
        "back_to_all": "Wszystkie wycieczki",
        "restricted_note": "Oferta w trakcie przeglądu prawnego i pod kątem dobrostanu zwierząt przed promocją.",

        "floating_wa_label": "Rezerwuj przez WhatsApp",

        "footer_about": "Wycieczki VIP i prywatne transfery w Hurghadzie, nad Morzem Czerwonym.",
        "footer_excursions_title": "Wycieczki",
        "footer_contact_title": "Kontakt",
        "social_follow": "Obserwuj nas",
        "social_aria": "{brand} na {network} (nowa karta)",
        "footer_disclaimer": "Dostępność i dokładne szczegóły odbioru potwierdzamy przez WhatsApp.",
        "footer_rights": "Wszelkie prawa zastrzeżone.",
        "footer_lang_title": "Języki",

        "wa_message_tour": "Dzień dobry! Chciał(a)bym zarezerwować wycieczkę {tour}. Jest nas [LICZBA] osób. Nasz hotel: [HOTEL]. Preferowana data: [DATA]. Czy możecie potwierdzić dostępność?",
        "wa_message_generic": "Dzień dobry! Chciał(a)bym uzyskać informacje o Waszych wycieczkach VIP w Hurghadzie. Czy możecie pomóc?",

        "notfound_title": "Nie znaleziono strony",
        "notfound_text": "Żądana strona nie istnieje. Wróć na stronę główną.",
        "notfound_home": "Powrót na stronę główną",
    },

    # =====================================================================
    "ro": {
        "meta_home_title": "KeRo Tours Hurghada - Excursii VIP și transferuri | Rezervare WhatsApp",
        "meta_home_desc": "Excursii VIP din Hurghada: Piramidele din Giza, Luxor, insulele Mării Roșii, safari cu ATV, Dolphin House. Fără avans, plată la început. Rezervare prin WhatsApp.",
        "meta_title_suffix": " | KeRo Tours Hurghada",

        "skip_to_content": "Sari la conținut",
        "nav_home": "Acasă",
        "nav_excursions": "Excursii",
        "nav_process": "Rezervare",
        "nav_why": "De ce noi",
        "nav_faq": "Întrebări",
        "nav_contact": "Contact",
        "nav_book": "Rezervă",
        "select_language": "Alege limba",
        "open_menu": "Deschide meniul",
        "close_menu": "Închide meniul",

        "hero_kicker": "Hurghada - Marea Roșie",
        "hero_h1": "Excursii VIP în Hurghada, fără avans",
        "hero_sub": "Piramide, Luxor, insulele Mării Roșii, safari în deșert și multe altele. Alegi, rezervi pe WhatsApp și plătești la începutul excursiei.",
        "hero_cta_primary": "Rezervă pe WhatsApp",
        "hero_cta_secondary": "Vezi excursiile",

        "payment_line": "Excursii VIP • Fără avans • Plată la începutul excursiei",
        "trust": ["Excursii VIP", "Fără avans", "Plată la început", "Rezervare WhatsApp"],

        "featured_title": "Excursiile noastre de top",
        "featured_sub": "O selecție a celor mai căutate ieșiri ale noastre.",
        "all_title": "Toate excursiile",
        "all_sub": "Filtrează după categorie și găsește-ți următoarea aventură.",
        "filter_all": "Toate",

        "process_title": "Cum rezervi",
        "process_sub": "Simplu, direct, fără plată în avans.",
        "process_steps": [
            ["Alege excursia", "Răsfoiește excursiile noastre VIP și oprește-te la cea care îți place."],
            ["Scrie-ne pe WhatsApp", "Trimite cererea: număr de persoane, hotel și data dorită."],
            ["Primești confirmarea", "Confirmăm disponibilitatea și detaliile de preluare."],
            ["Plătești la începutul excursiei", "Fără avans și fără plată în avans - achiți la plecare."],
        ],

        "why_title": "De ce KeRo Tours",
        "why_items": [
            ["Fără avans", "Plătești la începutul excursiei. Nu se cere nicio plată în avans."],
            ["Rezervare pe WhatsApp", "O discuție simplă și directă pentru a-ți confirma locul, în limba ta."],
            ["Transferuri de la hotel", "Transfer de la hotel și retur incluse atunci când fișa excursiei o precizează."],
            ["Bază în Hurghada", "O echipă locală care cunoaște regiunea și cele mai frumoase ieșiri."],
        ],

        "faq_title": "Întrebări frecvente",
        "faq": [
            ["Trebuie să plătesc în avans?", "Nu. Nu se cere niciun avans. Plătești la începutul excursiei, în momentul plecării sau al preluării."],
            ["Cum rezerv o excursie?", "Alege excursia și trimite-ne cererea pe WhatsApp. Confirmăm apoi disponibilitatea și detaliile de preluare."],
            ["Transferul de la hotel este inclus?", "Da, atunci când fișa excursiei o indică. Detaliile de preluare se confirmă prin WhatsApp."],
            ["Orele de preluare sunt garantate?", "Orarele indicate sunt aproximative. Ora exactă de preluare se confirmă prin WhatsApp."],
            ["„VIP” înseamnă privat?", "VIP înseamnă o experiență îngrijită. Transportul privat este garantat doar atunci când fișa o precizează (transfer privat sau barcă privată). Unele excursii, precum Cairo sau Luxor, se desfășoară cu minibuz în grup."],
            ["În ce limbă pot să scriu?", "Ne poți scrie în franceză, poloneză sau română."],
        ],

        "contact_title": "Contact și rezervare",
        "contact_sub": "Scrie-ne pe WhatsApp: îți confirmăm excursia și detaliile de preluare.",
        "contact_whatsapp": "Scrie-ne pe WhatsApp",

        "price_per_person": "/ persoană",
        "price_per_boat": "/ barcă privată",
        "price_total": "în total",
        "price_from": "De la",
        "group_base_label": "Pachet de bază",
        "persons": "pers.",

        "label_experience": "Puncte forte",
        "label_program": "Programul excursiei",
        "label_practical": "Informații practice",
        "label_included": "Ce include",
        "label_conditions": "De știut",
        "nav_excursions_all": "Toate excursiile",
        "gallery_prev": "Imaginea anterioară",
        "gallery_next": "Imaginea următoare",
        "gallery_close": "Închide",
        "gallery_open": "Mărește fotografia",
        "label_addons": "Opțiuni suplimentare",
        "label_addon_price": "supliment",
        "label_related": "Alte excursii",
        "label_schedule": "Orar aproximativ",
        "view_details": "Vezi detaliile",
        "card_details": "Detalii",
        "card_book": "Rezervă",
        "book_whatsapp": "Rezervă pe WhatsApp",
        "back_to_all": "Toate excursiile",
        "restricted_note": "Experiență aflată în curs de verificare legală și de bunăstare a animalelor înainte de promovare.",

        "floating_wa_label": "Rezervă pe WhatsApp",

        "footer_about": "Excursii VIP și transferuri private în Hurghada, la Marea Roșie.",
        "footer_excursions_title": "Excursii",
        "footer_contact_title": "Contact",
        "social_follow": "Urmărește-ne",
        "social_aria": "{brand} pe {network} (filă nouă)",
        "footer_disclaimer": "Disponibilitatea și detaliile exacte de preluare se confirmă prin WhatsApp.",
        "footer_rights": "Toate drepturile rezervate.",
        "footer_lang_title": "Limbi",

        "wa_message_tour": "Bună ziua! Aș dori să rezerv excursia {tour}. Suntem [NUMĂR] persoane. Hotelul nostru: [HOTEL]. Data dorită: [DATA]. Puteți confirma disponibilitatea?",
        "wa_message_generic": "Bună ziua! Aș dori informații despre excursiile VIP din Hurghada. Mă puteți ajuta?",

        "notfound_title": "Pagină inexistentă",
        "notfound_text": "Pagina solicitată nu există. Revino la pagina principală.",
        "notfound_home": "Înapoi la pagina principală",
    },
}
