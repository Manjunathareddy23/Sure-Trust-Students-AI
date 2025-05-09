import streamlit as st

st.set_page_config(page_title="Manju's Productivity Suite", page_icon="🚀")
background_image_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/entry.jpg"

# Inject custom CSS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
        background-image: url('{background_image_url}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }}

    .title-box {{
        padding: 20px;
        border-radius: 20px;
        background: linear-gradient(145deg, #1e3c72cc, #2a5298cc);  /* semi-transparent overlay */
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 30px;
        transition: transform 0.5s ease, box-shadow 0.5s ease;
    }}

    .title-box:hover {{
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 30px rgba(0,0,0,0.6);
    }}

    .markdown-text ul {{
        list-style: none;
        padding-left: 0;
    }}

    .markdown-text li {{
        background: #ffffff10;
        border-radius: 12px;
        padding: 12px 20px;
        margin: 10px 0;
        transition: all 0.3s ease-in-out;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }}

    .markdown-text li:hover {{
        background: #ffffff20;
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }}
    </style>
""", unsafe_allow_html=True)

# Animated Title Box
st.markdown("""
<div class="title-box">
    <h1>🚀 Welcome to Manju's Productivity Suite</h1>
</div>
""", unsafe_allow_html=True)
