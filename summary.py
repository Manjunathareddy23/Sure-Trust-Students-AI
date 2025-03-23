import streamlit as st
from fpdf import FPDF
import requests
import fitz  # PyMuPDF for PDF reading
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.set_page_config(page_title='Gemini PDF Summarizer', page_icon='📄', layout='centered')

# Tailwind CSS styling
st.markdown('''
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
        }
        .container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            width: 60%;
            margin: auto;
            margin-top: 50px;
            text-align: center;
        }
        h1 {
            color: #1e3a8a;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2rem;
            margin-bottom: 15px;
            color: #333;
        }
        .upload-btn {
            background-color: #3b82f6;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            margin-bottom: 20px;
            cursor: pointer;
            transition: 0.3s;
        }
        .upload-btn:hover {
            background-color: #1e40af;
        }
        .download-btn {
            background-color: #16a34a;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 20px;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        }
        .download-btn:hover {
            background-color: #065f46;
        }
        .result-box {
            background-color: #e2e8f0;
            padding: 15px;
            margin-top: 20px;
            border-radius: 8px;
            text-align: left;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
''', unsafe_allow_html=True)

st.markdown("<div class='container'><h1>📄 Gemini PDF Summarizer</h1>", unsafe_allow_html=True)

# Fetch the Gemini API key and version from environment variables
gemini_api_key = os.getenv('GEMINI_API_KEY')
gemini_version = 'flash'  # Specifying version as "flash"

uploaded_file = st.file_uploader("Upload a PDF file:", type=['pdf'])

def extract_text_from_pdf(pdf_path):
    text = ''
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def call_gemini_api(text):
    headers = {
        'Authorization': f'Bearer {gemini_api_key}',
        'Content-Type': 'application/json',
        'Gemini-Version': gemini_version  # Using version "flash"
    }
    payload = {
        'text': text,
        'features': ['summarization', 'key_points']
    }
    response = requests.post('https://api.gemini.com/summarize', headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch data from Gemini API. Please check your API key or version.')
        return None

if uploaded_file is not None:
    with open('uploaded_file.pdf', 'wb') as f:
        f.write(uploaded_file.read())

    pdf_text = extract_text_from_pdf('uploaded_file.pdf')
    st.markdown("<div class='result-box'><strong>Extracted Text:</strong><br>" + pdf_text[:200] + "...</div>", unsafe_allow_html=True)

    if st.button("Get Summary and Key Points"):
        result = call_gemini_api(pdf_text)

        if result:
            summary = result.get('summary', 'No summary available.')
            key_points = result.get('key_points', [])

            st.markdown("<div class='result-box'><strong>Summary:</strong><br>" + summary + "</div>", unsafe_allow_html=True)
            st.markdown("<div class='result-box'><strong>Key Points:</strong><ul>", unsafe_allow_html=True)
            for point in key_points:
                st.markdown(f"<li>{point}</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)

            # PDF Generation
            if st.button("Download as PDF"):
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, f"Summary:\n{summary}\n\nKey Points:")
                for idx, point in enumerate(key_points, 1):
                    pdf.multi_cell(0, 10, f"{idx}. {point}")
                pdf_file = "summary_output.pdf"
                pdf.output(pdf_file)
                st.download_button(
                    "📥 Download Summary PDF",
                    data=open(pdf_file, "rb"),
                    file_name=pdf_file,
                    mime="application/pdf"
                )

st.markdown("</div>", unsafe_allow_html=True)
