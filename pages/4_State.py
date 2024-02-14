import streamlit as st

LOGO = './media/images/nimbus_logo.png'
st.set_page_config(
    page_title='Streamlit Introduction',
    page_icon=LOGO,
    )

st.title('State')

st.divider()

st.write('Streamlit\'s st.state feature allows you to store and manage stateful information across user interactions within your Streamlit application. This is particularly useful when you need to retain information between different user interactions, such as maintaining the state of a checkbox, slider, or other input widgets.')
st.code("""# Initialize the counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Function to increment the counter
def increment_counter():
    st.session_state.counter += 1

# Display the current value of the counter and a button to increment it
st.write('Counter:', st.session_state.counter)
if st.button('Increment'):
    increment_counter()""")

# Initialize the counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Function to increment the counter
def increment_counter():
    st.session_state.counter += 1

# Display the current value of the counter and a button to increment it
st.write('Counter:', st.session_state.counter)
if st.button('Increment'):
    increment_counter()