import fitz  # PyMuPDF
import pdfplumber
from io import BytesIO
import base64

def extract_text_from_pdf(file_content):
    text = ""
    images = []
    
    # Extract text using PyMuPDF
    pdf_document = fitz.open(stream=BytesIO(file_content), filetype="pdf")
    for page_num in range(len(pdf_document)):
        text += f"Page "
        page = pdf_document.load_page(page_num)
        text += page.get_text("text") + "\n\n\n"
    
    # Extract images using pdfplumber
    with pdfplumber.open(BytesIO(file_content)) as pdf:
        for i, page in enumerate(pdf.pages):
            # Extract images
            image_counter = 1  # Counter to keep track of image numbers on each page
            for img in page.images:
                x0, top, x1, bottom = img["x0"], img["top"], img["x1"], img["bottom"]
                page_crop = page.within_bbox((x0, top, x1, bottom))
                image = page_crop.to_image()
                image_buffer = BytesIO()
                image.save(image_buffer, "PNG")
                image_buffer.seek(0)
                image_base64 = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
                image_path = f"page{i+1}_image{image_counter}.png"
                images.append({"path": image_path, "content": image_base64})
                image_counter += 1  # Increment the image counter for the current page
    
    return text, images
