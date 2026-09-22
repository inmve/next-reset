(() => {
  'use strict';
  const root = document.getElementById('reset-zen');
  const {strings, cards, config} = JSON.parse(document.getElementById('release-state').textContent);
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
    const active = [];
    const completedToday = [];
    for (const card of cards) {
      const element = root.querySelector(`[data-provider="${card.id}"]`);
      if (card.announced) {
        const overdue = card.expectedDate && card.expectedDate < today;
        element.querySelector('.scope').textContent = t(overdue ? 'awaitingScope' : card.expectedDate === today ? 'todayTimeUnknown' : 'expectedTimeUnknown');
        if (!overdue) active.push(card);
      } else {
        const age = Math.max(0, Math.floor((now - new Date(card.confirmedAt)) / 86400000));
        const q = Math.min(age / 30, 1);
        element.style.setProperty('--wait', `rgb(${Math.round(196 - 96 * q)},${Math.round(76 - 47 * q)},${Math.round(77 - 35 * q)})`);
        element.querySelector('.scope').textContent = t('daysSince', {days: age}) + (card.scopeLabelKey ? ' | ' + t(card.scopeLabelKey) : '');
        if (day(new Date(card.confirmedAt)) === today) completedToday.push(card.name);
      }
    }
    const todayPlans = active.filter(card => card.expectedDate === today);
    const datedPlans = active.filter(card => card.expectedDate).sort((a, b) => a.expectedDate.localeCompare(b.expectedDate));
    let title = t('noResetsToday');
    if (todayPlans.length) {
      title = t(todayPlans.length === 1 ? 'plannedToday' : 'plannedTodayPlural', {providers: todayPlans.map(card => card.name).join(', ')});
    } else if (completedToday.length) {
      title = t('completedToday', {providers: completedToday.join(', ')});
    } else if (datedPlans.length) {
      const nextDate = datedPlans[0].expectedDate;
      const next = datedPlans.filter(card => card.expectedDate === nextDate);
      const when = new Intl.DateTimeFormat(config.locale, {month:'long', day:'numeric'}).format(new Date(`${nextDate}T12:00:00`));
      title = t(next.length === 1 ? 'plannedForDate' : 'plannedForDatePlural', {providers:next.map(card => card.name).join(', '), when});
    } else if (active.length) {
      title = t(active.length === 1 ? 'plannedUndated' : 'plannedUndatedPlural', {providers:active.map(card => card.name).join(', ')});
    }
    root.querySelector('h1').textContent = title;
    document.title = t('statusPageTitle', {status:title, date:today});
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
