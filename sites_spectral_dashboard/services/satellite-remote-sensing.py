import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | Satellite remote sensing Dashboard')
   st.write('This is the main dashboard for Satellite remote sensing')
   st.warning('**This is a work in progress**')
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()