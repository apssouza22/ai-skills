# AI Skills

A collection of reusable AI agent skills for code review, image generation, and diagramming. Designed for Cursor but portable to any AI coding tool that supports custom instructions.

## Available Skills

| Skill | Description |
|-------|-------------|
| [browser-tools](skills/browser-tools/) | Interactive browser automation via Chrome DevTools Protocol for web page interaction, frontend testing, and scraping. |
| [c4-architecture](skills/c4-architecture/) | Generate architecture documentation using C4 model Mermaid diagrams (context, container, component, deployment). |
| [cli-code-review](skills/cli-code-review/) | Manual code review of uncommitted changes from the terminal using Vim, with file change heatmaps and side-by-side diffs. |
| [code-review-expert](skills/code-review-expert/) | Senior engineer code review covering SOLID, security, performance, code structure, and error handling. Supports local git changes and GitHub PR URLs. |
| [draw-io](skills/draw-io/) | draw.io diagram creation, editing, and review. Supports .drawio XML editing, PNG conversion, layout adjustment, and AWS icon usage. |
| [humanizer](skills/humanizer/) | Remove signs of AI-generated writing from text. Detects and fixes inflated symbolism, promotional language, AI vocabulary, and other telltale patterns. |
| [marp-slide](skills/marp-slide/) | Create professional Marp presentation slides with 7 built-in themes, custom image layouts, and automatic quality improvements. |
| [nano-banana-pro](skills/nano-banana-pro/) | Generate images from text prompts using Google Gemini. |
| [pdf](skills/pdf/) | PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms. |
| [pptx](skills/pptx/) | Presentation creation, editing, and analysis for .pptx files with template support, thumbnail generation, and visual validation. |
| [vscode](skills/vscode/) | VS Code integration for viewing diffs and comparing files side by side. |
| [youtube-transcript](skills/youtube-transcript/) | Fetch transcripts from YouTube videos for summarization and analysis. |

## Installation for Cursor

Skills can be installed **globally** (available in all projects) or **per-project**.

### Global Installation (all projects)

Copy a skill folder into your global Cursor skills directory:

```bash
# Clone the repo
git clone https://github.com/alexsandro-souza/ai-skills.git

# Copy a skill to Cursor's global skills directory
cp -r ai-skills/skills/code-review-expert ~/.cursor/skills/
cp -r ai-skills/skills/code-review-expert ~/.claude/skills/
```

Global skills are available in every Cursor workspace without any per-project setup.

### Per-Project Installation

Copy a skill folder into your project's `.cursor/skills/` directory:

```bash
# From your project root
mkdir -p .cursor/skills

# Copy the skill you need
cp -r /path/to/ai-skills/skills/code-review-expert .cursor/skills/
```

Alternatively, add this repo as a git submodule to keep skills up to date:

```bash
# From your project root
git submodule add https://github.com/alexsandro-souza/ai-skills.git .cursor/ai-skills

# Symlink the skills you need
mkdir -p .cursor/skills
ln -s ../ai-skills/skills/code-review-expert .cursor/skills/code-review-expert
```

### Verify Installation

After installing, the skill should appear in Cursor. You can invoke it by name in the chat (e.g., `/code-review-expert`) or reference it in your prompt.

### Directory Structure

```
# Global
~/.cursor/skills/
└── code-review-expert/
    ├── SKILL.md              # Skill instructions (main file)
    ├── agents/
    │   └── agent.yaml        # Agent interface config
    └── references/           # Supporting checklists and guidelines
        └── *.md

# Per-project
your-project/
└── .cursor/
    └── skills/
        └── code-review-expert/
            ├── SKILL.md
            ├── agents/
            └── references/
```

## License

MIT
