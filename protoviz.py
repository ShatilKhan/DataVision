import streamlit as st 
import os
from dotenv import load_dotenv
from stmol import showmol
import py3Dmol
from stmol import *

# Load the environment variables from the .env file
load_dotenv()
def app():
    st.title('ProtoViz')
    st.write('Visualize Protein Structures')

    protein_id = st.sidebar.text_input("Enter the PDB ID of the protein")
    residue_ids = st.sidebar.text_input("Enter the Residue IDs (optional, comma-separated)")

    # Check if the protein_id is not empty
    if protein_id:
        view = py3Dmol.view(query=f'pdb:{protein_id}') 
        view.setStyle({'cartoon':{'color':'spectrum'}})

        # If residue_ids are entered, render the residues
        if residue_ids:
            residues = [res.strip() for res in residue_ids.split(',')]
            render_pdb_resn(viewer = view, resn_lst = residues)
        else:
            showmol(view, height = 500,width=800)