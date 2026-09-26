# Provider reset alerts and September 26 Codex announcement

## Current Status
Last Updated: 2026-09-26T11:32:19.824191+00:00
Status: Testing
Completion: 85%

## Current Context
- Working: fresh main cloned/pulled for next-reset, free-ai-coding and token-limit-resets. Baseline release build and JavaScript syntax check pass. Original X post read directly.
- Incomplete: publication; all requested code/content is prepared. PR creation and CI verification next.
- Next: create PRs in six repositories, attach each to this task, check site CI, prepare draft release and present final publication step.

## Original requests
1. «так, найди тот проект по кодекса апдейтам и давай заапдейтим уже вот это: https://x.com/i/status/2103637477760311522»
2. «да- и тм еще была идея по использованию гитхаб нотификаций для алертов - для каждой нотификалки сделать по репозиторию; и так и сказать это внутри репо про это - мол \"сейчас ожидаем апдейт\", сейчас не ожидаем апдейт - подпишись что б узнать когда будет»
3. «а еще хочу непосредственно сделать цитату на источник, что б не было категоричности»
4. «на сайт next reset тоже должна быть полноценная цитата со ссылкой на источник а также кнопка подписки на следующий»
5. «а еще запиши в бэклог идею прикольной подписки - когда юзер уходит ввверх и пытается закрыть браузер, сделать какой-нибуд кричер который будет спускаться и предлагать сперва подписаться - это дарк паттерн но сделать его как-то креативно что б он как дарк не воспринимался»
6. Budget renewal: «еще можешь 15 потратить».

## Decisions
- Context: users need tool-specific subscriptions. Options: reuse/rename existing feeds (disrupts existing subscribers) or add dedicated feeds (clear opt-in). Choice: dedicated Codex, Claude Code and Grok Bot repositories, with combined feeds linking to them. Canonical event history remains in Next Reset to avoid divergent records.
- Context: latest Codex source promises a reset. Options: assume complete or retain announced. Choice: announced, date unknown, with an exact attributed excerpt and explicit completion uncertainty. Applies to website, README and release draft.
- Context: user requests a playful exit-intent idea. Choice: backlog only; optional dismissible character, no blocked browser close or repeated pressure.

## Timeline
- 2026-09-26: Located Next Reset and the prior per-tool-repository backlog item; verified latest source in browser.
- 2026-09-26: Cloned/pulled main, created feature/provider-reset-alerts in three isolated clones; baseline build/syntax passed.

## Challenges & Solutions
- Original X URL blocked in web fetch; direct in-app browser displayed the original post, author and timestamp.
- GitHub network access unavailable in sandbox; authorized network escalation works for Git/gh.
- Weekly usage reached initial 1 pp cap; stopped. Ivan renewed with 15 pp at 21% used. Reset 1790755860; pause again at +15 pp; account-wide readings may include other tasks.

## Files Modified
- This file: original requests, scope, evidence, progress and handoff context.
- Workspace work/memory.md: project structure and budget context.

## Next Steps
- [x] Add checks for isolated feeds, quote/source attribution, pending versus completed and locales.
- [x] Update source event, website and README generator.
- [x] Record exit-intent creature idea in backlog.
- [x] Prepare notification repositories and concrete release draft.
- [x] Run tests/build/syntax/diff checks and inspect rendered site.
- [ ] Create/attach PRs; present final publication step.

- 2026-09-26: Added five regression tests; observed failures before implementation. Implemented event/quote rendering, separate generated feeds, per-provider subscriptions and EN/RU locale text; all five tests pass. Added exit-intent creature to backlog. Browser inspection confirms original quote, link and provider buttons; remote repositories and publication pending.

## Implementation and verification details
- Created public notification repository shells through GitHub: inmve/codex-reset-alerts, inmve/claude-reset-alerts, inmve/grok-reset-alerts. GitHub initialized their default README; requested content is prepared on feature/provider-reset-alerts after pulling main.
- Existing free-ai-coding and token-limit-resets stay combined feeds and gain links to per-tool subscriptions; no repository rename or subscriber migration.
- Canonical history remains data/events.json; generated per-tool READMEs under notifications/ link back to it. No duplicated editable datasets in notification repositories.
- New strings use t() and both real locale files. Quote stays verbatim in English; attribution labels and explanations are translated.
- Quote uses a semantic blockquote plus linked author/date; HTML is escaped. Scope and lack of confirmed completion are visible on the page and in feeds.
- Existing banked labels now say announced and ask users to check account availability.
- Five tests passed, release build passed, node syntax and git whitespace checks passed. Browser confirmed quote/source/subscriptions; 375px mobile view has document width equal to viewport (no horizontal overflow).
- Generated README equality is checked before commit; meaningful-event release text prepared at workspace work/codex-updates/codex-release.md. No release published yet.

## Updated files
- build.py: provider repository validation, quote attribution and per-tool/combined README generation.
- data/events.json: original September 26 Codex promise, affected scope, quote and precise verification time.
- site.config.json: three real per-tool repositories.
- locales/en.json and locales/ru.json: actual translated status/subscription/attribution text.
- src/style.css and generated public/: quote and subscription rendering.
- notifications/*/README.md and minimal-README.md: generated feeds.
- tests/test_build.py and .github/workflows/pages.yml: source/quote/feed regression checks run in CI.
- README.md: canonical ownership, feed update and validation instructions.
- backlog.md: per-tool work status and exit-intent creature idea, explicitly backlog only.
- docs/features/provider-reset-alerts/progress.md: original requests and full handoff context.
- Five external notification repositories: README.md only; local handoff logs ignored and canonical progress tracked here.

## Budget checkpoint
Renewed allowance baseline 21%; latest account-wide reading 23%, +2 pp, 13 pp remaining; reset 1790755860. State kept in tool store and workspace memory.
