from app.rag.extractor import extract_text
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings
from app.rag.vector_store import VectorStore

text = extract_text("data/uploads/Ultimate PYQS DIRECTORY (2007-2026).pdf")

chunks = chunk_text(text)

embeddings = generate_embeddings(chunks)

# Create vector store
store = VectorStore(len(embeddings[0]))

# Store embeddings
store.add(embeddings, chunks)

# Search using a sample query
query = "GATE CS 2019 paper"

query_embedding = generate_embeddings([query])[0]

results = store.search(query_embedding)

print("\nTop Results:\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}:")
    print(result[:300])
    print("-" * 50)
