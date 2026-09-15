from pypdf import PdfReader


pdf_path = "data/documents/india_epi_factsheet.pdf"

reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))

for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()

    print(f"\n--- Page {page_number} ---")
    print(text)