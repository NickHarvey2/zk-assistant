# zk-assistant

A specialized skill designed to empower agents to interact seamlessly with a `zk` notebook. Instead of relying on generic filesystem tools like `grep` or `cat`, this skill leverages the full power of the `zk` command-line tool to manage, search, and organize your plain-text notes.

## 🚀 Capabilities

- **Intelligent Searching**: Uses `zk list` with advanced filtering (tags, dates, content matches) instead of standard text searches.
- **Smart Note Creation**: Supports creating new notes with specific titles, content, and templates.
- **Metadata Management**: Automatically handles YAML frontmatter for tags, aliases, and other metadata.
- **Graph Exploration**: Navigates the web of links between notes using `zk`'s relationship discovery features (backlinks, mentions, related notes).
- **Context Awareness**: Detects if it is operating within a `zk` repository and behaves appropriately.

## 🛠 How to Use

This skill is designed to be triggered automatically when you mention notes, journaling, or specific `zk` actions.

### Example Prompts

- **Creating Notes**:
  - *"Create a new note titled 'Project Alpha Strategy' with the tag #project and content: 'Focus on modular architecture.'"*
  - *"Start a new daily journal entry using my 'daily' template."*

- **Searching**:
  - *"Find all my notes that mention 'Python'."*
  - *"Show me all notes I've modified in the last week."*

- **Exploring Relationships**:
  - *"Show me all notes that are linked to the note '2024-05-31-meeting'."*
  - *"Find all mentions of 'Artificial Intelligence' in my notebook."*

- **Managing Metadata**:
  - *"Add the tag #important to the note titled 'annual-review'."*
  - *"Add an alias 'AI' to my 'Artificial Intelligence' note."*

## 📋 Requirements

- **`zk` CLI**: This skill requires the [zk](https://github.com/zk-org/zk) command-line tool to be installed on your system.
- **`zk` Notebook**: The skill is most effective when used within a directory initialized as a `zk` notebook (contains a `.zk` directory).

## 📦 Installation

1. Download the `.skill` package or the `zk-assistant` directory.
2. Place the directory in your opencode skills path.
3. (Optional) If using the packaged version, follow your environment's specific installation instructions.
