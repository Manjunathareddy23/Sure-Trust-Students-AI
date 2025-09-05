import streamlit as st

# Set page configuration
st.set_page_config(page_title="Manju's Productivity Suite", page_icon="🚀")

# Direct background image URL
background_image_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/entry.jpg"

# Inject custom CSS and background
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    html, body {{
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: 'Poppins', sans-serif;
        color: white;
        overflow-x: hidden;
    }}

    .background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url('{background_image_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        filter: brightness(0.4) blur(4px);
        z-index: -1;
    }}

    .title-box {{
        padding: 20px;
        border-radius: 20px;
        background: linear-gradient(145deg, #1e3c72cc, #2a5298cc);
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

    <div class="background"></div>
""", unsafe_allow_html=True)

# Title content
st.markdown("""
<div class="title-box">
    <h1>🚀 Welcome to Manju's Productivity Suite</h1>
</div>
""", unsafe_allow_html=True)
<link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
<script type="module">
	import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

	createChat({
		webhookUrl: 'https://manjunathareddy.app.n8n.cloud/webhook/f22fe423-dc75-452b-90ca-ea6ca6c2b2b9/chat'
	});
</script>
