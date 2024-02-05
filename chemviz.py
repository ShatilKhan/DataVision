import streamlit as st 
import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_ketcher import st_ketcher

# Load the environment variables from the .env file
load_dotenv()

# App
def app():
    st.title('ChemViz')
    st.write('Visualize Chemical Structures')
    smiles = st_ketcher()

   