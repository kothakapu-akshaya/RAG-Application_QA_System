from fastapi import APIRouter

from app.core.rag_instance import rag_pipeline
from app.schemas.query import QueryRequest
from app.rag.llm import generate_answer

router = APIRouter(prefix="/query", tags=["Query"])


@router.post("/")
def query_document(request: QueryRequest):
    results = rag_pipeline.search(request.question)

    if not results:
        return {
            "question": request.question,
            "answer": "No relevant information found."
        }

    # Combine all retrieved chunks
    context = "\n\n".join(results)

    answer = generate_answer(
        question=request.question,
        context=context,
    )

    return {
    "question": request.question,
    "answer": answer,
    }