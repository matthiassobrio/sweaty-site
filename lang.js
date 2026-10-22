// Language: ?lang=fr|en, then the visitor's last choice, then the browser.
// Contact address: set CONTACT once, it fills every .contact block.
(function () {
  var CONTACT = '';
  var root = document.documentElement;
  function pick() {
    var q = (location.search.match(/[?&]lang=(fr|en)/) || [])[1];
    if (q) return q;
    try { var s = localStorage.getItem('sweaty.lang'); if (s === 'fr' || s === 'en') return s; } catch (e) {}
    return /^fr/i.test(navigator.language || '') ? 'fr' : 'en';
  }
  function set(l) {
    root.className = root.className.replace(/\bl-(fr|en)\b/g, '').trim() + ' l-' + l;
    root.lang = l;
    var t = document.querySelector('meta[name="title-' + l + '"]');
    if (t) document.title = t.content;
  }
  set(pick());
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-set]').forEach(function (b) {
      b.addEventListener('click', function () {
        var l = b.getAttribute('data-set');
        set(l);
        try { localStorage.setItem('sweaty.lang', l); } catch (e) {}
      });
    });
    document.querySelectorAll('.contact').forEach(function (el) {
      if (!CONTACT) { el.style.display = 'none'; return; }
      el.querySelectorAll('a.mail').forEach(function (a) { a.href = 'mailto:' + CONTACT; a.textContent = CONTACT; });
    });
    var y = document.getElementById('y'); if (y) y.textContent = new Date().getFullYear();
  });
})();
