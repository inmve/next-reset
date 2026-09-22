# README notification section

## Current Status
Last Updated: 2026-09-22T13:34:19.306679+00:00
Status: Ready for Review
Completion: 85%

## Current Context
Working: generator adds Get notifications heading before the existing Star/Watch sentence and changes site-link prefix to Check out website. New text uses locale helpers.
Not working: no known issues; publication pending.
Next: regenerate, check and publish both feature PRs, then verify main README.

## Timeline
- 2026-09-22T13:34:19.306679+00:00: saved previous local completion note; pulled both main branches and created feature/readme-notifications-section.
- 2026-09-22T13:34:19.306679+00:00: changed README generator and English/Russian locale strings.

## Decisions
Context: user wants a separate notification section. Choice: H2 before the existing subscription sentence; keep its wording.
Context: user replaces Less minimalistic version. Choice: Check out website — existing Next Reset link; URL unchanged.
Context: README is generated. Choice: update generator and notification repo together so future builds retain changes. New strings use locale helpers.

## Challenges & Solutions
No blockers.

## Files Modified
build.py, locales/en.json, locales/ru.json, generated minimal-README.md and public/index.html; notification README.md.

## Next Steps
- [x] Implement requested copy changes.
- [x] Verify build and output.
- [ ] Publish and verify live README.

2026-09-22T13:35:05.115596+00:00: Release build, JavaScript syntax and whitespace checks passed; generated README contains separate Get notifications H2 and Check out website link.
