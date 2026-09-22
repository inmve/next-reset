# Expected status and current assets

## Current Status
Last Updated: 2026-09-22T12:13:11.220628+00:00
Status: Ready for Review
Completion: 90%

## Current Context
Working: combined Expected today · time not specified locale restored; content hashes added to stylesheet/script URLs.
Not working: public verification pending.
Next: build, syntax/diff checks, PR, deployment, verify16px captions and current status on live page.

## Timeline
- 2026-09-22T12:13:11.220628+00:00: pulled main, created feature/refine-expected-status, restored approved text in both locales.
- 2026-09-22T12:13:11.220628+00:00: diagnosed stale published CSS by inspecting loaded stylesheet rules; added asset content versions.

## Decisions
Context: latest feedback restores the time clause. Choice: retain green dot and Expected today, append time not specified.
Context: published HTML used cached CSS with the previous waiting-note rule. Options: ask visitors to clear cache or version source assets. Choice: deterministic content hashes in relative CSS/JS URLs so normal reloads get matching assets. Impact: build.py and page template; compatible with repository-path Pages.

## Challenges & Solutions
Problem: live captions were15px despite local16px. Evidence: live stylesheet contained old waiting-note rule and no pelican-note rule. Solution: content-based asset URL versions, to be verified after deployment.

## Files Modified
- locales/en.json and ru.json: restored time clause.
- build.py and src/page.html: cache-safe asset URLs.
- public/: regenerated site.
- docs/features/coding-card-copy/progress.md: preceding deployment outcome.

## Next Steps
- [x] Implement.
- [x] Verify build and browser.
- [ ] Publish and verify live.

Build, syntax and asset-hash validation passed. Browser confirms full combined status,16px captions, hashed asset URLs and no console errors.
