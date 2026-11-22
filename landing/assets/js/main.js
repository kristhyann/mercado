/* Projeto GCM PHB 2027 — interações da landing page (sem dependências). */
(function () {
  'use strict';
  var doc = document.documentElement;
  doc.classList.add('js');
  var cfg = window.GCM_CONFIG || {};

  /* ---------- checkout ---------- */
  function checkoutHref() {
    var url = (cfg.checkoutUrl || '').trim();
    if (!url) return '';
    if (cfg.forwardUtm && window.location.search) {
      try {
        var target = new URL(url, window.location.href);
        new URLSearchParams(window.location.search).forEach(function (v, k) {
          if (/^(utm_|src|sck|xcod|fbclid|gclid)/i.test(k) && !target.searchParams.has(k)) target.searchParams.set(k, v);
        });
        return target.toString();
      } catch (e) { return url; }
    }
    return url;
  }

  var href = checkoutHref();
  document.querySelectorAll('[data-checkout]').forEach(function (btn) {
    if (href) {
      btn.setAttribute('href', href);
      if (cfg.openInNewTab) { btn.setAttribute('target', '_blank'); btn.setAttribute('rel', 'noopener'); }
    } else {
      btn.addEventListener('click', function (ev) {
        ev.preventDefault();
        var msg = btn.parentElement.querySelector('.checkout-msg');
        if (msg) { msg.hidden = false; msg.textContent = 'O link de pagamento ainda não foi configurado. Tente novamente em breve.'; }
        if (window.console) console.warn('[GCM] checkoutUrl vazio: configure assets/js/config.js');
      });
    }
  });

  /* ---------- links do rodapé e vendedor ---------- */
  var links = cfg.links || {};
  document.querySelectorAll('[data-link]').forEach(function (a) {
    var u = links[a.getAttribute('data-link')];
    if (u) { a.setAttribute('href', u); }
    else { a.removeAttribute('href'); a.setAttribute('aria-disabled', 'true'); a.style.opacity = '.55'; }
  });
  var seller = document.querySelector('[data-seller]');
  if (seller && cfg.seller) seller.textContent = cfg.seller;
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = String(new Date().getFullYear());

  /* ---------- animações de entrada ---------- */
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- barra fixa (mobile): aparece só depois que o visitante passa do preço do hero
     e some quando a oferta ou o CTA final estão na tela ---------- */
  var bar = document.querySelector('.stickybar');
  var heroCard = document.querySelector('.hero .price-card');
  var zones = [document.getElementById('oferta'), document.querySelector('.sec--final')];
  if (bar && heroCard) {
    var link = bar.querySelector('a');
    var ticking = false;
    var update = function () {
      ticking = false;
      var vh = window.innerHeight;
      var passedHero = heroCard.getBoundingClientRect().bottom < 0;
      var inZone = zones.some(function (z) {
        if (!z) return false;
        var r = z.getBoundingClientRect();
        return r.top < vh * 0.85 && r.bottom > vh * 0.15;
      });
      var show = passedHero && !inZone;
      bar.classList.toggle('is-visible', show);
      bar.setAttribute('aria-hidden', show ? 'false' : 'true');
      if (link) link.tabIndex = show ? 0 : -1;
    };
    var onScroll = function () { if (!ticking) { ticking = true; window.requestAnimationFrame(update); } };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  }
})();
