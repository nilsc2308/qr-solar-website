# -*- coding: utf-8 -*-
"""Generator für die QR-Solar-Website: gemeinsamer Kopf/Fuß, alle Seiten, Sitemap. Aufruf: python3 _build.py"""
import json, os, datetime
OUT = os.path.dirname(os.path.abspath(__file__)) + '/'
DOMAIN = 'https://www.qr-solar.de'
TODAY = '2026-09-17'
VER = "20260917-2"
CO = dict(name='Quality Resources Global GmbH', brand='QR Solar', street='Robert-Koch-Straße 1', zip='52134', city='Herzogenrath', tel='02407 5548800', telh='+4924075548800', mail='kontakt@qr-solar.de', lat='50.8641', lon='6.0932')

MARK = '''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><circle cx="37" cy="11" r="7" fill="#eda944"/><g fill="#47a955"><path d="M8 20h10l-2 8H6z"/><path d="M20 20h10l-2 8h-10z"/><path d="M32 20h10l-2 8H30z"/><path d="M5 31h10l-2 8H3z"/><path d="M17 31h10l-2 8H15z"/><path d="M29 31h10l-2 8H27z"/></g></svg>'''
LOGO = '''<svg viewBox="0 0 250 48" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="QR Solar"><text x="0" y="36" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="36" letter-spacing="-1" fill="#eda944">QR</text><text x="58" y="36" font-family="Manrope,Arial,sans-serif" font-weight="800" font-size="36" letter-spacing="-1" fill="#47a955">Solar</text><g transform="translate(160 0) scale(.9)"><circle cx="37" cy="11" r="7" fill="#eda944"/><g fill="#47a955"><path d="M8 20h10l-2 8H6z"/><path d="M20 20h10l-2 8h-10z"/><path d="M32 20h10l-2 8H30z"/><path d="M5 31h10l-2 8H3z"/><path d="M17 31h10l-2 8H15z"/><path d="M29 31h10l-2 8H27z"/></g></g></svg>'''
LOGO_W = LOGO.replace('fill="#47a955"', 'fill="#ffffff"')
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.9 2z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'
PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>'
SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
SNOW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 2v20M2 12h20M5 5l14 14M19 5 5 19"/></svg>'
CAM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9h3l2-3h8l2 3h3v11H3z"/><circle cx="12" cy="14" r="3.5"/></svg>'

NAV = [('index.html', 'Start'), ('photovoltaik.html', 'Photovoltaik'), ('speicher-laden.html', 'Speicher & Laden'), ('warmwasser.html', 'Warmwasser mit PV'), ('angebote.html', 'Angebote'), ('referenzen.html', 'Referenzen'), ('ueber-uns.html', 'Über uns'), ('ratgeber.html', 'Ratgeber'), ('kontakt.html', 'Kontakt')]
SUB = [('faq.html', 'Häufige Fragen'), ('jobs.html', 'Jobs'), ('impressum.html', 'Impressum'), ('datenschutz.html', 'Datenschutz')]

def img(name, alt, w, h, cls='', lazy=True, sizes='(max-width: 820px) 100vw, 50vw'):
    small = 700 if w > 900 else w
    load = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ''
    return f'<img src="img/{name}.webp" srcset="img/{name}-m.webp {small}w, img/{name}.webp {w}w" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{load}{c}>'

def head(p):
    ld = [{
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": DOMAIN + "/#business", "name": CO['name'], "alternateName": "QR Solar",
        "description": "Fachbetrieb für Photovoltaik, Stromspeicher, zeitversetztes Laden und Warmwasser mit PV-Strom in Herzogenrath, Städteregion Aachen und Kreis Heinsberg.",
        "url": DOMAIN + "/", "telephone": "+49 2407 5548800", "email": CO['mail'], "image": DOMAIN + "/img/og.jpg", "logo": DOMAIN + "/favicon.svg", "priceRange": "€€",
        "address": {"@type": "PostalAddress", "streetAddress": CO['street'], "postalCode": CO['zip'], "addressLocality": CO['city'], "addressRegion": "Nordrhein-Westfalen", "addressCountry": "DE"},
        "geo": {"@type": "GeoCoordinates", "latitude": float(CO['lat']), "longitude": float(CO['lon'])},
        "areaServed": ["Herzogenrath", "Aachen", "Würselen", "Alsdorf", "Eschweiler", "Städteregion Aachen", "Kreis Heinsberg", "Rhein-Erft-Kreis"],
        "founder": [{"@type": "Person", "name": "Robert Tandetzki"}, {"@type": "Person", "name": "Frank Schreiber"}], "vatID": "DE297187579"
    }]
    if p.get('ld'): ld.append(p['ld'])
    url = DOMAIN + '/' + ('' if p['file'] == 'index.html' else p['file'])
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex, follow">' if p.get('noindex') else ''}
<meta property="og:type" content="{'article' if p.get('article') else 'website'}">
<meta property="og:site_name" content="QR Solar Herzogenrath">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#47a955">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" href="fonts/manrope-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css?v={VER}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Zum Inhalt springen</a>
<div class="curtain intro" aria-hidden="true">{LOGO_W}</div>
<div class="curtain leave" aria-hidden="true"></div>
<div class="progress" id="progress" aria-hidden="true"></div>
<nav class="rail" aria-label="Hauptnavigation">
  <a class="mark" href="index.html" aria-label="QR Solar – Startseite">{MARK}</a>
  <span class="vtext" aria-hidden="true">QR Solar · Herzogenrath</span>
  <button class="menu-btn" aria-expanded="false" aria-controls="drawer"><span class="lines"><span></span><span></span></span><span class="lbl">Menü</span></button>
  <a class="tel" href="tel:{CO['telh']}" aria-label="Anrufen: {CO['tel']}">{TEL}</a>
</nav>
<header class="head">
  <a class="logo" href="index.html" aria-label="QR Solar – Startseite">{LOGO}</a>
  <div class="right"><a class="tel" href="tel:{CO['telh']}" aria-label="Anrufen: {CO['tel']}">{TEL}</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="drawer"><span class="lbl">Menü</span><span class="lines"><span></span><span></span></span></button></div>
</header>
<div class="scrim" aria-hidden="true"></div>
<div class="drawer" id="drawer">
  <div>
    <ul>{''.join(f'<li><a href="{f}"{" class=active" if p["file"]==f or p.get("parent")==f else ""}><small>{i+1:02d}</small>{t}</a></li>' for i,(f,t) in enumerate(NAV))}</ul>
    <div class="sub">{''.join(f'<a href="{f}">{t}</a>' for f,t in SUB)}</div>
  </div>
  <div class="foot"><span>{CO['name']} · {CO['street']}, {CO['zip']} {CO['city']}</span><a href="tel:{CO['telh']}">{CO['tel']}</a><a href="mailto:{CO['mail']}">{CO['mail']}</a></div>
</div>
<main id="main">
'''

def foot(p):
    return f'''</main>
<div class="sticky-cta"><a class="btn sun" href="kontakt.html">Beratung anfragen {ARROW}</a></div>
<footer class="footer">
  <div class="wrap">
    <div class="top">
      <div class="brand">{LOGO_W}<p>Photovoltaik, Speicher und Warmwasser mit Sonnenstrom – geplant und gebaut vom lokalen Fachbetrieb in Herzogenrath.</p>
        <div class="partners"><img src="img/partner-alphaess.png" alt="Alpha ESS" height="52" loading="lazy" style="filter:none;opacity:1;background:#fff;border-radius:8px;padding:6px"><img src="img/partner-gts.png" alt="GTS New Energy" height="52" loading="lazy" style="filter:none;opacity:1;background:#fff;border-radius:8px;padding:6px"></div></div>
      <div><h4>Leistungen</h4><ul><li><a href="photovoltaik.html">Photovoltaik</a></li><li><a href="speicher-laden.html">Speicher & zeitversetztes Laden</a></li><li><a href="warmwasser.html">Warmwasser mit PV</a></li><li><a href="ratgeber-optimierer.html">Leistungsoptimierer</a></li><li><a href="ratgeber-hausanschluss.html">Hausanschluss</a></li></ul></div>
      <div><h4>Unternehmen</h4><ul><li><a href="angebote.html">Angebote</a></li><li><a href="referenzen.html">Referenzen</a></li><li><a href="ueber-uns.html">Über uns</a></li><li><a href="jobs.html">Jobs</a></li><li><a href="faq.html">Häufige Fragen</a></li><li><a href="ratgeber.html">Ratgeber</a></li></ul></div>
      <div><h4>Kontakt</h4><ul><li>{CO['name']}</li><li>{CO['street']}</li><li>{CO['zip']} {CO['city']}</li><li><a href="tel:{CO['telh']}">{CO['tel']}</a></li><li><a href="mailto:{CO['mail']}">{CO['mail']}</a></li></ul></div>
    </div>
    <div class="bottom"><span>© 2026 {CO['name']} · <a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></span><a class="totop" href="#">Nach oben <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m6 15 6-6 6 6"/></svg></a></div>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.11/dist/lenis.min.js"></script>
<script src="main.js?v={VER}"></script>
</body>
</html>
'''

def ph(title, lead, crumbs, photo=None, card=None):
    c = ' <span aria-hidden="true">/</span> '.join([f'<a href="index.html">Start</a>'] + [f'<a href="{f}">{t}</a>' for f, t in crumbs[:-1]] + [f'<span aria-current="page">{crumbs[-1][1]}</span>'])
    pic = ''
    if photo:
        pic = f'<div class="ph-photo reveal">{photo}{f"<div class=ph-card>{card}</div>" if card else ""}</div>'
    return f'''<section class="ph{'' if photo else ' no-photo'}"><div class="wrap">
  <nav class="crumbs" aria-label="Brotkrumen">{c}</nav>
  <h1 class="split">{title}</h1>
  <div class="row"><p class="lead reveal">{lead}</p>{pic}</div>
</div></section>'''

def cta(h, t, btn='Beratung anfragen', href='kontakt.html', btn2=None):
    b2 = f'<a class="btn ghost" href="{btn2[1]}">{btn2[0]}</a>' if btn2 else ''
    return f'''<section class="sec tight"><div class="wrap"><div class="cta-band reveal"><div><h2>{h}</h2><p class="lead">{t}</p></div><div class="actions"><a class="btn sun" href="{href}">{btn} {ARROW}</a>{b2}</div></div></div></section>'''

# ---------------- Referenzen (Texte von qr-solar.de) ----------------
REFS = [
    dict(t='Flachdachanlage auf Foliendach und Garagen', where='Städteregion Aachen', tags='flachdach optimierer speicher wallbox', kwp='12,32 kWp', bat='8,2 kWh', wr='Alpha ESS HI10', img=('ref-flachdach', 1800, 502), txt='Ost-West-Ausrichtung auf Foliendach und Garagen. Wegen der Aufbauten und der Modullage wurde die gesamte Fläche mit Leistungsoptimierern versehen. Wallbox mit Überschussladen.'),
    dict(t='Fassadenanlage mit Bestandsanlage', where='Städteregion Aachen', tags='fassade speicher', kwp='6,16 kWp Fassade', bat='12 kWh', wr='Solax X3-Hybrid G4', img=None, txt='Einbindung einer Bestandsanlage in das neue System, ohne diese zu verändern. Ein zusätzlicher Smartmeter zeigt die Daten korrekt in der Cloud; der Speicher wird auch aus der Bestandsanlage geladen. Gesamt ca. 8,2 kWp.'),
    dict(t='Schrägdachanlage mit Notstrom', where='Kreis Heinsberg', tags='schraegdach optimierer speicher notstrom', kwp='8,01 kWp', bat='12 kWh GTSystem', wr='Deye Sun-12K LV', img=None, txt='Verschattung durch Nachbargebäude und Kamine – die linke Solarfläche ist mit Optimierern ausgestattet. Die Anlage arbeitet auch als Notstromsystem.'),
    dict(t='Fassaden- und Schrägdachanlage', where='Städteregion Aachen', tags='fassade schraegdach optimierer speicher', kwp='9,24 kWp', bat='8,2 kWh', wr='Alpha ESS HI10', img=None, txt='Kamine, Nachbargebäude und Bäume werfen Schatten – vereinzelt eingesetzte Optimierer holen den maximalen Ertrag heraus.'),
    dict(t='Schrägdach mit Belegung auf den Gauben', where='Rhein-Erft-Kreis', tags='schraegdach optimierer speicher', kwp='6,16 kWp', bat='6 kWh', wr='Solax X3-Hybrid G4', img=('ref-rheinkreis', 1800, 646), txt='Gauben, Kamin und Satellitenschüssel können Schatten werfen, deshalb ist die gesamte Fläche mit Optimierern ausgestattet. Das Flachdachsystem auf den Gauben ist zusätzlich gegen Abrutschen gesichert.'),
    dict(t='Ost-West-Anlage auf Fertighausdach', where='Städteregion Aachen', tags='schraegdach optimierer speicher', kwp='8,9 kWp', bat='8,2 kWh', wr='Alpha ESS HI10', img=('ref-aachen', 1800, 1013), txt='Fertighausdach mit großen Sparrenabständen – die Montage wurde entsprechend angepasst. Eine Solarfläche ist mit Optimierern ausgestattet, weil das Nachbarhaus Schatten wirft.'),
    dict(t='Schrägdachanlage mit Notstrombox', where='Rhein-Kreis Neuss', tags='schraegdach speicher notstrom', kwp='7,2 kWp', bat='8,2 kWh', wr='Alpha ESS HI10 + Notstrombox Pro', img=('ref-frechen', 1800, 940), txt='Notstromfunktion, damit z. B. die elektrischen Rollläden jederzeit wieder geöffnet werden können.'),
    dict(t='Zeitversetztes Laden mit 24-kWh-Speicher', where='Städteregion Aachen', tags='schraegdach optimierer speicher wallbox notstrom', kwp='15,3 kWp', bat='24 kWh GTSystem', wr='Deye Sun 12K LV', img=None, txt='Größerer Speicher und entsprechende Solarleistung, damit das Auto abends aus dem Speicher lädt. Die vorhandenen Wallboxen mussten nicht umgebaut werden – das System liefert bis zu 12 kW. Notstrom für weite Bereiche des Hauses.'),
]

def ref_card(r):
    if r['img']:
        n, w, h = r['img']; pic = f'<div class="photo">{img(n, r["t"] + " – " + r["where"], w, h)}</div>'
    else:
        pic = f'<div class="noimg">{CAM}</div>'
    return f'''<article class="ref tilt" data-tags="{r['tags']}">{pic}<div class="body"><h3>{r['t']}</h3><div class="spec"><span>{r['kwp']}</span><span>Speicher {r['bat']}</span><span>{r['wr']}</span></div><p>{r['txt']}</p><span class="where">{r['where']}</span></div></article>'''

PACKS = [
    dict(name='Alpha ESS ohne Speicher', kwp=5.28, bat='', price=9730, items=['12 × Trinasolar Vertex S+ 440 W (TSM-NEG9RC.27), Doppelglas, schwarzer Rahmen, bifazial', 'Basis-Montagesystem', 'Alpha ESS Smile G3-S5 Wechselrichter (einphasig)', 'Montage, Anmeldung und Inbetriebnahme inklusive']),
    dict(name='Alpha ESS mit Speicher', kwp=5.28, bat='7,6 kWh Speicher (2 × Smile G3 BAT-3.8S)', price=13441, items=['12 × Trinasolar Vertex S+ 440 W, Doppelglas, schwarzer Rahmen, bifazial', 'Basis-Montagesystem', 'Alpha SMILE G3 T6 – 3-phasiger Hybrid-Wechselrichter der neuesten Generation', '2 × Batterie mit je 3,65 kWh nutzbarer Kapazität', 'Montage, Anmeldung und Inbetriebnahme inklusive']),
    dict(name='GTSystem mit Speicher', kwp=6.16, bat='12 kWh Speicher (Powerporter 12.0)', price=15646, items=['14 × Trinasolar Vertex S+ 440 W, Doppelglas, schwarzer Rahmen, bifazial', 'Basis-Montagesystem', 'GTSystem M-Powerporter-Paket: Deye Sun-12K LV, 3-phasiger Wechselrichter', 'Powerporter 12.0 Batteriespeicher', 'Montage, Anmeldung und Inbetriebnahme inklusive']),
]

# ---------------- Startseite ----------------
def planner_svg():
    # Satteldach-Fläche mit Kamin (links oben) und Gaube (rechts); 4 Reihen × 8 Module
    mods = ''
    for r in range(4):
        for c in range(8):
            x, y = 40 + c * 62, 60 + r * 50
            if r < 2 and c in (5, 6): continue  # Gaube
            shaded = ' data-shaded="1"' if (r == 2 and c == 1) else ''
            mods += f'<rect class="mod" data-row="{r}"{shaded} x="{x}" y="{y}" width="56" height="44" rx="2"/>'
    opts = ''.join(f'<circle class="opt" cx="{40 + c * 62 + 48}" cy="{60 + 2 * 50 + 8}" r="4"/>' for c in range(8))
    return f'''<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Belegungsplan eines Dachs mit Kamin und Gaube: Module, Schatten und Optimierer">
<defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a4a42"/><stop offset="1" stop-color="#3f322c"/></linearGradient></defs>
<path d="M20 40 L540 40 L560 280 L0 280 Z" fill="url(#tile)"/>
<g stroke="rgba(255,255,255,.07)">{''.join(f'<line x1="0" y1="{y}" x2="560" y2="{y}"/>' for y in range(52, 280, 12))}</g>
<rect x="350" y="52" width="120" height="96" rx="3" fill="#2a2f39"/><rect x="368" y="66" width="84" height="44" rx="2" fill="#b7d3ea"/><text x="410" y="132" font-size="11" fill="#9aa4b1" text-anchor="middle" font-family="Manrope,sans-serif" font-weight="700">Gaube</text>
<rect x="88" y="12" width="26" height="46" fill="#6b6b70"/><rect x="84" y="8" width="34" height="8" fill="#8c8c92"/>
<polygon class="shade" points="88,58 114,58 214,180 150,180" fill="#0b0f14"/>
{mods}{opts}
<text x="101" y="0" font-size="0"> </text>
</svg>'''

def home():
    packs_tabs = ''.join(f'<button role="tab" aria-selected="false"><strong>{p["name"]}</strong><span>{fmt_kwp(p["kwp"])} kWp{(" · " + p["bat"].split(" (")[0]) if p["bat"] else ""}</span></button>' for p in PACKS)
    tiles = ''.join(f'<figure class="tile">{img(n, a, w, h, sizes="(max-width: 1020px) 40vw, 22vw")}<figcaption>{a}</figcaption></figure>' for n, a, w, h in [('ref-flachdach', 'Flachdach, Städteregion Aachen', 1800, 502), ('ref-aachen', 'Ost-West, Städteregion Aachen', 1800, 1013), ('ref-rheinkreis', 'Gauben-Belegung, Rhein-Erft-Kreis', 1800, 646), ('ref-frechen', 'Schrägdach, Rhein-Kreis Neuss', 1800, 940), ('zaehler-1', 'Neuer Zählerschrank', 963, 1417), ('modul-dach', 'Modul-Montage', 1800, 1200)])
    return f'''
<section class="scene" aria-label="Einstieg">
  <div class="stage">
    <div class="layer l1">{img('stadt-abend', 'Luftaufnahme einer Stadt in der Region am Abend', 1800, 1200, lazy=False, sizes='100vw')}
      <div class="cap"><h1>Der Strom, den Sie brauchen, entsteht über Ihrem Kopf.</h1><p>Photovoltaik, Speicher und Warmwasser mit Sonnenstrom – geplant und gebaut in Herzogenrath, für die Städteregion Aachen, den Kreis Heinsberg und den Rhein-Erft-Kreis.</p></div></div>
    <div class="layer l2" data-img="img/modul-nah.webp" data-img-m="img/modul-nah-m.webp"><div class="diamonds" aria-hidden="true"></div>
      <div class="cap"><h2>Doppelglas, bifazial, schwarzer Rahmen.</h2><p>Wir verbauen Module, die auch von der Rückseite Licht sammeln und 30 Jahre auf dem Dach bleiben dürfen.</p></div></div>
    <div class="layer l3" data-img="img/ref-aachen.webp" data-img-m="img/ref-aachen-m.webp"><div class="halves" aria-hidden="true"></div>
      <div class="page" aria-hidden="true">{img('ref-aachen', '', 1800, 1013, sizes='100vw')}</div>
      <div class="cap"><h2>Ost und West statt nur Süd.</h2><p>Diese Anlage in der Städteregion Aachen liefert morgens und abends – genau dann, wenn zu Hause Strom gebraucht wird.</p></div></div>
    <div class="layer l4" style="opacity:0"><img data-src="img/monteur-dach.webp" data-srcset="img/monteur-dach-m.webp 700w, img/monteur-dach.webp 1800w" sizes="100vw" width="1800" height="1200" alt="Monteur bei der Arbeit an einem Solarmodul auf einem Dach" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==">
      <div class="cap"><h2>Handwerk und Energiewissen in einem Betrieb.</h2><p>Elektrohandwerk trifft Erfahrung aus dem Stromtarifgeschäft: Wir bauen nicht nur, wir rechnen auch.</p></div></div>
    <div class="layer l5" data-img="img/ref-frechen.webp" data-img-m="img/ref-frechen-m.webp"><div class="pixels" aria-hidden="true"></div>
      <div class="cap"><h2>Wo andere nein sagen, finden wir oft eine Lösung.</h2><p>Gauben, Kamine, Foliendächer, Fassaden – schwierige Dächer sind unser Alltag.</p></div></div>
    <div class="final"><div class="cap wrap"><h2>Sprechen wir über Ihr Dach.</h2><p>Ehrliche Beratung, gute Handwerksarbeit, Komplettpreise ohne versteckte Kosten.</p>
      <div class="actions"><a class="btn sun" href="kontakt.html">Beratung anfragen {ARROW}</a><a class="btn white" href="angebote.html">Pakete mit Preisen</a></div></div></div>
  </div>
</section>

<section class="cloud dark round" aria-label="Unser Anspruch"><div class="wrap"><p class="sentence">Wo andere nein sagen, haben wir oft eine gute Lösung für unsere Kunden.</p><p class="src">Frank Schreiber &amp; Robert Tandetzki, Gründer von QR Solar</p></div></section>

<section class="sec" id="leistungen"><div class="wrap">
  <div class="sec-head"><span class="kicker">Was wir für Sie bauen</span><h2 class="split">Drei Wege, die Sonne im Haus zu behalten.</h2></div>
  <div class="steps reveal">
    <div><b><a class="link" href="photovoltaik.html">Photovoltaik {ARROW}</a></b><p>Planung und Bau von PV-Anlagen auf Schrägdach, Flachdach und Fassade. Mit Leistungsoptimierern, wo Kamine, Gauben oder Bäume Schatten werfen. Hausanschluss auf Mindeststandard inklusive.</p></div>
    <div><b><a class="link" href="speicher-laden.html">Speicher &amp; zeitversetztes Laden {ARROW}</a></b><p>Batteriespeicher von Alpha ESS und GTSystem, auf Wunsch mit Notstrom. Unsere Lösung für alle, die tagsüber mit dem E-Auto unterwegs sind: Der Speicher lädt abends das Auto.</p></div>
    <div><b><a class="link" href="warmwasser.html">Warmwasser mit PV {ARROW}</a></b><p>Heizstab statt Einspeisung: Sonnenstrom wird zu warmem Wasser – auch als autarkes System ohne Anmeldung beim Netzbetreiber, in vielen Häusern nachrüstbar.</p></div>
  </div>
</div></section>

<section class="planner dark round" aria-label="Belegungsplaner"><div class="pin wrap">
  <div class="roof">{planner_svg()}</div>
  <div class="story">
    <div class="step"><span class="kicker">So planen wir</span><h3>Erst die Fläche: Jedes Modul bekommt seinen Platz.</h3><p>Gaube, Kamin, Dachfenster – wir belegen, was das Dach hergibt, auch in Ost-West-Ausrichtung.</p></div>
    <div class="step"><span class="kicker">Das Problem</span><h3>Ein Schatten – und die ganze Reihe bricht ein.</h3><p>Module hängen in Ketten. Ist eines verschattet, richtet sich die Leistung der ganzen Kette nach dem schwächsten Modul.</p></div>
    <div class="step"><span class="kicker">Unsere Lösung</span><h3>Optimierer: Nur das eine Modul liefert weniger.</h3><p>Leistungsoptimierer schaffen einen Bypass. Die unverschatteten Module liefern weiter volle Leistung und bleiben kühler.</p></div>
    <div class="step"><span class="kicker">Ergebnis</span><h3>Mehr Ertrag auf demselben Dach.</h3><p>Ob einzelne Module oder die ganze Fläche Optimierer bekommen, entscheiden wir nach Ihrer Einbausituation – nicht nach Katalog.</p>
      <div class="legend"><span><i style="background:#1b2a3f;border:1px solid #5b7fa8"></i>Modul</span><span><i style="background:#3a3f4a"></i>verschattet / gebremst</span><span><i style="background:#eda944;border-radius:50%"></i>Optimierer</span></div>
      <div class="actions"><a class="btn sun" href="photovoltaik.html">Mehr zu Verschattung {ARROW}</a></div></div>
  </div>
</div></section>

<section class="sec grey" id="pakete"><div class="wrap">
  <div class="sec-head"><span class="kicker">Komplettpreise</span><h2 class="split">Drei Pakete, ein Preis – inklusive Montage und Anmeldung.</h2><p class="lead reveal">Preise netto, ab. Ohne versteckte Kosten. Passt eines nicht genau, planen wir individuell.</p></div>
  <div class="packs reveal" data-packs='{json.dumps([dict(p, price=p["price"]) for p in PACKS], ensure_ascii=False)}'>
    <div class="tabs" role="tablist" aria-label="Paket wählen">{packs_tabs}</div>
    <div class="card tilt"><span class="kicker pname">Alpha ESS ohne Speicher</span><div class="kwp"><b>5,28</b><small>kWp Solarleistung</small></div><p class="bat"></p><ul></ul>
      <div class="price"><b>9.730 €</b><span>netto, ab · inkl. Montage, Anmeldung, Inbetriebnahme</span></div><p class="note">Preise laut qr-solar.de, Stand September 2026 – Änderungen vorbehalten.</p>
      <div class="actions"><a class="btn leaf" href="angebote.html">Pakete vergleichen {ARROW}</a><a class="btn ghost" href="kontakt.html?thema=angebot">Angebot anfragen</a></div><i class="fill" aria-hidden="true"></i></div>
  </div>
</div></section>

<section class="season" aria-label="Zeitversetztes Laden im Sommer und im Winter">
  <div class="pin">
    <div class="bg summer">{img('dach-orange', 'Dach mit Solarmodulen in der Sommersonne', 1800, 1200, sizes='100vw')}</div>
    <div class="bg winter">{img('sonne-wolken', 'Tiefstehende Sonne hinter Wolken', 1800, 1200, sizes='100vw')}</div>
    <div class="txt">
      <div class="main"><span class="lbl">{SUN.replace('<svg', '<i><svg', 1).replace('</svg>', '</svg></i>', 1)}Sommer bis Herbst</span><h2>Tagsüber weg, abends laden – aus dem eigenen Speicher.</h2><p>Ein 24-kWh-Speicher an einer 15-kWp-Anlage ist von Mai bis Oktober fast jeden Tag voll. Abends entlädt er mit bis zu 10 kW ins Auto – ohne teure Überschuss-Ladelösung, eine einfache Wallbox reicht.</p></div>
      <div class="alt"><span class="lbl w">{SNOW.replace('<svg', '<i><svg', 1).replace('</svg>', '</svg></i>', 1)}Winter</span><h2>Im Winter deckt der Speicher Abend und Nacht im Haus.</h2><p>Wenn die Sonne tiefer steht, versorgt der Speicher Licht, Kochen und Heizungspumpe. Das Auto lädt dann teilweise aus dem Netz – deshalb planen wir Speicher und Solarleistung von Anfang an passend zu Ihrem Fahrprofil.</p><div class="actions"><a class="btn sun" href="speicher-laden.html">So funktioniert zeitversetztes Laden {ARROW}</a></div></div>
    </div>
    <div class="meter" aria-hidden="true"><div class="tube"><div class="lvl"></div></div>Speicher</div>
  </div>
</section>

<section class="fly" aria-label="Referenzen">
  <div class="pin"><div class="tiles">{tiles}</div>
    <div class="mid"><h2>Acht Anlagen, acht schwierige Dächer.</h2><p class="lead">Foliendach, Gauben, Fassade, Fertighaus mit weiten Sparren, Notstrom für die Rollläden – jede Anlage mit ihrer eigenen Lösung.</p><div class="actions" style="justify-content:center"><a class="btn" href="referenzen.html">Alle Referenzen {ARROW}</a></div></div>
  </div>
</section>

<section class="sec ring-sec"><div class="wrap"><div class="two">
  <div class="ring reveal" data-value="14.5"><svg viewBox="0 0 200 200" aria-hidden="true"><circle class="track" cx="100" cy="100" r="86" pathLength="1"/><circle class="val" cx="100" cy="100" r="86" pathLength="1"/></svg><div class="num"><b>0 %</b><span>Anteil Solarstrom an der Stromerzeugung 2024</span></div></div>
  <div><span class="kicker">Solarenergie in Deutschland 2024</span><h2 class="split">Jede siebte Kilowattstunde kommt schon von der Sonne.</h2>
    <div class="facts"><div><b>4,75 Mio.</b><span>installierte Solaranlagen in Deutschland</span></div><div><b>72,2 Mrd. kWh</b><span>produzierter Solarstrom im Jahr 2024</span></div><div><b>14,5 %</b><span>Anteil an der Stromerzeugung</span></div></div>
    <p class="small muted" style="margin-top:16px">Zahlen laut qr-solar.de (Quelle siehe Launch-Checkliste). Solarstrom ist schadstofffrei und verursacht nach der Installation keine Treibhausgase.</p></div>
</div></div></section>

<section class="sec grey" id="anfrage"><div class="wrap"><div class="chat">
  <div class="side"><span class="kicker">In drei Fragen zum Gespräch</span><h2 class="split">Erzählen Sie uns kurz von Ihrem Dach.</h2><p class="lead">Drei Antworten reichen, damit wir wissen, worüber wir sprechen. Den Rest klären wir am Telefon oder vor Ort.</p>
    <div class="contact"><a href="tel:{CO['telh']}">{TEL}{CO['tel']}</a><a href="mailto:{CO['mail']}">{MAIL}{CO['mail']}</a><span style="display:inline-flex;gap:10px;align-items:center">{PIN}{CO['street']}, {CO['zip']} {CO['city']}</span></div></div>
  <div class="thread reveal" aria-live="polite"><div class="done"><p></p><a class="btn leaf" href="kontakt.html">Anfrage abschicken {ARROW}</a><button class="restart" type="button">Von vorn beginnen</button></div></div>
</div></div></section>
'''

def fmt_kwp(v): return f'{v:.2f}'.replace('.', ',')

# ---------------- Photovoltaik ----------------
def cmp_svg(with_opt):
    # Dachfläche mit 3 Reihen × 6 Modulen, Kamin links, Schatten; ohne Optimierer: ganze Reihe gedimmt, mit: nur ein Modul
    mods = ''
    for r in range(3):
        for c in range(6):
            x, y = 60 + c * 80, 70 + r * 66
            dim = (r == 1 and (with_opt and c == 0 or (not with_opt)))
            fill = '#3a3f4a' if dim else '#1b2a3f'
            mods += f'<rect x="{x}" y="{y}" width="72" height="58" rx="3" fill="{fill}" stroke="#5b7fa8" stroke-width="1"/>'
            if with_opt: mods += f'<circle cx="{x+62}" cy="{y+10}" r="5" fill="#eda944"/>'
    return f'''<svg viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><rect width="600" height="300" fill="#4a3d36"/><rect x="18" y="20" width="24" height="60" fill="#6b6b70"/><polygon points="18,80 42,80 150,180 100,180" fill="#0b0f14" opacity=".55"/>{mods}</svg>'''

def photovoltaik():
    body = ph('Photovoltaik für Dächer, die nicht einfach sind.', 'Schrägdach, Flachdach, Fassade, Gauben, Foliendach: Wir planen die Belegung so, dass Ihr Dach alles gibt – mit Leistungsoptimierern dort, wo Schatten fällt, und einem Hausanschluss, der für Wallbox und Wärmepumpe bereit ist.', [('photovoltaik.html', 'Photovoltaik')], img('ref-flachdach', 'Flachdachanlage auf Foliendach in der Städteregion Aachen', 1800, 502, sizes='50vw'), '<b>12,32 kWp auf Foliendach</b><span>Ost-West, gesamte Fläche mit Optimierern, Wallbox mit Überschussladen</span>')
    body += f'''
<section class="sec" id="verschattung"><div class="wrap">
  <div class="sec-head"><span class="kicker">Vorher / Nachher</span><h2 class="split">Ziehen Sie den Griff: Was ein Kamin mit der Anlage macht.</h2><p class="lead reveal">Module hängen in Reihen. Ist eines verschattet, liefert die ganze Reihe nur so viel wie das schwächste Modul. Ein Leistungsoptimierer macht einen Bypass – die Nachbarn bleiben unbeeinflusst.</p></div>
  <div class="cmp reveal" style="--x:50%"><div class="before">{cmp_svg(False)}</div><div class="after">{cmp_svg(True)}</div><span class="tag l">ohne Optimierer</span><span class="tag r">mit Optimierern</span>
    <div class="handle"><button type="button" role="slider" aria-label="Vergleich ohne und mit Optimierer" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6-6 6 6 6M15 6l6 6-6 6"/></svg></button></div></div>
  <div class="cmp-out reveal"><div><b>100 %</b><span>Leistung der mittleren Reihe ohne Optimierer (schematisch, je nach Schattenlage)</span></div><div><b>100 %</b><span>Leistung der mittleren Reihe mit Optimierern (schematisch)</span></div></div>
  <p class="small muted reveal" style="margin-top:12px">Schematische Darstellung. Wie stark ein Schatten wirkt, hängt von Tageszeit, Jahreszeit und Verschaltung ab – wir prüfen das vor Ort.</p>
</div></section>

<section class="sec dark round"><div class="wrap">
  <div class="feature"><div class="txt"><span class="kicker">Module und Montage</span><h2 class="split">Was wir aufs Dach bringen.</h2><p>Wir arbeiten mit Trinasolar-Modulen der Reihe Vertex S+ (440 W): Doppelglas, schwarzer Rahmen, bifazial – sie sammeln auch Licht von der Rückseite. Dazu ein Montagesystem, das zum Dach passt: Schrägdach mit Haken, Flachdach mit Ballast, Fassade mit eigener Unterkonstruktion.</p>
    <ul class="list"><li>Ost-West-Belegung, wenn Süd nicht reicht oder nicht passt</li><li>Fertighausdächer mit großen Sparrenabständen – Montage wird angepasst</li><li>Gauben-Belegung mit zusätzlicher Sicherung gegen Abrutschen</li><li>Bestandsanlagen werden eingebunden, ohne sie zu verändern</li></ul></div>
    <div class="photo wide reveal">{img('modul-dach', 'Solarmodul auf einem Ziegeldach', 1800, 1200)}</div></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="feature flip"><div class="txt"><span class="kicker">Hausanschluss</span><h2 class="split">Der Zählerschrank gehört dazu.</h2><p>PV-Anlage, Wallbox oder Wärmepumpe machen es oft nötig, den Hausanschluss auf einen Mindeststandard zu bringen. In vielen Fällen lässt sich der vorhandene Zählerkasten aufrüsten – die Kosten bleiben überschaubar. Manchmal muss ein neuer Zählerschrank installiert werden. Alle unsere Anlagen werden so übergeben, dass Erweiterungen später kein Problem sind.</p>
    <div class="actions"><a class="btn" href="ratgeber-hausanschluss.html">Beispiele im Ratgeber {ARROW}</a></div></div>
    <div class="photo tall reveal">{img('zaehler-1', 'Neu installierter Zählerschrank mit Smart Meter', 963, 1417)}</div></div>
</div></section>

<section class="sec grey"><div class="wrap">
  <div class="sec-head"><span class="kicker">Ablauf</span><h2 class="split">Von der Anfrage bis zum ersten eigenen Strom.</h2></div>
  <div class="steps reveal">
    <div><b>Anfrage</b><p>Sie melden sich mit Adresse und ein paar Angaben zum Dach. Wir schauen uns Luftbild und Ausrichtung an und rufen zurück.</p></div>
    <div><b>Termin vor Ort</b><p>Dach, Zählerschrank, Verschattung, Kabelwege – wir sehen uns alles an und besprechen, was Sie mit dem Strom vorhaben (Auto, Warmwasser, Notstrom).</p></div>
    <div><b>Angebot</b><p>Belegungsplan, Speichergröße, Komplettpreis mit Montage, Anmeldung und Inbetriebnahme. Keine versteckten Kosten.</p></div>
    <div><b>Montage</b><p>Unser Team montiert Unterkonstruktion, Module, Wechselrichter und Speicher; der Hausanschluss wird auf Mindeststandard gebracht.</p></div>
    <div><b>Anmeldung und Inbetriebnahme</b><p>Netzbetreiber, Marktstammdatenregister, Zählerwechsel – erledigen wir. Dann geht die Anlage ans Netz und Sie sehen Ihre Erträge in der App.</p></div>
  </div>
</div></section>
''' + cta('Wir schauen uns Ihr Dach an.', 'Vor-Ort-Termin in der Städteregion Aachen, im Kreis Heinsberg und im Rhein-Erft-Kreis.', href='kontakt.html?thema=photovoltaik', btn2=('Referenzen ansehen', 'referenzen.html'))
    return body

# ---------------- Speicher & Laden ----------------
def speicher():
    body = ph('Speicher, die auch das Auto laden.', 'Tagsüber, wenn das Dach am meisten liefert, ist das E-Auto meist unterwegs. Deshalb setzen wir auf große Batteriespeicher, die abends mit bis zu 10 kW ins Auto entladen – „zeitversetztes Laden“. Eine teure Überschuss-Ladelösung brauchen Sie dafür nicht.', [('speicher-laden.html', 'Speicher & Laden')], img('laden', 'Ladekabel wird in ein Elektroauto gesteckt', 1800, 1198, sizes='50vw'), '<b>24 kWh Speicher, 15 kWp Dach</b><span>Referenz Städteregion Aachen: Auto lädt abends aus dem Speicher, Notstrom fürs Haus</span>')
    body += f'''
<section class="sec"><div class="wrap">
  <div class="sec-head"><span class="kicker">Passt das zu mir?</span><h2 class="split">Drei Fragen – und Sie wissen, welcher Speicher sinnvoll ist.</h2></div>
  <div class="wiz reveal">
    <div class="bar"><i></i></div>
    <div class="q" data-key="E-Auto"><h3>Fahren Sie elektrisch – oder bald?</h3><div class="choices"><button type="button">Ja, ein E-Auto<small>oder Plug-in-Hybrid</small></button><button type="button">Bald<small>in den nächsten zwei Jahren</small></button><button type="button">Kein E-Auto<small>und keins geplant</small></button></div></div>
    <div class="q" data-key="Tagsüber"><h3>Steht das Auto tagsüber zu Hause?</h3><div class="choices"><button type="button">Meist unterwegs<small>Arbeit, Pendeln</small></button><button type="button">Meist zu Hause<small>Homeoffice, Schicht</small></button></div></div>
    <div class="q" data-key="Dachfläche"><h3>Wie groß ist die nutzbare Dachfläche etwa?</h3><div class="choices"><button type="button">Klein (unter 20 m²)</button><button type="button">Mittel (20–40 m²)</button><button type="button">Groß (über 40 m²)<small>oder mehrere Flächen</small></button></div></div>
    <div class="sum"><h3>Unsere Einschätzung</h3><div class="verdict"></div><dl></dl><div class="actions" style="margin-top:6px"><a class="btn leaf" href="kontakt.html?thema=speicher">Angaben mitschicken {ARROW}</a></div><button class="back" type="button">Antworten ändern</button></div>
  </div>
</div></section>

<section class="sec dark round"><div class="wrap">
  <div class="feature"><div class="txt"><span class="kicker">Zeitversetztes Laden</span><h2 class="split">Ein Beispiel aus der Praxis.</h2><p>Ein 24-kWh-Heimspeicher wird mit einer 15-kWp-Anlage kombiniert. In den Sommermonaten bis in den Herbst wird der Speicher praktisch immer voll. Mit einer Lade-/Entladeleistung von 10 kW lädt das Auto abends ohne großen Aufwand – eine einfache Wallbox reicht.</p><p>Bei vielen Fahrzeugen lässt sich die Ladeleistung in Stufen reduzieren. So stimmen Sie das Auto genau auf die Entladeleistung der Batterie ab und vermeiden Stromzukauf. Sinnvoll ist, täglich nachzuladen – der Speicher ist am nächsten Tag wieder voll.</p>
    <ul class="list"><li>Speicher: Alpha ESS Smile-Serie oder GTSystem Powerporter</li><li>Wechselrichter: Alpha ESS HI10 / SMILE G3 T6 oder Deye Sun-12K LV (3-phasig)</li><li>Notstromfunktion auf Wunsch – bis hin zu weiten Bereichen des Hauses</li><li>Wallbox mit Überschussladen, wenn das Auto tagsüber da ist</li></ul>
    <div class="actions"><a class="btn sun" href="ratgeber-zeitversetzt-laden.html">Ratgeber: zeitversetztes Laden {ARROW}</a></div></div>
    <div class="photo tall reveal">{img('elektriker', 'Elektriker installiert Verkabelung', 1800, 1202)}</div></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><span class="kicker">Notstrom</span><h2 class="split">Wenn das Netz ausfällt, gehen die Rollläden trotzdem auf.</h2><p class="lead reveal">Mit Notstrombox oder notstromfähigem Hybrid-Wechselrichter versorgt der Speicher bei Netzausfall ausgewählte Stromkreise – von den Rollläden bis zu weiten Bereichen des Hauses. Welche Kreise das sind, legen wir gemeinsam fest.</p></div>
  <div class="grid-2 reveal"><div class="photo wide">{img('zaehler-2', 'Aufgerüsteter Zählerschrank mit Umschaltung', 889, 726)}</div><div class="photo wide">{img('zaehler-3', 'Neuer Zählerschrank mit beschrifteten Sicherungen', 733, 1082)}</div></div>
</div></section>
''' + cta('Speicher, Auto, Notstrom – wir rechnen es für Ihr Haus durch.', 'Mit Ihrem Fahrprofil und Ihrem Dach statt mit Durchschnittswerten.', href='kontakt.html?thema=speicher')
    return body

# ---------------- Warmwasser ----------------
def warmwasser():
    rows = [
        ('Anmeldung beim Netzbetreiber', ['nicht nötig', 'nicht nötig', 'Anlage ist angemeldet']),
        ('Solarmodule', ['6 bis max. 10 Module', 'vorhandene Anlage', 'Teil der Gesamtanlage']),
        ('Heizelement', ['bis 3 kW pro Steuerung', '3 bis 9 kW, ggf. 3 × 3 kW für Schichtladung', 'bis 18 kW bei entsprechender Puffergröße']),
        ('Voraussetzung im Haus', ['Warmwassererzeuger mit Anschluss für Heizstab', 'freier 1,5-Zoll-Anschluss am Puffer', 'Puffergröße und Solarleistung passend'])
    ]
    cols = ['autark', 'nachruesten', 'gesamt']
    tbl = '<table class="tbl" id="ww"><thead><tr><th scope="col">Merkmal</th>' + ''.join(f'<th scope="col" class="col" data-col="{c}">{n}</th>' for c, n in zip(cols, ['Autarkes System', 'Nachrüstung', 'Mit PV-Anlage'])) + '</tr></thead><tbody>'
    for k, vs in rows:
        tbl += f'<tr><th scope="row">{k}</th>' + ''.join(f'<td class="col" data-col="{c}">{v}</td>' for c, v in zip(cols, vs)) + '</tr>'
    tbl += '</tbody></table>'
    body = ph('Warmwasser aus Sonnenstrom – statt Einspeisung.', 'Anstatt selbst erzeugten Strom für wenig Geld ins Netz zu geben, nutzen Sie ihn für Warmwasser oder Heizwärme. Das geht als Ergänzung Ihrer PV-Anlage – oder als kleines autarkes System, das nicht einmal beim Netzbetreiber angemeldet werden muss.', [('warmwasser.html', 'Warmwasser mit PV')], img('dach-orange', 'Dach mit Solarmodulen im Abendlicht', 1800, 1200, sizes='50vw'), '<b>Oft günstiger als gedacht</b><span>In vielen Häusern nachrüstbar, wenn der Speicher einen Heizstab-Anschluss hat</span>')
    body += f'''
<section class="sec"><div class="wrap">
  <div class="sec-head"><span class="kicker">Drei Wege im Vergleich</span><h2 class="split">Autark, nachgerüstet oder als Teil der Anlage.</h2><p class="lead reveal">Schalten Sie die Spalten ein und aus, um die Varianten nebeneinander zu sehen.</p></div>
  <div class="switcher reveal" data-table="#ww"><button type="button" aria-pressed="true" data-col="autark">Autarkes System</button><button type="button" aria-pressed="true" data-col="nachruesten">Nachrüstung</button><button type="button" aria-pressed="false" data-col="gesamt">Mit PV-Anlage</button></div>
  <div class="tbl-wrap reveal">{tbl}</div>
</div></section>

<section class="sec dark round"><div class="wrap"><div class="feature">
  <div class="txt"><span class="kicker">So funktioniert es</span><h2 class="split">Ein Heizstab, eine Steuerung, die Sonne.</h2><p>Die beste Voraussetzung: Ihr Warmwassererzeuger hat einen Anschluss für einen elektrischen Heizstab. In Pufferspeichern mit einem freien 1,5-Zoll-Anschluss lassen sich diese Heizelemente auch einbauen – damit ist schon bei einem großen Teil der vorhandenen Warmwassererzeuger und Puffer eine Nutzung der Sonnenenergie möglich.</p><p>Die Leistung der Heizelemente liegt zwischen 3 und 9 kW; bei Bedarf betreiben wir drei Elemente à 3 kW, um eine Schichtladung zu unterstützen. Insgesamt lässt sich ein System bis 18 kW bauen – das braucht dann aber eine entsprechende Puffergröße und Solarleistung vom Dach.</p>
    <ul class="list"><li>Autarke Systeme: Heizelemente bis 3 kW pro Steuerung, oft 6 bis 10 Module</li><li>Keine Anmeldung beim Netzbetreiber für rein autarke Warmwasser-Systeme</li><li>Die Technik ist günstiger, als man vermutet</li></ul></div>
  <div class="photo tall reveal">{img('sonne-wolken', 'Sonnenstrahlen durch Wolken', 1800, 1200)}</div>
</div></div></section>
''' + cta('Passt Ihr Warmwasserspeicher?', 'Schicken Sie uns ein Foto vom Typenschild – wir sagen Ihnen, ob sich ein Heizstab nachrüsten lässt.', href='kontakt.html?thema=warmwasser')
    return body

# ---------------- Angebote ----------------
def angebote():
    rows = [
        ('Solarleistung', ['5,28 kWp', '5,28 kWp', '6,16 kWp']),
        ('Module', ['12 × Trinasolar 440 W Vertex S+', '12 × Trinasolar 440 W Vertex S+', '14 × Trinasolar 440 W Vertex S+']),
        ('Wechselrichter', ['Alpha ESS Smile G3-S5, einphasig', 'Alpha SMILE G3 T6, 3-phasiger Hybrid', 'Deye Sun-12K LV, 3-phasig']),
        ('Speicher', ['<span class="no">ohne, nachrüstbar</span>', '<span class="ok">7,6 kWh</span> (2 × BAT-3.8S, je 3,65 kWh nutzbar)', '<span class="ok">12 kWh</span> Powerporter 12.0']),
        ('Montagesystem', ['Basis', 'Basis', 'Basis']),
        ('Montage, Anmeldung, Inbetriebnahme', ['<span class="ok">inklusive</span>', '<span class="ok">inklusive</span>', '<span class="ok">inklusive</span>']),
        ('Preis (netto, ab)', ['<strong>9.730 €</strong>', '<strong>13.441 €</strong>', '<strong>15.646 €</strong>']),
    ]
    cols = ['a', 'b', 'c']
    tbl = '<table class="tbl" id="pk"><thead><tr><th scope="col">Paket</th>' + ''.join(f'<th scope="col" class="col" data-col="{c}">{p["name"]}</th>' for c, p in zip(cols, PACKS)) + '</tr></thead><tbody>'
    for k, vs in rows:
        tbl += f'<tr><th scope="row">{k}</th>' + ''.join(f'<td class="col" data-col="{c}">{v}</td>' for c, v in zip(cols, vs)) + '</tr>'
    tbl += '</tbody></table>'
    body = ph('Komplettpreise ohne versteckte Kosten.', 'Drei Pakete mit Modulen, Wechselrichter, Montage, Anmeldung und Inbetriebnahme. Alle Preise netto, ab. Wenn Ihr Dach mehr hergibt oder anders geschnitten ist, planen wir individuell – zu denselben Bedingungen.', [('angebote.html', 'Angebote')])
    body += f'''
<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="switcher reveal" data-table="#pk"><button type="button" aria-pressed="true" data-col="a">Alpha ESS ohne Speicher</button><button type="button" aria-pressed="true" data-col="b">Alpha ESS mit Speicher</button><button type="button" aria-pressed="true" data-col="c">GTSystem mit Speicher</button></div>
  <div class="tbl-wrap reveal">{tbl}</div>
  <p class="small muted reveal" style="margin-top:14px">Preise laut qr-solar.de, Stand September 2026, zzgl. Umsatzsteuer – für private Anlagen bis 30 kWp gilt derzeit der Nullsteuersatz (§ 12 Abs. 3 UStG). Änderungen vorbehalten.</p>
</div></section>

<section class="sec dark round"><div class="wrap"><div class="two">
  <div><span class="kicker">Was immer dabei ist</span><h2 class="split">Kein Kleingedrucktes.</h2>
    <ul class="list"><li>Vor-Ort-Termin mit Belegungsplan</li><li>Montage durch unser eigenes Team</li><li>Anmeldung beim Netzbetreiber und im Marktstammdatenregister</li><li>Inbetriebnahme und Einweisung in die App</li><li>Hausanschluss auf Mindeststandard – Aufrüstung des Zählerschranks wird vorher besprochen</li></ul></div>
  <div><span class="kicker">Was individuell dazukommt</span><h2 class="split">Wenn Ihr Dach mehr will.</h2>
    <ul class="list"><li>Leistungsoptimierer für verschattete Module oder Flächen</li><li>Notstrombox oder notstromfähiger Wechselrichter</li><li>Wallbox, auf Wunsch mit Überschussladen</li><li>Heizstab und Steuerung für Warmwasser mit PV</li><li>Fassaden- oder Flachdachsysteme, Gauben-Belegung</li></ul></div>
</div></div></section>
''' + cta('Welches Paket passt zu Ihrem Dach?', 'Schicken Sie uns Ihre Adresse – wir prüfen Ausrichtung und Fläche am Luftbild und rufen zurück.', href='kontakt.html?thema=angebot')
    return body

# ---------------- Referenzen ----------------
def referenzen():
    body = ph('Referenzen aus der Region.', 'Acht Anlagen zwischen Aachen, Heinsberg, Rhein-Erft und Neuss – jede mit einer Besonderheit, die ein Standard-Angebot nicht abgedeckt hätte. Alle Hausanschlüsse wurden bei der Installation auf den neuesten Stand gebracht.', [('referenzen.html', 'Referenzen')])
    body += f'''
<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="filters reveal" role="group" aria-label="Referenzen filtern"><button type="button" aria-pressed="true" data-f="alle">Alle</button><button type="button" aria-pressed="false" data-f="schraegdach">Schrägdach</button><button type="button" aria-pressed="false" data-f="flachdach">Flachdach</button><button type="button" aria-pressed="false" data-f="fassade">Fassade</button><button type="button" aria-pressed="false" data-f="optimierer">Mit Optimierern</button><button type="button" aria-pressed="false" data-f="notstrom">Notstrom</button><button type="button" aria-pressed="false" data-f="wallbox">Wallbox</button></div>
  <div class="refs">{''.join(ref_card(r) for r in REFS)}</div>
</div></section>
''' + cta('Ihr Dach könnte das nächste sein.', 'Erzählen Sie uns, was an Ihrem Dach besonders ist – Gaube, Kamin, Bäume, Folie, Fassade.', btn2=('Pakete mit Preisen', 'angebote.html'))
    return body

# ---------------- Über uns ----------------
def ueber_uns():
    body = ph('Elektrohandwerk trifft Energiemarkt.', 'Wir sind Frank Schreiber und Robert Tandetzki, die Gründer von QR Solar. Unsere Erfahrung kommt aus zwei Bereichen, die sich ergänzen: dem Elektrohandwerk und dem Stromtarifgeschäft. Deshalb bauen wir Anlagen, die technisch sauber sind – und sich rechnen.', [('ueber-uns.html', 'Über uns')], img('monteur-dach', 'Monteur arbeitet an einem Solarmodul auf dem Dach', 1800, 1200, sizes='50vw'), '<b>Quality Resources Global GmbH</b><span>Robert-Koch-Straße 1, 52134 Herzogenrath · Handwerkskammer Aachen</span>')
    body += f'''
<section class="sec" style="padding-top:0"><div class="wrap"><div class="founders reveal">
  <div class="founder tilt"><span class="ini">RT</span><h3>Robert Tandetzki</h3><span class="role">Geschäftsführer · Elektrohandwerk</span><p>Bringt tiefgehendes Know-how aus dem Elektrohandwerk mit. Mit handwerklicher Präzision und Verständnis für technische Neuerungen sorgt er dafür, dass unsere Lösungen nicht nur effizient, sondern auch praxisnah umgesetzt werden.</p></div>
  <div class="founder tilt"><span class="ini">FS</span><h3>Frank Schreiber</h3><span class="role">Gründer · Energiemarkt</span><p>Ergänzt das Handwerk mit umfassender Erfahrung aus dem Stromtarifgeschäft. Mit klarem Blick für die Anforderungen des Energiemarktes findet er nachhaltige und wirtschaftliche Lösungen für unsere Kunden.</p></div>
</div></div></section>

<section class="sec dark round"><div class="wrap"><div class="feature">
  <div class="txt"><span class="kicker">Unser Ziel</span><h2 class="split">Die Energiewende so einfach machen wie möglich.</h2><p>Wir wollen die Energiewende aktiv mitgestalten und Ihnen den Weg zu einer umweltfreundlichen und unabhängigen Energieversorgung so einfach wie möglich machen. Wir stehen für Kompetenz, Transparenz und individuelle Beratung – von der ersten Idee bis zur Installation Ihrer Solaranlage.</p>
    <ul class="list"><li>Ehrliche Beratung: Wir sagen auch, wenn etwas nicht sinnvoll ist</li><li>Gute Handwerksarbeit – Hausanschluss immer auf aktuellem Stand</li><li>Komplettpreise ohne versteckte Kosten</li><li>Partner: Alpha ESS und GTS New Energy</li></ul>
    <div class="partners"><img src="img/partner-alphaess.png" alt="Alpha ESS" height="52" loading="lazy" style="background:#fff;border-radius:8px;padding:6px"><img src="img/partner-gts.png" alt="GTS New Energy" height="52" loading="lazy" style="background:#fff;border-radius:8px;padding:6px"></div></div>
  <div class="photo tall reveal">{img('modul-nah', 'Nahaufnahme eines Solarmoduls', 1600, 1067)}</div>
</div></div></section>

<section class="sec"><div class="wrap"><div class="two">
  <div><span class="kicker">Region</span><h2 class="split">Zu Hause in Herzogenrath, unterwegs in der ganzen Region.</h2><p class="lead">Städteregion Aachen, Kreis Heinsberg, Kreis Düren, Rhein-Erft-Kreis und Rhein-Kreis Neuss – unsere Referenzen zeigen, wie weit wir fahren.</p><div class="actions"><a class="btn" href="jobs.html">Wir suchen Verstärkung {ARROW}</a></div></div>
  <div class="map reveal"><button class="btn" type="button">Karte laden (OpenStreetMap)</button><p>Beim Laden werden Daten an OpenStreetMap übertragen.</p></div>
</div></div></section>
''' + cta('Lernen Sie uns kennen.', 'Ein Anruf genügt – oder Sie kommen in der Robert-Koch-Straße vorbei.')
    return body

# ---------------- Jobs ----------------
def jobs():
    body = ph('Arbeiten bei QR Solar.', 'Bei uns dreht sich alles um Action, echte Ergebnisse und die Energiewende. Wenn du nur einen bequemen Job suchst, bei dem du deine Zeit absitzt, bist du hier falsch. Bei uns zählen Leistung, Teamgeist und der Wille, wirklich etwas zu bewegen.', [('jobs.html', 'Jobs')], img('elektriker', 'Elektriker bei der Installation', 1800, 1202, sizes='50vw'), '<b>Elektrohandwerk & Solarmontage</b><span>Herzogenrath, Einsatz in der Region</span>')
    body += f'''
<section class="sec" style="padding-top:0"><div class="wrap"><div class="job reveal">
  <div class="box"><h3>Was QR Solar ausmacht</h3><ul class="list"><li><strong>Wir bauen die Zukunft:</strong> Solarenergie ist nicht nur ein Job, sondern eine Mission.</li><li><strong>Kein Stillstand:</strong> Langweilige Routine gibt es bei uns nicht – jeden Tag Neues lernen, Lösungen finden.</li><li><strong>Teamspirit:</strong> Keine anonyme Firma, sondern ein Team, in dem jeder dem anderen hilft.</li></ul></div>
  <div class="box"><h3>Wen wir suchen</h3><ul class="list"><li><strong>Macher und Anpacker:</strong> Du fackelst nicht lange, sondern packst an.</li><li><strong>Problemlöser:</strong> Frische Ideen und der Mut, alte Denkmuster zu durchbrechen.</li><li><strong>Teamplayer:</strong> Menschen, die das „Wir“ über das „Ich“ stellen.</li></ul></div>
  <div class="box"><h3>Was wir bieten</h3><ul class="list"><li><strong>Spannende Projekte:</strong> Von Solaranlagen auf schwierigen Dächern bis zu größeren Projekten.</li><li><strong>Entwicklung:</strong> Wir wollen, dass du wächst – beruflich und persönlich.</li><li><strong>Klare Ansage:</strong> Wer Verantwortung übernimmt, wird belohnt.</li></ul></div>
  <div class="box" style="background:var(--night);color:var(--on-night)"><h3>Bewirb dich jetzt</h3><p style="color:var(--on-night-2)">Ohne unnötigen Papierkram und ohne Ausreden: Schick uns ein paar Zeilen zu dir und was du bisher gemacht hast.</p><div class="actions"><a class="btn sun" href="mailto:{CO['mail']}?subject=Bewerbung">Bewerbung an {CO['mail']} {ARROW}</a></div></div>
</div></div></section>
'''
    return body

# ---------------- Ratgeber ----------------
POSTS = [
    dict(file='ratgeber-optimierer.html', t='Leistungsoptimierer: Wann sie sich lohnen – und wann nicht', d='2026-09-10', img=('modul-nah', 1600, 1067), teaser='Ein Baum, ein Kamin, eine Gaube – und die ganze Modulreihe bremst. Was Optimierer tun, wie wir sie planen und warum nicht jedes Dach welche braucht.'),
    dict(file='ratgeber-hausanschluss.html', t='Hausanschluss auf Mindeststandard: Was am Zählerschrank passiert', d='2026-09-03', img=('zaehler-1', 963, 1417), teaser='PV-Anlage, Wallbox oder Wärmepumpe machen oft eine Aufrüstung nötig. Drei echte Beispiele mit klickbaren Details.'),
    dict(file='ratgeber-zeitversetzt-laden.html', t='Zeitversetztes Laden: Solarstrom im Auto, obwohl es tagsüber weg ist', d='2026-08-27', img=('laden', 1800, 1198), teaser='Warum eine Überschuss-Ladelösung vielen Pendlern nichts bringt – und wie ein großer Speicher das löst. Mit einem Rechenbeispiel aus der Praxis.'),
]

def ratgeber():
    body = ph('Ratgeber: Wissenswertes aus der Praxis.', 'Keine Werbetexte, sondern das, was wir unseren Kunden am Küchentisch erklären: Verschattung, Hausanschluss, zeitversetztes Laden und Warmwasser mit Sonnenstrom.', [('ratgeber.html', 'Ratgeber')])
    body += f'''<section class="sec" style="padding-top:0"><div class="wrap"><div class="posts">{''.join(f'<a class="post reveal" href="{p["file"]}"><div class="photo">{img(p["img"][0], p["t"], p["img"][1], p["img"][2], sizes="(max-width: 1020px) 100vw, 33vw")}</div><div class="body"><time datetime="{p["d"]}">{datetime.date.fromisoformat(p["d"]).strftime("%d.%m.%Y")}</time><h3>{p["t"]}</h3><p>{p["teaser"]}</p><span class="link">Lesen {ARROW}</span></div></a>' for p in POSTS)}</div></div></section>''' + cta('Frage nicht dabei?', 'Rufen Sie an – wir erklären es lieber persönlich als in noch einem Artikel.', btn2=('Häufige Fragen', 'faq.html'))
    return body

def article(p, html):
    d = datetime.date.fromisoformat(p['d']).strftime('%d.%m.%Y')
    return f'''<section class="ph no-photo"><div class="wrap"><nav class="crumbs" aria-label="Brotkrumen"><a href="index.html">Start</a> <span aria-hidden="true">/</span> <a href="ratgeber.html">Ratgeber</a> <span aria-hidden="true">/</span> <span aria-current="page">{p['t']}</span></nav><h1 class="split">{p['t']}</h1><div class="row"><p class="lead reveal">{p['teaser']}</p></div></div></section>
<article class="article" style="padding-bottom:clamp(48px,6vw,96px)"><div class="meta"><time datetime="{p['d']}">{d}</time><span>QR Solar</span></div>{html}</article>''' + cta('Wir schauen uns das an Ihrem Haus an.', 'Vor-Ort-Termin in der Städteregion Aachen und im Kreis Heinsberg.', btn2=('Weitere Artikel', 'ratgeber.html'))

def art_optimierer():
    return article(POSTS[0], f'''
<div class="photo wide">{img('modul-nah', 'Nahaufnahme eines Solarmoduls', 1600, 1067, sizes='760px')}</div>
<h2>Warum ein Schatten die ganze Reihe bremst</h2>
<p>Oft ist es ein Baum, ein Kamin oder eine Gaube, die zu verschiedenen Zeiten Schatten auf einzelne Module oder ganze Bereiche der Fläche werfen. Wird das bei der Planung nicht berücksichtigt, kommt es zu Leistungseinbußen in der gesamten Fläche: Auch wenn nur ein Modul verschattet ist, richtet sich die maximale Leistung nach dem schwächsten Modul in der Kette.</p>
<p>Die nicht verschatteten Module werden dabei unnötig warm, verschleißen schneller und liefern deutlich weniger Strom, als eigentlich möglich wäre.</p>
<div class="note"><strong>Das Gartenschlauch-Bild:</strong> Stellen Sie sich vor, Sie gießen mit einem Schlauch. Tritt jemand – egal an welcher Stelle – auf den Schlauch, kommt vorne weniger Wasser an. Genau das passiert, elektrisch betrachtet, mit einer Solarfläche.</div>
<h2>Was Optimierer tun</h2>
<p>Leistungsoptimierer sorgen im Prinzip für einen Bypass: Das verschattete Modul wird umgangen, die maximal mögliche Leistung der übrigen Fläche bleibt erhalten, statt dass nur ein minimaler Strom fließt. Je nach Hersteller und Einbausituation versehen wir einzelne Module mit Optimierern oder statten die gesamte betroffene Fläche aus.</p>
<h2>Wie wir entscheiden</h2>
<ul><li><strong>Einzelne Module:</strong> Wenn ein Kamin oder das Nachbarhaus nur eine Ecke der Fläche trifft (Beispiel: Ost-West-Anlage auf einem Fertighausdach in der Städteregion Aachen).</li><li><strong>Ganze Fläche:</strong> Wenn Aufbauten, Gauben, Kamin und Satellitenschüssel zu verschiedenen Zeiten überall Schatten werfen (Beispiel: Flachdach auf Foliendach mit Garagen, Schrägdach mit Gauben im Rhein-Erft-Kreis).</li><li><strong>Gar keine:</strong> Auf einem freien Süddach ohne Aufbauten bringen Optimierer wenig – dann sparen wir Ihnen das Geld.</li></ul>
<h2>Was Sie davon haben</h2>
<p>Die Leistung der Anlage steigt, die Module altern gleichmäßiger, und Sie haben lange Freude an Ihrer Investition. Bei der Vor-Ort-Besichtigung schauen wir uns den Schattenwurf zu verschiedenen Tageszeiten an und legen fest, welche Module Optimierer bekommen.</p>
<p><a class="link" href="photovoltaik.html#verschattung">Zum Vorher/Nachher-Vergleich auf der Photovoltaik-Seite {ARROW}</a></p>''')

def art_hausanschluss():
    return article(POSTS[1], f'''
<p>Durch die Installation einer PV-Anlage, Wallbox oder Wärmepumpe ist es oftmals erforderlich, den Hausanschluss auf einen Mindeststandard zu bringen. In vielen Fällen kann man einen vorhandenen Zählerkasten aufrüsten – die Kosten bleiben überschaubar. Sollte es erforderlich sein, muss auch schon einmal ein neuer Zählerschrank installiert werden.</p>
<h2>Beispiel: komplett neuer Zählerschrank</h2>
<p>Tippen Sie auf die Punkte im Foto, um zu sehen, was hier eingebaut wurde.</p>
<div class="spots">{img('zaehler-1', 'Neuer Zählerschrank mit Smart Meter, Hauptschalter und PV-Umschaltung', 963, 1417, sizes='760px')}
  <button class="dot" type="button" style="left:62%;top:20%" aria-expanded="false" data-t="Sicherungen für die PV-Anlage" data-d="Eigener Abgang für Wechselrichter und Speicher, beschriftet – inklusive Hinweis zur Umschaltung bei Notstrombetrieb.">1</button>
  <button class="dot" type="button" style="left:60%;top:47%" aria-expanded="false" data-t="Moderner Messeinrichtung / Smart Meter" data-d="Der Zähler misst Bezug und Einspeisung getrennt. Der Zählerwechsel wird beim Netzbetreiber beantragt – das übernehmen wir.">2</button>
  <button class="dot" type="button" style="left:57%;top:31%" aria-expanded="false" data-t="Hauptschalter" data-d="Trennt das ganze Haus vom Netz. Vorgeschrieben bei neuen Zähleranlagen und praktisch bei jeder späteren Erweiterung.">3</button>
  <button class="dot" type="button" style="left:36%;top:78%" aria-expanded="false" data-t="Platzreserve" data-d="Freie Felder für Wallbox, Wärmepumpe oder einen späteren zweiten Stromkreis – so bleibt der Schrank erweiterbar.">4</button>
  <div class="tip" aria-live="polite"></div></div>
<h2>Beispiel: vorhandenen Zählerkasten aufrüsten</h2>
<div class="photo wide">{img('zaehler-2', 'Aufgerüsteter Zählerkasten', 889, 726, sizes='760px')}</div>
<p>Hier reichte es, den bestehenden Kasten mit neuem Zählerfeld, Hauptschalter und Überspannungsschutz auf Stand zu bringen. Die Kosten bleiben in solchen Fällen überschaubar.</p>
<h2>Beispiel: hier war ein neuer Schrank nötig</h2>
<div class="photo wide">{img('zaehler-3', 'Neu gesetzter Zählerschrank', 733, 1082, sizes='760px')}</div>
<p>Alte Anlage ohne Platz und ohne Hauptschalter – hier war ein neuer Zählerschrank die saubere Lösung. Alle unsere Hausanschlüsse sind nach der Installation auf dem neuesten Stand der Technik und damit vorbereitet für Erweiterungen wie Wallboxen oder Wärmepumpen.</p>''')

def art_laden():
    return article(POSTS[2], f'''
<div class="photo wide">{img('laden', 'Ladekabel wird in ein Elektroauto gesteckt', 1800, 1198, sizes='760px')}</div>
<h2>Das Problem der Pendler</h2>
<p>In der Regel ist man tagsüber, wenn der Stromertrag der Solaranlage am höchsten ist, mit dem Elektrofahrzeug unterwegs. Deshalb kann man in vielen Fällen den Solarstrom nicht direkt verbrauchen – er geht zu großen Teilen ins Stromnetz. Eine Wallbox mit Überschussladen bringt in dieser Situation nichts: Das Auto ist nicht da, wenn der Überschuss da ist.</p>
<h2>Unsere Lösung: zeitversetztes Laden</h2>
<p>Wir setzen entsprechend große Batteriespeicher ein, mit dem Ziel, möglichst viel selbst produzierten Strom in das Auto laden zu können. Ein kleines Beispiel zeigt, dass es über viele Monate im Jahr möglich ist, Solarstrom im eigenen Fahrzeug zu nutzen.</p>
<div class="note"><strong>Rechenbeispiel:</strong> Ein 24-kWh-Heimspeicher wird mit einer 15-kWp-Anlage kombiniert. In den Sommermonaten bis in den Herbst hinein wird der Speicher praktisch immer voll geladen. Mit einer Lade-/Entladeleistung von z. B. 10 kW kann man das Auto ohne großen Aufwand laden. Eine teure und aufwendige Überschuss-Ladelösung ist dafür nicht erforderlich – eine einfache Wallbox reicht aus.</div>
<h2>Feinabstimmung mit dem Auto</h2>
<p>Bei vielen Fahrzeugen kann man die Ladeleistung in gewissen Stufen reduzieren. Dadurch lässt sich das Fahrzeug noch genauer auf die Entladeleistung der Batterien einstellen, um einen Stromzukauf zu vermeiden. Sinnvoll ist, das Auto täglich nachzuladen, da der Speicher am nächsten Tag wieder voll wird.</p>
<h2>Was im Winter passiert</h2>
<p>Bei tiefer Sonne deckt der Speicher vor allem Abend und Nacht im Haus; das Auto lädt dann teilweise aus dem Netz. Deshalb planen wir Speichergröße und Solarleistung von Anfang an passend zu Ihrem Fahrprofil – und nicht nach Durchschnittswerten.</p>
<p><a class="link" href="speicher-laden.html">Zum Assistenten „Passt das zu mir?“ {ARROW}</a></p>''')

# ---------------- FAQ ----------------
FAQ = [
    ('Was kostet eine PV-Anlage bei QR Solar?', 'Unsere Komplettpakete beginnen bei 9.730 € netto (5,28 kWp ohne Speicher) und 13.441 € netto mit 7,6-kWh-Speicher; das GTSystem-Paket mit 6,16 kWp und 12 kWh Speicher liegt bei 15.646 € netto – jeweils inklusive Montage, Anmeldung und Inbetriebnahme. Für private Anlagen gilt derzeit der Nullsteuersatz. Individuelle Anlagen kalkulieren wir nach Vor-Ort-Termin.'),
    ('Mein Dach hat Gauben und einen Kamin – geht das trotzdem?', 'Ja, das ist unser Alltag. Wir belegen auch Gauben (mit zusätzlicher Sicherung gegen Abrutschen) und setzen Leistungsoptimierer dort ein, wo Kamin, Gaube oder Bäume Schatten werfen. So bremst ein verschattetes Modul nicht die ganze Reihe.'),
    ('Lohnt sich ein Speicher, wenn ich tagsüber nicht zu Hause bin?', 'Gerade dann. Unser Ansatz „zeitversetztes Laden“: Ein großer Speicher wird tagsüber vom Dach gefüllt und lädt abends mit bis zu 10 kW das E-Auto. Eine Überschuss-Ladelösung brauchen Sie dafür nicht – eine einfache Wallbox reicht.'),
    ('Kann meine bestehende Anlage eingebunden werden?', 'Ja. Wir haben Bestandsanlagen in neue Systeme eingebunden, ohne sie zu verändern. Ein zusätzlicher Smartmeter sorgt dafür, dass die Daten korrekt angezeigt werden und der Speicher auch aus der alten Anlage laden kann.'),
    ('Was ist mit Notstrom?', 'Mit Notstrombox oder notstromfähigem Hybrid-Wechselrichter versorgt der Speicher bei Netzausfall ausgewählte Stromkreise – von den elektrischen Rollläden bis zu weiten Bereichen des Hauses. Welche Kreise, legen wir gemeinsam fest.'),
    ('Muss mein Zählerschrank erneuert werden?', 'Nicht immer. Oft lässt sich der vorhandene Zählerkasten aufrüsten, die Kosten bleiben überschaubar. Manchmal ist ein neuer Zählerschrank nötig. Wir prüfen das beim Vor-Ort-Termin und nennen den Preis vorab.'),
    ('Was ist Warmwasser mit PV und muss ich das anmelden?', 'Ein Heizstab im Warmwasserspeicher wird mit Sonnenstrom betrieben. Als rein autarkes System (nur Warmwasser, 6 bis 10 Module) muss es nicht beim Netzbetreiber angemeldet werden. Voraussetzung ist ein Speicher mit Heizstab-Anschluss oder ein freier 1,5-Zoll-Anschluss.'),
    ('Übernehmen Sie die Anmeldung beim Netzbetreiber?', 'Ja. Netzanmeldung, Marktstammdatenregister, Zählerwechsel und Inbetriebnahme sind in unseren Paketen enthalten.'),
    ('Wo sind Sie tätig?', 'Wir sitzen in Herzogenrath und arbeiten in der Städteregion Aachen, im Kreis Heinsberg, im Kreis Düren, im Rhein-Erft-Kreis und im Rhein-Kreis Neuss.'),
    ('Welche Hersteller verbauen Sie?', 'Module von Trinasolar (Vertex S+, Doppelglas, bifazial), Speicher und Wechselrichter von Alpha ESS und GTSystem (Deye), außerdem Solax-Hybrid-Wechselrichter. Wir sind Partner von Alpha ESS und GTS New Energy.'),
]

def faq():
    body = ph('Häufige Fragen.', 'Die Fragen, die uns am Telefon am häufigsten gestellt werden – kurz beantwortet. Alles andere klären wir gern persönlich.', [('faq.html', 'Häufige Fragen')])
    body += f'''<section class="sec" style="padding-top:0"><div class="wrap narrow"><div class="faq reveal">{''.join(f'<details><summary>{q}<i>{PLUS}</i></summary><div class="a"><p>{a}</p></div></details>' for q, a in FAQ)}</div></div></section>''' + cta('Ihre Frage war nicht dabei?', 'Rufen Sie an oder schreiben Sie uns – wir antworten innerhalb von zwei Werktagen.')
    return body

# ---------------- Kontakt ----------------
def kontakt():
    body = ph('Sprechen wir über Ihr Dach.', 'Anruf, E-Mail oder das Formular – wir melden uns innerhalb von zwei Werktagen. Für ein erstes Gespräch reichen Adresse und ein Foto vom Dach oder vom Zählerschrank.', [('kontakt.html', 'Kontakt')])
    body += f'''
<section class="sec" style="padding-top:0"><div class="wrap"><div class="contact">
  <div class="info reveal">
    <div class="row"><i>{TEL}</i><div><b>Telefon</b><a href="tel:{CO['telh']}">{CO['tel']}</a></div></div>
    <div class="row"><i>{MAIL}</i><div><b>E-Mail</b><a href="mailto:{CO['mail']}">{CO['mail']}</a></div></div>
    <div class="row"><i>{PIN}</i><div><b>Adresse</b><span>{CO['name']}<br>{CO['street']}<br>{CO['zip']} {CO['city']}</span></div></div>
    <div class="map"><button class="btn" type="button">Karte laden (OpenStreetMap)</button><p>Beim Laden werden Daten an OpenStreetMap übertragen.</p></div>
    <p class="small muted">Öffnungszeiten auf Anfrage – Termine vor Ort nach Vereinbarung, auch abends.</p>
  </div>
  <form class="form reveal" name="kontakt" method="POST" action="danke.html" data-netlify="true" netlify-honeypot="firma" novalidate>
    <input type="hidden" name="form-name" value="kontakt">
    <p class="hp"><label>Firma (bitte leer lassen) <input name="firma" tabindex="-1" autocomplete="off"></label></p>
    <div class="f2"><label>Name <input name="name" required autocomplete="name"></label><label>E-Mail <input name="email" type="email" required autocomplete="email"></label></div>
    <div class="f2"><label>Telefon (optional) <input name="telefon" type="tel" autocomplete="tel"></label><label>Ort / Adresse (optional) <input name="ort" autocomplete="street-address"></label></div>
    <label>Thema <select name="thema"><option value="photovoltaik">Photovoltaik-Anlage</option><option value="speicher">Speicher / zeitversetztes Laden</option><option value="warmwasser">Warmwasser mit PV</option><option value="angebot">Angebot zu einem Paket</option><option value="erweiterung">Bestandsanlage erweitern</option><option value="sonstiges">Sonstiges</option></select></label>
    <label>Ihre Nachricht <textarea name="nachricht" required placeholder="Dachtyp, Besonderheiten (Gaube, Kamin, Bäume), Wünsche (Speicher, Auto, Notstrom) …"></textarea></label>
    <label class="check"><input type="checkbox" name="datenschutz" required> <span>Ich habe die <a href="datenschutz.html" style="text-decoration:underline">Datenschutzerklärung</a> gelesen und bin einverstanden, dass meine Angaben zur Bearbeitung der Anfrage gespeichert werden.</span></label>
    <p class="err" role="alert">Bitte füllen Sie die markierten Felder aus.</p>
    <div><button class="btn leaf" type="submit">Anfrage senden {ARROW}</button></div>
  </form>
</div></div></section>'''
    return body

def danke():
    return f'<section class="center"><div><span class="kicker">Anfrage gesendet</span><h1 class="split">Danke – wir melden uns.</h1><p class="lead">Innerhalb von zwei Werktagen rufen wir an oder antworten per E-Mail. Wenn es eilt: <a href="tel:{CO["telh"]}" style="font-weight:700">{CO["tel"]}</a>.</p><div class="actions"><a class="btn" href="index.html">Zur Startseite {ARROW}</a><a class="btn ghost" href="ratgeber.html">Ratgeber lesen</a></div></div></section>'

def err404():
    return f'<section class="center err-page"><div><span class="kicker">Fehler 404</span><h1 class="split">Diese Seite gibt es nicht.</h1><p class="lead">Vielleicht ist der Link alt – die Seiten der alten Website haben neue Adressen bekommen.</p><div class="actions"><a class="btn" href="index.html">Zur Startseite {ARROW}</a><a class="btn ghost" href="kontakt.html">Kontakt</a></div></div></section>'

def impressum():
    return f'''<section class="legal"><h1>Impressum</h1>
<p><strong>Angaben gemäß § 5 DDG</strong></p>
<p>{CO['name']}<br>{CO['street']}<br>{CO['zip']} {CO['city']}</p>
<p><strong>Vertreten durch:</strong> Robert Tandetzki (Geschäftsführer)</p>
<h2>Kontakt</h2><p>Telefon: <a href="tel:{CO['telh']}">{CO['tel']}</a><br>E-Mail: <a href="mailto:{CO['mail']}">{CO['mail']}</a></p>
<h2>Registereintrag</h2><p>Eintragung im Handelsregister.<br>Registergericht: Amtsgericht Aachen<br>Registernummer: HRB 19319</p>
<h2>Umsatzsteuer</h2><p>Umsatzsteuer-Identifikationsnummer gemäß § 27 a Umsatzsteuergesetz: DE297187579</p>
<h2>Berufsbezeichnung und Kammer</h2><p>Berufsbezeichnung: Elektroingenieur<br>Zuständige Kammer: Handwerkskammer Aachen, Sandkaulbach 21, 52062 Aachen<br>Berufsrechtliche Regelungen: Handwerksordnung (HwO), <a href="https://www.gesetze-im-internet.de/hwo/" rel="noopener" target="_blank">gesetze-im-internet.de/hwo</a></p>
<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2><p>Robert Tandetzki, Anschrift wie oben.</p>
<h2>Streitschlichtung</h2><p>Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: <a href="https://ec.europa.eu/consumers/odr/" rel="noopener" target="_blank">ec.europa.eu/consumers/odr</a>. Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte</h2><p>Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Wir sind jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt.</p>
<h2>Haftung für Links</h2><p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter verantwortlich. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>
<h2>Urheberrecht</h2><p>Die durch den Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche gekennzeichnet. Bildnachweise: eigene Aufnahmen sowie Fotos von Unsplash (Fotografen siehe <a href="img/BILDNACHWEIS.md">Bildnachweis</a>).</p>
</section>'''

def datenschutz():
    return f'''<section class="legal"><h1>Datenschutzerklärung</h1>
<div class="box">Kurz gesagt: Diese Website setzt keine Cookies, lädt keine externen Schriften und keine Analyse-Dienste. Daten fallen nur an, wenn Sie uns schreiben, anrufen oder die Karte per Klick laden.</div>
<h2>1. Verantwortlicher</h2><p>{CO['name']}, {CO['street']}, {CO['zip']} {CO['city']}, vertreten durch Robert Tandetzki. Telefon {CO['tel']}, E-Mail {CO['mail']}.</p>
<h2>2. Hosting und Server-Logfiles</h2><p>Beim Aufruf der Website verarbeitet der Hosting-Anbieter automatisch technische Daten (IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browsertyp, Referrer). Diese Daten werden zur Sicherstellung des Betriebs und der Sicherheit verarbeitet (Art. 6 Abs. 1 lit. f DSGVO) und nach kurzer Zeit gelöscht. Hosting-Anbieter: <em>[wird vor dem Start eingetragen]</em>.</p>
<h2>3. Kontaktformular, E-Mail und Telefon</h2><p>Wenn Sie uns über das Formular, per E-Mail oder telefonisch kontaktieren, verarbeiten wir Ihre Angaben (Name, E-Mail-Adresse, ggf. Telefonnummer, Adresse und Nachricht) zur Bearbeitung Ihrer Anfrage und für Anschlussfragen (Art. 6 Abs. 1 lit. b DSGVO). Die Daten werden gelöscht, sobald sie für den Zweck nicht mehr erforderlich sind und keine gesetzlichen Aufbewahrungspflichten entgegenstehen. Das Formular enthält ein verstecktes Feld zur Abwehr automatisierter Eingaben (Honeypot).</p>
<h2>4. Karte (OpenStreetMap)</h2><p>Die Karte auf der Kontaktseite wird erst geladen, wenn Sie auf „Karte laden“ klicken. Dann werden Ihre IP-Adresse und technische Daten an die OpenStreetMap Foundation (St John's Innovation Centre, Cowley Road, Cambridge, CB4 0WS, Großbritannien) übertragen (Art. 6 Abs. 1 lit. a DSGVO). Ohne Klick findet keine Übertragung statt.</p>
<h2>5. Schriften, Skripte</h2><p>Schriften werden lokal von unserem Server geladen. Die Animationsbibliotheken GSAP und Lenis werden vom Content-Delivery-Netzwerk jsDelivr (Prospect One, Krakau, Polen) geladen; dabei wird Ihre IP-Adresse an jsDelivr übertragen (Art. 6 Abs. 1 lit. f DSGVO – schnelle Auslieferung). Es werden keine Cookies gesetzt und keine Analyse- oder Werbedienste eingesetzt.</p>
<h2>6. Ihre Rechte</h2><p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21 DSGVO). Eine erteilte Einwilligung können Sie jederzeit widerrufen. Außerdem haben Sie das Recht, sich bei einer Aufsichtsbehörde zu beschweren – zuständig ist die Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Kavalleriestraße 2–4, 40213 Düsseldorf.</p>
<h2>7. Änderungen</h2><p>Wir passen diese Erklärung an, wenn sich die Website oder die Rechtslage ändert. Stand: September 2026.</p>
</section>'''

# ---------------- Seiten zusammensetzen ----------------
PAGES = [
    dict(file='index.html', title='QR Solar Herzogenrath – Photovoltaik, Speicher & Warmwasser mit PV', desc='Fachbetrieb für Photovoltaik, Batteriespeicher, zeitversetztes Laden und Warmwasser mit Sonnenstrom in Herzogenrath, Städteregion Aachen und Kreis Heinsberg.', body=home),
    dict(file='photovoltaik.html', title='Photovoltaik in Herzogenrath & Aachen – QR Solar', desc='PV-Anlagen für Schrägdach, Flachdach und Fassade – mit Leistungsoptimierern bei Verschattung und Hausanschluss auf Mindeststandard. Vorher/Nachher-Vergleich.', body=photovoltaik),
    dict(file='speicher-laden.html', title='Stromspeicher & zeitversetztes Laden – QR Solar', desc='Batteriespeicher von Alpha ESS und GTSystem, Notstrom und zeitversetztes Laden fürs E-Auto. Assistent: Passt ein Speicher zu mir?', body=speicher),
    dict(file='warmwasser.html', title='Warmwasser mit PV-Strom – QR Solar Herzogenrath', desc='Heizstab statt Einspeisung: Warmwasser und Heizwärme aus Sonnenstrom, auch als autarkes System ohne Netzanmeldung. Varianten im Vergleich.', body=warmwasser),
    dict(file='angebote.html', title='Angebote & Komplettpreise – QR Solar', desc='Drei PV-Pakete mit Preis: ab 9.730 € netto inklusive Montage, Anmeldung und Inbetriebnahme. Vergleichstabelle mit umschaltbaren Spalten.', body=angebote),
    dict(file='referenzen.html', title='Referenzen – Anlagen aus Aachen, Heinsberg & Rhein-Erft', desc='Acht PV-Anlagen mit Besonderheiten: Foliendach, Gauben, Fassade, Notstrom, 24-kWh-Speicher. Nach Dachtyp filterbar.', body=referenzen),
    dict(file='ueber-uns.html', title='Über uns – Frank Schreiber & Robert Tandetzki, QR Solar', desc='Elektrohandwerk trifft Energiemarkt: die Gründer von QR Solar in Herzogenrath, Partner von Alpha ESS und GTS New Energy.', body=ueber_uns),
    dict(file='jobs.html', title='Jobs bei QR Solar – Solarmontage & Elektrohandwerk', desc='Wir suchen Macher und Anpacker für Solaranlagen in der Region Aachen. Bewirb dich ohne unnötigen Papierkram.', body=jobs),
    dict(file='ratgeber.html', title='Ratgeber – Optimierer, Hausanschluss, zeitversetztes Laden', desc='Praxiswissen von QR Solar: Leistungsoptimierer bei Verschattung, Hausanschluss auf Mindeststandard, Solarstrom fürs E-Auto.', body=ratgeber),
    dict(file='ratgeber-optimierer.html', title='Leistungsoptimierer: Wann sie sich lohnen – QR Solar', desc='Warum ein Schatten die ganze Modulreihe bremst, was Optimierer tun und wie QR Solar entscheidet, welche Module welche bekommen.', body=art_optimierer, parent='ratgeber.html', article=True, ld={"@context": "https://schema.org", "@type": "Article", "headline": POSTS[0]['t'], "datePublished": POSTS[0]['d'], "author": {"@type": "Organization", "name": "QR Solar"}, "publisher": {"@id": DOMAIN + "/#business"}, "image": DOMAIN + "/img/modul-nah.webp"}),
    dict(file='ratgeber-hausanschluss.html', title='Hausanschluss auf Mindeststandard – Ratgeber QR Solar', desc='Was am Zählerschrank passiert, wenn PV-Anlage, Wallbox oder Wärmepumpe kommen – drei Beispiele mit klickbaren Details.', body=art_hausanschluss, parent='ratgeber.html', article=True, ld={"@context": "https://schema.org", "@type": "Article", "headline": POSTS[1]['t'], "datePublished": POSTS[1]['d'], "author": {"@type": "Organization", "name": "QR Solar"}, "publisher": {"@id": DOMAIN + "/#business"}, "image": DOMAIN + "/img/zaehler-1.webp"}),
    dict(file='ratgeber-zeitversetzt-laden.html', title='Zeitversetztes Laden: Solarstrom fürs E-Auto – QR Solar', desc='Warum Überschussladen Pendlern nichts bringt und wie ein 24-kWh-Speicher an 15 kWp das Auto abends lädt. Rechenbeispiel.', body=art_laden, parent='ratgeber.html', article=True, ld={"@context": "https://schema.org", "@type": "Article", "headline": POSTS[2]['t'], "datePublished": POSTS[2]['d'], "author": {"@type": "Organization", "name": "QR Solar"}, "publisher": {"@id": DOMAIN + "/#business"}, "image": DOMAIN + "/img/laden.webp"}),
    dict(file='faq.html', title='Häufige Fragen zu Photovoltaik & Speicher – QR Solar', desc='Kosten, Gauben und Kamine, Speicher für Pendler, Bestandsanlagen, Notstrom, Zählerschrank, Warmwasser mit PV – kurz beantwortet.', body=faq, ld={"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}),
    dict(file='kontakt.html', title='Kontakt – QR Solar, Robert-Koch-Straße 1, Herzogenrath', desc='Beratung anfragen: Telefon 02407 5548800, kontakt@qr-solar.de oder Formular. Vor-Ort-Termine in der Städteregion Aachen und im Kreis Heinsberg.', body=kontakt),
    dict(file='danke.html', title='Danke für Ihre Anfrage – QR Solar', desc='Wir melden uns innerhalb von zwei Werktagen.', body=danke, noindex=True),
    dict(file='404.html', title='Seite nicht gefunden – QR Solar', desc='Diese Seite gibt es nicht.', body=err404, noindex=True),
    dict(file='impressum.html', title='Impressum – Quality Resources Global GmbH', desc='Impressum der Quality Resources Global GmbH (QR Solar), Herzogenrath.', body=impressum),
    dict(file='datenschutz.html', title='Datenschutzerklärung – QR Solar', desc='Datenschutzerklärung der Quality Resources Global GmbH (QR Solar).', body=datenschutz),
]

for p in PAGES:
    with open(OUT + p['file'], 'w', encoding='utf-8') as f:
        f.write(head(p) + p['body']() + foot(p))

with open(OUT + 'sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{DOMAIN}/{"" if p["file"]=="index.html" else p["file"]}</loc><lastmod>{TODAY}</lastmod></url>\n' for p in PAGES if not p.get('noindex')) + '</urlset>\n')
print('ok', len(PAGES), 'Seiten')
