import streamlit as st
import yaml
import pandas as pd
import streamlit.components.v1 as components

def survey_state():
    if 'survey' not in st.session_state:
        st.session_state.survey = {}    
        
    survey = st.session_state.survey

    return survey


def new_survey():
    survey_form = st.form(key='survey_form', clear_on_submit=False)
    with survey_form:
        survey_name = st.text_input(
            label='**Survey name:**',
            placeholder='Enter survey name')
        submit_button = st.form_submit_button(label='Submit')
        if submit_button and survey_name:
            survey = survey_state()
            if survey_name not in survey:
                survey[survey_name] = {}
                st.session_state.survey = survey
                st.session_state.survey_name = survey_name
                st.experimental_rerun()
            else:
                st.error(f'Survey `{survey_name}` already exists')
        else:
            st.warning('Please fill the **survey_name**')

    if survey_name:
        return survey_name
    

def new_station(station_name):
    return {station_name: {'media':{'frames':{}}}}
            

def run():
    st.title("SEAMS-App Survey Initialization")
    st.write("This is the survey initialization page. Here you can initialize a new survey or load an existing one.")
    
    new_survey()

# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()