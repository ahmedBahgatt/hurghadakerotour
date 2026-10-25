#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CI quality gate for the built site. Run after build.py; exits non-zero on failure.
Checks: HTML well-formedness, one H1 per content page, canonical present,
no stale-domain references, and valid JSON-LD.
"""
import glob
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr"}
STALE = ["kero-tours-landing.pages.dev", "kero-tours-hurghada.pages.dev"]


class V(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.err = []

    def handle_starttag(self, t, a):
        if t not in VOID:
            self.stack.append(t)

    def handle_endtag(self, t):
        if t in VOID:
            return
        if self.stack and self.stack[-1] == t:
            self.stack.pop()
        elif t in self.stack:
            while self.stack and self.stack.pop() != t:
                pass
        else:
            self.err.append("stray </%s>" % t)


def main():
    if not os.path.isdir(DIST):
        print("dist/ not found - run build.py first")
        return 1
    files = sorted(glob.glob(os.path.join(DIST, "**", "*.html"), recursive=True))
    if not files:
        print("no HTML output")
        return 1
    problems = 0
    for f in files:
        rel = os.path.relpath(f, DIST)
        txt = open(f, encoding="utf-8").read()
        p = V()
        p.feed(txt)
        if p.stack:
            problems += 1
            print("FAIL %s unclosed: %s" % (rel, ",".join(p.stack[:5])))
        if p.err:
            problems += 1
            print("FAIL %s %s" % (rel, ";".join(p.err[:3])))
        is_content = rel not in ("404.html", "index.html")
        if is_content:
            if len(re.findall(r"<h1[ >]", txt)) != 1:
                problems += 1
                print("FAIL %s h1 count != 1" % rel)
            if 'rel="canonical"' not in txt:
                problems += 1
                print("FAIL %s missing canonical" % rel)
        for s in STALE:
            if s in txt:
                problems += 1
                print("FAIL %s stale domain %s" % (rel, s))
        for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', txt, re.S):
            try:
                json.loads(m)
            except Exception as e:
                problems += 1
                print("FAIL %s invalid JSON-LD: %s" % (rel, e))
    for extra in ("sitemap.xml", "robots.txt", ".nojekyll"):
        if not os.path.isfile(os.path.join(DIST, extra)):
            problems += 1
            print("FAIL missing %s" % extra)
    print("checked %d HTML files, %d problem(s)" % (len(files), problems))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
