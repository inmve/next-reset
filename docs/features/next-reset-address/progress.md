# Next Reset address and final labels

## Current Status
Last Updated: 2026-09-22T12:36:37.400809+00:00
Status: Ready for Review
Completion: 90%

## Current Context
Working: configured next-reset site and source URLs, localized terminal highlight on next reset, removed historical status row from provider cards. Coding labels, scope details, source timestamps and in-card captions retained.
Not working: no known UI issues; final PR merge and deployment verification pending.
Next: create and merge the prepared PRs, verify Pages at https://inmve.github.io/next-reset/ and the notification README.

## Timeline
- 2026-09-22T12:19:31.294053+00:00: next-reset returned404 (available); pulled main for both repositories and created feature branches.
- 2026-09-22T12:19:31.294053+00:00: changed configuration, locale terms, question markup, card rendering and styles.

## Decisions
Context: user selected next-reset for cleaner URL. Choice: website repository is next-reset; the subsequently approved notification repository name is token-limit-resets. Update canonical URL, data source repository and minimal README link.
Context: terminal-style highlight. Choice: static inverse-color mark around localized next reset phrase; no animation.
Context: user removed Last confirmed reset label. Choice: replace the historical label with elapsed days and Max plan scope above the date, as subsequently requested.

## Challenges & Solutions
No blockers yet. Repository rename must precede deployment at the new address.

## Files Modified
site.config.json, data/events.json, README.md: new addresses.
locales/en.json, locales/ru.json: translated highlight term.
build.py, src/style.css: terminal highlight and remove status row.
public/, minimal-README.md: regenerated outputs.

## Next Steps
- [x] Implement approved changes.
- [x] Verify build and browser.
- [ ] Rename and publish.
- [ ] Verify new public URL.

2026-09-22T12:31:50.009074+00:00: final scope includes renaming updates repository to token-limit-resets; approved exact description; Next Reset site-link label; exact one-line Star/Watch instruction (no delivery paragraph); status above dates; Announced source labels; Claude Take your time caption; author and public feedback links. No personal email supplied or published.

2026-09-22T12:36:37.400907+00:00: Both repositories renamed and remote URLs updated. Build, JavaScript syntax, diff whitespace and browser layout checks passed. Feature branches pushed; final PRs pending. Generated minimal README synchronized with exact approved text.
