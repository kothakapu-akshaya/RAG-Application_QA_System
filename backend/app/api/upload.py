from pathlib import Path
import shutil

from fastapi import APIRouter, File, UploadFile

from app.core.rag_instance import rag_pipeline

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the uploaded document
    total_chunks = rag_pipeline.process_document(str(file_path))

    return {
        "message": "Document uploaded successfully!",
        "filename": file.filename,
        "chunks": total_chunks,
    }