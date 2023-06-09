import streamlit as st

st.set_page_config(layout='wide')


def main():

    LOGO_SITES_SPECTRAL = st.secrets['LOGO_SITES_SPECTRAL']
    if LOGO_SITES_SPECTRAL: st.sidebar.image(
            LOGO_SITES_SPECTRAL, 
            #width=150,
            caption= 'Swedish Infrastructure for Ecosystem Science (SITES) spectral'
            )

if __name__ == '__main__':
    main()
else:
    st.error('The app failed initialization. Report issue to mantainers in github')