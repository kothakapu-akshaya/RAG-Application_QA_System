import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add(self, embeddings, chunks):
        embeddings = np.array(embeddings).astype("float32")
        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, k=3):
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, k)

        results = [self.chunks[i] for i in indices[0]]
        return results