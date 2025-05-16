from fastapi import FastAPI
from pydantic import BaseModel
from obsidian_agent.ai_providers import generate_content
import yaml

app = FastAPI()

# Load config and API key
with open('obsidian_agent/config.yaml', 'r') as f:
    config = yaml.safe_load(f)
api_key = config['openai_api_key']

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_markdown(req: PromptRequest):
    result = generate_content(req.prompt, api_key)
    return {"markdown": result} 