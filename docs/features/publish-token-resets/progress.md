# Publish Token Resets

## Current Status
- Last Updated: 2026-09-22T10:33:06.059481+00:00
- Status: Ready for Review
- Completion: 100%

## Current Context
- Working: static build, JavaScript syntax, original source links, cautious announcement status, English interface, Russian locale, animated cyclist and still waiting poses, desktop/mobile layout.
- Not working: No launch blockers remain. Future events require manual source verification and publication.
- Next: For a new event, verify its original source, update data, rebuild, merge via feature PR, update the notification README and publish one meaningful release.

## Timeline
- 2026-09-22T10:27:59.674135+00:00: initialized public repositories with GitHub-provided bootstrap commits; pulled main in both clones and created feature branches.
- 2026-09-22T10:27:59.674135+00:00: copied release source, data, SVGs, locales and built HTML. Added public URLs and final Token Resets name. Build/syntax checks and browser review passed at 320px and 1100px.

## Decisions
- Context: public notifications must remain minimal, while website must be forkable. Options: one repository (simple, more clutter) or separate repositories (minimal updates, independent site). Choice: README-only token-resets and website/data in token-resets-site. Impact: site.config.json and generated minimal-README.md.
- Context: upcoming reset is a public promise, not confirmation. Options: definite status (overstates evidence), cautious language (preserves uncertainty). Choice: likely to reset, no inferred hour, no automatic completion. Impact: data/events.json, build.py and src/site.js.
- Context: technical appearance while keeping calm tone. Options: rounded warm panels or restrained mono layout. Choice: monospace, thin borders, soft green, quiet pelicans. Impact: src/style.css and assets/pelicans.
- Context: notifications in v1. Options: implement push backend or use GitHub releases. Choice: Watch → Custom → Releases, one release per meaningful event. Impact: CTA and manual update instructions.
- Context: final public naming. Choice: Token Resets and question When is the next reset?, with current news as the answer. Impact: configuration, locales, template.

## Challenges & Solutions
- Problem: original X posts are unavailable to the text fetcher. Attempted solution: direct fetch returned 403. Final solution: read original posts in browser and retain original links and uncertainty. Lesson: aggregator estimates cannot replace source evidence.
- Problem: network-restricted CLI reports authentication failure. Attempted solution: sandboxed request. Final solution: network-approved gh request succeeded. Lesson: verify network access before asking for login.

## Files Modified
- site.config.json: final name and live destinations.
- src/page.html, src/style.css, src/site.js: technical calm layout, source proof, GitHub CTA, date/motion updates.
- locales/en.json, locales/ru.json: translated UI including the reset question.
- data/events.json: public source-backed records and provider scopes.
- assets/pelicans/: five SVG design families; design 5 selected.
- build.py: generate the static site and minimal repository README.
- public/: committed deployable HTML, JavaScript, styles, favicon and data.
- .github/workflows/pages.yml: PR checks and Pages deployment on main.
- README.md, minimal-README.md, .gitignore: operation instructions, notification repository output, local artifact exclusions.

## Next Steps
- [x] Configure names and URLs.
- [x] Build and check syntax.
- [x] Review browser at desktop and mobile widths.
- [x] Open and validate PRs.
- [x] Enable and deploy GitHub Pages.
- [x] Verify public page and notification README.
- [x] Publish initial source-backed reset release.

## Publication update 2026-09-22T10:31:31.467544+00:00
Both initial PRs were merged after local checks and successful website CI. GitHub Pages is configured for Actions. Deployment run: https://github.com/inmve/token-resets-site/actions/runs/35716265283. Minimal repository root verified to contain only README.md. Website progress record will be finalized after public verification.

## Launch verified 2026-09-22T10:33:06.059481+00:00
Website build and deployment completed successfully. Live https://inmve.github.io/token-resets-site/ opened in the browser with Token Resets branding, original sources, correct GitHub CTA, loaded styles, animated cyclist and no console errors or overflow. public/index.html is committed on main. The notification repository contains exactly README.md. First published release: https://github.com/inmve/token-resets/releases/tag/codex-2026-09-22-announced (not draft). GitHub notification delivery to individual subscribers was not tested; the release channel is ready. Browser push and automatic event monitoring remain outside v1.
