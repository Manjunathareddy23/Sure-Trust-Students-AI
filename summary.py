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

# Replace this URL with the direct link to your GitHub background image
background_image_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/summary.jpg"

# CSS styling with background image
st.markdown(f'''
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            backdrop-filter: blur(3px);  /* Optional blur for readability */
        }}
        .container {{
            background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent background */
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
            width: 60%;
            margin: auto;
            margin-top: 50px;
            text-align: center;
        }}
        h1 {{
            color: #1e40af;
            font-size: 2.5rem;
            margin-bottom: 20px;
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
        }}
        .error-msg {{
            color: red;
            font-weight: bold;
            margin-top: 10px;
        }}
    </style>
''', unsafe_allow_html=True)

st.markdown("<div class='container'><h1>📄 Manju PDF Summarizer</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a PDF file:", type=['pdf'])

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
    with st.spinner("Extracting text from the PDF..."):
        with open('uploaded_file.pdf', 'wb') as f:
            f.write(uploaded_file.read())
        pdf_text = extract_text_from_pdf('uploaded_file.pdf')
        os.remove('uploaded_file.pdf')  # Clean up the file after extraction

    if pdf_text:
        st.markdown(f"<div class='result-box'><strong>Extracted Text Preview:</strong><br>{pdf_text[:500]}...</div>", unsafe_allow_html=True)

        if st.button("Get Summary and Key Points"):
            with st.spinner("Fetching summary from Gemini API..."):
                prompt = "Provide a summary and key points for the given content."
                result = get_gemini_response("Summarize this PDF:", pdf_text, prompt)

            if result:
                st.markdown(f"<div class='result-box'><strong>Summary and Key Points:</strong><br>{result}</div>", unsafe_allow_html=True)

                # Trigger the PDF download
                download_pdf(result)

st.markdown("</div>", unsafe_allow_html=True)
