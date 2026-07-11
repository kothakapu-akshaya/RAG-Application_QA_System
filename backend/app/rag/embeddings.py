from sentence_transformers import SentenceTransformer

# Load the model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks: list[str]):
    """
    Generate normalized embeddings for semantic search.
    """

    embeddings = model.encode(
        chunks,
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    return embeddings