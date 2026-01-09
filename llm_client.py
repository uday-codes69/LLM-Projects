import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(
    prompt,
    model="tinyllama",
    temperature=0.6,
    max_tokens=200,
    top_p=0.9,
    top_k=40,
    min_p=0.0
):
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "top_k": top_k,
        "min_p": min_p,
        "stream": True
    }

    full_response = ""

    r = requests.post(OLLAMA_URL, json=payload, stream=True)

    for line in r.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))

            if "response" in data:
                full_response += data["response"]

            if data.get("done"):
                break

    return full_response