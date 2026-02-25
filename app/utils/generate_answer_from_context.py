import requests

from app.utils import build_prompt
from app.LLM import chat_with_gemini
OLLAMA_URL = "http://localhost:11434/api/generate"
async def generate_answer_from_context(query: str, context: str) -> str:
    prompt = build_prompt(query, context)
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    #answer = await chat_with_gemini(prompt)
    r = requests.post(OLLAMA_URL, json=payload, timeout=120)
    r.raise_for_status()
    answer = r.json()["response"]
    print("abcde         ",answer)
    return answer