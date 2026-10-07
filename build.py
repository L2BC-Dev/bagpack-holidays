# Generates the static Bagpack Holidays pages (shared header/footer). Run: python build.py
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))

PHONE_DISPLAY = "+91 92060 60645"
PHONE_TEL = "+919206060645"
EMAIL = "Bookings.bagpackholidays@gmail.com"
ADDRESS = "267, Sector 17, Faridabad, Haryana 121001"
HOURS = "Mon – Sun, 10 AM – 8 PM"
SITE = "https://www.bagpackholidays.com"

def ic(name, cls=""):
    paths = {
        "plane": '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
        "bed": '<path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><path d="M6 8v9"/><circle cx="8.5" cy="12.5" r="1.5"/>',
        "map": '<path d="M14.1 6.2 9.9 3.8a2 2 0 0 0-1.8 0L3.6 6.1A1 1 0 0 0 3 7v12.4a1 1 0 0 0 1.4.9l3.7-1.9a2 2 0 0 1 1.8 0l4.2 2.4a2 2 0 0 0 1.8 0l4.5-2.3a1 1 0 0 0 .6-.9V5.2a1 1 0 0 0-1.4-.9l-3.7 1.9a2 2 0 0 1-1.8 0z"/><path d="M15 6.5v14"/><path d="M9 3.5v14"/>',
        "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
        "passport": '<rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M8 17h8"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
        "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
        "pin": '<path d="M20 10c0 5-5.5 10.2-7.4 11.8a1 1 0 0 1-1.2 0C9.5 20.2 4 15 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
        "check": '<path d="M20 6 9 17l-5-5"/>',
        "checkc": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
        "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
        "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
        "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M6.3 17.7l-1.4 1.4M19.1 4.9l-1.4 1.4"/>',
        "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/>',
        "route": '<circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/>',
        "shield": '<path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.5 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
        "wallet": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
        "headset": '<path d="M3 11h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5a9 9 0 0 1 18 0v5a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/><path d="M21 16v2a4 4 0 0 1-4 4h-5"/>',
        "sparkle": '<path d="M9.9 15.5A2 2 0 0 0 8.5 14.1L2.4 12.5a.5.5 0 0 1 0-1l6.1-1.6A2 2 0 0 0 9.9 8.5l1.6-6.1a.5.5 0 0 1 1 0l1.6 6.1a2 2 0 0 0 1.4 1.4l6.1 1.6a.5.5 0 0 1 0 1l-6.1 1.6a2 2 0 0 0-1.4 1.4l-1.6 6.1a.5.5 0 0 1-1 0z"/>',
        "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
        "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v4a2 2 0 0 0 2 2h4M16 13H8M16 17H8M10 9H8"/>',
        "camera": '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3z"/><circle cx="12" cy="13" r="3"/>',
        "bank": '<path d="M3 22h18M6 18v-7M10 18v-7M14 18v-7M18 18v-7M12 2l8 5H4z"/>',
        "ticket": '<path d="M2 9a3 3 0 0 1 0 6v2a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-2a3 3 0 0 1 0-6V7a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M13 5v2M13 17v2M13 11v2"/>',
        "car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
        "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
        "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
        "edit": '<path d="M12 20h9"/><path d="M16.4 3.6a2.1 2.1 0 1 1 3 3L7 19l-4 1 1-4Z"/>',
    }
    if name == "wa":
        return '<svg class="%s" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>' % cls
    return '<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (cls, paths[name])

NAV = [("index.html", "Home"), ("services.html", "Services"), ("destinations.html", "Destinations"),
       ("visa.html", "Visa"), ("about.html", "About"), ("contact.html", "Contact")]

def head(title, desc, page, extra=""):
    canonical = SITE + "/" + ("" if page == "index.html" else page)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#2c3a54">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bagpack Holidays">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/logo-original.jpg">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,300;1,9..144,400&family=Jost:wght@300;400;500;600&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra}</head>
<body>
"""

def header(page):
    links = "\n".join(
        f'      <a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Bagpack Holidays — home">
      <img class="icon light" src="assets/img/logo-icon-white.png" alt="" width="270" height="295">
      <img class="icon dark" src="assets/img/logo-icon.png" alt="" width="270" height="295">
      <img class="word light" src="assets/img/logo-wordmark-white.png" alt="Bagpack Holidays" width="536" height="54">
      <img class="word dark" src="assets/img/logo-wordmark.png" alt="Bagpack Holidays" width="536" height="54">
    </a>
    <nav class="nav" aria-label="Main">
{links}
      <a class="btn btn-primary" href="#" data-wa="Hi Bagpack Holidays! I'd like to plan a trip.">{ic("wa")}Plan my trip</a>
    </nav>
    <div class="header-cta">
      <a class="btn btn-primary" href="#" data-wa="Hi Bagpack Holidays! I'd like to plan a trip.">{ic("wa")}Plan my trip</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
"""

def cta_band(title, text):
    return f"""<section class="section tight">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <span class="eyebrow light">Let's get you moving</span>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="actions">
        <a class="btn btn-wa" href="#" data-wa="Hi Bagpack Holidays! I'd like to plan a trip.">{ic("wa")}Chat on WhatsApp</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ic("phone")}Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </div>
</section>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <img class="icon" src="assets/img/logo-icon-white.png" alt="" width="270" height="295">
        <img class="word" src="assets/img/logo-wordmark-white.png" alt="Bagpack Holidays" width="536" height="54">
        <p>Flights, hotels, holidays and visas, all planned by people who pick up the phone. Based in Faridabad, booking trips across India and the world.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="services.html">Services</a></li>
          <li><a href="destinations.html">Destinations</a></li>
          <li><a href="visa.html">Visa assistance</a></li>
          <li><a href="about.html">About us</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>We book</h4>
        <ul>
          <li><a href="services.html#flights">Flight tickets</a></li>
          <li><a href="services.html#hotels">Hotel stays</a></li>
          <li><a href="services.html#holidays">Domestic trips</a></li>
          <li><a href="services.html#holidays">International trips</a></li>
          <li><a href="visa.html">Tourist visas</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul class="footer-contact">
          <li>{ic("phone")}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li>{ic("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ic("pin")}<span>{ADDRESS}</span></li>
          <li>{ic("clock")}<span>{HOURS}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Bagpack Holidays. All rights reserved.</span>
      <span>Pack light. We'll handle the rest.</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="#" data-wa="Hi Bagpack Holidays! I have a travel query." aria-label="Chat with us on WhatsApp">{ic("wa")}</a>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def page_hero(img, crumb, title, lead):
    return f"""<section class="page-hero">
  <div class="hero-bg" style="background-image:url('assets/img/dest/{img}')"></div>
  <div class="wrap">
    <div class="crumbs load-in"><a href="index.html">Home</a><span>/</span>{crumb}</div>
    <h1 class="load-in d1">{title}</h1>
    <p class="lead load-in d2">{lead}</p>
  </div>
</section>
"""

# ---------------- Data ----------------
DESTS = [
    # key, name, region, type, sub, best, days
    ("goa", "Goa", "India", "domestic", "Beaches, shacks and sunsets", "Nov – Feb", "4–5 days"),
    ("kashmir", "Kashmir", "India", "domestic", "Meadows, Dal Lake and snow peaks", "Mar – Oct", "5–7 days"),
    ("kerala", "Kerala", "India", "domestic", "Backwaters, tea hills and houseboats", "Sep – Mar", "5–6 days"),
    ("himachal", "Himachal", "India", "domestic", "Manali, Shimla and mountain roads", "Mar – Jun", "5–7 days"),
    ("rajasthan", "Rajasthan", "India", "domestic", "Palaces, forts and desert nights", "Oct – Mar", "6–8 days"),
    ("dubai", "Dubai", "UAE", "international", "Skyline, desert safari and shopping", "Nov – Mar", "4–6 days"),
    ("thailand", "Thailand", "Asia", "international", "Bangkok, Pattaya, Phuket and Krabi", "Nov – Apr", "5–7 days"),
    ("bali", "Bali", "Indonesia", "international", "Temples, rice terraces and beach clubs", "Apr – Oct", "5–7 days"),
    ("singapore", "Singapore", "Asia", "international", "Sentosa, Universal Studios and Gardens", "All year", "4–5 days"),
    ("europe", "Europe", "Schengen", "international", "Paris, Switzerland, Italy and beyond", "Apr – Oct", "8–12 days"),
    ("maldives", "Maldives", "Indian Ocean", "international", "Overwater villas and clear lagoons", "Nov – Apr", "3–5 days"),
    ("vietnam", "Vietnam", "Asia", "international", "Ha Long Bay, Hanoi and Da Nang", "Feb – Apr", "6–8 days"),
]

def dest_card(d, lazy=True):
    key, name, region, typ, sub, best, days = d
    msg = f"Hi Bagpack Holidays! I'm interested in a {name} trip. Please share options."
    return f"""      <a class="dest-card reveal" href="#" data-type="{typ}" data-wa="{msg}">
        <img src="assets/img/dest/{key}.jpg" alt="{name}" {'loading="lazy"' if lazy else ''} width="1400" height="933">
        <span class="dest-tag">{'Domestic' if typ == 'domestic' else 'International'} · {region}</span>
        <div class="dest-body">
          <h3>{name}</h3>
          <div class="sub">{sub}</div>
          <div class="dest-meta"><span>{ic("sun")}Best: {best}</span><span>{ic("cal")}{days}</span></div>
          <span class="dest-cta">Plan this trip {ic("arrow")}</span>
        </div>
      </a>"""

# ---------------- HOME ----------------
def home():
    ld = {
        "@context": "https://schema.org", "@type": "TravelAgency", "name": "Bagpack Holidays",
        "url": SITE, "logo": SITE + "/assets/img/logo-original.jpg", "telephone": PHONE_TEL, "email": EMAIL,
        "address": {"@type": "PostalAddress", "streetAddress": "267, Sector 17", "addressLocality": "Faridabad",
                    "addressRegion": "Haryana", "postalCode": "121001", "addressCountry": "IN"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "10:00", "closes": "20:00"}],
        "founder": {"@type": "Person", "name": "Kunal Bhatia"},
    }
    extra = '<script type="application/ld+json">' + json.dumps(ld) + '</script>\n<link rel="preload" as="image" href="assets/img/dest/hero.jpg">\n'
    services = [
        ("plane", "Flights", "Domestic and international tickets at fair fares, with help on changes, baggage and seats.", "services.html#flights"),
        ("bed", "Hotels", "Handpicked stays for every budget, from beach resorts to city hotels.", "services.html#hotels"),
        ("map", "Holiday Packages", "Custom domestic and international trips with transfers, sightseeing and stays.", "services.html#holidays"),
        ("passport", "Visa Assistance", "Document checklists, form filling and appointment help for tourist visas.", "visa.html"),
    ]
    tiles = "\n".join(f"""      <div class="service-tile reveal">
        <span class="num">0{i+1}</span>
        <div class="icon-badge">{ic(s[0])}</div>
        <h3>{s[1]}</h3>
        <p>{s[2]}</p>
        <a class="link-arrow" href="{s[3]}">Learn more {ic("arrow")}</a>
      </div>""" for i, s in enumerate(services))
    featured = [DESTS[i] for i in (7, 1, 5, 6, 10)]
    cards = "\n".join(dest_card(d) for d in featured)
    names = ["Goa", "Kashmir", "Kerala", "Himachal", "Rajasthan", "Dubai", "Thailand", "Bali", "Singapore", "Europe", "Maldives", "Vietnam"]
    marquee = "".join(f"<span>{n}</span>" for n in names * 2)

    body = f"""<main>
<section class="hero">
  <div class="hero-bg" style="background-image:url('assets/img/dest/hero.jpg')"></div>
  <svg class="hero-route" viewBox="0 0 440 300" fill="none" aria-hidden="true">
    <path class="dash" d="M10 280 C 120 200, 160 60, 300 70 S 420 40, 430 10" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
    <circle cx="10" cy="280" r="6" fill="#c9a46a"/><circle cx="430" cy="10" r="6" stroke="#fff" stroke-width="2"/>
  </svg>
  <div class="wrap">
    <span class="eyebrow light load-in">Flights · Hotels · Holidays · Visas</span>
    <h1 class="load-in d1">Pack light.<br><span class="serif">We'll handle the rest.</span></h1>
    <p class="lead load-in d2">Bagpack Holidays plans your whole trip, including tickets, stays, sightseeing and visas, so you only have to show up with your bag.</p>
    <div class="hero-actions load-in d3">
      <a class="btn btn-sand" href="destinations.html">Explore destinations {ic("arrow")}</a>
      <a class="btn btn-ghost" href="#" data-wa="Hi Bagpack Holidays! I'd like to plan a trip.">{ic("wa")}Talk to us on WhatsApp</a>
    </div>
  </div>
</section>

<div class="pass-dock">
  <div class="wrap">
    <form class="pass load-in d4" id="quick-enquiry" autocomplete="on">
      <div class="pass-main">
        <div class="pass-top">
          <div class="pass-title">{ic("ticket")}Get a free quote</div>
          <div class="pass-tabs" role="radiogroup" aria-label="What do you need?">
            <label><input type="radio" name="type" value="Holiday package" checked><span>Holiday</span></label>
            <label><input type="radio" name="type" value="Flight tickets"><span>Flights</span></label>
            <label><input type="radio" name="type" value="Hotel booking"><span>Hotels</span></label>
            <label><input type="radio" name="type" value="Visa"><span>Visa</span></label>
          </div>
        </div>
        <div class="pass-fields">
          <div class="pass-field"><label for="q-from">From</label><input id="q-from" name="from" placeholder="Delhi" autocomplete="address-level2"></div>
          <div class="pass-field"><label for="q-to">To</label><input id="q-to" name="to" placeholder="Bali, Dubai…" list="dest-list"></div>
          <div class="pass-field"><label for="q-date">Departure</label><input id="q-date" name="date" type="date"></div>
          <div class="pass-field"><label for="q-pax">Travellers</label>
            <select id="q-pax" name="pax">
              <option>1 Adult</option><option selected>2 Adults</option><option>2 Adults + 1 Child</option>
              <option>2 Adults + 2 Children</option><option>Family (5+)</option><option>Group (10+)</option>
            </select>
          </div>
        </div>
        <datalist id="dest-list">{''.join(f'<option value="{n}">' for n in names)}</datalist>
      </div>
      <div class="pass-stub">
        <div class="code">BPH<small>Boarding · Your next trip</small></div>
        <div class="barcode" aria-hidden="true"></div>
        <button class="btn btn-wa btn-block" type="submit">{ic("wa")}Get my quote</button>
      </div>
    </form>
  </div>
</div>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">What we do</span>
        <h2>Everything your trip needs, <span class="serif">in one place.</span></h2>
      </div>
      <p class="lead">One team, one WhatsApp chat, one point of contact from the first enquiry to your flight home.</p>
    </div>
    <div class="services-grid stagger">
{tiles}
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<section class="section bg-white">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Where to next</span>
        <h2>Popular trips our travellers <span class="serif">love.</span></h2>
      </div>
      <a class="link-arrow" href="destinations.html">See all destinations {ic("arrow")}</a>
    </div>
    <div class="dest-grid mosaic stagger">
{cards}
    </div>
  </div>
</section>

<section class="section bg-navy on-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Why Bagpack Holidays</span>
        <h2>The best service, <span class="serif">at the best price.</span></h2>
      </div>
      <p class="lead" style="color:#aab2c1">That's our promise on every booking, whether it's a weekend in Goa or two weeks in Europe.</p>
    </div>
    <div class="why-grid stagger">
      <div class="why-item reveal"><span class="k">01</span><h3>Made for you</h3><p>Every itinerary is built around your dates, budget and the people you're travelling with. Nothing is copy-paste.</p></div>
      <div class="why-item reveal"><span class="k">02</span><h3>Honest pricing</h3><p>A clear quote with inclusions and exclusions listed upfront, so there are no surprises later.</p></div>
      <div class="why-item reveal"><span class="k">03</span><h3>Everything sorted</h3><p>Flights, hotels, transfers, sightseeing and visa, all handled by one team so nothing slips through the cracks.</p></div>
      <div class="why-item reveal"><span class="k">04</span><h3>Real people</h3><p>Call or WhatsApp us 7 days a week. You'll always talk to someone who knows your booking.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal" style="justify-content:center;text-align:center">
      <div>
        <span class="eyebrow">How it works</span>
        <h2>From "let's go" to <span class="serif">boarding</span> in three steps.</h2>
      </div>
    </div>
    <div class="steps stagger">
      <div class="step reveal"><div class="dot">{ic("chat")}</div><h3>Tell us your plan</h3><p>Share where, when and who's travelling on WhatsApp, a call or our form.</p></div>
      <div class="step reveal"><div class="dot">{ic("route")}</div><h3>Get your itinerary</h3><p>We send a day-by-day plan with hotels, flights and a clear quote. Tweak it until it's perfect.</p></div>
      <div class="step reveal"><div class="dot">{ic("plane")}</div><h3>Pack and go</h3><p>We confirm everything and share your tickets and vouchers. We're a message away throughout the trip.</p></div>
    </div>
  </div>
</section>

{cta_band('Your next trip starts <span class="serif">with a hello.</span>', 'Tell us where you want to go. We usually reply within minutes during working hours (10 AM to 8 PM, all 7 days).')}
</main>
"""
    return head("Bagpack Holidays | Flights, Hotels, Holiday Packages & Visa — Faridabad",
                "Bagpack Holidays plans domestic and international holidays, flight tickets, hotel stays and tourist visas. Based in Sector 17, Faridabad. Call +91 92060 60645.",
                "index.html", extra) + header("index.html") + body + footer()

# ---------------- SERVICES ----------------
def services():
    rows = [
        ("flights", "flights.jpg", "plane", "Flight tickets", "Fair fares, <span class=\"serif\">zero fuss.</span>",
         "Domestic or international, one-way or round trip. We compare airlines and routes to find you the best mix of price, timing and comfort.",
         ["Domestic & international tickets", "Group and family bookings", "Seat, meal & baggage add-ons", "Date changes & cancellations", "Multi-city itineraries", "Web check-in help"],
         ("Best-fare search", "Across major airlines")),
        ("hotels", "hotel.jpg", "bed", "Hotel stays", "Stays you'll <span class=\"serif\">actually like.</span>",
         "We shortlist hotels we trust in the right neighbourhoods, matched to your budget. That could be a beach resort, a city hotel or a houseboat.",
         ["Budget to luxury options", "Breakfast-included deals", "Family rooms & villas", "Early check-in requests", "Honeymoon arrangements", "Resort & island stays"],
         ("Handpicked hotels", "Matched to your budget")),
        ("holidays", "plan.jpg", "map", "Domestic & international holidays", "Complete trips, <span class=\"serif\">planned end to end.</span>",
         "Tell us the vibe and we'll build the trip with flights, hotels, transfers, sightseeing and activities, all in one day-by-day itinerary.",
         ["Round-trip flights", "Hotels with daily breakfast", "Airport & inter-city transfers", "Sightseeing as per itinerary", "Tour guide where needed", "Taxes & GST included"],
         ("Day-by-day itinerary", "Shared before you pay")),
        ("visa", "visa.jpg", "passport", "Visa assistance", "Paperwork, <span class=\"serif\">handled.</span>",
         "Tourist visas can be confusing. We give you the exact document checklist, fill the forms, book appointments and track your application.",
         ["Country-wise checklists", "Form filling & review", "Appointment booking", "Cover letter drafting", "Flight & hotel bookings for visa", "Application tracking"],
         ("12+ countries", "e-Visa & sticker visa")),
    ]
    blocks = []
    for i, r in enumerate(rows):
        key, img, icon, eyebrow, title, text, items, fc = r
        lis = "\n".join(f"          <li>{ic('check')}{x}</li>" for x in items)
        link = '<a class="btn btn-outline" href="visa.html">See visa checklists ' + ic("arrow") + '</a>' if key == "visa" else \
               f'<a class="btn btn-primary" href="#" data-wa="Hi Bagpack Holidays! I need help with {eyebrow.lower()}.">{ic("wa")}Enquire on WhatsApp</a>'
        blocks.append(f"""<section class="section{' bg-white' if i % 2 else ''}" id="{key}">
  <div class="wrap">
    <div class="split{' reverse' if i % 2 else ''}">
      <div class="split-media reveal">
        <img src="assets/img/dest/{img}" alt="{eyebrow}" loading="lazy" width="1400" height="933">
        <div class="float-card"><div class="icon-badge">{ic(icon)}</div><div><strong>{fc[0]}</strong><small>{fc[1]}</small></div></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">0{i+1} · {eyebrow}</span>
        <h2>{title}</h2>
        <p class="lead">{text}</p>
        <ul class="check-list two">
{lis}
        </ul>
        {link}
      </div>
    </div>
  </div>
</section>
""")
    body = "<main>\n" + page_hero("airport.jpg", "Services", 'Four services. <span class="serif">One team.</span>',
        "Flights, hotels, complete holidays and visas. Book one or let us handle all of it.") + "".join(blocks) + \
        cta_band('Not sure what you need? <span class="serif">Just ask.</span>', "Tell us your rough plan and we'll suggest the simplest, best-value way to do it.") + "</main>\n"
    return head("Services | Flights, Hotels, Holidays & Visa — Bagpack Holidays",
                "Flight bookings, hotel stays, domestic and international holiday packages, and tourist visa assistance from Bagpack Holidays, Faridabad.",
                "services.html") + header("services.html") + body + footer()

# ---------------- DESTINATIONS ----------------
def destinations():
    cards = "\n".join(dest_card(d) for d in DESTS)
    body = "<main>\n" + page_hero("maldives.jpg", "Destinations", 'Pick a place. <span class="serif">We\'ll plan the rest.</span>',
        "Our most-loved trips in India and abroad. Every one can be customised to your dates, budget and pace.") + f"""
<section class="section">
  <div class="wrap">
    <div class="filter-bar reveal" role="group" aria-label="Filter destinations">
      <button class="active" data-filter="all">All destinations</button>
      <button data-filter="domestic">Domestic</button>
      <button data-filter="international">International</button>
    </div>
    <div class="dest-grid">
{cards}
    </div>
    <div class="notice reveal">{ic("info")}<span>Don't see your destination? We plan trips almost everywhere, including Sri Lanka, Nepal, Bhutan, Mauritius, Turkey, Japan, Australia and more. Just <a href="contact.html" style="text-decoration:underline">tell us where</a>.</span></div>
  </div>
</section>
""" + cta_band('Have a place in mind? <span class="serif">Let\'s plan it.</span>', "Share your dates and how many people are going. We'll send you a custom itinerary, free.") + "</main>\n"
    return head("Destinations | Domestic & International Holidays — Bagpack Holidays",
                "Holiday packages to Goa, Kashmir, Kerala, Himachal, Rajasthan, Dubai, Thailand, Bali, Singapore, Europe, Maldives and Vietnam.",
                "destinations.html") + header("destinations.html") + body + footer()

# ---------------- VISA ----------------
VISAS = [
    ("Dubai (UAE)", "Middle East", "e-Visa", "e", ["Passport (6+ months valid)", "Passport-size photo, white background", "Confirmed return ticket", "Hotel booking"]),
    ("Thailand", "Southeast Asia", "Visa-free*", "free", ["Passport (6+ months valid)", "Return ticket", "Hotel booking", "Proof of funds (if asked)"]),
    ("Singapore", "Southeast Asia", "e-Visa", "e", ["Passport (6+ months valid)", "Photo as per specs", "Form 14A", "Flight & hotel details", "Bank statement"]),
    ("Bali (Indonesia)", "Southeast Asia", "e-VOA", "e", ["Passport (6+ months valid)", "Return ticket", "Hotel booking", "Photo & passport scan"]),
    ("Vietnam", "Southeast Asia", "e-Visa", "e", ["Passport (6+ months valid)", "Passport scan & photo", "Entry & exit airport", "Hotel address"]),
    ("Maldives", "Indian Ocean", "On arrival", "free", ["Passport (6+ months valid)", "Confirmed resort booking", "Return ticket", "IMUGA travel declaration"]),
    ("Schengen (Europe)", "Europe", "Sticker visa", "", ["Passport (3+ months beyond trip)", "Bank statements (3–6 months)", "ITR / salary slips", "Travel insurance", "Day-wise itinerary", "Cover letter"]),
    ("United Kingdom", "Europe", "Sticker visa", "", ["Passport & old passports", "Bank statements (6 months)", "ITR & employment proof", "Travel plan & bookings", "Online form & biometrics"]),
    ("USA", "North America", "Interview", "", ["Passport (6+ months valid)", "DS-160 form", "Photo as per specs", "Financial & job proof", "Interview appointment"]),
    ("Canada", "North America", "Sticker visa", "", ["Passport & old passports", "Bank statements & ITR", "Employment proof", "Travel history", "Biometrics"]),
    ("Australia", "Oceania", "e-Visa", "e", ["Passport", "Bank statements & ITR", "Employment / business proof", "Itinerary", "Online application"]),
    ("Japan", "East Asia", "e-Visa", "e", ["Passport (6+ months valid)", "Photo as per specs", "Bank statement & ITR", "Day-wise itinerary", "Flight & hotel bookings"]),
]

def visa():
    cards = []
    for name, region, vtype, cls, docs in VISAS:
        lis = "\n".join(f"          <li>{ic('check')}{d}</li>" for d in docs)
        cards.append(f"""      <div class="visa-card reveal">
        <div class="visa-head"><div><h3>{name}</h3><div class="region">{region}</div></div><span class="visa-type {cls}">{vtype}</span></div>
        <div class="visa-body">
          <ul>
{lis}
          </ul>
          <a class="link-arrow" href="#" data-wa="Hi Bagpack Holidays! I need help with a {name} tourist visa.">Get help with this visa {ic("arrow")}</a>
        </div>
      </div>""")
    docs = [
        ("passport", "Valid passport", "At least 6 months validity from your return date, with 2+ blank pages."),
        ("camera", "Photographs", "Recent passport-size photos. Size and background differ by country."),
        ("bank", "Bank statements", "Usually the last 3 to 6 months, stamped by the bank, showing enough funds for the trip."),
        ("file", "ITR / income proof", "Income tax returns, salary slips or business documents for most sticker visas."),
        ("ticket", "Flight bookings", "Confirmed or dummy return tickets, depending on the visa rules."),
        ("bed", "Hotel bookings", "Stay confirmation for every night of the trip."),
        ("shield", "Travel insurance", "Mandatory for Schengen and recommended everywhere else."),
        ("edit", "Cover letter", "Explains your trip purpose and plans. We draft it for you."),
    ]
    docs_html = "\n".join(f'      <div class="doc reveal">{ic(d[0])}<h3>{d[1]}</h3><p>{d[2]}</p></div>' for d in docs)
    body = "<main>\n" + page_hero("visa.jpg", "Visa", 'Tourist visas, <span class="serif">made simple.</span>',
        "We tell you exactly what's needed, prepare your file, and keep track of your application, so you can focus on packing.") + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head reveal" style="justify-content:center;text-align:center">
      <div>
        <span class="eyebrow">How we help</span>
        <h2>Your visa, <span class="serif">step by step.</span></h2>
      </div>
    </div>
    <div class="steps stagger">
      <div class="step reveal"><div class="dot">{ic("chat")}</div><h3>Share your trip</h3><p>Tell us the country, travel dates and who's going. We'll confirm the right visa type.</p></div>
      <div class="step reveal"><div class="dot">{ic("file")}</div><h3>We prepare your file</h3><p>A personal checklist, form filling, cover letter, and flight and hotel bookings, all reviewed before submission.</p></div>
      <div class="step reveal"><div class="dot">{ic("checkc")}</div><h3>Apply & track</h3><p>We book appointments where needed and update you until your visa is in hand.</p></div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">Country checklists</span>
        <h2>What you'll <span class="serif">usually need.</span></h2>
      </div>
      <p class="lead">A quick starting point for popular destinations. We'll send you the complete, up-to-date list for your exact case.</p>
    </div>
    <div class="visa-grid">
{chr(10).join(cards)}
    </div>
    <div class="notice reveal">{ic("info")}<span><strong>Please note:</strong> Visa rules, fees and processing times are set by each country and change often. *Visa-free and on-arrival entries have conditions and stay limits. We always confirm the latest requirements before you apply. The final decision on any visa rests with the embassy.</span></div>
  </div>
</section>

<section class="section bg-navy on-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">General checklist</span>
        <h2>Documents to <span class="serif">keep ready.</span></h2>
      </div>
      <p class="lead" style="color:#aab2c1">Most tourist visas ask for some mix of these. Having them ready speeds everything up.</p>
    </div>
    <div class="doc-grid stagger">
{docs_html}
    </div>
  </div>
</section>
""" + cta_band('Travelling soon? <span class="serif">Start your visa today.</span>', "Some visas take weeks, so the earlier we start, the smoother it goes. Send us your travel dates and we'll take it from there.") + "</main>\n"
    return head("Visa Assistance | Tourist Visa Help — Bagpack Holidays",
                "Tourist visa assistance for Dubai, Thailand, Singapore, Bali, Vietnam, Schengen, UK, USA, Canada, Australia, Japan and more. Document checklists and application support.",
                "visa.html") + header("visa.html") + body + footer()

# ---------------- ABOUT ----------------
def about():
    body = "<main>\n" + page_hero("kerala.jpg", "About", 'A travel company <span class="serif">built on care.</span>',
        "Bagpack Holidays is a Faridabad-based travel company that plans holidays the way you'd plan them for family.") + f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split-media reveal">
        <img src="assets/img/dest/plan.jpg" alt="Planning a trip with a map" loading="lazy" width="1400" height="933">
        <div class="float-card"><div class="icon-badge">{ic("pin")}</div><div><strong>Sector 17, Faridabad</strong><small>Open 7 days, 10 AM – 8 PM</small></div></div>
      </div>
      <div class="reveal">
        <span class="eyebrow">Our story</span>
        <h2>Why we started <span class="serif">Bagpack Holidays.</span></h2>
        <p class="lead">Planning a trip should be exciting. Too often it means juggling ten tabs, comparing confusing prices and hoping nothing goes wrong.</p>
        <p>Founded by <strong>Kunal Bhatia</strong>, Bagpack Holidays puts everything in one place: flights, hotels, sightseeing, transfers and visas, planned by one team that knows your booking inside out. You tell us what kind of trip you want. We build it day by day, explain every inclusion clearly and stay reachable until you're back home.</p>
        <p>We're new, and that's exactly why every traveller matters to us. Each trip we plan is a chance to earn a customer for life.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <p class="quote-block reveal">Our commitment is simple: to serve you the best services at the best possible cost.</p>
    <p class="quote-by reveal">The Bagpack Holidays promise</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">What we stand for</span>
        <h2>Three things we <span class="serif">never compromise on.</span></h2>
      </div>
    </div>
    <div class="values stagger">
      <div class="value reveal"><div class="icon-badge">{ic("wallet")}</div><h3>Transparency</h3><p>Clear quotes and clearly listed inclusions and exclusions. What we promise is what you get.</p></div>
      <div class="value reveal"><div class="icon-badge">{ic("heart")}</div><h3>Personal care</h3><p>Birthdays, honeymoons and first trips abroad: we plan around the moments that matter to you.</p></div>
      <div class="value reveal"><div class="icon-badge">{ic("headset")}</div><h3>Always reachable</h3><p>A real person on call and WhatsApp before, during and after your trip.</p></div>
    </div>
  </div>
</section>

<section class="section bg-navy on-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <div>
        <span class="eyebrow">What's in a Bagpack trip</span>
        <h2>Every package, <span class="serif">properly put together.</span></h2>
      </div>
      <p class="lead" style="color:#aab2c1">A typical holiday itinerary from us includes:</p>
    </div>
    <div class="doc-grid stagger">
      <div class="doc reveal">{ic("plane")}<h3>Round-trip flights</h3><p>Booked on reliable airlines with sensible timings.</p></div>
      <div class="doc reveal">{ic("bed")}<h3>Hotels + breakfast</h3><p>Comfortable stays with daily breakfast.</p></div>
      <div class="doc reveal">{ic("car")}<h3>All transfers</h3><p>Airport pickups, drops and inter-city travel.</p></div>
      <div class="doc reveal">{ic("camera")}<h3>Sightseeing</h3><p>Tours and activities, day by day as per itinerary.</p></div>
    </div>
  </div>
</section>
""" + cta_band('Let\'s plan your first trip <span class="serif">together.</span>', "Message us with your idea. Even a rough one is enough to get started.") + "</main>\n"
    return head("About Us | Bagpack Holidays, Faridabad",
                "Bagpack Holidays is a Faridabad-based travel company founded by Kunal Bhatia, offering flights, hotels, holiday packages and visa assistance.",
                "about.html") + header("about.html") + body + footer()

# ---------------- CONTACT ----------------
def contact():
    map_q = "267+Sector+17+Faridabad+Haryana+121001"
    svc_opts = "".join(f"<option>{o}</option>" for o in ["Holiday package", "Flight tickets", "Hotel booking", "Visa assistance", "Something else"])
    body = "<main>\n" + page_hero("goa.jpg", "Contact", 'Say hello. <span class="serif">Let\'s plan.</span>',
        "Call, WhatsApp, email or drop by our office. We're open every day from 10 AM to 8 PM.") + f"""
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="contact-cards stagger">
      <a class="contact-card wa reveal" href="#" data-wa="Hi Bagpack Holidays! I have a travel query."><div class="icon-badge">{ic("wa")}</div><small>WhatsApp</small><strong>{PHONE_DISPLAY}</strong></a>
      <a class="contact-card reveal" href="tel:{PHONE_TEL}"><div class="icon-badge">{ic("phone")}</div><small>Call us</small><strong>{PHONE_DISPLAY}</strong></a>
      <a class="contact-card reveal" href="mailto:{EMAIL}"><div class="icon-badge">{ic("mail")}</div><small>Email</small><strong>{EMAIL}</strong></a>
      <a class="contact-card reveal" href="https://www.google.com/maps/search/?api=1&query={map_q}" target="_blank" rel="noopener"><div class="icon-badge">{ic("pin")}</div><small>Office</small><strong>267, Sector 17, Faridabad</strong></a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:20px">
  <div class="wrap">
    <div class="contact-layout">
      <div class="form-card reveal">
        <span class="eyebrow">Enquiry form</span>
        <h2 style="font-size:clamp(1.8rem,3vw,2.4rem)">Tell us about <span class="serif">your trip.</span></h2>
        <p style="color:var(--slate);margin-bottom:28px">Fill this in and hit send. It opens WhatsApp with your details already typed, so we can reply instantly.</p>
        <form id="contact-form" novalidate>
          <div class="form-grid">
            <div class="field" data-field="name"><label for="c-name">Your name *</label><input id="c-name" name="name" autocomplete="name" required><div class="err">Please enter your name.</div></div>
            <div class="field" data-field="phone"><label for="c-phone">Phone *</label><input id="c-phone" name="phone" type="tel" autocomplete="tel" placeholder="10-digit mobile" required><div class="err">Please enter a valid phone number.</div></div>
            <div class="field"><label for="c-service">Service</label><select id="c-service" name="service">{svc_opts}</select></div>
            <div class="field"><label for="c-dest">Destination</label><input id="c-dest" name="destination" placeholder="e.g. Bali" list="c-dest-list"><datalist id="c-dest-list">{''.join(f'<option value="{d[1]}">' for d in DESTS)}</datalist></div>
            <div class="field"><label for="c-date">Travel date</label><input id="c-date" name="date" type="date"></div>
            <div class="field" style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
              <div><label for="c-adults">Adults</label><input id="c-adults" name="adults" type="number" min="1" value="2"></div>
              <div><label for="c-kids">Children</label><input id="c-kids" name="children" type="number" min="0" value="0"></div>
            </div>
            <div class="field full"><label for="c-msg">Anything else?</label><textarea id="c-msg" name="message" placeholder="Budget, hotel preference, special occasion…"></textarea></div>
            <div class="full"><button class="btn btn-wa btn-block" type="submit">{ic("wa")}Send on WhatsApp</button></div>
          </div>
          <p class="form-note">{ic("shield")}Your details go only to Bagpack Holidays through your own WhatsApp.</p>
        </form>
      </div>
      <div class="info-stack">
        <div class="hours-card reveal">
          <h3>{ic("clock")}Opening hours</h3>
          <div class="hours-row"><span>Monday – Friday</span><strong>10 AM – 8 PM</strong></div>
          <div class="hours-row"><span>Saturday</span><strong>10 AM – 8 PM</strong></div>
          <div class="hours-row"><span>Sunday</span><strong>10 AM – 8 PM</strong></div>
          <div class="open-pill"><i></i><span>Open 7 days a week</span></div>
        </div>
        <div class="map-card reveal">
          <iframe title="Bagpack Holidays office on Google Maps" src="https://maps.google.com/maps?q={map_q}&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="addr">{ic("pin")}<div><strong>Bagpack Holidays</strong><br>{ADDRESS}, India</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap">
    <div class="section-head reveal" style="justify-content:center;text-align:center">
      <div><span class="eyebrow">FAQ</span><h2>Good to <span class="serif">know.</span></h2></div>
    </div>
    <div class="faq reveal">
      <details><summary>How quickly will I get a quote?</summary><p>During working hours (10 AM to 8 PM, all 7 days) we usually reply on WhatsApp within minutes. A full custom itinerary is typically ready within a few hours, depending on the destination.</p></details>
      <details><summary>Can you customise a package?</summary><p>Yes. Every trip is built around you. Change the hotels, add days, swap activities or plan around a birthday or anniversary.</p></details>
      <details><summary>Do you only do full packages, or can I book just a flight or hotel?</summary><p>Both. Book a single flight ticket, just a hotel, only visa help or a complete holiday, whatever you need.</p></details>
      <details><summary>What's usually not included in a package?</summary><p>Typically travel insurance, visa fees (if applicable), early check-in or late check-out charges, tips, personal expenses and meals not mentioned in the itinerary. Every quote lists the inclusions and exclusions clearly.</p></details>
      <details><summary>Can I visit your office?</summary><p>Of course. We're at {ADDRESS}. A quick call before you visit helps us make sure the right person is available.</p></details>
    </div>
  </div>
</section>
</main>
"""
    return head("Contact | Bagpack Holidays, Faridabad — +91 92060 60645",
                "Contact Bagpack Holidays: call or WhatsApp +91 92060 60645, email Bookings.bagpackholidays@gmail.com, or visit 267, Sector 17, Faridabad. Open 7 days, 10 AM to 8 PM.",
                "contact.html") + header("contact.html") + body + footer()

pages = {"index.html": home, "services.html": services, "destinations.html": destinations,
         "visa.html": visa, "about.html": about, "contact.html": contact}
for fn, f in pages.items():
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as fh:
        fh.write(f())
    print("wrote", fn)
