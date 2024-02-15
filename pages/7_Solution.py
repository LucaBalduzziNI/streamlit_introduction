import streamlit as st
import pandas as pd

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

if 'file_type' not in st.session_state:
    st.session_state['file_type'] = 'csv'


st.title('Solution')
st.divider()

upload_tab, edit_tab, settings_tab = st.tabs(['Upload', 'Edit', 'Settings'])

with upload_tab:
    f = st.file_uploader('Upload your file (csv):', type='csv')

with edit_tab:
    if f is None:
        st.error('Please upload your csv file!')
    else:
        st.write('Edit your file:')
        data = pd.read_csv(f)
        edited = st.data_editor(data)

        # Building the new file name with the correct extension
        new_file_path = f.name.replace('.csv', '')
        suffix = '_new'
        if st.button('Save file'):
            if st.session_state['file_type'] == 'csv':
                edited.to_csv(new_file_path + suffix + '.' + st.session_state['file_type'])
            elif st.session_state['file_type'] == 'json':
                edited.to_json(new_file_path + suffix + '.' +  st.session_state['file_type'])

with settings_tab:
    method = st.selectbox('Select the extension for the saved file:', ['csv', 'json'])
    if st.button('Save Settings'):
        st.session_state['file_type'] = method
        

