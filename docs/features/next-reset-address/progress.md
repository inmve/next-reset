# Next Reset address and final labels

## Current Status
Last Updated: 2026-09-22T12:19:31.294053+00:00
Status: Testing
Completion: 70%

## Current Context
Working: configured next-reset site and source URLs, localized terminal highlight on next reset, removed historical status row from provider cards. Coding labels, scope details, source timestamps and in-card captions retained.
Not working: remote rename and publication pending.
Next: build/browser verification; rename website repository; update remotes; publish both feature PRs; verify new Pages address.

## Timeline
- 2026-09-22T12:19:31.294053+00:00: next-reset returned404 (available); pulled main for both repositories and created feature branches.
- 2026-09-22T12:19:31.294053+00:00: changed configuration, locale terms, question markup, card rendering and styles.

## Decisions
Context: user selected next-reset for cleaner URL. Choice: rename website repository only; notification repository remains token-resets. Update canonical URL, data source repository and minimal README link.
Context: terminal-style highlight. Choice: static inverse-color mark around localized next reset phrase; no animation.
Context: user removed Last confirmed reset label. Choice: remove separate status row, retaining relative age and Max plan scope beneath the historical date.

## Challenges & Solutions
No blockers yet. Repository rename must precede deployment at the new address.

## Files Modified
site.config.json, data/events.json, README.md: new addresses.
locales/en.json, locales/ru.json: translated highlight term.
build.py, src/style.css: terminal highlight and remove status row.
public/, minimal-README.md: regenerated outputs.

## Next Steps
- [x] Implement approved changes.
- [ ] Verify build and browser.
- [ ] Rename and publish.
- [ ] Verify new public URL.

2026-09-22T12:31:50.009074+00:00: final scope includes renaming updates repository to token-limit-resets; approved exact description; Next Reset site-link label; exact one-line Star/Watch instruction (no delivery paragraph); status above dates; Announced source labels; Claude Take your time caption; author and public feedback links. No personal email supplied or published.
