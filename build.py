#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for Hurghada KeRo Tours & Transfer.

Zero runtime dependencies (Python 3 standard library only).
Run:  python3 build.py   ->  outputs the full static site into ./dist

What it produces:
  dist/index.html                      language splash (/) with x-default hreflang
  dist/{fr,pl,ro}/index.html           localized homepages
  dist/{fr}/excursions/{slug}/         localized tour detail pages
  dist/{pl}/wycieczki/{slug}/
  dist/{ro}/excursii/{slug}/
  dist/assets/...                       css / js / images (copied)
  dist/sitemap.xml, robots.txt, 404.html
"""

import html
import json
import os
import shutil
from datetime import date
from urllib.parse import quote

import site_config as cfg
from data.i18n import (T, LANG_ORDER, LANG_NATIVE, PATH_TOURS, HTML_LANG,
                       OG_LOCALE, CATEGORIES, CATEGORY_ORDER)
from data.tours import TOURS

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
SRC_ASSETS = os.path.join(ROOT, "assets")
YEAR = date.today().year
IMG_EXTS = (".avif", ".webp", ".jpg", ".jpeg", ".png")

# ---------------------------------------------------------------------------
# escaping helpers
# ---------------------------------------------------------------------------
def esc(s):   # visible text
    return html.escape(str(s), quote=False)

def esca(s):  # attribute value
    return html.escape(str(s), quote=True)

# ---------------------------------------------------------------------------
# icons (professional line/solid SVG - no emoji)
# ---------------------------------------------------------------------------
def _line(path, extra=""):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" '
            'aria-hidden="true" %s>%s</svg>' % (extra, path))

ICON = {
    "wa": ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
           '<path d="M19.05 4.91A9.82 9.82 0 0 0 12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 '
           '3.45 1.32 4.95L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.004c5.46 0 9.91-4.45 '
           '9.91-9.91 0-2.65-1.03-5.14-2.9-7.02zM12.04 20.15a8.23 8.23 0 0 1-4.19-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 '
           '8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 '
           '2.41 5.82c0 4.54-3.69 8.23-8.23 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.5.11-.11.25-.29.37-.43.13-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.4-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.86.85-.86 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.47-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.11-.22-.17-.47-.29z"/></svg>'),
    "check": _line('<path d="M20 6 9 17l-5-5"/>'),
    "check_circle": _line('<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4 12 14.01l-3-3"/>'),
    "shield": _line('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>'),
    "wallet": _line('<path d="M3 7a2 2 0 0 1 2-2h13v4"/><path d="M3 7v10a2 2 0 0 0 2 2h14a1 1 0 0 0 1-1v-3"/><path d="M16 12h5v4h-5a2 2 0 0 1 0-4z"/>'),
    "chat": _line('<path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.38 8.38 0 0 1 4 11.5 8.5 8.5 0 0 1 12.5 3 8.38 8.38 0 0 1 21 11.5z"/>'),
    "star": ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
             '<path d="m12 2 3.09 6.26L22 9.27l-5 4.87L18.18 22 12 18.56 5.82 22 7 14.14l-5-4.87 6.91-1.01L12 2z"/></svg>'),
    "clock": _line('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "info": _line('<circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><path d="M12 8h.01"/>'),
    "car": _line('<path d="M5 17h14"/><path d="M5 17 3.6 12A2 2 0 0 1 5.5 9.3h13A2 2 0 0 1 20.4 12L19 17"/><path d="M6.5 9.3 8 5.5h8l1.5 3.8"/><circle cx="7.5" cy="17.5" r="1.6"/><circle cx="16.5" cy="17.5" r="1.6"/>'),
    "pin": _line('<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>'),
    "camera": _line('<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>'),
    "phone": _line('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.7a2 2 0 0 1-.5 2.1L8 9.6a16 16 0 0 0 6 6l1.1-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.5 2.7.6a2 2 0 0 1 1.7 2z"/>'),
    "mail": _line('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
    "arrow": _line('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'),
    "arrow_left": _line('<path d="M19 12H5"/><path d="m12 19-7-7 7-7"/>'),
}

# ---------------------------------------------------------------------------
# placeholder art (branded gradient slots - NOT fake photos)
# ---------------------------------------------------------------------------
_PH_COLORS = {
    "sea_islands":      ("#13c2d1", "#07697a"),
    "desert_adventure": ("#efc879", "#bb7d1e"),
    "history":          ("#e0bd8e", "#8f5a2a"),
    "other":            ("#19bcc9", "#0d5a67"),
}
_ph_counter = [0]

def placeholder_svg(category, cls="ph"):
    c1, c2 = _PH_COLORS.get(category, _PH_COLORS["other"])
    _ph_counter[0] += 1
    gid = "g%d" % _ph_counter[0]
    # category motif
    if category == "sea_islands":
        motif = ('<path d="M0 360 Q200 320 400 360 T800 360 V500 H0 Z" fill="#ffffff" opacity=".10"/>'
                 '<path d="M0 410 Q200 375 400 410 T800 410 V500 H0 Z" fill="#ffffff" opacity=".14"/>'
                 '<circle cx="650" cy="120" r="54" fill="#ffffff" opacity=".22"/>')
    elif category == "desert_adventure":
        motif = ('<circle cx="640" cy="130" r="56" fill="#ffffff" opacity=".28"/>'
                 '<path d="M0 380 Q250 300 480 370 T800 350 V500 H0 Z" fill="#ffffff" opacity=".12"/>'
                 '<path d="M0 430 Q300 370 560 420 T800 410 V500 H0 Z" fill="#000000" opacity=".06"/>')
    elif category == "history":
        motif = ('<circle cx="650" cy="120" r="48" fill="#ffffff" opacity=".22"/>'
                 '<path d="M140 400 L250 220 L360 400 Z" fill="#ffffff" opacity=".16"/>'
                 '<path d="M330 400 L470 180 L610 400 Z" fill="#ffffff" opacity=".20"/>')
    else:
        motif = ('<circle cx="640" cy="130" r="52" fill="#ffffff" opacity=".20"/>'
                 '<path d="M190 250 l18 46 46 18 -46 18 -18 46 -18-46 -46-18 46-18z" fill="#ffffff" opacity=".28"/>')
    return ('<svg class="%s" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" '
            'role="img" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">'
            '<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
            '</linearGradient></defs>'
            '<rect width="800" height="500" fill="url(#%s)"/>%s</svg>'
            % (cls, gid, c1, c2, gid, motif))

def tour_image_file(tour_id):
    """Return (filename, exists) for a real tour photo in assets/img/tours/."""
    base = os.path.join(SRC_ASSETS, "img", "tours")
    for ext in IMG_EXTS:
        fn = tour_id + ext
        if os.path.isfile(os.path.join(base, fn)):
            return fn
    return None

def media(tour, lang, kind="card"):
    """Real <img> if a photo exists, else branded placeholder + slot badge."""
    alt = esca(tour["content"][lang]["name"])
    fn = tour_image_file(tour["id"])
    if fn:
        loading = "" if kind == "hero" else ' loading="lazy" decoding="async"'
        return '<img src="/assets/img/tours/%s" alt="%s"%s>' % (esca(fn), alt, loading)
    svg = placeholder_svg(tour["category"])
    badge = '<span class="ph__badge">%s</span>' % ICON["camera"]
    return svg + badge

# ---------------------------------------------------------------------------
# url helpers
# ---------------------------------------------------------------------------
def url_home(lang):
    return "/%s/" % lang

def url_tour(lang, slug):
    return "/%s/%s/%s/" % (lang, PATH_TOURS[lang], slug)

def abs_url(path):
    return cfg.SITE_URL.rstrip("/") + path

# ---------------------------------------------------------------------------
# WhatsApp link builder
# ---------------------------------------------------------------------------
def wa_text(lang, tour=None):
    if tour is None:
        return T[lang]["wa_message_generic"]
    return T[lang]["wa_message_tour"].format(tour=tour["content"][lang]["name"])

def wa_link(lang, label, classes, pos, tour=None, with_icon=True):
    tid = tour["id"] if tour else "none"
    text = wa_text(lang, tour)
    cls = classes
    if cfg.WHATSAPP_NUMBER:
        href = "https://wa.me/%s?text=%s" % (cfg.WHATSAPP_NUMBER, quote(text, safe=""))
        hattr = ('href="%s" data-wa-href="%s" target="_blank" rel="noopener"'
                 % (esca(href), esca(href)))
    else:
        cls += " is-pending"
        hattr = 'href="#" aria-disabled="true"'
    icon = ICON["wa"] if with_icon else ""
    return ('<a class="%s" %s data-wa data-wa-text="%s" data-tour="%s" data-pos="%s">'
            '%s<span>%s</span></a>'
            % (cls, hattr, esca(text), tid, pos, icon, esc(label)))

def wa_float(lang):
    text = wa_text(lang, None)
    cls = "wa-float"
    if cfg.WHATSAPP_NUMBER:
        href = "https://wa.me/%s?text=%s" % (cfg.WHATSAPP_NUMBER, quote(text, safe=""))
        hattr = 'href="%s" data-wa-href="%s" target="_blank" rel="noopener"' % (esca(href), esca(href))
    else:
        cls += " is-pending"
        hattr = 'href="#" aria-disabled="true"'
    return ('<a class="%s" %s data-wa data-wa-text="%s" data-tour="none" data-pos="float" '
            'aria-label="%s">%s<span class="wa-float__text">%s</span></a>'
            % (cls, hattr, esca(text), esca(T[lang]["floating_wa_label"]),
               ICON["wa"], esc(T[lang]["nav_book"])))

# ---------------------------------------------------------------------------
# price formatting
# ---------------------------------------------------------------------------
def price_unit(lang, tour):
    if tour["price_type"] == "per_boat":
        return T[lang]["price_per_boat"]
    return T[lang]["price_per_person"]

def card_price(lang, tour):
    unit = price_unit(lang, tour)
    return '<div class="card__price"><b>&euro;%d</b> <span>%s</span></div>' % (tour["price"], esc(unit))

# ---------------------------------------------------------------------------
# shared chrome: <head>, header, footer, scripts
# ---------------------------------------------------------------------------
BRAND_MARK = ('<svg class="brand__mark" viewBox="0 0 40 40" fill="none" aria-hidden="true">'
              '<rect width="40" height="40" rx="11" fill="#0bb4c4"/>'
              '<path d="M8 27 Q14 22 20 27 T32 27" stroke="#fff" stroke-width="2.4" '
              'stroke-linecap="round" fill="none"/>'
              '<path d="M8 21 Q14 16 20 21 T32 21" stroke="#bdf3f6" stroke-width="2.2" '
              'stroke-linecap="round" fill="none" opacity=".85"/>'
              '<circle cx="28.5" cy="12.5" r="3.4" fill="#f2c14e"/></svg>')

def brand_html():
    return ('<a class="brand" href="/%s/" aria-label="%s">%s'
            '<span class="brand__name"><b>KeRo</b> Tours<small>Hurghada</small></span></a>')

def analytics_head():
    ga, ads = cfg.GA4_MEASUREMENT_ID.strip(), cfg.GOOGLE_ADS_ID.strip()
    if not ga and not ads:
        return ""
    primary = ga or ads
    lines = ["window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}",
             "gtag('js',new Date());"]
    if ga:
        lines.append("gtag('config','%s');" % ga)
    if ads:
        lines.append("gtag('config','%s');" % ads)
        if cfg.GOOGLE_ADS_CONVERSION_LABEL.strip():
            lines.append("window.KERO_ADS_CONVERSION='%s/%s';"
                         % (ads, cfg.GOOGLE_ADS_CONVERSION_LABEL.strip()))
    return ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>\n'
            '<script>%s</script>\n' % (primary, "".join(lines)))

def head(lang, title, desc, canonical_path, alt_paths, xdefault_path, jsonld=None):
    alts = []
    for l in LANG_ORDER:
        if l in alt_paths:
            alts.append('<link rel="alternate" hreflang="%s" href="%s">'
                        % (HTML_LANG[l], abs_url(alt_paths[l])))
    alts.append('<link rel="alternate" hreflang="x-default" href="%s">' % abs_url(xdefault_path))
    jsonld_tag = ""
    if jsonld:
        jsonld_tag = '<script type="application/ld+json">%s</script>' % json.dumps(
            jsonld, ensure_ascii=False, separators=(",", ":"))
    og_img = abs_url("/assets/img/og-default.svg")
    return """<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
%s
<meta property="og:type" content="website">
<meta property="og:locale" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s">
<meta property="og:site_name" content="%s">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0bb4c4">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
%s<script src="/assets/js/config.js"></script>
%s</head>
<body>
<a class="skip-link" href="#main">%s</a>
""" % (HTML_LANG[lang], esca(title), esca(desc), abs_url(canonical_path),
       "\n".join(alts), OG_LOCALE[lang], esca(title), esca(desc),
       abs_url(canonical_path), og_img, esca(cfg.BRAND_NAME), jsonld_tag,
       analytics_head(), esc(T[lang]["skip_to_content"]))

def header(lang, alt_paths):
    tr = T[lang]
    home = url_home(lang)
    navlinks = [
        (tr["nav_excursions"], home + "#excursions"),
        (tr["nav_process"], home + "#process"),
        (tr["nav_why"], home + "#why"),
        (tr["nav_faq"], home + "#faq"),
        (tr["nav_contact"], home + "#contact"),
    ]
    desk = "".join('<a href="%s">%s</a>' % (esca(h), esc(t)) for t, h in navlinks)
    mob = "".join('<a href="%s">%s</a>' % (esca(h), esc(t)) for t, h in navlinks)

    langpills = []
    for l in LANG_ORDER:
        target = alt_paths.get(l, url_home(l))
        cur = ' aria-current="true"' if l == lang else ""
        langpills.append('<a href="%s"%s hreflang="%s">%s</a>'
                         % (esca(target), cur, HTML_LANG[l], l.upper()))
    langswitch = ('<div class="langswitch" role="group" aria-label="%s">%s</div>'
                  % (esca(tr["select_language"]), "".join(langpills)))

    book_btn = wa_link(lang, tr["nav_book"], "btn btn--wa nav__book", "nav")
    mob_book = wa_link(lang, tr["nav_book"], "btn btn--wa btn--block", "nav-mobile")

    return """<header class="header">
<div class="container">
<nav class="nav" data-nav data-open="false">
%s
<div class="nav__links">%s</div>
<div class="nav__right">%s%s
<button class="nav__toggle" data-nav-toggle aria-label="%s" aria-expanded="false" aria-controls="mobilemenu"><span></span><span></span><span></span></button>
</div>
</nav>
</div>
<div class="mobile-menu" id="mobilemenu"><ul><li>%s</li></ul></div>
</header>""" % (
        brand_html() % (lang, esca(cfg.BRAND_NAME), BRAND_MARK),
        desk, langswitch, book_btn, esca(tr["open_menu"]),
        "</li><li>".join([mob, mob_book]))

def footer(lang, public_tours):
    tr = T[lang]
    exc_links = "".join('<a href="%s">%s</a>' % (esca(url_tour(lang, t["slug"])),
                                                 esc(t["content"][lang]["name"]))
                        for t in public_tours)
    # contact column: only show fields the owner has actually provided
    contact_rows = [wa_link(lang, tr["contact_whatsapp"], "footer__wa", "footer")]
    if cfg.BUSINESS["phone_display"]:
        contact_rows.append('<a href="tel:%s">%s %s</a>'
                            % (esca(cfg.BUSINESS["phone_display"].replace(" ", "")),
                               ICON["phone"], esc(cfg.BUSINESS["phone_display"])))
    if cfg.BUSINESS["email"]:
        contact_rows.append('<a href="mailto:%s">%s %s</a>'
                            % (esca(cfg.BUSINESS["email"]), ICON["mail"],
                               esc(cfg.BUSINESS["email"])))
    if cfg.BUSINESS["address"]:
        contact_rows.append('<div>%s %s</div>' % (ICON["pin"], esc(cfg.BUSINESS["address"])))

    langs = " ".join('<a href="%s" hreflang="%s">%s</a>'
                     % (esca(url_home(l)), HTML_LANG[l], esc(LANG_NATIVE[l]))
                     for l in LANG_ORDER)

    legal = ""
    if cfg.BUSINESS["legal_name"] or cfg.BUSINESS["license_number"]:
        bits = []
        if cfg.BUSINESS["legal_name"]:
            bits.append(esc(cfg.BUSINESS["legal_name"]))
        if cfg.BUSINESS["license_number"]:
            bits.append(esc(cfg.BUSINESS["license_number"]))
        legal = '<div class="footer__legal">%s</div>' % " &middot; ".join(bits)

    return """<footer class="footer">
<div class="container">
<div class="footer__grid">
<div class="footer__brand">
<span class="brand">%s<span class="brand__name"><b>KeRo</b> Tours<small>Hurghada</small></span></span>
<p>%s</p>
</div>
<div><h4>%s</h4><div class="footer__links">%s</div></div>
<div><h4>%s</h4><div class="footer__links">%s</div></div>
</div>
<div class="footer__disclaimer">%s<p>%s</p></div>
<div class="footer__bottom">
<div>&copy; %d %s. %s%s</div>
<div class="footer__langs"><span>%s:</span> %s</div>
</div>
</div>
</footer>""" % (
        BRAND_MARK, esc(tr["footer_about"]),
        esc(tr["footer_excursions_title"]), exc_links,
        esc(tr["footer_contact_title"]), "".join(contact_rows),
        ICON["info"], esc(tr["footer_disclaimer"]),
        YEAR, esc(cfg.BRAND_NAME), esc(tr["footer_rights"]), legal,
        esc(tr["footer_lang_title"]), langs)

def scripts():
    return '<script src="/assets/js/app.js" defer></script>\n</body>\n</html>\n'

# ---------------------------------------------------------------------------
# components
# ---------------------------------------------------------------------------
def tour_card(lang, tour, delay=0):
    tr = T[lang]
    cat = CATEGORIES[lang][tour["category"]]
    flag = ('<span class="card__flag">%s</span>' % esc(tr["label_conditions"])) if tour["restricted"] else ""
    detail = url_tour(lang, tour["slug"])
    return """<article class="card reveal" data-tour-card data-category="%s" data-delay="%d">
<a class="card__media" href="%s" aria-label="%s">%s<span class="card__cat">%s</span>%s%s</a>
<div class="card__body">
<h3 class="card__title">%s</h3>
<p class="card__tag">%s</p>
<div class="card__actions">
<a class="btn btn--outline" href="%s">%s</a>
%s
</div>
</div>
</article>""" % (
        tour["category"], delay % 3, esca(detail), esca(tour["content"][lang]["name"]),
        media(tour, lang), esc(cat), flag, card_price(lang, tour),
        esc(tour["content"][lang]["name"]), esc(tour["content"][lang]["tagline"]),
        esca(detail), esc(tr["view_details"]),
        wa_link(lang, tr["book_whatsapp"], "btn btn--wa", "card", tour))

def trust_strip(lang):
    tr = T[lang]
    icons = [ICON["star"], ICON["shield"], ICON["wallet"], ICON["chat"]]
    items = "".join('<div class="trust__item">%s<span>%s</span></div>' % (icons[i], esc(tr["trust"][i]))
                    for i in range(4))
    return '<section class="trust" aria-label="%s"><div class="container"><div class="trust__row">%s</div></div></section>' % (
        esca(tr["payment_line"]), items)

# ---------------------------------------------------------------------------
# page: homepage
# ---------------------------------------------------------------------------
def build_home(lang, public_tours, featured):
    tr = T[lang]
    alt_paths = {l: url_home(l) for l in LANG_ORDER}

    # hero
    hero_media = placeholder_svg("sea_islands")
    hero_fn = os.path.join(SRC_ASSETS, "img", "hero")
    real_hero = None
    for ext in IMG_EXTS:
        if os.path.isfile(hero_fn + ext):
            real_hero = "hero" + ext
            break
    if real_hero:
        hero_media = '<img src="/assets/img/%s" alt="%s">' % (esca(real_hero), esca(tr["hero_kicker"]))

    hero = """<section class="hero" id="top">
<div class="hero__media">%s</div>
<div class="container"><div class="hero__inner">
<span class="hero__kicker">%s %s</span>
<h1>%s</h1>
<p class="hero__sub">%s</p>
<div class="hero__cta">%s<a class="btn btn--ghost" href="#excursions">%s %s</a></div>
<div class="hero__pay">%s<span>%s</span></div>
</div></div>
</section>""" % (
        hero_media, ICON["pin"], esc(tr["hero_kicker"]),
        esc(tr["hero_h1"]), esc(tr["hero_sub"]),
        wa_link(lang, tr["hero_cta_primary"], "btn btn--wa", "hero"),
        esc(tr["hero_cta_secondary"]), ICON["arrow"],
        ICON["shield"], esc(tr["payment_line"]))

    # featured
    feat_cards = "".join(tour_card(lang, t, i) for i, t in enumerate(featured))
    featured_sec = """<section class="section" id="featured">
<div class="container">
<div class="section__head reveal"><span class="section__kicker">%s</span>
<h2 class="section__title">%s</h2><p class="section__sub">%s</p></div>
<div class="grid">%s</div>
</div></section>""" % (
        esc(tr["nav_excursions"]), esc(tr["featured_title"]), esc(tr["featured_sub"]), feat_cards)

    # all + filters
    chips = ['<button class="filter" data-filter="all" aria-pressed="true">%s</button>' % esc(tr["filter_all"])]
    present = [c for c in CATEGORY_ORDER if any(t["category"] == c for t in public_tours)]
    for c in present:
        chips.append('<button class="filter" data-filter="%s" aria-pressed="false">%s</button>'
                     % (c, esc(CATEGORIES[lang][c])))
    all_cards = "".join(tour_card(lang, t, i) for i, t in enumerate(public_tours))
    all_sec = """<section class="section section--soft" id="excursions">
<div class="container">
<div class="section__head reveal"><span class="section__kicker">%s</span>
<h2 class="section__title">%s</h2><p class="section__sub">%s</p></div>
<div class="filters reveal">%s</div>
<div class="grid">%s</div>
</div></section>""" % (
        esc(tr["nav_excursions"]), esc(tr["all_title"]), esc(tr["all_sub"]),
        "".join(chips), all_cards)

    # process
    steps = "".join(
        '<div class="step reveal" data-delay="%d"><div class="step__num">%d</div><h3>%s</h3><p>%s</p></div>'
        % (i % 4, i + 1, esc(s[0]), esc(s[1])) for i, s in enumerate(tr["process_steps"]))
    process_sec = """<section class="section" id="process">
<div class="container">
<div class="section__head reveal"><span class="section__kicker">%s</span>
<h2 class="section__title">%s</h2><p class="section__sub">%s</p></div>
<div class="steps">%s</div>
</div></section>""" % (
        esc(tr["nav_process"]), esc(tr["process_title"]), esc(tr["process_sub"]), steps)

    # why
    why_icons = [ICON["shield"], ICON["chat"], ICON["car"], ICON["pin"]]
    why = "".join(
        '<div class="why__item reveal" data-delay="%d"><div class="why__icon">%s</div><div><h3>%s</h3><p>%s</p></div></div>'
        % (i % 2, why_icons[i], esc(it[0]), esc(it[1])) for i, it in enumerate(tr["why_items"]))
    why_sec = """<section class="section section--soft" id="why">
<div class="container">
<div class="section__head reveal"><span class="section__kicker">%s</span>
<h2 class="section__title">%s</h2></div>
<div class="why">%s</div>
</div></section>""" % (esc(tr["nav_why"]), esc(tr["why_title"]), why)

    # faq
    faqs = "".join(
        '<details%s><summary>%s</summary><div>%s</div></details>'
        % (" open" if i == 0 else "", esc(q), esc(a)) for i, (q, a) in enumerate(tr["faq"]))
    faq_sec = """<section class="section" id="faq">
<div class="container">
<div class="section__head reveal"><span class="section__kicker">FAQ</span>
<h2 class="section__title">%s</h2></div>
<div class="faq reveal">%s</div>
</div></section>""" % (esc(tr["faq_title"]), faqs)

    # contact
    contact_sec = """<section class="section section--soft" id="contact">
<div class="container">
<div class="contact__card reveal">
<h2>%s</h2><p>%s</p>
%s
</div>
</div></section>""" % (
        esc(tr["contact_title"]), esc(tr["contact_sub"]),
        wa_link(lang, tr["contact_whatsapp"], "btn btn--wa", "contact"))

    jsonld = {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": cfg.BRAND_NAME,
        "areaServed": "Hurghada, Egypt",
        "url": abs_url(url_home(lang)),
        "makesOffer": [{
            "@type": "Offer",
            "name": t["content"][lang]["name"],
            "price": t["price"],
            "priceCurrency": "EUR",
            "url": abs_url(url_tour(lang, t["slug"])),
        } for t in public_tours],
    }

    body = (header(lang, alt_paths) + '<main id="main">' + hero + trust_strip(lang)
            + featured_sec + all_sec + process_sec + why_sec + faq_sec + contact_sec
            + "</main>" + footer(lang, public_tours) + wa_float(lang))
    doc = head(lang, tr["meta_home_title"], tr["meta_home_desc"],
               url_home(lang), alt_paths, "/", jsonld) + body + scripts()
    write(os.path.join(DIST, lang, "index.html"), doc)

# ---------------------------------------------------------------------------
# page: tour detail
# ---------------------------------------------------------------------------
def build_tour(lang, tour, public_tours):
    tr = T[lang]
    c = tour["content"][lang]
    alt_paths = {l: url_tour(l, tour["slug"]) for l in LANG_ORDER}
    canonical = url_tour(lang, tour["slug"])

    # price block
    if tour["price_type"] == "per_boat":
        pill = ('<span class="pill">%s %s %s</span>'
                % (esc(tr["group_base_label"]), esc(tour.get("group_base", "")), esc(tr["persons"])))
        priceblock = ('<div class="priceblock"><b>&euro;%d</b><span>%s</span>%s</div>'
                      % (tour["price"], esc(tr["price_total"]), pill))
    else:
        priceblock = ('<div class="priceblock"><b>&euro;%d</b><span>%s</span></div>'
                      % (tour["price"], esc(price_unit(lang, tour))))

    program = "".join('<li><span>%s</span></li>' % esc(x) for x in c["highlights"])
    included = "".join('<li>%s<span>%s</span></li>' % (ICON["check_circle"], esc(x)) for x in c["included"])
    conditions = "".join('<li>%s<span>%s</span></li>' % (ICON["info"], esc(x)) for x in c["conditions"])

    # add-ons (hide restricted ones unless promotion is enabled)
    addon_html = ""
    visible_addons = [a for a in tour["addons"] if not a.get("restricted") or cfg.PROMOTE_LION_CUB]
    if visible_addons:
        rows = []
        for a in visible_addons:
            unit = tr["price_per_person"] if a["price_type"] == "per_person" else tr["price_total"]
            rcls = " is-restricted" if a.get("restricted") else ""
            rows.append('<div class="addon%s"><span>%s</span><b>+&euro;%d %s</b></div>'
                        % (rcls, esc(a["name"][lang]), a["price"], esc(unit)))
        addon_html = ('<div class="panel reveal"><h2>%s</h2><div class="addons">%s</div></div>'
                      % (esc(tr["label_addons"]), "".join(rows)))

    restricted_banner = ""
    if tour["restricted"]:
        restricted_banner = ('<div class="restricted-banner">%s<p>%s</p></div>'
                             % (ICON["info"], esc(tr["restricted_note"])))

    schedule_row = ""
    if tour.get("schedule"):
        schedule_row = ('<div class="paybar">%s<span>%s: %s</span></div>'
                        % (ICON["clock"], esc(tr["label_schedule"]), esc(tour["schedule"])))

    # related
    related = [t for t in public_tours if t["id"] != tour["id"] and t["category"] == tour["category"]]
    for t in public_tours:
        if len(related) >= 3:
            break
        if t["id"] != tour["id"] and t not in related:
            related.append(t)
    related = related[:3]
    related_html = ""
    if related:
        related_html = """<section class="section section--soft">
<div class="container">
<div class="section__head reveal"><h2 class="section__title">%s</h2></div>
<div class="related">%s</div>
</div></section>""" % (esc(tr["label_related"]),
                       "".join(tour_card(lang, t, i) for i, t in enumerate(related)))

    breadcrumb = ('<div class="container"><nav class="breadcrumb" aria-label="breadcrumb">'
                  '<a href="%s">%s</a><span>/</span><a href="%s#excursions">%s</a>'
                  '<span>/</span><span>%s</span></nav></div>'
                  % (esca(url_home(lang)), esc(tr["nav_home"]), esca(url_home(lang)),
                     esc(tr["nav_excursions"]), esc(c["name"])))

    tour_hero = """<section class="container"><div class="tour-hero">
<div class="tour-hero__media">%s</div>
<div>
<span class="tour-hero__cat">%s</span>
<h1>%s</h1>
<p class="tour-hero__intro">%s</p>
%s
<div class="tour-hero__cta">%s</div>
<div class="paybar">%s<span>%s</span></div>
</div>
</div></section>""" % (
        media(tour, lang, kind="hero"), esc(CATEGORIES[lang][tour["category"]]),
        esc(c["name"]), esc(c["intro"]), priceblock,
        wa_link(lang, tr["book_whatsapp"], "btn btn--wa", "detail-hero", tour),
        ICON["wallet"], esc(tr["payment_line"]))

    sticky = """<aside>
<div class="panel sticky-book reveal">
%s
<div style="margin:16px 0">%s</div>
<div class="paybar">%s<span>%s</span></div>
%s
</div>
</aside>""" % (
        priceblock,
        wa_link(lang, tr["book_whatsapp"], "btn btn--wa btn--block", "detail-sticky", tour),
        ICON["shield"], esc(tr["payment_line"]), schedule_row)

    main_col = """<div>
<div class="panel reveal"><h2>%s</h2><ul class="dotlist">%s</ul></div>
<div class="panel reveal"><h2>%s</h2><ul class="ticklist">%s</ul></div>
<div class="panel reveal"><h2>%s</h2><ul class="notelist">%s</ul>%s</div>
%s
</div>""" % (
        esc(tr["label_program"]), program,
        esc(tr["label_included"]), included,
        esc(tr["label_conditions"]), conditions, restricted_banner,
        addon_html)

    body_sec = """<section class="section"><div class="container">
<div class="tour-body">%s%s</div>
</div></section>""" % (main_col, sticky)

    # meta
    desc = c["intro"]
    if len(desc) > 158:
        desc = desc[:155].rstrip() + "..."
    title = "%s - &euro;%d%s" % (c["name"], tour["price"], tr["meta_title_suffix"])
    title = title.replace("&euro;", "€")

    jsonld = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": c["name"],
        "description": c["intro"],
        "brand": {"@type": "Brand", "name": cfg.BRAND_NAME},
        "offers": {
            "@type": "Offer",
            "price": tour["price"],
            "priceCurrency": "EUR",
            "availability": "https://schema.org/InStock",
            "url": abs_url(canonical),
        },
    }

    body = (header(lang, alt_paths) + '<main id="main">' + breadcrumb + tour_hero
            + body_sec + related_html + "</main>" + footer(lang, public_tours) + wa_float(lang))
    doc = head(lang, title, desc, canonical, alt_paths, alt_paths["fr"], jsonld) + body + scripts()
    out = os.path.join(DIST, lang, PATH_TOURS[lang], tour["slug"], "index.html")
    write(out, doc)

# ---------------------------------------------------------------------------
# page: root language splash
# ---------------------------------------------------------------------------
def build_root():
    links = "".join('<a href="%s" hreflang="%s">%s</a>'
                    % (esca(url_home(l)), HTML_LANG[l], esc(LANG_NATIVE[l])) for l in LANG_ORDER)
    alts = "".join('<link rel="alternate" hreflang="%s" href="%s">'
                   % (HTML_LANG[l], abs_url(url_home(l))) for l in LANG_ORDER)
    alts += '<link rel="alternate" hreflang="x-default" href="%s">' % abs_url("/")
    doc = """<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s - Hurghada VIP Excursions | FR / PL / RO</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
%s
<meta name="theme-color" content="#0bb4c4">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
<script>
(function(){try{var m={fr:'/fr/',pl:'/pl/',ro:'/ro/'};var l=(navigator.language||'').slice(0,2).toLowerCase();if(m[l]){location.replace(m[l]);}}catch(e){}})();
</script>
</head>
<body>
<main class="splash">
<div>
<span class="brand">%s<span class="brand__name"><b>KeRo</b> Tours<small>Hurghada</small></span></span>
<h1>%s</h1>
<p>%s</p>
<div class="splash__langs">%s</div>
</div>
</main>
</body>
</html>
""" % (cfg.DEFAULT_LANG, esc(cfg.BRAND_NAME),
       "Excursions VIP a Hurghada / Wycieczki VIP / Excursii VIP - FR PL RO",
       abs_url("/"), alts, BRAND_MARK,
       esc(cfg.BRAND_NAME),
       "Choisissez votre langue &middot; Wybierz jezyk &middot; Alege limba",
       links)
    write(os.path.join(DIST, "index.html"), doc)

def build_404():
    lang = cfg.DEFAULT_LANG
    tr = T[lang]
    doc = """<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="/assets/css/styles.css">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
</head>
<body>
<main class="splash"><div>
<span class="brand">%s<span class="brand__name"><b>KeRo</b> Tours</span></span>
<h1>%s</h1><p>%s</p>
<div class="splash__langs"><a href="/%s/">%s</a></div>
</div></main>
</body></html>
""" % (lang, esc(tr["notfound_title"]), BRAND_MARK, esc(tr["notfound_title"]),
       esc(tr["notfound_text"]), lang, esc(tr["notfound_home"]))
    write(os.path.join(DIST, "404.html"), doc)

# ---------------------------------------------------------------------------
# sitemap + robots + favicon + og image
# ---------------------------------------------------------------------------
def build_sitemap(public_tours):
    today = date.today().isoformat()
    urls = []

    def entry(path, alts):
        links = "".join('<xhtml:link rel="alternate" hreflang="%s" href="%s"/>'
                        % (HTML_LANG[l], abs_url(alts[l])) for l in LANG_ORDER)
        links += '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % abs_url("/")
        return ('<url><loc>%s</loc><lastmod>%s</lastmod>%s</url>'
                % (abs_url(path), today, links))

    home_alts = {l: url_home(l) for l in LANG_ORDER}
    for l in LANG_ORDER:
        urls.append(entry(url_home(l), home_alts))
    for t in public_tours:
        alts = {l: url_tour(l, t["slug"]) for l in LANG_ORDER}
        for l in LANG_ORDER:
            urls.append(entry(url_tour(l, t["slug"]), alts))

    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s\n</urlset>\n'
          % "\n".join(urls))
    write(os.path.join(DIST, "sitemap.xml"), sm)

def build_robots():
    txt = "User-agent: *\nAllow: /\n\nSitemap: %s\n" % abs_url("/sitemap.xml")
    write(os.path.join(DIST, "robots.txt"), txt)

def build_brand_assets():
    # favicon
    fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">'
           '<rect width="40" height="40" rx="11" fill="#0bb4c4"/>'
           '<path d="M8 27 Q14 22 20 27 T32 27" stroke="#fff" stroke-width="2.6" stroke-linecap="round" fill="none"/>'
           '<path d="M8 21 Q14 16 20 21 T32 21" stroke="#bdf3f6" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
           '<circle cx="28.5" cy="12.5" r="3.6" fill="#f2c14e"/></svg>')
    write(os.path.join(DIST, "assets", "img", "favicon.svg"), fav)
    # og default (branded, flagged as placeholder in IMAGE_AUDIT.md)
    og = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">'
          '<defs><linearGradient id="og" x1="0" y1="0" x2="1" y2="1">'
          '<stop offset="0" stop-color="#13c2d1"/><stop offset="1" stop-color="#06222a"/>'
          '</linearGradient></defs><rect width="1200" height="630" fill="url(#og)"/>'
          '<path d="M0 470 Q300 420 600 470 T1200 470 V630 H0 Z" fill="#ffffff" opacity=".10"/>'
          '<text x="80" y="300" font-family="Georgia,serif" font-size="78" fill="#ffffff" font-weight="bold">KeRo Tours Hurghada</text>'
          '<text x="82" y="370" font-family="Arial,sans-serif" font-size="34" fill="#bdf3f6">Excursions VIP &#183; Mer Rouge &#183; FR / PL / RO</text>'
          '</svg>')
    write(os.path.join(DIST, "assets", "img", "og-default.svg"), og)

# ---------------------------------------------------------------------------
# fs helpers + orchestration
# ---------------------------------------------------------------------------
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def copy_assets():
    dest = os.path.join(DIST, "assets")
    if os.path.isdir(SRC_ASSETS):
        shutil.copytree(SRC_ASSETS, dest, dirs_exist_ok=True)

def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)

    copy_assets()
    build_brand_assets()

    public_tours = [t for t in TOURS
                    if t["active"] and (not t["restricted"] or cfg.PROMOTE_LION_CUB)]
    featured = [t for t in public_tours if t["featured"]]

    for lang in LANG_ORDER:
        build_home(lang, public_tours, featured)
        for t in public_tours:
            build_tour(lang, t, public_tours)

    build_root()
    build_404()
    build_sitemap(public_tours)
    build_robots()

    # summary
    total_pages = 1 + len(LANG_ORDER) + len(LANG_ORDER) * len(public_tours) + 1
    print("Build complete -> dist/")
    print("  languages        : %s" % ", ".join(LANG_ORDER))
    print("  tours in data    : %d" % len(TOURS))
    print("  public tours     : %d" % len(public_tours))
    print("  featured         : %d" % len(featured))
    print("  pages generated  : %d (root + %d homepages + %d tour pages + 404)"
          % (total_pages, len(LANG_ORDER), len(LANG_ORDER) * len(public_tours)))
    print("  WhatsApp number  : %s" % (cfg.WHATSAPP_NUMBER or "NOT SET (launch blocker)"))

if __name__ == "__main__":
    main()
