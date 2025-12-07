import streamlit as st

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="CatGPT",
    page_icon="🐱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------ THEME STATE & TOGGLE ------------------ #
if "theme" not in st.session_state:
    st.session_state.theme = "dark"  # default

# Right-aligned toggle
left_col, right_col = st.columns([8, 1])
with center_col:
    toggle_value = st.toggle("Dark Mode", value=(st.session_state.theme == "dark"))

st.session_state.theme = "dark" if toggle_value else "light"
is_dark = st.session_state.theme == "dark"

# Theme-specific values
if is_dark:
    bg_gradient = "linear-gradient(135deg, #000000 0%, #444444 100%)"
    card_bg = "rgba(255, 255, 255, 0.12)"
    text_color = "#ffffff"
    input_bg = "rgba(255, 255, 255, 0.15)"
    input_border = "#cccccc"
    focus_border = "#ffffff"
    focus_shadow = "rgba(255, 255, 255, 0.35)"
else:
    bg_gradient = "linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%)"
    card_bg = "rgba(255, 255, 255, 0.85)"
    text_color = "#000000"
    input_bg = "rgba(255, 255, 255, 0.95)"
    input_border = "#999999"
    focus_border = "#000000"
    focus_shadow = "rgba(0, 0, 0, 0.25)"

# ------------------ CUSTOM STYLING ------------------ #
st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    font-family: 'Space Grotesk', sans-serif;
    background: {bg_gradient};
    background-size: cover;
    height: 100%;
    margin: 0;
    padding: 0;
    color: {text_color};

}}

/* Centered title */
.cat-title {{
    text-align: center;
    width: 100%;
    margin-bottom: 10px;
}}

/* General text color */
h1, p, label, .stMarkdown, span {{
    color: {text_color} !important;
}}

/* Text input */
.stTextInput > div > input {{
    background-color: {input_bg};
    color: {text_color};
    border-radius: 8px;
    border: 1px solid {input_border};
}}

.stTextInput > div > input:focus {{
    border: 1px solid {focus_border} !important;
    outline: none !important;
    box-shadow: 0 0 0 0.15rem {focus_shadow};
}}

/* Hide Streamlit's default menu (may change between versions) */
.e1nzilvr5 {{
    visibility: hidden;
}}
</style>
""",
    unsafe_allow_html=True
)

# ------------------ GLASSY WRAPPER ------------------ #
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Title (centered)
st.markdown(
    "<h1 class='cat-title' style='font-size:42px;'>CatGPT</h1>",
    unsafe_allow_html=True
)

# Centered cat gif
st.markdown(
    """
    <div style='display:flex; justify-content:center;'>
        <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjFpcGcxZndnb2xydmh3d3Q0MmJlNThnMjBleGFjOGN1ajJ2YWMxbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YJ85eVpdZDy7e/giphy.gif"
             width="200"
             style="margin-top:10px; margin-bottom:25px; border-radius:10px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Input field
user_input = st.text_input(
    "Well? What do you want from me?",
    placeholder="e.g., How are you?",
    label_visibility="visible"
)

# Output
if user_input:
    st.success("Meow.")

# Close glass card
st.markdown("</div>", unsafe_allow_html=True)
