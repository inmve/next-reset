# Pelicans in the notification README

## Current Status
Last Updated: 2026-09-22T13:01:56.725139+00:00
Status: Ready for Review
Completion: 80%

## Current Context
Working: README generator adds a small illustration and caption below each provider announcement. Cycling for the announced Codex reset, meditation for Claude Code. Assets exported by the website build; notification repository retains only README.md.
Not working: public assets and updated README not yet published.
Next: publish website assets first, verify them, then publish README and verify GitHub rendering.

## Timeline
- 2026-09-22T13:01:56.725139+00:00: saved prior completion note in private handoff files; pulled both main branches; created feature/readme-pelicans in both repositories.
- 2026-09-22T13:01:56.725139+00:00: added localized SVG exports and README embeds. Release build, JS syntax, whitespace and XML checks passed.

## Decisions
Context: user wants the site's calm spirit in the repo. Options: commit images into notification repo or host them with website. Choice: website-hosted images preserve the one-README repository.
Context: GitHub theme and motion. Choice: after user requested animation support, export the animated bicycle with a still fallback for prefers-reduced-motion; meditation stays static. A light background plate at 180×135 keeps artwork readable in either GitHub theme.
Context: cached images when a provider state changes. Choice: content-hash query on image URLs refreshes GitHub image caching after artwork changes.
Context: maintainability. Choice: generate image, pose, caption and URL from current provider data and existing locale strings.

## Challenges & Solutions
No implementation blockers. Image deployment must complete before README publication to avoid broken links.

## Files Modified
- build.py: generate README illustrations and embed localized captions.
- public/readme/*.svg: self-contained website-hosted illustrations (animated bicycle, static meditation).
- minimal-README.md: generated draft.
- Separate notification repository README.md: published notification page.

## Next Steps
- [x] Implement and run build, syntax, whitespace and SVG checks.
- [ ] Publish image assets and verify.
- [ ] Publish README and inspect GitHub rendering.

2026-09-22T13:03:19.204160+00:00: User asked whether animation is possible. Updated bicycle export to retain SMIL animation and respect reduced-motion preference via a static fallback. SVG checks confirm eight animation nodes for Codex and zero for Claude.

2026-09-22T13:04:18.646360+00:00: Staged whitespace check found blank lines left by removed SVG metadata. Normalized exported line endings and trailing spaces; regenerated image hashes and README.
