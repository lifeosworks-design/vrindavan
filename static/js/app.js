/* VRINDAVAN storefront JS — small, deferred, no framework. Everything degrades gracefully without it. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var csrf = (document.querySelector('meta[name=csrf]') || {}).content || '';
  document.documentElement.classList.add('js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- drawer ----
  var body = document.body;
  function setDrawer(open) {
    body.classList.toggle('drawer-open', open);
    var btn = $('.menu-btn'); if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    var d = $('#drawer'); if (d) { d.setAttribute('aria-hidden', open ? 'false' : 'true'); if (open) { var f = $('a,button', d); f && f.focus(); } }
  }
  $$('[data-drawer-open]').forEach(function (b) { b.addEventListener('click', function () { setDrawer(true); }); });
  $$('[data-drawer-close]').forEach(function (b) { b.addEventListener('click', function () { setDrawer(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setDrawer(false); var sp = $('.search-panel.open'); if (sp) sp.classList.remove('open'); } });

  // ---- search panel + suggestions ----
  var sp = $('.search-panel'), sInput = sp && $('input[name=q]', sp), sBox = sp && $('.suggest', sp), sTimer;
  $$('[data-search-toggle]').forEach(function (b) {
    b.addEventListener('click', function () { if (!sp) return; sp.classList.toggle('open'); if (sp.classList.contains('open')) sInput.focus(); });
  });
  if (sInput) {
    sInput.addEventListener('input', function () {
      clearTimeout(sTimer);
      var v = sInput.value.trim();
      if (v.length < 2) { sBox.hidden = true; return; }
      sTimer = setTimeout(function () {
        fetch('/api/suggest?q=' + encodeURIComponent(v), { headers: { 'Accept': 'application/json' } })
          .then(function (r) { return r.ok ? r.json() : { results: [] }; })
          .then(function (d) {
            sBox.textContent = '';
            if (!d.results.length) { sBox.hidden = true; return; }
            d.results.forEach(function (it) {
              var a = document.createElement('a'); a.href = it.url;
              var s1 = document.createElement('span'); s1.textContent = it.label;
              var s2 = document.createElement('small'); s2.textContent = it.sub;
              a.appendChild(s1); a.appendChild(s2); sBox.appendChild(a);
            });
            sBox.hidden = false;
          }).catch(function () { sBox.hidden = true; });
      }, 220);
    });
    document.addEventListener('click', function (e) { if (sBox && !sp.contains(e.target)) sBox.hidden = true; });
  }

  // ---- wishlist toggle ----
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-wish]'); if (!b) return;
    e.preventDefault();
    fetch('/api/wishlist/toggle', { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRF-Token': csrf }, body: JSON.stringify({ product_id: +b.dataset.wish }) })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d.error) return;
        b.setAttribute('aria-pressed', d.on ? 'true' : 'false');
        b.setAttribute('aria-label', d.on ? 'Remove from wishlist' : 'Add to wishlist');
        var c = $('[data-wish-count]'); if (c) { c.textContent = d.count; c.hidden = !d.count; }
      });
  });

  // ---- filters dialog ----
  var fd = $('dialog.filters');
  $$('[data-filters-open]').forEach(function (b) { b.addEventListener('click', function () { if (fd && fd.showModal) fd.showModal(); }); });
  $$('[data-filters-close]').forEach(function (b) { b.addEventListener('click', function () { fd && fd.close(); }); });
  if (fd) fd.addEventListener('click', function (e) { if (e.target === fd) fd.close(); });
  $$('[data-sort]').forEach(function (s) { s.addEventListener('change', function () { s.form.submit(); }); });

  // ---- gallery ----
  var track = $('.gallery-track');
  if (track) {
    var slides = $$('.gallery-slide', track), dots = $$('.dots i'), thumbs = $$('.thumbs button');
    function activate(i) {
      slides.forEach(function (s, n) { s.classList.toggle('active', n === i); });
      dots.forEach(function (d, n) { d.classList.toggle('on', n === i); });
      thumbs.forEach(function (t, n) { t.classList.toggle('on', n === i); });
    }
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

  // ---- qty steppers ----
  $$('.qty').forEach(function (q) {
    var inp = $('input', q), max = +inp.max || 10;
    $$('button', q).forEach(function (b) {
      b.addEventListener('click', function () {
        var v = (+inp.value || 1) + (b.dataset.step === '+' ? 1 : -1);
        inp.value = Math.max(+inp.min || 1, Math.min(max, v));
        inp.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
  });
  $$('[data-autosubmit]').forEach(function (el) { el.addEventListener('change', function () { el.form.submit(); }); });

  // ---- PIN check on product page ----
  var pin = $('#pin-input');
  if (pin) {
    var msg = $('#pin-msg'), btn = $('#pin-btn');
    function check() {
      var v = pin.value.trim();
      if (!/^[1-9][0-9]{5}$/.test(v)) { msg.textContent = 'Enter a valid 6-digit PIN code.'; msg.className = 'pin-msg bad'; return; }
      msg.textContent = 'Checking…'; msg.className = 'pin-msg';
      fetch('/api/pincode?pin=' + v + '&product=' + (pin.dataset.product || ''), { headers: { 'Accept': 'application/json' } })
        .then(function (r) { return r.json(); })
        .then(function (d) { msg.textContent = d.message; msg.className = 'pin-msg' + (d.ok ? '' : ' bad'); try { localStorage.setItem('vr_pin', v); } catch (e) {} })
        .catch(function () { msg.textContent = 'Could not check right now.'; msg.className = 'pin-msg bad'; });
    }
    btn.addEventListener('click', check);
    pin.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); check(); } });
    try { var sv = localStorage.getItem('vr_pin'); if (sv && !pin.value) pin.value = sv; } catch (e) {}
  }

  // ---- sticky buy bar on product page (shown once the main button leaves the viewport) ----
  var main = $('#main-cta'), bar = $('.sticky-buy');
  if (main && bar && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { bar.classList.toggle('show', !en[0].isIntersecting && en[0].boundingClientRect.top < 0); }, { threshold: 0 }).observe(main);
  }

  // ---- checkout: live totals, COD availability ----
  var co = $('#checkout-form');
  if (co) {
    var pmEls = $$('input[name=payment_method]', co), pinEl = $('#pincode', co), t;
    function quote() {
      var pm = (pmEls.filter(function (r) { return r.checked; })[0] || {}).value || 'cod';
      var p = pinEl ? pinEl.value.trim() : '';
      fetch('/api/quote?pm=' + pm + '&pin=' + encodeURIComponent(p), { headers: { 'Accept': 'application/json' } })
        .then(function (r) { return r.json(); })
        .then(function (d) {
          if (d.error) return;
          [['subtotal', 'subtotal'], ['discount', 'discount'], ['shipping', 'shipping'], ['cod_fee', 'cod_fee'], ['total', 'total']].forEach(function (k) {
            var el = $('[data-t=' + k[0] + ']'); if (el) el.textContent = d.fmt[k[1]];
          });
          var feeRow = $('[data-row=cod_fee]'); if (feeRow) feeRow.hidden = !d.cod_fee;
          var discRow = $('[data-row=discount]'); if (discRow) discRow.hidden = !d.discount;
          var cod = $('#pm-cod'), note = $('#cod-note');
          if (cod) {
            cod.disabled = !d.cod_ok; cod.closest('.radio-card').classList.toggle('disabled', !d.cod_ok);
            if (note) { note.textContent = d.cod_ok ? '' : d.cod_reason; note.hidden = d.cod_ok; }
            if (!d.cod_ok && cod.checked) { var on = $('#pm-online'); if (on && !on.disabled) { on.checked = true; quote(); } }
          }
          var warn = $('#block-all'); if (warn) warn.hidden = !d.block_all;
        });
    }
    pmEls.forEach(function (r) { r.addEventListener('change', quote); });
    if (pinEl) { pinEl.addEventListener('input', function () { clearTimeout(t); t = setTimeout(quote, 350); }); }
    quote();
    co.addEventListener('submit', function () { var b = $('button[type=submit]', co); if (b) { b.disabled = true; b.textContent = 'Placing order…'; } });
  }

  // ---- scroll reveal (elements already on screen are shown immediately, no flash) ----
  var rv = $$('.reveal');
  if (rv.length) {
    if (reduce || !('IntersectionObserver' in window)) { rv.forEach(function (e) { e.classList.add('in'); }); }
    else {
      var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }); }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      rv.forEach(function (e) { if (e.getBoundingClientRect().top < innerHeight) e.classList.add('in'); else io.observe(e); });
    }
  }

  // ---- confirm dialogs for destructive admin actions ----
  document.addEventListener('submit', function (e) {
    var m = e.target.getAttribute('data-confirm'); if (m && !window.confirm(m)) e.preventDefault();
  });
})();
