import streamlit as st
import pandas as pd
import requests
from io import StringIO

# --- Helper functions for Excel-based login ---
def validate_login(username, password):
    # Load Excel file with usernames and passwords
    df = pd.read_excel('users.xlsx')  # Assume 'users.xlsx' contains 'username' and 'password' columns
    user = df[df['username'] == username]
    if not user.empty and user['password'].iloc[0] == password:
        return True
    return False

# --- Helper function for To-Do List ---
def todo_list():
    tasks = ['Finish homework', 'Study for exams', 'Go to gym']
    tasks_str = "\n".join(tasks)
    st.text_area("Your To-Do List", value=tasks_str, height=200)
    st.download_button("Download To-Do List", data=tasks_str, file_name="todo_list.txt", mime="text/plain")

# --- Helper function for AI Doubt Solver (Gemini AI) ---
def get_answer_from_gemini(question):
    gemini_api_url = 'https://gemini-api.example.com/v1/completion'  # Placeholder URL, update with actual Gemini endpoint
    gemini_api_key = 'your_gemini_api_key'  # Replace with your actual Gemini API key

    headers = {
        'Authorization': f'Bearer {gemini_api_key}',
        'Content-Type': 'application/json'
    }

    # Request payload (adjust based on Gemini AI API docs)
    data = {
        'model': 'gemini-model',  # Placeholder model name, replace with the correct Gemini model name
        'prompt': question,
        'max_tokens': 100
    }

    # Send POST request to Gemini API
    response = requests.post(gemini_api_url, json=data, headers=headers)

    if response.status_code == 200:
        answer = response.json()['choices'][0]['text']  # Adjust based on Gemini API response structure
        return answer
    else:
        st.error("Error: Could not get a response from Gemini AI.")
        return None

def ai_bot():
    question = st.text_input("Ask a question:")
    if st.button("Get Answer"):
        answer = get_answer_from_gemini(question)
        if answer:
            st.write(answer)

# --- Streamlit Page Layout and Styling ---
def main_page():
    # Embed Tailwind CSS
    st.markdown("""
        <style>
            .stButton>button {
                background-color: #1D4ED8;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 16px;
                transition: all 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #2563EB;
            }
        </style>
    """, unsafe_allow_html=True)

    # Home page navigation bar
    st.markdown("""
        <header class="bg-blue-500 p-4">
            <nav class="flex justify-between">
                <div class="text-white text-lg">College Web App</div>
                <div class="space-x-4">
                    <a href="#home" class="text-white">Home</a>
                    <a href="#services" class="text-white">Services</a>
                    <a href="#about" class="text-white">About Us</a>
                    <a href="#contact" class="text-white">Contact</a>
                    <a href="#location" class="text-white">Location</a>
                </div>
            </nav>
        </header>
    """, unsafe_allow_html=True)

    # --- Home Page Section ---
    st.title("Welcome to College Web App!")
    st.write("This platform provides several study tools for college students. Let's get started!")

    # --- Services Section ---
    st.subheader("Our Services")
    st.write("""
        - To-Do List (Download)
        - Important Questions Generator (Download)
        - PDF Summary (Download)
        - Translator (Download)
        - Q&A Evaluation
        - Doubt Solver AI Bot
        - Timetable Setter (Download)
        - Resources
        - Notepad (Save/Download)
        - Quiz and Games
    """)
    
    st.markdown("""
        <div class="container mx-auto p-8">
            <ul class="space-y-4 mt-4">
                <li><a href="#todo" class="text-blue-500">To-Do List (Download)</a></li>
                <li><a href="#questions" class="text-blue-500">Important Questions Generator (Download)</a></li>
                <li><a href="#pdf" class="text-blue-500">PDF Summary (Download)</a></li>
                <li><a href="#translator" class="text-blue-500">Translator (Download)</a></li>
                <li><a href="#qna" class="text-blue-500">Q&A Evaluation</a></li>
                <li><a href="#bot" class="text-blue-500">Doubt Solver AI Bot</a></li>
                <li><a href="#timetable" class="text-blue-500">Timetable Setter (Download)</a></li>
                <li><a href="#resources" class="text-blue-500">Resources</a></li>
                <li><a href="#notepad" class="text-blue-500">Notepad (Save/Download)</a></li>
                <li><a href="#quiz" class="text-blue-500">Quiz and Games</a></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # Call the To-Do list function
    todo_list()

    # Call the AI bot function
    ai_bot()

# --- Login Page ---
def login_page():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        if validate_login(username, password):
            st.success('Login Successful')
            main_page()  # Redirect to main page after login
        else:
            st.error('Invalid Username or Password')

# --- Main Program Flow ---
if __name__ == "__main__":
    # Check if the user is logged in (for this example, we'll just show the login page)
    login_page()
