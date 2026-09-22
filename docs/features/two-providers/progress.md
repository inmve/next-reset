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

## Follow-up: remove unnecessary copy
User requested sentence case, removal of hero mechanism and duplicate source link, and a shell-command identity. Implemented header `$ cd token-usage/limits; reset`, sentence case provider/status labels, removed hero description/source and corresponding JS references. Original sources remain on cards. Replaced duplicate Enjoy the ride card badge with factual Expected today; retained the requested left-aligned bottom note. User selected a thin monochrome pelican resting on a stone. Replaced meditation SVG05 with a still fine-line drawing, closed eye, stone, no lotus or decorations; updated both locale accessibility descriptions.

Final local verification: build, syntax and browser checks passed. At 320px no overflow; all labels use natural case; hero proof removed without JS errors; new monochrome resting pelican visually inspected. Await latest PR CI and Pages deployment.
