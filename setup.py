import streamlit as st
from assets import logo,icon

def page_setup():
    st.set_page_config(
    page_title="Great Story",
    page_icon=icon)

    st.logo(logo,size='large',link='https://www.mygreatlearning.com/')

    col1, col2, col3 = st.columns([2, 4, 1])

    with col2:
        st.title("Great Query :penguin:")