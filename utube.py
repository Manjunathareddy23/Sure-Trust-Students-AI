import streamlit as st
from dotenv import load_dotenv
import os
import re
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable, TranscriptsDisabled

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Prompts for Google Gemini
summary_prompt = """You are a YouTube video summarizer. You will take the transcript of the video 
and summarize the entire video, providing the important information in points within 
250 words. The summary will be in a professional format. Please provide the summary of the text given here: """

transcript_prompt = """You are a transcript generator. Given the title and description of a YouTube video, 
generate an accurate transcript of what is spoken in the video. Please generate the transcript for the following: """

st.title("📹 YouTube Video Summarizer")
youtube_link = st.text_input("Enter YouTube video link:")

def extract_video_id(youtube_video_url):
    """Extracts the video ID from a YouTube URL."""
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/)([^"&?/\s]{11})'
    match = re.search(pattern, youtube_video_url)
    return match.group(1) if match else None

def extract_transcript_details(youtube_video_url):
    """Attempts to fetch the transcript of a YouTube video."""
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

def generate_gemini_content(prompt_text, prompt):
    """Generates content using the Google Gemini API."""
    try:
        response = genai.generate(
            model="text-bison-001",
            prompt=prompt + prompt_text,
            max_output_tokens=300
        )
        return response.generations[0].text  # Adjusted to access the generated text correctly
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

    # If transcript is unavailable, attempt Gemini-based generation
    if not transcript_text:
        transcript_text = generate_gemini_content(youtube_link, transcript_prompt)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, summary_prompt)
        if summary:
            st.markdown("## 📄 Detailed Summary:")
            st.write(summary)
