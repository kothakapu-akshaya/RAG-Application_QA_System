import time
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "phi3:mini"


def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are a document question answering assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    print(f"Prompt length: {len(prompt)}")

    start = time.time()

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0,
                    "num_predict": 120,
                    "num_ctx": 1024,
                },
            },
            timeout=180,
        )

        print(f"Ollama responded in {time.time() - start:.2f} seconds")

        response.raise_for_status()
        return response.json()["response"].strip()

    except requests.exceptions.ReadTimeout:
        print(f"Timed out after {time.time() - start:.2f} seconds")
        return "Model timed out."

    except Exception as e:
        print(e)
        return str(e)