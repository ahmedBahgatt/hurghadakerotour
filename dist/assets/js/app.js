/* =========================================================================
   KeRo Tours - progressive enhancement
   Fully functional without JS; this adds nav, dropdown, gallery, lightbox,
   scroll reveal, WhatsApp wiring and optional analytics events.
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
    document.querySelectorAll(".mobile-menu a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Excursions dropdown (desktop): click + keyboard, hover via CSS ---- */
  document.querySelectorAll("[data-dd]").forEach(function (dd) {
    var trigger = dd.querySelector("[data-dd-trigger]");
    if (!trigger) return;
    function setOpen(open) {
      dd.setAttribute("data-open", open ? "true" : "false");
      trigger.setAttribute("aria-expanded", open ? "true" : "false");
    }
    trigger.addEventListener("click", function (e) {
      e.preventDefault();
      setOpen(dd.getAttribute("data-open") !== "true");
    });
    trigger.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown") {
        e.preventDefault();
        setOpen(true);
        var first = dd.querySelector(".nav__dd a");
        if (first) first.focus();
      }
    });
    document.addEventListener("click", function (e) {
      if (!dd.contains(e.target)) setOpen(false);
    });
    dd.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { setOpen(false); trigger.focus(); }
    });
  });

  /* ---- WhatsApp link wiring ---- */
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
  document.addEventListener("click", function (e) {
    var el = e.target.closest ? e.target.closest("[data-wa]") : null;
    if (!el) return;
    if (el.classList.contains("is-pending")) { e.preventDefault(); return; }
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

  /* ---- Lightbox (shared) ---- */
  var lb = document.querySelector("[data-lightbox]");
  var lbImg = lb ? lb.querySelector("[data-lbimg]") : null;
  var lbCounter = lb ? lb.querySelector("[data-lbcounter]") : null;
  var lbList = [], lbIndex = 0, lbLastFocus = null;

  function lbRender() {
    if (!lbImg) return;
    lbImg.src = lbList[lbIndex];
    lbImg.alt = "";
    if (lbCounter) lbCounter.textContent = (lbIndex + 1) + " / " + lbList.length;
  }
  function lbOpen(list, i) {
    if (!lb) return;
    lbList = list; lbIndex = i; lbLastFocus = document.activeElement;
    lbRender();
    lb.hidden = false; lb.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    var c = lb.querySelector("[data-lbclose]"); if (c) c.focus();
  }
  function lbClose() {
    if (!lb) return;
    lb.hidden = true; lb.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (lbLastFocus) lbLastFocus.focus();
  }
  function lbStep(d) { lbIndex = (lbIndex + d + lbList.length) % lbList.length; lbRender(); }
  if (lb) {
    lb.querySelector("[data-lbclose]").addEventListener("click", lbClose);
    lb.querySelector("[data-lbprev]").addEventListener("click", function () { lbStep(-1); });
    lb.querySelector("[data-lbnext]").addEventListener("click", function () { lbStep(1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) lbClose(); });
    document.addEventListener("keydown", function (e) {
      if (lb.hidden) return;
      if (e.key === "Escape") lbClose();
      else if (e.key === "ArrowLeft") lbStep(-1);
      else if (e.key === "ArrowRight") lbStep(1);
    });
  }

  /* ---- Galleries ---- */
  document.querySelectorAll("[data-gallery]").forEach(function (g) {
    var images = [];
    try { images = JSON.parse(g.getAttribute("data-images") || "[]"); } catch (e) { images = []; }
    if (!images.length) return;
    var main = g.querySelector("[data-gmain]");
    var cur = g.querySelector("[data-gcur]");
    var thumbs = g.querySelectorAll("[data-gthumb]");
    var index = 0;

    function show(i) {
      index = (i + images.length) % images.length;
      if (main) main.src = images[index];
      if (cur) cur.textContent = index + 1;
      thumbs.forEach(function (t) {
        t.classList.toggle("is-active", parseInt(t.getAttribute("data-gthumb"), 10) === index);
      });
    }
    thumbs.forEach(function (t) {
      t.addEventListener("click", function () { show(parseInt(t.getAttribute("data-gthumb"), 10)); });
    });
    var prev = g.querySelector("[data-gprev]"), next = g.querySelector("[data-gnext]");
    if (prev) prev.addEventListener("click", function () { show(index - 1); });
    if (next) next.addEventListener("click", function () { show(index + 1); });
    var zoom = g.querySelector("[data-gzoom]");
    if (zoom) zoom.addEventListener("click", function () { lbOpen(images, index); });
    if (main) main.addEventListener("click", function () { lbOpen(images, index); });

    /* touch swipe on main */
    var x0 = null;
    if (main) {
      main.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
      main.addEventListener("touchend", function (e) {
        if (x0 === null) return;
        var dx = e.changedTouches[0].clientX - x0;
        if (Math.abs(dx) > 40) show(dx < 0 ? index + 1 : index - 1);
        x0 = null;
      }, { passive: true });
    }
  });

  /* ---- Scroll reveal ---- */
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduced || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-visible"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Hero slideshow (Ken-Burns crossfade) ---- */
  var heroWrap = document.querySelector("[data-hero-slides]");
  if (heroWrap) {
    var slides = heroWrap.querySelectorAll(".hero__slide");
    if (slides.length > 1 && !reduced) {
      var hi = 0;
      setInterval(function () {
        if (document.hidden) return;
        slides[hi].classList.remove("is-active");
        hi = (hi + 1) % slides.length;
        slides[hi].classList.add("is-active");
      }, 5000);
    }
  }
})();
