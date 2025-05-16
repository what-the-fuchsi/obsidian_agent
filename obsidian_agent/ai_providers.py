import openai
import yaml
import os
from pathlib import Path

# Load main config
with open('obsidian_agent/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

MAX_TOKENS = config.get('max_tokens', 500)
INITIAL_PROMPT = config.get('initial_prompt', "You are an assistant that generates well-structured markdown pages for Obsidian.")

# Resolve and load secret config
raw_secret_path = config.get('secret-config-path', None)
if not raw_secret_path:
    raise Exception("secret-config-path not set in config.yaml")
secret_path = Path(os.path.expandvars(raw_secret_path))
if not secret_path.exists():
    raise Exception(f"Secret config file not found at {secret_path}")
with open(secret_path, 'r') as f:
    secret_config = yaml.safe_load(f)
api_key = secret_config.get('openai_api_key')
if not api_key:
    raise Exception("openai_api_key not found in secret config")

def generate_content(text, api_key_override=None):
    key = api_key_override if api_key_override else api_key
    client = openai.OpenAI(api_key=key)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": INITIAL_PROMPT},
            {"role": "user", "content": text}
        ],
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content.strip() 