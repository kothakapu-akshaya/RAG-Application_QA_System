from sentence_transformers import SentenceTransformer

# Load the model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks: list[str]):
    """
    Generate embeddings for a list of text chunks.
    """
    embeddings = model.encode(chunks)
    return embeddings