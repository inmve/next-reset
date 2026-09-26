# Rotating terminal headline

## Current Status
Last Updated: 2026-09-26T17:12:25.199050+00:00
Status: Ready for Review
Completion: 95%

## Original request
«давай поставим на ротацию и на клик тоже будем менять - выбери топ-3 варианта и делай»

## Current Context
Implemented three title variants: cd token-usage/limits; reset, watch limits; await reset, tail -f reset.log. Choose a random title on load; advance on native button activation. No navigation on title click. Native button supports Enter/Space. There is no interval; reduced motion has no timer to pause. Manual switching always available; JavaScript-disabled page retains static original title. Actual EN/RU locales supply all strings through translation helper.
Pending: verify tests/build, PR, deploy/live check.

## Decisions
User authorized selection and execution. Kept original plus watch/tail options for terminal theme and feed intent. Avoided fictitious git watch command. Eight-second interval offers time to read. Instant text changes avoid animation; native button is semantically accurate for switching. Existing motion preference/visibility handlers control timer, preventing duplicate timers. Keyboard focus/hover pause automatic changes.

## Challenges & Solutions
None. Prior feature completion notes preserved in named stash and copied forward.

## Timeline
- 2026-09-26T17:12:25.199050+00:00: pulled main and created feature/rotating-shell-title.
- 2026-09-26T17:12:25.199050+00:00: wrote two interaction tests; confirmed failure without rotation implementation.
- 2026-09-26T17:12:25.199050+00:00: implemented button, rotation, preference/visibility handling, locales and CI test step.

## Files Modified
src/page.html; src/site.js; src/style.css; locales/en.json and ru.json; tests/test_title.cjs; .github/workflows/pages.yml; generated public assets; this progress file; previous Claude completion notes.

## Next Steps
- [ ] Run interaction tests, existing Python tests, build and syntax/whitespace checks.
- [ ] Publish PR and verify deployment.

## User corrections and pause
2026-09-26T17:32:16.000972+00:00
User: «не надо каждые 8 просто ротируй при загрузке». Timer removed and load/click behavior passes revised test. User then explicitly paused work to design event schema. Extra event-export test currently fails because export implementation was not begun. Do not publish this branch or assume tests pass. Grok was later excluded from the historical research and user says only Codex/Claude; do not continue planned Grok edits without new instruction. Current active work is separately scoped historical research; production changes paused.
