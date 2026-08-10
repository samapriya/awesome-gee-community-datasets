/* Replaces the `mkdocs-open-in-new-tab` plugin, which has no Zensical
   equivalent. Opens off-site links in a new tab.

   Bound to the `document$` observable rather than DOMContentLoaded so it also
   runs after instant navigation swaps the page content in place. */
(function () {
  function markExternal() {
    var host = location.hostname;
    document.querySelectorAll('.md-content a[href^="http"]').forEach(function (a) {
      if (a.hostname && a.hostname !== host && !a.target) {
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
      }
    });
  }
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(markExternal);
  } else {
    document.addEventListener('DOMContentLoaded', markExternal);
  }
})();
