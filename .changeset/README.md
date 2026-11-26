# Changesets

For user-visible changes, run `npm ci --ignore-scripts` and `npm exec -- changeset`.
Select `ha-location-history-card`, choose the bump, and describe the change in
English. Include the generated Markdown file in your PR. CI and documentation
changes that do not affect users can omit a Changeset.

## Release workflow

Set the repository Actions secret `VERSION_PR_TOKEN` to a fine-grained
personal access token scoped to this repository with Contents and Pull
requests read/write permissions. After Changesets reach `main`, **Prepare
version PR** maintains the `release/version-update` PR. Review the version,
CHANGELOG and consumption record before merging it.

**Validate** checks the test merge for pull requests. Target-branch pushes
schedule fresh checks for same-repository PRs against the exact new base.
Fork PRs use GitHub's native Actions approval. When their base moves without
a source update, they need a fresh native PR event so GitHub can apply that
approval policy. On a managed version PR, `[skip prettier]` in the head
commit message skips only the formatting check for that commit.

Merging the managed PR into `main` runs HACS and hassfest before publishing
`v<version>` with `location_history_card.zip`. To recover the same release,
run **Release integration** from `main` with the original version PR number
and merge SHA. If a published ZIP has different bytes, the workflow stops and
preserves it.

The GitHub release and version PR actions are pinned to
`tellok/actions` main at `9df224593aad286a012adc6760fa7de7cb175e22`,
verified on 2026-11-26 against the
[release skill](https://github.com/tellok/dotai/blob/971a85f244228d5c9248f8d75672a40c4c79c8ed/skills/design-pr-versionization/SKILL.md).
