# GitHub Releases as topic subscriptions

## Current Status
Last Updated: 2026-09-26T11:47:01.818662+00:00
Status: Complete
Completion: 100%

## Current Context
Working: source event/release already published. README generator now leads with GitHub Releases as a way to follow a topic, followed by subscription instructions, current status, then links to other topic feeds.
Incomplete: none. All four PRs merged, live README hashes match reviewed output, site deployment succeeded.
Next: future source-backed announcements only. Current Codex release is already published.

## Original requests
- «также в репо можешь похожие проекыт запустить»
- «делаем акцент на такой своеобразный способ подписки чрез гихаб релищы»
- «а, ну и релиз сделай»

## Decisions
Context: user clarifies the related-projects emphasis. Options: generic project list or other topic feeds using the same subscription mechanism. Choice: other feeds, because the value is subscribing through GitHub Releases. Applies to all three generated provider READMEs; original source quote is retained.
Context: user requests a release. Verified the existing Codex event release is already published and non-draft. Keep that real event release; presentation-only README edits do not warrant another alert according to the project's documented release policy.

## Timeline
- Pulled main and created feature/releases-as-subscriptions in source and three tool feeds.
- Updated generator and both actual locales; moved subscription explanation before current status and added other-feed links.

## Challenges & Solutions
Previous publication completion notes were locally modified. Preserved them in work/provider-reset-alerts-completed.md and a named Git stash before switching main.

## Files Modified
- build.py: generated README order and related-topic links.
- locales/en.json and locales/ru.json: actual localized copy.
- notifications/*/README.md and corresponding feed README.md files: generated user-facing text.
- public/index.html: bundled translated strings.
- This progress log.

## Next Steps
- [x] Validate generated content and existing tests.
- [x] Create and merge PRs, verify published READMEs.
- [x] Verify Codex event release is published: https://github.com/inmve/codex-reset-alerts/releases/tag/codex-reset-announced-2026-09-26

- Validation: five generator tests, release build, JavaScript syntax and whitespace checks passed. Manual generated-output checks confirm subscription comes first and each feed links exactly to the other tool feeds.

## Publication
- Next Reset PR #23 and each dedicated feed PR #2 merged. All attached to this task.
- README blobs in all three remote main branches match reviewed output.
- Pages deployment 36239769344 passed.
- Existing event release verified non-draft: https://github.com/inmve/codex-reset-alerts/releases/tag/codex-reset-announced-2026-09-26
- No duplicate release for presentation edits.
- Usage: 25%, baseline 21%, renewed increase 4 pp, 11 pp remaining; reset 1790755860.
