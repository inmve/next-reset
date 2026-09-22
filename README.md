# Token Resets

A quiet page for public AI usage-limit reset announcements. The separate notification repository contains only its minimal README. This repository contains the website and its source data.

## Build

Requires Python 3. No packages, account, API keys or build service are needed.

```sh
python3 build.py
python3 -m http.server 8000 --directory public
```

Open `http://localhost:8000`. Deploy only `public/` to a static host. All asset paths are relative, including when hosted below a repository path.

The included GitHub Pages workflow checks and builds pull requests, and deploys changes merged into `main`. Select GitHub Actions as the publishing source in the website repository's Pages settings. The minimal notification repository does not need a workflow or any additional files.

`site.config.json` selects the name, legacy design identifier, pelican design (1–5), language, public site address and the two repository addresses. The release uses a quiet technical layout with system monospace typography and Night lotus pelicans. Links are omitted until their real addresses are configured. Before a public deployment run:

```sh
python3 build.py --release
```

This refuses to build a release while an address is missing. Notifications live in [`token-resets`](https://github.com/inmve/token-resets); this website is published at [inmve.github.io/token-resets-site](https://inmve.github.io/token-resets-site/).

## Updating records

Edit `data/events.json` after reading the original source. Retain source URLs, affected plans, uncertainty and the actual verification time. Use `announced` for a promise and `confirmed_completed` only for explicit confirmation. Do not silently assume a reset happened when its announced date passes. The page then shows “Confirmation pending”. Provider status comes from its most recent recorded event. This is a manually maintained selection, not an automatic live feed or a personal usage timer.

Rebuild the website after changing records. Copy `minimal-README.md` into the other repository as its sole `README.md`. Do not copy this website, its documentation or data into that repository.

For each meaningful new reset announcement or confirmation, publish one GitHub Release in the notification repository, with the original source and affected scope. This is what triggers **Watch → Custom → Releases** notifications; a README commit does not. Do not publish releases for formatting edits. Check for an existing release before publishing to avoid duplicates.

## Structure

- `data/events.json`: public source records and provider definitions.
- `locales/`: actual English and Russian interface strings.
- `src/`: page, styles and date/motion enhancements.
- `assets/pelicans/`: SVGs in the five approved design directions.
- `build.py`: dependency-free static builder and minimal README generator.
- `public/`: deployable output, including the same factual dataset.

Provider cards and links render without JavaScript. JavaScript updates elapsed days and “today”, and controls the bicycle. Meditation stays still. Reduced-motion preferences pause the ride. There is no analytics, sign-in, browser permission prompt or fake subscription flow.

The central news and browser title follow the date and the recorded events. A pending reset for today reads “Codex limits are likely to reset today”, followed by “Enjoy the ride.” The title includes the viewer's current calendar date, for example `(2026-09-22)`. With no relevant reset news it reads “No resets today”. A confirmed reset today is identified as completed; an old promise is never treated as completion merely because time passed.

The browser-push service from the early prototype is deferred. Initial notifications use GitHub Releases. Releases are published manually for new, source-verified events.
