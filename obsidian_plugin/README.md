# Markdown AI Generator Obsidian Plugin

This plugin allows you to generate markdown content in Obsidian using a local Python AI server.

## Setup

1. Make sure your Python server is running (see the main project README).
2. Install dependencies and build the plugin:
   ```sh
   npm install
   npm run build
   ```
3. Copy `main.js`, `manifest.json`, and (optionally) `styles.css` to your Obsidian vault's `.obsidian/plugins/markdown-ai-generator/` directory.
4. Enable the plugin in Obsidian settings.

## Usage

- Use the command palette to run "Generate Markdown from AI" and follow the prompt. 