# Launch-Checkliste – QR Solar (Stand 17.9.2026)

Vorschau: https://nilsc2308.github.io/qr-solar-website/ · Lokal: `python3 -m http.server 8766` im Projektordner, dann http://127.0.0.1:8766

## Offene Kundenangaben (vor dem Start klären)
- [ ] **Einverständnis von QR Solar** (Robert Tandetzki / Frank Schreiber) – die Seite ist ein unbeauftragter Entwurf.
- [ ] **Fotorechte**: 4 Drohnenfotos + 3 Zählerschrank-Fotos + Partnerlogos stammen von qr-solar.de. Nutzung nur mit Freigabe des Kunden (und ggf. der Fotograf:innen).
- [ ] **Preise** der drei Pakete (netto, ab) von qr-solar.de übernommen – bestätigen lassen; Hinweis auf Nullsteuersatz prüfen.
- [ ] **Zahlen „Solarenergie 2024“** (14,5 %, 4,75 Mio., 72,2 Mrd. kWh) stehen so auf qr-solar.de – Quelle (BSW/Fraunhofer ISE/Bundesnetzagentur) beim Kunden erfragen und im Text nennen.
- [ ] **Öffnungszeiten** – auf der alten Seite nicht angegeben, derzeit „auf Anfrage“.
- [ ] **Hosting-Anbieter** in der Datenschutzerklärung (Abschnitt 2) eintragen.
- [ ] **Domain**: Canonical/OG/Sitemap zeigen auf https://www.qr-solar.de – bei anderer Domain in `_build.py` (`DOMAIN`) ändern und neu bauen.
- [ ] Assistent (Speicher & Laden) und Vergleichs-Slider sind **schematisch** – Texte vom Kunden gegenlesen lassen.
- [ ] Ratgeber-Daten (Veröffentlichungsdaten) sind Platzhalter-Daten aus September 2026.

## Recht
- [x] Impressum: Firma, Vertretung, HRB 19319 Aachen, USt-IdNr. DE297187579, HWK Aachen, Berufsbezeichnung, § 18 MStV, OS-Plattform (von qr-solar.de übernommen; § 5 TMG → § 5 DDG aktualisiert)
- [x] Datenschutz: Hosting, Formular (Honeypot), OSM-Karte per Klick, jsDelivr-CDN, Rechte, Aufsichtsbehörde NRW – Hoster fehlt (s. o.)
- [x] Kein Cookie-Banner nötig: keine Cookies, Schrift lokal, keine Analyse, Karte erst per Klick. `sessionStorage` nur für das Intro (technisch notwendig).
- [x] Google Fonts extern entfernt (alte Seite hatte sie)

## Technik
- [x] 18 Seiten, statisch, Generator `_build.py`, CSS/JS mit Version `?v=20260917-1`
- [x] Playwright Chromium + WebKit, 1400 px und 390 px, alle Seiten durchgescrollt: **0 JS-Fehler, kein horizontales Scrollen** (Stand 17.9., nach Fix von Wort-Wolke und Ratgeber-Titel)
- [x] Ladegröße bis „load“: **Desktop 396 KB, Handy 221 KB** (Ziel < 900 / < 500). Szenenfotos 2–5 werden erst nach „load“ nachgeladen.
- [x] Formular: Netlify-Forms-fertig (`data-netlify`, Honeypot `firma`), Pflichtfelder + E-Mail-Prüfung getestet, `?thema=` und `?notiz=` vorbelegen getestet, Weiterleitung auf danke.html
- [x] Interaktive Elemente getestet: Filter-Galerie (Flachdach → 1 Treffer), Assistent (3 Klicks → Einschätzung), FAQ (nur eins offen), Chat-Anfrage, Paket-Wähler, Vergleichs-Slider (Maus/Touch/Tastatur)
- [x] Link-Check: keine kaputten internen Links; extern jsDelivr, gesetze-im-internet, ec.europa.eu = 200
- [x] 404-Seite, danke.html (noindex), Weiterleitungen alter Groß-/Kleinschreibungs-URLs in netlify.toml (Angebote.html → angebote.html usw.)
- [x] Security-Header + CSP in netlify.toml (bei GitHub Pages nicht wirksam)
- [x] prefers-reduced-motion in drei Stufen (Szene wird zu Foto-Reihe, Pins aufgelöst, Reveals ohne Weg, Fokus-Ringe bleiben)
- [x] Tastatur: Skip-Link, Fokus-Ringe (orange), Menü-Fokusfalle, Slider mit Pfeiltasten, FAQ als `<details>`
- [ ] Performance mit Lighthouse am echten Hoster messen (lokal nicht aussagekräftig)

## SEO
- [x] Meta-Titel ≤ 65 Zeichen, Descriptions ≤ 155 Zeichen (Sichtprüfung), Canonical auf jeder Seite
- [x] OG-Tags + og.jpg 1200×630 (Drohnenfoto + Claim), Twitter Card
- [x] JSON-LD: LocalBusiness auf allen Seiten, FAQPage, Article (3 Ratgeber)
- [x] sitemap.xml (16 Seiten, ohne danke/404), robots.txt
- [x] favicon.svg, apple-touch-icon.png
- [x] Alt-Texte auf allen Fotos; Deko-SVGs `aria-hidden`
- [ ] Google Business Profile mit der neuen Adresse verknüpfen (Kunde)
- [ ] Nach Umzug auf die echte Domain: Search Console, Indexierung anstoßen

## Sicherung
- [x] Backup `qr-solar-web_2026-09-17.tar.gz` im Ordner „website 1“
- [x] Git-Repo + GitHub Pages (siehe oben)
