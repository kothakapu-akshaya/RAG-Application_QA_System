from fastapi import APIRouter

from app.core.rag_instance import rag_pipeline
from app.schemas.query import QueryRequest

router = APIRouter(prefix="/query", tags=["Query"])


@router.post("/")
def query_document(request: QueryRequest):
    results = rag_pipeline.search(request.question)

    return {
        "question": request.question,
        "results": results,
    }