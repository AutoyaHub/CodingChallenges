# PDF to Plain Text Extractor App

This project is a PDF to Plain Text Extractor application that allows users to upload PDF documents through a Streamlit interface. The backend, developed with FastAPI, processes these uploads by converting the PDFs into plain text. The converted text is then displayed back to the user within the Streamlit interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Overview

The application demonstrates handling file uploads, integrating FastAPI with Streamlit, and performing PDF to plain text conversion.

## Features

- Upload PDF files through a web interface
- Convert uploaded PDF files to plain text
- Display extracted text in the web interface

## Requirements

- Python 3.8+
- FastAPI
- Streamlit
- PyMuPDF (fitz) or pdfminer.six for PDF to text conversion
- Uvicorn (ASGI server for running FastAPI)
- python-dotenv (for environment variable management)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/sachins-ninjatech/CodingChallenges.git
    cd CodingChallenges
    ```

#### Go inside the submissions/sachin_2024_07_02/document_text_extractor_app


2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip3 install -r requirements.txt
    ```

4. **Create a `.env` file at the root of the project and add the following environment variables:**

    ```env
    FASTAPI_ENDPOINT=http://127.0.0.1:8000/upload/ # ENV file is already added in REPO
    ```

## Usage

1. **Start the FastAPI server:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Open a new terminal window and launch the Streamlit interface:**

    ```sh
    streamlit run streamlit_app.py
    ```

3. **Open your browser and go to `http://localhost:8501` to access the Streamlit interface.**

4. **Upload a PDF file using the file uploader and view the extracted text.**

## Project Structure

- **app/**: Contains the FastAPI application.
  - **main.py**: The entry point for the FastAPI app.
  - **pdf_to_text.py**: Module responsible for handling PDF file uploads and converting them to text.
- **streamlit_app.py**: Script for the Streamlit frontend application.
- **.env**: Environment variables file.
- **requirements.txt**: Specifies project dependencies.
- **README.md**: Project documentation.
