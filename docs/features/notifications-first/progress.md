# Notifications first and useful tokens caption

## Current Status
Last Updated: 2026-09-22T13:48:09.692250+00:00
Status: Ready for Review
Completion: 85%

## Current Context
Working: Get notifications is immediately below README H1 and before provider sections; Star sentence removed. Waiting pelican caption is Make your tokens count on site and README, via shared locales.
Not working: publication pending.
Next: verify generated output, publish both feature PRs, verify main README and live site.

## Timeline
- 2026-09-22T13:48:09.692250+00:00: pulled both main branches and created feature/notifications-first.
- 2026-09-22T13:48:09.692250+00:00: updated generator and English/Russian locales.

## Decisions
Context: user moved notifications to beginning. Choice: keep H1 as document title and put notification H2 immediately after it.
Context: user approved Make your tokens count via annotation. Choice: shared waitingNote updates both site and README; cycling caption unchanged.
Context: notification sentence is generated text. Choice: use localized resetNotifications key without Star wording.

## Challenges & Solutions
No blockers.

## Files Modified
build.py, locales/en.json, locales/ru.json, generated public/index.html and minimal-README.md; notification README.md.

## Next Steps
- [x] Apply requested changes.
- [ ] Verify and publish.

2026-09-22T13:48:41.176624+00:00: Release build, JavaScript syntax and whitespace checks passed. Generated README begins with title then Get notifications; caption is shared across outputs.
