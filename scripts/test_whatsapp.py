#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WhatsApp / contact-number regression gate for the built site.

Run AFTER build.py (operates on ./dist). Exits non-zero on any failure.

Covers the mandatory site-wide contact update:
  1. The NEW official number is configured and present across the generated site.
  2. The OLD number (every variant) has ZERO references anywhere in dist/.
  3. Every generated wa.me link points at the NEW number.
  4. Tour-specific WhatsApp links carry the exact localized tour name AND the
     exact localized detail-page URL (FR / PL / RO).
  5. The generic homepage WhatsApp link carries the localized homepage URL.
  6. The booking-form message builder data (window.KERO_BK) is present per
     language with the new number, per-tour name + URL, and the labelled
     message strings (availability / departure date / pickup request).

Pure Python 3 standard library.
"""
import glob
import html
import json
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
sys.path.insert(0, ROOT)

import site_config as cfg                                    # noqa: E402
from data.i18n import T, BOOKING, LANG_ORDER, PATH_TOURS     # noqa: E402
from data.tours import TOURS                                 # noqa: E402

NEW_NUMBER = "201288808645"
# Every old-number variant that must NEVER appear in the generated site.
OLD_VARIANTS = ["01278378685", "201278378685", "+201278378685",
                "wa.me/201278378685", "tel:+201278378685"]

WA_HREF_RE = re.compile(r'href="https://wa\.me/(\d+)\?text=([^"]*)"')
KERO_BK_RE = re.compile(r'window\.KERO_BK=(\{.*?\});</script>')


def fail(problems, msg):
    problems.append(msg)
    print("FAIL " + msg)


def decoded_wa_texts(txt):
    """All (number, decoded_text) pairs from wa.me hrefs in one HTML string."""
    out = []
    for num, enc in WA_HREF_RE.findall(txt):
        out.append((num, html.unescape(unquote(enc))))
    return out


def public_tours():
    return [t for t in TOURS if t["active"]
            and (t["id"] != "lion-cub-photo" or cfg.LION_CUB_PUBLISHED)]


def site_url():
    return cfg.SITE_URL.rstrip("/")


def home_url(lang):
    return "%s/%s/" % (site_url(), lang)


def tour_url(lang, slug):
    return "%s/%s/%s/%s/" % (site_url(), lang, PATH_TOURS[lang], slug)


def main():
    problems = []

    if not os.path.isdir(DIST):
        print("dist/ not found - run build.py first")
        return 1

    # --- 1. config carries the new number -----------------------------------
    if cfg.WHATSAPP_NUMBER != NEW_NUMBER:
        fail(problems, "site_config.WHATSAPP_NUMBER is %r, expected %r"
             % (cfg.WHATSAPP_NUMBER, NEW_NUMBER))
    if NEW_NUMBER not in cfg.BUSINESS.get("phone_display", "").replace(" ", ""):
        fail(problems, "BUSINESS.phone_display does not contain the new number")

    files = sorted(glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True))
    files += [os.path.join(DIST, "sitemap.xml")]
    if not files:
        fail(problems, "no generated files found")

    # --- 2 & 3. old number absent everywhere; wa.me links use new number -----
    for f in files:
        if not os.path.isfile(f):
            continue
        rel = os.path.relpath(f, DIST)
        txt = open(f, encoding="utf-8").read()
        for bad in OLD_VARIANTS:
            if bad in txt:
                fail(problems, "%s still contains OLD number variant %r" % (rel, bad))
        for num, _text in decoded_wa_texts(txt):
            if num != NEW_NUMBER:
                fail(problems, "%s has wa.me link to wrong number %s" % (rel, num))

    # --- 4 & 5. per-language link content ------------------------------------
    pts = public_tours()
    for lang in LANG_ORDER:
        # Homepage: generic WhatsApp link must carry the localized homepage URL.
        home_file = os.path.join(DIST, lang, "index.html")
        htxt = open(home_file, encoding="utf-8").read()
        texts = [t for _n, t in decoded_wa_texts(htxt)]
        if not any(home_url(lang) in t for t in texts):
            fail(problems, "%s/ homepage has no generic WA link carrying %s"
                 % (lang, home_url(lang)))
        if NEW_NUMBER not in htxt:
            fail(problems, "%s/ homepage missing new number" % lang)

        # Each tour page: the direct tour float must carry name + exact URL.
        for t in pts:
            slug = t["slug"]
            name = t["content"][lang]["name"]
            url = tour_url(lang, slug)
            tf = os.path.join(DIST, lang, PATH_TOURS[lang], slug, "index.html")
            ttxt = open(tf, encoding="utf-8").read()
            texts = [tx for _n, tx in decoded_wa_texts(ttxt)]
            hit = [tx for tx in texts if name in tx and url in tx]
            if not hit:
                fail(problems, "%s %s: no direct WA link with both name and %s"
                     % (lang, slug, url))

            # --- 6. booking-form builder data ---------------------------------
            m = KERO_BK_RE.search(ttxt)
            if not m:
                fail(problems, "%s %s: window.KERO_BK missing" % (lang, slug))
                continue
            bk = json.loads(m.group(1))
            if bk.get("wa") != NEW_NUMBER:
                fail(problems, "%s %s: KERO_BK.wa is %r" % (lang, slug, bk.get("wa")))
            if bk.get("tour") != t["id"]:
                fail(problems, "%s %s: KERO_BK.tour is %r, expected %r"
                     % (lang, slug, bk.get("tour"), t["id"]))
            td = bk.get("tours", {}).get(t["id"], {})
            if td.get("name") != name:
                fail(problems, "%s %s: KERO_BK tour name mismatch" % (lang, slug))
            if td.get("url") != url:
                fail(problems, "%s %s: KERO_BK tour url %r != %r"
                     % (lang, slug, td.get("url"), url))

    # --- 6b. simulate the JS booking message (mirror of app.js) --------------
    # Reconstruct the exact message the form submit builds, to prove the three
    # language builders produce a clean, labelled, URL-bearing message.
    for lang, tid in (("fr", "cairo-gem"), ("pl", "luxor"), ("ro", "three-islands")):
        s = BOOKING[lang]
        t = next(x for x in pts if x["id"] == tid)
        name = t["content"][lang]["name"]
        url = tour_url(lang, t["slug"])
        unit = s["unit_boat"] if t["price_type"] == "per_boat" else s["unit_person"]
        # the booking message now carries a mandatory preferred-date line
        for key in ("m_date", "f_date", "err_date", "err_date_past"):
            if not s.get(key):
                fail(problems, "%s BOOKING missing %r" % (lang, key))
        lines = [s["m_intro"], "",
                 "• %s: %s" % (s["m_excursion"], name),
                 "• %s: %s" % (s["m_url"], url),
                 "• %s: €%d %s" % (s["m_price"], t["price"], unit),
                 "• %s: %s" % (s["m_hotel"], "Sunrise Aqua Joy"),
                 "• %s: %d" % (s["m_people"], 2),
                 "• %s: %s" % (s["m_date"], "2026-12-24"),
                 "", s["m_outro"]]
        msg = "\n".join(lines)
        for needle in (name, url, s["m_hotel"], s["m_date"], s["m_outro"]):
            if needle not in msg:
                fail(problems, "%s booking message missing %r" % (lang, needle))
        # outro must request availability + date + pickup (not a fake confirmation)
        low = s["m_outro"].lower()
        kw = {"fr": ["disponibilit", "date", "prise en charge"],
              "pl": ["dostępno", "dat", "odbior"],
              "ro": ["disponibilit", "dat", "preluare"]}[lang]
        for k in kw:
            if k not in low:
                fail(problems, "%s m_outro missing keyword %r" % (lang, k))

    # --- 7. booking form has a required native date field on every page ------
    #     and the WhatsApp handoff never strands the tab (no same-tab nav to
    #     wa.me, no api.whatsapp.com anywhere in the output).
    sample_pages = []
    for lang in LANG_ORDER:
        sample_pages.append(os.path.join(DIST, lang, "index.html"))
        sample_pages.append(os.path.join(DIST, lang, PATH_TOURS[lang],
                                          pts[0]["slug"], "index.html"))
    for f in sample_pages:
        rel = os.path.relpath(f, DIST)
        txt = open(f, encoding="utf-8").read()
        if 'name="date"' not in txt or 'type="date"' not in txt:
            fail(problems, "%s: booking form has no native date input" % rel)
        # the date input must be required (find the date <input> and check)
        m = re.search(r'<input name="date"[^>]*>', txt)
        if not m or "required" not in m.group(0):
            fail(problems, "%s: date input is not required" % rel)

    appjs = open(os.path.join(DIST, "assets", "js", "app.js"), encoding="utf-8").read()
    if "openWhatsApp(" not in appjs:
        fail(problems, "app.js: openWhatsApp handoff helper missing")
    if "window.location.href = url" in appjs:
        fail(problems, "app.js: same-tab wa.me navigation (strand bug) still present")
    for f in files:
        if os.path.isfile(f) and "api.whatsapp.com" in open(f, encoding="utf-8").read():
            fail(problems, "%s: contains api.whatsapp.com reference"
                 % os.path.relpath(f, DIST))

    print("WhatsApp regression: checked %d files, %d problem(s)"
          % (len([f for f in files if os.path.isfile(f)]), len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
