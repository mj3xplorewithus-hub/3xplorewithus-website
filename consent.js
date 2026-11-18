/* 3xploreWithUs — Einwilligungsbanner / consent banner
   Loads Google Analytics (GA4) only after the visitor clicks "Accept".
   Choice is stored in localStorage; "Cookie settings" in the footer reopens it. */
(function () {
  'use strict';
  var GA_ID = 'G-BJH04YSJMG';
  var KEY = '3xwu-consent-v1';
  var script = document.currentScript;
  var noBanner = !!(script && script.hasAttribute('data-no-banner'));
  var de = (document.documentElement.lang || 'en').toLowerCase().indexOf('de') === 0;

  var T = de ? {
    title: 'Cookies & Statistik',
    text: 'Wir würden gern mit Google Analytics auswerten, wie unsere Website genutzt wird. Dafür setzt Google Cookies und verarbeitet Daten wie deine IP-Adresse. Das passiert nur, wenn du zustimmst. Du kannst deine Entscheidung jederzeit über „Cookie-Einstellungen“ im Footer ändern.',
    accept: 'Akzeptieren',
    decline: 'Ablehnen',
    more: 'Datenschutzerklärung',
    settings: 'Cookie-Einstellungen'
  } : {
    title: 'Cookies & statistics',
    text: 'We would like to use Google Analytics to understand how our website is used. Google sets cookies and processes data such as your IP address for this. This only happens if you agree. You can change your choice at any time via “Cookie settings” in the footer.',
    accept: 'Accept',
    decline: 'Decline',
    more: 'Privacy Policy',
    settings: 'Cookie settings'
  };

  function getChoice() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function setChoice(v) {
    try { localStorage.setItem(KEY, v); } catch (e) {}
  }

  function loadGA() {
    if (window.__gaLoaded) { window['ga-disable-' + GA_ID] = false; return; }
    window.__gaLoaded = true;
    window['ga-disable-' + GA_ID] = false;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { anonymize_ip: true });
  }

  function deleteGACookies() {
    var host = location.hostname;
    var parts = host.split('.');
    var domains = [host, '.' + host];
    if (parts.length > 2) domains.push('.' + parts.slice(-2).join('.'));
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (name.indexOf('_ga') === 0 || name.indexOf('_gid') === 0 || name.indexOf('_gat') === 0) {
        domains.forEach(function (d) {
          document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=' + d;
        });
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
      }
    });
  }

  function disableGA() {
    window['ga-disable-' + GA_ID] = true;
    deleteGACookies();
  }

  function css() {
    if (document.getElementById('consent-css')) return;
    var st = document.createElement('style');
    st.id = 'consent-css';
    st.textContent =
      '#consent-banner{position:fixed;left:1rem;right:1rem;bottom:1rem;max-width:620px;margin:0 auto;z-index:99999;' +
      'background:#131C1C;color:#F2EEE4;border:1px solid rgba(90,200,200,.35);border-radius:6px;padding:1.2rem 1.3rem;' +
      'box-shadow:0 10px 40px rgba(0,0,0,.55);font-family:Roboto,system-ui,sans-serif;font-size:.9rem;line-height:1.55}' +
      '#consent-banner h2{font-family:ProtestStrike,system-ui,sans-serif;font-weight:400;font-size:1.05rem;letter-spacing:.03em;color:#EDD9A3;margin:0 0 .4rem}' +
      '#consent-banner p{margin:0 0 .9rem;color:#F2EEE4}' +
      '#consent-banner a{color:#5AC8C8;text-decoration:underline}' +
      '#consent-banner .cb-row{display:flex;gap:.7rem;flex-wrap:wrap}' +
      '#consent-banner button{flex:1 1 140px;cursor:pointer;font-family:ProtestStrike,system-ui,sans-serif;font-size:.8rem;letter-spacing:.08em;' +
      'text-transform:uppercase;padding:.75rem 1rem;border-radius:3px;border:1px solid #5AC8C8;background:transparent;color:#F5F2EC}' +
      '#consent-banner button:hover,#consent-banner button:focus-visible{background:#1A9090;outline:none}';
    document.head.appendChild(st);
  }

  function closeBanner() {
    var b = document.getElementById('consent-banner');
    if (b) b.parentNode.removeChild(b);
  }

  function showBanner() {
    if (document.getElementById('consent-banner')) return;
    css();
    var b = document.createElement('div');
    b.id = 'consent-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-modal', 'false');
    b.setAttribute('aria-label', T.title);
    b.innerHTML =
      '<h2>' + T.title + '</h2>' +
      '<p>' + T.text + ' <a href="datenschutz.html">' + T.more + '</a></p>' +
      '<div class="cb-row"><button type="button" data-c="decline">' + T.decline + '</button>' +
      '<button type="button" data-c="accept">' + T.accept + '</button></div>';
    b.addEventListener('click', function (e) {
      var c = e.target && e.target.getAttribute && e.target.getAttribute('data-c');
      if (c === 'accept') { setChoice('accepted'); loadGA(); closeBanner(); }
      if (c === 'decline') { setChoice('declined'); disableGA(); closeBanner(); }
    });
    document.body.appendChild(b);
  }

  function addFooterLink() {
    var ul = document.querySelector('.footer-links');
    var a = document.createElement('a');
    a.href = '#';
    a.textContent = T.settings;
    a.addEventListener('click', function (e) { e.preventDefault(); showBanner(); });
    if (ul) {
      var li = document.createElement('li');
      li.appendChild(a);
      ul.appendChild(li);
    }
  }

  function init() {
    addFooterLink();
    var choice = getChoice();
    if (choice === 'accepted') loadGA();
    else if (choice === 'declined') disableGA();
    else if (!noBanner) showBanner();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
