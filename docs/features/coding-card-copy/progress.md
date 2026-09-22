# Coding cards and subscription placement

## Current Status
Last Updated: 2026-09-22T12:03:35.954930+00:00
Status: Ready for Review
Completion: 100%

## Current Context
Working: Claude Code naming with Max scope preserved; former colored meditation illustration restored from history; enlarged captions below birds inside cards; single combined expected-time line; GitHub subscription block after cards.
Not working: verification and public deployment pending.
Next: release build, syntax, browser at mobile/desktop, README sync, PR checks, publication.

## Timeline
- 2026-09-22T12:03:35.954930+00:00: saved previous feature handoff locally; pulled main in both repositories; created feature/coding-card-copy and feature/coding-focus.
- 2026-09-22T12:03:35.954930+00:00: updated source, locales, provider label and illustration.

## Decisions
Context: coding focus must not broaden an announcement for Max subscribers. Options: rename only (misleading) or retain plan scope (accurate). Choice: Claude Code display name plus localized Max plans detail, preserving original source and scope.
Context: repeated today labels. Choice: one Expected today · time not specified line beneath date; remove separate announced badge. Last confirmed reset remains above historical dates. A small shared status slot keeps desktop dates aligned.
Context: captions and follow-up action. Choice: 16px captions inside each card, GitHub link and Watch instructions beneath both cards.
Context: graphic too minimal. Choice: restore previous colored SVG05 from existing history, with decorative plus still removed; only cyclist animates.

## Challenges & Solutions
No new blockers. Saved the previous feature's uncommitted completion note before changing branches.

## Files Modified
- build.py: captions, combined status layout, localized scope in cards and minimal README.
- src/page.html, src/style.css, src/site.js: move subscription, enlarge captions, update date refresh.
- locales/en.json, locales/ru.json: combined status, restored accessibility text, plan scope.
- data/events.json: Claude Code display label with unchanged evidence.
- assets/pelicans/pelican-05-meditating.svg: restored colored illustration.
- README.md, public/, minimal-README.md: documentation and regenerated output.

## Next Steps
- [x] Implement approved changes.
- [x] Verify locally.
- [x] Publish and verify live.

2026-09-22T12:05:41.337746+00:00: release build, JS syntax, SVG parsing and matching locale keys passed. Browser verification at320/1100px: no overflow or console errors; two16px captions inside their corresponding cards; one CTA below cards; combined expected-time string once; Max scope preserved; only bicycle has animation.

Latest approved copy: green status dot plus Expected today below date; user removed the time-not-specified clause. Shell-command header retained. Local diff check caught a trailing blank line before commit; removed it and rebuilt. An initial PR request could not run before that commit; no site code was published from that attempt.

2026-09-22T12:13:11.220628+00:00: deployment35725498692 succeeded and live HTML verified. Live browser retained previous unversioned CSS (waiting-note rule, captions15px rather than16px). Follow-up feature/refine-expected-status adds content-based asset versions so already-open pages load matching styles/scripts.
