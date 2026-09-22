(() => {
  'use strict';
  const root = document.getElementById('reset-zen');
  const {strings, cards} = JSON.parse(document.getElementById('release-state').textContent);
  const t = (key, values = {}) => Object.entries(values).reduce((text, [k, value]) => text.replaceAll(`{${k}}`, String(value)), strings[key] ?? key);
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  let paused = preference.matches;
  const bicycles = [...root.querySelectorAll('svg[data-animated="cycling"]')];
  bicycles.forEach(svg => {
    svg.pauseAnimations();
    svg.querySelectorAll('animate, animateTransform').forEach(animation => animation.beginElement());
  });
  const day = date => [date.getFullYear(), String(date.getMonth() + 1).padStart(2, '0'), String(date.getDate()).padStart(2, '0')].join('-');
  function refreshDates() {
    const now = new Date();
    const today = day(now);
    for (const card of cards) {
      const element = root.querySelector(`[data-provider="${card.id}"]`);
      if (card.banked) continue;
      if (card.announced) {
        const overdue = card.expectedDate && card.expectedDate < today;
        element.querySelector('.scope').textContent = t(overdue ? 'awaitingScope' : card.expectedDate === today ? 'todayTimeUnknown' : 'expectedTimeUnknown');
      } else {
        const age = Math.max(0, Math.floor((now - new Date(card.confirmedAt)) / 86400000));
        const q = Math.min(age / 30, 1);
        element.style.setProperty('--wait', `rgb(${Math.round(196 - 96 * q)},${Math.round(76 - 47 * q)},${Math.round(77 - 35 * q)})`);
        element.querySelector('.scope').textContent = t('daysSince', {days: age}) + (card.scopeLabelKey ? ' | ' + t(card.scopeLabelKey) : '');
      }
    }
    document.title = t('statusPageTitle', {status:t('siteTitle'), date:today});
    document.querySelector('meta[property="og:title"]').content = document.title;
  }
  function syncMotion() {
    bicycles.forEach(svg => {
      if (paused || document.hidden) svg.pauseAnimations();
      else svg.unpauseAnimations();
    });
  }
  preference.addEventListener('change', event => { paused = event.matches; syncMotion(); });
  document.addEventListener('visibilitychange', () => { syncMotion(); if (!document.hidden) refreshDates(); });
  refreshDates();
  syncMotion();
  setInterval(refreshDates, 60000);
})();
