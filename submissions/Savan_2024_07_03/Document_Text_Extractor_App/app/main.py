import subprocess
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import PlainTextResponse, RedirectResponse, JSONResponse
from .pdf_to_text import extract_text_from_pdf
from io import BytesIO

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Start the Streamlit app
    subprocess.Popen(["streamlit", "run", "streamlit_app.py", "--server.port", "8501"])


@app.get("/")
def read_root():
    # Redirect to the Streamlit app
    return RedirectResponse(url="/streamlit")

@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...)):
    file_content = await file.read()
    text, images = extract_text_from_pdf(file_content)
    
    # Save the extracted text to a file in memory
    output_text = BytesIO()
    output_text.write(text.encode('utf-8'))
    output_text.seek(0)
    
    # Return paths and in-memory files
    return JSONResponse(content={
        "text": text,  # You can send the text content directly or provide a download link
        "images": images
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


