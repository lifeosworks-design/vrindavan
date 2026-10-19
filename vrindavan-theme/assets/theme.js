/* VRINDAVAN theme JS - small, deferred, no framework. Everything degrades gracefully without it. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement;
  root.classList.remove('no-js');
  root.classList.add('js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var body = document.body;

  /* ---------- drawer ---------- */
  function setDrawer(open) {
    body.classList.toggle('drawer-open', open);
    var btn = $('.menu-btn'); if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    var d = $('#drawer'); if (d) { d.setAttribute('aria-hidden', open ? 'false' : 'true'); if (open) { var f = $('a,button', d); if (f) f.focus(); } }
  }
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-drawer-open]')) setDrawer(true);
    else if (e.target.closest('[data-drawer-close]')) setDrawer(false);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { setDrawer(false); var sp = $('.search-panel.open'); if (sp) sp.classList.remove('open'); }
  });

  /* ---------- search panel + predictive suggestions ---------- */
  var sp = $('.search-panel'), sInput = sp && $('input[name=q]', sp), sBox = sp && $('.suggest', sp), sTimer;
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-search-toggle]');
    if (t && sp) { sp.classList.toggle('open'); if (sp.classList.contains('open') && sInput) sInput.focus(); }
    else if (sBox && sp && !sp.contains(e.target)) sBox.hidden = true;
  });
  if (sInput && sBox) {
    sInput.addEventListener('input', function () {
      clearTimeout(sTimer);
      var v = sInput.value.trim();
      if (v.length < 2) { sBox.hidden = true; return; }
      sTimer = setTimeout(function () {
        var url = (window.theme && theme.routes.predictiveSearch ? theme.routes.predictiveSearch : '/search/suggest') + '.json?q=' + encodeURIComponent(v) + '&resources[type]=product,collection&resources[limit]=6';
        fetch(url, { headers: { Accept: 'application/json' } })
          .then(function (r) { return r.ok ? r.json() : null; })
          .then(function (d) {
            sBox.textContent = '';
            var res = d && d.resources && d.resources.results ? d.resources.results : {};
            var items = [].concat(res.products || [], res.collections || []);
            if (!items.length) { sBox.hidden = true; return; }
            items.forEach(function (it) {
              var a = document.createElement('a'); a.href = it.url;
              var s1 = document.createElement('span'); s1.textContent = it.title;
              var s2 = document.createElement('small'); s2.textContent = it.price ? (window.theme ? theme.formatMoney(it.price) : it.price) : 'Collection';
              a.appendChild(s1); a.appendChild(s2); sBox.appendChild(a);
            });
            sBox.hidden = false;
          }).catch(function () { sBox.hidden = true; });
      }, 220);
    });
  }

  /* ---------- wishlist (stored in this browser; no app needed) ---------- */
  var WL_KEY = 'vr_wishlist';
  function wlGet() { try { return JSON.parse(localStorage.getItem(WL_KEY) || '[]'); } catch (e) { return []; } }
  function wlSet(a) { try { localStorage.setItem(WL_KEY, JSON.stringify(a.slice(0, 100))); } catch (e) {} wlRender(); }
  function wlRender() {
    var list = wlGet();
    $$('[data-wish]').forEach(function (b) {
      var on = list.indexOf(b.dataset.wish) > -1;
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.setAttribute('aria-label', on ? 'Remove from wishlist' : 'Add to wishlist');
    });
    var c = $('[data-wish-count]'); if (c) { c.textContent = list.length; c.hidden = !list.length; }
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-wish]'); if (!b) return;
    e.preventDefault();
    var list = wlGet(), h = b.dataset.wish, i = list.indexOf(h);
    if (i > -1) list.splice(i, 1); else list.push(h);
    wlSet(list);
    if (b.closest('[data-wishlist-grid]') && i > -1) { var card = b.closest('.card'); if (card) card.remove(); wlEmpty(); }
  });
  function wlEmpty() { var g = $('[data-wishlist-grid]'), e = $('[data-wishlist-empty]'); if (g && e) e.hidden = !!g.children.length; }
  wlRender();
  var wg = $('[data-wishlist-grid]');
  if (wg) {
    var handles = wlGet();
    if (!handles.length) { wlEmpty(); }
    handles.forEach(function (h) {
      fetch('/products/' + encodeURIComponent(h) + '?view=card')
        .then(function (r) { return r.ok ? r.text() : ''; })
        .then(function (html) { if (html.trim()) { var d = document.createElement('div'); d.innerHTML = html.trim(); while (d.firstChild) wg.appendChild(d.firstChild); wlRender(); } wlEmpty(); });
    });
  }

  /* ---------- filters dialog ---------- */
  var fd = $('dialog.filters');
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-filters-open]') && fd && fd.showModal) fd.showModal();
    else if (e.target.closest('[data-filters-close]') && fd) fd.close();
    else if (e.target === fd) fd.close();
  });

  /* ---------- product gallery ---------- */
  var track = $('.gallery-track');
  if (track) {
    var slides = $$('.gallery-slide', track), dots = $$('.dots i'), thumbs = $$('.thumbs button');
    var activate = function (i) {
      slides.forEach(function (s, n) { s.classList.toggle('active', n === i); });
      dots.forEach(function (d, n) { d.classList.toggle('on', n === i); });
      thumbs.forEach(function (t, n) { t.classList.toggle('on', n === i); });
    };
    activate(0);
    thumbs.forEach(function (t, n) { t.addEventListener('click', function () { activate(n); }); });
    var tick;
    track.addEventListener('scroll', function () {
      clearTimeout(tick);
      tick = setTimeout(function () {
        var w = slides[0] ? slides[0].getBoundingClientRect().width + 8 : 1;
        var i = Math.max(0, Math.min(slides.length - 1, Math.round(track.scrollLeft / w)));
        dots.forEach(function (d, n) { d.classList.toggle('on', n === i); });
      }, 60);
    }, { passive: true });
  }

  /* ---------- quantity steppers + autosubmit ---------- */
  $$('.qty').forEach(function (q) {
    var inp = $('input', q), max = +inp.max || 99;
    $$('button', q).forEach(function (b) {
      b.addEventListener('click', function () {
        var v = (+inp.value || 1) + (b.dataset.step === '+' ? 1 : -1);
        inp.value = Math.max(+inp.min || 1, Math.min(max, v));
        inp.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
  });
  document.addEventListener('change', function (e) {
    if (e.target.matches('[data-autosubmit]')) e.target.form.submit();
  });

  /* ---------- variant switching (price, availability, URL) ---------- */
  var vs = $('[data-variant-select]'), vj = $('[data-variants-json]');
  if (vs && vj) {
    var variants = [];
    try { variants = JSON.parse(vj.textContent); } catch (e) {}
    vs.addEventListener('change', function () {
      var v = variants.filter(function (x) { return String(x.id) === vs.value; })[0];
      if (!v) return;
      $$('[data-price]').forEach(function (p) {
        p.innerHTML = theme.formatMoney(v.price) + (v.compare_at_price && v.compare_at_price > v.price ? '<s>' + theme.formatMoney(v.compare_at_price) + '</s>' : '');
      });
      $$('[data-add-btn]').forEach(function (b) { b.disabled = !v.available; b.textContent = v.available ? theme.strings.add : theme.strings.soldOut; });
      $$('input[name=id]').forEach(function (i) { i.value = v.id; });
      var u = new URL(location.href); u.searchParams.set('variant', v.id); history.replaceState({}, '', u);
    });
  }

  /* ---------- PIN-code helper (format check + store message; real serviceability comes from Shopify shipping zones) ---------- */
  var pin = $('#pin-input');
  if (pin) {
    var msg = $('#pin-msg'), btn = $('#pin-btn');
    var check = function () {
      var v = pin.value.trim();
      if (!/^[1-9][0-9]{5}$/.test(v)) { msg.textContent = 'Enter a valid 6-digit PIN code.'; msg.className = 'pin-msg bad'; return; }
      msg.textContent = pin.dataset.ok || 'Thank you. We will confirm delivery for this PIN code after you order.';
      msg.className = 'pin-msg';
      try { localStorage.setItem('vr_pin', v); } catch (e) {}
    };
    btn.addEventListener('click', check);
    pin.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); check(); } });
    try { var sv = localStorage.getItem('vr_pin'); if (sv && !pin.value) pin.value = sv; } catch (e) {}
  }

  /* ---------- sticky buy bar ---------- */
  var main = $('#main-cta'), bar = $('.sticky-buy');
  if (main && bar && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { bar.classList.toggle('show', !en[0].isIntersecting && en[0].boundingClientRect.top < 0); }, { threshold: 0 }).observe(main);
  }

  /* ---------- scroll reveal ---------- */
  var rv = $$('.reveal');
  if (rv.length) {
    if (reduce || !('IntersectionObserver' in window)) { rv.forEach(function (e) { e.classList.add('in'); }); }
    else {
      var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }); }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      rv.forEach(function (e) { if (e.getBoundingClientRect().top < innerHeight) e.classList.add('in'); else io.observe(e); });
    }
  }

  /* ---------- theme editor: re-run reveal for sections added live ---------- */
  document.addEventListener('shopify:section:load', function (e) { $$('.reveal', e.target).forEach(function (el) { el.classList.add('in'); }); wlRender(); });
})();
