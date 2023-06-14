import os
import streamlit as st
from collections import OrderedDict
from bgstools.io import get_available_services
from bgstools.stt import build_activities_menu


st.set_page_config(
    layout='wide',
    page_title='SITES spectral',
    page_icon=':sun:',
    initial_sidebar_state='expanded',
    )


def run():
    LOGO_SITES_SPECTRAL = st.secrets['LOGOS']['LOGO_SIDEBAR_URL']
    if LOGO_SITES_SPECTRAL: st.sidebar.image(
            LOGO_SITES_SPECTRAL,             
            caption= 'Swedish Infrastructure for Ecosystem Science (SITES) spectral'
            )
        
    # Load the available services
    SERVICES_FILEPATH = st.secrets['PATHS']['SERVICES_FILEPATH']
    SERVICES_DIRPATH = st.secrets['PATHS']['SERVICES_DIRPATH']

    # Load the yaml with core services as activities    
    core_activities =  get_available_services(
        services_filepath=os.path.abspath(SERVICES_FILEPATH)        
    )
       
    build_activities_menu(
            activities_dict=core_activities, 
            label='**SITES spectral activities:**', 
            key='activitiesMenu', 
            services_dirpath=os.path.abspath(SERVICES_DIRPATH),
            disabled=False
            )


if __name__ == '__main__':
    run()
else:
    st.error('The app failed initialization. Report issue to mantainers in github')




if __name__ == '__main__':
    run()
else:
    st.error('The app failed initialization. Report issue to mantainers in github')