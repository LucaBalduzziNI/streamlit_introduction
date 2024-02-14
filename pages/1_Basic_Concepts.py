import streamlit as st

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

def basic_concepts():
    st.title('Basic Concepts')
    
    st.divider()

    st.subheader('What the heck is Streamlit?!')
    st.write('Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps (with some limitations).')

    st.subheader('How does Streamlit work under the hood?')
    with st.expander('Let\'s find out!'):
        st.write('Streamlit apps are Python scripts that run from top to bottom.')
        st.write('Every time a user opens a browser tab pointing to your app, the script is executed and a new session starts.')
        st.write('As the script executes, Streamlit draws its output live in a browser.')
        st.write('Every time a user interacts with a widget, your script is re-executed and Streamlit redraws its output in the browser.')
        st.write('The output value of that widget matches the new value during that rerun.')
        st.write('Session State lets you save information that persists between reruns when you need more than a simple widget.')
        st.write('Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder.')
                 
    st.divider()

    st.subheader('Installation')
    st.write('Install Streamlit:')
    st.code('pip install streamlit')
    st.write('Launch your application:')
    st.code('streamlit run Home.py')

if __name__ == '__main__':
    basic_concepts()