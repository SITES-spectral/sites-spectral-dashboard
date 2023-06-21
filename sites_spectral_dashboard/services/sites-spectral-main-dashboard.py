import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | Main Dashboard')
   st.write('This is the main dashboard for the SITES spectral project') 
   st.warning('**This is a work in progress**')
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()