import streamlit as st
import datetime

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

st.title('Tips & Tricks')

st.divider()

st.subheader('Centered Buttons')
st.code("""cols = st.columns(3)\ncols[1].button('Centered Button', use_container_width=True)""")
cols = st.columns(3)
cols[1].button('Centered Button', use_container_width=True)
st.divider()

st.subheader('Context Manager')
st.code("""expander = st.expander('Expander')
with expander:
    st.write('Inside expander')
st.write('Outside expander')
with expander:
    st.write('Inside expander again!')""")
expander = st.expander('Expander')
with expander:
    st.write('Inside expander')
st.write('Outside expander')
with expander:
    st.write('Inside expander again!')
st.divider()

st.subheader('Empty Widget')
st.code("""empty = st.empty()
st.write('Some stuff')
cols_2 = st.columns(2)
appear = cols_2[0].button('Appear!', use_container_width=True)
disappear = cols_2[1].button('Disappear!', use_container_width=True)
if appear:
    with empty:
        st.write('I appeared on top!')
elif disappear:
    empty.empty()
""")
empty = st.empty()
st.write('Some stuff')
cols_2 = st.columns(2)
appear = cols_2[0].button('Appear!', use_container_width=True)
disappear = cols_2[1].button('Disappear!', use_container_width=True)
if appear:
    with empty:
        st.write('I appeared on top!')
elif disappear:
    empty.empty()
st.divider()

st.subheader('Cache')
st.code("""@st.cache_data
def some_function(database: str) -> list:
    if database == 'DB':
        data = datetime.datetime.now()
    else:
        data = datetime.datetime.now()
    return data

cols_3 = st.columns(2)
clicked_1 = cols_3[0].button('Call with "DB"', use_container_width=True)
clicked_2 = cols_3[1].button('Call with gibberish', use_container_width=True)
st.button('Clear Cache', on_click=st.cache_data.clear)
empty = st.empty()
with empty:
    if clicked_1:
        data = some_function('DB')
    if clicked_2:
        data = some_function('kjfekljweewj')
    if clicked_1 or clicked_2:
        st.write(data)""")

@st.cache_data
def some_function(database: str) -> list:
    if database == 'DB':
        data = datetime.datetime.now()
    else:
        data = datetime.datetime.now()
    return data

cols_3 = st.columns(2)
clicked_1 = cols_3[0].button('Call with "DB"', use_container_width=True)
clicked_2 = cols_3[1].button('Call with gibberish', use_container_width=True)
st.button('Clear Cache', on_click=st.cache_data.clear)
empty = st.empty()
with empty:
    if clicked_1:
        data = some_function('DB')
    if clicked_2:
        data = some_function('kjfekljweewj')
    if clicked_1 or clicked_2:
        st.write(data)
