# Next Reset backlog

A parking lot for ideas from project conversations. These are possibilities, not commitments. Keep the live page small; move an item into active work only when it is useful and its sources are clear.

## Product ideas

- [ ] **Playful exit-intent subscription creature.** When a desktop visitor moves toward the top edge as if leaving, explore a little creature descending into view and inviting them to subscribe to their tool's next reset. Ivan's idea: «когда юзер уходит ввверх и пытается закрыть браузер, сделать какой-нибуд кричер который будет спускаться и предлагать сперва подписаться». Make the invitation funny and easy to dismiss, at most once per visit; respect reduced motion and keyboard navigation. Browser-close intent cannot be detected reliably, so use a best-effort pointer-exit cue, never intercept or block closing/navigation. Design and validate the experience before implementation; this request adds the idea only.

- [x] **Per-tool reset repositories (prepared in feature/provider-reset-alerts; publication pending).** Keep reset records and release notifications in a separate repository for each tool—Codex, Claude Code, and others as they qualify—so people can watch only the tools they use. Keep Next Reset as the combined overview. Decide how each repository links back to the overview and shares verified history before splitting the current notification repository.
- [ ] **Reset history and cadence.** Once there are enough source-verified events, show how often each provider has reset limits and the time since the last confirmed event. Avoid implying a schedule or predicting a date from sparse data.
- [ ] **Pelican states.** Explore a happy pelican after a completed reset, a calm pelican with a reset ticket for a banked reset, and gently escalating worry when a provider has gone a long time without a confirmed update. Keep the tone calm and make the illustration reflect the event state.
- [ ] **Banked-reset lifecycle.** Distinguish a reset that is announced, still being distributed, available in an account, or redeemed when the source supports those details. Show plan eligibility and timing without guessing.
- [ ] **Reset update releases.** Settle on a small, repeatable release format for source-verified updates so GitHub watchers can follow new records through `Watch → Custom → Releases`.

## Research before adding providers

- [ ] **Cursor and Google Antigravity.** Check official plan and usage documentation, then look for primary-source announcements of exceptional resets. Add either provider only when its subscription reset behavior is clear and supported by sources.

## Later, if people ask for it

- [ ] **Browser notifications.** Revisit web push only if GitHub release notifications prove insufficient; explain the permission prompt and offer a useful mobile experience before enabling it.
- [ ] **Search-friendly copy.** Review the page wording for the phrases people use to look up Codex and Claude Code limit resets, while keeping the first screen concise.
