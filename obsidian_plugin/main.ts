import { Plugin, Notice } from 'obsidian';

export default class MarkdownAIGenerator extends Plugin {
  async onload() {
    this.addCommand({
      id: 'generate-md-from-ai',
      name: 'Generate Markdown from AI',
      callback: async () => {
        let clipboardText = '';
        try {
          clipboardText = await navigator.clipboard.readText();
        } catch (e) {
          new Notice('Failed to read clipboard.');
          console.error(e);
          return;
        }
        if (!clipboardText) {
          new Notice('Clipboard is empty.');
          return;
        }
        try {
          const response = await fetch('http://127.0.0.1:8000/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: clipboardText })
          });
          if (!response.ok) throw new Error('Server error');
          const data = await response.json();
          const activeLeaf = this.app.workspace.activeLeaf;
          if (activeLeaf && data.markdown) {
            // Insert the markdown at the cursor position
            // @ts-ignore
            activeLeaf.view.editor.replaceSelection(data.markdown);
            new Notice('Markdown inserted!');
          } else {
            new Notice('No active editor or no markdown returned.');
          }
        } catch (e) {
          new Notice('Failed to contact AI server or an error occurred.');
          console.error(e);
        }
      }
    });
  }
} 