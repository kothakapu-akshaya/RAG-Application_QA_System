import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"


def generate_answer(question: str, context: str) -> str:
    """
    Generate an answer using Ollama based only on the retrieved context.
    """

    prompt = f"""
You are a helpful assistant for answering questions from uploaded documents.

Rules:
1. Answer ONLY using the provided context.
2. Do not make up information.
3. If the answer is not found in the context, reply:
   "I couldn't find the answer in the uploaded document."
4. Give concise answers.

Context:
{context}

Question:
{question}

Answer:
"""

    print("Sending prompt to Ollama...")

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0,
                "num_predict": 200
            }
        },
        timeout=300,
    )

    print("Response received from Ollama")

    response.raise_for_status()

    return response.json()["response"].strip()