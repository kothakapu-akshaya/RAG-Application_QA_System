from app.rag.extractor import extract_text
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import VectorStore


class RAGPipeline:
    def __init__(self):
        self.vector_store = None

    def process_document(self, pdf_path: str):
        text = extract_text(pdf_path)
        chunks = chunk_text(text)
        print(f"Total chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks):
            print("=" * 80)
            print(f"CHUNK {i}")
            print(chunk)
        embeddings = generate_embeddings(chunks)

        self.vector_store = VectorStore(384)
        self.vector_store.add(embeddings, chunks)

        return len(chunks)

    def search(self, question: str):
        query_embedding = generate_embeddings([question])[0]
        return self.vector_store.search(query_embedding)
