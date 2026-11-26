---
"ha-location-history-card": patch
---

Show the current Home Assistant avatar on person and device tracker markers, including during playback. A single marker without a current avatar shows the full name. For all initials, split English-style names at whitespace and count each displayed character as a name part in Chinese, Japanese, Korean, Thai, Lao, Khmer, and Burmese scripts. In a group, text markers start with the first part's initial. When initials match, show the complete given name in space-separated scripts and add the surname if the given names also match. Use the recorded name when Home Assistant has yet to load the entity's current name.
