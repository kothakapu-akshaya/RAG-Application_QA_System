import time
from fastapi import APIRouter

from app.core.rag_instance import rag_pipeline
from app.schemas.query import QueryRequest
from app.rag.llm import generate_answer

router = APIRouter(prefix="/query", tags=["Query"])


@router.post("/")
def query_document(request: QueryRequest):
    # Measure retrieval time
    retrieval_start = time.time()

    results = rag_pipeline.search(request.question)

    retrieval_time = time.time() - retrieval_start
    print(f"Retrieval Time: {retrieval_time:.2f} seconds")

    if not results:
        return {
            "question": request.question,
            "answer": "No relevant information found."
        }

    # Combine all retrieved chunks
    context = results[0]

    # Measure LLM generation time
    llm_start = time.time()

    answer = generate_answer(
        question=request.question,
        context=context,
    )

    llm_time = time.time() - llm_start
    print(f"LLM Response Time: {llm_time:.2f} seconds")

    return {
        "question": request.question,
        "answer": answer,
    }