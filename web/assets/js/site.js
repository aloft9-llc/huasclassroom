/** Hua's Classroom — shared static behaviors */
(function () {
  const topbar = document.querySelector('.topbar');
  if (!topbar) return;

  const onScroll = () => {
    const hero = document.querySelector('.hero');
    const past = hero
      ? window.scrollY > hero.offsetHeight - 64
      : window.scrollY > 12;
    topbar.classList.toggle('is-scrolled', past);
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
