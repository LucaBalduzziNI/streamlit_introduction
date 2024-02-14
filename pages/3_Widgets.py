import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

st.title('Widgets')

st.divider()

st.write('Streamlit widgets are interactive elements that you can integrate into your Streamlit applications to enhance user experience and enable user input. These widgets allow users to interact with your application in real-time, providing a dynamic and engaging experience.')

text_tab, data_tab, chart_tab, input_tab, media_tab, layout_tab = st.tabs(['Text Elements', 'Data Elements', 'Chart Elements', 'Input Widgets', 'Media Elements', 'Layout Elements'])

with text_tab:
    st.header('Header')
    st.code('st.header(\'Header\')')
    st.divider()
    
    st.subheader('Subheader')
    st.code('st.subheader(\'Subheader\')')
    
    st.divider()
    
    st.text('Text')
    st.code('st.text(\'Text\')')
    

with data_tab:
    st.subheader('Dataframe')
    st.code('catalog = pd.read_csv(\'./media/data/Product_v5.csv\')\nst.dataframe(catalog)')
    catalog = pd.read_csv('./media/data/Product_v5.csv')
    st.dataframe(catalog)
    st.divider()

    st.subheader('Data Editor')
    st.code('catalog = pd.read_csv(\'./media/data/Product_v5.csv\')\nst.data_editor(catalog)')
    catalog = pd.read_csv('./media/data/Product_v5.csv')
    st.data_editor(catalog)

with chart_tab:
    st.subheader('Charts')
    stocks = pd.read_csv('./media/data/Stocks.csv')
    fig = go.Figure(data=[go.Candlestick(x=stocks['Date'],
                open=stocks['Open'],
                high=stocks['High'],
                low=stocks['Low'],
                close=stocks['Close'])])
    st.plotly_chart(fig)
    st.divider()

    st.subheader('Maps')
    map = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
    st.map(map, use_container_width=True)

with input_tab:
    st.subheader('Buttons')
    st.code('st.button(\'Click Me!\')')
    st.button('Click Me!')
    st.divider()

    st.subheader('Checkboxes')
    st.code('st.checkbox(\'I agree to be amazed by Streamlit\')')
    st.checkbox('I agree to be amazed by Streamlit')
    st.divider()

    st.subheader('Sliders')
    st.code('st.slider(\'Try to find 65378!\', min_value=0, max_value=100000)')
    st.slider('Try to find 65378!', min_value=0, max_value=100000, value=50000)
    st.divider()

    st.subheader('Select Boxes')
    st.code('st.selectbox(\'Select the food you love:\', [\'Pizza\', \'Pizza\']')
    st.selectbox('Select the food you love:', ['Pizza', 'Pizza', 'Pizza', 'Pizza', 'Pizza', 'Pizza', 'Pizza', 'I don\'t like being happy'])

with media_tab:
    st.subheader('Images')
    st.code('st.image(\'./media/images/dog.jpeg\')')
    st.image('./media/images/dog.jpg')
    st.divider()

    st.subheader('Videos')
    st.code('st.video(\'./media/videos/stars.mp4\')')
    st.video('./media/videos/stars.mp4')

with layout_tab:
    st.subheader('Columns')
    st.code('cols = st.columns(2)\ncols[0].text(\'First Column\')\ncols[1].text(\'Second Column\')')
    cols = st.columns(2)
    cols[0].text('First Column')
    cols[1].text('Second Column')
    st.divider()

    st.subheader('Expanders')
    st.code('exp = st.expander(\'Open Me!\')\nexp.text(\'Now I can breathe!\')')
    exp = st.expander('Open Me!')
    exp.text('Now I can breathe!')