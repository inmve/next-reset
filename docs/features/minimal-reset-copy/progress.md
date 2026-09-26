# Minimal reset copy publication

## Current Status
Last Updated: 2026-09-26T16:11:52.179305+00:00
Status: Ready for Review
Completion: 90%

## Current Context
Working: final copy approved in chat; canonical EN/RU strings and generator updated. User explicitly authorized publication: «отлично, публикуем - ия. хочу уже получить».
Pending: build, tests, publish source and feed PRs, update GitHub About, verify remote result.
Previous news draft was published in next-reset#25 and codex-reset-alerts#4 before user requested preview. Work stopped, disclosed the premature publication, and resumed only after current approval.

## Original requests
- «get a heads-up through GitHub Releases. use your remaining tokens before the reset. сократим -> get an alert to use ...»
- «we’re still waiting for confirmation. не надо ... we post reset updates as releases. you get a GitHub notification. в одно надо»
- «finish a feature. try an idea. tackle a refactor. plan your next big task around fresh limits. убери ... each repo covers one tool. choose the alerts you want. это тоже»
- «заголовок on web и дальше описание ... минимальный тайтл –> обьяснение простое ... максимально минималистично»
- «how to? не хочу слишком разговорногго ... other labs? ... got a web version? или без got - что думаешь?»
- Approved headings: how to subscribe? → why? → other tools? → web version?
- Final approval: «отлично, публикуем - ия. хочу уже получить»

## Decisions
Context: publish exactly the approved minimalist draft. Considered keeping conversational headings vs short explicit questions; chose approved explicit questions. Remove extra examples and waiting sentence; retain exact attributed quote and unknown reset time. Add translated web section heading in generator. Source locales remain canonical; generated README copied to dedicated feed. About: codex reset coming? get an alert to use your remaining tokens before the reset. subscribe via GitHub Releases.
Existing public event release already fulfills release request; copy edits do not create duplicate subscriber alerts.

## Challenges & Solutions
Previous publication preceded user's preview-only instruction. Disclosure and stop already occurred. Current explicit approval now authorizes final publication.

## Timeline
- 2026-09-26T16:11:52.179305+00:00: pulled main in both repositories, created feature/minimal-reset-copy.
- 2026-09-26T16:11:52.179305+00:00: updated EN/RU locales and web-section heading.

## Files Modified
- locales/en.json, locales/ru.json: approved short copy.
- build.py: translated web heading.
- notifications/codex/README.md: generated final draft.
- codex-reset-alerts/README.md: published feed copy.
- this progress file: original requests, decisions and handoff.

## Next Steps
- [x] Run tests, build and syntax checks.
- [ ] Create, attach and merge PRs.
- [ ] Update About description and verify README/release.

2026-09-26T16:12:33.838848+00:00: five existing tests, release build, JavaScript syntax and whitespace checks passed. Generated README reviewed against approved draft. User additionally wants a link/title ready for publication on HN; prepare copy in chat, do not submit on their behalf.
