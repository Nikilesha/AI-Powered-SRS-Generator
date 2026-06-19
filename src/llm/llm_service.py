import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"

def generate_srs(prompt):
    payload ={
        "model":MODEL_NAME,
        "prompt":prompt,
        "stream":False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )
    data = response.json()

    return data["response"]