from pypdf import PdfReader
def clean_text(text):
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            text = clean_text(text)

        pages.append({
            "page_number": page_number,
            "text": text
        })
    return pages

pdf_path = "data/documents/2024_Annual_Report.pdf"
output_path = "data/extracted/2024_Annual_Report.txt"
pages = extract_text_from_pdf(pdf_path)
with open(output_path, "w", encoding="utf-8") as file:
    for page in pages:
        file.write(f"--- Page {page['page_number']} ---\n")
        file.write(page["text"])
        file.write("\n\n")


print("Number of pages:", len(pages))
print("Extracted and cleaned text saved to:", output_path)