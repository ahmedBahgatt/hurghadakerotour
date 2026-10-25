#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static site generator for Hurghada KeRo Tours & Transfer (V2).
Zero runtime dependencies (Python 3 standard library only).
Run:  python3 build.py   ->  outputs the full static site into ./dist
"""

import html
import json
import os
import shutil
from datetime import date
from urllib.parse import quote

import site_config as cfg
from data.i18n import (T, BOOKING, LANG_ORDER, LANG_NATIVE, PATH_TOURS, HTML_LANG,
                       OG_LOCALE, CATEGORIES, CATEGORY_ORDER, CATEGORY_INTRO)
from data.tours import TOURS

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
SRC_ASSETS = os.path.join(ROOT, "assets")
YEAR = date.today().year
IMG_EXTS = (".avif", ".webp", ".jpg", ".jpeg", ".png")

def esc(s):
    return html.escape(str(s), quote=False)

def esca(s):
    return html.escape(str(s), quote=True)

# ---------------------------------------------------------------------------
# icons
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
    "chevron": _line('<path d="m6 9 6 6 6-6"/>'),
    "calendar": _line('<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>'),
    "boat": _line('<path d="M3 15h18l-2 4a2 2 0 0 1-1.8 1H6.8A2 2 0 0 1 5 19z"/><path d="M5 15V8l7-3 7 3v7"/><path d="M12 5V2"/>'),
    "sun": _line('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
    "landmark": _line('<path d="M3 21h18"/><path d="M5 21V10M10 21V10M14 21V10M19 21V10"/><path d="m3 10 9-6 9 6z"/>'),
    "sparkle": _line('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>'),
    "zoom": _line('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5M11 8v6M8 11h6"/>'),
    "close": _line('<path d="M18 6 6 18M6 6l12 12"/>'),
    # --- social brand glyphs (filled, monochrome via currentColor) ---
    "instagram": ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                  '<path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.22.42.56.22.96.48 1.38.9.42.42.68.82.9 1.38.17.42.37 1.05.42 2.22.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.42 2.22-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.17-1.05.37-2.22.42-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.22-.42-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.17-.42-.37-1.05-.42-2.22-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85c.05-1.17.25-1.8.42-2.22.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.17 1.05-.37 2.22-.42 1.27-.06 1.65-.07 4.85-.07M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63c-.79.3-1.46.72-2.12 1.38C1.35 2.67.94 3.34.63 4.14.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.3.79.72 1.46 1.38 2.12.66.66 1.33 1.08 2.12 1.38.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56.79-.3 1.46-.72 2.12-1.38.66-.66 1.08-1.33 1.38-2.12.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91-.3-.79-.72-1.46-1.38-2.12-.66-.66-1.33-1.08-2.12-1.38-.76-.3-1.64-.5-2.91-.56C15.67.01 15.26 0 12 0m0 5.84A6.16 6.16 0 1 0 18.16 12 6.16 6.16 0 0 0 12 5.84M12 16a4 4 0 1 1 4-4 4 4 0 0 1-4 4m6.41-10.85a1.44 1.44 0 1 0 1.44 1.44 1.44 1.44 0 0 0-1.44-1.44"/></svg>'),
    "facebook": ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                 '<path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.96.93-1.96 1.89v2.25h3.33l-.53 3.49h-2.8V24C19.61 23.1 24 18.1 24 12.07"/></svg>'),
    "tiktok": ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
               '<path d="M16.6 5.82a4.28 4.28 0 0 1-1.01-2.82h-3.3v12.9a2.59 2.59 0 0 1-2.59 2.5 2.6 2.6 0 0 1-.6-5.11v-3.37a5.92 5.92 0 0 0-5.3 5.88 5.92 5.92 0 0 0 11.84 0V8.9a7.57 7.57 0 0 0 4.42 1.42V7.02a4.27 4.27 0 0 1-3.46-1.2"/></svg>'),
}

CATEGORY_ICON = {"sea_islands": "boat", "desert_safari": "sun",
                 "history_culture": "landmark", "activities": "sparkle"}

# ---------------------------------------------------------------------------
# placeholder art
# ---------------------------------------------------------------------------
_PH_COLORS = {
    "sea_islands":      ("#13c2d1", "#07697a"),
    "desert_safari":    ("#efc879", "#bb7d1e"),
    "history_culture":  ("#e0bd8e", "#8f5a2a"),
    "activities":       ("#19bcc9", "#0d5a67"),
}
_ph_counter = [0]

def placeholder_svg(category, cls="ph"):
    c1, c2 = _PH_COLORS.get(category, _PH_COLORS["activities"])
    _ph_counter[0] += 1
    gid = "g%d" % _ph_counter[0]
    if category == "sea_islands":
        motif = ('<path d="M0 360 Q200 320 400 360 T800 360 V500 H0 Z" fill="#ffffff" opacity=".10"/>'
                 '<path d="M0 410 Q200 375 400 410 T800 410 V500 H0 Z" fill="#ffffff" opacity=".14"/>'
                 '<circle cx="650" cy="120" r="54" fill="#ffffff" opacity=".22"/>')
    elif category == "desert_safari":
        motif = ('<circle cx="640" cy="130" r="56" fill="#ffffff" opacity=".28"/>'
                 '<path d="M0 380 Q250 300 480 370 T800 350 V500 H0 Z" fill="#ffffff" opacity=".12"/>'
                 '<path d="M0 430 Q300 370 560 420 T800 410 V500 H0 Z" fill="#000000" opacity=".06"/>')
    elif category == "history_culture":
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
    base = os.path.join(SRC_ASSETS, "img", "tours")
    for ext in IMG_EXTS:
        fn = tour_id + ext
        if os.path.isfile(os.path.join(base, fn)):
            return fn
    return None

def media(tour, lang, kind="card"):
    """Cover image for cards: real photo if present, else branded placeholder."""
    alt = esca(tour["content"][lang]["name"])
    fn = tour_image_file(tour["id"])
    if fn:
        loading = "" if kind == "hero" else ' loading="lazy" decoding="async"'
        dims = ' width="800" height="500"'
        return '<img src="/assets/img/tours/%s" alt="%s"%s%s>' % (esca(fn), alt, dims, loading)
    svg = placeholder_svg(tour["category"])
    badge = '<span class="ph__badge">%s</span>' % ICON["camera"]
    return svg + badge

def gallery_files(tour_id):
    """Sorted list of web paths for a tour's gallery images."""
    gdir = os.path.join(SRC_ASSETS, "img", "gallery", tour_id)
    if not os.path.isdir(gdir):
        return []
    files = sorted(f for f in os.listdir(gdir) if f.lower().endswith((".webp", ".avif", ".jpg", ".jpeg", ".png")))
    return ["/assets/img/gallery/%s/%s" % (tour_id, f) for f in files]

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
# structured data (SEO / AEO / GEO)
# ---------------------------------------------------------------------------
def sd_org(lang):
    org = {
        "@type": "TravelAgency",
        "@id": abs_url("/") + "#business",
        "name": cfg.BRAND_NAME,
        "url": abs_url(url_home(lang)),
        "image": abs_url("/assets/img/og-logo.png"),
        "logo": abs_url("/assets/img/logo.png"),
        "areaServed": {"@type": "City", "name": cfg.GEO["locality"]},
        "address": {"@type": "PostalAddress", "addressLocality": cfg.GEO["locality"],
                    "addressRegion": cfg.GEO["region"], "addressCountry": cfg.GEO["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": cfg.GEO["latitude"], "longitude": cfg.GEO["longitude"]},
        "priceRange": "€€",
    }
    if cfg.WHATSAPP_NUMBER:
        org["telephone"] = "+" + cfg.WHATSAPP_NUMBER
    same_as = [u for u in getattr(cfg, "SOCIAL", {}).values() if u]
    if same_as:
        org["sameAs"] = same_as
    return org

def sd_website(lang):
    return {"@type": "WebSite", "@id": abs_url("/") + "#website",
            "url": abs_url(url_home(lang)), "name": cfg.BRAND_NAME, "inLanguage": HTML_LANG[lang]}

def sd_faq(lang):
    return {"@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}}
                           for q, a in T[lang]["faq"]]}

def sd_breadcrumb(lang, tour):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": T[lang]["nav_home"], "item": abs_url(url_home(lang))},
        {"@type": "ListItem", "position": 2, "name": CATEGORIES[lang][tour["category"]],
         "item": abs_url(url_home(lang)) + "#cat-" + tour["category"]},
        {"@type": "ListItem", "position": 3, "name": tour["content"][lang]["name"],
         "item": abs_url(url_tour(lang, tour["slug"]))},
    ]}

# ---------------------------------------------------------------------------
# WhatsApp
# ---------------------------------------------------------------------------
def wa_text(lang, tour=None):
    # Generic (no tour): friendly inquiry that carries the localized HOMEPAGE
    # URL. Tour context: carries the exact localized DETAIL-PAGE URL + name.
    if tour is None:
        return T[lang]["wa_message_generic"].format(url=abs_url(url_home(lang)))
    return T[lang]["wa_message_tour"].format(
        tour=tour["content"][lang]["name"],
        url=abs_url(url_tour(lang, tour["slug"])))

def wa_link(lang, label, classes, pos, tour=None, with_icon=True, aria_label=None, book_open=False):
    tid = tour["id"] if tour else "none"
    text = wa_text(lang, tour)
    cls = classes
    if cfg.WHATSAPP_NUMBER:
        href = "https://wa.me/%s?text=%s" % (cfg.WHATSAPP_NUMBER, quote(text, safe=""))
        hattr = 'href="%s" data-wa-href="%s" target="_blank" rel="noopener"' % (esca(href), esca(href))
    else:
        cls += " is-pending"
        hattr = 'href="#" aria-disabled="true"'
    aria = ' aria-label="%s"' % esca(aria_label) if aria_label else ""
    icon = ICON["wa"] if with_icon else ""
    # book_open: JS upgrades this link to open the booking dialog (preselecting
    # the tour); the wa.me href remains the no-JS fallback.
    book = ' data-book-open' if book_open else ""
    return ('<a class="%s" %s%s%s data-wa data-wa-text="%s" data-tour="%s" data-pos="%s">'
            '%s<span>%s</span></a>'
            % (cls, hattr, aria, book, esca(text), tid, pos, icon, esc(label)))

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
# price
# ---------------------------------------------------------------------------
def price_unit(lang, tour):
    if tour["price_type"] == "per_boat":
        return T[lang]["price_per_boat"]
    return T[lang]["price_per_person"]

def card_price(lang, tour):
    return '<div class="card__price"><b>&euro;%d</b> <span>%s</span></div>' % (tour["price"], esc(price_unit(lang, tour)))

# ---------------------------------------------------------------------------
# brand / head / header / footer
# ---------------------------------------------------------------------------
LOGO_ALT = "Hurghada KeRo Tours &amp; Transfer"

def brand(lang, extra_cls=""):
    return ('<a class="brand %s" href="/%s/" aria-label="%s">'
            '<img class="brand__logo" src="/assets/img/logo.png" alt="%s" width="120" height="120"></a>'
            % (extra_cls, lang, esca(cfg.BRAND_NAME), LOGO_ALT))

SOCIAL_NAMES = {"instagram": "Instagram", "facebook": "Facebook", "tiktok": "TikTok"}

def social_links(lang, cls="social", with_label=True):
    """Row of brand icon links (open in a new tab). Empty if none configured."""
    social = getattr(cfg, "SOCIAL", {})
    links = [(k, v) for k, v in social.items() if v and k in ICON]
    if not links:
        return ""
    tr = T[lang]
    items = []
    for key, url in links:
        net = SOCIAL_NAMES.get(key, key.title())
        aria = tr["social_aria"].format(brand=cfg.BRAND_SHORT, network=net)
        items.append('<a class="social__link social__link--%s" href="%s" target="_blank" '
                     'rel="noopener" aria-label="%s">%s</a>' % (key, esca(url), esca(aria), ICON[key]))
    label = ('<span class="social__label">%s</span>' % esc(tr["social_follow"])) if with_label else ""
    return ('<div class="%s">%s<div class="social__row" role="list" aria-label="%s">%s</div></div>'
            % (cls, label, esca(tr["social_follow"]), "".join(items)))

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
            lines.append("window.KERO_ADS_CONVERSION='%s/%s';" % (ads, cfg.GOOGLE_ADS_CONVERSION_LABEL.strip()))
    return ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>\n'
            '<script>%s</script>\n' % (primary, "".join(lines)))

CSP = ("default-src 'self'; "
       "img-src 'self' data:; "
       "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
       "font-src https://fonts.gstatic.com; "
       "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; "
       "connect-src 'self' https://www.google-analytics.com https://region1.google-analytics.com; "
       "frame-ancestors 'none'; base-uri 'self'; form-action 'self'")

def security_meta():
    robots = "index,follow,max-image-preview:large" if getattr(cfg, "ALLOW_INDEXING", True) else "noindex,follow"
    m = ['<meta name="referrer" content="strict-origin-when-cross-origin">',
         '<meta http-equiv="Content-Security-Policy" content="%s">' % CSP,
         '<meta name="robots" content="%s">' % robots]
    if cfg.GOOGLE_SITE_VERIFICATION.strip():
        m.append('<meta name="google-site-verification" content="%s">' % esca(cfg.GOOGLE_SITE_VERIFICATION.strip()))
    if cfg.BING_SITE_VERIFICATION.strip():
        m.append('<meta name="msvalidate.01" content="%s">' % esca(cfg.BING_SITE_VERIFICATION.strip()))
    return "".join(m)

def head(lang, title, desc, canonical_path, alt_paths, xdefault_path, jsonld=None):
    alts = []
    for l in LANG_ORDER:
        if l in alt_paths:
            alts.append('<link rel="alternate" hreflang="%s" href="%s">' % (HTML_LANG[l], abs_url(alt_paths[l])))
    alts.append('<link rel="alternate" hreflang="x-default" href="%s">' % abs_url(xdefault_path))
    jsonld_tag = ""
    if jsonld:
        jsonld_tag = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False, separators=(",", ":"))
    og_img = abs_url("/assets/img/og-logo.png")
    return """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{sec}
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website">
<meta property="og:locale" content="{oglocale}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{ogimg}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="{brand}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0bb4c4">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/img/favicon-16.png">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/img/favicon-512.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/styles.css">
{analytics}<script src="/assets/js/config.js"></script>
{jsonld}</head>
<body>
<a class="skip-link" href="#main">{skip}</a>
""".format(lang=HTML_LANG[lang], sec=security_meta(), title=esca(title), desc=esca(desc),
           canon=abs_url(canonical_path), alts="\n".join(alts), oglocale=OG_LOCALE[lang],
           ogimg=og_img, brand=esca(cfg.BRAND_NAME), analytics=analytics_head(),
           jsonld=jsonld_tag, skip=esc(T[lang]["skip_to_content"]))

def langswitch_html(lang, alt_paths, cls="langswitch"):
    tr = T[lang]
    pills = []
    for l in LANG_ORDER:
        target = alt_paths.get(l, url_home(l))
        cur = ' aria-current="true"' if l == lang else ""
        pills.append('<a href="%s"%s hreflang="%s">%s</a>' % (esca(target), cur, HTML_LANG[l], l.upper()))
    return '<div class="%s" role="group" aria-label="%s">%s</div>' % (cls, esca(tr["select_language"]), "".join(pills))

def header(lang, alt_paths, public_tours, home_base=None):
    tr = T[lang]
    bk = BOOKING[lang]
    home = home_base or url_home(lang)

    # --- Desktop: Excursions dropdown ---
    dd_items = ['<a href="%s#excursions" role="menuitem">%s</a>' % (esca(home), esc(tr["nav_excursions_all"]))]
    for cid in CATEGORY_ORDER:
        dd_items.append('<a href="%s#cat-%s" role="menuitem">%s%s</a>'
                        % (esca(home), cid, ICON[CATEGORY_ICON[cid]], esc(CATEGORIES[lang][cid])))
    dropdown = ('<li class="nav__item nav__has-dd" data-dd>'
                '<button class="nav__dd-trigger" data-dd-trigger aria-expanded="false" aria-haspopup="true">'
                '%s %s</button>'
                '<div class="nav__dd" role="menu">%s</div></li>'
                % (esc(tr["nav_excursions"]), ICON["chevron"], "".join(dd_items)))
    other = [(tr["nav_process"], home + "#process"), (tr["nav_why"], home + "#why"),
             (tr["nav_faq"], home + "#faq"), (tr["nav_contact"], home + "#contact")]
    other_html = "".join('<li><a href="%s">%s</a></li>' % (esca(h), esc(t)) for t, h in other)

    langswitch = langswitch_html(lang, alt_paths)
    # Mobile header center: language switcher (FR/PL/RO). Socials live in the
    # drawer only, to keep the mobile header clean (logo / langs / hamburger).
    langswitch_mobile = langswitch_html(lang, alt_paths, "langswitch langswitch--mobile")
    book_btn = ('<button class="btn btn--wa btn--sm nav__book" data-book-open data-pos="nav">%s<span>%s</span></button>'
                % (ICON["wa"], esc(tr["nav_book"])))

    # --- Mobile slide-in drawer (right) ---
    # Excursions: one expandable section per category, listing its tour links.
    draw_cats = []
    for cid in CATEGORY_ORDER:
        cts = [t for t in public_tours if t["category"] == cid]
        if not cts:
            continue
        links = "".join('<a href="%s">%s</a>' % (esca(url_tour(lang, t["slug"])), esc(t["content"][lang]["name"])) for t in cts)
        links += '<a class="draw-cat__all" href="%s#cat-%s">%s</a>' % (esca(home), cid, esc(tr["nav_excursions_all"]))
        draw_cats.append(
            '<details class="draw-cat"><summary>%s%s<span class="draw-cat__chev">%s</span></summary>'
            '<div class="draw-cat__list">%s</div></details>'
            % (ICON[CATEGORY_ICON[cid]], esc(CATEGORIES[lang][cid]), ICON["chevron"], links))
    draw_other = "".join('<a class="draw-link" href="%s">%s</a>' % (esca(h), esc(t)) for t, h in other)
    draw_book = ('<button class="btn btn--wa btn--block drawer__book" data-book-open data-pos="drawer">%s<span>%s</span></button>'
                 % (ICON["wa"], esc(bk["drawer_book"])))
    draw_social = social_links(lang, "drawer__social", with_label=False)
    drawer = """<div class="drawer" data-drawer id="drawer" aria-hidden="true">
<div class="drawer__scrim" data-drawer-close></div>
<aside class="drawer__panel" role="dialog" aria-modal="true" aria-label="%s">
<div class="drawer__head">
<img class="drawer__logo" src="/assets/img/logo.png" alt="%s" width="44" height="44">
<button class="drawer__close" data-drawer-close aria-label="%s">%s</button>
</div>
<div class="drawer__body">
%s
<nav class="drawer__nav" aria-label="%s">
<p class="drawer__group">%s</p>
%s
<div class="drawer__links">%s</div>
</nav>
<div class="drawer__foot">
%s
%s
</div>
</div>
</aside>
</div>""" % (
        esca(bk["menu_title"]), LOGO_ALT, esca(tr["close_menu"]), ICON["close"],
        draw_book, esca(tr["nav_excursions"]), esc(tr["nav_excursions"]),
        "".join(draw_cats), draw_other,
        langswitch_html(lang, alt_paths, "langswitch drawer__lang"), draw_social)

    return """<header class="header">
<div class="container">
<nav class="nav" aria-label="%s">
%s
%s
<ul class="nav__links">%s%s</ul>
<div class="nav__right">%s%s
<button class="nav__toggle" data-drawer-open aria-label="%s" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
</div>
</nav>
</div>
</header>
%s""" % (
        esca(tr["nav_excursions"]), brand(lang), langswitch_mobile, dropdown, other_html,
        langswitch, book_btn, esca(tr["open_menu"]), drawer)

def footer(lang, public_tours, home_base=None):
    tr = T[lang]
    home = home_base or url_home(lang)
    # Column 2 - Explore: the four categories only (not all 11 tours).
    cat_links = "".join('<a href="%s#cat-%s">%s%s</a>' % (esca(home), cid, ICON[CATEGORY_ICON[cid]], esc(CATEGORIES[lang][cid]))
                        for cid in CATEGORY_ORDER)
    # Column 3 - Contact.
    contact_rows = [wa_link(lang, tr["contact_whatsapp"], "footer__wa", "footer")]
    if cfg.BUSINESS["phone_display"]:
        contact_rows.append('<a href="tel:%s">%s %s</a>'
                            % (esca(cfg.BUSINESS["phone_display"].replace(" ", "")), ICON["phone"], esc(cfg.BUSINESS["phone_display"])))
    if cfg.BUSINESS["email"]:
        contact_rows.append('<a href="mailto:%s">%s %s</a>' % (esca(cfg.BUSINESS["email"]), ICON["mail"], esc(cfg.BUSINESS["email"])))
    if cfg.BUSINESS["address"]:
        contact_rows.append('<div class="footer__addr">%s %s</div>' % (ICON["pin"], esc(cfg.BUSINESS["address"])))
    langs = " ".join('<a href="%s" hreflang="%s">%s</a>' % (esca(url_home(l)), HTML_LANG[l], l.upper()) for l in LANG_ORDER)
    legal = ""
    if cfg.BUSINESS["legal_name"] or cfg.BUSINESS["license_number"]:
        bits = []
        if cfg.BUSINESS["legal_name"]:
            bits.append(esc(cfg.BUSINESS["legal_name"]))
        if cfg.BUSINESS["license_number"]:
            bits.append(esc(cfg.BUSINESS["license_number"]))
        legal = ' <span class="footer__legal">&middot; %s</span>' % " &middot; ".join(bits)
    return """<footer class="footer">
<div class="container">
<div class="footer__grid">
<div class="footer__brand">
<img class="footer__logo" src="/assets/img/logo.png" alt="%s" width="150" height="150">
<p>%s</p>
<p class="footer__pay">%s %s</p>
%s
</div>
<nav class="footer__col" aria-label="%s"><h4>%s</h4><div class="footer__links footer__cats">%s</div></nav>
<div class="footer__col"><h4>%s</h4><div class="footer__links">%s</div></div>
</div>
<div class="footer__bottom">
<div class="footer__copy">&copy; %d %s. %s%s</div>
<div class="footer__langs">%s</div>
</div>
</div>
</footer>""" % (
        LOGO_ALT, esc(tr["footer_about"]),
        ICON["shield"], esc(tr["payment_line"]),
        social_links(lang, "footer__social"),
        esca(tr["footer_excursions_title"]), esc(tr["footer_excursions_title"]), cat_links,
        esc(tr["footer_contact_title"]), "".join(contact_rows),
        YEAR, esc(cfg.BRAND_NAME), esc(tr["footer_rights"]), legal,
        langs)

def scripts():
    return '<script src="/assets/js/app.js" defer></script>\n</body>\n</html>\n'

# ---------------------------------------------------------------------------
# Booking: data for JS, the dialog (bottom-sheet / modal), the sticky bar
# ---------------------------------------------------------------------------
def booking_data_script(lang, public_tours, tour_id=None):
    """Runtime data for the booking form: baked WhatsApp number + localized
    message/label strings + a tour map (name, price, unit, type, canonical URL)
    so the form can show read-only tour context and build the message without
    an editable dropdown. `tour` is the current page's tour (reliable context on
    a tour page); empty on general pages. config.js may still override
    KERO_WHATSAPP."""
    baked = cfg.WHATSAPP_NUMBER or ""
    bk = BOOKING[lang]
    tours = {}
    for t in public_tours:
        unit = bk["unit_boat"] if t["price_type"] == "per_boat" else bk["unit_person"]
        tours[t["id"]] = {
            "name": t["content"][lang]["name"],
            "price": t["price"],
            "unit": unit,
            "type": t["price_type"],
            "url": abs_url(url_tour(lang, t["slug"])),
        }
    payload = {"wa": baked, "tour": tour_id or "", "s": bk, "tours": tours}
    return '<script>window.KERO_BK=%s;</script>' % json.dumps(payload, ensure_ascii=False, separators=(",", ":"))

def booking_options(lang, public_tours):
    opts = []
    for t in public_tours:
        opts.append('<option value="%s" data-price="%d" data-type="%s">%s</option>'
                    % (esca(t["id"]), t["price"], t["price_type"], esc(t["content"][lang]["name"])))
    return "".join(opts)

def booking_dialog(lang, public_tours):
    """Booking dialog. Two modes, resolved by JS:
    - tour context present (tour page / clicked card / sticky bar): read-only
      tour title + price, no excursion dropdown;
    - no context (homepage general CTAs): an excursion selector is shown.
    Fields: hotel (required), room (optional), people (required int), notes
    (optional). No customer-name field. No date field (confirmed on WhatsApp)."""
    bk = BOOKING[lang]
    return """<div class="bookdlg" data-bookdlg hidden aria-hidden="true">
<div class="bookdlg__scrim" data-book-close></div>
<div class="bookdlg__panel" role="dialog" aria-modal="true" aria-labelledby="bk-title">
<div class="bookdlg__head">
<div><h2 id="bk-title">%s</h2><p>%s</p></div>
<button class="bookdlg__close" type="button" data-book-close aria-label="%s">%s</button>
</div>
<form class="bookform" data-bookform novalidate>
<div class="bookform__context" data-bk-context hidden>
<span class="bookform__context-label">%s</span>
<b data-bk-context-name></b>
<span class="bookform__context-price" data-bk-context-price></span>
</div>
<label class="bookform__field" data-bk-select-field hidden><span>%s</span>
<select name="excursion" data-bk-exc>
<option value="" disabled selected>%s</option>
%s
</select></label>
<div class="bookform__price" data-bk-price hidden></div>
<label class="bookform__field"><span>%s</span>
<input name="hotel" type="text" autocomplete="off" placeholder="%s" required></label>
<div class="bookform__grid">
<label class="bookform__field"><span>%s</span><input name="room" type="text" inputmode="numeric" autocomplete="off" placeholder="%s"></label>
<label class="bookform__field"><span>%s</span><input name="people" type="number" inputmode="numeric" min="1" max="40" step="1" value="2" placeholder="%s" required></label>
</div>
<label class="bookform__field"><span>%s</span>
<textarea name="notes" rows="2" placeholder="%s"></textarea></label>
<p class="bookform__note">%s<span>%s</span></p>
<div class="bookform__err" data-bk-err role="alert" hidden></div>
<button type="submit" class="btn btn--wa btn--block bookform__submit">%s<span>%s</span></button>
</form>
</div>
</div>""" % (
        esc(bk["form_title"]), esc(bk["form_sub"]), esca(bk["f_close"]), ICON["close"],
        esc(bk["f_excursion"]),
        esc(bk["f_excursion"]), esc(bk["f_excursion_ph"]), booking_options(lang, public_tours),
        esc(bk["f_hotel"]), esca(bk["f_hotel_ph"]),
        esc(bk["f_room"]), esca(bk["f_room_ph"]),
        esc(bk["f_people"]), esca(bk["f_people_ph"]),
        esc(bk["f_notes"]), esca(bk["f_notes_ph"]),
        ICON["shield"], esc(bk["f_nodeposit"]),
        ICON["wa"], esc(bk["f_submit"]))

def book_bar(lang, tour):
    """Sticky mobile bottom booking bar for a tour page. LEFT: localized price +
    unit. RIGHT: one premium KeRo-teal BOOKING button (opens the form, never
    WhatsApp directly, no WhatsApp icon/color)."""
    bk = BOOKING[lang]
    unit = bk["unit_boat"] if tour["price_type"] == "per_boat" else bk["unit_person"]
    return ('<div class="bookbar" data-bookbar>'
            '<div class="bookbar__price"><b>&euro;%d</b> <span>%s</span></div>'
            '<button class="btn btn--book bookbar__btn" type="button" data-book-open data-tour="%s" data-pos="bar">'
            '%s<span>%s</span></button>'
            '</div>' % (tour["price"], esc(unit), esca(tour["id"]), ICON["calendar"], esc(bk["bar_book"])))

def wa_tour_float(lang, tour):
    """Separate floating circular WhatsApp button on a tour page, sitting just
    above the right side of the sticky booking bar. Opens a DIRECT WhatsApp chat
    (no booking form) with the tour name + canonical URL prefilled. Green
    WhatsApp identity, clearly distinct from the teal booking CTA."""
    text = T[lang]["wa_tour_direct"].format(tour=tour["content"][lang]["name"],
                                            url=abs_url(url_tour(lang, tour["slug"])))
    cls = "wa-bubble"
    if cfg.WHATSAPP_NUMBER:
        href = "https://wa.me/%s?text=%s" % (cfg.WHATSAPP_NUMBER, quote(text, safe=""))
        hattr = 'href="%s" data-wa-href="%s" target="_blank" rel="noopener"' % (esca(href), esca(href))
    else:
        cls += " is-pending"
        hattr = 'href="#" aria-disabled="true"'
    return ('<a class="%s" %s data-wa data-wa-text="%s" data-tour="%s" data-pos="tour-float" aria-label="%s">%s</a>'
            % (cls, hattr, esca(text), esca(tour["id"]), esca(T[lang]["floating_wa_label"]), ICON["wa"]))

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
<a class="btn btn--outline btn--sm" href="%s" aria-label="%s">%s</a>
%s
</div>
</div>
</article>""" % (
        tour["category"], delay % 3, esca(detail), esca(tour["content"][lang]["name"]),
        media(tour, lang), esc(cat), flag, card_price(lang, tour),
        esc(tour["content"][lang]["name"]), esc(tour["content"][lang]["tagline"]),
        esca(detail), esca("%s - %s" % (tr["view_details"], tour["content"][lang]["name"])),
        esc(tr["card_details"]),
        wa_link(lang, tr["card_book"], "btn btn--wa btn--sm", "card", tour,
                aria_label="%s - %s" % (tr["book_whatsapp"], tour["content"][lang]["name"]),
                book_open=True))

def trust_strip(lang):
    tr = T[lang]
    icons = [ICON["star"], ICON["shield"], ICON["wallet"], ICON["chat"]]
    items = "".join('<div class="trust__item">%s<span>%s</span></div>' % (icons[i], esc(tr["trust"][i])) for i in range(4))
    return '<section class="trust" aria-label="%s"><div class="container"><div class="trust__row">%s</div></div></section>' % (esca(tr["payment_line"]), items)

def gallery_html(tour, lang):
    """Premium gallery for the detail page. Falls back to single media / placeholder."""
    imgs = gallery_files(tour["id"])
    name = tour["content"][lang]["name"]
    if not imgs:
        return '<div class="tour-hero__media">%s</div>' % media(tour, lang, kind="hero")
    data = esca(json.dumps(imgs))
    main_alt = esca("%s - 1" % name)
    main = ('<div class="gallery__main">'
            '<button class="gallery__nav gallery__nav--prev" data-gprev aria-label="%s">%s</button>'
            '<img class="gallery__img" data-gmain src="%s" alt="%s" width="1200" height="825" decoding="async">'
            '<button class="gallery__nav gallery__nav--next" data-gnext aria-label="%s">%s</button>'
            '<span class="gallery__counter"><b data-gcur>1</b> / %d</span>'
            '<button class="gallery__zoom" data-gzoom aria-label="%s">%s</button>'
            '</div>'
            % (esca(T[lang]["gallery_prev"]), ICON["chevron"].replace('m6 9 6 6 6-6', 'm15 6-6 6 6 6'),
               esca(imgs[0]), main_alt,
               esca(T[lang]["gallery_next"]), ICON["chevron"].replace('m6 9 6 6 6-6', 'm9 6 6 6-6 6'),
               len(imgs), esca(T[lang]["gallery_open"]), ICON["zoom"]))
    thumbs = ""
    if len(imgs) > 1:
        tb = []
        for i, u in enumerate(imgs):
            cls = "gallery__thumb is-active" if i == 0 else "gallery__thumb"
            tb.append('<button class="%s" data-gthumb="%d" aria-label="%s"><img src="%s" alt="%s - %d" width="160" height="110" loading="lazy" decoding="async"></button>'
                      % (cls, i, esca("%s - %d" % (name, i + 1)), esca(u), esca(name), i + 1))
        thumbs = '<div class="gallery__thumbs">%s</div>' % "".join(tb)
    return '<div class="gallery" data-gallery data-images="%s">%s%s</div>' % (data, main, thumbs)

# ---------------------------------------------------------------------------
# hero media (slideshow of clean stills, or single image / placeholder)
# ---------------------------------------------------------------------------
def hero_media_html(lang):
    """Single responsive panoramic hero image (WebP, srcset). The LCP image:
    eager + fetchpriority high, explicit intrinsic size to avoid layout shift.
    Falls back to a branded placeholder if the variants are missing."""
    hdir = os.path.join(SRC_ASSETS, "img", "hero")
    variants = [480, 768, 1200, 1672]
    have = all(os.path.isfile(os.path.join(hdir, "hero-%d.webp" % w)) for w in variants)
    if have:
        srcset = ", ".join("/assets/img/hero/hero-%d.webp %dw" % (w, w) for w in variants)
        return ('<div class="hero__media">'
                '<img class="hero__img" src="/assets/img/hero/hero-1200.webp" '
                'srcset="%s" sizes="100vw" alt="" aria-hidden="true" '
                'width="1672" height="941" fetchpriority="high" decoding="async"></div>'
                % srcset)
    return '<div class="hero__media">%s</div>' % placeholder_svg("sea_islands")

# ---------------------------------------------------------------------------
# homepage
# ---------------------------------------------------------------------------
def build_home(lang, public_tours, out_path=None, canonical_path=None, home_base=None):
    tr = T[lang]
    alt_paths = {l: url_home(l) for l in LANG_ORDER}
    canonical_path = canonical_path or url_home(lang)

    hero_media = hero_media_html(lang)

    hero = """<section class="hero" id="top">
%s
<div class="container"><div class="hero__inner">
<span class="hero__kicker">%s %s</span>
<h1>%s</h1>
<p class="hero__sub">%s</p>
<div class="hero__cta">%s<a class="btn btn--ghost" href="#excursions">%s %s</a></div>
<div class="hero__pay">%s<span>%s</span></div>
</div></div>
</section>""" % (
        hero_media, ICON["pin"], esc(tr["hero_kicker"]), esc(tr["hero_h1"]), esc(tr["hero_sub"]),
        wa_link(lang, tr["hero_cta_primary"], "btn btn--wa", "hero", book_open=True),
        esc(tr["hero_cta_secondary"]), ICON["arrow"], ICON["shield"], esc(tr["payment_line"]))

    # category shortcut chips
    chips = "".join('<a class="catchip" href="#cat-%s">%s%s</a>' % (cid, ICON[CATEGORY_ICON[cid]], esc(CATEGORIES[lang][cid])) for cid in CATEGORY_ORDER)
    chipbar = '<div class="catbar"><div class="container"><div class="catbar__row">%s</div></div></div>' % chips

    # four category sections, each tour exactly once
    sections = ['<span id="excursions" class="anchor"></span>']
    for idx, cid in enumerate(CATEGORY_ORDER):
        tours = [t for t in public_tours if t["category"] == cid]
        if not tours:
            continue
        cards = "".join(tour_card(lang, t, i) for i, t in enumerate(tours))
        soft = " section--soft" if idx % 2 == 1 else ""
        sections.append("""<section class="section cat-section%s" id="cat-%s">
<div class="container">
<div class="section__head reveal"><span class="section__kicker">%s %s</span>
<h2 class="section__title">%s</h2><p class="section__sub">%s</p></div>
<div class="grid">%s</div>
</div></section>""" % (soft, cid, ICON[CATEGORY_ICON[cid]], esc(CATEGORIES[lang][cid]),
                       esc(CATEGORIES[lang][cid]), esc(CATEGORY_INTRO[lang][cid]), cards))

    # process
    steps = "".join('<div class="step reveal" data-delay="%d"><div class="step__num">%d</div><h3>%s</h3><p>%s</p></div>'
                    % (i % 4, i + 1, esc(s[0]), esc(s[1])) for i, s in enumerate(tr["process_steps"]))
    process_sec = """<section class="section section--soft" id="process">
<div class="container"><div class="section__head reveal"><span class="section__kicker">%s</span>
<h2 class="section__title">%s</h2><p class="section__sub">%s</p></div><div class="steps">%s</div></div></section>""" % (
        esc(tr["nav_process"]), esc(tr["process_title"]), esc(tr["process_sub"]), steps)

    why_icons = [ICON["shield"], ICON["chat"], ICON["car"], ICON["pin"]]
    why = "".join('<div class="why__item reveal" data-delay="%d"><div class="why__icon">%s</div><div><h3>%s</h3><p>%s</p></div></div>'
                  % (i % 2, why_icons[i], esc(it[0]), esc(it[1])) for i, it in enumerate(tr["why_items"]))
    why_sec = """<section class="section" id="why">
<div class="container"><div class="section__head reveal"><span class="section__kicker">%s</span>
<h2 class="section__title">%s</h2></div><div class="why">%s</div></div></section>""" % (
        esc(tr["nav_why"]), esc(tr["why_title"]), why)

    faqs = "".join('<details%s><summary>%s</summary><div>%s</div></details>' % (" open" if i == 0 else "", esc(q), esc(a))
                   for i, (q, a) in enumerate(tr["faq"]))
    faq_sec = """<section class="section section--soft" id="faq">
<div class="container"><div class="section__head reveal"><span class="section__kicker">FAQ</span>
<h2 class="section__title">%s</h2></div><div class="faq reveal">%s</div></div></section>""" % (esc(tr["faq_title"]), faqs)

    contact_sec = """<section class="section" id="contact">
<div class="container"><div class="contact__card reveal"><h2>%s</h2><p>%s</p>%s%s</div></div></section>""" % (
        esc(tr["contact_title"]), esc(tr["contact_sub"]),
        wa_link(lang, tr["contact_whatsapp"], "btn btn--wa", "contact", book_open=True),
        social_links(lang, "contact__social"))

    org = sd_org(lang)
    org["makesOffer"] = [{"@type": "Offer", "name": t["content"][lang]["name"], "price": t["price"],
                          "priceCurrency": "EUR", "url": abs_url(url_tour(lang, t["slug"]))} for t in public_tours]
    jsonld = {"@context": "https://schema.org", "@graph": [sd_website(lang), org, sd_faq(lang)]}

    body = (header(lang, alt_paths, public_tours, home_base) + '<main id="main">' + hero + trust_strip(lang) + chipbar
            + "".join(sections) + process_sec + why_sec + faq_sec + contact_sec
            + "</main>" + footer(lang, public_tours, home_base) + wa_float(lang)
            + booking_dialog(lang, public_tours) + booking_data_script(lang, public_tours))
    doc = head(lang, tr["meta_home_title"], tr["meta_home_desc"], canonical_path, alt_paths, "/", jsonld) + body + scripts()
    write(out_path or os.path.join(DIST, lang, "index.html"), doc)

# ---------------------------------------------------------------------------
# tour detail
# ---------------------------------------------------------------------------
def build_tour(lang, tour, public_tours):
    tr = T[lang]
    c = tour["content"][lang]
    alt_paths = {l: url_tour(l, tour["slug"]) for l in LANG_ORDER}
    canonical = url_tour(lang, tour["slug"])

    if tour["price_type"] == "per_boat":
        pill = '<span class="pill">%s %s %s</span>' % (esc(tr["group_base_label"]), esc(tour.get("group_base", "")), esc(tr["persons"]))
        priceblock = '<div class="priceblock"><b>&euro;%d</b><span>%s</span>%s</div>' % (tour["price"], esc(tr["price_total"]), pill)
    else:
        priceblock = '<div class="priceblock"><b>&euro;%d</b><span>%s</span></div>' % (tour["price"], esc(price_unit(lang, tour)))

    experience = "".join('<li>%s<span>%s</span></li>' % (ICON["check_circle"], esc(x)) for x in c["highlights"])
    program = "".join('<li class="progstep"><span class="progstep__n">%d</span><div><b>%s</b><p>%s</p></div></li>'
                      % (i + 1, esc(st[0]), esc(st[1])) for i, st in enumerate(c.get("program", [])))
    included = "".join('<li>%s<span>%s</span></li>' % (ICON["check"], esc(x)) for x in c["included"])
    practical = "".join('<li>%s<span>%s</span></li>' % (ICON["info"], esc(x)) for x in c.get("practical", []))
    conditions = "".join('<li>%s<span>%s</span></li>' % (ICON["info"], esc(x)) for x in c["conditions"])

    addon_html = ""
    visible_addons = [a for a in tour["addons"] if not a.get("restricted") or cfg.SHOW_LION_ADDON]
    if visible_addons:
        rows = []
        for a in visible_addons:
            unit = tr["price_per_person"] if a["price_type"] == "per_person" else tr["price_total"]
            rcls = " is-restricted" if a.get("restricted") else ""
            rows.append('<div class="addon%s"><span>%s</span><b>+&euro;%d %s</b></div>' % (rcls, esc(a["name"][lang]), a["price"], esc(unit)))
        addon_html = '<div class="panel reveal"><h2>%s</h2><div class="addons">%s</div></div>' % (esc(tr["label_addons"]), "".join(rows))

    restricted_banner = ""
    if tour["restricted"]:
        restricted_banner = '<div class="restricted-banner">%s<p>%s</p></div>' % (ICON["info"], esc(tr["restricted_note"]))

    schedule_row = ""
    if tour.get("schedule"):
        schedule_row = '<div class="paybar">%s<span>%s: %s</span></div>' % (ICON["clock"], esc(tr["label_schedule"]), esc(tour["schedule"]))

    # related: same category first, then fill
    related = [t for t in public_tours if t["id"] != tour["id"] and t["category"] == tour["category"]]
    for t in public_tours:
        if len(related) >= 3:
            break
        if t["id"] != tour["id"] and t not in related:
            related.append(t)
    related = related[:3]
    related_html = ""
    if related:
        related_html = """<section class="section section--soft"><div class="container">
<div class="section__head reveal"><h2 class="section__title">%s</h2></div>
<div class="related">%s</div></div></section>""" % (esc(tr["label_related"]), "".join(tour_card(lang, t, i) for i, t in enumerate(related)))

    breadcrumb = ('<div class="container"><nav class="breadcrumb" aria-label="breadcrumb">'
                  '<a href="%s">%s</a><span>/</span><a href="%s#cat-%s">%s</a><span>/</span><span>%s</span></nav></div>'
                  % (esca(url_home(lang)), esc(tr["nav_home"]), esca(url_home(lang)), tour["category"],
                     esc(CATEGORIES[lang][tour["category"]]), esc(c["name"])))

    tour_hero = """<section class="container"><div class="tour-hero">
%s
<div>
<span class="tour-hero__cat">%s</span>
<h1>%s</h1>
<p class="tour-hero__intro">%s</p>
%s
<div class="tour-hero__cta">%s</div>
<div class="paybar">%s<span>%s</span></div>
</div>
</div></section>""" % (
        gallery_html(tour, lang), esc(CATEGORIES[lang][tour["category"]]), esc(c["name"]), esc(c["intro"]),
        priceblock, wa_link(lang, tr["book_whatsapp"], "btn btn--wa", "detail-hero", tour, book_open=True),
        ICON["wallet"], esc(tr["payment_line"]))

    sticky = """<aside>
<div class="panel sticky-book reveal">
%s
<div style="margin:16px 0">%s</div>
<div class="paybar">%s<span>%s</span></div>
%s
</div>
</aside>""" % (priceblock, wa_link(lang, tr["book_whatsapp"], "btn btn--wa btn--block", "detail-sticky", tour, book_open=True),
               ICON["shield"], esc(tr["payment_line"]), schedule_row)

    program_panel = ('<div class="panel reveal"><h2>%s</h2><ol class="program">%s</ol></div>' % (esc(tr["label_program"]), program)) if program else ""
    practical_panel = ('<div class="panel reveal"><h2>%s</h2><ul class="notelist">%s</ul></div>' % (esc(tr["label_practical"]), practical)) if practical else ""

    main_col = """<div>
<div class="panel reveal"><h2>%s</h2><ul class="ticklist">%s</ul></div>
%s
<div class="panel reveal"><h2>%s</h2><ul class="ticklist">%s</ul></div>
%s
<div class="panel reveal"><h2>%s</h2><ul class="notelist">%s</ul>%s</div>
%s
</div>""" % (
        esc(tr["label_experience"]), experience,
        program_panel,
        esc(tr["label_included"]), included,
        practical_panel,
        esc(tr["label_conditions"]), conditions, restricted_banner,
        addon_html)

    body_sec = '<section class="section"><div class="container"><div class="tour-body">%s%s</div></div></section>' % (main_col, sticky)

    desc = c["intro"]
    if len(desc) > 158:
        desc = desc[:155].rstrip() + "..."
    title = "%s - €%d%s" % (c["name"], tour["price"], tr["meta_title_suffix"])

    product = {
        "@type": "Product", "name": c["name"], "description": c["intro"],
        "brand": {"@type": "Brand", "name": cfg.BRAND_NAME},
        "image": [abs_url(u) for u in gallery_files(tour["id"])] or [abs_url("/assets/img/og-logo.png")],
        "offers": {"@type": "Offer", "price": tour["price"], "priceCurrency": "EUR",
                   "availability": "https://schema.org/InStock", "url": abs_url(canonical)},
    }
    jsonld = {"@context": "https://schema.org", "@graph": [product, sd_breadcrumb(lang, tour)]}

    body = (header(lang, alt_paths, public_tours) + '<main id="main" class="has-bookbar">' + breadcrumb + tour_hero + body_sec + related_html
            + "</main>" + footer(lang, public_tours) + lightbox_html(lang)
            + book_bar(lang, tour) + wa_tour_float(lang, tour)
            + booking_dialog(lang, public_tours) + booking_data_script(lang, public_tours, tour["id"]))
    doc = head(lang, title, desc, canonical, alt_paths, alt_paths["fr"], jsonld) + body + scripts()
    write(os.path.join(DIST, lang, PATH_TOURS[lang], tour["slug"], "index.html"), doc)

def lightbox_html(lang):
    tr = T[lang]
    return ("""<div class="lightbox" data-lightbox hidden aria-hidden="true" role="dialog" aria-modal="true">
<button class="lightbox__close" data-lbclose aria-label="%s">%s</button>
<button class="lightbox__nav lightbox__nav--prev" data-lbprev aria-label="%s">%s</button>
<img class="lightbox__img" data-lbimg src="" alt="">
<button class="lightbox__nav lightbox__nav--next" data-lbnext aria-label="%s">%s</button>
<span class="lightbox__counter" data-lbcounter></span>
</div>""" % (esca(tr["gallery_close"]), ICON["close"], esca(tr["gallery_prev"]),
             ICON["chevron"].replace('m6 9 6 6 6-6', 'm15 6-6 6 6 6'),
             esca(tr["gallery_next"]), ICON["chevron"].replace('m6 9 6 6 6-6', 'm9 6 6 6-6 6')))

# ---------------------------------------------------------------------------
# root splash + 404
# ---------------------------------------------------------------------------
def build_root(public_tours):
    # The root URL "/" serves the full French homepage immediately (no splash,
    # no JS redirect). It canonicalises to /fr/ so there is no duplicate content;
    # /pl/ and /ro/ stay the entry points for Polish/Romanian (e.g. Google Ads).
    build_home(cfg.DEFAULT_LANG, public_tours,
               out_path=os.path.join(DIST, "index.html"),
               canonical_path=url_home(cfg.DEFAULT_LANG),
               home_base="/")

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
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
</head>
<body>
<main class="splash"><div class="splash__card">
<img class="splash__logo" src="/assets/img/logo.png" alt="%s" width="200" height="200">
<h1>%s</h1><p>%s</p>
<div class="splash__langs"><a href="/%s/">%s</a></div>
</div></main>
</body></html>
""" % (lang, esc(tr["notfound_title"]), LOGO_ALT, esc(tr["notfound_title"]),
       esc(tr["notfound_text"]), lang, esc(tr["notfound_home"]))
    write(os.path.join(DIST, "404.html"), doc)

# ---------------------------------------------------------------------------
# sitemap + robots
# ---------------------------------------------------------------------------
def build_sitemap(public_tours):
    today = date.today().isoformat()
    urls = []

    def entry(path, alts):
        links = "".join('<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (HTML_LANG[l], abs_url(alts[l])) for l in LANG_ORDER)
        links += '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % abs_url("/")
        return '<url><loc>%s</loc><lastmod>%s</lastmod>%s</url>' % (abs_url(path), today, links)

    home_alts = {l: url_home(l) for l in LANG_ORDER}
    for l in LANG_ORDER:
        urls.append(entry(url_home(l), home_alts))
    for t in public_tours:
        alts = {l: url_tour(l, t["slug"]) for l in LANG_ORDER}
        for l in LANG_ORDER:
            urls.append(entry(url_tour(l, t["slug"]), alts))

    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n%s\n</urlset>\n' % "\n".join(urls))
    write(os.path.join(DIST, "sitemap.xml"), sm)

def build_robots():
    write(os.path.join(DIST, "robots.txt"), "User-agent: *\nAllow: /\n\nSitemap: %s\n" % abs_url("/sitemap.xml"))

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
    # GitHub Pages: serve files/dirs beginning with "_" and skip Jekyll processing.
    write(os.path.join(DIST, ".nojekyll"), "")
    # favicon.ico at site root (browsers request /favicon.ico by default)
    ico = os.path.join(SRC_ASSETS, "img", "favicon.ico")
    if os.path.isfile(ico):
        shutil.copyfile(ico, os.path.join(DIST, "favicon.ico"))

    public_tours = [t for t in TOURS if t["active"]
                    and (t["id"] != "lion-cub-photo" or cfg.LION_CUB_PUBLISHED)]

    for lang in LANG_ORDER:
        build_home(lang, public_tours)
        for t in public_tours:
            build_tour(lang, t, public_tours)

    build_root(public_tours)
    build_404()
    build_sitemap(public_tours)
    build_robots()

    by_cat = {}
    for t in public_tours:
        by_cat.setdefault(t["category"], []).append(t["id"])
    gal_total = sum(len(gallery_files(t["id"])) for t in TOURS)

    print("Build complete -> dist/")
    print("  site url         : %s" % cfg.SITE_URL)
    print("  languages        : %s" % ", ".join(LANG_ORDER))
    print("  tours in data    : %d | public: %d" % (len(TOURS), len(public_tours)))
    for cid in CATEGORY_ORDER:
        print("    %-16s %d tours" % (cid, len(by_cat.get(cid, []))))
    print("  gallery images   : %d (target 55)" % gal_total)
    print("  pages generated  : %d" % (1 + len(LANG_ORDER) + len(LANG_ORDER) * len(public_tours) + 1))
    print("  WhatsApp number  : %s" % (cfg.WHATSAPP_NUMBER or "NOT SET (launch blocker)"))
    print("  lion cub         : published=%s  ads_eligible=%s" % (cfg.LION_CUB_PUBLISHED, cfg.LION_CUB_ADS_ELIGIBLE))

if __name__ == "__main__":
    main()
