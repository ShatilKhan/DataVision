# This file converts pdf book to training data
import streamlit as st
import pandas as pd
from pdfminer.high_level import extract_text
from pdf2image import convert_from_path
import pytesseract
import tempfile
import PyPDF2

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text

# Use the file_uploader function to allow the user to upload a file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Create a temporary file and save the uploaded file to it
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Pass the path of the temporary file to the extract_text_from_pdf function
    text = extract_text_from_pdf(tmp_path)

    # Convert the text into a DataFrame
    data = pd.DataFrame([text], columns=['text'])

    # Display the DataFrame
    st.write(data)