import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | UAVs Dashboard')
   st.write('This SITES spectral UAVs dashboard')
   st.warning('**This is a work in progress**')
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()