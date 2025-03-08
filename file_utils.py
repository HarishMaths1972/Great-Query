def save(uploaded_files):
    import streamlit as st
    import pandas as pd

    for file in uploaded_files:
        file_path = file.name
        if '.csv' in file_path:
            st.session_state['df_path'] = file_path
        else:
            st.session_state['meta'] = file_path

        with open(file_path,"wb") as f:
            f.write(file.getbuffer())

        if 'df_path' in st.session_state and 'meta' in st.session_state:
            st.session_state['df'] = pd.read_csv(st.session_state['df_path'])
            st.session_state['metadata'] = open(st.session_state['meta'])