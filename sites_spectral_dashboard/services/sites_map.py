import streamlit as st
from bgstools.io import load_yaml

SITES_STATIONS_FILEPATH = st.secrets['PATHS']['SITES_STATIONS_FILEPATH']

sites = load_yaml(SITES_STATIONS_FILEPATH)

st.title('SITES spectral stations')
st.json(sites)

st.map(sites)