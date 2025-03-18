# app.py
import streamlit as st
import requests

# Check if the user is logged in
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning('You must log in first!')
    st.stop()  # Stop execution if not logged in

# --- Helper function for To-Do List ---
def todo_list():
    tasks = ['Finish homework', 'Study for exams', 'Go to gym']
    tasks_str = "\n".join(tasks)
    st.text_area("Your To-Do List", value=tasks_str, height=200)
    st.download_button("Download To-Do List", data=tasks_str, file_name="todo_list.txt", mime="text/plain")

# --- Helper function for AI Doubt Solver ---
def get_answer_from_gemini(question):
    gemini_api_url = 'https://gemini-api.example.com/v1/completion'  # Replace with the actual Gemini endpoint
    gemini_api_key = 'your_gemini_api_key'  # Replace with your actual Gemini API key

    headers = {
        'Authorization': f'Bearer {gemini_api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': 'gemini-model',  # Replace with the correct Gemini model name
        'prompt': question,
        'max_tokens': 100
    }

    try:
        response = requests.post(gemini_api_url, json=data, headers=headers)
        
        if response.status_code == 200:
            answer = response.json().get('choices')[0].get('text')  # Adjust based on API response format
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

def main_page():
    st.title("Main App Page")

    # Call the To-Do List and AI Bot functions
    todo_list()  # To-Do list
    ai_bot()  # AI Doubt Solver Bot

if __name__ == "__main__":
    main_page()  # Show main page after login
