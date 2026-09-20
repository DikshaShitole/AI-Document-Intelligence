from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def generate_embeddings(chunks):
    model = SentenceTransformer(MODEL_NAME)

    embeddings = model.encode(chunks)

    return embeddings


if __name__ == "__main__":
    from text_splitter import split_text

    text_file_path = "data/extracted/india_epi_factsheet.txt"

    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = split_text(text)

    embeddings = generate_embeddings(chunks)

    print("Total chunks:", len(chunks))
    print("Total embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))
    print("First 5 values:", embeddings[0][:5])