# Two providers

## Current Status
Last Updated: 2026-09-22T11:42:53.290065+00:00
Status: Ready for Review
Completion: 90%

## Current Context
Working: Grok removed from provider definitions and public events; both locales name only Codex and Claude Max; two desktop columns; Enjoy the ride note aligned left.
Not working: publication pending.
Next: rebuild, browser check, PR checks, merge and verify deployment.

## Timeline
- 2026-09-22T11:42:53.290065+00:00: pulled main in both repositories and created feature/two-providers branches; updated data, locales and styles.

## Decisions
Context: simplify to OpenAI and Anthropic and move the bottom note left. Options: preserve an empty third column or use two equal columns. Choice: two equal columns, single column on mobile; align the existing note left. Impact: CSS, data, both locales, generated HTML and minimal README.
No notification release: this is a display/coverage change, not a new reset event.

## Challenges & Solutions
None.

## Files Modified
- src/style.css: two columns and left-aligned note.
- data/events.json: remove Grok provider and event.
- locales/en.json, locales/ru.json: two-provider description.
- public/: rebuilt output.
- minimal-README.md: two provider lines.

## Next Steps
- [x] Implement changes.
- [x] Verify build, syntax and browser.
- [ ] Publish via PRs and verify Pages.

2026-09-22T11:43:46.797108+00:00: release build and syntax passed; browser confirms two columns, left-aligned note, no Grok and no horizontal overflow.
