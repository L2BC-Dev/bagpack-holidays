/* Bagpack Holidays — site behaviour */
(function () {
  "use strict";

  var WA_NUMBER = "919206060645";

  function waLink(text) {
    return "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text);
  }

  // Header: turns solid after scrolling past the hero
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    header.classList.toggle("solid", window.scrollY > 40);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Mobile menu
  var toggle = document.querySelector(".menu-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    header.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () {
        header.classList.remove("menu-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Reveal on scroll
  document.querySelectorAll(".stagger").forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (el, i) {
      el.style.setProperty("--i", i);
    });
  });
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  // Destination filter
  var filterBar = document.querySelector(".filter-bar");
  if (filterBar) {
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest("button");
      if (!btn) return;
      filterBar.querySelectorAll("button").forEach(function (b) { b.classList.remove("active"); });
      btn.classList.add("active");
      var f = btn.getAttribute("data-filter");
      document.querySelectorAll(".dest-card[data-type]").forEach(function (card) {
        card.classList.toggle("is-hidden", f !== "all" && card.getAttribute("data-type") !== f);
      });
    });
  }

  // Any element with data-wa="message" opens WhatsApp with that message
  document.querySelectorAll("[data-wa]").forEach(function (el) {
    el.setAttribute("href", waLink(el.getAttribute("data-wa")));
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener");
  });

  function val(form, name) {
    var el = form.elements[name];
    return el ? String(el.value || "").trim() : "";
  }

  function formatDate(v) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) return v;
    var d = new Date(v + "T00:00:00");
    return d.toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric" });
  }

  // Home: boarding-pass quick enquiry
  var quick = document.getElementById("quick-enquiry");
  if (quick) {
    quick.addEventListener("submit", function (e) {
      e.preventDefault();
      var type = (quick.querySelector("input[name=type]:checked") || {}).value || "Holiday package";
      var lines = ["Hi Bagpack Holidays! I'd like a quote.", "", "Service: " + type];
      var from = val(quick, "from"), to = val(quick, "to"), date = val(quick, "date"), pax = val(quick, "pax");
      if (from) lines.push("From: " + from);
      if (to) lines.push("To: " + to);
      if (date) lines.push("Travel date: " + formatDate(date));
      if (pax) lines.push("Travellers: " + pax);
      window.open(waLink(lines.join("\n")), "_blank", "noopener");
    });
  }

  // Contact form → WhatsApp
  var contact = document.getElementById("contact-form");
  if (contact) {
    contact.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      var nameField = contact.querySelector("[data-field=name]");
      var phoneField = contact.querySelector("[data-field=phone]");
      var name = val(contact, "name");
      var phone = val(contact, "phone").replace(/[\s-]/g, "");
      nameField.classList.toggle("invalid", !name);
      var phoneOk = /^(\+?\d{10,14})$/.test(phone);
      phoneField.classList.toggle("invalid", !phoneOk);
      if (!name || !phoneOk) ok = false;
      if (!ok) {
        (contact.querySelector(".invalid input") || {}).focus && contact.querySelector(".invalid input").focus();
        return;
      }
      var lines = ["Hi Bagpack Holidays! New enquiry from the website.", ""];
      lines.push("Name: " + name);
      lines.push("Phone: " + phone);
      [["service", "Service"], ["destination", "Destination"], ["date", "Travel date"], ["adults", "Adults"], ["children", "Children"], ["message", "Details"]].forEach(function (p) {
        var v = val(contact, p[0]);
        if (p[0] === "date") v = formatDate(v);
        if (v) lines.push(p[1] + ": " + v);
      });
      window.open(waLink(lines.join("\n")), "_blank", "noopener");
    });
  }

  // Open-now pill on contact page (10:00–20:00 IST, all days)
  var pill = document.querySelector(".open-pill");
  if (pill) {
    var now = new Date();
    var istMinutes = (now.getUTCHours() * 60 + now.getUTCMinutes() + 330) % 1440;
    var open = istMinutes >= 600 && istMinutes < 1200;
    pill.classList.toggle("open", open);
    pill.querySelector("span").textContent = open ? "Open now — we'll reply quickly" : "Closed now — message us, we'll reply at 10 AM";
  }

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
