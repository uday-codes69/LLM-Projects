import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt, model="tinyllama"):
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": 0.2,
        "max_tokens": 300,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    return r.json()["response"]