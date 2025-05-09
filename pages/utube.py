import streamlit as st
from dotenv import load_dotenv
import os
import re
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable, TranscriptsDisabled

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Prompts
summary_prompt = """You are a YouTube video summarizer. You will take the transcript of the video 
and summarize the entire video, providing the important information in points within 
300 words. The summary will be in a professional format. Please provide the summary of the text given here: """

transcript_prompt = """You are a transcript generator. Given the title and description of a YouTube video, 
generate an accurate transcript of what is spoken in the video. Please generate the transcript for the following: """

# Local background image
background_image_url = "https://raw.githubusercontent.com/Manjunathareddy23/HACK-WITH-NELLORE-25/main/assests/utube.jpg"

# Background and custom styling
st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        font-family: 'Arial', sans-serif;
        color: white;
    }}
    .title {{
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 5px black;
        margin-bottom: 20px;
    }}
    .subtitle {{
        font-size: 20px;
        color: #87CEEB;
        text-align: center;
        margin-bottom: 30px;
    }}
    .result-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 15px;
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="title">📹 YouTube Video Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate professional summaries from YouTube videos</div>', unsafe_allow_html=True)

# Input YouTube link
youtube_link = st.text_input("Enter YouTube video link:")

# Helper: Extract Video ID
def extract_video_id(youtube_video_url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/\s]{11})'
    match = re.search(pattern, youtube_video_url)
    return match.group(1) if match else None

# Helper: Fetch transcript
def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([item["text"] for item in transcript_data])
        return transcript_text
    except (NoTranscriptFound, VideoUnavailable, TranscriptsDisabled):
        st.warning("⚠️ Transcript not available. Attempting to generate a transcript using Gemini API...")
        return None
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {e}")
        return None

# Helper: Generate content with Gemini
def generate_gemini_content(prompt_text, prompt):
    try:
        response = genai.generate(
            model="text-bison-001",
            prompt=prompt + prompt_text,
            max_output_tokens=300
        )
        return response.generations[0].text
    except Exception as e:
        st.error(f"❌ Failed to fetch data from Gemini API: {e}")
        return None

# Display thumbnail if valid
if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    else:
        st.error("⚠️ Invalid YouTube link. Please check and try again.")

# Main button
if st.button("Get Summary"):
    transcript_text = extract_transcript_details(youtube_link)

    if not transcript_text:
        transcript_text = generate_gemini_content(youtube_link, transcript_prompt)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, summary_prompt)
        if summary:
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown("## 📄 Detailed Summary:")
            st.write(summary)
            st.markdown('</div>', unsafe_allow_html=True)
