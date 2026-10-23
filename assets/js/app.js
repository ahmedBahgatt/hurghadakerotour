/* =========================================================================
   KeRo Tours - progressive enhancement
   The site is fully functional without JS; this adds nav, filters,
   scroll reveal, WhatsApp link wiring and optional analytics events.
   ========================================================================= */
(function () {
  "use strict";

  /* ---- Mobile navigation toggle ---- */
  var nav = document.querySelector("[data-nav]");
  var toggle = document.querySelector("[data-nav-toggle]");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", open ? "false" : "true");
      toggle.setAttribute("aria-expanded", open ? "false" : "true");
    });
    // close menu when a link is tapped
    document.querySelectorAll(".mobile-menu a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Category filters ---- */
  var filters = document.querySelectorAll("[data-filter]");
  var cards = document.querySelectorAll("[data-tour-card]");
  if (filters.length) {
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.getAttribute("data-filter");
        filters.forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
        btn.setAttribute("aria-pressed", "true");
        cards.forEach(function (card) {
          var show = cat === "all" || card.getAttribute("data-category") === cat;
          card.classList.toggle("is-hidden", !show);
        });
      });
    });
  }

  /* ---- WhatsApp link wiring ----
     Builds wa.me links from the runtime number + each button's prefilled
     text. Falls back to the href baked at build time. If no number is
     available, the button is marked pending (disabled) so we never publish
     an invalid booking link. */
  var runtimeNum = (window.KERO_WHATSAPP || "").replace(/[^0-9]/g, "");
  document.querySelectorAll("[data-wa]").forEach(function (el) {
    var text = el.getAttribute("data-wa-text") || "";
    var baked = el.getAttribute("data-wa-href") || "";
    var href = "";
    if (runtimeNum) {
      href = "https://wa.me/" + runtimeNum + (text ? "?text=" + encodeURIComponent(text) : "");
    } else if (baked) {
      href = baked;
    }
    if (href) {
      el.setAttribute("href", href);
      el.setAttribute("target", "_blank");
      el.setAttribute("rel", "noopener");
      el.classList.remove("is-pending");
      el.removeAttribute("aria-disabled");
    } else {
      el.setAttribute("href", "#");
      el.classList.add("is-pending");
      el.setAttribute("aria-disabled", "true");
    }
  });

  /* ---- Click handling: block pending buttons, fire analytics event ---- */
  document.addEventListener("click", function (e) {
    var el = e.target.closest ? e.target.closest("[data-wa]") : null;
    if (!el) return;
    if (el.classList.contains("is-pending")) {
      e.preventDefault();
      return;
    }
    // Optional analytics: only a real WhatsApp click, never a page-load event.
    if (typeof window.gtag === "function") {
      window.gtag("event", "whatsapp_click", {
        tour_id: el.getAttribute("data-tour") || "none",
        language: document.documentElement.lang || "unknown",
        cta_position: el.getAttribute("data-pos") || "unknown"
      });
      var conv = window.KERO_ADS_CONVERSION;
      if (conv) { window.gtag("event", "conversion", { send_to: conv }); }
    }
  });

  /* ---- Scroll reveal (respects reduced motion) ---- */
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduced || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  }
})();
