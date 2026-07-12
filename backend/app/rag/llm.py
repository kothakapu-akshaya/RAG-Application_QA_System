import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"


def generate_answer(question: str, context: str) -> str:
    prompt = f"""
Answer the question using ONLY the context below.

If the answer is not in the context, say:
"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    print(f"Prompt length: {len(prompt)}")

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
                "num_predict": 100,
                "num_ctx": 2048,
            },
        },
        timeout=180,
    )

    response.raise_for_status()

    return response.json()["response"].strip()
