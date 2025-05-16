import os
import sys
import yaml
import openai
import pyperclip
from datetime import datetime

from ai_providers import generate_content

def load_config():
    with open('obsidian_agent/config.yaml', 'r') as f:
        return yaml.safe_load(f)

def get_input_text():
    if len(sys.argv) > 1:
        return ' '.join(sys.argv[1:])
    else:
        return pyperclip.paste()

def apply_template(content, title):
    template = f"""---
ai-content: true
reviewed: false
title: {title}
---

{content}
"""
    return template

def save_to_vault(markdown, title, vault_path):
    filename = f"{title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    filepath = os.path.join(vault_path, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Saved to {filepath}")

def main():
    config = load_config()
    vault_path = config['vault_path']
    openai.api_key = config['openai_api_key']

    text = get_input_text()
    print(f"Input text:\n{text}\n")

    title = input("Enter a title for the new page: ")
    print("Generating content with AI...")
    ai_content = generate_content(text, config['openai_api_key'])
    markdown = apply_template(ai_content, title)

    print("\nGenerated Markdown:\n")
    print(markdown)
    approve = input("Approve and save to vault? (Y/n): ").strip().lower()
    if approve in ('', 'y', 'yes'):
        save_to_vault(markdown, title, vault_path)
    else:
        print("Not saved.")

if __name__ == "__main__":
    main() 