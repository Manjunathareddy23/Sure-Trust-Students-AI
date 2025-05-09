import streamlit as st
from fpdf import FPDF
import fitz  # PyMuPDF for PDF reading
import os
from dotenv import load_dotenv
import google.generativeai as genai  # Import the Google Gemini library

# Load environment variables from .env file
load_dotenv()

# Configure the Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title='Manju PDF Summarizer', page_icon='📄', layout='centered')

# GitHub link to your background image
background_image_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/summary.jpg"

# Updated CSS styling with enhanced text stylings
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: #000;
            font-family: Arial, sans-serif;
        }}
        .container {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            width: 60%;
            margin: 50px auto;
            text-align: center;
            animation: fadeIn 1.5s;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        h1 {{
            color: #ffd700;  /* Golden color for the title */
            font-size: 3rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            font-weight: bold;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-decoration: underline;
        }}
        label {{
            color: #1e40af;  /* Stylish blue for labels */
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 10px;
            font-family: 'Verdana', sans-serif;
        }}
        .result-box {{
            background-color: #f1f5f9;
            padding: 15px;
            margin-top: 20px;
            border-radius: 8px;
            text-align: left;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
            max-height: 300px;
            color: #0f172a;
            font-weight: 500;
            font-family: 'Calibri', sans-serif;
        }}
        .error-msg {{
            color: red;
            font-weight: bold;
            margin-top: 10px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
        }}
        .highlight {{
            color: #ff5722;
            font-weight: bold;
            font-style: italic;
        }}
        .stButton>button {{
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s;
        }}
        .stButton>button:hover {{
            background-color: #45a049;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='container'><h1>📄 Manju PDF Summarizer</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("🔹 Upload a PDF file:", type=['pdf'])

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using PyMuPDF."""
    text = ''
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        st.error("❌ Error reading the PDF file. Please try again.")
        return None

def get_gemini_response(input_text, pdf_content, prompt):
    """Fetches a response from the Google Gemini model."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([input_text, pdf_content, prompt])
        return response.text
    except Exception as e:
        st.error("❌ Failed to fetch data from Gemini API. Please check your API key or connection.")
        return None

def download_pdf(content):
    """Generates and allows download of the summary PDF."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Summary and Key Points:\n")
    pdf.multi_cell(0, 10, content)
    pdf_file = "summary_report.pdf"
    pdf.output(pdf_file)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📥 Download Summary PDF",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )

if uploaded_file is not None:
    with st.spinner("🔄 Extracting text from the PDF..."):
        with open('uploaded_file.pdf', 'wb') as f:
            f.write(uploaded_file.read())
        pdf_text = extract_text_from_pdf('uploaded_file.pdf')
        os.remove('uploaded_file.pdf')  # Clean up the file after extraction

    if pdf_text:
        st.markdown(f"<div class='result-box'><strong class='highlight'>📑 Extracted Text Preview:</strong><br>{pdf_text[:500]}...</div>", unsafe_allow_html=True)

        if st.button("🔎 Get Summary and Key Points"):
            with st.spinner("🔄 Fetching summary from Gemini API..."):
                prompt = "Provide a summary and key points for the given content."
                result = get_gemini_response("Summarize this PDF:", pdf_text, prompt)

            if result:
                st.markdown(f"<div class='result-box'><strong class='highlight'>✅ Summary and Key Points:</strong><br>{result}</div>", unsafe_allow_html=True)
                download_pdf(result)

st.markdown("</div>", unsafe_allow_html=True)
