import streamlit as st
import protoviz , agent, chemviz, dataviz, live

PAGES = {
    "Rsearch Agent" : agent,
    "Data Analysis" : dataviz,
    "IoT DataStream" : live,
    "Protein Visualization": protoviz,
    "Chemical Visulaization" : chemviz,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()