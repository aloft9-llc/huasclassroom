/** Hua's Classroom — homepage semester / book panels */
(function () {
  const panels = {
    'first-semester': document.getElementById('first-semester'),
    'second-semester': document.getElementById('second-semester'),
    'singapore-3a': document.getElementById('singapore-3a'),
  };

  if (!panels['first-semester']) return;

  function show(id, opts) {
    opts = opts || {};
    Object.entries(panels).forEach(([key, el]) => {
      if (!el) return;
      const on = key === id;
      el.classList.toggle('is-active', on);
      el.hidden = !on;
    });
    document.querySelectorAll('[data-jump]').forEach((btn) => {
      btn.classList.toggle('is-selected', btn.dataset.jump === id);
    });
    const book = id === 'singapore-3a' ? 'singapore' : 'shanghai';
    document.querySelectorAll('.book-pick').forEach((card) => {
      card.classList.toggle('is-active', card.dataset.book === book);
    });
    history.replaceState(null, '', '#' + id);
    if (opts.scroll) {
      const target = document.getElementById('lessons');
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  document.querySelectorAll('[data-jump]').forEach((btn) => {
    btn.addEventListener('click', () => {
      show(btn.dataset.jump, { scroll: true });
    });
  });

  const hash = location.hash.replace('#', '');
  if (hash === 'second-semester' || hash.startsWith('s2-')) {
    show('second-semester');
    if (hash.startsWith('s2-') || hash.startsWith('chapter-')) {
      const el = document.getElementById(hash);
      if (el && el.tagName === 'DETAILS') {
        el.open = true;
        setTimeout(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }), 50);
      }
    }
  } else if (hash === 'singapore-3a' || hash.startsWith('sg-')) {
    show('singapore-3a');
    const el = document.getElementById(hash);
    if (el && el.tagName === 'DETAILS') {
      el.open = true;
      setTimeout(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }), 50);
    }
  } else if (hash.startsWith('chapter-') || hash === 'first-semester') {
    show('first-semester');
    const el = document.getElementById(hash);
    if (el && el.tagName === 'DETAILS') {
      el.open = true;
      setTimeout(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }), 50);
    }
  } else if (hash === 'lessons') {
    document.getElementById('lessons')?.scrollIntoView();
  } else {
    show('first-semester');
  }

  document.querySelectorAll('.semester').forEach((sem) => {
    sem.addEventListener('toggle', (e) => {
      const t = e.target;
      if (t.tagName !== 'DETAILS' || !t.open) return;
      sem.querySelectorAll('details.chapter').forEach((d) => {
        if (d !== t) d.open = false;
      });
    }, true);
  });
})();
