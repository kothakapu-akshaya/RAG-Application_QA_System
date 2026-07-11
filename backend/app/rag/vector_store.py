import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):
        # Use cosine similarity (via inner product on normalized vectors)
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embeddings, chunks):
        embeddings = np.array(embeddings).astype("float32")
        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, k=5):
        query_embedding = np.array([query_embedding]).astype("float32")

        scores, indices = self.index.search(query_embedding, k)

        print("\nTop Retrieved Chunks")
        print("-" * 60)

        results = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            print(f"\nScore: {score:.4f}")
            print(self.chunks[idx][:250])
            print("-" * 60)

            results.append(self.chunks[idx])

        return results