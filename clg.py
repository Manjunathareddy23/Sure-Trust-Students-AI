import streamlit as st
import pandas as pd
import openai
from io import StringIO

# --- Helper functions for CSV-based login ---
def validate_login(username, password):
    # Load CSV file with usernames and passwords
    df = pd.read_csv('users.csv')  # Assume 'users.csv' contains 'username' and 'password' columns
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

# --- Helper function for AI Doubt Solver ---
def get_answer_from_ai(question):
    openai.api_key = 'your_openai_api_key'  # Replace with your actual API key
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=question,
      max_tokens=100
    )
    return response.choices[0].text.strip()

def ai_bot():
    question = st.text_input("Ask a question:")
    if st.button("Get Answer"):
        answer = get_answer_from_ai(question)
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
