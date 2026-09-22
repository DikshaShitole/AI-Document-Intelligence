from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(text)

    return chunks


if __name__ == "__main__":
    text_file_path = "data/extracted/2024_Annual_Report.txt"

    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    chunks = split_text(text)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:5], start=1):
        print(f"\n--- Chunk {i} ---")
        print(chunk)