import streamlit as st
import requests, base64
from io import BytesIO

# Define the FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/process-pdf/"

# Set page configuration and title
st.set_page_config(page_title="PDF Text Extractor", layout="wide")

# Title and file uploader
st.title("PDF Text Extractor")
st.subheader("Extracted Text")
uploaded_file = st.file_uploader("**Choose a PDF file**", type=["pdf"])

if uploaded_file is not None:
    # Sending file to FastAPI for processing
    with st.spinner("Extracting text and images from PDF..."):
        files = {"file": uploaded_file}
        response = requests.post(FASTAPI_URL, files=files)
        
        if response.status_code == 200:
            result = response.json()
            extracted_text = result["text"]
            extracted_images = result["images"]

            # Display extracted text
            st.success("Text and images extracted successfully!")

            search_query = st.text_input("**Search within extracted text**")
            if search_query:
                results = [line for line in extracted_text.split('\n') if search_query.lower() in line.lower()]
                if results:
                    highlighted_results = '\n\n'.join([line.replace(search_query, f"<mark>{search_query}</mark>") for line in results])
                    st.markdown(highlighted_results, unsafe_allow_html=True)
                else:
                    st.write("No results found.")
            else:
                st.subheader("Extracted Text")
                st.text_area("", extracted_text, height=600)
                
                 # Download extracted text button
                st.download_button(label="Download Extracted Text", data=extracted_text, file_name="extracted_text.txt", mime="text/plain")

            # Sidebar for text manipulation options
            st.sidebar.header("Text Manipulation Options")
            option = st.sidebar.selectbox("Choose an option", ["None", "Uppercase", "Lowercase", "Titlecase"])

            if st.sidebar.button("Apply"):
                if option == "Uppercase":
                    manipulated_text = extracted_text.upper()
                elif option == "Lowercase":
                    manipulated_text = extracted_text.lower()
                elif option == "Titlecase":
                    manipulated_text = extracted_text.title()
                else:
                    manipulated_text = extracted_text
                
                st.subheader("Manipulated Text")
                st.text_area("", manipulated_text, height=400)
            
            # Display extracted images with captions in a grid
            st.header("Extracted Images")

            # Determine the number of columns for the grid
            num_columns = 5
            rows = (len(extracted_images) + num_columns - 1) // num_columns  # Calculate the number of rows needed

            # Display images in a grid
            for row in range(rows):
                cols = st.columns(num_columns)  # Create a row with `num_columns` columns
                for col_idx, img_idx in enumerate(range(row * num_columns, (row + 1) * num_columns)):
                    if img_idx < len(extracted_images):
                        img_info = extracted_images[img_idx]
                        img_data = base64.b64decode(img_info["content"])
                        with cols[col_idx]:
                            st.markdown(f"**{img_info['path']}**")
                            st.image(img_data, caption=img_info["path"], use_column_width=True)
                            st.download_button(label=f"Download {img_info['path']}", data=img_data, file_name=img_info['path'], mime="image/jpeg")

        else:
            st.error(f"Error: {response.json()['detail']}")
