import streamlit as st 
from openai import AzureOpenAI
import os
from dotenv import load_dotenv
import pandas as pd


# Load the environment variables from the .env file
load_dotenv()

def app():
    st.title('Data Analyst')
    st.write('Analyze & Chat with your Data')

    uploaded_file = st.sidebar.file_uploader("Upload your Dataset", type=["csv"])

    # Add a query input form
    query = st.text_input("Enter your query")


    # Process CSV & Chat
    if uploaded_file is not None:
        input_dataframe = pd.read_csv(uploaded_file)
        st.write(input_dataframe)


    # If a query is entered, process it
    if query:
        st.write(f"You entered: {query}")