# ha-location-history-card

## 1.1.1

### Patch Changes

- ab4235a: Show the current Home Assistant avatar on person and device tracker markers, including during playback. A single marker without a current avatar shows the full name. For all initials, split English-style names at whitespace and count each displayed character as a name part in Chinese, Japanese, Korean, Thai, Lao, Khmer, and Burmese scripts. In a group, text markers start with the first part's initial. When initials match, show the complete given name in space-separated scripts and add the surname if the given names also match. Use the recorded name when Home Assistant has yet to load the entity's current name.

## 1.1.0

### Minor Changes

- 49c3f96: Show an available avatar on person markers, even when only one person is visible. People without avatars use the first initial of their name. When those initials match, use initials from each name part and fall back to the full name if needed.

## 1.0.3

### Patch Changes

- Improved person markers with initials and clustering.
- Refreshed the integration icon and documented common location history use cases.
