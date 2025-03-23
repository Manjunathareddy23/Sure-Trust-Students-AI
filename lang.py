import streamlit as st
from googletrans import Translator, LANGUAGES  

# Apply custom CSS with a GitHub background image
st.markdown('''
    <style>
    /* Full-page background image */
    [data-testid="stAppViewContainer"] {
        background-image: url('https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/lang.jpg');
        background-size: cover;
        background-position: center;
    }

    /* Title Styling - Highlighting the main heading */
    h1 {
        background-color: #FFD700; /* Gold background */
        color: #FFFFFF; /* White text */
        text-align: center;
        font-size: 2.5rem;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    }

    /* Text area styling */
    textarea {
        background-color: #FFFFFF !important; /* White */
        color: black !important;
        font-size: 16px;
        font-weight: bold;
        border: 2px solid #32CD32; /* Lime Green */
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }

    /* Dropdown styling */
    [data-testid="stSelectbox"] {
        background-color: rgba(144, 238, 144, 0.8); /* Light Green with transparency */
        border-radius: 10px;
        border: 2px solid #32CD32;
        padding: 5px;
        margin-bottom: 15px;
    }

    /* Button styling */
    [data-testid="stButton"] button {
        background-color: #FF1493 !important; /* Dark Pink */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        margin-top: 10px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
        transition: 0.3s;
    }
    [data-testid="stButton"] button:hover {
        background-color: #D6006E !important;
    }

    /* Translated text styling */
    .translated-text {
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
        margin-top: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }

    /* Success message styling */
    .success-message {
        background-color: #FFC0CB; /* Pink */
        color: black;
        padding: 10px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: bold;
        margin-top: 30px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    </style>
''', unsafe_allow_html=True)

# Streamlit UI
st.title("🌍 Language Translation App 🇮🇳")

text_to_translate = st.text_area("Enter text to translate:", height=150)

languages = {"English": "en", "Hindi": "hi", "Telugu": "te", "Kannada": "kn", "Tamil": "ta",
              "Malayalam": "ml", "French": "fr", "German": "de", "Spanish": "es", "Italian": "it",
              "Portuguese": "pt", "Dutch": "nl"}

source_language = st.selectbox("Choose the source language:", list(languages.keys()))
target_language = st.selectbox("Choose the target language:", list(languages.keys()))

translator = Translator()

def translate_with_google(text, source_lang, target_lang):
    translated = translator.translate(text, src=languages[source_lang], dest=languages[target_language])
    return translated.text

if st.button("Translate 🔄"):
    if text_to_translate:
        translated_text = translate_with_google(text_to_translate, source_language, target_language)
        st.markdown(f'<div class="translated-text">Translated Text: {translated_text}</div>', unsafe_allow_html=True)

        # Download translated text as a .txt file
        st.download_button("Download Translated Text", translated_text, file_name="translated_text.txt", mime="text/plain")
    else:
        st.warning("⚠️ Please enter some text to translate.")

st.markdown('<div class="success-message">Developed by K.Manjunathareddy-6300138360</div>', unsafe_allow_html=True)
