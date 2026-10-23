# -*- coding: utf-8 -*-
"""
Central site configuration for Hurghada KeRo Tours & Transfer.

Edit the values in this file, then rebuild with:  python3 build.py

Nothing in here is secret. Do NOT put API keys or passwords in the repo.
"""

# ---------------------------------------------------------------------------
# WHATSAPP  --  LAUNCH BLOCKER
# ---------------------------------------------------------------------------
# The booking buttons send customers to WhatsApp. Until a real number is set
# here the buttons render in a clearly "pending" (disabled) state so that we
# never publish a booking link that dials a wrong/guessed number.
#
# Format: full international number, digits only, NO "+", NO spaces, NO dashes.
# Example for an Egyptian number +20 100 123 4567  ->  "201001234567"
WHATSAPP_NUMBER = "201278378685"  # official KeRo Tours booking line (+20 127 837 8685)

# ---------------------------------------------------------------------------
# SITE / DEPLOYMENT
# ---------------------------------------------------------------------------
# Used for canonical URLs, hreflang and the sitemap. Change this if you move
# to a custom domain.
SITE_URL = "https://kero-tours-hurghada.pages.dev"

BRAND_NAME = "Hurghada KeRo Tours & Transfer"
BRAND_SHORT = "KeRo Tours"
OPERATING_BASE = "Hurghada, Egypt"

# ---------------------------------------------------------------------------
# BUSINESS INFORMATION  --  REQUIRES REAL OWNER INPUT
# ---------------------------------------------------------------------------
# Leave a value as "" to keep it hidden. Do NOT invent a licence number,
# company registration or address. These must be supplied by the operator.
BUSINESS = {
    "legal_name": "",        # registered company name, if any
    "address": "",           # full street address in Hurghada
    "license_number": "",    # tourism / travel licence number
    "email": "",             # public contact email
    "phone_display": "+20 127 837 8685",  # official KeRo Tours booking line (WhatsApp)
}

# ---------------------------------------------------------------------------
# ANALYTICS  --  leave empty until real IDs are provided
# ---------------------------------------------------------------------------
# No tag is injected while these are empty. No conversion event is ever fired
# on page load; a conversion is only counted on an actual WhatsApp click.
GA4_MEASUREMENT_ID = ""      # e.g. "G-XXXXXXXXXX"
GOOGLE_ADS_ID = ""           # e.g. "AW-XXXXXXXXXX"
GOOGLE_ADS_CONVERSION_LABEL = ""  # e.g. "abCDefGhIJ"  (for the WhatsApp-click conversion)

# ---------------------------------------------------------------------------
# COMPLIANCE FLAGS
# ---------------------------------------------------------------------------
# The lion cub photo experience involves direct interaction with a wild animal.
# The owner has asked for it to appear in the public catalog (Activities), with a
# factual disclaimer. It is NEVER eligible for Google Ads / paid landing paths
# until a local legal + animal-welfare + facility + ad-policy review is confirmed.
#
#   LION_CUB_PUBLISHED  -> show the tour + detail page in the public catalog.
#       Keep its URL OUT of Google Ads campaigns regardless of this flag.
#   SHOW_LION_ADDON     -> show the optional lion-cub add-on inside the safaris.
#       Kept False by default (same compliance caution).
LION_CUB_PUBLISHED = True
SHOW_LION_ADDON = False

# This tour must never be used as a Google Ads final URL / paid landing page
# until the compliance review is signed off. Build reports it as ads-excluded.
LION_CUB_ADS_ELIGIBLE = False

# Default language when a visitor hits the root "/" and we cannot detect one.
DEFAULT_LANG = "fr"
