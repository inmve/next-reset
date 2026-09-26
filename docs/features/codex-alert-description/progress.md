# Codex alert title and description

## Current Status
Last Updated: 2026-09-26T11:50:48.665867+00:00
Status: Complete
Completion: 100%

## Current Context
Working: wording corrected; Codex-specific title/intro use real EN/RU locale keys in canonical generator. Original reset quote and release preserved.
Incomplete: none. About metadata and README title/intro are published and verified.
Next: future source-backed announcements.

## Original request
«можно явно сказать в описании гихаба и в тайтле - Alerting the upcoming codex limit resets. Whenver codex is known to get reseted, a new release of tis repo is published so you get a chance to spend all your remaining tokens before limits are rests (поправь gramma)»

## Decisions
Context: user wants clear benefit in title/About. Options: rename repository URL or change README title and GitHub About. Choice: title and About; existing share URL remains appropriate. Say announced, with a chance to use remaining tokens; no guarantee of lead time or confirmed completion. Codex-specific locale overrides keep other feeds' copy stable.

## Timeline
- Saved previous local completion notes, pulled main and created feature/codex-alert-description in source and feed.
- Updated canonical generator and English/Russian strings.

## Challenges & Solutions
Previous local handoff edits preserved in work/releases-as-subscriptions-completed.md and named Git stash before switching branches.

## Files Modified
build.py; locales/en.json; locales/ru.json; generated notifications/codex/README.md and public/index.html; Codex feed README.md; this progress log. GitHub About metadata to be updated.

## Next Steps
- [x] Validate and publish PRs.
- [x] Update About and verify live title/description.

## Completion
- Source PR #24 and Codex feed PR #3 merged and attached to task.
- Five tests, release build, JavaScript syntax and whitespace checks passed.
- GitHub About description read back exactly; remote main README hash matches local reviewed generated file.
- Final title: Alerts for upcoming Codex usage-limit resets.
- No new event release needed for wording-only changes; original published event remains linked.
- Shell readback initially used an unquoted question mark in an API URL; retried with quoted URL and verified successfully. No publication was affected.
