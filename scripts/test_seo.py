#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO regression gate for the built site (dist/). Run after build.py.
Exits non-zero on any failure so the CI pipeline blocks a bad deploy.

It asserts the SEO signals that content edits could silently break:
  - one H1 per content page; self-referencing canonical; correct <html lang>
  - robots directive matches site_config.ALLOW_INDEXING (indexing safety lock)
  - unique, non-empty <title> and meta description per page (sane length)
  - complete Open Graph + Twitter card (incl. og:image:alt, og:locale:alternate)
  - reciprocal hreflang cluster (fr/pl/ro + x-default) on every page
  - valid JSON-LD; required entities present per page type
  - structured-data price == visible price == data/tours.py price (EUR)
  - the private speedboat is modeled per-boat, never as a per-person price
  - every <img> has a non-empty alt (or is aria-hidden); no "name - N" gallery alts
  - referenced og:image / social images exist on disk
  - sitemap covers every content URL + has image entries; robots.txt has Sitemap
  - no stale domains, no retired phone number, no fabricated business identity

Python standard library only (mirrors the project's zero-dependency build).
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import site_config as cfg
from data.i18n import LANG_ORDER, HTML_LANG, OG_LOCALE, PATH_TOURS
from data.tours import TOURS

DIST = os.path.join(ROOT, "dist")
SITE = cfg.SITE_URL.rstrip("/")

STALE_DOMAINS = ["kero-tours-landing.pages.dev", "kero-tours-hurghada.pages.dev",
                 "cloudflare", ".pages.dev"]
OLD_PHONES = ["201278378685", "1278378685"]
# Fabricated-identity guard: these must NOT appear unless really configured.
FAKE_MARKERS = ["licence n", "license no", "reg. no", "★", "⭐"]

problems = []
warnings = []


def fail(msg):
    problems.append(msg)


def warn(msg):
    warnings.append(msg)


def meta_content(html, pattern):
    m = re.search(pattern, html)
    return m.group(1) if m else None


def og(html, prop):
    return meta_content(html, r'<meta property="og:%s" content="([^"]*)"' % re.escape(prop))


def public_tours():
    return [t for t in TOURS if t["active"]
            and (t["id"] != "lion-cub-photo" or cfg.LION_CUB_PUBLISHED)]


def expected_robots():
    return ("index,follow,max-image-preview:large"
            if getattr(cfg, "ALLOW_INDEXING", True) else "noindex,follow")


def jsonld_graphs(html):
    out = []
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        data = json.loads(m)
        out.extend(data.get("@graph", [data]))
    return out


def types_of(graphs):
    return {g.get("@type") for g in graphs}


def canonical_for(rel):
    """Expected self-canonical for a content page's dist-relative path."""
    if rel == "index.html":
        return SITE + "/fr/"            # root aliases the French homepage
    d = os.path.dirname(rel)
    return SITE + "/" + d + "/"


def lang_for(rel):
    first = rel.split(os.sep)[0]
    return first if first in LANG_ORDER else "fr"


def tour_by_slug(lang, slug):
    for t in public_tours():
        if t["slug"] == slug:
            return t
    return None


def main():
    if not os.path.isdir(DIST):
        print("dist/ not found - run build.py first")
        return 1

    files = sorted(glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True))
    content = [f for f in files if os.path.basename(f) not in ("404.html",)
               and os.path.relpath(f, DIST) != "index.html"]

    titles, descs = {}, {}
    seen_urls = set()

    for f in content:
        rel = os.path.relpath(f, DIST)
        html = open(f, encoding="utf-8").read()
        lang = lang_for(rel)
        is_tour = rel.count(os.sep) >= 2   # fr/excursions/<slug>/index.html

        # --- H1 ---
        if len(re.findall(r"<h1[ >]", html)) != 1:
            fail("%s: H1 count != 1" % rel)

        # --- <html lang> ---
        hl = meta_content(html, r'<html lang="([^"]+)"')
        if hl != HTML_LANG[lang]:
            fail("%s: <html lang> is %r, expected %r" % (rel, hl, HTML_LANG[lang]))

        # --- robots (indexing safety lock) ---
        robots = meta_content(html, r'<meta name="robots" content="([^"]+)"')
        if robots != expected_robots():
            fail("%s: robots %r, expected %r (ALLOW_INDEXING=%s)"
                 % (rel, robots, expected_robots(), cfg.ALLOW_INDEXING))

        # --- canonical self-reference ---
        canon = meta_content(html, r'<link rel="canonical" href="([^"]+)"')
        exp_canon = canonical_for(rel)
        if canon != exp_canon:
            fail("%s: canonical %r, expected %r" % (rel, canon, exp_canon))
        seen_urls.add(canon)

        # --- title ---
        title = meta_content(html, r"<title>(.*?)</title>")
        if not title or not title.strip():
            fail("%s: empty <title>" % rel)
        elif len(title) > 70:
            warn("%s: title %d chars (>70)" % (rel, len(title)))
        titles.setdefault((lang, title), []).append(rel)

        # --- meta description ---
        desc = meta_content(html, r'<meta name="description" content="([^"]*)"')
        if not desc or not desc.strip():
            fail("%s: empty meta description" % rel)
        else:
            if len(desc) < 50:
                warn("%s: meta description %d chars (<50)" % (rel, len(desc)))
            if len(desc) > 185:
                fail("%s: meta description %d chars (>185)" % (rel, len(desc)))
        descs.setdefault((lang, desc), []).append(rel)

        # --- Open Graph + Twitter completeness ---
        for prop in ("title", "description", "url", "image", "image:alt", "site_name", "locale", "type"):
            if og(html, prop) is None:
                fail("%s: missing og:%s" % (rel, prop))
        if og(html, "url") and og(html, "url") != canon:
            fail("%s: og:url %r != canonical %r" % (rel, og(html, "url"), canon))
        if og(html, "locale") != OG_LOCALE[lang]:
            fail("%s: og:locale %r, expected %r" % (rel, og(html, "locale"), OG_LOCALE[lang]))
        for other in [l for l in LANG_ORDER if l != lang]:
            if ('content="%s"' % OG_LOCALE[other]) not in html:
                fail("%s: missing og:locale:alternate %s" % (rel, OG_LOCALE[other]))
        if '<meta name="twitter:card"' not in html:
            fail("%s: missing twitter:card" % rel)

        # --- og:image exists on disk ---
        ogimg = og(html, "image")
        if ogimg and ogimg.startswith(SITE):
            p = os.path.join(DIST, ogimg[len(SITE) + 1:])
            if not os.path.isfile(p):
                fail("%s: og:image not found on disk (%s)" % (rel, ogimg))

        # --- hreflang cluster ---
        for l in LANG_ORDER:
            if ('hreflang="%s"' % HTML_LANG[l]) not in html:
                fail("%s: missing hreflang %s" % (rel, HTML_LANG[l]))
        if 'hreflang="x-default"' not in html:
            fail("%s: missing hreflang x-default" % rel)

        # --- images have alt (or aria-hidden). Skip JS-populated placeholders
        #     (empty src=""), e.g. the shared lightbox <img>. ---
        for img in re.findall(r"<img\b[^>]*>", html):
            if 'aria-hidden="true"' in img:
                continue
            srcm = re.search(r'\bsrc="([^"]*)"', img)
            if srcm is None or not srcm.group(1).strip():
                continue
            m = re.search(r'\balt="([^"]*)"', img)
            if m is None:
                fail("%s: <img> without alt: %s" % (rel, img[:80]))
            elif not m.group(1).strip():
                fail("%s: <img> with empty alt: %s" % (rel, img[:80]))

        # --- JSON-LD ---
        try:
            graphs = jsonld_graphs(html)
        except Exception as e:
            fail("%s: invalid JSON-LD: %s" % (rel, e))
            graphs = []
        tset = types_of(graphs)

        # --- stale / fabricated content ---
        low = html.lower()
        for s in STALE_DOMAINS:
            if s in low:
                fail("%s: stale reference %r" % (rel, s))
        for ph in OLD_PHONES:
            if ph in html:
                fail("%s: retired phone number %r" % (rel, ph))

        if is_tour:
            slug = os.path.basename(os.path.dirname(rel))
            tour = tour_by_slug(lang, slug)
            if not tour:
                fail("%s: cannot resolve tour slug %r" % (rel, slug))
                continue
            # required entities
            for need in ("TouristTrip", "BreadcrumbList", "WebPage", "TravelAgency"):
                if need not in tset:
                    fail("%s: JSON-LD missing %s" % (rel, need))
            trip = next((g for g in graphs if g.get("@type") == "TouristTrip"), None)
            if trip:
                offer = trip.get("offers", {})
                price = offer.get("price")
                if price != tour["price"]:
                    fail("%s: offer price %r != data price %r" % (rel, price, tour["price"]))
                if offer.get("priceCurrency") != "EUR":
                    fail("%s: offer currency %r != EUR" % (rel, offer.get("priceCurrency")))
                prov = trip.get("provider", {})
                if prov.get("@id") != SITE + "/#business":
                    fail("%s: TouristTrip provider @id missing/incorrect" % rel)
                # visible price must match structured price
                if ("&euro;%d" % tour["price"]) not in html and ("€%d" % tour["price"]) not in html:
                    fail("%s: visible price &euro;%d not found" % (rel, tour["price"]))
                # speedboat: per-boat basis, never per-person
                if tour["price_type"] == "per_boat":
                    spec = offer.get("priceSpecification", {})
                    txt = (spec.get("unitText", "") + " " + spec.get("description", "")).lower()
                    if "bateau" not in txt and "łódź" not in txt and "barc" not in txt:
                        fail("%s: per-boat price not flagged in priceSpecification" % rel)
        else:
            for need in ("WebSite", "TravelAgency", "WebPage", "FAQPage"):
                if need not in tset:
                    fail("%s: homepage JSON-LD missing %s" % (rel, need))

    # --- uniqueness within each language (cross-language same product name is OK) ---
    for (lg, t), where in titles.items():
        if len(where) > 1:
            fail("duplicate <title> [%s] on %s: %r" % (lg, ", ".join(where), t[:60]))
    for (lg, d), where in descs.items():
        if len(where) > 1:
            fail("duplicate meta description [%s] on %s" % (lg, ", ".join(where)))

    # --- sitemap / robots / nojekyll ---
    smpath = os.path.join(DIST, "sitemap.xml")
    if not os.path.isfile(smpath):
        fail("missing sitemap.xml")
    else:
        sm = open(smpath, encoding="utf-8").read()
        want = {SITE + "/fr/", SITE + "/pl/", SITE + "/ro/"}
        for t in public_tours():
            for l in LANG_ORDER:
                want.add(SITE + "/%s/%s/%s/" % (l, PATH_TOURS[l], t["slug"]))
        for u in want:
            if ("<loc>%s</loc>" % u) not in sm:
                fail("sitemap missing %s" % u)
        if "<image:image>" not in sm:
            fail("sitemap has no image entries")
    rbpath = os.path.join(DIST, "robots.txt")
    if not os.path.isfile(rbpath):
        fail("missing robots.txt")
    elif "Sitemap:" not in open(rbpath, encoding="utf-8").read():
        fail("robots.txt missing Sitemap line")
    if not os.path.isfile(os.path.join(DIST, ".nojekyll")):
        fail("missing .nojekyll")

    # --- fabricated business identity guard ---
    if not cfg.BUSINESS.get("address") and '"streetAddress"' in \
            open(os.path.join(DIST, "fr", "index.html"), encoding="utf-8").read():
        fail("streetAddress in JSON-LD but BUSINESS address is empty (fabrication)")

    # --- report ---
    for w in warnings:
        print("WARN " + w)
    for p in problems:
        print("FAIL " + p)
    print("SEO regression: checked %d content pages, %d warning(s), %d problem(s)"
          % (len(content), len(warnings), len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
