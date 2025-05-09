import streamlit as st

st.set_page_config(page_title="Manju's Productivity Suite", page_icon="🚀")

# Inject custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }

    .title-box {
        padding: 20px;
        border-radius: 20px;
        background: linear-gradient(145deg, #1e3c72, #2a5298);
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        text-align: center;
        margin-bottom: 30px;
        transition: transform 0.5s ease, box-shadow 0.5s ease;
    }

    .title-box:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 30px rgba(0,0,0,0.6);
    }

    .markdown-text ul {
        list-style: none;
        padding-left: 0;
    }

    .markdown-text li {
        background: #ffffff10;
        border-radius: 12px;
        padding: 12px 20px;
        margin: 10px 0;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }

    .markdown-text li:hover {
        background: #ffffff20;
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    }

    .markdown-text a {
        color: white;
        text-decoration: none;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div class="title-box">
    <h1>🚀 Welcome to Manju's Productivity Suite</h1>
</div>
""", unsafe_allow_html=True)

# Feature List with Navigation Links
st.markdown("""
<div class="markdown-text">
    <ul>
        <li><a href=https://github.com/Manjunathareddy23/HACK-WITH-NELLORE-25/blob/main/pages/lang.py>📝 To-Do List Generator</a></li>
        <li><a href="/Student_Timetable_Planner">📅 Student Timetable Planner</a></li>
        <li><a href="/Language_Translator">🌍 Language Translator</a></li>
        <li><a href="/PDF_Summarizer">📄 PDF Summarizer</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)
