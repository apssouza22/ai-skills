# AI Agent related instructions

The rules *.mdc files are cursor rules with front-matter. 

We have rules for Claude and Cursor since the front-matter is different for each one. 

## Cursor rules
A .md file with no YAML front-matter does not define description or globs or alwaysApply: true in the file, so it lines up with that case: it is not auto-attached by globs, not chosen “intelligently” from a
description, and not “always apply” from the file. In practice, that means it only gets loaded into context when you manually @ the rule (unless Cursor is also storing type/metadata for that rule elsewhere,
e.g. from Cursor Settings → Rules — the docs focus on the front-matter model for file behavior).

## Claude rules
So unlike Cursor’s project-rule matrix (where missing description / globs / alwaysApply often means only @-mention), in Claude Code a plain .md rule with no YAML is still loaded into context every session at
launch.

## Symbolic link
Cursor reads the rules from `.agents`. For Claude we need to create symlinks in .claude/

References:
- Cursor rules: https://cursor.com/docs/rules
- Claude rules: https://docs.anthropic.com/claude/reference/custom_rules
