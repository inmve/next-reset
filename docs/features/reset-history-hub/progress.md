# Two-feed reset history hub

## Current Status
Last Updated: 2026-09-26T18:30:00.423334+00:00
Status: Ready for Review
Completion: 90%

## Current Context
Canonical schema v2 events imported from active research snapshot: frozen research SHA d57cdebf... now imported: four directly sourced records, two Codex (Sep12/Sep26), two Claude (Apr23/Sep22). Research coverage is partial: 62 unresolved candidates and incomplete Jan–Feb checks. Site and two feed README/JSON files now generate from the same canonical data. All five Python tests and two headline interaction tests pass; release build succeeds. No PR created yet. Network publication and live verification remain.

## Original requests
- «нужно различать banked resets и обычные»
- «все эти три репо (сайт и два этих возьмём под один колпак)»
- «на сайте ... историю из последних 5-10 резетов (да и не только на сайте но и на репо)»
- «время между announced и reset показывать»
- «tibo сбросил лимиты — посмотри там»
- «давай добавляем данные и делаем все как обговорили»
- Earlier correction: title rotates only at load and on click, no 8s timer.

## Decisions
next-reset is canonical; Codex and Claude repos remain notification channels. Grok removed from config/build output because user excludes services not used and took deletion of remote repo manually. No scheduled personal quota windows. Real sources embedded at each fact in v2; unknown occurredAt stays null. Display exact announcement→occurrence hours only if both facts have timestamps and known timezone; otherwise day-level confirmation label or unknown. Banked grant availability is separate. Site shows last five, expandable to ten if available; README shows up to ten. Historical imports don't trigger releases. Genuine new confirmation from Tibo should get one notification after publication.

## Timeline
- 2026-09-26T18:30:00.423334+00:00: preserved prior uncommitted rotating-title work on feature branch; corrected to load/click only, passing two tests.
- 2026-09-26T18:30:00.423334+00:00: added schema v2 adapter, recent history site/README rendering, provider exports, EN/RU strings, removed Grok configuration and old generated feed artifacts.
- 2026-09-26T18:30:00.423334+00:00: five Python tests pass, release build and JS checks pass; Codex Sept26 confirmation source independently read in original X browser.

## Challenges & Solutions
Research coverage partial; most aggregator candidates unresolved. Only verified records are imported. Existing v1 builder expected flat dates; adapter preserves current site behavior during v2 migration. No exact reset instant appears in Tibo's confirmation, so delay to actual reset is not fabricated.

## Files Modified
build.py, data/events.json/schema.json, site.config.json, src/page.html/site.js/style.css, locales/en.json/ru.json, tests/test_build.py/test_title.cjs, generated public assets, notifications/codex+claude/README.md and data/events.json, removed notifications/grok and old Grok SVG, this progress file. Prior feature progress logs preserved.

## Next Steps
- [x] Receive research freeze; recopy exact version, validate schema and sources, rebuild.
- [ ] Inspect desktop/mobile preview and core claims.
- [ ] Update dedicated feed repos on feature branches from fresh main.
- [ ] Create, attach and merge three checked PRs; verify deployment and readback.
- [ ] Publish one genuine Codex confirmation release and verify. No historical release burst.

- 2026-09-26T18:34:24.175295+00:00: froze source dataset at SHA-256 d57cdebf08f6f8c14d25af5d01cb9db570f6059df258f56321dbb636bcf19e4b; build and all 5 Python + 2 JS interaction tests pass. Site and provider exports reconcile to four events. Fixed test fixture that targeted older Codex event.
