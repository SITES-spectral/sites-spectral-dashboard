import streamlit as st
import pandas as pd


def run():
   st.title('SITES spectral | UAVs planning flying calendar')
   st.write('This is a calendar to schedule the UAVs flights')

   st.warning('**This is a work in progress**')
    

# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()