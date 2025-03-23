import streamlit as st
from dotenv import load_dotenv
import os
import re
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable, TranscriptsDisabled

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Prompt for Google Gemini
prompt = """You are a YouTube video summarizer. You will take the transcript of the video 
and summarize the entire video, providing the important information in points within 
250 words. The summary will be in a professional format. Please provide the summary of the text given here: """

st.title("📹 YouTube Video Summarizer")
youtube_link = st.text_input("Enter YouTube video link:")

def extract_video_id(youtube_video_url):
    """Extracts the video ID from a YouTube URL."""
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/\s]{11})'
    match = re.search(pattern, youtube_video_url)
    return match.group(1) if match else None

def extract_transcript_details(youtube_video_url):
    """Fetches the transcript of a YouTube video."""
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([item["text"] for item in transcript_data])
        return transcript_text
    except NoTranscriptFound:
        st.error("❌ No transcript available for this video.")
    except VideoUnavailable:
        st.error("❌ The video is unavailable. Please check the link.")
    except TranscriptsDisabled:
        st.error("❌ Transcripts are disabled for this video.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
    return None

def generate_gemini_content(transcript_text, prompt):
    """Generates a summary using the Google Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-1.5-turbo")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"❌ Failed to fetch data from Gemini API: {e}")
        return None

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    else:
        st.error("⚠️ Invalid YouTube link. Please check and try again.")

if st.button("Get Summary"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        if summary:
            st.markdown("## 📄 Detailed Summary:")
            st.write(summary)
