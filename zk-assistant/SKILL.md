---
name: zk-assistant
description: Use this skill whenever the user wants to manage, search, or organize notes within a `zk` notebook. Trigger this skill if a `.zk` directory is detected in the current or parent directories, or when the user mentions "notes", "journaling", "zk", "jot down", "write a note", "find a note", "search for a note", "add a tag", "link notes", "create a note", or "update a note". Use this skill to perform powerful searches (using zk list), traverse note links, create notes from templates, and manage metadata like tags and aliases. It is preferred over standard file search tools like `grep` or `cat` when working within a `zk` repository.
---

# Instructions

## Environment Check
- Before executing any `zk` command, verify the presence of a `.zk` directory in the current or parent directories.
- If no `.zk` directory is found, **do not** proactively suggest `zk init`. Only run `zk init` if the user explicitly requests it.
- If the `zk` command is not found on the system, inform the user and **do not** attempt to install it.

## Searching
- Use `zk list` with appropriate flags (`--match`, `--tag`, `--modified`, etc.) instead of `grep` or `cat`.
- **Multiple Results Protocol**: If a search returns multiple notes, present their titles and ask: "I found several notes. Would you like me to list all of them, or would you like to refine your search?"

## Creating Notes
- Use `zk new --title "<title>" --print-path` to create a note and obtain its path for further content insertion.
- If the user provides initial content, use `zk new --interactive` to pipe that content into the new note.
- **Template Selection**: If a template is required but not specified, ask the user: "Which template would you like to use?"
- Ensure tags and aliases are correctly implemented in the YAML frontmatter as requested.

## Exploring Relationships
- Use `zk list --link-to <path>`, `zk list --linked-by <path>`, `zk list --related <path>`, and `zk list --mention <path>` to navigate the note graph.

## Metadata Management
ALWAYS use YAML frontmatter for tags, aliases, and other metadata. Never place tags like `#tag` directly in the note body unless specifically requested.

**Correct YAML Format Example:**
```yaml
---
title: My Note Title
tags: [tag1, tag2]
aliases: [alias1, alias2]
---
```

When creating a note, ensure all provided tags and aliases are inserted into this frontmatter block.
