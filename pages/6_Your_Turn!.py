import streamlit as st

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

st.title('Your Turn!')
st.divider()

st.write('Try to implement the followong behaviour:')
st.write('- Two tabs, one containing a file uploader and one containing settings')
st.write('- In the file uploader tab, show the uploaded file as an editable dataframe')
st.write('- In the settings tab implement a selectbox to select the method (json, csv, etc.) to save the modified file')
st.write('- At the bottom of the page, create a button to save the file in the format choosen in the settings tab')
st.write('Bonus Points:')
st.write('- Implement a "Discard Changes" button')
st.write('- Remake the app to be on multiple pages')