import streamlit as st
from bgstools.io import load_yaml


def run():
    st.title('SITES spectral | Field stations map overview')
    st.write('This is a map overview of the field stations')
    
    st.warning('**This is a work in progress**')

    SITES_STATIONS_FILEPATH = st.secrets['PATHS']['SITES_STATIONS_FILEPATH']

    sites = load_yaml(SITES_STATIONS_FILEPATH)

    st.json(sites)


    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()