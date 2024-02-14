import streamlit as st
import pandas as pd

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

st.title('Use Cases')

st.divider()

with st.expander('Analyses and Data Visualization'):
    st.write('- Data visualization and data exploration')
    st.write('- Filter and order data')
    
    catalog = pd.read_csv('./media/data/Product_v5.csv')
    st.dataframe(catalog)

with st.expander('Dashboard and Reporting Tools'):
    st.write('- Creation of custom dashboard to analyze KPI (Key Performance Indicators)')
    st.write('- Automate periodic reports to ease the decision process')
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

with st.expander('Automation and Optimization'):
    st.write('- Automate repetitive or complex tasks, such as inventory management')
    st.write('- Develop applications to optimize business processes or daily operations')

    inventory = st.file_uploader('Upload Inventory:', type='csv')
    if inventory is not None:
        st.dataframe(pd.read_csv(inventory))