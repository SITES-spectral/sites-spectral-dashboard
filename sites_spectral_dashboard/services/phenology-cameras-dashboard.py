import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | Phenology cameras Dashboard')
   st.write('This is the main dashboard for Phenology cams')

   st.warning('**This is a work in progress**')
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()