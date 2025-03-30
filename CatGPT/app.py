
import streamlit as st

# Set page config
st.set_page_config(
    page_title="CatGPT",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style with black and white gradient and Space Grotesk font
st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');

    html, body, [data-testid="stAppViewContainer"], .center-wrapper {
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #000000 0%, #ffffff 100%);
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
        height: 100%;
        margin: 0;
        padding: 0;
        text-align: center;
    }

    .center-wrapper {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 90vh;
    }

    .stTextInput > div > input {
        background-color: #333;
        color: white;
        border-radius: 8px;
        border: 1px solid #aaa;
    }

    .stTextInput > div > input:focus {
        border: 1px solid #fff !important;
        outline: none !important;
        box-shadow: 0 0 0 0.15rem rgba(255, 255, 255, 0.4);
    }

    .stButton>button {
        background-color: white;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #e0e0e0;
    }

    .e1nzilvr5 { visibility: hidden; }
    </style>
''', unsafe_allow_html=True)

# Start center wrapper
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

# Title
st.markdown("<h1 style='color:white; text-align:center;'>CatGPT</h1>", unsafe_allow_html=True)

# Subtitle with cat gif
st.markdown("""
<p style='color:white; text-align:center; font-size:18px; margin: 0 auto; max-width: 500px;'>
  Well? Can I help you?
</p>
<https://media4.giphy.com/media/t4wfJ082RWlig/200w.gif?cid=6c09b952amn4x29bbg8bljqlbs1ofln5djedxq54zb0b0ju0&ep=v1_gifs_search&rid=200w.gif&ct=g""", unsafe_allow_html=True)

# Input field
user_input = st.text_input("Type something", placeholder="e.g., How are you?", label_visibility="visible")

# Output
if user_input:
    st.success("Meow.")

# End center wrapper
st.markdown('</div>', unsafe_allow_html=True)
