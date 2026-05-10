/* ── 3xploreWithUs — site-wide motion layer ────────────────────────
 * Tasteful, professional animation. No bouncing, no springs, no spin.
 * Everything keys off scroll position via IntersectionObserver, so
 * nothing animates twice and nothing animates off-screen.
 * Honors prefers-reduced-motion.
 * ----------------------------------------------------------------- */
(function () {
  'use strict';

  var prefersReduced = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ─── INJECT BASE STYLES ─────────────────────────────────────────
  var css = [
    /* Generic reveal — fade + 14px lift, decel ease */
    '[data-reveal]{opacity:0;transform:translateY(14px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1);will-change:opacity,transform;}',
    '[data-reveal].is-in{opacity:1;transform:none;}',
    /* Variant: rise from further with slight blur for hero-class type */
    '[data-reveal="major"]{transform:translateY(28px);}',
    /* Polaroids — restore the per-card rotation once revealed */
    '.story-polaroids .s-pol[data-reveal]{opacity:0;}',
    '.story-polaroids .s-pol[data-reveal].is-in{opacity:1;}',
    /* Vehicle cards — quiet stagger */
    '.v-card[data-reveal]{transform:translateY(20px) scale(.985);}',
    '.v-card[data-reveal].is-in{transform:none;}',
    /* The 40px sand rule grows in from 0 when revealed */
    '.warm-divider[data-reveal-rule]{width:0!important;transition:width .8s cubic-bezier(.2,.7,.2,1);}',
    '.warm-divider[data-reveal-rule].is-in{width:40px!important;}',
    /* Soft underline-on-hover for nav links (subtle, sand) */
    'nav .nav-links a{position:relative;}',
    'nav .nav-links a::after{content:"";position:absolute;left:0;right:0;bottom:-6px;height:1px;background:var(--sand-lt);transform:scaleX(0);transform-origin:left center;transition:transform .35s cubic-bezier(.2,.7,.2,1);}',
    'nav .nav-links a:hover::after,nav .nav-links a.active::after{transform:scaleX(1);}',
    /* Buttons — quiet press */
    '.btn{transition:transform .25s cubic-bezier(.2,.7,.2,1),opacity .25s,box-shadow .25s,border-color .25s;}',
    '.btn:active{transform:translateY(0)!important;}',
    /* Image hover — gentle zoom on figure-class wrappers */
    '.s-pol img,.team-photo img,.v-img img{transition:transform .9s cubic-bezier(.2,.7,.2,1);}',
    /* Stat numbers — count-up keeps numerics monospaced */
    '.stat-num,.tc-val{font-variant-numeric:tabular-nums;}',
    /* Photo break — subtle parallax target */
    '[data-parallax]{will-change:transform;}',
    /* Scroll progress bar — sits under the fixed nav, ~2px tall */
    '#scroll-progress{position:fixed;top:72px;left:0;height:2px;width:0;background:linear-gradient(90deg,var(--teal-lt),var(--sand-lt));z-index:199;pointer-events:none;transition:width .12s linear;}',
    /* Back-to-top — appears after scrolling past the hero */
    '#to-top{position:fixed;right:1.5rem;bottom:1.5rem;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:rgba(13,21,21,.85);backdrop-filter:blur(8px);border:1px solid rgba(237,217,163,.3);color:var(--sand-lt);cursor:pointer;opacity:0;pointer-events:none;transform:translateY(8px);transition:opacity .35s,transform .35s,background .25s,border-color .25s;z-index:198;}',
    '#to-top.is-visible{opacity:1;pointer-events:auto;transform:none;}',
    '#to-top:hover{background:rgba(13,21,21,.95);border-color:var(--sand-lt);}',
    '#to-top svg{width:16px;height:16px;}',
    /* Reduced-motion override */
    '@media (prefers-reduced-motion: reduce){[data-reveal],[data-reveal-rule]{opacity:1!important;transform:none!important;width:40px!important;}}',
  ].join('');
  var style = document.createElement('style');
  style.id = 'site-animations-css';
  style.textContent = css;
  document.head.appendChild(style);

  if (prefersReduced) return;

  // ─── BUILD CHROME — progress bar + back-to-top ──────────────────
  var bar = document.createElement('div');
  bar.id = 'scroll-progress';
  document.body.appendChild(bar);

  var top = document.createElement('button');
  top.id = 'to-top';
  top.setAttribute('aria-label', 'Back to top');
  top.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="18,15 12,9 6,15"/></svg>';
  top.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
  document.body.appendChild(top);

  function onScroll() {
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
    bar.style.width = pct + '%';
    if (window.scrollY > window.innerHeight * 0.7) top.classList.add('is-visible');
    else top.classList.remove('is-visible');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ─── AUTO-TAG ELEMENTS THAT SHOULD REVEAL ──────────────────────
  // Skip the hero and its descendants — heroes already have their
  // own entrance cascade and a custom cursor we don't want to touch.
  function inHero(el) {
    return !!el.closest('#hero, #hero-split, .hero, [data-no-reveal]');
  }

  function tag(selector, mode) {
    var nodes = document.querySelectorAll(selector);
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (inHero(el)) continue;
      if (el.hasAttribute('data-reveal')) continue;
      el.setAttribute('data-reveal', mode || '');
    }
  }

  // Headings, eyebrows, body — major
  tag('section h1, section h2, .vehicles-header h2, .map-header h2, .team-header h2, #intro h2, #our-choice h2, #steyr-cta h2, #follow h2, #title-card .site-wordmark', 'major');
  // Eyebrows / labels
  tag('.section-label, .warm-label, .family-line');
  // Body paragraphs in editorial sections
  tag('#intro p, #our-choice .choice-lead-in, #our-choice .choice-question, #our-choice .choice-anchor, #our-choice .choice-paragraph, #our-choice .choice-trio p, #our-choice .choice-closer, #steyr-cta p, #follow p, .story-body p, .vehicles-header p, .chose-truck, .vehicle-lessons .vl-item, .map-header-text');
  // Stats
  tag('.stat-item');
  // Team & vehicle cards
  tag('.team-card, .v-card');
  // Polaroids — staggered per group
  tag('.story-polaroids .s-pol');
  // The map
  tag('.map-wrap');
  // The 40px sand rules — special grow-in
  document.querySelectorAll('.warm-divider, .hero-rule').forEach(function (rule) {
    if (inHero(rule)) return;
    rule.setAttribute('data-reveal-rule', '');
  });

  // ─── STAGGER WITHIN GROUPS ─────────────────────────────────────
  function stagger(selector, base, step) {
    document.querySelectorAll(selector).forEach(function (group) {
      var kids = group.querySelectorAll('[data-reveal]');
      kids.forEach(function (k, i) {
        k.style.transitionDelay = (base + i * step) + 'ms';
      });
    });
  }
  stagger('.story-polaroids', 80, 110);
  stagger('.team-grid', 60, 90);
  stagger('.v-grid', 60, 80);
  stagger('.stats-inner', 80, 90);
  stagger('.choice-trio', 60, 130);
  stagger('.vehicle-lessons', 60, 90);

  // ─── INTERSECTION OBSERVER ─────────────────────────────────────
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      // Trigger count-up on stat numbers when their parent stat reveals
      var num = entry.target.querySelector && entry.target.querySelector('.stat-num');
      if (num && !num.dataset.counted) countUp(num);
      io.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

  document.querySelectorAll('[data-reveal], [data-reveal-rule]').forEach(function (el) {
    io.observe(el);
  });

  // ─── STAT COUNT-UP ─────────────────────────────────────────────
  function countUp(el) {
    var raw = el.textContent.trim();
    // skip the infinity glyph and anything non-numeric
    var match = raw.match(/^([\d,]+)(.*)$/);
    if (!match) return;
    el.dataset.counted = '1';
    var target = parseInt(match[1].replace(/,/g, ''), 10);
    var suffix = match[2] || '';
    if (!isFinite(target) || target <= 0) return;
    var start = performance.now();
    var dur = Math.min(1600, 700 + Math.log10(target + 1) * 250);
    function frame(now) {
      var t = Math.min(1, (now - start) / dur);
      // ease-out cubic
      var e = 1 - Math.pow(1 - t, 3);
      var v = Math.round(target * e);
      el.textContent = v.toLocaleString() + suffix;
      if (t < 1) requestAnimationFrame(frame);
      else el.textContent = target.toLocaleString() + suffix;
    }
    requestAnimationFrame(frame);
  }

  // ─── SMOOTH IN-PAGE ANCHOR JUMPS ───────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (id.length < 2) return;
      var t = document.querySelector(id);
      if (!t) return;
      e.preventDefault();
      var y = t.getBoundingClientRect().top + window.scrollY - 132;
      window.scrollTo({ top: y, behavior: 'smooth' });
    });
  });

  // ─── ACTIVE PAGE-NAV LINK ON SCROLL ────────────────────────────
  var pageLinks = document.querySelectorAll('.page-nav-link');
  if (pageLinks.length) {
    var sections = [];
    pageLinks.forEach(function (a) {
      var id = a.getAttribute('href');
      if (id && id[0] === '#') {
        var s = document.querySelector(id);
        if (s) sections.push({ link: a, el: s });
      }
    });
    function syncActive() {
      var y = window.scrollY + 180;
      var current = null;
      sections.forEach(function (s) {
        if (s.el.offsetTop <= y) current = s;
      });
      pageLinks.forEach(function (a) { a.classList.remove('is-current'); });
      if (current) current.link.classList.add('is-current');
    }
    var pn = document.createElement('style');
    pn.textContent = '.page-nav-link.is-current{color:var(--sand-lt)!important;border-bottom-color:var(--sand-lt)!important;}';
    document.head.appendChild(pn);
    window.addEventListener('scroll', syncActive, { passive: true });
    syncActive();
  }

  // ─── HOVER-LIFT ON CARDS (subtle) ──────────────────────────────
  // Adds a 2px lift to team cards & v-cards on hover for tactility.
  // Skips v-cards on the story page that already have 3D tilt.
  var hasTilt = document.querySelector('#vehicles .v-card');
  document.querySelectorAll('.team-card').forEach(function (card) {
    card.style.transition = 'transform .35s cubic-bezier(.2,.7,.2,1)';
    card.addEventListener('mouseenter', function () { card.style.transform = 'translateY(-3px)'; });
    card.addEventListener('mouseleave', function () { card.style.transform = ''; });
  });
})();
