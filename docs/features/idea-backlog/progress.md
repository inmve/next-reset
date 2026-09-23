# Per-tool reset repositories backlog item

## Current Status
Last Updated: 2026-09-23T08:34:00Z
Status: In Progress
Completion: 75%

## Original request
«первая идейка - разьединить на три репозитория и в каждом хранить только по определенным резетам; для клода, для кодекса, и так далее; что б юзеры могли подписываться через вотч только на тот тулз которым они ползуются».

## Decisions
- Add this as the first backlog item, not as an implementation request.
- Describe one notification/data repository per eligible tool, including Codex and Claude Code, so GitHub Watch can be scoped to what each user uses.
- Keep Next Reset as the combined overview.
- Record repository linkage and history ownership as unresolved design questions before any split.

## Timeline
- 2026-09-23: Fetched latest `origin/main`, then created `feature/per-tool-reset-repos` from it.
- 2026-09-23: Added the per-tool repository idea as the first item in `backlog.md`.

## Decisions/Impact
- `backlog.md` now leads with the user's idea; no repositories or notification flows are being split in this task.

## Challenges & Solutions
- None encountered.

## Files Modified
- `backlog.md` — added the per-tool reset repository idea at the top of Product ideas.
- `docs/features/idea-backlog/progress.md` — updated handoff context for this follow-up.

## Current Context
- What's working: the idea is captured with intended user value and overview behavior.
- What's not working: none.
- What's next: review, open and merge a docs-only PR.

## Next Steps
- [x] Fetch main and create a feature branch.
- [x] Add the idea.
- [ ] Open PR and merge.
