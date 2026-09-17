(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) document.documentElement.classList.add('no-motion');
  gsap.registerPlugin(ScrollTrigger);
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const fmt = (n, d = 0) => n.toLocaleString('de-DE', { minimumFractionDigits: d, maximumFractionDigits: d });
  const small = () => innerWidth <= 1020;

  // ---------- Lenis (weiches Scrollen) ----------
  let lenis;
  if (!reduce) {
    lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(t => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  }
  const scrollToEl = (el, off = -30) => lenis ? lenis.scrollTo(el, { offset: off, duration: 1.3 }) : el.scrollIntoView({ behavior: 'smooth' });
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const id = a.getAttribute('href'); if (id.length < 2) return;
    const el = $(id); if (!el) return;
    e.preventDefault(); closeMenu(); scrollToEl(el);
  }));

  // ---------- Schublade (Menü) ----------
  const drawer = $('#drawer'), btns = $$('.menu-btn'), scrim = $('.scrim');
  $$('li', drawer).forEach((li, i) => li.style.setProperty('--i', i));
  let lastFocus;
  const setBtns = open => btns.forEach(b => { b.setAttribute('aria-expanded', open ? 'true' : 'false'); const l = $('.lbl', b); if (l) l.textContent = open ? 'Schließen' : 'Menü'; });
  const closeMenu = () => {
    if (!drawer.classList.contains('open')) return;
    document.body.classList.remove('menu-open'); drawer.classList.remove('open'); setBtns(false);
    lenis && lenis.start(); lastFocus && lastFocus.focus();
  };
  const openMenu = () => {
    lastFocus = document.activeElement;
    document.body.classList.add('menu-open'); drawer.classList.add('open'); setBtns(true);
    lenis && lenis.stop(); setTimeout(() => $('a', drawer).focus(), 450);
  };
  btns.forEach(b => b.addEventListener('click', () => drawer.classList.contains('open') ? closeMenu() : openMenu()));
  scrim && scrim.addEventListener('click', closeMenu);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) { closeMenu(); btns[0].focus(); }
    if (e.key === 'Tab' && drawer.classList.contains('open')) { // Fokus in der Schublade halten
      const f = $$('a, button', drawer).filter(x => x.offsetParent); const first = f[0], last = f[f.length - 1];
      const vis = btns.find(b => b.offsetParent);
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); (vis || last).focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); (vis || first).focus(); }
    }
  });
  $$('a.active', drawer).forEach(a => a.setAttribute('aria-current', 'page'));

  // ---------- Wort-für-Wort-Reveals ----------
  $$('.split').forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    el.setAttribute('aria-label', words.join(' '));
    el.innerHTML = words.map(w => `<span class="split-line" aria-hidden="true"><span class="w">${w}</span></span>`).join(' ');
  });

  // ---------- Vorhang + Brand-Intro (nur beim ersten Besuch) ----------
  const intro = $('.curtain.intro');
  let seen = false; try { seen = sessionStorage.getItem('qr-intro'); } catch (e) {}
  if (intro && !seen && !reduce) {
    try { sessionStorage.setItem('qr-intro', '1'); } catch (e) {}
    document.body.classList.add('intro-on');
    setTimeout(() => document.body.classList.add('ready'), 1250);
  } else requestAnimationFrame(() => document.body.classList.add('ready'));
  $$('a[href$=".html"], a[href*=".html#"], a[href*=".html?"]').forEach(a => a.addEventListener('click', e => {
    if (e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank' || reduce) return;
    const href = a.getAttribute('href'); if (/^https?:/.test(href)) return;
    const [path] = href.split(/[#?]/), here = location.pathname.split('/').pop() || 'index.html';
    if (path === here && href.includes('#')) { const el = $('#' + href.split('#')[1]); if (el) { e.preventDefault(); closeMenu(); scrollToEl(el); return; } }
    e.preventDefault(); closeMenu(); document.body.classList.add('leaving');
    setTimeout(() => location.href = href, 560);
  }));
  addEventListener('pageshow', e => { if (e.persisted) document.body.classList.remove('leaving'); });

  // ---------- Fortschrittsbalken + Sticky-CTA ----------
  const prog = $('#progress');
  if (prog) ScrollTrigger.create({ onUpdate: s => prog.style.transform = `scaleX(${s.progress})` });
  const sticky = $('.sticky-cta');
  if (sticky) { const first = $('.scene') || $('.ph'); ScrollTrigger.create({ start: () => (first ? first.offsetHeight - innerHeight * .5 : 300), end: 'max', onToggle: t => sticky.classList.toggle('show', t.isActive) }); }
  $$('.totop').forEach(a => a.addEventListener('click', e => { e.preventDefault(); lenis ? lenis.scrollTo(0, { duration: 1.3 }) : scrollTo({ top: 0, behavior: 'smooth' }); }));

  // ---------- Magnetische Buttons + Lichtreflex, 3D-Tilt ----------
  const fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  if (fine && !reduce) {
    $$('.btn').forEach(b => {
      b.addEventListener('mousemove', e => {
        const r = b.getBoundingClientRect(); const x = e.clientX - r.left, y = e.clientY - r.top;
        b.style.setProperty('--mx', x + 'px'); b.style.setProperty('--my', y + 'px');
        gsap.to(b, { x: (x - r.width / 2) * .22, y: (y - r.height / 2) * .32, duration: .5, ease: 'power3.out' });
      });
      b.addEventListener('mouseleave', () => gsap.to(b, { x: 0, y: 0, duration: .8, ease: 'elastic.out(1,.5)' }));
    });
    $$('.tilt').forEach(c => {
      c.addEventListener('mousemove', e => { const r = c.getBoundingClientRect(); const px = (e.clientX - r.left) / r.width - .5, py = (e.clientY - r.top) / r.height - .5; gsap.to(c, { rotateY: px * 7, rotateX: -py * 7, transformPerspective: 900, duration: .5, ease: 'power2.out' }); });
      c.addEventListener('mouseleave', () => gsap.to(c, { rotateY: 0, rotateX: 0, duration: .9, ease: 'power3.out' }));
    });
  }

  // ---------- Allgemeine Scroll-Reveals ----------
  if (!reduce) {
    $$('.split').forEach(el => gsap.to($$('.w', el), { y: 0, duration: 1, ease: 'power4.out', stagger: .045, scrollTrigger: { trigger: el, start: 'top 88%' } }));
    ScrollTrigger.batch('.reveal', { start: 'top 90%', onEnter: els => gsap.to(els, { opacity: 1, y: 0, duration: 1, ease: 'power3.out', stagger: .08, overwrite: true }) });
  }

  // Wörter eines Elements einzeln umhüllen (für Szenen-Texte)
  const wrapWords = el => $$('h1, h2, h3, p', el).forEach(t => { const words = t.textContent.trim().split(/\s+/); t.setAttribute('aria-label', words.join(' ')); t.innerHTML = words.map(w => `<span class="w" aria-hidden="true">${w}</span>`).join(' '); });

  // ---------- Foto-Scroll-Through: Rautenraster, Spiegel-Split, Seiten-Umblättern, Pixel-Auflösung, Rotations-Kreuzblende ----------
  const scene = $('.scene');
  if (scene) {
    const L = i => $('.l' + i, scene); const sm = innerWidth <= 820;
    const dCols = sm ? 5 : 8, dRows = sm ? 6 : 5, pCols = sm ? 8 : 16, pRows = 10;
    $('.diamonds', L(2)).innerHTML = Array.from({ length: dCols * dRows }, (_, i) => `<i style="background-position:${(i % dCols) / (dCols - 1) * 100}% ${Math.floor(i / dCols) / (dRows - 1) * 100}%"></i>`).join('');
    $('.halves', L(3)).innerHTML = '<i></i><i></i>';
    $('.pixels', L(5)).innerHTML = Array.from({ length: pCols * pRows }, (_, i) => `<i style="background-position:${(i % pCols) / (pCols - 1) * 100}% ${Math.floor(i / pCols) / (pRows - 1) * 100}%"></i>`).join('');
    // Fotos 2–5 erst nach „load“ nachziehen
    let lateDone = false; const late = () => { if (lateDone) return; lateDone = true;
      $$('img[data-src]', scene).forEach(im => { im.srcset = im.dataset.srcset; im.src = im.dataset.src; });
      [[2, '.diamonds i'], [3, '.halves i'], [5, '.pixels i']].forEach(([n, sel]) => { const l = L(n); $$(sel, l).forEach(i => i.style.backgroundImage = `url(${sm ? l.dataset.imgM : l.dataset.img})`); }); };
    if (document.readyState === 'complete') setTimeout(late, 250); else addEventListener('load', () => setTimeout(late, 250));
    addEventListener('scroll', late, { once: true, passive: true });
    $$('.cap', scene).forEach(wrapWords);
    if (!reduce) {
      const dots = document.createElement('div'); dots.className = 'dots'; dots.setAttribute('aria-hidden', 'true'); dots.innerHTML = '<i></i>'.repeat(5); $('.stage', scene).appendChild(dots); const bars = $$('i', dots);
      const tl = gsap.timeline({ scrollTrigger: { trigger: scene, start: 'top top', end: 'bottom bottom', scrub: .6, onUpdate: s => bars.forEach((b, i) => b.style.setProperty('--p', clamp(s.progress * 5.6 - i, 0, 1))) } });
      const capIn = (c, t) => tl.set(c, { opacity: 1, visibility: 'visible' }, t).fromTo($$('.w', c), { yPercent: 36, opacity: 0 }, { yPercent: 0, opacity: 1, duration: .35, stagger: .02, ease: 'power3.out', immediateRender: false }, t);
      const capOut = (c, t) => tl.to($$('.w', c), { yPercent: -28, opacity: 0, duration: .2, stagger: .01, ease: 'power2.in' }, t).set(c, { visibility: 'hidden' }, t + .3);
      // 1: Städteregion am Abend – ruhiger Zoom
      tl.fromTo($('img', L(1)), { scale: 1.05 }, { scale: 1.16, duration: 1.1, ease: 'none' }, 0);
      capOut($('.cap', L(1)), .72);
      // 2: Rautenraster – Modul-Rauten wachsen von der Mitte nach außen
      tl.to($$('.diamonds i', L(2)), { scale: 1.02, duration: .45, stagger: { each: .012, grid: [dRows, dCols], from: 'center' }, ease: 'power2.out' }, .9);
      capIn($('.cap', L(2)), 1.35); capOut($('.cap', L(2)), 1.85);
      // 3: Spiegel-Split – obere und untere Hälfte fahren aus der Mitte auseinander
      tl.to($$('.halves i', L(3)), { scaleY: 1, duration: .55, ease: 'power3.inOut' }, 2.0)
        .set($('.halves', L(3)), { opacity: 0 }, 2.56).set($('.page', L(3)), { opacity: 1 }, 2.56);
      capIn($('.cap', L(3)), 2.5); capOut($('.cap', L(3)), 3.0);
      // 4: Seiten-Umblättern – das Blatt mit Foto 3 klappt nach links, darunter liegt Foto 4
      tl.set(L(4), { opacity: 1 }, 3.1)
        .to($('.page', L(3)), { rotateY: -180, '--shade': 1, duration: .7, ease: 'power2.inOut' }, 3.15)
        .fromTo($('img', L(4)), { scale: 1.12 }, { scale: 1.02, duration: 1, ease: 'power2.out' }, 3.2);
      capIn($('.cap', L(4)), 3.7); capOut($('.cap', L(4)), 4.2);
      // 5: Pixel-Auflösung – Blöcke des Fotos 5 erscheinen zufällig
      tl.fromTo($$('.pixels i', L(5)), { opacity: 0, scale: .6 }, { opacity: 1, scale: 1, duration: .3, stagger: { each: .006, from: 'random' }, ease: 'power1.out' }, 4.35);
      capIn($('.cap', L(5)), 4.85); capOut($('.cap', L(5)), 5.3);
      // Rotations-Kreuzblende ins Schlussbild
      tl.to($('.final', scene), { opacity: 1, visibility: 'visible', rotate: 0, scale: 1, duration: .5, ease: 'power2.out' }, 5.45);
      capIn($('.final .cap', scene), 5.7);
      tl.to({}, { duration: .5 });
    } else $$('.w', scene).forEach(w => w.style.opacity = 1);
  }

  // ---------- Wort-Wolke ordnet sich zum Satz ----------
  const cloud = $('.cloud');
  if (cloud) {
    const s = $('.sentence', cloud); const words = s.textContent.trim().split(/\s+/); s.setAttribute('aria-label', words.join(' '));
    s.innerHTML = words.map(w => `<span class="w${/nein|Lösung/.test(w) ? ' hi' : ''}" aria-hidden="true">${w}</span>`).join(' ');
    if (!reduce) {
      const ws = $$('.w', s); const R = () => (Math.random() - .5);
      ws.forEach(w => gsap.set(w, { x: R() * innerWidth * .8, y: R() * innerHeight * .7, rotate: R() * 60, opacity: 0, scale: .6 + Math.random() * .8 }));
      gsap.to(ws, { x: 0, y: 0, rotate: 0, opacity: 1, scale: 1, ease: 'power3.out', stagger: { each: .04, from: 'random' }, scrollTrigger: { trigger: cloud, start: 'top 75%', end: 'center 45%', scrub: .8 } });
    }
  }

  // ---------- Signature: Belegungsplaner ----------
  const planner = $('.planner');
  if (planner) {
    const roof = $('.roof svg', planner); const mods = $$('.mod', roof), opts = $$('.opt', roof), shade = $('.shade', roof), steps = $$('.step', planner);
    steps.forEach(wrapWords);
    if (!reduce) {
      const tl = gsap.timeline({ scrollTrigger: { trigger: planner, start: 'top top', end: 'bottom bottom', scrub: .7 } });
      const sIn = (c, t) => tl.set(c, { opacity: 1, visibility: 'visible' }, t).fromTo($$('.w', c), { yPercent: 36, opacity: 0 }, { yPercent: 0, opacity: 1, duration: .3, stagger: .015, ease: 'power3.out', immediateRender: false }, t);
      const sOut = (c, t) => tl.to($$('.w', c), { yPercent: -28, opacity: 0, duration: .18, stagger: .008, ease: 'power2.in' }, t).set(c, { visibility: 'hidden' }, t + .25);
      // 1: Module legen sich Reihe für Reihe aufs Dach
      sIn(steps[0], 0);
      tl.to(mods, { opacity: 1, y: 0, duration: .5, stagger: { each: .03, grid: 'auto', from: 'start' }, ease: 'power2.out' }, .1);
      sOut(steps[0], .95);
      // 2: Der Kamin wirft Schatten – ohne Optimierer dimmt die ganze Reihe
      sIn(steps[1], 1.2);
      tl.to(shade, { opacity: .55, duration: .3 }, 1.2).fromTo(shade, { x: -40 }, { x: 60, duration: 1.2, ease: 'none' }, 1.2)
        .to(mods.filter(m => m.dataset.row === '2'), { fill: '#3a3f4a', duration: .3 }, 1.35);
      sOut(steps[1], 2.15);
      // 3: Mit Optimierern leuchtet nur das eine Modul – der Rest liefert weiter
      sIn(steps[2], 2.4);
      tl.to(mods.filter(m => m.dataset.row === '2' && m.dataset.shaded !== '1'), { fill: '#1b2a3f', duration: .3 }, 2.45)
        .to(opts, { opacity: 1, scale: 1, duration: .3, stagger: .05, ease: 'back.out(2)' }, 2.5);
      sOut(steps[2], 3.35);
      // 4: Ergebnis
      sIn(steps[3], 3.6);
      tl.to({}, { duration: .5 });
    } else steps.forEach(c => $$('.w', c).forEach(w => w.style.opacity = 1));
  }

  // ---------- Paket-Wähler (Preise von qr-solar.de, netto, Stand Checkliste) ----------
  const packs = $('.packs');
  if (packs) {
    const data = JSON.parse(packs.dataset.packs); const tabs = $$('.tabs button', packs), card = $('.card', packs);
    const kwp = $('.kwp b', card), bat = $('.bat', card), list = $('ul', card), price = $('.price b', card), fill = $('.fill', card), name = $('.pname', card);
    const show = i => {
      const d = data[i]; tabs.forEach((t, j) => t.setAttribute('aria-selected', j === i));
      const obj = { v: parseFloat(kwp.textContent.replace(',', '.')) || 0 };
      gsap.to(obj, { v: d.kwp, duration: .6, ease: 'power2.out', onUpdate: () => kwp.textContent = fmt(obj.v, 2) });
      name.textContent = d.name; bat.textContent = d.bat || 'Ohne Speicher – jederzeit nachrüstbar';
      list.innerHTML = d.items.map(x => `<li>${x}</li>`).join('');
      const po = { v: parseFloat(price.textContent.replace(/\./g, '')) || 0 };
      gsap.to(po, { v: d.price, duration: .6, ease: 'power2.out', onUpdate: () => price.textContent = fmt(Math.round(po.v)) + ' €' });
      fill.style.setProperty('--w', (d.kwp / 6.16).toFixed(3));
      gsap.fromTo($$('li', list), { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: .4, stagger: .05, ease: 'power2.out' });
    };
    tabs.forEach((t, i) => t.addEventListener('click', () => show(i)));
    show(0);
  }

  // ---------- Sommer/Winter-Wechsel per Scroll ----------
  const season = $('.season');
  if (season) {
    const main = $('.txt > .main', season), alt = $('.txt > .alt', season); [main, alt].forEach(wrapWords);
    if (!reduce) {
      const tl = gsap.timeline({ scrollTrigger: { trigger: season, start: 'top top', end: 'bottom bottom', scrub: .8 } });
      tl.fromTo($('.meter .lvl', season), { '--h': '20%' }, { '--h': '100%', duration: .5, ease: 'none' }, 0)
        .to($$('.w', main), { yPercent: -28, opacity: 0, duration: .15, stagger: .008, ease: 'power2.in' }, .5)
        .set(main, { visibility: 'hidden' }, .7)
        .to($('.bg.winter', season), { opacity: 1, duration: .5, ease: 'power2.inOut' }, .55)
        .to($('.pin', season), { '--sky': '#cfe3f7', duration: .5 }, .55)
        .to($('.meter .lvl', season), { '--h': '45%', duration: .5, ease: 'none' }, .6)
        .set(alt, { opacity: 1, visibility: 'visible' }, .8)
        .fromTo($$('.w', alt), { yPercent: 36, opacity: 0 }, { yPercent: 0, opacity: 1, duration: .3, stagger: .012, ease: 'power3.out', immediateRender: false }, .8)
        .to({}, { duration: .3 });
    } else $$('.w', season).forEach(w => w.style.opacity = 1);
  }

  // ---------- Referenz-Kacheln: aus dem Raster in die Komposition ----------
  const fly = $('.fly');
  if (fly && !reduce) {
    const tiles = $$('.tile', fly); const n = tiles.length; const sm2 = innerWidth <= 1020;
    const place = () => {
      const W = fly.clientWidth, H = innerHeight;
      tiles.forEach((t, i) => {
        // Zielposition: Komposition rund um den Text
        // Desktop: Ellipse um den Text; Handy: je drei Kacheln oben und unten, der Text bleibt frei
        let tx, ty;
        if (sm2) { const col = i % 3, row = i < 3 ? -1 : 1; tx = (col - 1) * W * .33; ty = row * (H * .33 + (col === 1 ? 20 : 0)); }
        else { const ang = (i / n) * Math.PI * 2 - Math.PI / 2; tx = Math.cos(ang) * W * .38; ty = Math.sin(ang) * H * .36; }
        gsap.set(t, { x: 0, y: 0, scale: .3, rotate: (i % 2 ? 1 : -1) * 12, opacity: 0, left: '50%', top: '50%', xPercent: -50, yPercent: -50 });
        t.dataset.tx = tx; t.dataset.ty = ty;
      });
    };
    place();
    const tl = gsap.timeline({ scrollTrigger: { trigger: fly, start: 'top top', end: 'bottom bottom', scrub: .8, invalidateOnRefresh: true } });
    tiles.forEach((t, i) => tl.to(t, { x: () => +t.dataset.tx, y: () => +t.dataset.ty, scale: 1, rotate: (i % 3 - 1) * 4, opacity: 1, duration: .8, ease: 'power2.out' }, i * .07));
    tl.fromTo($('.mid', fly), { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: .5 }, .3).to({}, { duration: .3 });
    ScrollTrigger.addEventListener('refreshInit', place);
  }

  // ---------- Kreisdiagramm zeichnet sich ----------
  const ring = $('.ring');
  if (ring) {
    const val = $('.val', ring), num = $('.num b', ring), target = +ring.dataset.value, facts = $$('.facts div');
    if (!reduce) {
      const o = { v: 0 };
      gsap.to(o, { v: target, ease: 'power2.out', scrollTrigger: { trigger: ring, start: 'top 75%', end: 'bottom 45%', scrub: .6 }, onUpdate: () => { val.style.strokeDashoffset = 1 - o.v / 100; num.textContent = fmt(o.v, 1).replace('.', ',') + ' %'; } });
      facts.forEach((f, i) => ScrollTrigger.create({ trigger: f, start: 'top 80%', onEnter: () => f.classList.add('on'), onLeaveBack: () => f.classList.remove('on') }));
    } else { val.style.strokeDashoffset = 1 - target / 100; num.textContent = fmt(target, 1) + ' %'; }
  }

  // ---------- Chat-artige Anfrage in drei Fragen ----------
  const chat = $('.chat');
  if (chat) {
    const thread = $('.thread', chat), done = $('.done', chat), link = $('.done a.btn', chat), sum = $('.done p', chat);
    const Q = [
      { q: 'Wie sieht Ihr Dach aus?', o: ['Schrägdach', 'Flachdach', 'Fassade / gemischt', 'Weiß ich nicht'] },
      { q: 'Soll ein Speicher dazu – vielleicht auch fürs E-Auto?', o: ['Ja, mit Speicher', 'Erst einmal ohne', 'Speicher und E-Auto'] },
      { q: 'Wann soll es losgehen?', o: ['So bald wie möglich', 'In den nächsten Monaten', 'Ich informiere mich erst'] }
    ];
    const answers = []; let step = 0;
    const add = (txt, me) => { const m = document.createElement('div'); m.className = 'msg ' + (me ? 'me' : 'bot'); m.textContent = txt; thread.insertBefore(m, done); requestAnimationFrame(() => m.classList.add('show')); };
    const ask = () => {
      if (step >= Q.length) { finish(); return; }
      add(Q[step].q, false);
      const o = document.createElement('div'); o.className = 'opts';
      Q[step].o.forEach(t => { const b = document.createElement('button'); b.type = 'button'; b.textContent = t; b.addEventListener('click', () => { answers.push(t); o.remove(); add(t, true); step++; setTimeout(ask, 350); }); o.appendChild(b); });
      thread.insertBefore(o, done); requestAnimationFrame(() => o.classList.add('show'));
    };
    const finish = () => {
      add('Danke – das reicht für ein erstes Gespräch. Wir melden uns innerhalb von zwei Werktagen.', false);
      sum.textContent = `Ihre Angaben: ${answers.join(' · ')}`;
      link.href = 'kontakt.html?thema=' + encodeURIComponent(answers[1].includes('Speicher') ? 'speicher' : 'photovoltaik') + '&notiz=' + encodeURIComponent(answers.join(', '));
      done.classList.add('show');
    };
    $('.restart', chat).addEventListener('click', () => { $$('.msg, .opts', thread).forEach(x => x.remove()); done.classList.remove('show'); answers.length = 0; step = 0; ask(); });
    ScrollTrigger.create({ trigger: chat, start: 'top 75%', once: true, onEnter: ask });
  }

  // ---------- Vergleichs-Slider: Verschattung ohne / mit Optimierer ----------
  $$('.cmp').forEach(c => {
    const h = $('.handle button', c); let x = 50;
    const out = $('.cmp-out'); const set = v => { x = clamp(v, 2, 98); c.style.setProperty('--x', x + '%'); h.setAttribute('aria-valuenow', Math.round(x));
      if (out) { const ohne = 100 - Math.round(x * .55), mit = 100 - Math.round(x * .09); $$('b', out)[0].textContent = fmt(ohne) + ' %'; $$('b', out)[1].textContent = fmt(mit) + ' %'; } };
    const move = e => { const r = c.getBoundingClientRect(); const cx = (e.touches ? e.touches[0].clientX : e.clientX); set((cx - r.left) / r.width * 100); };
    let drag = false;
    h.addEventListener('pointerdown', e => { drag = true; h.setPointerCapture(e.pointerId); });
    addEventListener('pointerup', () => drag = false);
    c.addEventListener('pointermove', e => { if (drag) move(e); });
    c.addEventListener('click', e => { if (e.target !== h && !h.contains(e.target)) move(e); });
    h.addEventListener('keydown', e => { if (e.key === 'ArrowLeft') { e.preventDefault(); set(x - 4); } if (e.key === 'ArrowRight') { e.preventDefault(); set(x + 4); } if (e.key === 'Home') set(2); if (e.key === 'End') set(98); });
    set(50);
    if (!reduce) { const o = { v: 50 }; gsap.fromTo(o, { v: 8 }, { v: 62, duration: 1.6, ease: 'power3.out', onUpdate: () => set(o.v), scrollTrigger: { trigger: c, start: 'top 75%', once: true } }); }
  });

  // ---------- Schritt-für-Schritt-Assistent (Speicher & Laden) ----------
  const wiz = $('.wiz');
  if (wiz) {
    const qs = $$('.q', wiz), bar = $('.bar i', wiz), sum = $('.sum', wiz); const a = {}; let i = 0;
    const show = () => { qs.forEach((q, j) => q.classList.toggle('on', j === i)); sum.classList.toggle('on', i >= qs.length); bar.style.setProperty('--w', (Math.min(i, qs.length) / qs.length).toFixed(3)); if (i >= qs.length) result(); };
    const result = () => {
      const v = $('.verdict', sum), dl = $('dl', sum);
      dl.innerHTML = Object.entries(a).map(([k, x]) => `<dt>${k}</dt><dd>${x}</dd>`).join('');
      const car = a['E-Auto'] !== 'Kein E-Auto', away = a['Tagsüber'] === 'Meist unterwegs', roof = a['Dachfläche'];
      let txt, warn = false;
      if (car && away && roof !== 'Klein (unter 20 m²)') txt = 'Zeitversetztes Laden passt gut zu Ihnen: Das Auto ist tagsüber weg, also lohnt ein größerer Speicher, der abends ins Auto entlädt. Wir planen Speicher und Solarleistung so, dass Sie über viele Monate Ihren eigenen Strom fahren.';
      else if (car && !away) txt = 'Sie sind tagsüber oft zu Hause – dann kann das Auto direkt vom Dach laden. Ein Speicher lohnt sich trotzdem für Abend und Nacht, muss aber nicht auf das Auto ausgelegt sein.';
      else if (!car) txt = 'Ohne E-Auto reicht ein Speicher, der Abend und Nacht abdeckt. Warmwasser mit PV-Strom ist für Sie oft der bessere zweite Schritt als ein sehr großer Speicher.';
      else { txt = 'Bei kleiner Dachfläche wird ein großer Speicher selten voll. Wir schauen uns Fassade, Garage oder Carport als zusätzliche Fläche an – oft finden wir mehr, als man denkt.'; warn = true; }
      v.textContent = txt; v.classList.toggle('warn', warn);
      $('.sum a.btn', sum).href = 'kontakt.html?thema=speicher&notiz=' + encodeURIComponent(Object.entries(a).map(([k, x]) => k + ': ' + x).join(', '));
    };
    qs.forEach((q, j) => $$('button', q).forEach(b => b.addEventListener('click', () => { a[q.dataset.key] = b.dataset.v || b.firstChild.textContent.trim(); i = j + 1; show(); })));
    $('.back', wiz).addEventListener('click', () => { i = 0; show(); });
    show();
  }

  // ---------- Vergleichstabelle mit umschaltbaren Spalten ----------
  $$('.switcher').forEach(sw => {
    const tbl = $(sw.dataset.table); const bs = $$('button', sw);
    const apply = () => { const on = bs.filter(b => b.getAttribute('aria-pressed') === 'true').map(b => b.dataset.col); $$('.col', tbl).forEach(c => c.classList.toggle('on', on.includes(c.dataset.col))); };
    bs.forEach(b => b.addEventListener('click', () => { const now = b.getAttribute('aria-pressed') === 'true'; if (now && bs.filter(x => x.getAttribute('aria-pressed') === 'true').length === 1) return; b.setAttribute('aria-pressed', !now); apply(); }));
    apply();
  });

  // ---------- Filter-Galerie (Referenzen) ----------
  const filters = $('.filters');
  if (filters) {
    const bs = $$('button', filters), refs = $$('.ref');
    bs.forEach(b => b.addEventListener('click', () => {
      bs.forEach(x => x.setAttribute('aria-pressed', x === b)); const f = b.dataset.f;
      refs.forEach(r => r.classList.toggle('hide', f !== 'alle' && !r.dataset.tags.includes(f)));
      if (!reduce) gsap.fromTo(refs.filter(r => !r.classList.contains('hide')), { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: .45, stagger: .05, ease: 'power2.out' });
      ScrollTrigger.refresh();
    }));
  }

  // ---------- Klickbares Foto mit Punkten ----------
  $$('.spots').forEach(s => {
    const tip = $('.tip', s), dots = $$('.dot', s);
    dots.forEach(d => d.addEventListener('click', () => { const open = d.getAttribute('aria-expanded') === 'true'; dots.forEach(x => x.setAttribute('aria-expanded', 'false')); if (open) { tip.classList.remove('show'); return; } d.setAttribute('aria-expanded', 'true'); tip.innerHTML = `<b>${d.dataset.t}</b>${d.dataset.d}`; tip.classList.add('show'); }));
  });

  // ---------- FAQ: nur eins offen ----------
  $$('.faq details').forEach(d => d.addEventListener('toggle', () => { if (d.open) $$('.faq details').forEach(o => { if (o !== d) o.open = false; }); ScrollTrigger.refresh(); }));

  // ---------- Karte erst per Klick (OpenStreetMap) ----------
  const map = $('.map');
  if (map) $('.btn', map).addEventListener('click', () => {
    const f = document.createElement('iframe'); f.title = 'Karte: QR Solar, Robert-Koch-Straße 1, Herzogenrath'; f.loading = 'lazy';
    f.src = 'https://www.openstreetmap.org/export/embed.html?bbox=6.078%2C50.856%2C6.108%2C50.872&layer=mapnik&marker=50.8641%2C6.0932';
    map.innerHTML = ''; map.appendChild(f);
  });

  // ---------- Kontaktformular: Themen-Vorwahl per ?thema=, Notiz per ?notiz=, Prüfung vor dem Senden ----------
  const form = $('form.form');
  if (form) {
    const p = new URLSearchParams(location.search); const sel = $('select[name=thema]', form);
    if (sel && p.get('thema') && [...sel.options].some(o => o.value === p.get('thema'))) sel.value = p.get('thema');
    if (p.get('notiz')) { const t = $('textarea', form); if (t && !t.value) t.value = 'Aus der Kurz-Anfrage: ' + p.get('notiz') + '\n\n'; }
    form.addEventListener('submit', e => {
      let ok = true; $$('[required]', form).forEach(f => { const bad = f.type === 'checkbox' ? !f.checked : !f.value.trim() || (f.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.value)); f.setAttribute('aria-invalid', bad); if (bad) ok = false; });
      $('.err', form).classList.toggle('show', !ok); if (!ok) { e.preventDefault(); $('[aria-invalid=true]', form).focus(); }
    });
  }

  // Nach dem Laden aller Bilder Trigger neu berechnen
  addEventListener('load', () => ScrollTrigger.refresh());
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => ScrollTrigger.refresh());
})();
