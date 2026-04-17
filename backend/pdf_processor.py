import io
import fitz  # PyMuPDF

def extract_text(file_bytes: bytes) -> str:
    """
    Extract text from a PDF file provided as bytes.
    Uses PyMuPDF (fitz) to open the PDF from memory and concatenate text from all pages.
    Cleans extra whitespace and returns a single string.
    """
    # Open the PDF from bytes
    pdf_document = fitz.open(stream=file_bytes, filetype="pdf")
    full_text = []
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text()
        if text:
            full_text.append(text)
    
    pdf_document.close()
    
    # Join all pages and clean up whitespace
    combined = " ".join(full_text)
    # Replace multiple newlines and spaces with a single space
    cleaned = " ".join(combined.split())
    return cleaned
