import chromadb

from sentence_transformers import SentenceTransformer


DB_PATH = "data/chroma_db"
COLLECTION_NAME = "documents"
MODEL_NAME = "all-MiniLM-L6-v2"


def get_collection():
    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_collection(
        name=COLLECTION_NAME
    )

    return collection


def retrieve_documents(query, top_k=3):
    model = SentenceTransformer(MODEL_NAME)

    query_embedding = model.encode(query)

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results


if __name__ == "__main__":

    query = "What was Microsoft's revenue in fiscal year 2024?"

    results = retrieve_documents(query)

    print("Query:", query)
    print("\nRetrieved documents:")

    for i, document in enumerate(results["documents"][0], start=1):
        print(f"\n--- Result {i} ---")
        print(document)