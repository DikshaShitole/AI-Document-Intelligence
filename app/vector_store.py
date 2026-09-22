import chromadb

from text_splitter import split_text
from embeddings import generate_embeddings


DB_PATH = "data/chroma_db"
COLLECTION_NAME = "documents"


def create_vector_store(chunks, embeddings):
    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    metadatas = [
        {
            "source": "india_epi_factsheet.pdf",
            "chunk_index": i
        }
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    return collection


if __name__ == "__main__":
    text_file_path = "data/extracted/2024_Annual_Report.txt"
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()
    chunks = split_text(text)
    embeddings = generate_embeddings(chunks)
    collection = create_vector_store(chunks, embeddings)
    print("Vector store created successfully")
    print("Total documents:", collection.count())