import streamlit as st
import requests
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get FastAPI endpoint from environment variables
FASTAPI_ENDPOINT = os.getenv("FASTAPI_ENDPOINT")

# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    """
    Streamlit application for uploading a PDF and extracting its text.
    """
    st.title("PDF to Text Extractor")

    # File uploader for selecting a PDF file
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Prepare the file for the request
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
        logging.info(f"Uploaded file details: {uploaded_file.name}")
        
        # Send the file to the FastAPI endpoint
        response = requests.post(FASTAPI_ENDPOINT, files=files)
        
        # Handle the response
        if response.status_code == 200:
            extracted_text = response.json().get("text")
            st.text_area("Extracted Text", extracted_text, height=400)
        else:
            st.error(response.json().get("message"))

if __name__ == "__main__":
    main()
