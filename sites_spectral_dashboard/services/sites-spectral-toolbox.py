import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | Toolbox')
   st.write('This is SITEs spectral toolbox')
   st.warning('**This is a work in progress**')
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()