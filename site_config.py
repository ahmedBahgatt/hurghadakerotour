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
WHATSAPP_NUMBER = ""  # <-- SET THIS BEFORE GOING LIVE

# ---------------------------------------------------------------------------
# SITE / DEPLOYMENT
# ---------------------------------------------------------------------------
# Used for canonical URLs, hreflang and the sitemap. Change this if you move
# to a custom domain.
SITE_URL = "https://kero-tours-landing.pages.dev"

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
    "phone_display": "",     # human-readable phone, e.g. "+20 100 123 4567"
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
# The lion cub photo experience (and the optional lion cub add-on on the
# safaris) involves direct interaction with a wild animal and requires legal,
# welfare and advertising-policy review BEFORE promotion. It stays in the
# source data either way; this flag only controls public visibility.
#
#   False  -> preserved in data, hidden from the public site and from ads.
#   True   -> shown publicly (only flip this AFTER a compliance/welfare review).
PROMOTE_LION_CUB = False

# Default language when a visitor hits the root "/" and we cannot detect one.
DEFAULT_LANG = "fr"
