import streamlit as st
import pandas as pd


def run():
   st.title('UAVs flying calendar')
   st.write('This is a calendar to schedule the UAVs flights')
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()