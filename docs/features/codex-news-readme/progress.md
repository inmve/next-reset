# News-style Codex README

## Current Status
Last Updated: 2026-09-26T16:01:32.550818+00:00
Status: Ready for Review
Completion: 90%

## Current Context
Working: approved lowercase headline/paragraph layout implemented in canonical generator and real locales. Other provider feeds retain their current layout. Codex facts and quote are unchanged.
Incomplete: validate, publish PRs and verify live README.
Next: build, existing tests, copy generated Codex README, merge feature PRs and read back GitHub output.

## Original requests
«давай на верхне строке писать, что б читалась как новости ... UPD 26.09 - new reset is likely ... затем говорим как подписаться ... затем why? ... дальше заголовок other feeds ... начинать с маленькой буквы ... давай сперва мне тут покажи как это будет»
Approved draft writing block 58317. Final correction/approval: «how to subscribe скорее wanna receive alerts about resets? да, прикольный стиль».

## Decisions
Context: user approves a news-first narrative. Choice: dated lowercase H1, attributed announcement/quote, uncertainty, conversational subscription heading, why paragraph, other feeds. Date/status are generated from the recorded event so future updates cannot silently turn promises into completed resets. Source-specific summary key belongs only to the September 26 event; future events default to their own source/status text.

## Timeline
- Preserved previous local completion notes, pulled main, created feature/codex-news-readme.
- Updated builder, actual EN/RU locales and the source event's optional README summary key.

## Challenges & Solutions
None beyond preserving local handoff notes in work/codex-alert-description-completed.md and a named Git stash.

## Files Modified
build.py; data/events.json; locales/en.json and ru.json; generated notifications/codex/README.md, public/events.json and public/index.html; external Codex README.md; this progress file.

## Next Steps
- [x] Validate and inspect approved text.
- [ ] Create/merge PRs and verify publication.

Validation: five tests, release build, JavaScript syntax and whitespace checks passed. Inspected generated README against approved draft; only subscription heading reflects the user’s final correction.
