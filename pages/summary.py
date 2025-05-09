import streamlit as st
from fpdf import FPDF
import fitz  # PyMuPDF for PDF reading
import os
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini API

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set background image
background_image_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/assests/summary.jpg"
# Or use local file: background_image_url = "assets/lang.jpg"

st.set_page_config(page_title='Manju PDF Summarizer', page_icon='📄', layout='centered')

# Custom CSS for background and UI
st.markdown(f"""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
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
            color: #ffd700;
            font-size: 3rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            font-weight: bold;
            text-decoration: underline;
        }}
        label {{
            color: #1e40af;
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 10px;
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

# Title inside styled container
st.markdown("<div class='container'><h1>📄 Manju PDF Summarizer</h1>", unsafe_allow_html=True)

# PDF Upload
uploaded_file = st.file_uploader("🔹 Upload a PDF file:", type=['pdf'])

# Function to extract text
def extract_text_from_pdf(pdf_path):
    try:
        text = ''
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        st.error("❌ Error reading the PDF file. Please try again.")
        return None

# Gemini summarization function
def get_gemini_response(input_text, pdf_content, prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([input_text, pdf_content, prompt])
        return response.text
    except Exception as e:
        st.error("❌ Failed to fetch data from Gemini API. Check your API key or connection.")
        return None

# PDF generation for summary
def download_pdf(content):
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

# Processing PDF
if uploaded_file is not None:
    with st.spinner("🔄 Extracting text from the PDF..."):
        with open('uploaded_file.pdf', 'wb') as f:
            f.write(uploaded_file.read())
        pdf_text = extract_text_from_pdf('uploaded_file.pdf')
        os.remove('uploaded_file.pdf')  # Clean up

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
