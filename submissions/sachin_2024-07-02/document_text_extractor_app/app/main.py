import logging
from fastapi import (
    FastAPI, 
    File, 
    UploadFile, 
    HTTPException
)
from .pdf_to_text import convert_pdf_to_text

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF file and convert it to plain text.

    Args:
        file (UploadFile): The uploaded PDF file.

    Returns:
        dict: A dictionary containing the extracted text from the PDF.
    
    Raises:
        HTTPException: If the uploaded file is not a PDF.
    """
    logging.info(f"Received file: {file.filename}, content_type: {file.content_type}")

    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")
    
    content = await file.read()
    text = convert_pdf_to_text(content)
    return {"text": text}
