# Any resets yet?

## Current Status
Last Updated: 2026-09-22T19:35:45.454956+00:00
Status: Ready for Review
Completion: 98%

## Original request
User selected “Any resets yet” and said «давай этот».

## Decisions
Use “Any resets yet?” as site heading and browser title through the shared siteTitle translation key. Preserve Next Reset brand and dated title format. Update Russian locale as well. No layout or provider changes.

## Timeline
Created feature/any-resets-title from latest origin/main. Updated both locales.

## Files Modified
locales/en.json, locales/ru.json and generated public output.

## Challenges & Solutions
None.

## Current Context
Heading change implemented; build and publication pending.

## Next Steps
- [x] Release build and syntax/whitespace checks
- [ ] PR and deployment

Validation: release build, node syntax check, git diff --check passed; generated H1 and title verified.

## Follow-up: Codex banked reset and riding pelican variants

Source checked: Tibo’s X post https://x.com/thsottiaux/status/2102463847714247142 says a banked reset is being loaded into all Plus, Pro and Business accounts; OpenAI Community launch announcement repeats it. This is a saved reset credit, distinct from the earlier expected regular reset. Codex card now uses banked state and an accurate subscriber scope. Use cycling SVG design 4 for Codex and existing design 5 for Claude so riding illustrations differ.

Files changed: data/events.json, locales/en.json, locales/ru.json, build.py.
Next: build and check rendered card/source, commit feature branch, PR, deploy.

Validation: release build succeeded; generated page includes the banked status, plan scope and original X source. The two banked reset cards now use different cycling SVG designs.
