import requests
import time

start = time.time()

response = requests.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": "What is RNN?",
        "stream": False,
    },
    timeout=120,
)

print("Time:", time.time() - start)
print("Status:", response.status_code)
print("Answer:", response.json()["response"])