import streamlit as st
import pandas as pd
import requests

# --- Helper functions for Excel-based login ---
def validate_login(username, password):
    try:
        # Load Excel file
        df = pd.read_excel('III Sem Section Wise Students.xlsx')  # Ensure the path to your file is correct
        
        # Check if 'Reg Number' column exists
        if 'Reg Number' not in df.columns:
            st.error("Missing 'Reg Number' column in the Excel sheet.")
            return False
        
        # Find user by Reg Number and validate if the username and password match
        user = df[df['Reg Number'] == username]
        
        # Validate if user exists and matches the password (Reg Number)
        if not user.empty and user['Reg Number'].iloc[0] == password:
            return True
        else:
            st.error('Invalid Username or Password')
            return False
    except Exception as e:
        st.error(f"An error occurred while validating login: {e}")
        return False

# --- Helper function for To-Do List ---
def todo_list():
    tasks = ['Finish homework', 'Study for exams', 'Go to gym']
    tasks_str = "\n".join(tasks)
    st.text_area("Your To-Do List", value=tasks_str, height=200)
    st.download_button("Download To-Do List", data=tasks_str, file_name="todo_list.txt", mime="text/plain")

# --- Helper function for AI Doubt Solver (Gemini AI) ---
def get_answer_from_gemini(question):
    gemini_api_url = 'https://gemini-api.example.com/v1/completion'  # Replace with the actual Gemini endpoint
    gemini_api_key = 'your_gemini_api_key'  # Replace with your actual Gemini API key

    headers = {
        'Authorization': f'Bearer {gemini_api_key}',
        'Content-Type': 'application/json'
    }

    # Request payload (adjust based on Gemini AI API docs)
    data = {
        'model': 'gemini-model',  # Replace with the correct Gemini model name
        'prompt': question,
        'max_tokens': 100
    }

    try:
        # Send POST request to Gemini API
        response = requests.post(gemini_api_url, json=data, headers=headers)
        
        if response.status_code == 200:
            # Handle response depending on Gemini's actual response structure
            answer = response.json().get('choices')[0].get('text')  # Ensure this matches Gemini's API response format
            return answer
        else:
            st.error("Error: Could not get a response from Gemini AI.")
            return None
    except Exception as e:
        st.error(f"Error during Gemini API request: {e}")
        return None

def ai_bot():
    question = st.text_input("Ask a question:")
    if st.button("Get Answer"):
        answer = get_answer_from_gemini(question)
        if answer:
            st.write(answer)

# --- Main Page --- 
def main_page():
    # Home page navigation bar with Tailwind CSS
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

    # --- Call the To-Do List and AI Bot functions ---
    todo_list()  # To-Do list
    ai_bot()  # AI Doubt Solver Bot

# --- Login Page --- 
def login_page():
    st.markdown("""
        <style>
            /* Tailwind CSS and Custom Styling */
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

            .login-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #F3F4F6;
            }

            .login-box {
                background-color: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 400px;
            }

            .login-title {
                font-size: 28px;
                font-weight: 600;
                margin-bottom: 20px;
                text-align: center;
                color: #1D4ED8;
            }

            .input-field {
                padding: 12px;
                font-size: 16px;
                border: 1px solid #E2E8F0;
                border-radius: 6px;
                transition: border-color 0.3s;
            }

            .input-field:focus {
                border-color: #1D4ED8;
                outline: none;
            }

            .error-message {
                color: red;
                font-size: 14px;
                margin-top: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    st.markdown('<div class="login-title">Login</div>', unsafe_allow_html=True)

    username = st.text_input('Username (Reg Number)', key='username', label_visibility="collapsed", placeholder="Enter your Reg Number", 
                             help="Please enter your Registration Number.", max_chars=10, key="username", 
                             label_visibility="collapsed", class_="input-field")
    password = st.text_input('Password (Reg Number)', type='password', key='password', placeholder="Enter your Reg Number", 
                             help="Please enter your Reg Number as password.", max_chars=10, 
                             label_visibility="collapsed", class_="input-field")

    if st.button('Login'):
        if validate_login(username, password):
            st.success('Login Successful')
            main_page()  # Redirect to main page after successful login
        else:
            st.markdown('<div class="error-message">Invalid Username or Password</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Main Program Flow ---
if __name__ == "__main__":
    # Check if the user is logged in (for this example, we'll just show the login page)
    login_page()
