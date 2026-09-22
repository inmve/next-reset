# Breathing pelican

## Current Status
Last Updated: 2026-09-22T13:53:16.106503+00:00
Status: Testing
Completion: 75%

## Current Context
Working: existing meditating SVG subtly expands over seven seconds. Same artwork is embedded on site and exported for README. Reduced-motion disables the animation. Make your tokens count caption and notifications-first README are retained.
Not working: deployment and notification PR#8 pending.
Next: build/check, publish SVG and site, refresh README image hash in existing PR#8, merge and verify.

## Timeline
- 2026-09-22T13:53:16.106503+00:00: user clarified animation means slow breathing; pulled main and created feature/pelican-breathing.
- 2026-09-22T13:53:16.106503+00:00: added gentle CSS scale animation to bird only, fixed shadow, localized description.

## Decisions
Context: user now wants meditation animated. Choice: 7-second ease-in-out cycle, at most 1.5% width and 2.5% height change, anchored at bottom. CSS is self-contained in SVG and works inline or as image.
Context: movement preferences. Choice: prefers-reduced-motion disables breathing.
Context: notification README PR#8 still open. Choice: update it with new image hash before merging to include all current requests without another release.

## Challenges & Solutions
Earlier GitHub API calls intermittently timed out. Read actual PR state before retrying mutations; no duplicate PR created.

## Files Modified
assets/pelicans/pelican-05-meditating.svg, locales/en.json, locales/ru.json, generated public/index.html, public/readme/claude.svg, minimal-README.md; notification README.md.

## Next Steps
- [x] Add subtle breathing and reduced-motion support.
- [ ] Publish and verify site and README.
