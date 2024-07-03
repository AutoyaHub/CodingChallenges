# PDF Text and Image Extractor

This project is a web application designed to extract text and images from PDF files. The backend is powered by FastAPI, while the frontend is built with Streamlit. This combination allows for a high-performance, user-friendly interface for processing and viewing the content of PDF files.

## Features

- **Upload PDF Files**: Users can upload PDF files directly through the Streamlit interface.
- **Text Extraction**: Extracts text from PDF files, excluding tables.
- **Image Extraction**: Extracts and displays images found within the PDF.
- **Text Search**: Users can search for specific text within the extracted content.
- **Text Manipulation**: Options to manipulate the extracted text (e.g., convert to uppercase, lowercase, titlecase).
- **Download Options**: Download the extracted text as a `.txt` file and download images individually.
- **Original PDF View**: Embedded view of the original PDF for reference.

## Technologies Used

- **FastAPI**: For creating the backend RESTful API.
- **Streamlit**: For the frontend user interface.
- **pdfplumber**: For extracting text and images from PDF files.
- **uvicorn**: ASGI server for running the FastAPI application.
- **Requests**: For handling HTTP requests within Streamlit.

## Getting Started

### Project Structure

.
├── app/
│ ├── main.py # FastAPI application file
│ ├── pdf_to_text.py # PDF text and image extraction logic
├── streamlit_app.py # Streamlit frontend application file
├── requirements.txt # Python dependencies
└── README.md # Project documentation


### Prerequisites

- Python 3.6+
- `pip` (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pdf-extractor.git
   cd pdf-extractor

2. **Create and activate a virtual environment:**
    ```On macOS and Linux:
    python3 -m venv venv    
    source venv/bin/activate

    ```On Windows:
    python -m venv venv
    .\venv\Scripts\activate

3. **Install the required dependencies:**
    ```pip install -r requirements.txt


### Running the Application

1. **Start the FastAPI backend and Streamlit Frontend:**
    ```uvicorn app.main:app --reload


```markdown
 PyMuPDF can only convert the text within a PDF. Additionally, I used pdfplumber to extract images from the PDF.
\```
