
import streamlit as st

LINK_GITHUB = 'https://github.com/LucaBalduzziNI/streamlit_introduction'
LINK_STREAMLIT_DOCS = 'https://docs.streamlit.io/'

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

def home():

    st.title('Streamlit Introduction')

    st.subheader('Agenda:')
    st.page_link('./pages/1_Basic_Concepts.py', label='Basic Streamlit Concepts ✔️')
    st.page_link('./pages/2_Use_Cases.py', label='Use Cases 📄')
    st.page_link('./pages/3_Widgets.py', label='Widgets ⚙️')
    st.page_link('./pages/4_State.py', label='State 👿')
    st.page_link('./pages/5_Tips_&_tricks.py', label='Tips & Tricks 🎉')
    st.page_link('./pages/6_Your_Turn!.py', label='Your Turn! 👉')
    
    st.divider()
    cols = st.columns(3)
    with cols[1]:
        st.link_button('Public Github Repo', LINK_GITHUB, use_container_width=True)
        st.link_button('Streamlit Docs', LINK_STREAMLIT_DOCS, use_container_width=True)

if __name__ == '__main__':
    home()