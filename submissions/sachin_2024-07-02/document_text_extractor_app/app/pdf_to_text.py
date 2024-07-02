import fitz  # PyMuPDF
import logging

def convert_pdf_to_text(pdf_bytes: bytes) -> str:
    """
    Converts a PDF document provided as bytes to a plain text string.

    Args:
        pdf_bytes (bytes): The PDF document as bytes.

    Returns:
        str: The extracted plain text from the PDF.
    """
    try:
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        text = []
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text.append(page.get_text())
        
        return "\n".join(text)
    except Exception as e:
        logging.error(f"Error converting PDF to text: {e}")
        return ""
