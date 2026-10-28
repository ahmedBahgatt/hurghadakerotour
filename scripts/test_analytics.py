#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Ads tag + WhatsApp-conversion regression gate for the built site (dist/).
Run after build.py; exits non-zero on any failure so CI blocks a bad deploy.

It locks the analytics contract the owner authorized (2026-10-26):
  - exactly ONE global gtag.js install per content page, async (non-blocking),
    id = the real Google Ads tag AW-18538088460; no duplicate tracking tags
  - gtag('config','AW-18538088460') once; KERO_ADS_CONVERSION points at the one
    real conversion AW-18538088460/HOYlCNeOq6odEIyQ04dF
  - NO GA4 (no G-XXXX), NO GTM container (no gtm.js / GTM-XXXX)
  - Consent Mode v2 defaults set BEFORE config, denied in the EEA/UK/CH
  - the 404 page carries no tag and stays noindex (one global tag PER PAGE)
  - the meta CSP actually ALLOWS the Google Ads endpoints, so the conversion
    beacon cannot be silently blocked
  - app.js fires exactly ONE conversion per deliberate WhatsApp handoff
    (direct [data-wa] click OR validated booking-form submit), never on a
    form-open ([data-book-open] is skipped), never with personal data in the
    payload, and never blocks/redirects the WhatsApp navigation (no
    `window.location = url`, no event_callback gating the handoff)

Python standard library only (mirrors the zero-dependency build).
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import site_config as cfg  # noqa: E402

DIST = os.path.join(ROOT, "dist")

ADS_ID = "AW-18538088460"
CONV = "AW-18538088460/HOYlCNeOq6odEIyQ04dF"
CLARITY_ID = "z4klch73ka"
# Official Clarity bootstrap invocation - exact spacing matters (verbatim snippet).
CLARITY_SIG = '(window, document, "clarity", "script", "%s")' % CLARITY_ID

problems = []


def fail(msg):
    problems.append(msg)
    print("FAIL " + msg)


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    if not os.path.isdir(DIST):
        print("dist/ not found - run build.py first")
        return 1

    # ---- config is the single source of truth -----------------------------
    if cfg.GOOGLE_ADS_ID.strip() != ADS_ID:
        fail("site_config.GOOGLE_ADS_ID is %r, expected %r" % (cfg.GOOGLE_ADS_ID, ADS_ID))
    if cfg.GOOGLE_ADS_CONVERSION_LABEL.strip() != "HOYlCNeOq6odEIyQ04dF":
        fail("site_config.GOOGLE_ADS_CONVERSION_LABEL is %r" % cfg.GOOGLE_ADS_CONVERSION_LABEL)
    if cfg.GA4_MEASUREMENT_ID.strip():
        fail("GA4 must stay empty (no GA4), got %r" % cfg.GA4_MEASUREMENT_ID)
    if getattr(cfg, "CLARITY_PROJECT_ID", "").strip() != CLARITY_ID:
        fail("site_config.CLARITY_PROJECT_ID is %r, expected %r"
             % (getattr(cfg, "CLARITY_PROJECT_ID", None), CLARITY_ID))

    html_files = sorted(glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True))
    if not html_files:
        print("no HTML output")
        return 1

    content_pages = 0
    for path in html_files:
        rel = os.path.relpath(path, DIST)
        html = read(path)
        is_404 = rel == "404.html"

        tag_loads = len(re.findall(r'googletagmanager\.com/gtag/js\?id=', html))
        configs = len(re.findall(r"gtag\('config','AW-18538088460'\)", html))

        clarity_installs = html.count(CLARITY_SIG)

        if is_404:
            # one global tag PER PAGE: the 404 is not a content/landing page and
            # must stay noindex with no tracking tag (gtag OR Clarity).
            if tag_loads:
                fail("404.html unexpectedly carries a gtag.js load")
            if clarity_installs:
                fail("404.html unexpectedly carries a Clarity install")
            if 'content="noindex"' not in html:
                fail("404.html is not noindex")
            continue

        content_pages += 1

        # exactly one Microsoft Clarity install per content page, async, real id
        if clarity_installs != 1:
            fail("%s: expected exactly 1 Clarity install, found %d" % (rel, clarity_installs))
        if 'src="https://www.clarity.ms/tag/"+i' not in html:
            fail("%s: Clarity async tag src missing/altered" % rel)
        if "t.async=1" not in html:
            fail("%s: Clarity loader is not async (t.async=1 missing)" % rel)
        # Clarity must come AFTER the gtag Consent Mode default so its native GCM
        # integration reads analytics_storage (no second consent surface).
        if clarity_installs == 1 and "gtag('consent','default'" in html:
            if html.index(CLARITY_SIG) < html.index("gtag('consent','default'"):
                fail("%s: Clarity loads before the gtag consent default "
                     "(GCM signal not yet set)" % rel)

        # exactly one global tag, loaded async (non-blocking)
        if tag_loads != 1:
            fail("%s: expected exactly 1 gtag.js load, found %d" % (rel, tag_loads))
        if ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s">' % ADS_ID) not in html:
            fail("%s: async gtag.js load for %s missing/altered" % (rel, ADS_ID))
        if configs != 1:
            fail("%s: expected exactly 1 gtag config for the Ads id, found %d" % (rel, configs))
        if ("window.KERO_ADS_CONVERSION='%s'" % CONV) not in html:
            fail("%s: KERO_ADS_CONVERSION is not the real conversion %s" % (rel, CONV))

        # no GA4 / no GTM container anywhere
        if re.search(r"gtag/js\?id=G-|'config','G-", html):
            fail("%s: a GA4 (G-) tag is present - must be none" % rel)
        if re.search(r"gtm\.js|GTM-[A-Z0-9]", html):
            fail("%s: a GTM container is present - must be none" % rel)

        # Consent Mode v2 set before config, denied in the EEA (spot-check FR/DE)
        if "gtag('consent','default'" not in html:
            fail("%s: Consent Mode default missing" % rel)
        else:
            denied = re.search(r"'ad_storage':'denied'.*?'region':\[([^\]]*)\]", html)
            if not denied or '"FR"' not in denied.group(1) or '"DE"' not in denied.group(1):
                fail("%s: EEA consent-denied region list missing FR/DE" % rel)
            ci = html.index("gtag('consent','default'")
            cci = html.index("gtag('config','%s')" % ADS_ID)
            if ci > cci:
                fail("%s: consent default must precede config" % rel)

        # the meta CSP must ALLOW the Ads endpoints PER DIRECTIVE, aligned with
        # Google's official CSP guidance (Tag Assistant flags missing hosts even
        # when requests currently succeed).
        csp = re.search(r'Content-Security-Policy" content="([^"]+)"', html)
        if not csp:
            fail("%s: no CSP meta" % rel)
        else:
            directives = {}
            for part in csp.group(1).split(";"):
                toks = part.split()
                if toks:
                    directives[toks[0].strip()] = set(toks[1:])
            required = {
                # the "blocking Google scripts" fix: Ads conversion-linker script host
                "script-src": ["https://www.googletagmanager.com",
                               "https://www.googleadservices.com",
                               "https://googleads.g.doubleclick.net",
                               "https://www.google.com"],
                # Tag Assistant debug channel + gtag beacons/frames
                "frame-src": ["https://www.googletagmanager.com"],
                "connect-src": ["https://www.googletagmanager.com",
                                "https://www.googleadservices.com",
                                "https://googleads.g.doubleclick.net",
                                "https://ad.doubleclick.net",
                                "https://www.google.com"],
                "img-src": ["https://www.googletagmanager.com",
                            "https://www.googleadservices.com",
                            "https://googleads.g.doubleclick.net",
                            "https://pagead2.googlesyndication.com",
                            "https://www.google.com"],
            }
            for directive, hosts in required.items():
                have = directives.get(directive, set())
                for h in hosts:
                    if h not in have:
                        fail("%s: CSP %s missing %s" % (rel, directive, h))
            # the visitor's local Google ccTLD must be allowed for the 1p pings
            for directive in ("img-src", "connect-src"):
                if "https://www.google.com.eg" not in directives.get(directive, set()):
                    fail("%s: CSP %s missing a regional Google ccTLD "
                         "(e.g. www.google.com.eg)" % (rel, directive))
            # Microsoft Clarity: enumerated hosts (no wildcard). The tag host and
            # the a..z env shards on script/connect/img; c.bing.com (MUID sync)
            # on connect/img.
            for directive in ("script-src", "connect-src", "img-src"):
                have = directives.get(directive, set())
                for h in ("https://www.clarity.ms", "https://a.clarity.ms",
                          "https://z.clarity.ms"):
                    if h not in have:
                        fail("%s: CSP %s missing Clarity host %s" % (rel, directive, h))
            for directive in ("connect-src", "img-src"):
                if "https://c.bing.com" not in directives.get(directive, set()):
                    fail("%s: CSP %s missing https://c.bing.com (Clarity MUID sync)"
                         % (rel, directive))
            # never widen with wildcards or unsafe-eval
            if "'unsafe-eval'" in csp.group(1) or "*" in csp.group(1):
                fail("%s: CSP uses unsafe-eval or a wildcard" % rel)

    print("checked %d content pages for the Ads tag" % content_pages)

    # ---- app.js: firing logic (single conversion, no PII, non-blocking) ----
    appjs_path = os.path.join(DIST, "assets", "js", "app.js")
    if not os.path.isfile(appjs_path):
        fail("dist/assets/js/app.js missing")
    else:
        js = read(appjs_path)

        # exactly two conversion send sites: direct [data-wa] click + form submit
        conv_sends = re.findall(r'gtag\("event",\s*"conversion",\s*\{\s*send_to:\s*conv\s*\}\)', js)
        if len(conv_sends) != 2:
            fail("app.js: expected exactly 2 conversion send sites (direct click + "
                 "form submit), found %d" % len(conv_sends))
        if "window.KERO_ADS_CONVERSION" not in js:
            fail("app.js: conversion does not read window.KERO_ADS_CONVERSION")

        # opening the booking form must NOT count as a conversion
        if 'hasAttribute("data-book-open")) return' not in js:
            fail("app.js: [data-wa] handler no longer skips [data-book-open] "
                 "(would double-count form opens)")

        # invalid form submits must bail before the conversion: validation errors
        for key in ("err_hotel", "err_people", "err_date"):
            if key not in js:
                fail("app.js: booking validation key %s missing (invalid submits "
                     "could fire a conversion)" % key)

        # no personal data in any gtag payload (hotel/room/notes/date value/URL/text)
        for m in re.finditer(r'gtag\("event"[^;]*?\{[^}]*\}', js):
            blob = m.group(0)
            for bad in ("hotel", "room", "notes", "wa.me", "encodeURIComponent",
                        "\"text\"", "message", ".value"):
                if bad in blob:
                    fail("app.js: gtag payload may leak personal data (%r): %s"
                         % (bad, blob[:80]))

        # WhatsApp navigation preserved: no same-tab redirect, no callback gating
        if re.search(r"window\.location(\.href)?\s*=\s*url", js):
            fail("app.js: same-tab WhatsApp redirect (window.location = url) present")
        if "openWhatsApp" not in js or 'target = "_blank"' not in js or 'rel = "noopener"' not in js:
            fail("app.js: openWhatsApp new-tab handoff (target=_blank/rel=noopener) altered")
        if "event_callback" in js:
            fail("app.js: event_callback present - conversion must not gate the "
                 "WhatsApp handoff (non-blocking)")

    print("analytics regression: %d problem(s)" % len(problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
