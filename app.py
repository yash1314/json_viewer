import streamlit as st

st.title(":rainbow[JSON Viewer]")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

st.markdown("""You can now view your Json Data Format with ease. Just Copy your Json Data in Side text
and get your formatted json data.""")
st.markdown('------------------------------------------')

user_input = st.sidebar.text_area('Enter your data here')

button = st.sidebar.button('Format')

if button:
    if user_input[:] == "":
        st.warning('Enter your message!')
    else:
        st.json(user_input, expanded=True)