from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        separators=[
            "\n# ",
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            " ",
            "",
        ],
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_text(text)

    print("\n========== GENERATED CHUNKS ==========\n")
    for i, chunk in enumerate(chunks):
        print(f"\n----- CHUNK {i} -----")
        print(chunk[:300])  # Print first 300 characters
        print("-" * 60)

    return chunks