import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | Fixed sensors dashboard')
   st.write('This is the main dashboard for fixed sensors')
   st.warning('**This is a work in progress**')
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()