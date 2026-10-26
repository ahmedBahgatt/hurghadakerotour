/* =========================================================================
   KeRo Tours - progressive enhancement
   Nav drawer, Excursions dropdown, booking dialog + WhatsApp message,
   sticky booking bar, gallery, lightbox, scroll reveal, WhatsApp wiring.
   Works without JS for core content; these add the premium interactions.
   ========================================================================= */
(function () {
  "use strict";
  var doc = document;
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- shared scroll lock (iOS-safe, reference-counted) ---- */
  var _scrollY = 0, _locks = 0;
  function lockScroll() {
    if (_locks++ === 0) {
      _scrollY = window.scrollY || window.pageYOffset || 0;
      var b = doc.body;
      b.style.position = "fixed"; b.style.top = (-_scrollY) + "px";
      b.style.left = "0"; b.style.right = "0"; b.style.width = "100%";
    }
  }
  function unlockScroll() {
    if (_locks > 0 && --_locks === 0) {
      var b = doc.body;
      b.style.position = ""; b.style.top = ""; b.style.left = "";
      b.style.right = ""; b.style.width = "";
      window.scrollTo(0, _scrollY);
    }
  }

  var FOCUSABLE = 'a[href],button:not([disabled]),select,textarea,input:not([type=hidden]),[tabindex]:not([tabindex="-1"])';
  function focusablesIn(el) {
    return Array.prototype.filter.call(el.querySelectorAll(FOCUSABLE), function (n) {
      return n.offsetParent !== null || n === doc.activeElement;
    });
  }
  function trapTab(container, e) {
    if (e.key !== "Tab") return;
    var f = focusablesIn(container);
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
  }

  /* ====================================================================
     WhatsApp handoff (shared) + date helpers
     ==================================================================== */
  /* Open wa.me in a SEPARATE browsing context (a new tab) so the current KeRo
     page stays intact in its own tab. Returning from the WhatsApp app then lands
     the visitor back on KeRo, not stranded on the api.whatsapp.com "Continue to
     Chat" interstitial. A synthesized <a target="_blank" rel="noopener"> click is
     the most reliable user-gesture new-tab trigger across iOS Safari / Android
     Chrome and mirrors the site's anchor CTAs. This replaces the old
     `window.open(...,"noopener")` + `if(!w) location.href=url` fallback: with
     noopener, window.open returns null by spec, so that fallback ALWAYS ran and
     navigated the same tab to wa.me - the exact strand bug. No same-tab fallback
     here by design; we never claim to override OS/browser app-return behaviour. */
  function openWhatsApp(url) {
    try {
      var a = doc.createElement("a");
      a.href = url; a.target = "_blank"; a.rel = "noopener";
      doc.body.appendChild(a);
      a.click();
      doc.body.removeChild(a);
    } catch (e) {
      /* last resort only if DOM click threw: a new window, still never same-tab */
      window.open(url, "_blank", "noopener");
    }
  }

  /* Today's date in Egypt (Africa/Cairo) as yyyy-mm-dd, independent of the
     visitor's own timezone - so "no past dates" uses the Hurghada calendar day
     and never shifts by one around midnight/UTC. */
  function cairoTodayISO() {
    try {
      return new Intl.DateTimeFormat("en-CA", { timeZone: "Africa/Cairo" }).format(new Date());
    } catch (e) {
      var d = new Date();
      return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
    }
  }

  var DATE_LOCALE = { fr: "fr-FR", pl: "pl-PL", ro: "ro-RO" };
  /* Format an ISO yyyy-mm-dd as a natural, unambiguous localized date. The ISO
     string is parsed as a LOCAL date (new Date(y, m-1, d)) - never
     `new Date(iso)`, which is UTC midnight and can roll back a day. */
  function formatLocalDate(iso, lang) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(iso)) return iso;
    var p = iso.split("-");
    var d = new Date(+p[0], +p[1] - 1, +p[2]);
    try {
      return new Intl.DateTimeFormat(DATE_LOCALE[lang] || "fr-FR",
        { weekday: "long", day: "numeric", month: "long", year: "numeric" }).format(d);
    } catch (e) { return iso; }
  }

  /* ====================================================================
     Mobile navigation drawer (slide-in from right)
     ==================================================================== */
  var drawer = doc.querySelector("[data-drawer]");
  var drawerOpenBtn = doc.querySelector("[data-drawer-open]");
  var drawerLastFocus = null;
  function openDrawer() {
    if (!drawer) return;
    drawer.setAttribute("aria-hidden", "false");
    drawer.classList.add("is-open");
    if (drawerOpenBtn) drawerOpenBtn.setAttribute("aria-expanded", "true");
    drawerLastFocus = doc.activeElement;
    lockScroll();
    var c = drawer.querySelector("[data-drawer-close]");
    if (c) c.focus();
  }
  function closeDrawer() {
    if (!drawer || drawer.getAttribute("aria-hidden") === "true") return;
    drawer.setAttribute("aria-hidden", "true");
    drawer.classList.remove("is-open");
    if (drawerOpenBtn) drawerOpenBtn.setAttribute("aria-expanded", "false");
    unlockScroll();
    if (drawerLastFocus && drawerLastFocus.focus) drawerLastFocus.focus();
  }
  if (drawer && drawerOpenBtn) {
    drawerOpenBtn.addEventListener("click", openDrawer);
    drawer.querySelectorAll("[data-drawer-close]").forEach(function (b) {
      b.addEventListener("click", closeDrawer);
    });
    /* close after navigating to any in-drawer link (not the expanders) */
    drawer.querySelectorAll(".drawer__nav a, .drawer__lang a").forEach(function (a) {
      a.addEventListener("click", function () { setTimeout(closeDrawer, 10); });
    });
    drawer.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closeDrawer(); }
      else { trapTab(drawer.querySelector(".drawer__panel"), e); }
    });
    /* Resizing up to the desktop breakpoint hides the hamburger + drawer via CSS;
       force the drawer closed so the scroll lock is released and aria state /
       focus are reset (no stuck body, no hidden-but-"open" dialog). */
    var deskMQ = window.matchMedia("(min-width: 1000px)");
    var onDesk = function (e) { if (e.matches) closeDrawer(); };
    if (deskMQ.addEventListener) deskMQ.addEventListener("change", onDesk);
    else if (deskMQ.addListener) deskMQ.addListener(onDesk);
  }

  /* ====================================================================
     Booking dialog (bottom-sheet on mobile, centered modal on desktop)
     ==================================================================== */
  var BK = window.KERO_BK || { wa: "", tour: "", s: {}, tours: {} };
  var S = BK.s || {};
  var TOURS = BK.tours || {};
  var dlg = doc.querySelector("[data-bookdlg]");
  var form = dlg ? dlg.querySelector("[data-bookform]") : null;
  var dlgLastFocus = null;
  var activeTourId = "";           /* tour resolved for the open form (context mode) */
  var lastEntry = {};              /* in-memory ONLY (never localStorage) - preserves
                                      input if the sheet is closed and reopened */

  function waNumber() {
    var runtime = (window.KERO_WHATSAPP || "").replace(/[^0-9]/g, "");
    return runtime || (BK.wa || "").replace(/[^0-9]/g, "");
  }

  function priceLine(t) {
    var html = '<b>€' + t.price + '</b> <span>' + (t.unit || "") + '</span>';
    if (t.type === "per_boat" && S.note_boat) {
      html += '<em class="bookform__boatnote">' + S.note_boat + '</em>';
    }
    return html;
  }

  function updateSelectPrice() {
    if (!form) return;
    var sel = form.elements["excursion"];
    var priceEl = dlg.querySelector("[data-bk-price]");
    if (!sel || !priceEl) return;
    var t = TOURS[sel.value];
    if (!t) { priceEl.hidden = true; return; }
    priceEl.innerHTML = priceLine(t);
    priceEl.hidden = false;
  }

  /* context mode = the tour is already known (tour page / clicked card / bar):
     show a read-only title + price, hide the selector. Otherwise show the
     selector (homepage / general CTAs). */
  function setMode(tourId) {
    var ctx = dlg.querySelector("[data-bk-context]");
    var selField = dlg.querySelector("[data-bk-select-field]");
    var priceEl = dlg.querySelector("[data-bk-price]");
    var sel = form && form.elements["excursion"];
    var t = TOURS[tourId];
    activeTourId = t ? tourId : "";
    if (t) {
      if (ctx) {
        var nameEl = ctx.querySelector("[data-bk-context-name]");
        var priceCtx = ctx.querySelector("[data-bk-context-price]");
        if (nameEl) nameEl.textContent = t.name;
        if (priceCtx) priceCtx.innerHTML = priceLine(t);
        ctx.hidden = false;
      }
      if (selField) selField.hidden = true;
      if (sel) sel.disabled = true;     /* excluded from submission/validation */
      if (priceEl) priceEl.hidden = true;
    } else {
      if (ctx) ctx.hidden = true;
      if (selField) selField.hidden = false;
      if (sel) sel.disabled = false;
      updateSelectPrice();
    }
  }

  var ENTRY_KEYS = ["hotel", "room", "people", "date", "notes"];
  function restoreEntry() {
    if (!form) return;
    ENTRY_KEYS.forEach(function (k) {
      if (lastEntry[k] != null && form.elements[k]) form.elements[k].value = lastEntry[k];
    });
  }
  function saveEntry() {
    if (!form) return;
    ENTRY_KEYS.forEach(function (k) {
      if (form.elements[k]) lastEntry[k] = form.elements[k].value;
    });
  }

  /* The date field's minimum selectable day is ALWAYS "today in Cairo". Set it on
     init and on every open so the native picker greys out / blocks past days, and
     a page left open across Egyptian midnight still refuses yesterday. Never
     hardcoded; recomputed from Africa/Cairo each time. */
  var dateField = form ? form.elements["date"] : null;
  function refreshDateMin() { if (dateField) dateField.min = cairoTodayISO(); }
  refreshDateMin();

  function openBooking(tourId) {
    if (!dlg) return;
    dlgLastFocus = doc.activeElement;
    /* derive context from the clicked element, else the current page's tour */
    var resolved = (tourId && tourId !== "none") ? tourId : (BK.tour || "");
    if (!TOURS[resolved]) resolved = "";
    setMode(resolved);
    restoreEntry();
    refreshDateMin();   /* native picker blocks past days; re-checked on submit */
    var err = dlg.querySelector("[data-bk-err]"); if (err) { err.hidden = true; err.textContent = ""; }
    dlg.hidden = false; dlg.setAttribute("aria-hidden", "false");
    dlg.classList.add("is-open");
    lockScroll();
    var sel = form && form.elements["excursion"];
    var focusTarget = (!resolved && sel && !sel.disabled) ? sel : (form ? form.elements["hotel"] : null);
    if (focusTarget) setTimeout(function () { focusTarget.focus(); }, 30);
  }
  function closeBooking() {
    if (!dlg || dlg.hidden) return;
    saveEntry();
    dlg.hidden = true; dlg.setAttribute("aria-hidden", "true");
    dlg.classList.remove("is-open");
    unlockScroll();
    if (dlgLastFocus && dlgLastFocus.focus) dlgLastFocus.focus();
  }

  /* delegated opener: any [data-book-open] (links keep wa.me as no-JS fallback) */
  doc.addEventListener("click", function (e) {
    var t = e.target.closest ? e.target.closest("[data-book-open]") : null;
    if (!t || !dlg) return;
    if (t.classList.contains("is-pending")) { e.preventDefault(); return; }
    e.preventDefault();
    if (drawer && drawer.getAttribute("aria-hidden") === "false") closeDrawer();
    openBooking(t.getAttribute("data-tour"));
  });

  if (dlg) {
    dlg.querySelectorAll("[data-book-close]").forEach(function (b) {
      b.addEventListener("click", closeBooking);
    });
    dlg.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closeBooking(); }
      else { trapTab(dlg.querySelector(".bookdlg__panel"), e); }
    });
  }
  if (form) {
    if (form.elements["excursion"]) form.elements["excursion"].addEventListener("change", updateSelectPrice);

    /* Guard the date field against values that slip past the native picker's min
       (manual typing, paste, or programmatic set). On any change/input: refresh
       the min to the live Cairo day, and if the value is in the past, clear it
       (never keep a past value) and show the localized inline error. A valid
       value clears that error. */
    if (dateField) {
      var onDateCheck = function () {
        refreshDateMin();
        var err = dlg.querySelector("[data-bk-err]");
        var v = dateField.value;
        if (v && /^\d{4}-\d{2}-\d{2}$/.test(v) && v < cairoTodayISO()) {
          dateField.value = "";
          if (err) { err.textContent = S.err_date_past; err.hidden = false; }
          try { dateField.focus(); } catch (e2) {}
        } else if (v && err && !err.hidden && err.textContent === S.err_date_past) {
          err.hidden = true; err.textContent = "";
        }
      };
      dateField.addEventListener("change", onDateCheck);
      dateField.addEventListener("input", onDateCheck);
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var err = dlg.querySelector("[data-bk-err]");
      function fail(msg, field) {
        if (err) { err.textContent = msg; err.hidden = false; }
        if (field && field.focus) field.focus();
      }
      var f = form.elements;
      /* resolve the tour: context mode (activeTourId) or the selector */
      var tourId = activeTourId;
      if (!tourId) {
        var sel = f["excursion"];
        if (!sel || !sel.value) return fail(S.err_excursion, sel);
        tourId = sel.value;
      }
      var t = TOURS[tourId];
      if (!t) return fail(S.err_excursion, f["excursion"]);
      var hotel = f["hotel"].value.trim();
      if (!hotel) return fail(S.err_hotel, f["hotel"]);
      var people = parseInt(f["people"].value, 10);
      if (isNaN(people) || people < 1) return fail(S.err_people, f["people"]);
      /* preferred excursion date: required + never in the past (Cairo calendar).
         ISO strings compare lexicographically, so no Date()/timezone shift. */
      var dateVal = (f["date"] ? f["date"].value : "").trim();
      if (!dateVal || !/^\d{4}-\d{2}-\d{2}$/.test(dateVal)) return fail(S.err_date, f["date"]);
      if (dateVal < cairoTodayISO()) return fail(S.err_date_past, f["date"]);
      var room = (f["room"].value || "").trim();
      var notes = (f["notes"].value || "").trim();
      var quote = (t.type === "per_boat") && people > 5;
      var lang = doc.documentElement.lang || "fr";

      var L = [];
      L.push(S.m_intro); L.push("");
      L.push("• " + S.m_excursion + ": " + t.name);
      if (t.url) L.push("• " + S.m_url + ": " + t.url);
      L.push("• " + S.m_price + ": €" + t.price + " " + (t.unit || ""));
      L.push("• " + S.m_hotel + ": " + hotel);
      if (room) L.push("• " + S.m_room + ": " + room);
      L.push("• " + S.m_people + ": " + people);
      L.push("• " + S.m_date + ": " + formatLocalDate(dateVal, lang));
      if (notes) L.push("• " + S.m_notes + ": " + notes);
      if (quote) { L.push(""); L.push(S.m_quote); }
      L.push(""); L.push(S.m_outro);

      var num = waNumber();
      if (!num) { if (err) { err.textContent = "WhatsApp unavailable."; err.hidden = false; } return; }
      var url = "https://wa.me/" + num + "?text=" + encodeURIComponent(L.join("\n"));

      if (typeof window.gtag === "function") {
        window.gtag("event", "whatsapp_click", {
          tour_id: tourId, language: doc.documentElement.lang || "unknown", cta_position: "booking_form"
        });
        var conv = window.KERO_ADS_CONVERSION;
        if (conv) window.gtag("event", "conversion", { send_to: conv });
      }
      saveEntry();
      openWhatsApp(url);
      closeBooking();
    });
  }

  /* ====================================================================
     Excursions dropdown (desktop): click + keyboard, hover via CSS
     ==================================================================== */
  doc.querySelectorAll("[data-dd]").forEach(function (dd) {
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
        e.preventDefault(); setOpen(true);
        var first = dd.querySelector(".nav__dd a"); if (first) first.focus();
      }
    });
    doc.addEventListener("click", function (e) { if (!dd.contains(e.target)) setOpen(false); });
    dd.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { setOpen(false); trigger.focus(); }
    });
  });

  /* ====================================================================
     WhatsApp link wiring (non-form links: footer, floating, fallbacks)
     ==================================================================== */
  var runtimeNum = (window.KERO_WHATSAPP || "").replace(/[^0-9]/g, "");
  doc.querySelectorAll("[data-wa]").forEach(function (el) {
    var text = el.getAttribute("data-wa-text") || "";
    var baked = el.getAttribute("data-wa-href") || "";
    var href = "";
    if (runtimeNum) {
      href = "https://wa.me/" + runtimeNum + (text ? "?text=" + encodeURIComponent(text) : "");
    } else if (baked) { href = baked; }
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
  doc.addEventListener("click", function (e) {
    var el = e.target.closest ? e.target.closest("[data-wa]") : null;
    if (!el) return;
    if (el.hasAttribute("data-book-open")) return; /* handled by booking opener */
    if (el.classList.contains("is-pending")) { e.preventDefault(); return; }
    if (typeof window.gtag === "function") {
      window.gtag("event", "whatsapp_click", {
        tour_id: el.getAttribute("data-tour") || "none",
        language: doc.documentElement.lang || "unknown",
        cta_position: el.getAttribute("data-pos") || "unknown"
      });
      var conv = window.KERO_ADS_CONVERSION;
      if (conv) { window.gtag("event", "conversion", { send_to: conv }); }
    }
  });

  /* ====================================================================
     Lightbox (shared)
     ==================================================================== */
  var lb = doc.querySelector("[data-lightbox]");
  var lbImg = lb ? lb.querySelector("[data-lbimg]") : null;
  var lbCounter = lb ? lb.querySelector("[data-lbcounter]") : null;
  var lbList = [], lbAlts = [], lbIndex = 0, lbLastFocus = null;
  function lbRender() {
    if (!lbImg) return;
    lbImg.src = lbList[lbIndex]; lbImg.alt = lbAlts[lbIndex] || "";
    if (lbCounter) lbCounter.textContent = (lbIndex + 1) + " / " + lbList.length;
  }
  function lbOpen(list, i, alts) {
    if (!lb) return;
    lbList = list; lbAlts = alts || []; lbIndex = i; lbLastFocus = doc.activeElement;
    lbRender();
    lb.hidden = false; lb.setAttribute("aria-hidden", "false");
    lockScroll();
    var c = lb.querySelector("[data-lbclose]"); if (c) c.focus();
  }
  function lbClose() {
    if (!lb) return;
    lb.hidden = true; lb.setAttribute("aria-hidden", "true");
    unlockScroll();
    if (lbLastFocus && lbLastFocus.focus) lbLastFocus.focus();
  }
  function lbStep(d) { lbIndex = (lbIndex + d + lbList.length) % lbList.length; lbRender(); }
  if (lb) {
    lb.querySelector("[data-lbclose]").addEventListener("click", lbClose);
    lb.querySelector("[data-lbprev]").addEventListener("click", function () { lbStep(-1); });
    lb.querySelector("[data-lbnext]").addEventListener("click", function () { lbStep(1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) lbClose(); });
    doc.addEventListener("keydown", function (e) {
      if (lb.hidden) return;
      if (e.key === "Escape") lbClose();
      else if (e.key === "ArrowLeft") lbStep(-1);
      else if (e.key === "ArrowRight") lbStep(1);
      else trapTab(lb, e);
    });
  }

  /* ====================================================================
     Galleries
     ==================================================================== */
  doc.querySelectorAll("[data-gallery]").forEach(function (g) {
    var images = [], alts = [];
    try { images = JSON.parse(g.getAttribute("data-images") || "[]"); } catch (e) { images = []; }
    try { alts = JSON.parse(g.getAttribute("data-alts") || "[]"); } catch (e) { alts = []; }
    if (!images.length) return;
    var main = g.querySelector("[data-gmain]");
    var cur = g.querySelector("[data-gcur]");
    var thumbs = g.querySelectorAll("[data-gthumb]");
    var index = 0;
    function show(i) {
      index = (i + images.length) % images.length;
      if (main) { main.src = images[index]; if (alts[index]) main.alt = alts[index]; }
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
    if (zoom) zoom.addEventListener("click", function () { lbOpen(images, index, alts); });
    if (main) main.addEventListener("click", function () { lbOpen(images, index, alts); });
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

  /* ====================================================================
     Scroll reveal
     ==================================================================== */
  var revealEls = doc.querySelectorAll(".reveal");
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
})();
