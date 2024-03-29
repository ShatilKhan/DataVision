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
    molecule = st.text_input("Molecule", "C[N+]1=CC=C(/C2=C3\C=CC(=N3)/C(C3=CC=CC(C(N)=O)=C3)=C3/C=C/C(=C(\C4=CC=[N+]"
    "(C)C=C4)C4=N/C(=C(/C5=CC=CC(C(N)=O)=C5)C5=CC=C2N5)C=C4)N3)C=C1")
    smile_code = st_ketcher(molecule)
   